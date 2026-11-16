"""Build selected specialty readings around the unchanged V8 topic sequence."""
import argparse
import copy
import hashlib
import json
import re
import uuid
from collections import Counter, defaultdict
from pathlib import Path

from markdown_it import MarkdownIt
import roadmap_v6 as old

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "kaiwa_skill/planning"
OUT = P / "v9"
BOOKS = {
    "B06": "すぐに使える 日本語会話 超ミニフレーズ 発展210",
    "B07": "すぐに使える 日本語会話 超ミニフレーズ200",
    "B11": "わかる！話せる！日本語会話 基本文型88",
    "B12": "わかる！話せる！日本語会話 発展文型125",
    "B18": "外国人のための日本語敬語の使い方 基本表現85",
    "B20": "日本人がよく使う 日本語会話お決まり表現180",
    "B24": "気持ちが伝わる 日本語会話 基本表現180",
}
CATEGORIES = {"patterns", "mini", "keigo", "idioms", "emotion"}


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    temporary.replace(path)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build(publish=False):
    topics = old.rows(P / "v8/KAIWA_CHANG_V8.jsonl")
    learner_base = old.read(P / "v8/learner.json")
    by_code = {t["display_code"]: t for t in topics}
    positions = {t["uid"]: i for i, t in enumerate(topics)}
    base_entries = {e["uid"]: e for e in learner_base["stages"]}
    decisions = [old.read(f) for f in sorted((OUT / "decisions").glob("*.json"))]
    assert decisions, "No specialties"
    assert len({d["key"] for d in decisions}) == len(decisions)
    anchors = defaultdict(list)
    content, reverse, admin = {}, [], []
    renderer = MarkdownIt("commonmark", {"html": False}).enable("table")
    used = Counter()
    warnings = []
    seen_content = {}
    for decision in decisions:
        assert decision["status"] == "reviewed"
        anchor = by_code[decision["before_topic_code"]]
        level_topics = [t for t in topics if t["level"] == anchor["level"]]
        assert anchor["level"] == decision["level"]
        assert level_topics.index(anchor) >= 2, decision["key"]
        for field in ("title_vi", "objective_vi", "placement_reason_vi", "load_reason_vi"):
            assert decision[field].strip()
        assert decision["applications"] and decision["sections"]
        for application in decision["applications"]:
            topic = by_code[application["topic_code"]]
            assert topic["level"] == decision["level"]
            assert positions[topic["uid"]] >= positions[anchor["uid"]]
            assert application["situation_id"] in {s["id"] for s in topic["situations"]}
            assert application["use_vi"].strip()
        uid = str(uuid.uuid5(uuid.NAMESPACE_URL, "kaiwa/v9/" + decision["key"]))
        selections, materials = [], []
        item_keys = set()
        for section in decision["sections"]:
            assert section["category"] in CATEGORIES and section["items"]
            assert section["title_vi"].strip()
            for item in section["items"]:
                assert item["key"] not in item_keys, decision["key"]
                item_keys.add(item["key"])
                assert item["role"] in ("core", "extension")
                for field in ("title_vi", "summary_vi", "reading_note_vi", "learner_md"):
                    assert item[field].strip()
                assert item["source_spans"]
                spans, excerpts = [], []
                for span in item["source_spans"]:
                    book = span["book_id"]
                    assert span["book_title"] == BOOKS[book]
                    path = ROOT / span["path"]
                    assert path.resolve() == (ROOT / "kaiwa_skill/knowledge" / BOOKS[book] / "book.md").resolve()
                    raw = path.read_bytes()
                    lines = raw.decode("utf-8-sig").splitlines()
                    start, end = span["start_line"], span["end_line"]
                    assert 1 <= start <= end <= len(lines)
                    if book == "B18":
                        lower = next(i+1 for i, l in enumerate(lines) if l.startswith("## PART1"))
                        upper = next(i+1 for i, l in enumerate(lines) if l.startswith("## PART2"))
                        assert lower <= start <= end < upper, decision["key"]
                    excerpt = "\n".join(lines[start-1:end])
                    excerpts.append(excerpt)
                    spans.append(dict(span, sha256=digest(raw), excerpt_sha256=digest(excerpt.encode("utf8"))))
                    used[book] += 1
                md = item["learner_md"]
                if re.search(r"<a\s|CD[- －]*\d|PDF\s*\d|Lưu ý nguồn|Trang in:|はじめに|この本の使い方|さくいん", md, re.I):
                    raise ValueError("Learner metadata or front matter: " + decision["key"] + "/" + item["key"])
                key = digest(md.encode("utf8"))
                if key in seen_content:
                    warnings.append({"type": "repeated_reading", "first": seen_content[key], "next": decision["key"]})
                seen_content[key] = decision["key"]
                html = renderer.render(md)
                content[key] = html
                selection_id = decision["key"] + "-" + item["key"]
                selections.append({"id": selection_id, "title": item["title_vi"], "kind": "speak_japanese",
                                   "support": False, "category": section["category"],
                                   "section_title": section["title_vi"], "role": item["role"], "content_key": key})
                material_file = "materials/" + selection_id + ".md"
                target = OUT / material_file
                target.parent.mkdir(exist_ok=True)
                target.write_text(md + "\n", encoding="utf8")
                materials.append({"id": selection_id, "title_vi": item["title_vi"], "source_spans": spans,
                                  "summary_vi": item["summary_vi"], "reading_note_vi": item["reading_note_vi"],
                                  "file": material_file, "sha256": digest(target.read_bytes())})
                reverse.append({"specialty_uid": uid, "specialty_key": decision["key"],
                                "item_id": selection_id, "source_spans": spans})
        admin.append({"uid": uid, "decision": decision, "materials": materials})
        anchors[anchor["uid"]].append((decision, uid, selections))
    entries, rows = [], []
    numbers = Counter()
    for topic in topics:
        for decision, uid, selections in sorted(anchors[topic["uid"]], key=lambda s: s[0]["key"]):
            level = decision["level"]
            numbers[level] += 1
            entries.append({"uid": uid, "code": decision["key"], "stage_kind": "speak_japanese",
                            "level": level, "number": numbers[level], "title": decision["title_vi"],
                            "cluster": topic["cluster_title"], "cluster_id": topic["cluster_id"],
                            "objective": decision["objective_vi"], "events": [], "situations": [],
                            "vocabulary": [], "selections": selections,
                            "order": [{"type": "source_pack", "selection_id": s["id"]} for s in selections],
                            "shadowing": None})
            rows.append(dict(decision, uid=uid, stage_kind="speak_japanese", roadmap_order=numbers[level]))
        numbers[topic["level"]] += 1
        entry = copy.deepcopy(base_entries[topic["uid"]])
        entry.update(stage_kind="topic", number=numbers[topic["level"]])
        entries.append(entry)
        rows.append(dict(topic, stage_kind="topic", roadmap_order=numbers[topic["level"]]))
    assert [e["uid"] for e in entries if e["stage_kind"] == "topic"] == [t["uid"] for t in topics]
    for level in numbers:
        level_entries = [e for e in entries if e["level"] == level]
        assert level_entries[-1]["stage_kind"] == "topic"
    payload = {"version": "9.0", "stages": entries, "content": content, "branches": learner_base["branches"]}
    write(OUT / "learner.json", payload)
    for record in admin:
        write(OUT / "admin" / (record["decision"]["key"] + ".json"), record)
    write(OUT / "SOURCE_INDEX.json", reverse)
    write(OUT / "QA_WARNINGS.json", warnings)
    status = {"version": "9.0", "topic_stages": len(topics), "specialty_stages": len(decisions),
              "total_stages": len(entries), "levels": dict(numbers), "source_spans_by_book": dict(used),
              "readings": len(reverse), "unique_readings": len(content),
              "basis_sha256": digest((P / "v8/KAIWA_CHANG_V8.jsonl").read_bytes())}
    write(OUT / "STATUS.json", status)
    write(OUT / "SOURCE_POLICY.json", {"version": "9.0", "books": BOOKS, "basis": "../v8/KAIWA_CHANG_V8.jsonl",
                                      "selection": "read_and_curate", "keigo_scope": "Part1",
                                      "target_topic_interval": 4, "fixed_specialty_count": None})
    report = ["# Báo cáo V9", "",
              f"{len(topics)} chặng topic, {len(decisions)} chuyên đề, tổng {len(entries)} chặng.", "",
              f"{len(reverse)} mục đọc đã tuyển. Số mục thể hiện lượt đặt, một nội dung có thể dùng lại có lý do.", "",
              "Phạm vi bảy sách được tuyển theo nhu cầu giao tiếp của cụm topic tiếp theo. "
              "Báo cáo chỉ đếm phần đã chọn. Phạm vi đọc và phần để dành do từng worker ghi ở work/.", "",
              "B18 chỉ lấy Part 1. Mục 存じる② thiếu thân bài nguồn, nằm ngoài nội dung đã tuyển.", ""]
    spacing = {}
    for level in numbers:
        level_entries = [e for e in entries if e["level"] == level]
        runs, count = [], 0
        for entry in level_entries:
            if entry["stage_kind"] == "topic":
                count += 1
            else:
                runs.append(count)
                count = 0
        runs.append(count)
        spacing[level] = runs
        specialties_count = sum(e["stage_kind"] == "speak_japanese" for e in level_entries)
        report += [f"## {level}", "", f"{len(level_entries)-specialties_count} topic và {specialties_count} chuyên đề.",
                   "", "Số topic trước, giữa và sau các chuyên đề theo thứ tự", "",
                   ", ".join(map(str, runs)), ""]
        for decision in decisions:
            if decision["level"] != level:
                continue
            report += [f"### {decision['title_vi']}", "",
                       "Đặt trước " + decision["before_topic_code"] + ". " + decision["placement_reason_vi"], "",
                       decision["load_reason_vi"], ""]
            for section in decision["sections"]:
                report.append("- " + section["title_vi"] + " — " + ", ".join(i["title_vi"] for i in section["items"]))
            report.append("")
    (OUT / "REPORT_V9.md").write_text("\n".join(report), encoding="utf8")
    write(OUT / "SPACING.json", spacing)
    roadmap = OUT / "KAIWA_CHANG_V9.jsonl"
    roadmap.write_text("".join(json.dumps(r, ensure_ascii=False)+"\n" for r in rows), encoding="utf8")
    for level, name in zip(numbers, ("SO_CAP.md", "TRUNG_CAP.md", "THUONG_CAP.md")):
        text = "# " + level + "\n\n"
        for e in entries:
            if e["level"] == level:
                text += f"## {e['number']}. {e['title']}\n\n{e['objective']}\n\n"
                text += "\n".join("- " + s["title"] for s in e["selections"] + e["situations"]) + "\n\n"
        (OUT / name).write_text(text, encoding="utf8")
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    html = template.replace("__COURSE_DATA__", json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c"))
    (OUT / "ROADMAP.html").write_text(html, encoding="utf8")
    if publish:
        write(P / "CURRENT_ROADMAP.json", {"version": "9.0", "registry": "kaiwa_skill/planning/v5/chang_registry.json",
                                         "roadmap": roadmap.relative_to(ROOT).as_posix(),
                                         "policy": "kaiwa_skill/planning/v9/SOURCE_POLICY.json"})
        (ROOT / "docs/index.html").write_text(html, encoding="utf8")
    print(json.dumps(status, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    build(parser.parse_args().publish)
