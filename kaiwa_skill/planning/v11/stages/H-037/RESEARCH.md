# H-037 — Nguồn và tự rà biên tập

Tra BOOK_GUIDE.md, source_index.jsonl và manifest.json của catalog27 theo 接客, ホテル, おもてなし, 静か, 客室. Đọc sâu B03-C15 và B27-C04, cùng sj-thuong-10 lesson/practice. Khách sạn Kaze, quy trình, phòng, suất ăn, giờ và điều kiện đổi đều hư cấu; không nêu quyền khách hàng hay chính sách chung. Mọi lượt thoại viết mới.

## Nguồn đã đọc

- **b03_welcome / B03** `kaiwa_skill/knowledge/しごとの日本語 ビジネスマナー編/chapters/14-Unit12-接客・訪問.md` dòng 23–35: chuẩn bị đón, gọi tên phù hợp và dẫn khách theo nhịp họ.
- **b27_hotel / B27** `kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/03-bai-02-hoteru-de.md` dòng 23–79: bối cảnh hỏi phòng/tiện nghi và phân biệt thông tin chắc với chưa chắc.

## Chuyên đề trước

Đã đọc `kaiwa_skill/planning/v10/stages/sj-thuong-10/lesson.md` và `practice.json`; không gắn specialty ID vì không dùng trực tiếp các mẫu đó.

## Tự rà từng cảnh

### E01 — Đón khách quen hoặc khách đặc biệt

- **S001 e996afd3-2180-50a4-b63b-73e6d7ad24cb** (routine; sau mở riêng): Khách cũ nhưng nhu cầu mới; đón kín đáo, không tự mang hồ sơ cũ ra. Nguồn: b03_welcome.
- **S002 da7d28cd-3407-5e2a-9e82-77c33f339e19** (misunderstanding; sau S001): Sửa lỗi tiết lộ sở thích cũ trước người đi cùng; khách chủ động gọi nhu cầu mới. Nguồn: b03_welcome.
- **S003 72ab7cf5-3291-5ab0-8614-cbfda017bff7** (routine; sau mở riêng): Hỏi loại riêng tư thực cần, không suy khách muốn phòng VIP hoặc tiết lộ nội dung cuộc gọi. Nguồn: b03_welcome.
- **S004 e0153f56-51f3-5cc9-a801-f13e98553c66** (conditional; sau S003): Khu riêng hết chỗ, mô tả rõ chỗ có vách nhưng không cách âm; lựa chọn chưa bị áp đặt. Nguồn: b27_hotel.

### E02 — Yêu cầu không nói thẳng

- **S005 e82a1774-3da9-5922-90a5-682f330a2e22** (routine; sau mở riêng): Làm rõ nguồn tiếng nói và giờ, không tự suy phòng hỏng hoặc khách đòi đổi phòng. Nguồn: b03_welcome.
- **S006 30957d2a-da8b-5373-adc8-9f8162e93c83** (misunderstanding; sau S005): Sửa hiểu nhầm đổi phòng, tôn trọng chi phí di chuyển của khách. Nguồn: b03_welcome.
- **S007 c309e226-0407-5ae7-8fd4-54ea7f938181** (routine; sau mở riêng): Khách đồng ý thử trước, nguồn tiếng chưa chốt; mốc 20 phút kiểm hiệu quả. Nguồn: b03_welcome.
- **S008 a6ebca2e-54a6-5ad0-a2b4-ae6968641f97** (follow_up; sau S007): Follow-up phản hồi hỗn hợp: lời nói giảm nhưng xe đẩy còn; xác định mức đủ cho khách. Nguồn: b03_welcome.

### E03 — Đòi hỏi vượt quy trình

