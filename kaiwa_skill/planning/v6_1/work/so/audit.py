import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
DEC = ROOT / 'kaiwa_skill/planning/v6_1/decisions'
all_dec = [json.loads(p.read_text(encoding='utf-8')) for p in sorted(DEC.glob('S-*.json'))]
registry = json.loads((ROOT/'kaiwa_skill/planning/v5/chang_registry.json').read_text(encoding='utf-8'))
books = collections.Counter()
empty = []
problems = []
unique_units = set()
situations = set()
for d in all_dec:
    code = d['display_code']
    sels = d['selections']
    if not sels: empty.append(code)
    m = re.search(r'Đọc đủ (\d+) tình huống', ' '.join(d['search_notes']))
    if m:
        asserted = int(m.group(1))
        key = registry[d['stage_uid']]['stage_key']
        stage = json.loads((ROOT/'kaiwa_skill/planning/v5/work/stages'/f'{key}.json').read_text(encoding='utf-8'))
        valid_ids = {x['id'] for x in stage['situations']}
        if asserted != len(valid_ids): problems.append((code, 'count in note mismatch', asserted, len(valid_ids)))
        for s in sels:
            invalid = set(s['situation_ids']) - valid_ids
            if invalid: problems.append((code, 'unrecognized situation IDs', sorted(invalid)))
    else: problems.append((code, 'missing stage count note'))
    seen = set()
    for s in sels:
        books[s['book_id']] += 1
        unique_units.add((s['book_id'], s['unit_id']))
        key = (s['book_id'], s['unit_id'])
        if key in seen: problems.append((code, 'duplicate unit', key))
        seen.add(key)
        situations.update(s['situation_ids'])
        source = ROOT / s['path']
        if not source.exists():
            problems.append((code, 'missing path', str(source)))
            continue
        lines = source.read_text(encoding='utf-8-sig').splitlines()
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        if sha != s['sha256']: problems.append((code, 'hash mismatch', s['unit_id']))
        a, b = s['start_line'], s['end_line']
        if a < 1 or b > len(lines) or a > b:
            problems.append((code, 'bad range', a, b, len(lines)))
            continue
        if not (lines[a-1].startswith('<a id=') or lines[a-1].startswith('## ')
                or lines[a-1].startswith('### ') or (code == 'S-059' and a == 1)):
            problems.append((code, 'range does not start with unit anchor', a, lines[a-1][:80]))
        if 'kết thúc trước anchor đơn vị kế tiếp ở dòng' in s['boundary']:
            nextline = b+1
            if nextline > len(lines) or not lines[nextline-1].startswith('<a id='):
                problems.append((code, 'boundary next anchor claim', nextline, lines[nextline-1][:60] if nextline<=len(lines) else 'EOF'))
        if b < len(lines) and not (lines[b].startswith('<a id=') or lines[b].startswith('## ') or lines[b].startswith('### ')):
            problems.append((code, 'range stops before next unit boundary', b+1, lines[b][:60]))
        if s['book_id'] in {'B19','B20','B24'}:
            print('BREADTH', code, s['book_id'], s['unit_id'], f'{a}-{b}', s['title_ja'])
print('DECISIONS', len(all_dec), 'NONEMPTY', len(all_dec)-len(empty), 'EMPTY', len(empty), ','.join(empty))
print('SELECTIONS', sum(books.values()), 'BOOKS', dict(books), 'UNIQUE_UNITS', len(unique_units), 'UNIQUE_MAPPED_SITUATIONS', len(situations))
print('PROBLEMS', len(problems))
for p in problems: print('PROBLEM', p)
