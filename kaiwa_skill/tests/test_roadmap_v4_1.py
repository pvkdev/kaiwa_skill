"""Regression checks for roadmap metadata; these are not learner tests."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "kaiwa_skill/tools/roadmap_v4_1.py"
FOLDER = ROOT / "kaiwa_skill/planning/v2"
SPEC = importlib.util.spec_from_file_location("roadmap", SCRIPT)
ROADMAP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ROADMAP)


class RoadmapRegression(unittest.TestCase):
    def setUp(self):
        self.rows = [json.loads(s) for s in (FOLDER / "KAIWA_CHANG_V4_1.jsonl").read_text(encoding="utf-8").splitlines()]
        self.registry = ROADMAP.read(FOLDER / "chang_registry.json")
        self.meta = ROADMAP.read(FOLDER / "KAIWA_CHANG_V4_1_META.json")

    def row(self, sid):
        return next(r for r in self.rows if r["id"] == sid)

    def validate(self):
        ROADMAP.validate(self.rows, self.registry, self.meta)

    def test_accepted_identity_and_inventory(self):
        self.validate()
        self.assertEqual(len(self.rows), 194)
        self.assertEqual(sum(len(r["situations"]) for r in self.rows), 645)

    def test_missing_companion_lesson_rejected(self):
        self.row("T-23")["banks"].remove("B23:L8")
        with self.assertRaisesRegex(ValueError, "source regression"):
            self.validate()

    def test_unqualified_memo_stage_rejected(self):
        self.row("T-56")["banks"].append("S16:STAGE1")
        with self.assertRaisesRegex(ValueError, "unknown/coarse"):
            self.validate()

    def test_semantic_regression_cannot_hide_behind_correct_kind(self):
        situation = self.row("H-56")["situations"][0]
        situation.update(sources=["S08:19"], kind="memo", ai=False)
        self.row("H-56")["sources"] = ["S08:19", "S01:B1-23"]
        with self.assertRaisesRegex(ValueError, "source regression"):
            self.validate()

    def test_uid_reassignment_rejected_even_if_registry_changed(self):
        first, second = self.rows[:2]
        first["uid"], second["uid"] = second["uid"], first["uid"]
        self.registry[first["uid"]], self.registry[second["uid"]] = self.registry[second["uid"]], self.registry[first["uid"]]
        with self.assertRaisesRegex(ValueError, "identity or order"):
            self.validate()

    def test_fact_check_flag_cannot_silently_disappear(self):
        self.row("H-10")["fact_check"] = False
        with self.assertRaisesRegex(ValueError, "fact_check required"):
            self.validate()

    def test_bank_does_not_promote_ai_situation(self):
        self.row("T-23")["situations"][0].update(kind="book", ai=False)
        with self.assertRaisesRegex(ValueError, "inconsistent situation"):
            self.validate()

    def test_stage_source_union_must_match_situations(self):
        self.row("T-34")["sources"].remove("B02:S32")
        with self.assertRaisesRegex(ValueError, "ordered situation-source union"):
            self.validate()

    def test_readonly_check_and_idempotent_render(self):
        cache = (ROOT / "kaiwa_skill/.cache").resolve()
        cache.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="roadmap-check-", dir=cache) as name:
            folder = Path(name).resolve()
            self.assertTrue(folder.is_relative_to(cache))
            for file in ["KAIWA_CHANG_V4_1.jsonl", "KAIWA_CHANG_V4_1_META.json", "KAIWA_CHANG_V4_1.md", "chang_registry.json"]:
                shutil.copy2(FOLDER / file, folder / file)
            path = folder / "KAIWA_CHANG_V4_1.md"
            original = path.read_bytes()
            command = [sys.executable, "-B", "-X", "utf8", str(SCRIPT), "--directory", str(folder)]
            p = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(path.read_bytes(), original)
            text = path.read_text(encoding="utf-8").replace("Có token sách: 212.", "Có token sách: 999.")
            path.write_text(text, encoding="utf-8")
            p = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("Markdown is stale", p.stderr)
            p = subprocess.run(command + ["--write"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(path.read_text(encoding="utf-8"), original.decode("utf-8").replace("\r\n", "\n"))
            restored = path.read_bytes()
            p = subprocess.run(command + ["--write"], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(path.read_bytes(), restored)


if __name__ == "__main__":
    unittest.main()
