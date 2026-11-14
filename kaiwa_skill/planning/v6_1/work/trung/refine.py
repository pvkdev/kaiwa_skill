import importlib.util, json, os
from pathlib import Path

root=Path('kaiwa_skill/planning/v6_1')
module_path=root/'work/trung/make_decision.py'
spec=importlib.util.spec_from_file_location('maker',module_path)
maker=importlib.util.module_from_spec(spec)
spec.loader.exec_module(maker)

def save(path,x):
    temp=path.with_suffix(path.suffix+'.tmp')
    with temp.open('w',encoding='utf-8') as f:
        json.dump(x,f,ensure_ascii=False,indent=2)
        f.write('\n')
    os.replace(temp,path)

def update(code,fn):
    sp=root/'work/trung'/f'{code}.spec.json'
    dp=root/'decisions'/f'{code}.json'
    s=json.loads(sp.read_text(encoding='utf-8'))
    d=json.loads(dp.read_text(encoding='utf-8'))
    fn(s,d)
    save(sp,s)
    save(dp,d)

def remove_uid(s,d,uid):
    s['selections']=[x for x in s['selections'] if x['uid']!=uid]
    d['selections']=[x for x in d['selections'] if x['unit_id']!=uid]

def set_situations(s,d,uid,ids):
    next(x for x in s['selections'] if x['uid']==uid)['situations']=ids
    next(x for x in d['selections'] if x['unit_id']==uid)['situation_ids']=ids

def t121(s,d):
    set_situations(s,d,'u-ch4-unit05',['S011','S012','S017','S018'])
    s['notes'][1]+=' Bài Unit5 là gửi hàng, không chứng minh thủ tục nhận kiện; phần nhận kiện cần học tại quầy.'
    d['search_notes']=s['notes']
update('T-121',t121)

def t123(s,d):
    set_situations(s,d,'u-ch5-unit06',['S015','S016'])
    s['notes'][1]+=' Bài Unit6 không có đồ bỏ quên; dùng quy trình đồ thất lạc riêng.'
    d['search_notes']=s['notes']
update('T-123',t123)

def t129(s,d):
    remove_uid(s,d,'u-part4-unit27')
    s['notes'][0]='Đọc 25 tình huống T-129; quét レンタカー/thuê xe trong catalog, không thấy whole pack chuyên thuê ô tô. Đọc trọn B18 chức năng1 xác nhận, B08 Part4 Unit27 về vé concert, Unit31 hỏi dịch vụ du lịch và B05 Ch6 Unit4 thuê DVD. Chỉ chọn khung xác nhận và hỏi điều kiện dịch vụ có thể chuyển ngữ cảnh.'
    d['search_notes']=s['notes']
    c={'book_id':'B08','locator':'Part4 Unit27, CD-2/30','reason':'Vé concert không đủ sát thủ tục nhận/trả ô tô; không gán pack chỉ vì có 予約.','status':'unsuitable'}
    s['considerations'].append(c); d['considerations'].append(c)
update('T-129',t129)

def t135(s,d):
    remove_uid(s,d,'u-part4-unit29')
    c={'book_id':'B08','locator':'Part4 Unit29, CD-2/32','reason':'Một câu tai nạn trong pack chủ yếu mất đồ không đủ để dạy tường thuật va chạm; bỏ chọn.','status':'unsuitable'}
    s['considerations'].append(c); d['considerations'].append(c)
update('T-135',t135)

def t145(s,d):
    remove_uid(s,d,'u-part4-unit27')
    s['notes'][0]='Đọc 16 tình huống T-145; kết nối nguồn đã đọc trọn B18 chức năng1 xác nhận, B08 Part4 Unit24–25 điện thoại công việc và B07 bài192 cảm ơn. B08 Part4 Unit27 về vé concert đã xem nhưng không đủ sát hẹn dịch vụ cá nhân.'
    d['search_notes']=s['notes']
    c={'book_id':'B08','locator':'Part4 Unit27, CD-2/30','reason':'Hủy vé concert khác đổi lịch hẹn dịch vụ cá nhân; không dùng pack này cho đoạn đời sống.','status':'deferred'}
    s['considerations'].append(c); d['considerations'].append(c)
update('T-145',t145)

def t144(s,d):
    item={'uid':'u-180-f-023','kind':'speak_japanese','situations':['S011','S012','S014','S015'],
          'fit':'Trọn CD12 gồm 手とり足とり và 一から十まで: kể được hướng dẫn kỹ từng bước và điều còn cần được giải thích.',
          'difficulty':'Bài24 có ví dụ chê người khác phiền; chỉ dùng nghĩa mô tả mức hướng dẫn, tránh gán nhãn người học.'}
    s['selections'].insert(3,item)
    d['selections'].insert(3,maker.select(None,item))
    s['notes'][0]+=' Đọc thêm trọn B20 Section F bài23–24 cùng CD12 về được hướng dẫn kỹ từng bước.'
    d['search_notes']=s['notes']
update('T-144',t144)
