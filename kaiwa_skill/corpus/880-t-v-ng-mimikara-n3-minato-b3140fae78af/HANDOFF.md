# Bàn giao đang xử lý — production_book_02

- Sách: `880-t-v-ng-mimikara-n3-minato-b3140fae78af`; nguồn `vocab/880 TỪ VỰNG MIMIKARA N3 MINATO.pdf`; 47 trang vật lý, nguồn chỉ đọc.
- Claim CLI: owner `production_book_02`, token `production_book_02_20261110_6f8c`.
- Đã render p1–47 scale 2.2 (~158 DPI) tại `.cache/renders/<book_id>/`. Nguồn scan không có text layer.
- Đã thực sự mở ảnh toàn trang p1–9 và đối chiếu bảng; verified p1–9 (mục 1–168). Có crop lớn p3 mục 43, p5 mục 78, p6 các mục 93/94/108.
- Header quote và footer Fanpage hiện diện trên CẢ 47 trang: vùng pixel header y220–355 có hash giống hệt trên mọi trang, OCR vùng riêng đọc quote; OCR vùng footer y1600–1710 đọc Fanpage trên mọi trang. Một số lần `view_image` không hiển thị vùng chữ lặp khi mở ảnh toàn trang/crop; dùng crop đảo màu hoặc xoay để nhìn trực tiếp, và kiểm pixel/OCR để không bỏ chữ. Không khẳng định nguyên nhân hiển thị.
- Mọi trang đã ghi có nhãn `Đầu bảng (biên tập):`/`Cuối bảng (biên tập):`, vì các nhãn này không in trong nguồn. Đã re-record/reverify p1–9 sau sửa nhãn; p2/p3 còn được reverify sau bổ sung quote/Fanpage thiếu ban đầu.
- Mục 89 (p5) và 125 (p7) có hai ô Kanji/Âm Hán Việt trống đúng nguồn; không điền. Mục 78 Kanji là `黴`, so với glyph mẫu để xác nhận.
- Draft OCR theo từng cột lưu `.cache/ocr/<book_id>/pNNNN.json` và script `draft.py`; OCR chỉ là bản nháp. `draft.py` mới có FIRST/LAST và sửa tay cho p1–9. Phải mở và đối chiếu từng trang p10–47; không tự xác nhận OCR/số thứ tự.
- Tiếp tục từ p10. Chưa build/release vì chưa hoàn tất. Chỉ ghi corpus sách và scratch/cache sách; không sửa tools/skill/git.

## Cập nhật p10–14

- Đã mở ảnh, đối chiếu và verified p10–14 (mục 169–264). Tổng hiện 14/47.
- p10 mục 172,185,186; p11 mục 187–189,200–201 có hai ô Kanji/Hán Việt trống theo nguồn.
- Crop p13 mục 232 xác nhận âm Hán Việt `TAO`; p14 mục 261 `KHỔ THỦ`, mục 264 `THỐI KHUẤT`.
- `draft.py` đã có range/sửa tay đến p14. Tiếp tục p15.

## Cập nhật p15–19

- Đã mở ảnh, đối chiếu và verified p15–19 (mục 265–357). Tổng hiện 19/47.
- Nhiều ô Kanji/Hán Việt trống đúng nguồn (p15 mục 269–271/274–275, p16 mục 292/295–296, p17 mục 317/319, p18 mục 320/335).
- Sửa Kanji OCR p19 翻訳/混雑/渋滞/被害; range và sửa tay trong `draft.py` đến p19. Tiếp tục p20.

## Cập nhật p20–24

- Đã mở ảnh, đối chiếu và verified p20–24 (mục 358–452). Tổng hiện 24/47.
- Crop p22 mục 413 xác nhận `掻く`. p24 mục 437/438 có hai dạng Kanji trong cùng ô, đã giữ `替わる・換わる` và `替える・換える`.
- Theo audit coordinator, sửa p19 mục 347 thành `HỖN TẠP` (ngã), re-record/reverify p19; đã mở crop phóng to và rà dấu toàn cột Hán Việt p15–19, không thấy lỗi khác.
- `draft.py` đã có range/sửa tay đến p24. Tiếp tục p25.

## Rà dấu tiếng Việt p1–24

- Đã mở crop phóng to riêng hai cột Âm Hán Việt và Nghĩa trên toàn bộ p1–24, đối chiếu từng dòng với Markdown đã ghi. Rà cả ô trống, dấu trên chữ hoa và dấu trong nghĩa. Các crop lưu `.cache/ocr/<book_id>/audit_pNNNN.png`.
- Theo audit coordinator, p24 mục 450 source `ẨN` (dấu hỏi); đã sửa, record và verify lại. Phát hiện thêm p4 mục 63 source `VIỄN LỰ` (dấu ngã); đã sửa, record và verify lại.
- Ngoài p4:63, p19:347 và p24:450, lượt rà này chưa phát hiện sai dấu Việt khác. P1–24 hiện verified; từ p25 trở đi mở crop phóng to hai cột tiếng Việt trước verify.

## Cập nhật p25–29

- Đã mở toàn trang và crop phóng to hai cột tiếng Việt p25–29, đối chiếu mọi hàng; record/verify từng trang, tổng 29/47 (mục 1–546).
- Sửa dấu theo ảnh: p25 mục 463 `KIẾN`, p26 mục 477 `KIẾN`; cả hai từng bị OCR thành `KIÊN`.
- P28–29 chuyển sang các từ Katakana, ô Kanji/Hán Việt trống đúng nguồn. `draft.py` có range/sửa tay đến p29. Tiếp tục p30.

