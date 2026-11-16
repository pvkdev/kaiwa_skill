"""Print a private review worksheet or verify its coverage against the current draft."""
import argparse
import hashlib
import json
import runpy
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
ROOT = SKILL.parents[2]
V11 = ROOT / "kaiwa_skill/planning/v11"
AUTHOR = runpy.run_path(str(SKILL.parent / "kaiwa-topic-dialogue/scripts/dialogue.py"))
read = AUTHOR["read"]


def digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf8")).hexdigest()


def snapshot(code):
    ctx = AUTHOR["brief"](code)
    paths = [p for folder in ("stages", "pilot")
             if (p := V11 / folder / code / "dialogues.json").is_file()]
    if len(paths) != 1:
        raise ValueError(f"{code}: expected one authored stage, found {len(paths)}")
    draft = read(paths[0])
    AUTHOR["validate"](draft, ctx)
    stage = {k: ctx[k] for k in ("uid", "level", "title", "objective", "editorial_context")}
    events = {e["id"]: e for e in ctx["events"]}
    files = {}
    sources = {}
    for key, ref in draft["admin_sources"].items():
        excerpt = None
        if ref["kind"] == "book":
            path = ROOT / ref["path"]
            if path not in files:
                files[path] = path.read_text("utf-8-sig").splitlines()
            excerpt = files[path][ref["start_line"] - 1:ref["end_line"]]
        sources[key] = digest([ref, excerpt])

    scenes = {}
    by_id = {}
    for brief, scene in zip(ctx["situations"], draft["dialogues"]):
        uid = brief["uid"]
        used_sources = {k: sources[k] for k in scene["admin"]["source_refs"]}
        stamp = digest([stage, events[brief["event_id"]], brief, scene, used_sources])
        scenes[uid] = {"hash": stamp, "result": "pending", "turn_id": "", "note_vi": ""}
        by_id[brief["id"]] = stamp

    branches = {}
    for eid, event in events.items():
        members = [s for s in ctx["situations"] if s["event_id"] == eid]
        if members:
            edges = [[by_id[s["id"]], [by_id[p] for p in s.get("continues_from", [])]]
                     for s in members]
            branches[eid] = {"hash": digest([event, edges]), "result": "pending", "note_vi": ""}
    return ({"stage_uid": ctx["uid"], "reviewer": "", "scenes": scenes, "events": branches},
            {s["situation_uid"]: {t["id"] for t in s["turns"]} for s in draft["dialogues"]})


def issues(actual, expected, turns):
    if actual.get("stage_uid") != expected["stage_uid"]:
        yield "wrong stage"
    if not str(actual.get("reviewer") or "").strip():
        yield "missing reviewer"
    for group in ("scenes", "events"):
        recorded = actual.get(group, {})
        for key in recorded.keys() - expected[group].keys():
            yield f"{group}/{key}: outside brief"
        for key, current in expected[group].items():
            row = recorded.get(key, {})
            allowed = ("kept", "fixed") if group == "scenes" else ("read",)
            if row.get("hash") != current["hash"]:
                yield f"{group}/{key}: missing or stale"
            elif row.get("result") not in allowed or not str(row.get("note_vi") or "").strip():
                yield f"{group}/{key}: open or missing evidence"
            elif group == "scenes" and row.get("turn_id") not in turns[key]:
                yield f"scenes/{key}: cite an existing turn"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code")
    parser.add_argument("--check", type=Path, metavar="REVIEW_JSON")
    args = parser.parse_args()
    expected, turns = snapshot(args.code)
    if args.check is None:
        print(json.dumps(expected, ensure_ascii=False, indent=2))
        return 0
    errors = list(issues(read(args.check), expected, turns))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{args.code}: review evidence current for {len(turns)} scenes and "
          f"{len(expected['events'])} events")
    return 0


if __name__ == "__main__":
    sys.exit(main())
