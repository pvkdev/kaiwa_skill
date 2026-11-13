# Nghiệm thu biên tập pilot S-011

## Phạm vi và nguồn

Pilot đủ 15/15 tình huống V5, không viết thay lộ trình khác. Đọc lại toàn bộ Nhật–Việt của 15 hội thoại, 5 bài kiến thức và các ví dụ shadowing trong quá trình soạn từng cụm. Đã quét chỉ mục đủ B01–B27; chỉ đọc sâu các phần B01/B08/B11/B14/B27 có locator ở sources.json, cộng Minna và hai nguồn chính thức cho dữ kiện. Không tuyên bố đọc hết 27 sách hoặc kiểm lại ảnh PDF.

Kiến thức/cách luyện được chuyển soạn; các cuộc thoại tuyến giả định là original_extension. B11 bài 1 chọn chức năng xác nhận/báo ý định của ね, ví dụ viết mới và shadowing nối ngay sau. B14 góp cách hỏi lại một từ chưa rõ, B27 góp chiến lược kiểm thông tin, không đưa các mẫu trung cấp dài thành yêu cầu Sơ. B01/B08 góp nhóm câu đi lại; không dùng những câu nguồn kém tự nhiên chỉ để tăng độ phủ. Không có chỉ tiêu dùng hết tài nguyên.

## Gối đầu

Bài l02 dùng nội dung l01; l03 đã đối chiếu l01/l02; l04 dùng l02/l03 và từ l01; l05 dùng l03/l04 cùng nội dung cũ cần thiết. Từ review trỏ tới đúng item có thật. Chặng trước chưa biên soạn: giữ một pending_previous, chưa tuyên bố nối gối đầu xuyên chặng. Danh sách nguồn/ôn là metadata biên tập, không phải gate learner.

## Những chỗ đã sửa khi review

- Đánh nhầm 乗り場 là từ ôn dù v01 chưa có: sửa thành new, không thêm ngược vào bài cũ để vượt validator. Các từ ôn còn lại được nối chính xác tới item hash ổn định.
- Giản hóa hai lượt gọi điện ở S010 để giảm việc dùng mẫu chưa cần thiết cho nhiệm vụ.
- Loại ghi chú làm video/chuyển soạn khỏi lời giảng user nhìn thấy; giữ chúng trong metadata. Bài kiến thức vẫn giữ nội dung giải thích và ví dụ.
- Nhánh bus chuyển xe ban đầu dùng số tuyến/điểm chuyển có thể mâu thuẫn với S008. Đổi sang xe số 9 và bến giả định Aoba-dōri, giữ nhất quán xe số 5/8 trong hội thoại mẫu.
- Nhánh hỗ trợ đang chờ được nhắc rõ không lấy kết quả đã xác nhận của S014 áp vào call hiện tại.

## Dữ kiện và level

Lộ trình, sân ga, bến, số xe, giá và mốc thời gian trong hội thoại là giả định. Hướng dẫn Kyoto chỉ chứng minh quy tắc lên/trả tiền có thể khác theo tuyến; JR East chỉ chứng minh có nhu cầu phối hợp/chờ, không cam kết thời gian hoặc dịch vụ ở mọi ga. Không nhập quy định vé, y tế hoặc mức phí thật. Grammar có level + tên; mapping N5/N4 phục vụ tìm kiếm và được ghi là biên tập, không phải danh mục chính thức JLPT.

## Challenge và free talk

Ba challenge, mỗi cái hai variant, đều có brief user và AI scenario riêng. Vai AI cố định trong mỗi call; context không yêu cầu diễn mọi nhân vật. Có nhánh sai thông tin, cần đổi xe và phải chờ, không chỉ cùng nhiệm vụ đổi tên địa điểm. Goal là nhiệm vụ giao tiếp, không pass/fail. Free talk có tổng hợp riêng và đủ material nodes; không ghép lệnh kín của challenge. Không trần 1000 ký tự.

## Phục hồi và giới hạn nghiệm thu

Pilot thật đã pause rồi resume cùng run với file/spec/source pins không đổi; giữ nguyên nội dung. Test dữ liệu giả định kiểm recovery JSON đang viết dở và nâng revision. Chưa chạy Claude Code, Live AI, TTS hoặc import DB. Đây là nghiệm thu nội dung và dữ liệu của tác giả; chưa có người bản ngữ/độc giả ngoài kiểm, chưa có bằng chứng hiệu quả sư phạm trên user thật. Không gọi script validate là bằng chứng tiếng Nhật hoàn hảo.

## Kết luận

Có thể chốt revision pilot để người dùng đọc preview và feedback. Không tự chạy hàng loạt 289 chặng trong lượt này. Sau feedback, nâng revision theo phạm vi; giữ ID, nguồn và lịch sử. Với rollout, ưu tiên chất lượng, checkpoint từng cụm; tiếp tục khi có quota, không thu hẹp nội dung để chốt sớm.
