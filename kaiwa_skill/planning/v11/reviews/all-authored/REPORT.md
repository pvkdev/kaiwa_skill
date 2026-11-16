# Rà độc lập hội thoại V11 đã soạn

Phạm vi được xác định từ bản thảo và hồ sơ nghiệm thu tại lúc nhận việc. Có 120 chặng hàng loạt cần rà, tổng 2.532 cảnh. Chín pilot có 176 cảnh đã qua các lượt rà trước, được đối chiếu dấu vân tay nội dung với hồ sơ root_review để xác nhận mốc đó còn khớp.

Ba phiên gpt-6-sol/high mới rà lần lượt từng cấp theo thứ tự chặng, độc lập với phiên tác giả. Điều phối dùng gpt-6.1-sol, kiểm chứng cứ, đối chiếu diff, đọc mẫu các cảnh đã sửa và kiểm gói preview.

- Sơ có 40 chặng, 680 cảnh đã rà. Chỉnh 92 cảnh có thay đổi phần học viên đọc, thêm 22 cảnh chỉ sửa nguồn quản trị gắn với cảnh. Còn mở 0 điểm.
- Trung có 40 chặng, 945 cảnh đã rà. Chỉnh 113 cảnh có thay đổi phần học viên đọc, thêm 0 cảnh chỉ sửa nguồn quản trị gắn với cảnh. Còn mở 0 điểm.
- Thượng có 40 chặng, 907 cảnh đã rà. Chỉnh 62 cảnh có thay đổi phần học viên đọc, thêm 0 cảnh chỉ sửa nguồn quản trị gắn với cảnh. Còn mở 0 điểm.

Tổng có 289 cảnh được đánh dấu fixed. Trong đó 267 cảnh đổi lời thoại, bối cảnh hoặc vai và 22 cảnh chỉ đổi nguồn quản trị. Các chỉnh diễn đạt gồm cả sửa lỗi có căn cứ và lựa chọn cách nói rõ hơn trong ngữ cảnh. Ghi chú từng cảnh giải thích quyết định. Một số cập nhật nguồn dùng chung nằm ở admin_sources, xem danh sách mã chặng trong RUN.json.

Mỗi cảnh đã được đọc riêng bằng Nhật và Việt, kiểm mục tiêu, vai, cách người nghe hiểu kết quả và độ vừa sức. Các sự kiện được đọc theo nhánh continues_from. Sau sửa, người rà mở lại phần liên quan trước khi chốt hash.

- Mạch cảnh được chỉnh ở những chỗ nhắc thông tin tương lai, dẫn sai lời trước, mang vật dụng từ nhánh khác sang hoặc coi việc chờ duyệt là đã đồng ý.
- Bản Việt được chỉnh ở các điểm đổi chủ thể, đổi mức chắc chắn, sai nghĩa hạn thời gian và cách gọi nhân vật.
- Nguồn được đối chiếu khi có dữ kiện thực tế. Các cập nhật gồm dẫn chiếu hành lang chung cư S-007, thủ tục PASMO S-012, phạm vi nguồn dịch vụ S-028–S-032 và chương khiếu nại H-034/H-039.
- Vai, tên và gender được kiểm nhất quán để phục vụ luyện đổi vai và TTS.

Không còn điểm vướng được ghi nhận trong 120 chặng của lượt này. Phiếu từng chặng lưu cạnh thư mục báo cáo theo đường dẫn `../<mã>/review.json`. Phiếu có UID cảnh, lượt dẫn chứng, lý do giữ/sửa và ghi chú nhánh. Bản trước khi rà truy được từ baseline_commit trong RUN.json.

Bộ dựng xác nhận đủ 129 chặng topic có hội thoại trong preview lũy kế, tổng 2.708 cảnh. Dữ liệu Nhật–Việt và hai vai hiển thị khớp bản tác giả ở cả chiều rộng 1.280 và 390 px. Dữ liệu lộ trình ngoài hội thoại và chín pilot được đối chiếu với mốc ban đầu. JSON nhúng HTML khớp learner.json, bản Pages trong docs/index.html khớp ROADMAP.html.

Mở [preview lũy kế](../../ROADMAP.html), [tiến độ và số liệu](PROGRESS.json) hoặc [phân công và mốc nguồn](RUN.json).
