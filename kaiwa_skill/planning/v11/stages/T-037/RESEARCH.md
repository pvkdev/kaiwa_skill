# T-037 — nhật ký biên soạn

Đã rà SOURCE_LABELS catalog27 tìm 年金/保険料 (không có mục chuyên biệt); đọc B04 Unit23 dòng 1–75 để lấy khung lời hỏi điện thoại và chọn đúng đầu mối, đọc sj-trung-09 lesson/practice. Đọc Japan Pension Service về đặt tư vấn (cập nhật 2026-09-30, dòng 173–194, 256–266), tư vấn đa ngôn ngữ (dòng 55–123, có tiếng Việt và các nhánh hỏi khác nhau), và miễn/hoãn đóng quốc dân (cập nhật 2026-11-05, dòng 173–240). Danh mục miễn/hoãn là chế độ phải nộp đơn và xét, không tự áp dụng. Mọi lịch, số hồ sơ và giai đoạn việc làm trong cảnh là hư cấu; không suy ra quyền nhận lương hưu hay số khoản đóng. Quầy đối chiếu hồ sơ và yêu cầu xác nhận từ nơi trả lương nếu cần.

- Đã đối chiếu V10: 16 cảnh, 4 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Đặt tư vấn theo loại thông báo, không giả định mọi việc bắt buộc hẹn.
- S002 (E01, routine): Hỗ trợ tiếng Việt có nguồn JPS nhưng giờ cụ thể cần kiểm và xác nhận.
- S003 (E01, pending): Nối S001: hết lịch không đồng nghĩa tự kéo dài hạn; tìm kênh phù hợp và hỏi hạn trực tiếp.
- S004 (E01, misunderstanding): Nối S001: sửa nhầm văn phòng bằng số hẹn/địa chỉ, không đưa địa chỉ hư cấu như thực tế.
- S005 (E02, routine): Đối chiếu giai đoạn theo dữ kiện và hồ sơ, không suy ra quyền lợi.
- S006 (E02, problem): Nối S005: làm từ tháng 4 không tự chứng minh ghi nhận tháng 4 sai; yêu cầu xác minh.
- S007 (E02, unresolved): Nối S005: giữ ngày chưa rõ, không bịa mốc để lấp hồ sơ.
- S008 (E02, conditional): Nối S006: xác định cần công ty xác nhận ngày tham gia, không áp đặt tên giấy cụ thể.
- S009 (E03, routine): Khó đóng cần phân loại giấy và hỏi chế độ phù hợp, không hứa miễn.
- S010 (E03, routine): Ba lựa chọn được phân biệt, điều kiện xét cá nhân và cần đơn chứ không tự động.
- S011 (E03, pending): Nối S010: chưa chọn chế độ, chủ động hỏi hạn trên giấy và tái tư vấn.
- S012 (E03, misunderstanding): Nối S010: sửa tự động miễn, giữ xét duyệt riêng và thời hạn cần hỏi.
- S013 (E04, routine): Quay lại với chứng cứ công ty; nhận giấy khác kết luận sửa xong.
- S014 (E04, pending): Nối S013: tiến độ chờ rõ và kênh hỏi, không tuyên bố dữ liệu đã sửa.
- S015 (E04, problem): Nối S013: cải thiện một phần nhưng còn sai khác một ngày, tiếp tục tra nguồn.
- S016 (E04, resolved): Nối S013: trách nhiệm của công ty, quầy và người học cùng mốc hỏi; chưa nhận kết quả chỉnh sửa.

## Nguồn đã dùng

- jps_appt: Japan Pension Service: 予約相談について, https://www.nenkin.go.jp/section/guidance/yoyaku.html (đọc 2026-11-16): Dòng 173–194 và 256–266: có tư vấn hẹn, kiểm lịch sử ghi nhận và thông báo; không phải mọi việc đều cần hẹn.
- jps_lang: Japan Pension Service: Consultations in multiple languages, https://www.nenkin.go.jp/international/english/consult/interpretation_eg.html (đọc 2026-11-16): Dòng 55–123: có hỗ trợ tiếng Việt, chủ đề và kênh hỏi; cần hỏi khả dụng theo buổi.
- jps_relief: Japan Pension Service: 国民年金保険料の免除制度・納付猶予制度, https://www.nenkin.go.jp/service/kokunen/menjo/20150428.html (đọc 2026-11-16): Dòng 173–240: miễn/hoãn đóng quốc dân cần hồ sơ và phê duyệt, điều kiện khác nhau; không hứa đương sự đủ điều kiện.

## Còn mở

- Biên tập độc lập chưa thực hiện.

## Rà độc lập — /root/dc_all_trung (2026-11-16)

Đọc lại đủ 16 cảnh Nhật/Việt và các nhánh E01–E04; đối chiếu ba trang Japan Pension Service nêu trên. S005 sửa “xác minh người” thành “xác minh danh tính”; S010/S012 sửa bản Việt của 失業 thành “thất nghiệp”, tránh nhầm với tạm nghỉ. S009 là tình huống tạm nghỉ riêng; S011/S012 nối S010. Không còn lỗi mở.
