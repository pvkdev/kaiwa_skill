# Harumii Kaiwa Exchange 1.0.0

Quyết định ngày 2026-11-13 theo yêu cầu chủ app. Đây là **hợp đồng đầu ra của skill và đầu vào của feature Kaiwa Curriculum mới**, không phải mô tả API/DB hiện đã triển khai. Không thay đổi 289 chặng V5. Thiết kế không có bài thi, điểm, điều kiện mở khóa hoặc ép người học theo thứ tự.

Nguồn chuẩn ở repo skill: `kaiwa_skill/contracts/harumii-kaiwa/v1/`. Schema được sinh từ `kaiwa_exchange.py::schemas()`; thay cấu trúc phải cập nhật generator, schema và fixture tại đây. Mirror Harumi trước đó chỉ là bản bàn giao; theo phạm vi mới, không cập nhật repo app trong task lộ trình. Khi build app sau này lấy lại bản chuẩn này. Bổ sung trước pilot: grammar bắt buộc có `jlpt_level` N5–N1; đây là điều chỉnh hợp đồng chưa phát hành production, không phải migration dữ liệu người học.

## 1. Ranh giới và đơn vị chuyển dữ liệu

- **Catalog** mô tả thứ tự/chặng/cụm/cấp độ của lộ trình; không chứng minh chặng đã có nội dung.
- **Stage** là một snapshot nội dung đầy đủ của **một chặng**, gồm nhiều node có thứ tự, các câu Nhật–Việt dùng chung và các liên kết. Import từng chặng, không phải đưa toàn bộ 289 chặng vào một transaction.
- **Manifest** có SHA-256 của các file trong artifact; entrypoint là `catalog.json` hoặc `stage.json`. DB importer đọc entrypoint; các MD là preview/context dẫn xuất, không là dữ liệu gốc thứ hai.
- JSON import có nguồn và chỉ dẫn tra CD dành riêng cho admin. Sổ biên tập, checkpoint, script gốc và file âm thanh nằm ngoài gói import.

Thư mục xuất dự kiến:

```text
harumii_export/catalog-v5/                 catalog.json + manifest.json
harumii_export/<stage_uid>/r0001/          stage.json + manifest.json
                                         knowledge-*.md
                                         challenge-<id>-<variant>.learner.md
                                         challenge-<id>-<variant>.ai.md
                                         free-talk-situation.md
```

Không có asset âm thanh, furigana, URL máy cá nhân hoặc ID DB Harumi trong gói. Importer xác nhận hash **byte gốc** trước parse. Không deserialize rồi serialize lại để kiểm hash. File xuất UTF-8 không BOM, LF. JSON reformat có thể đổi hash; cùng revision chỉ chấp nhận đúng artifact đã chốt. `manifest.json` không tự băm chính nó; importer chỉ chấp nhận file trong allowlist, tên file phẳng, không truy cập đường dẫn do file gói cung cấp.

## 2. ID, revision và thứ tự

- `course_id`: namespace ổn định, mặc định `kaiwa-main`.
- `stage_uid`: UUID đã có trong registry V5. Không dùng tên sách/chặng hoặc `display_code` làm khóa.
- `revision`: số nguyên tăng dần, `1` tương ứng thư mục `r0001`; **không phải schema version hoặc V5**.
- Node và câu có `id` ổn định bên trong chặng. Khóa trao đổi lần lượt là `(course_id, stage_uid, node.id)` và `(course_id, stage_uid, utterance.id)`.
- Turn/item/variant có ID trong phạm vi node cha. Mỗi lượt có thứ tự theo vị trí trong mảng; không thêm trường order có thể mâu thuẫn với mảng.
- Thứ tự chặng lấy từ `catalog.stages[].order`; thứ tự node, lượt thoại, mục shadowing lấy từ mảng. Thay thứ tự không đổi ID và không reset lịch sử học.
- Cùng một đối tượng thì giữ ID khi sửa câu. Đổi bản chất thì dùng ID mới; `retired` ghi ID cũ, lý do và ID thay thế nếu có. Không tái dùng ID đã nghỉ cho đối tượng khác.
- Tên/level/display code lặp ở catalog và stage phải khớp bản catalog đang dùng khi activate. Sửa bằng một bản catalog mới khi cần; không tự tạo stage khác do đổi tên.
- `retired` mô tả những identity bỏ ở lần cập nhật này; lịch sử retire nằm trong các snapshot/DB. Không bắt danh sách retire cũ trỏ mãi tới một replacement vẫn còn active ở mọi revision sau.

