import hashlib, json
from collections import Counter
from pathlib import Path

repo = Path('D:/CODE/git/kaiwa_skill')
cache = repo / '.cache/root-live-qa'
pdf = repo / 'kaiwa_skill/book/Kaiwa/日本人がよく使う日本語会話オノマトペ基本表現180.pdf'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source_sha = '458b548674d123f0e35c8df67395c3e569eab80ffa6e9c4a7848a8489547d439'
assert sha(pdf) == source_sha
splits = {210:[15,17,16],211:[17,14,16],212:[16,17,19],213:[18,16,4],214:[29,32],215:[31,31],216:[33,24]}
page_rows={}
for type_name, filename in [('english','onomato-index-english-rows.txt'),('japanese','onomato-index-japanese-rows.txt')]:
    page=None
    for raw in (cache/filename).read_text(encoding='utf-8').splitlines():
        if raw.startswith('# PDF'):
            page=int(raw.split('|',1)[0][5:]); page_rows[page]=[]
        elif raw:
            parts=raw.split('|')
            if type_name=='english':
                key,roman,refs=parts
                item={'english_key':key,'roman':roman,'printed_refs':refs,'refs':[int(x) for x in refs.split(',')]}
            else:
                roman,refs=parts
                item={'roman':roman,'printed_refs':refs,'refs':[int(x) for x in refs.split(',')]}
            page_rows[page].append(item)
pages=[]
for page in range(210,217):
    rows=page_rows[page]
    assert len(rows)==sum(splits[page])
    pos=0
    for col,count in enumerate(splits[page],1):
        for item in rows[pos:pos+count]:item['column']=col;item['ordinal_on_page']=pos+1;pos+=1
    image=cache/f'onomato-index-p{page}.png'
    pages.append({'pdf_page':page,'printed_page':page-1,'index_type':'english' if page<=213 else 'japanese','printed_heading':'英語さくいん / Index (English version)' if page<=213 else '日本語さくいん / Index (Japanese version)','rotation_degrees':270,'reading_order':'columns left to right, top to bottom within each','column_counts':splits[page],'raw_entry_count':len(rows),'expanded_ref_count':sum(len(x['refs']) for x in rows),'legibility':'all keys and references readable in the full-page render; no index entry lost to cropping','render':image.name,'render_sha256':sha(image),'entries':rows})
english=[x for p in pages if p['index_type']=='english' for x in p['entries']]
japanese=[x for p in pages if p['index_type']=='japanese' for x in p['entries']]
en_pairs=Counter((x['roman'],ref) for x in english for ref in x['refs'])
jp_pairs=Counter((x['roman'],ref) for x in japanese for ref in x['refs'])
assert en_pairs==jp_pairs
assert len(english)==185 and len(japanese)==180
assert len(en_pairs)==185
report={
 'source_pdf':'kaiwa_skill/book/Kaiwa/'+pdf.name,
 'source_pdf_sha256':source_sha,
 'review_scope':{'pdf_pages':[210,216],'printed_pages':[209,215],'index_only':True,'whole_book_semantic_review':False},
 'method':'Visually opened every physical PDF page 210–216 at 3×; zoomed uncertain romaji at 6×. Transcribed entries in physical column order. Cross-checked the complete English and Japanese romaji/ref pair multisets. No main-body text was used to fill an index key.',
 'pages':pages,
 'counts':{
   'raw_occurrences_total':len(english)+len(japanese),
   'english_raw_entries':len(english),'english_unique_key_texts':len({x['english_key'] for x in english}),'english_unique_roman_ref_pairs':len(en_pairs),
   'japanese_raw_entries':len(japanese),'japanese_unique_key_texts':len({x['roman'] for x in japanese}),'japanese_expanded_ref_occurrences':sum(len(x['refs']) for x in japanese),'japanese_unique_roman_ref_pairs':len(jp_pairs),
   'shared_roman_ref_pairs_between_indexes':len(en_pairs),
   'counts_by_pdf_page':{str(p['pdf_page']):p['raw_entry_count'] for p in pages}
 },
 'repeated_key_texts_within_index':{
   'english':[{'key':key,'count':n} for key,n in Counter(x['english_key'] for x in english).items() if n>1],
   'japanese':[{'key':key,'count':n} for key,n in Counter(x['roman'] for x in japanese).items() if n>1]
 },
 'duplicate_physical_pages':[],
 'duplicate_panels':[],
 'cross_index_note':'The two indexes intentionally share 185 roman/ref pairs but present different sort keys; this is not a duplicated page or panel.',
 'clipped_or_obscured_index_entries':[],
 'recoverable_from_duplicate':[],
 'unresolved_readings':[]
}
report_path=cache/'onomato-index-independent.json'
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
md='''# QA độc lập hai index オノマトペ\n\n- Nguồn: PDF210–216, SHA-256 `{sha}`; trang in 209–215. Cả bảy trang đã mở ảnh 3×; vài khóa có dấu trường âm được crop 6×. Đây chỉ là QA index, không phải review nghĩa toàn sách.\n- PDF210–213: index English, số dòng theo trang **48 / 47 / 52 / 38 = 185**. PDF214–216: index Japanese, **61 / 62 / 57 = 180** dòng. Năm dòng Nhật có hai số tham chiếu, nên mở rộng thành 185 cặp romaji/trang. Đối chiếu chéo hai index: **185/185 cặp khớp chính xác**.\n- Tổng **365 occurrence dòng in**; unique English key text **179**, unique Japanese roman key text **178**. Các alias/dạng có slash và khóa lặp cùng tên nhưng khác ref được giữ nguyên theo từng dòng.\n- Bảy trang in liên tiếp 209–215, nội dung/panel riêng biệt. **Không có trang hoặc panel trùng thật; không có khóa/refs bị cắt hoặc mờ không đọc được.** Những cặp romaji/ref trùng giữa hai index là chức năng tra cứu của hai bảng, không phải scan trùng.\n- Dữ liệu từng dòng, thứ tự cột, ảnh/hash ở `onomato-index-independent.json`.\n'''.format(sha=source_sha)
(cache/'onomato-index-independent.md').write_text(md,encoding='utf-8')
sidecar={'source_pdf_sha256':source_sha,'report_sha256':sha(report_path),'md_sha256':sha(cache/'onomato-index-independent.md'),'render_sha256':{p['render']:p['render_sha256'] for p in pages}}
(cache/'onomato-index-independent.sha256.json').write_text(json.dumps(sidecar,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(report['counts'])
print('report SHA256',sidecar['report_sha256'])
