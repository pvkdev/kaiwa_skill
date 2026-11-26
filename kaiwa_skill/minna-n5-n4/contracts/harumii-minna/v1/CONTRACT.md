# Hợp đồng nhập lộ trình Minna vào Harumii

Phiên bản trao đổi `1.0.0-rc.1`. Phạm vi đã chạy được là `grammar_practice` của một bài. Bài 39 là gói draft đầu tiên. Đơn vị nhập nhỏ như vậy cho phép đưa ngữ pháp vào trước khi hoàn tất nghe, đọc hoặc sản xuất video. Phần khai triển sang các loại node còn lại nằm cuối tài liệu.

## Bài 39 được tổ chức thế nào?

Mỗi dòng dưới đây là hai node kế tiếp nhau. Node đầu có một video dành riêng cho mẫu, bài giảng chữ và một ví dụ Nhật–Việt. Node sau chứa các nhóm thực hành theo thứ tự.

1. **Vて** → B1, nối một sự việc với cảm xúc.
2. **Vなくて** → B2, một sự việc không xảy ra gây nên cảm xúc.
3. **Aくて／Aで** → B3, tính chất dẫn đến hệ quả.
4. **Nで** → B4, bốn tình huống chữ thay cho đề phụ thuộc tranh.
5. **ので** → B5, B6, B7, B8. B8 đặt cuối vì người học cần phối hợp cả Nで ở mục 4 và ので ở mục 5.
6. **途中で** → hai câu luyện thêm về Vる途中で và Nの途中で. Cả hai có xuất xứ biên soạn mới.

Đối với bài khác, giữ nguyên đề nguồn khi đề tự đủ dữ kiện, có đáp án dùng được và Harumii hỗ trợ đúng thao tác. Khi cần chuyển thể, lưu ID câu nguồn, đáp án riêng của biến thể và ghi lời giải AI bằng tiếng Việt. Với B4, bối cảnh chữ được viết từ tình huống mà đáp án đã xác nhận. Một đề đã thay tình huống cần bản dịch và audio tương ứng với câu mới. Nếu thiếu transcript hay đáp án nghe, có thể viết bài nghe mới và làm audio mới. Giữ mục nguồn thiếu dữ liệu trong danh sách đối chiếu.

Pilot có một phương án trắc nghiệm cho mỗi câu B vì bộ định dạng đã kiểm ở Learning có MCQ thủ công, còn chưa xác minh được luồng xếp thẻ có thẻ nhiễu của nguồn. Gói lưu lời giải cho **câu nguồn** trong `ai_note_for_source_vi` và lời giải cho **câu Harumii** trong `explanation_vi`. Ví dụ mới, bài giảng và biến thể trong gói do AI biên soạn. Bản ghi nguồn tiếp tục giữ định danh ban đầu để có thể dùng lại khi renderer hỗ trợ.

## Lưu dữ liệu ở đâu?

Đợt biên soạn 50 bài còn có `exports/harumii/minna-50-exercises-preview.zip`. Mỗi `lessons/NN.json` chứa thứ tự node, các mục ngữ pháp từ VNJPClub, đề và lời giải ở định dạng storage của editor. Các mục từ vựng tham chiếu bảng Harumii đã xuất, với khoảng số dòng cho từng video và lượt học. Các phần bổ sung đã có nằm trong `supplements/NN/`. Manifest ghi SHA-256 của mọi thành phần. Gói dùng để kiểm nội dung và chuẩn bị binding. API từng exercise của admin và cách kiểm trạng thái media được mô tả trong [hợp đồng năm template](../../../references/TEMPLATES.md).

Bài giảng Harumii được chuẩn bị riêng trong `authored/grammar-upload/`. Gói tổng hợp theo [hợp đồng Markdown do admin cung cấp](../../../materials/grammar/HUONG-DAN-AI.md) có thể chọn trực tiếp trong “Biên soạn với AI” để xem diff theo UUID. Biên bản QA toàn khóa xác định file ZIP hiện hành.

