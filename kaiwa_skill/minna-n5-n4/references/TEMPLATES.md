# Xuất bài tập sang năm template giáo trình Harumii

## Đầu vào trung lập

`authored/lesson-39/templates/sections.json` là mẫu có cả năm loại. `sections[]` gồm `id`, `kind`, `cluster_prompt_ja`, `questions[]`. Mỗi câu giữ `id`, `prompt_ja`, `explanation_vi`, `source_item_id` và `grammar_refs`. Với câu chọn đáp án, `choices[]` có ID riêng; đáp án là `correct_choice_id` hoặc toàn bộ `correct_choice_ids` cho chọn nhiều. Với câu điền, `blank_answers[]` ứng với từng dấu `(...)` trong prompt. Với đọc/nghe, `media` chứa passage Nhật–Việt hoặc URL audio, script Nhật–Việt, bằng chứng xác minh và tình trạng upload. Nguồn gốc cùng ID ở bản trung lập; JSON native không có cột nguồn tương ứng.

`scripts/curriculum_templates.py` kiểm tra ID trùng, đáp án không thuộc lựa chọn, phương án trùng, thiếu lời giải, số ô trống không khớp và media thiếu. Chạy:

```powershell
py -X utf8 scripts/curriculum_templates.py authored/lesson-39/templates/sections.json
py -X utf8 scripts/curriculum_templates.py --renshuu authored/renshuu/lesson-39.json --out exports/curriculum-exercises/renshuu/lesson-39
```

Adapter `--renshuu` nhận trực tiếp `authored/renshuu/lesson-NN.json` của lane Renshuu. `correct` là **choice ID** cho `manualQnA`, là chữ Nhật cho `manualFillInBlank`. Dấu `＿＿` được chuyển thành `(...)` vì đường lưu hiện tại của Harumii chỉ đếm chuỗi này. `instruction_vi` được đặt ở `clusterPrompt.text` để hiện trước khi trả lời. Bản nguồn và nhãn `provenance` vẫn nằm ở file authored; không coi đáp án AI là đáp án chính thức của drill.

`--quick-check` nhận cùng schema item của `--renshuu` nhưng buộc mỗi item có `grammar_refs` và mỗi nhóm cùng bộ refs có 1–3 câu. Lệnh xuất khi có file:

```powershell
py -X utf8 scripts/curriculum_templates.py --quick-check authored/quick-checks/lesson-39.json --out exports/curriculum-exercises/quick-checks/lesson-39
```

`index.json` ghi `placement_after_grammar_refs` cho từng section và `groups[]` theo bộ refs. Mỗi item là một section riêng để `instruction_vi` của từng câu hiện trước đáp án. Lộ trình gắn nhóm sau **mẫu cuối** trong `grammar_refs`; không suy vị trí chỉ từ thứ tự file. Khi chuyển sang API, mỗi nhóm có thể dùng một `ExerciseSession` riêng; API hiện tại không có trường link trực tiếp từ exercise sang grammar entry, nên quyết định đặt sau video thuộc tầng learning path.

## Đầu ra

Mỗi thư mục lesson có `index.json`, file `*.storage.json` cho cả năm loại, và `*.paste.json` **chỉ** cho đường dán đã qua round trip an toàn. `storage.json` gồm `format`, `content` và `audioPath`; `content` là payload native tương đương `serializeSectionContent`, đáp án được tính từ ID sang chỉ số 0-based ngay lúc xuất. File này là dữ liệu chuẩn bị migration, không phải API import đã được Harumii xác nhận. `paste.json` là envelope `harumiExerciseCopy: 1` dành cho ô dán JSON của editor.

| Template | Native storage → learner | Paste → save → learner | Trạng thái |
|---|---|---|---|
| `manualQnA` | Đạt | Không an toàn | Chỉ xuất storage; editor nhập tay hoặc fix parser |
| `manualFillInBlank` | Đạt | Đạt với `(...)` | Xuất cả hai |
| `manualMultiSelect` | Đạt | Không an toàn | Chỉ xuất storage; editor nhập tay hoặc fix parser |
| `jlptReading` | Đạt | Đạt | Xuất cả hai |
| `jlptListening` | Đạt về cấu trúc | Đạt về cấu trúc, media chưa phát được trong app | Chỉ xuất storage cho tới khi upload MP3 |

**Lỗi Harumii đã xác nhận:** `parseCopiedExerciseJson` trong `frontend/src/lib/learning/curriculumExerciseCopyPaste.ts` tái tạo `questions[].choices[].id` của section không phải JLPT nhưng giữ nguyên `correctChoiceId` và `correctChoiceIds`. Khi lưu, `questionToQuizDto` tìm ID cũ trong lựa chọn mới, dẫn đến `correct_index` sai hoặc `correct_indices=[]`. Cần remap ID đáp án theo ánh xạ ID cũ → ID mới ngay trong `regenerateSectionIds`, rồi có test với đáp án không nằm ở vị trí đầu và multi-select nhiều ID. Không sửa repo Harumi trong phạm vi này.

### Đưa native storage vào API

