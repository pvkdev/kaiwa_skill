"""Atomic authoring helper; never generates scenario content."""
from pathlib import Path
import json,os
HERE=Path(__file__).resolve().parent
BRANCHES={'routine','accepted','declined','conditional','pending','alternative','misunderstanding','problem','resolved','unresolved','follow_up'}
def write_stage(owner,key,objective,knowledge_focus,events,coverage_note,cross_stage_refs=None,source_refs=None,source_findings=None):
    assigned={x['key']:x for x in json.loads((HERE/f'{owner}_assignment.json').read_text(encoding='utf8'))}
    assert key in assigned,(owner,key)
    path=HERE/'stages'/f'{key}.json'
    if path.exists():raise FileExistsError(f'Preserve IDs; read/edit existing {path}')
    all_events=[];situations=[]
    for ei,event in enumerate(events,1):
        eid=f'E{ei:02}';all_events.append({'id':eid,'name':event['name'],'roles':event['roles']})
        local=[]
        for case in event['cases']:
            if isinstance(case,str):case={'title':case,'branch':'routine'}
            sid=f'S{len(situations)+1:03}'
            refs=case.get('from',[])
            if isinstance(refs,int):refs=[refs]
            assert all(1<=x<=len(local) for x in refs),(key,eid,case)
            branch=case.get('branch','routine');assert branch in BRANCHES,branch
            row={'id':sid,'event_id':eid,'title':case['title'],'branch':branch,'origin':'ai_authored'}
            if refs:row['continues_from']=[local[x-1] for x in refs]
            situations.append(row);local.append(sid)
    assert objective and len(knowledge_focus)>=2 and len(situations)>=8,(key,len(situations))
    assert len({s['title'].casefold() for s in situations})==len(situations),key
    result={'stage_key':key,'uid':assigned[key]['uid'],'objective':objective,'knowledge_focus':knowledge_focus,'events':all_events,'situations':situations,'coverage_note':coverage_note,'cross_stage_refs':cross_stage_refs or [],'source_refs':source_refs or [],'source_findings':source_findings or [],'status':'authored_needs_root_review','worker':owner}
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n');os.replace(temp,path)
    print(f'{key}: {len(all_events)} events, {len(situations)} situations')
