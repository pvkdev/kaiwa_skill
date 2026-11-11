"""Regression cases from book layouts encountered during bulk cleaning."""
from pathlib import Path
import runpy
import tempfile
import unittest


API = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'scripts/validate_fork.py'))


class TranslationLayoutTest(unittest.TestCase):
    def report(self, body):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'chapter.md'
            path.write_text('<a id="u-fixture"></a>\n# Bài học\n\n' + body, encoding='utf-8')
            report = API['Report']()
            API['validate_chapter'](path, report)
            return report

    def check(self, body):
        return self.report(body).errors

    def test_self_introduction_translation_cannot_add_a_fourth_blank(self):
        report = self.report('**JP:** 私は＿＿＿＿の＿＿＿＿と申します。＿＿＿＿からまいりました。\n\n'
                             '**VI:** Tôi là＿＿＿＿thuộc＿＿＿＿, tên là＿＿＿＿. Tôi đến từ＿＿＿＿.\n')
        self.assertTrue(any('JP 3, VI 4' in warning for warning in report.warnings))

    def test_self_introduction_retains_three_functional_blanks(self):
        report = self.report('**JP:** 私は＿＿＿＿の＿＿＿＿と申します。＿＿＿＿からまいりました。\n\n'
                             '**VI:** Tôi thuộc＿＿＿＿, tên là＿＿＿＿. Tôi đến từ＿＿＿＿.\n')
        self.assertEqual([], report.warnings)

    def test_translation_should_not_solve_the_blank(self):
        report = self.report('**JP:** ここに（　）を入れてください。\n\n**VI:** Điền tên vào đây.\n')
        self.assertTrue(any('JP 1, VI 0' in warning for warning in report.warnings))

    def test_blank_width_and_glyph_are_layout_not_content(self):
        report = self.report('**JP:** 名前は＿＿＿＿です。\n\n**VI:** Tôi tên là________.\n')
        self.assertEqual([], report.warnings)

    def test_numbered_examples_preserve_numbering(self):
        self.assertEqual([], self.check('1. **JP:** 明日までにお願いします。\n\n   **VI:** Chậm nhất ngày mai nhé.\n'))

    def test_bulleted_examples(self):
        self.assertEqual([], self.check('- **JP:** お願いします。\n  **VI:** Nhờ bạn nhé.\n'))

    def test_named_japanese_speakers(self):
        self.assertEqual([], self.check('**係の人 (JP):** どうぞ。\n\n**係の人 (VI):** Xin mời.\n'))

    def test_translated_role_keeps_adjacent_pair(self):
        self.assertEqual([], self.check('**係の人 (JP):** どうぞ。\n\n**Nhân viên (VI):** Xin mời.\n'))

    def test_romanized_name_with_example_number(self):
        self.assertEqual([], self.check('**2 ルイス (JP):** お願いします。\n\n**Louis (VI):** Nhờ anh.\n'))

    def test_example_number_is_not_role_identity(self):
        self.assertEqual([], self.check('**1 リサ (JP):** はい。\n\n**リサ (VI):** Vâng.\n'))

    def test_different_japanese_roles_still_fail(self):
        self.assertTrue(self.check('**先生 (JP):** はい。\n\n**学生 (VI):** Vâng.\n'))

    def test_translated_role_still_requires_vi_tag(self):
        self.assertTrue(self.check('**係の人 (JP):** はい。\n\n**Nhân viên (JP):** Vâng.\n'))

    def test_translated_role_still_requires_adjacent_translation(self):
        self.assertTrue(self.check('**係の人 (JP):** はい。\n\n## Phần khác\n\n**Nhân viên (VI):** Vâng.\n'))

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
