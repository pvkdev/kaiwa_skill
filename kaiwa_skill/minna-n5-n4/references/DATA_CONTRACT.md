# Contract biên tập Minna — dự thảo 0.1

Tài liệu này mô tả mô hình biên tập cả lộ trình. Phần video ngữ pháp và luyện tập đã có [hợp đồng trao đổi 1.0.0-rc.1](../contracts/harumii-minna/v1/CONTRACT.md), gồm JSON Schema và bộ đóng gói chạy được. Dữ liệu dùng UTF-8, field snake_case và thời gian ghi nhận UTC.

## Bốn lớp dữ liệu

1. `sources`: snapshot bất biến và metadata nhận từ nguồn; không sửa để “làm đẹp”.
2. `normalized`: parse source thành cấu trúc, có provenance; có thể dựng lại từ snapshot.
3. `authored`: bài giảng, mapping B, MCQ chuyển thể, script video và chỉnh sửa đã duyệt.
4. `exports` chứa snapshot cùng manifest và trạng thái `draft` hoặc `reviewed`. Adapter phía app quản lý GUID, media binding và quyền xuất bản.

Không bắt đầu bằng một cột HTML cho cả lesson: sẽ mất speaker, đáp án, clip và quan hệ B–ngữ pháp. HTML được giữ như bằng chứng nguồn; bản learner render qua cấu trúc đã làm sạch.

## Lesson envelope

- `schema_version`, `course_id`, `lesson_id`, `lesson_number`, `revision`, `status`.
- `volume`: 1 cho bài 1–25, 2 cho 26–50. `target_level` N5/N4 là cách tổ chức lộ trình, không chứng nhận mỗi điểm trong sách tương đương tuyệt đối JLPT.
- `sources[]`: resource references.
- `grammar_points[]`, `utterances[]`, `exercise_groups[]`, `dialogues[]`, `passages[]`, `assets[]`, `nodes[]`.
- `vocabulary_binding_request`: tham chiếu bộ Minna và số bài, trạng thái unresolved/resolved/ambiguous. Không tạo từ mới, không chia batch bằng số lượng ước đoán.
- `coverage`: trạng thái và số lượng riêng từng phần/trường; `issues[]`: lỗi/pending có source và mức ảnh hưởng.

Stable IDs ví dụ: `minna.l39.g01`, `minna.l39.b01.q01`, `minna.l39.shadow.bunkei.s01`. ID cấp một lần và giữ xuyên reorder/sửa wording. `source_id`/DOM locator là chứng cứ, không phải identity duy nhất; source đổi ID cần reconciliation, không tự coi câu mới.

## Provenance dùng cho mọi nội dung

`provenance` gồm `source_resource_id`, `source_url`, `page_variant`, `section_id`, `source_item_id`, `locator`, `retrieved_at`, `snapshot_sha256`, `parser_version`.

`origin`: `source` / `editor` / `ai_adaptation`; nội dung dẫn xuất thêm `derived_from[]`, revision nguồn, prompt/model khi có, người duyệt và thời gian duyệt. `usage_rights_status` lưu tình trạng dùng lại để xử lý khi xuất bản; truy cập công khai không tự chứng minh quyền tái phân phối audio.

Trạng thái field: `present`, `pending`, `absent_confirmed`, `not_applicable`, `failed`. `null` phải có lý do đi kèm khi trường ấy nằm trong scope. Không dùng chuỗi rỗng để đồng nghĩa mọi trạng thái.

## GrammarPoint

- `id`, `source_order`, `title_ja`, `title_vi`, `pattern`, `form_rules`, `meaning_vi`, `usage_vi`, `constraints`, `common_errors`.
- `example_utterance_ids[]`, `source_quiz_group_ids[]`, `lesson_text_blocks[]`.
- `app_binding_hint`: tên/mẫu/số bài để admin đối chiếu; không coi tên là khóa unique của GrammarPool.
- `video_asset_id` là ID riêng cho video của từng mẫu. Lưu trạng thái `planned` đến khi có URL phát thực.

## Utterance và căn chỉnh Nhật–Việt

- `id`, `ja`, `vi`, `ruby_tokens[]`, `speaker_id`, `source_order`, `audio_refs[]` và trạng thái từng trường.
- `ja` là chữ cơ sở, không ghép `rt/rp` vào câu. Lấy ruby thành `{surface, reading}` riêng; giữ dấu câu và ranh giới câu.
- `vi` ghép theo container tương ứng, không zip hai list toàn trang. Một lượt nói có nhiều câu phải giữ `turn_id` và thứ tự câu.
- Nếu một bản dịch bao quát nhiều câu, dùng `translation_group_id`; chưa tách được thì giữ group, không nhân bản bản dịch vào từng câu như thể đã căn chỉnh.
- Có thể lưu ruby nguồn để đối chiếu; furigana/tokenization phục vụ app theo chính sách app, không giả định ruby nguồn khớp tokenizer đích.

## ExerciseGroup và Exercise

Group: `id`, `family` (renshuu_b / grammar_quick_check / listening / reading / mondai), `source_group_label`, `source_order`, `grammar_refs[]`, `items[]`.

Item:

- `id`, `kind`: `mcq`, `reorder`, `fill_blank`, `conjugation`, `true_false`, `matching`, `short_answer`, `open_response`.
- `prompt_ja`, `prompt_vi`, `context_refs[]`, `stimulus_asset_refs[]`, `requires_image`, `example_only`.
- `choices[]` dùng `{id, ja, vi}`; `tokens[]` dùng ID cho từng lần xuất hiện để xử lý từ trùng.
- `source_answer`: tagged union theo `kind`: `choice_ids[]`, `ordered_token_ids[]`, `accepted_texts[]`, `pairs[]`, `boolean_value`, hoặc rubric/example cho câu mở. Tách `answer_status`.
- `source_explanation` và `editor_explanation` riêng; nếu nguồn chỉ có đáp án thì giữ lời giải nguồn absent/pending, không tự gán lời giải AI vào đó.
- `authored_variant_ids[]`, `review_status`, `derived_from`.

