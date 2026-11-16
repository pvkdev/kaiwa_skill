"""Validate whole-pack allocations and build the V7 specialty/topic roadmap."""
import argparse
import copy
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import roadmap_v6 as old

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / 'kaiwa_skill/planning'
V7 = P / 'v7'
BOOKS = ['B06', 'B07', 'B11', 'B12', 'B18', 'B19', 'B20', 'B24']


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    temporary.replace(path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def catalog():
    result = {}
    for book in BOOKS:
        data = old.read(P / 'v6_3/coverage' / (book + '.json'))
        for pack in data['packs']:
            selection = pack['selection']
            result[(book, selection['pack_id'])] = selection
    return result


def load_allocations(from_workers=False):
    if not from_workers and (V7 / 'inventory.json').exists():
        registry = old.read(V7 / 'DECISION_REGISTRY.json')
        return ([old.read(V7 / 'decisions' / (uid + '.json')) for uid in registry],
                old.read(V7 / 'inventory.json'), old.read(V7 / 'EXCEPTIONS.json'))
    groups = [old.read(V7 / 'work' / (name + '.json')) for name in 'abc']
    return ([s for g in groups for s in g['specialties']],
            [r for g in groups for r in g['inventory']],
            [r for g in groups for r in g.get('exceptions', [])])


def validate(specialties, inventory, exceptions, packs, topics):
    by_uid = {s['uid']: s for s in topics}
    order = {s['uid']: i for i, s in enumerate(topics)}
    assert len({s['uid'] for s in specialties}) == len(specialties), 'Duplicate specialty UID'
    assert not set(by_uid) & {s['uid'] for s in specialties}
    inventory_keys = [(r['book_id'], r['pack_id']) for r in inventory]
    assert len(set(inventory_keys)) == len(inventory_keys) and set(inventory_keys) == set(packs)
    for r in inventory:
        assert r['read_status'] == 'whole_pack_read' and r['summary_vi'].strip()
    used = Counter()
    for s in specialties:
        anchor = by_uid[s['before_topic_uid']]
        assert s['level'] == anchor['level'], s['title_vi']
        assert s['status'] == 'reviewed' and s['stage_kind'] == 'speak_japanese'
        assert s['title_vi'].strip() and s['objective_vi'].strip() and s['ordered_packs']
        assert isinstance(s['rank_at_anchor'], int)
        for field in ('level_reason_vi', 'placement_reason_vi', 'order_reason_vi'):
            assert s[field].strip()
        keys = [(r['book_id'], r['pack_id']) for r in s['ordered_packs']]
        assert len(set(keys)) == len(keys), s['title_vi']
        for key in keys:
            assert key in packs, key
            used[key] += 1
        for a in s.get('applications', []):
            topic = by_uid[a['topic_uid']]
            assert a['situation_id'] in {x['id'] for x in topic['situations']}
            assert order[topic['uid']] >= order[anchor['uid']]
            assert a['use_vi'].strip()
    excluded = {(e['book_id'], e['pack_id']) for e in exceptions}
    assert set(used) | excluded == set(packs), 'Unallocated pack'
    assert not set(used) & excluded, 'Pack both used and excluded'
    for e in exceptions:
        assert e['reason_vi'].strip()
    return used


def material(selection):
    chunks = []
    for part in [selection, *selection.get('extra_parts', [])]:
        data = (ROOT / part['path']).read_bytes()
        assert sha(data) == part['sha256'], part['path']
        lines = data.decode('utf-8-sig').splitlines(keepends=True)
        assert 1 <= part['start_line'] <= part['end_line'] <= len(lines)
        chunks.append(''.join(lines[part['start_line'] - 1:part['end_line']]).encode('utf8'))
    return b'\n\n'.join(chunks)


def build(publish=False, from_workers=False):
    packs = catalog()
    topics = old.rows(P / 'v6_5/KAIWA_CHANG_V6_5.jsonl')
    specialties, inventory, exceptions = load_allocations(from_workers)
    used = validate(specialties, inventory, exceptions, packs, topics)
    anchors = defaultdict(list)
    for s in specialties:
        anchors[s['before_topic_uid']].append(s)
    base = old.read(P / 'v6_5/learner.json')
    entries_by_uid = {s['uid']: s for s in base['stages']}
    materials, metadata = {}, {}
    for key, count in used.items():
        selection = packs[key]
        data = material(selection)
        filename = selection['book_id'] + '-' + sha(selection['pack_id'].encode())[:16] + '.md'
        destination = V7 / 'materials' / filename
        destination.parent.mkdir(exist_ok=True)
        destination.write_bytes(data)
        s = dict(selection)
        if 'source_number_prefix' not in s:
            match = re.match(r'^(?:\(?\d+\)?[.．、\u3000 ]+|Unit\s*\d+\s*[—–:：-]?\s*)', s['title_ja'])
            s['source_number_prefix'] = match[0] if match else ''
        html = old.render_excerpt(data, s)
        html = re.sub(r'\b(?:CD|DISC|DISK)[ -]*\d+(?:\s*[/／]\s*\d+)?', '', html)
        html = re.sub(r'(?:<strong>)?Trang in:(?:</strong>)?\s*\d+(?:\s*[–-]\s*\d+)?\.?', '', html)
        html = re.sub(r'(<h[1-6]>)\s*(?:\d+[.．、]\s*|(?:Unit|Section)\s*\d+\s*[—–:：-]?\s*)', r'\1', html)
        content_key = sha(html.encode())
        materials[content_key] = html
        metadata[key] = {'source': selection, 'file': 'materials/' + filename,
                         'sha256': sha(data), 'learner_title': old.learner_title(s), 'content_key': content_key}
    entries, rows = [], []
    numbers = Counter()
    reverse = defaultdict(list)
    for topic in topics:
        for specialty in sorted(anchors[topic['uid']], key=lambda s: (s['rank_at_anchor'], s['uid'])):
            s = copy.deepcopy(specialty)
            level = s['level']
            numbers[level] += 1
            selections = []
            admin = {'decision': s, 'materials': []}
            for rank, ref in enumerate(s['ordered_packs']):
                key = (ref['book_id'], ref['pack_id'])
                meta = metadata[key]
                admin['materials'].append(meta)
                reverse[key].append({'uid': s['uid'], 'title_vi': s['title_vi'], 'level': level, 'order': rank})
                selections.append({'id': 'material-' + sha((key[0] + '/' + key[1]).encode()), 'title': meta['learner_title'],
                                   'kind': 'speak_japanese', 'support': False, 'content_key': meta['content_key']})
            order = [{'type': 'source_pack', 'selection_id': s['id']} for s in selections]
            entries.append({'uid': s['uid'], 'code': 'SJ-' + s['uid'][:8], 'stage_kind': 'speak_japanese',
                            'level': level, 'number': numbers[level], 'title': s['title_vi'],
                            'cluster': topic['cluster_title'], 'cluster_id': topic['cluster_id'],
                            'objective': s['objective_vi'], 'events': [], 'situations': [],
                            'vocabulary': [], 'selections': selections, 'order': order, 'shadowing': None})
            rows.append(dict(s, roadmap_order=numbers[level]))
            write(V7 / 'decisions' / (s['uid'] + '.json'), s)
            write(V7 / 'admin' / (s['uid'] + '.json'), admin)
        numbers[topic['level']] += 1
        entry = copy.deepcopy(entries_by_uid[topic['uid']])
        entry.update(stage_kind='topic', number=numbers[topic['level']])
        entries.append(entry)
        rows.append(dict(topic, stage_kind='topic', roadmap_order=numbers[topic['level']]))
    write(V7/'inventory.json', inventory)
    write(V7/'DECISION_REGISTRY.json', [s['uid'] for s in specialties])
    write(V7/'EXCEPTIONS.json', exceptions)
    write(V7/'SOURCE_INDEX.json', [{'book_id': b, 'pack_id': p, 'placements': reverse[(b,p)]} for b,p in packs])
    payload = {'version': '7.0', 'stages': entries, 'content': materials, 'branches': base['branches']}
    write(V7/'learner.json', payload)
    target = V7/'KAIWA_CHANG_V7.jsonl'
    target.write_text(''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in rows), encoding='utf8')
    status = {'version': '7.0', 'status': 'complete', 'topic_stages': len(topics), 'specialty_stages': len(specialties),
              'total_stages': len(entries), 'unique_packs': len(used), 'placements': sum(used.values()),
              'exceptions': exceptions, 'levels': dict(numbers),
              'by_book': {b: sum(k[0] == b for k in used) for b in BOOKS},
              'basis_sha256': sha((P/'v6_5/KAIWA_CHANG_V6_5.jsonl').read_bytes())}
    status['catalog_hashes'] = {b: sha((P/'v6_3/coverage'/(b+'.json')).read_bytes()) for b in BOOKS}
    status['skill_sha256'] = sha((ROOT/'.agents/skills/kaiwa-speak-japanese-roadmap/SKILL.md').read_bytes())
    write(V7/'STATUS.json', status)
    write(V7/'SOURCE_POLICY.json', {'version': '7.0', 'books': BOOKS, 'whole_packs': True,
          'basis': '../v6_5/KAIWA_CHANG_V6_5.jsonl', 'basis_sha256': status['basis_sha256']})
    text = f"# Báo cáo V7\n\n{len(topics)} chặng topic và {len(specialties)} chuyên đề, tổng {len(entries)} chặng.\n\n"
    text += f"Đã phân bổ {len(used)}/1004 pack duy nhất, {sum(used.values())} lượt đặt. Ngoại lệ {len(exceptions)}.\n\n"
    text += '\n'.join(f'- {b}: {n} pack.' for b,n in status['by_book'].items())
    text += '\n\nCác pack giữ nguyên kiến thức, ví dụ và thứ tự nguồn, gồm phần bổ trợ. Tên và vị trí là quyết định biên tập có lý do trong admin. Video/bài giảng sẽ biên soạn ở pha sau. B18 thiếu bài14 trong nguồn gốc; giới hạn nguồn và nhãn audio lịch sử truy được qua catalog.\n'
    text += '\nSố chặng theo cấp (gồm topic và chuyên đề):\n' + '\n'.join(f'- {level}: {count} chặng.' for level, count in numbers.items()) + '\n'
    (V7/'REPORT_V7.md').write_text(text, encoding='utf8')
    for level, filename in zip(dict.fromkeys(t['level'] for t in topics), ['SO_CAP.md','TRUNG_CAP.md','THUONG_CAP.md']):
        lines = ['# ' + level, '']
        for entry in entries:
            if entry['level'] != level:
                continue
            lines += [f"## {entry['number']}. {entry['title']}", '', entry['objective'], '']
            lines += ['- ' + s['title'] for s in entry['selections']]
            lines += ['- ' + s['title'] for s in entry['situations']]
            lines += ['']
        (V7/filename).write_text('\n'.join(lines), encoding='utf8')
    html = (ROOT/'tools/review_site.html').read_text('utf8').replace('__COURSE_DATA__', json.dumps(payload, ensure_ascii=False, separators=(',',':')).replace('<','\\u003c'))
    (V7/'ROADMAP.html').write_text(html, encoding='utf8')
    if publish:
        write(P/'CURRENT_ROADMAP.json', {'version':'7.0', 'registry':'kaiwa_skill/planning/v5/chang_registry.json',
              'roadmap':target.relative_to(ROOT).as_posix(), 'policy':'kaiwa_skill/planning/v7/SOURCE_POLICY.json'})
        (ROOT/'docs/index.html').write_text(html, encoding='utf8')
    print(json.dumps(status, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--publish', action='store_true')
    parser.add_argument('--from-workers', action='store_true')
    args = parser.parse_args()
    build(args.publish, args.from_workers)
