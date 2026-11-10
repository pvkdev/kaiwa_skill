# Ghi chú kiểm tra đang diễn ra

Đây là ghi chú coordinator, không phải nghiệm thu sách. Quyết định cuối có báo cáo và acceptance gắn hash riêng trong corpus.

## 880-t-v-ng-mimikara-n3-minato-b3140fae78af

Coordinator đã mở nguồn p1, p4, p9, p19 và p24, đọc đối chiếu Markdown bảng đầy đủ. Nhãn tự thêm `Đầu bảng:` và `Cuối bảng:` thiếu `(biên tập)` đã được worker sửa p1–p9, record/verify lại; bản mới p9 và evidence p1 đã đọc lại, nhãn hiện đúng. P19 mục347 có lỗi dấu Việt: nguồn `HỖN TẠP`, bản ghi đầu `HỒN TẠP`. Coordinator mở crop riêng xác nhận, worker đã sửa/record/reverify p19 và rà cột Hán Việt p15–19 bằng crop phóng to. P24 mục450 có thêm lỗi `ẤN` thay vì `ẨN`; crop riêng xác nhận cả450/451 đều dấu hỏi. Đã giao sửa p24 và mở rộng rà hai cột Việt toàn p1–24, thêm lượt zoom dấu khi làm trang mới. P25–29 lúc nhận yêu cầu mới chỉ ở scratch draft. Cần đọc kết quả rà/bản cuối trước nghiệm thu.

Worker báo ảnh toàn trang/crop có những quan sát thiếu vùng lặp; sau đối chứng, quote header và Fanpage footer thực có trên mọi trang. Worker đang kiểm và sửa các trang đầu bị bỏ thiếu. Không suy ra nguyên nhân hiển thị. Coordinator cần đọc lại output sau sửa, kiểm mẫu thêm các bố cục/nhóm từ/đầu-cuối bảng, và kiểm tất cả trang có issue trước nghiệm thu47tr.

Rà mở rộng p1–24 đã xong theo báo cáo worker: thêm lỗi p4:63 `VIÊN LỰ` → `VIỄN LỰ`, đã record/reverify. Coordinator mở crop độc lập p4:63 và xác nhận dấu ngã; lượt xem toàn trang ban đầu của coordinator đã bỏ sót. P25–29 được zoom hai cột Việt trước verify; worker sửa KIẾN ở p25:463 và p26:477. Coordinator đã đọc toàn bảng p29 (Katakana, cột Kanji/Hán Việt trống, nhiều từ xuống dòng), chưa thấy sai khác.

## 1170-t-v-ng-mimikara-n1-e1d2f2dffd69

Đã giao toàn70tr cho worker03, chưa nghiệm thu. Coordinator đã mở và so toàn bảng p1, p4, p8, p9. P1 tiêu đề tự thêm `Bảng từ vựng` thiếu `(biên tập)` và STT p1–10 thiếu dấu chấm nguồn đã giao sửa/reverify, worker báo đã áp dụng. Cần kiểm lại bản cuối. P4 mục58 `ÔI` đúng nguồn, đã mở thêm crop300DPI để xác nhận; p8 mục123 in `を／がわめく`, p9 mục135 in `をひずく` và đều được giữ đúng. Ô trống, watermark, quote/footer phải giữ theo nguồn. Chưa thấy lỗi từ khác trong các mẫu này.

Coordinator đã mở và đọc toàn bảng p13/p14, chưa thấy sai khác. p13:211 `PHẠP` đúng bản in; p14:226/228 xuống dòng trong cùng ô được nối đúng. Worker báo đã rà crop hai cột Việt p1–14 và áp dụng từ đó trở đi. Các ghi chú cần kiểm thêm khi nghiệm thu: p15:242 hai dạng 温和な・穏和な; p16:261 “Danh đá”; p17:273 “k rõ ràng”; p20:320 “ÁM KÌ”; p22:360 có dấu ] sau PHẢN ẢNH; p22:368–370 ba Kanji cho ついきゅう; p25:408 がいきつける. Đây là đặc điểm nguồn worker báo, chưa phải coordinator xác nhận.

## Đóng QA N3

Các ghi chú N3 phía trên là lịch sử giữa đợt. Kết quả cuối: ACCEPTED, commit `ea221b1`. Coordinator mở rộng đọc cả hai cột Việt trên 47/47 trang, kiểm lại mọi sửa; tiếng Nhật/bố cục mẫu 1,4,9,19,24,29,34,40,42,47. Sổ `corpus/880-t-v-ng-mimikara-n3-minato-b3140fae78af/COORDINATOR_VIET_AUDIT.json` và REVIEW.md ghi đầy đủ các lỗi dấu, cụm nghĩa thiếu đã phục hồi, p47 `まだ`→`また`, cùng nhận định DOORIMU sai do đường nối crop ghép. Full source band giữ DORIMU. Hash-bound acceptance và build cuối hợp lệ, claim đã release. N1 vẫn cần QA cuối.
