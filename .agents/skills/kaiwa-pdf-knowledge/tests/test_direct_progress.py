"""PDF-native provenance, resume, and audio checks with a synthetic book."""
from __future__ import annotations

import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock
from contextlib import redirect_stdout


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/direct_progress.py"
spec = importlib.util.spec_from_file_location("direct_progress", SCRIPT)
direct = importlib.util.module_from_spec(spec)
spec.loader.exec_module(direct)


class DirectProgressTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="direct-progress-")
        self.addCleanup(temporary.cleanup)
        self.repo = Path(temporary.name)
        self.pdf = self.repo / "kaiwa_skill/book/sample.pdf"
        self.pdf.parent.mkdir(parents=True)
        self.pdf.write_bytes(b"%PDF-1.4 fixture")
        self.book = self.repo / "kaiwa_skill/knowledge/Sample"
        self.count = mock.patch.object(direct, "pdf_page_count", return_value=3)
        self.count.start()
        self.addCleanup(self.count.stop)
        self.chapters = ["chapters/01.md", "chapters/02.md"]
        direct.init(self.repo, self.book, "kaiwa_skill/book/sample.pdf", "Sample", [1, 2],
                    self.chapters, "pilot_partial")
        for page, chapter in enumerate(self.chapters, 1):
            uid = f"u-{page}"
            (self.book / chapter).write_text(
                f'<a id="{uid}"></a>\n# Bài {page}\n**JP:** 日本語。\n\n**VI:** Tiếng Việt.\n',
                encoding="utf-8")
        self.rows = [{"unit_id": f"u-{p}", "chapter": self.chapters[p-1],
                      "heading": f"Bài {p}", "review_status": "author_checked", "issues": [],
                      "source": [{"pdf_page": p, "pdf_blocks": [f"p{p:04d}-b001"]}]}
                     for p in (1, 2)]
        self.write_units()
        for p in (1, 2):
            self.write_page(p, "included", f"u-{p}")
        audio_path = self.book / "_meta/audio.json"
        audio = direct.read(audio_path)
        audio["checked_pdf_pages"] = [1, 2]
        audio["book_identity"]["evidence_pages"] = [1]
        direct.write(audio_path, audio)

    def write_units(self):
        (self.book / "_meta/units.jsonl").write_text(
            "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in self.rows),
            encoding="utf-8")

    def write_page(self, p, disposition, uid=None):
        block = {"id": f"p{p:04d}-b001", "label": "Nội dung trang",
                 "disposition": disposition}
        if uid:
            block["unit_ids"] = [uid]
        direct.write(direct.page_path(self.book, p), {
            "schema_version": 1, "pdf_page": p, "source_pdf_sha256": direct.sha(self.pdf),
            "render_sha256": "a" * 64, "review_status": "author_checked",
            "review_note": "Đã mở ảnh và đối chiếu từng dòng.",
            "checks": {x: True for x in direct.CHECKS}, "blocks": [block]})

    def check_all(self):
        for p in (1, 2):
            direct.checkpoint(self.repo, self.book, p, None, "author_checked", "Đã xem ảnh.")
        for chapter in self.chapters:
            direct.checkpoint(self.repo, self.book, None, chapter, "author_checked",
                              "Đã đối chiếu ảnh, nội dung và dịch.")

    def mark_source_issue(self):
        evidence = direct.read(direct.page_path(self.book, 1))
        evidence["review_status"] = "needs_review"
        evidence["review_note"] = "Đã mở ảnh p1; chữ in bị ghi tay che, không đoán chữ còn thiếu."
        evidence["checks"]["text_complete"] = False
        evidence["checks"]["japanese_accuracy"] = False
        evidence["issues"] = [{"pdf_block": "p0001-b001",
                                "description": "Chữ in trong ví dụ bị ghi tay che; chưa đọc được."}]
        direct.write(direct.page_path(self.book, 1), evidence)
        self.rows[0]["review_status"] = "needs_review"
        self.rows[0]["issues"] = [{"pdf_page": 1, "pdf_block": "p0001-b001",
                                    "description": "Câu Nhật bị che, giữ dấu thiếu thay vì đoán."}]
        self.write_units()

    def check_issue_book(self):
        self.mark_source_issue()
        direct.checkpoint(self.repo, self.book, 1, None, "needs_review",
                          "Đã mở ảnh; vùng bị che cần kiểm từ bản nguồn khác.")
        direct.checkpoint(self.repo, self.book, 2, None, "author_checked", "Đã xem ảnh.")
        direct.checkpoint(self.repo, self.book, None, self.chapters[0], "needs_review",
                          "Đã kiểm chương; còn chữ in bị che ở p1.")
        direct.checkpoint(self.repo, self.book, None, self.chapters[1], "author_checked",
                          "Đã kiểm đủ p2.")

    def test_build_validate_without_raw_and_resume(self):
        self.check_all()
        direct.build(self.repo, self.book)
        self.assertEqual(direct.validate(self.repo, self.book), 0)
        meta = direct.read(self.book / "_meta/book.json")
        self.assertNotIn("source_markdown", meta)
        self.assertEqual(meta["build"]["unit_count"], 2)
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["chapters"]["completed"], self.chapters)

    def test_pdf_and_content_change_stale(self):
        self.check_all()
        (self.book / self.chapters[0]).write_text("<a id=\"u-1\"></a>\n# Sửa nội dung\n",
                                                  encoding="utf-8")
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["chapters"]["stale"], [self.chapters[0]])
        self.assertEqual(progress["chapters"]["completed"], [self.chapters[1]])
        self.pdf.write_bytes(b"%PDF-1.4 changed")
        progress = direct.resume(self.repo, self.book)
        self.assertTrue(progress["blocked"])
        self.assertEqual(progress["chapters"]["stale"], self.chapters)

    def test_unrelated_unit_and_audio_changes_keep_chapter_checkpoint(self):
        self.check_all()
        self.rows[1]["heading"] = "Tên bài sửa"
        self.write_units()
        audio_path = self.book / "_meta/audio.json"
        audio = direct.read(audio_path)
        audio["notes"] = "Đã kiểm kê lại thông tin CD."
        direct.write(audio_path, audio)
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["chapters"]["completed"], [self.chapters[0]])
        self.assertEqual(progress["chapters"]["stale"], [self.chapters[1]])

    def test_missing_source_block_mapping_and_audio_fail(self):
        self.rows[0]["source"][0]["pdf_blocks"] = ["p0001-b002"]
        self.write_units()
        with self.assertRaisesRegex(ValueError, "missing source block"):
            direct.build(self.repo, self.book)
        self.rows[0]["source"][0]["pdf_blocks"] = ["p0001-b001"]
        self.write_units()
        (self.book / "_meta/audio.json").unlink()
        with self.assertRaises(FileNotFoundError):
            direct.build(self.repo, self.book)

    def test_supplemental_audio_page_and_no_false_not_seen(self):
        audio_path = self.book / "_meta/audio.json"
        audio = direct.read(audio_path)
        audio.update({"supplemental_evidence_pages": [3], "checked_pdf_pages": [1, 2, 3],
                      "inventory_status": "documented", "actual_files_status": "not_provided",
                      "locations": [{"label": "CD hội thoại", "pdf_page": 3,
                                     "pdf_block": "p0003-b001"}]})
        direct.write(audio_path, audio)
        self.write_page(3, "audio_evidence")
        self.assertEqual(direct.audio_errors(audio, direct.read(self.book / "_meta/book.json"),
                                             self.rows, self.book), [])
        self.check_all()
        direct.build(self.repo, self.book)
        self.assertEqual(direct.validate(self.repo, self.book), 0)
        audio["inventory_status"] = "not_seen"
        direct.write(audio_path, audio)
        self.assertTrue(any("entire PDF" in x for x in direct.audio_errors(
            audio, direct.read(self.book / "_meta/book.json"), self.rows, self.book)))

    def test_partial_scope_cannot_be_initialized_as_full(self):
        with self.assertRaisesRegex(ValueError, "every physical PDF page"):
            direct.init(self.repo, self.repo / "kaiwa_skill/knowledge/Incomplete",
                        "kaiwa_skill/book/sample.pdf", "Incomplete", [1, 2],
                        self.chapters, "full")

    def test_changed_page_evidence_invalidates_dependent_chapter(self):
        self.check_all()
        evidence = direct.read(direct.page_path(self.book, 1))
        evidence["blocks"][0]["label"] = "Đã thay đổi phân vùng nguồn"
        direct.write(direct.page_path(self.book, 1), evidence)
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["pages"]["stale"], [1])
        self.assertEqual(progress["chapters"]["stale"], [self.chapters[0]])
        self.assertEqual(progress["chapters"]["completed"], [self.chapters[1]])

    def test_audio_file_found_requires_existing_hash_matched_asset(self):
        audio = direct.read(self.book / "_meta/audio.json")
        audio.update(actual_files_status="found", actual_files=[
            {"path": "kaiwa_skill/audio/track01.mp3", "sha256": "a" * 64}])
        meta = direct.read(self.book / "_meta/book.json")
        self.assertTrue(any("actual file missing/changed" in x for x in
                            direct.audio_errors(audio, meta, self.rows, self.book)))
        asset = self.repo / "kaiwa_skill/audio/track01.mp3"
        asset.parent.mkdir(parents=True)
        asset.write_bytes(b"audio fixture")
        audio["actual_files"][0]["sha256"] = direct.sha(asset)
        self.assertEqual(direct.audio_errors(audio, meta, self.rows, self.book), [])

    def test_scope_extension_retains_checkpoint_and_records_history(self):
        self.check_all()
        before = direct.read(self.book / "_meta/direct-state.json")
        output = direct.extend_scope(self.repo, self.book, [1, 2, 3],
                                     self.chapters + ["chapters/03.md"], "full",
                                     "Pilot accepted; full book authorized by coordinator.")
        after = direct.read(self.book / "_meta/direct-state.json")
        self.assertEqual(after["pages"]["1"], before["pages"]["1"])
        self.assertEqual(after["chapters"][self.chapters[0]],
                         before["chapters"][self.chapters[0]])
        self.assertEqual(after["pages"]["3"]["status"], "pending")
        self.assertEqual(direct.read(self.book / output["history"])["state_before"], before)
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["chapters"]["completed"], self.chapters)
        self.assertEqual(progress["pages"]["pending"], [3])

    def test_scope_extension_cannot_drop_or_recertify_old_content(self):
        self.check_all()
        with self.assertRaisesRegex(ValueError, "additive"):
            direct.extend_scope(self.repo, self.book, [2, 3], self.chapters,
                                "partial", "Wrongly drops old page.")
        (self.book / self.chapters[0]).write_text("Changed after review", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "stale"):
            direct.extend_scope(self.repo, self.book, [1, 2, 3], self.chapters,
                                "full", "Cannot erase stale evidence.")

    def test_needs_review_is_distinct_and_requires_explicit_validation_mode(self):
        self.check_issue_book()
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["pages"]["needs_review"], [1])
        self.assertEqual(progress["pages"]["completed"], [2])
        self.assertEqual(progress["chapters"]["needs_review"], [self.chapters[0]])
        result = direct.build(self.repo, self.book)
        self.assertEqual(result["completion_status"], "source_issues_unresolved")
        self.assertIn("_meta/source-issues.md", (self.book / "book.md").read_text(encoding="utf-8"))
        with redirect_stdout(io.StringIO()):
            self.assertEqual(direct.validate(self.repo, self.book), 1)
        output = io.StringIO()
        with redirect_stdout(output):
            self.assertEqual(direct.validate(self.repo, self.book, allow_source_issues=True), 0)
        self.assertIn("WARN", output.getvalue())
        self.assertIn("chưa xác nhận nội dung", output.getvalue())

    def test_needs_review_requires_mapped_issue_and_fresh_checkpoint(self):
        self.mark_source_issue()
        self.rows[0]["issues"][0]["pdf_block"] = "p0001-b999"
        self.write_units()
        with self.assertRaisesRegex(ValueError, "mapped pdf_page/pdf_block"):
            direct.build(self.repo, self.book)
        self.rows[0]["issues"][0]["pdf_block"] = "p0001-b001"
        self.write_units()
        evidence = direct.read(direct.page_path(self.book, 1))
        evidence["issues"] = []
        direct.write(direct.page_path(self.book, 1), evidence)
        with self.assertRaisesRegex(ValueError, "concrete source issues"):
            direct.checkpoint(self.repo, self.book, 1, None, "needs_review", "Đã xem ảnh.")
        evidence["issues"] = [{"pdf_block": "p0001-b001", "description": "Chữ bị che."}]
        direct.write(direct.page_path(self.book, 1), evidence)
        direct.checkpoint(self.repo, self.book, 1, None, "needs_review", "Đã xem ảnh.")
        with self.assertRaisesRegex(ValueError, "compatible"):
            direct.checkpoint(self.repo, self.book, None, self.chapters[0], "author_checked", "Đã xem ảnh.")
        direct.checkpoint(self.repo, self.book, None, self.chapters[0], "needs_review", "Còn chữ bị che.")
        evidence["issues"][0]["description"] = "Đổi mô tả sau checkpoint."
        direct.write(direct.page_path(self.book, 1), evidence)
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["pages"]["stale"], [1])
        self.assertEqual(progress["chapters"]["stale"], [self.chapters[0]])

    def test_page_issue_cannot_leave_affected_unit_author_checked(self):
        self.mark_source_issue()
        self.rows[0]["review_status"] = "author_checked"
        self.rows[0]["issues"] = []
        self.write_units()
        with self.assertRaisesRegex(ValueError, "requires matching needs_review unit"):
            direct.build(self.repo, self.book)

    def test_allow_source_issues_still_rejects_pending_and_missing(self):
        self.check_issue_book()
        direct.build(self.repo, self.book)
        state_path = self.book / "_meta/direct-state.json"
        state = direct.read(state_path)
        state["pages"]["2"] = {"status": "pending"}
        direct.write(state_path, state)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(direct.validate(self.repo, self.book, allow_source_issues=True), 1)
        self.assertEqual(direct.resume(self.repo, self.book)["chapters"]["stale"], [self.chapters[1]])
        direct.page_path(self.book, 2).unlink()
        with redirect_stdout(io.StringIO()):
            self.assertEqual(direct.validate(self.repo, self.book, allow_source_issues=True), 1)

    def test_needs_review_chapter_rejects_draft_related_page(self):
        self.mark_source_issue()
        self.rows[0]["source"].append({"pdf_page": 2, "pdf_blocks": ["p0002-b001"]})
        self.write_units()
        direct.checkpoint(self.repo, self.book, 1, None, "needs_review", "Đã xem ảnh.")
        with self.assertRaisesRegex(ValueError, "compatible"):
            direct.checkpoint(self.repo, self.book, None, self.chapters[0], "needs_review", "Còn chữ bị che.")

    def test_resume_prioritizes_unfinished_work_before_known_source_issue(self):
        self.mark_source_issue()
        direct.checkpoint(self.repo, self.book, 1, None, "needs_review", "Đã xem ảnh, còn chữ bị che.")
        direct.checkpoint(self.repo, self.book, None, self.chapters[0], "needs_review", "Giữ issue nguồn.")
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["next_page"], 2)
        self.assertEqual(progress["next_chapter"], self.chapters[1])
        direct.checkpoint(self.repo, self.book, 2, None, "author_checked", "Đã đối chiếu ảnh.")
        direct.checkpoint(self.repo, self.book, None, self.chapters[1], "author_checked", "Đã kiểm chương2.")
        progress = direct.resume(self.repo, self.book)
        self.assertEqual(progress["next_page"], 1)
        self.assertEqual(progress["next_chapter"], self.chapters[0])

    def test_legacy_issue_free_build_does_not_require_rewriting_accepted_pilot(self):
        self.check_all()
        direct.build(self.repo, self.book)
        meta_path = self.book / "_meta/book.json"
        meta = direct.read(meta_path)
        meta["build"].pop("review_state")
        meta["build"].pop("source_issues_sha256")
        direct.write(meta_path, meta)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(direct.validate(self.repo, self.book), 0)
        # A stale report must not be hidden by falling back to the older schema.
        (self.book / "_meta/source-issues.md").write_text("Old source issue", encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(direct.validate(self.repo, self.book), 1)


if __name__ == "__main__":
    unittest.main()
