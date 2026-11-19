"""Exercise publishing and checkpoint integrity exclusively in temporary folders."""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import audit as A

SPEC = importlib.util.spec_from_file_location("shadowing_pilot", Path(__file__).with_name("pilot.py"))
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.plan = Path(self.temp.name)
        self.code = "T-002"
        self.source = P.inputs(self.code)
        self.original = P.PLAN / "v13/pilot" / self.code
        self.original_hashes = {p.name: P.digest(p) for p in self.original.glob("*.json")}
        for target in ("pilot", "stages"):
            shutil.copytree(self.original, self.plan / "v13" / target / self.code)
        self.addCleanup(self.assert_pilot_untouched)
        self.patch_plan = patch.object(P, "PLAN", self.plan)
        self.patch_plan.start()
        self.addCleanup(self.patch_plan.stop)
        self.patch_inputs = patch.object(P, "inputs", side_effect=lambda code: copy.deepcopy(self.source))
        self.patch_inputs.start()
        self.addCleanup(self.patch_inputs.stop)

    def assert_pilot_untouched(self):
        self.assertEqual(self.original_hashes, {p.name: P.digest(p) for p in self.original.glob("*.json")})

    def call(self, mode, target="pilot"):
        with contextlib.redirect_stdout(io.StringIO()):
            P.build(self.code, mode, ["temporary test review"], target)

    def file(self, name, target="stages"):
        return self.plan / "v13" / target / self.code / name

    def change(self, name, fn):
        path = self.file(name)
        data = json.loads(path.read_text("utf8"))
        fn(data)
        P.save(path, data)

    def test_default_stays_pilot_and_checkpoint_is_read_only(self):
        before = {p.name: p.read_bytes() for p in self.file("draft.json", "pilot").parent.glob("*.json")}
        self.call("checkpoint")
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.file("draft.json", "pilot").parent.glob("*.json")})
        self.call("publish")
        self.assertEqual(json.loads(self.file("status.json", "pilot").read_text("utf8"))["code"], self.code)
        self.assertNotIn("code", json.loads(self.file("status.json").read_text("utf8")))

    def test_stages_publish_check_and_checkpoint(self):
        self.call("check", "stages")
        self.call("publish", "stages")
        before = {p.name: p.read_bytes() for p in self.file("draft.json").parent.glob("*.json")}
        self.call("checkpoint", "stages")
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.file("draft.json").parent.glob("*.json")})

    def test_tampering_is_rejected(self):
        for field, value in (("code", "T-003"), ("state", "draft"), ("v11", "wrong"),
                             ("v12", "wrong"), ("skill", "wrong"), ("draft", "wrong"),
                             ("output", "wrong"), ("count", 1)):
            with self.subTest(field=field):
                self.call("publish", "stages")
                self.change("status.json", lambda d: d.update({field: value}))
                with self.assertRaises(ValueError):
                    self.call("checkpoint", "stages")

    def test_output_cannot_be_replaced_even_with_updated_hash(self):
        self.call("publish", "stages")
        self.change("shadowing.json", lambda d: d["items"][0]["turns"][0].update(vi="Altered export"))
        self.change("status.json", lambda d: d.update(output=P.digest(self.file("shadowing.json"))))
        with self.assertRaisesRegex(ValueError, "exported node"):
            self.call("checkpoint", "stages")

    def test_draft_edit_invalidates_checkpoint(self):
        self.call("publish", "stages")
        self.change("draft.json", lambda d: d["items"][0].update(vi="Edited translation"))
        with self.assertRaisesRegex(ValueError, "draft"):
            self.call("checkpoint", "stages")

    def test_stale_pins_and_source_change_during_publish(self):
        self.source["pins"]["v12"] = "changed"
        with self.assertRaisesRegex(ValueError, "Inputs or skill changed"):
            self.call("publish", "stages")
        self.source["pins"] = json.loads(self.file("draft.json").read_text("utf8"))["pins"]
        changed = copy.deepcopy(self.source)
        changed["pins"]["v12"] = "new revision"
        with patch.object(P, "inputs", side_effect=[self.source, changed]):
            with self.assertRaisesRegex(ValueError, "changed during validation"):
                self.call("publish", "stages")


class AuditTests(unittest.TestCase):
    def test_all_293_topics_have_the_exact_chat_partition(self):
        course = P.V["read"](P.PLAN / "v11/learner.json")
        codes = [s["code"] for s in course["stages"] if s.get("stage_kind") == "topic"]
        self.assertEqual(len(codes), 293)
        self.assertEqual(len(set(codes)), 293)
        self.assertEqual({o: sum(A.chat_owner(c) == o for c in codes) for o in ("so", "trung", "thuong")},
                         {"so": 98, "trung": 98, "thuong": 97})

    def test_census_counts_only_valid_production_checkpoints_and_does_not_write(self):
        with tempfile.TemporaryDirectory() as tmp:
            plan = Path(tmp)
            (plan / "v11").mkdir()
            shutil.copy(P.PLAN / "v11/learner.json", plan / "v11/learner.json")
            for code in ("T-001", "T-002"):
                folder = plan / "v13/stages" / code
                folder.mkdir(parents=True)
                P.save(folder / "status.json", {"count": 20})
            def checkpoint(code, *args, **kwargs):
                if code == "T-002":
                    raise ValueError("stale pins")
            before = {p.relative_to(plan): p.read_bytes() for p in plan.rglob("*") if p.is_file()}
            with patch.object(A, "PLAN", plan), patch.object(A, "inputs", return_value={}), patch.object(A, "build", side_effect=checkpoint):
                result = A.audit()
            self.assertEqual(result["scope_total"], 293)
            self.assertEqual(result["reviewed"], 1)
            self.assertEqual(result["sentences"], 20)
            self.assertIn("T-002", result["remaining_codes"])
            self.assertNotIn("T-001", result["remaining_codes"])
            self.assertEqual(before, {p.relative_to(plan): p.read_bytes() for p in plan.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
