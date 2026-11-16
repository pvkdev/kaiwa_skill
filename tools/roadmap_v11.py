"""Validate and merge authorized V11 dialogue drafts into the V10 reader."""
import argparse
import copy
import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "kaiwa_skill/planning/v11"
BASE = ROOT / "kaiwa_skill/planning/v10"
CODES = ("S-011", "T-044", "H-004", "S-021", "T-027", "H-020", "S-035", "T-008", "H-047")
HELPER = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py"))


def read(path):
    return json.loads(path.read_text("utf-8-sig"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    temporary.replace(path)


def build(publish=False, batch=None):
    payload = read(BASE / "learner.json")
    destination = OUT / "pilot"
    inputs = [(code, OUT / "pilot" / code / "dialogues.json") for code in CODES]
    if batch:
        plan_path = OUT / "batches" / batch / "PLAN.json"
        plan = read(plan_path)
        base_hash = hashlib.sha256((BASE / "KAIWA_CHANG_V10.jsonl").read_bytes()).hexdigest()
        previous_names = plan.get("previous_batches", [])
        if len(previous_names) != len(set(previous_names)) or batch in previous_names:
            raise ValueError("Repeated batch in cumulative build")
        plans = [read(OUT / "batches" / name / "PLAN.json") for name in previous_names]
        if any(previous["state"] != "production_complete" for previous in plans):
            raise ValueError("Previous batch production is incomplete")
        plans.append(plan)
        if any(assigned_plan["base_sha256"] != base_hash for assigned_plan in plans):
            raise ValueError("V10 changed since batch assignment")
        assigned = [stage for assigned_plan in plans
                    for stages in assigned_plan["levels"].values() for stage in stages]
        codes = [stage["code"] for stage in assigned]
        if len(codes) != len(set(codes)) or set(codes).intersection(CODES):
            raise ValueError("Repeated batch assignment or overlap with existing pilots")
        inputs.extend((code, OUT / "stages" / code / "dialogues.json") for code in codes)
        destination = OUT
    payload["version"] = "11.0-" + (batch or "pilot")
    seen_ids, scripts = set(), set()
    totals = []
    expected_dialogues = 0
    for code, path in inputs:
        draft = read(path)
        context = HELPER["brief"](code)
        expected_dialogues += len(context["situations"])
        HELPER["validate"](draft, context)
        stage = next(s for s in payload["stages"] if s["uid"] == draft["stage_uid"])
        turns = 0
        for scene, dialogue in zip(stage["situations"], draft["dialogues"]):
            assert scene["uid"] == dialogue["situation_uid"]
            script = tuple("".join(t["ja"].split()) for t in dialogue["turns"])
            assert script not in scripts, "Duplicate dialogue across V11 stages: " + code
            scripts.add(script)
            for turn in dialogue["turns"]:
                assert turn["id"] not in seen_ids, "Duplicate turn ID"
                seen_ids.add(turn["id"])
            turns += len(dialogue["turns"])
            scene["dialogue"] = copy.deepcopy({k: dialogue[k] for k in
                ("context_vi", "speakers", "turns")})
        totals.append({"code": code, "uid": stage["uid"], "level": stage["level"],
                       "dialogues": len(draft["dialogues"]), "turns": turns,
                       **({"draft_path": path.relative_to(ROOT).as_posix(),
                           "independent_review": "pending" if code not in CODES else "completed"}
                          if batch else {}),
                       "draft_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    assert sum(t["dialogues"] for t in totals) == expected_dialogues
    payload["pilot_stages"] = [t["uid"] for t in totals if t["code"] in CODES]
    write(destination / "learner.json", payload)
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", encoded)
    (destination / "ROADMAP.html").write_text(html, encoding="utf8")
    write(destination / "BUILD.json", {
        "version": payload["version"], "base": "kaiwa_skill/planning/v10/learner.json",
        "base_sha256": hashlib.sha256((BASE / "learner.json").read_bytes()).hexdigest(),
        "stages": totals, "dialogues": expected_dialogues,
        "turns": sum(t["turns"] for t in totals)})
    if publish:
        (ROOT / "docs/index.html").write_text(html, encoding="utf8")
    print(json.dumps(totals, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--batch", choices=("batch01", "batch02"))
    args = parser.parse_args()
    build(args.publish, args.batch)
