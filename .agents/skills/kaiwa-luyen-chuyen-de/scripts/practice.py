"""Read one V9.2 specialty and its following topics, or check a V10 practice file."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
BASE = ROOT / "kaiwa_skill/planning/v9_2"


def read(path):
    return json.loads(path.read_text("utf8"))


def context(code, extra_codes=()):
    stages = read(BASE / "learner.json")["stages"]
    index = next(i for i, s in enumerate(stages) if s["code"] == code and s["stage_kind"] == "speak_japanese")
    stage = stages[index]
    folder = BASE / "stages" / code
    manifest = read(folder / "manifest.json")
    topics = []
    nearby = True
    found = set()
    for topic in stages[index + 1:]:
        if topic["level"] != stage["level"]:
            break
        if topic["stage_kind"] != "topic":
            nearby = False
            continue
        if topic["code"] in extra_codes:
            found.add(topic["code"])
        elif not nearby:
            continue
        topics.append({k: topic[k] for k in ("uid", "code", "title", "objective", "events", "situations")})
    if found != set(extra_codes):
        raise ValueError("Extended topics must follow this specialty in the same level")
    return {"stage_uid": stage["uid"], "code": code, "level": stage["level"], "title": stage["title"],
            "items": [s["id"] for s in stage["selections"]],
            "bundle": folder.relative_to(ROOT).as_posix(),
            "prior_applications": read(ROOT / manifest["source_admin"])["decision"]["applications"],
            "following_topics": topics}


def check(data, ctx):
    def require(condition, message):
        if not condition:
            raise ValueError(message)

    require(data["stage_uid"] == ctx["stage_uid"], "Wrong specialty UID")
    require([i["item_id"] for i in data["items"]] == ctx["items"], "Missing or reordered selections")
    scenes = {(t["uid"], s["uid"]) for t in ctx["following_topics"] for s in t["situations"]}
    ids, scripts = set(), set()
    for item in data["items"]:
        require(item["practice"], "Empty practice for " + item["item_id"])
        for ex in item["practice"]:
            eid = ex["id"]
            require(isinstance(eid, str) and eid.startswith(item["item_id"] + "-ex") and eid not in ids, eid)
            ids.add(eid)
            require(ex["authorship"] == "ai_authored", eid + " authorship")
            require((ex["topic_uid"], ex["situation_uid"]) in scenes, eid + " situation outside following topics")
            require(ex["context_vi"].strip(), eid + " missing setting")
            speakers = {s["id"]: s for s in ex["speakers"]}
            turns = ex["turns"]
            require(len(speakers) == len(ex["speakers"]) and all(
                s["role_vi"].strip() and s["gender"] in ("male", "female") for s in speakers.values()), eid + " cast")
            require({t["speaker_id"] for t in turns} == set(speakers), eid + " speaker references")
            if ex["type"] == "single_sentence":
                require(len(turns) == len(speakers) == 1, eid + " single")
            else:
                require(ex["type"] == "dialogue" and len(speakers) == 2 and len(turns) >= 2, eid + " dialogue")
            require(all(t["ja"].strip() and t["vi"].strip() for t in turns), eid + " missing text")
            script = tuple("".join(t["ja"].split()) for t in turns)
            require(script not in scripts, eid + " duplicate script")
            scripts.add(script)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code")
    parser.add_argument("--check", type=Path)
    parser.add_argument("--extra-topic", action="append", default=[])
    args = parser.parse_args()
    data = read(args.check) if args.check else None
    ctx = context(args.code, data.get("extra_topic_reasons", {}).keys() if data is not None else args.extra_topic)
    if args.check:
        check(data, ctx)
        print("OK", args.code)
    else:
        print(json.dumps(ctx, ensure_ascii=False, indent=2))
