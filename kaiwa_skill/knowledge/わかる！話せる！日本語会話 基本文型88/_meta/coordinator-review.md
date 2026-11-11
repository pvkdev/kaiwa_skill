# Nghiệm thu phạm vi PDF và giới hạn kiểm tra

Bản đọc bao phủ đủ 96 trang PDF được cung cấp, 16 chương và 113 unit. Tác giả đối chiếu toàn nguồn; 94 trang author_checked, PDF9 và28 needs_review. Validator với --allow-source-issues trả 0 lỗi, 4 cảnh báo cho hai page/unit tương ứng; không còn pending, draft hoặc stale.

Root đã mở 21 trang nguồn qua pilot, migration và QA mở rộng: 1–12, 18–22, 28, 31, 95–96. Root đọc toàn phần mở đầu và pilot cũ; đối chiếu toàn 48 câu ôn, lựa chọn, ô trống và 48 số đáp án in riêng cùng chú thích ở PDF18–22. Bài đọc どうも giữ bốn cách dùng, gồm cách kéo dài âm có chủ đích. Bảng 88 mẫu và chỉ mục 143 mục được đọc trong output, so ảnh hai trang cuối; đây không phải rà độc lập toàn bộ các bài chính liên quan.

Theo QA đã sửa ô trống tương ứng trong bản Việt, phân biệt cặp từ đầu vào Drill B với chỗ cần điền; không điền đáp án vào đề. Root xác minh thêm ngữ cảnh trời tối tại PDF31 và sửa hàng17 của bảng tra cứu: 降りそう là có vẻ sắp mưa. Các bài chính khác vẫn thuộc phạm vi đối chiếu của tác giả, chưa full independent semantic review.

PDF9 in công thức ～では→～ちゃ mâu thuẫn với ví dụ 来てはだめ→来ちゃだめ; bản clean giữ ví dụ và cảnh báo thay vì công nhận công thức sai. PDF28 bị cắt đáy, chỉ còn đầu câu8A trong phần C; giữ các câu đọc được, bản Việt của A dựa trên English còn rõ và không dựng Nhật hoặc lượt B mất. Root đã mở ảnh28 và đọc unit liên quan. Chi tiết nguồn ở source-issues.md.

Audio có nhãn CD1–88 theo trang bài và hướng dẫn dùng CD ở PDF6; đây là mã tra cứu, không suy có88 đĩa. Chưa xác nhận số đĩa hay tệp nghe thực tế, actual_files_status vẫn not_checked. Migration và scope history giữ nguyên chứng cứ pilot cũ; báo cáo/hash cũ chỉ áp dụng phạm vi lịch sử.

Rà hạn thời gian: Warm-up第6回5 tạiPDF20 là明日までに, bản Việt sửa thành chậm nhất ngày mai, không dời hạn sớm và không thay từ seed/giải bài. Hash bản đọc hiện hành: 2d2f478ceabde5c8c864093f125513070e1c89a65740d11467acc77040dc6e3b. Validator vẫn0lỗi/4cảnh báo nguồn đã biết.
