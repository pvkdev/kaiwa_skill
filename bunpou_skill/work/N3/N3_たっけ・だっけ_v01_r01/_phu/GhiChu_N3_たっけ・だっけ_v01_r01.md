# Ghi chú biên tập – N3_たっけ・だっけ_v01_r01

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: 〜たっけ／だっけ – Hình như là… nhỉ? / Có phải… đúng không nhỉ?
- Cấp độ: N3
- Phiên bản quy tắc: 7.2.0
- Ngày tạo: 2026-11-04
- Công cụ AI / model: Claude Code – Claude Sonnet 5.5

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: 〜たっけ／だっけ – Hình như là… nhỉ? / Có phải… đúng không nhỉ?
- Các dòng cấu trúc trong bài gốc: Động từ thể た + っけ (でしたっけ／ましたっけ lịch sự hơn); Tính từ な／Danh từ + だ／だった + っけ; Tính từ い (bỏ い) + かった + っけ. Phần NÂNG CAO: んだ（った）っけ.
- Gán thẻ cấu trúc: bài chỉ có MỘT cách dùng (①②③ cùng nghĩa: hỏi lại điều từng biết mà quên; ② là biến thể với từ nghi vấn, ③ là ghi chú về mức độ thân mật) nên chỉ có chương 3.1, tiêu đề không đánh số. Bốn thẻ: 1 = V た + っけ, 2 = Aな／N + だ／だった + っけ (gộp だ／だった), 3 = Aい (bỏ い) + かった + っけ, 4 = thể thường + んだ／んだった + っけ (lấy từ phần NÂNG CAO).
- Cách nói thường gặp: bài gốc không có phần này.
- Ghi chú nhỏ đã đưa vào phần Ý nghĩa/Cách chia: thân mật, không dùng với người trên và văn viết (Không dùng khi); dạng lịch sự でしたっけ／ましたっけ／んでしたっけ (Sắc thái, Cách chia); quá khứ だった／でした nhấn mạnh đã nghe trước đó (Sắc thái); từ nghi vấn + だっけ, hỏi người khác hoặc tự hỏi mình (Khi nào dùng, Dấu hiệu nhận biết).

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| 3.1 Hỏi lại điều từng biết mà quên | 24 (22 + 2 NÂNG CAO; 4 cặp trùng → 20 ý khác nhau) | 5 | 1 | 6 |

