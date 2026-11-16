# H-031 — Nguồn và tự rà biên tập

Đã tra BOOK_GUIDE.md, source_index.jsonl, manifest.json qua 27 sách theo 障害, 復旧, 原因, 報告, 連絡. Đọc sâu B03-C21 và sj-thuong-09 lesson/practice với ví dụ trỏ trực tiếp H-031. Cổng, khách, sự cố, thời gian, chi phí và quyền quyết hoàn toàn hư cấu; không đưa ra khẳng định về một dịch vụ thực tế. Mọi lời thoại sáng tác mới.

## Nguồn đã đọc

- **b03_report / B03 — しごとの日本語 ビジネスマナー編**, `kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/20-Unit18-報告・連絡・相談.md` dòng 23–39: báo tin xấu đúng trọng tâm, tách dữ kiện và báo thay đổi cho người liên quan.
- **Chuyên đề trước** `kaiwa_skill/planning/v10/stages/sj-thuong-09/lesson.md` và `practice.json`: đọc cách hỏi 調子, theo dõi có mốc, và tình huống mất khả năng tự xử lý; chỉ gắn ID nếu biểu thức thực dùng.

## Tự rà từng cảnh

### E01 — Phát hiện sự cố

- **S001 3fc41859-49a1-545a-b4f8-13787f9ca6c4** (routine; nối mở riêng): Chỉ một quan sát lúc 9:10, phạm vi và nguyên nhân chưa xác nhận.
- **S002 4040b224-f02b-5ead-a5fc-17aec7ce3cb0** (misunderstanding; nối S001): Sửa suy đoán nguyên nhân, không phủ nhận khả năng nhưng giữ trạng thái kiểm.
- **S003 397fd10e-6391-5dba-bff3-251a6f7c8759** (routine; nối mở riêng): Tách lịch đã nhận, thông báo chậm và hiểu biết của khách.
- **S004 dcfb2e13-e88e-5102-b7a0-db8b845ce31a** (routine; nối mở riêng): Dừng thao tác trong quyền nhóm, không tự tắt toàn cổng hay hệ thống tự động.

### E02 — Phân người xác minh

- **S005 f380e260-0d7b-58a3-86c7-050cb59857d2** (routine; nối mở riêng): Hai người kiểm hai mảng, 10:30 là mốc dữ kiện đầu, không ép kết luận.
- **S006 7ecf606f-812c-5348-a174-20ae8ea6b33e** (conditional; nối S005): Thiếu quyền thật, không tự vượt; số hai là mẫu quan sát, không phải toàn bộ.
- **S007 e3ca08a6-0875-5114-ba2a-24894592f84a** (routine; nối mở riêng): Mốc dữ kiện đầu là phạm vi, không phải nguyên nhân/khôi phục.
- **S008 8f989c60-b317-55c3-a568-2d44697d0e8b** (follow_up; nối S007): Nối mốc 10:30: năm là số tối thiểu đã thấy, không toàn bộ, chưa quy đổi cấu hình là nguyên nhân.

### E03 — Ưu tiên khôi phục

- **S009 43c0b802-cc19-5db5-9a72-96ad208b8466** (routine; nối mở riêng): Ưu tiên giảm ảnh hưởng, chỉ nói trạng thái lịch đã xác minh.
- **S010 8276e166-ec49-57ef-9b2e-e6c92cc61bf0** (alternative; nối S009): Tạm thời chỉ năm lịch đã kiểm; không đánh đồng ứng phó với sửa gốc.
- **S011 eb6f8d41-aae0-5ef1-9d4e-595f7791b34a** (declined; nối S010): Nối tạm thời: rủi ro trùng thật làm đổi phương án, không giữ cách cũ vì đã nói.
- **S012 d3e894c1-0c2b-53c5-9aed-89275911cb57** (routine; nối mở riêng): Theo dõi hai phía, quyền dừng cấu hình chưa được giả định.

### E04 — Báo cho cấp trên/khách

- **S013 8805e1b4-ab10-5e45-9ac8-4a2a128ef05f** (routine; nối mở riêng): Báo tin xấu/số tối thiểu, nguyên nhân chưa rõ, mốc 11:30.
- **S014 2acc62c2-ac93-51bf-b63c-92e96727ded2** (misunderstanding; nối S013): Sửa tương quan thành nguyên nhân, không tự hoàn nguyên khi chưa kiểm.
- **S015 e182930f-6227-5cfa-b7c1-0e63785c2aed** (pending; nối S013): Nối báo lần đầu: không bịa giờ khôi phục, có mốc cập nhật và đầu mối khách.
- **S016 ffd317ce-be8d-5c7a-8a56-21396ac647f9** (follow_up; nối S015): Nối S015: mốc 13:00 là thử, 14:00 là báo kết quả, không hứa khôi phục.

### E05 — Vượt quyền quyết

- **S017 8f12d445-4090-5350-bcc0-e429338c88b1** (routine; nối mở riêng): Hai phương án đều chờ duyệt, tiền và gián đoạn giả định có phạm vi rõ.
- **S018 c2074d53-d3bb-5513-ac3e-35fddca17f58** (conditional; nối S017): Duyệt một phần rõ trần 5万円/30 phút/notification only, không tự duyệt full shutdown.
- **S019 f0998f92-cbd2-56c0-8d02-72ad93f59096** (declined; nối S017): Nhánh từ chối: không lén dừng, vẫn có cách phục vụ và điều kiện báo lại.
- **S020 b49fd548-c9d6-5411-a637-094bb7a0f66c** (follow_up; nối S018): Nối S018: đội nhận nguyên giới hạn, không mở rộng chi/gián đoạn.

### E06 — Khôi phục và bàn sau

- **S021 84608bc6-ae7c-5416-9d5d-0a86d93b4939** (routine; nối mở riêng): Chỉ ba lịch thử mới thành công; phần cũ và trùng chưa rõ, có người/mốc theo dõi.
- **S022 94419eaa-64d1-52f0-b306-b1042186282c** (misunderstanding; nối S021): Sửa ba lịch thử thành một phần chức năng, chưa tuyên bố toàn hệ thống.
- **S023 86205a0c-8b73-5f6e-af45-ff0c33d13260** (routine; nối mở riêng): Người báo khách là Fujita, thông tin chưa thành toàn bộ khôi phục.
- **S024 92d0ddca-fa73-5ddd-837b-dfdd4da8610e** (follow_up; nối S023): Nối S023: cập nhật khách không chờ họp nhìn lại; lịch họp mới là đề xuất.
