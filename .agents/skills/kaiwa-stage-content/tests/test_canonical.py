"""Actual canonical lifecycle, including interrupted work; fictional content only."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts/stage_work.py"
UID = "00000000-0000-4000-8000-000000000001"


class CanonicalLifecycle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        p = self.root / "kaiwa_skill/planning/v2/chang_registry.json"
        p.parent.mkdir(parents=True)
        self.data = json.loads((ROOT / "kaiwa_skill/contracts/harumii-kaiwa/v1/example-stage.json").read_text(encoding="utf-8"))
        p.write_text(json.dumps({UID: {"display_code": self.data["display_code"], "title": self.data["title_vi"], "level": "Sơ"}}), encoding="utf-8")
        opened = self.cli("begin")
        self.run, self.draft = opened["run"], Path(opened["draft"])
        self.put("harumii-stage.json", self.data)
        self.put("source-map.json", {"nodes": {n["id"]: {"authorship": "original_extension", "source_refs": []}
                                                for n in self.data["nodes"] if n["type"] not in {"live_challenge", "free_talk"}},
                                     "vocabulary_evidence": {"v01": [{"term": "メニュー", "kind": "other", "dictionary_form_reviewed": True,
                                                                        "evidence": [{"utterance_id": "u01", "surface": "メニュー"}]}]}})
        self.put("sources.json", {"scan": [{"book_id": f"B{i:02}", "status": "index_only", "note": "Fixture"} for i in range(1, 28)], "entries": []})
        self.put("learning-map.json", {"schema_version": "1.0", "stage_uid": UID, "lessons": [
            {"id": l["id"], "summary": l["title_vi"], "node_ids": l["node_ids"], "lookback": [], "reuse": [],
             "pending_previous": [], "reason_no_reuse": "Fictional lifecycle fixture"} for l in self.data["lessons"]]})

    def put(self, name, data):
        (self.draft / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def cli(self, command, run=None, args=(), ok=True):
        cmd = [sys.executable, "-B", "-X", "utf8", str(SCRIPT), command, "--repo-root", str(self.root), "--stage", UID]
        if run:
            cmd += ["--run", run]
        result = subprocess.run(cmd + list(args), capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return json.loads(result.stdout) if result.stdout.startswith("{") else result.stdout + result.stderr

    def test_generate_validate_pause_resume_finalize_and_upgrade(self):
        before = (self.draft / "harumii-stage.json").read_bytes()
        self.cli("validate", self.run)
        self.assertEqual((self.draft / "harumii-stage.json").read_bytes(), before)
        self.assertTrue((self.draft / "knowledge/k01.md").exists())
        self.cli("pause", self.run, ["--next", "Read fixture again before finishing"])
        self.cli("resume", self.run)
        self.cli("finalize", self.run, ["--editor-reviewed", "--note", "Fictional fixture reviewed"])
        upgraded = self.cli("begin", args=["--from-current"])
        payload = json.loads((Path(upgraded["draft"]) / "harumii-stage.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["revision"], 2)
        self.cli("validate", upgraded["run"])

    def test_recovery_preserves_partial_canonical_source(self):
        self.cli("checkpoint", self.run, ["--next", "Finish next conversation"])
        partial = '{"schema_version":"1.0.0","notes":"unfinished'
        (self.draft / "harumii-stage.json").write_text(partial, encoding="utf-8")
        recovered = self.cli("recover", self.run, ["--ack-stopped", "--next", "Repair partial JSON, preserving authored text"])
        self.assertEqual((Path(recovered["draft"]) / "harumii-stage.json").read_text(encoding="utf-8"), partial)
        self.assertEqual((self.draft / "harumii-stage.json").read_text(encoding="utf-8"), partial)

    def test_foreign_owner_cannot_compile(self):
        self.cli("sync", "00000000-0000-4000-8000-000000000099", ok=False)

    def test_dictionary_form_is_not_polite_form(self):
        node = next(n for n in self.data["nodes"] if n["type"] == "vocabulary")
        node["data"]["terms_ja"] = ["行きます"]
        self.put("harumii-stage.json", self.data)
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        audit["vocabulary_evidence"]["v01"] = [{"term": "行きます", "kind": "verb", "dictionary_form_reviewed": True,
                                                "evidence": [{"utterance_id": "u01", "surface": "行きます"}]}]
        self.put("source-map.json", audit)
        self.assertIn("dictionary form", self.cli("validate", self.run, ok=False))

    def test_vocabulary_must_come_from_actual_spoken_material(self):
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        audit["vocabulary_evidence"]["v01"][0]["evidence"][0]["surface"] = "not-in-dialogue"
        self.put("source-map.json", audit)
        self.assertIn("actual spoken example", self.cli("validate", self.run, ok=False))