Đường editor thực tế `curriculumExerciseSave.ts` gọi `ensureExerciseTemplates()`, lấy template ID theo `format`, rồi POST từng exercise. `*.storage.json` **không dán vào ô JSON**; nó chứa nguyên liệu cho body API:

- URL: `/api/learning/admin/{grammar|vocab}-curriculum-units/{unitId}/exercises`.
- `exerciseTemplateId`: UUID template có `format` khớp `storage.format` (`QuizMultipleChoice`, `Reading`, `Listening`).
- `content`: **chuỗi** `JSON.stringify(storage.content)`, không phải object JSON lồng.
- `orderInSession`: thứ tự 1-based; `sessionId` UUID khi đặt vào nhóm. `audioPath` chỉ gửi sau upload nếu có.

`scripts/curriculum_api_requests.py` tạo file body để review, **không gọi API**:

```powershell
py -X utf8 scripts/curriculum_api_requests.py exports/curriculum-exercises/lesson-39 --scope grammar
py -X utf8 scripts/curriculum_api_requests.py exports/curriculum-exercises/quick-checks/lesson-39 --scope grammar --grouped --unit-id UUID --template-ids template-ids.json --session-ids session-ids.json
```

`template-ids.json` map format → UUID; `session-ids.json` map `group_key` từ index → UUID session. Khi thiếu ID, manifest ghi `ready_to_send=false` và placeholder, không được gửi nguyên trạng. `saveCurriculumUnitExercises` hiện **xóa exercise cũ không có trong mảng sections**, còn POST từng file không làm bước xóa; trước migration cần so diff và thứ tự với dữ liệu admin đang có. Không có API import preview theo schema này; preview hiện là UI editor. Đường learner đọc `templateFormat` + `content` bằng `sectionsFromLessonExerciseContent`.

## Nghe bài 39

Với media đang chờ upload, index của gói liệt kê `pending_audio_media_ids`. Sau khi tệp đã được upload và kiểm phát trên Harumii, truyền `--audio-urls audio-urls.json` cho `curriculum_api_requests.py`. File này đối chiếu từng media ID với HTTPS URL phát được trên môi trường đích. Chừng nào còn thiếu binding, preview ghi rõ ID đó trong `unresolved`.

Nguồn gốc B1-1 có câu `地震のニュースを見て、びっくりしました。` và metadata clip 24,71–27,25 giây trong `reports/lesson-39-renshuu-b.json`. `reports/audio-39-b1.json` xác minh MP3 nguồn đã giải mã được ở đoạn đó. Lần yêu cầu media trực tiếp ngày 2026-11-25 trả HTTP 403, nên URL nguồn trong payload **chưa dùng được để phát trong app**. Không truy cập trang challenge để vượt kiểm tra.

File `authored/lesson-39/templates/audio/earthquake-news.mp3` là **bản đọc mới bằng Microsoft Haruka Desktop (ja-JP)** đúng script trên, không phải clip nguồn. FFprobe xác minh 3,973 giây, 25.083 byte; FFmpeg giải mã toàn file thành công; SHA-256 `881da8b9a45df4ad8e10ef8833c2432582cf505bec43d1c951e1dd4c418513b3`. Audio chưa upload lên Harumii. Trước khi phát hành, admin upload file MP3 qua editor JLPT audio và thay `mediaItems[0].audio.url` bằng URL công khai trả về; sau đó kiểm lại trong learner. `*.storage.json` hiện giữ URL nguồn để còn đối chiếu, không được xem là media production.

## Kiểm

Với bài nghe đã có MP3 cục bộ, `pending_audio_media_ids` trong `index.json` liệt kê ID cần gắn. Sau khi upload MP3 và kiểm tra URL phát lại trên Harumii, tạo `audio-urls.json` với mỗi khóa là một ID trong danh sách đó và giá trị là URL HTTPS tương ứng. Thêm `--audio-urls audio-urls.json` khi chạy `curriculum_api_requests.py`. Dù UUID template và unit đã đủ, công cụ vẫn giữ `ready_to_send=false` nếu còn thiếu URL. Với nhóm bài theo mẫu ngữ pháp, dùng thêm `--grouped` và binding session.

```powershell
py -X utf8 scripts/curriculum_templates_test.py
& ../../../harumi/frontend/node_modules/.bin/vitest.cmd run curriculum_roundtrip.test.ts --config ../../../harumi/frontend/vitest.config.ts --root scripts
ffmpeg -v error -i authored/lesson-39/templates/audio/earthquake-news.mp3 -f null NUL
```

Vitest nhập bằng code frontend Harumii thật, lưu bằng `serializeSectionContent`, đọc bằng `sectionsFromLessonExerciseContent`. Bài 39 có 5 section / 8 câu; adapter Renshuu đã xuất 50 bài / 359 câu. Quick check đã xuất 50 bài / 420 câu thuộc 318 nhóm: 218 nhóm một câu, 98 nhóm hai câu, hai nhóm ba câu. Cả 318 nhóm khớp ID, độ phủ và thứ tự của `catalog/grammar-points.json`. `reports/template-roundtrip.md` ghi kết quả và giới hạn.
