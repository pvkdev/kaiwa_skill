import json
import os
import re
import subprocess
import sys
from pathlib import Path
from source_lookup import ROOT, entries

WORK = Path(__file__).parent
PLAN = ROOT / 'kaiwa_skill/planning/v6_1'
QUEUE = json.loads((PLAN / 'QUEUE_so.json').read_text(encoding='utf-8'))
LOOKUP = {(e['book_id'], e['unit_id']): e for e in entries()}

def defaults(entry):
    body = entry['body']
    bid = entry['book_id']
    title = entry['heading'].split(' — ')[0]
    if bid == 'B08':
        match = re.search(r'CD-(\d+)\s*/\s*(\d+)', body)
        count = len(re.findall(r'^\d+\. \*\*', body.split('### Câu Nhật')[-1], re.M))
        unit_type = f'{count} mục câu Nhật' if count else 'toàn bộ câu Nhật'
        disc, track = ('CD-'+match[1], match[2]) if match else (None, None)
    elif bid == 'B05':
        match = re.search(r'CD-(\d+)\s*/\s*(\d+)', body)
        count = len(re.findall(r'^\d+\. \*\*', body.split('### Câu mẫu')[-1], re.M))
        unit_type = f'{count} câu mẫu Nhật và phần luyện/giải thích'
        disc, track = ('CD-'+match[1], match[2]) if match else (None, None)
    elif bid == 'B07':
        match = re.search(r'CD-(\d+)\s+(\d+)', body)
        count = len(re.findall(r'^\d+\. ', body, re.M))
        unit_type = f'{count} ví dụ và mọi phần giải thích'
        disc, track = ('CD-'+match[1], match[2]) if match else (None, None)
    elif bid == 'B18':
        match = re.search(r'音声\s*(\d+)', body)
        count = len(re.findall(r'^### シーン', body, re.M))
        unit_type = f'{count} シーン, đủ mọi lượt' if count else 'mọi ví dụ và giải thích'
        disc, track = (None, match[1]) if match else (None, None)
    else:
        raise ValueError('Need manual audio/boundary for ' + bid)
    if track is None:
        raise ValueError('Missing printed audio for '+bid+'/'+entry['unit_id'])
    source_lines = (ROOT / entry['path']).read_text(encoding='utf-8-sig').splitlines()
    tail = ('ở cuối chương clean' if entry['end_line'] == len(source_lines)
            else f'trước anchor đơn vị kế tiếp ở dòng {entry["end_line"]+1}')
    boundary = f'Trọn {title}, {unit_type}, dòng {entry["start_line"]}–{entry["end_line"]}; kết thúc {tail}.'
    audio = [{'disc': disc, 'track': track,
              'locator': f'{title}; nhãn {disc + " / " if disc else "音声 "}{track} in trong clean'}]
    note = 'Đã đối chiếu nhãn và toàn bộ chữ trong chương clean; chưa nghe file audio.'
    return boundary, audio, note

def main():
    spec = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    code = spec['code']
    stage = next(s for s in QUEUE['stages'] if s['code'] == code)
    selections = []
    for item in spec['selections']:
        entry = LOOKUP[(item['book_id'], item['unit_id'])]
        title = item.get('title_ja', entry['heading'].split(' — ')[0])
        prefix = re.match(r'^(?:\(\d+\)|\d+(?:-\d+)?[.　 ]?|Unit\s+\d+\s*[— ]\s*)[.　 ]*', title)
        row = {k: entry[k] for k in ('book_id', 'book_title', 'unit_id', 'path', 'sha256', 'start_line', 'end_line')}
        for key in ('start_line', 'end_line'):
            if key in item:
                row[key] = item[key]
        default_boundary, default_audio, default_note = defaults(entry) if not all(k in item for k in ('boundary', 'audio', 'audio_note')) else (None,None,None)
        row.update({'kind': item['kind'], 'title_ja': title,
                    'pack_id': item.get('pack_id', entry['book_id'] + '/' + entry['unit_id']),
                    'boundary': item.get('boundary', default_boundary), 'audio': item.get('audio', default_audio),
                    'audio_note': item.get('audio_note', default_note), 'situation_ids': item['situations'],
                    'fit_vi': item['fit'], 'difficulty_vi': item['difficulty'],
                    'read_status': 'whole_unit_read'})
        if 'source_number_prefix' in item:
            row['source_number_prefix'] = item['source_number_prefix']
        elif prefix:
            row['source_number_prefix'] = prefix.group(0)
        selections.append(row)
    decision = {'stage_uid': stage['uid'], 'display_code': code,
                'vocabulary_topics': spec['topics'], 'search_notes': spec['notes'],
                'selections': selections, 'considerations': spec['considerations']}
    dest = PLAN / 'decisions' / (code + '.json')
    tmp = WORK / (code + '.tmp.json')
    tmp.write_text(json.dumps(decision, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    env = os.environ.copy()
    env['KAIWA_ROADMAP_DIR'] = str(PLAN)
    result = subprocess.run(['py', '-X', 'utf8', 'tools/roadmap_v6.py', 'check-one', str(tmp)],
                            cwd=ROOT, env=env, text=True, capture_output=True)
    print(result.stdout, result.stderr, sep='', end='')
    if result.returncode:
        raise SystemExit(result.returncode)
    tmp.replace(dest)
    print('saved', dest)

if __name__ == '__main__':
    main()
