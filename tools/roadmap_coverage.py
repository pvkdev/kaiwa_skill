"""Audit complete source-book coverage and merge independent book allocations."""
import argparse
import hashlib
import json
import os
import tempfile
from collections import defaultdict
from pathlib import Path
import roadmap_v6 as roadmap

ROOT = roadmap.ROOT
OUT = roadmap.V6


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as f:
        f.write((json.dumps(data, ensure_ascii=False, indent=2)+"\n").encode("utf8"))
        temp = f.name
    os.replace(temp, path)


def signature(selection):
    import re
    return (selection["book_id"], tuple(
        (p["path"], re.sub(r'^<a id="[^"]+"></a>[ \t]*$', "",
                          roadmap.source_bytes(p).decode("utf8").replace("\r\n", "\n"),
                          flags=re.MULTILINE).strip())
        for p in [selection, *selection.get("extra_parts", [])]))


def catalogs(books=None):
    for path in sorted((OUT/"coverage").glob("*.json")):
        if books is None or path.stem in books:
            yield path, roadmap.read(path)


def merge(selected_books=None):
    decisions = {p.stem: roadmap.read(p) for p in (OUT/"decisions").glob("*.json")}
    catalog_list = list(catalogs(selected_books))
    complete_packs = defaultdict(list)
    for _, cat in catalog_list:
        for pack in cat["packs"]:
            complete_packs[cat["book_id"]].append(pack["selection"])
    line_cache, required_cache = {}, {}
    def contains(container, fragment):
        parent_parts = [container, *container.get("extra_parts", [])]
        for child in [fragment, *fragment.get("extra_parts", [])]:
            matching = [p for p in parent_parts if p["path"] == child["path"]]
            if not matching:
                return False
            key = (child["path"], child["start_line"], child["end_line"])
            if key not in required_cache:
                if child["path"] not in line_cache:
                    line_cache[child["path"]] = (ROOT / child["path"]).read_text("utf-8-sig").splitlines()
                lines = line_cache[child["path"]]
                required_cache[key] = [i for i in range(child["start_line"], child["end_line"]+1)
                                       if lines[i-1].strip() and not lines[i-1].startswith('<a id=')]
            required = required_cache[key]
            if required and any(p["start_line"] <= required[0] and p["end_line"] >= required[-1]
                                for p in matching):
                continue
            if not all(any(p["start_line"] <= i <= p["end_line"] for p in matching) for i in required):
                return False
        return True
    # Upgrade historical single-anchor selections to the actual complete audio unit.
    for decision in decisions.values():
        upgraded = []
        for old in decision["selections"]:
            possible = [s for s in complete_packs[old["book_id"]] if contains(s, old)]
            if possible:
                full = min(possible, key=lambda s: sum(p["end_line"]-p["start_line"]+1
                           for p in [s, *s.get("extra_parts", [])]))
                revised = full.copy()
                revised["situation_ids"] = old["situation_ids"]
                note = " Học trọn đơn vị bổ trợ, gồm các ví dụ khác bối cảnh trong cùng pack."
                revised["fit_vi"] = old["fit_vi"].replace(note, "")
                if note in old["fit_vi"] or signature(full) != signature(old):
                    revised["fit_vi"] += note
            else:
                revised = old
            previous = next((s for s in upgraded if signature(s) == signature(revised)), None)
            if previous:
                previous["situation_ids"] = list(dict.fromkeys(previous["situation_ids"]+revised["situation_ids"]))
            else:
                upgraded.append(revised)
        decision["selections"] = upgraded
    existing = {}
    for decision in decisions.values():
        for selection in decision["selections"]:
            existing.setdefault(signature(selection), selection)
    appended = 0
    for _, catalog in catalog_list:
        for pack in catalog["packs"]:
            code = pack["stage_code"]
            decision = decisions[code]
            selection = pack["selection"].copy()
            sig = signature(selection)
            if sig in existing:
                canonical = existing[sig]
                for key in ("pack_id", "unit_id", "path", "sha256", "start_line", "end_line",
                            "extra_parts", "title_ja", "source_number_prefix"):
                    if key in canonical:
                        selection[key] = canonical[key]
                    else:
                        selection.pop(key, None)
            if any(signature(s) == sig for s in decision["selections"]):
                continue
            decision["selections"].append(selection)
            decision["selections"].sort(key=lambda s: s["kind"] != "speak_japanese")
            decision["search_notes"].append("Bổ sung từ kiểm kê toàn sách "+catalog["book_id"]+
                                            ": "+selection["pack_id"]+". "+selection["fit_vi"])
            existing.setdefault(sig, selection)
            appended += 1
    for code, decision in decisions.items():
        roadmap.check(decision)
    for code, decision in decisions.items():
        write(OUT/"decisions"/(code+".json"), decision)
    print("Added placements", appended)


