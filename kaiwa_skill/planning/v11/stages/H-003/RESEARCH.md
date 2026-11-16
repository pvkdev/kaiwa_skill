# H-003 — Nguồn và tự rà biên tập

Đọc catalog27/BOOK_GUIDE.md, source_index.jsonl và manifest.json; tra theo chức năng nói, quan hệ và cụm Nhật. Đọc các đoạn Markdown bên dưới gồm lời trước và sau. Mọi lời thoại trong stage do tác giả viết mới; nguồn sách chỉ định hướng ngữ dụng và trình tự. Không có khẳng định chính sách, phí hay thủ tục thực tế cần xác minh web.

## Nguồn đã đọc

- **b04_phone / B04 — しごとの日本語 電話応対 基礎編**, `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/01-ビジネス電話応対の基本.md` dòng 10–24: Cách xưng phía trong và ngoài công ty khi gọi điện, kể cả tên người phụ trách; hội thoại mới không gán người của mình kính xưng với khách.
- **b15_appoint / B15 — 上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―**, `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/11-bai-11.md` dòng 4–78: Trình tự gọi khách mới: tự xưng, nêu lý do, đáp câu hỏi, xin gặp, xác nhận mục tiêu, giờ và người tham gia; cuộc gọi mới tránh coi lời xã giao là lịch hẹn.

## Tự rà theo từng cảnh

Đã mở riêng từng cảnh, đọc liền tiếng Nhật và riêng tiếng Việt, đổi vai hai người nói, rồi đọc nối từng quan hệ `continues_from`. Kết quả và điểm kiểm cụ thể:

- **S001 cab28fde-da97-5862-9c02-ac9dd05c6947** (routine, từ mở riêng): Minh tự xưng và xin gặp đúng người theo lĩnh vực. Kato hỏi lý do rồi chỉ hứa kiểm khả năng chuyển máy. Chưa suy rằng khách đã nhận cuộc gọi; tên người cần gặp chưa biết.
- **S002 473f21ba-0393-503c-915d-1fbcd713cd03** (declined, từ S001): Minh hỏi kênh phù hợp sau lời không chuyển máy. Kato chỉ kênh chung và nói rõ không hứa phản hồi. Nối S001: câu cuối không gán quyền tiếp cận riêng cho Minh.
- **S003 0db4ced7-4a5d-5e42-9453-d5b9d15fef38** (accepted, từ S001): Minh nêu mục đích trong một phút và xin cuộc gặp ngắn. Sato hỏi nội dung dự định, rồi muốn nghe trước. Nối S001: sau chuyển máy vai B đổi sang Sato, có nói rõ trong bối cảnh; vẫn chưa chốt cuộc hẹn.
- **S004 86f9e9f4-a10b-56dd-8cc4-dc3c7fd912b0** (misunderstanding, từ S003): Minh sửa hiểu lầm về đổi dịch vụ lưu trữ. Sato chấp nhận trao đổi nếu giữ nơi lưu hiện tại. Nối S003: giải thích nội dung gặp, không hứa sẵn giải pháp hay kết quả.

### E01 đã checkpoint

- **S005 022e4684-6384-5eb8-acd3-c0093ecd0ee2** (routine, từ mở riêng): Minh hỏi một vấn đề ưu tiên. Sato nêu chỗ khó nhận ra bản mới nhất. Câu đáp sau dùng chính chi tiết khách vừa cung cấp.
- **S006 e5722d79-eb84-5e7d-af53-2ee6ddc72598** (conditional, từ S005): Minh thu gọn cuộc gặp vào một vấn đề. Sato chỉ chấp nhận mười lăm phút, chưa nhận xem toàn dịch vụ. Nối S005: vấn đề phiên bản mới nhất được giữ; không phóng đại sự đồng ý.
- **S007 9ef488f5-b42d-511c-a715-97656416b6b4** (pending, từ S005): Minh xin ngày gọi lại chỉ để kiểm tình hình. Sato chưa chốt người tham gia hoặc lịch gặp. Nối S005: lời Việt giữ と思います là khả năng, không phải cam kết.
- **S008 9045dba2-0751-5633-bc1b-58bc0db763d1** (follow_up, từ S007): Minh gọi đúng ngày hẹn, xác nhận giờ, người tham gia và mục tiêu. Sato xác nhận đồng nghiệp tham gia và nội dung. Nối S007: lịch được chốt tại đây, không sớm hơn.

