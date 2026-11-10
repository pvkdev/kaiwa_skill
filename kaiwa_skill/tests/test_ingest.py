"""Isolated end-to-end ledger tests; review attestations here are synthetic fixtures."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from reportlab.pdfgen import canvas

SPEC = importlib.util.spec_from_file_location("ingest", Path(__file__).resolve().parents[1] / "tools" / "ingest.py")
ingest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ingest)


class IngestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "book").mkdir()
        self.source = self.root / "book" / "tiny.pdf"
        pdf = canvas.Canvas(str(self.source))
        for number in (1, 2):
            pdf.drawString(72, 720, f"Fixture page {number}")
            pdf.showPage()
        pdf.save()
        self.original_source = self.source.read_bytes()
        self.manifest = ingest.initialize(self.root, "book/tiny.pdf")
        self.book = self.manifest["id"]
        self.directory = ingest.book_dir(self.root, self.book)
        self.draft = self.root / "draft.md"
        self.draft.write_text("# Fixture\n\nJapanese: 日本語。\n", encoding="utf-8")

    def run_cli(self, *args, expect=0):
        output = io.StringIO()
        errors = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            code = ingest.main(["--root", str(self.root), *args])
        self.assertEqual(code, expect, errors.getvalue())
        return json.loads(output.getvalue()) if output.getvalue() else errors.getvalue()

    def draft_page(self, page=1):
        ingest.render_pages(self.directory, self.manifest, self.source, [page])
        ingest.record_page(self.directory, self.manifest, page, self.draft)

    def verify_fixture(self, page=1):
        evidence = ingest.evidence_template(self.directory, self.manifest, page)
        evidence.update(reviewer="unit-test synthetic reviewer", reviewed_at=ingest.now(), notes="Synthetic fixture only; no production visual review is asserted.")
        evidence["checks"] = dict.fromkeys(ingest.CHECKS, True)
        ingest.verify_page(self.directory, self.manifest, page, evidence)
        return evidence

    def test_inventory_stable_ids_and_read_only_sources(self):
        catalog = self.run_cli("inventory")
        self.assertEqual(catalog["books"][0]["id"], self.book)
        self.assertEqual(catalog["books"][0]["page_count"], 2)
        self.assertEqual(catalog["books"][0]["source"], "book/tiny.pdf")
        self.draft_page()
        self.assertEqual(self.source.read_bytes(), self.original_source)

    def test_end_to_end_build_excludes_drafts_and_labels_incomplete(self):
        self.draft_page(1)
        self.draft_page(2)
        self.verify_fixture(1)
        result = self.run_cli("build", self.book)
        self.assertFalse(result["complete"])
        self.assertEqual(result["verified_pages"], [1])
        body = (self.directory / "book.md").read_text(encoding="utf-8")
        self.assertIn("INCOMPLETE", body)
        self.assertNotIn("## PDF page 2", body)
        index = [json.loads(line) for line in (self.directory / "search.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual([row["page"] for row in index], [1])
        self.assertTrue(self.run_cli("status", self.book)["build_current"])
        self.verify_fixture(2)
        self.assertFalse(self.run_cli("status", self.book)["build_current"])
        self.assertTrue(self.run_cli("build", self.book)["complete"])

    def test_claim_enforces_owner_and_explicit_recovery(self):
        self.run_cli("claim", self.book, "--owner", "worker-A", "--token", "owner-token")
        self.run_cli("render", self.book, "--pages", "1", expect=2)
        self.run_cli("render", self.book, "--pages", "1", "--token", "wrong", expect=2)
        self.run_cli("claim", self.book, "--owner", "worker-B", expect=2)
        self.run_cli("render", self.book, "--pages", "1", "--token", "owner-token")
        self.run_cli("release", self.book, "--token", "wrong", expect=2)
        self.run_cli("recover", self.book, "--kind", "claim", "--expected-token", "wrong", "--reason", "test", expect=2)
        self.run_cli("release", self.book, "--token", "owner-token")
        self.assertFalse((self.directory / "claim.json").exists())

    def test_write_lock_blocks_and_requires_matching_recovery(self):
        ingest.exclusive_json(self.directory / ".write.lock", {"token": "crashed", "pid": -1})
        self.run_cli("render", self.book, "--pages", "1", expect=2)
        self.run_cli("recover", self.book, "--kind", "write", "--expected-token", "wrong", "--reason", "crash", expect=2)
        self.run_cli("recover", self.book, "--kind", "write", "--expected-token", "crashed", "--reason", "Confirmed synthetic writer stopped", "--confirm-writer-stopped")
        self.run_cli("render", self.book, "--pages", "1")
        self.assertEqual(len(list((self.directory / "recovery").glob("*.json"))), 1)

    def test_source_change_fails_before_mutation(self):
        before = (self.directory / "manifest.json").read_bytes()
        self.source.write_bytes(self.original_source + b"\nchanged")
        error = self.run_cli("render", self.book, "--pages", "1", expect=2)
        self.assertIn("Source PDF changed", error)
        self.assertEqual((self.directory / "manifest.json").read_bytes(), before)

    def test_render_never_verifies_and_rerender_invalidates(self):
        self.draft_page()
        self.verify_fixture()
        ingest.render_pages(self.directory, self.manifest, self.source, [1], scale=1)
        state, errors = ingest.page_integrity(self.directory, self.manifest, 1)
        self.assertFalse(errors)
        self.assertEqual(state["status"], "draft")
        self.assertNotIn("evidence", state)

    def test_review_requires_true_checks_and_matching_hashes(self):
        self.draft_page()
        evidence = ingest.evidence_template(self.directory, self.manifest, 1)
        with self.assertRaises(ingest.IngestError):
            ingest.verify_page(self.directory, self.manifest, 1, evidence)
        evidence = self.verify_fixture()
        evidence["markdown_sha256"] = "wrong"
        with self.assertRaises(ingest.IngestError):
            ingest.verify_page(self.directory, self.manifest, 1, evidence)

    def test_external_markdown_corruption_excluded_and_repairable(self):
        self.draft_page()
        self.verify_fixture()
        ingest.page_paths(self.directory, 1)[1].write_text("unreviewed change", encoding="utf-8")
        result = self.run_cli("build", self.book)
        self.assertEqual(result["verified_pages"], [])
        state = ingest.read_json(ingest.page_paths(self.directory, 1)[0])
        self.assertEqual(state["status"], "invalid")
        self.assertNotIn("evidence", state)
        self.run_cli("render", self.book, "--pages", "1")
        self.assertEqual(ingest.read_json(ingest.page_paths(self.directory, 1)[0])["status"], "draft")

    def test_corrupt_page_checkpoint_never_enters_build(self):
        self.draft_page()
        state_path = ingest.page_paths(self.directory, 1)[0]
        for broken in ("{truncated", "[]"):
            state_path.write_text(broken, encoding="utf-8")
            result = self.run_cli("build", self.book)
            self.assertEqual(result["verified_pages"], [])
            self.assertEqual(ingest.read_json(self.directory / "manifest.json")["counts"]["invalid"], 1)

    def test_crash_after_page_commit_reconcile_restores_manifest(self):
        self.draft_page()
        evidence = self.verify_fixture()
        state_path = ingest.page_paths(self.directory, 1)[0]
        state = ingest.read_json(state_path)
        state["status"] = "draft"
        state.pop("evidence")
        ingest.atomic_json(state_path, state)
        with patch.object(ingest, "checkpoint", side_effect=RuntimeError("simulated process failure")):
            with self.assertRaises(RuntimeError):
                ingest.verify_page(self.directory, self.manifest, 1, evidence)
        result = self.run_cli("reconcile", self.book)
        self.assertEqual(result["counts"]["verified"], 1)

    def test_failed_atomic_replace_preserves_old_data(self):
        target = self.root / "checkpoint.json"
        ingest.atomic_json(target, {"generation": 1})
        with patch.object(ingest.os, "replace", side_effect=OSError("simulated crash")):
            with self.assertRaises(OSError):
                ingest.atomic_json(target, {"generation": 2})
        self.assertEqual(ingest.read_json(target), {"generation": 1})
        self.assertFalse(list(self.root.glob("*.tmp-*")))

    def test_interrupted_build_detected_by_commit_marker(self):
        self.draft_page()
        self.verify_fixture()
        self.run_cli("build", self.book)
        (self.directory / "book.md").write_text("interrupted replacement", encoding="utf-8")
        self.assertFalse(self.run_cli("status", self.book)["build_current"])
        self.run_cli("build", self.book)
        self.assertTrue(self.run_cli("status", self.book)["build_current"])

    def test_build_detects_new_review_of_same_page(self):
        self.draft_page()
        self.verify_fixture()
        self.run_cli("build", self.book)
        self.draft.write_text("corrected transcription", encoding="utf-8")
        ingest.record_page(self.directory, self.manifest, 1, self.draft)
        self.verify_fixture()
        self.assertFalse(self.run_cli("status", self.book)["build_current"])

    def test_paths_and_ranges_reject_escape(self):
        for name in ("../outside", "..", "a/b", "a\\b"):
            with self.assertRaises(ingest.IngestError):
                ingest.book_dir(self.root, name)
        with self.assertRaises(ingest.IngestError):
            ingest.safe_child(self.root, "../outside.pdf")
        for value in ("0", "3", "2-1", "1,,2"):
            with self.assertRaises(ingest.IngestError):
                ingest.parse_pages(value, 2)

    def test_torn_lock_recovery_requires_digest_and_stopped_confirmation(self):
        lock = self.directory / ".write.lock"
        lock.write_bytes(b'{"token":')
        digest = ingest.sha(lock)
        self.run_cli("recover", self.book, "--kind", "write", "--expected-sha256", digest, "--reason", "torn lock", expect=2)
        self.run_cli("recover", self.book, "--kind", "write", "--expected-sha256", "wrong", "--reason", "torn lock", "--confirm-writer-stopped", expect=2)
        self.run_cli("recover", self.book, "--kind", "write", "--expected-sha256", digest, "--reason", "torn lock", "--confirm-writer-stopped")
        log = ingest.read_json(next((self.directory / "recovery").glob("*.json")))
        self.assertEqual(bytes.fromhex(log["previous"]["raw_hex"]), b'{"token":')

    def test_needs_review_is_excluded_until_new_draft_and_review(self):
        self.draft_page()
        self.verify_fixture()
        self.run_cli("needs_review", self.book, "--page", "1", "--issue", "Unreadable ruby annotation")
        result = self.run_cli("status", self.book)
        self.assertEqual(result["counts"]["needs_review"], 1)
        self.assertEqual(result["issue_count"], 1)
        self.assertEqual(self.run_cli("build", self.book)["verified_pages"], [])

    def test_status_all_counts_uninitialized_books_and_errors(self):
        (self.root / "vocab").mkdir()
        (self.root / "vocab" / "second.pdf").write_bytes(self.original_source + b"\nsecond")
        self.run_cli("inventory")
        self.draft_page()
        result = self.run_cli("status-all")
        self.assertEqual(result["total_pages"], 4)
        self.assertEqual(result["counts"], {"draft": 1, "pending": 3})
        (self.directory / "manifest.json").write_text("[]", encoding="utf-8")
        result = self.run_cli("status-all")
        self.assertTrue(any("error" in row for row in result["books"]))

    def test_assets_validate_and_rebase_and_blocks_index(self):
        self.draft_page()
        self.draft.write_text("![crop](../assets/missing.png)", encoding="utf-8")
        with self.assertRaises(ingest.IngestError):
            ingest.record_page(self.directory, self.manifest, 1, self.draft)
        assets = self.directory / "assets"
        assets.mkdir()
        (assets / "crop.png").write_bytes(b"fixture")
        self.draft.write_text('<a id="p0001-b001"></a>\nFirst\n![crop](../assets/crop.png)\n<a id="p0001-b002"></a>\nSecond', encoding="utf-8")
        ingest.record_page(self.directory, self.manifest, 1, self.draft)
        self.verify_fixture()
        self.run_cli("build", self.book)
        self.assertIn("pages/../assets/crop.png", (self.directory / "book.md").read_text(encoding="utf-8"))
        rows = [json.loads(line) for line in (self.directory / "search.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual([row["block_id"] for row in rows], ["p0001-b001", "p0001-b002"])
        (assets / "crop.png").unlink()
        self.assertEqual(self.run_cli("build", self.book)["verified_pages"], [])


if __name__ == "__main__":
    unittest.main()
