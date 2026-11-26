"""Curated grammar decisions from the first text drill in B2+ for every lesson.

The saved exercise is a prompt and option bank, not a revealed answer key.
Every correct choice and explanation below is editorial AI work.
"""

import json
from pathlib import Path

from renshuu_dom import parse, reviewed_snapshots
from renshuu_examples import additional_items


ROOT = Path(__file__).resolve().parents[1]

# lesson, B group, grammar point, Vietnamese task, correct, two distractors, explanation
SPECS = [
 (1,3,'mg-phu-dinh','Chọn đuôi phủ định lịch sự cho 「山田さんは 学生…」.','じゃ ありません。','じゃ ありませんです。','です。','学生 là danh từ. Phủ định lịch sự là 学生じゃ ありません; じゃ ありません đã đủ lịch sự nên không thêm です.'),
 (2,4,'mg-lua-chon','Chọn phần đầu của câu hỏi lựa chọn “sách hay tạp chí?”.','本ですか、','本です、','本じゃ ありませんか、','Liệt kê hai khả năng bằng 「本ですか、雑誌ですか」; か phải xuất hiện sau lựa chọn thứ nhất.'),
 (3,4,'mg-doko-dochira','Chọn từ hỏi vị trí lịch sự của thang cuốn.','どちらですか。','どなたですか。','いくらですか。','どちら hỏi phương hướng hoặc nơi chốn một cách lịch sự; どなた hỏi người, いくら hỏi giá.'),
 (4,4,'mg-kara-made','Bưu điện mở từ 9 giờ đến 5 giờ. Chọn cụm kết thúc giờ hoạt động.','5時までです。','5時からです。','5時にです。','Khoảng hoạt động dùng 9時から 5時まで; まで đánh dấu mốc kết thúc.'),
 (5,2,'mg-noi-den-e','Với mốc 先月, chọn dạng hỏi đã đi đâu trong quá khứ.','行きましたか。','行きますか。','行きませんか。','先月 là tháng trước, nên hỏi bằng quá khứ lịch sự 行きましたか.'),
 (6,3,'mg-doi-tuong-wo','Hỏi “học gì?” khi câu trả lời là tiếng Nhật.','何を','どこで','だれと','日本語 là đối tượng của 勉強します. Từ hỏi đối tượng là 何を; どこで hỏi nơi, だれと hỏi người cùng làm.'),
 (7,3,'mg-nguoi-nhan-ni','Chọn cụm chỉ người nhận khi cho anh Lee mượn sách.','イーさんに','イーさんを','イーさんで','Người nhận trong 「イーさんに 本を 貸します」 đi với に; 本 là vật được cho mượn nên đi với を.'),
 (8,3,'mg-khang-dinh-phu-dinh','Đổi 忙しい sang phủ định lịch sự trong 「ミラーさんは 忙し…」.','くないです。','いじゃ ありません。','く ありません。','Tính từ い bỏ い rồi thêm くないです: 忙しくないです. じゃ ありません dùng cho danh từ và tính từ な.'),
 (9,5,'mg-ga-arimasu','Hỏi có từ điển không: chọn trợ từ sau 辞書.','が','を','で','Mẫu tồn tại là 「辞書が ありますか」; 辞書 đi với が, không phải を hay で.'),
 (10,2,'mg-arimasu-imasu','Dưới ghế có mèo. Chọn động từ tồn tại.','います。','あります。','です。','猫 là sinh vật nên dùng います. あります dành cho vật không sống.'),
 (11,2,'mg-cach-dem','Hỏi số đĩa CD: chọn lượng từ phù hợp.','何枚','何台','何人','CD là vật mỏng, dẹt, dùng 枚. 台 đếm máy, 人 đếm người.'),
 (12,2,'mg-qua-khu-i','Nói “tháng trước bận”: chọn dạng quá khứ của 忙しい.','忙しかった','忙しい','忙しいでした','Tính từ い đổi い thành かった để nói quá khứ: 忙しかったです.'),
 (13,5,'mg-muc-dich-v','Nói đến cửa hàng bách hóa để mua quà: chọn dạng chỉ mục đích của 買います.','買いに','買いで','買いますに','Mục đích đi đâu dùng thân ます của động từ + に: 買います → 買いに 行きます.'),
 (14,2,'mg-te-kudasai','Nhờ bật điều hòa: chọn thể て của つけます.','つけて','つけます','消して','Đề nghị 「つけて ください」 dùng thể て. 消して là tắt, trái với gợi ý bật.'),
 (15,3,'mg-tewa-ikemasen','Cấm chụp ảnh ở đây: chọn thể て của 撮ります trước は いけません.','撮って','撮りて','撮ります','撮ります thuộc nhóm 1: 撮って. Mẫu cấm là 撮っては いけません.'),
 (16,3,'mg-te-kara','Nói sau khi rút tiền thì đi mua sắm: chọn dạng 下ろします.','下ろしてから、','下ろしから、','下ろすから、','Hành động hoàn tất trước dùng Vてから: 下ろします → 下ろしてから.'),
 (17,2,'mg-naide-kudasai','Vì nguy hiểm, xin đừng đẩy: chọn dạng của 押します.','押さないで','押しないで','押して','押す chuyển thể ない thành 押さない, thêm で trước ください. 押して là lời yêu cầu đẩy.'),
 (18,3,'mg-dekimasu','Hỏi có thể bơi bao nhiêu mét: chọn dạng 泳ぎます trước ことができますか.','泳ぐ','泳ぎます','泳いで','Trước ことができます cần thể từ điển: 泳ぎます → 泳ぐ.'),
 (19,3,'mg-tari-tari','Liệt kê ví dụ hoạt động buổi tối: chọn dạng 入ります trước たり.','入ったり、','入って、','入りたり、','Liệt kê vài việc tiêu biểu dùng thể た + り: 入ります → 入ったり.'),
 (20,2,'mg-tinh-tu-i','Đổi 「おもしろいです」 sang lối nói thân mật hiện tại.','おもしろい。','おもしろいだ。','おもしろかった。','Tính từ い ở thể thường hiện tại giữ nguyên おもしろい; không thêm だ. おもしろかった là quá khứ.'),
 (21,3,'mg-to-omoimasu','Trước と 思います, chọn thể thường của 「よく 働きます」.','ほんとうに よく 働く','ほんとうに よく 働きます','ほんとうに よく 働いた','Mệnh đề dẫn ý nghĩ dùng thể thường; 働きます đổi thành 働く, giữ nguyên ý hiện tại.'),
 (22,4,'mg-bo-nghia-danh-tu','Bổ nghĩa cho 所 bằng “lần đầu gặp chồng”: chọn dạng của 会いました.','初めて 主人に 会った','初めて 主人に 会いました','初めて 主人に 会って','Mệnh đề đứng trước danh từ 所 dùng thể thường quá khứ 会った, không dùng dạng lịch sự 会いました.'),
 (23,2,'mg-ru-ta-toki','Chọn dạng “trước khi đi ngủ” để nói お休みなさい.','寝る','寝た','寝ます','Lời chúc được nói trước khi ngủ, nên dùng 寝る とき. 寝た とき là sau khi việc ngủ đã xảy ra.'),
 (24,3,'mg-te-moraimasu','Tôi được anh Wang cho xem ảnh: chọn động từ nhận giúp đỡ.','もらいました。','くれました。','あげました。','Chủ ngữ わたし nhận hành động từ ワンさんに nên dùng 見せてもらいました.'),
 (25,2,'mg-tara-dieu-kien','Nếu ga gần thì tiện: chọn dạng điều kiện của 近い.','近かったら、','近くたら、','近いだったら、','Tính từ い đổi い thành かったら: 近い → 近かったら.'),
 (26,4,'mg-hoi-ndesuka','Hỏi lý do người kia sắp chuyển nhà: chọn dạng của 引っ越しします trước んですか.','引っ越しするんですか。','引っ越ししますんですか。','引っ越ししたんですか。','Trước んですか dùng thể thường hiện tại 引っ越しする; しますんですか không đúng dạng nối.'),
 (27,2,'mg-cau-kha-nang','Thiếu tiền nên không thể mua máy tính: chọn động từ khả năng phủ định.','買えません。','買いません。','買えます。','お金が 足りない là trở ngại về khả năng; 買えません nghĩa là không thể mua, khác 買いません là không mua.'),
 (28,2,'mg-nagara','Vừa nghe vừa ghi chép: chọn dạng 聞きます trước ながら.','聞きながら','聞くながら','聞いてから','Vながら nối vào thân ます: 聞きます → 聞きながら. 聞いてから là nghe xong rồi mới làm tiếp.'),
 (29,4,'mg-hoan-tat','Hỏi đã viết xong báo cáo rồi sao: chọn dạng trước しまったんですか.','書いて','書いた','書きます','完了 với しまう dùng thể て: 書いて しまったんですか.'),
 (30,3,'mg-chuan-bi-truoc','Trước khi bạn đến, dọn phòng sẵn: chọn dạng trước まえに.','友達が 来る','友達が 来ます','友達が 来た','Trước まえに chỉ việc sắp xảy ra dùng thể từ điển 来る, rồi tiếp theo là 片づけて おきます.'),
 (31,2,'mg-you-to-omotteimasu','Đang định đi nhà thờ với gia đình: chọn dạng 行きます trước と 思って います.','行こうと','行きますと','行ったと','Ý định dùng thể ý chí + と 思って います: 行きます → 行こうと.'),
 (32,2,'mg-houga-ii','Bị bỏng thì nên làm mát ngay: chọn dạng 冷やします trước ほうが いい.','冷やした','冷やして','冷やします','Lời khuyên nên làm việc gì dùng Vた ほうが いい: 冷やした ほうが いい.'),
 (33,2,'mg-cam-chi','Biển “cấm bơi”: chọn dạng trước な.','泳ぐ','泳がない','泳ぎます','Lệnh cấm dùng thể từ điển + な: 泳ぐな. 泳がないな không phải mẫu này.'),
 (34,3,'mg-ato-de','Sau khi giải thích xong, hãy hỏi: chọn dạng 終わります trước あとで.','説明が 終わった','説明が 終わる','説明が 終わります','Sau khi hoàn tất dùng Vた あとで: 終わった あとで.'),
 (35,3,'mg-ba-dieu-kien','Nếu không đeo kính thì không đọc được chữ: chọn dạng điều kiện phủ định.','かけなければ、','かけないれば、','かけるなければ、','Phủ định điều kiện của かける là かけなければ; ない đổi thành なければ.'),
 (36,3,'mg-youni-narimasu','Nói nay đã viết được gần hết katakana: chọn dạng trước ように なりました.','はい、ほとんど 書ける','はい、ほとんど 書けます','はい、ほとんど 書いた','Trước ように なりました dùng thể thường của động từ khả năng: 書ける ように なりました.'),
 (37,3,'mg-bi-tac-dong-do-vat','Bị trộm lấy máy ảnh: chọn động từ bị động.','取られました。','取りました。','取ります。','Người nói chịu tác động từ 泥棒に, nên dùng bị động 取られました; máy ảnh vẫn đi với を.'),
 (38,3,'mg-no-ga','Nói thích đi dạo bờ biển: chọn cụm danh từ hóa trước 好きです.','散歩するのが','散歩しますのが','散歩するのを','好きです nói về việc yêu thích đi với Vるのが; thể lịch sự します không đặt trước の.'),
 (39,2,'mg-nakute-nguyen-nhan','Không gặp được gia đình nên buồn: chọn dạng nối nguyên nhân.','会えなくて、','会えないで、','会えないて、','Phủ định khả năng 会えない nối với cảm xúc 寂しい bằng 会えなくて; ない đổi thành なくて.'),
 (40,3,'mg-ka-douka','Lo không biết buổi trình bày có thuận lợi không: chọn mệnh đề nghi vấn lồng.','うまく いくか どうか、','うまく いきますか どうか、','うまく いって どうか、','Trước か どうか dùng thể thường いく, không giữ いきますか.'),
 (41,4,'mg-te-itadakimasu','Tôi được thầy Kobayashi sửa phát âm: chọn đuôi khiêm nhường.','いただきました。','くださいました。','やりました。','Với わたしは 小林先生に, người nói là bên nhận giúp đỡ; dùng 直して いただきました.'),
 (42,2,'mg-n-tameni','Học tiếng Nhật hằng tuần vì công việc: chọn dạng nối 仕事 với ために.','仕事の ために、','仕事な ために、','仕事ために、','Danh từ đứng trước ために cần の: 仕事の ために.'),
 (43,2,'mg-sou-dong-tu','Dựa vào dấu hiệu trời sắp mưa: chọn dạng 降ります trước そうです.','降りそうですよ。','降るそうですよ。','降ったそうですよ。','Vẻ sắp xảy ra dùng thân ます + そう: 降ります → 降りそう. 降るそうです là nghe nói trời mưa.'),
 (44,2,'mg-sugimasu','Áo khoác quá rộng: chọn dạng của 大きい trước すぎます.','大きすぎます。','大きいすぎます。','大きくすぎます。','Tính từ い bỏ い trước すぎます: 大きい → 大きすぎます.'),
 (45,4,'mg-noni','Xếp hàng hai tiếng mà không mua được vé: chọn vế nhượng bộ.','2時間 並んだのに、','2時間 並んだなのに、','2時間 並ぶのに、','Việc xếp hàng đã xảy ra nên dùng thể た + のに: 並んだのに.'),
 (46,2,'mg-tokoro-teiru','Đang điều tra nguyên nhân hỏng: chọn dạng trước ところです.','調べて いる','調べる','調べた','Đang trong quá trình điều tra dùng Vている ところです. 調べる là sắp làm, 調べた là vừa xong.'),
 (47,5,'mg-you-desu','Từ dấu hiệu thấy người cầm ô, suy đoán trời đang mưa: chọn dạng trước ようです.','降って いるようですね。','降って いますようですね。','降るそうですね。','Suy đoán từ dấu hiệu dùng thể thường 降っている + よう; 降るそう là lời truyền đạt.'),
 (48,2,'mg-nguoi-ni','Trưởng bộ phận sai anh Sato tổng hợp dữ liệu: chọn cụm đánh dấu người thực hiện.','部長は 佐藤さんに データを','部長は 佐藤さんを データを','部長が 佐藤さんで データを','Với tha động từ まとめる còn có tân ngữ データを, người bị sai khiến đi với に: 佐藤さんに.'),
 (49,3,'mg-o-ni-narimasu','Nói kính trọng việc thầy nghỉ việc: chọn dạng của やめます.','おやめに なります。','おやめを なります。','おやめします。','Hành động của 先生 dùng tôn kính お + thân ます + に なります: おやめに なります.'),
 (50,2,'mg-go-shimasu','Tôi giới thiệu thầy Ito một cách khiêm nhường: chọn dạng của 紹介します.','ご紹介します。','お紹介します。','ご紹介に なります。','Động từ gốc Hán 紹介します dùng ご～します khi nói về hành động của mình hướng tới người được kính trọng.'),
]

