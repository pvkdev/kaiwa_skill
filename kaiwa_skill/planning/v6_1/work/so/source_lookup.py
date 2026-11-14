import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
MANIFEST = json.loads((ROOT / 'kaiwa_skill/planning/catalog27/manifest.json').read_text(encoding='utf-8'))
ALLOWED = {'B01','B05','B06','B07','B08','B11','B12','B13','B14','B18','B19','B20','B24'}

def entries():
    for book in MANIFEST['books']:
        if book['book_id'] not in ALLOWED:
            continue
        for chapter in book['chapters']:
            path = ROOT / chapter['path']
            lines = path.read_text(encoding='utf-8-sig').splitlines()
            marks = [(i+1, m.group(1)) for i, line in enumerate(lines)
                     if (m := re.search(r'<a id="([^"]+)"', line))]
            for n, (start, unit_id) in enumerate(marks):
                end = marks[n+1][0]-1 if n+1 < len(marks) else len(lines)
                heading = next((line.strip('# ').strip() for line in lines[start:end]
                                if line.startswith('#')), '')
                body = '\n'.join(lines[start-1:end])
                yield {'book_id': book['book_id'], 'book_title': book['title'],
                       'unit_id': unit_id, 'path': chapter['path'],
                       'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                       'start_line': start, 'end_line': end,
                       'heading': heading, 'body': body}

if __name__ == '__main__':
    query = ' '.join(sys.argv[1:]).casefold()
    results = [e for e in entries() if query in e['heading'].casefold() or query in e['body'].casefold()]
    for e in results:
        print(f"{e['book_id']} {e['unit_id']} {e['path'].split('/')[-1]}:{e['start_line']}-{e['end_line']} {e['heading']}")
