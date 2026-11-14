import json
import os
import subprocess
from pathlib import Path

WORK = Path(__file__).parent
PLAN = WORK.parents[1]
ROOT = WORK.parents[4]
for code in ['S-029','S-030','S-051','S-076','S-078']:
    dest=PLAN/'decisions'/f'{code}.json'
    d=json.loads(dest.read_text(encoding='utf-8'))
    if code in ['S-029','S-030']:
        d['search_notes']=[x.replace('Seletions rỗng','Selections rỗng') for x in d['search_notes']]
    if code=='S-051':
        d['search_notes'].append('Đọc lại trọn B19 CD55–57 (các cặp đau bụng/khó chịu, chóng mặt/đau đầu); không cặp nào có nha sĩ, răng hoặc điều trị răng, nên không gắn vào chặng nha khoa.')
        d['considerations'].append({'book_id':'B19','locator':'B19 04-part3.md, CD55–57, dòng 746–825','reason':'Đã đọc đủ ba cặp biểu cảm triệu chứng: シクシク/ゴロゴロ, ムカムカ/チカチカ, ガンガン/クラクラ; toàn bài mô tả đau bụng, khó chịu, mắt/đầu/chóng mặt, không có răng hoặc chữa nha khoa.','status':'unsuitable'})
    if code=='S-076':
        for c in d['considerations']:
            if c['book_id']=='B01':
                c['locator']='B01 07-phuong-tien-van-chuyen.md, 1. Xe buýt, dòng 5–129'
                c['reason']='Đã đọc trọn 33 câu/đối thoại của nhóm xe buýt, chỉ câu 4 hỏi bus sân bay, không dạy thủ tục bay; _meta/audio không có track theo nhóm.'
    if code=='S-078':
        d['search_notes']=[x.replace('B01 mục sinh hoạt có tắm ở nhà, không phải cơ sở công cộng và không có mapping track CD.', 'B01 chương vận động chỉ có câu 今朝はシャワーの時間もなかった khi quét từ khóa シャワー; không có mục về cơ sở tắm công cộng hoặc mapping track CD.') for x in d['search_notes']]
        for c in d['considerations']:
            if c['book_id']=='B01':
                c['locator']='B01 04-van-dong.md, từ khóa シャワー dòng 219'
                c['reason']='Chỉ thấy câu 今朝はシャワーの時間もなかった trong mục lịch sinh hoạt; không phải pack về sento/sauna, và _meta/audio không ghi track theo bài.'
    temp=WORK/f'{code}.semantic.tmp.json'
    temp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    env=os.environ.copy();env['KAIWA_ROADMAP_DIR']=str(PLAN)
    p=subprocess.run(['py','-X','utf8','tools/roadmap_v6.py','check-one',str(temp)],cwd=ROOT,env=env,text=True,capture_output=True)
    print(code,p.stdout,p.stderr)
    if p.returncode: raise SystemExit(p.returncode)
    temp.replace(dest)
