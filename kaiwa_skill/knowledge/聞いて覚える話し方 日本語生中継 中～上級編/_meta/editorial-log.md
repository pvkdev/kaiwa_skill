# Hồ sơ biên tập — 日本語生中継 中～上級編

## Phạm vi và trạng thái

- Phạm vi khóa trong book.json: PDF vật lý 1–89, 11 chương theo bìa/mục lục, hướng dẫn, tám bài và hậu ký.
- Đã mở ảnh và đối chiếu nội dung PDF 9–18 với raw snapshot. Chương bài 1 có đủ phạm vi nguồn và đã được tác giả rà lại toàn bài.
- PDF 1–8 đã mở ảnh, đối chiếu raw và clean trong hai chapter đầu. Hồ sơ từng trang và quyết định lọc ở `frontmatter-review.md`.
- Không có audio transcript trong PDF hoặc raw corpus; không tự dựng lời thoại hay đáp án bài nghe.

## Kiểm kê theo thứ tự nguồn

| PDF | Vùng nguồn | Vị trí trong bản clean | Quyết định |
| --- | --- | --- | --- |
| 9 | b001–b002: đầu bài, câu hỏi dẫn, chỉ dẫn khởi động | u-nc01-warmup | Giữ tình huống; sửa đếm ①～⑥ thành năm lời nhắn hiện hữu (xem issue). |
| 9 | b003–b007: năm lời nhắn | u-nc01-warmup | Giữ nguyên câu Nhật, tên riêng, mức độ thân mật/trang trọng; dịch sau vùng trả lời. |
| 9 | b008: năm dòng chọn người nhận và điền chủ đề | u-nc01-warmup | Giữ năm dòng, hai lựa chọn mỗi dòng và chỗ trống. |
| 10 | b001–b004: track, câu hỏi, bảng sáu hàng, hai bộ phương án | u-nc01-listen1-q1 | Giữ thứ tự, nhãn スキット, mọi lựa chọn, blank, track; thêm nghĩa Việt để dùng được. |
| 10 | b005: danh sách từ cho sáu skit | u-nc01-listen1-q1 | Giữ đủ từng từ theo nhóm; dịch Việt. |
| 11 | b001–b007: chỉ dẫn và sáu mẫu phiếu nhắn | u-nc01-listen1-q2 | Chuyển khung giấy thành text; giữ liên hệ người gửi/người nhận/phòng/số điện thoại, blank và thứ tự. Nhãn tiếng Anh trong mẫu được chuyển sang Việt khi không mang chức năng ngôn ngữ Nhật riêng. |
| 12 | b001: câu hỏi 3 và bảng sáu dòng | u-nc01-listen1-q3 | Giữ yêu cầu nghe lại, hai cột ghi cách nói và cách nói thay thế, năm track ghi cạnh bài; không suy track thứ sáu. |
| 12 | b002–b003: track và câu hỏi 1 của luyện nghe II | u-nc01-listen2-q1 | Giữ sáu track, sáu ô trả lời và trường hợp không cần hành động. |
| 13 | b001: danh sách từ cho sáu lời nhắn | u-nc01-listen2-q1 | Giữ theo nhóm, dịch Việt. |
| 13 | b002: câu hỏi 2, sáu cặp a/b | u-nc01-listen2-q2 | Giữ đầy đủ lựa chọn; bản dịch không chỉ ra đáp án. |
| 13 | b003: câu hỏi 3 | u-nc01-listen2-q3 | Giữ yêu cầu thảo luận trong lớp. |
| 13 | b004: point listening, track 16, bảng 3×8 | u-nc01-point-listening | Giữ ba loại người gọi và tám lượt, ô trống. |
| 14 | b001–b003: ba ví dụ và hai nhóm thân mật/trang trọng của 伝言を頼む | u-nc01-request-message | Giữ mọi lượt A/B, từng biến thể cuối câu, tham chiếu 練I và dịch Việt. |
| 14 | b004: hỏi đáp khi nhờ người khác gọi điện sau | u-nc01-request-message | Giữ cả Q/A, hai quan hệ người nghe và toàn ví dụ Nhật. |
| 15 | b001: hai tình huống nhờ chuyển lời | u-nc01-request-message | Giữ yêu cầu tự nói, không tự điền đáp án. |
| 15 | b002–b003: ví dụ và hai nhóm biểu thức của 伝言を申し出る | u-nc01-offer-message | Giữ các biến thể, phân biệt ngữ cảnh. |
| 15 | b004: hai đoạn thoại điền chỗ trống | u-nc01-offer-message | Giữ vai, thứ tự lượt, blank và lời thoại sau blank. |
| 16 | b001–b002: ví dụ và hai nhóm biểu thức của 電話をかけることを申し出る | u-nc01-offer-call | Giữ khác biệt tự gọi/để người khác gọi và mọi biến thể. |
| 16 | b003: hỏi đáp về người thực hiện cuộc gọi | u-nc01-offer-call | Dịch đủ điều kiện công ty và đồng nghiệp. |
| 16 | b004: hai đoạn thoại điền chỗ trống | u-nc01-offer-call | Giữ vai và blank. |
| 17 | b001–b002: ví dụ và hai nhóm biểu thức nhờ người gọi gọi lại | u-nc01-request-callback | Giữ từng biểu thức, sắc thái lịch sự và tham chiếu 練I. |
| 17 | b003: hai hỏi đáp tình huống | u-nc01-request-callback | Giữ cả quy tắc khi gọi vì việc của mình, không chỉ danh sách câu. |
| 17 | b004: hai đoạn thoại điền chỗ trống | u-nc01-request-callback | Giữ vai, thứ tự và blank. |
| 18 | b001–b003: track 2/8 và hai tình huống đóng vai | u-nc01-roleplay | Giữ đề, hai tình huống, quan hệ người nói; không tự viết lời thoại mẫu. |

