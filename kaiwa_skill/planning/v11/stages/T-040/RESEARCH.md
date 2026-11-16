# T-040 — nhật ký biên soạn

Đã rà nhãn toàn bộ catalog27, đọc B08 U13–U14 dòng 356–412 về ngôn ngữ giao dịch ngân hàng và B04 dòng 1–75 về hỏi qua điện thoại; đọc sj-trung-10 lesson/practice. Đọc trực tiếp trang Japan Post Bank quốc tế dòng 50–67 về kiểm mục đích/nguồn tiền, khả năng yêu cầu tài liệu và từ chối; FAQ phí dòng 794–800, tình trạng dòng 801–813, người nhận chưa thấy dòng 794–800, thông báo sửa dữ liệu dòng 799–804. Các nguồn chỉ làm tiền lệ nghiên cứu, mọi dịch vụ, giá, ngày, số tham chiếu và câu trả lời cụ thể trong cảnh là hư cấu của さくら送金. Phí/giá trị tới người nhận cần đơn vị gửi và ngân hàng nhận kiểm; không hứa số tiền hay ngày nhận. Trạng thái đã nhận đơn hoặc chuyển đi không tự bằng đã vào tài khoản. Việc sửa/hủy tùy trạng thái và chính đơn vị xác nhận, không tự hứa thành công.

- Đã đối chiếu V10: 16 cảnh, 4 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Hỏi tuyến gửi cụ thể, nhân viên tra trước khi nói nhận được; không đoán mạng lưới phục vụ.
- S002 (E01, routine): Đối chiếu đúng dữ liệu nguồn từ người nhận, không để quầy đoán phiên âm.
- S003 (E01, conditional): Nối S001: hỏi phí và lượng nhận theo tình huống 100.000 yên giả định, không hứa giá trị nhận.
- S004 (E01, misunderstanding): Nối S003: giải nhầm phí gửi với phí nhận; hành động là đưa bảng tách khoản.
- S005 (E02, routine): Mục đích thật theo giả định, nhân viên chỉ báo giấy sau kiểm từng hồ sơ.
- S006 (E02, pending): Nối S005: dừng trước khi chốt, không đoán số tài khoản; giữ tư vấn nhưng phải kiểm lại.
- S007 (E02, conditional): Nối S005: trả lời nguồn theo sự thật, hỏi phạm vi tài liệu, không hứa nhận đơn.
- S008 (E02, declined): Nối S005 nhánh từ chối: lý do trong phạm vi có thể nói, bước hỏi tiếp, xác nhận chưa gửi.
- S009 (E03, routine): Mốc/số tiền giả định, phân biệt nhận đơn với vào tài khoản, hỗ trợ tra theo tham chiếu.
- S010 (E03, pending): Nối S009: trạng thái pending có số tra, mốc hỏi lại và lời báo đúng cho mẹ.
- S011 (E03, misunderstanding): Nối S009 nhánh sai tên; lời nói miệng không tự sửa lệnh, không hứa sửa được.
- S012 (E03, follow_up): Nối S009: phân ai hỏi bên gửi, ai hỏi ngân hàng nhận; chưa tự chia sẻ dữ liệu nhạy cảm.
- S013 (E04, routine): Sai tên trước thông báo hoàn tất không đồng nghĩa có quyền sửa/dừng; tra trạng thái trước.
- S014 (E04, conditional): Nối S013: hỏi hai đường xử lý, phí và thời điểm; nhận yêu cầu không đồng nghĩa sửa/hủy thành công.
- S015 (E04, declined): Nối S014: quầy từ chối quyền sửa, bàn giao với hai số riêng, chưa gọi là đã sửa.
- S016 (E04, resolved): Nối S013 nhánh sau xử lý: nhận yêu cầu ≠ sửa có hiệu lực ≠ tiền đã đến; follow-up có số và người nhận kiểm.

## Nguồn đã dùng

- b08: B08 どんどん話せる！日本語会話フレーズ大特訓 必須700, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md` dòng 356–412: Mẫu hỏi và xác nhận tại ngân hàng, không lấy làm quy định chuyển quốc tế.
- jp_fee: Japan Post Bank FAQ: 国際送金の手数料, https://faq.jp-bank.japanpost.jp/faq_detail.html?id=11143 (đọc 2026-11-16): Dòng 794–800: phí gửi riêng và có thể có khoản khấu trừ trung gian tùy nơi nhận; cảnh luyện hỏi tách khoản, không nêu giá thật.
- jp_check: Japan Post Bank: 国際送金をご利用いただくお客さまへのお願い, https://www.jp-bank.japanpost.jp/kojin/sokin/kokusou/kj_sk_ks_goriyou.html (đọc 2026-11-16): Dòng 50–67: ngân hàng có thể kiểm mục đích/nguồn tiền, yêu cầu tài liệu hoặc từ chối theo trường hợp; không chuyển thành quy tắc của dịch vụ hư cấu.
- b04: B04 しごとの日本語 電話応対 基礎編, `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/24-Unit23-問い合わせをする.md` dòng 1–75: Cách nêu việc và số tham chiếu khi gọi hỏi.
- jp_status: Japan Post Bank FAQ: 国際送金の取引状況, https://faq.jp-bank.japanpost.jp/faq_detail.html?id=11133 (đọc 2026-11-16): Dòng 801–813: các bước nhận đơn, xử lý, gửi đi và vào tài khoản khác nhau; trạng thái cụ thể trong cảnh do đơn vị hư cấu xác nhận.
- jp_received: Japan Post Bank FAQ: 受取口座への入金確認, https://faq.jp-bank.japanpost.jp/faq_detail.html?id=11140 (đọc 2026-11-16): Dòng 794–800: có lúc cần người nhận tự kiểm tài khoản nhận; tránh kết luận đã nhận tiền chỉ từ bên gửi.
- jp_correct: Japan Post Bank FAQ: 送金人・受取人情報の不備通知, https://faq.jp-bank.japanpost.jp/faq_detail.html?category=89&id=11137&page=1 (đọc 2026-11-16): Dòng 799–804: khi có lỗi dữ liệu có thể có yêu cầu sửa theo thông báo; không khái quát rằng mọi giao dịch đều sửa được.

## Còn mở

- Biên tập độc lập chưa thực hiện.

## Rà độc lập — /root/dc_all_trung (2026-11-16)

Đọc đủ 16 cảnh Nhật/Việt và mọi nhánh E01–E04; đọc B08 U13–U14, B04 U23, đối chiếu các trang Japan Post Bank nêu trên như tiền lệ nghiên cứu, không áp sang dịch vụ さくら送金 hư cấu. S009 u02 sửa 本人確認 trong bản Việt thành “xác minh danh tính”. Các nhánh đều giữ riêng trạng thái đơn, yêu cầu sửa và tiền đến. Không còn lỗi mở.
