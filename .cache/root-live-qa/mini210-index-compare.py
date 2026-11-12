"""Read-only helper to inspect every index row and target unit."""

import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
BOOK = ROOT / 'kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210'
CHAPTER = BOOK / 'chapters/14-index.md'
raw = CHAPTER.read_text(encoding='utf-8')
sections = re.split(r'(?m)(?=^<a id="u-210-index-\d+"></a>)', raw)
rows = []
for section in sections:
    m = re.match(r'<a id="u-210-index-(\d+)"></a>', section)
    if not m:
        continue
    page = int(m.group(1))
    for line in section.splitlines():
        if not line.startswith('- **'):
            continue
        mm = re.fullmatch(r'- \*\*(.*?)\*\* — (.*?): (.*?) \(PDF(\d+)(?:;.*?)?\)\.', line)
        if not mm:
            raise ValueError((page, line))
        key, vi, jp, ref = mm.groups()
        rows.append({'pdf_page': page, 'key': key, 'vi': vi, 'jp': jp, 'printed_ref': int(ref)})

assert len(rows)==320
sections_by_head={}
for chapter in (BOOK/'chapters').glob('*.md'):
    text=chapter.read_text(encoding='utf-8')
    for m in re.finditer(r'<a id="u-210-(\d+)"></a>',text):
        n=int(m.group(1))
        after=re.search(r'<a id="u-210-\d+"></a>',text[m.end():])
        end=m.end()+after.start() if after else len(text)
        sections_by_head[n]={'chapter':str(chapter.relative_to(ROOT)).replace('\\','/'),'text':text[m.start():end]}

def norm(s):
    return re.sub(r'[\s\u200b\u00ad.,。、!?？!（）()~～・ー／/\[\]「」\-]', '',s)

for r in rows:
    head=r['printed_ref']-15
    target=sections_by_head.get(head)
    r['target_head']=head
    r['target_anchor']=f'u-210-{head}'
    r['target_chapter']=target['chapter'] if target else None
    r['jp_exact_in_target']=r['jp'] in target['text'] if target else False
    r['jp_normalized_in_target']=norm(r['jp']) in norm(target['text']) if target else False
    r.pop('vi')

print('rows', len(rows), 'counts', {p: sum(r['pdf_page'] == p for r in rows) for p in range(226, 232)})
print('missing targets',sum(r['target_chapter'] is None for r in rows))
print('JP absent even normalized', [(r['pdf_page'],r['key'],r['jp'],r['printed_ref'],r['target_head']) for r in rows if not r['jp_normalized_in_target']])
(ROOT/'.cache/root-live-qa/mini210-index-target-preliminary.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
