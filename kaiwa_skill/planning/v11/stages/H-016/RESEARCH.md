# H-016 — Nguồn và tự rà biên tập

Đọc catalog27/BOOK_GUIDE.md, source_index.jsonl và manifest.json; tra theo chức năng nói, quan hệ và cụm Nhật. Đọc các đoạn Markdown bên dưới gồm lời trước và sau. Mọi lời thoại trong stage do tác giả viết mới; nguồn sách chỉ định hướng ngữ dụng và trình tự. Không có khẳng định chính sách, phí hay thủ tục thực tế cần xác minh web.

## Nguồn đã đọc

- **b15_negotiate / B15 — 上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―**, `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/14-bai-14.md` dòng 8–77: Trình tự hỏi điều kiện, ưu tiên của người quyết và hẹn phản hồi; tình huống và số lượng được viết mới.
- **b15_claim / B15 — 上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―**, `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/08-bai-08.md` dòng 8–40: Lắng nghe tình trạng hàng, xin dữ liệu và hứa kiểm tra trước khi nêu cách xử lý.
- **customs_docs — Japan Customs, FAQ 1107 Documents to be Submitted for Import Clearance**, https://www.customs.go.jp/english/c-answer_e/imtsukan/1107_e.htm (2026-11-16): Trang ghi invoice là chứng từ nhập khẩu và nêu tên, số lượng, trị giá; S015–S016 chỉ dùng chi tiết thiếu số lượng của tình huống hư cấu, không kết luận đủ điều kiện thông quan.
- **customs_outline — Japan Customs, FAQ 1101 Outline of Import Clearance Procedures**, https://www.customs.go.jp/english/c-answer_e/imtsukan/1101_e.htm (2026-11-16): Phân biệt hàng đến, việc khai/kiểm và giấy phép nhập; S013–S016 tránh đồng nhất lịch cập cảng với ngày giao tới cửa hàng.

## Tự rà theo từng cảnh

Đã mở riêng từng cảnh, đọc liền tiếng Nhật và riêng tiếng Việt, đổi vai hai người nói, rồi đọc nối từng quan hệ `continues_from`. Kết quả và điểm kiểm cụ thể:

- **S001 ef77c82e-a1a0-505a-800a-b2d6cbd90cf7** (routine, từ mở riêng): Nam nhắc lượng, ngày dùng và hai điều mở. Kato nêu điều mong muốn tại cửa hàng. Ngày dùng không biến thành ngày giao đã cam kết.
- **S002 d4e3d871-dd78-5a1a-b100-981b57709c94** (misunderstanding, từ S001): Nam sửa hiểu lầm báo giá 600 cho 800. Kato giữ đơn chờ. Nối S001: lượng mới cần báo giá mới.
- **S003 cff7e523-7dfb-51de-8981-128e6e74a099** (routine, từ mở riêng): Nam hỏi người duyệt cuối. Kato nêu trưởng phòng mua. Đầu mối tổng hợp khác người phê duyệt.
- **S004 45fa18fa-27cd-5e54-b34a-95935e2f011e** (pending, từ S003): Nam hỏi mốc có duyệt. Kato hẹn ba giờ ngày sau. Nối S003: đơn chưa đặt.

### E01 đã checkpoint

- **S005 23cbe618-a55d-53bc-bb31-3d8bb800b477** (routine, từ mở riêng): Nam hỏi số lượng và ngày mỗi đợt. Kato đưa 400 rồi 200. Điều kiện giao hai đợt rõ trước khi hỏi vận hành.
- **S006 6b515942-fa40-546a-b32c-85e264fa15f8** (conditional, từ S005): Nam kiểm khả năng thực tế. Mai chỉ dự kiến 300 rồi 300. Nối S005: chưa nói thay thế đã được khách nhận.
- **S007 93e17334-b50a-593d-be29-26c68d421162** (declined, từ S006): Nam hỏi ưu tiên sau khi lịch bị từ chối. Kato cần 400 ngày đầu. Nối S006: từ chối có lý do cụ thể.
- **S008 c86740d8-b3d4-55eb-8b12-5954aed63e69** (alternative, từ S007): Nam đưa nguồn thứ hai có điều kiện. Kato đòi hình thức thống nhất. Nối S007: mẫu, phí và phê duyệt còn mở.

### E02 đã checkpoint

