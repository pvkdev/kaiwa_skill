---
name: kaiwa-dialogue-double-check
description: Rà biên tập lần hai cho các chặng topic V11 đã có hội thoại Nhật–Việt. Đọc từng cảnh và từng nhánh, tự sửa lỗi có căn cứ, lưu tiến độ và kiểm lại đúng bản đã sửa. Dùng khi được yêu cầu double check hoặc hậu kiểm hội thoại đã soạn.
---

# Rà lần hai hội thoại Kaiwa V11

Mục tiêu là để người Việt mở riêng một tình huống, hiểu vai mình, nghe được lời đáp tự nhiên và tập nói đúng việc họ sẽ cần làm ở Nhật. Mặc định rà và sửa ngay trong phạm vi được giao. Nếu người dùng yêu cầu chỉ đánh giá, báo lỗi kèm UID và cách sửa, giữ nguyên dữ liệu và trạng thái. Một chặng tốt có thể qua lượt rà mà giữ nguyên toàn bộ lời thoại.

## Nhận chặng đã có

- Theo mã chặng, level hoặc batch mà người dùng chọn. Lấy thứ tự từ lộ trình và đối chiếu danh sách đã soạn trong `kaiwa_skill/planning/v11/BUILD.json` hoặc bản thảo đã có trên đĩa. Chặng chưa soạn thì báo thiếu. Khi chạy song song, mỗi chặng có một người sửa. Để gọi đây là lượt **độc lập**, giao cho người/phiên rà khác phiên đã viết chặng. Có thể dùng cùng model Sol/high. Ghi đúng vai trò khi tự rà lại.
- Đọc brief V10 bằng `py -X utf8 .agents/skills/kaiwa-topic-dialogue/scripts/dialogue.py S-023`, thay mã theo thực tế. Mở `dialogues.json` ở `v11/stages/<mã>/` hoặc `v11/pilot/<mã>/`. Giữ bản thảo tác giả làm nơi sửa chính. Đọc [hợp đồng bản thảo](../kaiwa-topic-dialogue/references/draft.md) khi sửa dữ liệu.
- Lấy mục tiêu, vai, kết quả dự kiến từ brief trước khi xem nhận xét cũ trong `RESEARCH.md` và `status.json`. Chữ “reviewed” ở hồ sơ tác giả ghi nhận vòng trước. Đọc trực tiếp **toàn bộ** cảnh thuộc phạm vi để đưa ra nhận định mới.

## Đọc và quyết định sửa

1. **Mở riêng từng cảnh.** Xem tiêu đề và bối cảnh như người mới mở app. Xác định điều người học cần tự nói và chỉ được đúng lượt họ làm việc đó. Đọc riêng mạch Nhật, tiếp đến đọc riêng mạch Việt, cuối cùng đặt cạnh nhau. Xem câu đáp có thực sự trả lời ý vừa hỏi, xưng hô có tự nhiên ở cả hai đầu, mức lịch sự có hợp trong/ngoài công ty, có chuyển nhầm chủ thể kính ngữ hay quyền quyết định. Kiểm vai phát từng câu và giọng TTS của cùng nhân vật xuyên sự kiện. Không suy giới tính từ nghề hoặc câu chữ.
2. **Nghe ý nghĩa người học mang đi.** Đối chiếu ai làm gì, điều kiện, thời hạn, lượng tiền, phủ định, mức chắc chắn và lời hứa. Ví dụ 「確認してからご連絡します」 là “Tôi sẽ kiểm tra rồi báo lại”. Dịch thành “Bên tôi đã duyệt rồi” làm đổi cả kết quả. Với tiếng Việt, đọc cả hai vai liền mạch để phát hiện cách gọi đổi bất chợt, câu dịch bám chữ, câu văn hành chính trong cuộc trò chuyện thân mật. Sửa ở ngôn ngữ có lỗi nếu ngôn ngữ còn lại đã đúng.
3. **Thử vai ở cấp độ thực tế.** Ở Sơ, nghe được câu cố định của nhân viên và tự đáp bằng câu vừa sức. Ở Trung, khi tình huống cần, người học phải có cơ hội giải thích, hỏi lại điều kiện hoặc chọn bước tiếp. Ở Thượng, xem cách xử lý hàm ý, lợi ích, trách nhiệm và quan hệ. Cảnh ngắn vẫn đạt nếu người học làm được việc. Giữ các nghi thức Nhật tự nhiên. Sửa khi cùng một lời kết, mẫu ngữ pháp hoặc sự lặp lại làm hỏng ý của cảnh. Chuyên đề phía trước có thể bổ trợ khi dùng đúng sắc thái.
4. **Đọc nối theo nhánh.** Đi từng đường `continues_from` trong brief. Đặt câu kết trước cạnh câu mở sau. Ai đã biết điều gì, ai mới đề nghị, việc nào đã được đồng ý, việc nào còn chờ? Khi quay về điểm rẽ, bắt đầu lại từ dữ kiện chung. Ví dụ một nhánh được cấp trên cho về sớm và một nhánh đang chờ trả lời phải dẫn tới hai cách đáp khác nhau. Với cảnh đứng riêng trong cùng sự kiện, giữ đủ bối cảnh và sự nhất quán của nhân vật, tránh tự nối các cảnh chỉ vì chúng đứng cạnh nhau.
5. **Kiểm căn cứ cho điều được dạy.** Khi câu phụ thuộc một đoạn sách, mở đúng đoạn trong `admin_sources`. Kiểm câu trích nguyên, ý chuyển soạn và lời AI viết mới. Với y tế, an toàn, cư trú, quyền lợi, tiền, hợp đồng hoặc quy định của nhà cung cấp, đối chiếu từng khẳng định có thể làm học viên hành động sai với nguồn chính thức đúng phạm vi và còn áp dụng. Ghi URL, ngày xem, phạm vi ở phần quản trị. Nếu chưa xác minh được, cho nhân vật hỏi đúng cơ quan hoặc nêu điều kiện cụ thể khi vẫn đạt mục tiêu nói. Nếu còn nghi vấn ảnh hưởng kết quả, ghi `needs_fix` cùng câu hỏi còn mở rồi tiếp tục các cảnh khác.

