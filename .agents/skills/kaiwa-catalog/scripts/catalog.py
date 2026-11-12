"""Structure-first metadata index; no model/API calls and no source mutations."""
from pathlib import Path
from collections import defaultdict, Counter
import argparse
import hashlib
import json
import re
import unicodedata

EXCLUDED = {'Danh sách 1160 từ vựng MINATO DORIMU', 'TỔNG HỢP 1170 TỪ VỰNG MIMIKARA N1', 'TỔNG HỢP 880 TỪ VỰNG MIMIKARA N3'}
OUT = Path('kaiwa_skill/planning/catalog27')
CACHE = Path('kaiwa_skill/.cache/catalog27-packets')
HEAD = re.compile(r'^(#{1,6})\s+(.+)$')
ANCHOR = re.compile(r'(?:<a\s+id="([^"]+)"|unit_id:\s*([^\s>]+))')
NUM = re.compile(r'^\s*(?:[-*]\s+)?(?:\d+[.)]|[①②③④⑤⑥⑦⑧⑨⑩])\s*(.+)$')
LEVELS = {'sơ', 'trung', 'thượng'}


def readj(p):
    return json.loads(p.read_text(encoding='utf-8'))


def writej(p, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def clean(s):
    return re.sub(r'\s+', ' ', re.sub(r'[*`]', '', s)).strip()


def short(s, n=105):
    s = clean(s)
    return s if len(s) <= n else s[:n - 1] + '…'


def key(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip().casefold()


def phrases(items):
    return '; '.join(clean(s).rstrip(' .;') for s in items)


def extract(text, bid, cid):
    """Retain headings, numbered material and titled microcontexts, not body summaries."""
    lines = text.splitlines()
    rows, stack, anchor = [], [], None
    for i, line in enumerate(lines):
        am = ANCHOR.search(line)
        if am:
            anchor = am[1] or am[2]
        hm = HEAD.match(line)
        kind, label = None, None
        if hm:
            depth = len(hm[1])
            stack = [(d, s) for d, s in stack if d < depth]
            label, kind = clean(hm[2]), 'heading'
            stack.append((depth, label))
        else:
            nm = NUM.match(line)
            if nm:
                value = nm[1]
                bm = re.match(r'\*\*([^*]+)\*\*', value)
                if bm and bm[1].strip() not in {'C', 'JP:', 'JP', 'A:', 'B:', 'VI:', 'VI'} and not re.fullmatch(r'[A-Z](?:[/・ ]+[A-Z])*', bm[1].strip()):
                    label, kind = short(bm[1]), 'named_item'
                    if re.search(r'\(JP\)|\(VI\)', value):
                        kind = 'situation_caption'
                else:
                    end = i + 1
                    while end < min(len(lines), i + 12) and not (HEAD.match(lines[end]) or NUM.match(lines[end])):
                        end += 1
                    look = '\n'.join(lines[i:end])
                    vm = re.search(r'(?:\*\*VI:\*\*|\(VI\):|\*\*VI\*\*:)\s*([^\n]+)', look)
                    label = short(vm[1] if vm else value, 105)
                    if label and label not in {'C', 'JP', 'VI'}:
                        label = f'{line.strip().split()[0]} {label}'
                        kind = 'numbered_material'
            elif re.match(r'^\*\*(?:POINT|Related|Variation|Words|Gợi ý|Lưu ý|Cách dùng|Diễn đạt)', line, re.I):
                label, kind = short(line), 'knowledge_label'
        if kind:
            rows.append({'book_id': bid, 'chapter_id': cid, 'line': i + 1, 'anchor': anchor,
                         'kind': kind, 'label': label, 'context': [s for _, s in stack[-2:]]})
    return rows


def intro(text, limit=1550):
    picks, used = [], 0
    blocks = re.split(r'(?m)(?=^#{1,5}\s)', text)
    pattern = re.compile(r'はじめに|使い方|ねらい|対象|特徴|目的|構成|lời (?:đầu|nói đầu|mở đầu)|mục đích|cách dùng|cấu trúc|trình tự|luồng học', re.I)
    for block in blocks:
        first = block.splitlines()[0] if block.splitlines() else ''
        if pattern.search(first):
            excerpt = short(block, min(430, limit - used))
            if excerpt:
                picks.append(excerpt)
                used += len(excerpt)
            if used >= limit - 100:
                break
    return '\n'.join(picks) if picks else short(text, min(limit, 850))


def prepare(root):
    out, cache = root / OUT, root / CACHE
    metas = sorted((root / 'kaiwa_skill/knowledge').glob('*/_meta/book.json'))
    assert len(metas) == 30, f'Expected30 knowledge sources, got{len(metas)}'
    selected = [p for p in metas if p.parent.parent.name not in EXCLUDED]
    assert len(selected) == 27
    books, rows, packets = [], [], {}
    for i, mp in enumerate(selected, 1):
        m, b = readj(mp), mp.parent.parent
        bid = f'B{i:02d}'
        chapters, prows = [], []
        intro_text = []
        for j, rel in enumerate(m['scope']['chapters'], 1):
            p = b / rel
            text = p.read_text(encoding='utf-8')
            cid = f'{bid}-C{j:02d}'
            title = next((clean(x[2]) for x in [HEAD.match(s) for s in text.splitlines()] if x), p.stem)
            cr = extract(text, bid, cid)
            rows.extend(cr)
            ch = {'chapter_id': cid, 'path': p.relative_to(root).as_posix(), 'sha256': sha(p),
                  'title': title, 'line_count': len(text.splitlines()), 'entry_count': len(cr)}
            chapters.append(ch)
            candidates = [x['label'] for x in cr if x['kind'] in {'heading', 'situation_caption'} and x['label'] != title]
            preview = list(dict.fromkeys(candidates))
            # One early and one later heading give shape without sending the chapter body.
            samples = preview[:1] + (preview[len(preview)//2:len(preview)//2+1] if len(preview) > 2 else preview[1:2])
            prows.append({'chapter_id': cid, 'title': short(title, 105), 'peek': [short(s, 75) for s in samples]})
            if j <= 3:
                intro_text.append(text)
        unitp = b / '_meta/units.jsonl'
        units = [json.loads(s) for s in unitp.read_text(encoding='utf-8').splitlines() if s.strip()]
        book = {'book_id': bid, 'title': m['title'], 'directory': b.relative_to(root).as_posix(),
                'source_sha256': sha(b / 'book.md'), 'source_pdf_sha256': m['source_pdf']['sha256'],
                'pdf_pages': len(m['scope']['pdf_pages']), 'unit_count': len(units),
                'needs_review_units': sum(u.get('review_status') == 'needs_review' for u in units),
                'units_with_issues': sum(bool(u.get('issues')) for u in units), 'chapters': chapters}
        books.append(book)
        packets[bid] = {'book_id': bid, 'title': m['title'], 'directory': book['directory'],
                        'source_sha256': book['source_sha256'], 'intro_excerpt': intro('\n'.join(intro_text)),
                        'identity_excerpt': short((b / m['scope']['chapters'][0]).read_text(encoding='utf-8'), 520),
                        'source_warnings': {'needs_review_units': book['needs_review_units'], 'units_with_issues': book['units_with_issues']},
                        'chapters': prows}
    old = readj(out / 'manifest.json') if (out / 'manifest.json').exists() else None
    if old:
        signature = lambda b: (b['book_id'], b['source_sha256'], [(c['path'], c['sha256']) for c in b['chapters']])
        assert [signature(b) for b in old['books']] == [signature(b) for b in books], 'Source changed: use a separate snapshot/review; do not silently overwrite'
    lanes, loads = [[], [], []], [0, 0, 0]
    if old:
        lanes = [old['lanes'][str(i+1)] for i in range(3)]
        loads = [sum(len(json.dumps(packets[bid], ensure_ascii=False)) for bid in lane) for lane in lanes]
    else:
        for bid in sorted(packets, key=lambda x: len(json.dumps(packets[x], ensure_ascii=False)), reverse=True):
            lane = min(range(3), key=lambda n: loads[n])
            lanes[lane].append(bid)
            loads[lane] += len(json.dumps(packets[bid], ensure_ascii=False))
    manifest = {'schema_version': 1, 'scope': '27metadata catalogs;3lexicons reference-only',
                'excluded_reference_only': sorted(EXCLUDED), 'books': books,
                'lanes': {str(i+1): lane for i, lane in enumerate(lanes)},
                'packet_chars_by_lane': loads, 'structural_index_rows': len(rows),
                'index_counts_by_kind': dict(Counter(r['kind'] for r in rows)),
                'limits': 'Machine structure scan; targeted AI metadata. Not a full semantic read of every sentence.'}
    writej(out / 'manifest.json', manifest)
    for bid, packet in packets.items():
        writej(cache / f'{bid}.json', packet)
    (out / 'annotations').mkdir(parents=True, exist_ok=True)
    with (out / 'source_index.jsonl').open('w', encoding='utf-8') as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(json.dumps({'books': len(books), 'chapters': sum(len(b['chapters']) for b in books),
                      'pdf_pages': sum(b['pdf_pages'] for b in books), 'index_rows': len(rows),
                      'packet_chars': sum(loads), 'lanes': manifest['lanes']}, ensure_ascii=False))


def link(root, out, path, line=None, anchor=None):
    import os
    rel = Path(os.path.relpath(root / path, out)).as_posix()
    return f'<{rel}' + (f'#{anchor}' if anchor else '') + '>'


def build(root):
    out = root / OUT
    m = readj(out / 'manifest.json')
    assert len(m['books']) == 27, 'Build requires the complete27-source manifest'
    profiles = {}
    for b in m['books']:
        assert sha(root / b['directory'] / 'book.md') == b['source_sha256'], f'Stale book {b["book_id"]}'
        for ch in b['chapters']:
            assert sha(root / ch['path']) == ch['sha256'], f'Stale chapter {ch["chapter_id"]}'
        a = readj(out / 'annotations' / f'{b["book_id"]}.json')
        assert a['book_id'] == b['book_id'] and a['source_sha256'] == b['source_sha256']
        assert {c['chapter_id'] for c in a['chapters']} == {c['chapter_id'] for c in b['chapters']}
        assert len(a['chapters']) == len(b['chapters'])
        for c in a['chapters']:
            assert c['kind'] in {'lesson', 'front', 'reference', 'answers', 'publication'}
            assert c['summary'].strip() and isinstance(c['topics'], list)
            assert set(c['levels']) <= LEVELS
        assert set(a['levels']) <= LEVELS and a['purpose'].strip()
        profiles[b['book_id']] = a
    guide = ['# Mục lục tổng hợp 27 sách kaiwa', '', 'Metadata ngắn để chọn sách và tìm chương/phần. Có 486 file chương/phần trong bản clean, gồm cả hướng dẫn và phụ lục; không phải 486 chương bài học theo bản in. Máy quét cấu trúc; AI đọc trích đoạn có mục tiêu, chưa phân tích ngữ nghĩa từng câu. Level là nhãn/khoảng sơ bộ, chưa quyết định lộ trình.', '', '<a id="tra-theo-ten-sach"></a>', '## Tra theo tên sách', '']
    guide += [f'- [{b["book_id"]} — {b["title"]}](#{b["book_id"].lower()})' for b in m['books']]
    guide.append('')
    topics = defaultdict(list)
    for b in m['books']:
        a = profiles[b['book_id']]
        guide += [f'<a id="{b["book_id"].lower()}"></a>', f'## {b["book_id"]} — {b["title"]}', '', f'- **Dùng để:** {a["purpose"]}',
                  f'- **Thế mạnh:** {phrases(a["strengths"])}.', f'- **Cách học:** {phrases(a["methods"])}.',
                  f'- **Kiến thức:** {phrases(a["knowledge"])}.',
                  f'- **Level:** {a["level_source"].rstrip(" .;")}; phạm vi gợi ý: {", ".join(a["levels"]) or "chưa rõ"}. {a["level_note"]}',
                  f'- **Phạm vi:** {b["pdf_pages"]} trang/{len(b["chapters"])} chương-phần/{b["unit_count"]} unit; {b["needs_review_units"]} unit needs_review, {b["units_with_issues"]} unit có ghi chú issues.', '',
                  f'[Bản đọc]({link(root,out,b["directory"]+"/book.md")}) · [Thông tin audio]({link(root,out,b["directory"]+"/_meta/audio.md")})', '']
        amap = {c['chapter_id']: c for c in a['chapters']}
        for c in b['chapters']:
            ac = amap[c['chapter_id']]
            guide += [f'- **{c["chapter_id"]} — [{c["title"]}]({link(root,out,c["path"])})**: {ac["summary"]} · `{ac["kind"]}`' + (f' · {", ".join(ac["levels"])}' if ac['levels'] else '')]
            if ac['kind'] == 'lesson':
                for topic in ac['topics']:
                    topic = clean(topic).strip(' .;')
                    if topic:
                        topics[key(topic)].append((topic, b['book_id'], c, ac['levels']))
        guide.append('')
    (out / 'BOOK_GUIDE.md').write_text('\n'.join(guide).rstrip() + '\n', encoding='utf-8')
    tt = ['# Topic tổng hợp từ 27 sách', '', f'Có **{len(topics)} nhãn topic/chức năng metadata** được hợp theo chữ sau chuẩn hóa khoảng trắng/Unicode; nhãn gần nghĩa có thể còn đứng riêng. Đây chưa phải taxonomy cuối hoặc mọi khái niệm ngầm trong từng câu.', '', 'Mỗi nhãn dẫn đến sách/chương có liên quan. Mã Bxx là sách, Cxx là file chương/phần; [tra tên sách](BOOK_GUIDE.md#tra-theo-ten-sach). [Tất cả nhãn nguồn chi tiết](SOURCE_LABELS.md) và `source_index.jsonl` bổ sung tình huống nhỏ, biểu đạt, bài tập; [mục lục sách](BOOK_GUIDE.md) mô tả công dụng/cách học.', '']
    for _, vals in sorted(topics.items()):
        label = vals[0][0]
        levels = [l for l in ['sơ','trung','thượng'] if any(l in v[3] for v in vals)]
        refs = list(dict.fromkeys(f'[{v[2]["chapter_id"]}]({link(root,out,v[2]["path"])})' for v in vals))
        tt += [f'- **{label}** — {", ".join(levels) or "chưa rõ"}; ' + ' · '.join(refs)]
    (out / 'TOPICS_ALL.md').write_text('\n'.join(tt) + '\n', encoding='utf-8')
    rows = [json.loads(s) for s in (out/'source_index.jsonl').read_text(encoding='utf-8').splitlines() if s]
    labels = defaultdict(list)
    chapters = {c['chapter_id']: c for b in m['books'] for c in b['chapters']}
    # No body interpretation: this register includes reference/method labels as explicitly typed records.
    for row in rows:
        labels[(row['kind'], key(row['label']))].append(row)
    ll = ['# Nhãn mục, tình huống và biểu đạt trích từ nguồn', '', f'**{len(labels)} nhãn phân biệt theo loại/chữ**, từ {len(rows)} vị trí cấu trúc. Gồm cả tên mục phương pháp/phụ lục; không gọi tất cả là topic. Đối thoại thiếu tên giữ mảnh lời nguồn để tìm, không đặt bối cảnh tưởng tượng.', '', 'Các vị trí có line number và anchor nằm trong `source_index.jsonl`. Mở file chapter rồi tìm nhãn nếu trình đọc không hỗ trợ #L.', '']
    for (kind, _), vals in sorted(labels.items()):
        r = vals[0]
        refs = list(dict.fromkeys(f'[{x["chapter_id"]}:{x["line"]}]({link(root,out,chapters[x["chapter_id"]]["path"],anchor=x.get("anchor"))})' for x in vals))
        ll += [f'- `{kind}` **{r["label"]}** — ' + ' · '.join(refs)]
    (out/'SOURCE_LABELS.md').write_text('\n'.join(ll)+'\n',encoding='utf-8')
    readme = ['# Chỉ mục metadata 27 sách', '', '[Topic tổng hợp](TOPICS_ALL.md) · [Mục lục sách/chương](BOOK_GUIDE.md) · [Nhãn nguồn chi tiết](SOURCE_LABELS.md)', '', f'27 sách; {sum(len(b["chapters"]) for b in m["books"])} chương/phần theo bản clean; {len(topics)} nhãn topic gộp; {len(rows):,} vị trí index. Ba tập từ vựng chỉ để tham chiếu, ghi trong manifest.', '', 'Đã quét cấu trúc toàn văn bằng script và bổ sung metadata bằng ba worker sol/high. Không phải đợt đọc sâu toàn corpus, không khẳng định đã khai phá mọi tình huống ngầm. Level còn sơ bộ; audio là inventory, chưa xác nhận file thực.', '', 'Tra cứu: tìm nhãn trong TOPICS_ALL/SOURCE_LABELS hoặc dùng rg trên source_index.jsonl. Dòng index cho book_id/chapter_id/line/anchor; manifest giải chapter_id ra đường dẫn. Một số nhãn được rút gọn còn105ký tự; nội dung đầy đủ vẫn ở nguồn. Khi biên soạn, mở đúng chương và tìm toàn văn trong knowledge để lấy kiến thức đầy đủ, gồm cả từ nằm ngoài nhãn.', '', f'Packet ở snapshot prepare hiện tại: {sum(m["packet_chars_by_lane"]):,} ký tự JSON theo serializer; đây không phải số token hoặc phần trăm quota. [Ghi nhận lượt chạy](RUN_SUMMARY.json) tách packet lúc giao việc và snapshot có thể bổ sung sau QA. Hash nguồn được kiểm trước build.', '']
    (out/'README.md').write_text('\n'.join(readme),encoding='utf-8')
    run = readj(out/'RUN_SUMMARY.json') if (out/'RUN_SUMMARY.json').exists() else {}
    run.update({'books':27,'chapters_parts':len(chapters),'topics_metadata_labels':len(topics),
                'source_labels':len(labels),'index_positions':len(rows),'source_hashes_checked':True,
                'reading_depth':'machine structure scan plus targeted AI metadata, not full semantic read'})
    writej(out/'RUN_SUMMARY.json',run)
    print(json.dumps({'books':27,'chapters':len(chapters),'topics':len(topics),'source_labels':len(labels),'index_rows':len(rows)},ensure_ascii=False))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command',choices=['prepare','build'])
    ap.add_argument('--repo-root',default='.')
    args=ap.parse_args()
    root=Path(args.repo_root).resolve()
    (prepare if args.command=='prepare' else build)(root)


if __name__=='__main__':
    main()
