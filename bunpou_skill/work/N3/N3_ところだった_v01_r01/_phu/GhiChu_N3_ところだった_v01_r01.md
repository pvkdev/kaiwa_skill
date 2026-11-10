# Ghi chú biên tập – N3_ところだった_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜ところだった – Suýt nữa thì…, suýt chút nữa là…
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Claude Code – Claude Sonnet 5.5

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜ところだった – Suýt nữa thì…, suýt chút nữa là…
- Các dòng cấu trúc trong bài gốc: Động từ thể từ điển (Vる) + ところだった; Động từ thể ない + ところだった.
- Gán thẻ cấu trúc: bài chỉ có một cách dùng (các ①②③ của bài gốc cùng nói về nghĩa "suýt xảy ra nhưng không xảy ra"), nên chỉ có chương 3.1 không đánh số. Thẻ 1 = Vる, thẻ 2 = Vない (giữ đúng hai dòng của bài gốc, không gộp).
- Ý ② (đi kèm もう少しで／もうちょっとで／危うく) đưa vào Sắc thái và Dấu hiệu nhận biết; ý ③ (không dùng cho hiện tượng tự nhiên, chuyện không tránh được) đưa vào Không dùng khi.
- Cách nói thường gặp: không có (bài gốc không có phần này).

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Suýt xảy ra nhưng rốt cuộc không xảy ra | 19 | 6 | 0 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 1 | Bài gốc câu 1 (Vる, もう少しで) |
| 2 | 3.1 | 1 | Bài gốc câu 3 (Vる, quên hẹn) |
| 3 | 3.1 | 1 | Bài gốc câu 4 (thể khả năng Vる, chuyện tốt suýt thành, のに) |
| 4 | 3.1 | 2 | Bài gốc câu 10 (Vない: 買えないところだった) |
| 5 | 3.1 | 1 | Bài gốc câu 15 (あやうく, chuyện nguy hiểm, bị động nối て) |
| 6 | 3.1 | 1 | Bài gốc câu 17 (thể bị động Vる, 〜たら) |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | 危なく〜ところだった (ở ý ②) | 危うく／あやうく〜ところだった | Từ đi cùng mẫu này là 危うく／あやうく, không phải 危なく |
| 2 | 駅の ホーム で押されて | 駅のホームで押されて | Khoảng trắng thừa trong câu Nhật (ví dụ 5) |
| 3 | もう少しで １００点取れる | もう少しで１００点取れる | Khoảng trắng thừa trong câu Nhật (ví dụ 3) |
| 4 | Dịch "ngã vào làn đường sắt" (câu 15) | "rơi xuống đường ray" | 線路に落ちる = rơi xuống đường ray; dịch cho đúng nghĩa |
| 5 | Dịch "vé xem phim sắp tới" (câu 10) | "vé xem phim" | 映画の予約券 không có nghĩa "sắp tới" |
| 6 | "hômሁ nay" (câu 3, bản dịch) | "hôm nay" | Ký tự lạ lẫn vào chính tả tiếng Việt |
| 7 | "Tiếc quá… chỉ được 97 điểm" (câu 4) | "Tiếc quá. Suýt nữa là được 100 điểm rồi mà, chỉ được 97 điểm." | Chỉnh dấu câu cho rõ ý, không đổi nghĩa |

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | もう少しで遅刻するところだった。 | Câu điển hình nhất, có もう少しで |
| Chọn | あ、今日は１５日だった。うっかり約束を忘れるところだった。 | Chuyện quên, nhẹ nhõm, đời thường |
| Chọn | 残念だ。もう少しで１００点取れるところだったのに、９７点だった。 | Sắc thái tiếc nuối, のに |
| Chọn | 切符売り場に来るのがもう少し遅かったら、映画の予約券が買えないところだった。 | Duy nhất có dạng Vない, phủ thẻ cấu trúc 2 |
| Chọn | 駅のホームで押されて、あやうく線路に落ちるところだった。 | Có あやうく, chuyện nguy hiểm, dễ dựng tình huống |
| Chọn | 彼女が注意してくれなかったら、だまされるところだった。 | Thể bị động, có vế 〜たら nêu lý do thoát nạn |
| Lược | 2 あと少しで合格するところだったのに… | Trùng sắc thái tiếc nuối với câu 4, dạng giống nhau |
| Lược | 5 誤解がもとで…失うところだった | Câu dài, trùng chuyện xấu suýt xảy ra |
| Lược | 6 考えごとをしながら…ぶつかるところだった | Trùng kiểu "suýt tai nạn" với câu 15 |
| Lược | 7 留年になるところだったが… | Câu dài, vế sau phức tạp |
| Lược | 8 危うく溺れ死ぬところだった。 / 9 危うく川に落ちるところだった。 / 13 あやうく大けがをするところだった。 / 14 あやうく追突するところだった | Câu ngắn nhưng trùng dạng với câu 1 và câu 15 |
| Lược | 11 もう少しで新幹線の発車に間に合わなくなるところだった。 | Trùng ý "suýt muộn" với câu 1 |
| Lược | 12 あやうく大事故になるところだったが… | Trùng ý với câu 15 |
| Lược | 16 もう少しでさいふを忘れるところだった。 | Trùng ý "quên đồ" với câu 3 |
| Lược | 18 あと少しで書き終わるところだったのに… | Trùng sắc thái tiếc nuối với câu 4 |
| Lược | 19 高橋選手は…正選手になれるところだったのだが… | Câu dài, trùng sắc thái tiếc nuối |

