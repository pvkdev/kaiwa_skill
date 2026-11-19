"""Publish reviewed V12 vocabulary over the V11 roadmap for local or Pages preview."""
import argparse
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "kaiwa_skill/planning/v12"
PILOT = PLAN / "pilot"
STAGES = PLAN / "stages"
VOCAB = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-vocabulary/scripts/vocab.py"))
CODES = ("S-011", "S-024", "T-044", "T-008", "H-004", "H-020")


def write(path, text):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(text, encoding="utf8")
    temp.replace(path)


def build(bulk=False, require_complete=False):
    raw_course = VOCAB["LEARNER"].read_bytes()
    course = json.loads(raw_course.decode("utf-8-sig"))
    learner_hash = VOCAB["sha"](raw_course.replace(b"\r\n", b"\n"))
    stages = {stage["code"]: stage for stage in course["stages"]}
    topics = [code for code, stage in stages.items() if stage["stage_kind"] == "topic"]
    packages = {}
    pending = []
    for code in topics if bulk else CODES:
        stage = stages[code]
        folder = (STAGES if bulk else PILOT) / code
        context = VOCAB["stage_brief"](stage, course, learner_hash)
        try:
            draft, _ = VOCAB["reviewed_draft"](folder / "vocabulary.json", context)
        except (FileNotFoundError, ValueError) as exc:
            if not bulk:
                raise
            pending.append(code)
            if (folder / "status.json").exists():
                print("Pending", code, str(exc))
            continue
        package = VOCAB["export"](draft)
        stage["vocabulary_nodes"] = package["nodes"]
        stage["vocabulary_glosses"] = {}
        for node, group in zip(package["nodes"], draft["groups"], strict=True):
            glosses = {}
            for term in group["terms"]:
                glosses.setdefault(term["ja"], []).append({"reading": term["reading"], "han_viet": term["han_viet"], "vi": term["vi"]})
            stage["vocabulary_glosses"][node["id"]] = glosses
        packages[code] = (folder, package)
    if require_complete and pending:
        raise ValueError(f"{len(pending)} topic stages still pending: " + ", ".join(pending))
    course["version"] = ("12.0-progress" if pending else "12.0") if bulk else "12.0-pilot"
    course["pilot_stages"] = [stages[code]["uid"] for code in CODES]
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    embedded = json.dumps(course, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", embedded)
    for folder, package in packages.values():
        write(folder / "exchange.json", json.dumps(package, ensure_ascii=False, indent=2) + "\n")
    write((PLAN if bulk else PILOT) / "ROADMAP.html", html)
    print(f"Published vocabulary for {len(packages)}/{len(topics)} topic stages")
    write(ROOT / "docs/index.html", html)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bulk", action="store_true", help="publish reviewed stages from the V12 stages directory")
    parser.add_argument("--require-complete", action="store_true", help="fail if any V12 topic stage is pending")
    args = parser.parse_args()
    build(bulk=args.bulk or args.require_complete, require_complete=args.require_complete)
