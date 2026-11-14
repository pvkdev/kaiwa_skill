import json,subprocess
from pathlib import Path
W=Path(__file__).parent

def pack(first, end, cd, category, number, first_name, second_name, ids, fit, difficulty):
    title=f'{category}｜{number} {first_name}'
    return dict(kind='speak_japanese',book_id='B19',unit_id=first,
                start_line=None,end_line=end,title_ja=title,
                source_number_prefix=f'{category}｜{number} ',
                pack_id=f'B19/CD-{cd}-{number}-{number+1}',
                boundary=f'Trọn cặp biểu đạt {number} {first_name} và {number+1} {second_name}, mọi ví dụ Nhật, giải thích, hình chuyển chữ và Small Steps nếu có; kết thúc trước anchor mục {number+2}. Một nhãn CD {cd} in ở mục đầu của cặp.',
                audio=[{'disc':None,'track':str(cd),'locator':f'B19 Part 3, mục {number}–{number+1}; icon CD {cd} ở mục {number} và _meta/audio.json'}],
                audio_note='Đã đọc trọn hai mục liên tiếp và đối chiếu icon CD tại mục đầu với _meta/audio.json; chưa nghe file audio.',
                situations=ids,fit=fit,difficulty=difficulty)

changes={
 'S-031':[pack('u-p3-head-044',597,49,'料理・味',44,'さっぱり · Sappari','ピリッと · Piritto',['S006','S007','S008','S014'],'Hai biểu đạt vị thanh mát và cay the giúp hỏi/đáp về món trước khi gọi, gồm lời rủ món trưa và nhận xét súp.','Onomatopoeia theo vị hơi mới nhưng cặp thoại ngắn; giữ cả ví dụ nghĩa bóng như phần nguồn để phân biệt.')],
 'S-033':[pack('u-p3-head-042',571,48,'料理・味',42,'こってり · Kotteri','あっさり · Assari',['S005','S006','S007','S008'],'Hai biểu đạt món đậm béo và thanh nhẹ, có cặp người rủ nhau đến quán ramen, sát trò chuyện chọn món với đồng nghiệp.','Giảng cặp đối lập theo vị; giữ cả Small Steps nghĩa bóng trong bài mà không gán thành lời gọi món.')],
 'S-040':[pack('u-p3-head-061',825,57,'体調',61,'ガンガン · Gangan','クラクラ · Kurakura',['S001','S002','S003','S009','S010'],'Cặp mô tả đau đầu dữ và choáng váng kèm người hỏi thăm, hữu ích nói tình trạng khi xin nghỉ và cập nhật.','Từ tượng thanh cụ thể, không chẩn đoán nguyên nhân từ cơn đau; toàn pack có cả nghĩa bóng được chú giải.')],
 'S-049':[
   pack('u-p3-head-057',769,55,'体調',57,'シクシク · Shikushiku','ゴロゴロ · Gorogoro',['S005','S006','S008','S015'],'Cặp mô tả đau âm ỉ bụng/răng và bụng sôi, giúp chỉ triệu chứng bằng lời chính xác hơn.','Từ tượng thanh mới nhưng người bệnh có thể nói ngắn; không biến ví dụ răng thành chẩn đoán.'),
   pack('u-p3-head-059',797,56,'体調',59,'ムカムカ · Mukamuka','チカチカ · Chikachika',['S005','S006','S008','S015'],'Cặp nôn nao và mắt nhức vì chói, bổ sung triệu chứng khác với B08 bệnh viện.','Một ví dụ người nghe đoán mang thai chỉ là thoại nguồn, không suy kết luận y tế.'),
   pack('u-p3-head-061',825,57,'体調',61,'ガンガン · Gangan','クラクラ · Kurakura',['S005','S006','S008','S015'],'Cặp đau đầu dữ và choáng váng giúp trả lời câu hỏi mức độ và mô tả lúc tái khám.','Giữ nguyên nghĩa bóng trong Small Steps, nhưng tập trung tách khỏi triệu chứng thể chất.')]
}
for code, additions in changes.items():
    p=W/(code+'.spec.json')
    spec=json.loads(p.read_text(encoding='utf-8'))
    for a in additions:
        del a['start_line']
    spec['selections']=additions+spec['selections']
    spec['notes'].append('Rà bổ sung B19 theo cặp CD in trong sách; đã đọc trọn các cặp biểu đạt mới chọn và giữ cả hai mục mỗi track, không lấy lẻ một từ. Hash và dải dòng kiểm qua check-one.')
    p.write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('rechecking',code,flush=True)
    subprocess.run(['py','-X','utf8',str(W/'save_one.py'),str(p)],check=True)
