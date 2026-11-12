import json, pathlib, pymupdf, re, unicodedata, difflib
root=pathlib.Path(__file__).resolve().parents[2]
pdf=pymupdf.open(root/'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf')
rows=json.loads((root/'.cache/root-live-qa/mini210-index-target-preliminary.json').read_text(encoding='utf8'))
def n(s):
 s=unicodedata.normalize('NFKC',s).lower()
 s=s.replace('г','i').replace('т','m').replace('ү','y')
 return ''.join(c for c in s if c.isascii() and c.isalnum())
for r in rows:
 target=pdf[r['printed_ref']-1].get_text()[:350]
 key=n(r['key'])
 english=n(target)
 # This checks page identity, not exact alias equivalence.
 r['key_in_main_intro']=key in english
 r['main_intro']=target.splitlines()[:8]
missing=[r for r in rows if not r['key_in_main_intro']]
print('not verbatim in main intro',len(missing))
for r in missing:
 print(r['pdf_page'],r['key'],r['printed_ref'],'|',' / '.join(r['main_intro'])[:140])
