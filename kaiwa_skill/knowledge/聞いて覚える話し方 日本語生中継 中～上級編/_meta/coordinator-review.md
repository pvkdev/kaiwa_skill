# Rà soát điều phối — bản đủ PDF được cung cấp

Root kiểm độc lập theo mẫu, không tuyên bố rà toàn bộ bản dịch.

- Đã mở ảnh PDF9,11,79,89 và đối chiếu phần truyền lời/ghi chú, bài tập sắc thái hài lòng–hối hận ở bài8, thông tin tác giả và ấn bản. Tác giả ghi coverage 89/89 trang, 11 chương và 122 unit.
- Các câu `明日まで` đã sửa nghĩa “trước ngày mai” thành “chậm nhất vào ngày mai”; giới hạn thời gian không bị rút ngắn.
- PDF9 chỉ dẫn ghi ①～⑥ nhưng thực tế có năm tin nhắn: giữ đủ năm theo trang, ghi chênh lệch nguồn; không tự viết tin thứ sáu.
- Bài8 giữ các cặp đối chiếu, chỗ lựa chọn và bản dịch sau khi làm bài. Track và số phần giữ theo nguồn, không tự sửa chỉ vì số track khác giữa skit và câu hỏi.
- Mọi chapter trong kế hoạch được giữ theo thứ tự; coverage/hash/anchor kiểm bằng công cụ riêng, không thay việc đọc ảnh.

Phạm vi hoàn tất: 89 trang PDF được cung cấp. Không có CD/kịch bản riêng trong đầu vào này; không tự phục dựng hội thoại chỉ có trong audio. Các issue của nguồn vẫn nằm trong hồ sơ biên tập và đơn vị liên quan.

## Vòng độc lập toàn sách

Worker khác tác giả `/root/clean_namachuukei_sho` đã mở ảnh/so raw snapshot và bản clean đủ89/89 trang; ghi từng phần trong `_meta/independent-review.md`. Không phát hiện lỗi rõ cần sửa nên giữ chapters. Ranh giới cuối được kiểm lại: Bài8 PDF79–87, hậu ký/tiểu sử/ấn bản PDF88–89. Hash các chapter được rà nằm trong book.json.completion.independent_review; sửa sau đó cần rà lại phần liên quan. Phạm vi ảnh theo mẫu của riêng root vẫn như trên.
