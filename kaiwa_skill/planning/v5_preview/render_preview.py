"""Render/validate a read-only V5 proposal. Never mutates the accepted roadmap."""
from __future__ import annotations
import argparse, hashlib, html, json, re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LABELS = {'add': 'Bổ sung chặng', 'split': 'Tách từ chặng hiện có', 'expand': 'Mở rộng chặng cũ', 'merge': 'Gộp ứng viên', 'reframe': 'Làm rõ chặng cũ', 'defer': 'Lựa chọn sau'}
RELATIONS = {'direct_topic': 'đúng topic', 'partial_event': 'một phần sự kiện', 'function_only': 'chỉ cùng chức năng nói', 'other_role': 'khác vai', 'context_only': 'chỉ bối cảnh', 'counterexample': 'không coi là mẫu ứng xử'}

def read_json(name):
    return json.loads((HERE / name).read_text(encoding='utf8'))

def read_lines(name):
    return [json.loads(x) for x in (HERE / name).read_text(encoding='utf8').splitlines() if x.strip()]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def md_link(label, path, line=None):
    target = (ROOT / path).as_posix()
    return f'[{label}](<{target}{":" + str(line) if line else ""}>)'

def load():
    return {'cards': read_lines('candidates.jsonl'), 'reviews': read_lines('review_ai120.jsonl'), 'own': read_lines('own_additions.jsonl'), 'travel': read_json('travel_modules.json'), 'sources': read_json('sources.json'), 'audit': read_json('book_audit.json'), 'snapshot': read_json('snapshot.json')}

def validate(data):
    snap = data['snapshot']
    assert digest(ROOT / snap['base_path']) == snap['base_sha256'], 'Accepted roadmap changed; rebase review explicitly.'
    assert digest(ROOT / 'kaiwa_skill/planning/v2/chang_registry.json') == snap['registry_sha256'], 'Accepted registry changed.'
    base = [json.loads(x) for x in (ROOT / snap['base_path']).read_text(encoding='utf8').splitlines()]
    stage_ids = {x['id'] for x in base}
    assert len(base) == 194 and len({x['uid'] for x in base}) == 194
    assert sum(len(x['situations']) for x in base) == 645
    assert {x['original_id'] for x in data['reviews']} == set(range(1, 121)) and len(data['reviews']) == 120
    assert len(data['own']) == 13
    cards = data['cards']; card_ids = {x['id'] for x in cards}
    assert len(card_ids) == len(cards)
    assert len({x['title'].casefold() for x in cards}) == len(cards)
    assert len(data['audit']) == 27 and {x['book_id'] for x in data['audit']} == {f'B{i:02}' for i in range(1, 28)}
    evidence = {x['id']: x for x in data['sources']['book_evidence']}
    web = {x['id']: x for x in data['sources']['web']}
    for e in evidence.values():
        ls = (ROOT / e['path']).read_text(encoding='utf8').splitlines()
        assert 0 < e['line_start'] <= e['line_end'] <= len(ls)
        excerpt = '\n'.join(ls[e['line_start'] - 1:e['line_end']])
        assert hashlib.sha256(excerpt.encode()).hexdigest() == e['excerpt_sha256'], e['id']
    for r in data['reviews'] + data['own']:
        assert r['decision'] in LABELS
        assert set(r['existing_stage_ids']) <= stage_ids
        assert r['reason'].strip()
        for target in r['target'].split():
            assert target in card_ids | stage_ids, (r['id'], target)
        if r['decision'] == 'expand':
            assert len(r['additional_situations']) >= 3
    for c in cards:
        assert c['decision'] in ['add', 'split', 'defer', 'reframe']
        assert c['priority'] in ['P1', 'P2', 'P3']
        assert 5 <= len(c['situations']) <= 8 and len(set(c['situations'])) == len(c['situations'])
        assert c['authoring_ready'] is False
        assert c['situation_origin'] == 'editorial_proposal_not_book_transcription'
        assert set(c['existing_stage_ids']) <= stage_ids
        assert set(c['lookup_books']) <= {x['book_id'] for x in data['audit']}
        assert set(c['web_refs']) <= set(web)
        for e in c['book_evidence']:
            assert e['id'] in evidence and e['relation'] in RELATIONS
    assert len(data['travel']) == 16 and len({x['id'] for x in data['travel']}) == 16
    for t in data['travel']:
        assert t['count_as_new_stage'] is False
        assert set(t['host_refs']) <= card_ids | stage_ids
        assert len(t['situations']) >= 3
    return base

