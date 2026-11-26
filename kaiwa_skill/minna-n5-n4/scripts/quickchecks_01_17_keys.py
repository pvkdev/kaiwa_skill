"""Editorial answer audit of the visible quick checks in lessons 1–17.

Choice IDs below were selected by reading each prompt and all its options.
They are AI answer judgments, not a VNJPClub reveal or official key.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# In source order within each lesson, across all point sections.
KEYS = {
 1: '1 2 0 1 2 1 0 1 2 1 0 1 0 2',
 2: '2 0 1 0 2 1 0 1 2 2 0',
 3: '1 2 X 2 1 0 1 2 0 1 2',
 4: '1 2 0 2 0 1 1 2 0 1 2 0',
 5: '1 2 0 1 2 0 1 2 0 1 2 0 1',
 6: '0 1 2 0 1 2 0 1 2',
 7: '1 2 0 1 2 X 1 2',
 8: '3 1 0 2 1 0 0 1 0 2 0 2 X 0 X',
 9: '1 0 2 0 1 2 0 1 2',
 10: '1 0 2 0 1 2 0 1 2 0',
 11: '1 2 0 1 2 0 1 2 0',
 12: '1 0 2 1 0 2 1 0 2 1',
 13: '0 2 1 0 2 1 0 1 2',
 14: '1 2 0 1 2 0 1 2 0 1 2',
 15: '1 2 0 1 2 0 1 2 0 2',
 16: '1 0 2 1 2 0 2 0 1',
 17: '1 0 2 0 1 2 1 0',
}

ISSUES = {
 (3,'vi-tri-1'): '“Nhà tôi ở đây” có thể hiểu là chỉ vị trí hoặc chỉ chính ngôi nhà đang đứng trước mặt; cả 「わたしの うちは ここです」 và 「ここは わたしの うちです」 đều diễn đạt hợp lý. Cần nêu rõ đang hỏi vị trí của nhà.',
 (7,'nguoi-cho-ni-kara-2'): 'Nguồn vừa dạy に／から cho người cho hoặc nguồn nhận. Với 銀行, cả 「銀行から お金を 借ります」 và 「銀行に お金を 借ります」 đều có thể hiểu là vay từ ngân hàng; cần hỏi “dùng から” hoặc sửa phương án.',
 (8,'soshite-1'): '「日本の 車は 高いです。そして、いいです」 và 「奈良は 静かです。そして、きれいです」 đều nối hai nhận xét cùng chiều bằng そして; hai đáp án hợp lý.',
 (8,'ga-2'): 'Câu 「地下鉄は 便利ですが、きれいです」 có thể dùng が để nối hai nhận xét tương phản tùy ngữ cảnh; 「そして、きれいです」 cũng tự nhiên. Cần nêu rõ muốn liệt kê hai ưu điểm.',
}

# One explanation per source question, in source order. X marks an issue above.
EXPL = {
 1: '''は làm trợ từ chủ đề được đọc là “wa”, dù chữ viết là は.
インド là nước Ấn Độ; thêm 人 thành インド人 mới chỉ người Ấn Độ.
Danh từ 医者 phủ định bằng じゃ ありません; không thêm です vào sau.
では ありません trang trọng hơn じゃ ありません và cùng nghĩa phủ định.
Câu hỏi có/không giữ 医者です rồi thêm か ở cuối.
いいえ phủ nhận 学生です, nên đáp 学生じゃ ありません.
あの方 là “vị kia”; どなた là cách hỏi “ai” lịch sự.
だれ hỏi tên người, nên trả lời trực tiếp 山田さんです, không dùng はい／いいえ.
20 tuổi có cách đọc đặc biệt はたち.
Hỏi tuổi thầy giáo dùng おいくつ, lịch sự hơn 何歳.
Hai người cùng là nhân viên công ty nên dùng も nghĩa là “cũng”.
Câu trả lời phủ nhận việc Santos cũng là sinh viên nên chuyển sang は, không dùng も.
さくら大学の 先生 là giảng viên thuộc Đại học Sakura; の nối nơi công tác với người.
Không tự gắn さん vào tên mình khi giới thiệu: わたしは ミラーです. ''',
 2: '''あれ chỉ vật xa cả người nói lẫn người nghe.
何ですか hỏi “là gì”, nên trả lời bằng tên đồ vật ノートです.
その đứng trước 辞書 và chỉ vật gần người nghe.
はい、そうです xác nhận lời người hỏi là đúng.
Hai lựa chọn được hỏi bằng ノートですか、手帳ですか.
コンピューターの 本 là sách có nội dung về máy tính.
だれの hỏi “của ai”; 何の hỏi loại hoặc nội dung.
Khi danh từ chỉ vật đã rõ, わたしのです lược danh từ sau の.
社員 chỉ người nên không lược bằng の thay danh từ chỉ vật trong mẫu này.
お thêm vào một số từ để tạo cách nói lịch sự; không gắn tùy tiện vào mọi danh từ.
そうですか với giọng hạ xuống thể hiện đã tiếp nhận thông tin mới. ''',
 3: '''あそこ chỉ nơi xa cả người nói và người nghe.
そちら là cách nói lịch sự tương ứng với そこ.
X
どちら hỏi địa điểm một cách lịch sự; だれ hỏi người, 何 hỏi vật hoặc nội dung.
学校は どこですか khi làm quen có thể hỏi người nghe học ở trường nào.
どこの 時計 hỏi đồng hồ xuất xứ từ nước hoặc nơi nào.
Nói về nước mình dùng 国, không tự dùng tiền tố tôn kính お.
3階 đọc là さんがい, với âm がい đặc biệt.
地下1階 nghĩa là tầng thứ nhất dưới mặt đất.
いくら hỏi giá của chiếc cà vạt.
10.000 là 一万, đọc いちまん. ''',
 4: '''9時 đọc là くじ, không phải きゅうじ.
6分 đọc là ろっぷん do biến âm của ろく + ふん.
何曜日 hỏi thứ trong tuần; 何時 hỏi giờ.
きのう chỉ hôm qua nên 休みました ở quá khứ.
寝ませんでした là phủ định lịch sự ở quá khứ của 寝ます.
Câu hỏi きのう 休みましたか hỏi quá khứ; đáp không cũng dùng 休みませんでした.
あした là mốc tương đối nên không thêm に trong あした 休みます.
8時 là giờ cụ thể, đi với に trước 起きます.
から đánh dấu 2 giờ bắt đầu, まで đánh dấu 4 giờ kết thúc.
Chỉ nêu mốc bắt đầu thì dùng 会議は 2時からです.
と nối 月曜日 và 火曜日 thành hai ngày nghỉ.
2時からですね nhắc lại giờ bắt đầu để xác nhận với người nghe. ''',
 5: '''へ khi là trợ từ chỉ hướng được đọc là “e”.
帰ります diễn đạt trở về nơi gốc hoặc nhà mình: うちへ 帰ります.
どこも đi với phủ định 行きませんでした để nói đã không đi đâu.
Đi bộ dùng 歩いて, không thêm trợ từ phương tiện で vào sau động từ này.
飛行機 là phương tiện, dùng 飛行機で 行きます.
友達と diễn đạt đi cùng bạn; と đánh dấu người đồng hành.
一人で là một mình; で đi với số người trong trường hợp này.
Ngày 1 là ついたち, tháng 9 là くがつ.
Ngày 24 có cách đọc にじゅうよっか.
いつ hỏi khi nào và không thêm に ngay sau.
来年の 3月 là mốc tháng cụ thể nên thêm に: 来年の 3月に.
よ báo tin mới cho người nghe: あしたは 休みですよ.
そうですね bày tỏ đồng tình với thông tin hai người cùng biết. ''',
 6: '''ジュース là thứ được uống nên đi với を.
Trợ từ を trong tiếng Nhật hiện đại đọc là “o”.
宿題を します là làm bài tập về nhà; 見ます và 聞きます mang nghĩa khác.
おととい là hôm kia nên dùng quá khứ しましたか để hỏi đã làm gì.
Trong 何の 本, 何 đọc là なん trước の.
図書館 là nơi diễn ra hành động đọc, đánh dấu bằng で.
Vませんか là lời mời: いっしょに 日本へ 行きませんか.
Vましょう là lời rủ hoặc đề nghị cùng làm: 休みましょう.
京都ですか với ngữ điệu hạ là tiếp nhận thông tin “Kyoto à”. ''',
 7: '''英語 là ngôn ngữ dùng để viết thư, đi với で.
Hỏi cách nói trong một ngôn ngữ dùng ～語で 何ですか.
友達 là người nhận hoa nên đi với に; 花 là vật được tặng đi với を.
貸します là cho người khác mượn; 借ります là mình mượn.
Người nói nhận sách từ bạn nên dùng もらいます.
X
まだです trả lời rằng đến lúc này vẫn chưa ăn trưa.
Trong hội thoại, は sau この スプーン có thể lược khi chủ đề đã rõ. ''',
 8: '''きれい thuộc nhóm tính từ な dù kết thúc bằng chữ い.
有名 là tính từ な: 有名な 人, 有名です.
寒い đổi い thành くない: 寒くないです.
きれい là tính từ な nên phủ định bằng きれいじゃ ありません.
いい có dạng phủ định bất quy tắc よくないです.
Tính từ な đứng trước danh từ cần な: きれいな 花.
新しい là tính từ い nên đặt trực tiếp trước カメラ.
あまり đi với phủ định: あまり おいしくないです.
とても bổ nghĩa cho きれい để nói “rất đẹp”.
どうですか hỏi đánh giá công việc; なんですか hỏi đó là gì.
どんな đứng trước 人 để hỏi người như thế nào.
どんな phải đứng trước danh từ, nên どんなですか thiếu danh từ.
X
が nối hai vế “đắt nhưng ngon” theo quan hệ tương phản.
X ''',
 9: '''好きです nói điều mình thích bằng Nが: ジャズが 好きです.
上手 là tính từ な nên phủ định bằng 上手じゃ ありません.
わかります đi với đối tượng được hiểu bằng が: 日本語が わかります.
あります diễn đạt có vật: チケットが あります.
どんな 音楽 hỏi thể loại âm nhạc.
全然 đi với わかりません để nói hoàn toàn không hiểu.
だいたい わかります nghĩa là hiểu phần lớn hoặc nắm ý chính.
から theo sau lý do 忙しいです rồi mới đến kết quả 行きません.
どうしてですか hỏi nguyên nhân của điều vừa được nói. ''',
 10: '''木 là cây, một thực thể không tự di chuyển, nên dùng あります.
象 là động vật sống, nên dùng います.
教室 là nơi có 先生, đi với に trong câu tồn tại.
だれが いますか hỏi ai hiện diện ở nơi đó.
佐藤さん là người nên hỏi vị trí bằng どこに いますか.
Giữa hai nơi dùng AとBの間: 銀行と 郵便局の 間.
食べます là hành động diễn ra gần ga nên 駅の 近くで.
や…など nêu vài ví dụ tiêu biểu, không khẳng định danh sách đầy đủ.
など đứng sau các món được liệt kê: 肉や 卵などを 買いました.
アジアストアですか lặp lại tên cửa hàng để xác nhận đã nghe đúng. ''',
 11: '''Máy tính là thiết bị nên dùng 台 để đếm.
Hai người có cách đọc đặc biệt ふたり.
りんご là đối tượng được mua, đi với を; よっつ là số lượng đặt trước động từ.
いくつ hỏi số lượng đồ vật đếm bằng ひとつ, ふたつ.
一日 chỉ thời lượng một ngày, đọc いちにち; ついたち là ngày mùng một.
2時間 là thời lượng hai tiếng, đặt trực tiếp trước 勉強します.
どのくらい hỏi độ dài thời gian chuyến đi mất.
1か月に 2回 diễn đạt tần suất hai lần mỗi tháng.
1人だけ nghĩa là chỉ một người; ぐらい chỉ khoảng chừng. ''',
 12: '''きれい là tính từ な nên quá khứ lịch sự là きれいでした.
雪です là câu danh từ; phủ định quá khứ là 雪じゃ ありませんでした.
Tính từ い 高い đổi thành 高くなかったです ở phủ định quá khứ.
あまり おいしくなかったです nghĩa là đã không ngon lắm; なかった là quá khứ phủ định.
A は B より 安いです đặt A làm vật rẻ hơn B.
Trong どちらが 軽いですか, が đánh dấu bên được hỏi trong so sánh hai vật.
どちらも nghĩa là cả hai phía; trong câu sở thích là thích cả hai.
どこ hỏi địa điểm đẹp nhất trong phạm vi đang so sánh.
で trong 世界で giới hạn phạm vi so sánh là cả thế giới.
きれいな かばん lược かばん thành きれいなの; tính từ な giữ な trước の. ''',
 13: '''ほしいです nói thứ người nói muốn có bằng Nが: 友達が ほしいです.
Mời khách uống cà phê dùng コーヒーは いかがですか, lịch sự hơn hỏi mong muốn bằng ほしい.
寝ます bỏ ます rồi thêm たいです thành 寝たいです.
会います trong mẫu muốn gặp ai dùng người đi với に: 人に 会いたいです.
Thân ます của 食べます là 食べ; thêm に để nêu mục đích đi ăn.
3時ごろ là quanh thời điểm 3 giờ; 3時間ぐらい là thời lượng khoảng ba tiếng.
Danh từ hoạt động 買い物 đi trực tiếp với に 行きます để nói đi mua sắm.
何か nghĩa là thứ gì đó, phù hợp trước 飲みたいです.
ご trong ご注文 là tiền tố biểu thị sự lịch sự, tôn trọng. ''',
 14: '''借ります thuộc nhóm II: bỏ ます rồi thêm て thành 借りて.
コピーします thuộc nhóm III do cấu trúc danh từ + します.
持ちます thuộc nhóm I, đuôi ち đổi thành って: 持って.
見せます thuộc nhóm II, bỏ ます thêm て: 見せて.
どうぞ mở lời mời khách uống một cách tự nhiên.
Trước ください dùng thể て: 書きます → 書いて ください.
Đang nghe nhạc bây giờ dùng 聞いて います.
Phủ định của Vて います là Vて いません: 泳いで いません.
貸しましょうか là lời đề nghị cho người nghe mượn bút.
雨が 降って います dùng が để nêu hiện tượng mưa.
すみませんが dùng が nối lời mở đầu lịch sự với yêu cầu chính. ''',
 15: '''Xin phép dùng Vても いいですか: 飲んでも いいですか.
すみません、ちょっと… là cách từ chối gián tiếp, giữ lịch sự.
飲んでは いけません nghĩa là không được uống; 飲んでも いいです là được phép.
住んで います chỉ nơi cư trú bằng に: 東京に 住んで います.
持って います diễn đạt trạng thái đang có hoặc mang theo một vật.
Nghĩa “không biết” của 知っています phủ định bằng 知りません.
働いて います ở đây diễn đạt công việc hiện tại, không khẳng định đang có mặt tại ngân hàng.
パン là thứ cửa hàng bán nên đi với を trước 売って います.
座ります nhận nơi ngồi bằng に: いすに 座って ください.
置きます nhận vị trí đặt vật bằng に: 机の 上に 本を 置いて ください. ''',
 16: '''飲みます đổi thành 飲んで để nối việc uống trà rồi nghỉ.
便利 là tính từ な nên dạng nối là 便利で.
“Hẹp nhưng sạch” là tương phản, nối hai câu bằng が.
会社員 là danh từ; dạng nối với câu sau là 会社員で.
読んでから nghĩa là đọc xong rồi mới làm việc tiếp theo.
目 là đặc điểm của người được nói tới, nên dùng 目が 大きい.
乗ります nhận phương tiện bằng に: バスに 乗って.
どうやって hỏi cách thực hiện hoặc sử dụng máy.
どれ đứng độc lập để hỏi quyển nào; どの cần danh từ đi sau. ''',
 17: '''待ちます thuộc nhóm I, ち đổi thành た trước ない: 待たない.
借ります thuộc nhóm II, bỏ ます thêm ない: 借りない.
忘れないで ください là “xin đừng quên”; ないで nối phủ định với lời nhờ.
Vなければ なりません diễn đạt nghĩa vụ phải làm.
飲まなくても いいです nghĩa là không uống cũng được, tức không cần uống.
Đưa 新聞を lên làm chủ đề thì を được thay bằng は: 新聞は.
あしたまでに là hạn chót phải trả xong muộn nhất ngày mai.
6時まで diễn đạt làm việc kéo dài tới 6 giờ; までに chỉ hạn hoàn thành. ''',
}


def main():
    result = []
    stats = {'lessons': 17, 'questions_read': 0, 'ai_answered': 0, 'issues': 0}
    for lesson in range(1,18):
        doc = json.loads((ROOT / 'normalized' / f'lesson-{lesson:02}' / 'grammar.json').read_text(encoding='utf-8'))
        questions = [(p,q) for p in doc['points'] for q in p['questions']]
        keys = KEYS[lesson].split()
        assert len(keys)==len(questions), (lesson,len(keys),len(questions))
        notes = [x.strip() for x in EXPL[lesson].strip().splitlines()]
        assert len(notes)==len(questions), (lesson,len(notes),len(questions))
        for (point,question),key,note in zip(questions,keys,notes):
            stats['questions_read'] += 1
            source_id = question['id']
            if key=='X':
                assert note=='X'
                issue=ISSUES[(lesson,source_id)]
                result.append({'lesson':lesson,'source_id':source_id,'issue':issue})
                stats['issues']+=1
                continue
            assert any(c['id']==key for c in question['choices'])
            assert note!='X'
            result.append({'lesson':lesson,'source_id':source_id,'correct':key,
                           'explanation_vi':note,
                           'provenance':{'answer':'ai_editorial_inference','explanation':'ai_authored','human_review':'pending'}})
            stats['ai_answered']+=1
    path=ROOT/'authored'/'quick-checks'/'keys-01-17.json'
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'reports'/'quick-checks-01-17.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(stats)


if __name__=='__main__':
    main()
