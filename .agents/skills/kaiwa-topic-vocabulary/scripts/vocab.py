"""Brief a V11 topic stage, then check or export its V12 vocabulary draft (read-only on inputs)."""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[4]
PLAN = ROOT / "kaiwa_skill/planning"
LEARNER = PLAN / "v11/learner.json"
KNOWLEDGE = ROOT / "kaiwa_skill/knowledge"
LEVELS = ["N5", "N4", "N3", "N2", "N1"]
BANDS = {"Sơ": ("N5", "N4"), "Trung": ("N3", "N2"), "Thượng": ("N2", "N1")}
POS = {"noun", "verb", "i_adj", "na_adj", "adverb", "expression", "counter", "other"}
VOCAB_BOOKS = {"VOCAB-N3": ("MIMIKARA N3", "N3"), "VOCAB-N2": ("MINATO", "N2"), "VOCAB-N1": ("MIMIKARA N1", "N1")}
JAPANESE = re.compile(r"[ぁ-ゖァ-ヺ一-鿿々〆ヵヶ]")
KANA_ONLY = re.compile(r"^[ぁ-ゖァ-ヺー・ゝゞヽヾ]+$")
VERB_END = tuple("うくぐすつぬぶむる")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def group_hash(group):
    return sha(json.dumps(group, ensure_ascii=False, sort_keys=True).encode("utf8"))


def filled(value):
    return isinstance(value, str) and bool(value.strip())


def nfc(text):
    return unicodedata.normalize("NFC", text)


def vocab_folder(marker):
    for folder in KNOWLEDGE.iterdir():
        if folder.is_dir() and marker in nfc(folder.name).upper():
            return folder
    return None


def stage_row(code):
    raw = LEARNER.read_bytes()
    course = json.loads(raw.decode("utf-8-sig"))
    for stage in course["stages"]:
        if stage["code"] == code:
            if stage.get("stage_kind") != "topic":
                raise ValueError(code + " is not a topic stage; specialty stages have no vocabulary node")
            return stage, course, sha(raw)
    raise ValueError("Unknown V11 stage: " + code)


def brief(code):
    stage, course, learner_hash = stage_row(code)
    low, high = BANDS[stage["level"]]
    situations, utterances = [], {}
    for scene in stage["situations"]:
        dialogue = scene.get("dialogue") or {"speakers": [], "turns": []}
        cast = {s["id"]: s["role_vi"] + " (" + s["gender"] + ")" for s in dialogue["speakers"]}
        turns = [{"id": t["id"], "speaker": cast.get(t["speaker_id"], t["speaker_id"]), "ja": t["ja"], "vi": t["vi"]}
                 for t in dialogue["turns"]]
        for t in turns:
            utterances[t["id"]] = t["ja"]
        situations.append({"id": scene["id"], "event_id": scene["event_id"], "title": scene["title"],
                           "branch": course["branches"].get(scene["branch"], scene["branch"]),
                           "context_vi": dialogue.get("context_vi", ""), "turns": turns})
    shadowing = [{"id": item["id"], "type": item["type"],
                  "turns": [{"ja": t["ja"], "vi": t["vi"]} for t in item["turns"]]}
                 for item in (stage.get("shadowing") or {}).get("items", [])]
    return {
        "uid": stage["uid"], "code": code, "level": stage["level"],
        "level_band": low + "–" + high, "level_ceiling": high,
        "title": stage["title"], "cluster": stage["cluster"], "objective": stage["objective"],
        "vocabulary_topics": stage["vocabulary"],
        "events": [{"id": e["id"], "name": e["name"], "roles": e["roles"]} for e in stage["events"]],
        "situations": situations, "shadowing": shadowing,
        "learner_path": LEARNER.relative_to(ROOT).as_posix(), "learner_sha256": learner_hash,
        "_utterances": utterances,
        "_shadowing": {item["id"]: "\n".join(t["ja"] for t in item["turns"]) for item in shadowing},
    }


