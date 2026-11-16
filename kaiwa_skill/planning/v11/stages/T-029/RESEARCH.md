# T-029 — nhật ký biên soạn

- Catalog27: tra 自炊・注文・配達・定期購入・変更・休止 trên toàn 27 sách; đọc B01 ẩm thực, B26 買い物. Kiểm 国民生活センター về điều kiện số phần/kỳ giao/thay đổi/hủy của dịch vụ thực phẩm định kỳ; các quy tắc lịch, phí và cách nhận của “みどり食材便” đều hư cấu, không chuyển chính sách của Pal System/Coop Deli sang cảnh.

- Đã đối chiếu V10: 25 cảnh, 5 sự kiện; giữ UID, thứ tự và nhánh continues_from. Bối cảnh giá, lịch, địa điểm và tên riêng nếu có là giả định của tình huống, không phải cam kết nhà cung cấp.
- Đọc chuyên đề trước và practice theo brief; chỉ gắn item ID khi cách nói hiện rõ trong lượt. Lời Nhật đều viết mới; nguồn sách/web là nền cho tình huống và cách hỏi.
- Rà từng cảnh độc lập bằng tiếng Nhật rồi tiếng Việt, kiểm lượt đích và lượt đáp, thử cả hai vai; đọc nối các nhánh continues_from theo riêng từng đường.

## Ghi chú từng cảnh

- S001 (E01, routine): Nêu số người/bữa/chu kỳ, chưa tự tạo đăng ký.
- S002 (E01, routine): Nội dung đổi theo tuần chỉ trong gói hư cấu; khả năng bỏ món còn cần kiểm.
- S003 (E01, conditional): Thứ Ba cố định trong dịch vụ hư cấu; chưa giả định giao không người nhận.
- S004 (E01, declined): Từ chối gói có món không dùng, hỏi gói khác nhưng chưa đăng ký.
- S005 (E01, resolved): Nối S003: có người nhận thứ Ba, tổng giả định 3600+400=4000; điều kiện tạm nghỉ riêng gói.
- S006 (E02, routine): Không tự cho phép để thực phẩm ở nơi chung; chờ người nhận/ban quản lý.
- S007 (E02, routine): Hỏi lịch và nhãn bảo quản cụ thể, không bịa nhiệt độ/hạn an toàn chung.
- S008 (E02, problem): Không đoán hàng đã giao; hai bên xác định vị trí hộp và đúng đầu mối lịch hẹn.
- S009 (E02, misunderstanding): Sửa địa chỉ công ty vs nhà trước giao, người giao xác nhận lại.
- S010 (E02, resolved): Nối S009: địa chỉ nhà đúng, kiểm một hộp/số phần; bên trong sẽ kiểm tiếp.
- S011 (E03, routine): Đổi nhu cầu về thời điểm cụ thể, chưa áp thay đổi khi chưa biết gói/giá.
- S012 (E03, routine): Không khẳng định đổi từng nguyên liệu phổ quát; hỏi hai cách xử lý.
- S013 (E03, conditional): Giữ kỳ này chưa đổi, hỏi lựa chọn riêng có mốc trả lời.
- S014 (E03, alternative): Phương án giảm thay vì bỏ, hỏi hiệu lực một kỳ để không giảm vô thời hạn.
- S015 (E03, resolved): Nối S014: khác mức chỉ một tuần, kỳ sau quay lại đúng hai người/ba bữa, phí riêng hợp đồng giả định.
- S016 (E04, routine): Thiếu món xác định bằng danh sách/mã, nêu mốc cần dùng; chưa tự hứa giao bổ sung.
- S017 (E04, problem): Không kết luận an toàn thực phẩm qua điện thoại; ghi giao trễ và hạn phản hồi.
- S018 (E04, pending): Pending có mốc/đầu mối/mã; không biến điều tra thành bổ sung chắc chắn.
- S019 (E04, alternative): Chọn không nhận món thay, kỳ sau chỉ đang cân nhắc; tiền chưa biết.
- S020 (E04, follow_up): Nối S019: sau xác nhận điều chỉnh ở khoảng giữa, kiểm tiền riêng và đủ món kỳ này.
- S021 (E05, routine): Xác định đúng hai kỳ ngừng, hỏi hạn và cơ chế nối lại.
- S022 (E05, misunderstanding): Sửa nhầm hủy vĩnh viễn thành nghỉ hai kỳ; chưa xác nhận hiệu lực khi chưa kiểm hạn.
- S023 (E05, conditional): Không giả vờ hủy kỳ đã khóa; người học có kế hoạch nhận hộp hiện tại.
- S024 (E05, follow_up): Follow-up về kỳ nối lại, giờ chỉ biết ngày, lượng và địa chỉ cần kiểm.
- S025 (E05, resolved): Nối S024: ngày/địa chỉ/lượng/tiền được xác nhận trước khi người học chấp nhận.

## Nguồn đã dùng

- b01: B01 5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày, `kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/05-am-thuc.md` dòng 73–85: Đọc ngữ cảnh hỏi thói quen tự nấu để xác định nhu cầu số bữa; lời thoại mới.
- regular: 国民生活センター — インターネットで注文する食事宅配に関する消費者トラブル, https://www.kokusen.go.jp/news/data/n-20241106_2.html (đọc 2026-11-16): Dịch vụ thực phẩm giao định kỳ: kiểm số phần, số kỳ, điều kiện thay đổi/ngừng và lịch nhận trước đăng ký. Không suy ra thời hạn của nhà cung cấp hư cấu.
- b26: B26 聞いて覚える話し方 日本語生中継 初中級編 1, `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編 1/chapters/05-bai-5.md` dòng 20–50: Đọc cách hỏi hàng giao, đặt và thay thế; lời thoại mới.

## Còn mở

- Biên tập độc lập chưa thực hiện.
