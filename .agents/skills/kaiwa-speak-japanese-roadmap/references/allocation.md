# Dữ liệu phân bổ V7

Bộ dựng hiện có ở `tools/roadmap_v7.py`. Sau khi đã phát hành, đọc `DECISION_REGISTRY.json`, các decision và inventory đã commit. Sửa chuyên đề qua tệp decision có UID rồi chạy `py -X utf8 tools/roadmap_v7.py --publish`; `tools/build_review_site.py` cũng route theo CURRENT_ROADMAP.json. Các bản trích nguyên pack ở `materials/`, manifest nguồn trong `admin/`, chỉ mục ngược `SOURCE_INDEX.json`. Tham số `--from-workers` dành cho lượt ghép từ checkpoint worker; khi tiếp quản release đã chốt dùng dữ liệu canonical đã commit.

Đây là thiết kế cho pha chạy V7. Trong các đường dẫn dưới đây, `planning/` nằm trong `kaiwa_skill/`. Đường dẫn nguồn lưu trong dữ liệu dùng đường dẫn tương đối từ gốc repo, UTF-8.

B05 là nguồn tham khảo cho kiến thức tình huống dịch vụ. Tập khóa kiểm kê chuyên đề V7 lấy từ B06/B07/B11/B12/B18/B19/B20/B24. Lọc bằng book_id trước khi đối chiếu với hồ sơ V6.4.

## Đơn vị và quyết định

- Catalog V6.3 xác định một pack bằng cặp `book_id`, `pack_id`. Tham chiếu tới toàn bộ các phần của pack theo thứ tự catalog, giữ `book_title`, `title_ja`, path, hash, start_line, end_line và extra_parts. Mỗi placement dùng cùng bản nguồn. Ghi chú về nghĩa phụ chỉ để đánh giá fit của cả pack.
- Phiếu một pack lưu khóa nguồn, nội dung chính, yêu cầu về độ khó, level đề xuất, vị trí cũ nếu có và trạng thái đọc. Các kiến thức hỗ trợ, bảng và hướng dẫn cũng thuộc mẫu số.
- Quyết định chuyên đề gồm `uid`, `stage_kind=speak_japanese`, `title_vi`, `objective_vi`, `level`, `before_topic_uid`, `rank_at_anchor`, `ordered_packs[]`, `order_reason_vi`, `level_reason_vi`, `placement_reason_vi`, `applications[]`, `status`. Dùng giá trị level của V6.5. Mỗi mục trong ordered_packs là một khóa pack đầy đủ. Thứ tự mảng là thứ tự học. Ghi `reuse_reason_vi` tại lượt dùng lại khi cần. UID ổn định khi đổi tên, chuyển cấp hoặc dời vị trí.
- before_topic_uid xác định chỗ chèn trên giao diện. applications là các cơ hội áp dụng đã tìm thấy, có thể là mảng rỗng. Nếu có liên kết, lưu `topic_uid`, `situation_id`, `use_vi`, `relation=direct|reuse` và khóa pack liên quan. S001 chỉ có nghĩa trong phạm vi một topic. Với chuyên đề độc lập, placement_reason_vi giải thích vì sao ở vị trí đó phù hợp để học.
- Thư mục dự kiến gồm planning/v7/inventory/ cho phiếu đọc, decisions/ cho chuyên đề và admin/ cho chỉ mục ngược. Trạng thái biên tập draft, reviewed hoặc needs_review. Ghim hash snapshot/skill và ghi kết quả nguyên tử để có thể chạy lại hoặc sửa một nhóm riêng.

## Ghép bản học và kiểm

Đọc tuần tự các topic V6.5 theo level. Tại mỗi topic, chèn các chuyên đề có before_topic_uid tương ứng theo rank_at_anchor rồi xuất topic. Chọn cả hai khóa từ quyết định đã lưu để dựng lại được cùng thứ tự. Tính số thứ tự hiển thị sau cùng. UID của chuyên đề độc lập với tên, level và số thứ tự. Với từng topic, giữ UID, cụm, thứ tự tương đối và toàn bộ nội dung học V6.5, gồm cả các chặng có shadowing rỗng.

Preview pilot có ba tab level, hiển thị hai loại chặng trong cùng thanh điều hướng. Dùng tiêu đề, mục tiêu và vị trí thật cho chuyên đề dự kiến. Hồ sơ admin cho phép reviewer mở chính xác các bài nguồn và tình huống sẽ dùng. Payload learner chỉ chứa trường hiển thị. Mã sách, ghi chú phân vai, hash, locator và lý do xếp chặng chỉ có ở admin. Kiểm cả dữ liệu nhúng trong HTML. Giữ từ Speak Japanese ở nhãn loại chặng theo yêu cầu sản phẩm. Tên chặng và câu mục tiêu không đề cập mã sách hoặc tên cấp.

Khi build pilot, dùng đường dẫn bản nháp riêng và tập UID pilot. Khi build release đầy đủ, kiểm các điều kiện sau trước khi cập nhật CURRENT_ROADMAP.json và trang review chung.

1. Mọi UID duy nhất, mọi anchor tồn tại, cùng level và có thứ tự rõ nếu dùng chung anchor. Tất cả applications tham chiếu đúng tình huống, nằm sau chuyên đề trong toàn lộ trình. Cơ hội ôn ở cấp sau có thể tham chiếu về chuyên đề đã học.
2. Lọc stage_kind=topic rồi so với 289 topic gốc theo thứ tự và nội dung. Kiểm 1.304 sự kiện, 5.914 tình huống, 125 node shadowing với 296 item/406 lượt, 164 topic không có node này. Khi so từng hàng, chỉ cho phép các trường điều hướng V7 được thiết kế thêm.
3. Đối soát tập khóa với 1.004 pack của tám catalog. Kiểm mỗi placement mở được toàn pack theo đúng dải dòng, đủ extra_parts, đúng thứ tự và hash nguồn. Báo riêng theo sách số pack duy nhất đã đặt, số lượt đặt lại, pack chờ và ngoại lệ có lý do. Mỗi khóa phải có đích hoặc ngoại lệ đã duyệt trước khi hoàn tất. Một lượt chỉ trỏ một phần pack không đạt. Thống kê riêng giới hạn nguồn vật lý. Bản đồ chỉ xác nhận phân bổ; video được sản xuất sau.
4. Kiểm byte/hash của tệp nguồn, các locator kể cả extra_parts, tham chiếu mồ côi và phần tài liệu đang cần đối chiếu. B18 thiếu trang cho bài 14 存じる② ở snapshot nguồn. Giới hạn đó thuộc báo cáo tư liệu.
5. Chạy build hai lần trên cùng input rồi so UID, thứ tự, nguồn và hash learner. Kiểm UI thực tế trên desktop/mobile cho cả hai loại chặng và một topic không có shadowing. Bàn giao báo cáo theo level và theo sách, chỉ mục ngược, preview và commit riêng của release.
