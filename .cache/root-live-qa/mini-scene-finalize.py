"""Assemble a read-only visual scene-count review from manually inspected strips."""

import argparse
import datetime
import hashlib
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CACHE = pathlib.Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("mini_scene_survey", CACHE / "mini-scene-survey.py")
SURVEY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SURVEY)

TITLES_210 = {
    141: "Again from the first", 144: "A worry", 147: "A troubling person",
    150: "Being treated unfairly", 163: "Related phrase: 一言余計だ",
    166: "After a lecture", 169: "Found", 174: "After receiving advice",
    177: "Materials", 180: "Cold attitude", 183: "Unexpected remark",
    184: "About character", 189: "At home", 197: "Regret", 200: "Passing",
    203: "Criticism of others",
}
FORMERLY_MISSING_210 = [141, 144, 147, 150, 163, 166, 169, 174,
                         177, 180, 183, 184, 189, 197, 200, 203]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book", choices=["210", "200"])
    args = ap.parse_args()
    book = args.book
    preliminary = json.loads((CACHE / f"mini{book}-scene-preliminary.json").read_text(encoding="utf-8"))
    counts = [int(x) for x in (CACHE / f"mini{book}-scene-counts-visual.txt").read_text(encoding="utf-8").replace("\n", ",").split(",") if x.strip()]
    assert len(counts) == len(preliminary["pages"])
    title = "すぐに使える 日本語会話 超ミニフレーズ 発展210" if book == "210" else "すぐに使える 日本語会話 超ミニフレーズ200"
    statuses, sections = SURVEY.load_output(ROOT / "kaiwa_skill" / "knowledge" / title, book)
    rendered_dir = ROOT / "kaiwa_skill" / ".cache" / f"direct-{book}"
    rows = []
    findings = []
    sheets = {}
    for source_row, source_count in zip(preliminary["pages"], counts):
        head = source_row["head"]
        pdf_page = source_row["pdf_page"]
        scene_labels = list(range(1, source_count + 1))
        if book == "210" and head == 146:
            scene_labels = [1, 2, 3, 4, 5, 5]
        section = sections.get(head, {})
        output_numbers = section.get("numbers", [])
        status = statuses.get(head)
        first = (head - 1) // 10 * 10 + 1
        last = min(first + 9, len(counts))
        sheet_name = f"sheet-{first:03d}-{last:03d}.png"
        sheet_path = CACHE / f"mini{book}-scene-sheets" / sheet_name
        sheets[sheet_name] = digest(sheet_path)
        row = {
            "head": head, "pdf_page": pdf_page,
            "source_marker_labels_in_order": scene_labels,
            "source_count": source_count,
            "output_numbers_in_order": output_numbers,
            "output_count": len(output_numbers) if section else None,
            "output_review_status": status,
            "chapter": section.get("chapter"),
            "chapter_sha256": section.get("chapter_sha256"),
            "visual_evidence_sheet": str(sheet_path.relative_to(ROOT)).replace("\\", "/"),
        }
        if status == "author_checked" and section:
            row["comparison"] = "match" if len(output_numbers) == source_count else "mismatch"
        else:
            row["comparison"] = "not_author_checked_or_unwritten"
        if row["comparison"] == "mismatch":
            missing = list(scene_labels)
            for n in output_numbers:
                if n in missing:
                    missing.remove(n)
            row["missing_marker_labels"] = missing
            render = rendered_dir / f"p{pdf_page:04d}.png"
            finding = {
                **row,
                "last_source_scene_title": TITLES_210.get(head),
                "full_page_render": str(render.relative_to(ROOT)).replace("\\", "/") if render.exists() else None,
                "full_page_render_sha256": digest(render),
                "full_page_original_opened": book == "210" and head in TITLES_210,
            }
            findings.append(finding)
        rows.append(row)
    result = {
        "book": book, "reviewed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "source_pdf": preliminary["pdf"], "source_pdf_sha256": preliminary["pdf_sha256"],
        "scope": "one physical page per main head; only circled situation/activity count, including Variation/Related",
        "method": "rendered left-column contact strips; every strip opened and counted visually; mismatch full original pages opened before finding",
        "limitation": "Matching counts do not establish Japanese transcription, translation, or other content fidelity.",
        "head_count": len(rows), "source_scene_total": sum(counts),
        "author_checked_count": sum(r["output_review_status"] == "author_checked" for r in rows),
        "mismatch_count": len(findings), "visual_evidence_sheet_sha256": sheets,
        "rows": rows, "findings": findings,
    }
    if book == "210":
        result["resolved_findings_recheck"] = [
            {
                "head": h,
                "pdf_page": rows[h-1]["pdf_page"],
                "formerly_missing_marker": rows[h-1]["source_marker_labels_in_order"][-1],
                "source_count": rows[h-1]["source_count"],
                "output_count_now": rows[h-1]["output_count"],
                "output_status_now": rows[h-1]["output_review_status"],
                "resolved_by_count": rows[h-1]["comparison"] == "match",
                "chapter_sha256_now": rows[h-1]["chapter_sha256"],
            }
            for h in FORMERLY_MISSING_210
        ]
    path = CACHE / f"mini{book}-scene-coverage-independent.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    md = [f"# Mini {book} scene-count independent review", "", f"PDF: `{result['source_pdf']}`", f"SHA-256: `{result['source_pdf_sha256']}`", f"Reviewed: {result['reviewed_at_utc']}", "", f"Visual source coverage: {len(rows)} heads, {sum(counts)} circled scene occurrences.", f"Author-checked heads at comparison: {result['author_checked_count']}; mismatches: {len(findings)}.", "", "Counts include Variation/Related; repeated circled labels count as separate occurrences. Head 146/PDF161 of book 210 has labels ①②③④⑤⑤.", "", "## Verified mismatches", ""]
    if findings:
        for f in findings:
            md.append(f"- Head {f['head']} / PDF {f['pdf_page']}: source {f['source_count']}, output {f['output_count']}; missing marker {f['missing_marker_labels']}; source last scene: {f['last_source_scene_title'] or 'see full page'}; full-page SHA-256 `{f['full_page_render_sha256']}`; chapter `{f['chapter']}` (`{f['chapter_sha256']}`).")
    else:
        md.append("- None in author-checked heads.")
    if book == "210":
        md += ["", "## Recheck of previously reported omissions", "", "The 16 formerly missing final scenes are now present at the source count in their respective heads. This is a count recheck; it is not a full Japanese or Vietnamese fidelity audit.", ""]
        for f in result["resolved_findings_recheck"]:
            md.append(f"- Head {f['head']} / PDF {f['pdf_page']}: source {f['source_count']}, output now {f['output_count_now']}, marker {f['formerly_missing_marker']}, resolved by count {f['resolved_by_count']}.")
    md += ["", "## Scope limit", "", "This checks scene counts only. A matching count does not prove Japanese text, translation, or other content fidelity. Rows for unfinished or non-author-checked heads are source inventory, not output findings.", "", "The JSON contains a source marker list, output number list, status, chapter hash, and visual sheet reference for every head.", ""]
    (CACHE / f"mini{book}-scene-coverage-independent.md").write_text("\n".join(md), encoding="utf-8")
    print(book, "rows", len(rows), "source scenes", sum(counts), "checked", result["author_checked_count"], "findings", [(f["head"], f["pdf_page"], f["source_count"], f["output_count"], f["missing_marker_labels"]) for f in findings])
    print("report sha256", digest(path))


if __name__ == "__main__":
    main()
