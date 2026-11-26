"""Export neutral, ID-answered Minna exercises to Harumi editor copy JSON.

Usage: py -X utf8 scripts/curriculum_templates.py authored/lesson-39/templates/sections.json
       py -X utf8 scripts/curriculum_templates.py --renshuu authored/renshuu/lesson-01.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"manualQnA", "manualFillInBlank", "manualMultiSelect", "jlptReading", "jlptListening"}
BLANK = re.compile(r"\(\.\.\.\)|\([\s ]+\)|（[\s　]+）")


def require(value, message):
    if not value:
        raise ValueError(message)
    return value


def block(text, vi=""):
    return {"text": text, "textVi": vi, "reading": "", "kuroshiroJson": None, "sudachiJson": None}


def validate_question(q, kind, place):
    require(isinstance(q.get("id"), str) and q["id"].strip(), f"{place}: missing id")
    require(isinstance(q.get("prompt_ja"), str) and q["prompt_ja"].strip(), f"{place}: missing prompt_ja")
    require(isinstance(q.get("explanation_vi"), str) and q["explanation_vi"].strip(), f"{place}: missing explanation_vi")
    if kind == "manualFillInBlank":
        answers = q.get("blank_answers")
        count = len(BLANK.findall(q["prompt_ja"]))
        require(count > 0 and isinstance(answers, list) and len(answers) == count, f"{place}: blank count differs from answers")
        require(all(isinstance(x, str) and x.strip() for x in answers), f"{place}: empty blank answer")
        return
    choices = q.get("choices")
    require(isinstance(choices, list) and 2 <= len(choices) <= 26, f"{place}: choices must have 2–26 entries")
    ids = [c.get("id") for c in choices if isinstance(c, dict)]
    require(len(ids) == len(choices) and len(set(ids)) == len(ids), f"{place}: duplicate or invalid choice IDs")
    require(all(isinstance(c.get("text"), str) and c["text"].strip() for c in choices), f"{place}: empty choice")
    require(len({c["text"].strip() for c in choices}) == len(choices), f"{place}: duplicate choice text")
    if kind == "manualMultiSelect":
        correct = q.get("correct_choice_ids")
        require(isinstance(correct, list) and len(correct) >= 2 and len(set(correct)) == len(correct), f"{place}: multi-select needs distinct correct IDs")
        require(all(x in ids for x in correct), f"{place}: unknown correct ID")
    else:
        require(q.get("correct_choice_id") in ids, f"{place}: unknown correct ID")


def question(q, kind):
    choices = q.get("choices") or [{"id": "a", "text": ""}, {"id": "b", "text": ""}]
    answer = q.get("correct_choice_id") or (q.get("correct_choice_ids") or [choices[0]["id"]])[0]
    return {
        "id": q["id"], "prompt": block(q["prompt_ja"], q.get("prompt_vi", "")),
        "choices": choices, "correctChoiceId": answer,
        **({"correctChoiceIds": q["correct_choice_ids"]} if kind == "manualMultiSelect" else {}),
        **({"blankAnswers": [block(a) for a in q["blank_answers"]]} if kind == "manualFillInBlank" else {}),
        "explanation": q["explanation_vi"], "adminShowExplanation": True,
    }


def convert(source):
    sections = source.get("sections")
    require(isinstance(sections, list) and sections, "missing sections")
    seen = set()
    result = []
    for n, s in enumerate(sections, 1):
        place = f"section {n}"
        kind = s.get("kind")
        require(kind in KINDS, f"{place}: invalid kind")
        sid = require(s.get("id"), f"{place}: missing id")
        require(sid not in seen, f"{place}: duplicate ID {sid}")
        seen.add(sid)
        qs = s.get("questions")
        require(isinstance(qs, list) and qs, f"{place}: missing questions")
        if kind == "manualMultiSelect":
            require(len(qs) == 1, f"{place}: multi-select has one question")
        for q in qs:
            validate_question(q, kind, f"{sid}/{q.get('id')}")
            require(q["id"] not in seen, f"{place}: duplicate ID {q['id']}")
            seen.add(q["id"])
        length = max(len(q.get("choices", [])) for q in qs)
        if kind in {"jlptReading", "jlptListening"}:
            require(all(len(q["choices"]) == length for q in qs), f"{place}: JLPT choice counts differ")
            media = s.get("media") or {}
            require(media.get("kind") == ("audio" if kind == "jlptListening" else "passage"), f"{place}: wrong media kind")
            if kind == "jlptReading":
                require(media.get("ja") and media.get("vi"), f"{place}: reading passage missing")
                item = {"id": sid + ".media", "kind": "passage", "passage": {"jaMd": media["ja"], "jaHtml": None, "viMd": media["vi"], "viHtml": None}}
            else:
                require(media.get("url") and media.get("script_ja") and media.get("script_vi"), f"{place}: audio URL/script missing")
                require(media.get("verification") and media.get("upload_status"), f"{place}: audio provenance missing")
                if media.get("local_asset"):
                    require((ROOT / media["local_asset"]).is_file(), f"{place}: local audio asset missing")
                item = {"id": sid + ".media", "kind": "audio", "audio": {"url": media["url"], "rssTitle": None, "rssAudioUrl": None, "scriptJaMd": media["script_ja"], "scriptJaHtml": None, "scriptViMd": media["script_vi"], "scriptViHtml": None, "sttRawJson": None}}
            jqs = []
            for q in qs:
                native = question(q, kind)
                if kind == "jlptListening":
                    native["jlptListenScript"] = {"scriptJaMd": q.get("script_ja", media["script_ja"]), "scriptJaHtml": None, "scriptViMd": q.get("script_vi", media["script_vi"]), "scriptViHtml": None}
                jqs.append(native)
            sec = {"id": sid, "type": "ListenAnswer" if kind == "jlptListening" else "ReadAnswer", "isManual": True, "clusterPrompt": block(s.get("cluster_prompt_ja") or ("話を聞いて、質問に答えてください。" if kind == "jlptListening" else "次の文章を読んで、質問に答えてください。")), "choiceCount": length, "questions": jqs, "jlptBlock": {"id": sid + ".block", "choiceCount": length, "mediaItems": [item], "questions": jqs}}
        else:
            sec = {"id": sid, "type": "FillInBlankInline" if kind == "manualFillInBlank" else "QnA4Answer", "isManual": True, "clusterPrompt": block(s.get("cluster_prompt_ja", "")), "questions": [question(q, kind) for q in qs]}
            if kind == "manualFillInBlank":
                sec["fillBlankUseSelect"] = False
            else:
                sec["variant"] = "multiSelect" if kind == "manualMultiSelect" else "jaToVi"
                sec["choiceCount"] = length
        fmt = "Listening" if kind == "jlptListening" else "Reading" if kind == "jlptReading" else "QuizMultipleChoice"
        result.append((sid, {"harumiExerciseCopy": 1, "adminKind": kind, "templateFormat": fmt, "audioPath": None, "section": sec}))
    return result


def from_renshuu(data, quick_check=False):
    require(isinstance(data.get("items"), list), "renshuu: missing items")
    sections = []
    for item in data["items"]:
        kind = item.get("kind")
        require(kind in {"manualQnA", "manualMultiSelect", "manualFillInBlank"}, "renshuu: unsupported item kind")
        prompt = item["prompt_ja"]
        if kind == "manualFillInBlank":
            prompt = prompt.replace("＿＿", "(...)")
        q = {"id": item["id"], "prompt_ja": prompt, "explanation_vi": item["explanation_vi"], "source_item_id": item.get("source_id"), "grammar_refs": item.get("grammar_refs", [])}
        if kind == "manualQnA":
            q.update({"choices": item["choices"], "correct_choice_id": item["correct"]})
        elif kind == "manualMultiSelect":
            q.update({"choices": item["choices"], "correct_choice_ids": item["correct"]})
        else:
            q["blank_answers"] = [item["correct"]]
        refs = item.get("grammar_refs") or []
        if quick_check:
            require(isinstance(refs, list) and refs and all(isinstance(x, str) and x.strip() for x in refs), f"{item['id']}: quick check needs grammar_refs")
        sections.append({"id": item["id"] + ".section", "kind": kind, "grammar_refs": refs, "cluster_prompt_ja": item.get("instruction_vi") or "答えを書きなさい。", "questions": [q]})
    return {"lesson": data.get("lesson"), "sections": sections}


def storage_content(section):
    """Build DB content with answer indices computed before the copy parser changes IDs."""
    native = section["section"]
    kind = section["adminKind"]
    if kind in {"jlptReading", "jlptListening"}:
        payload = {
            "section_type": native["type"], "jlpt_style": "listening" if kind == "jlptListening" else "reading",
            "is_manual": True, "cluster_prompt_ja": native["clusterPrompt"]["text"],
            "jlpt_block": native["jlptBlock"], "questions": [],
        }
    else:
        dtos = []
        for q in native["questions"]:
            ids = [c["id"] for c in q["choices"]]
            dto = {
                "type": native["variant"] if kind != "manualFillInBlank" else "FillInBlankInline",
                "question_ja": q["prompt"]["text"], "question": q["prompt"].get("textVi", ""),
                "choices": [c["text"] for c in q["choices"]],
                "correct_index": ids.index(q["correctChoiceId"]), "explanation": q["explanation"],
            }
            if kind == "manualMultiSelect":
                dto["correct_indices"] = [ids.index(x) for x in q["correctChoiceIds"]]
            if kind == "manualFillInBlank":
                dto["blank_answers"] = [x["text"] for x in q["blankAnswers"]]
            dtos.append(dto)
        payload = {
            "section_type": native["type"], "is_manual": True,
            "cluster_prompt_ja": native["clusterPrompt"]["text"], "questions": dtos,
        }
        if kind == "manualMultiSelect":
            payload["variant"] = "multiSelect"
            payload["choice_count"] = native["choiceCount"]
        if kind == "manualQnA":
            payload["variant"] = "jaToVi"
            payload["choice_count"] = native["choiceCount"]
        if kind == "manualFillInBlank":
            payload["fill_blank_use_select"] = False
    return {"format": section["templateFormat"], "content": payload, "audioPath": section.get("audioPath")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--renshuu", action="store_true")
    ap.add_argument("--quick-check", action="store_true", help="same item schema as --renshuu, require 1–3 questions per grammar group")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    data = json.loads(args.source.read_text(encoding="utf-8"))
    if args.renshuu or args.quick_check:
        data = from_renshuu(data, quick_check=args.quick_check)
    # Some lessons have no additional reviewed drills beyond the primary B bank.
    outputs = [] if args.renshuu and data["sections"] == [] else convert(data)
    groups = {}
    for source_section in data["sections"]:
        refs = source_section.get("grammar_refs") or sorted({ref for q in source_section["questions"] for ref in q.get("grammar_refs", [])})
        if not refs:
            continue
        key = "+".join(refs)
        groups.setdefault(key, {"grammar_refs": refs, "section_ids": [], "question_count": 0})
        groups[key]["section_ids"].append(source_section["id"])
        groups[key]["question_count"] += len(source_section["questions"])
    if args.quick_check:
        catalog = json.loads((ROOT / "catalog/grammar-points.json").read_text(encoding="utf-8"))
        lesson = next((x for x in catalog if x["lesson"] == data.get("lesson")), None)
        require(lesson is not None, f"lesson {data.get('lesson')}: missing grammar catalog")
        expected = [point["id"] for point in lesson["points"]]
        require(list(groups) == expected, f"lesson {data.get('lesson')}: grammar groups differ from catalog order/coverage")
        for order, point in enumerate(lesson["points"], 1):
            groups[point["id"]]["grammar_point_order"] = order
            groups[point["id"]]["grammar_point_title"] = point["title"]
        for key, group in groups.items():
            require(1 <= group["question_count"] <= 3, f"quick check group {key}: expected 1–3 questions")
    out = args.out or ROOT / "exports" / "curriculum-exercises" / f"lesson-{int(data['lesson']):02d}"
    out.mkdir(parents=True, exist_ok=True)
    index = []
    for (sid, payload), source_section in zip(outputs, data["sections"]):
        stem = re.sub(r"[^a-zA-Z0-9._-]", "-", sid)
        kind = payload["adminKind"]
        storage_name = stem + ".storage.json"
        (out / storage_name).write_text(json.dumps(storage_content(payload), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        copy_name = None
        if kind in {"manualFillInBlank", "jlptReading"}:
            copy_name = stem + ".paste.json"
            (out / copy_name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        refs = source_section.get("grammar_refs") or sorted({ref for q in source_section["questions"] for ref in q.get("grammar_refs", [])})
        key = "+".join(refs) if refs else None
        row = {"id": sid, "kind": kind, "storage_file": storage_name, "paste_file": copy_name,
               "question_count": len(payload["section"]["questions"]), "placement_after_grammar_refs": refs,
               "group_key": key}
        if args.quick_check:
            row["grammar_point_order"] = groups[key]["grammar_point_order"]
        if kind == "jlptListening" and source_section["media"].get("harumii_audio_bound") is False:
            row["pending_audio_media_ids"] = [m["id"] for m in payload["section"]["jlptBlock"]["mediaItems"]
                                              if m["kind"] == "audio"]
        index.append(row)
    try:
        source_path = args.source.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        source_path = str(args.source)
    (out / "index.json").write_text(json.dumps({"lesson": data.get("lesson"), "source": source_path, "sections": index, "groups": list(groups.values())}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"exported {len(index)} sections / {sum(x['question_count'] for x in index)} questions -> {out}")


if __name__ == "__main__":
    main()
