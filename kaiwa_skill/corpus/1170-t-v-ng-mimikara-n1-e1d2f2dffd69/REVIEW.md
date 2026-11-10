# Nghiệm thu — Mimikara N1

Quyết định: ACCEPTED. Nguồn `vocab/1170 TỪ VỰNG MIMIKARA N1.pdf` (từ `kaiwa_skill/`), 70 trang vật lý; SHA-256 `e1d2f2dffd69aadc03a195bd23564f29a481fbfd8bc43accf9715a9f16c38ba0`. Worker `production_book_03`, gpt-6-sol/high; coordinator gpt-6-astra/high; skill 0.2.1. Trạng thái cuối: 70 verified, 0 issues, build hiện tại, claim đã release.

## Phạm vi đối chiếu

Worker mở và đối chiếu 100% trang, riêng quote/Fanpage và các cột nhỏ được crop phóng to. Coordinator đọc toàn bảng trên các trang 1,4,8,9,13,14,20,22,29,40,64,67,69,70, gồm bảng mở đầu, danh từ/động từ/tính từ, chuyển sang Katakana với ô trống, bảng có watermark, nghĩa nhiều dòng và bảng cuối cùng với logo riêng. Ngoài mẫu toàn bảng, coordinator mở crop các hàng được worker gắn cờ trên các trang khác. Sổ `COORDINATOR_AUDIT.json` ghi chính xác các hàng và hash.

Sau lỗi ký tự Nhật, worker đã mở lại crop 300 DPI của cả hai cột Nhật, so toàn bộ 102 hàng trên p39–41 và p54–56, kể cả kana đầu/cuối. Sau lỗi tiếng Việt, worker mở lại hai cột Việt toàn bộ 120 hàng trên p15–17 và p66–70. Đây là lần rà rộng của worker; coordinator không tuyên bố đã tự đọc toàn bộ các nhóm mở rộng đó ngoài các mẫu và hàng đã ghi.

## Lỗi đã sửa và kiểm lại

- P1 tiêu đề tự thêm được ghi `(biên tập)`; dấu chấm số thứ tự bị thiếu trong p1–10 đã phục hồi theo bản in.
- P16:261 `Danh đá` → `Đanh đá`.
- P40:674 `あく` → `はあく`.
- P55:923 `致命的` → `致命的な`.
- P67:1120 `quỳnh lên` → `quýnh lên`.

Nhận định ban đầu của worker rằng nguồn thiếu な ở p55 hoặc in quỳnh/Danh là sai; các crop nguyên hàng xác nhận ký tự đúng. HANDOFF và evidence đã sửa lại, không giữ các khẳng định đó như sự thật của nguồn. Từng trang sửa được record/reverify; coordinator đọc lại bản cuối và các evidence cụ thể. Những sai sót này cho thấy lần tự kiểm đầu không bảo đảm mọi ký tự đã khớp.

Các cách ghi thật của nguồn được giữ: p4 `ÔI`, p9 `をひずく`, p20 `ÁM KÌ`, p22 `PHẢN ẢNH]`, p29 `をひきしめる` đi với `引きずる`, p38 `XUNG KÍCH]`, p40 `SÚC TÍCH]`/`SĨ QUẢI`, p51 `khoông`, p64 `をなだめる/募る` và `をはたる/謀る`. Coordinator đã đọc các hàng này, không tự chuẩn hóa theo từ điển.

Quan sát header/footer từ ảnh toàn trang đôi lúc khác crop riêng; không xác định nguyên nhân và không kết luận lỗi công cụ. Các vùng nguồn phải được quyết định bằng crop nguyên vùng. Ảnh ghép/crop chỉ là cache đọc, không thuộc output.

## Kiểm tra sản phẩm và giới hạn

Kiểm máy cho thấy đủ 1170 hàng theo thứ tự 1–1170, không thiếu/trùng. Search có 1170 block từng hàng, kèm tiêu đề cột và ngữ cảnh trang; đã đọc mẫu block đầu, giữa và cuối để kiểm nội dung/ngữ cảnh. Book và search được build từ các Markdown hiện tại; không có ảnh nhúng.

Nghiệm thu dựa trên worker đối chiếu toàn sách, coordinator lấy mẫu và kiểm mọi hàng được gắn cờ, cùng các sửa/rà rộng nêu trên. Không tuyên bố coordinator đã kiểm độc lập toàn bộ 70 trang hoặc bảo đảm tuyệt đối không còn lỗi chưa phát hiện. `acceptance.json` chỉ được lập sau trạng thái cuối hợp lệ, gắn hash nguồn, trang, build và sản phẩm.
