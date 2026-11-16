"""Build repeatable V6.4/6.5 releases from the immutable V6.3 snapshot."""
import argparse
import copy
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import roadmap_v6 as old

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / 'kaiwa_skill/planning'
BASE = PLANNING / 'v6_3'
SJ = {'B05', 'B06', 'B07', 'B11', 'B12', 'B18', 'B19', 'B20', 'B24'}
SHADOW = {'B01', 'B08', 'B13', 'B14', 'INTERVIEW'}


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    temp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate(stage, decision):
    code = stage['display_code']
    assert decision['display_code'] == code
    assert decision['stage_uid'] == stage['uid'] and decision['status'] == 'reviewed'
    materials = {s['material_path']: s for s in stage['v6']['decision']['selections'] if s['book_id'] in SHADOW}
    reviews = decision['source_review']
    assert {r['material_path'] for r in reviews} == set(materials), f'{code}: incomplete source_review'
    seen_ids, seen_text = set(), set()
    for item in decision['items']:
        assert item['id'] not in seen_ids
        seen_ids.add(item['id'])
        assert item['type'] in ('single_sentence', 'dialogue')
        speakers = {s['id']: s for s in item['speakers']}
        assert len(speakers) == len(item['speakers'])
        for speaker in speakers.values():
            assert speaker['gender'] in ('male', 'female') and speaker['role_vi']
            assert speaker['gender_basis'] in ('source', 'editorial_cast')
        turns = item['turns']
        assert (len(turns) == 1 if item['type'] == 'single_sentence' else len(turns) >= 2)
        assert len({t['speaker_id'] for t in turns}) >= (1 if item['type'] == 'single_sentence' else 2)
        for turn in turns:
            assert turn['speaker_id'] in speakers and turn['ja'].strip() and turn['vi'].strip()
            assert turn['source_refs'], f'{code}: missing source'
            for ref in turn['source_refs']:
                path = ref['material_path']
                assert path in materials, f'{code}: unexpected material {path}'
                assert ref['book_id'] == materials[path]['book_id'] and ref['book_title'] == materials[path]['book_title']
                original = materials[path]
                parts = [original, *original.get('extra_parts', [])]
                assert any(ref['source_path'] == p['path'] and
                           ref['source_start_line'] == p['start_line'] and
                           ref['source_end_line'] == p['end_line'] for p in parts), f'{code}: locator mismatch'
                raw = (BASE / path).read_text(encoding='utf-8-sig')
                assert ref['quote_ja'] and ref['quote_ja'] in raw, f'{code}: quote not found {ref["quote_ja"]}'
            assert not re.search(r'<[^>]+>|\{\{|[／/]', turn['ja']), f'{code}: TTS markup or alternative'
        key = tuple(''.join(c for c in unicodedata.normalize('NFKC', t['ja'])
                            if not c.isspace() and not unicodedata.category(c).startswith('P')) for t in turns)
        assert key not in seen_text, f'{code}: duplicate item'
        seen_text.add(key)
    for review in reviews:
        assert review['disposition'] in ('selected', 'knowledge_only', 'off_topic', 'unusable')
        assert review.get('reason')
        assert set(review.get('item_ids', [])) <= seen_ids
        used = {i['id'] for i in decision['items'] for t in i['turns'] for r in t['source_refs'] if r['material_path'] == review['material_path']}
        assert used == set(review.get('item_ids', [])), f'{code}: review item mapping'
        assert (review['disposition'] == 'selected') == bool(used), f'{code}: disposition mismatch'
    return True


def audit():
    stages = {s['display_code']: s for s in old.rows(BASE / 'KAIWA_CHANG_V6_3.jsonl')}
    errors = []
    paths = sorted((PLANNING/'v6_5/decisions').glob('*.json'))
    for path in paths:
        try:
            validate(stages[path.stem], old.read(path))
        except Exception as error:
            errors.append({'stage': path.stem, 'error': str(error), 'type': type(error).__name__})
    result = {'checked': len(paths), 'missing': sorted(set(stages) - {p.stem for p in paths}), 'errors': errors}
    write(PLANNING/'v6_5/AUDIT.json', result)
    print(json.dumps({'checked': len(paths), 'missing_count': len(result['missing']), 'errors': errors}, ensure_ascii=False))
    return result


