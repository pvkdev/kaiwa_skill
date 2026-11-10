# Nghiệm thu

## Trang

Đối chiếu mọi vùng có nội dung với ảnh. Kiểm đủ ký tự Nhật, dấu câu, vai/lượt, thứ tự đọc, bảng, bài tập, lựa chọn, furigana, số trang, track, ghi chú và hình. Review ghi vùng đã kiểm và các sửa đổi cụ thể. Tự xác nhận không phải chứng cứ độc lập tuyệt đối: coordinator vẫn kiểm tra chéo ảnh.

Không verified nếu scan chưa rõ, còn issue mất chữ, link ảnh hỏng, hoặc tiếp nối trang chưa được kiểm tra. Lỗi cấu trúc tự động có thể chặn; validator không đánh giá ngữ nghĩa.

## Pilot

Sol/high làm 4–6 trang đại diện. Astra/high mở ảnh gốc và đọc toàn bộ output pilot; ghi báo cáo `kaiwa_skill/pilot/REVIEW.md` gồm sách/hash, trang, mẫu đã bao phủ, lỗi phát hiện, sửa đổi, hạn chế và quyết định PASS/REVISE.

Kiểm thử phục hồi bằng hai worker tuần tự trên cùng sách: worker A hoàn tất một phần rồi release; worker B context mới đọc trạng thái để tiếp tục, không làm thay đổi hash trang đạt. Ngoài ra test tự động mô phỏng crash giữa các bước ghi, hỏng Markdown, thiếu ảnh/review và đổi PDF. Bàn giao sạch không được báo là đã mô phỏng kill process.

PASS cần không có lỗi mất/sai nội dung đã biết trong phạm vi pilot; định dạng truy xuất rõ; mọi trang pilot được đối chiếu; cơ chế resume và hash invalidation đã kiểm chứng. Không suy diễn pilot PASS nghĩa là 4.597 trang sẽ không có lỗi.

## Production

Gate PASS được lưu trên đĩa và gắn phiên bản skill/commit, phạm vi pilot. Nếu sửa quy tắc nội dung ảnh hưởng pilot phải đánh giá lại. Mỗi sách: worker đối chiếu 100% trang, coordinator kiểm tất cả trang bị gắn cờ và lấy mẫu theo loại bố cục, đầu/cuối unit; lỗi hệ thống mở rộng rà soát cả nhóm trang liên quan.

Book completed chỉ khi tổng trang verified bằng số trang PDF, không có lỗi còn mở, sản phẩm ghép/chỉ mục được build từ nội dung hiện tại và kiểm tra chéo đạt. Sách không đạt vẫn giữ checkpoint và issues, không ngăn xử lý sách độc lập khác.
