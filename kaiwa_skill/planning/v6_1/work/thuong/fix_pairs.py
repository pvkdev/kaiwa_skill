import json
from pathlib import Path

ROOT = Path(__file__).parent
DROP = {
    ('H-051','B20','u-180-o-082'): 'CD41 còn 心を鬼にして về nghiêm khắc với trẻ/người vay, lệch H-051.',
    ('H-054','B20','u-180-p-090'): 'CD45 còn 村八分 về tẩy chay nhóm, không hợp cảnh kiểm tin hàng xóm.',
    ('H-060','B20','u-180-p-090'): 'CD45 còn 村八分 về tẩy chay nhóm, quá xa hỏi nguồn chính sách.',
    ('H-056','B20','u-180-d-017'): 'CD9 còn 空気を読む về đọc không khí, không phải kể hồi ức.',
    ('H-051','B24','u-r-164'): 'CD82 còn 謎 về suy đoán hôn nhân người khác, không phù hợp nghe bất mãn mà không gán động cơ.',
}
PAIRS = {
    ('B24','u-r-166'): (43,82,'Unit 83 — 五分五分／どっちもあり〔CD 83〕','Unit 83 — ','B24/CD-83-165-166','CD','83','五分五分 về hai khả năng ngang nhau cùng track cũng hỗ trợ giữ kết luận mở.'),
    ('B24','u-i-76'): (41,80,'Unit 38 — ドキドキ（する）／気になる〔CD 38〕','Unit 38 — ','B24/CD-38-75-76','CD','38','ドキドキ về hồi hộp cùng track; phân biệt lo trong người và điều cụ thể đang bận tâm.'),
    ('B24','u-m-116'): (3,42,'Unit 58 — がっくり／落ち込む〔CD 58〕','Unit 58 — ','B24/CD-58-115-116','CD','58','がっくり về thất vọng đột ngột cùng track; không coi hai sắc thái là chẩn đoán.'),
    ('B24','u-e-41'): (41,80,'Unit 21 — ありがたい（んだ）けど／～たら・れば・と＋うれしい〔CD 21〕','Unit 21 — ','B24/CD-21-41-42','CD','21','～たら／れば／と＋うれしい cũng là lời nhờ mềm trong cùng track; cả hai vẫn cần nêu phạm vi rõ.'),
    ('B24','u-o-143'): (159,195,'Unit 72 — なんか違う／そうじゃなくて〔CD 72〕','Unit 72 — ','B24/CD-72-143-144','CD','72','そうじゃなくて trong cùng track giúp sửa khi người kia hiểu sai cảm giác なんか違う.'),
    ('B24','u-f-48'): (3,38,'Unit 24 — どっぷり／～にハマる〔CD 24〕','Unit 24 — ','B24/CD-24-47-48','CD','24','どっぷり trong cùng track nói mức độ đắm chìm, có thể hỏi liệu sở thích ảnh hưởng lịch khác không.'),
    ('B20','u-180-y-155'): (3,42,None,None,'B20/CD-78-155-156','CD','78','うなぎ上り trong cùng track là tăng vọt; đối chiếu với 右肩上がり tăng đều, không nhập hai mức.'),
    ('B20','u-180-y-157'): (43,84,None,None,'B20/CD-79-157-158','CD','79','足踏み trong cùng track là giậm chân; phân biệt mức trần và không tiến triển.'),
    ('B20','u-180-y-162'): (123,159,'161. 空回り','161. ','B20/CD-81-161-162','CD','81','空回り trong cùng track là cố gắng không hiệu quả; đánh giá chi phí trước khi chọn cách đánh đổi.'),
}

for code in [f'H-{n:03d}' for n in range(1,65) if n != 50]:
    p=ROOT/f'{code}.spec.json'
    d=json.loads(p.read_text(encoding='utf8'))
    changed=False
    out=[]
    for u in d['units']:
        key=(code,u['book_id'],u['unit_id'])
        if key in DROP:
            d['considerations'].append({'book_id':u['book_id'],'locator':u['unit_id'],
                'reason':'Đã đọc trọn biểu đạt được xét; bỏ sau khi đọc cả cặp audio: '+DROP[key],
                'status':'unsuitable'})
            changed=True
            continue
        pair=PAIRS.get((u['book_id'],u['unit_id']))
        if pair:
            lo,hi,title,prefix,pid,disc,track,note=pair
            u.update(start_line=lo,end_line=hi,pack_id=pid,
                     boundary=f'Toàn cặp audio {disc} {track} từ dòng {lo} đến {hi}, gồm cả hai biểu đạt liền nhau; dừng trước cặp kế.',
                     audio=[{'disc':disc,'track':track,'locator':f'{pid}, nhãn CD ở đầu cặp'}],
                     difficulty_vi=u['difficulty_vi']+' '+note)
            if title:u['title_ja']=title
            if prefix:u['source_number_prefix']=prefix
            if u['book_id']=='B20' and u['unit_id']=='u-180-y-162':u['unit_id']='u-180-y-161'
            changed=True
        out.append(u)
    if changed:
        d['units']=out
        d['search_notes'].append('Rà sau phân bổ: B20/B24 mỗi CD ghép hai biểu đạt; đọc cả biểu đạt kề và chỉ giữ cặp nguyên vẹn có ích cho chặng.')
        p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        print(code)
