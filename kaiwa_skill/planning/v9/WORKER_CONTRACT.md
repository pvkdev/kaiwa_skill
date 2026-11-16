# Triển khai chuyên đề V9

Áp dụng .agents/skills/kaiwa-chuyen-de/SKILL.md. Nền là planning/v8, 289 topic có tình huống đầy đủ. Mỗi worker sở hữu một cấp, đọc trực tiếp Markdown knowledge. B07/B11 gợi ý từ nửa sau Sơ đến đầu Trung, B06/B12 gợi ý giữa Trung lên Thượng, nội dung thực quyết định.

Mỗi chuyên đề ghi một JSON UTF-8 ở decisions/<key>.json. key dùng sj-so-01, sj-trung-01, sj-thuong-01 theo thứ tự trong cấp. Ghi sau từng cụm, file tạm rồi thay nguyên tử.

Các trường bắt buộc

- key, level (Sơ/Trung/Thượng), title_vi, objective_vi
- before_topic_code (mã V8), placement_reason_vi, load_reason_vi
- applications gồm topic_code, situation_id, use_vi. Đọc ba topic sau vị trí chèn, chỉ ghi ứng dụng có thật.
- sections gồm category (patterns/mini/keigo/idioms/emotion), title_vi, items.
- items gồm key ổn định, title_vi (cách nói Nhật có thể giữ), role (core/extension), summary_vi, reading_note_vi, source_spans, learner_md.
- source_spans gồm book_id, book_title, path tương đối từ repo tới book.md, start_line, end_line (1-based inclusive). Đọc toàn bài trước khi lấy đoạn. Nhiều span nếu bỏ phần phụ ở giữa.
- learner_md là nội dung học đã tuyển từ span. Giữ nguyên Nhật, giữ dịch Việt tương ứng và lời giải thích có ích. Loại mã sách, số mục, CD/track, số trang, thẻ HTML, đáp án, lời tựa và ghi chú nguồn. Đọc lại phần xuất để bảo đảm không kéo cả hướng dẫn dùng sách vào. Phần luyện điền chỗ trống có thể bỏ để tập trung bài nói. Tên sách và bằng chứng nguồn chỉ nằm trong source_spans.
- status bằng reviewed sau self-review.

Tạo work/<level>.md ghi tiến độ và phần đã đọc để dành, phần nguồn thiếu. Không đánh dấu đã đọc nếu chỉ tìm thấy tiêu đề. Không bắt đủ mẫu hoặc đủ chuyên đề. Nhịp khoảng 4 topic, gợi ý Sơ 14–18, Trung 32–40, Thượng 14–18 nếu nội dung hợp. Có thể ít/nhiều hơn với căn cứ. Mỗi chuyên đề nhóm theo việc sẽ nói ở các topic sau, nhiều nhóm sách khi tự nhiên. Cố khai thác nhiều kiến thức có ích nhưng tránh lặp vô nghĩa. Giữ nguyên cặp/Unit có đối chiếu cần thiết.

B18 chỉ Part1, 75 vị trí đánh số và thiếu thân bài 存じる②. Part2 để ngoài phạm vi. B19 để ngoài chuyên đề. B05/B08 để ngoài bảy sách.

Root ghép, kiểm trùng giữa cấp, kiểm dữ liệu và dựng HTML. Worker chỉ sửa file cấp mình trong v9/decisions và work, không dùng Git, không đổi V8 hoặc CURRENT_ROADMAP. Hoàn tất báo số chuyên đề, phần đã đọc và giới hạn còn lại.