def learner_items(decision):
    return [{
        'id': i['id'], 'type': i['type'],
        'speakers': [{k: s[k] for k in ('id', 'role_vi', 'gender')} for s in i['speakers']],
        'turns': [{k: t[k] for k in ('speaker_id', 'ja', 'vi')} for t in i['turns']]
    } for i in decision['items']]


def build(version, publish=False):
    directory = PLANNING / ('v' + version.replace('.', '_'))
    source = BASE / 'KAIWA_CHANG_V6_3.jsonl'
    stages = old.rows(source)
    entries, output, rendered, admin = [], [], {}, []
    total_items = total_turns = active = 0
    for original in stages:
        stage = copy.deepcopy(original)
        code = stage['display_code']
        data = stage['v6']
        selections = data['decision']['selections']
        snapshot_manifest = old.read(BASE / 'stages' / code / 'manifest.json') if selections else {'materials': []}
        snapshot_hashes = {m['file']: m['sha256'] for m in snapshot_manifest['materials']}
        for selection in selections:
            assert digest(BASE / selection['material_path']) == snapshot_hashes[Path(selection['material_path']).name], f'{code}: snapshot hash changed'
        record = {'stage_uid': stage['uid'], 'display_code': code,
                  'baseline': '../v6_3/KAIWA_CHANG_V6_3.jsonl',
                  'hidden_speak_japanese': [s for s in selections if s['book_id'] in SJ],
                  'knowledge_archive': selections,
                  'snapshot_hashes': {s['material_path']: digest(BASE / s['material_path']) for s in selections}}
        data['decision']['selections'] = []
        order = [n for n in data['learning_order'] if n['type'] not in
                 ('speak_japanese_video', 'speak_japanese_examples', 'independent_shadowing')]
        display_selections = []
        if version == '6.4':
            kept = [copy.deepcopy(s) for s in selections if s['book_id'] not in SJ]
            for s in kept:
                raw = (BASE / s['material_path']).read_bytes()
                html = old.render_excerpt(raw, s)
                key = hashlib.sha256(html.encode('utf8')).hexdigest()
                rendered[key] = html
                display_selections.append({'book_id': s['book_id'], 'pack_id': s['pack_id'],
                    'title': old.learner_title(s), 'kind': s['kind'],
                    'support': s.get('pack_scope') == 'educational_support', 'content_key': key})
                s['material_path'] = '../v6_3/' + s['material_path']
            data['decision']['selections'] = kept
            order = [n for n in data['learning_order'] if n['type'] not in
                     ('speak_japanese_video', 'speak_japanese_examples')]
        else:
            decision = old.read(directory / 'decisions' / (code + '.json'))
            validate(original, decision)
            record['curation'] = decision
            items = learner_items(decision)
            data['shadowing'] = {'id': stage['uid'] + '-shadowing', 'type': 'shadowing', 'items': items} if items else None
            if items:
                active += 1
                index = next(i for i, n in enumerate(order) if n['type'] == 'stage_lecture')
                order.insert(index, {'id': stage['uid'] + '-shadowing', 'type': 'merged_shadowing'})
            total_items += len(items)
            total_turns += sum(len(i['turns']) for i in items)
        data['learning_order'] = order
        data['version'] = version
        data['internal_ref'] = f'admin/{code}.json'
        write(directory / 'admin' / (code + '.json'), record)
        admin.append(record)
        entry = {'uid': stage['uid'], 'code': code, 'level': stage['level'], 'number': stage['level_order'],
                 'title': stage['title'], 'cluster': stage['cluster_title'], 'cluster_id': stage['cluster_id'],
                 'objective': stage['objective'], 'events': stage['events'], 'situations': stage['situations'],
                 'vocabulary': data['decision']['vocabulary_topics'], 'selections': display_selections, 'order': order,
                 'shadowing': data.get('shadowing')}
        entries.append(entry)
        output.append(stage)
    roadmap_path = directory / ('KAIWA_CHANG_V' + version.replace('.', '_') + '.jsonl')
    roadmap_path.write_text(''.join(json.dumps(s, ensure_ascii=False) + '\n' for s in output), encoding='utf8')
    policy = {'version': version, 'basis': '../v6_3/KAIWA_CHANG_V6_3.jsonl', 'basis_sha256': digest(source),
              'shadowing_optional': True, 'speak_japanese_visibility': 'internal', 'audio': 'tts',
              'max_shadowing_nodes': 1 if version == '6.5' else None}
    write(directory / 'SOURCE_POLICY.json', policy)
    report = {'version': version, 'stages': len(stages), 'hidden_speak_japanese_placements': sum(len(a['hidden_speak_japanese']) for a in admin),
              'shadowing_stages': active if version == '6.5' else None,
              'without_shadowing': len(stages) - active if version == '6.5' else None,
              'items': total_items, 'turns': total_turns, 'status': 'complete', 'basis_sha256': digest(source)}
    write(directory / 'STATUS.json', report)
    text = f'# Báo cáo V{version}\n\nGiữ {len(stages)} chặng topic, 1304 sự kiện và 5914 tình huống. '
    text += f"Ẩn mềm {report['hidden_speak_japanese_placements']} lượt Speak Japanese; hồ sơ admin giữ nguồn, nội dung cũ qua đường dẫn tương đối V6.3 và hash.\n\n"
    if version == '6.5':
        text += f'{active} chặng có một node shadowing; {len(stages)-active} chặng không có nội dung phù hợp. Tổng {total_items} câu/đoạn, {total_turns} lượt nói Nhật–Việt có vai và giọng male/female.\n\n'
        counts = {}
        for a in admin:
            for r in a['curation']['source_review']:
                disposition = r['disposition']
                counts[disposition] = counts.get(disposition, 0) + 1
        report['material_review'] = counts
        report['editorial_gender_casting'] = sum(s['gender_basis'] == 'editorial_cast' for a in admin for i in a['curation']['items'] for s in i['speakers'])
        write(directory / 'STATUS.json', report)
        text += 'Kết quả rà material: ' + ', '.join(f'{k} {v}' for k, v in counts.items()) + '.\n\n'
        text += 'Mỗi chặng bên dưới có thống kê riêng để review. Trống là quyết định tuyển chọn, không phải bài lỗi hoặc nhiệm vụ phải lấp đầy.\n\n'
        for a in admin:
            items = a['curation']['items']
            text += f"- [{a['display_code']}](admin/{a['display_code']}.json): {len(items)} câu/đoạn, {sum(len(i['turns']) for i in items)} lượt nói.\n"
        text += '\n'
    text += 'Kiến thức kèm shadowing lưu ở admin; learner preview không nhúng metadata nguồn. Giới tính không có căn cứ gốc được phân giọng biên tập và ghi editorial_cast. Video chặng và các phần tình huống/challenge/free talk vẫn là khung. V7 chưa triển khai.\n'
    (directory / ('REPORT_V' + version.replace('.', '_') + '.md')).write_text(text, encoding='utf8')
    payload = {'version': version, 'stages': entries, 'content': rendered, 'branches': old.BRANCH}
    template = (ROOT / 'tools/review_site.html').read_text('utf8')
    html = template.replace('__COURSE_DATA__', json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c'))
    (directory / 'ROADMAP.html').write_text(html, encoding='utf8')
    write(directory / 'learner.json', payload)
    if publish:
        write(PLANNING / 'CURRENT_ROADMAP.json', {'version': version, 'registry': 'kaiwa_skill/planning/v5/chang_registry.json',
              'roadmap': roadmap_path.relative_to(ROOT).as_posix(), 'policy': (directory/'SOURCE_POLICY.json').relative_to(ROOT).as_posix()})
        (ROOT / 'docs/index.html').write_text(html, encoding='utf8')
    print(json.dumps(report, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('version', choices=['6.4', '6.5', 'audit'])
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    if args.version == 'audit':
        audit()
    else:
        build(args.version, args.publish)
