"""Build the read-only, page-by-page visual QA record for Mini210 index."""

import hashlib
import json
import pathlib
import re
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[2]
CACHE = ROOT / '.cache/root-live-qa'
BOOK = ROOT / 'kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210'
PDF = ROOT / 'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf'
BASELINE = CACHE / 'mini210-index-baseline.md'
INDEX = BOOK / 'chapters/14-index.md'

def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

def parse_index(p):
    raw = p.read_text(encoding='utf-8')
    result = []
    for section in re.split(r'(?m)(?=^<a id="u-210-index-\d+"></a>)', raw):
        m = re.match(r'<a id="u-210-index-(\d+)"></a>', section)
        if not m:
            continue
        source_page = int(m.group(1))
        ordinal = 0
        for line in section.splitlines():
            if not line.startswith('- **'):
                continue
            mm = re.fullmatch(r'- \*\*(.*?)\*\* — (.*?): (.*?) \(PDF(\d+)(?:;.*?)?\)\.', line)
            if not mm:
                raise ValueError(line)
            ordinal += 1
            key, vi, jp, ref = mm.groups()
            result.append({'source_pdf_page': source_page, 'output_ordinal_on_page': ordinal,
                           'output_key': key, 'output_japanese': jp, 'output_vi': vi,
                           'output_printed_ref': int(ref), 'output_line': line})
    return result

rows = parse_index(BASELINE)
assert len(rows) == 320
current_rows = parse_index(INDEX)
assert len(current_rows) == 320

known = {
    (226, 1): {'source_key': 'A big dea'},
    (226, 12): {'source_key': '(Not) ~at all'},
    (226, 45): {'source_japanese': 'そうおもわなない？'},
    (226, 46): {'source_japanese': 'そうおもわなない？'},
    (231, 6): {'source_key': "Tthat's what I said"},
}
for r in rows:
    page = r['source_pdf_page']
    ordinal = r['output_ordinal_on_page']
    r['source_ordinal_on_page'] = ordinal
    # The printed P order differs from the baseline output order.
    if page == 229 and ordinal in (49, 50, 51):
        r['source_ordinal_on_page'] = {49: 51, 50: 49, 51: 50}[ordinal]
    r['source_key'] = r['output_key']
    r['source_japanese'] = r['output_japanese']
    r['source_printed_ref'] = r['output_printed_ref']
    r.update(known.get((page, ordinal), {}))
    r['target_head'] = r['source_printed_ref'] - 15
    r['target_anchor'] = f"u-210-{r['target_head']}"
    r['visual_comparison'] = 'reviewed_full_page_at_original_resolution; crops_for_findings'
rows.sort(key=lambda r: (r['source_pdf_page'], r['source_ordinal_on_page']))
current_by_position = {(r['source_pdf_page'], r['output_ordinal_on_page']): r for r in current_rows}
for r in rows:
    current = current_by_position[(r['source_pdf_page'], r['source_ordinal_on_page'])]
    r['current_key'] = current['output_key']
    r['current_japanese'] = current['output_japanese']
    r['current_printed_ref'] = current['output_printed_ref']
    r['current_matches_source_transcript'] = (
        r['current_key'] == r['source_key']
        and r['current_japanese'] == r['source_japanese']
        and r['current_printed_ref'] == r['source_printed_ref']
    )
assert all(r['current_matches_source_transcript'] for r in rows)

targets = {}
for chapter in (BOOK / 'chapters').glob('*.md'):
    chapter_text = chapter.read_text(encoding='utf-8')
    for m in re.finditer(r'<a id="u-210-(\d+)"></a>', chapter_text):
        targets[int(m.group(1))] = str(chapter.relative_to(ROOT)).replace('\\', '/')
for r in rows:
    r['target_chapter'] = targets.get(r['target_head'])
    r['target_exists'] = r['target_chapter'] is not None
assert all(r['target_exists'] for r in rows)

images = []
for page in range(226, 232):
    image = ROOT / f'kaiwa_skill/.cache/direct-210/p{page:04d}.png'
    images.append({'pdf_page': page, 'path': str(image.relative_to(ROOT)).replace('\\','/'),
                   'sha256': sha(image), 'rows': sum(r['source_pdf_page'] == page for r in rows)})

