# H-042 — Nguồn và tự rà biên tập

Căn hộ Kaze, hợp đồng, tiền thuê 90.000 yên, cọc 90.000, phí gia hạn, lỗi bình nóng, số tiền sửa và khấu trừ là hồ sơ giả định. Không suy một mức phí hoặc nghĩa vụ áp dụng chung. Brief V10 đánh dấu fact_check và DW01/DW03. Kiểm nguồn chính thức ngày 2026-11-16: DW01 Tokyo Housing Policy Bureau https://www.juutakuseisaku.metro.tokyo.lg.jp/fudosan/torihiki/301jirei (ví dụ tranh chấp thuê, thú nuôi, sửa thiết bị, trả nhà); DW03 MLIT https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000026.html trong registry cũ hiện trả 404 khi mở, nên dùng trang MLIT cùng chủ đề https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000020.html về hướng dẫn nguyên trạng. MLIT nói hướng dẫn là chuẩn tham khảo chung, cần xem hợp đồng hiện tại và trao đổi khi điều khoản mơ hồ; khuyến nghị kiểm hiện trạng vào/ra. Vì vậy hội thoại chỉ yêu cầu điều khoản, ảnh, biên bản, báo giá và tư vấn, không phán quyết ai phải trả trong vụ giả định.

## Nguồn đã đọc

- **B08-C05, dòng 583–609**: đã đọc bài 21 不動産屋で, đặc biệt hỏi nhu cầu nhà và phí ngoài tiền thuê; không biến mẹo sách thành điều khoản cụ thể.
- **B07-C08, dòng 225–237**: đã đọc đơn vị 念のため về kiểm lại và sao chụp tài liệu; dùng cho kiểm ảnh/bảng nhận nhà.
- **B06-C04, dòng 118–127**: đã đọc đơn vị 追ってご連絡します; trong hồ sơ tranh chấp luôn kèm người và mốc khi phù hợp.
- **DW01, Tokyo Housing Policy Bureau**, https://www.juutakuseisaku.metro.tokyo.lg.jp/fudosan/torihiki/301jirei (truy cập 2026-11-16): ví dụ tranh chấp thuê; giới hạn địa bàn Tokyo và không quyết hồ sơ Kaze.
- **MLIT, 原状回復をめぐるトラブルとガイドライン**, https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk3_000020.html (truy cập 2026-11-16): trang thay cho liên kết DW03 cũ lỗi 404; nêu phạm vi hướng dẫn và việc đối chiếu hợp đồng, hiện trạng, không ấn định khoản Kaze.

## Chuyên đề trước

Đã đọc lesson.md và practice.json của sj-thuong-12. Dùng 話が違う sau khi nêu email/lời cũ cụ thể; ちょっと… với lý do về khoản phí; 百歩譲って chỉ dùng khi giới hạn nhượng bộ và giữ khoản cửa riêng. 大目に見る không đưa vào vì dễ tạo kỳ vọng miễn trách nhiệm. Gắn specialty ID chỉ các cảnh dùng thật.

## Tự rà từng cảnh

### E01 — Đối chiếu và thương lượng điều kiện gia hạn

- **S001 f5eb967d-1edf-5842-9db3-e0a92c1e2480** (routine; sau mở riêng): Lời hiểu cũ vs đề nghị mới tách, chưa gán lời cũ là hợp đồng. Nguồn: housing.
- **S002 00833278-c4e6-54a1-8893-4921042f7df9** (misunderstanding; sau S001): Sau S001 nhận email chỉ là cân nhắc, không khẳng định quyền 1 năm/45k. Nguồn: housing.
- **S003 aa078bb2-c7ea-59a8-a618-7814ca64e344** (conditional; sau S002): Đề xuất có điều kiện, chưa chấp thuận hai năm; thẩm quyền phí ở chủ nhà. Nguồn: housing.
- **S004 f8d8272b-7331-5a57-8e5d-d436e7236cd0** (alternative; sau S003): Sau S003 chỉ nhượng phí xuống 60k, không biến hỏi thành chấp nhận. Nguồn: housing.
- **S005 265475b0-7d68-5ff9-8e30-55f36ac4fe85** (pending; sau S004): Sau S004 chỉ 90k tiền thuê được giữ, phí/kỳ hạn pending, người quyết và mốc rõ. Nguồn: housing, callback.

### E02 — Sửa chữa có tranh luận

- **S006 5f8ee060-0f45-5f7f-8f38-cd633c02ac1b** (routine; sau mở riêng): Báo lỗi lặp với mốc, chứng cứ và sửa tạm; không tự kết luận trách nhiệm. Nguồn: housing.
- **S007 634122aa-f6e4-5be2-b89c-0279783e787c** (misunderstanding; sau mở riêng): Sửa suy đoán cách dùng thành vấn đề cần chứng cứ; không miễn hay gán phí. Nguồn: housing.
- **S008 1ab8af74-ed84-5756-ac47-46ecee104b10** (conditional; sau mở riêng): 12k/24k chỉ đề nghị tạm; yêu cầu phạm vi và an toàn. Nguồn: housing.
- **S009 03197470-87cd-5d77-ad57-b90835e58519** (unresolved; sau mở riêng): Unresolved phí, bảo toàn kiểm kỹ thuật, phân quyền quản lý/chủ nhà. Nguồn: housing.
- **S010 3917c525-dbd4-5708-b98f-167b82d8aab7** (follow_up; sau S009): Sau S009 có kết quả kỹ thuật nhưng chưa ra quyết định phí; sửa có điều kiện linh kiện. Nguồn: housing.

