# Phối hợp nguồn và biên tập từng chủ đề

## Tra rộng, đọc sâu đúng chỗ

Đọc profile/chỉ mục đủ 27 sách một lần khi nhận chặng, ghi cuốn nào có khả năng đóng góp. Tìm bằng cả tên topic, chức năng giao tiếp, quan hệ và các từ Nhật gần nghĩa; ví dụ chủ đề nhà hàng còn liên quan 注文、予約、変更、断る、苦情、会計. Mục lục chỉ giúp định vị. Đọc toàn bộ phần được chọn, cả lời giải thích và các lượt đáp, thay vì chỉ lấy một câu tìm được qua `rg`.

Mỗi lần chọn nguồn phải trả lời: nguồn này giúp phần nào của chặng, có đúng cấp độ/quan hệ không, đã đọc chưa? Nếu không liên quan, ghi ngắn và bỏ qua. Không cần sao chép hàng nghìn đoạn vào sổ nguồn; lưu vị trí đủ tìm lại. Khi token hạt giống sai, ghi chú và trỏ nguồn đúng trong chặng; không cố viết cho khớp nhãn sai, không âm thầm sửa toàn bộ V4.1.

## Vai trò của các nhóm sách

- **B01 (5500), B05, B06–B08:** bối cảnh, cách nói và phương án phản hồi. Dùng để bổ sung biến thể vào sự kiện có mục đích thực; không biến từng cụm từ thành một chặng.
- **B02–B04, B10, B15–B18, B21–B23:** quan hệ công việc, điện thoại, roleplay, kính ngữ, diễn biến nhiệm vụ. B21/B22/B23 là các phần đồng hành, đối chiếu chứ không tính thành ba lần độ bao phủ độc lập. B03 phần quy tắc chỉ lấy điều cần hiểu/nói; không bê bài viết vào lộ trình nói.
- **B11–B12 Speak Japanese:** cách triển khai mẫu câu/cấu trúc diễn đạt, dùng để xây node kiến thức và lời nói trong nhiều cảnh. Không tách người học sang một lộ trình mẫu câu riêng, không nhét mẫu chưa phù hợp chỉ để đánh dấu đã dùng sách.
- **B13–B14 Shadowing:** nhịp lượt nói, câu đáp, tiếng nói tự nhiên, độ dài và biến thể. Chọn đoạn thích hợp cấp độ, giữ quan hệ ngữ cảnh. Mọi hội thoại được app hỗ trợ shadowing; không phải chỉ đoạn lấy từ hai sách này mới được luyện.
- **B25–B27 Nama Chuukei:** nghe ý định, nắm thông tin quan trọng, phản hồi khi thiếu/hiểu sai thông tin, cách cuộc trao đổi diễn ra. Chuyển lợi ích nghe thành các lượt hỏi lại/xác nhận/xử lý trong tình huống; không tạo bài thi nghe hay cần audio gốc mới học được.
- **B09, B19, B20, B24:** khẩu ngữ, rút gọn, tượng thanh, quán ngữ, cảm xúc. Rải vào nơi thực sự tự nhiên, có node giải thích sắc thái khi cần; không bắt dùng trong mọi cuộc thoại, không tạo topic giả chỉ từ một cách nói.
- **Ba sách từ vựng tham chiếu:** chỉ bổ trợ chọn từ và nghĩa, không tính vào 27 giáo trình hay mở thêm ba lộ trình.
- **Memo web:** tìm góc còn thiếu, tên sự kiện/chức năng. Mục lục không cung cấp lời thoại. Nếu chưa đọc tài liệu đầy đủ, hội thoại mở rộng phải được ghi là viết mới.

Mục tiêu tận dụng tất cả sách được đánh giá trên **toàn lộ trình**, không phải ép 27 nguồn vào mỗi chặng. Tích lũy các `used_for` theo revision để xem sách nào ít được dùng và tìm chặng phù hợp. Không gọi một cuốn đã được tận dụng chỉ vì đã xuất hiện một source token.

