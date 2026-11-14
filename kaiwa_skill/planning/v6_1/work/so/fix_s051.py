import json, os, subprocess
from pathlib import Path
W=Path(__file__).parent; P=W.parents[1]; R=W.parents[4]
dest=P/'decisions/S-051.json';d=json.loads(dest.read_text(encoding='utf-8'))
d['search_notes']=[x.replace('không cặp nào có nha sĩ, răng hoặc điều trị răng, nên không gắn vào chặng nha khoa.', 'CD55 có đúng một câu 歯がシクシク痛くて, còn lại chủ yếu bụng/đầu/mắt; không cặp nào dạy đặt lịch hay chữa răng, nên không gắn nguyên pack vào chặng nha khoa.') for x in d['search_notes']]
for c in d['considerations']:
    if c['book_id']=='B19':
        c['reason']='Đã đọc đủ ba cặp biểu cảm triệu chứng. CD55 có một câu 歯がシクシク痛くて nhưng ba câu còn lại thiên về bụng; CD56–57 mô tả mắt/đầu/chóng mặt. Không có mạch đặt lịch hoặc điều trị răng, nên không chọn nguyên pack cho chặng nha khoa.'
tmp=W/'S-051.fix.tmp.json';tmp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
env=os.environ.copy();env['KAIWA_ROADMAP_DIR']=str(P)
p=subprocess.run(['py','-X','utf8','tools/roadmap_v6.py','check-one',str(tmp)],cwd=R,env=env,text=True,capture_output=True)
print(p.stdout,p.stderr)
if p.returncode:raise SystemExit(p.returncode)
tmp.replace(dest)