def level_index():
    """Map headwords from the cleaned Mimikara/Minato tables to their book level (editorial hint only)."""
    index = {}
    for marker, level in VOCAB_BOOKS.values():
        folder = vocab_folder(marker)
        if not folder:
            continue
        for path in sorted((folder / "chapters").glob("*.md")):
            columns = None
            for line in path.read_text("utf-8-sig").splitlines():
                if not line.startswith("|"):
                    columns = None
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if cells and cells[0].upper() == "STT":
                    columns = [c.lower() for c in cells]
                    continue
                if not columns or set(line) <= set("|-: "):
                    continue
                words = set()
                for name, cell in zip(columns, cells):
                    if not cell:
                        continue
                    if "kanji" in name or name == "từ":
                        words.add(cell)
                    elif "hiragana" in name:
                        words.add(cell)
                        if len(cell) > 2 and cell[0] in "がをにでと":
                            words.add(cell[1:])
                for word in words:
                    index.setdefault(nfc(word), set()).add(level)
    return index


def check(data, ctx):
    errors, notes = [], []

    def need(condition, label):
        if not condition:
            errors.append(label)
        return condition

    need(data.get("stage_uid") == ctx["uid"], "stage_uid does not match " + ctx["code"])
    need(data.get("stage_code") == ctx["code"], "stage_code does not match")
    topics = ctx["vocabulary_topics"]
    ceiling = LEVELS.index(ctx["level_ceiling"])
    floor = LEVELS.index(ctx["level_band"].split("–")[0])

    sources = data.get("admin_sources", {})
    books = {b["book_id"]: b for b in read(PLAN / "catalog27/manifest.json")["books"]}
    for key, src in sources.items():
        if not need(filled(key) and isinstance(src, dict) and filled(src.get("use_vi")), "source " + str(key) + " use_vi"):
            continue
        if src.get("kind") == "book":
            book_id = src.get("book_id")
            if book_id in VOCAB_BOOKS:
                folder = vocab_folder(VOCAB_BOOKS[book_id][0])
            elif need(book_id in books, key + " unknown book_id"):
                folder = ROOT / books[book_id]["directory"]
                need(src.get("title", books[book_id]["title"]) == books[book_id]["title"], key + " book title")
            else:
                continue
            path = (ROOT / src.get("path", "")).resolve()
            if need(folder is not None and path.is_file() and path.suffix == ".md"
                    and path.is_relative_to(folder.resolve()), key + " book path"):
                lines = path.read_text("utf-8-sig").splitlines()
                need(isinstance(src.get("start_line"), int) and isinstance(src.get("end_line"), int)
                     and 1 <= src["start_line"] <= src["end_line"] <= len(lines), key + " line range")
        elif need(src.get("kind") == "web", key + " kind must be book or web"):
            url = urlsplit(src.get("url", ""))
            need(filled(src.get("title")) and url.scheme in ("http", "https") and url.hostname, key + " web source")
            try:
                date.fromisoformat(src.get("accessed", ""))
            except ValueError:
                errors.append(key + " accessed date")

    dropped = data.get("dropped_topics", {})
    for topic, reason in dropped.items():
        need(topic in topics and filled(reason), "dropped_topics: " + topic)
    groups = data.get("groups")
    if not need(isinstance(groups, list) and groups, "groups must be a non-empty array"):
        return errors, notes
    covered = {g.get("v10_topic") for g in groups}
    missing = [t for t in topics if t not in covered and t not in dropped]
    need(not missing, "V10 topics not covered or dropped: " + "; ".join(missing))

    index = level_index()
    group_ids, term_ids, pairs = set(), set(), set()
    total = below = from_dialogue = 0
    for group in groups:
        gid = group.get("id")
        need(filled(gid) and gid not in group_ids, "group id " + str(gid))
        group_ids.add(gid)
        need(filled(group.get("title_vi")), gid + " title_vi")
        topic = group.get("v10_topic")
        if topic is None:
            need(filled(group.get("added_reason_vi")), gid + " added group needs added_reason_vi")
        else:
            need(topic in topics, gid + " v10_topic is not a V10 topic of this stage")
        terms = group.get("terms") or []
        need(terms, gid + " has no terms")
        if terms and not 8 <= len(terms) <= 25:
            notes.append(f"{gid} has {len(terms)} terms (guide 8–25)")
        for term in terms:
            tid = term.get("id")
            label = f"{gid}/{tid}"
            need(filled(tid) and tid not in term_ids, label + " id missing or repeated")
            term_ids.add(tid)
            ja, reading = term.get("ja", ""), term.get("reading", "")
            need(filled(ja) and JAPANESE.search(ja) and not re.search(r"\s", ja)
                 and not ja.endswith(("。", "？", "！", "?", "!")), label + " ja")
            need(filled(reading) and KANA_ONLY.match(reading), label + " reading must be kana only")
            need(filled(term.get("vi")) and re.search(r"[A-Za-zÀ-ỹ]", term.get("vi", "")), label + " vi")
            pos = term.get("pos")
            if need(pos in POS, label + " pos"):
                if pos == "verb":
                    need(ja.endswith(VERB_END) and not ja.endswith(("ます", "ません", "ました")),
                         label + " verb must be in dictionary form")
                if pos == "i_adj":
                    need(ja.endswith("い"), label + " i_adj must be in basic form")
                if pos == "na_adj":
                    need(not ja.endswith(("な", "だ")), label + " na_adj without な/だ")
            pair = (ja, reading)
            need(pair not in pairs, label + " duplicate entry " + ja)
            pairs.add(pair)
            hint = term.get("level_hint")
            if need(hint in LEVELS or hint == "none", label + " level_hint"):
                above = hint == "none" or LEVELS.index(hint) > ceiling
                if above:
                    need(filled(term.get("level_note_vi")), label + f" {hint} needs level_note_vi at {ctx['level']}")
                elif LEVELS.index(hint) < floor:
                    below += 1
                listed = index.get(nfc(ja)) or index.get(nfc(reading))
                if listed and hint not in listed and len(listed) == 1:
                    notes.append(f"{label} {ja}: level_hint {hint}, vocabulary book lists {'/'.join(sorted(listed))}")
            origin = term.get("origin")
            if need(origin in ("dialogue", "topic_extension"), label + " origin"):
                evidence = term.get("evidence") or []
                if origin == "dialogue":
                    from_dialogue += 1
                    need(1 <= len(evidence) <= 2, label + " dialogue terms need 1–2 evidence items")
                for item in evidence:
                    surface = item.get("surface", "")
                    text = ctx["_utterances"].get(item.get("utterance_id")) if "utterance_id" in item \
                        else ctx["_shadowing"].get(item.get("shadowing_item"))
                    need(text is not None and filled(surface) and surface in text,
                         label + " evidence not found: " + json.dumps(item, ensure_ascii=False))
            refs = term.get("source_refs", [])
            need(isinstance(refs, list) and set(refs) <= sources.keys(), label + " source_refs")
            total += 1
    if not 40 <= total <= 100:
        notes.append(f"{total} terms in stage (guide 40–100)")
    if total and ctx["level"] != "Sơ" and below / total > .4:
        notes.append(f"{below}/{total} terms are below the {ctx['level_band']} band")
    if total and not from_dialogue:
        notes.append("No term is linked to the stage dialogues; check that useful dialogue words were reviewed")
    return errors, notes


