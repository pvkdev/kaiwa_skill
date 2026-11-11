# Rà soát điều phối — bản đủ PDF được cung cấp

Root kiểm độc lập theo mẫu, không tuyên bố đã kiểm mọi bản dịch trong sách.

- Đã mở ảnh PDF1,5,14,29,53,83,87,90; đối chiếu các phần lời gửi học viên, từ chối lời mượn, menu, mở chủ đề, bài nghe/chọn, bài điền thông báo chung cư và giới thiệu tác giả. Toàn sách có 91 trang nguồn, 13 chương và 253 unit theo hồ sơ tác giả.
- PDF14: đã sửa nghĩa `先約があって` thành “đã có hẹn trước”, tránh thêm chuyện cho mượn chưa có trong câu Nhật.
- PDF53: đã sửa đại từ trong lời dẫn có `僕` từ “cậu” thành “mình”; câu Nhật không thay đổi.
- PDF29: menu vừa ghi Special Lunch chỉ ngày thường, vừa ghi tăng giá cuối tuần/ngày lễ. Đây có thể là dữ kiện gây thắc mắc có chủ đích trong bài hỏi làm rõ; giữ cả hai, không tự giải hoặc gọi chắc là lỗi in.
- PDF83/87: giữ câu hỏi, lựa chọn, chỗ trống và tám ô điền; không tự tạo đáp án. Dịch nằm sau phần luyện. Giữ track và vai luyện nói theo nguồn.
- Bìa, mục lục và ấn bản có hồ sơ metadata; lời bạt và tiểu sử giữ cuối sách. Không ép các bài theo template mới.

Phạm vi hoàn tất: toàn bộ 91 trang của PDF đầu vào này. CD và tập kịch bản riêng không có trong đầu vào; bản này không bao gồm nội dung chưa được cung cấp. Checkpoint/hash và validator xác nhận cấu trúc, không chứng minh mọi bản dịch đúng tuyệt đối.

## Vòng độc lập toàn sách sau build đầu

Worker khác tác giả `/root/clean_keigo` đã mở ảnh và đối chiếu đủ91/91 trang, ghi `_meta/independent-review.md`. Các sửa dịch ở Bài8/9/10 làm rõ vai, giữ đủ nhánh lựa chọn và sửa cú pháp Việt; không sửa câu Nhật hoặc tự giải ô trống. Root xem diff, kiểm ledger rồi rebuild/validate lại. Hash của chapter được rà nằm trong book.json.completion.independent_review; các chỉnh sau đó cần review phần liên quan lại. Giới hạn mẫu ảnh của riêng root nêu trên vẫn giữ.
