import json
import subprocess
from pathlib import Path

WORK = Path(__file__).parent
path = WORK / 'S-001.spec.json'
spec = json.loads(path.read_text(encoding='utf-8'))
spec['notes'][2] += ' Đọc thêm trọn B14 Unit 1 Section 2, cả mười cặp lời chào/ra về/xin lỗi/cảm ơn/hỏi thăm trên CD 03; chọn trọn section để luyện nhịp đối đáp.'
spec['selections'].append({
    'kind': 'shadowing_pack', 'book_id': 'B14', 'unit_id': 'u-sd-u1-s02',
    'title_ja': 'Section 2',
    'boundary': 'Trọn Unit 1 Section 2, CD 03, mười cặp thoại đánh số 1–10, dòng 88–164; dừng trước anchor Section 3 ở dòng 165.',
    'audio': [{'disc': 'CD', 'track': '03', 'locator': 'Unit 1 Section 2; nhãn CD 03 in tại dòng 91 của chương clean'}],
    'audio_note': 'Đã đọc đủ mười cặp và kiểm nhãn CD 03 trong clean; chưa nghe file audio.',
    'situations': ['S001', 'S005', 'S007', 'S011', 'S012', 'S013', 'S014', 'S015'],
    'fit': 'Mười cặp A/B đưa lời chào theo quan hệ, tạm biệt khi rời công sở/nhà, xin lỗi, cảm ơn, bình luận thời tiết và hỏi khỏe vào nhịp đối đáp tự nhiên.',
    'difficulty': 'Nhiều câu rất ngắn; giữ cả cặp thời tiết và hỏi khỏe vì là phần mở chuyện cùng Section, chú giải sắc thái thân mật/lịch sự.'
})
path.write_text(json.dumps(spec, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
subprocess.run(['py','-X','utf8',str(WORK/'save_one.py'),str(path)], check=True)
