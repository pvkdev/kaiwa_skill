# Báo cáo V6.3

V6.3 kế thừa toàn bộ V6.2 và thêm phần B01, B08, B13, B14 và Mensetsu còn lại theo nhóm/Section nguyên vẹn, đặt tại chặng gần topic hoặc chức năng giao tiếp.

## Kiểm kê nguồn bổ sung

- B01 — 5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày: 70 bài/pack và phần bổ trợ, 4282/4282 dòng nội dung học.
- B08 — どんどん話せる！日本語会話フレーズ大特訓 必須700: 105 bài/pack và phần bổ trợ, 2092/2092 dòng nội dung học.
- B13 — シャドーイング 日本語を話そう！ 中～上級編 インドネシア語・タイ語・ベトナム語翻訳版: 41 bài/pack và phần bổ trợ, 3104/3104 dòng nội dung học.
- B14 — シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版: 61 bài/pack và phần bổ trợ, 2603/2603 dòng nội dung học.
- INTERVIEW — シャドーイング 日本語を話そう 就職・アルバイト・進学面接編 インドネシア語・タイ語・ベトナム語訳版: 20 bài/pack và phần bổ trợ, 1820/1820 dòng nội dung học.

Toàn bộ 14 nguồn mục tiêu có 1421 đơn vị kiểm kê và 31858 dòng nội dung học đã gán. Không còn phạm vi hở hoặc pack chưa có vị trí trong nguồn clean hiện có.

B14 giữ 42 Section trọn vẹn, đủ 411 hội thoại và nhãn CD02–43. B13 giữ 22 Section audio với 62 nhãn DISK; Mensetsu có13 nhóm chương audio với55 nhãn DISC riêng biệt. Nhãn lặp trên trang tiếp được ghi theo bản nguồn.

## Đầu ra và kiểm tra

Giữ 289 chặng, 33 cụm, 1.304 sự kiện, 5.914 tình huống theo V5. Có 1592 lượt Speak Japanese và 449 lượt nhóm shadowing/tài liệu bổ trợ, lưu 2041 bản Markdown cục bộ.

Các bản trích có manifest theo chặng, truy ngược mã/tên sách, chapter, dòng, hash và CD. Bài/pack lặp giữa cấp có thể tiếp tục sử dụng đầy đủ. Hai skill bài giảng và nội dung challenge vẫn là giai đoạn sau; các vị trí video là placeholder.

[Bao phủ từng sách](COVERAGE_REPORT.md) · [Kiểm kê bằng máy](COVERAGE_REPORT.json) · [Preview](ROADMAP.html)

## Giới hạn nguồn phải giữ trong dữ liệu

B01 không có số đĩa/track hoặc audiofile đã kiểm trong metadata; audio để rỗng. Bảy chương học của B01 có trạng thái needs_review vì chỗ scan bị cắt hoặc chữ Nhật bất thường. Các pack mang source_quality_note, cần đối chiếu/biên tập trước khi đưa bản luyện hoàn thiện vào app.

B08 thiếu đầu phần Introduction (trang in2). Mensetsu PDF bắt đầu từ trang in25, nên phần đầu bản sách gốc không có trong tài liệu được cung cấp. Hai chương Mensetsu có điểm nguồn chưa rõ (PDF32 và PDF106), được lưu nguyên kèm hash và source_quality_note. Các ô trống MyPage được giữ làm bài tập gốc, không bịa câu trả lời.

Giới hạn B18 thiếu bài14 và các nhãn audio chưa chắc ở V6.2 vẫn được giữ. Bao phủ100% ở báo cáo này có mẫu số là nội dung học có trong Markdown, không đồng nghĩa các trang vật lý thiếu đã được khôi phục. Chưa nghe đối chiếu các file âm thanh.

## Lịch sử

V6.2 commit022e41f6 đã hoàn tất trước khi bắt đầu V6.3. Cả hai phiên bản có báo cáo, dữ liệu và preview riêng.

## Kiểm tra phục hồi

Đã chạy lại bước merge toàn bộ catalog sau khi hoàn tất. Không thêm placement và hash của cả 289 decision không đổi. Có thể tiếp tục từ checkpoint mà không nhân bản bài hoặc ghi chú.