## 4. Quyết định đã tự đưa ra

- Bài chỉ có một cách dùng nên tiêu đề là `## 3.1 Cách dùng: …` không số, lời giảng không nói "cách dùng 1" hay "mấy cách dùng".
- Giữ hai thẻ cấu trúc đúng như bài gốc (Vる và Vない), không gộp; thẻ 2 chỉ có 1 ví dụ bài gốc (câu 10: 買えない), đủ phủ thẻ nên không viết [MỚI].
- Không viết ví dụ [MỚI]: bài gốc đủ 19 câu, chọn 6 câu.
- Dòng Tô màu luôn chỉ là ところだった (liền nhau); もう少しで／あやうく nằm ở đầu câu, tách rời mẫu nên không tô, chỉ nhắc ở phần Cách ghép.
- Giữ chữ số toàn góc １５, １００, ９７ như bài gốc trong câu Nhật.
- Hai bẫy "giống hình thức": 〜ところだ (sắp làm) và 〜たところだ (vừa làm xong); cả hai câu mẫu đều là câu đời thường chắc chắn.
- Phần "Người Nhật thường nói" chọn 2 câu cửa miệng chắc chắn tự nhiên; "Tình huống thực tế" viết ngắn.
- Nhân vật mục 1 và câu Kết: dùng gợi ý Sơn, nhân vật phụ Takeshi, bối cảnh khách sạn. Điều chỉnh nhẹ để hợp ngữ pháp và ngoại hình vest nhăn: Sơn đi làm phù rể ở khách sạn; Takeshi là nhân viên soát thiệp mời ở cửa phòng tiệc (thay cho "soát vé").
- Các ví dụ dùng nhân vật khác nhau: Lan, Hùng, Mai, Hà, Dũng, Quân.
- Câu mẫu trong phần Ý nghĩa tự viết: 階段で転ぶところだった。

- Rà soát mở màn 7.2.0: Khẳng định đến trước giờ lễ để sự kiện trễ rốt cuộc không xảy ra, đúng ところだった. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định: đã soát 6 câu ví dụ, 1 câu mẫu, 2 câu bẫy, 2 câu người Nhật thường nói, câu kết; không phải thay câu nào.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: không có

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
