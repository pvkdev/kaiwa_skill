"""Publish the reviewed V12.0 vocabulary pilots over the V11 roadmap for local or Pages preview."""
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "kaiwa_skill/planning/v12/pilot"
VOCAB = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-vocabulary/scripts/vocab.py"))
CODES = ("S-011", "S-024", "T-044", "T-008", "H-004", "H-020")


def write(path, text):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(text, encoding="utf8")
    temp.replace(path)


def build():
    course = VOCAB["read"](VOCAB["LEARNER"])
    stages = {stage["code"]: stage for stage in course["stages"]}
    packages = {}
    for code in CODES:
        context = VOCAB["brief"](code)
        draft, _ = VOCAB["reviewed_draft"](PILOT / code / "vocabulary.json", context)
        package = VOCAB["export"](draft)
        stage = stages[code]
        stage["vocabulary_nodes"] = package["nodes"]
        stage["vocabulary_glosses"] = {}
        for node, group in zip(package["nodes"], draft["groups"], strict=True):
            glosses = {}
            for term in group["terms"]:
                glosses.setdefault(term["ja"], []).append({"reading": term["reading"], "han_viet": term["han_viet"], "vi": term["vi"]})
            stage["vocabulary_glosses"][node["id"]] = glosses
        packages[code] = package
    course["version"] = "12.0-pilot"
    course["pilot_stages"] = [stages[code]["uid"] for code in CODES]
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    embedded = json.dumps(course, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", embedded)
    for code, package in packages.items():
        write(PILOT / code / "exchange.json", json.dumps(package, ensure_ascii=False, indent=2) + "\n")
    write(PILOT / "ROADMAP.html", html)
    write(ROOT / "docs/index.html", html)


if __name__ == "__main__":
    build()