Khi được giao chạy nhiều chặng, lấy danh sách UID từ registry và trạng thái trên đĩa: có `current.json` thì giữ revision đã chốt, có run dở thì phục hồi đúng run sau khi kiểm chủ sở hữu, chưa có mới `begin`. Không lấy việc có thư mục hoặc số node làm dấu hiệu hoàn thành. Chỉ mục tiến độ toàn lộ trình có thể dựng lại từ các trạng thái này; không để một bảng tổng hợp riêng trở thành bản gốc thứ hai.

## Thiết kế sự đa dạng có ý nghĩa

Với từng chủ đề, viết ngắn bản đồ trước khi viết hội thoại:

1. Người học cần làm được những việc gì ngoài đời? Trước, trong và sau sự kiện có các cuộc trao đổi nào?
2. Quan hệ/vai nào thực sự làm thay đổi cách nói: khách–nhân viên, bạn bè, cấp trên–cấp dưới, mới quen–thân, nội bộ–đối tác?
3. Kết quả nào thay đổi diễn biến: thành công, từ chối, có điều kiện, chưa rõ, hết lựa chọn ban đầu, cần nhờ người khác?
4. Có chỗ nghe sai, thiếu thông tin, đổi ý, bất đồng hoặc cần sửa lời không? Khi nào phương án khác là hợp lý?
5. Các cảnh có khác **hành động giao tiếp và diễn biến** hay chỉ đổi món ăn/tên người? Gộp biến thể bề mặt thành ghi chú/từ vựng; giữ nhánh có hệ quả thành tình huống riêng.
6. Ở cấp này người học sẽ nói ngắn, hỏi rõ từng phần hay giải thích/điều chỉnh/đàm phán tinh tế? Không tăng cấp bằng cách đổi sang từ khó hoặc kính ngữ dày hơn.

Không tạo tích Descartes của mọi vai × kênh × kết quả. Không có số lượng tình huống bắt buộc. Nếu một chặng chỉ có một hai hạt giống, cần chủ động tìm sâu và đề xuất mở rộng có nhãn, không coi hạt giống là giới hạn. Nếu chủ đề quá rộng, đề xuất tách hoặc nhóm sự kiện, không tự đổi registry hàng loạt.

## Xen kẽ nội dung

Một cách bố trí có thể là: hiểu tình huống → nhóm từ dùng ngay → hội thoại cơ bản → kiến thức giải thích phản hồi → nhánh từ chối → nhánh thương lượng điều kiện → cụm tình huống tiếp theo → Live AI. Có thể đặt tên ngữ pháp ngay trước cụm cần nó hoặc gom một danh sách ngắn cho cả chặng. Không lặp bài kiến thức đầy đủ mỗi lần xuất hiện cùng một mẫu; dùng liên kết và nhắc lại có chọn lọc.

Tận dụng nội dung sâu của sách nhưng xây lại mạch học theo chủ đề. Khi trộn nguồn, giữ nhất quán nhân vật, vai, mức thân mật, thời điểm, thông tin đã biết và mục đích. Không chắp nửa đoạn lễ phép với nửa đoạn suồng sã mà không giải thích sự đổi quan hệ.

## Trước khi chốt một chặng

- Đọc hội thoại thành một cuộc trao đổi: có lý do mở lời, phản hồi phù hợp, tiếp nối và kết thúc/thống nhất bước tiếp theo không?
- Tiếng Nhật tự nhiên; nghĩa Việt đúng cả ý định, phủ định, điều kiện, sắc thái. Không đưa furigana, header/footer, bản dịch Trung/Anh, chỉ dẫn hình ảnh còn sót vào bài.
- Kiến thức/từ/ngữ pháp có ích cho các tình huống đã viết; không phải danh sách trang trí. Các nhánh đủ khác nhau và không mâu thuẫn sự kiện.
- Nguồn đã đọc hỗ trợ đúng điều được gắn. Tách nguồn kiến thức, nhãn mục lục và phần tự viết. Câu viết lại không dùng track audio gốc như thể khớp lời.
- Ghi trong `editorial.md`: phạm vi được bao phủ, các góc chưa có/không phù hợp, lý do dừng ở revision này, những nguồn quan trọng đã dùng và phần cần nâng cấp. Không tuyên bố bao phủ vô hạn hay “đầy đủ mọi tình huống”.

Đây là quyết định biên tập của tác giả. Không có bài thi, điểm đạt, điều kiện hoàn thành hay hạn chế quyền chọn bài của người học.
