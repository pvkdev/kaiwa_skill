# Nghiệm thu V9

## Dữ liệu

- 289 bản ghi topic giữ nguyên toàn bộ nội dung và thứ tự V8, chỉ thêm trường điều hướng stage_kind/roadmap_order.
- 72 chuyên đề, tổng 361 chặng. Sơ 18, Trung 36, Thượng 18 chuyên đề.
- 322 mục tuyển, 72 hồ sơ admin và 322 bản Markdown học viên. Mỗi mục có tên sách, mã, vị trí, hash và ghi chú đọc trong hồ sơ quản trị.
- Tất cả ứng dụng chỉ tới tình huống thật trong ba topic kế tiếp. Đầu mỗi cấp có 2–3 topic, cuối mỗi cấp là topic. Khoảng cách linh hoạt theo cụm.
- B18 chỉ Part 1. Thiếu thân bài 存じる② được ghi ở nhật ký đọc.
- 253 điểm bắt đầu đoạn nguồn khác nhau, 70 điểm có nhiều lượt dùng. Đây là thống kê locator, không phải số kiến thức duy nhất hay tỷ lệ phủ toàn sách. Tái dùng liên cấp được giữ khi hỗ trợ vai hoặc nhiệm vụ mới.

## Đọc và sửa

Ba worker Sol/high đọc phần nguồn định tuyển rồi tự rà nội dung xuất. Root đọc mẫu đầu, giữa và cuối mỗi cấp, kiểm metadata và tính khớp ứng dụng. Hai worker đọc chéo sáu chuyên đề ở Sơ/Thượng. Các vòng sửa đã bỏ lời dẫn kỹ thuật, mở rộng bản nháp quá mỏng, khử lặp trong cấp, sửa ví dụ theo dõi sự cố, thu hẹp mục tiêu Sơ và dời 16 vị trí Trung theo cụm. Phạm vi đã đọc và phần để dành nằm ở work/so.md, work/trung.md, work/thuong.md.

## Preview

Playwright mở bản HTML ở chiều rộng 320, 390 và 1440 px, kiểm một chuyên đề mỗi cấp tại mỗi chiều rộng. Nội dung mở được, không tràn ngang hoặc lỗi JavaScript. Root đã xem ảnh mobile thực tế. Gói HTML dùng learner.json, nguồn quản trị không nằm trong nội dung học viên. Mọi mục đọc có content tương ứng.

## Giới hạn

V9 là tuyển và bố trí kiến thức từ bảy sách. Số 72 là kết quả phân bổ hiện tại. Phạm vi đọc được ghi theo những bài thực sự xem xét, chưa tuyên bố đọc hoặc dùng hết bảy sách. Bộ kiểm cấu trúc và hash hỗ trợ tính toàn vẹn, đánh giá ý nghĩa dựa vào lượt đọc biên tập. Tình huống, video và các phần Live của topic tiếp tục có trạng thái như nền V8.