def statistics(data, base):
    cards = data['cards']
    chosen = [c for c in cards if c['decision'] in ['add', 'split']]
    return {
        'base_stages': len(base),
        'base_levels': dict(Counter(x['level'] for x in base)),
        'base_seeds': sum(len(x['situations']) for x in base),
        'ai120_decisions': dict(Counter(x['decision'] for x in data['reviews'])),
        'own_additions': len(data['own']),
        'cards': len(cards),
        'proposed_add_or_split': len(chosen),
        'conceptually_new': sum(x['decision'] == 'add' for x in chosen),
        'split_existing_scope': sum(x['decision'] == 'split' for x in chosen),
        'proposed_by_priority': dict(Counter(x['priority'] for x in chosen)),
        'proposed_by_entry_level': dict(Counter(x['level'].split(' → ')[0] for x in chosen)),
        'cards_with_some_topic_or_event_evidence': sum(any(e['relation'] in ['direct_topic', 'partial_event'] for e in c['book_evidence']) for c in cards),
        'cards_without_topic_or_event_evidence_yet': sum(not any(e['relation'] in ['direct_topic', 'partial_event'] for e in c['book_evidence']) for c in cards),
        'preview_situation_seeds': sum(len(c['situations']) for c in cards),
        'expansion_seeds': sum(len(r.get('additional_situations', [])) for r in data['reviews']),
        'travel_contexts_not_new_stages': len(data['travel']),
        'book_evidence_windows': len(data['sources']['book_evidence']),
        'books_with_selected_body_windows': len({e['book'] for e in data['sources']['book_evidence']}),
        'web_sources': len(data['sources']['web']),
        'final_v5_stage_count': None,
        'note': 'Counts describe an editorial preview, not a completed, source-verified V5 or textbook coverage percentage.'
    }

