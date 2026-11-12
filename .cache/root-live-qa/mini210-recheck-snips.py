"""Print the formerly missing final scene from each changed head, read only."""

import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT / '.cache/root-live-qa/mini210-scene-coverage-independent.json').read_text(encoding='utf-8'))
HEADS = {141, 144, 147, 150, 163, 166, 169, 174, 177, 180, 183, 184, 189, 197, 200, 203}

for row in DATA['rows']:
    if row['head'] not in HEADS:
        continue
    raw = (ROOT / row['chapter']).read_text(encoding='utf-8')
    a = raw.index(f'<a id="u-210-{row["head"]}"></a>')
    b = raw.find('<a id="u-210-', a + 3)
    section = raw[a:b if b >= 0 else None]
    m = re.search(rf'(?m)^{row["source_count"]}\. ', section)
    assert m
    print(f'\nHEAD {row["head"]} PDF {row["pdf_page"]} {row["output_review_status"]} {row["chapter_sha256"]}')
    print(section[m.start():m.start()+550])
