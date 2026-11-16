# V11 · Pilot vòng ba

Ba worker gpt-6-sol/high biên soạn theo skill V11 hiện hành, mỗi người một cấp. Điều phối viên đọc đủ 50 hội thoại Nhật–Việt theo mục tiêu từng cảnh và đối chiếu các nhánh nối tiếp. Tổng cộng 249 lượt nói. Chủ dự án review qua các liên kết sau.

- [S-035 · Nhờ vả & đề nghị lịch sự](ROADMAP.html#stage=eb72c7c9-57d0-51a3-9260-0dbbc625cdaa) có 20 cảnh, 78 lượt. [Hồ sơ nguồn](S-035/RESEARCH.md) · [Checkpoint](S-035/status.json)
- [T-008 · An ủi, đồng cảm & chia buồn](ROADMAP.html#stage=fc19cbb2-ccaf-5c9c-aadf-f59a4a77edf8) có 15 cảnh, 86 lượt. [Hồ sơ nguồn](T-008/RESEARCH.md) · [Checkpoint](T-008/status.json)
- [H-047 · Tâm sự: tình cảm, sức khỏe & giấc ngủ](ROADMAP.html#stage=3cbdb697-395a-5147-b8f0-1bdeae58aba2) có 15 cảnh, 85 lượt. [Hồ sơ nguồn](H-047/RESEARCH.md) · [Checkpoint](H-047/status.json)

## Điểm đã kiểm và sửa

- Sơ gồm nhờ giữ đồ, nhận lời có giới hạn, bị từ chối, chụp ảnh, nhận đồ và nhận giúp người khác. Lời nhờ đầu giữ mở để các phản hồi đồng ý, chỉ giữ đến một giờ nhất định và không thể giúp đều hợp mạch. Hai mốc 2 giờ 55 và 3 giờ làm rõ việc giữ trong năm phút.
- Trung gồm nghe bạn kể thất bại, sửa lời động viên không hợp, chia buồn với đồng nghiệp và đề nghị hỗ trợ cụ thể. Đã sửa các câu Việt dịch sát chữ, giữ đúng người muốn được lắng nghe và bỏ lời xin lỗi về một câu hỏi chưa xuất hiện. Cảnh hỏi thăm và hẹn gặp dùng trao đổi bằng lời.
- Thượng gồm xin thời gian tâm sự, sửa suy đoán, đặt giới hạn khi nghe hoặc kể, trao đổi với bạn đời và cập nhật việc tìm bác sĩ. Đã để lời hẹn ban đầu chờ phản hồi để nhánh bận hoặc chưa sẵn sàng diễn ra hợp lý. Cảnh hỏi tiếp hay nghỉ có lựa chọn được nói và được đáp rõ.

## Nghiệm thu sau khi sửa lời thoại

Đã mở riêng 50 cảnh rồi đọc 26 điểm nối theo `continues_from`. Các hàng theo cảnh nằm trong hồ sơ nguồn của từng chặng ở trên. Ba chặng có 249 lượt sau biên tập, giảm 10 lượt so với bản pilot đầu.

- S-035 có 8 điểm nối. Sau lời nhờ trông túi ở S002, S003 chốt đủ năm phút. S004 thương lượng quay lại lúc 2:57 trước khi bạn đi lúc 2:58. Ở S005 bạn đi ngay nên người nhờ tự mang túi.
- T-008 có 10 điểm nối. S006 kết sau lời chia buồn và lời đáp của đồng nghiệp. S008 bắt đầu khi chính chị nói muốn giữ riêng chuyện gia đình. S005 dùng lời mời đi uống trà giữa bạn bè.
- H-047 có 8 điểm nối. S003 để ngỏ nguyên nhân nên Ken có thể hỏi về công việc ở S004. Ở S006, Yuta đang đợi tin và mới nghe Aya nói cô thấy cô đơn. S007 cho hai người cơ hội làm rõ hiểu lầm. S012 mở sau khi Ken đã lắng nghe. Aya hỏi cách chuẩn bị, nghe Ken gợi ý ghi chú rồi tự chọn điều muốn thử. S014 và S015 giữ quyền quyết định kể đến đâu cho Aya.

## Nguồn và giới hạn

Nguồn ngôn ngữ được tra qua chỉ mục 27 sách rồi đọc các đoạn phù hợp, gồm Mini Phrase, mẫu câu, Nama Chūkei và hội thoại công sở. Các chuyên đề gần trước chỉ được gắn khi có cách nói thực sự vận dụng trong hội thoại. Lời thoại mới có nhãn nguồn từng lượt trong bản quản trị.

H-047 dùng tình huống mất ngủ để luyện tâm sự và nói giới hạn riêng tư. Quyết định hỏi bác sĩ của nhân vật được đối chiếu tài liệu ngủ của Bộ Y tế Nhật. Nội dung khám cụ thể được để riêng tư trong cảnh. [睡眠ガイド2023](https://www.mhlw.go.jp/content/10904750/001222166.pdf)

## Dữ liệu và preview

Đã kiểm tập UID/thứ tự V10, hai vai và giới tính dùng cho từng giọng TTS, hai trường Nhật–Việt, nguồn và nhãn từng lượt. Root review gắn hash với đúng nội dung đã đọc. Bộ dựng ghép cả chín pilot vào learner.json và HTML. Đã đối chiếu JSON nhúng với learner.json và hai bản HTML với nhau. Trên Chrome ở chiều rộng 1280 và 390 px, mở phần tình huống của cả ba chặng rồi so bối cảnh, vai, giọng và từng lượt JA–VI trong DOM với bản tác giả. Sáu pilot trước và phần nền đã được đối chiếu với commit 02707527.

Kết thúc ở trạng thái awaiting_user_review, bulk_run_authorized=false.