- **S009 7a3fe232-7dd0-513a-9424-2b7e81715d8f** (routine; sau mở riêng): Không hứa chen lượt; hỏi hạn thực và nhu cầu món nóng trước khi đề xuất. Nguồn: b03_welcome.
- **S010 b5b01567-dac5-50cc-b01c-c798a12b4ccb** (conditional; sau S009): Hỗ trợ một phần còn chờ bếp/quản lý, mốc trả lời 5 phút; không hứa chen lượt. Nguồn: b03_welcome.
- **S011 55272352-11df-5583-ae6e-563122fdbdad** (declined; sau S009): Từ chối món nóng kịp giờ, cung cấp lựa chọn đã kiểm, khách chọn trái cây. Nguồn: b03_welcome.
- **S012 bd5c5a9c-a792-5a69-bfef-be9236cc9b19** (follow_up; sau S010): Follow-up nhánh conditional: bếp/quản lý xác nhận súp chuẩn bị sẵn, không chen lượt; 15 phút là dự kiến. Nguồn: b03_welcome.

### E04 — Phối hợp hậu trường

- **S013 340e95dc-87be-55ff-96de-6eadd5df1a7c** (routine; sau mở riêng): Backstage chỉ chia sẻ khu/khung giờ cần thiết; tác động phòng khác phải kiểm. Nguồn: b03_welcome.
- **S014 aad65f45-230e-58a8-937b-d41b43bc077e** (misunderstanding; sau S013): Sửa phạm vi từ toàn khách sạn về một hành lang/giờ; chưa hứa kết quả. Nguồn: b03_welcome.
- **S015 42ff057a-56df-58ac-bb11-eaa8765bc311** (routine; sau mở riêng): Owner vách/đèn/dọn/chỗ trống rõ, khách chưa được hứa giữ chỗ. Nguồn: b03_welcome.
- **S016 8c6bdac9-f564-5610-bccf-08e9b2c0d6ff** (follow_up; sau S015): Backstage kiểm sẵn thật, giới hạn âm và hạn giữ chỗ được nói rõ. Nguồn: b03_welcome.

### E05 — Khi dịch vụ sai kỳ vọng

- **S017 47f35b5e-78d6-58a6-8dd1-64b4cf54988e** (routine; sau mở riêng): Nghe kỳ vọng bị hụt ở lối đi phía sau, không dùng kỷ niệm cũ để bác. Nguồn: b03_welcome.
- **S018 5e9ffd48-0c92-53e3-abec-9e5bbb163555** (misunderstanding; sau S017): Sửa việc dùng hồ sơ cũ để bác mong muốn mới; quyết định thuộc khách. Nguồn: b03_welcome.
- **S019 e8dce435-8997-5704-aed1-c67d10a6c5b3** (routine; sau mở riêng): Sửa ánh sáng ngay nhưng chỗ khác và an toàn đèn còn chờ; mốc 10 phút. Nguồn: b03_welcome.
- **S020 5ee8d58a-f760-5f9e-8f5d-ebbbcd3a690f** (pending; sau S019): Quản lý chưa được hứa có mặt; mốc 10 phút phản hồi. Nguồn: b03_welcome.

### E06 — Sau phục vụ

- **S021 20cfe972-5207-5080-92ea-61cfe685f5ae** (routine; sau mở riêng): Follow-up phân biệt tiếng xe đã hết và tiếng người còn; khách chưa hài lòng. Nguồn: b03_welcome.
- **S022 3a06d154-583a-54c6-a2c6-ade06f5264a8** (problem; sau S021): Chưa hài lòng, chuyển đúng người quyết đổi phòng/phí; điều khoản chỉ là của khách sạn giả định. Nguồn: b03_welcome.
- **S023 71a85b2f-495f-5699-91e8-bc618018dcb0** (resolved; sau S022): Khách nhận phương án đổi phòng, nhưng giờ 10 và hỗ trợ hành lý còn xác nhận; không nói đã chuyển xong. Nguồn: b03_welcome.
- **S024 1dad433e-3bdf-59eb-9b7b-ea67414d68c8** (routine; sau mở riêng): Cảm ơn phản hồi, không lưu sở thích như mặc định; đầu mối khi cần. Nguồn: b03_welcome.
