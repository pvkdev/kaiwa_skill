---
name: harumii-grammar-edit
description: Rà và nâng cấp bài giảng ngữ pháp Harumii đang có ở N5–N4, đối chiếu lộ trình Minna và đóng gói Markdown để admin so sánh, áp dụng. Dùng cả khi cần sửa bài giảng hiện có độc lập với lộ trình.
---

# Sửa bài giảng ngữ pháp để nhập lại Harumii

Đọc [hợp đồng đi kèm bản xuất](../../../kaiwa_skill/minna-n5-n4/materials/grammar/HUONG-DAN-AI.md) mỗi lần làm gói. Các đường dẫn dưới đây tính từ `kaiwa_skill/minna-n5-n4/` của repo.

1. Đọc bản xuất hiện hành và các mục VNJPClub liên quan. Có thể chuẩn bị bản nâng cấp ngay khi phát hiện lỗi, đồng thời với việc biên soạn lộ trình. Với từng mẫu, tra cả `materials/grammar/N5` và `N4`, đọc nghĩa, cấu trúc và ví dụ trước khi chọn ID. Một bài Harumii có thể bao quát nhiều cách dùng, hoặc một mẫu xuất hiện ở nhiều bài Minna. Gộp đề xuất sửa cho cùng ID, giữ các cách dùng đúng mà bài Minna này chưa dạy. Ghi những chỗ mơ hồ hoặc chưa xác minh được vào biên bản.
2. So sánh với bản xuất. Giữ nguyên mẫu đã đủ tốt. Với mẫu cần sửa, chép file vào `authored/grammar-upload/<đợt>/N4/` hoặc `N5/` và chỉnh bản chép. Giữ nguyên tên file, UUID và cấp. Chỉ tạo `<tên mẫu>__new.md` với `id: new` khi đã kiểm tra tên và cách dùng trong kho. Dùng tên mẫu, cấu trúc và ví dụ thích hợp với vốn từ bài. Ghi đối chiếu source ID và lý do thay đổi ở hồ sơ biên tập bên ngoài ZIP.
3. Áp hợp đồng cho từng file đã sửa, kể cả khi Markdown cũ có định dạng khác. Một H1 trùng tên mẫu, blockquote nghĩa, nhóm cấu trúc và các cặp ví dụ H5 Nhật / H6 dịch Việt liền nhau. Giữ ví dụ đúng, sửa đồng bộ câu và dịch khi cần. Đối chiếu thủ công nội dung, số thứ tự ví dụ, định dạng và cấp. Với trường bị lược khỏi front matter của mẫu cũ, admin giữ giá trị hiện tại.
4. Chạy `py -X utf8 scripts/grammar_upload.py authored/grammar-upload/<đợt> exports/grammar-upload/<đợt>.zip`. Công cụ đối chiếu các file sửa với bản xuất, kiểm cấu trúc và tạo ZIP chỉ chứa các mẫu đã chọn. Bàn giao ZIP cùng số mẫu sửa, thêm và các trường hợp còn chờ. Admin upload ở “Biên soạn với AI”, xem bản New và diff rồi chọn “Áp dụng”.
