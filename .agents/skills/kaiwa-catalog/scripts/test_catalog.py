"""Small regression checks for source location and micro-dialogue boundaries."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('catalog', Path(__file__).with_name('catalog.py'))
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)


class IndexTests(unittest.TestCase):
    def test_named_microcontext_keeps_real_line_and_anchor(self):
        text = '# Bài\n<a id="u-1"></a>\n## Biểu đạt\n1. **Email chưa đến.** A (JP): メール。 — A (VI): Chưa tới.\n'
        rows = catalog.extract(text, 'B01', 'B01-C01')
        row = rows[-1]
        self.assertEqual((row['kind'], row['label'], row['line'], row['anchor']), ('situation_caption', 'Email chưa đến.', 4, 'u-1'))

    def test_dialogue_without_setting_uses_source_words(self):
        rows = catalog.extract('# Section\n1. **C**\n- **A:** そう？\n **VI:** Vậy sao?\n', 'B01', 'B01-C01')
        self.assertEqual(rows[-1]['kind'], 'numbered_material')
        self.assertIn('Vậy sao?', rows[-1]['label'])

    def test_next_item_translation_cannot_leak_back(self):
        rows = catalog.extract('# Section\n1. x\n2. y\n **VI:** của mục2\n', 'B01', 'B01-C01')
        self.assertNotIn('của mục2', rows[1]['label'])
        self.assertIn('của mục2', rows[2]['label'])

    def test_style_marker_is_not_a_topic(self):
        rows = catalog.extract('# Section\n1. **D**\n- **A:** はい。\n **VI:** Vâng.\n', 'B01', 'B01-C01')
        self.assertEqual(rows[-1]['kind'], 'numbered_material')
        self.assertIn('Vâng.', rows[-1]['label'])

    def test_no_imagined_situation_for_expression(self):
        rows = catalog.extract('# Vui\n1. **うれしいです。** — Tôi vui.\n', 'B01', 'B01-C01')
        self.assertEqual(rows[-1]['kind'], 'named_item')
        self.assertEqual(rows[-1]['label'], 'うれしいです。')

    def test_unicode_normalization_does_not_merge_different_topics(self):
        self.assertEqual(catalog.key('Ａ  B'), catalog.key('A B'))
        self.assertNotEqual(catalog.key('Nhận lời'), catalog.key('Từ chối'))


if __name__ == '__main__':
    unittest.main()
