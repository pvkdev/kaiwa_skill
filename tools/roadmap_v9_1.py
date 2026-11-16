"""Apply the five editorial changes to the released V9 data and render V9.1."""
import argparse
import hashlib
import json
import uuid
from collections import Counter
from pathlib import Path

from roadmap_v9 import P, ROOT, old, write

BASE = P / "v9"
OUT = P / "v9_1"


def stable_id(key):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "kaiwa/v9.1/" + key))


def apply_content(row, edit):
    row.update(title=edit["title"], objective=edit["objective"])
    data = row["v6"]
    vocabulary = data["decision"]["vocabulary_topics"]
    vocabulary.extend(edit["vocabulary"])
    for event in edit["events"]:
        eid = f"E{len(row['events']) + 1:02}"
        row["events"].append({"id": eid, "name": event["name"], "roles": event["roles"]})
        for scene in event["situations"]:
            sid = f"S{len(row['situations']) + 1:03}"
            assert scene["branch"] in old.BRANCH
            row["situations"].append(dict(scene, id=sid, uid=stable_id(row["uid"] + "/" + sid),
                                          origin="ai_authored", level=row["level"], event_id=eid))
    for node in data["learning_order"]:
        if node["type"] == "v5_situations":
            node["situation_ids"] = [s["id"] for s in row["situations"]]
        elif node["type"] == "vocabulary_topics":
            node["topics"] = vocabulary
    row["edition_notes"] = {"version": "9.1", "editorial_file": "edits/" + row["display_code"] + ".json",
                            "context_sources": edit.get("sources", []), "scenario_authorship": "ai_authored"}


def new_topic(code, edit, anchor):
    uid = stable_id(code)
    row = {k: anchor[k] for k in ("level", "track", "cluster_id", "cluster_title", "cluster_order")}
    row.update(uid=uid, display_code=code, key="V91-" + code, stage_kind="topic",
               scope_note=edit["scope"], knowledge_focus=edit["vocabulary"], learner_access="open",
               recommended_previous_stage_uids=[anchor["uid"]], fact_check=True, authorship="ai_authored",
               roadmap_status="authored", lesson_status="not_authored", events=[], situations=[])
    row["v6"] = {"version": "9.1", "decision": {"stage_uid": uid, "display_code": code,
                 "vocabulary_topics": [], "selections": []}, "shadowing": None, "learning_order": [
                     {"type": "vocabulary_topics"}, {"type": "stage_lecture", "video_status": "placeholder"},
                     {"type": "v5_situations"}, {"type": "live_challenges", "status": "deferred"},
                     {"type": "free_kaiwa", "status": "planned"}]}
    apply_content(row, edit)
    return row


def build(publish=False):
    rows = old.rows(BASE / "KAIWA_CHANG_V9.jsonl")
    payload = old.read(BASE / "learner.json")
    learners = {s["uid"]: s for s in payload["stages"]}
    edits = {p.stem: old.read(p) for p in sorted((OUT / "edits").glob("*.json"))}
    for code, edit in edits.items():
        if edit.get("extend"):
            row = next(r for r in rows if r.get("display_code") == code)
            apply_content(row, edit)
        else:
            index = next(i for i, r in enumerate(rows) if r.get("display_code") == edit["after"])
            row = new_topic(code, edit, rows[index])
            rows.insert(index + 1, row)
            learners[row["uid"]] = {"uid": row["uid"], "code": code, "level": row["level"],
                                    "cluster": row["cluster_title"], "cluster_id": row["cluster_id"],
                                    "stage_kind": "topic", "shadowing": None, "selections": []}
        learners[row["uid"]].update(title=row["title"], objective=row["objective"], events=row["events"],
                                    situations=row["situations"], order=row["v6"]["learning_order"],
                                    vocabulary=row["v6"]["decision"]["vocabulary_topics"])
    numbers, topic_numbers, registry = Counter(), Counter(), {}
    for index, row in enumerate(rows, 1):
        level = row["level"]
        numbers[level] += 1
        row["roadmap_order"] = numbers[level]
        learner = learners[row["uid"]]
        learner["number"] = numbers[level]
        if row["stage_kind"] == "topic":
            topic_numbers[level] += 1
            row["level_order"] = topic_numbers[level]
            row["order"] = sum(topic_numbers.values())
        registry[row["uid"]] = {"display_code": learner["code"], "level": level, "title": learner["title"],
                                "cluster_id": learner["cluster_id"], "stage_kind": row["stage_kind"],
                                "order": index, "stage_key": row["key"], "status": "active"}
    entries = [learners[r["uid"]] for r in rows]
    assert len(rows) == len(registry) == 365 and list(numbers.values()) == [99, 184, 82]
    payload.update(version="9.1", stages=entries)
    write(OUT / "learner.json", payload)
    write(OUT / "chang_registry.json", registry)
    target = OUT / "KAIWA_CHANG_V9_1.jsonl"
    target.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf8")
    write(OUT / "SOURCE_POLICY.json", dict(old.read(BASE / "SOURCE_POLICY.json"), version="9.1",
          basis="../v9/KAIWA_CHANG_V9.jsonl", specialty_provenance="../v9/admin"))
    status = old.read(BASE / "STATUS.json")
    status.update(version="9.1", levels=numbers, topic_stages=sum(topic_numbers.values()),
                  specialty_stages=len(rows) - sum(topic_numbers.values()), total_stages=len(rows),
                  basis_sha256=hashlib.sha256((BASE / "KAIWA_CHANG_V9.jsonl").read_bytes()).hexdigest(),
                  situations=sum(len(s["situations"]) for s in entries),
                  added_situations={code: sum(len(e["situations"]) for e in edit["events"])
                                    for code, edit in edits.items()})
    write(OUT / "STATUS.json", status)
    for level, name in zip(numbers, ("SO_CAP.md", "TRUNG_CAP.md", "THUONG_CAP.md")):
        lines = ["# " + level]
        for s in entries:
            if s["level"] == level:
                lines.extend(["", f"## {s['number']}. {s['title']}", "", s["objective"], ""])
                lines.extend("- " + x["title"] for x in s["selections"] + s["situations"])
        (OUT / name).write_text("\n".join(lines).rstrip()+"\n", encoding="utf8")
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    html = template.replace("__COURSE_DATA__", json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c"))
    (OUT / "ROADMAP.html").write_text(html, encoding="utf8")
    if publish:
        (ROOT / "docs/index.html").write_text(html, encoding="utf8")
        pointer = {"version": "9.1"}
        for field, file in (("registry", "chang_registry.json"), ("roadmap", target.name), ("policy", "SOURCE_POLICY.json")):
            pointer[field] = (OUT / file).relative_to(ROOT).as_posix()
        write(P / "CURRENT_ROADMAP.json", pointer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    build(parser.parse_args().publish)
