"""Build or verify the V6.0 roadmap pilot without publishing a production pointer."""
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import unicodedata
from collections import Counter, defaultdict
from functools import lru_cache
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "kaiwa_skill/planning"
V6 = PLANNING / "v6"
V5 = PLANNING / "v5"
POLICY_PATH = V6 / "SOURCE_POLICY.json"
FILES = {"Sơ": "SO_CAP.md", "Trung": "TRUNG_CAP.md", "Thượng": "THUONG_CAP.md"}
BRANCH = {"routine": "Tiến hành", "misunderstanding": "Hiểu nhầm", "resolved": "Đã xử lý",
          "conditional": "Có điều kiện", "follow_up": "Tiếp nối", "declined": "Từ chối",
          "problem": "Gặp trở ngại", "alternative": "Phương án khác", "pending": "Chờ",
          "accepted": "Đồng ý", "unresolved": "Chưa giải quyết"}


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def rows(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def dumps(obj, pretty=False):
    return json.dumps(obj, ensure_ascii=False, indent=2 if pretty else None,
                      separators=None if pretty else (",", ":"))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def require(test, message):
    if not test:
        raise ValueError(message)


@lru_cache(maxsize=1)
def inputs():
    policy = read(POLICY_PATH)
    base = (V6 / policy["basis"]).resolve()
    require(digest(base.read_bytes()) == policy["basis_sha256"], "V5 đã đổi so với checkpoint.")
    course = rows(base)
    catalog = read(PLANNING / "catalog27/manifest.json")
    books = {book["book_id"]: book for book in catalog["books"]}
    for key, book in policy["supplement"].items():
        books[key] = {**book, "directory": "kaiwa_skill/knowledge/" + book["title"]}
    return policy, course, books


def text_field(obj, key):
    value = obj.get(key)
    require(isinstance(value, str) and value.strip(), "Thiếu trường chữ " + key)
    return value


def list_field(obj, key, nonempty=False):
    value = obj.get(key)
    require(isinstance(value, list) and (not nonempty or len(value)), "Danh sách sai: " + key)
    return value


def check_part(part, book):
    path = (ROOT / text_field(part, "path")).resolve()
    require(path.is_relative_to((ROOT / book["directory"] / "chapters").resolve()),
            f"Locator sai sách: {path}")
    data = path.read_bytes()
    require(digest(data) == part.get("sha256"), f"Source hash thay đổi: {path.name}")
    if book.get("require_stable_clean_unit"):
        directory = ROOT / book["directory"]
        state = read(directory / "_meta/direct-state.json")["chapters"]
        entry = state.get(path.relative_to(directory).as_posix(), {})
        require(entry.get("chapter_sha256") == part["sha256"] and entry.get("status") in
                {"author_checked", "verified"}, "Chương nguồn bổ sung chưa ổn định: " + path.name)
    lines = data.decode("utf-8-sig").splitlines()
    lo, hi = part.get("start_line"), part.get("end_line")
    require(type(lo) is int and type(hi) is int and 1 <= lo <= hi <= len(lines),
            f"Sai dải dòng {lo}–{hi}: {path.name}")
    if book.get("require_stable_clean_unit"):
        # Interview chapter files correspond to printed subsections; keep consecutive discs together.
        require(not any(line.strip() for line in lines[:lo-1] + lines[hi:]),
                "Sách phỏng vấn: chọn trọn mục in có nhiều track.")
    marker = 'id="' + text_field(part, "unit_id") + '"'
    require(any(marker in line for line in lines[max(0, lo-4):hi]), f"Anchor xa đoạn đã chọn: {marker}")


def check(decision):
    policy, course, books = inputs()
    code = text_field(decision, "display_code")
    stage = next((row for row in course if row["display_code"] == code), None)
    require(stage and stage["uid"] == decision.get("stage_uid"), "UID hoặc mã chặng sai: " + code)
    require(code in policy["pilot"], "Ngoài phạm vi quyết định của bản pilot: " + code)
    for key in ("vocabulary_topics", "search_notes"):
        require(all(isinstance(x, str) and x.strip() for x in list_field(decision, key, True)),
                f"{code}: {key} cần nội dung")
    situations = {s["id"] for s in stage["situations"]}
    seen, units = set(), set()
    independent = False
    for s in list_field(decision, "selections"):
        kind = s.get("kind")
        require(kind in ("speak_japanese", "shadowing_pack"), "Vai trò không hợp lệ")
        require(kind != "speak_japanese" or not independent, "Sai thứ tự Speak Japanese")
        independent = kind == "shadowing_pack"
        bid = text_field(s, "book_id")
        require(bid in policy[kind] and bid in books, f"Nguồn {bid} không dùng cho {kind}")
        book = books[bid]
        require(s.get("book_title") == book["title"], f"{bid}: sai tên sách")
        for key in ("pack_id", "title_ja", "title_vi", "fit_vi", "difficulty_vi", "boundary", "audio_note"):
            text_field(s, key)
        require(s.get("read_status") == "whole_unit_read", "Ứng viên chưa đọc trọn")
        check_part(s, book)
        for p in s.get("extra_parts", []):
            check_part(p, book)
        if bid == "INTERVIEW":
            labels = []
            for part in [s, *s.get("extra_parts", [])]:
                source = (ROOT / part["path"]).read_text(encoding="utf-8-sig").splitlines()
                labels.extend(re.findall(r"^#+[^\n]*DISC\s+(\d+)\s*/\s*(\d+)",
                                         "\n".join(source[part["start_line"]-1:part["end_line"]]),
                                         flags=re.MULTILINE | re.IGNORECASE))
            audio = [(str(a["disc"]).upper(), str(a["track"])) for a in s["audio"]]
            require(labels and audio == [("DISC "+disc, track) for disc, track in labels],
                    "Sách phỏng vấn: danh sách nhãn audio cần đủ, đúng thứ tự mục in.")
        ref = (bid, s["pack_id"])
        unit = (bid, s["path"], s["unit_id"], s["start_line"], s["end_line"])
        require(ref not in seen and unit not in units, f"Trùng pack trong {code}: {ref}")
        seen.add(ref)
        units.add(unit)
        ids = list_field(s, "situation_ids", True)
        require(set(ids) <= situations and len(ids) == len(set(ids)), f"{code}: sai tình huống {ids}")
        for audio in list_field(s, "audio"):
            text_field(audio, "locator")
            require({"disc", "track"} <= audio.keys(), "Thiếu trường disc/track")
    for c in list_field(decision, "considerations"):
        require(c.get("book_id") in books and c.get("status") in ("deferred", "unsuitable"),
                "Sai ứng viên xem xét")
        for key in ("locator", "reason"):
            text_field(c, key)


def find_units(keyword, book_id):
    policy, _, books = inputs()
    def fold(text):
        return unicodedata.normalize("NFKC", text).casefold()
    for bid in dict.fromkeys(policy["speak_japanese"] + policy["shadowing_pack"]):
        if book_id and book_id != bid:
            continue
        meta = ROOT / books[bid]["directory"] / "_meta/units.jsonl"
        if not meta.exists():
            continue
        for unit in rows(meta):
            if fold(keyword) in fold(unit["heading"] + " " + unit["unit_id"]):
                print(bid, unit["unit_id"], unit["heading"], unit["chapter"], sep=" | ")


def blocks(stage, decision):
    def node(kind, **fields):
        return {"type": kind, **fields}
    result = [node("vocabulary_topics", topics=decision["vocabulary_topics"] if decision else [])]
    for s in decision["selections"] if decision else []:
        ref = {"book_id": s["book_id"], "pack_id": s["pack_id"]}
        if s["kind"] == "speak_japanese":
            result.extend([node("speak_japanese_video", **ref), node("speak_japanese_examples", **ref)])
        else:
            result.append(node("independent_shadowing", **ref))
    result.extend([node("stage_lecture", status="planned"),
                   node("v5_situations", situation_ids=[s["id"] for s in stage["situations"]]),
                   node("live_challenges", status="deferred"), node("free_kaiwa", status="planned")])
    return result


def locator(part):
    relative = os.path.relpath(ROOT / part["path"], V6).replace(os.sep, "/")
    return f"[{part['unit_id']}, dòng {part['start_line']}–{part['end_line']}]({quote(relative)}#{quote(part['unit_id'])})"


def selected_md(s, stage):
    situations = {c["id"]: c["title"] for c in stage["situations"]}
    aud = " · ".join(" ".join(str(x) for x in (a["disc"], a["track"]) if x is not None)
                     + " (" + a["locator"] + ")" for a in s["audio"])
    return [f"##### {s['title_vi']}", "", f"**{s['book_id']} · {s['book_title']}** — {s['title_ja']}", "",
            s["fit_vi"], "", "**Độ khó.** " + s["difficulty_vi"], "",
            "**Tình huống.** " + " · ".join(f"{i} {situations[i]}" for i in s["situation_ids"]), "",
            "**Phạm vi.** " + s["boundary"], "", "**Tra sách.** " +
            " · ".join(locator(p) for p in [s, *s.get("extra_parts", [])]), "",
            "**Audio.** " + (aud + ". " if aud else "") + s["audio_note"], ""]


def stage_md(stage):
    a = stage["v6"]
    lines = [f"### {stage['display_code']} — {stage['title']}", "", stage["objective"], ""]
    decision = a["decision"]
    if decision:
        lines += ["**Nhóm từ theo topic.** " + " · ".join(decision["vocabulary_topics"]), ""]
        for kind, title in (("speak_japanese", "Speak Japanese · mỗi bài có video rồi luyện nguyên ví dụ"),
                            ("shadowing_pack", "Shadowing độc lập · một pack một node")):
            lines += ["#### " + title, ""]
            selected = [s for s in decision["selections"] if s["kind"] == kind]
            for s in selected:
                lines += selected_md(s, stage)
            if not selected:
                lines += ["Đã xét nguồn. Chưa chọn bài cho phần này.", ""]
    else:
        lines += ["*Chưa phân bổ nguồn ở V6.0.*", ""]
    lines += ["**Trọng tâm cho bài giảng.** " + " · ".join(stage["knowledge_focus"]), ""]
    for event in stage["events"]:
        lines += [f"#### {event['id']} — {event['name']}", "", "Vai: " + " ↔ ".join(event["roles"]), ""]
        for c in stage["situations"]:
            if c["event_id"] == event["id"]:
                parent = " · tiếp từ " + ", ".join(c["continues_from"]) if c.get("continues_from") else ""
                lines.append(f"- {c['id']} · {BRANCH[c['branch']]} · {c['title']}{parent}")
        lines.append("")
    lines += [stage["coverage_note"], "", "Sau thực hành: challenge tổng hợp → một free Kaiwa cuối chặng.", ""]
    if decision:
        lines += ["#### Sổ chọn nguồn", "", *("- " + n for n in decision["search_notes"]), ""]
        for c in decision["considerations"]:
            lines.append(f"- {c['book_id']} · {c['locator']} · {c['reason']} ({c['status']})")
        lines.append("")
    return lines


def preview(course):
    # No server or external resources needed on mobile. Details open on demand.
    page = ['<!doctype html><html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
            '<title>Lộ trình Kaiwa V6.0</title><style>html{color-scheme:light dark}body{max-width:58rem;margin:auto;padding:1rem;font:1rem/1.6 system-ui}summary{cursor:pointer;font-weight:650;padding:.7rem 0}details{border-bottom:1px solid #8886}article{padding-left:1rem}small{opacity:.85}select,input{font:inherit;margin:.3rem;padding:.45rem;max-width:90%}h3{margin-bottom:0}</style>',
            '<h1>Lộ trình Kaiwa V6.0</h1><p>Chọn chặng để xem theo thứ tự học. Mở mục nguồn để đối chiếu sách và CD.</p>',
            '<label>Cấp <select id="level"><option value="">Tất cả</option>' +
            ''.join('<option>'+escape(l)+'</option>' for l in FILES) + '</select></label>',
            '<label><input id="only" type="checkbox" checked>Chỉ chặng pilot</label>']
    for s in course:
        d = s["v6"]["decision"]
        e = escape
        page.append(f'<details class="stage" data-level="{e(s["level"])}" data-pilot="{int(d is not None)}"><summary>{e(s["display_code"])} · {e(s["title"])}</summary><article><small>{e(s["cluster_title"])}</small><p>{e(s["objective"])}</p>')
        if d:
            page.append('<h3>Từ vựng theo topic</h3><p>' + e(" · ".join(d["vocabulary_topics"])) + '</p>')
            for x in d["selections"]:
                pair = x["kind"] == "speak_japanese"
                page.append('<h3>' + ('Video · ' if pair else 'Shadowing · ') + e(x["title_vi"]) + '</h3>')
                if pair:
                    page.append('<p>Tiếp theo · Shadowing toàn bộ ví dụ của bài</p>')
                page.append('<details><summary>Nguồn và lý do chọn</summary><p>' +
                            e(x["book_id"]+" · "+x["book_title"]+" · "+x["title_ja"]) + '</p><p>' +
                            e(x["fit_vi"]+" "+x["difficulty_vi"]) + '</p><p>' + e(x["boundary"]) + '</p><p>' +
                            e(" · ".join(str(a.get("disc") or "")+" "+str(a.get("track") or "")+" "+a["locator"] for a in x["audio"])) +
                            ' ' + e(x["audio_note"]) + '</p><p>' + e(", ".join(x["situation_ids"])) + '</p></details>')
        else:
            page.append('<p>Chưa phân bổ nguồn ở V6.0.</p>')
        page.append('<h3>Bài giảng tổng hợp · dự kiến</h3><p>' + e(" · ".join(s["knowledge_focus"])) + '</p>')
        for ev in s["events"]:
            page.append('<h3>' + e(ev["name"]) + '</h3><ul>')
            for c in s["situations"]:
                if c["event_id"] == ev["id"]:
                    page.append('<li>' + e(c["id"]+" · "+c["title"]) + '</li>')
            page.append('</ul>')
        page.append('<p>Challenge Live AI → Free Kaiwa cuối chặng</p></article></details>')
    page += ['<script>const level=document.querySelector("#level"),only=document.querySelector("#only");function filter(){for(const s of document.querySelectorAll(".stage"))s.hidden=(level.value&&s.dataset.level!==level.value)||(only.checked&&s.dataset.pilot!=="1")}level.onchange=only.onchange=filter;filter()</script></html>']
    return "\n".join(page)


def artifacts():
    policy, base, books = inputs()
    decisions = {}
    for path in sorted((V6 / "decisions").glob("*.json")):
        d = read(path)
        check(d)
        require(path.stem == d["display_code"], "Tên file sai mã chặng")
        decisions[path.stem] = d
    require(set(decisions) == set(policy["pilot"]), "Chưa đủ chính xác tập pilot đã giao.")
    course, reverse = [], defaultdict(list)
    boundaries = {}
    pack_by_location = {}
    counts = Counter()
    for original in base:
        code = original["display_code"]
        d = decisions.get(code)
        stage = {**original, "v6": {"version": policy["version"],
                                    "assignment_status": "reviewed" if d else "not_reviewed",
                                    "decision": d, "learning_order": blocks(original, d)}}
        course.append(stage)
        for s in d["selections"] if d else []:
            key = (s["book_id"], s["pack_id"])
            location = tuple((p["path"], p["unit_id"], p["start_line"], p["end_line"])
                             for p in [s, *s.get("extra_parts", [])])
            require(boundaries.setdefault(key, location) == location, f"Pack trùng ID khác ranh giới: {key}")
            require(pack_by_location.setdefault(location, key) == key, f"Cùng phần nguồn bị gán hai ID: {key}")
            reverse[key].append(code)
            counts[s["kind"]] += 1
    files = {"KAIWA_CHANG_V6_0.jsonl": "\n".join(dumps(s) for s in course)}
    pilot_reader = ["# Pilot phân bổ nguồn Kaiwa V6.0", "", "Ba chặng để duyệt trước khi phân bổ đại trà. Mỗi bài Speak Japanese đi kèm một node luyện ví dụ. Mỗi pack độc lập là một node.", ""]
    for level, filename in FILES.items():
        lines = ["# Kaiwa V6.0 — " + level, "", "Lộ trình nghe nói · bản phân bổ pilot. Các UID và tình huống kế thừa từ V5.", ""]
        prev = None
        for s in (x for x in course if x["level"] == level):
            if prev != s["cluster_id"]:
                lines += ["## "+s["cluster_id"]+" — "+s["cluster_title"], ""]
                prev = s["cluster_id"]
            detail = stage_md(s)
            lines += detail
            if s["v6"]["decision"]:
                pilot_reader += detail
        files[filename] = "\n".join(lines)
    files["PILOT.md"] = "\n".join(pilot_reader)
    index = ["# Tra từ sách đến chặng · V6.0", "", "Chỉ phản ánh các chặng đã đọc ở pilot.", ""]
    for bid in dict.fromkeys(policy["speak_japanese"] + policy["shadowing_pack"]):
        index += ["## " + bid + " — " + books[bid]["title"], ""]
        entries = [(key, codes) for key, codes in sorted(reverse.items()) if key[0] == bid]
        for (_, pack), codes in entries:
            index.append("- " + pack + " → " + ", ".join(codes))
        if not entries:
            index.append("Chưa có đơn vị được chọn trong pilot.")
        index.append("")
    files["KAIWA_CHANG_V6_0.md"] = "\n".join([
        "# Kaiwa V6.0 — Khung lộ trình và pilot phân bổ nguồn", "",
        f"{len(course)} chặng · {len(decisions)} chặng đã xét · {len(course)-len(decisions)} chặng chờ phân bổ.",
        "", "[Mở pilot theo thứ tự học](PILOT.md) · [Xem lộ trình trên trình duyệt](ROADMAP.html)",
        "", "[Sơ](SO_CAP.md) · [Trung](TRUNG_CAP.md) · [Thượng](THUONG_CAP.md)",
        "", "[Yêu cầu gốc](CHECKPOINT_YEU_CAU.md) · [Tra ngược theo sách](TRA_THEO_SACH.md) · [Trạng thái](STATUS.json)",
        "", "Hai bước Speak Japanese và shadowing là quyết định chọn nội dung. Các bài giảng và nhiệm vụ Live sẽ được thiết kế ở giai đoạn sau.",
        "", *[f"- {code} — {next(row['title'] for row in course if row['display_code']==code)}" for code in policy["pilot"]]
    ])
    files["TRA_THEO_SACH.md"] = "\n".join(index)
    files["ROADMAP.html"] = preview(course)
    files["STATUS.json"] = dumps({"version": policy["version"], "state": "awaiting_pilot_review",
                                  "basis_sha256": policy["basis_sha256"], "stages": len(course),
                                  "clusters": len({s["cluster_id"] for s in course}),
                                  "events": sum(len(s["events"]) for s in course),
                                  "situations": sum(len(s["situations"]) for s in course),
                                  "reviewed": list(decisions), "not_reviewed": len(course)-len(decisions),
                                  "assignment_occurrences": dict(counts), "unique_book_pack_keys": len(reverse),
                                  "next_action": "Chờ người dùng duyệt pilot trước khi giao ba worker Sol/high cho V6.1."}, True)
    return {name: (value.rstrip()+"\n").encode("utf8") for name, value in files.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build")
    sub.add_parser("verify")
    sub.add_parser("check-one").add_argument("file", type=Path)
    find = sub.add_parser("find")
    find.add_argument("keyword")
    find.add_argument("--book")
    args = parser.parse_args()
    if args.cmd == "find":
        find_units(args.keyword, args.book)
        return
    if args.cmd == "check-one":
        check(read(args.file))
        print("OK", args.file)
        return
    outputs = artifacts()
    if args.cmd == "build":
        # Validate the full set before writing. Interruption is recoverable with build + verify.
        for name, contents in outputs.items():
            with tempfile.NamedTemporaryFile(dir=V6, delete=False) as f:
                f.write(contents)
                tmp = f.name
            os.replace(tmp, V6 / name)
    for name, contents in outputs.items():
        require((V6 / name).read_bytes() == contents, "Cần dựng lại " + name)
    actual = rows(V6 / "KAIWA_CHANG_V6_0.jsonl")
    for s in actual:
        del s["v6"]
    require(actual == inputs()[1], "Nội dung hoặc thứ tự V5 sai lệch")
    print(outputs["STATUS.json"].decode("utf8"))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError) as exc:
        sys.exit(str(exc))