### E02 đã checkpoint

- **S009 322c668c-6947-513d-8bdb-f1dbf12e1bd3** (routine, từ mở riêng): Minh báo chuyên viên kỹ thuật không đi được và đề xuất giờ mới. Sato nói cần kiểm, chưa đồng ý đổi. Giờ thứ Năm ba giờ là đề xuất; lời Việt giữ chưa xác nhận.
- **S010 2d01af30-d8b5-51a0-91a1-ebf0f837c3bd** (declined, từ S009): Minh nhận lời từ chối đổi giờ và xin thời gian kiểm người thay. Sato yêu cầu báo cả chuyên môn của người thay. Nối S009: không giả định chuyên viên khác đã nhận.
- **S011 86f7386c-acc9-568f-9c34-3dbcf4b74e08** (conditional, từ S009): Minh chấp nhận gặp trực tuyến và hỏi mục tiêu trước khi kiểm người dự. Sato sẽ chia sẻ quy trình qua màn hình. Nối S009: cuộc gặp trực tuyến vẫn cần xác nhận người tham gia, lời cuối chỉ hứa gọi lại.
- **S012 e09f8ad9-a274-5a2e-94ea-3343d07aeac3** (follow_up, từ S011): Minh xác nhận người tham gia hai phía và thứ tự trao đổi. Sato xác nhận chỉ một mình phía khách. Nối S011: sau khi kiểm nội bộ, Mai là người tham gia đã xác nhận, không phải phương án còn chờ.

### E03 đã checkpoint

- **S013 3d5a5557-ac62-5fca-8697-b2610d5557a4** (routine, từ mở riêng): Minh thăm dò thời điểm phù hợp rồi ngừng chủ động liên hệ. Sato chưa có kế hoạch, muốn tự chủ động khi cần. Không diễn câu nói lịch sự thành quyền gọi lại.
- **S014 93db759e-5eb0-5a28-ab15-485eebea0823** (declined, từ S013): Minh nhận yêu cầu không gọi tiếp. Sato xác nhận đã được hiểu. Nối S013: ngừng liên hệ hoàn toàn theo yêu cầu rõ hơn.
- **S015 84669327-aa3f-5ba1-9767-0db54238cbd9** (alternative, từ S013): Minh hỏi ai chủ động liên hệ sau khi nghe khả năng để ngỏ. Sato sẽ liên hệ nếu cần, không nêu thời điểm. Nối nhánh S013: không gán thành cuộc hẹn chắc chắn.
- **S016 f751a393-e514-508b-8398-2d7befd72026** (misunderstanding, từ S015): Minh sửa ngay hiểu lầm của đồng nghiệp đang ngồi cạnh. Sato nhắc lại chỉ liên hệ khi phát sinh nhu cầu. Nối S015 trong cùng cuộc gọi: không gọi thêm sau khi khách yêu cầu để họ chủ động.

### E04 đã checkpoint


## Tra cứu chuyên đề và điểm nối

Tra catalog27 bằng `電話`, `取り次ぐ`, `新規顧客`, `アポイント`, `断る`, `伺う`, `御社`, `弊社`; đọc B04 và B15 theo các đoạn có cả câu trước/sau. Đã mở `sj-thuong-01/lesson.md` và `practice.json`; chỉ gắn item khi đúng hình thức xuất hiện trong thoại. S001 rẽ sang lễ tân từ chối S002 hoặc nối máy S003; S003→S004 sửa đúng chủ đề. S005 rẽ sang mười lăm phút S006 hoặc chờ S007→S008. S009 rẽ sang không đổi giờ S010 hoặc trực tuyến S011→S012. S013 có nhánh không liên hệ S014 và nhánh khách chủ động S015→S016, không gán lịch chắc chắn. Công ty, dịch vụ và giờ trong cảnh là hư cấu; không có quy trình công ty thực được khẳng định.