# Full sentence frames with an explicit conjugation cue. These have one requested
# surface form; the learner types it instead of selecting a chip from the bank.
FILL = {
 8: ('ミラーさんは ＿＿。', 'Từ 忙しい, điền phủ định lịch sự theo dạng Aくないです; dùng đuôi ないです.', '忙しくないです'),
 12: ('先月は ＿＿。', 'Từ 忙しい, điền quá khứ lịch sự theo dạng Aかったです.', '忙しかったです'),
 13: ('デパートへ お土産を ＿＿ 行きます。', 'Từ 買います, bỏ ます rồi thêm に để chỉ mục đích đi mua.', '買いに'),
 17: ('危ないですから、＿＿ ください。', 'Từ 押します, điền thể ない cộng で để nói “xin đừng đẩy”.', '押さないで'),
 25: ('駅が ＿＿、便利です。', 'Từ 近い, điền điều kiện bằng dạng Aかったら.', '近かったら'),
 28: ('話を ＿＿ メモして ください。', 'Từ 聞きます, lấy thân ます rồi thêm ながら để nói “vừa nghe vừa…”.', '聞きながら'),
 35: ('眼鏡を ＿＿、辞書の 字が 読めません。', 'Từ かけます, điền điều kiện phủ định bằng đuôi なければ.', 'かけなければ'),
 38: ('わたしは 海岸を ＿＿ 好きです。', 'Giữ đúng động từ 散歩します, đổi sang thể từ điển 散歩する rồi thêm のが; không thêm từ hay trợ từ khác vào ô.', '散歩するのが'),
 39: ('家族に ＿＿、寂しいです。', 'Từ 会えません, điền phủ định khả năng nối nguyên nhân bằng đuôi なくて.', '会えなくて'),
 42: ('＿＿、毎週 日本語を 習って います。', 'Dùng danh từ 仕事 và mẫu Nのために, viết ために bằng kana; dấu phẩy đã có sau ô trống.', '仕事のために'),
 44: ('この 上着は ＿＿。', 'Từ 大きい, bỏ い rồi thêm すぎます để nói áo quá rộng.', '大きすぎます'),
 46: ('故障の 原因は わかりましたか。— いいえ、今 ＿＿ ところです。', 'Từ 調べます, điền Vている thể thường trước ところです để nói “đang điều tra”.', '調べている'),
 49: ('先生は 3月に 大学を ＿＿。', 'Từ やめます, điền dạng tôn kính お＋thân ます＋になります.', 'おやめになります'),
 50: ('はじめに 伊藤先生を ＿＿。', 'Từ 紹介します, điền dạng khiêm nhường ご＋danh từ Hán Nhật＋します.', 'ご紹介します'),
}


