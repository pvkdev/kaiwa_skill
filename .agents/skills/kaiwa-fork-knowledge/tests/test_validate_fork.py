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

    def test_multiline_example_keeps_numbered_lines_and_arrows_before_vi(self):
        report = self.report('**Ví dụ (JP):**\n\n1. その日は都合が悪いので\n'
                             '2. 来週に変更してもらえますか。\n\n'
                             '→ その日は都合が悪いので、来週に変更してもらえますか。\n\n'
                             '**Ví dụ (VI):** Vì hôm đó không tiện, có thể đổi sang tuần sau không?\n')
        self.assertEqual([], report.errors)

    def test_empty_marker_with_dialogue_block_and_qualified_vi(self):
        report = self.report('**Khung hội thoại in sẵn (JP):**\n\n'
                             '> A₁: いらっしゃいませ。  \n> B₁: ＿＿＿＿と申します。\n\n'
                             '**Khung hội thoại (VI, giữ ô trống):**\n\n'
                             '> A₁: Xin mời vào.  \n> B₁: Tôi là ＿＿＿＿.\n')
        self.assertEqual([], report.errors)
        self.assertEqual([], report.warnings)

    def test_descriptive_jp_label_can_have_plain_vi(self):
        self.assertEqual([], self.check('**Chỉ dẫn in sẵn (JP):** 帰る時、あいさつをします。  \n'
                                        '**VI:** Chào khi ra về.\n'))

    def test_dialogue_role_cannot_be_erased_by_plain_vi(self):
        self.assertTrue(self.check('**A (JP):** どうぞ。\n\n**VI:** Xin mời.\n'))

    def test_numbered_dialogue_role_cannot_be_erased_by_plain_vi(self):
        for label in ('1 A', '例1 A'):
            with self.subTest(label=label):
                errors = self.check(f'**{label} (JP):** どうぞ。\n\n**VI:** Xin mời.\n')
                self.assertTrue(any('must be followed' in error for error in errors))
                self.assertTrue(any('lacks preceding' in error for error in errors))

    def test_placeholder_only_pair_is_valid_exercise_payload(self):
        for blank in ('＿＿＿＿', '____', '( )'):
            with self.subTest(blank=blank):
                self.assertEqual([], self.check(f'**JP:** {blank}\n\n**VI:** {blank}\n'))

    def test_placeholder_only_multiline_block_is_valid(self):
        self.assertEqual([], self.check('**JP:**\n\n> A₁: ＿＿＿＿\n\n'
                                        '**VI:**\n\n> A₁: ＿＿＿＿\n'))

    def test_multiline_missing_vi_before_heading_still_fails(self):
        self.assertTrue(any('must be followed' in error for error in self.check(
            '**Ví dụ (JP):**\n\n→ お願いします。\n\n## Bài tiếp theo\n')))

    def test_empty_marker_with_only_markup_and_role_prefix_fails(self):
        errors = self.check('**Khung hội thoại (JP):**\n\n> A₁:\n\n'
                            '**Khung hội thoại (VI):**\n\n> A₁: Xin chào.\n')
        self.assertTrue(any('empty Khung hội thoại (JP)' in error for error in errors))

    def test_multiline_wrong_speaker_still_fails(self):
        errors = self.check('**A (JP):** どうぞ。\n\n→ こちらです。\n\n'
                            '**B (VI):** Xin mời, ở đây ạ.\n')
        self.assertTrue(any('must be followed' in error for error in errors))
        self.assertTrue(any('lacks preceding' in error for error in errors))

    def test_multiline_placeholder_mismatch_still_warns(self):
        report = self.report('**JP:**\n\n> A: ＿＿＿＿に＿＿＿＿を入れてください。\n\n'
                             '**VI:**\n\n> A: Hãy điền vào ＿＿＿＿.\n')
        self.assertTrue(any('JP 2, VI 1' in warning for warning in report.warnings))

    def test_second_jp_label_does_not_hide_missing_vi(self):
        errors = self.check('**Ví dụ (JP):** お願いします。\n\n'
                            '**Ghi chú (JP):** ありがとうございます。\n\n'
                            '**Ghi chú (VI):** Xin cảm ơn.\n')
        self.assertTrue(any('Ví dụ (JP) must be followed' in error for error in errors))

    def test_second_vi_cannot_reuse_japanese_quoted_in_previous_vi_marker(self):
        errors = self.check('**JP:** 日本語です。\n\n'
                            '**VI:** Đây là từ 日本語.\n\n'
                            '**VI:** Một bản dịch khác không có câu nguồn.\n')
        self.assertTrue(any('VI lacks preceding JP' in error for error in errors))

    def test_repeated_unlabelled_japanese_speakers_keep_plain_vi_glosses(self):
        body = ('**グエン:** すみません。\n**VI:** Xin lỗi.\n\n'
                '**担当者:** どうぞ。\n**VI:** Xin mời.\n\n'
                '**グエン:** ありがとうございます。\n**VI:** Xin cảm ơn.\n')
        self.assertEqual([], self.check(body))

    def test_unlabelled_source_after_explicit_pair_keeps_plain_vi(self):
        self.assertEqual([], self.check('**JP:** はい。\n**VI:** Vâng.\n\n'
                                        '**先生:** どうぞ。\n**VI:** Xin mời.\n'))

    def test_numbered_exercise_mark_is_not_part_of_jp_vi_payload(self):
        report = self.report('1. (　) **JP:** お願いします。\n'
                             '   **VI:** Nhờ anh/chị.\n')
        self.assertEqual([], report.errors)
        self.assertEqual([], report.warnings)

    def test_ellipsis_is_a_real_dialogue_turn(self):
        self.assertEqual([], self.check('**夫 (JP):** ……\n**Chồng (VI):** …\n'))

    def test_inline_vi_does_not_absorb_next_table_or_exercise_heading(self):
        report = self.report('**JP:** お願いします。\n**VI:** Nhờ anh/chị.\n\n'
                             '6. **＿＿＿＿ほど＿＿＿＿**\n'
                             '| Đề | Nghĩa |\n|---|---|\n| （　） | ô trống |\n')
        self.assertEqual([], report.errors)
        self.assertEqual([], report.warnings)

    def test_explicit_a_role_still_cannot_use_plain_vi_after_continuation(self):
        self.assertTrue(self.check('**A (JP):** どうぞ。\n\n→ こちらです。\n\n'
                                   '**VI:** Xin mời.\n'))

    def test_second_plain_vi_without_new_japanese_source_is_orphan(self):
        errors = self.check('**JP:** はい。\n**VI:** Vâng.\n\n**VI:** Vâng ạ.\n')
        self.assertTrue(any('lacks preceding' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
