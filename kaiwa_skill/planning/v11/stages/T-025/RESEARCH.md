# T-025 — nhật ký biên soạn

- Catalog27: tra 注文・配達・在庫・取り寄せ・電話・確認 trên toàn 27 sách; đọc B26 bài 買い物 và B04 Unit 23. Tra 国民生活センター về kiểm màu/cỡ/số lượng khi nhận hàng qua internet; chỉ vận dụng thao tác kiểm món, không suy chính sách mua qua điện thoại. Cửa hàng “青空” cùng giá, phí, vùng giao, lịch và điều kiện sửa đơn đều hư cấu.

- Đã đối chiếu V10: 25 cảnh, 5 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Nêu loại/cỡ/màu/lượng, nhân viên chưa khẳng định tồn kho.
- S002 (E01, routine): Hết mẫu đầu, hỏi hàng tương tự và giá tổ hợp trước quyết định.
- S003 (E01, conditional): Chi nhánh khác còn hàng trong tình huống giả định; thời hạn nhận chưa xác nhận.
- S004 (E01, declined): Nhánh từ chối vì mốc giao, không lén tạo đơn.
- S005 (E01, resolved): Nối S003 theo nhánh hàng kịp thứ Năm; chỉ nhắc món/lượng, chưa chốt khi chưa biết giá.
- S006 (E02, routine): Số tiền giả định 5400+600, nhắc chưa phải tổng cuối khi chưa kiểm vùng.
- S007 (E02, routine): Địa chỉ giả định tách từng phần, chưa kết luận vùng/phí.
- S008 (E02, misunderstanding): Sửa đúng phần sai 202→302, nhắc lại tòa và lối vào.
- S009 (E02, conditional): Phí cộng và tổng đúng 5400+600+300=6300, vẫn chưa chốt khi thiếu lịch/cách trả.
- S010 (E02, resolved): Nối S009, chỉ chốt sau khi có tổng, khung, cách trả và địa chỉ.
- S011 (E03, routine): Báo thay số lượng, chưa tự cho đã sửa; mã đơn hư cấu 816.
- S012 (E03, conditional): Đã đóng gói không đồng nghĩa đã gửi; nhân viên kiểm trước khi trả lời.
- S013 (E03, declined): Nhánh không đổi được, không hứa quyền trả hàng; đơn còn bốn.
- S014 (E03, alternative): Phương án thay giờ thay món; lịch cũ giữ cho tới khi có xác nhận.
- S015 (E03, resolved): Nối S014, số lượng không đổi, tổng 4×1800+600=7800 là giả định của đơn này.
- S016 (E04, routine): Kiểm số kiện trước ký nhận, chưa tự khẳng định đúng món bên trong.
- S017 (E04, problem): Tách trách nhiệm hỏi vị trí kiện và nội dung đơn; ghi thiếu trước khi nhận phần đúng.
- S018 (E04, misunderstanding): Sửa nhầm hình thức thanh toán trước khi giao tiền, không coi đã trả trước.
- S019 (E04, pending): Pending rõ; chưa ký nhận toàn đơn hoặc hứa thời gian kiện thiếu.
- S020 (E04, resolved): Nối S019: nhận đúng phần có thật, giữ một kiện chưa đến và tiền chưa giải quyết.
- S021 (E05, routine): Gọi đúng mã và chi tiết thiếu, không suy kết quả điều tra hay thanh toán.
- S022 (E05, alternative): Hai lựa chọn thật, cả lịch nhập và giá chưa rõ; người học chưa đồng ý.
- S023 (E05, conditional): Nêu mâu thuẫn mốc dùng thật, hỏi phương án khác; chưa tự giữ lịch giao.
- S024 (E05, follow_up): Theo dõi mốc thứ Hai trễ; Satō hứa cập nhật 6 giờ nhưng chưa hứa ngày giao mới.
- S025 (E05, resolved): Nối S024: kiểm đủ ba ghế và thanh toán đúng tổng giả định, nhân viên xác nhận hoàn tất.

## Nguồn đã dùng

- b26: B26 聞いて覚える話し方 日本語生中継 初中級編 1, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/05-bai-5.md` dòng 20–50: Mẫu hỏi hàng đặt, giao, đổi và thời gian; phát triển thành hội thoại điện thoại mới.
- b04: B04 しごとの日本語 電話応対 基礎編, `kaiwa_skill/knowledge/しごとの日本語 電話応対 基礎編/chapters/24-Unit23-問い合わせをする.md` dòng 27–47: Cách hỏi đúng đầu mối và rõ từng nội dung qua điện thoại.
- check: 国民生活センター — インターネットショッピングで購入した商品はクーリング・オフできるの？, https://www.kokusen.go.jp/t_box/data/t_box-faq_qa2015_20.html (đọc 2026-11-16): Trang nói về mua trực tuyến, khuyên kiểm ngay món/số lượng/màu/cỡ khi nhận. Chỉ dùng nguyên tắc kiểm thực tế; không áp quy định trả hàng trực tuyến cho đơn gọi điện.

## Còn mở

- Biên tập độc lập chưa thực hiện.
