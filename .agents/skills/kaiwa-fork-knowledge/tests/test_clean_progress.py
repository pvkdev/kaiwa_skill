"""Behavioral tests for the resumable clean-progress utility; no real corpus writes."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "clean_progress.py"
CHAPTERS = ["chapters/01-ne.md", "chapters/02-yo.md"]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def put_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class CleanProgressTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="clean-progress-test-")
        self.addCleanup(self.temporary.cleanup)
        self.repo = Path(self.temporary.name)
        self.corpus = self.repo / "kaiwa_skill" / "corpus" / "sample-corpus"
        self.pages = self.corpus / "pages"
        self.pages.mkdir(parents=True)
        self.pdf = self.repo / "kaiwa_skill" / "book" / "sample.pdf"
        self.pdf.parent.mkdir(parents=True)
        self.pdf.write_bytes(b"%PDF-1.4\nfixture\n")
        self.raw_book = self.corpus / "book.md"
        self.raw_book.write_text("# Raw book\n<a id=\"p0001\"></a>\n<a id=\"p0002\"></a>\n", encoding="utf-8")
        self.search = self.corpus / "search.jsonl"
        self.search.write_text("{}\n", encoding="utf-8")
        self.page_files = {}
        for page in (1, 2):
            markdown = self.pages / f"p{page:04d}.md"
            markdown.write_text(f'<a id="p{page:04d}"></a>\n<a id="p{page:04d}-b001"></a>\n日本語 {page}\n', encoding="utf-8")
            self.page_files[page] = markdown
        self.make_ingest(complete=True)
        self.book = self.repo / "kaiwa_skill" / "knowledge" / "Sample Book"
        (self.book / "chapters").mkdir(parents=True)
        (self.book / "_meta").mkdir()
        for index, chapter in enumerate(CHAPTERS, 1):
            (self.book / chapter).write_text(
                f'<a id="u-{index}"></a>\n# Chapter {index}\n**JP:** 日本語。\n\n**VI:** Tiếng Việt.\n',
                encoding="utf-8",
            )
        rows = []
        for index, chapter in enumerate(CHAPTERS, 1):
            rows.append({
                "unit_id": f"u-{index}", "chapter": chapter, "heading": f"Chapter {index}",
                "source": [{"pdf_page": index,
                            "raw_page": f"kaiwa_skill/corpus/sample-corpus/pages/p{index:04d}.md",
                            "raw_anchors": [f"p{index:04d}-b001"]}],
                "review_status": "draft", "issues": [],
            })
        self.units_path = self.book / "_meta" / "units.jsonl"
        self.write_units(rows)
        put_json(self.book / "_meta" / "book.json", {
            "schema_version": 1, "title": "Sample Book", "status": "pilot_partial",
            "source_pdf": {"path": "kaiwa_skill/book/sample.pdf", "sha256": digest(self.pdf)},
            "source_markdown": {"path": "kaiwa_skill/corpus/sample-corpus/book.md",
                                "sha256": digest(self.raw_book)},
            "scope": {"pdf_pages": [1, 2], "chapters": CHAPTERS},
        })

    def write_units(self, rows: list[dict]) -> None:
        self.units_path.write_text(
            "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8"
        )

    def make_ingest(self, complete: bool) -> None:
        source_hash = digest(self.pdf)
        page_hashes = {str(i): digest(self.page_files[i]) for i in (1, 2)}
        states = {"1": "verified", "2": "verified" if complete else "needs_review"}
        put_json(self.corpus / "manifest.json", {
            "schema_version": 1, "id": "sample-corpus", "source": "book/sample.pdf",
            "source_sha256": source_hash, "page_count": 2,
            "counts": {"verified": 2 if complete else 1}, "pages": states,
        })
        for page in (1, 2):
            verified = complete or page == 1
            put_json(self.pages / f"p{page:04d}.json", {
                "page": page, "status": "verified" if verified else "needs_review",
                "source_sha256": source_hash, "markdown_sha256": page_hashes[str(page)],
                "render_sha256": "a" * 64, "asset_sha256": {},
                "evidence": {
                    "source_sha256": source_hash,
                    "markdown_sha256": page_hashes[str(page)],
                    "render_sha256": "a" * 64,
                    "asset_sha256": {},
                    "checks": {key: verified for key in (
                        "visual_review", "text_complete", "reading_order", "japanese_accuracy")},
                },
            })
        put_json(self.corpus / "build.json", {
            "source_sha256": source_hash, "complete": complete,
            "transcription_complete": complete,
            "verified_pages": [1, 2] if complete else [1],
            "page_hashes": page_hashes,
            "book_sha256": digest(self.raw_book), "search_sha256": digest(self.search),
        })

    def run_cli(self, command: str, *args: str, success: bool = True) -> dict | str:
        argv = [sys.executable, "-B", str(SCRIPT), command]
        if command != "scan":
            argv.append(str(self.book))
        argv += ["--repo-root", str(self.repo), *args]
        process = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8")
        if success:
            self.assertEqual(process.returncode, 0, process.stderr)
            return json.loads(process.stdout)
        self.assertNotEqual(process.returncode, 0, process.stdout)
        return process.stderr

    def init(self) -> tuple[dict, dict]:
        summary = self.run_cli("init")
        state = json.loads((self.book / "_meta" / "clean-state.json").read_text(encoding="utf-8"))
        return summary, state

    def checkpoint(self, chapter: str, status: str = "draft") -> dict:
        return self.run_cli("checkpoint", "--chapter", chapter, "--status", status,
                            "--note", "Đã đối chiếu ảnh nguồn trang 1" if status == "author_checked" else "draft")

    def test_scan_readiness_requires_full_fresh_verified_ingest(self) -> None:
        self.make_ingest(complete=False)
        scan = self.run_cli("scan")
        self.assertEqual(scan["books"][0]["status"], "waiting")
        self.make_ingest(complete=True)
        scan = self.run_cli("scan")
        self.assertEqual(scan["books"][0]["status"], "ready_for_fork")
        self.page_files[2].write_text("changed after build\n", encoding="utf-8")
        scan = self.run_cli("scan")
        self.assertNotEqual(scan["books"][0]["status"], "ready_for_fork")
        self.assertTrue(any("Page 2" in reason for reason in scan["books"][0]["reasons"]))
        self.make_ingest(complete=True)
        (self.corpus / "claim.json").write_text("{}\n", encoding="utf-8")
        scan = self.run_cli("scan")
        self.assertEqual(scan["books"][0]["status"], "waiting")
        self.assertTrue(any("claim" in reason.lower() for reason in scan["books"][0]["reasons"]))

    def test_init_snapshots_sources_and_reinit_preserves_them(self) -> None:
        summary, state = self.init()
        self.assertEqual(summary["status"], "initialized")
        snapshot_root = self.repo / state["snapshot"]["root"]
        self.assertTrue(snapshot_root.is_dir())
        self.assertFalse(snapshot_root.is_relative_to(self.book))
        self.assertGreaterEqual(len(state["snapshot"]["files"]), 3)
        for relative, expected in state["snapshot"]["files"].items():
            self.assertEqual(digest(snapshot_root / relative), expected)
        state_before = (self.book / "_meta" / "clean-state.json").read_bytes()
        snapshot_before = {rel: digest(snapshot_root / rel)
                           for rel in state["snapshot"]["files"]}
        self.assertIn("already exists", self.run_cli("init", success=False))
        self.assertEqual((self.book / "_meta" / "clean-state.json").read_bytes(), state_before)
        self.assertEqual({rel: digest(snapshot_root / rel)
                          for rel in state["snapshot"]["files"]}, snapshot_before)

    def test_resume_keeps_checkpoints_across_processes_and_localizes_edits(self) -> None:
        self.init()
        self.checkpoint(CHAPTERS[0], "author_checked")
        resumed = self.run_cli("resume")  # separate Python process from checkpoint
        self.assertEqual(resumed["completed"], [CHAPTERS[0]])
        self.assertEqual(resumed["pending"], [CHAPTERS[1]])
        self.assertEqual(resumed["next"], CHAPTERS[1])
        scanned = self.run_cli("scan")["books"][0]
        self.assertEqual(scanned["clean_progress"]["completed"], [CHAPTERS[0]])
        self.assertEqual(scanned["clean_progress"]["pending"], [CHAPTERS[1]])
        self.checkpoint(CHAPTERS[1])
        first = self.book / CHAPTERS[0]
        original = first.read_text(encoding="utf-8")
        first.write_text(original + "\nSửa bản nháp\n", encoding="utf-8")
        resumed = self.run_cli("resume")
        self.assertEqual([item["chapter"] for item in resumed["stale"]], [CHAPTERS[0]])
        self.assertEqual(resumed["draft"], [CHAPTERS[1]])
        first.write_text(original, encoding="utf-8")
        rows = [json.loads(line) for line in self.units_path.read_text(encoding="utf-8").splitlines()]
        rows[0]["heading"] = "Changed unit metadata"
        self.write_units(rows)
        resumed = self.run_cli("resume")
        self.assertEqual([item["chapter"] for item in resumed["stale"]], [CHAPTERS[0]])
        self.assertEqual(resumed["draft"], [CHAPTERS[1]])

    def test_live_raw_change_requests_rebase_without_rewriting_snapshot(self) -> None:
        _, state = self.init()
        self.checkpoint(CHAPTERS[0], "author_checked")
        snapshot_root = self.repo / state["snapshot"]["root"]
        relative = "kaiwa_skill/corpus/sample-corpus/pages/p0001.md"
        snap_digest = digest(snapshot_root / relative)
        self.page_files[1].write_text("Changed raw source\n", encoding="utf-8")
        resumed = self.run_cli("resume")
        self.assertIn(relative, resumed["needs_rebase"])
        self.assertIn(CHAPTERS[0], resumed["completed"])
        self.assertEqual(digest(snapshot_root / relative), snap_digest)

    def test_pdf_change_blocks_checkpoint_and_stales_prior_work(self) -> None:
        self.init()
        self.checkpoint(CHAPTERS[0], "author_checked")
        self.pdf.write_bytes(b"changed PDF bytes")
        resumed = self.run_cli("resume")
        self.assertEqual([item["chapter"] for item in resumed["stale"]], [CHAPTERS[0]])
        self.assertIn("source PDF changed", resumed["needs_rebase"])
        self.assertIn("changed", self.run_cli(
            "checkpoint", "--chapter", CHAPTERS[0], "--status", "author_checked",
            "--note", "Đã đối chiếu ảnh", success=False).lower())

    def test_snapshot_change_blocks_checkpoint_and_stales_prior_work(self) -> None:
        _, state = self.init()
        self.checkpoint(CHAPTERS[0], "author_checked")
        snapshot_root = self.repo / state["snapshot"]["root"]
        (snapshot_root / "kaiwa_skill/corpus/sample-corpus/pages/p0001.md").write_text(
            "tampered snapshot\n", encoding="utf-8")
        resumed = self.run_cli("resume")
        self.assertEqual([item["chapter"] for item in resumed["stale"]], [CHAPTERS[0]])
        self.assertTrue(resumed["snapshot_errors"])
        self.assertIn("snapshot", self.run_cli(
            "checkpoint", "--chapter", CHAPTERS[0], "--status", "author_checked",
            "--note", "Đã đối chiếu ảnh", success=False).lower())

    def test_snapshot_book_tamper_is_detected_before_any_checkpoint(self) -> None:
        _, state = self.init()
        snapshot_root = self.repo / state["snapshot"]["root"]
        (snapshot_root / "kaiwa_skill/corpus/sample-corpus/book.md").write_text(
            "tampered raw book\n", encoding="utf-8")
        resumed = self.run_cli("resume")
        self.assertTrue(resumed["snapshot_errors"])
        self.assertEqual(resumed["pending"], CHAPTERS)
        self.assertIn("snapshot", self.run_cli(
            "checkpoint", "--chapter", CHAPTERS[0], "--status", "draft",
            success=False).lower())

    def test_snapshot_raw_page_reference_is_normalized(self) -> None:
        _, state = self.init()
        rows = [json.loads(line) for line in self.units_path.read_text(encoding="utf-8").splitlines()]
        rows[0]["source"][0]["raw_page"] = (
            state["snapshot"]["root"] + "/kaiwa_skill/corpus/sample-corpus/pages/p0001.md")
        self.write_units(rows)
        self.checkpoint(CHAPTERS[0], "author_checked")
        resumed = self.run_cli("resume")
        self.assertEqual(resumed["completed"], [CHAPTERS[0]])
        self.assertFalse(resumed["stale"])

    def test_scope_change_blocks_resume_and_checkpoint(self) -> None:
        self.init()
        self.checkpoint(CHAPTERS[0], "author_checked")
        meta_path = self.book / "_meta" / "book.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        meta["scope"]["chapters"].append("chapters/03-new.md")
        (self.book / "chapters" / "03-new.md").write_text("# New chapter\n", encoding="utf-8")
        put_json(meta_path, meta)
        resumed = self.run_cli("resume")
        self.assertTrue(resumed["blocked"])
        self.assertTrue(resumed["scope_changed"])
        self.assertEqual(resumed["declared_scope"]["chapters"], CHAPTERS + ["chapters/03-new.md"])
        self.assertEqual(resumed["completed"], [])
        self.assertIn("scope differs", self.run_cli(
            "checkpoint", "--chapter", CHAPTERS[0], "--status", "draft",
            success=False).lower())

    def test_orphan_snapshot_after_ledger_write_failure_can_be_reused(self) -> None:
        spec = importlib.util.spec_from_file_location("clean_progress_under_test", SCRIPT)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with mock.patch.object(module, "atomic_json", side_effect=OSError("injected ledger write failure")):
            with self.assertRaises(OSError):
                module.init(self.repo, self.book)
        self.assertFalse((self.book / "_meta" / "clean-state.json").exists())
        snapshots = list((self.repo / "kaiwa_skill" / "source_snapshots").glob("sample-corpus/*/*"))
        self.assertEqual(len(snapshots), 1)
        summary, state = self.init()
        self.assertEqual(summary["status"], "initialized")
        self.assertEqual(self.repo / state["snapshot"]["root"], snapshots[0])

    def test_source_change_during_snapshot_leaves_no_final_state(self) -> None:
        spec = importlib.util.spec_from_file_location("clean_progress_under_test", SCRIPT)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = module.book_info
        calls = 0

        def changing_source(repo: Path, book: Path):
            nonlocal calls
            calls += 1
            if calls == 2:
                self.raw_book.write_text(self.raw_book.read_text(encoding="utf-8") + "changed\n",
                                         encoding="utf-8")
            return original(repo, book)

        with mock.patch.object(module, "book_info", side_effect=changing_source):
            with self.assertRaises((ValueError, OSError)):
                module.init(self.repo, self.book)
        self.assertGreaterEqual(calls, 2)
        self.assertFalse((self.book / "_meta" / "clean-state.json").exists())


if __name__ == "__main__":
    unittest.main()
