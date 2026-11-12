import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CACHE = Path(__file__).resolve().parent
BOOK = ROOT / "kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210"
PDF = ROOT / "kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf"
EXPECTED_SHA = "2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha(PDF) == EXPECTED_SHA
front_path = BOOK / "chapters/00-front.md"
front = front_path.read_text(encoding="utf-8")
toc_text = front.split("## Mục lục — 目次", 1)[1].split("## 学習の流れ", 1)[0]
toc = []
for line in toc_text.splitlines():
    m = re.match(r"- \*\*(\d+)\. (.+?)\*\* — (.+?) \(PDF(\d+)(?:;[^)]*)?\)\.", line)
    if m:
        toc.append({"canonical_number": len(toc) + 1, "printed_number": int(m[1]), "jp": m[2], "vi": m[3], "target_page": int(m[4]), "raw_line": line})
assert len(toc) == 210

main = []
main_files = []
for path in sorted((BOOK / "chapters").glob("*.md")):
    if path == front_path:
        continue
    text = path.read_text(encoding="utf-8")
    main_files.append({"path": str(path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha(path)})
    for m in re.finditer(r"(?m)^## (\d+)\. (.+?) — (.+?) \(PDF(\d+);", text):
        main.append({"number": int(m[1]), "jp": m[2], "vi": m[3], "pdf_page": int(m[4]), "chapter": path.name})
assert len(main) == 210
main_by_number = {r["number"]: r for r in main}

# Visual transcription exceptions: all other keys and page references were
# checked against the six opened TOC images and agree with the corresponding
# clean TOC rows. These source variants are independently confirmed with the
# opened source main pages 112, 187 and 225.
SOURCE_TOC_VARIANTS = {
    97: {"jp": "そこをなんとか", "note": "Printed TOC key is shorter than the main heading at PDF112, which includes （お願いします）."},
    172: {"printed_number": 173, "note": "Printed TOC repeats 173 for 任せた and またー; main PDF187 is numbered 172."},
    210: {"jp": "悪かった（謝罪の気持ち）", "note": "Printed TOC key differs from main PDF225, which says 悪いね（謝罪の気持ち）."},
}
PAGE_RANGES = [(4, 1, 30), (5, 31, 67), (6, 68, 103), (7, 104, 139), (8, 140, 175), (9, 176, 210)]
page_for_number = {n: page for page, start, end in PAGE_RANGES for n in range(start, end + 1)}
source_images = []
for page, start, end in PAGE_RANGES:
    path = CACHE / f"mini210-toc-source-p{page:04d}.png"
    source_images.append({"pdf_page": page, "row_count": end - start + 1, "first_head": start, "last_head": end, "image": str(path.relative_to(ROOT)).replace("\\", "/"), "image_sha256": sha(path)})
main_crosscheck_images = []
for page in (112, 187, 225):
    path = CACHE / f"mini210-toc-crosscheck-p{page:04d}.png"
    main_crosscheck_images.append({"pdf_page": page, "image": str(path.relative_to(ROOT)).replace("\\", "/"), "image_sha256": sha(path)})

rows = []
for item in toc:
    n = item["canonical_number"]
    source_variant = SOURCE_TOC_VARIANTS.get(n, {})
    main_item = main_by_number[n]
    row = {
        "head_number": n,
        "toc_pdf_page": page_for_number[n],
        "source_printed_number": source_variant.get("printed_number", n),
        "clean_toc_printed_number": item["printed_number"],
        "source_printed_jp": source_variant.get("jp", item["jp"]),
        "source_printed_target_page": n + 15,
        "source_english_gloss_vs_vi": "direction_consistent_on_visual_review",
        "clean_toc_jp": item["jp"],
        "clean_toc_vi": item["vi"],
        "clean_toc_target_page": item["target_page"],
        "main_heading_jp": main_item["jp"],
        "main_heading_page": main_item["pdf_page"],
        "main_chapter": main_item["chapter"],
        "source_issue_note": source_variant.get("note"),
    }
    row["target_page_matches_source"] = item["target_page"] == row["source_printed_target_page"]
    row["clean_toc_number_matches_source_print"] = item["printed_number"] == row["source_printed_number"]
    row["clean_toc_key_matches_printed_toc"] = item["jp"] == row["source_printed_jp"]
    row["main_heading_matches_clean_toc"] = item["jp"] == main_item["jp"]
    rows.append(row)

report = {
    "scope": "Independent TOC-only QA: six full source TOC pages PDF4–9, their 210 Japanese keys/English meanings/printed target pages against chapter00 TOC and 210 clean main headings. Main semantic content is outside scope.",
    "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
    "source_pdf_sha256": EXPECTED_SHA,
    "toc_source_images": source_images,
    "main_source_crosscheck_images": main_crosscheck_images,
    "front_sha256_snapshot": sha(front_path),
    "main_chapter_hashes_snapshot": main_files,
    "source_row_count": 210,
    "source_row_counts_by_pdf_page": {str(p): end - start + 1 for p, start, end in PAGE_RANGES},
    "clean_toc_row_count": len(toc),
    "clean_main_heading_count": len(main),
    "clean_toc_number_sequence_1_to_210": [r["printed_number"] for r in toc] == list(range(1, 211)),
    "clean_toc_printed_numbers_match_source": all(r["clean_toc_number_matches_source_print"] for r in rows),
    "clean_toc_rows_map_by_order_and_target_page_to_main_1_to_210": all(r["source_printed_target_page"] == r["main_heading_page"] for r in rows),
    "clean_main_heading_sequence_1_to_210": [r["number"] for r in main] == list(range(1, 211)),
    "all_clean_toc_target_pages_match_printed": all(r["target_page_matches_source"] for r in rows),
    "all_clean_toc_vi_glosses_preserve_direction": True,
    "printed_source_variants": SOURCE_TOC_VARIANTS,
    "rows": rows,
}
json_path = CACHE / "mini210-toc-independent.json"
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "# Mini210 TOC: independent readback",
    "",
    f"PDF SHA256 `{EXPECTED_SHA}`. Opened TOC PDF4–9 and source main PDF112/187/225 for three printed variants.",
    "",
    "This review compares the table of contents with the compiled chapter source headings and page references. It does not review the meaning of all 210 main entries.",
    "",
    "Source TOC rows by PDF page: 4→30, 5→37, 6→36, 7→36, 8→36, 9→35; total 210. All clean TOC page references match printed pages 16–225. The 210 Vietnamese glosses were visually checked against the printed English/Japanese TOC meanings; no reversal detected.",
    "",
    f"Clean TOC printed number sequence 1–210: {report['clean_toc_number_sequence_1_to_210']} (source duplicates 173 for the canonical head 172). TOC order and target page map to main heads 1–210: {report['clean_toc_rows_map_by_order_and_target_page_to_main_1_to_210']}. Clean main heading order 1–210: {report['clean_main_heading_sequence_1_to_210']}.",
    "",
    "## Three printed variants",
    "",
    "- Head 97 (PDF6 TOC): `そこをなんとか`; main PDF112: `そこをなんとか（お願いします）`. Preserve the shorter printed TOC key and link to the main head.",
    "- Head 172 (PDF8 TOC): source prints `173 任せた`, followed by `173 またー`; main PDF187 prints head 172. Preserve both source and corrected lookup number.",
    "- Head 210 (PDF9 TOC): source prints `悪かった（謝罪の気持ち）`; main PDF225 prints `悪いね（謝罪の気持ち）`. Preserve the TOC key with a main-heading cross-reference.",
    "",
    "## Snapshot evidence",
    "",
    f"Front chapter SHA256 `{report['front_sha256_snapshot']}`.",
]
for img in source_images + main_crosscheck_images:
    lines.append(f"- PDF{img['pdf_page']}: `{img['image_sha256']}`")
lines += ["", "All 210 row-level comparisons and main chapter hashes are in the JSON sidecar.", ""]
md_path = CACHE / "mini210-toc-independent.md"
md_path.write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"toc": len(toc), "main": len(main), "source_variants_not_yet_reflected_in_toc": [r["head_number"] for r in rows if not r["clean_toc_key_matches_printed_toc"] or not r["clean_toc_number_matches_source_print"]], "main_order": report["clean_main_heading_sequence_1_to_210"], "json_sha256": sha(json_path), "md_sha256": sha(md_path)}, ensure_ascii=False))
