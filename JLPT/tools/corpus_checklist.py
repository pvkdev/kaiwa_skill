"""Build an offline inventory from the latest SingleFile audit and canonical packages."""
import argparse
from collections import Counter, defaultdict
import json
import os
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "contracts/v1"))
from jlpt_coverage import coverage
from validate_package import sha256, source_snapshot
sys.path.insert(0, str(ROOT / ".agents/skills/jlpt-exam-ingest/scripts"))
from audit_sources import audit_page


def write_report(path, text):
    with NamedTemporaryFile(dir=path.parent, suffix=".tmp", delete=False) as stream:
        tmp = Path(stream.name)
        stream.write(text.encode("utf-8"))
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def inventory(root):
    audit = json.loads((root / "reports/source-gaps.json").read_bytes())
    periods = defaultdict(list)
    unmatched = []
    for page in audit["pages"]:
        if not page.get("period"):
            unmatched.append(page["path"])
        else:
            periods[(page["level"], page["period"])].append(page)
    packages = {(p.parent.parent.name, p.parent.name): p for p in (root / "packages").glob("*/*/package.json")}
    masters = defaultdict(list)
    for path in root.glob("N[1-5]/*/*"):
        if path.parent.name.lower() in ("old", "sample") or not path.is_file():
            continue
        match = re.fullmatch(r"JLPT-(N[1-5])-(\d{4}-(?:07|12))\.(?:mp3|m4a|wav|ogg|flac)", path.name, re.I)
        if match and match[1].upper() == path.parent.parent.name:
            masters[match[1].upper(), match[2]].append(path.relative_to(root).as_posix())
    exams = []
    for level, period in sorted(periods.keys() | packages.keys() | masters.keys()):
        pages = periods[level, period]
        path = packages.get((level, period))
        package = json.loads(path.read_bytes()) if path else None
        for s in (package or {}).get("sources", []):
            if s["sourceId"] not in ("written", "listening") or any(p.get("section") == s["sourceId"] for p in pages):
                continue
            # The admin may move a capture to old/ after freezing a package.
            try:
                archived = source_snapshot(root, s)
            except ValueError:
                continue
            if sha256(archived) == s["sha256"]:
                saved = audit_page(root, archived, list(archived.parent.glob("*.mp3")))
                if (saved.get("level"), saved.get("period"), saved.get("section")) == (level, period, s["sourceId"]):
                    pages.append(saved)
        captures = Counter(p["section"] for p in pages)
        evidence = {p["section"]: p["sha256"] for p in pages}
        declared = {s["sourceId"]: s["sha256"] for s in package["sources"]
                    if s["sourceId"] in ("written", "listening")} if package else {}
        resolved_keys = set()
        scripts = set()
        if package:
            nodes = {n["nodeId"]: (n.get("sourceId"), n.get("locator")) for n in package["annotations"]["nodes"]}
            for answer in package["annotations"]["answers"]:
                if answer["resolvedChoiceId"] and answer["resolution"] != "unresolved":
                    resolved_keys.add(nodes.get(answer["questionId"]))
            for m in package["content"]["choukai"]["mondais"]:
                for b in m["blocks"]:
                    shared = any(i.get("audio", {}).get("scriptJaMd", "").strip() for i in b["mediaItems"])
                    for q in b["questions"]:
                        if shared or (q.get("jlptListenScript") or {}).get("scriptJaMd", "").strip():
                            scripts.add(nodes.get(q["id"]))
        scope = "written" if (level, period) == ("N3", "2015-07") and not captures["listening"] else "full"
        master = (package or {}).get("masterAudio") or {}
        playable = master.get("assetId") or master.get("rss")
        local = masters[level, period]
        gaps = []
        for part in (("written",) if scope == "written" else ("written", "listening")):
            if captures[part] != 1:
                gaps.append({"owner": "admin" if not captures[part] else "editor", "field": part,
                             "detail": "thiếu HTML" if not captures[part] else "có nhiều HTML cần đối chiếu"})
        for page in pages:
            part = page.get("section")
            current = declared.get(part) == page["sha256"]
            if page.get("issue"):
                gaps.append(dict(owner="editor", field="capture", detail=page["issue"], path=page["path"]))
            for group in page.get("unverifiedKeys", []):
                pending = [q for q in group["questions"] if not current or (part, "#" + q) not in resolved_keys]
                if pending:
                    gaps.append(dict(owner="source", field="answer", path=page["path"],
                                     mondai=group["mondai"], questions=pending))
            if page["section"] == "listening":
                local = sorted(set(local) | {p for p in page.get("masterAudioCandidates", [])
                               if Path(p).parent == Path(page["path"]).parent and (root / p).is_file()})
                if not local and not playable:
                    gaps.append(dict(owner="admin", field="master", path=page["path"]))
                for group in page.get("requestScript", []):
                    pending = [q for q in group["questions"] if not current or (part, "#" + q) not in scripts]
                    if pending:
                        gaps.append(dict(owner="audio" if local or playable else "admin", field="sourceScript",
                                         path=page["path"], mondai=group["mondai"], questions=pending))
        counts = {}
        if package:
            counts, content_gaps = coverage(package)
            for gap in content_gaps:
                if gap["field"] == "master" and local:
                    gap["owner"] = "editor"
            gaps.extend(content_gaps)
            if declared != evidence:
                gaps.append(dict(owner="editor", field="sourceRevision", detail="So sánh nguồn hiện tại với revision đã đóng gói"))
            if package["review"]["status"] != "approved":
                gaps.append(dict(owner="editor", field="review", detail=package["review"]["status"]))
            for issue in package["review"]["issues"]:
                if issue["severity"] == "error" and not issue["code"].startswith("COVERAGE_"):
                    gaps.append(dict(owner="admin" if issue["code"] == "VERIFY_SOURCE_TEXT" else "editor",
                                     field=issue["code"], targetId=issue["targetId"], detail=issue["message"]))
        else:
            gaps.append(dict(owner="editor", field="package", detail="Biên soạn gói từ nguồn"))
        exams.append(dict(level=level, slug=period.replace("-", "/"), scope=scope,
                          status="incomplete" if gaps else "complete",
                          package=path.relative_to(root).as_posix() if path else None,
                          revision=package["revision"] if package else None, counts=counts,
                          audioUrl=(master.get("rss") or {}).get("enclosureUrl"),
                          localAudio=local,
                          scopeEvidence="N3/1507/KIEM_TRA.md" if scope == "written" else None,
                          sources=[dict(path=p["path"], sha256=p["sha256"], part=p["section"],
                                        questions=p["questionCount"],
                                        unverifiedKeys=p.get("unverifiedKeys", []), missingScript=p.get("requestScript", []),
                                        missingExplanations=p.get("missingSourceExplanations", []),
                                        missingVi=p.get("missingScannedTranslationLines", []),
                                        missingCue=p.get("unverifiedTiming", [])) for p in pages], gaps=gaps))
    return dict(version=1, exams=exams, unclassified=unmatched)


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=ROOT)
    root = cli.parse_args().root.resolve()
    report = inventory(root)
    lines = ["# Kho đề JLPT", "", "Số câu lấy từ lần kiểm kê HTML gần nhất. Nếu một bản đã chuyển vào old/, dùng đúng bản trùng SHA của gói. Trạng thái hoàn thành yêu cầu gói đã duyệt, khớp nguồn và đủ các mục áp dụng.",
             "Mỗi thiếu sót theo file, mondai, câu hoặc dòng nằm trong [checklist JSON](exam-checklist.json).",
             "", "| Cấp | Kỳ | Câu viết | Câu nghe | Gói | Trạng thái |", "|---|---|---:|---:|---|---|"]
    admin = []
    for exam in report["exams"]:
        sizes = Counter()
        for page in exam["sources"]:
            sizes[page["part"]] += page["questions"]
        package = f"[r{exam['revision']}](../{exam['package']})" if exam["package"] else "Chờ biên soạn"
        listen = sizes["listening"] if exam["scope"] == "full" else "Nguồn chỉ có phần viết"
        state = "Hoàn thành" if exam["status"] == "complete" else "Còn thiếu"
        lines.append(f"| {exam['level']} | {exam['slug']} | {sizes['written']} | {listen} | {package} | {state} |")
        requested = [gap for gap in exam["gaps"] if gap["owner"] == "admin"]
        has_master_request = any(gap["field"] == "master" for gap in requested)
        if has_master_request:
            missing_scripts = [q for gap in requested if gap["field"] == "sourceScript" for q in gap["questions"]]
            detail = f" để khôi phục script cho {len(missing_scripts)} câu ({missing_scripts[0]} đến {missing_scripts[-1]})" if missing_scripts else ""
            admin.append(f"- {exam['level']} {exam['slug']} · Cần audio tổng{detail}.")
        for gap in requested:
            if gap["field"] in ("master", "rssUrl") or (gap["field"] == "sourceScript" and has_master_request):
                continue
            label = {"written":"Phần viết", "listening":"Phần nghe", "VERIFY_SOURCE_TEXT":"Đối chiếu đề gốc"}.get(gap["field"], gap["field"])
            admin.append(f"- {exam['level']} {exam['slug']} · {label} · {gap.get('path', gap.get('detail', ''))} {' '.join(gap.get('questions', []))}".rstrip())
    needs_feed = any(not exam["audioUrl"] and any(p["part"] == "listening" for p in exam["sources"]) for exam in report["exams"])
    if needs_feed:
        admin.insert(0, "- Điền RSS vào sổ audio sau khi các tập đã được đăng. Tra các tệp chưa khớp trong sổ.")
    lines += ["", "## Admin chuẩn bị", "", *(dict.fromkeys(admin) or ["Đã đủ nguồn được yêu cầu."])]
    for file in report["unclassified"]:
        lines.append(f"- Kiểm tra cấp/kỳ và cấu trúc HTML của `{file}`.")
    write_report(root / "reports/exam-checklist.json", json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    write_report(root / "reports/EXAM_CHECKLIST.md", "\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
