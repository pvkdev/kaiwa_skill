# Dữ liệu phân bổ V7

Đây là thiết kế cho pha chạy V7. Trong các đường dẫn dưới đây, `planning/` nằm trong `kaiwa_skill/`. Đường dẫn nguồn lưu trong dữ liệu dùng đường dẫn tương đối từ gốc repo, UTF-8.

## Từ nguồn đến quyết định

- `source_key` dùng cặp `(book_id, pack_id)` của catalog V6.3. Giữ đầy đủ `book_title`, tên mục gốc, chapter path, hash chương, dải dòng và các extra_parts. Khi chia một mục, cấp ID tiểu mục ổn định, lưu key cha và locator riêng. Nội dung MD gốc vẫn truy được. Thông tin track lịch sử có thể theo tham chiếu admin.
- Phiếu đọc ghi ý học, sắc thái, vai điển hình, bằng chứng từ phần đã đọc, các vị trí gợi ý từ V6.4 và tình trạng nguồn. Ghi mức sử dụng theo từng ý có thể dạy khi nhóm nguồn chứa nhiều ý. Phân biệt nguồn giảng chính, ví dụ bổ sung, tài liệu hỗ trợ và nội dung chưa phân bổ. Trùng ý giữa hai sách có thể dùng một lần và liên kết cả hai nguồn. Tệp hỏng hoặc trang thiếu được ghi giới hạn, kèm vị trí cần kiểm.
- Quyết định chuyên đề có `uid` ổn định, `stage_kind=speak_japanese`, `title_vi`, `objective_vi`, `level`, `before_topic_uid`, `rank_at_anchor`, `sources[]`, `applications[]`, `level_reason_vi`, `placement_reason_vi`, `status`. Mỗi source có key, vai trò và ý đóng góp. Mỗi application có `topic_uid`, `situation_id` và `use_vi`. Cặp UID + situation_id là khóa vì mã S001 có thể xuất hiện ở nhiều chặng. Dùng giá trị level đúng như dữ liệu V6.5.
- Ưu tiên một chuyên đề chính dạy mỗi ý. Có thể ghi thêm nơi ôn hoặc nâng độ khó. Nếu một ứng viên chưa có vị trí thuyết phục, lưu pending kèm lý do rồi xem lại khi gom toàn bộ chín sách. Một lần gán cũ ở V6.3/V6.4 chỉ là manh mối. CD và độ dài track không định ranh giới chuyên đề.
- Các thư mục dự kiến khi chạy là `planning/v7/inventory/` cho ghi chú từng sách, `decisions/` cho quyết định chuyên đề và `admin/` cho chỉ mục nguồn ↔ chuyên đề ↔ tình huống. Bảng checkpoint lưu khóa công việc, trạng thái, hash đầu vào, phiên bản skill, tệp đầu ra. Trạng thái dùng draft, reviewed, needs_review. Khi chạy tiếp, ưu tiên duyệt hoặc sửa quyết định dở trước khi tạo quyết định mới cho cùng ý học.

## Ghép bản học và kiểm

Mỗi ý học hoặc nhóm ví dụ có cùng đóng góp cần có locator và kết quả phân bổ. Ghi chặng tiếp nhận và vị trí dự kiến (phần giảng, nhóm ví dụ luyện, bài tập hoặc tài liệu bổ trợ có công dụng rõ). Khi gộp ý tương đương, dẫn tới mục tiêu đã dạy và đối chiếu sắc thái còn riêng. Với ngoại lệ, ghi đoạn cụ thể, lý do và phương án đã xem xét. Tách giới hạn nguồn vật lý khỏi ngoại lệ biên tập. Trong pilot có thể còn pending ngoài phạm vi. Khi nghiệm thu toàn bộ, số ý dạy được chưa có đích hoặc lý do ngoại lệ phải bằng 0. Báo cáo riêng số ý được phân bổ và số ngoại lệ; chỉ gọi là đã dạy khi phần nội dung thực tế đã được biên soạn.

Đọc tuần tự các topic V6.5 theo level. Tại mỗi topic, chèn các chuyên đề có before_topic_uid tương ứng theo rank_at_anchor rồi xuất topic. Chọn cả hai khóa từ quyết định đã lưu để dựng lại được cùng thứ tự. Tính số thứ tự hiển thị sau cùng. UID của chuyên đề độc lập với tên, level và số thứ tự. Với từng topic, giữ UID, cụm, thứ tự tương đối và toàn bộ nội dung học V6.5, gồm cả các chặng có shadowing rỗng.

Preview pilot có ba tab level, hiển thị hai loại chặng trong cùng thanh điều hướng. Dùng tiêu đề, mục tiêu và vị trí thật cho chuyên đề dự kiến. Hồ sơ admin cho phép reviewer mở chính xác các bài nguồn và tình huống sẽ dùng. Payload learner chỉ chứa trường hiển thị. Mã sách, ghi chú phân vai, hash, locator và lý do xếp chặng chỉ có ở admin. Kiểm cả dữ liệu nhúng trong HTML. Giữ từ Speak Japanese ở nhãn loại chặng theo yêu cầu sản phẩm. Tên chặng và câu mục tiêu không đề cập mã sách hoặc tên cấp.

Khi build pilot, dùng đường dẫn bản nháp riêng và tập UID pilot. Khi build release đầy đủ, kiểm các điều kiện sau trước khi cập nhật CURRENT_ROADMAP.json và trang review chung.

1. Mọi UID duy nhất, mọi anchor tồn tại, cùng level và có thứ tự rõ nếu dùng chung anchor. Tất cả applications tham chiếu đúng tình huống, nằm sau chuyên đề trong toàn lộ trình. Cơ hội ôn ở cấp sau có thể tham chiếu về chuyên đề đã học.
2. Lọc stage_kind=topic rồi so với 289 topic gốc theo thứ tự và nội dung. Kiểm 1.304 sự kiện, 5.914 tình huống, 125 node shadowing với 296 item/406 lượt, 164 topic không có node này. Khi so từng hàng, chỉ cho phép các trường điều hướng V7 được thiết kế thêm.
3. Với chín catalog, đối soát theo key và phạm vi nguồn thực. Báo riêng số đơn vị đã xét, số ý học được dạy, được liên kết để ôn, tài liệu bổ trợ, pending và khoảng trống nguồn. Một source_key có nhiều lượt tái dùng vẫn chỉ tính một lần trong số đơn vị nguồn. Giữ dấu vết từng tiểu mục nếu phân bổ một đơn vị cho nhiều chuyên đề. Dòng chỉ ghi “đã lưu trữ” chưa chứng minh một ý đã có nơi học. Liệt kê cụ thể các ý chưa phân bổ và lý do.
4. Kiểm byte/hash của tệp nguồn, các locator kể cả extra_parts, tham chiếu mồ côi và phần tài liệu đang cần đối chiếu. B18 thiếu trang cho bài 14 存じる② ở snapshot nguồn. Giới hạn đó thuộc báo cáo tư liệu.
5. Chạy build hai lần trên cùng input rồi so UID, thứ tự, nguồn và hash learner. Kiểm UI thực tế trên desktop/mobile cho cả hai loại chặng và một topic không có shadowing. Bàn giao báo cáo theo level và theo sách, chỉ mục ngược, preview và commit riêng của release.