Schema version 1.0.0 độc lập với curriculum V5 và hợp đồng biên tập 3.2. V1 là full snapshot, không phải JSON Patch. Field lạ bị từ chối; thay đổi phá vỡ schema phải tăng major. Không tự đoán schema khi import.

## 3. Từ vựng và ngữ pháp

`vocabulary.data.terms_ja` **chỉ là mảng chuỗi Nhật**: ví dụ `["会議室", "予約", "変更"]`. Không cần nghĩa, reading, Hán Việt, ảnh, audio, example hoặc ID dictionary. Cắt khoảng trắng hai đầu, giữ dạng từ người biên soạn đã chọn; không tự gộp đồng âm/đồng nghĩa khác cách dùng. Chặn trùng chuỗi trong cùng danh sách; từ xuất hiện lại ở chặng/bài khác có thể là ôn có chủ ý.

Từ được trích ngược từ hội thoại/câu luyện thực có trong chặng; động từ dùng thể từ điển, tính từ dùng dạng cơ bản. Không sửa lời thoại theo mục từ. Dấu vết surface → lemma và nơi xuất hiện lưu ở metadata biên tập; app vẫn chỉ cần list Nhật.

Harumii dùng list này để tạo draft danh sách từ qua hệ thống sẵn có; enrichment và xác nhận thuộc app. Lưu binding của node/list và từng term ở phía app. Import lại không sinh lại list nếu dữ liệu không đổi; thay list tạo revision/bản nháp mới, không xóa SRS hoặc danh sách người học đã lưu.

`grammar.data.patterns` có `{catalog: minna|bunpou, jlpt_level: N5|N4|N3|N2|N1, name_ja}`. Không cần giải thích, ví dụ hoặc ID DB. Admin tìm theo level + tên và lưu binding riêng. Chỉ đưa tên khi đã tra được nguồn thật; không bịa bunpou ID. Một tên có thể có nhiều kết quả tìm; không tự chọn kết quả đầu tiên. Level ưu tiên metadata đã xác minh; mapping biên tập từ Minna phải ghi căn cứ ở sổ nguồn, không gọi là danh mục JLPT chính thức và không quy đổi cứng từ số bài.

Mapping ngữ pháp chờ admin là `pending`, không coi là lỗi dịch hoặc tự tạo grammar mới bằng AI. Khi text tên đổi, mapping cũ chuyển `needs_review` thay vì âm thầm áp vào tên mới. Không khóa cả chặng/người học vì mapping chưa xong; admin có thể tạm chưa bật node grammar, các node nội dung khác vẫn dùng được.

Đây là yêu cầu tối giản của **gói app**. `sources.json`/`learning-map.json` vẫn được giữ ở repo để theo dõi nguồn và ôn gối đầu; không bắt soạn thêm nghĩa từ chỉ để rồi bỏ khi export.

## 4. Mọi câu Nhật luyện tập có nghĩa Việt, dùng một kho câu

`utterances` chứa `{id, ja, vi}`. Hai chuỗi bắt buộc, không furigana/HTML ruby, không audio field. Nội dung Nhật là dạng hiển thị/TTS chính; app tự xử lý furigana và TTS.

Gói mới có `source_registry` nhẹ (ID, loại, tên sách/nguồn, locator), và từng câu có `authorship: source_quote|source_adaptation|original_extension`, `source_refs`, có thể thêm `source_locator`. `source_quote` nói về chữ Nhật giữ đúng nguồn; nghĩa Việt vẫn được biên tập cho đúng. Không gán câu viết mới thành trích nguyên nguồn. Node/câu có thể đánh dấu `learning_scope: core|source_reference`; ví dụ nguồn khó hơn được nhận diện là tham khảo, kèm `grammar_node_ids` nếu cần tra. Các trường mới tùy chọn để đọc snapshot cũ; nếu có source_registry thì validator bắt đủ nguồn gốc từng câu.

