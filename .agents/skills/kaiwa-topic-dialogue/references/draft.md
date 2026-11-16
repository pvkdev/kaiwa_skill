# Bản thảo V11 cho một chặng

Pilot nằm ở `kaiwa_skill/planning/v11/pilot/<stage_code>/dialogues.json`. Bộ dựng đọc V10 làm nền và ghép dữ liệu theo UID. Bản phân phối sau duyệt dùng `v11/stages/<stage_code>/dialogues.json`. Mỗi hội thoại nằm ngay trong tình huống tương ứng của bản JSON dùng cho học viên. Phần private gồm `admin_sources` và `admin` lưu trong hồ sơ chặng. Giữ V10 làm mốc đối chiếu. Trường `origin` đã có trong tình huống V10 mô tả nguồn của **khung cảnh**; nguồn của từng lời thoại được lưu riêng.

Các trường bắt buộc trong bản tác giả:

- Gốc có `stage_uid`, `admin_sources` (object theo mã cục bộ) và `dialogues` (array theo thứ tự tình huống V10).
- Từng hội thoại có `situation_uid`, `event_id`, `context_vi`, `speakers`, `turns`, `admin`. Đọc nhánh, sự kiện và quan hệ nối tiếp từ V10 bằng UID thay vì chép tay. Hai speaker có `id`, `role_vi` và `gender` đúng `male` hoặc `female`. Đây là lựa chọn giọng TTS của nhân vật, nhất quán khi nhân vật quay lại trong một sự kiện.
- Từng turn có `id`, `speaker_id`, `ja`, `vi`. Đề xuất ID dạng `<situation_uid>-u01`, cấp ID một lần. Thứ tự do array quyết định. Một lượt chứa lời của đúng một vai. Bối cảnh và chỉ dẫn diễn xuất đặt ngoài chuỗi phát âm. Khi cần xuất theo Exchange v1, ánh xạ turn sang speaker và utterance bank có hai chuỗi Nhật–Việt bằng ID, bảo toàn gender ở dữ liệu vai cho TTS.
- `admin.source_refs` liệt kê mã các nguồn thực dùng cho cảnh. `admin.specialty_item_ids` liệt kê những bài đã vận dụng thuộc chuyên đề gần trước, có thể rỗng. `admin.turn_origins` là object keyed theo ID lượt. Lời viết mới có `kind: original_extension`. Lượt chuyển soạn có `kind: source_adaptation`, `source_ref`, `change_vi`. Lượt giữ nguyên lời Nhật có `kind: source_quote` và `source_ref` đến đoạn chứa chính lời đó. Một hướng dẫn nghiệp vụ từ web có thể làm căn cứ cho cảnh trong khi toàn bộ hội thoại là lời mới.
- Mỗi entry sách trong `admin_sources` có `kind: book`, `book_id` B01–B27, `title` đúng manifest, `path` Markdown từ gốc repo, `start_line`, `end_line` (tính từ 1, bao gồm hai đầu), `use_vi` mô tả điều lấy từ đoạn đó. Nguồn web có `kind: web`, `title`, `url`, `accessed` dạng YYYY-MM-DD, `use_vi` nêu dữ kiện và phạm vi. Câu mới chỉ lấy cảm hứng dùng nguồn ở cấp cảnh và `original_extension` ở cấp lượt.

Kiểm từ gốc repo bằng `py -X utf8 .agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py <stage_code> --check <dialogues.json>`. Lệnh kiểm đúng tập/thứ tự tình huống, hai vai thực sự nói, gender, JA–VI riêng, nguồn sách có thật và nằm trong đường dẫn đúng sách, quan hệ tới chuyên đề, ghi nguồn từng lượt và kịch bản trùng nguyên chuỗi trong chặng. Khi ghép nhiều chặng, kiểm thêm ID và đoạn trùng xuyên chặng. Phần QA ngôn ngữ, tính đúng của nguồn web và độ độc lập giữa các nhánh cần người biên tập đọc.

## Tiếp tục sau khi gián đoạn

Lưu `status.json` cạnh bản thảo. Ghi `stage_uid`, revision của V10 và skill, SHA-256 các đoạn nguồn đã dùng, SHA-256 của `dialogues.json`, cùng trạng thái theo UID cảnh (`drafted`, `needs_fix`, `reviewed`). Mỗi lỗi đang mở ghi UID lượt, mô tả và phần cần đọc lại. Tình huống chưa có bản thảo được suy ra từ danh sách đầu vào.

Lưu dữ liệu trước rồi mới ghi status bằng thay file nguyên tử. Nếu hai hash lệch vì dừng giữa hai lần ghi, đọc bản thảo trên đĩa và khôi phục tiến độ từ các UID có thật. Chỉ giữ trạng thái `reviewed` cho cảnh có dấu vân tay nội dung khớp bản đã rà. Khi bắt đầu rà, lưu hash riêng của từng cảnh được duyệt. Khi sửa lượt nói, rà cả lượt đáp và các cảnh tiếp nối trong cùng sự kiện. Báo cáo tổng hợp được dựng lại từ status từng chặng.
