import json, os, sys

for code in sys.argv[1:]:
    for base in ['work/trung', 'decisions']:
        suffix = '.spec.json' if base == 'work/trung' else '.json'
        path = f'kaiwa_skill/planning/v6_1/{base}/{code}{suffix}'
        x = json.load(open(path, encoding='utf-8'))
        x['selections'].sort(key=lambda s: 0 if s['kind'] == 'speak_japanese' else 1)
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(x, f, ensure_ascii=False, indent=2)
            f.write('\n')
        os.replace(tmp, path)
