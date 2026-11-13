"""Authoring-data regressions, using disposable fictional content only."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO = Path(__file__).resolve().parents[4]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts/stage_work.py"
SPEC = importlib.util.spec_from_file_location("stage_work", SCRIPT)
WORK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WORK)
UIDS = ["50993510-7b18-5086-90de-24f6c44efecb", "8e4f2dbd-74ad-5332-a86e-ea63c1949286", "a5e3e992-bd3e-5c38-9cc8-83cc6c900a04"]


def put(path, value):
    WORK.atomic(path, value)


class ContentRegression(unittest.TestCase):
    def setUp(self):
        cache = (REPO / "kaiwa_skill/.cache").resolve()
        cache.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="content-contract-", dir=cache)
        self.root = Path(self.temp.name).resolve()
        self.assertTrue(self.root.is_relative_to(cache))
        self.addCleanup(self.temp.cleanup)
        put(self.root / "kaiwa_skill/planning/v2/chang_registry.json", {
            uid: {"display_code": f"S-{i + 1:02}", "title": "Fictional fixture", "level": "Sơ"} for i, uid in enumerate(UIDS)})
        self.run_id, self.draft = self.bundle(UIDS[0])

    def cli(self, command, uid, run=None, args=(), success=True):
        argv = [sys.executable, "-B", "-X", "utf8", str(SCRIPT), command, "--repo-root", str(self.root), "--stage", uid]
        if run:
            argv += ["--run", run]
        result = subprocess.run(argv + list(args), capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode == 0, success, result.stdout + result.stderr)
        return json.loads(result.stdout) if result.stdout.startswith("{") else result.stdout + result.stderr

    def bundle(self, uid):
        opened = self.cli("begin", uid)
        draft, run = Path(opened["draft"]), opened["run"]
        stage = WORK.read(draft / "stage.json")
        stage.update(scope="Fixture, not course material", events=[{"id": "e01", "title": "Event", "situation_ids": ["s01"]}], nodes=[
            {"id": "v01", "type": "vocabulary", "title": "Words", "path": "vocabulary/v01.json"},
            {"id": "k01", "type": "knowledge", "title": "Knowledge", "path": "knowledge/k01.md", "source_family": "speak_japanese", "video": {"status": "planned", "asset_ref": None}, "practice_node_id": "sh01"},
            {"id": "sh01", "type": "shadowing", "title": "Examples", "path": "shadowing/sh01.json"},
            {"id": "v02", "type": "vocabulary", "title": "Review words", "path": "vocabulary/v02.json"},
            {"id": "s01", "type": "situation", "title": "Situation", "path": "situations/s01.json"},
            {"id": "k03", "type": "knowledge", "title": "New point", "path": "knowledge/k03.md"},
            {"id": "sh03", "type": "shadowing", "title": "Practice", "path": "shadowing/sh03.json"},
            {"id": "live01", "type": "live_context", "title": "Live", "path": "live/live01.json"}])
        put(draft / "stage.json", stage)
        (draft / "knowledge").mkdir()
        (draft / "knowledge/k01.md").write_text('# Kiến thức thử\n<a id="ex01"></a>\nVí dụ thử, không trích sách.\n', encoding="utf-8")
        (draft / "knowledge/k03.md").write_text("# Điểm mới thử\n", encoding="utf-8")
        put(draft / "vocabulary/v01.json", {"id": "v01", "items": [{"id": "v01-w01", "ja": "メニュー", "vi": "thực đơn", "exposure": "new"}]})
        put(draft / "vocabulary/v02.json", {"id": "v02", "items": [{"id": "v02-w01", "ja": "メニュー", "vi": "thực đơn", "exposure": "review"}]})
        turns = [{"id": "s01-t01", "speaker": "A", "ja": "メニューはありますか。", "vi": "Có thực đơn không?"}, {"id": "s01-t02", "speaker": "B", "ja": "はい、どうぞ。", "vi": "Có, mời bạn."}]
        speakers = [{"id": "A", "role": "Customer"}, {"id": "B", "role": "Staff"}]
        put(draft / "situations/s01.json", {"id": "s01", "title": "Scene", "event_id": "e01", "setting": "Restaurant", "communication_goal": "Ask for menu", "relationship": "Customer/staff", "outcome": "received", "speakers": speakers, "turns": turns, "authorship": "original_extension"})
        put(draft / "shadowing/sh01.json", {"id": "sh01", "knowledge_ids": ["k01"], "items": [{"id": "sh01-e01", "kind": "sentence", "example_id": "ex01", "ja": "おいしいですね。", "vi": "Ngon nhỉ.", "authorship": "original_extension"}]})
        put(draft / "shadowing/sh03.json", {"id": "sh03", "knowledge_ids": ["k03"], "items": [
            {"id": "sh03-e01", "kind": "sentence", "ja": "メニューを見せてください。", "vi": "Cho tôi xem thực đơn.", "authorship": "original_extension"},
            {"id": "sh03-d01", "kind": "dialogue", "speakers": speakers, "turns": [{**t, "id": "sh03-" + t["id"]} for t in turns], "authorship": "original_extension"},
            {"id": "sh03-r01", "kind": "situation_ref", "situation_id": "s01"}]})
        put(draft / "live/live01.json", {"id": "live01", "context_node_ids": [n["id"] for n in stage["nodes"][:-1]], "context_export": "live-context.md"})
        put(draft / "sources.json", {"scan": [{"book_id": f"B{i:02}", "status": "index_only", "note": "Fixture only"} for i in range(1, 28)], "entries": []})
        def ref(lid, nid=None, item=None):
            value = {"stage_uid": uid, "revision": None, "lesson_id": lid}
            if nid:
                value["node_id"] = nid
            if item:
                value["item_id"] = item
            return value
        put(draft / "learning-map.json", {"schema_version": "1.0", "stage_uid": uid, "lessons": [
            {"id": "l01", "summary": "New word and point", "node_ids": ["v01", "k01", "sh01"], "lookback": [], "reuse": [], "reason_no_reuse": "First fixture lesson", "pending_previous": []},
            {"id": "l02", "summary": "A new scene", "node_ids": ["v02", "s01"], "lookback": [ref("l01")], "reuse": [{"from": ref("l01", "v01", "v01-w01"), "in": [{"node_id": "v02", "item_id": "v02-w01"}, {"node_id": "s01", "item_id": "s01-t01"}], "purpose": "Use the word in another exchange"}], "pending_previous": []},
            {"id": "l03", "summary": "New phrasing with cumulative review", "node_ids": ["k03", "sh03"], "lookback": [ref("l01"), ref("l02")], "reuse": [{"from": ref("l01", "v01", "v01-w01"), "in": [{"node_id": "sh03", "item_id": "sh03-e01"}], "purpose": "Use prior vocabulary"}, {"from": ref("l02", "s01"), "in": [{"node_id": "sh03", "item_id": "sh03-r01"}], "purpose": "Review the earlier scene"}], "pending_previous": []}]})
        (draft / "editorial.md").write_text("# Fictional fixture, not production lessons\n", encoding="utf-8")
        return run, draft

    def test_three_lessons_sentence_dialogue_and_scene_reference(self):
        WORK.check(self.draft, UIDS[0], self.root)
        stage = WORK.read(self.draft / "stage.json")
        WORK.export_context(self.draft, stage)
        context = (self.draft / "live-context.md").read_text(encoding="utf-8")
        self.assertIn("sh03-r01", context)
        self.assertIn("l03", context)
        self.assertIn("メニューを見せてください。", context)

    def test_speak_pair_must_be_adjacent(self):
        stage = WORK.read(self.draft / "stage.json")
        stage["nodes"][0], stage["nodes"][1] = stage["nodes"][1], stage["nodes"][0]
        put(self.draft / "stage.json", stage)
        with self.assertRaisesRegex(ValueError, "immediately followed"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_speak_example_requires_knowledge_anchor(self):
        (self.draft / "knowledge/k01.md").write_text("# Missing example", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "example missing"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_future_local_lesson_rejected(self):
        learning = WORK.read(self.draft / "learning-map.json")
        learning["lessons"][1]["lookback"][0]["lesson_id"] = "l03"
        put(self.draft / "learning-map.json", learning)
        with self.assertRaisesRegex(ValueError, "same/future"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_review_word_needs_actual_earlier_item(self):
        learning = WORK.read(self.draft / "learning-map.json")
        learning["lessons"][1]["reuse"][0]["from"]["item_id"] = "missing-word"
        put(self.draft / "learning-map.json", learning)
        with self.assertRaisesRegex(ValueError, "Unknown earlier"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_future_stage_cannot_be_used_as_previous_knowledge(self):
        learning = WORK.read(self.draft / "learning-map.json")
        learning["lessons"][0]["lookback"] = [{"stage_uid": UIDS[1], "revision": "r0001", "lesson_id": "l01"}]
        put(self.draft / "learning-map.json", learning)
        with self.assertRaisesRegex(ValueError, "earlier curriculum stage"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_new_word_cannot_claim_review_without_link(self):
        data = WORK.read(self.draft / "vocabulary/v01.json")
        data["items"][0]["exposure"] = "review"
        put(self.draft / "vocabulary/v01.json", data)
        with self.assertRaisesRegex(ValueError, "Review word needs"):
            WORK.check(self.draft, UIDS[0], self.root)

    def test_pause_resume_keeps_learning_map(self):
        before = (self.draft / "learning-map.json").read_bytes()
        self.cli("pause", UIDS[0], self.run_id, ["--next", "Review next example"])
        self.cli("resume", UIDS[0], self.run_id)
        self.assertEqual((self.draft / "learning-map.json").read_bytes(), before)

    def external_bundle(self):
        self.cli("finalize", UIDS[0], self.run_id, ["--editor-reviewed", "--note", "Fixture only"])
        run, draft = self.bundle(UIDS[1])
        learning = WORK.read(draft / "learning-map.json")
        first = learning["lessons"][0]
        first["lookback"] = [{"stage_uid": UIDS[0], "revision": "r0001", "lesson_id": lid} for lid in ["l02", "l03"]]
        first["reuse"] = [{"from": {**first["lookback"][0], "node_id": "v02", "item_id": "v02-w01"}, "in": [{"node_id": "v01", "item_id": "v01-w01"}], "purpose": "Carry vocabulary across stages"}]
        put(draft / "learning-map.json", learning)
        data = WORK.read(draft / "vocabulary/v01.json")
        data["items"][0]["exposure"] = "review"
        put(draft / "vocabulary/v01.json", data)
        return run, draft

    def test_external_lessons_pin_actual_revision_materials(self):
        _, draft = self.external_bundle()
        WORK.check(draft, UIDS[1], self.root)
        pins = WORK.learning_pins(self.root, draft)
        self.assertTrue(any(p.endswith("current.json") for p in pins))
        self.assertTrue(any(p.endswith("shadowing/sh03.json") for p in pins))

    def test_prior_upgrade_detected_on_resume_and_recovery_preserves_work(self):
        run, draft = self.external_bundle()
        before = (draft / "learning-map.json").read_bytes()
        self.cli("pause", UIDS[1], run, ["--next", "Continue after previous-stage check"])
        upgrade = self.cli("begin", UIDS[0], args=["--from-current"])
        self.cli("finalize", UIDS[0], upgrade["run"], ["--editor-reviewed", "--note", "New fixture revision"])
        message = self.cli("resume", UIDS[1], run, success=False)
        self.assertIn("Pinned", message)
        recovered = self.cli("recover", UIDS[1], run, ["--ack-stopped"])
        self.assertEqual((Path(recovered["draft"]) / "learning-map.json").read_bytes(), before)
        with self.assertRaisesRegex(ValueError, "revision changed"):
            WORK.check(Path(recovered["draft"]), UIDS[1], self.root)

    def test_pilot_pending_continuity_is_visible_in_manifest(self):
        learning = WORK.read(self.draft / "learning-map.json")
        learning["lessons"][0]["pending_previous"] = [{"note": "Standalone pilot, earlier content absent"}]
        put(self.draft / "learning-map.json", learning)
        finalized = self.cli("finalize", UIDS[0], self.run_id, ["--editor-reviewed", "--note", "Fixture with explicit continuity gap"])
        manifest = WORK.read(Path(finalized["content"]).parent / "manifest.json")
        self.assertEqual(manifest["continuity_pending"], 1)

    def test_legacy_draft_can_be_read_without_overwriting_it(self):
        stage = WORK.read(self.draft / "stage.json")
        stage["schema_version"] = "3.0-draft"
        put(self.draft / "stage.json", stage)
        (self.draft / "learning-map.json").unlink()
        WORK.check(self.draft, UIDS[0], self.root)
        self.assertEqual(WORK.read(self.draft / "stage.json")["schema_version"], "3.0-draft")

    def test_begin_uses_published_v5_registry_and_pins_curriculum(self):
        new_uid = "9d98dd08-a68c-5fa9-99e6-053b65ba98c1"
        pointer = {"version": "5.0", "registry": "kaiwa_skill/planning/v5/chang_registry.json",
                   "roadmap": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5.jsonl",
                   "policy": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5_META.json"}
        put(self.root / pointer["registry"], {
            new_uid: {"display_code": "T-101", "title": "Fictional new V5 stage", "level": "Trung"}})
        roadmap = self.root / pointer["roadmap"]
        roadmap.write_text(json.dumps({"uid": new_uid}) + "\n", encoding="utf-8")
        put(self.root / pointer["policy"], {"version": "5.0"})
        put(self.root / "kaiwa_skill/planning/CURRENT_ROADMAP.json", pointer)
        result = self.cli("begin", new_uid)
        stage = WORK.read(Path(result["draft"]) / "stage.json")
        self.assertEqual(stage["title"], "Fictional new V5 stage")
        self.assertEqual(stage["curriculum"], pointer)
        state = WORK.read(self.root / "kaiwa_skill/courseware" / new_uid / "runs" / (result["run"] + ".json"))
        self.assertIn(pointer["roadmap"], state["spec_pins"])
        changed = {**pointer, "version": "future", "roadmap": "kaiwa_skill/planning/future.jsonl"}
        put(self.root / "kaiwa_skill/planning/CURRENT_ROADMAP.json", changed)
        self.assertEqual(WORK.curriculum_spec(self.root, stage["curriculum"]), pointer)

    def test_curriculum_pointer_cannot_escape_repo(self):
        pointer = {"version": "5.0", "registry": "../../outside.json", "roadmap": "r.jsonl", "policy": "p.json"}
        put(self.root / "kaiwa_skill/planning/CURRENT_ROADMAP.json", pointer)
        with self.assertRaisesRegex(ValueError, "outside"):
            WORK.curriculum_spec(self.root)


if __name__ == "__main__":
    unittest.main()
