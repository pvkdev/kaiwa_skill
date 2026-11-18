# V11 batch04 — hoàn tất 60 chặng mới

Đã biên soạn 18 chặng Sơ, 41 Trung và 1 Thượng, tổng 1.012 hội thoại Nhật–Việt, 4.556 lượt nói và 238 sự kiện. Ba worker gpt-6.2-sol/high thực hiện đúng phân công, tuần tự trong nhóm và không trùng quyền sở hữu file.

- Sub Sơ: S-063–S-080 rồi T-084–T-085; 20 chặng, 365 hội thoại, 1.586 lượt.
- Sub Trung: T-064–T-083; 20 chặng, 318 hội thoại, 1.592 lượt.
- Sub Thượng: H-064 rồi T-086–T-104; 20 chặng, 329 hội thoại, 1.378 lượt.

Mỗi chặng có dialogues.json, RESEARCH.md, status.json. Nhật và Việt tách trường; từng lượt gắn speaker_id, hai vai có gender male/female để làm TTS. Nguồn sách có tên, mã, file, dải dòng; nguồn web có URL, ngày đọc, phạm vi. Nguồn và ghi chú biên tập giữ trong hồ sơ quản trị, không chèn vào lời học viên.

Các tác giả đọc đoạn sách thực dùng và chuyên đề trước đó, tự rà từng cảnh bằng Nhật và Việt rồi đọc nối từng đường continues_from. Điều phối đọc mẫu, yêu cầu sửa cách xưng hô, nhãn vai gọi lại và một số câu Việt khó hiểu; các tác giả đọc lại phần liên quan trước cập nhật hash. Giá/lịch/dịch vụ/thủ tục được giới hạn theo nguồn hoặc quy trình hư cấu đã nêu, không đặt thành quy tắc chung cho mọi nơi.

T-067 có một điểm nối bất thường trong V10: S015 đã nhận việc nhưng S016 lại chưa quyết. Bản mới giữ nguyên UID/cạnh, đặt S016 ở một cơ hội mới sau hai năm đi làm và ghi rõ trong bối cảnh, RESEARCH, status. V10 không bị sửa. Ghi chú này giúp truy lại quyết định khi muốn chỉnh khung sau.

Cả 60 chặng qua dialogue.py --check, đúng UID/thứ tự V10, SHA bản thảo/từng cảnh/nguồn sách và dấu vân tay các đầu vào đã ghi. Bộ dựng kiểm ID lượt và kịch bản Nhật trùng xuyên cả 249 chặng. Không còn điểm mở ghi nhận trong phạm vi biên soạn. Đây là vòng authored_self_reviewed; 60 chặng mới vẫn pending cho lượt double check độc lập.

Preview lũy kế có 249 chặng topic đã soạn, 5.032 hội thoại và 21.641 lượt nói. Phần hội thoại Sơ đủ 81/81, Trung 104/148, Thượng 64/64; còn 44 chặng Trung chưa soạn. Các phần video, challenge và free talk thuộc phase khác.

Đã đối chiếu export của toàn bộ 60 chặng với đúng context_vi/speakers/turns của bản tác giả. 189 bản thảo cũ và dữ liệu lộ trình ngoài hội thoại mới được giữ nguyên. JSON nhúng HTML khớp learner.json, docs/index.html trùng ROADMAP.html. Trình duyệt mở đủ 249 chặng ở 1.280 px và 390 px, so vai/giới tính/Nhật/Việt của 5.032 cảnh và 21.641 lượt; không phát hiện tràn ngang tại hai kích thước đó. Kiểm render không thay thế đánh giá ngôn ngữ.

Phân công và mốc đầu vào ở [PLAN.json](PLAN.json), tiến độ ở [PROGRESS.json](PROGRESS.json), bằng chứng kiểm ở [QA.json](QA.json). Mở [preview lũy kế](../../ROADMAP.html).
