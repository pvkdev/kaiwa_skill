"""Reviewed quickcheck answer key for Minna lessons 18–34."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANSWERS = """
18|dictionary-form-1|1|歌います là nhóm I; đổi âm trước ます từ い sang う để được 歌う.
18|dictionary-form-2|0|見ます là nhóm II; bỏ ます rồi thêm る thành 見る.
18|dekimasu-1|2|Danh từ chỉ kỹ năng 英語 đi với ができます.
18|dekimasu-2|0|Trước ことができます dùng động từ thể từ điển 読む; を của 本 được giữ.
18|shumi-1|1|読む được danh từ hóa bằng こと trước です để nói sở thích.
18|maeni-1|2|Trước まえに, động từ dùng thể từ điển 食べる.
18|time-maeni-1|0|Khoảng thời gian 2時間 đứng trực tiếp trước まえに; 2時 là mốc hai giờ.
18|nakanaka-1|2|なかなか đi với phủ định できません để nói mãi vẫn chưa làm được.
18|zehi-1|1|ぜひ nhấn mạnh mong muốn tha thiết trong lời mời 遊びに来てください.
19|the-ta-1|1|待ちます thuộc nhóm I đuôi ち; thể た đổi thành った: 待った.
19|the-ta-2|2|泳ぎます thuộc nhóm I đuôi ぎ; thể た đổi thành いだ: 泳いだ.
19|kinh-nghiem-1|0|Mẫu kinh nghiệm dùng Vたことがあります; 読む đổi thành 読んだ.
19|kinh-nghiem-2|1|Hôm qua là một lần cụ thể, nên kể bằng 行きました thay vì mẫu kinh nghiệm.
19|tari-tari-1|2|きのう đặt sự việc ở quá khứ nên kết thúc bằng しました.
19|tari-tari-2|0|Vたり liệt kê vài việc tiêu biểu, không khẳng định thứ tự hay đầy đủ mọi việc.
19|narimasu-1|1|Tính từ い 暑い bỏ い thêm く trước なります: 暑くなります.
19|narimasu-2|2|Danh từ 先生 đi với に trước なります: 先生になります.
20|chon-loi-noi-1|1|Mới gặp đồng nghiệp dù cùng tuổi vẫn nên dùng lối lịch sự です／ます.
20|dong-tu-thong-thuong-1|2|来ませんでした đổi sang phủ định quá khứ thông thường là 来なかった, đọc こなかった.
20|dong-tu-thong-thuong-2|0|Dạng thông thường phủ định của あります là ない.
20|tinh-tu-i-1|1|いい đổi gốc thành よ trước dạng quá khứ: よかった.
20|tinh-tu-i-2|2|安い bỏ い rồi thêm くなかった để được 安くなかった.
20|tinh-tu-na-danh-tu-1|0|Danh từ 先生でした ở thể thường quá khứ khẳng định là 先生だった.
20|tinh-tu-na-danh-tu-2|1|きれい là tính từ な; làm vị ngữ thể thường hiện tại là きれいだ.
20|mau-da-hoc-1|2|食べてもいいです bỏ です ở cuối để thành 食べてもいい.
20|mau-da-hoc-2|0|Vたことがない diễn tả chưa từng có kinh nghiệm làm việc đó.
20|hoi-dap-than-mat-1|1|Câu hỏi danh từ thân mật trung tính có thể bỏ ですか và lên giọng: 学生？
20|hoi-dap-than-mat-2|2|ううん là cách đáp phủ định thân mật tương ứng いいえ.
20|luoc-trong-hoi-thoai-1|0|Trong khẩu ngữ, ている thường rút thành てる: 待ってる.
20|kedo-1|1|Tính từ い 安い nối trực tiếp với けど: 安いけど.
21|to-omoimasu-1|1|Trước と 思います dùng thể thường; 降る là dạng từ điển của 降ります.
21|y-kien-1|2|について đánh dấu chủ đề được hỏi ý kiến: Nについてどう思いますか.
21|to-iimasu-1|0|母 là người nghe lời nói nên gắn trợ từ に: 母に言いました.
21|deshou-1|1|Tính từ な 静か đứng trước でしょう mà không thêm だ hay です.
21|su-kien-de-1|2|Bữa tiệc diễn ra tại công ty nên địa điểm sự kiện dùng 会社で.
21|dip-de-1|0|Trong パーティーで, で chỉ dịp hoặc bối cảnh gặp bạn.
21|demo-1|1|Nでも gợi ý một lựa chọn nhẹ, ở đây là trà hoặc thứ tương tự.
21|nai-to-1|2|帰らないと lược vế sau như いけない; người nói phải về.
22|bo-nghia-danh-tu-1|1|Mệnh đề bổ nghĩa dùng thể thường 読んだ đặt ngay trước 本.
22|chu-ngu-ga-1|2|Chủ ngữ 兄 trong mệnh đề bổ nghĩa đứng với が: 兄が使っている.
22|vai-tro-cum-danh-tu-1|0|Cả cụm 兄が買ったパソコン là tân ngữ của 使います nên dùng を.
22|nhan-dien-nguoi-1|1|セーター là áo mặc trên thân, đi với 着ます.
22|jikan-yakusoku-youji-1|2|Động từ bổ nghĩa cho 時間 dùng thể từ điển: 電話をする時間.
22|mashouka-1|0|行きましょうか rủ người nghe cùng đi: Chúng ta đi nhé?
23|toki-1|1|Tính từ い đứng trực tiếp trước とき: 忙しいとき.
23|toki-2|0|Danh từ 学生 nối với とき bằng の: 学生のとき.
23|ru-ta-toki-1|2|Việc đến Paris đã hoàn tất trước khi mua túi nên dùng 行ったとき.
23|ru-ta-toki-2|1|Dạng trước とき phụ thuộc thứ tự hai việc, không chỉ vào thì của câu chính.
23|dieu-kien-to-1|0|Điều kiện lặp hoặc kết quả tự nhiên dùng thể từ điển 押す trước と.
23|dieu-kien-to-2|2|水が出ます là kết quả tự nhiên khi thực hiện điều kiện ở vế trước.
23|ga-tinh-tu-1|1|Âm thanh được mô tả bằng 音が小さいです, dùng が cho chủ ngữ.
23|wo-di-chuyen-1|0|Con đường đi qua là この道を歩きます; を đánh dấu lộ trình.
24|kuremasu-1|0|Bạn cho tôi áo nên dùng くれました từ góc nhìn người nhận.
24|kuremasu-2|1|Trong 先生は弟に本をくれました, 弟 là người nhận sách.
24|te-agemasu-1|2|Nhờ giúp thầy nên đề nghị 手伝いましょうか; てあげます có thể thiếu lịch sự với thầy.
24|te-moraimasu-1|1|兄に直してもらいました nghĩa là anh trai làm việc sửa máy cho tôi.
24|te-kuremasu-1|2|兄 là người làm giúp người nói nên dùng くれました.
24|chu-de-va-chu-ngu-1|0|Từ hỏi だれ là chủ ngữ của 直してくれました nên dùng が.
24|chu-de-va-chu-ngu-2|1|Khi cuốn sách đã rõ, có thể lược この本は và giữ 姉がくれました.
25|tara-dieu-kien-1|2|いい dùng gốc よい khi chia たら: よかったら.
25|tara-dieu-kien-2|0|Nếu có thời gian là 時間があったら; vế sau là lời rủ.
25|tara-thoi-diem-1|1|帰ったら chỉ sau khi về đến nhà; sau đó mới tắm.
25|temo-1|1|Vない đổi ない thành なくても: 行かなくても.
25|temo-2|2|高くても là dù đắt, vế sau vẫn quyết định mua.
25|moshi-1|0|あったら vẫn thể hiện điều kiện dù bỏ từ nhấn mạnh もし.
25|ga-menh-de-phu-1|2|友達 là chủ ngữ trong mệnh đề điều kiện nên dùng が.
26|cach-noi-ndesu-1|1|Tính từ な 静か cần な trước んです: 静かなんです.
26|hoi-ndesuka-1|0|Thể thường 降っている nối trực tiếp với んですか để hỏi có bối cảnh.
26|giai-thich-ndesu-1|2|忙しい ở quá khứ là 忙しかった; thêm んです để giải thích.
26|mo-loi-ndesuga-1|0|が nối lời nêu hoàn cảnh với lời nhờ ở phía sau.
26|te-itadakemasenka-1|1|いただけませんか đi sau động từ thể て: 言っていただけませんか.
26|tara-ii-1|2|行く đổi thể た thành 行った rồi thêm らいいですか.
26|doi-tuong-wa-1|1|Đưa 時間 lên chủ đề bằng は, thay vị trí của が: 時間はあります.
27|chia-kha-nang-1|2|泳ぎます nhóm I đổi âm ぎ sang げ rồi thêm ます: 泳げます.
27|cau-kha-nang-1|0|この店 là nơi dùng thẻ, nên dùng địa điểm hành động で.
27|mieru-kikoeru-1|1|Âm thanh tự lọt đến tai dùng 聞こえます và chủ ngữ 音が.
27|dekimasu-hoan-thanh-1|2|Bữa tối đã làm xong dùng 晩ごはんができました.
27|shika-1|0|しか phải đi với dạng phủ định 書けません.
27|wa-doi-chieu-1|1|は đặt sau cả 肉 và 魚 để đối chiếu hai đối tượng.
27|wa-sau-tro-tu-1|2|からは kết hợp trợ từ chỉ điểm xuất phát với は để nhấn mạnh từ đây.
28|nagara-1|1|飲みます bỏ ます lấy thân 飲み, thêm ながら.
28|teimasu-thoi-quen-1|2|Thói quen trong quá khứ dùng 飲んでいました.
28|shi-liet-ke-1|0|丈夫 là tính từ な; dạng thể thường trước し là 丈夫だし.
28|shi-ly-do-1|1|Tính từ い 安い nối trực tiếp với し: 安いし.
28|soreni-1|2|それに thêm một ưu điểm cùng hướng với điều vừa nói.
28|sorede-1|0|それで tiếp nhận lý do vừa nghe rồi nêu kết quả được ưa chuộng.
28|toki-tro-tu-1|1|Đưa cả cụm 勉強するとき lên chủ đề thì thêm は.
29|trang-thai-1|1|消える là tự động từ; 消えています mô tả trạng thái đèn đã tắt.
29|trang-thai-2|2|Chiếc ghế này là chủ đề câu nên dùng このいすは.
29|hoan-tat-1|0|食べてしまいます nói sẽ làm cho xong việc ăn hết.
29|hoan-tat-2|1|Ngữ cảnh đọc hết sách nhấn mạnh sự hoàn tất, không nhất thiết hối hận.
29|tiec-nuoi-1|2|なくしてしまったんです là dạng quá khứ thể thường trước んです để giải thích việc lỡ mất hộ chiếu.
29|noi-den-ni-1|0|Đích đến 交番に行きます có thể thay に bằng へ.
29|nhac-lai-noi-dung-1|1|その bổ nghĩa trực tiếp cho 本 đã được nhắc đến.
29|tim-thay-1|2|ありました trong lúc tìm đồ diễn tả đã thấy món đồ cần tìm.
29|dokoka-1|0|Nơi xảy ra hành động đánh rơi vé là どこかで.
30|te-arimasu-1|1|閉める là tha động từ; 窓が閉めてあります nhấn mạnh kết quả có chủ ý.
30|te-arimasu-2|2|Trong mẫu trạng thái 手紙が入れてあります, 手紙 là vật được đặt sẵn.
30|chuan-bi-truoc-1|0|予約しておきます diễn tả đặt phòng trước để chuẩn bị.
30|thu-xep-sau-khi-dung-1|1|Sau khi しまって cần おいてください trong mẫu Vておく.
30|giu-nguyen-1|2|そのままにしておいてください là mẫu nhờ để nguyên.
30|mada-1|0|まだ với 降っています khẳng định nghĩa là trời vẫn đang mưa.
30|toka-1|1|N1とかN2とか liệt kê vài ví dụ như là trong hội thoại.
30|tro-tu-mo-1|2|で kết hợp も thành でも để nói ở thư viện cũng học.
31|chia-the-y-chi-1|1|泳ぎます nhóm I đổi ぎ sang ご, thêm う: 泳ごう.
31|chia-the-y-chi-2|0|見ます nhóm II bỏ ます rồi thêm よう: 見よう.
31|ru-va-de-nghi-1|2|手伝おうか là thể ý chí cộng か, lời đề nghị thân mật để mình giúp.
31|you-to-omotteimasu-1|1|Trước と思っています dùng thể ý chí 続けよう.
31|tsumori-1|0|Ý định không mua dùng Vないつもりです: 買わないつもりです.
31|yotei-1|2|Danh từ thời gian 来週 gắn の trước 予定: 来週の予定です.
31|mada-teimasen-1|1|Phủ định của まだ dùng Vていません: まだ送っていません.
31|danh-tu-than-masu-1|0|帰り là danh từ chỉ lượt về trong cụm 帰りの電車.
32|houga-ii-1|1|Lời khuyên nên làm dùng Vたほうがいい: 持ったほうがいい.
32|houga-ii-2|0|Lời khuyên tránh làm dùng Vないほうがいい: 吸わないほうがいい.
32|deshou-1|2|Danh từ 休み nối trực tiếp でしょう, không có だ hoặc な.
32|deshou-2|0|でしょうか là đuôi hỏi phỏng đoán một cách mềm mại.
32|kamoshiremasen-1|1|Tính từ い 難しい nối trực tiếp かもしれません.
32|kamoshiremasen-2|2|かもしれません diễn tả khả năng, không phải điều chắc chắn.
32|mashou-nhan-lam-1|0|Người thợ tự nhận kiểm tra máy nên 調べましょう là để tôi kiểm tra.
32|luong-tu-de-1|1|千円で đánh dấu giới hạn giá tiền để mua được.
32|nanika-koto-1|2|何かおいしいもの là một thứ gì đó ngon; おいしい bổ nghĩa cho もの.
33|menh-lenh-1|1|急ぎます nhóm I đổi ぎ sang げ để thành mệnh lệnh 急げ.
33|menh-lenh-2|0|くれます có mệnh lệnh đặc biệt là くれ.
33|cam-chi-1|2|Cấm chỉ dùng thể từ điển する cộng な: するな.
33|ngu-canh-menh-lenh-1|0|頑張れ là lời hô thúc giục, phù hợp cổ vũ thi đấu.
33|nasai-1|2|読 みます lấy thân 読み rồi thêm なさい: 読みなさい.
33|yomu-kaku-1|1|Nội dung ghi trên biển được trích bằng と trước 書いてあります.
33|toiu-imi-1|0|どういう意味ですか hỏi một ký hiệu có nghĩa như thế nào.
33|to-itte-imashita-1|2|Danh từ/tính từ な ở vị ngữ thể thường cần だ: 元気だと言っていました.
33|to-itte-imashita-2|1|帰りました đổi sang thể thường quá khứ 帰った trước と言っていました.
33|to-tsutaete-1|0|Người nhận lời nhắn 佐藤さん đi với に trước 伝える.
34|toori-ni-1|1|Danh từ 説明書 nối với とおりに bằng の: 説明書のとおりに.
34|toori-ni-2|ISSUE|見たとおりに là đáp án giáo trình, nhưng 見ましたとおりに cũng có thể dùng trong văn cảnh trang trọng; đề chưa giới hạn văn phong nên có hai dạng có thể chấp nhận.
34|ato-de-1|0|Vたあとで diễn tả sau khi hoàn tất mua sắm: したあとで.
34|ato-de-2|1|Danh từ 仕事 nối với あとで bằng の: 仕事のあとで.
34|te-naide-1|2|食べないで diễn tả không ăn sáng mà đi học.
34|naide-lua-chon-1|0|買わないで、借ります diễn tả không mua mà mượn.
"""


def main():
    selected = {}
    for raw in ANSWERS.strip().splitlines():
        lesson, sid, choice, explanation = raw.split("|", 3)
        key = (int(lesson), sid)
        assert key not in selected, key
        selected[key] = (choice, explanation)
    records = []
    for lesson in range(18, 35):
        data = json.loads((ROOT / f"normalized/lesson-{lesson:02d}/grammar.json").read_text(encoding="utf-8"))
        for point in data["points"]:
            for question in point.get("questions", []):
                key = (lesson, question["id"])
                assert key in selected, key
                choice, explanation = selected.pop(key)
                assert explanation.strip(), key
                if choice == "ISSUE":
                    records.append({"lesson": lesson, "source_id": question["id"], "issue": explanation})
                else:
                    ids = {option["id"] for option in question["choices"]}
                    assert choice in ids, key
                    records.append({"lesson": lesson, "source_id": question["id"], "correct": choice, "explanation_vi": explanation})
    assert not selected, selected
    assert len(records) == 137, len(records)
    output = ROOT / "authored/quick-checks/keys-18-34.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(records)} reviewed: {sum('correct' in r for r in records)} keys, {sum('issue' in r for r in records)} issues")


if __name__ == "__main__":
    main()