def first_drill(snapshot, group):
    section = next(s for s in snapshot['sections'] if s['id'] == f'mg-b{group}')
    node = parse(section['html'])
    drill = node.all('mg-drill')[0]
    cue = drill.all('mg-drill-q')[0].text()
    chips = [x.text() for x in drill.all('mg-chip')]
    return drill.attrs['data-mg-drill'], cue, chips


def main():
    snapshots = reviewed_snapshots(ROOT)
    out = ROOT / 'authored' / 'renshuu'
    out.mkdir(parents=True, exist_ok=True)
    reviewed_path = ROOT / 'authored' / 'renshuu-reviewed.json'
    group_map = {}
    for name in ('group-map-01-25.json', 'group-map-26-50.json'):
        mapping_path = ROOT / 'authored' / 'renshuu' / name
        if mapping_path.exists():
            group_map.update(json.loads(mapping_path.read_text(encoding='utf-8')))
    assert set(group_map) == {str(n) for n in range(1,51)}, 'Checked B group maps must cover all 50 lessons'
    companion = {}
    if reviewed_path.exists():
        for record in json.loads(reviewed_path.read_text(encoding='utf-8')):
            lesson = record['lesson']
            assert 1 <= lesson <= 50 and lesson not in companion
            companion[lesson] = record['item']
    report = {'status': 'editorial_draft_not_human_reviewed', 'lessons': 50, 'items': 0,
              'manualQnA': 0, 'manualFillInBlank': 0,
              'source_example_recognition_items': 0, 'source_B_groups': 0,
              'B_groups_with_authored_item': 0, 'B_groups_pending': 0,
              'source_drills_total': 0, 'source_drills_pending_official_answer': 0,
              'source_drills_with_ai_adaptation': 0, 'source_drills_without_ai_adaptation': 0,
              'source_bank_choices': 0, 'ai_added_choices': 0,
              'vocabulary_files_loaded': 0, 'vocabulary_lexical_review': 'pending_human',
              'note': 'instruction_vi must be rendered together with prompt_ja; pending_source_drill_ids tracks missing official answer text, not authored coverage',
              'group_map_status': 'checked_against_group_titles_instructions_and_examples',
              'per_lesson': []}
    assert len(SPECS) == 50
    for lesson, group, grammar, task, good, bad1, bad2, why in SPECS:
        vocab_paths = list((ROOT / 'materials' / 'vocabulary').rglob(f'*Bài-{lesson}.md'))
        assert len(vocab_paths) == 1, (lesson, vocab_paths)
        assert vocab_paths[0].read_text(encoding='utf-8').startswith('# Bài')
        report['vocabulary_files_loaded'] += 1
        path = snapshots[lesson]
        snap = json.loads(path.read_text(encoding='utf-8'))
        drill_id, cue, chips = first_drill(snap, group)
        assert grammar in {p['id'] for p in snap['points']}, (lesson, grammar)
        assert good in chips, (lesson, group, good)
        base_options = [good, bad1, bad2]
        turn = lesson % 3
        options = base_options[turn:] + base_options[:turn]
        assert len(set(options)) == 3
        bank_count = sum(choice in chips for choice in options)
        item = {
            'id': f'rb-{lesson:02}-{drill_id}-grammar',
            'kind': 'manualQnA',
            'source_id': drill_id,
            'source_group_id': f'b{group}',
            'prompt_ja': cue.removeprefix('1) ').strip(),
            'instruction_vi': task,
            'choices': [{'id': f'c{i+1}', 'text': choice} for i, choice in enumerate(options)],
            'correct': f'c{options.index(good)+1}',
            'explanation_vi': why,
            'grammar_refs': [grammar],
            'provenance': {
                'source_prompt': 'official_snapshot',
                'source_option_bank': 'official_snapshot',
                'answer': 'ai_editorial_inference',
                'explanation': 'ai_authored',
                'human_review': 'pending',
                'choice_origin': {f'c{i+1}': 'official_option_bank' if choice in chips else 'ai_authored'
                                  for i, choice in enumerate(options)},
            },
        }
        if lesson in FILL:
            frame, instruction, answer = FILL[lesson]
            item['source_prompt_ja'] = item['prompt_ja']
            item['prompt_ja'] = frame
            item['instruction_vi'] = instruction
            item['kind'] = 'manualFillInBlank'
            item.pop('choices')
            item['correct'] = answer
            item['provenance']['source_prompt'] = 'ai_adapted_from_official_drill'
            item['provenance'].pop('choice_origin')
        else:
            report['source_bank_choices'] += bank_count
            report['ai_added_choices'] += 3 - bank_count
        report[item['kind']] += 1
        items = []
        if lesson in companion:
            extra = companion[lesson]
            assert extra['source_id'] in snap['drill_ids'], (lesson, extra['source_id'])
            assert set(extra.get('grammar_refs', [])) <= {p['id'] for p in snap['points']}
            assert extra['id'] != item['id']
            items.append(extra)
            report[extra['kind']] += 1
        items.append(item)
        adapted_drill_ids = list(dict.fromkeys(x['source_id'] for x in items))
        example_items, pending_groups, group_count = additional_items(snap, adapted_drill_ids)
        items.extend(example_items)
        checked = group_map[str(lesson)]
        assert set(checked) == {f'b{n}' for n in range(1, group_count+1)}, (lesson, set(checked))
        point_order = {p['id']: idx for idx,p in enumerate(snap['points'])}
        for authored in items:
            source_group = authored.get('source_group_id', authored['source_id'].split('-')[0])
            refs = checked[source_group]
            assert refs and set(refs) <= set(point_order), (lesson, source_group, refs)
            authored['source_group_id'] = source_group
            authored['grammar_refs'] = refs
            authored['grammar_mapping_status'] = 'checked_group_map'
            authored['placement_after_point_id'] = max(refs, key=lambda x: point_order[x])
        report['manualQnA'] += len(example_items)
        report['source_example_recognition_items'] += len(example_items)
        report['source_B_groups'] += group_count
        report['B_groups_with_authored_item'] += group_count - len(pending_groups)
        report['B_groups_pending'] += len(pending_groups)
        for authored in items:
            assert authored['source_id'] in snap['drill_ids'] or '-rei-' in authored['source_id']
            assert authored['prompt_ja'] and authored['instruction_vi'] and authored['explanation_vi']
            if authored['kind'] == 'manualQnA':
                ids = [c['id'] for c in authored['choices']]
                assert len(ids) == len(set(ids)) and authored['correct'] in ids
                assert len({c['text'] for c in authored['choices']}) == len(ids)
            elif authored['kind'] == 'manualFillInBlank':
                assert '＿＿' in authored['prompt_ja'] and isinstance(authored['correct'], str)
            else:
                raise AssertionError((lesson, authored['kind']))
        adapted = adapted_drill_ids
        payload = {
            'lesson': lesson,
            'source_snapshot': path.relative_to(ROOT).as_posix(),
            'source_url': snap['url'],
            'items': items,
            'source_drill_count': len(snap['drill_ids']),
            'source_drill_ids_with_ai_adaptation': adapted,
            'source_drill_ids_without_ai_adaptation': [x for x in snap['drill_ids'] if x not in adapted],
            'pending_source_groups': pending_groups,
            'pending_source_drill_ids': snap['drill_ids'],
            'review_status': 'ai_editorial_draft',
            'render_instruction_vi_with_prompt_ja': True,
        }
        (out / f'lesson-{lesson:02}.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        report['items'] += len(items)
        report['source_drills_total'] += len(snap['drill_ids'])
        report['source_drills_pending_official_answer'] += len(snap['drill_ids'])
        report['source_drills_with_ai_adaptation'] += len(adapted)
        report['source_drills_without_ai_adaptation'] += len(snap['drill_ids']) - len(adapted)
        report['per_lesson'].append({'lesson': lesson, 'authored_items': len(items),
                                     'source_B_groups': group_count,
                                     'B_groups_with_authored_item': group_count-len(pending_groups),
                                     'adapted_source_drills': len(adapted),
                                     'source_drills': len(snap['drill_ids']),
                                     'official_answer_text_available_in_snapshot': 0})
    (ROOT / 'reports' / 'renshuu-authoring.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"Wrote {report['items']} items across 50 lessons; adapted source drills: {report['source_drills_with_ai_adaptation']}; official answer text pending: {report['source_drills_total']}")


if __name__ == '__main__':
    main()
