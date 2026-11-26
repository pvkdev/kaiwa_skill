"""Build independent B-example recognition items for groups without a drill adaptation.

These are editorial questions using official example JA–VI pairs. The choice key
is editorial; a B example is never represented as a revealed B-drill answer.
"""

import re

from renshuu_dom import parse


def words(text):
    return set(re.findall(r'[\wÀ-ỹ]+', text.lower()))


def overlap(a, b):
    x, y = words(a), words(b)
    return len(x & y) / max(1, len(x | y))


def text_only_instruction(source_instruction):
    visual = r'tranh|hình|ảnh|mặt cười|mặt buồn|ký hiệu|sơ đồ|mũi tên|nhãn tên|đồng hồ|bản đồ|được khoanh'
    if not re.search(visual, source_instruction, flags=re.IGNORECASE):
        return source_instruction
    parts = [x.strip() for x in re.split(r'[,.，。]', source_instruction)]
    kept = [x for x in parts if x and not re.search(visual, x, flags=re.IGNORECASE)]
    return '. '.join(kept) + ('.' if kept else 'Dựa vào gợi ý và nghĩa đích.')


def evidence_mapping(snapshot, instruction):
    found = []
    for point in snapshot['points']:
        tokens = [t for t in re.findall(r'[\u3040-\u30ff\u3400-\u9fffー]+', point['title'])
                  if len(t) >= 3 and t not in {'です', 'ます', 'しています'}]
        hits = [t for t in tokens if t in instruction]
        if hits:
            found.append((max(map(len, hits)), point['id']))
    if not found:
        return [], 'pending_no_exact_form_match'
    found.sort(reverse=True)
    if len(found) > 1 and found[0][0] == found[1][0]:
        return [], 'pending_multiple_form_matches'
    return [found[0][1]], 'exact_form_match_in_group_instruction'


def source_groups(snapshot):
    groups = []
    for section in snapshot['sections']:
        match = re.fullmatch(r'mg-b(\d+)', section['id'])
        if not match:
            continue
        root = parse(section['html'])
        title = root.all('mg-point-t')[0].text()
        instruction = root.all('mg-part-ins')[0].text()
        rei = root.all('mg-rei')[0]
        rei_item = rei.all('mg-rei-item')[0]
        prompt_nodes = rei_item.all('mg-drill-prompt')
        example_prompt = prompt_nodes[0].text() if prompt_nodes else ''
        pairs = []
        for line in rei_item.all('mg-line'):
            ja = line.all('mg-ja')
            vi = line.all('mg-vi')
            if ja and vi and ja[0].text() and vi[0].text():
                pairs.append((ja[0].text(), vi[0].text()))
        groups.append({'group': f'b{match.group(1)}', 'title': title,
                       'instruction': instruction, 'example_prompt': example_prompt,
                       'ja': ' '.join(pair[0] for pair in pairs),
                       'vi': ' '.join(pair[1] for pair in pairs)})
    return groups


def additional_items(snapshot, adapted_drill_ids):
    groups = source_groups(snapshot)
    adapted_groups = {x.split('-')[0] for x in adapted_drill_ids}
    items = []
    pending = []
    for group in groups:
        if group['group'] in adapted_groups:
            continue
        if not group['ja'] or not group['vi']:
            pending.append({'source_group_id': group['group'], 'reason': 'source_example_lacks_ja_vi_pair'})
            continue
        candidates = [x for x in groups if x['group'] != group['group']
                      and x['ja'] != group['ja'] and x['vi'] != group['vi']
                      and overlap(x['vi'], group['vi']) < 0.35]
        if len(candidates) < 2:
            pending.append({'source_group_id': group['group'], 'reason': 'fewer_than_two_distinct_example_meanings'})
            continue
        # Prefer close Japanese surface forms so the learner has to inspect the
        # target phrase, while avoiding Vietnamese paraphrases of the same idea.
        candidates.sort(key=lambda x: (abs(len(x['ja']) - len(group['ja'])), x['group']))
        distractors = []
        for candidate in candidates:
            if candidate['ja'] not in {x['ja'] for x in distractors}:
                distractors.append(candidate)
            if len(distractors) == 2:
                break
        if len(distractors) < 2:
            pending.append({'source_group_id': group['group'], 'reason': 'fewer_than_two_distinct_japanese_options'})
            continue
        ordered = [group] + distractors
        rotate = (snapshot['lesson'] + int(group['group'][1:])) % 3
        ordered = ordered[rotate:] + ordered[:rotate]
        wrong_in_display_order = [x for x in ordered if x['group'] != group['group']]
        refs, mapping = evidence_mapping(snapshot, group['instruction'])
        exercise_instruction = text_only_instruction(group['instruction'])
        explanation = (f'“{group["ja"]}” diễn đạt “{group["vi"]}”. '
                       f'Nhóm B này yêu cầu: {exercise_instruction} '
                       f'Hai phương án sai có nghĩa “{wrong_in_display_order[0]["vi"]}” '
                       f'và “{wrong_in_display_order[1]["vi"]}”.')
        items.append({
            'id': f'rb-{snapshot["lesson"]:02}-{group["group"]}-rei-1-recognition',
            'kind': 'manualQnA',
            'source_id': f'{group["group"]}-rei-1',
            'source_group_id': group['group'],
            'source_example_prompt_ja': group['example_prompt'],
            'source_group_instruction_vi': group['instruction'],
            'prompt_ja': group['example_prompt'] or 'どれですか。',
            'instruction_vi': (f'Chọn câu tiếng Nhật diễn đạt đúng nghĩa “{group["vi"]}”. '
                               f'{exercise_instruction}'),
            'choices': [{'id': f'c{i+1}', 'text': x['ja']} for i, x in enumerate(ordered)],
            'correct': f'c{ordered.index(group)+1}',
            'explanation_vi': explanation,
            'grammar_refs': refs,
            'grammar_mapping_status': mapping,
            'exercise_focus': 'source_example_meaning_and_pattern_recognition',
            'provenance': {
                'source_prompt': 'official_B_example',
                'source_ja_vi_pair': 'official_B_example',
                'answer': 'ai_authored_selection_from_example',
                'explanation': 'ai_authored',
                'human_review': 'pending',
            },
        })
    return items, pending, len(groups)
