# Pilot S-011 — Tàu điện & xe buýt

Bản hiện hành **r0002**, đã sửa theo review Claude và feedback về từ vựng/gối đầu. Không thay V5 và chưa chạy hàng loạt.

- [Đọc toàn chặng r0002](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/stage-preview.md)
- [Bài Speak Japanese: ね](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/knowledge-k02.md)
- [Challenge buýt: phía người học](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/challenge-c02-transfer.learner.md)
- [Cùng challenge: phía AI](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/challenge-c02-transfer.ai.md)
- [Free talk đã có context tổng hợp](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/free-talk-situation.md)
- [JSON migration r0002](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0002/stage.json)
- [Nghiệm thu, quyết định và giới hạn](revisions/r0002/content/editorial.md)
- [Nguồn và locator](revisions/r0002/content/sources.json)
- [Bản r0001 để đối chiếu](../../harumii_export/da5c16e5-9425-5a4f-9086-8c109aa79c90/r0001/stage-preview.md)

## Nội dung mới

Giữ đủ 15/15 tình huống V5, 104 lượt hội thoại lõi (r0001: 112; đã lược tám lời kết thừa). Năm bài kiến thức, năm nhóm shadowing, bốn list từ, bốn node ngữ pháp, ba challenge/sáu variant và một free talk: 37 node, chia năm cụm bài.

Shadowing gồm 42 câu độc lập và 13 hội thoại mini/36 lượt. Bài B11 ね giữ hội thoại donut, dạng lịch sự và đủ tám cặp ví dụ/ba chức năng, rồi thêm phần áp dụng vào tàu điện. Cặp kiến thức → shadowing dùng chung utterance ID. B14 có ba đoạn nguồn; B27 có một skit chuyển soạn; B01/B08 góp các nhóm câu đi lại thực. Không dùng tên sách thay cho nội dung luyện.

90 mục từ qua bốn list, 82 từ khác nhau, được trích ngược từ lời nói thực xuất hiện. Động từ dạng từ điển, tính từ dạng cơ bản; source-map có câu và surface để tra lại. Từ chưa còn dùng sau giản hóa đã bỏ. Gối đầu chỉ là cân nhắc vận dụng tự nhiên; review_links rỗng, không bắt link từng từ, tái dùng đủ hai bài trước hoặc ghi nợ cho chặng chưa có.

Mỗi trong 182 đơn vị Nhật–Việt có nhãn nguồn: 41 quote, 21 chuyển soạn, 120 viết mới. Nguồn quote giữ chữ Nhật, nghĩa Việt có thể được biên tập. Bảy mục ngữ pháp lõi và tám mục nguồn tham khảo (14 tên khác nhau) có N5/N4 + tên để admin tìm. Phần nguồn khó hơn được ghi source_reference và có hướng dẫn rõ; phần lõi đã giản hóa các cấu trúc bị review chỉ ra. Không mặc định người học đã biết mọi mẫu trong nguồn.

## Kiểm tra và giới hạn

Đã đọc lại 15 hội thoại, năm bài kiến thức và toàn bộ nhóm shadowing; đối chiếu B11 với trọn bài nguồn. Đã kiểm 15 UID tình huống V5, dấu vết từ vựng, nguồn từng câu, schema, nhánh, context và hash snapshot/artifact. 44 kiểm tra tooling đạt; chúng không chứng minh tiếng Nhật hoàn hảo hoặc hiệu quả sư phạm.

Lượt nâng cấp có pause/recover thật khi thay spec/helper, giữ draft cũ và tiếp nội dung đã ghi. r0001 không bị sửa. Chưa chạy Claude Code, Live AI, TTS, import DB hoặc pilot Trung/Thượng trong lượt này; chưa có nghiệm thu bản ngữ/user thật. Không sửa repo Harumi.

Dữ kiện mạng tuyến, giá và thời gian là giả định. Hai nguồn JR East/Kyoto kế thừa lần đọc r0001, không có tra cứu web mới. Tên ga thật của đoạn sách chỉ là bối cảnh luyện, không lịch trình hiện hành. Không có KPI dùng hết 27 sách; r0002 chỉ đọc lại phần cần thiết đã chọn, không đọc lại toàn kho.

## Tiếp tục hoặc chỉnh sửa

Đọc AGENTS.md, skill và references/run-and-resume.md. current.json trỏ r0002; runs/ giữ lịch sử. Bản đã finalized không resume/recover để viết đè. Nâng cấp bằng begin --from-current; giữ ID còn cùng nghĩa, sửa canonical source, rà từ/ngữ pháp/nguồn/context liên quan rồi chốt revision mới. Không tự chạy hàng loạt chỉ vì pilot đã chốt.

## Chi phí

Chưa đo token bill hoặc quota thật; không suy phần trăm từ số chữ hoặc thời gian. Canonical JSON là nội dung gốc duy nhất, các MD/context/artifact được script sinh không gọi thêm model. Các chặng sau tái sử dụng tooling nhưng vẫn cần đọc nguồn, biên soạn và review theo chất lượng.
