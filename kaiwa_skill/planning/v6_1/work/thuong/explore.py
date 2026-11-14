import json, pathlib, sys, re, hashlib

ROOT=pathlib.Path(__file__).resolve().parents[5]
MAN=json.loads((ROOT/'kaiwa_skill/planning/catalog27/manifest.json').read_text(encoding='utf8'))
BOOKS={b['book_id']:b for b in MAN['books']}
BOOKS['INTERVIEW']={'book_id':'INTERVIEW','title':'シャドーイング 日本語を話そう 就職・アルバイト・進学面接編 インドネシア語・タイ語・ベトナム語訳版','directory':'kaiwa_skill/knowledge/シャドーイング 日本語を話そう 就職・アルバイト・進学面接編 インドネシア語・タイ語・ベトナム語訳版'}
STAGES={x['display_code']:x for x in (json.loads(s) for s in (ROOT/'kaiwa_skill/planning/v5/KAIWA_CHANG_V5.jsonl').read_text(encoding='utf8').splitlines())}

def units(bid):
    p=ROOT/BOOKS[bid]['directory']/'_meta/units.jsonl'
    return [json.loads(s) for s in p.read_text(encoding='utf8').splitlines()] if p.exists() else []

def extract(bid, uid):
    u=next(x for x in units(bid) if x['unit_id']==uid)
    p=ROOT/BOOKS[bid]['directory']/u['chapter']; lines=p.read_text(encoding='utf-8-sig').splitlines()
    ai=next(i for i,s in enumerate(lines) if 'id="'+uid+'"' in s)
    start=next(i for i in range(ai,len(lines)) if re.match(r'^#{1,6} ',lines[i]))
    next_anchor=next((i for i in range(ai+1,len(lines)) if re.match(r'^<a id="',lines[i]) and i>start),len(lines))
    level=len(lines[start].split(' ')[0])
    next_heading=next((i for i in range(start+1,next_anchor) if re.match(r'^#{1,'+str(level)+r'} ',lines[i])),next_anchor)
    end=min(next_anchor,next_heading)
    while end>start and not lines[end-1].strip():end-=1
    return u,p,start+1,end,lines[start:end]

cmd=sys.argv[1]
if cmd=='stages':
    for code in sys.argv[2:]:
        s=STAGES[code];print('\n',code,s['title'],'\n',s['objective'],'\n',' | '.join(s['knowledge_focus']))
        print(' ; '.join(x['id']+' '+x['title'] for x in s['situations']))
elif cmd=='list':
    for bid in sys.argv[2:]:
        print('\n'+bid)
        for u in units(bid):print(u['unit_id'],'|',u['heading'])
elif cmd=='read':
    bid,uid=sys.argv[2:4];u,p,lo,hi,lines=extract(bid,uid)
    print(bid,uid,'|',u['heading'],'|',p.relative_to(ROOT),'|',hashlib.sha256(p.read_bytes()).hexdigest(),'|',lo,hi)
    for n,s in enumerate(lines,lo):print(f'{n:04d} {s}')
