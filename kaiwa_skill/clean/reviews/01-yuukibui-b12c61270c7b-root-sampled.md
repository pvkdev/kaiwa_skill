# Root QA mẫu — 本文冊

Đã mở ảnh PDF14/15 ở lượt trước và PDF30/42/43/49/130/131/135/137 trong lượt hiện tại. Đọc khung đối thoại ở30/42/130, toàn hội thoại43/131, bảng họ49, ví dụ135 và lời bạt137 để đối chiếu bản clean. Đây là10trang mẫu; chưa có lượt reviewer độc lập đọc toàn138trang.

Các sửa đã kiểm: khung tự giới thiệu đúng3ô theo thứ tự đơn vị–tên–nơi đến; 水泳の好きな方がいらっしゃったら giữ điều kiện tồn tại “nếu có ai thích bơi”; bỏ furigana phụ trợ tiêu đề bảng họ nhưng giữ đủ cách đọc/biến thể/ô trống; そろそろ終わりにしようか dịch thành đề nghị kết thúc ngày làm việc. Lượt phỏng vấn Ken/Sawada và13mục ngữ dụng trong các vùng mở giữ nguyên dữ kiện/ý; lời bạt đủ bốn đoạn, năm/tháng và bốn tên tác giả.

Các vùng mẫu sau sửa không còn vấn đề root nêu. Fullbook vẫn dựa author đối chiếu từng trang và báo cáo full-review.md; không gọi đây là full independent semantic review.

Source drift: root so snapshot với live, toàn138pages/*.md byte-identical, chỉbook.md/build.json/manifest.json khác. Chờ helper rebase kiểm normalization chỉ anchor/dòng trống, tạo snapshot mới và history; tuyệt đối không sửa corpus hoặc snapshot cũ. Sau rebase cần báo cáo cuối với hash metadata/units mới.

Hash các chapter có vùng mẫu (nội dung học không được đổi trong rebase metadata):

- `chapters/01-jiko-shoukai.md`: `459169beb5923326f2ca65a333b1dddca89c5bda640ee7d7ca19b16b3477350b`
- `chapters/04-kotowari.md`: `0b281055c67fffde7d8c037d25ab6a6990196a927761820dbc4e82c634477fd1`
- `chapters/06-aisatsu.md`: `03d082dc7a88f2945b98c2348f3560e2d0975eacae7a2fe74ce13c74484711a3`
- `chapters/20-mensetsu-shiken.md`: `247aee2607ed6c10f2c7e4a43290bde86a1969bef4099201e6aef842af50d8d9`
- `chapters/21-atogaki.md`: `e67e007a2d16f8d771efdfc477c3679d4922e33ac8f3fa26c2227aa2f37859d7`