def render_md(data, base, stats):
    text = ['# Kết quả rà soát và bản xem trước V5\n', '> Chưa áp dụng vào 194 chặng. Đọc bản này để duyệt hướng; xem TOPIC_CARDS.md để đọc mọi tình huống.\n']
    text += ['## Kết quả định lượng\n', f"- **120/120** đề xuất gốc đã có quyết định: **47 bổ sung**, **44 tách sâu**, **14 mở rộng tại chỗ**, **9 gộp**, **4 làm rõ chặng cũ**, **2 để lựa chọn sau**.", f"- Có thêm **13** phương án sau đối chiếu: 5 bổ sung và 8 tách sâu.", f"- Kho đề xuất gồm **{stats['proposed_add_or_split']} phương án bổ sung/tách**: **{stats['conceptually_new']} topic mới về phạm vi** và **{stats['split_existing_scope']} phần đã có cần tách sâu**. Không gọi toàn bộ là 104 chủ đề chưa từng có.", f"- Trong 104 phương án: **{stats['proposed_by_priority'].get('P1',0)} P1**, **{stats['proposed_by_priority'].get('P2',0)} P2**, **{stats['proposed_by_priority'].get('P3',0)} P3**; P3 chủ yếu theo hoàn cảnh riêng.", f"- **{stats['cards']} thẻ** có tổng **{stats['preview_situation_seeds']} seed tình huống**; gồm 104 phương án trên, 4 làm rõ chặng cũ và 2 để sau. 14 mở rộng có thêm {stats['expansion_seeds']} seed riêng; 16 địa danh/mô-đun được để ngoài phép đếm chặng.", f"- **{stats['cards_with_some_topic_or_event_evidence']} thẻ** có đoạn đã đọc hỗ trợ ít nhất một phần topic/sự kiện; **{stats['cards_without_topic_or_event_evidence_yet']} thẻ** còn cần nguồn trực tiếp, dù có thể có nền chức năng nói. Đây không phải tỷ lệ dùng sách và không là tỷ lệ được xác nhận của các seed.", '- **Chưa chốt tổng chặng V5**: 194 + 104 = 298 chỉ là kịch bản giữ nguyên mọi chặng mẹ; chưa khử các ô cần gộp/đổi thành bài tổng hợp. Không đề nghị chốt 298.\n']
    text += ['## Mở tài liệu\n', '- [Danh sách đầy đủ và tình huống từng thẻ](TOPIC_CARDS.md)', '- [Đối chiếu đủ 120 đề xuất gốc](REVIEW_AI120.md)', '- [16 lớp bối cảnh du lịch](TRAVEL.md)', '- [Sổ nguồn và vai trò 27 sách](SOURCE_AUDIT.md)', '- [Bản tra cứu có bộ lọc](PREVIEW.html)', '- Dữ liệu: `candidates.jsonl`, `review_ai120.jsonl`, `own_additions.jsonl`, `travel_modules.json`, `sources.json`, `book_audit.json`, `snapshot.json`, `stats.json`.\n']
    text.append((HERE / 'EDITORIAL.md').read_text(encoding='utf8').split('\n', 1)[1])
    text.append('\n## Nhóm P1 nên duyệt trước\n\nP1 là thứ tự ưu tiên đầu tư nội dung; mỗi người chỉ cần chọn nhánh phù hợp. Không phải yêu cầu viết hết nhóm này ngay.\n')
    for track in ['Đời sống', 'Công việc']:
        text.append(f'### {track}\n')
        for c in data['cards']:
            if c['priority'] == 'P1' and c['track'] == track:
                text.append(f"- **{c['id']} — {c['title']}** · {c['level']} · {LABELS[c['decision']]}")
        text.append('')
    (HERE / 'V5_PREVIEW.md').write_text('\n'.join(text) + '\n', encoding='utf8')
    text = ['# Toàn bộ thẻ topic/tình huống V5 đề xuất\n', '[Đọc kết luận và cách duyệt](V5_PREVIEW.md) · [Tra nguồn](SOURCE_AUDIT.md)\n', 'Các tình huống dưới đây là phác thảo biên tập. Sáu seed không có nghĩa phải có đúng sáu bài hoặc mọi seed đã có trong sách. `Bxx` tra tiếp khác với `Exx` đã đọc. ID tạm không là thứ tự học.\n']
    group = None
    for c in data['cards']:
        if group != c['group']:
            group = c['group']; text.append(f'## {group}\n')
        text += [f"### {c['id']} — {c['title']}\n", f"**{LABELS[c['decision']]} · {c['priority']} · {c['level']} · {c['track']}**  ", f"Đối tượng: {c['audience']}. Liên quan: {', '.join(c['existing_stage_ids']) or 'không có chặng tương ứng rõ'}.\n", f"**Ranh giới:** {c['difference']}\n", f"**Bố trí khi được duyệt:** {c['migration']}\n"]
        for i, s in enumerate(c['situations'], 1): text.append(f'{i}. {s}.')
        text.append('')
        refs = [f"{e['id']} ({RELATIONS[e['relation']]})" for e in c['book_evidence']]
        text += [f"**Đoạn đọc:** {', '.join(refs) or 'chưa có đoạn trực tiếp'}.", f"**Tra tiếp trong sách:** {', '.join(c['lookup_books']) or 'chưa chỉ định'}. **Memo:** {', '.join(c['memo_refs']) or 'không gắn'}. **Web:** {', '.join(c['web_refs']) or 'chưa gắn nguồn riêng'}.", f"**Tình trạng:** {c['source_status']}"]
        if c.get('safety_entry'): text.append(c['safety_entry'])
        if c['fact_check']: text.append('**Cần kiểm dữ kiện khi soạn:** quy định/quy trình theo cơ quan, địa phương và thời điểm; preview chỉ là khung giao tiếp.')
        text.append('')
    (HERE / 'TOPIC_CARDS.md').write_text('\n'.join(text) + '\n', encoding='utf8')
    text = ['# Đánh giá đủ 120 đề xuất AI\n', '[Kết luận](V5_PREVIEW.md) · [Thẻ tình huống](TOPIC_CARDS.md)\n', 'Giữ nguyên số thứ tự đính kèm. Bổ sung/tách có thẻ V5P tương ứng; gộp trỏ đến thẻ hoặc chặng tiếp nhận.\n']
    for r in data['reviews']:
        text += [f"## {r['id']} — {LABELS[r['decision']]}\n", f"**Đề xuất gốc:** {r['original_proposal']}\n", f"**Đánh giá:** {r['reason']}\n", f"**Chặng cũ liên quan:** {', '.join(r['existing_stage_ids']) or 'xem đích gộp'}. **Đích:** {r['target']}.\n"]
        if r.get('additional_situations'):
            text.append('Tình huống nên thêm tại chặng cũ:\n')
            text += [f'- {s}.' for s in r['additional_situations']]; text.append('')
    (HERE / 'REVIEW_AI120.md').write_text('\n'.join(text) + '\n', encoding='utf8')
    text = ['# 16 lớp bối cảnh du lịch — không mặc định 16 chặng mới\n', 'Tên địa danh là cách tạo hứng thú và thay bối cảnh. Chặng gốc phải có mục tiêu giao tiếp khác trước khi tăng số. Các điểm đến chưa được kiểm toàn bộ hoạt động/quy định; cần tra nguồn chính thức khi viết chi tiết.\n']
    for t in data['travel']:
        text += [f"## {t['id']} — {t['title']}\n", t['recommendation'] + '\n', f"**Chặng nhận:** {', '.join(t['host_refs'])}.\n"]
        text += [f'- {s}.' for s in t['situations']]; text.append('')
    (HERE / 'TRAVEL.md').write_text('\n'.join(text) + '\n', encoding='utf8')
    text = ['# Sổ nguồn và phạm vi đọc\n', f"Ngày 13/11/2026. {len(data['audit'])} hồ sơ sách/chỉ mục được đối chiếu; {stats['book_evidence_windows']} cửa sổ nội dung được ghi nhận ở {stats['books_with_selected_body_windows']} cuốn. Không phải đọc lại trọn {len(data['audit'])} PDF. Không có trang PDF nào được xác minh ảnh lại trong lượt preview.\n", '## Vai trò cả 27 sách\n']
    for b in data['audit']:
        text += [f"### {b['book_id']} — {b['title']}\n", b['role_in_unified_course'] + '\n', f"**Đầu mối tích hợp:** {', '.join(b['possible_targets_not_verified_mapping'])}. Đây là hướng tuyển chọn, chưa phải mapping nội dung đã xác nhận.  ", f"**Đoạn ghi nhận đã đọc:** {', '.join(b['body_evidence_read']) or 'chưa có cửa sổ nội dung được ghi vào sổ lượt này; chỉ mục/hồ sơ'}.  ", f"**Kho clean:** {md_link('Thư mục sách', b['directory'])}.\n"]
    text += ['## Các đoạn sách đã đọc\n', 'Mỗi đoạn có hash và giới hạn hỗ trợ trong sources.json. Nguồn cùng chức năng hoặc khác vai không được gọi là phủ đủ topic.\n']
    for e in data['sources']['book_evidence']:
        text += [f"### {e['id']} — {e['book']}\n", f"{md_link('Mở đoạn nguồn', e['path'], e['line_start'])} · dòng {e['line_start']}–{e['line_end']}.\n", f"**Có:** {e['supports']}\n", f"**Không chứng minh:** {e['does_not_establish']}\n"]
    text.append('## Nguồn internet và giới hạn\n')
    for w in data['sources']['web']:
        text += [f"### {w['id']} — {w['title']}\n", f"[{w['title']}]({w['url']}) · {w['kind']} · truy cập {w['accessed']}.\n", w['scope_read'] + '\n', '**Giới hạn:** ' + w['limitation'] + '\n']
    text += ['## Memo và độ tin cậy\n', md_link('Memo web hiện có', data['sources']['memo_file']), '\nMemo chỉ có mục lục/mô tả, không thay toàn văn. Nguồn cộng đồng và diễn đàn gợi ý nhu cầu, không xác minh quy định. Các seed tình huống mới vẫn là đề xuất biên tập cho đến khi được soạn và kiểm nguồn riêng.\n']
    (HERE / 'SOURCE_AUDIT.md').write_text('\n'.join(text), encoding='utf8')


