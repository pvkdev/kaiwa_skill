"""Reconstruct a row-oriented OCR aid from the six original PDF index pages."""

import json
import pathlib
import re

import pymupdf

ROOT = pathlib.Path(__file__).resolve().parents[2]
PDF = ROOT / 'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf'
doc = pymupdf.open(PDF)
report = {}
for pdf_page in range(226, 232):
    page = doc[pdf_page-1]
    lines = []
    for block in page.get_text('dict')['blocks']:
        if 'lines' not in block:
            continue
        for line in block['lines']:
            x,y = line['bbox'][:2]
            t = ''.join(span['text'] for span in line['spans']).strip()
            if 50 < y < 585 and t:
                lines.append({'x':x,'y':y,'text':t})
    # On odd/even spreads the right column starts at x≈201/217.  Keep
    # the separator left of both starts so index rows do not interleave.
    split_x = 190
    groups=[]
    for side in ('left','right'):
        ls=[l for l in lines if (l['x'] < split_x)==(side=='left')]
        ls.sort(key=lambda a:(a['y'],a['x']))
        pending=[]
        for l in ls:
            t=l['text']
            if re.fullmatch('[A-ZА-Я]',t):
                continue
            pending.append(t)
            if re.search(r'(?<!\d)(?:1\d|2\d|[3-9]\d|1\d\d|2[01]\d|22[0-5])\s*$',t):
                groups.append({'column':side,'text':' '.join(pending),'first_y':round(l['y'],1)})
                pending=[]
        if pending:
            groups.append({'column':side,'unclosed':' '.join(pending)})
    report[pdf_page]=groups
    print(pdf_page,len(groups), 'unclosed',sum('unclosed' in x for x in groups))
    for i,g in enumerate(groups,1):
        print(f'{i:02d}',g.get('text',g.get('unclosed')))
(ROOT/'.cache/root-live-qa/mini210-index-source-ocr.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
