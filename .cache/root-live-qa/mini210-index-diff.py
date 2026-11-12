import json, pathlib, re, difflib, unicodedata

root=pathlib.Path(__file__).resolve().parents[2]
ocr=json.loads((root/'.cache/root-live-qa/mini210-index-source-ocr.json').read_text(encoding='utf8'))
raw=(root/'kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210/chapters/14-index.md').read_text(encoding='utf8')
sections=re.split(r'(?m)(?=^<a id="u-210-index-\d+"></a>)',raw)
rows={}
for s in sections:
    m=re.match(r'<a id="u-210-index-(\d+)"></a>',s)
    if m:
        p=m.group(1)
        rows[p]=[]
        for line in s.splitlines():
            if line.startswith('- **'):
                mm=re.fullmatch(r'- \*\*(.*?)\*\* — (.*?): (.*?) \(PDF(\d+)(?:;.*?)?\)\.',line)
                assert mm,line
                rows[p].append(mm.groups())

def n(s):
    return ''.join(c.lower() for c in unicodedata.normalize('NFKC',s) if c.isalnum())

for p in ['226','227','228','229','230','231']:
    srcgroups=sorted([g for g in ocr[p] if 'text' in g],key=lambda x:(x.get('column')=='right',x.get('first_y',999)))
    print('PAGE',p,'source',len(srcgroups),'out',len(rows[p]))
    if p in ['228','229']:
        for i,(key,vi,jp,ref) in enumerate(rows[p],1):
            print('OUTPUT',i,key,jp,ref)
        continue
    for i,(g,(key,vi,jp,ref)) in enumerate(zip(srcgroups,rows[p]),1):
        src=g.get('text','')
        # The source text layer sometimes substitutes Cyrillic for Latin glyphs.
        src=src.replace('Г','I').replace('т','m').replace('Т','T')
        score=difflib.SequenceMatcher(None,n(key),n(src[:len(key)+10])).ratio()
        nums=re.findall(r'\d+',src)
        sref=nums[-1] if nums else None
        if score<.67 or str(ref)!=sref or n(jp) not in n(src):
            print(i,'key',key,'JP',jp,'ref',ref,'score',round(score,2),'sref',sref,'SRC',src)
