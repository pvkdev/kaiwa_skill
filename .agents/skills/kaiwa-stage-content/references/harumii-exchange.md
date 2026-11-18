# Đầu ra để nhập Harumii

Đọc trước khi biên soạn chặng phục vụ feature mới. **Hợp đồng chuẩn**: `kaiwa_skill/contracts/harumii-kaiwa/v1/CONTRACT.md`, `stage.schema.json`, `catalog.schema.json`, `example-stage.json`. Các đường dẫn tính từ gốc repo. Hợp đồng biên tập 3.2 trong thư mục skill là workspace/checkpoint, **không phải DTO app**. Không lấy JSON biên tập cũ import thẳng vào DB.

## Những quyết định bắt buộc

- Giữ 289 UID V5; `schema_version=1.0.0` của gói app độc lập với V5 hoặc workspace 3.2.
- App nhận đúng wire JSON snake_case của schema, không cần đoán field hoặc đọc đường dẫn PDF trên máy tác giả.
- Vocabulary xuất duy nhất `terms_ja: string[]`. Danh sách phủ rộng theo chủ đề để người học tự nói, theo [kaiwa-topic-vocabulary](../../kaiwa-topic-vocabulary/SKILL.md); hội thoại/câu luyện đã soạn là nguồn rà, được thêm từ không xuất hiện trong lời thoại. Động từ thể từ điển, tính từ dạng cơ bản. `source-map.vocabulary_evidence` ghi mục từ đã rà, nguồn gốc `dialogue`/`topic_extension` và một vài surface/utterance thật cho từ lấy từ lời thoại; không yêu cầu mapping mọi lần xuất hiện. Reading và nghĩa Việt ở tầng biên tập, không vào gói app; không soạn audio cho list.
- Grammar xuất `patterns: [{catalog: minna|bunpou, jlpt_level: N5|N4|N3|N2|N1, name_ja}]`; admin pick theo level + tên. Lấy level từ metadata đã đối chiếu; nếu Minna cần mapping biên tập thì ghi căn cứ trong source-map, không gọi đó là danh mục JLPT chính thức hoặc suy máy móc từ số bài. Mục chưa rõ level phải rà trước export, không bịa ID DB hoặc level.
- Mọi câu Nhật luyện tập/ví dụ/hint có `ja` + `vi` trong `utterances`. Chia sẻ ID câu giữa bài kiến thức, shadowing, dialogue và hint khi cùng nghĩa. Từ, tên mẫu ngữ pháp và tên riêng không phải câu luyện, không bắt dịch riêng từng chuỗi này.
- Gói mới thêm `source_registry` và mỗi utterance có `authorship: source_quote|source_adaptation|original_extension`, `source_refs`, locator khi có ích. Nguồn giữ nguyên và câu AI mới không dùng chung một nhãn node để che khác biệt. `learning_scope: source_reference` phân biệt câu nguồn thực sự vượt cấp với phần chủ động core; xét từng câu, câu nguồn vừa sức vẫn là `core` và câu viết mới không bao giờ là `source_reference`. `grammar_node_ids` chỉ trỏ danh sách chứa mẫu mà chính câu đó dùng.
- Mỗi node kiến thức mới xuất có `data.admin_provenance` gồm `authorship`, `source_refs` và `cd_refs`. Từng source ref phải tra được trong `source_registry` của chính stage với tên đầy đủ, loại, vị trí bài/cảnh và mã sách nếu là sách. Khi một sách đóng góp nhiều bài, đăng ký nguồn theo bài/cảnh nếu một locator chung chưa đủ tìm lại. Bài tự soạn ghi `original_extension` và mảng rỗng nếu không dùng nguồn. Cả kiến thức tổng hợp và ví dụ đi kèm phải tra được nguồn thực đã dùng.
- Soạn nguồn **một lần** ở `source-map.json.nodes[knowledge_id]` và registry. Compiler/packager bổ sung nguồn từng ví dụ và lấy CD từ pack đã đối chiếu. Với CD được xác nhận trong sách nhưng không thuộc pack đã chọn, ghi thêm `cd_refs` trong mục node của source-map, ví dụ `{"source_ref":"lesson70","disc":"unknown","track":"70","locator":"trang 154, ký hiệu CD 70"}`. Đặt `unknown` ở phần chưa xác định, ghi bằng chứng ở locator. Chỉ ghi CD liên quan tới chính bài. Mỗi CD tra về đúng sách qua source_ref; pack đã chọn còn có pack_id và edition. Giữ thứ tự track từ kiểm kê. Không suy ra số đĩa từ số bài hoặc tự nhận có file audio.
- Admin/import đọc các trường này. Màn hình học và context đưa cho AI để trò chuyện chỉ đọc các trường nội dung. Duyệt cả tiêu đề, câu Nhật–Việt, các lựa chọn challenge, danh sách từ và phần free talk. Giữ nguyên tiếng Nhật của pack; nếu nội dung pack bắt buộc phải đọc lời giới thiệu nguồn, chọn pack phù hợp khác.
- Knowledge giữ Markdown, ví dụ chèn `{{utterance:ID}}`; đọc lại cả bản MD đã hydrate Nhật–Việt. Không để câu ví dụ Nhật nằm ngoài kho câu. Speak Japanese vẫn là kiến thức/video planned → shadowing ngay sau, dùng chung câu.
- Mỗi situation chỉ có một bộ turns cho cả hai chế độ. Shadowing tham chiếu câu/tình huống; một đoạn nguồn riêng có thể là item `dialogue` ngay trong bài luyện, với turns trỏ utterance bank, không cần nhân thành node tình huống riêng. Ghi nguồn từng câu trong canonical và metadata đọc nguồn trong workspace.
- Challenge có brief user + tình huống AI + biến thể; free talk cuối chặng có tình huống đã soạn và context đủ tài liệu. Không trần 1.000 ký tự, không trộn lệnh các challenge vào free talk. Không có test/điểm/gate.
- `review_links` chỉ là metadata tùy chọn. Có thể để `[]`; không xuất link từng từ ôn, không ép đối chiếu một-một với `learning-map.reuse`. Nếu chọn ghi link thì phải thật, không trỏ tương lai. Gối đầu là cân nhắc khi viết, không điều kiện hoàn thành.

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

Tool dùng Python với `jsonschema` từ 4.0 trở lên (cần validator Draft 2020-12); không tự cài dependency hoặc gọi model/network. Thư mục đích phải mới để tránh ghi đè bản đã duyệt hoặc bản đang xuất dở. Manifest chỉ xuất sau khi các file đã ghi xong; gói dở chưa có manifest không được đưa vào app.

Sổ nguồn, bằng chứng đã đọc, gối đầu và nhận xét biên tập tiếp tục ở revision workspace; không nhét các đường dẫn/note kỹ thuật đó vào nội dung user nhìn thấy.

## Khi chỉnh sửa

Giữ ID nếu vẫn cùng đối tượng; revision mới khi thay nội dung. `retired` khai báo những node/câu bỏ ở lần cập nhật, không dùng lại ID cũ cho ý khác. App giữ lịch sử và mapping riêng. Đổi title/order không đổi identity; sửa Việt không đòi skill tái tạo audio. Không thêm ID DB, asset URL hoặc progress learner vào source để khớp tạm một DB.

Khi sửa hợp đồng, đồng bộ generator/schema/example trong repo này và chạy regression. Bản chuẩn luôn ở repo lộ trình; mirror cũ ở Harumi được cập nhật trong task app sau này. Không sửa repo Harumi, chạy import hoặc EF migration trong task lộ trình.
