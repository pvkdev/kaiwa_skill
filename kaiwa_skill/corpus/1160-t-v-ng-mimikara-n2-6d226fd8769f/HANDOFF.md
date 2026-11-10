# Bàn giao đã chuyển đổi — 1160 TỪ VỰNG MIMIKARA N2

- Nguồn: `vocab/1160 TỪ VỰNG MIMIKARA N2.pdf`, SHA-256 `6d226fd8769f2e248518d8d32e542002738a13160e14a4ea90aaf102a67eab6d`.
- Phạm vi: 8 trang PDF. Đã mở ảnh gốc từng trang để đọc bố cục, sau khi record đã mở lại và đối chiếu. p0001–p0008 đều `verified`; `issue_count=0`; `build_current=true`. Build gồm `book.md`, `search.jsonl`, `build.json`; chờ coordinator kiểm mẫu và nghiệm thu.
- Worker `production_book_01` đã kết thúc phạm vi và release claim.
- Trang nên kiểm mẫu: p0003 (dải số nhảy 459→511), p0007 (bảng KATAKANA và các ô xuống dòng), p0008 (ô đỏ 1161, footer đa ngôn ngữ). Có thể thêm p0004 để kiểm bảng năm cột thông thường.
- Audit lần 2 đã mở lại toàn bộ 8 trang và crop 300 DPI từng header. Khẩu hiệu tiếng Việt và chữ logo thực có trên cả 8 trang: crop khẩu hiệu p0001–p0008 có SHA-256 giống hệt; crop logo p0001–p0006 và p0008 giống hệt, p0007 hơi khác bố cục. Quan sát ảnh toàn trang và crop từng không khớp; nguyên nhân hiển thị chưa xác định. Header được giữ trên cả 8 trang. Các lần bỏ header tạm thời trong draft đã được khôi phục trước khi verify/build.
- Lỗi nội dung thật đã sửa: dải MINATO giữa trang p0002 nằm sau hàng 170, p0004 sau 534, p0006 sau 901. p0007 đã đổi từ danh sách theo cột sang bảng theo hàng để giữ dải giữa sau 1064. Crop 300 DPI quanh từng ranh giới xác nhận. Nội dung các từ không đổi; hash Markdown p0001, p0003, p0005, p0008 giữ nguyên so với build trước. p0002, p0004, p0006, p0007 được record và verify lại với notes cụ thể.
- Footer p0008 có đúng bảy chữ `え` sau `ぜ` theo crop 300 DPI và text layer; Markdown giữ nguyên.
- Dữ kiện nguồn cần lưu ý: p0003 nhảy từ số 459 sang 511; số 460 không thấy trên bất kỳ trang nào; 461–510 nằm ở p0007. Dải 791–840 tiếp nối tại p0007–p0008. p0008 có ô đỏ `1161 パス`, dù tên tệp ghi 1160.
- Nháp và script tạm chỉ ở `.cache/work/production_book_01/`; không thuộc output/commit. Chỉ corpus là kết quả text cần bàn giao.