def export(data):
    return {"stage_uid": data["stage_uid"], "stage_code": data["stage_code"],
            "nodes": [{"node_id": data["stage_code"] + "-" + g["id"], "type": "vocabulary",
                       "title_vi": g["title_vi"], "terms_ja": [t["ja"] for t in g["terms"]]}
                      for g in data["groups"]]}


def hashes(path, data):
    return {"vocabulary_sha256": sha(Path(path).read_bytes()),
            "groups": {g["id"]: group_hash(g) for g in data["groups"]}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage_code")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", type=Path, help="validate a vocabulary.json draft")
    mode.add_argument("--export", type=Path, help="print terms_ja nodes for the Exchange package")
    mode.add_argument("--hashes", type=Path, help="print file and group hashes for status.json")
    args = parser.parse_args()
    ctx = brief(args.stage_code)
    if args.check:
        errors, notes = check(read(args.check), ctx)
        for note in notes:
            print("Note:", note)
        for error in errors:
            print("Error:", error)
        if errors:
            sys.exit(1)
        print("OK", args.stage_code)
    elif args.export:
        print(json.dumps(export(read(args.export)), ensure_ascii=False, indent=2))
    elif args.hashes:
        print(json.dumps(hashes(args.hashes, read(args.hashes)), ensure_ascii=False, indent=2))
    else:
        print(json.dumps({k: v for k, v in ctx.items() if not k.startswith("_")}, ensure_ascii=False, indent=2))
