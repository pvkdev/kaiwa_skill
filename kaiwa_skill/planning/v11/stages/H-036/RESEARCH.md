# H-036 — Nguồn và tự rà biên tập

Tra BOOK_GUIDE.md, source_index.jsonl và manifest.json của catalog27 theo 報告, 相談, 上司, 問題, 顧客. Đọc sâu B03-C21 và B15-C07, cùng sj-thuong-10 lesson/practice. Dự án, lịch đặt, chênh giờ, khách, số liệu và quy trình là hư cấu. Tất cả lượt thoại sáng tác mới; trạng thái rủi ro, xác minh, duyệt gửi và khách chấp nhận được tách riêng.

## Nguồn đã đọc

- **b03_report / B03** `kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md` dòng 27–32: báo cụ thể, nêu kết luận và tin xấu trước.
- **b03_consult / B03** `kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md` dòng 62–67: chuẩn bị phương án khi xin cấp trên quyết.
- **b15_handoff / B15** `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/06-bai-06.md` dòng 18–42: báo sự cố khách và phân công điều tra/ứng phó.

## Chuyên đề trước

Đã đọc `kaiwa_skill/planning/v10/stages/sj-thuong-10/lesson.md` và `practice.json`; không dùng nguyên mẫu ở specialty nên không gắn ID.

## Tự rà từng cảnh

### E01 — Phát hiện vấn đề

- **S001 c154e342-2231-5980-bda1-6603098b726c** (routine; sau mở riêng): 88/100 đã kiểm, 12 rủi ro, hạn thứ Sáu chưa trễ; nguyên nhân còn giả thuyết. Nguồn: b03_report, b15_handoff.
- **S002 6fdb3ce0-9fb9-57be-be00-d7c09361525e** (misunderstanding; sau S001): Sửa nguy cơ thành chưa chắc trễ; thông báo khách đúng trạng thái. Nguồn: b03_report.
- **S003 1e23fa7f-b310-580b-91d1-50ca26d89553** (routine; sau mở riêng): Hỏi nhu cầu báo khách dựa trên thời điểm sử dụng; chờ tối đa một giờ có mốc. Nguồn: b03_report.
- **S004 7ed6ad71-76a4-56b3-a370-24ad42b67b7c** (pending; sau S003): Một giờ là mốc kiểm ngày dùng, không chờ chắc nguyên nhân rồi mới báo. Nguồn: b03_report.

### E02 — Đề xuất khắc phục

- **S005 b3a2defe-3e5b-5987-b24c-c3e99f064391** (routine; sau mở riêng): Hai cách kèm tradeoff; ba lịch thứ Bảy đã kiểm; A còn chờ người và quy trình an toàn. Nguồn: b03_consult.
- **S006 2ed73423-dadd-5988-94fc-545ccc6377d6** (conditional; sau S005): Chọn có điều kiện, không biến người chưa xác nhận thành triển khai. Nguồn: b03_report.
- **S007 e6b9c63b-fd8f-52ed-8809-1b0beca1797c** (declined; sau S005): Bác quy trình không an toàn; ưu tiên ba lịch thứ Bảy và phương án thay. Nguồn: b03_consult.
- **S008 be2348f1-15a6-507b-ad54-18e60081abbf** (follow_up; sau S006): Điều kiện người và read-only đạt, được bắt đầu; vẫn chưa đảm bảo xong 100. Nguồn: b03_consult.

### E03 — Giải thích nguyên nhân chưa chắc

- **S009 07bb4ca2-1d65-5738-a3ec-e126aba5cf0e** (routine; sau mở riêng): Dấu hiệu chênh một giờ chỉ là giả thuyết, không kết luận mất/không mất khi chưa đối chiếu. Nguồn: b03_report.
- **S010 a932cfce-8092-593b-a28a-93d71f644f3c** (misunderstanding; sau S009): Không quy đồng nghiệp qua tên trong log; có phép kiểm trước/sau và hỏi bối cảnh. Nguồn: b03_report.
- **S011 aaf1b7ae-c087-5163-8ea2-889801296ac5** (routine; sau mở riêng): Owner dữ liệu/log và mốc kiểm rõ; không điền dữ kiện thiếu. Nguồn: b03_report.
- **S012 b0e26eb7-ad6b-54fd-bc8a-6554ebd389b2** (follow_up; sau S011): Nguyên nhân đã có log, bác suy đoán về Yui; 12 giờ sai nhưng chưa gửi khách. Nguồn: b03_report.

### E04 — Nói với khách/người bị ảnh hưởng

- **S013 db8e0413-6ab1-566a-bd0a-57218d4c4234** (routine; sau mở riêng): Khách biết 12 cần kiểm, 3 lịch thứ Bảy, chưa gửi bảng sai; yêu cầu tránh dùng giờ cũ. Nguồn: b03_report.
- **S014 5c07bbe2-a8cc-54fb-b2da-3b496a871e73** (pending; sau S013): Không hứa chắc giờ khôi phục, mốc 17 giờ cập nhật và thứ Sáu 17 còn mục tiêu. Nguồn: b03_report.
- **S015 3ce45e02-762e-57cf-b764-46e5127155f1** (conditional; sau S013): Ưu tiên 3 nhưng khả năng kiểm chưa được duyệt, không khẳng định kết quả 17 giờ. Nguồn: b03_report.
- **S016 af79f7a6-98d8-5e94-a89d-682fd4e92b14** (follow_up; sau S015): Chỉ 3 đã xác nhận, 9 còn kiểm; không biến ưu tiên thành toàn bộ đã xong. Nguồn: b03_report.

### E05 — Sau khi xử lý

- **S017 87657919-1d4b-5f29-90d5-aa5bf4460318** (routine; sau mở riêng): 100 bản sửa khớp nhưng gửi/nhận và lần xuất sau còn mở. Nguồn: b03_report.
- **S018 3b05d5bb-9c89-58bb-ae34-06974a058164** (problem; sau S017): Giải pháp tạm phát sinh rủi ro gửi nhầm; đề nghị lưu bản cũ có lịch sử, không xóa. Nguồn: b03_report.
- **S019 e181591d-7bcb-5dfb-9e77-646c6cf92e19** (resolved; sau S018): Quyết quản lý bản có owner/approval; gửi khách vẫn chờ duyệt. Nguồn: b03_report.
- **S020 307b5f5b-a526-5b54-9fe4-2106eeb4d6ff** (follow_up; sau S019): Cuối mốc: đã gửi/nhận, 20 lần sau khớp; khách chưa chấp nhận nội dung, theo dõi vẫn hữu hạn. Nguồn: b03_report.
