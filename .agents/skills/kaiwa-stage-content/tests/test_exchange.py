"""Contract/packaging checks only; never a learner test or a database import."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[4]
SCRIPT = Path(__file__).resolve().parents[1] / "scripts/kaiwa_exchange.py"
SPEC = importlib.util.spec_from_file_location("kaiwa_exchange", SCRIPT)
EXCHANGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(EXCHANGE)
CONTRACT = ROOT / "kaiwa_skill/contracts/harumii-kaiwa/v1"


class ExchangeRegression(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((CONTRACT / "example-stage.json").read_text(encoding="utf-8"))

    def node(self, kind):
        return next(node for node in self.data["nodes"] if node["type"] == kind)

    def test_public_copy_blocks_source_labels_across_student_surfaces(self):
        self.data["source_registry"] = [{"id": "textbook", "kind": "book", "book_id": "B27",
                                         "title": "聞いて覚える話し方", "locator": "Bài 1"}]
        EXCHANGE.check_public_copy(self.data)
        for owner, key, text in [
            (self.node("knowledge")["data"], "body_md", "Trong skit B27, câu mở là hỏi chỗ ngồi."),
            (self.data["lessons"][0], "title_vi", "Luyện nghe với Speak Japanese"),
            (self.node("live_challenge")["data"]["variants"][0], "learner_addendum_vi", "Nghe track 12."),
            (self.data["utterances"][0], "ja", "聞いて覚える話し方"),
        ]:
            with self.subTest(key=key):
                old = owner[key]
                owner[key] = text
                with self.assertRaisesRegex(ValueError, "Learner copy"):
                    EXCHANGE.check_public_copy(self.data)
                owner[key] = old

    def test_new_pack_needs_knowledge_metadata_but_legacy_json_still_valid(self):
        lesson = self.node("knowledge")["data"]
        del lesson["admin_provenance"]
        EXCHANGE.validate(self.data)
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / "out"
            with self.assertRaisesRegex(ValueError, "admin_provenance"):
                EXCHANGE.pack(self.data, dest)
            self.assertFalse(dest.exists())

    def test_knowledge_cd_is_searchable_and_private_after_packing(self):
        src = {"id": "a", "kind": "book", "book_id": "B11", "title": "Tên sách thử", "locator": "Bài 3"}
        self.data["source_registry"] = [src]
        self.data["utterances"][0]["source_refs"] = ["a"]
        audit = {"nodes": {"k01": {"authorship": "source_adaptation", "source_refs": ["a"]}}}
        tracks = [{"disc": "2", "track": t, "locator": "Phụ lục trang 10"} for t in ["4", "5"]]
        pack = {"pack_id": "B11/example", "edition": "Ấn bản thử", "shadowing_node_id": "sh01",
                "utterance_ids": ["u01"], "tracks": tracks}
        EXCHANGE.attach_knowledge_credits(self.data, audit, [pack])
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp) / "out"
            EXCHANGE.pack(self.data, dest)
            exported = EXCHANGE.verify(dest)
            knowledge = next(n for n in exported["nodes"] if n["type"] == "knowledge")
            cds = knowledge["data"]["admin_provenance"]["cd_refs"]
            self.assertEqual([(c["source_ref"], c["disc"], c["track"]) for c in cds], [("a", "2", "4"), ("a", "2", "5")])
            self.assertTrue(all("Tên sách thử" not in p.read_text(encoding="utf-8") for p in dest.glob("*.md")))
        self.node("knowledge")["data"]["admin_provenance"]["cd_refs"][0]["pack_id"] = "B27/wrong"
        with self.assertRaisesRegex(ValueError, "CD pack and book disagree"):
            EXCHANGE.validate(self.data)

    def test_full_seven_node_example(self):
        EXCHANGE.validate(self.data)
        self.assertEqual(len({node["type"] for node in self.data["nodes"]}), 7)

    def test_generated_schema_files_are_current(self):
        for name, schema in EXCHANGE.schemas().items():
            self.assertEqual((CONTRACT / name).read_text(encoding="utf-8"), EXCHANGE.dumps(schema))

    def test_missing_vietnamese_is_rejected(self):
        del self.data["utterances"][0]["vi"]
        with self.assertRaises(ValueError):
            EXCHANGE.validate(self.data)

    def test_each_new_utterance_has_truthful_source_category(self):
        utterance = self.data["utterances"][0]
        utterance["authorship"] = "source_quote"
        with self.assertRaisesRegex(ValueError, "actual source reference"):
            EXCHANGE.validate(self.data)
        utterance["source_refs"] = ["missing"]
        with self.assertRaisesRegex(ValueError, "Unknown utterance source"):
            EXCHANGE.validate(self.data)

    def test_b11_knowledge_cannot_hide_as_general(self):
        self.data["source_registry"] = [{"id": "b11", "kind": "book", "book_id": "B11", "title": "Fixture source", "locator": "Fixture section"}]
        self.data["utterances"][0]["source_refs"] = ["b11"]
        self.node("knowledge")["data"]["source_family"] = "general"
        with self.assertRaisesRegex(ValueError, "B11/B12 knowledge"):
            EXCHANGE.validate(self.data)

    def test_grammar_requires_searchable_jlpt_level(self):
        pattern = self.node("grammar")["data"]["patterns"][0]
        del pattern["jlpt_level"]
        with self.assertRaises(ValueError):
            EXCHANGE.validate(self.data)
        pattern["jlpt_level"] = "beginner"
        with self.assertRaises(ValueError):
            EXCHANGE.validate(self.data)

    def test_audio_dictionary_fields_and_furigana_are_not_exchange_fields(self):
        for field in ["audio_url", "furigana", "harumi_dictionary_id"]:
            data = copy.deepcopy(self.data)
            data["utterances"][0][field] = "not-owned-by-skill"
            with self.assertRaises(ValueError):
                EXCHANGE.validate(data)
        self.data["utterances"][0]["ja"] = "<ruby>言葉<rt>ことば</rt></ruby>"
        with self.assertRaisesRegex(ValueError, "furigana"):
            EXCHANGE.validate(self.data)

    def test_broken_dialogue_reference_and_role_are_rejected(self):
        turn = self.node("situation")["data"]["turns"][0]
        turn["utterance_id"] = "missing"
        with self.assertRaisesRegex(ValueError, "Unknown utterance"):
            EXCHANGE.validate(self.data)
        turn["utterance_id"] = "u01"
        for entry in self.node("situation")["data"]["turns"]:
            entry["speaker_id"] = "A"
        with self.assertRaisesRegex(ValueError, "Both roles"):
            EXCHANGE.validate(self.data)

    def test_free_talk_cannot_include_challenge_commands(self):
        self.node("free_talk")["data"]["context_node_ids"].append("c01")
        with self.assertRaisesRegex(ValueError, "Invalid node reference/type"):
            EXCHANGE.validate(self.data)

    def test_challenge_requires_taught_material_and_valid_variant(self):
        self.node("live_challenge")["data"]["default_variant_id"] = "missing"
        with self.assertRaisesRegex(ValueError, "Unknown default"):
            EXCHANGE.validate(self.data)
        self.node("live_challenge")["data"]["default_variant_id"] = "normal"
        challenge = self.node("live_challenge")
        self.data["nodes"].remove(challenge)
        self.data["nodes"].insert(0, challenge)
        with self.assertRaisesRegex(ValueError, "must precede"):
            EXCHANGE.validate(self.data)

    def test_knowledge_and_shadowing_share_one_example(self):
        knowledge = self.node("knowledge")["data"]
        knowledge["body_md"] += "\n{{utterance:missing}}"
        with self.assertRaisesRegex(ValueError, "tokens must match"):
            EXCHANGE.validate(self.data)

    def test_vocabulary_is_japanese_strings_and_grammar_is_names(self):
        self.node("vocabulary")["data"]["terms_ja"][0] = {"ja": "料理", "vi": "món ăn"}
        with self.assertRaises(ValueError):
            EXCHANGE.validate(self.data)

    def test_local_review_must_come_from_earlier_material(self):
        self.data["review_links"] = [{"from_stage_uid": self.data["stage_uid"], "from_revision": 1,
                                      "from_node_id": "s01", "to_node_ids": ["k01"], "purpose_vi": "Invalid reverse review"}]
        with self.assertRaisesRegex(ValueError, "earlier material"):
            EXCHANGE.validate(self.data)

    def test_pack_preserves_long_prompts_separates_variants_and_hashes_files(self):
        data = self.node("live_challenge")["data"]
        data["ai_situation_vi"] += " Giữ nội dung đầy đủ để luyện nói." * 100
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "new-export"
            manifest = EXCHANGE.pack(self.data, path)
            self.assertEqual(json.loads((path / "stage.json").read_text(encoding="utf-8")), self.data)
            self.assertEqual(EXCHANGE.verify(path), self.data)
            for name, digest in manifest["files"].items():
                self.assertEqual(hashlib.sha256((path / name).read_bytes()).hexdigest(), digest)
            ai = (path / "challenge-c01-normal.ai.md").read_text(encoding="utf-8")
            learner = (path / "challenge-c01-normal.learner.md").read_text(encoding="utf-8")
            self.assertIn(data["ai_situation_vi"], ai)
            self.assertNotIn(data["variants"][1]["ai_addendum_vi"], ai)
            self.assertNotIn(data["variants"][0]["ai_addendum_vi"], learner)
            free = (path / "free-talk-situation.md").read_text(encoding="utf-8")
            self.assertNotIn(data["ai_situation_vi"], free)
            for utterance in self.data["utterances"]:
                self.assertIn(utterance["ja"], free)
                self.assertIn(utterance["vi"], free)
            with self.assertRaises(FileExistsError):
                EXCHANGE.pack(self.data, path)
            (path / "stage.json").write_text("{}", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing/changed"):
                EXCHANGE.verify(path)

    def test_manifest_cannot_reference_paths_outside_artifact(self):
        manifest = {"schema_version": "1.0.0", "kind": "artifact_manifest", "entrypoint": "stage.json",
                    "files": {"stage.json": "a" * 64, "../other.json": "a" * 64}}
        with self.assertRaises(ValueError):
            EXCHANGE.validate(manifest)

    def test_editorial_export_gate_preserves_stage_identity_and_node_types(self):
        script = SCRIPT.with_name("stage_work.py")
        spec = importlib.util.spec_from_file_location("exchange_stage_work", script)
        work = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(work)
        stage = {"harumii_export": "harumii-stage.json", "stage_uid": self.data["stage_uid"],
                 "title": self.data["title_vi"], "display_code": self.data["display_code"], "level": "Sơ",
                 "nodes": [{"id": n["id"], "type": "live_context" if n["type"] == "free_talk" else n["type"]}
                           for n in self.data["nodes"] if n["type"] != "live_challenge"]}
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            (directory / "harumii-stage.json").write_text(EXCHANGE.dumps(self.data), encoding="utf-8")
            self.assertEqual(work.check_harumii_export(directory, stage), self.data)
            stage["stage_uid"] = "00000000-0000-4000-8000-000000000002"
            with self.assertRaisesRegex(ValueError, "does not match editorial stage"):
                work.check_harumii_export(directory, stage)


if __name__ == "__main__":
    unittest.main()
