# H-014 — Nguồn và tự rà biên tập

Đọc catalog27/BOOK_GUIDE.md, source_index.jsonl và manifest.json; tra theo chức năng nói, quan hệ và cụm Nhật. Đọc các đoạn Markdown bên dưới gồm lời trước và sau. Mọi lời thoại trong stage do tác giả viết mới; nguồn sách chỉ định hướng ngữ dụng và trình tự. Không có khẳng định chính sách, phí hay thủ tục thực tế cần xác minh web.

## Nguồn đã đọc

- **b15_negotiate / B15 — 上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―**, `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/14-bai-14.md` dòng 8–77: Hỏi lại yếu tố giá, phạm vi và người quyết; cuộc mua hộp là giả định riêng, không dùng báo giá sách.
- **nta_tax — 国税庁 No.6303 消費税および地方消費税の税率**, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6303.htm (2026-11-16): Nguồn cơ quan thuế Nhật về thuế suất tiêu chuẩn 10% và mức giảm 8%. Cảnh S022–S023 chỉ áp mức tiêu chuẩn cho hộp nhựa bán trong nước của tình huống hư cấu sau khi nhân vật xác nhận mặt hàng; không khái quát cho mọi giao dịch.

## Tự rà theo từng cảnh

Đã mở riêng từng cảnh, đọc liền tiếng Nhật và riêng tiếng Việt, đổi vai hai người nói, rồi đọc nối từng quan hệ `continues_from`. Kết quả và điểm kiểm cụ thể:

- **S001 1fbdbce5-5bd5-5f0e-a7d8-fe2bc373b023** (routine, từ mở riêng): Nam hỏi hai yếu tố làm giá tăng. Kato nêu vật liệu và số chuyến giao. Giá 1.000 yên là chưa thuế của 500 hộp, không bao gồm phí khác.
- **S002 627f5581-42ca-5fd3-8b31-242a7ead932f** (misunderstanding, từ S001): Nam kiểm và sửa hiểu lầm cước nằm trong đơn giá. Kato sẽ tách tiền hàng và vận chuyển. Nối S001: giá hàng và phí giao là hai mục.
- **S003 5bbddfa3-2d1d-5df7-96aa-48a30193e042** (routine, từ mở riêng): Nam xin so 500 và 800 theo cùng điều kiện. Kato phải hỏi lại vật liệu. Chưa quyết mua 800.
- **S004 cddfb634-cdf4-5f13-8005-337a6d21e0e9** (pending, từ S003): Nam hỏi mốc nhận bảng so. Kato hẹn chiều thứ Sáu. Nối S003: chưa có giá mới để dùng.

### E01 đã checkpoint

- **S005 726fbf68-32b6-5042-a8c3-0ede2d5acafb** (routine, từ mở riêng): Nam thử đề nghị giá cho ba đợt, không cam kết mua. Kato chỉ nói khả năng gom vật liệu. Giá mới vẫn là phương án có điều kiện.
- **S006 66e88b2a-6d5e-5ab0-8c49-41035045ce67** (conditional, từ S005): Nam nhắc điều kiện 800 hộp mới có 950 yên. Kato giữ 1.000 yên khi 500. Nối S005: không tự nâng lượng trước khi hỏi sử dụng.
- **S007 3c53c7c9-4727-5f0a-b2d9-e6e725d14cb7** (declined, từ S005): Nam nhận đơn giá không giảm và chuyển sang cước. Kato cần nơi và số chuyến để báo giá. Nhánh khác S005, không dùng mức 950 yên của S006.
- **S008 2b80fc82-a15b-52d3-9121-50047cb550b1** (alternative, từ S007): Nam xin so một và hai chuyến. Kato hỏi chỗ lưu và lịch dùng. Nối S007: giảm cước có thể tăng gánh nặng bên nhận.

### E02 đã checkpoint

- **S009 a7c4517c-9a3e-5ed0-9e1e-bf7bfc0f10c1** (routine, từ mở riêng): Nam hỏi tiêu chí đổi vật liệu. Kato nêu độ bền khi xếp chồng. Không coi giảm giá là chất lượng giữ nguyên.
- **S010 d8142496-3b9c-5006-aa15-29382143e8fd** (conditional, từ S009): Nam xin mẫu và thử dùng trước chốt. Kato sẽ chuẩn bị sau khi biết mục thử. Nối S009: thử xếp chồng và mang đi.
- **S011 1c5f54e9-841d-5026-8a2b-42566707e6fc** (problem, từ S009): Nam nêu rủi ro giao trễ cho người dùng. Kato đồng ý chờ ngày thực cần. Không chọn phí thấp trước khi kiểm hạn.
- **S012 6aeab8b7-b3be-5173-aae7-3aff0d90ee29** (follow_up, từ S011): Nam giữ mốc giao vì hiện trường không thể chờ. Kato bỏ chuyến muộn và kiểm cách đóng kiện khác. Nối S011: rủi ro giao trễ đã được xác nhận.

