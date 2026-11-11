"""Regression cases from book layouts encountered during bulk cleaning."""
from pathlib import Path
import runpy
import tempfile
import unittest


API = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/validate_fork.py'))


class TranslationLayoutTest(unittest.TestCase):
    def check(self, body):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'chapter.md'
            path.write_text('<a id="u-fixture"></a>\n# Bài học\n\n' + body, encoding='utf-8')
            report = API['Report']()
            API['validate_chapter'](path, report)
            return report.errors

    def test_numbered_examples_preserve_numbering(self):
        self.assertEqual([], self.check('1. **JP:** 明日までにお願いします。\n\n   **VI:** Chậm nhất ngày mai nhé.\n'))

    def test_bulleted_examples(self):
        self.assertEqual([], self.check('- **JP:** お願いします。\n  **VI:** Nhờ bạn nhé.\n'))

    def test_named_japanese_speakers(self):
        self.assertEqual([], self.check('**係の人 (JP):** どうぞ。\n\n**係の人 (VI):** Xin mời.\n'))

    def test_unlabelled_source_speaker(self):
        self.assertEqual([], self.check('**A₁:** 伝言をお願いします。\n**VI:** Nhờ chuyển lời giúp tôi.\n'))

    def test_unlabelled_japanese_paragraph(self):
        self.assertEqual([], self.check('この本は会話を学ぶための本です。\n\n**VI:** Sách dùng để học hội thoại.\n'))

    def test_explicit_source_missing_translation_fails(self):
        self.assertTrue(self.check('**JP:** お願いします。\n\n## Phần tiếp theo\n'))

    def test_orphan_translation_fails(self):
        self.assertTrue(self.check('**VI:** Không có câu nguồn ở đây.\n'))

    def test_explicit_speaker_mismatch_fails(self):
        self.assertTrue(self.check('**A (JP):** どうぞ。\n\n**B (VI):** Xin mời.\n'))

    def test_raw_image_marker_still_fails(self):
        self.assertTrue(self.check('Hình (biên tập): Có người ở bên trái.\n'))


if __name__ == '__main__':
    unittest.main()
