# Rà tác giả sau khi hoàn tất phạm vi PDF1–96

Ngày 2026-11-11. Đây là rà của người viết bản clean, không thay cho QA độc lập của điều phối.

- Đã mở ảnh nguồn của từng trang vật lý PDF1–96 khi viết; PDF95–96 còn được mở lại từng cột ở độ phân giải cao để đối chiếu bảng 88 mẫu và 143 mục chỉ mục. Bản raw cũ chỉ hỗ trợ chép chữ, không dùng thay cho ảnh PDF.
- Giữ toàn bộ 16 chương theo mạch sách, 113 đơn vị nội dung. Bảng tra cứu cuối sách có 88 hàng ví dụ Nhật, bản Việt và chức năng Nhật–Việt; chỉ mục có 143 mục cùng số trang in. Hội thoại, MEMO, bài tập, lựa chọn và ô trống được giữ ở các chương tương ứng. Không điền đáp án bài tập.
- Inventory âm thanh ghi các nhãn CD 1–88 nhìn thấy trên trang bài, coi là mã tra cứu; số đĩa và trạng thái tệp nghe không được suy đoán. Trạng thái tệp nghe vẫn `not_checked`.
- Hai vấn đề chưa giải quyết nằm ngay ở bản PDF: PDF9 in công thức không khớp ví dụ; PDF28 bị cắt ở đáy và mất phần cuối một lượt hội thoại. Page và unit liên quan giữ `needs_review`, không bổ sung chữ Nhật bằng suy đoán. Các trang còn lại đều `author_checked`.
- Sau build toàn sách, `validate --allow-source-issues` trả **0 lỗi, 4 cảnh báo** (hai page và hai unit ghi cùng hai vấn đề nguồn). Strict `validate` trả 3 lỗi trạng thái do hai trang chưa thể `author_checked`, như mong đợi; vì vậy chưa công bố strict PASS.

Build/validate ghi trạng thái tại thời điểm bản clean hoàn tất. Điều phối cần kiểm độc lập bản Nhật–Việt và nguồn in trước khi phát hành.
