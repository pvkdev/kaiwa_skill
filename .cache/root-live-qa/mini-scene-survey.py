"""Read-only source scene survey; renders labeled left-column contacts in cache."""

import argparse
import hashlib
import json
import pathlib
import re

import pymupdf


ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent


def load_output(book_dir, prefix):
    statuses = {}
    units = book_dir / '_meta' / 'units.jsonl'
    if units.exists():
        for line in units.read_text(encoding='utf-8').splitlines():
            if line.strip():
                u = json.loads(line)
                m = re.fullmatch(rf'u-{prefix}-(\d+)', u.get('unit_id', ''))
                if m:
                    statuses[int(m.group(1))] = u.get('review_status')
    sections = {}
    for chapter in (book_dir / 'chapters').glob('*.md'):
        raw = chapter.read_text(encoding='utf-8')
        parts = re.split(rf'(?m)(?=^<a id="u-{prefix}-\d+"></a>)', raw)
        for section in parts:
            m = re.match(rf'<a id="u-{prefix}-(\d+)"></a>', section)
            if not m:
                continue
            n = int(m.group(1))
            nums = [int(x) for x in re.findall(r'(?m)^(\d+)\. ', section)]
            sections[n] = {'numbers': nums, 'chapter': str(chapter.relative_to(ROOT)).replace('\\', '/'), 'chapter_sha256': hashlib.sha256(chapter.read_bytes()).hexdigest()}
    return statuses, sections


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--book', choices=['210', '200'], required=True)
    args = ap.parse_args()
    if args.book == '210':
        pdf_rel = 'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf'
        book_dir = ROOT / 'kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210'
        pages = [(n, n + 15) for n in range(1, 211)]
        prefix = '210'
    else:
        pdf_rel = 'kaiwa_skill/book/Kaiwa/200-quick-and-easy-phrases-for-japanese-conversation-9784863922068_compress.pdf'
        book_dir = ROOT / 'kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ200'
        pages = [(n, n + 15 if n <= 130 else n + 17) for n in range(1, 201)]
        prefix = '200'
    pdf = pymupdf.open(ROOT / pdf_rel)
    statuses, sections = load_output(book_dir, prefix)
    report = {'book': args.book, 'pdf': pdf_rel, 'pdf_sha256': hashlib.sha256((ROOT / pdf_rel).read_bytes()).hexdigest(), 'pages': []}
    sheets_dir = OUT / f'mini{args.book}-scene-sheets'
    sheets_dir.mkdir(parents=True, exist_ok=True)
    tiles = []
    for head, physical in pages:
        page = pdf[physical - 1]
        # The circled scene labels are in the left column below the pink head panel.
        r = page.rect
        clip = pymupdf.Rect(24, 145, min(225, r.width * .58), min(555, r.height - 25))
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2.5, 2.5), clip=clip, alpha=False)
        tiles.append((head, physical, pix))
        labels = []
        a_blocks = []
        for block in page.get_text('blocks'):
            x0, y0, x1, y1, txt = block[:5]
            if x0 >= r.width * .6 or y0 < 145 or y0 > r.height - 30:
                continue
            t = ' '.join(txt.split())
            if re.search(r'^[AＡ]\s*[:：]', t):
                a_blocks.append({'y': round(y0, 1), 'text': t[:90]})
            if re.search(r'[①②③④⑤⑥⑦⑧⑨⑩❶❷❸❹❺❻❼❽❾❿]', t):
                labels.append({'y': round(y0, 1), 'text': t[:90]})
        sec = sections.get(head, {})
        report['pages'].append({'head': head, 'pdf_page': physical, 'source_a_block_count_heuristic': len(a_blocks), 'source_a_blocks': a_blocks, 'extracted_label_hints': labels, 'output_numbers': sec.get('numbers'), 'output_count': len(sec['numbers']) if sec else None, 'output_status': statuses.get(head), 'chapter': sec.get('chapter'), 'chapter_sha256': sec.get('chapter_sha256')})
        if len(tiles) == 10 or head == pages[-1][0]:
            cols = 5
            rows = (len(tiles) + cols - 1) // cols
            tw = max(t[2].width for t in tiles) + 16
            th = max(t[2].height for t in tiles) + 38
            sheet_pdf = pymupdf.open()
            sheet_page = sheet_pdf.new_page(width=cols * tw, height=rows * th)
            for i, (item_head, item_page, item_pix) in enumerate(tiles):
                x, y = (i % cols) * tw, (i // cols) * th
                sheet_page.insert_text((x + 10, y + 25), f'HEAD {item_head:03d} / PDF {item_page:03d}', fontsize=22)
                sheet_page.insert_image(pymupdf.Rect(x + 8, y + 35, x + 8 + item_pix.width, y + 35 + item_pix.height), pixmap=item_pix)
            name = f'sheet-{head - len(tiles) + 1:03d}-{head:03d}.png'
            sheet_page.get_pixmap(matrix=pymupdf.Matrix(1, 1), alpha=False).save(str(sheets_dir / name))
            sheet_pdf.close()
            tiles.clear()
    (OUT / f'mini{args.book}-scene-preliminary.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print('book', args.book, 'pages', len(report['pages']), 'sheets', len(list(sheets_dir.glob('*.png'))))
    mismatches = [p for p in report['pages'] if p['output_status'] == 'author_checked' and p['output_count'] != p['source_a_block_count_heuristic']]
    print('heuristic checked mismatches', [(p['head'], p['pdf_page'], p['source_a_block_count_heuristic'], p['output_count']) for p in mismatches])


if __name__ == '__main__':
    main()
