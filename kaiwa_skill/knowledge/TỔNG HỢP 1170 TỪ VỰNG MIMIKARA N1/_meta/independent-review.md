# Rà soát độc lập — TỔNG HỢP 1170 TỪ VỰNG MIMIKARA N1

Ngày 2026-11-11. Tôi dùng PDF `kaiwa_skill/vocab/1170 TỪ VỰNG MIMIKARA N1.pdf`, raw snapshot ghim trong `book.json`, ảnh cache `kaiwa_skill/.cache/clean/1170-mimikara-n1/pNNNN.png`, bảy chapter bảng và `units.jsonl`. Tôi mở từng ảnh được ghi dưới đây, đối chiếu dải STT, thứ tự và năm cột với raw/clean. Kiểm đẳng thức 1170 hàng raw–clean trong `coordinator-review.md` là bằng chứng bổ trợ về cấu trúc, không thay cho việc xem ảnh.

## Tiến độ theo ảnh đã mở

- **PDF1–10:** Đã mở đủ 10 ảnh. Dải STT **1–168** liên tục; bảng có đúng năm cột STT, HIRAGANA, KANJI, ÂM HÁN VIỆT, NGHĨA. Trang 1 xác nhận nhan đề; các ô trống và trường hợp có nhiều cách viết/tiểu từ ở PDF7–10 giữ nguyên hình thức nguồn. Chưa thấy lệch clean với ảnh. Dòng trích dẫn, `MINATO DORIMU` và Fanpage là dàn trang/branding, không phải hàng từ vựng.
- **PDF11–20:** Đã mở đủ 10 ảnh. Dải STT **169–336** liên tục, bao gồm hai dòng cùng cách đọc `かえりみる` ở STT173–174 với Kanji khác nhau, và cặp cách viết ở STT242. Các ô trống và năm cột phù hợp ảnh. Đã xem ảnh PDF20 độ phân giải cao để phân biệt `しや` (STT322) với `しゃ`; ảnh in `しや`, khớp clean nên không ghi issue. Chưa thấy lệch clean với ảnh.
- **PDF21–30:** Đã mở đủ 10 ảnh. Dải STT **337–506** liên tục. PDF23–29 có các nhóm động từ ghép, cách viết Nhật và ô Kanji/âm Hán Việt trống; PDF29–30 chuyển sang từ Katakana với hai cột ấy trống. Đã so hình thức các ô, cách đọc và nghĩa trong năm cột; chưa thấy lệch clean với ảnh.
- **PDF31–40:** Đã mở đủ 10 ảnh. Dải STT **507–676** liên tục. PDF31–32 tiếp nối từ Katakana rồi chuyển sang phó từ; PDF33–36 chứa biến thể cách đọc, cách viết và nhiều ô trống; PDF37–40 chuyển sang danh từ. Đã so năm cột và thứ tự hàng; chưa thấy lệch clean với ảnh. Các nghĩa nguồn có thể rộng hoặc hẹp được giữ theo PDF, không tự sửa.
- **PDF41–50:** Đã mở đủ 10 ảnh. Dải STT **677–846** liên tục. PDF41–48 có nhóm danh từ, động từ và tính từ với ô Kanji/âm Hán Việt trống xen kẽ; PDF48–50 chuyển sang Katakana. Các biến thể có tiểu từ và cách viết được giữ theo ảnh. Chưa thấy lệch clean với ảnh.
- **PDF51–60:** Đã mở đủ 10 ảnh. Dải STT **847–1016** liên tục. PDF51–55 là tính từ với nhiều ô trống và cách viết Kanji khác nhau; PDF56–60 là danh từ/biểu thức, có cả bảng STT1000–1016. Đã đối chiếu năm cột và ranh giới trang; chưa thấy lệch clean với ảnh.
- **PDF61–70:** Đã mở đủ 10 ảnh. Dải STT **1017–1170** liên tục; PDF67–70 có các biến thể trong ngoặc và nhiều ô Kanji/âm Hán Việt trống. PDF68 được xem lại ở 300 dpi: **STT1132 in `きっちり（と）`**, trong khi raw snapshot và bản clean cũ chỉ ghi `きっちり`. Đã sửa riêng ô HIRAGANA trong chapter theo ảnh, ghi chú sau bảng, đánh dấu `u-vocab-p0068` `needs_review` vì raw vẫn thiếu `（と）`; không sửa nguồn. PDF69 STT1159 và PDF70 STT1165 đúng là in các cụm nghĩa đã được gắn nghi vấn; giữ nguyên bảng, ghi chú và trạng thái `needs_review` của hai unit đó.

## Kết luận và giới hạn

- Đã mở và so **70/70 ảnh**, đủ **1170/1170 STT** với năm cột. Chỉ thấy một lỗi chép biến thể từ PDF sang raw/clean ở STT1132; đã sửa chapter. Không thấy thiếu hàng, lặp STT hoặc lệch cột khác khi rà ảnh.
- Cụm nghĩa nguồn ở STT1159/1165 vẫn chưa có xác nhận bằng từ điển; phần review này xác nhận chúng được chép đúng PDF, không khẳng định chúng đúng nghĩa tiếng Nhật. Các gloss rộng/hẹp khác không được kết luận là lỗi khi chưa có bằng chứng cụ thể.
- Bản `book.md`/`search.jsonl` là đầu ra build cũ và sẽ được root làm mới sau khi nhận chapter/metadata đã sửa.

## Trạng thái

Rà độc lập hoàn tất phạm vi PDF1–70. Chương `tu-vung-1017-1170.md` và unit68 đã đổi; các chapter khác giữ nguyên. Đã cập nhật editorial log và checkpoint chương bị sửa.
