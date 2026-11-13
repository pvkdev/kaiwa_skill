# Đầu ra để nhập Harumii

Đọc trước khi biên soạn chặng phục vụ feature mới. **Hợp đồng chuẩn**: `kaiwa_skill/contracts/harumii-kaiwa/v1/CONTRACT.md`, `stage.schema.json`, `catalog.schema.json`, `example-stage.json`. Các đường dẫn tính từ gốc repo. Hợp đồng biên tập 3.2 trong thư mục skill là workspace/checkpoint, **không phải DTO app**. Không lấy JSON biên tập cũ import thẳng vào DB.

## Những quyết định bắt buộc

- Giữ 289 UID V5; `schema_version=1.0.0` của gói app độc lập với V5 hoặc workspace 3.2.
- App nhận đúng wire JSON snake_case của schema, không cần đoán field hoặc đọc đường dẫn PDF trên máy tác giả.
- Vocabulary xuất duy nhất `terms_ja: string[]`; không soạn thêm nghĩa, reading, ví dụ, audio hoặc furigana cho list. Metadata ID/ôn trong workspace chỉ phục vụ biên tập.
- Grammar xuất `patterns: [{catalog: minna|bunpou, jlpt_level: N5|N4|N3|N2|N1, name_ja}]`; admin pick theo level + tên. Lấy level từ metadata đã đối chiếu; nếu Minna cần mapping biên tập thì ghi căn cứ trong source-map, không gọi đó là danh mục JLPT chính thức hoặc suy máy móc từ số bài. Mục chưa rõ level phải rà trước export, không bịa ID DB hoặc level.
- Mọi câu Nhật luyện tập/ví dụ/hint có `ja` + `vi` trong `utterances`. Chia sẻ ID câu giữa bài kiến thức, shadowing, dialogue và hint khi cùng nghĩa. Từ, tên mẫu ngữ pháp và tên riêng không phải câu luyện, không bắt dịch riêng từng chuỗi này.
- Không tạo furigana, CD/track/audio file, TTS URL hoặc voice vendor trong gói app. Harumii tự furigana/TTS; không chọn giọng thay app. Metadata CD vốn có trong nguồn clean vẫn giữ ở nguồn, không xóa hoặc bắt truy tìm thêm.
- Knowledge giữ Markdown, ví dụ chèn `{{utterance:ID}}`; đọc lại cả bản MD đã hydrate Nhật–Việt. Không để câu ví dụ Nhật nằm ngoài kho câu. Speak Japanese vẫn là kiến thức/video planned → shadowing ngay sau, dùng chung câu.
- Mỗi situation chỉ có một bộ turns cho cả hai chế độ shadowing. Shadowing tham chiếu câu hoặc tình huống, không copy lại dialogue. Ghi metadata nguồn/viết mới trong sổ nguồn workspace.
- Challenge có brief user + tình huống AI + biến thể; free talk cuối chặng có tình huống đã soạn và context đủ tài liệu. Không trần 1.000 ký tự, không trộn lệnh các challenge vào free talk. Không có test/điểm/gate.

## Quy trình biên soạn và đóng gói

1. Tiếp tục dùng workspace/checkpoint, sổ nguồn và gối đầu để đọc/soạn có căn cứ. Với lượt mới, `stage_work.py begin` khai báo đích xuất `harumii-stage.json`.
2. Trong canonical mode, **soạn nội dung một lần trong `harumii-stage.json`**. `stage_work.py sync/validate/finalize` sinh workspace 3.2 và MD; không viết hai bản lời thoại. `source-map.json` ghi nguồn/viết mới từng material node; sổ bài và nguồn là metadata do tác giả ghi. Xem `run-and-resume.md`.
3. Chuẩn hóa ID/tên mẫu/list từ/câu Nhật–Việt; chuyển ví dụ trong Markdown thành token câu, dùng lại utterance ID khi cần. Không tự suy ra ngữ nghĩa hoặc nghĩa Việt bằng script. Validator chỉ kiểm cấu trúc.
4. Trước chốt revision, chạy validator. Helper sẽ kiểm nếu draft khai báo `harumii_export`; UUID/tên/cấp/code và revision gói phải khớp snapshot chặng. Workspace cũ không có khai báo vẫn đọc được, nhưng **chưa sẵn sàng import feature mới** cho tới khi bổ sung gói đúng chuẩn.
5. Chốt revision rồi đóng gói từ file `harumii-stage.json` trong snapshot đã chốt, không lấy draft đang viết. `pack` tạo thư mục mới, entrypoint `stage.json`, manifest hash và các MD preview/context. Không chạy TTS hoặc gọi app khi đóng gói.

```powershell
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/kaiwa_exchange.py validate PATH_TO_HARUMII_STAGE_JSON
py -B -X utf8 .agents/skills/kaiwa-stage-content/scripts/kaiwa_exchange.py pack PATH_TO_FINALIZED_HARUMII_STAGE_JSON --output NEW_EXPORT_DIRECTORY
```

Tool dùng Python với `jsonschema`; không tự cài dependency hoặc gọi model/network. Thư mục đích phải mới để tránh ghi đè bản đã duyệt hoặc bản đang xuất dở. Manifest chỉ xuất sau khi các file đã ghi xong; gói dở chưa có manifest không được đưa vào app.

Sổ nguồn, bằng chứng đã đọc, gối đầu và nhận xét biên tập tiếp tục ở revision workspace; không nhét các đường dẫn/note kỹ thuật đó vào nội dung user nhìn thấy.

## Khi chỉnh sửa

Giữ ID nếu vẫn cùng đối tượng; revision mới khi thay nội dung. `retired` khai báo những node/câu bỏ ở lần cập nhật, không dùng lại ID cũ cho ý khác. App giữ lịch sử và mapping riêng. Đổi title/order không đổi identity; sửa Việt không đòi skill tái tạo audio. Không thêm ID DB, asset URL hoặc progress learner vào source để khớp tạm một DB.

Khi sửa hợp đồng, đồng bộ generator/schema/example trong repo này và chạy regression. Bản chuẩn luôn ở repo lộ trình; mirror cũ ở Harumi được cập nhật trong task app sau này. Không sửa repo Harumi, chạy import hoặc EF migration trong task lộ trình.
