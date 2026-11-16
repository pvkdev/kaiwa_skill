# T-033 — nhật ký biên soạn

Đã rà catalog27 SOURCE_LABELS cho 市役所/窓口, đọc B08 chương chỉ đường dòng 45–78 và B18 kính ngữ quầy dòng 100–113 (lưu ý bản in có tiểu từ nghi vấn, không sao chép). Đã đọc sj-trung-09 lesson/practice. Nguồn chính thống Shinjuku hướng dẫn khai địa chỉ cư dân nước ngoài dòng 231–278, cấp 住民票 dòng 165–195, quốc bảo dòng 194–201 và 251–268. Các trang này là ví dụ thực, không tự áp dụng địa chỉ, giờ và giấy tờ cho thành phố 青葉 hư cấu. Cảnh luyện lời hỏi để quầy kiểm theo hồ sơ cá nhân; mọi lịch, số quầy và cách nhận giấy trong cảnh là giả định của thành phố hư cấu.

- Đã đối chiếu V10: 20 cảnh, 5 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Hỏi đúng quầy và mốc chuyển; hướng dẫn viên không khẳng định hồ sơ đủ.
- S002 (E01, alternative): Nối S001: thứ tự quầy rõ, không suy ra bảo hiểm tự xong.
- S003 (E01, problem): Nối S001 theo nhánh khác: đã quá giờ, lấy lịch hư cấu và kênh kiểm, không khẳng định đã nộp.
- S004 (E01, misunderstanding): Nối S001 theo nhánh không biết thuật ngữ; diễn đạt nhu cầu và ngày, được chỉ quầy.
- S005 (E02, routine): Phân biệt rời nơi cũ và bắt đầu ở nơi mới; kiểm trước ghi.
- S006 (E02, misunderstanding): Nối S005: sửa cách đọc nhưng không đổi chữ tên, tiếp tục đối chiếu địa chỉ.
- S007 (E02, problem): Nối S005: đối chiếu nguồn số phòng, không in giấy với dữ liệu chưa đúng.
- S008 (E02, conditional): Nối S005 theo nhánh nhiều người, không hứa đại diện luôn hợp lệ.
- S009 (E03, routine): Danh sách được lọc theo trường hợp, không áp dụng mọi mục cho mọi người.
- S010 (E03, conditional): Nối S009: thiếu bản gốc, chưa nói đã nhận; hỏi rõ lưu tiến độ và bước quay lại.
- S011 (E03, pending): Nối S010: chưa xác nhận, hẹn cụ thể kênh/giờ và đánh dấu chưa hoàn tất.
- S012 (E03, follow_up): Nối S010: mang đúng giấy còn thiếu, không tự cho rằng đã hoàn tất.
- S013 (E04, routine): Hỏi mục đích, quầy không đoán thay yêu cầu của công ty.
- S014 (E04, alternative): Nối S013: so sánh theo mục/định dạng, quyết định theo nơi nhận, không tuyên bố hai giấy thay thế được.
- S015 (E04, pending): Nối S013 theo nhánh chờ: ngày/nơi/kênh/giấy nhận cụ thể, chưa nói đã cấp.
- S016 (E04, problem): Nối S015: phát hiện lỗi thật trên giấy đã nhận, ngừng dùng và kiểm nguồn.
- S017 (E05, problem): Nối S016: hai quầy không đồng bộ ngay, bảo hiểm không tự xong; nhân viên kiểm liên quầy.
- S018 (E05, misunderstanding): Nối S017: giải nghĩa nhận yêu cầu khác dữ liệu cập nhật, chưa tuyên bố sửa đã có hiệu lực.
- S019 (E05, pending): Nối S018: hẹn trạng thái rõ, trách nhiệm hỏi liên quầy ở nhân viên, không tạo hai cuộc gọi vô ích.
- S020 (E05, follow_up): Nối S019: hai quầy xác nhận số phòng đúng, bảo hiểm mới nhận đơn, không hứa tư cách đã duyệt.

## Nguồn đã dùng

- b08: B08 どんどん話せる！日本語会話フレーズ大特訓 必須700, `kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md` dòng 45–78: Mẫu hỏi nơi đến và quầy, không dùng sách làm quy tắc hành chính.
- move: Shinjuku: Notification Procedures for a Change of Address for Foreign Residents, https://www.foreign.city.shinjuku.lg.jp/en/wp-content/uploads/sites/3/2025/03/2todoke_e2025.pdf (đọc 2026-11-16): Dòng 231–278: thủ tục chuyển đến, giấy tùy trường hợp, xác minh cá nhân, phiên dịch và giờ đặc biệt cần hỏi riêng.
- nhi: Shinjuku: 国民健康保険の届出について, https://www.city.shinjuku.lg.jp/hoken/file02_02_00001.html (đọc 2026-11-16): Dòng 194–201, 251–268: xử lý bảo hiểm cần xác minh riêng, thông tin liên thông có thể trễ; không tự kết luận đủ tư cách.
- cert: Shinjuku: 住民票の写し等の交付, https://www.foreign.city.shinjuku.lg.jp/jp/kurashi/jyuminhyoutsushi/ (đọc 2026-11-16): Dòng 165–195: có hai loại chứng nhận và cần giấy xác minh; hỏi cơ quan nhận loại nào.

## Còn mở

- Biên tập độc lập chưa thực hiện.
