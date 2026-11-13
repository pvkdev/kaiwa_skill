# Nhật ký biên tập H-050

Đã quét profile đủ 27 cuốn bằng BOOK_GUIDE, rồi đọc sâu B09 §21, B10 bài 5, B21 bài 4. B09 §21 là pack 用例 ba hội thoại/14 lượt, có manifest mới; phần thứ ba luyện việc nói rõ vấn đề sau cách nói để ngỏ. B10/B21 hỗ trợ mạch từ chối và thương lượng, không gán câu mới thành lời sách. Đã đọc Can-do của Japan Foundation để đặt mục tiêu hành động, không lấy câu thoại.

Bản đồ sự kiện: lời nhờ mơ hồ → hỏi phạm vi và quyền quyết; cân nhắc → nhận một phần/từ chối/chờ; bị ép → đính chính lời chưa cam kết và giữ ranh giới; đã nhận → phát sinh và đổi hạn; bàn giao → nêu việc xong/chưa xong; gặp lại → giữ quan hệ mà không hứa bù. Ưu tiên nhánh có hậu quả và cuộc nói tiếp, không triển khai máy móc toàn bộ 30 nhãn seed.

Cần tiếp: soạn canonical, source-map và learning-map; rà sâu tiếng Nhật/Việt, track, admin registry, grammar rồi sync/validate/finalize/pack.

## Đối chiếu hạt giống V5 và quyết định gộp

- E01 S001–S003: s01 hỏi kết quả thật, s02 hỏi hạn/quyền quyết, s03 chỉ hẹn trả lời khi có lịch. S004 được s06 cụ thể hóa thành không nhận vai phân xử vượt thẩm quyền. S005 nằm ngay trong lời chốt s03: chưa hứa nhận.
- E02 S006–S010: s04 nhận phần nhỏ, s05 nhận việc đã rõ và hẹn cập nhật, s06 từ chối có lý do thật, s07 giới thiệu người khác sau khi xin phép. Tình huống “người kia tự làm bước khác” được tích hợp vào s04 qua việc quyết thay đổi; không tách một cảnh chỉ để đổi tên trách nhiệm.
- E03 S011–S015: s08 giữ câu không khi bị nài, s09 sửa lời gợi ý bị hiểu là cam kết, s10 chỉ bàn lại vì phạm vi giảm thật, s11 kết thúc khi chưa có phương án. Chưa làm riêng cảnh chỉ lặp giới hạn vì s08 đã có diễn biến đó.
- E04 S016–S020: s12 báo phần mới, s13 thêm việc với điều kiện dời hạn, s14 giữ phần cũ/từ chối phần mới, s15 chuyển quyết định cho người phụ trách. Việc chốt phạm vi mới nằm trong câu cuối s13; không dựng cảnh thứ hai chỉ để nhắc lại cùng một thỏa thuận.
- E05 S021–S025: s16 nêu phần xong/chưa xong, s17 sửa tưởng lầm “xong hết”, s18 xác nhận người mới đã nhận và giới hạn hỗ trợ. Câu hỏi người tiếp quản cần gì được luyện trong challenge bàn giao; một cảnh chỉ hỏi thông tin mà không đổi kết quả sẽ trùng s16/s18.
- E06 S026–S030: s19 gặp lại sau lời không và hỏi tình hình, s20 sửa hiểu nhầm “giận”. Lời cảm ơn và đổi sang chuyện chung đã nằm trong hai cảnh; không nhân thêm ba cảnh chỉ để đổi câu mở.

## Rà nguồn, độ khó và ngữ nghĩa

- B09 §21: đúng ba hội thoại của 用例, đủ 14 lượt, nguyên văn Nhật và thứ tự như manifest; nhãn CD/track của 用例 không in. Băng bán riêng chỉ được xác nhận cho phần 聞きとり練習 ở trang sau, vì vậy không tuyên bố có file nghe cho pack này. Đoạn về tiếng chó khác bối cảnh nhờ vả nhưng cùng kỹ năng chuyển từ cách nói để ngỏ sang nói rõ vấn đề; phần giảng chỉ ra giới hạn áp dụng.
- B10 bài 5: đọc bảng cách nhờ/từ chối, 会話1–2 và lời đáp. B21 bài 4: đọc 本文会話 và 類話; nội dung giảm tần suất rồi vẫn từ chối cung cấp mạch thương lượng. Không gán lời thoại AI mới thành trích sách. B12/B13 chưa chọn vì đơn vị/pack đã kiểm ở bước tra chưa gần bằng B09/B10/B21 với mục tiêu ranh giới trách nhiệm; không ép Speak Japanese vào chặng.
- Danh sách từ rút từ câu nói của tình huống hoặc pack, động từ đưa về thể từ điển; `source-map.vocabulary_evidence` pin surface. Grammar N4/N3/N2 là ánh xạ biên tập cho mẫu thực có trong lời nói, không tuyên bố là phân loại JLPT chính thức.
- Đã đọc lại 20 cảnh hai vai: lý do mở lời, người có quyền quyết, trạng thái nhận/chưa nhận, thứ tự sự kiện và lời chốt. Các cuộc nói sau kết quả được nối ở `follows` khi cùng việc. Giọng Nhật thân mật của nhóm quen khớp cách xưng “tớ/cậu” trong Việt; đoạn mẫu nguồn giữ nguyên giọng và vai của sách. Đã sửa câu hỏi không tự nhiên ở s15, dịch ý theo dõi hồi âm ở s16, thông tin liên lạc s07, mức trách nhiệm s20 và cách nói trực tiếp s17. Những giấy tờ/danh sách chỉ là vật được nhắc trong lời nói, không có bài viết.
- Mỗi challenge có một base phù hợp mọi biến thể; c01 hỏi rõ, c02 từ chối/nhận phần, c03 thay phạm vi, c04 bàn giao, c05 gặp lại. Context của c01 không trỏ từ/ngữ pháp chưa học. Free talk đứng cuối và chứa toàn bộ node học, cho phép người học đổi hướng.
