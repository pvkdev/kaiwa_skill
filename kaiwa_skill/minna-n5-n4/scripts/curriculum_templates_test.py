import copy
import json
import unittest
from pathlib import Path

from curriculum_templates import convert


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "authored/lesson-39/templates/sections.json"


class TemplateValidationTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_good_source(self):
        self.assertEqual(len(convert(self.data)), 5)

    def test_unknown_correct_choice(self):
        data = copy.deepcopy(self.data)
        data["sections"][0]["questions"][0]["correct_choice_id"] = "missing"
        with self.assertRaisesRegex(ValueError, "unknown correct ID"):
            convert(data)

    def test_missing_explanation(self):
        data = copy.deepcopy(self.data)
        data["sections"][2]["questions"][0]["explanation_vi"] = ""
        with self.assertRaisesRegex(ValueError, "missing explanation_vi"):
            convert(data)

    def test_blank_count_mismatch(self):
        data = copy.deepcopy(self.data)
        data["sections"][1]["questions"][0]["blank_answers"] = []
        with self.assertRaisesRegex(ValueError, "blank count differs"):
            convert(data)

    def test_audio_asset_missing(self):
        data = copy.deepcopy(self.data)
        data["sections"][4]["media"]["local_asset"] = "missing.mp3"
        with self.assertRaisesRegex(ValueError, "local audio asset missing"):
            convert(data)


if __name__ == "__main__":
    unittest.main()
