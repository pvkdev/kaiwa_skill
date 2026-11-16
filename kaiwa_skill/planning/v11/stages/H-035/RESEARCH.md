# H-035 — Nguồn và tự rà biên tập

Tra BOOK_GUIDE.md, source_index.jsonl và manifest.json của catalog27 theo クレーム, 上司, 印刷, 工場, 報告. Đọc sâu B15-C07 và B03-C21, cùng sj-thuong-10 lesson/practice. Mọi doanh nghiệp, số liệu, nhà máy, công suất và lịch là giả định; các lượt thoại viết mới. Phân biệt dấu hiệu hàng sai, nguyên nhân công đoạn, người chịu trách nhiệm, quyền duyệt và chấp nhận của khách.

## Nguồn đã đọc

- **b15_internal / B15** `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/06-bai-06.md` dòng 1–42: báo khiếu nại in sai lên sếp và chia việc đi gặp khách/kiểm nhà máy. Không dùng lời hứa nhà máy khác chắc kịp trong ví dụ sách cho tình huống giả định.
- **b03_report / B03** `kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md` dòng 27–32: báo cụ thể, kết luận và tin xấu trước.

## Chuyên đề trước

Đã đọc `kaiwa_skill/planning/v10/stages/sj-thuong-10/lesson.md` và `practice.json`; không gắn specialty ID vì không dùng trực tiếp các mẫu đó. Mọi lượt là original_extension.

## Tự rà từng cảnh

### E01 — Nhân viên báo sếp

- **S001 ab9104b9-ddaf-531a-87b0-8cdf4b1fe7db** (routine; sau mở riêng): Báo 200 quan sát/400 chưa kiểm, hạn 100 chiếc, ảnh và hàng thật tách rõ. Nguồn: b15_internal, b03_report.
- **S002 5b1e0dd4-f769-567d-8573-cbe7c8b18c1f** (misunderstanding; sau S001): Sửa nhầm nguyên nhân đã rõ thành quan sát ảnh; tránh quy lỗi nhà máy. Nguồn: b15_internal.
- **S003 b16e730a-4133-5ffc-88fa-06867c6d9084** (routine; sau mở riêng): Cam kết chỉ về giờ kiểm/báo, không ngầm hứa làm lại, phí hoặc ngày giao. Nguồn: b15_internal.
- **S004 6c907ec2-6b47-5158-b73b-b7e3fdb4a1e7** (routine; sau mở riêng): Chia QA/chỗ sản xuất/khách, giữ phạm vi liên lạc và quyết phí. Nguồn: b15_internal.

### E02 — Phân công kiểm nguyên nhân

- **S005 faa63a76-f4cb-530a-8053-a8fa53734c88** (routine; sau mở riêng): Điều tra bằng phiên bản 3, mã thùng, không gộp 400 chưa xem. Nguồn: b15_internal.
- **S006 1cfd2aa7-1bd2-517a-b747-c5275698e787** (pending; sau S005): QA báo tiến độ chứng cứ, không hứa chắc kết luận nguyên nhân. Nguồn: b15_internal.
- **S007 6c74ef52-6528-5380-899a-4abab7d738e9** (problem; sau S005): Mã trùng mở rộng điều tra chứ chưa mở rộng kết luận lỗi. Nguồn: b15_internal.
- **S008 01858dbd-828e-5051-a449-70b0a44d3c20** (follow_up; sau S006): Nối mốc 17 giờ: 200 sai, 100 khớp, 300 chưa xem; quy trình rõ hơn trách nhiệm người. Nguồn: b15_internal.

### E03 — Làm việc với khách tại chỗ

- **S009 2c907c3d-b25f-50ad-99c2-6d5450861bfa** (routine; sau mở riêng): Xem thực vật với khách, không thu toàn lô khi chưa xác định phạm vi/được đồng ý. Nguồn: b15_internal.
- **S010 fde7d238-4829-568c-b86f-d699d31f926a** (misunderstanding; sau S009): Sửa hiểu nhầm mục đích chuyến thăm; phạm vi thu hồi cần thỏa thuận. Nguồn: b15_internal.
- **S011 6f95c445-b95d-5a53-8850-cce74584ed02** (routine; sau mở riêng): Ưu tiên 100 logo mới; năng lực và giao chưa chắc, mốc 18 giờ. Nguồn: b15_internal.
- **S012 6ecf4d13-7123-55fe-a5b4-3d05b1b44091** (conditional; sau S011): Đồng ý có điều kiện cho 100, chưa chốt xuất/giao hay toàn 600. Nguồn: b15_internal.