def audit(selected_books=None):
    policy, _, books = roadmap.inputs()
    expected = selected_books or policy["coverage_books"]
    actual = {d["book_id"]: d for _, d in catalogs(expected)}
    missing = sorted(set(expected)-set(actual))
    placed = defaultdict(list)
    for path in (OUT/"decisions").glob("*.json"):
        decision = roadmap.read(path)
        for s in decision["selections"]:
            placed[signature(s)].append(decision["display_code"])
    result = {"version": policy["version"], "missing_catalogs": missing, "books": []}
    for bid in expected:
        if bid not in actual:
            continue
        cat = actual[bid]
        directory = ROOT/books[bid]["directory"]
        chapters = {p.relative_to(ROOT).as_posix():p for p in (directory/"chapters").glob("*.md")}
        declared = {x["path"]:x for x in cat["chapters"]}
        roadmap.require(chapters.keys() == declared.keys(), bid+": thiếu hoặc sai chương kiểm kê")
        covered, excluded = defaultdict(set), defaultdict(set)
        unmapped = []
        for pack in cat["packs"]:
            s = pack["selection"]
            roadmap.require(s["book_id"] == bid, "Pack sai sách")
            if pack["stage_code"] not in placed[signature(s)]:
                unmapped.append(s["pack_id"])
            for part in [s, *s.get("extra_parts", [])]:
                roadmap.check_part(part, books[bid])
                covered[part["path"]].update(range(part["start_line"], part["end_line"]+1))
        for exc in cat["exclusions"]:
            roadmap.require(exc["path"] in chapters and exc.get("reason") and exc.get("category"),
                            "Phạm vi loại thiếu nguồn/lý do")
            size = len(chapters[exc["path"]].read_text("utf-8-sig").splitlines())
            roadmap.require(1 <= exc["start_line"] <= exc["end_line"] <= size, "Dòng loại ngoài nguồn")
            excluded[exc["path"]].update(range(exc["start_line"],exc["end_line"]+1))
        gaps, total, retained, administrative = [], 0, 0, 0
        for path, chapter in chapters.items():
            roadmap.require(hashlib.sha256(chapter.read_bytes()).hexdigest()==declared[path]["sha256"],
                            "Chapter hash changed: "+path)
            lines = chapter.read_text("utf-8-sig").splitlines()
            substantive = {i for i,line in enumerate(lines,1) if line.strip() and not line.startswith('<a id=')}
            # Excluded administrative text is reported separately.
            learn = substantive - excluded[path]
            total += len(learn)
            retained += len(learn & covered[path])
            administrative += len(substantive & excluded[path])
            absent = sorted(learn-covered[path])
            if absent:
                ranges = []
                for i in absent:
                    if ranges and ranges[-1][1]+1 == i:
                        ranges[-1][1] = i
                    else:
                        ranges.append([i,i])
                gaps.append({"path":path,"ranges":ranges})
        result["books"].append({"book_id":bid,"book_title":books[bid]["title"],
                                "pack_count":len(cat["packs"]),
                                "educational_support":sum(p["selection"].get("pack_scope") == "educational_support" for p in cat["packs"]),
                                "learning_lines":total,
                                "covered_learning_lines":retained,
                                "excluded_administrative_lines":administrative,
                                "coverage_percent":round(100*retained/total,3) if total else 0,
                                "unmapped_packs":unmapped,"uncovered":gaps})
    result["complete"] = not missing and all(not b["unmapped_packs"] and not b["uncovered"] for b in result["books"])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command",choices=["merge","audit","report"])
    parser.add_argument("--books",nargs="+")
    args=parser.parse_args()
    if args.command=="merge":
        merge(args.books)
        return
    report=audit(args.books)
    if args.command=="report":
        write(OUT/"COVERAGE_REPORT.json",report)
        md=["# Báo cáo bao phủ V"+report["version"],"",
            "Kiểm kê nội dung học trong các chương Markdown nguồn hiện có. Các đoạn hành chính/chỉ mục/lặp được kê riêng trong catalog; không dùng tỷ lệ này để tuyên bố các trang PDF thiếu đã được khôi phục hoặc đã nghe lại CD.",""]
        for b in report["books"]:
            md += ["## "+b["book_id"]+" — "+b["book_title"],"",
                   f"{b['pack_count']} bài/pack · {b['covered_learning_lines']}/{b['learning_lines']} dòng nội dung học đã có chỗ trong lộ trình ({b['coverage_percent']}%).",
                   "",f"{b['excluded_administrative_lines']} dòng hành chính hoặc lặp được ghi riêng.",
                   "", "Pack chưa gán: "+str(len(b["unmapped_packs"]))+". Phạm vi còn hở: "+str(len(b["uncovered"]))+".",""]
        (OUT/"COVERAGE_REPORT.md").write_text("\n".join(md)+"\n","utf8",newline="\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report["complete"]:
        raise SystemExit(1)


if __name__=="__main__":
    main()

