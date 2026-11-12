"""Validate V4.1 metadata and render sections 1-6 of its Markdown from JSONL.

Read-only by default. --write updates only the derived Markdown sections.
This does not verify the meaning of all source references or generate lessons.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid


STEM = "KAIWA_CHANG_V4_1"
LEVELS = ["Sơ", "Trung", "Thượng"]


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def identity_hash(rows):
    identities = [{"id": r["id"], "uid": r["uid"]} for r in rows]
    return hashlib.sha256(json.dumps(identities, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def tokens(row):
    return list(dict.fromkeys(row["sources"] + row["banks"]))


def base_token(token):
    source, unit = token.split(":", 1)
    return source, re.split(r"[/#]", unit, maxsplit=1)[0]


def grouped(rows):
    groups = []
    for row in rows:
        key = (row["level"], row["cum"])
        if not groups or groups[-1][0] != key:
            groups.append((key, []))
        groups[-1][1].append(row)
    return groups


def validate(rows, registry, meta):
    errors = []
    by_id = {r["id"]: r for r in rows}
    if len(rows) != 194 or len(by_id) != 194 or len({r["uid"] for r in rows}) != 194:
        errors.append("Expected 194 distinct stage IDs and UIDs")
    if identity_hash(rows) != meta["identity_sha256"]:
        errors.append("Stage identity or order changed from accepted V4.1")
    if set(registry) != {r["uid"] for r in rows}:
        errors.append("Registry UID set does not match JSONL")
    if Counter(r["level"] for r in rows) != Counter(meta["expected_levels"]):
        errors.append("Level counts changed")
    expected_groups = [(g["level"], g["name"]) for g in meta["clusters"]]
    if [key for key, _ in grouped(rows)] != expected_groups or len(expected_groups) != 39:
        errors.append("Cluster identity/order differs from accepted 39 clusters")
    targets = {t["id"]: t for t in meta["source_targets"]}
    for row in rows:
        reg = registry.get(row["uid"], {})
        if reg != {"display_code": row["id"], "level": row["level"], "title": row["title"]}:
            errors.append(row["id"] + ": registry fields mismatch")
        if row["track"] not in {"Đời sống", "Công việc"} or not isinstance(row["fact_check"], bool):
            errors.append(row["id"] + ": invalid track/fact_check")
        union = list(dict.fromkeys(t for s in row["situations"] for t in s["sources"]))
        if row["sources"] != union:
            errors.append(row["id"] + ": stage sources must equal ordered situation-source union")
        for situation in row["situations"]:
            sources = situation["sources"]
            kind = "book" if any(re.match(r"B\d{2}:", t) for t in sources) else "memo" if sources else "ai"
            if situation["kind"] != kind or situation["ai"] is not (kind == "ai"):
                errors.append(row["id"] + ": inconsistent situation kind/ai")
        for token in tokens(row):
            source, unit = base_token(token)
            target = targets.get(source)
            if target is None or unit not in target["units"] + target.get("extra_units", []):
                errors.append(row["id"] + ": unknown/coarse source token " + token)
    for sid in meta["fact_check_required"]:
        if not by_id[sid]["fact_check"]:
            errors.append(sid + ": fact_check required by editorial review")
    for rule in meta["source_rules"]:
        subject = by_id[rule["stage"]]
        if "situation_index" in rule:
            subject = subject["situations"][rule["situation_index"]]
        actual = set(subject[rule["field"]])
        missing = set(rule.get("required", [])) - actual
        forbidden = set(rule.get("forbidden", [])) & actual
        if missing or forbidden:
            errors.append(rule["stage"] + ": source regression " + str({"missing": sorted(missing), "forbidden": sorted(forbidden)}))
    if errors:
        raise ValueError("\n".join(errors))


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, rows):
    result = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    result += ["| " + " | ".join(cell(v) for v in row) + " |" for row in rows]
    return "\n".join(result)


def compact(items):
    by_source = defaultdict(list)
    for token in items:
        source, unit = token.split(":", 1)
        if unit not in by_source[source]:
            by_source[source].append(unit)
    return " · ".join(k + " " + ",".join(v) for k, v in by_source.items()) or "—"


def sections(rows, meta, original):
    groups = grouped(rows)
    summaries = {(g["level"], g["name"]): g["summary"] for g in meta["clusters"]}
    kinds = Counter(s["kind"] for r in rows for s in r["situations"])
    count = sum(kinds.values())
    result = {}
    level_table = []
    for lv in LEVELS:
        selected = [r for r in rows if r["level"] == lv]
        level_table.append([lv, len(selected), sum(r["track"] == "Đời sống" for r in selected), sum(r["track"] == "Công việc" for r in selected)])
    level_table.append(["**Tổng**", "**" + str(len(rows)) + "**", sum(r["track"] == "Đời sống" for r in rows), sum(r["track"] == "Công việc" for r in rows)])
    result[1] = "## 1. Con số\n\n" + table(["Level", "Chặng", "Đời sống", "Công việc"], level_table)
    result[1] += f"\n\n**Tình huống trong danh sách: {count}.** Có token sách: {kinds['book']}. Chỉ có token memo hoặc NHK: {kinds['memo']}. Không có nguồn, do AI đề xuất [AI]: {kinds['ai']}. Khoảng {(kinds['book'] + kinds['memo']) / count:.0%} có token nguồn và {kinds['book'] / count:.0%} có token sách. Đây là nhãn định vị, không phải chứng nhận nội dung đã được kiểm hết."
    result[1] += f"\n\n{sum(len(r['situations']) <= 2 for r in rows)} chặng hiện liệt kê tối đa 2 tình huống. Danh sách là **hạt giống** để đọc sâu và mở rộng khi biên soạn; không áp số lượng tình huống cố định cho mọi chặng."
    result[1] += "\n\n**Quy ước nguồn:** `book` có ít nhất một token Bxx trong chính tình huống; `memo` chỉ có Sxx/N/W; `ai` chưa có token. `banks` là ngân hàng tham khảo, không tự nâng nhãn nguồn của tình huống. Token chi tiết dùng `S16:<bài>/STAGE<mục>/<nhánh>/<số>` hoặc `B18:P2-1#scene<số>`.\n\n**FC:** cờ cần đối chiếu dữ kiện theo nơi/thời điểm khi viết bài; không có nghĩa đã kiểm xong và không tạo cổng cho người học."
    # Preserve the accepted pedagogical explanation; only its derived tables change.
    old_section = re.search(r"(?ms)^## 2\. .*?(?=^## 3\.)", original).group(0)
    preamble = old_section.split("### Thứ tự level", 1)[0].rstrip()
    result[2] = preamble
    for lv in LEVELS:
        data = []
        for i, (key, selected) in enumerate((g for g in groups if g[0][0] == lv), 1):
            data.append([i, key[1], f"{selected[0]['id']} đến {selected[-1]['id']} ({len(selected)})", "".join("Đ" if r["track"] == "Đời sống" else "C" for r in selected), summaries[key]])
        result[2] += "\n\n### Thứ tự level " + lv + "\n\n" + table(["Bước", "Cụm", "Chặng", "Nhịp ĐS/CV", "Sau cụm này bạn làm được"], data)
    result[2] += "\n\nGhi chú nhịp: Đ = chặng đời sống, C = chặng công việc, theo thứ tự gợi ý trong cụm; không phải điều kiện mở khóa."
    topics = defaultdict(lambda: defaultdict(list))
    for row in rows:
        topics[row["master_topic"]][row["level"]].append(row["id"])
    result[3] = "## 3. Chủ đề gốc và các level xuất hiện\n\n" + table(["Chủ đề gốc", *LEVELS], [[topic, *[", ".join(levels[lv]) or "—" for lv in LEVELS]] for topic, levels in topics.items()])
    result[4] = "## 4. Danh sách chặng theo cụm (theo thứ tự học)\n\nĐS = đời sống; CV = công việc; [AI] = chưa có nguồn trong tình huống. `N` = NHK 48; `W` = NHK công sở; `Sxx` = memo; `Bxx` = sách. FC = cần kiểm tra dữ kiện hiện hành khi viết nội dung."
    policy = meta.get("learning_design")
    if policy:
        result[4] += "\n\n**Cách đóng gói bài trong các chặng — " + policy["version"] + ":**\n\n"
        result[4] += "- **Gối đầu:** " + policy["progression"] + "\n"
        result[4] += "- **Speak Japanese:** " + policy["speak_japanese"] + "\n"
        result[4] += "- **Từ vựng:** " + policy["vocabulary"] + "\n"
        result[4] += "\n" + "\n".join("- **" + "/".join(p["book_ids"]) + ":** " + p["grouping"] for p in policy["source_delivery"] if p["delivery"] == "shadowing")
        result[4] += "\n\n" + policy["scope_note"]
    for lv in LEVELS:
        result[4] += "\n\n### Level " + lv
        for key, selected in groups:
            if key[0] != lv:
                continue
            data = []
            for r in selected:
                situations = "; ".join(s["title"] + (" [AI]" if s["kind"] == "ai" else "") for s in r["situations"])
                notes = r["level_notes"] + (["FC: cần kiểm tra dữ kiện hiện hành."] if r["fact_check"] else [])
                data.append([r["id"], "ĐS" if r["track"] == "Đời sống" else "CV", "**" + r["title"] + "**", situations, compact(r["sources"]), compact(r["banks"]), " ".join(notes) or "—"])
            result[4] += "\n\n#### Cụm: " + key[1] + "\n\n*Sau cụm: " + summaries[key] + "*\n\n" + table(["ID", "Loại", "Chặng", "Tình huống", "Nguồn", "Mẫu & ngân hàng", "Lưu ý"], data)
    used = defaultdict(set)
    for r in rows:
        for t in tokens(r):
            source, unit = base_token(t)
            used[source].add(unit)
    coverage = []
    for target in meta["source_targets"]:
        expected = target["units"]
        missing = [u for u in expected if u not in used[target["id"]]]
        coverage.append([target["label"], len(expected), len(expected) - len(missing), ", ".join(missing) or "—"])
    result[5] = "## 5. Báo cáo phủ nguồn\n\n" + table(["Nguồn", "Mục tiêu chỉ mục", "Đã gắn", "Chưa gắn"], coverage)
    result[5] += "\n\nTính từ token của tình huống **và** ngân hàng. Mẫu số là tập nhãn chỉ mục được khai báo trong `KAIWA_CHANG_V4_1_META.json`, không phải số trang, số đoạn đã đọc hoặc tỷ lệ nội dung đã tận dụng. Token con quy về mục cha trước khi đếm; không cộng trùng vì có nhiều scene/STAGE. Các phần/mục con khác độ sâu giữa các sách không dùng để so sánh lượng kiến thức."
    result[5] += "\n\nB03 bỏ U2–U4 và U16 khỏi tập mục tiêu nói. B08 đếm 61 nhãn (gồm 33 cảnh P4), sửa con số 58 cũ. B14 có đủ U1–U5 ở mức ngân hàng, chưa có định vị section. B21/B22/B23 cùng số bài nhưng có vai trò khác nhau. S04 chỉ là T4–T9 đã nhận trong memo; S15 cơ sở nằm trong tập S14 cùng chủ đề. NHK công sở chỉ có 43 tập trong memo, không giả định #31/#32/#34."
    book_table = []
    for i in range(1, 28):
        book = f"B{i:02}"
        matched = [r for r in rows if any(t.startswith(book + ":") for t in tokens(r))]
        book_table.append([book, len(matched), *[sum(r["level"] == lv for r in matched) for lv in LEVELS]])
    result[6] = "## 6. 27 sách dùng ở đâu\n\n" + table(["Sách", "Số chặng", *LEVELS], book_table)
    result[6] += "\n\nĐây là số chặng có token sách trong tình huống hoặc ngân hàng, chưa phải bằng chứng sách đã được trích/đọc sâu. Cần kiểm tra đóng góp thực tế khi biên soạn từng chặng."
    return result


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path(__file__).resolve().parents[1] / "planning/v2")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    folder = args.directory.resolve()
    rows = [json.loads(line) for line in (folder / (STEM + ".jsonl")).read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    meta = read(folder / (STEM + "_META.json"))
    validate(rows, read(folder / "chang_registry.json"), meta)
    path = folder / (STEM + ".md")
    original = path.read_text(encoding="utf-8-sig")
    rendered = original
    for number, body in sections(rows, meta, original).items():
        pattern = rf"(?ms)^## {number}\. .*?(?=^## {number + 1}\.)"
        rendered, replacements = re.subn(pattern, lambda _: body.rstrip() + "\n\n", rendered)
        if replacements != 1:
            raise ValueError("Expected one section " + str(number))
    if args.write and rendered != original:
        temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
        try:
            temporary.write_text(rendered, encoding="utf-8", newline="\n")
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
    elif rendered != original:
        raise ValueError("Derived Markdown is stale; run with --write after reviewing JSONL changes")
    kinds = Counter(s["kind"] for r in rows for s in r["situations"])
    print(json.dumps({"status": "OK", "stages": len(rows), "clusters": len(grouped(rows)), "situations": sum(kinds.values()),
                      "kinds": dict(kinds), "fact_check_stages": sum(r["fact_check"] for r in rows), "markdown": "rendered" if args.write else "in_sync"}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        run()
    except (ValueError, KeyError, OSError, TypeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        sys.exit(2)
