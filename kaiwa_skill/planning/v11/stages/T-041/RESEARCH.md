# T-041 — nhật ký biên soạn

Đã rà nhãn catalog27, đọc B08 U13–U14 dòng 356–412 và B04 Unit23 dòng 1–75; đọc sj-trung-10 lesson/practice. Đọc trực tiếp Visa hỗ trợ dòng 23–32 (thẻ bị từ chối và tranh chấp hỏi bên phát hành), Visa mất thẻ dòng 0–3, 46–59, JCB mất thẻ dòng 97–105 (thẻ tìm lại sau báo mất tùy quy trình), JCB FAQ khoản trùng dòng 23–77. Các điều kiện riêng của Visa/JCB chỉ là tiền lệ nghiên cứu; công ty thẻ みどり và cửa hàng trong cảnh là hư cấu, mọi trạng thái, thời gian, hoàn tiền và bảo vệ thẻ phải hỏi bên phát hành. Tách thông báo/chờ xử lý với khoản đã ghi, khoản lạ với khoản trùng, nhận khiếu nại với xác nhận hoàn. Ngày, tiền và lịch gọi lại là dữ kiện tình huống hư cấu.

- Đã đối chiếu V10: 16 cảnh, 4 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Vai b là cửa hàng; chỉ nói trạng thái terminal của cửa hàng, không đoán nguyên nhân thẻ.
- S002 (E01, conditional): Nối S001: phương án giữ hàng do cửa hàng hư cấu tự xác nhận, chưa thanh toán.
- S003 (E01, routine): Vai b là phát hành; cung cấp mốc/chỗ/lời máy và sự kiện phía cửa hàng, chưa đoán lý do.
- S004 (E01, misunderstanding): Nối S003: từ chối một giao dịch không bằng khóa toàn thẻ; hỏi hai trạng thái riêng.
- S005 (E02, routine): Một khoản xác nhận, một khoản chờ; chưa khẳng định bị tính trùng.
- S006 (E02, pending): Nối S005: trạng thái chờ với mốc tra hư cấu, không hứa tự mất hay hoàn tiền.
- S007 (E02, problem): Nối S005: khoản lạ là hồ sơ riêng, hỏi bảo vệ thẻ ngay, không hứa bồi hoàn.
- S008 (E02, misunderstanding): Nối S005 nhánh sửa số, không giữ giả định hai khoản giống nhau.
- S009 (E03, routine): Báo mất nhanh, không yêu cầu người dùng nhớ số thẻ hay hứa đã khóa trước thao tác.
- S010 (E03, routine): Hỏi trạng thái bảo vệ qua kênh chính thức; không tự xem báo mất là đã dừng.
- S011 (E03, conditional): Nối S010: thiếu giấy không tự chặn liên hệ, kết quả dừng phải được xác nhận.
- S012 (E03, follow_up): Nối S009: tìm thấy ví không tự khôi phục thẻ; JCB chỉ là tiền lệ nghiên cứu.
- S013 (E04, routine): Gọi lại bằng mã đúng về khoản trùng, yêu cầu hai trạng thái và hoàn tiền được xác nhận.
- S014 (E04, pending): Nối S013: điều chỉnh được nhận không phải hoàn tất, có mốc theo dõi giả định.
- S015 (E04, alternative): Nối S013: đầu mối trả lời xác định, không tự chuyển trách nhiệm sang cửa hàng.
- S016 (E04, resolved): Nối S013: resolved chỉ là trách nhiệm và bước tiếp đã rõ, khoản tiền vẫn pending.

## Nguồn đã dùng

- visa_help: Visa: 消費者サポート, https://www.visa.co.jp/support.html (đọc 2026-11-16): Dòng 23–32: vấn đề từ chối thanh toán hoặc tranh chấp nên hỏi nhà phát hành về giao dịch cụ thể.
- b04: B04 しごとの日本語 電話応対 基礎編, `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/24-Unit23-問い合わせをする.md` dòng 1–75: Nêu số tham chiếu và tóm tắt sự cố qua điện thoại.
- jcb_double: JCB FAQ: 同じお店から二重で請求, https://j-faq.jcb.co.jp/faq/show/1603?back=front%2Fcategory%3Ashow&category_id=119&page=2&site_domain=default&sort=sort_access&sort_order=desc (đọc 2026-11-16): Dòng 23–77: cần xem tình trạng hai khoản và có thể hỏi nơi bán hoặc bên phát hành; không hứa hoàn tiền trước tra soát.
- visa_loss: Visa: カード紛失/停止手続き, https://www.visa.co.jp/support/consumer/lost-stolen-card.html (đọc 2026-11-16): Dòng 0–3, 46–59: khi mất thẻ liên hệ bên phát hành và hỏi bảo vệ; cách xử lý theo từng thẻ.
- jcb_loss: JCB: カードの紛失・盗難, https://www.jcb.co.jp/support/lost-and-stolen.html (đọc 2026-11-16): Dòng 97–105: sau báo mất, thẻ tìm lại có thể không dùng được theo JCB; không khái quát cho みどり.

## Còn mở

- Biên tập độc lập chưa thực hiện.

## Rà độc lập — /root/dc_all_trung (2026-11-16)

Đọc 16 cảnh Nhật/Việt và mọi nhánh; đọc B08 U13–U14, B04 U23, đối chiếu Visa/JCB nêu trên như nguồn tham khảo cho thẻ みどり hư cấu. S003/S009/S010 sửa 本人確認 trong bản Việt; S010 u05 sửa JA tránh mặc định thẻ còn dùng trước khi biết trạng thái dừng. Không còn lỗi mở.
