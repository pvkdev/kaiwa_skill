# Quy trình nguồn PDF → Markdown

## Đầu vào và nhận dạng

Kiểm kê mọi PDF trong book và vocab. Ghi đường dẫn tương đối, SHA-256, số trang vật lý, mã sách ổn định. Bản chính/sách bài tập/tập từ vựng là các nguồn riêng; chỉ liên kết quan hệ khi xác nhận từ sách. Không suy ra nội dung hoặc level từ tên file.

## Xử lý trang

- Mọi trang vật lý đều được quản lý, kể cả bìa, trang trắng, mục lục, copyright, đáp án, phụ lục. Blank phải được nhìn và xác nhận.
- Render ảnh tạm trong `.cache/renders/` tối thiểu khoảng 150 DPI để xem tổng thể, tăng 250–300 DPI hoặc crop nếu chữ nhỏ/furigana chưa rõ. Không đánh dấu verified mới nếu môi trường không thể mở ảnh. Ảnh không thuộc output hay commit; có thể tạo lại từ PDF khi cần rà soát.
- OCR/text layer chỉ là bản nháp. Có thể đọc trực tiếp từ ảnh nếu không có OCR; ghi đúng phương pháp đã dùng.
- Trước verify, đối chiếu hai chiều: đi từng vùng ảnh sang Markdown để tìm nội dung thiếu, rồi đọc từng dòng Markdown về đúng vùng ảnh để tìm chữ/ruby/nhãn tự thêm. Với furigana nhỏ, crop đủ rõ và so từng kana, kể cả ký tự nhỏ hoặc cuối chuỗi; kiểm đúng lần xuất hiện và phần chữ được chú âm. Không chỉ kiểm cách đọc có hợp lý theo kiến thức tiếng Nhật hay không. Review ghi vùng đã crop và sai khác đã sửa, không dùng một câu xác nhận chung thay cho việc đối chiếu.
- Đi theo thứ tự đọc của trang; trang scan đôi giữ mã PDF, thêm panel trái/phải và số trang in riêng. Trang nối câu/hội thoại phải kiểm với hàng xóm, kể cả ngoài phạm vi pilot (chỉ đọc).
- Lưu Markdown theo trang trước, verify sau. Kết quả verified gắn với hash nguồn, ảnh đã dùng để đối chiếu và Markdown cụ thể; giữ hash render trong hồ sơ text. Xóa cache sau khi kiểm tra không làm mất hiệu lực xác nhận; cache còn tồn tại nhưng bị sửa hoặc render lại khác phải kiểm tra lại. PDF hoặc Markdown thay đổi luôn làm mất hiệu lực xác nhận.
- Giữ checkpoint trên đĩa, không chỉ ở lời trả lời của worker. Viết file atomic; trạng thái lệch file sau crash được reconcile theo hướng thận trọng.

## Hoàn tất

`book.md` và chỉ mục truy xuất là sản phẩm sinh từ trang verified, không sửa trực tiếp. Pilot hoặc sách dở phải ghi rõ phạm vi và incomplete. Một file ghép được tạo thành công không phải bằng chứng đủ toàn sách.

Status cấp kho tổng hợp từ dữ liệu sách; status sách đối chiếu hash và từng trang. Báo total/draft/verified/needs_review/missing riêng. Không sử dụng tỷ lệ OCR để tuyên bố chính xác.

## Tiếp tục sau gián đoạn

1. Kiểm tra worker cũ; dừng hoặc xác nhận nó đã chết trước khi thu hồi claim.
2. Chạy status/reconcile; hash khác, thiếu review hoặc file dữ liệu hỏng phải làm mất hiệu lực verified. Thiếu cache ảnh không làm mất trạng thái verified cũ; muốn đọc/đối chiếu mới thì render lại.
3. Nhận quyền sở hữu mới; đọc manifest, review/issues và trang dang dở.
4. Tiếp tục từ trang chưa đạt đầu tiên trong phạm vi. Không tự xóa file tạm chứa nội dung chưa cứu.
5. Build lại sản phẩm dẫn xuất sau khi sửa; ghi báo cáo bàn giao và release claim.
