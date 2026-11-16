# T-035 — nhật ký biên soạn

Đã rà catalog27 SOURCE_LABELS về 問い合わせ/窓口, đọc B04 Unit23 dòng 1–75 cho cách hỏi đúng đầu mối; đọc sj-trung-09 lesson/practice. Đọc ISA danh sách hồ sơ '家族滞在' cho 在留資格認定証明書交付申請 dòng 0–12, đặc biệt các loại giấy chứng minh quan hệ và giấy bên bảo trợ. Đây chỉ là một đường thủ tục có thể được nhân viên cân nhắc, không khẳng định gia đình hư cấu đủ điều kiện, không trộn với hồ sơ xin cư trú của người đang ở Nhật. Đọc hướng dẫn Shinjuku đổi địa chỉ dòng 262–278 về giấy quan hệ hộ và dịch Nhật cho việc thành phố; cơ quan thành phố và Nyukan có thẩm quyền khác nhau. Lịch và thông tin người nhà trong cảnh là hư cấu. Tên trên giấy nguồn phải kiểm với cơ quan cấp giấy và nơi xử lý hồ sơ, không tự sửa bản gốc.

- Đã đối chiếu V10: 16 cảnh, 4 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Ai ở Nhật/ngoài Nhật và mục tiêu rõ; không giả định diện hay kết quả.
- S002 (E01, routine): Phân biệt giấy đang có với yêu cầu nộp thực tế, không mặc định bản dịch cho mọi cơ quan.
- S003 (E01, follow_up): Nối S001: mốc dự kiến mới không được biến thành lịch chắc hay tự kéo dài giấy.
- S004 (E01, alternative): Nối S001: quầy thông tin chuyển đúng bộ phận, không khẳng định ai được đại diện nộp.
- S005 (E02, routine): Đối chiếu hai hệ chữ, không tự đổi giấy nguồn.
- S006 (E02, problem): Nối S005: khác một ký tự cụ thể, không tự chọn phiên bản tên hay hứa cơ quan Nhật sửa giấy Việt.
- S007 (E02, conditional): Nối S005: tư vấn trước với bản sao, nộp đơn và bản gốc là việc sau.
- S008 (E02, resolved): Nối S006: trách nhiệm cơ quan nguồn và quầy xử lý tách rõ, lỗi chưa coi đã sửa.
- S009 (E03, routine): Phân thời điểm/cơ quan: hồ sơ trước đến hỏi ISA, địa chỉ sau đến hỏi thành phố.
- S010 (E03, alternative): Nối S009 theo nhánh sai quầy: không để thành phố quyết đơn trước nhập cảnh.
- S011 (E03, misunderstanding): Nối S010: hướng dẫn khác vì giai đoạn khác, không tạo mâu thuẫn giả.
- S012 (E03, pending): Nối S009: chưa liên hệ gia đình được, hẹn sau, không bịa dữ kiện.
- S013 (E04, routine): Báo thông tin xác nhận từ giấy, nêu điểm tên khác còn cần xử lý.
- S014 (E04, pending): Nối S013: quan hệ được trình bày nhưng xử lý tên vẫn pending, kênh phản hồi rõ.
- S015 (E04, problem): Nối S013: lịch thay đổi, chưa tự kết luận giấy hay hồ sơ vô hiệu.
- S016 (E04, resolved): Nối S013: phân công ai hỏi gì ở ba đầu mối, chưa coi hồ sơ được chấp thuận.

## Nguồn đã dùng

- isa_family: ISA: 「家族滞在」に係る提出書類一覧（認定証明書交付申請用）, https://www.moj.go.jp/isa/content/001404137.pdf (đọc 2026-11-16): Dòng 0–12: ví dụ đường hồ sơ người ở nước ngoài, liệt kê giấy chứng minh quan hệ và bên bảo trợ; cần cơ quan xác định áp dụng.
- city_household: Shinjuku: Notification Procedures for a Change of Address for Foreign Residents, https://www.foreign.city.shinjuku.lg.jp/en/wp-content/uploads/sites/3/2025/03/2todoke_e2025.pdf (đọc 2026-11-16): Dòng 262–278: việc hộ tại thành phố có thể cần giấy quan hệ và bản dịch; không thay thế việc Nyukan.
- b04: B04 しごとの日本語 電話応対 基礎編, `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/24-Unit23-問い合わせをする.md` dòng 1–75: Cách hỏi đầu mối, xin phản hồi và tách câu hỏi; không dùng làm quy định cư trú.

## Còn mở

- Không còn vấn đề sau rà độc lập.

## Rà độc lập — 2026-11-16

- Đã đọc 16 cảnh Nhật–Việt và bốn sự kiện, gồm nhánh khác tên giấy và phân biệt hồ sơ trước sang với khai địa chỉ sau sang. Đối chiếu B04, danh sách giấy 家族滞在 của ISA `https://www.moj.go.jp/isa/content/001404137.pdf` và hướng dẫn Shinjuku `https://www.foreign.city.shinjuku.lg.jp/en/wp-content/uploads/sites/3/2025/03/2todoke_e2025.pdf`; hồ sơ cụ thể vẫn cần nơi phụ trách xác định.
- S013 u04–u05: trong cuộc gọi, nhân viên chỉ ghi thông tin và hẹn xem giấy ở lần sau, không nói đã xem tài liệu vật lý ngay qua điện thoại. S015 u02: sửa “giấy đã nộp” thành giấy đang chuẩn bị; S012 và S016 khẳng định chưa nộp đơn.
- Checker xác nhận bản thoại 16 cảnh và phiếu rà 16 cảnh/4 sự kiện; cập nhật hash thoại, hai cảnh sửa và hai nguồn web trong `status.json`.