- **S009 01cb67ee-d3f0-5cf2-bb5d-a184415595d7** (routine, từ mở riêng): Nam phân biệt điều đã xác nhận và chưa. Mai ghi trạng thái kiểm mẫu. Không coi nguồn thứ hai đã duyệt.
- **S010 915d6690-5824-5162-9b5e-2f4e3202239b** (misunderstanding, từ S009): Nam sửa suy diễn từ “trông được”. Mai dừng đặt 100 chiếc. Nối S009: ấn tượng không phải quyết định.
- **S011 ad5cfa0f-b94a-55da-b85c-51078b1f8c3a** (routine, từ mở riêng): Nam giao đầu mối theo dõi xuất và báo khách. Mai nhận phần xuất. Ngày xuất và ngày nhận được tách.
- **S012 970357b2-c720-5e8c-b8f6-b54ad96fa2b4** (follow_up, từ S011): Nam hỏi cả hai mốc. Mai chỉ có ngày rời xưởng. Nối S011: chưa dùng ngày xuất làm ngày giao.

### E03 đã checkpoint

- **S013 a8a54461-d780-5e4d-aab3-fc6eb76f3504** (routine, từ mở riêng): Nam hỏi trạng thái chứng từ và đầu mối. Yui nói mới có lịch tới cảng. Nguồn Customs chỉ hỗ trợ phân biệt bước, không bảo đảm ngày.
- **S014 a7fe0622-cb7b-5537-bdb8-28a3f587fc20** (pending, từ S013): Nam báo khách điều chưa biết và mốc kiểm. Kato có giờ để báo cửa hàng. Nối S013: không hứa hàng tới ngày dùng.
- **S015 2c01b349-7f80-5038-ab41-952024459bf8** (problem, từ S013): Nam hỏi ai sửa invoice thiếu lượng. Yui chuyển yêu cầu tới nơi phát hành. Nối S013: Customs 1107 ghi quantity trên invoice; không kết luận giấy tờ khác.
- **S016 cd432fca-e785-5f91-9389-56fd8b76ac04** (follow_up, từ S015): Nam báo bản sửa đã gửi, tình trạng vẫn mở. Kato tính cách dùng lô tới trước. Nối S015: dự kiến tới cửa hàng không phải xác nhận thông quan.

### E04 đã checkpoint

- **S017 1b8deb44-a6aa-5c08-96fe-ed4b8af07e35** (routine, từ mở riêng): Nam hỏi việc dùng lô đầu. Kato dùng được và theo dõi số. Không tự coi toàn đơn đã xong.
- **S018 8a5f4255-bd86-505a-ab11-cf45fad85a5b** (problem, từ S017): Nam xin số, ảnh và mã thùng. Kato có năm chiếc lỗi. Nối S017: chưa đoán nguyên nhân.
- **S019 3d80da83-5bfe-5bc9-a050-f5af1f4b3cad** (resolved, từ S018): Nam hỏi sau đổi năm chiếc. Kato dùng được nhưng tiếp tục quan sát. Nối S018: chỉ giải quyết phần được báo.
- **S020 7acee5d7-5ec2-5180-a084-120ebd7e0d05** (routine, từ mở riêng): Nam cảm ơn và hỏi thời điểm trao đổi lô sau. Kato chưa có lượng. Không ép khách cam kết tương lai.

### E05 đã checkpoint

- **S021 4d1519c0-3c79-56a3-b96a-9861d349b01b** (routine, từ mở riêng): Nam hỏi lý do nếu khách tiện. Kato nói ưu tiên ngày giao. Quyết định chọn bên khác được tôn trọng.
- **S022 94b9b718-8dff-50e1-8a4f-40948f868168** (declined, từ S021): Nam dừng hỏi khi khách từ chối. Kato không cần giải thích thêm. Nối S021: chỉ chia sẻ phạm vi được cho phép.
- **S023 70e82c18-fed5-5010-96bd-983660d3420a** (alternative, từ S021): Nam xin phép liên hệ khi có đề xuất phù hợp. Kato không muốn gửi định kỳ. Nối S021: liên hệ có điều kiện cụ thể.
- **S024 508001e2-3885-5fa2-9f04-5d744a1b5bfc** (follow_up, từ S023): Nam hỏi nhu cầu mới đúng một lần. Kato nói chưa có, sẽ chủ động liên hệ. Nối S023: không tiếp tục thúc ép.

### E06 đã checkpoint
