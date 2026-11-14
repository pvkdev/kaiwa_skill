import collections, glob, json, re

base='kaiwa_skill/planning/v6_1/decisions/'
files=[f'{base}T-{i:03}.json' for i in range(1,146)]
ds=[json.load(open(f,encoding='utf-8')) for f in files]
books=collections.Counter()
kinds=collections.Counter()
unique=collections.defaultdict(set)
special=[]
empty=[]
for d in ds:
    code=d['display_code']
    if not d['selections']: empty.append(code)
    for s in d['selections']:
        books[s['book_id']]+=1
        kinds[s['kind']]+=1
        unique[s['book_id']].add(s['pack_id'])
        if s['book_id'] in ['B19','B20','B24']:
            special.append((code,s['book_id'],s['unit_id'],s['pack_id'],s['start_line'],s['end_line'],s.get('audio')))
print('files',len(ds),'selections',sum(books.values()),'empty',empty)
print('books',dict(books),'unique', {k:len(v) for k,v in unique.items()},'kinds',dict(kinds))
for z in special: print('SPECIAL',z)
issues=[]
for d in ds:
    for s in d['selections']:
        title=s['title_ja']
        m=re.match(r'^(?:Unit [0-9]+ |\([0-9]+\) |[0-9]+\. |[0-9]+　\([0-9]+\) |[0-9]+　|[0-9]+ )',title)
        if m and s.get('source_number_prefix')!=m.group():
            issues.append((d['display_code'],s['book_id'],s['unit_id'],'prefix',m.group(),s.get('source_number_prefix')))
        path='.'.join([])
        try:
            lines=open(s['path'],encoding='utf-8-sig').read().splitlines()
            first=lines[s['start_line']-1]
            if not first.startswith('<a id=') and s['book_id'] not in ['INTERVIEW']:
                issues.append((d['display_code'],s['book_id'],s['unit_id'],'first',first[:80]))
        except Exception as exc:
            issues.append((d['display_code'],s['book_id'],s['unit_id'],'path',str(exc)))
print('issues',issues[:30],len(issues))
