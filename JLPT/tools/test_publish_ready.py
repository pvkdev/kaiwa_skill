"""Regression checks for authoring QA and the admin handoff. All release fixtures are temporary."""
import base64
import hashlib
import json
import tempfile
import unittest
import uuid
from pathlib import Path

from build_publish_ready import export
from batch_job import checkpoint
from convert_singlefile import ROOT, SingleFileDocument, passage_markdown
from jlpt_coverage import coverage
from jlpt_sentences import sentence_units


def fixture(root, level):
    raw = (ROOT / "contracts/v1/synthetic-draft.json").read_text(encoding="utf-8")
    data = json.loads(raw)
    for identity in [data["packageId"], *(n["nodeId"] for n in data["annotations"]["nodes"])]:
        raw = raw.replace(identity, str(uuid.uuid5(uuid.NAMESPACE_URL, level + identity)))
    data = json.loads(raw)
    data["schemaVersion"] = "1.3.0"
    data["exam"].update(level=level, slug="2024/12", year=2024, month=12)
    data["content"]["choukai"]["mondais"] = []
    data["masterAudio"] = None
    data["structure"]["expectations"] = data["structure"]["expectations"][:1]
    mondai = data["content"]["dokkai"]["mondais"][0]
    block = mondai["blocks"][0]
    passage = block["mediaItems"][0]
    ann = data["annotations"]
    ann["audioSegments"] = []
    ann["sentencePairs"] = {passage["id"]: [{"ja": passage["passage"]["jaMd"], "vi": passage["passage"]["viMd"]}]}
    ids = {mondai["id"], block["id"], passage["id"], *(q["id"] for q in block["questions"])}
    ann["nodes"] = [n for n in ann["nodes"] if n["nodeId"] in ids]
    ann["answers"] = [a for a in ann["answers"] if a["questionId"] in ids]
    for field in ann["fields"]:
        field["reviewStatus"] = "approved"
    for q, prompt in zip(block["questions"], ["Mở lúc mấy giờ?", "Đóng lúc mấy giờ?"], strict=True):
        q["prompt"]["textVi"] = prompt
        for choice, vi in zip(q["choices"], ["9 giờ sáng", "10 giờ sáng", "6 giờ chiều", "7 giờ tối"], strict=True):
            choice["textVi"] = vi
    # Reuse the same local image in both exams to exercise cross-level deduplication.
    png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACklEQVR4nGPoAAAAigCJ/xNBzgAAAABJRU5ErkJggg==")
    digest = hashlib.sha256(png).hexdigest()
    image_path = f"assets/sha256/{digest[:2]}/{digest}.png"
    (root / image_path).parent.mkdir(parents=True, exist_ok=True)
    (root / image_path).write_bytes(png)
    data["assets"].append(dict(assetId="sha256:" + digest, path=image_path, sha256=digest, mediaType="image/png",
                               byteLength=len(png), durationMs=None, width=1, height=1,
                               origins=[dict(sourceId="synthetic-author", locator="fixture/image")],
                               derivedFromAssetId=None, transform=None))
    block["questions"][0]["imageUrl"] = "asset://" + digest
    data["review"].update(status="approved", reviewedBy="test", reviewedAt="2026-11-28T00:00:00Z", issues=[])
    path = root / f"packages/{level}/2024-12/package.json"
    path.parent.mkdir(parents=True)
    path.write_bytes(json.dumps(data).encode())
    receipt = dict(packageId=data["packageId"], revision=data["revision"], sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    path.with_name("release-review.json").write_text(json.dumps(receipt), encoding="utf-8")
    return path


class ReleaseChecks(unittest.TestCase):
    def test_export_retry_changed_receipt_and_withdrawal(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            files = [fixture(root, level) for level in ("N3", "N5")]
            self.assertEqual(export(root), 2)
            self.assertEqual(len(list((root / "publish-ready/assets").rglob("*.png"))), 1)
            index = root / "publish-ready/catalog.json"
            original = index.read_bytes()
            paths = [e["path"] for e in json.loads(original)["packages"]]
            self.assertEqual(paths, [f"{level}/JLPT-{level}-2024-12-r01/package.json" for level in ("N3", "N5")])
            self.assertEqual(export(root), 2)
            self.assertEqual(original, index.read_bytes())
            files[0].write_bytes(files[0].read_bytes() + b" ")
            with self.assertRaisesRegex(ValueError, "receipt mismatch"):
                export(root)
            self.assertEqual(original, index.read_bytes())
            for remaining, path in zip((1, 0), files, strict=True):
                data = json.loads(path.read_bytes())
                data["review"]["status"] = "draft"
                path.write_text(json.dumps(data), encoding="utf-8")
                self.assertEqual(export(root), remaining)
            self.assertFalse(index.exists())

    def test_batch_checkpoint_detects_other_worker_and_stale_input(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder).resolve()
            raw = root / "N3/2412/written.html"
            raw.parent.mkdir(parents=True)
            raw.write_bytes(b"example")
            (root / "reports").mkdir()
            page = dict(level="N3", period="2024-12", section="written", path="N3/2412/written.html",
                        sha256=hashlib.sha256(raw.read_bytes()).hexdigest())
            (root / "reports/source-gaps.json").write_text(json.dumps({"pages": [page]}), encoding="utf-8")
            claimed = checkpoint(root, "N3", "2024-12", "worker-1")
            self.assertEqual(checkpoint(root, "N3", "2024-12", None), claimed)
            with self.assertRaisesRegex(ValueError, "Already assigned"):
                checkpoint(root, "N3", "2024-12", "worker-2")
            raw.with_suffix(".mp3").write_bytes(b"added source")
            with self.assertRaisesRegex(ValueError, "Inputs or canonical"):
                checkpoint(root, "N3", "2024-12", None)

    def test_table_boundaries_preserve_cells(self):
        doc = SingleFileDocument()
        doc.feed("<div>one<table><tr><td>A</td><td>B</td></tr></table><table><tr><td>C</td></tr></table>end</div>")
        doc.close()
        self.assertEqual(passage_markdown(doc.root), "one\n\n| A | B |\n| --- | --- |\n\n| C |\n| --- |\n\nend")

    def test_missing_table_cell_and_sentence_translation_are_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            data = json.loads(fixture(Path(folder), "N3").read_bytes())
        media = data["content"]["dokkai"]["mondais"][0]["blocks"][0]["mediaItems"][0]
        media["passage"]["jaMd"] = "| A | B |\n| --- | --- |\n| 10 | 20 |"
        data["annotations"]["sentencePairs"][media["id"]] = [
            {"ja": "| A | B |", "vi": "| A | B |"}, {"ja": "| 1020 |", "vi": None}]
        gaps = [g["detail"] for g in coverage(data)[1] if g["targetId"] == media["id"]]
        self.assertIn("JA coverage", gaps)
        self.assertIn("row 2", gaps)

    def test_quote_continuation_and_extra_sentence(self):
        context = []
        sentence_units("「おいしい。", context)
        self.assertEqual(len(sentence_units("栄養もあるんだよ。」と教えてくれた。", context)), 1)
        self.assertEqual(len(sentence_units("食べた。帰った。", context)), 2)

    def test_image_labels_require_an_image_and_a_pure_label(self):
        data = json.loads((ROOT / "contracts/v1/synthetic-draft.json").read_bytes())
        question = data["content"]["choukai"]["mondais"][0]["blocks"][0]["questions"][0]
        choice = question["choices"][0]
        def missing():
            return any(g["field"] == "choiceVi" and g["targetId"] == question["id"] and g["detail"] == choice["id"]
                       for g in coverage(data)[1])
        choice.update(text="ア → イ", textVi=None)
        self.assertTrue(missing())
        question["imageUrl"] = "asset://test"
        self.assertFalse(missing())
        choice["text"] = "アイス"
        self.assertTrue(missing())