## Nội dung bỏ khỏi bản học

- Furigana phụ trên PDF 9–13: chỉ là trợ đọc, không phải dữ kiện bài tập.
- Biểu tượng tai nghe/CD và hình ống nghe trang trí: đã chuyển quan hệ chức năng thành nhãn bài và số track; không xuất hình.
- Số trang, đường kẻ, header nhắc lại tên bài và khung trang trí: chỉ phục vụ dàn trang. Tên bài vẫn được giữ ở đầu chương.
- Hình dáng khác nhau của sáu phiếu nhắn: chỉ là kiểu giấy; mọi trường nhập thông tin mang nghĩa đã được giữ bằng text.
- Ký hiệu áo phông/cà vạt ở PDF 14–17: đã chuyển thành nhãn “thân mật”/“trang trọng”; quan hệ của ký hiệu với nhóm câu được giữ.
- Hình hai con mèo cạnh tiêu đề ロールプレイ ở PDF 18: trang trí, không mang dữ kiện bài tập.

## Vấn đề nguồn và quyết định

1. PDF 9 in “①～⑥” nhưng chỉ có lời nhắn và dòng trả lời ①–⑤; raw cũng ghi ①～⑥. Bản clean nói “năm lời nhắn” theo nội dung hiện hữu; không tạo mục ⑥ hoặc đáp án.
2. PDF 12 cạnh 問題3 chỉ in track riêng cho 問い1, 2, 3, 5, 6. Không có nhãn track cho 問い4 ở đó. Bản clean giữ đúng năm track, không suy số còn thiếu.
3. PDF 9 dùng tên 美保子 trong lời nhắn; PDF 13 dùng 美佐子 trong lựa chọn bài nghe khác. Giữ đúng từng tên, không đồng nhất.
4. Bản raw p9 mô tả biểu tượng ống nghe cạnh lời nhắn; đối chiếu ảnh cho thấy chúng không mã hóa lựa chọn hay người nói, nên không mang sang bản học.
5. PDF 14–18 không có transcript của các track và không in đáp án cho các ô bài tập; bản clean giữ đúng phần đề và ví dụ có sẵn.
6. Cụm 「無事チェックインができた」 ở PDF 13 không cho biết đó là check-in khách sạn hay sân bay; bản Việt dùng “làm thủ tục check-in suôn sẻ”, không gán địa điểm.
7. Root QA phát hiện bản Việt của hai cụm 「明日までには」「明日までに」 ở PDF 14–15 từng ghi “trước ngày mai”, làm sớm hạn của nguồn. Đã sửa cả hai thành “chậm nhất vào ngày mai” và checkpoint lại Bài 1.

## Review tiếp theo

Đã rà lại ảnh PDF 9–18 theo thứ tự cùng chapter clean. Đủ 13 unit và mọi anchor raw p9–18 có vị trí tương ứng; đã kiểm các lựa chọn, blank, track, bốn chức năng trong 重要表現, tình huống/quan hệ người nói, và phần ロールプレイ. Bài đi theo mạch nguồn: khởi động → 聞き取り練習 I → 聞き取り練習 II → ポイントリスニング → 重要表現 → ロールプレイ. Các vấn đề p9/p12 được giữ trong log, không lấp bằng nội dung tự tạo. Người review độc lập cần đối chiếu ảnh PDF và bản Việt; checkpoint tác giả không thay thế bước này.