- **Bản chính để sửa:** `authored/lesson-NN/grammar-practice.json`. Lưu UTF-8 và giữ ID ổn định cho mẫu, video, node, nhóm, câu. Người biên tập sửa file này rồi tăng `revision` khi thay đổi một gói đã đóng. Bản biên soạn, hợp đồng, script và metadata bằng chứng nằm trong repo Git.
- **Nguồn và bản phân tích:** `sources/lesson-NN/` giữ snapshot thô, `normalized/lesson-NN/` giữ bản parse theo ID nguồn, `reports/` giữ kiểm chứng. Pilot dùng inventory bài 39 và kết quả reveal đã xác minh. Lưu snapshot hoặc bản sao media cần giữ lâu dài trong kho riêng có sao lưu.
- **Media:** lúc chưa quay, cấp một `asset_id` riêng, `status=planned`, `playback_url=null`. Khi có file, lưu bản master ở kho media riêng và checksum vào metadata. Với video đã host, dùng HTTPS playback URL ổn định. Khi dùng R2 của app, binding theo asset ID, checksum và object key trên môi trường đích. Presigned URL chỉ dùng để chuyển file. Đối với audio nguồn, một object cho mỗi track và nhiều clip theo ms. Nếu player chỉ nhận một AudioPath, tạo file cắt dẫn xuất, giữ liên kết tới hash track và mốc trong metadata. Câu AI đổi lời cần audio khác.
- **Gói để chuyển:** `exports/harumii/lesson-NN/grammar_practice/rRRRR.zip`. Thư mục exports được Git bỏ qua vì có thể dựng lại. Với bản đã dùng để migration, lưu nguyên ZIP và SHA-256 trong kho artifact riêng có backup. Khóa lưu đề xuất là `minna-n5-n4/lesson-NN/grammar_practice/rRRRR/<zip-sha256>.zip`. Việc build tại máy chỉ ghi file local.
- **Phía Harumii:** Learning sở hữu các bản ghi course, unit, task, curriculum entry, exercise và tiến độ. Đề xuất thêm sổ import và binding bền vững trong DB của Learning. Sổ ghi course, lesson, scope, revision, hash, trạng thái và kết quả. Binding ghi source ID → entity kind + GUID, fingerprint lần nhập và quyền sở hữu trường. Khi đường dẫn file hay vị trí node đổi, đối chiếu theo source ID.

## Dựng và kiểm tra gói

Python 3.10+ với `jsonschema` 4.x. Chạy từ thư mục skill trên volume hỗ trợ hard link, ví dụ NTFS.

```powershell
py -X utf8 scripts/harumii_package.py build authored/lesson-39/grammar-practice.json
py -X utf8 scripts/harumii_package.py verify exports/harumii/lesson-39/grammar_practice/r0003.zip
```

ZIP có đúng ba file JSON UTF-8. `lesson.json` là snapshot đầy đủ để đối chiếu và dựng lại. `projection.json` chứa thứ tự task và payload bài tập đã đổi sang dạng Harumii đọc. `manifest.json` chứa `course_id`, `lesson_number`, `scope`, `revision`, `state`, `format_version` và SHA-256 của hai file kia. Cùng input tạo gói giống từng byte. Build từ chối ghi thay revision đã tồn tại nếu bytes khác. [Schema lesson](grammar-practice.schema.json) · [Schema manifest](manifest.schema.json).

`verify` so với cách biểu diễn JSON chuẩn của bộ đóng gói, kiểm hash, cấu trúc, thứ tự, ID và tính lại toàn bộ projection. Validator yêu cầu các video khác ID, mỗi node video có một node thực hành theo sau và các nhóm chỉ dùng mẫu đã dạy. Đáp án phải khớp một trong bốn lựa chọn phân biệt. Kiểm tra kỹ thuật tách biệt với việc xem xét câu tiếng Nhật và quay video.

## Adapter phía app

Màn hình học hiện dùng phần tiếng Nhật của `question.prompt` làm đề trắc nghiệm thủ công. Vì vậy, khi chỉ nhìn đề Nhật và bốn lựa chọn, người học phải có đủ dữ kiện để chọn đúng. Revision 2 bổ sung tình huống vào nhóm B2 và B7, đặc biệt chỉ rõ người nào đang xin phép làm việc gì. Trường tác giả `model` có thể để null khi phiên chạy không cung cấp định danh đã xác minh.

Đã đối chiếu checkout Harumi `fc5f0ce1`. Gói có thể kiểm và xem preview cục bộ. Bộ đọc ZIP, sổ import và giao dịch dưới đây là công việc cần triển khai ở app.