def render_html(data, base, stats):
    payload = json.dumps({'cards': data['cards'], 'reviews': data['reviews'], 'travel': data['travel'], 'stats': stats, 'evidence': data['sources']['book_evidence'], 'web': data['sources']['web'], 'base': {x['id']: x['title'] for x in base}}, ensure_ascii=False).replace('<', '\\u003c')
    template = r'''<!doctype html>
<html lang="vi"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>V5 Kaiwa — bản duyệt topic và tình huống</title>
<style>
:root{color-scheme:light dark;--bg:#fafaf8;--fg:#202724;--muted:#58645d;--line:#d5dcd6;--accent:#176246;--panel:#f0f3ef}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.65 system-ui,sans-serif}header,main{max-width:1180px;margin:auto;padding:22px 28px}h1{font-size:27px;line-height:1.3;margin:10px 0}h2{font-size:20px;margin-top:20px}h3{font-size:17px;margin:0}a{color:var(--accent)}.muted,.meta{color:var(--muted)}.metrics{display:flex;gap:32px;flex-wrap:wrap;border-block:1px solid var(--line);padding:14px 0;margin:22px 0}.metrics strong{display:block;font-size:25px;color:var(--accent)}.controls{display:flex;gap:8px;flex-wrap:wrap;position:sticky;top:0;background:var(--bg);padding:12px 0;border-bottom:1px solid var(--line);z-index:2}input,select,button{font:inherit;color:inherit;background:var(--bg);border:1px solid var(--line);border-radius:4px;padding:8px}input{flex:1;min-width:220px}button{cursor:pointer}button[aria-pressed=true]{background:var(--accent);color:white}details{border-bottom:1px solid var(--line);padding:14px 0}summary{cursor:pointer;list-style-position:outside;padding-right:10px}summary strong{font-size:17px}summary .meta{display:block;padding-left:16px;font-size:14px}.body{max-width:900px;margin-left:18px;padding-top:8px}.tag{color:var(--accent);font-weight:650}.source{background:var(--panel);padding:12px 16px}.source p{margin:8px 0}li{margin:5px 0}.intro{max-width:900px}.small{font-size:14px}.tabs{display:flex;gap:8px;flex-wrap:wrap}.no-print{display:block}@media(prefers-color-scheme:dark){:root{--bg:#18201c;--fg:#e3e9e4;--muted:#aebbb1;--line:#45544a;--accent:#8bd6ac;--panel:#232e27}button[aria-pressed=true]{color:#18201c}}@media(max-width:650px){header,main{padding:16px}.controls{position:static}h1{font-size:23px}}@media print{.controls,.tabs,.no-print{display:none}details{break-inside:avoid}body{font-size:11px}}
</style>
<header><p class="tag">KAIWA / PREVIEW V5 / 13.11.2026</p><h1>Dày hơn bằng nhiệm vụ thật, giữ ranh giới giữa các chặng</h1>
<p class="intro">Đã đánh giá 120 đề xuất và thêm 13 phương án sau đối chiếu. Bản này để duyệt phạm vi và tình huống, chưa thay khung 194 chặng. <strong>104 phương án bổ sung/tách không đồng nghĩa 104 topic chưa từng có.</strong></p>
<div class="metrics"><div><strong>52</strong>Topic mới về phạm vi</div><div><strong>52</strong>Phần đang có cần tách sâu</div><div><strong>4</strong>Chặng cũ làm rõ lại</div><div><strong>16</strong>Bối cảnh du lịch</div></div>
<p class="small muted">Cơ sở: khung 194/645, hồ sơ và chỉ mục 27 sách; đọc chọn đoạn liên quan. Không đọc lại toàn văn 27 PDF. Các seed là đề xuất biên tập; bằng chứng cùng chức năng/khác vai được phân biệt với nguồn đúng topic. P1/P2/P3 là ưu tiên biên soạn, không là cổng học.</p>
<p><a href="V5_PREVIEW.md">Đọc kết luận & cách bố trí</a> · <a href="SOURCE_AUDIT.md">Sổ nguồn</a> · <a href="TOPIC_CARDS.md">Toàn bộ tình huống</a></p>
<div class="tabs" id="tabs"><button data-tab="cards" aria-pressed="true">Thẻ topic</button><button data-tab="reviews" aria-pressed="false">Đánh giá đủ 120 ý</button><button data-tab="travel" aria-pressed="false">Du lịch</button></div></header>
<main><div class="controls"><input id="q" aria-label="Tìm kiếm" placeholder="Tìm topic, tình huống, ID cũ/mới hoặc tên sách Bxx…"><select id="action" aria-label="Quyết định"><option value="">Mọi quyết định</option value="add">Bổ sung</option><option value="split">Tách sâu</option><option value="expand">Mở rộng tại chỗ</option><option value="merge">Gộp</option><option value="reframe">Làm rõ chặng cũ</option><option value="defer">Lựa chọn sau</option></select><select id="level" aria-label="Cấp độ"><option value="">Mọi cấp</option><option>Sơ</option><option>Trung</option><option>Thượng</option></select><select id="priority" aria-label="Ưu tiên"><option value="">Mọi ưu tiên</option><option>P1</option><option>P2</option><option>P3</option></select><select id="track" aria-label="Nhánh"><option value="">Đời sống & công việc</option><option>Đời sống</option><option>Công việc</option></select></div><p id="count" class="muted" aria-live="polite"></p><section id="results"></section></main>
<script id="data" type="application/json">__DATA__</script>
<script>
'use strict';
const D=JSON.parse(document.getElementById('data').textContent);
const labels={add:'Bổ sung',split:'Tách từ phạm vi đang có',expand:'Mở rộng chặng cũ',merge:'Gộp',reframe:'Làm rõ chặng cũ',defer:'Lựa chọn sau'};
const relations={direct_topic:'đúng topic',partial_event:'một phần sự kiện',function_only:'chỉ cùng chức năng nói',other_role:'khác vai',context_only:'chỉ bối cảnh',counterexample:'không coi là mẫu ứng xử'};
const E=Object.fromEntries(D.evidence.map(e=>[e.id,e]));const W=Object.fromEntries(D.web.map(w=>[w.id,w]));
let tab='cards';const $=id=>document.getElementById(id);const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const norm=s=>String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[đĐ]/g,'d').toLowerCase();
const items=s=>'<ol>'+s.map(t=>'<li>'+esc(t)+'</li>').join('')+'</ol>';
const old=ids=>ids.map(id=>esc(id+' — '+(D.base[id]||''))).join('<br>');
function sources(c){let body=c.book_evidence.map(r=>{const e=E[r.id];return '<p><strong>'+esc(r.id+' / '+e.book+' / '+relations[r.relation])+'</strong><br>'+esc(e.supports)+'<br><span class="muted">Giới hạn: '+esc(e.does_not_establish)+'</span></p>'}).join('');return '<div class="source"><strong>'+esc(c.source_status)+'</strong>'+body+'<p>Tra tiếp (chưa xác nhận mapping): '+esc(c.lookup_books.join(', '))+'</p><p>Memo: '+esc(c.memo_refs.join(', ')||'chưa gắn')+'</p><p>'+c.web_refs.map(id=>'<a target="_blank" rel="noopener" href="'+esc(W[id].url)+'">'+esc(id+' — '+W[id].title)+'</a>').join('<br>')+'</p></div>'}
function card(c){return '<details id="'+esc(c.id)+'"><summary><strong>'+esc(c.id+' — '+c.title)+'</strong><span class="meta">'+esc([labels[c.decision],c.priority,c.level,c.track].join(' · '))+'</span></summary><div class="body"><p><strong>Ranh giới: </strong>'+esc(c.difference)+'</p><p><strong>Chặng liên quan:</strong><br>'+old(c.existing_stage_ids)+'</p><p><strong>Khi được duyệt: </strong>'+esc(c.migration)+'</p><p class="muted">Đối tượng: '+esc(c.audience)+'. Sáu seed dưới đây là phác thảo, chưa là sáu bài đã soạn.</p>'+items(c.situations)+(c.safety_entry?'<p>'+esc(c.safety_entry)+'</p>':'')+sources(c)+(c.fact_check?'<p class="small">Khi viết chi tiết cần kiểm dữ kiện theo thời điểm, cơ quan và địa phương. Chưa có bài được tự động sinh từ thẻ này.</p>':'')+'</div></details>'}
function review(r){return '<details><summary><strong>'+esc(r.id+' — '+labels[r.decision])+'</strong><span class="meta">'+esc(r.original_proposal)+'</span></summary><div class="body"><p>'+esc(r.reason)+'</p><p><strong>Đích:</strong> '+esc(r.target)+'</p><p>'+old(r.existing_stage_ids)+'</p>'+(r.additional_situations?items(r.additional_situations):'')+'</div></details>'}
function travel(t){return '<details><summary><strong>'+esc(t.id+' — '+t.title)+'</strong><span class="meta">Bối cảnh, chưa cộng chặng</span></summary><div class="body"><p>'+esc(t.recommendation)+'</p><p>Chặng nhận: '+esc(t.host_refs.join(', '))+'</p>'+items(t.situations)+'<p class="muted">Chưa kiểm đầy đủ dữ kiện điểm đến. Tra nguồn chính thức trước khi soạn.</p></div></details>'}
function render(){const q=norm($('q').value),act=$('action').value,lvl=$('level').value,pri=$('priority').value,tr=$('track').value;
const list=D[tab].filter(c=>{if(q&&!norm(JSON.stringify(c)).includes(q))return false;if(tab==='cards')return(!act||c.decision===act)&&(!lvl||c.level.includes(lvl))&&(!pri||c.priority===pri)&&(!tr||c.track===tr);if(tab==='reviews')return !act||c.decision===act;return true});
$('count').textContent=list.length+' / '+D[tab].length+' mục. '+(tab==='cards'?'52 bổ sung + 52 tách + 4 làm rõ + 2 để sau.':tab==='reviews'?'Bộ lọc cấp/ưu tiên/nhánh chỉ áp dụng cho thẻ topic.':'Không tự động tạo một chặng cho mỗi địa danh.');
$('results').innerHTML=list.map(tab==='cards'?card:tab==='reviews'?review:travel).join('')||'<p>Không có kết quả theo bộ lọc này. Thử bỏ bớt điều kiện.</p>';}
['q','action','level','priority','track'].forEach(id=>$(id).addEventListener(id==='q'?'input':'change',render));
document.querySelectorAll('[data-tab]').forEach(b=>b.addEventListener('click',()=>{tab=b.dataset.tab;document.querySelectorAll('[data-tab]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));render()}));render();
</script></html>'''
    (HERE / 'PREVIEW.html').write_text(template.replace('__DATA__', payload), encoding='utf8')

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--write', action='store_true'); args = parser.parse_args()
    data = load(); base = validate(data); stats = statistics(data, base)
    if args.write:
        (HERE / 'stats.json').write_text(json.dumps(stats, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
        render_md(data, base, stats); render_html(data, base, stats)
        for path in HERE.glob('*.md'):
            clean = '\n'.join(line.rstrip() for line in path.read_text(encoding='utf8').splitlines()).rstrip() + '\n'
            path.write_text(clean, encoding='utf8')
    print(json.dumps({'valid': True, **stats}, ensure_ascii=False, indent=2))

if __name__ == '__main__': main()
