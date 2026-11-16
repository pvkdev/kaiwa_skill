# T-038 — nhật ký biên soạn

Đã rà catalog27 SOURCE_LABELS và đọc B08 phần bệnh viện dòng 326–354: câu hỏi không có giấy bảo hiểm là chức năng giao tiếp, nhưng thuật ngữ 保険証 trong sách đã cũ, nên cảnh mới dùng マイナ保険証/資格確認書 phù hợp hiện tại. Đã đọc sj-trung-09 lesson/practice. Đọc MHLW trang 資格確認書 dòng 260–297 và Kyokai Kenpo trang khám với マイナ保険証/資格確認書 dòng 112–130, 166–175: 資格情報のお知らせ riêng lẻ không đủ để tiếp nhận khám bảo hiểm. Đọc Shinjuku về báo đổi quốc bảo khi rời/đến công ty dòng 203–208, 222–268. Các nhân viên trong cảnh chỉ hỏi và kiểm hồ sơ cá nhân, không hứa tư cách, mức trả, hoàn tiền hay hiệu lực hồi tố; ngày/lịch và phòng khám 青葉 đều hư cấu. Tách người quyết tư cách bảo hiểm (bên bảo hiểm), người xác nhận ngày ở công ty (HR), và cơ sở khám (cách tiếp nhận/chi phí hôm đó).

- Đã đối chiếu V10: 20 cảnh, 5 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Hai mốc việc làm chưa tự quyết tư cách trong khoảng trống; hỏi hai bên.
- S002 (E01, routine): Phân biệt ngày nghỉ và ngày mất tư cách, không chốt khoảng trống trước khi có ngày mới.
- S003 (E01, alternative): Nối S001: chuyển đúng đầu mối xác nhận ngày tham gia công ty, quầy thành phố xử lý phần của họ.
- S004 (E01, pending): Nối S001: chưa đồng bộ, có số hẹn kiểm lại, không tự kết thúc.
- S005 (E02, routine): Cùng hộ không đồng nghĩa cùng bảo hiểm, giữ từng cá nhân.
- S006 (E02, problem): Nối S005: phân nơi phát hành và chủ quản dữ liệu, chưa tự sửa phiên âm.
- S007 (E02, conditional): Nối S005: tư vấn trước khác nhận hồ sơ, không tự suy diện phụ thuộc.
- S008 (E02, misunderstanding): Nối S005: làm rõ chủ thể, tránh áp một người lên hồ sơ người kia.
- S009 (E03, routine): Hiện dùng thuật ngữ mới, không hứa bảo hiểm chi trả khi chưa xác nhận.
- S010 (E03, routine): Chia thẩm quyền cơ sở khám và bên bảo hiểm, xin phí trước khi tiếp nhận.
- S011 (E03, pending): Nối S010: chưa kiểm được, phí chưa biết trước nội dung khám, hoàn trả không bảo đảm.
- S012 (E03, follow_up): Nối S009: truyền đúng thông tin phòng khám, bảo hiểm xác định tư cách, không tự hứa hoàn tiền.
- S013 (E04, routine): Kỳ, người, hộ được kiểm trên giấy và hồ sơ, không suy từ cùng địa chỉ.
- S014 (E04, misunderstanding): Nối S013: phân ngày đi làm và ngày có tư cách, chưa kết luận phí trùng.
- S015 (E04, pending): Nối S013: kiểm tiền còn chờ nhưng hạn cần hỏi ngay, không ngầm hoãn nghĩa vụ.
- S016 (E04, resolved): Nối S014: trách nhiệm công ty và quầy rõ, chỉnh số tiền chưa chắc.
- S017 (E05, problem): Nối S016: HR xác nhận đã gửi, chưa khẳng định đã được bảo hiểm nhận hoặc thành phố phản ánh.
- S018 (E05, misunderstanding): Nối S017: ngày làm và ngày có tư cách không tự đồng nhất, HR hỏi bảo hiểm để xác nhận.
- S019 (E05, conditional): Nối S018: tư cách còn kiểm, viện phụ trách tiếp nhận và phí; không bảo đảm mức chi trả.
- S020 (E05, follow_up): Nối S019: có kết quả bên bảo hiểm nhưng chưa có credential, bệnh viện kiểm và báo phí, không hứa tự động bao trả.

## Nguồn đã dùng

- city: Shinjuku: 国民健康保険の届出について, https://www.city.shinjuku.lg.jp/hoken/file02_02_00001.html (đọc 2026-11-16): Dòng 203–208, 222–268: đổi từ bảo hiểm công ty sang quốc bảo và ngược lại cần xác minh/dựng hồ sơ riêng; không áp cho mọi người.
- mhlw: MHLW: 資格確認書について（マイナ保険証を使わない場合の受診方法）, https://www.mhlw.go.jp/stf/newpage_45470.html (đọc 2026-11-16): Dòng 260–297: loại giấy hiện hành, hình thức/hạn tùy bảo hiểm, hỏi bên đang tham gia.
- kyokai: Kyokai Kenpo: マイナ保険証等での受診, https://www.kyoukaikenpo.or.jp/benefit/mynumber_insurance_card/001/ (đọc 2026-11-16): Dòng 112–130, 166–175: マイナ保険証 hoặc 資格確認書 khi khám, 資格情報のお知らせ một mình không dùng được.

## Còn mở

- Biên tập độc lập chưa thực hiện.

## Rà độc lập — /root/dc_all_trung (2026-11-16)

Đọc đủ 20 cảnh Nhật/Việt, năm sự kiện và mọi nhánh tiếp nối; đối chiếu Shinjuku, MHLW, Kyokai Kenpo nêu trên. S009 u04 làm rõ bệnh nhân hỏi bên bảo hiểm, phòng khám giải thích tiếp nhận và phí. S012 u03 sửa lời kể để khớp S009: phòng khám giải thích khoản trả hôm nay, bên bảo hiểm cùng tham gia xử lý sau. Không còn lỗi mở.