Một câu được dùng trong kiến thức, shadowing, hội thoại và gợi ý challenge thì **tham chiếu cùng ID** khi đúng là cùng câu/cùng nghĩa. Không chép lại hai bản phải sửa song song. Cùng Nhật nhưng nghĩa/ngữ cảnh Việt khác có thể là hai câu riêng; không tự dedupe theo chữ Nhật hoặc gộp mọi câu giống nhau xuyên chặng. App có thể tái dùng cache TTS theo chữ Nhật mà không gộp nội dung học.

Một utterance là một đơn vị nói tự nhiên để phát/check; tránh gom cả đoạn dài. Một lượt thoại có thể dài hơn một câu khi cần ngữ dụng. Skill không tạo điểm hay luật phát âm.

**Ngoại lệ không phải câu luyện:** từ trong list, tên mẫu ngữ pháp và tên riêng không cần một dòng Việt trong utterance bank. Mọi ví dụ/câu thoại/hint tiếng Nhật cần luyện phải vào kho câu. Câu tự do do AI tạo trong Live không thuộc artifact tĩnh.

## 5. Bảy loại node

### Knowledge

Mỗi node kiến thức trong gói xuất mới có `data.admin_provenance`. Trường này chỉ phục vụ tra cứu trong admin/import, tách khỏi mọi chữ người học thấy và ngữ liệu Live. Đọc snapshot trước thay đổi vẫn được khi trường vắng mặt.

- `authorship` mô tả phần giảng. `source_refs` liệt kê nguồn của bài và ví dụ; tra từng ID trong `source_registry` để lấy loại, tên sách đầy đủ, mã sách và vị trí. Bài hoàn toàn tự soạn dùng `original_extension` và hai mảng rỗng.
- `cd_refs` chứa các mục gồm `source_ref` của đúng sách, `disc`, `track` và `locator`; có thêm `pack_id` và `edition` với pack đã kiểm kê. Giá trị `unknown` ghi nhận phần chưa xác định trong một CD có bằng chứng. Mảng rỗng nghĩa là chưa có chỉ dẫn CD áp dụng cho bài này.
- API cho người học chỉ chọn trường cần hiển thị. Không gửi nguyên snapshot quản trị vào màn hình học hay prompt Live. Chế độ kỹ thuật của HTML preview dành cho chủ dự án xem JSON.

`body_md` là bài kiến thức Markdown tiếng Việt. Chèn ví dụ qua token `{{utterance:u01}}`; renderer thay token bằng câu Nhật + nghĩa Việt và có thể gắn nút TTS/furigana. `utterance_ids` khai báo đúng các token dùng trong bài. Không cài HTML tùy ý để nhúng media; app render Markdown an toàn. Tên mẫu/từ Nhật trong diễn giải vẫn có thể viết trực tiếp, nhưng không viết câu ví dụ Nhật nằm ngoài kho câu.

`source_family=speak_japanese` yêu cầu `video_status=planned`, `practice_node_id` trỏ node shadowing **ngay sau**, và bài luyện bao phủ các ví dụ của bài kiến thức. Video thật do admin gắn riêng trong app; skill không bịa URL hoặc yêu cầu upload video để import. `video_status` trong gói chỉ là ý định biên soạn, không ghi đè asset video app đã gắn.

### Vocabulary / Grammar

Theo mục 3. Có thể có nhiều node list theo cụm tình huống hoặc một list chung tùy nội dung.

### Situation

Một sự kiện và một diễn biến/kết quả cụ thể. Hai vai A/B có nhãn/vai Việt; mỗi turn có ID, speaker ID và utterance ID. Cả hai vai phải thực sự nói. `follows` cho nối tiếp thời gian, `alternative_to` cho nhánh thay thế; không dùng hai trường như prerequisite.