Không biểu diễn mọi loại bài bằng `correct_index`. Với MCQ, canonical giữ choice ID; index chỉ tính khi xuất theo contract đích đã kiểm chứng. Mẫu trả lời tự do là gợi ý, không là một đáp án duy nhất.

Reorder giữ pool có thẻ nhiễu, chuỗi đáp án và biến thể hợp lệ được duyệt. Không suy đáp án từ `data-p`. Khi chuyển thành MCQ phải có đáp án/giải thích của phiên bản mới và bảo đảm một lựa chọn đúng (hoặc khai báo rõ multiple choice).

## Mapping B → ngữ pháp

Mapping record: `exercise_group_id`, `grammar_ids[]`, `evidence_refs[]`, `rationale_vi`, `mapping_status` (`proposed` / `reviewed`), `reviewed_by`.

Quan hệ nhiều–nhiều. Cho phép override ở item nếu một nhóm luyện nhiều mục tiêu. `placement_after_grammar_ids[]` dùng bố trí node; nhóm nhiều mẫu xuất hiện sau mẫu cuối theo thứ tự dạy. Không biến quan hệ sư phạm thành hard gate của learner.

Giữ `requires_image=true` ở source; bản chuyển thể có `requires_image=false` chỉ khi tình huống chữ đủ thông tin và đã duyệt. Không bỏ ảnh rồi giữ nguyên prompt bị thiếu dữ kiện.

## Dialogue và Passage

Dialogue: `id`, `family` (`renshuu_c` / `kaiwa`), `scenario_ja/vi`, `speakers[]`, `turns[]`, `variants[]`, `grammar_refs[]`, `audio_refs[]`. Turn có speaker và utterance IDs; variant có turns riêng, không ghi đè bản mẫu. Không ép mọi hội thoại có đúng hai người hoặc suy giới tính từ tên.

Passage: `id`, `family` (`short_reading` / `topic25`), `title`, `paragraphs[]` Nhật/Việt theo cặp hoặc translation group, `exercise_group_refs[]`, `audio_refs[]`. Không ghép ba đoạn bài ngắn thành ba passage độc lập nếu chúng cùng một bài.

## AudioAsset và AudioRef

Asset: `asset_id`, `kind` (`source_recording` / `source_tts_cache` / `generated_tts` / `browser_tts` / `unresolved`), `source_url`, `resolved_url`, `mime_type`, `byte_length`, `sha256`, `duration_ms`, `local_path`, `fetch_status`, `usage_rights_status`.

Ref: `asset_id`, `source_track_key`, `start_ms`, `end_ms`, `alignment_status`.

- Một file dùng nhiều refs. Tách fragment `#t=...` khỏi URL tải; giữ clip trong ref.
- Chuyển seconds sang ms có quy tắc, validate `0 <= start < end <= duration` khi đã đo duration. Không có duration thì chưa xác minh giới hạn, không làm tròn/đoán.
- URL query có thể có ý nghĩa; không tự strip query để dedupe. Dedupe bytes theo SHA-256 sau tải; URL/fragment chỉ giúp discovery.
- URL hết hạn lưu metadata cần thiết, không token trong export. Storage URL đích do adapter/app sinh.
- Browser TTS không phải file tải được. TTS tự sinh về sau giữ nguồn gốc riêng, không thay âm thầm audio nguồn.
- Không suy `/39.mp3` từ lesson number; bài 39 đã có track Kaiwa tên `40.mp3`.
- Mỗi file tải phải xác minh response không phải HTML/challenge, MIME/bytes, checksum và duration bằng công cụ media phù hợp. Chưa chạy bước này trong discovery.

## RoadmapNode

`id`, `kind`, `order`, `content_refs[]`, `grammar_refs[]`, `recommended_after[]`, `optional`, `default_enabled`, `publication_status`, `video_asset_id`.

Kinds biên tập: `vocab_video`, `vocab_learning`, `grammar`, `grammar_practice`, `shadowing`, `listening`, `reading`, `conversation_video`, `renshuu_c`, `kaiwa`, `assessment`. Đây là tên trung lập, không tuyên bố tồn tại trong enum Harumi.

Mỗi mẫu có một video riêng. Thứ tự node lấy từ mảng `nodes` của gói trao đổi. Mỗi node `grammar_video` có một node `grammar_practice` nối ngay sau, có thể chứa nhiều nhóm B hoặc phần luyện thêm. Thay đổi thứ tự vẫn giữ ID của node.

## Export gate

Gói có `schema_version`, `course_id`, `export_revision`, lesson file list/hash, media list/hash, unresolved bindings và provenance summary. Chỉ nội dung reviewed mới là publishable. Có thể xuất draft để preview nhưng bắt buộc phân biệt draft với published.

Semantic checks bắt buộc khi có dataset: unique IDs; refs tồn tại; source/group/lesson không lệch; phạm vi đúng; MCQ answer tồn tại; reorder không dùng token không có trong pool; không chấm câu mở bằng đáp án đơn; Nhật–Việt không lệch; timing hợp lệ; asset được xác minh; đáp án không lộ trong learner prompt; các node tắt không chặn luồng chính. Mọi số lượng so với inventory cùng source variant/revision.