**Khi sửa**, chọn thay đổi nhỏ nhất xử lý được lỗi. Có thể sửa bối cảnh, đổi từ, thêm lượt người học cần nói, hoặc viết lại cả cảnh khi hai vai đang diễn sai việc. Giữ nguyên UID V10, mục tiêu, thứ tự và quan hệ nhánh. Giữ ID của lượt còn cùng nghĩa, cấp ID mới cho lượt mới và cập nhật `admin.turn_origins`. Một câu trích đã đổi tiếng Nhật phải được phân loại lại theo căn cứ thực dùng. Giữ tên sách, mã cảnh, tên level và lời bàn biên tập trong hồ sơ nội bộ. Sau sửa, đọc lại cả cảnh ở hai ngôn ngữ, đọc các nhánh đi qua phần chung vừa đổi, kiểm lượt trước/sau và kết quả mới. Mâu thuẫn nằm trong brief V10 thì ghi đề xuất cho chủ lộ trình và để mở phần bị ảnh hưởng.

## Checkpoint và bàn giao

Từ gốc repo chạy lệnh sau để lấy phiếu trống ra stdout. Công cụ dùng validator V11 sẵn có và chỉ đọc dữ liệu. Nếu báo lỗi cấu trúc, đối chiếu brief và sửa lỗi trong bản thảo trước khi tạo phiếu. Trường hợp có hai bản cùng mã, xác định bản tác giả đang được bộ dựng dùng trước khi rà.

```powershell
py -X utf8 .agents/skills/kaiwa-dialogue-double-check/scripts/review.py S-023
```

- Lưu phiếu biên tập riêng ở `kaiwa_skill/planning/v11/reviews/<mã>/review.json` theo UTF-8. Lần đầu ghi `reviewer` là phiên/người rà thực tế và `input_sha256` là SHA-256 byte của bản thảo lúc nhận. Lần tiếp tục đọc phiếu đang có. So hash với phiếu trống hiện tại để biết cảnh và sự kiện cần mở lại. So hồ sơ nguồn/web và điểm nghi vấn đang mở khi tiếp quản.
- Với mỗi UID, ghi `kept`, `fixed` hoặc `needs_fix`, một `turn_id` có thật và `note_vi` ngắn về quyết định. Ví dụ “Khách xin giữ hàng, nhân viên chỉ hẹn gọi lại sau khi hỏi kho” giải thích được tại sao cảnh đạt. Với lỗi đã sửa, ghi vấn đề trước sửa và nghĩa đúng sau sửa. Với mỗi sự kiện, ghi `read` cùng điểm nối/điểm rẽ đã kiểm sau khi đọc hết các cảnh liên quan, kể cả sự kiện chỉ có một cảnh. Để `pending` ở phần chưa đọc.
- Sau từng sự kiện, kiểm bản trên đĩa vẫn đúng bản mình đang biên tập. Lưu thay file nguyên tử theo thứ tự bản thảo, hồ sơ tác giả, phiếu rà. Khi nội dung đổi, cập nhật hash bản thảo và các hash cảnh/nguồn có liên quan theo dạng sẵn có của `status.json`, cập nhật ghi chú bị thay thế và lưu dấu vết vòng cũ. Chỉ chép hash mới vào phiếu lần hai sau khi đã đọc lại nội dung tương ứng. Việc thay cả phiếu bằng bộ hash mới sẽ làm mất căn cứ resume. Khi dừng giữa hai lần ghi, lấy nội dung trên đĩa làm mốc và rà lại phần lệch cùng các nhánh phụ thuộc.
- Kiểm kết quả bằng lệnh dưới. Thiếu UID, dấu vân tay cũ, tham chiếu lượt sai hoặc phần còn mở đều chưa đạt. Công cụ đối chiếu dấu vân tay và độ phủ, chất lượng ngôn ngữ do người rà chịu trách nhiệm.

```powershell
py -X utf8 .agents/skills/kaiwa-dialogue-double-check/scripts/review.py S-023 --check kaiwa_skill/planning/v11/reviews/S-023/review.json
```

Chỉ ghi `independent_review: completed` khi đúng là lượt độc lập, mọi sự kiện đã đọc, không còn lỗi mở và lệnh kiểm thành công. Khi sửa sau mốc đó, xét lại theo hash. Khi có sửa lời cho học viên, điều phối dựng lại preview bằng `tools/roadmap_v11.py` với batch lũy kế đang dùng, xem đúng chặng, đối chiếu vai/JA/VI với bản tác giả. Thêm `--publish` khi cập nhật bản Pages trong repo. Bộ dựng hiện gán nhãn rà theo nhóm pilot/batch, vì vậy lấy phiếu khớp hash làm căn cứ báo cáo, giữ báo cáo sản xuất cũ như mốc lịch sử. Bàn giao số cảnh giao/đã đọc/giữ/sửa/còn mở, các lỗi ảnh hưởng việc học, mã chặng có thể mở trong preview và điểm tiếp tục nếu còn dở.
