---
name: kaiwa-roadmap
description: Dựng, phục hồi, kiểm và xuất khung lộ trình Kaiwa V6 từ các chặng V5 và quyết định chọn nguồn đã đọc, gồm bản mobile, preview và tra ngược theo sách.
---

# Điều phối lộ trình Kaiwa

Làm việc từ gốc repo. Yêu cầu gốc ở `kaiwa_skill/planning/v6/CHECKPOINT_YEU_CAU.md`, chính sách đọc bằng máy ở cùng thư mục trong `SOURCE_POLICY.json`. V5 có 289 UID với sự kiện, tình huống, liên kết tiếp nối, thứ tự và cấp do người dùng chốt. V6.0 xuất mỗi hàng V5 nguyên nội dung, thêm đối tượng v6 chứa trạng thái, quyết định và thứ tự học. Phạm vi pilot được đọc từ policy. V5 tiếp tục là con trỏ sản xuất trong thời gian duyệt pilot.

## Từ phân công đến bản review

1. Đọc policy và trạng thái từng UID. Điều phối giao các mã chặng tách biệt. Worker áp dụng skill [kaiwa-source-assignment](../kaiwa-source-assignment/SKILL.md), một decision cho mỗi chặng. Chỉ người điều phối ghép chung và dùng Git. Nếu gián đoạn, xác định worker cũ đã dừng, giữ draft và nguồn đã kiểm để tiếp tục đúng UID. Tệp decisions hoàn tất là checkpoint bền vững; draft dở đặt ngoài decisions để build chỉ nhận kết quả đã bàn giao.
2. Dùng `py -X utf8 tools/roadmap_v6.py find "<topic hoặc chức năng tiếng Nhật/Việt>" [--book B07]` để bắt đầu tra chỉ mục đơn vị đã có. Công cụ tìm tiêu đề; tiếp tục tra toàn văn/annotation khi không gặp từ khóa, đọc trực tiếp từng mục đáng chọn. Không sinh bài giảng, hội thoại hay nhiệm vụ challenge trong task phân bổ.
3. Với mỗi decision, chạy `py -X utf8 tools/roadmap_v6.py check-one <path>`. Đọc lại locator, ranh giới, số track và vai người học. Với các chặng gần chủ đề, so các đơn vị lặp lại và lý do. Giữ bài lặp có ích ở nhiều cấp; nhiều bài khác nhau ở cùng chặng được khuyến khích khi bổ sung giá trị. Rà cả những ứng viên bỏ qua vì pack chứa nhiều cảnh lạc đề.
4. Từ quyết định đã duyệt nội bộ, chạy `py -X utf8 tools/roadmap_v6.py build`, sau đó `py -X utf8 tools/roadmap_v6.py verify`. Nếu gián đoạn khi render, chạy lại build rồi verify. Hash nguồn đổi cần đọc lại đơn vị và cập nhật quyết định sau khi xác minh. Bản gốc V5 được ghim hash, từng hàng sau khi bỏ v6 phải bằng bản gốc. Sáu pilot nội dung cũ vẫn dùng hợp đồng phiên bản gốc.
5. Mở `planning/v6/PILOT.md` hoặc `ROADMAP.html` trong kaiwa_skill để xem đúng thứ tự bài. Trong JSON, khóa v6.learning_order có một cặp liên tiếp cho từng bài và một node cho từng pack độc lập. Thông tin quản trị tập trung ở v6.decision. Các node dự kiến đánh dấu giai đoạn soạn sau. Chặng chưa được giao có status not_reviewed; chặng đã xét có thể có selections rỗng.
   Build sao trọn mỗi bài/pack đã chọn thành một Markdown trong `stages/<mã chặng>/`, cùng `manifest.json` ghi tên sách, vị trí nguồn, hash, CD/track, tên file và thứ tự. Hai node Speak Japanese dùng cùng bản Markdown. AI ở giai đoạn soạn bài đọc file trong manifest ngay tại chặng. Giữ tên bài gốc ở tất cả các cấp. Mỗi bài Speak Japanese có vị trí video chờ gắn, rồi mở được bài shadowing ngay bên dưới. Bài giảng tổng hợp chỉ có vị trí chờ video. Shadowing độc lập mở trực tiếp. Preview HTML nhúng phần đọc để mở offline, các file Markdown gốc cho phép kiểm lại bản đầy đủ. Trình render dùng gói Python `markdown-it-py`.
6. Bàn giao bản review cùng STATUS.json và TRA_THEO_SACH.md. V6.0 dừng ở ba chặng được chỉ định. Khi chủ dự án cho lệnh gán hàng loạt, mở release V6.1 riêng từ checkpoint V6.0, kế thừa các decision đã duyệt và mở hàng đợi 3 worker Sol/high. Cập nhật phạm vi, dựa theo cụm gần nhau, theo dõi từng UID và tổng hợp lại chỉ mục ngược. Chỉ chuyển con trỏ sản xuất sau nghiệm thu bản được chọn.

## Nâng cấp một chặng

Mở decision đúng mã, giữ nguyên stage_uid, lưu lịch sử qua Git. Khi đổi một bài, xem cả chặng khác dùng cùng pack trong chỉ mục ngược. Tái kiểm hash, tình huống và thứ tự ở chặng sửa rồi dựng lại các bản dẫn xuất. Đổi chủ đề lộ trình hoặc sản xuất bài học là công việc riêng với một lần điều chỉnh nguồn.

## Release V6.1 đã được giao

Người dùng chốt mỗi worker một cấp và đi tuần tự theo QUEUE_so.json, QUEUE_trung.json, QUEUE_thuong.json trong planning/v6_1. Ba worker Sol/high. Các chặng pilot kế thừa. Trước khi chạy helper, đặt KAIWA_ROADMAP_DIR trỏ tuyệt đối tới kaiwa_skill/planning/v6_1. SOURCE_POLICY.json trong release ghi scope đầy đủ. Lưu từng decision đã check-one; draft trong work/<cấp>. Điều phối build/verify các bản đọc và nội dung cục bộ sau các lượt bàn giao. Chỉ đánh dấu hoàn tất khi có đủ 289 decision hợp lệ. V6.0 tiếp tục là snapshot pilot.
