import json
import runpy
import tempfile
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
V = runpy.run_path(str(SKILL_DIR / "scripts/vocab.py"))


class VocabularyPublication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ctx = V["brief"]("T-044")

    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = Path(folder.name) / "vocabulary.json"
        self.status = self.path.with_name("status.json")
        self.terms = [
            dict(id="v1", ja="EMS", reading="イーエムエス", vi="chuyển phát nhanh quốc tế", pos="noun",
                 origin="topic_extension", level_hint="none", level_note_vi="Tên dịch vụ bưu điện",
                 source_domain="procedural", source_refs=["post"])
        ]
        self.group = dict(id="g01", title_vi="Bưu điện", v10_topic=self.ctx["vocabulary_topics"][0], terms=self.terms)
        self.draft = dict(stage_uid=self.ctx["uid"], stage_code=self.ctx["code"], groups=[self.group],
                          dropped_topics={key: "Mẫu kiểm" for key in self.ctx["vocabulary_topics"][1:]},
                          admin_sources={"post": dict(kind="web", title="Japan Post", url="https://www.post.japanpost.jp/int/ems/",
                            accessed="2026-11-18", use_vi="Tên dịch vụ")})
        self.save()

    def save(self):
        self.path.write_text(json.dumps(self.draft), encoding="utf8")
        digest = V["group_hash"](self.group)
        self.record = dict(stage_uid=self.ctx["uid"], stage_code=self.ctx["code"], owner="review",
                           learner_sha256=self.ctx["learner_sha256"], skill_sha256=V["sha"](V["SKILL"].read_bytes()),
                           vocabulary_sha256=V["sha"](self.path.read_bytes()), open_issues=[],
                           groups={"g01":dict(state="reviewed", sha256=digest, reviewed_sha256=digest, note_vi="Đã rà")})
        self.status.write_text(json.dumps(self.record), encoding="utf8")

    def review(self):
        return V["reviewed_draft"](self.path, self.ctx)[0]

    def test_exchange_and_latin(self):
        node, = V["export"](self.review())["nodes"]
        self.assertEqual(node, {"id": "T-044-g01", "type": "vocabulary", "title_vi": "Bưu điện",
                                "data": {"terms_ja": ["EMS"]}})
        self.terms[0]["source_refs"] = []
        self.save()
        with self.assertRaisesRegex(ValueError, "needs source_refs"):
            self.review()

    def test_editor_selects_one_reading(self):
        for tid, reading in [("v2", "いちば"), ("v3", "しじょう")]:
            self.terms.append(dict(id=tid, ja="市場", reading=reading, vi="chợ", pos="noun",
                                   origin="topic_extension", level_hint="N3"))
        self.save()
        with self.assertRaisesRegex(ValueError, "duplicate terms_ja"):
            self.review()
        self.terms[-1]["export_ja"] = False
        self.save()
        self.assertEqual(V["export"](self.review())["nodes"][0]["data"]["terms_ja"], ["EMS", "市場"])
        self.terms[-2]["export_ja"] = False
        self.save()
        with self.assertRaisesRegex(ValueError, "representative"):
            self.review()

    def test_checkpoint(self):
        for key in ("stage_uid", "stage_code", "owner", "learner_sha256", "skill_sha256", "vocabulary_sha256",
                    "open_issues", "groups"):
            with self.subTest(key=key):
                self.status.write_text(json.dumps({**self.record, key: None}), encoding="utf8")
                with self.assertRaises(ValueError):
                    self.review()
        self.record["groups"]["g01"]["state"] = "needs_fix"
        self.status.write_text(json.dumps(self.record), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "needs current review"):
            self.review()
        self.save()
        self.terms[0]["vi"] = "nghĩa đã sửa"
        self.path.write_text(json.dumps(self.draft), encoding="utf8")
        with self.assertRaisesRegex(ValueError, "vocabulary_sha256"):
            self.review()


if __name__ == "__main__":
    unittest.main()
