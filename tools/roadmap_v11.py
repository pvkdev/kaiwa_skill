"""Validate and merge the three authorized dialogue pilots into the V10 reader."""
import argparse
import copy
import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "kaiwa_skill/planning/v11"
BASE = ROOT / "kaiwa_skill/planning/v10"
CODES = ("S-011", "T-044", "H-004")
HELPER = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py"))


def read(path):
    return json.loads(path.read_text("utf-8-sig"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    temporary.replace(path)


def build(publish=False):
    payload = read(BASE / "learner.json")
    payload["version"] = "11.0-pilot"
    seen_ids, scripts = set(), set()
    totals = []
    for code in CODES:
        path = OUT / "pilot" / code / "dialogues.json"
        draft = read(path)
        context = HELPER["brief"](code)
        HELPER["validate"](draft, context)
        stage = next(s for s in payload["stages"] if s["uid"] == draft["stage_uid"])
        turns = 0
        for scene, dialogue in zip(stage["situations"], draft["dialogues"]):
            assert scene["uid"] == dialogue["situation_uid"]
            script = tuple("".join(t["ja"].split()) for t in dialogue["turns"])
            assert script not in scripts, "Duplicate dialogue across pilots"
            scripts.add(script)
            for turn in dialogue["turns"]:
                assert turn["id"] not in seen_ids, "Duplicate turn ID"
                seen_ids.add(turn["id"])
            turns += len(dialogue["turns"])
            scene["dialogue"] = copy.deepcopy({k: dialogue[k] for k in
                ("context_vi", "speakers", "turns")})
        totals.append({"code": code, "uid": stage["uid"], "level": stage["level"],
                       "dialogues": len(draft["dialogues"]), "turns": turns,
                       "draft_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    assert sum(t["dialogues"] for t in totals) == 55
    payload["pilot_stages"] = [t["uid"] for t in totals]
    write(OUT / "pilot/learner.json", payload)
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", encoded)
    (OUT / "pilot/ROADMAP.html").write_text(html, encoding="utf8")
    write(OUT / "pilot/BUILD.json", {
        "version": "11.0-pilot", "base": "kaiwa_skill/planning/v10/learner.json",
        "base_sha256": hashlib.sha256((BASE / "learner.json").read_bytes()).hexdigest(),
        "stages": totals, "dialogues": 55, "turns": sum(t["turns"] for t in totals)})
    if publish:
        (ROOT / "docs/index.html").write_text(html, encoding="utf8")
    print(json.dumps(totals, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true")
    build(parser.parse_args().publish)