App lấy cùng hội thoại để shadowing toàn bộ hoặc đóng một vai rồi đổi vai. Không lưu hai bản dialogue cho hai chế độ, không gán mặc định giới tính/giọng do skill quyết. App chọn giọng cho từng vai.

### Shadowing

`items` có câu đơn (`utterance_id`), tham chiếu tình huống (`situation_node_id`) hoặc hội thoại luyện ngắn `kind=dialogue` gồm title, hai speakers và turns trỏ utterance IDs. Đoạn nguồn chỉ phục vụ một nhóm shadowing có thể đặt ngay trong nhóm, không tạo thêm bước học riêng để đáp ứng cấu trúc kỹ thuật. Nếu đã có tình huống độc lập thì dùng ref thay vì copy. Lời Nhật–Việt vẫn chỉ có một bản trong utterance bank. B01/必須700/Nama/なめらか/Shadowing dùng đúng chất liệu luyện ở đây; B11/B12 nối ngay sau kiến thức/video.

### Live challenge

`learner_brief` chứa bối cảnh, hai vai, mục tiêu và gợi ý bước, danh sách node từ/ngữ pháp có thể dùng, hint qua utterance IDs. `ai_situation_vi` là chỉ dẫn nhập vai riêng, không hiện thay brief. `context_node_ids` chọn tài liệu đã xuất hiện trước node; đây là mạch biên soạn, không khóa user mở challenge sớm.

`variants` có base prompt chung và phụ lục cho **một variant đã chọn**. Chỉ ghép `ai_situation_vi + variant.ai_addendum_vi + tài liệu được chọn`; không ghép tất cả variant cùng lúc. Brief cuối = brief chung + learner addendum của variant, không lộ addendum dành AI. Giữ ID/revision/variant trong snapshot phiên Live. Một đối tác mỗi cuộc gọi; thay đối tác thì node challenge khác.

Goal là nhiệm vụ giao tiếp, không có pass/fail hoặc exact-match câu. AI phản hồi theo nghĩa, trợ giúp, cho user dừng/đổi hướng; không tự đóng call khi checklist xong. Không có trần 1.000 ký tự của text user nhập tay.

### Free talk

Đúng một node cuối chặng. Có sẵn `ai_situation_vi` tổng hợp riêng theo chặng, giới thiệu và gợi ý tùy chọn. `context_node_ids` phải gồm **mọi node tài liệu học theo đúng thứ tự node**, không chứa Live challenge/free talk. App hydrate các câu và ghép tài liệu để AI có toàn bộ chất liệu chặng; không nạp chỉ dẫn nhập vai/nhánh kín của các challenge.

Không coi user đã học thuộc mọi node. Theo hướng user muốn nói, cho phép mở rộng ngoài topic. File `free-talk-situation.md` được tạo sẵn để preview hoặc nạp context; `stage.json` vẫn là nguồn chuẩn. Không rút kiến thức để vừa form nhập tay.

## 6. Catalog, nhóm bài và ôn gối đầu

Catalog khai báo đủ 289 chặng có thể import trước khi soạn nội dung; app phân biệt `outline_only` với `content_available`. Không sinh bài placeholder hoặc giả có kiến thức.

`lessons` chia node tài liệu theo thứ tự, không lấy Live thành bài kiến thức mới. Gối đầu là cân nhắc vận dụng kiến thức/từ/ngữ pháp cũ vào lời thoại mới nếu tự nhiên, không yêu cầu đọc/tái dùng đủ hai bài trước. `review_links` có thể để `[]`; không cần xuất sổ từ ôn hoặc đồng bộ từng dòng với learning-map.reuse. Nếu ghi liên kết cụ thể thì source/node/revision phải có thật và đứng trước; không giả vờ đã đọc hoặc đã dạy. Không bắt ghi debt khi bài trước chưa tồn tại.

Không import `learning-map.json` như tiến độ user. Tiến độ người học là dữ liệu riêng của app, không có trong file nguồn.

## 7. Thiết kế lưu DB cho feature mới — quyết định logic

