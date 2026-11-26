# Đối chiếu Harumi cho migration sau này

Đối chiếu checkout `../harumi` (tính từ gốc repo Git) ngày 2026-11-25. Các đường dẫn backend và frontend bên dưới tính từ gốc repo Harumi.

## Những gì đã tồn tại

- `backend/src/Harumi.Learning/Data/Entities/Curriculum/LearningPath.cs`: path có `VocabCurriculumId`, `GrammarCurriculumId` bắt buộc.
- `.../LearningPathUnit.cs`: unit có order/topic và reference curriculum unit.
- `.../LearningPathUnitTask.cs`: task có `TaskType`, `Order`, `ConfigJson`.
- `backend/src/Harumi.Learning/Data/Enums/TaskType.cs`: có VocabLearning, Grammar, SpecializedLesson, PronunciationPractice, VocabReview, GrammarReview, Exercise, ListeningPractice, ReadingPractice, KanjiTracing, RolePlay, LiveAiMockKaiwa, LiveAiFreeTalk, Test. **Không có enum Video riêng** trong file đã đọc.
- `.../LearningPathPronunciationExample.cs`: câu Nhật/Việt, audio path và các trường tokenizer. Comment nhắc tối đa 10; handler generate tại `LearningPathTaskAuthoringSlices.cs` lại validate 1–50. Không lấy comment làm giới hạn dữ liệu nguồn.
- `.../LearningPathRolePlayItem.cs`: roleplay và lines có speaker dạng số, Content, ContentVi, AudioPath. Chưa xác minh renderer hỗ trợ đầy đủ nhiều speaker, variants hoặc media clip.
- `.../LearningPathTaskExercise.cs`: nội dung bài nghe/đọc có `Format`, `Content`, `AudioPath`; không đồng nghĩa canonical JSON của Minna đã được renderer hỗ trợ.

## Hướng mapping, chưa phải quyết định triển khai

- Vocab → binding curriculum/unit/list đã có. Chỉ chia batch 20–30 sau khi resolve đúng edition/bài và thứ tự; ambiguous không auto-pick.
- Grammar → GrammarPool/Grammar curriculum sau khi đối chiếu mẫu cụ thể. Tên tương tự không đủ để auto-bind.
- B → `TaskType.Exercise` với `GrammarExerciseConfig`. Gói bài 39 chiếu 9 nhóm thành 9 `GrammarExercise.Content`, chia cho 6 task thực hành theo thứ tự.
- Shadowing → xem xét PronunciationPractice engine, nhưng cần kiểm tra hỗ trợ clip và thứ tự nhóm A; không áp giới hạn comment 10 vào dataset.
- Listening/Reading → task hiện có với adapter đúng `Format/Content`; không ép text passage thành MCQ nếu mất cấu trúc câu hỏi.
- C/Kaiwa → xem xét RolePlay hoặc engine hội thoại phù hợp; mẫu/variant/speaker không tự flatten.
- Mondai 1–6 → Exercise/Test sau khi kiểm contract kiểm tra; đây là bài ôn Minna, không tự biến thành đề JLPT chuẩn.
- Mỗi `GrammarCurriculumEntry.VideoUrl` nhận URL video của đúng mẫu sau khi resolve asset. Route learner có link mở video. Video vocab/hội thoại cần binding riêng. [Quy cách gói trao đổi và xử lý khi nhập lại](../contracts/harumii-minna/v1/CONTRACT.md).
- `Shared/LearningPathTaskConfigSchemas.cs` khai báo `VocabLearningConfig` nhận unit ID + danh sách vocab item IDs, `GrammarConfig` nhận unit ID + entry ID, nghe/đọc nhận exercise ID. Adapter phải resolve các binding này trên môi trường đích.
- Bật/tắt node → chưa thấy field chuyên dụng trong entity task đã đọc; cần thiết kế config/publication/learner preference sau. Không tuyên bố tính năng đã có.

## Contract trước đây cần giữ riêng

`design/kaiwa-curriculum/IMPLEMENTATION_CONTRACT_V1.md` mô tả feature Kaiwa curriculum mới, ghi rõ chưa có importer/DB migration. Contract đó không chứa source audio và giao TTS/furigana cho app. Minna ở đây cần cả audio nguồn và bài tập/đáp án, nên không nhập lẫn hoặc sửa contract Kaiwa v1 âm thầm.

Repo biên soạn có [hợp đồng Kaiwa v1](../../contracts/harumii-kaiwa/v1/CONTRACT.md) và [hợp đồng Minna](../contracts/harumii-minna/v1/CONTRACT.md). Dùng hợp đồng Minna khi đóng gói dữ liệu lộ trình 50 bài.

`design/jlpt/curriculum_nodes_import.sample.json` và `curriculum_questions_import.sample.json` chỉ là mẫu import node/câu hỏi JLPT, không chứng minh toàn bộ roadmap/media Minna có thể import bằng chúng. Sample dùng `correctIndex`; chưa kiểm quy ước index của handler, adapter phải xác minh trước khi xuất.

## Trình tự migration đề xuất

1. Chốt canonical schema sau pilot; thêm fixture có nhiều speaker, clip audio, câu mở, B nhiều mẫu, node optional và ảnh chuyển thể.
2. Thiết kế wire contract Minna riêng hoặc version mới có tương thích rõ ràng. Giữ stable source IDs/revisions, không lẫn GUID môi trường vào source dataset.
3. Preview: validate schema + semantic refs + checksum, resolve vocab/grammar, hiển thị diff add/update/retire và các phần thiếu.
4. Commit: transaction theo lesson, idempotency theo course/lesson/revision/hash; cùng revision khác hash bị conflict, retry không nhân bản. Import media riêng, có thể tiếp tục khi gián đoạn.
5. Publish các node đã đủ nội dung/media cần thiết. Pending optional không làm mất nội dung core.
6. Import lại không ghi đè binding admin, video đính kèm, progress và media generation đang dùng. Text/clip đổi thì đánh dấu cần review/generation mới.
7. Rollback đổi con trỏ revision, không xóa lịch sử học. Retire node thay vì cascade delete progress.

Khi code ở repo app phải theo AGENTS.md của Harumi, qua boundary/interface domain đã định; không viết SQL trực tiếp xuyên domain từ crawler. Những bước trên là kế hoạch, chưa có endpoint hoặc migration nào được tạo/chạy.
