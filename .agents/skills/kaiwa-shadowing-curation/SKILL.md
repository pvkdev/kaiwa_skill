---
name: kaiwa-shadowing-curation
description: Biên tập V6.5 từ nguồn shadowing V6.3 thành tối đa một chuỗi câu và hội thoại sát topic mỗi chặng, có vai, giới tính TTS, nghĩa Việt và hồ sơ nguồn nội bộ.
---

# Biên tập chuỗi shadowing

Đọc yêu cầu trong planning/v6_5/REQUIREMENTS.md dưới kaiwa_skill. Chỉ xử lý các chặng được giao theo thứ tự trong level. V6.3 là snapshot chỉ đọc. Chín sách B05/B06/B07/B11/B12/B18/B19/B20/B24 đã chuyển sang hồ sơ nội bộ V6.4, dành cho V7 sau này. Nguồn bài luyện hiện tại chỉ B01/B08/B13/B14/INTERVIEW tại chính chặng V6.3. Có thể tra nguồn tương ứng của năm sách nếu cần xác minh. Không tự soạn câu để lấp thiếu. Chặng không có câu phù hợp có items=[] và không có node shadowing.

Đọc toàn bộ topic, mục tiêu, sự kiện và tình huống trước khi tuyển. Đọc toàn bộ material shadowing hiện có ở chặng, phân biệt câu luyện Nhật, bản dịch, lời dẫn và kiến thức. Chỉ giữ câu thực sự dùng được trong topic với vai và mục đích cụ thể. Loại câu chỉ trùng từ khóa hoặc chỉ hữu ích giao tiếp chung. Có thể tách khỏi Section/CD, giữ đủ ngữ cảnh để đối đáp có nghĩa. Mỗi item là single_sentence hoặc dialogue. Giữ lời Nhật nguồn, có thể sửa lỗi scan khi đã đối chiếu và ghi rõ thay đổi. Không ghép lượt ở những cuộc thoại khác nhau thành một cuộc thoại. Bản dịch Việt phải tự nhiên, sát nghĩa và đúng quan hệ. Không thêm furigana.

Khử trùng trong chặng, gom nguồn khi cùng câu/đoạn. Giữ khác biệt có giá trị về nghĩa/vai/sắc thái. Sắp từ câu đơn ngắn, đối đáp trực tiếp tới đoạn cần giải thích, hỏi lại, thương lượng. Chọn theo độ khó thực tế, không lấy độ dài hoặc nhãn sách làm tiêu chuẩn duy nhất. Không có quota câu.

Văn bản TTS chỉ có lời thực nói. Nếu nguồn dùng ngoặc tùy chọn hoặc nhiều biến thể ngăn bởi slash, chọn một cách đọc đầy đủ; giữ quote_ja nguyên văn và text_edit_note trong hồ sơ nội bộ. Đọc tới cuối câu trả lời có nghĩa, không cắt đoạn ngay sau phần mở đầu khiến câu hỏi chưa được trả lời. Nghĩa Việt không suy diễn buổi sáng/tối, mối quan hệ hay giới tính khi tiếng Nhật chưa cho biết; dùng vai/giọng đã chọn để giữ xưng hô nhất quán.

Mỗi speaker có id, role_vi, gender=male|female, gender_basis=source|editorial_cast. Nếu nguồn không rõ giới tính, phân vai TTS có chủ ý, không khẳng định đó là giới tính gốc. Cùng vai trong một item giữ một giọng. Từng turn có speaker_id, ja, vi và source_refs. Nguồn có book_id, book_title, material_path (tương đối V6.3), quote_ja chính xác có trong MD, source_path và source_start_line/source_end_line từ selection. Source refs là admin, tách khỏi gói learner.

Mỗi decision lưu stage_uid, display_code, status=reviewed, items, internal_knowledge, source_review và review_note. Item có id ổn định, type, speakers, turns, fit_vi, difficulty_vi. internal_knowledge tham chiếu material gốc và giữ ghi chú kiến thức hữu ích, chỉ nội bộ. source_review liệt kê TẤT CẢ material hợp lệ tại chặng với disposition=selected|knowledge_only|off_topic|unusable, lý do, các item_ids. Phần bổ trợ kiến thức không biến thành câu luyện. Nguồn needs_review phải đọc cảnh báo và loại câu bất thường chưa xác minh, ghi rõ hạn chế.

Ghi từng decision hoàn tất bằng file tạm rồi replace vào planning/v6_5/decisions/<code>.json. Đây là checkpoint, resume từ file còn thiếu hoặc chưa reviewed. Worker chỉ ghi các file thuộc level được giao, helper/cache đặt trong work/<level>. Không Git, không build file dùng chung. Root kiểm schema, nguồn quote, vai/giọng/dịch/trùng và đọc QA ngữ nghĩa rồi mới publish. Bài thiếu là kết quả hợp lệ. Mỗi chặng có tối đa một node. Kiến thức/video shadowing chỉ ở nội bộ, không hiện node video mới.