findings = [
  {'id': 'idx226-a-big-dea', 'pdf_page': 226, 'row': 1,
   'source': 'A big dea たいしたもんだ 132',
   'output': 'A big deal たいしたもんだ 132',
   'proposal': 'Retain printed key A big dea; a note may identify main PDF132 as A big deal.',
   'status': 'open'},
  {'id': 'idx226-not-at-all', 'pdf_page': 226, 'row': 12,
   'source': '(Not) ~at all ぜんぜん 109',
   'output': '(Not) at all ぜんぜん 109',
   'proposal': 'Restore printed ~ placeholder in the key.', 'status': 'open'},
  {'id': 'idx226-dont-you-agree', 'pdf_page': 226, 'rows': [45,46],
   'source': 'Both aliases print そうおもわなない？ 111',
   'output': 'Both aliases show そうおもわない？ 111',
   'proposal': 'Retain printed index spelling and note that main PDF111 has そう思わない？.',
   'status': 'open'},
  {'id': 'idx229-p-order', 'pdf_page': 229, 'rows': [49,50,51],
   'source': 'Pissed off → Pitiful → Please do it as soon as possible',
   'output': 'Please do it as soon as possible → Pissed off → Pitiful',
   'proposal': 'Restore printed order of the three rows, retaining their key/JP/ref.',
   'status': 'open'},
  {'id': 'idx231-tthats', 'pdf_page': 231, 'row': 6,
   'source': "Tthat's what I said だからいったのに 134",
   'output': "That's what I said だからいったのに 134",
   'proposal': 'Retain printed Tthat’s typo; a note may identify main PDF134 as That’s what I said.',
   'status': 'open'},
]
for f in findings:
    f['status'] = 'resolved_after_writer_fix'

report = {
  'report_type': 'independent_read_only_index_row_review',
  'generated_utc': datetime.now(timezone.utc).isoformat(),
  'source_pdf': str(PDF.relative_to(ROOT)).replace('\\','/'),
  'source_pdf_sha256': sha(PDF),
  'baseline_index': str(BASELINE.relative_to(ROOT)).replace('\\','/'),
  'baseline_index_sha256': sha(BASELINE),
  'current_index_sha256_at_report': sha(INDEX),
  'readback_status': 'all_320_rows_match_reviewed_source_transcript_after_writer_fix',
  'open_findings': 0,
  'scope': 'PDF226–231, all 320 printed row occurrences; key/Japanese/ref/order and main ref location. No full-book language review.',
  'method': 'Opened all six full source bitmaps; inspected row-by-row against the stable index; used PDF text extraction as an aid; rendered targeted crops for ambiguous glyphs; checked all ref numbers lead to existing corresponding main head positions (head = PDF ref - 15). Spaces and wave-dash typography treated as equivalent where alias meaning is retained.',
  'counts_by_source_page': {str(p): sum(r['source_pdf_page'] == p for r in rows) for p in range(226,232)},
  'total_source_rows': len(rows),
  'target_refs_with_existing_head': sum(r['target_exists'] for r in rows),
  'source_bitmaps': images,
  'finding_crops': [str((CACHE/n).relative_to(ROOT)).replace('\\','/') for n in ['mini210-index-226-a-top.png','mini210-index-226-d-middle.png','mini210-index-231-thats-crop.png']],
  'findings': findings,
  'rows_in_source_order': rows,
  'limits': 'This is index-only QA. Main-page target identity was verified by printed ref/head and main title or English gloss; the full main-page Japanese/translation content was not independently re-reviewed. Source transcription normalizes inconsequential spacing; explicit source typos and aliases are listed as findings.',
}

out = CACHE / 'mini210-index-independent.json'
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

md = [
  '# Mini210 index: independent read-only review',
  '',
  f'Baseline index SHA256: `{report["baseline_index_sha256"]}`',
  f'Current index SHA256: `{report["current_index_sha256_at_report"]}`',
  f'Source PDF SHA256: `{report["source_pdf_sha256"]}`',
  '',
  'Opened source PDF226–231. Source rows per page: 56/57/58/51/50/48 = 320. All 320 printed refs lead to a corresponding main head and existing unit anchor. After writer fixes, all 320 current rows match the reviewed source transcript; 0 open findings.',
  '',
  '## Findings',
  '',
]
for f in findings:
    md += [f'- **{f["id"]}**, PDF{f["pdf_page"]}: source `{f["source"]}`; output `{f["output"]}`. {f["proposal"]}']
md += ['', 'Full row-by-row source/output transcript, bitmap hashes, target positions, and scope limits are in the JSON report.', '']
(CACHE/'mini210-index-independent.md').write_text('\n'.join(md), encoding='utf-8')
print(out)
print('rows',len(rows),'bitmap hashes',len(images),'findings',len(findings))