### Bảng phủ ví dụ

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | 2 | Bài gốc câu 5 (N + だっけ, từ nghi vấn 何時から) |
| 2 | 3.1 | 2 | Bài gốc câu 10 – Aな嫌いだったっけ |
| 3 | 3.1 | 2 | Bài gốc câu 17 (N + でしたっけ, dạng lịch sự) |
| 4 | 3.1 | 1 | Bài gốc câu 20 (V た + っけ, tự hỏi mình) |
| 5 | 3.1 | 4 | Bài gốc NÂNG CAO câu 1 (んだっけ) |
| 6 | 3.1 | 3 | MỚI – bài gốc không có ví dụ Aい + かったっけ |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | Tính từ ~~い~~ + かった + っけ (gạch ngang chữ い) | Aい（bỏ い）＋ かった ＋ っけ | Làm rõ cách chia: bỏ い rồi thêm かった |
| 2 | 明日の テスト は何時からだっけ ? (khoảng trắng thừa, dấu ? nửa góc) | 明日のテストは何時からだっけ？ | Khoảng trắng thừa và thiếu dấu câu Nhật |
| 3 | これからどこへ行くんだっけ ? | これからどこへ行くんだっけ？ | Dấu ? nửa góc và khoảng trắng thừa |
| 4 | 国へ帰るのは、来週だ（った)っけ ? (câu 1) | 国へ帰るのは、来週だったっけ？ (câu 15) | Câu 1 và 15 trùng; dùng bản sạch, bỏ ngoặc |
| 5 | Ngoặc lệch ở câu 1 "だ（った)っけ" và câu 2 "話（まし）たっけ" | Không dùng hai câu này | Ngoặc không đồng bộ; đã có câu sạch tương ứng |
| 6 | Câu 21: ケン討する (chữ kanji bị thay bằng katakana), "bộ Nhâ (人)" | Không dùng câu này | Phải là 検討; bản dịch cũng gõ sai "Nhân". Lược |
| 7 | Câu 16 dịch "Cậu nói ai đến gặp chúng ta quên rồi?" | Không dùng câu này | Bản dịch lệch nghĩa, khó đọc. Lược |
| 8 | "không dử dụng" | Không dùng trong Kịch bản | Lỗi chính tả "dử" → "dùng" (chỉ nằm ở bài gốc) |

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| Chọn | 明日のテストは何時からだっけ？ | N + だっけ điển hình, có từ nghi vấn |
| Lược | 国へ帰るのは、来週だったっけ？ | Rà soát: dành chỗ cho dạng cấu trúc còn thiếu; không sửa câu Nhật này. |
| Chọn | 今日は何曜日でしたっけ？ | Dạng lịch sự でしたっけ |
| Chọn | あれ、わたし、さっき眼鏡をどこに置いたっけ？ | V た + っけ, tự hỏi mình (lấy câu 20 vì sạch hơn câu 4) |
| Chọn | これからどこへ行くんだっけ？ | Thẻ 4 んだっけ (NÂNG CAO) |
| MỚI | あの店のランチ、安かったっけ？ | Thẻ 3 Aい + かったっけ không có trong bài gốc |
| Lược | 次の祝日っていつだっけ？来週だっけ？ (6) | Trùng dạng N + だっけ đã có |
| Lược | あの人の名前はなんでしたっけ？ (7) | Trùng dạng でしたっけ đã có |
| Lược | あの人、田村さんだっけ？ (8) | Trùng dạng N + だっけ |
| Lược | 彼が何て言ったっけ？ (9) | Trùng dạng V た + っけ |
| Lược | もう手紙出したっけ？ (11) | Trùng dạng V た + っけ |
| Lược | 明日のパーティーのこと、話したっけ？ (12, và câu 2) | Trùng dạng V た + っけ |
| Lược | あなたの誕生日、いつだっけ？ (13) | Trùng dạng N + だっけ |
| Lược | 自己紹介したっけ？ (14) | Trùng dạng V た + っけ |
| Lược | 誰が僕たちに会いに来るって言ったっけ？ (16) | Dịch lệch, trùng dạng V た |
| Lược | 英語の試験は５番教室だっけ。／８番じゃない？ (18) | Đối thoại hai người, có chữ Latin Ａ／Ｂ |
| Lược | 夢を見た日はいつだって言ったっけ？ (19) | Trùng dạng V た + っけ |
| Lược | 「ケン討する」の「ケン」は、キヘンだっけ、ニンベンだっけ。 (21) | Lỗi chữ, phải giảng thêm về bộ thủ |
| Lược | あれ、僕言わなかったっけ？ (22) | Dạng phủ định なかったっけ không có trong cấu trúc gốc |
| Lược | どこに住んでいるんだっけ？ (NÂNG CAO 2) | Trùng thẻ 4 đã có ví dụ |


| Lược sau rà soát | 国へ帰るのは、来週だったっけ？ | Dành chỗ cho dạng còn thiếu, không thay đuôi để ép mẫu. |
| Chọn bổ sung | 君、これ嫌いだったっけ？ | Bài gốc câu 10 – Aな嫌いだったっけ |

## 4. Quyết định đã tự đưa ra

- Kiểm tra chéo mở màn 7.2.0: Sơn từng biết tên thầy nhưng nhất thời quên, hỏi đồng nghiệp là đúng. Bỏ tên Takeshi ở kết vì câu chuyện chỉ cần vai thầy, không cần tên ngoài phạm vi được giới thiệu.