Đặt dữ liệu nội dung và import trong **Harumi.Learning**, cùng miền sở hữu học liệu; gọi Dictionary/ChatPractice qua interface hoặc event. Các tên sau là **bảng/entity mới được thiết kế**, chưa tồn tại trong code:

- `KaiwaCurriculum`: ID nội bộ + `CourseKey` unique; revision catalog hiện hành.
- `KaiwaCatalogVersion`: snapshot catalog, raw artifact hash, metadata revision/roadmap, trạng thái draft/active; giữ lịch sử đổi thứ tự.
- `KaiwaStage`: GUID nội bộ, curriculum ID, `SourceStageUid`; unique cặp. Giữ ID xuyên revision.
- `KaiwaStageVersion`: stage ID + `SourceRevision` unique; schema version, artifact SHA-256, JSONB snapshot đầy đủ, trạng thái draft/published/archived. Snapshot là nguồn nội dung bất biến, không sửa hàng đã publish.
- `KaiwaNodeIdentity` và `KaiwaUtteranceIdentity`: GUID nội bộ + stage ID + source local ID unique. Độc lập với revision để giữ progress/bindings. Index/materialization của payload theo revision là projection, không tạo bản nội dung gốc thứ hai.
- `KaiwaNodeBinding`: node identity + loại binding (vocab list/grammar pattern/video) + nguồn/term/name fingerprint + target ID; trạng thái pending/resolved/needs_review. Một grammar node có nhiều pattern bindings; khóa thêm `(catalog,name)` hoặc fingerprint. Vocab binding có list target và tập term đã xử lý, không chỉ một cờ cho cả list.
- `KaiwaImportRun`: idempotency key, request hash, trạng thái, checkpoint, expected current version, diff/binding warnings/error report. Không phải trạng thái học của user.

Payload typed JSONB là đủ để giữ đúng thứ tự/nhánh và cấu trúc bảy node mà không ép vào schema bài tập cũ. Có thể thêm projection truy vấn, nhưng phải tái dựng được từ snapshot. Không ghi trực tiếp vào schema Dictionary/ChatPractice, không lạm dụng `LearningPathUnitTask.ConfigJson` làm kho payload chưa có hợp đồng.

Nếu cần đưa chặng vào màn hình roadmap hiện có, một adapter/projection liên kết stage identity/version với path/unit/task hiện hành. **Không bắt buộc mỗi chặng phải có VocabCurriculumId/GrammarCurriculumId** như LearningPath hiện tại, không tạo curriculum giả để thỏa khóa ngoại. Domain extension/projection là công việc build feature sau, không chạy migration DB ở task thiết kế này.

## 8. Input import phía app và xử lý cập nhật

Admin cung cấp artifact folder/zip (hoặc JSON entrypoint + các file manifest), target course, idempotency key và `expected_current_revision` ở lệnh commit. Body học liệu **đúng schema trong repo skill**, không đổi tên field sang DTO khác. C# có thể dùng PascalCase nội bộ với JSON attribute; wire JSON giữ snake_case thống nhất.

Luồng import dự kiến, chưa phải endpoint đang tồn tại:

1. **Preview:** đọc/kiểm file, schema, hash, trùng ID, liên kết, diff với snapshot hiện hành, grammar pending, thay đổi list/từ/câu, và mapping catalog. Chưa ghi published content, chưa gọi TTS hoặc AI. Lưu một kế hoạch commit/preview hash có thời hạn để dùng đúng nội dung đã review.
2. **Commit:** xác nhận preview hash + expected revision; trong transaction một stage, upsert identity, ghi snapshot version, binding pending và outbox cho phần enrichment cần thiết. Không gọi dịch vụ AI bên trong transaction. Không xóa progress/media của revision cũ.
3. **Curation:** app build danh sách từ qua engine hiện có; admin pick grammar; gắn video/chọn voice nếu cần. Lỗi enrichment có thể retry từng node, không import trùng cả chặng.
4. **Publish:** admin chọn bản đủ dùng; có thể chưa bật node binding còn pending. Không đồng nghĩa bài kiểm tra hoặc unlock người học. Đang học một phiên thì pin version; phiên mới dùng published version.

