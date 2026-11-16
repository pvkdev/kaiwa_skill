"""Read the V10 brief for a topic or validate a full V11 topic draft (read-only)."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from datetime import date

ROOT = Path(__file__).resolve().parents[4]
PLAN = ROOT / "kaiwa_skill/planning"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def brief(code):
    recent = {}
    for line in (PLAN / "v10/KAIWA_CHANG_V10.jsonl").read_text("utf8").splitlines():
        row = json.loads(line)
        level = row["level"]
        if row["stage_kind"] == "speak_japanese":
            recent[level] = row["key"]
        elif row["display_code"] == code:
            result = {k: row[k] for k in ("uid", "display_code", "level", "title", "objective", "events", "situations")}
            result["editorial_context"] = {k: row[k] for k in ("scope_note", "knowledge_focus", "fact_check",
                "related_stage_uids", "source_refs", "source_findings", "edition_notes") if k in row}
            previous = recent.get(level)
            result["previous_specialty"] = previous
            result["previous_items"] = []
            if previous:
                folder = PLAN / "v10/stages" / previous
                result["previous_items"] = [{"id": item["id"], "title": item["title"]}
                                            for item in read(folder / "manifest.json")["items"]]
                result["previous_lesson"] = (folder / "lesson.md").relative_to(ROOT).as_posix()
            return result
    raise ValueError("Unknown V10 topic: " + code)


def require(condition, label):
    if not condition:
        raise ValueError(label)


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def validate(data, ctx):
    require(data["stage_uid"] == ctx["uid"], "stage_uid")
    expected = ctx["situations"]
    require([d["situation_uid"] for d in data["dialogues"]] == [s["uid"] for s in expected],
            "Missing, repeated or reordered V10 situations")
    books = {b["book_id"]: b for b in read(PLAN / "catalog27/manifest.json")["books"]}
    sources = data["admin_sources"]
    for key, src in sources.items():
        require(filled(key) and filled(src["use_vi"]), "Empty source note")
        if src["kind"] == "book":
            book = books[src["book_id"]]
            require(src["title"] == book["title"], key + " book title")
            path = (ROOT / src["path"]).resolve()
            require(path.is_relative_to((ROOT / book["directory"]).resolve()) and path.suffix == ".md", key + " book path")
            lines = path.read_text("utf-8-sig").splitlines()
            require(1 <= src["start_line"] <= src["end_line"] <= len(lines), key + " source range")
        else:
            require(src["kind"] == "web" and filled(src["title"]) and urlsplit(src["url"]).scheme in ("http", "https")
                    and urlsplit(src["url"]).hostname, key + " web source")
            date.fromisoformat(src["accessed"])
    previous = {i["id"] for i in ctx["previous_items"]}
    turn_ids, scripts = set(), set()
    for d, s in zip(data["dialogues"], expected):
        uid = s["uid"]
        require(d["event_id"] == s["event_id"] and filled(d["context_vi"]), uid + " event/context")
        cast = {p["id"]: p for p in d["speakers"]}
        require(len(d["speakers"]) == len(cast) == 2 and all(filled(p["id"]) and filled(p["role_vi"]) and
                p["gender"] in ("male", "female") for p in cast.values()), uid + " cast")
        turns = d["turns"]
        require({t["speaker_id"] for t in turns} == set(cast), uid + " missing or unknown speaker")
        admin = d["admin"]
        require(set(admin["source_refs"]) <= sources.keys() and set(admin["specialty_item_ids"]) <= previous,
                uid + " invalid source/specialty reference")
        require(set(admin["turn_origins"]) == {t["id"] for t in turns}, uid + " missing turn origin")
        for t in turns:
            tid = t["id"]
            require(filled(tid) and tid not in turn_ids and filled(t["ja"]) and filled(t["vi"])
                    and t["ja"] != t["vi"], uid + " turn ID or language fields")
            require(re.search(r"[ぁ-ヿ一-鿿]", t["ja"]) and "<ruby" not in t["ja"].lower(), tid + " Japanese text")
            turn_ids.add(tid)
            origin = admin["turn_origins"][tid]
            require(origin["kind"] in ("source_quote", "source_adaptation", "original_extension"), tid + " origin")
            if origin["kind"] != "original_extension":
                ref = origin["source_ref"]
                require(ref in admin["source_refs"] and sources[ref]["kind"] == "book", tid + " book attribution")
                if origin["kind"] == "source_quote":
                    src = sources[ref]
                    excerpt = (ROOT / src["path"]).read_text("utf-8-sig").splitlines()[src["start_line"]-1:src["end_line"]]
                    require(t["ja"] in "\n".join(excerpt), tid + " quote not found")
                else:
                    require(filled(origin["change_vi"]), tid + " adaptation note")
        script = tuple("".join(t["ja"].split()) for t in turns)
        require(script not in scripts, uid + " duplicate dialogue")
        scripts.add(script)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topic")
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    ctx = brief(args.topic)
    if args.check:
        validate(read(args.check), ctx)
        print("OK", args.topic, len(ctx["situations"]))
    else:
        print(json.dumps(ctx, ensure_ascii=False, indent=2))
