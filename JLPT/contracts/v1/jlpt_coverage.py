"""Editorial coverage on the same question, media and cue IDs consumed by Harumi."""
import re
from jlpt_sentences import sentence_units

FIELDS = {
    "master": "Audio tổng", "rssUrl": "URL audio RSS", "mondaiTime": "Mốc đầu–cuối mondai",
    "questionTime": "Mốc đầu–cuối câu", "answer": "Đáp án đã đối chiếu",
    "explanation": "Lời giải", "questionVi": "Dịch câu hỏi", "choiceVi": "Dịch lựa chọn",
    "script": "Script tiếng Nhật", "scriptPairs": "Cặp câu script Nhật–Việt",
    "passagePairs": "Cặp câu bài đọc Nhật–Việt", "sentenceSplit": "Tách bản dịch theo câu",
}


def meaningful(text):
    return bool(re.search(r"[ぁ-ヺ一-龯々A-Za-z]", text or ""))


def coverage(package):
    counters = {}
    gaps = []
    ann = package["annotations"]
    nodes = {n["nodeId"]: n for n in ann["nodes"]}
    master = package.get("masterAudio") or {}
    listening = package["content"]["choukai"]["mondais"]

    def check(field, ok, node=None, detail="", owner="editor"):
        counter = counters.setdefault(field, {"present": 0, "required": 0})
        counter["required"] += 1
        if ok:
            counter["present"] += 1
        else:
            origin = nodes.get(node, {})
            gaps.append(dict(field=field, targetId=node, sourceId=origin.get("sourceId"),
                             locator=origin.get("locator"), sourceNumber=origin.get("sourceNumber"),
                             detail=detail, owner=owner))

    def sentence_pairs(node, field, japanese):
        rows = ann.get("sentencePairs", {}).get(node, [])
        check(field, rows, node, "mapping")
        for index, row in enumerate(rows, 1):
            check(field, bool((row.get("vi") or "").strip()), node, f"row {index}")
            # Table rows are structural pairs. Quoted dialogue may end inside a sentence.
            if "|" not in row["ja"]:
                check("sentenceSplit", len(sentence_units(row["ja"])) == 1, node, f"row {index}")
        # A dropped anchor must not make a partially translated passage appear complete.
        compact = lambda text: re.sub(r"[\s|]+|(?m:^\|(?:\s*:?-+:?\s*\|)+\s*$)", "", text)
        if rows:
            check(field, compact(japanese) == compact("\n".join(r["ja"] for r in rows)), node, "JA coverage")

    if listening:
        check("master", master.get("assetId") or master.get("rss"), owner="admin")
        check("rssUrl", (master.get("rss") or {}).get("enclosureUrl"), owner="admin")
    for section, paper in package["content"].items():
        for m in paper["mondais"]:
            cues = [s for s in ann["audioSegments"] if s["mondaiId"] == m["id"] and s["endMs"] is not None]
            if section == "choukai":
                check("mondaiTime", any(s["role"] == "mondai" for s in cues), m["id"], owner="audio")
            for block in m["blocks"]:
                shared = False
                for item in block["mediaItems"]:
                    if item["kind"] == "passage":
                        sentence_pairs(item["id"], "passagePairs", item["passage"]["jaMd"])
                    if item["kind"] == "audio" and item["audio"]["scriptJaMd"].strip():
                        shared = True
                        sentence_pairs(item["id"], "scriptPairs", item["audio"]["scriptJaMd"])
                for q in block["questions"]:
                    qid = q["id"]
                    check("answer", q["correctChoiceId"], qid, owner="source")
                    check("explanation", (q.get("explanation") or "").strip(), qid)
                    prompt = q["prompt"]
                    # Usage tasks print a headword and ask the learner to choose a sentence.
                    usage = section == "mojigoi" and any(s in m["instruction"] for s in ("使い方", "つかいかた", "使われ方"))
                    if meaningful(prompt["text"]) and not usage:
                        check("questionVi", (prompt.get("textVi") or q.get("translationVi") or "").strip(), qid)
                    for c in q["choices"]:
                        if meaningful(c["text"]) and (usage or section in ("dokkai", "choukai")):
                            check("choiceVi", (c.get("textVi") or "").strip(), qid, c["id"])
                    if section == "choukai":
                        script = (q.get("jlptListenScript") or {}).get("scriptJaMd", "").strip()
                        check("script", shared or script, qid, owner="audio")
                        if script:
                            sentence_pairs(qid, "scriptPairs", script)
                        check("questionTime", any(qid in c["questionIds"] for c in cues), qid, owner="audio")
    return counters, gaps


def checklist_issues(package):
    _, gaps = coverage(package)
    result = []
    for gap in gaps:
        field = gap["field"]
        where = " · ".join(str(v) for v in (gap["sourceId"], gap["sourceNumber"], gap["locator"], gap["detail"]) if v)
        result.append(dict(code="COVERAGE_" + field, severity="error", targetId=gap["targetId"],
                           message=FIELDS[field] + (" · " + where if where else "")))
    return result