### E03 đã checkpoint

- **S013 3ecee1a7-9f8f-5f61-99d4-1b8d4d058a77** (routine, từ mở riêng): Nam báo giảm đơn giá chỉ ở 800 hộp. Aki hiểu tổng tiền phải tính theo lượng. Không biến đơn giá thấp thành tổng chi thấp.
- **S014 9a37b62b-a9ba-54da-a6c6-558e97313d7a** (misunderstanding, từ S013): Nam sửa hiểu lầm chất lượng mẫu rẻ đã bằng hộp cũ. Aki chờ kết quả thử. Nối S013 theo sự kiện nội bộ: giá không chứng minh chất lượng.
- **S015 d5bae6e1-5f8e-5984-95fc-2bd9f380c2ae** (routine, từ mở riêng): Nam hỏi điều kiện người dùng không thể bỏ. Aki nêu vừa kệ và dễ lấy. Không tự quyết thay bộ phận dùng.
- **S016 676a0e3f-bdd9-5b15-8008-190141c72e5e** (pending, từ S015): Nam hẹn mốc có kết quả thử. Aki giữ đặt hàng sau kiểm thứ Hai. Nối S015: mẫu chưa được duyệt.

### E04 đã checkpoint

- **S017 5e1d05f7-5f2a-5ce1-94ba-bfc388156aff** (routine, từ mở riêng): Nam báo nội bộ chưa duyệt và hỏi phương án ngoài đơn giá. Kato cần ngày sử dụng trước khi so giao. Không ép giảm khi chưa có điều kiện.
- **S018 3eef2717-7a7f-52db-a878-52ed3e885864** (declined, từ S017): Nam nhận giới hạn nhà cung cấp và tạm hỏi nội bộ. Kato giữ báo giá hiện tại. Nhánh S017: không nói Kato đã đồng ý giảm.
- **S019 abfc8699-a846-56b3-a312-2a02485d4efb** (alternative, từ S017): Nam hẹn hỏi lại theo số liệu quý sau. Kato chỉ hứa báo giá lại, không hứa giảm. Nhánh khác S017; mốc sau quý là xem điều kiện.
- **S020 c5fff0c0-2d89-5d55-bdcc-4c6d5241308e** (follow_up, từ S019): Nam đưa số dùng thực tế 600 hộp. Kato không áp mức 950 của 800 hộp. Nối S019: dữ liệu mới mở báo giá mới, không hồi tố lời hứa.

### E05 đã checkpoint

- **S021 c680bebf-7350-5cd0-ae4d-05dc7078466b** (routine, từ mở riêng): Nam nhắc giá, lượng, ngày mong muốn và cước riêng. Kato phải kiểm hàng mới xác nhận ngày. Ngày hai mươi tháng Sáu là mong muốn, chưa là hạn giao chốt.
- **S022 06f8b89d-d322-5a4b-ae6c-2f4c6efc7cb7** (misunderstanding, từ S021): Nam hỏi lại cách hiểu giá trước thuế. Kato hứa báo giá ghi rõ thuế. Nối S021: 1.000 yên chưa thuế, chưa tự tính tổng.
- **S023 22da1136-824f-5588-be90-ad50d784d646** (accepted, từ S022): Nam nhắc 1.100 yên đã thuế cho 500 hộp. Kato giữ cước riêng. Nối S022: NTA tiêu chuẩn 10% đã kiểm cho mặt hàng trong tình huống, 1.000→1.100; không coi tổng chi phí đã chốt.
- **S024 5e8381ef-6a51-53f6-9ca7-9d34dd9561f2** (follow_up, từ S023): Nam hỏi số xuất và đơn giá chứng từ. Kato cho 500 hộp và 1.100 yên đã thuế, cước riêng. Nối S023: chất lượng và số nhận thực tế chỉ biết khi kiểm hàng.

### E06 đã checkpoint
