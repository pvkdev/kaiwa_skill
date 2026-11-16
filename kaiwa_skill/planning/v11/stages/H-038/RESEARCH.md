# H-038 — Nguồn và tự rà biên tập

Tra BOOK_GUIDE.md, source_index.jsonl và manifest.json của catalog27 theo 出張, 空港, 荷物, 欠航, 税関. Đọc sâu B16-C05 và B17-C09, sj-thuong-11 lesson/practice. Tra Japan Customs và ANA/JAL chính thức ngày 2026-11-16. Chuyến SA206, Sora Air, tuyến Tokyo–Seoul, công ty và đối tác đều giả định. Hội thoại không khẳng định quyền đổi vé hay điều kiện thông quan; hỏi đúng hãng/công chức, giữ quyết định pending.

## Nguồn đã đọc

- **b16_trip / B16** `kaiwa_skill/knowledge/中級レベル ロールプレイで学ぶ ビジネス日本語 ―就活から入社まで―/chapters/05-Unit4-初めての仕事.md` dòng 198–229: mục tiêu, nội dung, kết quả, quyết định trong báo cáo công tác.
- **b17_airport / B17** `kaiwa_skill/knowledge/初中級レベル ロールプレイで学ぶ ビジネス日本語 ―場面に合わせて適切に話そう―/chapters/08-いとこを空港まで迎えに.md` dòng 18–38: xin điều chỉnh lịch làm và bàn giao trước khi ra sân bay.
- **Japan Customs, 7205** https://www.customs.go.jp/english/c-answer_e/keitaibetsuso/7205_e.htm (đọc 2026-11-16): xuất mẫu thương mại mang theo có thủ tục tùy loại/giá trị; nên hỏi công chức hải quan, S011–S012 không đưa kết luận thông quan.
- **JAL international disruption guidance** https://www.jal.co.jp/jp/en/inter/change/irregular/webguidance/index.html và **ANA** https://www.ana.co.jp/en/jp/guide/boarding-procedures/support/international/ (đọc 2026-11-16): điều kiện đổi chuyến tùy đặt chỗ; chỉ dùng để tránh khái quát dịch vụ hãng giả định trong S013–S016.

## Chuyên đề trước

Đã đọc `kaiwa_skill/planning/v10/stages/sj-thuong-11/lesson.md` và `practice.json`; S001 và S021 dùng cách mở lời 急な話で恐縮ですが/急なご連絡で恐縮ですが đúng nghĩa báo gấp. Không gắn ID cho các mẫu khác.

## Tự rà từng cảnh

### E01 — Nhận lệnh công tác gấp

- **S001 a9139839-06da-5ba6-b5af-e3eb1f714f34** (routine; sau mở riêng): Công tác gấp có mục tiêu/giới hạn quyền rõ, không ngầm cho phép đổi hợp đồng. Nguồn: b16_trip.
- **S002 1073505e-04b0-5b7a-a5d3-2b62063385b5** (routine; sau mở riêng): 16 giờ là lịch gặp, trưa là chuyến dự kiến; phần đối chiếu làm từ xa trước. Nguồn: b16_trip.
- **S003 77ad92e0-3c2d-53d2-8c02-50a860729516** (conditional; sau S002): Nhánh hỗ trợ từ xa không tự hủy công tác; mốc 21 giờ để cấp trên quyết. Nguồn: b16_trip.
- **S004 ac1dc3ff-d3d5-594b-a715-2af28971c790** (routine; sau mở riêng): Bàn giao việc hiện tại có owner/trạng thái, không bỏ báo giá chưa duyệt. Nguồn: b16_trip.

### E02 — Thiếu giấy tờ/thông tin trước đi

- **S005 ecd19d01-f593-52b4-b9e2-1e63f2936017** (routine; sau mở riêng): Thiếu bản duyệt nội bộ, không nhầm thành thiếu giấy tờ xuất nhập cảnh. Nguồn: b16_trip.
- **S006 f463359d-34e0-59fa-a1dd-cd319c5d44ec** (pending; sau S005): Mốc 19:30 chờ bản đúng; bản 2 không được nhận nhầm thành bản duyệt. Nguồn: b16_trip.
- **S007 06b63aa0-8be0-5a1a-88d9-002b219277ae** (misunderstanding; sau S005): Sửa hiểu nhầm final filename, chỉ bản có mã/duyệt khớp mới dùng. Nguồn: b16_trip.
- **S008 25daaac3-18df-54b7-9339-6e05b96ca36f** (follow_up; sau S006): Có bản 3 và ghi nhận duyệt, gửi không đồng nghĩa người chi nhánh đã xem. Nguồn: b16_trip.

### E03 — Hỏi tại sân bay/hải quan

