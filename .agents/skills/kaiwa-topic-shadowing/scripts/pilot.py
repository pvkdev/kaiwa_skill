"""Read validated inputs, check an editorial draft, or publish a reviewed V13 roadmap node."""
import argparse
import hashlib
import json
import re
import runpy
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PLAN = ROOT / "kaiwa_skill/planning"
SKILL = Path(__file__).resolve().parents[1] / "SKILL.md"
V = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-vocabulary/scripts/vocab.py"))


def digest(path):
    return hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def save(path, data):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf8", newline="\n")
    temporary.replace(path)


def inputs(code):
    brief = V["brief"](code)
    path = PLAN / "v12/stages" / code / "vocabulary.json"
    pinned = digest(path)
    draft, _ = V["reviewed_draft"](path, brief)
    if digest(path) != pinned:
        raise ValueError("Vocabulary changed during checkpoint validation: read the brief again")
    brief["words"] = {g["title_vi"]: {t["ja"]: t["vi"] for t in g["terms"]} for g in draft["groups"]}
    brief["pins"] = {"v11": brief["learner_sha256"], "v12": pinned, "skill": digest(SKILL)}
    return brief


def build(code, mode, review_notes=()):
    source = inputs(code)
    if mode == "brief":
        print(json.dumps({k: v for k, v in source.items() if not k.startswith("_")}, ensure_ascii=False))
        return
    folder = PLAN / "v13/pilot" / code
    path = folder / "draft.json"
    draft = V["read"](path)
    if draft.get("pins") != source["pins"]:
        raise ValueError("Inputs or skill changed: compare the current brief and review the affected draft")
    groups, items = draft["groups"], draft["items"]
    words = {word for group in source["words"].values() for word in group}
    scenes = {s["id"] for s in source["situations"]}
    if draft["code"] != code or not items or not groups or set(groups) != {i["group"] for i in items}:
        raise ValueError("Stage or group mismatch")
    ids, lines, out = set(), set(), []
    for i in items:
        sid = i["id"]
        ja = re.sub(r"[\s。？！?!]+", "", unicodedata.normalize("NFKC", i["ja"]))
        if sid in ids or not re.fullmatch(re.escape(code) + r"-V13-\d{3}", sid) or ja in lines:
            raise ValueError(f"{sid}: duplicate sentence or invalid ID")
        ids.add(sid)
        lines.add(ja)
        if not all(i[k].strip() for k in ("role_vi", "vi", "ja", "pattern")) or i["gender"] not in ("male", "female"):
            raise ValueError(f"{sid}: incomplete sentence or voice")
        if not re.search(r"[ぁ-ヿ一-鿿]", ja) or re.search(r"[。！？?!].*[^。！？?!\s]", i["ja"]):
            raise ValueError(f"{sid}: expected one Japanese sentence")
        if not isinstance(i["terms"], list) or not set(i["terms"]) <= words or not i["scenes"] or not set(i["scenes"]) <= scenes:
            raise ValueError(f"{sid}: check terms and scene links")
        out.append({"id": sid, "type": "single_sentence",
                    "speakers": [{"id": "a", "gender": i["gender"], "role_vi": i["role_vi"]}],
                    "turns": [{"speaker_id": "a", "ja": i["ja"], "vi": i["vi"]}]})
    patterns = Counter(i["pattern"] for i in items)
    if not any(n >= 2 for n in patterns.values()):
        print(f"{code}: review whether learners revisit a useful pattern")
    if not any(i["terms"] for i in items):
        raise ValueError(f"{code}: no linked V12 vocabulary in this lesson")
    if mode == "publish":
        save(folder / "shadowing.json", {"id": source["uid"] + "-shadowing", "type": "shadowing", "items": out})
        save(folder / "status.json", {"state": "reviewed", **source["pins"], "draft": digest(path),
                                      "output": digest(folder / "shadowing.json"), "count": len(out),
                                      "review_notes": list(review_notes)})
    print(code, len(out), "sentences", len(groups), "groups")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["brief", "check", "publish"])
    parser.add_argument("code")
    parser.add_argument("--note", action="append", default=[], help="Editorial note for the pilot review checkpoint")
    args = parser.parse_args()
    build(args.code, args.mode, args.note)
