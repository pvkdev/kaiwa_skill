import json
import os
import subprocess
from pathlib import Path

WORK = Path(__file__).parent
PLAN = WORK.parents[1]
ROOT = WORK.parents[4]
items = {
    'S-011': ('Đọc trọn B01 mục 1 Xe buýt, chương phương tiện dòng 5–129: 33 câu và đối thoại, nhưng lặp yêu cầu báo trạm/xuống xe, có địa danh ngoài Nhật và chưa có bản đồ track theo mục; hai pack B08 điện tàu/bus gọn và đủ tác vụ.',
              {'book_id':'B01','locator':'B01 07-phuong-tien-van-chuyen.md, 1. Xe buýt, dòng 5–129','reason':'Đã đọc trọn 33 câu/đối thoại: có câu lặp 10/28, 25/31 và địa danh Trung Quốc; không bổ sung tiến trình hỏi tuyến so với B08 Part 4 Unit 01/02, audio CD-MP3 không có số track tương ứng.','status':'deferred'}),
    'S-031': ('Đọc trọn B01 mục 5 Chọn Món Ăn, chương ẩm thực dòng 265–328: có câu nguồn bất thường 友達を持っているから và thiếu đơn vị đếm りんごを一ください; giữ B08 và cặp vị B19 đã chọn.',
              {'book_id':'B01','locator':'B01 05-am-thuc.md, 5. Chọn Món Ăn, dòng 265–328','reason':'Đã đọc trọn 16 câu/đối thoại; hai câu Nhật được chính bản clean chú thích dùng bất thường hoặc thiếu đơn vị đếm, không đưa nguyên pack lỗi vào shadowing.','status':'unsuitable'}),
    'S-042': ('Đọc trọn B01 mục 1 Gọi điện thoại, chương điện thoại dòng 5–63: có câu mở cuộc gọi nhưng lẫn câu đường dài, hỏng máy, máy bận và lặp lời gọi; B08 Part 4 Unit 23 mạch gọi bạn/thầy rõ hơn.',
              {'book_id':'B01','locator':'B01 06-dien-thoai.md, 1. Gọi điện thoại, dòng 5–63','reason':'Đã đọc trọn 14 câu/đối thoại; mở cuộc gọi lặp nhiều tên riêng, còn trộn báo máy hỏng/đường dài vào cùng mục. B08 Part 4 Unit 23 phù hợp mạch gọi và có track CD in rõ; B01 không có track theo mục.','status':'deferred'})
}
for code, (note, consideration) in items.items():
    dest = PLAN/'decisions'/f'{code}.json'
    d = json.loads(dest.read_text(encoding='utf-8'))
    d['search_notes'].append(note)
    d['considerations'].append(consideration)
    temp = WORK/f'{code}.b01.tmp.json'
    temp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    env = os.environ.copy()
    env['KAIWA_ROADMAP_DIR'] = str(PLAN)
    p = subprocess.run(['py','-X','utf8','tools/roadmap_v6.py','check-one',str(temp)],cwd=ROOT,env=env,text=True,capture_output=True)
    print(code, p.stdout, p.stderr)
    if p.returncode: raise SystemExit(p.returncode)
    temp.replace(dest)
