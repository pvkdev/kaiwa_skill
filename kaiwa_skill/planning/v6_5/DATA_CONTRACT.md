# Dữ liệu V6.5

`KAIWA_CHANG_V6_5.jsonl` giữ mỗi hàng V5 và trường `v6` mới. UID, cấp, thứ tự, cụm và các tình huống gốc tiếp tục dùng được. `v6.learning_order` có tối đa một mục `merged_shadowing`. Không có nội dung phù hợp thì bỏ mục này và `v6.shadowing=null`. Danh sách từ vựng topic và các vị trí chờ của bài giảng/tình huống/challenge/free talk tiếp tục được xuất.

`learner.json` là dữ liệu mà ROADMAP.html và docs/index.html thực sự render. Mỗi `stages[]` có `uid`, `code`, `level`, `number`, `title`, `cluster`, `objective`, `events`, `situations`, `vocabulary`, `order`, `shadowing`. Trường `selections` rỗng ở V6.5. Shadowing có `id`, `type=shadowing`, `items[]` theo thứ tự luyện.

Item gồm `id`, `type=single_sentence|dialogue`, `speakers[]`, `turns[]`. Speaker gồm `id`, `role_vi`, `gender=male|female`. Turn gồm `speaker_id`, `ja`, `vi`. Một câu đơn có một lượt. Hội thoại có ít nhất hai lượt và hai vai. Tra speaker_id trong chính item để lấy giọng TTS. Tên vai và danh tính chỉ có phạm vi trong item. ID item đã xuất cần được giữ khi chỉnh sửa; chuyển vị trí bằng thứ tự mảng, không đổi ID các câu cũ.

`decisions/<code>.json` là bản biên tập canonical của từng chặng. Thông tin nguồn ở từng lượt, fit/difficulty ở từng item, căn cứ giới tính, ghi chú kiến thức, kết quả xét từng material và ghi chú review chỉ dành cho admin. `admin/<code>.json` được build từ decision cộng snapshot V6.3, giữ cả chín sách Speak Japanese đã ẩn và toàn bộ nguồn shadowing cũ. Hồ sơ ghi đường dẫn source, title, book_id/book_title và hash. `snapshot_hashes`/`knowledge_archive` dùng đường dẫn tương đối thư mục V6.3. Nguồn CD lịch sử nằm trong archive; learner dùng TTS theo giới tính vai.

Kiến thức chưa chuyển thành bài giảng vẫn mở đầy đủ từ Markdown V6.3. Các trường internal không được nhúng vào learner.json/HTML. Không có video mới cho kiến thức shadowing ở UI trong phase này. Video bài giảng chặng tiếp tục là placeholder.

Phục hồi bằng `py -X utf8 tools/roadmap_topic_shadowing.py audit` tại gốc repo. AUDIT.json liệt kê chặng đã kiểm, còn thiếu và lỗi. Worker tiếp tục đúng UID thiếu, không ghi đè các decision đã duyệt nếu không có yêu cầu sửa. Build V6.5 chỉ chạy sau khi đủ 289 decision hợp lệ. Chạy `py -X utf8 tools/roadmap_topic_shadowing.py 6.5 --publish` để tạo báo cáo, roadmap, admin, learner, preview và cập nhật CURRENT_ROADMAP.json. Lệnh có thể chạy lại từ canonical, không thêm bài trùng. Khi sửa một chặng, sửa decision đó rồi audit và rebuild.