## Cập nhật p30–34

- Đã mở ảnh toàn trang và crop phóng to hai cột tiếng Việt p30–34; đối chiếu Kanji/kana và toàn bảng; record/verify từng trang. Tổng 34/47 (mục 1–639).
- Sửa OCR ở các mục khó: p30 mục 550/559/562/565; p31 mục 566/571–573/579–580; p32 mục 585–587/594; p33 mục 605/609/614/619; p34 mục 620–621/629/631/637/639. Chi tiết trong `draft.py` và evidence từng trang.
- p32 mục 587 Hán Việt nguồn in `CƠ BỔN ĐÍCH`, giữ nguyên chữ in. Tiếp tục p35.

## Cập nhật p35–39

- Sau audit coordinator, p34 mục 635 sửa Hán Việt `THỰC` (Ư có móc, nặng), đã record/reverify p34.
- Đã mở toàn trang và crop phóng to hai cột Việt p35–39; đối chiếu Kanji/kana và từng hàng, record/verify từng trang. Tổng 39/47 (mục 1–734).
- Giữ các cách ghi nguồn khác lạ như p35 `CHỨNG TRẠNG`, p36 `CƠ BỔN`, p37 `THIÊU CHIẾN`/`BIẾN CANH`, p38 `HUỀ ĐỚI`/`HẾ KỈ`. Các sửa OCR khác ghi ở `draft.py` và evidence từng trang. Tiếp tục p40.

## Cập nhật p40–44 và QA p2–8

- Đã mở ảnh toàn trang và crop phóng to hai cột tiếng Việt p40–44, đối chiếu hàng bảng/Japanese, record và verify từng trang. Tổng 44/47 (mục 1–826). p42 mục 773–774 đã crop Kanji xác nhận `纏まる`/`纏める`.
- Theo audit coordinator, mở crop độc lập và sửa/reverify p2 mục 21 `TIẾN HỌC`, 22 `THỐI HỌC`, 24 `THỐI CHỨC`; p5 mục 75 `THẤP ĐỘ`, 76 `THẤP KHÍ`; p7 mục 124 `ẨU`; p8 mục 131 `TẦM`, 133 `KHIẾU`, 136 `SỔ`, 137–138 `KIỀN`.
- Các dấu hỏi/sắc/huyền trong bản in rất nhỏ; coordinator đang rà độc lập toàn hai cột tiếng Việt p1–47. Chờ QA cuối sau khi hoàn tất p45–47, không gọi accepted.

## Cập nhật p45–47 và sửa theo QA độc lập

- Đã mở toàn trang p45–47, crop phóng to hai cột tiếng Việt và kiểm các hàng mục 827–880; record/verify từng trang. Tổng hiện 47/47, mục 1–880. Riêng p46 mục 861/863 mở crop sát xác nhận `THIỂU`; quote/Fanpage p46–47 mở crop riêng.
- Sau QA của coordinator, mở crop nguồn, sửa và reverify: p10 mục 177 `VU`; p12 mục 226 nghĩa bắt đầu chữ thường `suy nghĩ`; p13 mục 228 `PHIẾN`, 242 `CẤP`; p14 mục 255 `TIẾU`, nghĩa `cười`; p15 mục 268 `HỐI`, mục 273 thêm phần nghĩa từng thiếu `thẳng thắn,`; p18 mục 325 `TIẾN BỘ`; p21 mục 378 `TUYỂN CỬ`; p22 mục 413 `TAO`. Các lỗi ban đầu đã được sửa sau đối chiếu, không khẳng định bản chép đầu đúng hoàn toàn.
- Dải xanh intact p11–12 và p45–47 xác nhận `MINATO DORIMU` bốn lần; nghi ngờ `DOORIMU` do crop ghép cột tạo đường nối giả, không sửa bản chép. Chờ coordinator hoàn tất QA độc lập p28–47 trước kết luận nghiệm thu.

## QA độc lập toàn bộ cột Việt và mẫu tiếng Nhật

- Coordinator đã rà độc lập cả hai cột Việt trên đủ 47 trang. Các sửa cuối đã mở crop, record và reverify theo từng trang: p30:561 `THIỂN`; p35:650 `HẬU HỐI`/`hối hận`; p39:718–719 `TIẾN`, 734 `KHUYẾN`; p40:735 `TIẾN`; p41:764 nghĩa kết thúc `..`, 771–772 `TIỄN`; p42:779–781 `GIAO HỖN`; p43:795 `Giơ(tay)`; p47:877 kana `また` không có dakuten.
- Tất cả 47 trang hiện đã verified lại sau sửa; cần `build` lại vì các trang thay đổi sau build trước. Giữ claim `production_book_02` chờ coordinator kiểm nghiệm thu/mẫu tiếng Nhật cuối. Không gọi accepted.

## Bàn giao cuối sách

- Đã build lại sau tất cả các sửa: 47/47 trang verified, mục 1–880 đủ và không trùng, `build_current=True`; có `book.md`, `search.jsonl`, `build.json`.
- Coordinator đã đọc độc lập đủ hai cột tiếng Việt của 47 trang và kiểm mẫu tiếng Nhật/trình bày; đã đọc lại các hàng từng sửa và xác nhận khớp quan sát nguồn. Phạm vi QA này không phải soát độc lập toàn bộ cột tiếng Nhật.
- Claim được release sau xác nhận recheck của coordinator. Acceptance và commit do coordinator xử lý riêng; worker không gọi accepted và không dùng git.
