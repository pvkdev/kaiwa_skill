# Double check V11 — 44 chặng Trung cuối

Đã rà độc lập đủ **44 chặng, 972 hội thoại Nhật–Việt, 208 sự kiện và 427 nhánh nối**. Ba phiên reviewer mới gpt-6.2-sol/high chia 15/15/14 chặng, mỗi phiên đi tuần tự theo lộ trình. Giữ nguyên 582 cảnh, sửa nội dung hiển thị ở 390 cảnh, không còn cảnh mở. Đây là số cảnh có chỉnh sửa, không phải số lỗi riêng lẻ.

- Nhóm A: 15 chặng, 337 cảnh — giữ 153, sửa 184; 71 sự kiện, 196 cạnh.
- Nhóm B: 15 chặng, 340 cảnh — giữ 264, sửa 76; 75 sự kiện, 129 cạnh.
- Nhóm C: 14 chặng, 295 cảnh — giữ 165, sửa 130; 62 sự kiện, 102 cạnh.

## Đã rà và sửa gì

Các reviewer đọc riêng mạch Nhật, riêng mạch Việt rồi đối chiếu hai vai trong từng cảnh. Sau sửa, đọc lại các nhánh bị ảnh hưởng: ai biết điều gì, việc nào mới được đề nghị, việc nào đã chốt và ai thực hiện tiếp. Bối cảnh, vai TTS và mục tiêu nói được kiểm cùng nội dung.

Các sửa đổi gồm câu Việt bám chữ, xưng hô, giờ hoàn thành so với giờ gửi tin, hạn chót, trách nhiệm sau bàn giao, đề xuất so với đồng ý, lời gọi lại và mức chắc chắn của kết quả. Đã làm rõ các cảnh về lao động, dị ứng, thuê xe/bằng lái, cấp cứu, thiên tai, quấy rối và bạo lực bằng nguồn chính thức đúng phạm vi. Bối cảnh hỏi HR về nơi tư vấn được tách khỏi cuộc tư vấn thực sự.

Điều phối đọc mẫu bản sửa tại 14 chặng và yêu cầu chỉnh thêm các điểm có nguy cơ đổi nghĩa. Việc đọc mẫu này bổ sung cho lượt rà toàn bộ của ba reviewer, không được tính thành một lượt đọc độc lập thứ ba cho toàn bộ 972 cảnh.

## Mạch thời gian được làm rõ

- T-112: cảnh sau tuần đầu dẫn tới ngày đầu thử kế hoạch điều chỉnh. Nhật và Việt nêu rõ đây là ngày thử đầu, không phải một thống kê nhiều ngày.
- T-113: cạnh phi tuyến S015 → S016 có sẵn trong V10 được giữ. S015 xảy ra sau khi thôi việc; S016 mở hồi tưởng trước khi chốt ngày; tới S019 mới xác nhận ngày. Đã đọc lại toàn nhánh và ghi trong hồ sơ. Không sửa UID, mục tiêu, thứ tự hay graph V10.

## Kiểm dữ liệu và bản xem

Cả 44 phiếu đều đạt kiểm tra hiện hành: đủ UID và thứ tự, turn ID tham chiếu có thật, dấu vân tay đầu vào/bản thảo/từng cảnh/nguồn khớp. Đủ 208 sự kiện được đọc và 427 cạnh được ghi bằng chứng. 141 tham chiếu sách và 147 tham chiếu web được tính theo hồ sơ từng chặng, có thể dùng lại cùng tài liệu.

Một số nguồn web bị lỗi hoặc chặn truy cập. Trang thay thế, phần chỉ đọc qua chỉ mục và phạm vi dùng được ghi trong RESEARCH.md; không ghi thành đã đọc toàn văn khi chỉ tiếp cận trích đoạn.

Giữ nguyên 249 bản hội thoại ngoài phạm vi. So JSON xác nhận chỉ 44 lớp hội thoại được thay; lộ trình và các phần khác giữ nguyên. Toàn bộ 26.005 ID lượt là duy nhất; không có hội thoại Nhật trùng nguyên kịch bản. JSON nhúng HTML khớp learner.json; docs/index.html khớp ROADMAP.html.

Chrome headless kiểm toàn bộ 293 chặng có hội thoại ở chiều rộng 1.280 px và 390 px: đủ 6.004 cảnh, 26.005 lượt, đúng hai ngôn ngữ và vai, không tràn ngang.

## Trạng thái hiện tại

**293/293 chặng topic đã có hội thoại và hoàn tất rà độc lập**: Sơ 81, Trung 148, Thượng 64. Tổng 6.004 cảnh và 26.005 lượt. 72 chặng chuyên đề không đổi trong đợt này.

Báo cáo sản xuất cũ được giữ như mốc lịch sử. BUILD.json và báo cáo rà này phản ánh trạng thái sau double check.

- [HTML xem trước](../../ROADMAP.html)
- [QA chi tiết và hash đầu ra](QA.json)
- [Tiến độ từng chặng](PROGRESS.json)
- [Phân công và hash đầu vào](RUN.json)
