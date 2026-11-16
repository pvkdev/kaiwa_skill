# T-039 — nhật ký biên soạn

Đã rà catalog27 SOURCE_LABELS, đọc B08 U13–U14 dòng 356–412 về lời hỏi ở ngân hàng/ATM; đọc sj-trung-10 lesson/practice, gắn ～かと khi thực sự có. Đọc trực tiếp trang Japan Post Bank đổi địa chỉ/tên dòng 64–139, FAQ chuyển liên ngân hàng dòng 794–800, cảnh báo cuộc gọi giả danh dòng 48–55. Các điều kiện này là của Japan Post Bank, không áp dụng máy móc cho ngân hàng あおば hư cấu; mọi hẹn, giấy, lý do hạn chế và trạng thái chuyển tiền trong cảnh phải do chính ngân hàng hư cấu kiểm. Không hứa mở lại tài khoản, hoàn tiền hoặc thời điểm chuyển đến. Với cuộc gọi lạ, người học dùng số trên thẻ/trang chính thức tự gọi lại, không nói mật khẩu hay mã PIN.

- Đã đối chiếu V10: 20 cảnh, 5 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Mô tả thao tác bị lỗi và phần vẫn dùng được, ngân hàng kiểm nguyên nhân.
- S002 (E01, routine): Xác minh an toàn, không để nhân viên hỏi PIN bằng lời.
- S003 (E01, pending): Nối S001: chờ có mốc và số tham chiếu, tránh chuyển lặp khi chưa biết trạng thái.
- S004 (E01, misunderstanding): Nối S001: sửa nhầm máy lỗi với hạn chế giao dịch, nguyên nhân cụ thể vẫn pending.
- S005 (E02, routine): Tên khác một chữ, hỏi nguồn và thủ tục, không tự sửa hay khẳng định giao dịch bị chặn vì thế.
- S006 (E02, routine): Chưa cập nhật chỉ vì nói miệng; kênh/giấy tùy tài khoản hư cấu.
- S007 (E02, conditional): Nối S006: thiếu giấy, không nói đã đổi; hẹn quay lại với danh sách cụ thể.
- S008 (E02, alternative): Nối S005: quầy chuyển bộ phận có số tham chiếu, chưa hứa sửa ngay.
- S009 (E03, routine): Số tiền/ngày hư cấu, phân lệnh chuyển và tiền đến, không hứa giờ.
- S010 (E03, pending): Nối S009: lệnh được nhận, tiền đến chưa rõ, số tra và tránh gửi lặp.
- S011 (E03, misunderstanding): Nối S009 theo nhánh nhầm ngày, sửa điều kiện tra theo biên nhận gốc.
- S012 (E03, alternative): Nối S009: người gửi tra ở ngân hàng gửi, người nhận tự xem tài khoản nhận, không áp quy tắc JP cho mọi bank.
- S013 (E04, routine): Gọi đúng số về hạn chế tài khoản, không lẫn số tra khoản chuyển.
- S014 (E04, follow_up): Nối S013: xác minh xong không đồng nghĩa giao dịch dùng được, bước tiếp cụ thể.
- S015 (E04, unresolved): Nối S013: unresolved với người phụ trách và hẹn, không tự khẳng định nguyên nhân.
- S016 (E04, resolved): Nối S013: phân trách nhiệm kiểm trạng thái và chủ tài khoản xác minh liên hệ, không khẳng định đã mở lại.
- S017 (E05, problem): Nối S016: xác minh cuộc gọi qua số độc lập, không tiết lộ bí mật, dù người gọi tự xưng nhân viên.
- S018 (E05, misunderstanding): Nối S017: gọi lại chính thức, khác giấy vì mục đích khác, cần danh sách riêng.
- S019 (E05, pending): Nối S018: người phụ trách/hạn cụ thể, tách hai case và kênh xác minh.
- S020 (E05, follow_up): Nối S019: hạn chế đã gỡ nhưng giao dịch cũ vẫn độc lập, tiếp tục tra, không hứa tiền đến.

## Nguồn đã dùng

- b08: B08 どんどん話せる！日本語会話フレーズ大特訓 必須700, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md` dòng 356–412: Chức năng hỏi ngân hàng, ATM và giấy, không dùng làm chính sách tài khoản.
- jp_change: Japan Post Bank: 住所・氏名・印章の変更, https://www.jp-bank.japanpost.jp/tetuzuki/henko/tzk_hnk_henko.html (đọc 2026-11-16): Dòng 64–139: cập nhật tên/địa chỉ cần đối chiếu giấy và kênh phù hợp theo tài khoản; chỉ làm tiền lệ nghiên cứu.
- jp_safety: Japan Post Bank: 不審な電話について, https://www.jp-bank.japanpost.jp/crime/crm_kanyu.html (đọc 2026-11-16): Dòng 48–55: không nói số tài khoản/PIN cho cuộc gọi lạ; xác minh kênh qua đầu mối chính thức.
- jp_transfer: Japan Post Bank FAQ: 他の金融機関への振込時間, https://faq.jp-bank.japanpost.jp/faq_detail.html?id=1267 (đọc 2026-11-16): Dòng 794–800: giờ phản ánh thay đổi, người gửi hỏi ngân hàng đã chuyển để tra trạng thái; không hứa thời điểm.

## Còn mở

- Biên tập độc lập chưa thực hiện.