- **S009 d7965035-ee02-54eb-a679-5a0f3728d283** (routine; sau mở riêng): Hỏi quầy dựa trên hãng/số chuyến; vị trí và chuyến bay chỉ thuộc tình huống giả định. Nguồn: b17_airport.
- **S010 5529c839-0fd3-5566-aa4a-b2410e702ee4** (misunderstanding; sau S009): Sửa quầy theo số chuyến/hãng, không đoán từ đích chung. Nguồn: b16_trip.
- **S011 0d1ac5a4-8776-5db3-b4dc-f3db474c37ad** (routine; sau mở riêng): Đúng đầu mối hải quan Nhật xuất mẫu, không dạy thông quan hay khẳng định miễn thủ tục. Nguồn: b17_airport.
- **S012 9c2e4061-2cd6-597c-98e7-0537b40addd0** (pending; sau S011): Tài liệu đã nhận chưa bằng thông quan; không hứa thời gian khi công chức chưa kiểm. Nguồn: b16_trip.

### E04 — Chuyến bay đổi/hủy

- **S013 88d80f42-2b9f-58e8-a5db-1c7b1cd3c2e1** (routine; sau mở riêng): Chuyến hủy, 15 giờ/18 giờ chỉ ứng viên chưa giữ chỗ; không tự đưa ra quyền đổi vé. Nguồn: b16_trip.
- **S014 7ac487bf-b27c-5dd3-88a7-de755e3281ca** (conditional; sau S013): Giữ tạm khác vé cấp lại, giờ đến dự kiến khác thời gian thực, phí/bag tùy vé giả định. Nguồn: b16_trip.
- **S015 6a5b60fd-46b1-5cf7-a72d-b7bb6e96b4a2** (declined; sau S013): Nhánh không còn chuyến trong ngày; dịch vụ chỗ ở và hành lý chỉ hỏi điều kiện vé cụ thể. Nguồn: b16_trip.
- **S016 695d18bc-2705-51a2-8a47-7bb4683daf0f** (follow_up; sau S014): Vé đã cấp nhưng đến 18 giờ là dự kiến; gặp/đón chờ phía kia xác nhận. Nguồn: b16_trip.

### E05 — Hành lý và phương tiện đến nơi

- **S017 f20043bf-0439-5812-b1f8-9fee891c955a** (routine; sau mở riêng): Quầy có ghi nhận bag chưa cùng chuyến nhưng chưa biết vị trí/giờ, có mã tra cứu. Nguồn: b16_trip.
- **S018 18cd809b-c911-595e-badb-5dda1c32c753** (pending; sau S017): Đầu mối 20 giờ, giấy trong bag nhưng bản điện tử có thể thay; không suy sẽ tới ngay. Nguồn: b16_trip.
- **S019 f8108c4c-1bc9-5786-b6ba-fd8891027b8c** (alternative; sau S018): Chi nhánh có bản 3 đã nhận và mở được, nhưng in/chia sẻ phụ thuộc nhu cầu và phạm vi. Nguồn: b16_trip.
- **S020 4cb83e84-96d2-5e91-82e4-a98bc02ceb11** (follow_up; sau S019): Bag tới thật, nơi/giờ nhận là chi tiết hồ sơ giả định do hãng xác nhận, không là quy tắc chung. Nguồn: b16_trip.

### E06 — Đổi lịch gặp

- **S021 b4fe6e49-4cdb-5e7d-8bea-ff81ad9c4dfe** (routine; sau mở riêng): Dùng specialty mở lời thật, chuyến thay mới dự kiến, khách hẹn 13 giờ trả lời khả năng đổi lịch; chưa có giờ gặp mới. Nguồn: b16_trip.
- **S022 c00c6782-48dc-593a-8694-5791336ef62d** (declined; sau S021): Đối tác từ chối đổi lịch, đồng nghiệp chỉ giải thích bản duyệt, quyết định hợp đồng chờ. Nguồn: b16_trip.
- **S023 a4cdd831-3dc3-59d9-8bd7-bf87abc6d874** (conditional; sau S021): 15 phút chọn nội dung cấp bách, chi phí chưa được quyết; mốc báo trễ rõ. Nguồn: b16_trip.
- **S024 7a62f5f1-b5d0-5e07-a83b-94b98da06016** (follow_up; sau S023): Buổi ngắn chỉ kiểm hai điểm, tài liệu ngày mai dự kiến, chi phí/phạm vi và lịch tiếp còn chờ. Nguồn: b16_trip.

### E07 — Kết công tác/chuyển người

- **S025 61c2a686-2afc-5371-8b08-3d73a37eab8e** (routine; sau mở riêng): Kết công tác tách hai điểm đã kiểm, nháp chưa duyệt, phí/phạm vi pending, owner từng phần. Nguồn: b16_trip.
- **S026 f1086064-b459-5e09-9434-e136aef34681** (misunderstanding; sau S025): Sửa hiểu nhầm ở lại thêm; ngày về chốt, tuyến liên hệ sau về rõ. Nguồn: b16_trip.
- **S027 605ca56f-9913-5b95-8727-9caf20147826** (routine; sau mở riêng): Đầu mối chi nhánh/bản; Tokyo/phí; backup khi vắng; bàn giao chưa mặc định đã được đọc. Nguồn: b16_trip.
- **S028 d51626c8-79f7-5c39-9ca3-beb2383b2911** (follow_up; sau S027): Follow-up xác nhận người nhận đã đọc; phí/hợp đồng chờ Tokyo, có giờ hỏi lại. Nguồn: b16_trip.