- Bài chỉ có MỘT cách dùng: chương `## 3.1 Cách dùng: …` không số; lời giảng mục 2 chỉ nói "cách dùng", không nói số cách dùng.
- Phần NÂNG CAO "んだ（った）っけ" gộp thành Cấu trúc 4; phần NÂNG CAO 2 (quá khứ nhấn mạnh đã nghe) đưa vào dòng Sắc thái và Ví dụ 2. Không tách chương riêng vì cùng một nghĩa.
- Gộp だ／だった vào Cấu trúc 2 vì cùng chia (Aな／N). Lịch sự でしたっけ／ましたっけ ghi trong ngoặc ở thẻ.
- Dòng Tô màu: V た dùng `たっけ`, N／Aな dùng `だっけ`／`だったっけ`／`でしたっけ`, Aい dùng `かったっけ`, んだ dùng `んだっけ` (chép đoạn liền có thật trong câu).
- Dịch lại Việt cho tự nhiên: dùng "mình" thay "tôi"; thêm "ấy nhỉ" để giữ sắc thái nhớ lại.
- Nhân vật: giữ gợi ý (Sơn, y tá, phụ là thầy Takeshi). Điều chỉnh nhỏ: Takeshi là thầy giáo cũ của Sơn đến khám, hợp với bối cảnh phòng khám và đúng mẫu "quên tên người". Các ví dụ dùng người khác (Linh, Hiếu, bác Khoa, bà Lan, Tuấn, chị Thảo).
- Ví dụ [MỚI] (Aい): tự viết câu ngắn あの店のランチ、安かったっけ？ – tự nhiên, từ vựng N5–N4, dạng đã nghe giá nhưng quên.
- Bẫy 1 (giống hình thức): だっけ và だけ. Bẫy 2 (gần nghĩa): hỏi điều mình chưa từng biết thì dùng câu hỏi thường (これは何ですか？). Cả hai đều chắc chắn đúng.
- Mục 5 có "Tình huống thực tế" (3 dòng) và "Người Nhật thường nói" (えーと、何だっけ？／あれ、何しに来たんだっけ？ – hai câu cửa miệng thật).
- Tên riêng Latin (Takeshi) chỉ xuất hiện trong phần tiếng Việt.

- Rà soát trước sản xuất ngày 2026-11-04: Bổ sung lời giảng cụ thể cho ví dụ 3, 4, 5, 6, bảo đảm tình huống và cách ghép đủ ít nhất 60 từ tiếng Việt khi bỏ câu Nhật; giữ nguyên câu Nhật và nghĩa đã chọn.

- Rà soát trước sản xuất ngày 2026-11-04: Ưu tiên câu gốc 10 君、これ嫌いだったっけ？ để phủ Aな đã bị lược nhầm; thay lựa chọn N来週だったっけ lặp dạng. Vẫn năm ví dụ gốc và một [MỚI] Aい, không viết lại câu Nhật gốc.

- Rà soát trước sản xuất ngày 2026-11-04: Chuẩn hóa nhãn dạng trong Cách ghép theo đúng thẻ được minh họa và đối chiếu lại tô màu Việt với bản dịch.

- Rà soát mở màn 7.2.0: Điều hỏi là tên từng biết rồi quên nhất thời, không phải hỏi thông tin lần đầu; chi tiết bị gọi lên bảng tăng tự nhiên và hài nhẹ. Giữ nguyên câu Nhật và nội dung ví dụ.

## 5. Kết quả kiểm tra

- Tự thẩm định trước sản xuất ngày 2026-11-04: đã soát 6 ví dụ (1 [MỚI]), 4 thẻ cấu trúc, câu mẫu, bẫy và câu kết; đối chiếu nghĩa, cách ghép, thứ tự, bảng phủ, tên gọi và sự tự nhiên. Những câu Nhật được giữ lại không bị viết lại.
- validate.py: ĐẠT – 0 lỗi, 0 cảnh báo.
- Cảnh báo được giữ lại và lý do: Không có.

- QA toàn bộ N3/N2/N1 ngày 2026-11-04: đã rà nội dung, độ phủ thực, bản dịch, phần tô màu, tên nhân vật và bộ file; kết quả kiểm tra kỹ thuật thực tế đã ghi trong mục này.
- Tự thẩm định mở màn 7.2.0: đã đối chiếu diễn biến, nhu cầu phát ngôn, sắc thái mẫu và câu Nhật kết; lời kể tự nhiên, không liệt kê đặc điểm tạo ảnh.
- Kiểm tra chéo mở màn 7.2.0: đã đối chiếu độc lập tình huống, ý muốn nói, thời điểm, sắc thái, phần nối và câu kết; các điểm cần chỉnh đã xử lý.