Idempotency:

- Cùng key + cùng request hash: trả kết quả cũ. Cùng key + body khác: conflict.
- Cùng stage/revision + cùng artifact hash: no-op. Cùng revision + hash khác: conflict, yêu cầu tăng revision; không sửa dữ liệu đã import.
- Revision mới không tự activate/publish và không được làm current lùi về bản cũ. Rollback là thao tác chọn lại snapshot đã có của admin.
- Hai commit cùng expected revision: chỉ một thành công (optimistic concurrency + unique DB constraints).
- V1 là full snapshot. Node/câu biến mất so với snapshot trước phải có `retired` rõ; retire không xóa lịch sử. Chỉ áp snapshot của stage đó, không xóa các stage không có trong một batch.
- Nội dung nhập là source-managed: sửa kiến thức/hội thoại qua revision mới từ skill. Các chọn lựa app (vocab/grammar/video/voice) ở binding/asset riêng, không bị import ghi đè. Nếu app cho sửa trực tiếp nội dung nhập, phải fork namespace/stage hoặc xuất ngược revision theo workflow riêng; không để silent drift giữa source và DB.

Import status như pending/resolved là trạng thái biên tập, không phải test/grade của learner.

## 9. TTS, furigana, media và Live

- Import không gọi TTS cho hàng nghìn câu ngay. App enqueue/lazy-generate theo cách build feature; cache key ít nhất có provider/model/voice/version settings và hash text Nhật chính xác. Không dùng riêng utterance ID làm cache key vì câu có thể sửa.
- Sửa Việt không làm hết hạn TTS Nhật; sửa Nhật hoặc voice/settings thì tạo asset generation mới. Media cũ giữ để snapshot cũ còn hoạt động. Furigana cache tương tự theo hash Nhật + tokenizer/version.
- App chọn voice theo vai/mục luyện. Không bake male/female hoặc vendor voice vào artifact. Không giả định giới hạn 10 câu của entity pronunciation cũ áp vào shadowing mới.
- Giữ sentence ID + text hash trong job để job cũ hoàn tất không gắn nhầm vào revision đã sửa. Retry theo generation key để tránh tạo trùng asset hoặc chi phí.
- Learning gửi ChatPractice một context đã resolve/pin version, challenge ID/variant hoặc free talk ID qua interface nội bộ mới. ChatPractice tiếp tục sở hữu phiên/token/nhân vật. Không cho client gửi nội dung rồi tự gắn cờ trusted; server xác minh node/version từ học liệu đã publish.
- Tách route/adapter nội dung lộ trình khỏi customize text user nhập. Nội dung do tác giả soạn vẫn tuân thủ prompt gốc và chính sách app, nhưng không chịu trần nhập tay 1.000 ký tự. Compiler chỉ ghép một variant và các node context đã chọn; không nhét mọi nhiệm vụ vào cùng call.

## 10. Nghiệm thu hợp đồng

JSON Schema kiểm hình dạng; `kaiwa_exchange.py validate` kiểm thêm ID/thứ tự/liên kết, cặp Speak Japanese, vai thoại, free talk và hint. Script không chứng minh bản dịch đúng, dữ kiện thật, đã đọc sách hoặc đoạn Nhật tự nhiên; tác giả phải đọc lại.

`example-stage.json` dùng fixture giả định, bao phủ đủ bảy node, hai variant và reuse câu giữa bài/video-shadowing-hội thoại-hint. Không phải bài học thật hoặc nguồn sách.

App khi build cần chạy cùng fixture: preview → commit lại không trùng → revision mới chỉ cập nhật phần thay đổi → grammar cần admin → TTS lỗi retry → pause/resume import → rollback giữ progress. Đây là kiểm thử feature/import, không phải bài kiểm tra người học.

Không build/import production, không gọi TTS, không publish course hoặc chạy EF migration chỉ vì chốt hợp đồng này. Đầu ra hiện tại là schema, example, validator/packager, rule skill và bản thiết kế DB/import phía Harumi.