### E04 — Chọn cách xử lý

- **S013 f5c2a905-ff33-5054-93c5-1640f8f2d87f** (routine; sau mở riêng): Hai lựa chọn có điều kiện khác nhau; không đồng nhất dự kiến và lịch chắc. Nguồn: b15_internal.
- **S014 b1f8fc8d-29f4-5820-a4ff-eadf5bf6f9ac** (conditional; sau S013): Lựa chọn nhà máy khác chưa final vì logistics/fee chưa duyệt. Nguồn: b15_internal.
- **S015 9794e3b6-d469-5960-88b9-29f8801caa36** (declined; sau S013): Từ chối mục tiêu 600 thứ Sáu, quay về 100 cần trước và hỏi khách. Nguồn: b15_internal.
- **S016 382ff888-86cf-501f-906a-18f8775b1b3a** (routine; sau mở riêng): Không sáng tác thẩm quyền phí: đường duyệt nội bộ phải được xác nhận. Nguồn: b15_internal.

### E05 — Báo khách kết quả kiểm

- **S017 2a0da528-2af9-56ec-bb7b-38e284c9e539** (routine; sau mở riêng): Nguyên nhân dùng bản 2 ở 200 có ghi nhận; 100 khớp, 300 chờ; không quy cá nhân. Nguồn: b15_internal.
- **S018 39fb5cfb-2b55-5478-b641-d68b5d8b5549** (pending; sau S017): Giữ 300 ở trạng thái tạm riêng, không kết luận cùng lỗi hay an toàn. Nguồn: b15_internal.
- **S019 e123f581-b38c-57e4-af2b-9f70c57113c2** (routine; sau mở riêng): Lịch có hai điều kiện, chi phí chưa nằm trong thỏa thuận. Nguồn: b15_internal.
- **S020 21d55f68-2ba4-51ec-8267-92ad729cc67d** (declined; sau S019): Khách từ chối lịch tạm, đưa lên người quyết hai bên, không ngầm chốt cuộc họp/chuyến giao. Nguồn: b15_internal.

### E06 — Hàng sửa và sau giao

- **S021 d1f4aae3-3d05-509d-8820-ce63733e0e5c** (routine; sau mở riêng): 20 chiếc được khách kiểm khớp, 80 chưa; nghiệm thu toàn lô chưa chốt. Nguồn: b15_internal.
- **S022 de602609-38ba-56ae-8bdf-3c489d7aaf77** (problem; sau S021): Lỗi mới ở 10 chiếc, không suy 90 chiếc còn lại; báo QA đúng phạm vi. Nguồn: b15_internal.
- **S023 7fe92a60-2832-5ae5-b692-559222bf2a11** (resolved; sau S022): Lỗi đường gấp sửa ở mười chiếc, khách chỉ chấp nhận mười; 90 vẫn chờ. Nguồn: b15_internal.
- **S024 b258d5c8-6810-564d-a5a9-eb5c89680342** (follow_up; sau S023): Follow-up thực tế: 100 được nhận và dùng, 500 còn chờ ngày; không tuyên bố toàn đơn xong. Nguồn: b15_internal.

### E07 — Học từ sự cố

- **S025 f2d39e21-c240-5bbb-9684-d38ee74dc934** (routine; sau mở riêng): Định vị hai lỗ hổng quy trình có bằng chứng, không quy lỗi người. Nguồn: b15_internal.
- **S026 a1d15960-9d3e-5991-9799-c3989bc908dd** (misunderstanding; sau S025): Sửa quy lỗi một người khi chưa có bằng chứng; bước kiểm được thử ở lô sau. Nguồn: b15_internal.
- **S027 e9490c9e-5e45-558c-8641-d54479422e93** (routine; sau mở riêng): Thử hai điểm kiểm ở lô nhỏ, đo tải và phát hiện; chưa áp toàn bộ. Nguồn: b15_internal.
- **S028 e6194167-ec6c-5207-bf9d-30d51b3bb178** (follow_up; sau S027): Follow-up thử thật ở một lô, phát hiện bản cũ trước in; chưa vội kết luận toàn hệ thống. Nguồn: b15_internal.
