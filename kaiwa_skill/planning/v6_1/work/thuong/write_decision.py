import json, pathlib, re, sys
from explore import ROOT, BOOKS, STAGES, extract

spec=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf8'))
stage=STAGES[spec['display_code']]
selections=[]
for item in spec['units']:
    bid,uid=item['book_id'],item['unit_id']
    u,p,lo,hi,lines=extract(bid,uid)
    lo=item.get('start_line',lo)
    hi=item.get('end_line',hi)
    heading=re.sub(r'^#{1,6} ', '', lines[0]).split('　〔')[0].strip()
    if bid not in {'B11','B12','B13','B14'}:heading=heading.split(' — ')[0]
    heading=item.get('title_ja',heading)
    prefix=re.match(r'^(?:\d+\. |\d+ |\d+　|\(\d+\) |\d+　\(\d+\) )',heading)
    prefix=item.get('source_number_prefix',prefix.group(0) if prefix else '')
    audio=[]
    if 'audio' in item:
        audio=item['audio']
    else:
        match=re.search(r'CD-(\d+)\s*(?:/|\s)\s*(\d+)',lines[0]+'\n'+''.join(lines[1:3]))
        if match:audio=[{'disc':'CD-'+match[1], 'track':match[2], 'locator':f'{heading}; nhãn trong clean'}]
        else:
            match=re.search(r'音声\s*(\d+)',lines[0])
            if match:audio=[{'disc':None,'track':match[1],'locator':f'{heading}; nhãn 音声 trong clean'}]
    selections.append({
        'kind':item.get('kind','speak_japanese'), 'book_id':bid,'book_title':BOOKS[bid]['title'],
        'unit_id':uid,'title_ja':heading,'path':p.relative_to(ROOT).as_posix(),
        'sha256':__import__('hashlib').sha256(p.read_bytes()).hexdigest(),
        'start_line':lo,'end_line':hi,'pack_id':item.get('pack_id',bid+'/'+uid),
        'boundary':item['boundary'],'audio':audio,'audio_note':item.get('audio_note','Đã đối chiếu nhãn in và toàn chữ Nhật trong chapter clean; chưa nghe file âm thanh.'),
        'situation_ids':item['situation_ids'],'fit_vi':item['fit_vi'],
        'difficulty_vi':item['difficulty_vi'],'read_status':'whole_unit_read',
        'source_number_prefix':prefix
    })
out={k:spec[k] for k in ('display_code','vocabulary_topics','search_notes','considerations')}
out['stage_uid']=stage['uid'];out['selections']=selections
out={k:out[k] for k in ('stage_uid','display_code','vocabulary_topics','search_notes','selections','considerations')}
path=ROOT/'kaiwa_skill/planning/v6_1/decisions'/f"{stage['display_code']}.json"
tmp=path.with_suffix('.tmp')
tmp.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
tmp.replace(path)
print(path)
