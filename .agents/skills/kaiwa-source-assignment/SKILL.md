---
name: kaiwa-source-assignment
description: Tuyển bài Speak Japanese và pack shadowing từ kho sách clean cho từng UID chặng Kaiwa V6, ghi nguồn, bằng chứng ranh giới, độ phù hợp và tình trạng đã đọc.
---

# Gán bài và pack vào chặng

Nhận một UID/display code và thư mục làm việc do điều phối cấp. Đọc SOURCE_POLICY.json tại release được điều phối giao (hiện là kaiwa_skill/planning/v6_1). Đặt KAIWA_ROADMAP_DIR trỏ thư mục đó khi dùng helper. V6.0 trong planning/v6 dành cho pilot lịch sử. Đọc tất cả sự kiện, tình huống, mục tiêu và trọng tâm của đúng chặng trong JSONL V5. Quyết định theo topic, vai, hành vi nghe/nói và độ khó của cả đơn vị. Nhãn cấp sách và thứ tự bài chỉ gợi ý.

Tìm theo hai chiều. Tra topic, đồng nghĩa Việt/Nhật trong catalog27/source_index.jsonl, annotations, knowledge/*/_meta/units.jsonl, mục lục và tiêu đề. Xem cả những bài có chức năng bổ sung cho tình huống (mở lời, hỏi lại, sửa hiểu lầm, thương lượng, kết thúc). Xem lại các nhóm bài/pack có triển vọng trong danh mục đã phép để tránh bỏ sót do từ khóa. Đọc nguyên đơn vị tại nguồn clean trước khi chọn. Nhãn mục lục là bằng chứng ứng viên. Phân biệt “tìm qua chỉ mục”, “đã đọc trọn”, và “chưa đủ căn cứ”. Báo phạm vi quét thực tế. Không tự quét/gán các chặng ngoài phân công.

- **Speak Japanese**. Mỗi bài được chọn tạo một cặp bài giảng/video → shadowing nguyên ví dụ ngay sau. Chọn nhiều bài từ một hoặc nhiều sách khi chúng bổ sung cách nói có ích. Ghim trọn bài cùng phạm vi ví dụ/track, kể cả bài có nhiều lượt hoặc ví dụ. Nếu vài ví dụ hay nhưng trọn bài lạc đề thì xét ứng viên khác.
- **Shadowing độc lập**. Mỗi pack nguyên vẹn là đúng một node, có thể có nhiều pack cho cùng chặng. Kiểm tên mục, trang/anchor, đánh số câu và nhãn audio ở phần nội dung và _meta/audio khi có. Riêng B19, một nhãn CD ở mục đầu có thể gom hai mục liền nhau; B20/B24 cũng có các cặp biểu đạt cùng track. Đọc tới nhãn audio/Unit kế tiếp và tra metadata, thay vì coi một anchor là một pack. Một số DISC/track liên tiếp có thể nằm trong cùng bài nghe. Ranh giới node theo bài hoặc section được sách xác định; chỉ tách khi có bằng chứng các phần là bài nghe độc lập. Một số track khác tự thân chưa đủ để chia node. B01 có thể là nhóm in theo mục đích giao tiếp. Chọn toàn nhóm phù hợp và ghi ranh giới thực tế. Track chưa biết ghi rõ; nếu chưa xác định được ranh giới pack thì giữ pending. Dùng các inventory sẵn có trong catalog27/audio_packs khi phù hợp, tra nguồn in/clean nếu chưa có inventory. Giữ nguyên chữ Nhật và thứ tự khi sản xuất sau này.
- Được chọn lại cùng đơn vị ở nhiều cấp, kể cả học đầy đủ lần nữa. Ghi tình huống cụ thể và lý do ở mỗi chặng. Trong một chặng cùng đơn vị xuất hiện một lần theo đúng vai trò. Tìm đến khi các ứng viên đáng kể đã được cân nhắc, không đặt số lượng tối thiểu/tối đa. Thiếu bài phù hợp có thể trả về mảng rỗng đã xét.
- 27 sách và nguồn bổ sung có thể tham khảo cho lời giảng, hội thoại và Live. Vai trò tham khảo không tự cấp quyền làm node audio độc lập. Sách phỏng vấn mới chỉ chốt pack khi đúng phần clean đã ổn định, có locator/ranh giới kiểm được. Ghi pending trung thực nếu còn ở pilot ingest.

## Tệp bàn giao theo chặng

Tạo `<display_code>.json` trong thư mục decisions được chỉ định. Dùng UTF-8. Object có stage_uid, display_code, vocabulary_topics (mảng nhóm tiếng Việt), search_notes (mảng ghi các nguồn/chỉ mục đã xét và khoảng trống), selections, considerations. Giữ thứ tự giảng trong selections (Speak Japanese trước các pack độc lập). Mỗi selection gồm:

- kind (`speak_japanese` hoặc `shadowing_pack`), book_id, book_title (đúng manifest), unit_id (anchor chính, không có #), title_ja (tên bài gốc lấy nguyên từ heading nguồn, gồm số bài nếu có; dùng chung ở mọi chặng), path (đường dẫn chapter tương đối từ gốc repo), sha256 (hash byte của chapter), start_line, end_line (1-based inclusive, bao trọn đơn vị được chọn).
- source_number_prefix (nếu có): chép đúng phần đánh số đầu tiêu đề và dấu cách theo sách, ví dụ `(3) `, `45. ` hoặc `1-2　`. Bản nguồn và manifest giữ tiêu đề gốc. Tiêu đề cho người học bỏ tiền tố này; giữ những số mang nghĩa trong tiếng Nhật.
- pack_id (ID ổn định của bài/pack, ưu tiên ID inventory sẵn có), boundary (tên mục, toàn bộ nhóm/đối thoại/ví dụ gồm những gì và bằng chứng kết thúc; nếu pack vắt qua phần khác, ghi thêm các locator trong extra_parts với cùng path/sha256/start_line/end_line/unit_id).
- audio (mảng object disc, track, locator; null cho nhãn chưa biết), audio_note (nêu phần nào đã xác minh trên nguồn chữ và phần nào chưa), situation_ids (mã Sxxx thuộc đúng chặng), fit_vi (giải thích áp dụng cụ thể), difficulty_vi (xét toàn bài/pack), read_status = whole_unit_read.
- considerations là mảng ứng viên cụ thể chưa chọn, mỗi mục có book_id, locator, reason, status (deferred hoặc unsuitable). Chỉ ghi nguồn thực sự đã xét. Trình dựng dùng locator và hash để sao nguyên phần Markdown được chọn vào thư mục từng chặng. Phải bao gồm đầy đủ bài, lời giảng và mọi ví dụ theo thứ tự trong nguồn clean. Fit theo topic chỉ giải thích trong metadata. Tiêu đề bài và câu luyện giữ nguyên.

Checkpoint sau mỗi cụm nguồn vào draft riêng. Chạy `py -X utf8 tools/roadmap_v6.py check-one <file>` trước bàn giao. Điều phối đọc lại các vị trí, rà lý do, nhóm giáp ranh và thứ tự. Validator không chứng minh đã đọc hay khớp nghĩa.

## Chế độ bao phủ toàn sách từ V6.2

Chủ dự án yêu cầu tận dụng toàn bộ nội dung học của chín sách Speak Japanese ở V6.2, rồi phần B01/shadowing còn lại ở V6.3. Trong chế độ coverage_mode, tìm chặng gần topic hoặc chức năng nói, cho phép các ví dụ khác bối cảnh cùng pack. Một bài là kiến thức bổ trợ có giá trị độc lập. Giữ trọn pack và nhiều bài trong chặng. Quy tắc tuyển chọn có thể bỏ vì chưa khớp toàn pack của release trước nhường cho yêu cầu bao phủ mới này.

Kiểm kê trước theo từng sách và từng chương. Mọi nội dung học (lời giải thích, sơ đồ, bảng mẫu, mini-column, phần mở đầu có kiến thức, ví dụ và bài luyện) phải có vị trí trong pack hoặc bài bổ trợ. Chỉ loại bìa, thông tin xuất bản, mục lục/chỉ mục, bibliographic và phần lặp không có kiến thức mới. Ghi từng phạm vi loại với lý do. Phần kiến thức bổ trợ không gắn audio có pack_scope=educational_support, audio=[], audio_note giải thích; không bịa số CD.

Worker sở hữu nhóm sách và xuất catalog coverage/<book_id>.json, root ghép vào decisions để tránh nhiều worker cùng sửa một chặng. Catalog có chapters (path/hash), packs (stage_code/selection), exclusions (path/start_line/end_line/category/reason). Kiểm phủ dòng và kiểm con trỏ thực sự có trong quyết định, cộng trạng thái nội dung nguồn chưa chắc. Bao phủ nguồn clean có sẵn không chứng minh đã khôi phục các trang thiếu của PDF hoặc nghe lại audio.