1. **Preview.** Xác thực manifest, schema, hash, tái tạo projection. Chọn learning path/unit đích, vocab + grammar curriculum đã tồn tại. Resolve từng grammar entry, exercise template theo format chính xác, media theo asset ID. Trả diff theo source ID, các binding còn thiếu, video còn chờ và các phần học khác của unit. Việc vắng một phần trong gói chỉ có nghĩa phần ấy nằm ngoài phạm vi nhập.
2. **Grammar.** `TaskType.Grammar` dùng `GrammarConfig(grammarCurriculumUnitId, grammarCurriculumEntryId)`. Video đi vào `GrammarCurriculumEntry.VideoUrl`. Bài giảng chữ + ví dụ phải hiển thị ở node đó. Learner hiện đọc `GrammarPoolEntry.Description/ExplanationHtml`. Nếu pool entry đang dùng chung và bài giảng mới khác, ưu tiên lưu nội dung ở entry riêng cho Minna hoặc bổ sung override theo curriculum entry. Chỉ sửa hàng do importer sở hữu. Route tác vụ learner hiện hiển thị link mở video. Phát nhúng trực tiếp trên lộ trình là thay đổi giao diện riêng.
3. **Exercise.** Một group → một `GrammarExercise` trong grammar curriculum unit. Resolve `ExerciseTemplateId` từ format `QuizMultipleChoice`. Ghi `GrammarExercise.Content` bằng chuỗi JSON serialize từ `projection.exercises[].content`. `item_ids[]` giữ liên kết theo thứ tự với câu hỏi của section. Một node thực hành → một task `Exercise` với `GrammarExerciseConfig` chứa `grammarCurriculumUnitId` và `grammarExerciseIds[]` theo đúng thứ tự nhóm. JSON manual QnA dùng `section_type=QnA4Answer`, `variant=jaToVi`, `is_manual=true`, `choice_count=4`. Mỗi câu có `question_ja`, `question` (hướng dẫn Việt), `choices`, `correct_index` tính từ 0, `explanation`. Trên gói bài 39, bộ đọc và serializer thật của frontend đã đọc–ghi lại **9 nhóm, 34 câu**, giữ nguyên đề, hướng dẫn, lựa chọn, đáp án và lời giải.
4. **Thứ tự.** `relative_order` chỉ là thứ tự trong đoạn ngữ pháp của một unit. Đặt cả đoạn sau các node vocab và trước shadowing. Cập nhật riêng các task thuộc đoạn và giữ thứ tự tương đối của các node ngoài phạm vi.
5. **Commit và chạy lại.** Khóa import theo (course, lesson, scope). Cùng revision và hash trả lại kết quả cũ. Cùng revision khác hash báo conflict. Revision mới cần preview dựa trên phiên bản đang active, cập nhật task/exercise/binding trong cùng một transaction. Các thay đổi thủ công sau lần nhập trước xuất hiện trong diff để chọn policy giữ hoặc thay. Đưa công việc media ra ngoài transaction.
6. **Xuất bản và phục hồi.** Draft có thể preview khi cả sáu video còn planned. Khi sẵn sàng, resolve video trên môi trường đích, kiểm phát được, duyệt nội dung, rồi publish revision. Việc một scope vắng mặt hoặc một node optional bị tắt giữ nguyên progress. Khi cần khôi phục, kích hoạt lại revision trước theo stable IDs. Với thay đổi membership, giữ mapping lịch sử, retire các node thuộc scope theo diff tường minh.

Ranh giới dữ liệu đề xuất cho các gói tiếp theo:

- **Vocab/video vocab:** tham chiếu curriculum unit và danh sách item đã có, batch khoảng 20–30 từ. Adapter dùng `VocabLearningConfig` và một binding riêng cho từng video.
- **Shadowing:** group Văn mẫu/A, thứ tự utterance, cặp Nhật–Việt, asset ID và clip. Đích dự kiến `PronunciationPractice` với pronunciation examples.
- **Nghe, đọc:** passage/transcript + bản dịch, danh sách câu hỏi và đáp án theo ID, clip gắn đúng mục. Đích `ListeningPractice` hoặc `ReadingPractice` với exercise ID. Lưu cờ tùy chọn của node khi app triển khai tính năng bật/tắt.
- **C và Kaiwa:** lưu từng mẫu C, biến thể, lượt nói, người nói, utterance + clip. Thứ tự là video hướng dẫn → các nhóm C → Kaiwa. Đích dự kiến `RolePlay`. Cần kiểm các trường hợp nhiều người nói và biến thể.
- **Mondai 1–6:** giữ số Mondai, thứ tự câu và đáp án. Chọn renderer Exercise hoặc Test theo cách hiển thị đã xác minh. Bổ sung schema/fixture cho từng scope trước khi nhập scope đó.

Mỗi scope bổ sung có schema, phạm vi replace và bài kiểm thử tương thích riêng. Backend đọc phiên bản/phạm vi trước khi áp payload. Workspace hiện tại giữ toàn bộ thay đổi ở khâu biên soạn và gói trao đổi.