### E03 — Thay đổi điều kiện sống

- **S011 a71a7653-c263-5fcb-9b45-4a59aab37abf** (routine; sau mở riêng): Điều khoản giả định được hỏi riêng; chưa chuyển người hay nuôi mèo. Nguồn: housing, verify.
- **S012 26ae1b78-0d54-54cc-a2ec-3654a8746a6e** (routine; sau mở riêng): Đề nghị thay đổi có thời điểm, tách người và thú, chưa tự thực hiện. Nguồn: housing.
- **S013 9a7aa363-dd1e-5556-9f3a-bb67bc2165c5** (conditional; sau mở riêng): Chấp nhận có điều kiện chỉ việc ở cùng; phí và giấy cuối vẫn cần kiểm. Nguồn: housing.
- **S014 be11cce9-4d04-5268-b89a-63a4bb4fa0f8** (declined; sau mở riêng): Từ chối mèo không suy phủ định người ở cùng, không gợi nuôi trái quy định. Nguồn: housing.
- **S015 d3580f38-9715-57c8-9fd5-fc226bb170a2** (resolved; sau S014): Sau S014 chốt hành vi phù hợp; đơn ở cùng chưa duyệt, chưa ở. Nguồn: housing.

### E04 — Chuyển đi và kiểm phòng

- **S016 daa13851-7364-514d-ad7e-eb920abe739d** (routine; sau mở riêng): Rời nhà 30/6 theo hồ sơ, kiểm phòng không đồng nghĩa chốt tiền. Nguồn: housing, verify.
- **S017 004a6484-84d0-543e-b161-87165aea32a1** (routine; sau mở riêng): Chứng cứ vết cũ có ngày và số mục, người kiểm mới ghi đối chiếu chứ chưa kết luận. Nguồn: verify.
- **S018 d3ce1d2c-2caf-5f03-9106-bbf3f751b228** (misunderstanding; sau mở riêng): Sửa hiểu nhầm new vs reported; không tự chốt vết cũ nếu ảnh chưa so xong. Nguồn: verify.
- **S019 f007b527-b164-5ece-b1e8-ab03a3bdb20a** (conditional; sau mở riêng): Khu chưa nhìn được ghi pending, có hẹn 14 giờ, chìa khóa sau đó. Nguồn: verify.
- **S020 af332c9a-873f-573d-8db2-965a0ba99be7** (resolved; sau S019): Sau S019 hoàn tất kiểm khu tủ, hiện trạng rõ; door và phí chưa chốt. Nguồn: verify, callback.

### E05 — Bàn khoản hoàn trả/khấu trừ

- **S021 8921477a-8801-5553-9ce6-8d623e8d313b** (routine; sau mở riêng): Phép cộng đúng 54k trừ và 36k trả nhưng đều tạm, không chấp nhận. Nguồn: housing, verify.
- **S022 ee976ecf-68ec-53df-8dd1-43fe4116b9bb** (routine; sau mở riêng): Thách căn cứ từng dòng và điều khoản, không tự khẳng định miễn cọc. Nguồn: housing, verify.
- **S023 7a1f7d57-f780-54ff-9859-5fd2428d9828** (pending; sau mở riêng): Pending chứng cứ có mốc nhận và trả lời, không hứa hoàn tiền. Nguồn: callback, verify.
- **S024 01c3aaf0-e770-516f-9202-b8f06462eb75** (alternative; sau mở riêng): Alternative giới hạn tranh chấp vào cửa trước, cleaning chỉ giả định, không đồng ý thực. Nguồn: housing.
- **S025 0af294cd-2289-5d7a-bc93-4e95e1a1963e** (declined; sau S024): Sau S024 vẫn chưa căn cứ cửa; từ chối ký số cuối và xin tư vấn, không khẳng định kết quả. Nguồn: housing.

### E06 — Giữ kênh giải quyết

- **S026 f0ea6493-601f-5f76-b56f-17fcd422c027** (routine; sau mở riêng): Tách hợp đồng, repair, deposit; không suy rằng báo cáo kỹ thuật quyết phí. Nguồn: verify, callback.
- **S027 59bdb5b3-2a30-5bf3-8f0d-aeb76bed1cdd** (routine; sau mở riêng): Thẩm quyền owner/manager/inspector/vendor được tách; chưa có kết luận. Nguồn: housing.
- **S028 0b222f2d-2bd7-5963-8417-65ff04f7d4b2** (conditional; sau mở riêng): Tư vấn giúp lập câu hỏi, chưa phán quyết hoặc đại diện pháp lý. Nguồn: housing, verify.
- **S029 b5c3a198-a8cf-5286-a828-d5d955edb48b** (follow_up; sau mở riêng): Follow-up sau tư vấn: câu hỏi rõ hơn, không biến lời tư vấn thành kết luận. Nguồn: verify, callback.
- **S030 c2f0c801-1f9f-57aa-8965-bc08a2d589a0** (resolved; sau S029): Sau S029 có giấy nhưng chưa kết luận; resolved là kênh, mốc, record, không phải số tiền. Nguồn: verify, callback.
