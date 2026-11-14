import json, sys

root = 'kaiwa_skill/planning/v6_1/'
idx = json.load(open(root+'work/trung/unit_index.json', encoding='utf-8'))
if sys.argv[1] == 'unit':
    for uid in sys.argv[2:]:
        matches = [x for x in idx if x['unit_id'] == uid]
        for x in matches:
            print('\n###', x['book_id'], x['unit_id'], x['heading'], x['path'], x['start_line'], x['end_line'])
            print(x['text'])
elif sys.argv[1] == 'find':
    term = sys.argv[2]
    for x in idx:
        if term.lower() in (x['heading'] + ' ' + x['text']).lower() and (len(sys.argv)<4 or x['book_id']==sys.argv[3]):
            print(x['book_id'], x['unit_id'], x['heading'])
elif sys.argv[1] == 'stage':
    codes = set(sys.argv[2:])
    for line in open(root+'KAIWA_CHANG_V6_1.jsonl', encoding='utf-8'):
        x = json.loads(line)
        if x.get('display_code') in codes or x.get('code') in codes:
            print(json.dumps(x, ensure_ascii=False, indent=2))
elif sys.argv[1] == 'brief':
    codes = set(sys.argv[2:])
    for line in open(root+'KAIWA_CHANG_V6_1.jsonl', encoding='utf-8'):
        x = json.loads(line)
        if x.get('display_code') in codes:
            print('\n###', x['display_code'], x['title'], x['objective'])
            for s in x['situations']:
                print(s['id'], s['title'])
