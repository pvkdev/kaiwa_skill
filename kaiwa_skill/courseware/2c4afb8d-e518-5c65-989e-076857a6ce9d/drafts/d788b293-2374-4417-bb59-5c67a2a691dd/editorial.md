# Nhật ký biên tập — T-001

## Phạm vi và lộ trình

UID `2c4afb8d-e518-5c65-989e-076857a6ce9d`, V5 display `T-001`, mức Trung. Mục tiêu: bắt chuyện trong lớp/nhóm và sự kiện, phản hồi theo chi tiết vừa nghe, kể về mình vừa đủ, đặt ranh giới riêng tư, gặp lại, khép lời và giữ đường tiếp. Không lặp bài tự giới thiệu Sơ như mục tiêu chính. Năm sự kiện V5 được thể hiện bằng 25 hội thoại cụ thể, 5 challenge có nhánh AI và một free talk cuối. Đây là độ phủ theo nhu cầu của chính chặng, không phải quota cho các chặng khác.

## Tìm và chọn nguồn

Đã quét `catalog27/source_index.jsonl` đủ B01–B27, 22.110 entry; sổ `sources.json.scan` phân biệt index_only/read. Đã đọc trọn B11 bài 70 và 73, B27 skit ① của bài 出会い trong script phụ lục. Có đọc B14 Unit 1 Section 6 để cân nhắc, nhưng pack thiên về giới thiệu cơ bản Sơ nên không đưa vào Trung. B08, B09, B13 và các sách khác được tra heading, không gọi là đã đọc nội dung. B11 bài 67 được xem, nhưng toàn pack lan sang quà sinh nhật, rượu, sukiyaki, công việc nên không hợp nguyên pack T-001. B11 70 và 73 giữ đủ hội thoại mở đầu, câu đối chiếu và các cặp luyện trong từng CD. B27 skit ① 1-2 giữ đúng 14 lượt; skit ② 1-3 mở sang quan hệ/độ khó khác nên là pack độc lập, không cắt đôi một track.

Inventory độc lập: `catalog27/audio_packs/B11/u-88-part2-70.json`, `B11/u-88-part2-73.json`, `B27/l01-skit-1-2.json`. Ranh giới dựa nhãn bài/track trong bản clean và thứ tự script, không dựa câu đã chọn từ draft. `source-map.audio_packs` pin SHA-256 inventory và ID toàn bộ lượt. Không nghe file CD, không xác nhận file audio thật hoặc giọng thu. Chỉ ghi nhãn track in trên sách; nhãn đĩa chưa xác minh là `unknown`.

Nghiên cứu ngoài: JF Can-do B1 mục 196 nêu cuộc nói ở tiệc/nhóm mới có câu hỏi về sở thích/công việc và câu trả lời đủ chi tiết để duy trì trao đổi; Irodori 初中級 L8 đặt lời bắt chuyện vào lớp/nhóm và bối cảnh thực. Đây là căn cứ thiết kế mục tiêu/chức năng, không gán bất cứ câu AI mới nào cho hai nguồn này. URL và locator nằm ở `sources.json`/`source_registry`.

## Thiết kế mạch và nhánh

- E01 lớp/nhóm: hỏi từ việc chung, hỏi thời gian tham gia, tự kể lý do, đính chính hiểu nhầm vai, nối tên và buổi sau.
- E02 sự kiện: kinh nghiệm tham dự, cảm nhận khác nhau, người kia chờ bạn, muốn xem một mình, tình cờ gặp lại ở gian khác.
- E03 giới hạn riêng tư: chọn mức kể quê quán, đổi từ nghề sang sở thích, tự xin lỗi khi hỏi sâu, người học giữ chuyện cá nhân, hai bên gặp chủ đề chung.
- E04 lần gặp thứ hai: nhớ sách/tranh, chấp nhận việc dự định chưa diễn ra, nhận sửa khi nhớ nhầm, lời mời hoạt động chung được nhận hoặc đi riêng bị từ chối.
- E05 kết thúc: cảm ơn chi tiết cụ thể, liên lạc khi hai bên muốn, tôn trọng lời từ chối, kế hoạch buổi sau chưa chắc, gặp lại thật và hỏi tiếp.

Các tình huống là nội dung nói hai vai hoàn chỉnh, không bài viết hay bài test. Nhánh từ chối/đang bận có hậu quả nói tiếp riêng; `follows` và `alternative_to` là liên kết truyện, không cổng mở khóa. Nội dung mới đều `original_extension`, câu sách đều `source_quote`; kiến thức giải thích bài gốc là `source_adaptation` ở mức node, nhưng câu trích giữ nguyên.

## Rà từ và ngữ pháp

Ba list từ được rút ngược từ lượt hội thoại thực. `source-map.vocabulary_evidence` ghi surface và utterance cho mỗi từ, đã kiểm: `参加されている → 参加する`, `続けよう → 続ける`, `選ばない → 選ぶ`, `取り違えて → 取り違える`, `立ち入った → 立ち入る`, `親しく → 親しい`, `確かめたかった → 確かめる`. Không thay câu nói thành thể từ điển. Tên grammar lấy đúng `MINNA_01_50_GRAMMAR.json`, trong đó bài 19/21/25/26/31/32/35/39; gán N4 theo độ khó sơ cấp cao đã rà cho mục admin pick, không coi đây là bảng JLPT chính thức. Một số câu nguồn B27 dùng khẩu ngữ `なんか`, `〜って`, `〜んで`, `そーお` để nhận diện khi nghe; bài k27 nêu ranh giới dùng với người mới. Không bắt chước nguyên mức thân mật khi chưa có quan hệ.

## QA trước khi chốt

Chưa chốt. Cần sync, đọc `stage-preview.md`, `knowledge/k70.md`, `knowledge/k73.md`, `shadowing` và các nhánh; đối chiếu audio-index với ba inventory, rà một lần Nhật–Việt, điều kiện Live, thứ tự node và tên grammar. Script chỉ kiểm cấu trúc/nguyên văn đã pin; không chứng minh tự nhiên hay chất lượng dịch. Không có đánh giá chất lượng âm thanh vì chưa nghe CD.
