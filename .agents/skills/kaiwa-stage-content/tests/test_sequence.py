"""Book-order plan checks; fictional anchors and stages only."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
SPEC = importlib.util.spec_from_file_location("source_sequence", SCRIPTS / "source_sequence.py")
SEQUENCE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEQUENCE)
UIDS = ["00000000-0000-4000-8000-000000000001", "00000000-0000-4000-8000-000000000002",
        "00000000-0000-4000-8000-000000000003"]


class PlanFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        planning = self.root / "kaiwa_skill/planning"
        (planning / "v5").mkdir(parents=True)
        (planning / "catalog27").mkdir()
        self.example = json.loads((ROOT / "kaiwa_skill/contracts/harumii-kaiwa/v1/example-stage.json").read_text(encoding="utf-8"))
        registry = {uid: {"display_code": "X-0" + str(i), "title": self.example["title_vi"],
                          "level": "Trung" if i == 3 else "Sơ", "order": i} for i, uid in enumerate(UIDS, 1)}
        (planning / "v5/chang_registry.json").write_text(json.dumps(registry, ensure_ascii=False), encoding="utf-8")
        (planning / "CURRENT_ROADMAP.json").write_text(json.dumps({
            "version": "5.0", "registry": "kaiwa_skill/planning/v5/chang_registry.json",
            "roadmap": "kaiwa_skill/planning/v5/ROADMAP.jsonl", "policy": "kaiwa_skill/planning/v5/META.json"}), encoding="utf-8")
        rows = [("B11", "u-88-front", "Front matter"), ("B11", "u-part1-01", "Lesson 1"), ("B11", "u-part1-02", "Lesson 2"),
                ("B11", "u-88-part2-09", "Lesson 9"), ("B14", "u-sd-u1-s01", "Section 1"), ("B14", "u-sd-u1-s02", "Section 2")]
        (planning / "catalog27/source_index.jsonl").write_text(
            "".join(json.dumps({"book_id": b, "anchor": a, "label": label}) + "\n" for b, a, label in rows), encoding="utf-8")
        self.plan = {"schema_version": "1.0", "approval": {"status": "approved"}, "books": {
            "B11": {"family": "speak_japanese", "levels": ["Sơ"], "status": "active", "unit_pattern": r"^u-(88-)?part[12]-\d+$"},
            "B14": {"family": "shadowing", "levels": ["Sơ", "Trung"], "status": "active", "unit_pattern": r"^u-sd-u\d+-s\d+$"},
            "B26": {"family": "nama_chuukei", "levels": ["Sơ"], "status": "excluded", "reason": "No dialogue script"}},
            "assignments": []}

    def assign(self, book, unit, stage, status="planned", **extra):
        self.plan["assignments"].append({"book_id": book, "unit": unit, "stage_uid": UIDS[stage - 1], "status": status, **extra})

    def save(self):
        (self.root / "kaiwa_skill/planning/v5/SOURCE_SEQUENCE.json").write_text(json.dumps(self.plan, ensure_ascii=False), encoding="utf-8")

    def check(self):
        errors, warnings, _, _ = SEQUENCE.check_plan(self.root, self.plan)
        return errors, warnings


class SequencePlan(PlanFixture):
    def test_units_in_book_order_pass(self):
        self.assign("B11", "u-part1-01", 1)
        self.assign("B11", "u-part1-02", 1)
        self.assign("B11", "u-88-part2-09", 2)
        self.assign("B14", "u-sd-u1-s01", 3)
        self.assertEqual(self.check(), ([], []))

    def test_later_unit_can_precede_an_earlier_unit(self):
        self.assign("B11", "u-part1-02", 1)
        self.assign("B11", "u-part1-01", 2)
        self.assertEqual(self.check(), ([], []))

    def test_provisional_pilot_is_reported_without_blocking(self):
        self.assign("B11", "u-part1-02", 1, status="provisional")
        self.assign("B11", "u-part1-01", 2)
        errors, warnings = self.check()
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_unit_must_be_schedulable_and_fit_stage_level(self):
        self.assign("B11", "u-88-front", 1)
        self.assign("B11", "u-part1-01", 3)
        self.assign("B26", "anything", 1)
        text = " ".join(self.check()[0])
        self.assertIn("not a schedulable unit", text)
        self.assertIn("outside the book levels", text)
        self.assertIn("not active in the plan", text)

    def test_a_unit_cannot_be_split_between_stages(self):
        self.assign("B14", "u-sd-u1-s01", 1)
        self.assign("B14", "u-sd-u1-s01", 2)
        self.assertIn("assigned twice", " ".join(self.check()[0]))
        self.plan["assignments"] = []
        self.assign("B14", "u-sd-u1-s01", 1, part="1/2")
        self.assign("B14", "u-sd-u1-s01", 2, part="2/2")
        self.assertIn("cannot be split", " ".join(self.check()[0]))

    def test_draft_allocations_are_optional(self):
        self.plan["approval"]["status"] = "draft"
        self.assertEqual(self.check(), ([], []))

    def test_cli_reports_plan_and_review_table(self):
        self.assign("B11", "u-part1-01", 1)
        self.assign("B11", "u-part1-02", 2, status="provisional")
        self.save()
        def cli(*args):
            return subprocess.run([sys.executable, "-B", "-X", "utf8", str(SCRIPTS / "source_sequence.py"), *args,
                                   "--repo-root", str(self.root)], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(json.loads(cli("check").stdout)["assigned_units"], {"B11": 2})
        self.assertIn("X-02 | " + self.example["title_vi"] + " | B11 · Lesson 2 · tạm", cli("table", "--level", "Sơ").stdout)
        self.assertIn("u-88-part2-09\t-\tLesson 9", cli("units", "--book", "B11").stdout)
        self.assertEqual(json.loads(cli("stage", "--stage", UIDS[1]).stdout)["units_listed_earlier_per_book"], {"B11": 1})
        self.plan["assignments"][0]["unit"] = "u-88-front"
        self.save()
        self.assertEqual(cli("check").returncode, 2)


class SequenceInAuthoring(PlanFixture):
    """The compiler refuses a stage that teaches ordered books outside the plan."""

    def open(self, stage=1, units=None):
        self.save()
        uid = UIDS[stage - 1]
        opened = self.cli("begin", uid)
        self.run_id, self.draft = opened["run"], Path(opened["draft"])
        data = dict(copy.deepcopy(self.example), stage_uid=uid)
        audit = {"nodes": {n["id"]: {"authorship": "original_extension", "source_refs": []}
                           for n in data["nodes"] if n["type"] not in {"live_challenge", "free_talk"}},
                 "vocabulary_evidence": {"v01": [{"term": "メニュー", "kind": "other", "dictionary_form_reviewed": True,
                                                    "evidence": [{"utterance_id": "u01", "surface": "メニュー"}]}]}}
        if units is not None:
            audit["sequence_units"] = units
        self.put("harumii-stage.json", data)
        self.put("source-map.json", audit)
        self.put("sources.json", {"scan": [{"book_id": f"B{i:02}", "status": "index_only", "note": "Fixture"} for i in range(1, 28)], "entries": []})
        self.put("learning-map.json", {"schema_version": "1.0", "stage_uid": uid, "lessons": [
            {"id": l["id"], "summary": l["title_vi"], "node_ids": l["node_ids"]} for l in data["lessons"]]})
        if units and units.get("k01"):
            self.seed_cd(data, audit, units["k01"][0]["unit"])
        return uid

    def seed_cd(self, data, audit, unit):
        src = {"id": "cd", "kind": "book", "book_id": "B11", "title": "Fixture", "locator": unit}
        first, second = data["utterances"][:2]
        script = self.root / "fixture.md"
        script.write_text('<a id="' + unit + '"></a>\n' + first["ja"] + "\n" + second["ja"], encoding="utf-8")
        digest = hashlib.sha256(script.read_bytes()).hexdigest()
        for u in (first, second):
            u.update(authorship="source_quote", source_refs=["cd"])
        data["source_registry"] = [src]
        lesson = next(n["data"] for n in data["nodes"] if n["type"] == "knowledge")
        lesson["utterance_ids"].append(second["id"])
        lesson["body_md"] += "\n\n{{utterance:" + second["id"] + "}}"
        sh = next(n for n in data["nodes"] if n["type"] == "shadowing")
        ids = [first["id"], second["id"]]
        sh["data"]["items"] = [{"id": "i"+str(i), "kind": "sentence", "utterance_id": uid} for i, uid in enumerate(ids)]
        sources = json.loads((self.draft / "sources.json").read_text(encoding="utf-8"))
        sources["entries"] = [dict(src, path=script.name, read_status="read", used_for=["k01", "sh01"], sha256=digest)]
        self.put("sources.json", sources)
        part = {"path": script.name, "sha256": digest, "unit": unit,
                "turns": [[2, 0, len(first["ja"])], [3, 0, len(second["ja"])]]}
        key = "B11/" + unit
        manifest = {"pack_id": key, "edition": "Fixture", "boundary_evidence": "Whole lesson",
                    "tracks": [{"track": "1", "disc": "unknown", "locator": unit, "parts": [part]}]}
        path = self.root / "kaiwa_skill/planning/catalog27/audio_packs" / (key + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest), encoding="utf-8")
        audit["audio_packs"] = [{"pack_id": key, "shadowing_node_id": sh["id"], "utterance_ids": ids,
                                 "manifest_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}]
        self.put("harumii-stage.json", data)
        self.put("source-map.json", audit)

    def put(self, name, data):
        (self.draft / name).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def cli(self, command, uid, run=None, ok=True):
        cmd = [sys.executable, "-B", "-X", "utf8", str(SCRIPTS / "stage_work.py"), command, "--repo-root", str(self.root), "--stage", uid]
        if run:
            cmd += ["--run", run]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return json.loads(result.stdout) if result.stdout.startswith("{") else result.stdout + result.stderr

    def test_scheduled_speak_japanese_lesson_validates(self):
        self.assign("B11", "u-part1-01", 1)
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        self.cli("validate", uid, self.run_id)

    def test_provisional_pilot_can_finalize(self):
        self.assign("B11", "u-part1-01", 1, status="provisional")
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        cmd = [sys.executable, "-B", "-X", "utf8", str(SCRIPTS / "stage_work.py"), "finalize", "--repo-root", str(self.root),
               "--stage", uid, "--run", self.run_id, "--editor-reviewed", "--note", "Fictional fixture reviewed"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["revision"], "r0001")

    def test_speak_japanese_lesson_needs_its_scheduled_unit(self):
        self.assign("B11", "u-part1-01", 2)
        uid = self.open(1)
        self.assertIn("needs its source book unit", self.cli("validate", uid, self.run_id, ok=False))

    def test_stage_can_teach_a_unit_suggested_elsewhere(self):
        self.assign("B11", "u-part1-01", 2)
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        self.cli("validate", uid, self.run_id)

    def test_stage_can_skip_a_suggested_unit(self):
        self.assign("B11", "u-part1-01", 1)
        self.assign("B14", "u-sd-u1-s01", 1)
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        self.cli("validate", uid, self.run_id)

    def test_suggested_allocation_does_not_constrain_selection(self):
        self.assign("B11", "u-part1-01", 1)
        self.assign("B11", "u-part1-02", 2)
        self.assign("B14", "u-sd-u1-s01", 1)
        self.assign("B14", "u-sd-u1-s02", 3)
        units = {"k01": [{"book_id": "B11", "unit": "u-part1-02"}],
                 "sh01": [{"book_id": "B14", "unit": "u-sd-u1-s01", "role": "review"}]}
        uid = self.open(2, units)
        self.cli("validate", uid, self.run_id)
        units["sh01"][0]["unit"] = "u-sd-u1-s02"
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        audit["sequence_units"] = units
        self.put("source-map.json", audit)
        self.cli("validate", uid, self.run_id)

    def test_ordered_book_in_sources_needs_declared_units(self):
        self.assign("B11", "u-part1-01", 1)
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        sources = json.loads((self.draft / "sources.json").read_text(encoding="utf-8"))
        sources["entries"] += [{"id": "src-b14", "kind": "book", "book_id": "B14", "read_status": "read",
                               "locator": {"heading": "Fixture"}, "used_for": ["sh01"]}]
        self.put("sources.json", sources)
        self.assertIn("without sequence_units", self.cli("validate", uid, self.run_id, ok=False))

    def test_unallocated_audio_pack_matches_script_without_rewriting(self):
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-02"}]})
        data = json.loads((self.draft / "harumii-stage.json").read_text(encoding="utf-8"))
        first = data["utterances"][0]
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        pack = audit["audio_packs"].pop()
        self.put("source-map.json", audit)
        self.assertIn("Missing audio pack", self.cli("validate", uid, self.run_id, ok=False))
        ids = pack["utterance_ids"]
        audit["audio_packs"] = [pack]
        self.put("source-map.json", audit)
        self.cli("validate", uid, self.run_id)
        pack["utterance_ids"] = ids[::-1]
        self.put("source-map.json", audit)
        self.assertIn("contiguous", self.cli("validate", uid, self.run_id, ok=False))
        pack["utterance_ids"] = ids
        self.put("source-map.json", audit)
        first["authorship"] = "source_adaptation"
        self.put("harumii-stage.json", data)
        self.assertIn("original Japanese", self.cli("validate", uid, self.run_id, ok=False))

    def test_ai_only_and_wrong_book_lesson_are_rejected(self):
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-02"}]})
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        audit["sequence_units"]["k01"][0]["unit"] = "u-part1-01"
        self.put("source-map.json", audit)
        self.assertIn("matching CD pack", self.cli("validate", uid, self.run_id, ok=False))
        audit["audio_packs"] = []
        self.put("source-map.json", audit)
        self.put("harumii-stage.json", self.example)
        self.assertIn("matching CD pack", self.cli("validate", uid, self.run_id, ok=False))

    def test_full_multitrack_pack_keeps_middle_turn_and_one_node(self):
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-02"}]})
        data = json.loads((self.draft / "harumii-stage.json").read_text(encoding="utf-8"))
        audit = json.loads((self.draft / "source-map.json").read_text(encoding="utf-8"))
        pack = audit["audio_packs"][0]
        path = self.root / "kaiwa_skill/planning/catalog27/audio_packs" / (pack["pack_id"] + ".json")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        track2 = copy.deepcopy(manifest["tracks"][0])
        track2["track"] = "2"
        # The next track repeats the first line of the script.
        track2["parts"][0]["turns"] = track2["parts"][0]["turns"][:1]
        manifest["tracks"].append(track2)
        path.write_text(json.dumps(manifest), encoding="utf-8")
        self.assertIn("inventory changed", self.cli("validate", uid, self.run_id, ok=False))
        pack["manifest_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.put("source-map.json", audit)
        self.assertIn("every source turn", self.cli("validate", uid, self.run_id, ok=False))
        sh = next(n["data"] for n in data["nodes"] if n["type"] == "shadowing")
        sh["items"].append(dict(sh["items"][0], id="repeat"))
        pack["utterance_ids"].append(pack["utterance_ids"][0])
        lesson = next(n["data"] for n in data["nodes"] if n["type"] == "knowledge")
        lesson["body_md"] += "\n{{utterance:u01}}"
        self.put("harumii-stage.json", data)
        self.put("source-map.json", audit)
        self.cli("validate", uid, self.run_id)
        full = pack["utterance_ids"].copy()
        pack["utterance_ids"] = [full[0],full[-1]]
        sh["items"].pop(1)
        lesson["body_md"] = "{{utterance:u01}}"
        lesson["utterance_ids"] = ["u01"]
        self.put("harumii-stage.json", data)
        self.put("source-map.json", audit)
        self.assertIn("every source turn", self.cli("validate", uid, self.run_id, ok=False))

    def test_catalog_pack_from_another_book_is_checked(self):
        spec = importlib.util.spec_from_file_location("stage_compile_pack", SCRIPTS / "stage_compile.py")
        compiler = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(compiler)
        path = self.root / "kaiwa_skill/planning/catalog27/audio_packs/B15/model.json"
        path.parent.mkdir(parents=True)
        manifest = {"pack_id": "B15/model", "edition": "fixture", "boundary_evidence": "complete fixture",
                    "tracks": [{"disc": "1", "track": "7", "locator": "model", "parts": [
                        {"path": "script.md", "sha256": "fixture", "unit": "model", "turns": [[2, 0, 3]]}]}]}
        path.write_text(json.dumps(manifest), encoding="utf-8")
        source = {"src": {"book_id": "B15", "path": "script.md", "sha256": "fixture"}}
        texts = {"src": '<a id="model"></a>\nはい。'}
        data = {"utterances": [{"id": "u", "ja": "はい。", "authorship": "source_quote", "source_refs": ["src"]}],
                "nodes": [{"id": "sh", "type": "shadowing", "data": {
                    "items": [{"kind": "sentence", "utterance_id": "u"}]}}]}
        audit = {"audio_packs": [{"pack_id": "B15/model", "manifest_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                                 "shadowing_node_id": "sh", "utterance_ids": ["u"]}]}
        self.assertEqual(len(compiler.check_audio_packs(self.root, data, audit, source, texts)), 1)
        data["nodes"][0]["data"]["items"].append({"kind": "sentence", "utterance_id": "u"})
        with self.assertRaisesRegex(ValueError, "declared order"):
            compiler.check_audio_packs(self.root, data, audit, source, texts)

    def test_new_writing_cannot_be_labelled_source_reference(self):
        self.assign("B11", "u-part1-01", 1)
        uid = self.open(1, {"k01": [{"book_id": "B11", "unit": "u-part1-01"}]})
        data = json.loads((self.draft / "harumii-stage.json").read_text(encoding="utf-8"))
        data["utterances"][-1]["learning_scope"] = "source_reference"
        self.put("harumii-stage.json", data)
        self.assertIn("simplify newly written lines", self.cli("validate", uid, self.run_id, ok=False))


if __name__ == "__main__":
    unittest.main()
