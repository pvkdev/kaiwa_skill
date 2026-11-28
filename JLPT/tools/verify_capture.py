"""Compare a candidate package back to the immutable SingleFile question sheets."""
import argparse
import base64
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

from convert_singlefile import ROOT, SingleFileDocument, first, ja, passage_markdown, tidy
from audit_sources import ANSWER, appendix_answers, source_explanation
from validate_package import source_snapshot


def verify(package, root):
    nodes = {n["nodeId"]: n for n in package["annotations"]["nodes"]}
    source_answers = {a["questionId"]: a for a in package["annotations"]["answers"]}
    fields = {}
    for field in package["annotations"]["fields"]:
        if field["fieldPointer"] == "/explanation":
            fields.setdefault(field["targetId"], []).append(field)
    counts = Counter()

    def same(expected, actual, field):
        if expected != actual:
            raise ValueError(f"{source['localPath']} {field}: package differs from source")

    for source in package["sources"]:
        part = source["sourceId"]
        if part not in ("listening", "written"):
            continue
        raw = source_snapshot(root, source).read_bytes()
        same(source["sha256"], sha256(raw).hexdigest(), "SHA-256")
        document = SingleFileDocument()
        document.feed(raw.decode("utf-8-sig"))
        document.close()
        compiled = [(q, b) for section, tab in package["content"].items()
                    if (section == "choukai") == (part == "listening")
                    for m in tab["mondais"] for b in m["blocks"] for q in b["questions"]]
        originals = document.root.find("q-item")
        same(len(originals), len(compiled), "question count")
        appendix = appendix_answers(document.root)
        materials = {}
        previous = []
        for element in document.root.find("mondai-block"):
            group = element.find("q-item")
            if group:
                texts = [passage_markdown(p) for p in element.find("passage-content")]
                texts.extend(passage_markdown(p) for p in element.find("vnjp-dokkai-thongtindich")
                             if p in element.children)
                for q in group:
                    materials[q.attrs["id"]] = [p for p in texts if p]
                previous = [q.attrs["id"] for q in group]
            elif extra := first(element, "vnjp-dokkai-thongtindich"):
                for anchor in previous:
                    materials[anchor].append(passage_markdown(extra))
        for original, (question, block) in zip(originals, compiled, strict=True):
            locator = "#" + original.attrs["id"]
            identity = nodes[question["id"]]
            same((part, locator, first(original, "q-no").text()),
                 (identity["sourceId"], identity["locator"], identity["sourceNumber"]), locator + "/order")
            same(tidy(ja(first(original, "vnjp-quiz-q"))), question["prompt"]["text"], locator + "/prompt")
            same(materials[original.attrs["id"]],
                 [i["passage"]["jaMd"] for i in block["mediaItems"] if i["kind"] == "passage"], locator + "/passages")
            choices = original.find("choice")
            same([tidy(ja(first(c, "choice-text"))) for c in choices],
                 [c["text"] for c in question["choices"]], locator + "/choices")
            explanation, _ = source_explanation(original, appendix)
            origins = fields.get(question["id"], [])
            if explanation:
                same(explanation, question["explanation"], locator + "/explanation")
                same([("source", part)], [(f["origin"], f["sourceId"]) for f in origins], locator + "/explanation/origin")
                counts["sourceExplanations"] += 1
            elif question["explanation"]:
                same(True, len(origins) == 1 and origins[0]["origin"] in {"ai", "human"}, locator + "/explanation/origin")
                counts["authoredExplanations"] += 1
            answer = source_answers[question["id"]]
            if answer["resolution"] == "source_confirmed":
                same([chr(97 + i) for i, c in enumerate(choices) if "choice-correct" in c.classes],
                     [question["correctChoiceId"]], locator + "/key")
                same([int(match[1]) for line in original.find("result-line") for match in ANSWER.finditer(line.text())],
                     [ord(question["correctChoiceId"]) - 96], locator + "/gradedKey")
            images = [n for wrapper in original.find("vnjp-q-image") for n in wrapper.walk() if n.tag == "img"]
            hashes = ["asset://" + sha256(base64.b64decode(n.attrs["src"].split(",", 1)[1], validate=True)).hexdigest()
                      for n in images]
            same(hashes, [question["imageUrl"]] if question.get("imageUrl") else [], locator + "/image")
            script = tidy(ja(first(original, "vnjp-choukai-script-inner")))
            if script:
                candidates = [(question.get("jlptListenScript") or {}).get("scriptJaMd")]
                candidates += [i["audio"]["scriptJaMd"] for i in block["mediaItems"] if i["kind"] == "audio"]
                same(True, script in candidates, locator + "/script")
                counts["sourceScripts"] += 1
            counts[part] += 1
            counts["choiceTexts"] += len(choices)
            counts["questionImages"] += len(images)
    return dict(counts)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("package", type=Path)
    cli.add_argument("--root", type=Path, default=ROOT)
    args = cli.parse_args()
    try:
        print(json.dumps(verify(json.loads(args.package.read_bytes()), args.root.resolve()), indent=2))
    except (OSError, ValueError, KeyError) as exc:
        sys.exit(str(exc))
