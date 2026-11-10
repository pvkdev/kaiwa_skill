# Ghi chú biên tập – N3_te-kara-denaito-te-kara-denakereba

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜てからでないと／てからでなければ – Chưa làm A thì chưa thể B
- Cấp độ: N3
- Phiên bản quy tắc: 6.2.0
- Ngày tạo: 2026-11-02
- Công cụ AI / model: Codex – GPT-6

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜てからでないと／てからでなければ – Chưa làm A thì chưa thể B.
- Các dòng cấu trúc trong bài gốc, chỉ chuẩn hóa ký hiệu:
  - Vてから ＋ でないと、〜
  - Vてから ＋ でなければ、〜
- Hai biến thể cùng một nghĩa nên gộp một cách dùng: phải hoàn thành bước A trước; chưa A thì B không làm được, không được phép, khó thực hiện hoặc xảy ra điều bất lợi. Không tách “phủ định” và “hậu quả xấu” thành hai cách dùng.
- Gán thẻ cấu trúc: giữ hai thẻ đúng hai dòng gốc. Thẻ 1 là Vてから ＋ でないと; thẻ 2 là Vてから ＋ でなければ. Khi chia nói rõ Vて chính là động từ đã chuyển sang thể て; không gắn thêm một て sau dạng kết thúc bằng で như 読んで.
- Bài gốc đánh số 20 mục; chỉ 18 mục chứa mẫu. Mục 3 là lời nhân viên dẫn vào lời khách ở mục 4; mục 17 là lời rủ dẫn vào câu trả lời ở mục 18. Chúng không phải hai ví dụ ngữ pháp độc lập.
- Gán toàn bộ 18 câu có mẫu vào phần 3.1; chọn mục gốc 1, 6, 7, 8, 11, 13, đúng thứ tự. Hai đoạn hội thoại không được chọn nên không cần mang lời dẫn vào Kịch bản.
- Cách nói thường gặp: không có cụm riêng trong bài gốc; không tạo chương cụm mới.
- Chuẩn bị Ý nghĩa: hình ảnh cửa có chốt, A là bước mở chốt. Chưa mở thì chưa đi tiếp, hoặc cố bỏ bước sẽ có rắc rối. Diễn đạt “chỉ sau khi” phải giữ ý điều kiện cần, không hứa cứ A xong là B chắc chắn xảy ra. Vế sau có thể mang nghĩa bất lợi nhưng hình thức khẳng định như 失敗する／心配だ.
- Đối chiếu với bài giảng gốc của [J-nihongo](https://j-nihongo.com/n2-index-0222fd5357/) về hành động chuẩn bị cần thiết và kết quả phủ định; đối chiếu [日本語教員プラネット](https://nihongokyoin-planet.com/oshiekata/chukyu-kara-manabu/11) về dạng Vた上で. Chỉ tra cứu để thẩm định, không lấy câu ví dụ từ bên ngoài.

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Chưa hoàn thành bước trước thì chưa thể làm tiếp | 18 câu có mẫu; 2 mục dẫn thoại | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc mục 1; 洗う → 洗って; vế sau cấm làm 食べてはいけません |
| 2 | 3.1 | 2 | Bài gốc mục 6; 治る → 治って; vế sau khó/không thể 無理だ |
| 3 | 3.1 | 1 | Bài gốc mục 7; 確かめる → 確かめて; hậu quả bất lợi 失敗する |
| 4 | 3.1 | 2 | Bài gốc mục 8; もらう → もらって; không thể đăng ký 申し込めない |
| 5 | 3.1 | 1 | Bài gốc mục 11; 洗う → 洗って; lo ngại 心配だ, không có đuôi phủ định |
| 6 | 3.1 | 1 | Bài gốc mục 13; 相談する → 相談して; chưa thể quyết định 決められません |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | Mục 4: “Vì hơi đắt… chưa thể quyết định mua được” | “Vì là món đồ đắt tiền… chưa thể quyết định có mua hay không” | 高いもの nói đồ đắt tiền; 買うかどうか là có mua hay không, không phải đã nghiêng về quyết định mua. Câu này bị lược; chỉ ghi lại kết quả thẩm định, không thay bản lưu gốc. |
| 2 | Mục 5: “vẫn không thể lái được xe ô tô” | “không được phép lái ô tô” | 運転してはいけない là cấm/không được phép, không phải không có khả năng lái. Câu này bị lược; ghi nhận lỗi dịch, không thay bản lưu gốc. |
| 3 | Mục 6: “không được vận động mạnh nhé” | “chưa thể vận động mạnh” | 無理だ nhấn không thể/không kham nổi trong hoàn cảnh đó; không tự nó là mệnh lệnh cấm. Áp dụng ở Ví dụ 2. |
| 4 | Mục 8: “chưa xin phép bố mẹ” | “chưa được bố mẹ cho phép” | 許可をもらう là đã nhận được sự cho phép, không chỉ mới hỏi xin. Áp dụng ở Ví dụ 4. |
| 5 | Đoạn ④ gọi chung 上で và diễn giải cả hai như điều kiện tuyệt đối “nếu không A thì không thể B” | Chỉ rõ Vた上で: làm A xong, dựa vào đó làm B; mẫu chính nhấn việc chưa A cản trở B hoặc gây bất lợi | Tránh đánh đồng các cách dùng của 上で và tránh suy diễn rằng Vた上で tự khẳng định B không thể xảy ra nếu thiếu A. Áp dụng ở Bẫy 2. |

Giữ nguyên văn cả 6 câu Nhật được chọn. Các lỗi dịch ở câu bị lược chỉ được ghi nhận trong nhật ký; bản lưu Bài gốc vẫn nguyên văn.

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn – mục 1 | 手を洗ってからでないと、ご飯を食べてはいけませんよ。 | Thẻ 1, quy định không được làm, bối cảnh dễ hình dung |
| Lược – mục 2 | 歯を磨いてからでないと、キス したくありません。 | Đã đủ 6 câu; ưu tiên kết quả khác nhau và nhiều bối cảnh |
| Dẫn thoại bị lược – mục 3 | 店員:「いかがですか。こちらの絵はすばらしいですよ。」 | Không chứa mẫu, chỉ dẫn vào mục 4 |
| Lược – mục 4 | 客:「う ー ん。高いものなので、家族と相談してからでないと買うかどうかきめられませんね。」 | Đã chọn dạng 相談してからでないと với 決められません ở mục 13, gọn và rõ hơn |
| Lược – mục 5 | 運転免許を取ってからでなければ車を運転してはいけない。 | Ý không được phép đã có mục 1; thẻ 2 đã có hai ví dụ khác sắc thái |
| Chọn – mục 6 | 病気が治ってからでなければ激しい運動は無理だ。 | Thẻ 2, kết quả 無理だ; A là trạng thái thay đổi, không nhất thiết hành động chủ ý |
| Chọn – mục 7 | きちんと確かめてからでないと失敗するよ。 | Thẻ 1, vế sau khẳng định về hình thức nhưng nghĩa bất lợi |
| Chọn – mục 8 | 親の許可をもらってからでなければ、申し込めない。 | Thẻ 2, điều kiện nhận sự cho phép trước khi đăng ký |
| Lược – mục 9 | 証拠を掴んでからでないと、彼を逮捕することはできない。 | Dạng không thể đã có; từ vựng chuyên biệt hơn các câu được chọn |
| Lược – mục 10 | 何事であれ実践してからでなければ、ことの是非は分からない。 | Trừu tượng, khó dựng cảnh hơn; không bổ sung thẻ cấu trúc |
| Chọn – mục 11 | 野菜を生で食べるなら、よく洗ってからでないと、農薬が心配だ。 | Thẻ 1, lo ngại 心配だ cho thấy không bắt buộc đuôi phủ định |
| Lược – mục 12 | 手続きしてからでないと、図書館の本は借りられない。 | Không thể làm tiếp nếu chưa làm thủ tục đã được phủ qua mục 8 |
| Chọn – mục 13 | この件については、上司と相談してからでないと、決められません。 | Thẻ 1, cách nói công sở lịch sự, dạng động từ する |
| Lược – mục 14 | 野村教授には前もって電話してからでないと、お会いできないかもしれません。 | Kính ngữ và phỏng đoán làm phần câu phức tạp hơn; đã đủ 6 câu |
| Lược – mục 15 | 彼の実力を見てからでないと、仕事は任せられない。 | Dạng không thể và quyết định công việc đã có mục 13 |
| Lược – mục 16 | もう少し彼が実務経験を積んでからでないと、この仕事は任せられません。 | Gần ý mục 15; không thêm thẻ cấu trúc |
| Dẫn thoại bị lược – mục 17 | ｢明日、うちへ泊まりにおいでよ。｣ | Không chứa mẫu, chỉ dẫn vào mục 18 |
| Lược – mục 18 | ｢後で返事するよ。お母さんに聞いてからでないと、怒られるから。｣ | Hậu quả bất lợi đã có mục 7; ưu tiên câu một mạch, không cần dẫn thoại |
| Lược – mục 19 | 引っ越してからでなければ、家の周りの様子はわからない。 | Dạng chưa biết trước khi trải nghiệm đã gần mục 10; không thêm thẻ |
| Lược – mục 20 | そのことについては、よく調査してからでなければ、責任ある説明はできない。 | Từ vựng, ý nghĩa trừu tượng hơn; đã có công việc và điều kiện chuẩn bị |

Không có ví dụ [MỚI]. Tổng lược 14 mục được đánh số trong bài gốc: 12 câu có mẫu và 2 lời dẫn thoại.

## 4. Quyết định đã tự đưa ra

- Tạo bài mới output/N3_te-kara-denaito-te-kara-denakereba theo VERSION 6.2.0; dùng khung 3.x và giới thiệu có Mô tả, không dùng mục Tổng quan. Cấp độ N3 giữ đúng yêu cầu, dù một số nơi tra cứu xếp mẫu trong nhóm N2.
- Gộp hai biến thể vào một cách dùng, giữ hai thẻ công thức để dễ nhìn cách nối; không biến các kiểu kết quả thành cách dùng mới.
- Chọn 6 câu gốc 1, 6, 7, 8, 11, 13; không thêm câu [MỚI]. Mỗi biến thể đều có ví dụ. Thể て có cả 洗って、治って、確かめて、もらって、相談して.
- Phân biệt 18 câu có mẫu với hai lời dẫn thoại ở mục 3, 17. Khi báo tổng số lược, tính đủ 14 mục gốc không được đưa vào Kịch bản; trong phân tích ghi riêng 12 câu mục tiêu và 2 lời dẫn.
- Dùng nguyên bộ pick_cast: Linh, thực tập sinh kỹ thuật hay quên đồ, áo hoodie vàng và ba lô to; Ngọc là bạn cùng phòng; tiệm giặt là tự động. Cảnh kiểm tra túi trước khi giặt nối lại ở câu kết.
- Chọn hai bẫy: てから chỉ trình tự thông thường, và Vた上で diễn tả bước chuẩn bị rồi thực hiện. Không thêm cách dùng của 上で vào chương chính.
- Tô màu đúng mẫu てからでないと hoặc てからでなければ. Với 洗って／治って／もらって, không tô thêm っ phía trước て. Giải thích riêng cách chia thể て, không ghi cách đọc và không tô cả động từ.
- Mục 5 thêm ứng dụng đời thường và công việc; bỏ Người Nhật thường nói vì các câu đầy đủ đã đủ minh họa. Phần giảng nhấn điều kiện cần, phân biệt hậu quả bất lợi với hình thức phủ định và không bảo đảm cứ A xong là B xảy ra.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã soát 10 câu Nhật đầy đủ, gồm 6 ví dụ nguyên văn bài gốc, 1 câu mẫu, 2 câu bẫy, 1 câu kết. Đã soát thêm các cụm Nhật trong lời giải thích, bản dịch và các đoạn tô màu. Không phải thay câu Nhật nào sau thẩm định.
- Đối chiếu tự động: 6 câu Nhật khớp nguyên văn Bài gốc ở mục 1, 6, 7, 8, 11, 13 và đúng thứ tự; không có [MỚI]; đủ 2 thẻ cấu trúc. Meta đúng N3, 6.2.0; bài đã có trong output/_index.js.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Đã đọc lại TuyChinh do công cụ sinh: tên cách dùng đúng, đầy đủ 6 ví dụ, 2 thẻ, 2 bẫy; có intro và quy định khung ví dụ luôn đủ câu Nhật cùng câu Việt, không tạo khung chỉ có câu Việt.
- Cảnh báo được giữ lại và lý do: không có.
