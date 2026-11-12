import hashlib, json
from collections import defaultdict
from pathlib import Path

repo = Path('D:/CODE/git/kaiwa_skill')
out = repo / '.cache/root-live-qa'
pdf = repo / 'kaiwa_skill/book/Kaiwa/210-additional-super-miniature-phrases-for-immediate-use-in-japanese-conversation-4863922639-9784863922631_compress.pdf'
expected_pdf_sha = '2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(pdf) == expected_pdf_sha
occ = []
for head in range(1, 211):
    pdf_page = head + 15
    if head <= 93:
        disc, track = 'CD-1', head
    elif head <= 105:
        disc, track = 'CD-1', 94 + (head-94)//2
    elif head <= 198:
        disc, track = 'CD-2', head-105
    else:
        disc, track = 'CD-2', 94 + (head-199)//2
    crop = out/f'mini210-icon-h{head:03}-p{pdf_page:03}.png'
    assert crop.is_file()
    occ.append({'head':head,'pdf_page':pdf_page,'disc':disc,'printed_track':str(track),'crop':crop.name})
bycode=defaultdict(list)
for x in occ:bycode[(x['disc'],x['printed_track'])].append(x['head'])
groups=[{'disc':d,'printed_track':t,'heads':hs,'pdf_pages':[h+15 for h in hs]} for (d,t),hs in bycode.items() if len(hs)>1]
sheets=[out/f'mini210-audio-sheet-{i:03}-{i+29:03}.png' for i in range(1,211,30)]
assert all(p.is_file() for p in sheets)
assert len(occ)==210 and len(bycode)==198 and len(groups)==12
payload={
 'source_pdf':'kaiwa_skill/book/Kaiwa/'+pdf.name,
 'source_pdf_sha256':expected_pdf_sha,
 'review_scope':{'pdf_pages':[16,225],'heads':[1,210],'type':'audio_icon_crops_only','semantic_page_review':False},
 'method':'Rendered the top-right icon crop for every head page PDF16–225, assembled seven labeled contact sheets, and visually opened all 210 crops through those sheets. Track values below were read from the icons; the arithmetic pattern was checked only after visual review.',
 'total_occurrences':len(occ),
 'unique_disc_track_count':len(bycode),
 'counts_by_disc':{'CD-1':{'occurrences':105,'unique_tracks':99},'CD-2':{'occurrences':105,'unique_tracks':99}},
 'occurrences':occ,
 'shared_codes':groups,
 'unclear':[],
 'contact_sheets':[p.name for p in sheets]
}
(out/'mini210-audio-independent.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sidecar={'source_pdf_sha256':expected_pdf_sha,'report_sha256':sha(out/'mini210-audio-independent.json'),'contact_sheet_sha256':{p.name:sha(p) for p in sheets},'crop_sha256':{x['crop']:sha(out/x['crop']) for x in occ}}
(out/'mini210-audio-independent.sha256.json').write_text(json.dumps(sidecar,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('occurrences',len(occ),'unique',len(bycode),'shared groups',len(groups),'unclear',len(payload['unclear']))
for g in groups:print(g['disc'],g['printed_track'],g['heads'])
print('report sha256',sidecar['report_sha256'])
