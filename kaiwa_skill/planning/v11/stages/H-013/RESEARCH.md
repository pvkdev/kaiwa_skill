# H-013 — Nguồn và tự rà biên tập

Đọc catalog27/BOOK_GUIDE.md, source_index.jsonl và manifest.json; tra theo chức năng nói, quan hệ và cụm Nhật. Đọc các đoạn Markdown bên dưới gồm lời trước và sau. Mọi lời thoại trong stage do tác giả viết mới; nguồn sách chỉ định hướng ngữ dụng và trình tự. Không có khẳng định chính sách, phí hay thủ tục thực tế cần xác minh web.

## Nguồn đã đọc

- **b15_negotiate / B15 — 上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―**, `kaiwa_skill/knowledge/上級レベル ロールプレイで学ぶ ビジネス日本語 ―グローバル企業でのキャリア構築をめざして―/chapters/14-bai-14.md` dòng 8–77: Hỏi vấn đề, điều kiện và người quyết trong đàm phán; thoại mới dùng dự án hư cấu, mọi giá và lịch là điều kiện riêng của hai bên.

## Tự rà theo từng cảnh

Đã mở riêng từng cảnh, đọc liền tiếng Nhật và riêng tiếng Việt, đổi vai hai người nói, rồi đọc nối từng quan hệ `continues_from`. Kết quả và điểm kiểm cụ thể:

- **S001 3fcddada-fe9f-546d-805a-30245e8be7ed** (routine, từ mở riêng): Nam đặt mục tiêu và ba điểm mở. Kato muốn bàn giá trước. Không gọi việc mở buổi là đã có hợp đồng.
- **S002 3885267b-c0cb-586f-8bbf-7900f647d483** (misunderstanding, từ S001): Nam sửa hiểu lầm giá là điểm duy nhất. Kato nhận còn hạn và hỗ trợ. Nối S001: giữ đúng ba điểm đã nêu.
- **S003 0ef00f2a-35ee-5179-a08e-512853a764ca** (routine, từ mở riêng): Nam hỏi ưu tiên thật. Kato chọn khả năng dùng thử trước cuối tháng Sáu. Giá xét theo phạm vi, không là số cố định cho mọi trường hợp.
- **S004 35f95256-1132-5ff5-bb0d-485ddfdef741** (routine, từ mở riêng): Nam hỏi người duyệt cuối và tài liệu cần. Kato nêu trưởng bộ phận và một trang tóm tắt. Không xem phản hồi của Kato là phê duyệt.

### E01 đã checkpoint

- **S005 28b623b1-dfa8-56ac-b591-4f3cd85b889e** (routine, từ mở riêng): Nam gắn 600.000 yên với một bộ phận, bốn tuần, hai buổi. Kato hỏi bỏ một buổi thì giá thế nào. Con số là ví dụ của vụ hư cấu, chưa áp phạm vi khác.
- **S006 d87fa3cf-99b4-5e47-9471-680f3012a815** (conditional, từ S005): Nam đưa phương án 550.000 yên khi còn một buổi. Kato cần xem người dự. Nối S005: giảm giá đi với giảm hạng mục, không giảm vô điều kiện.
- **S007 58cf10ff-d85a-50d7-ac70-77e0c470220a** (declined, từ S006): Nam nhận khách cần đủ hai buổi và hỏi cách đổi tiến độ. Kato ưu tiên biết ngày buổi hai. Nối S006: phương án 550.000 yên bị từ chối.
- **S008 f6af96fd-38bf-5785-85a9-cbfa661b09c1** (pending, từ S005): Nam xin duyệt ngoại lệ rồi báo trước trưa thứ Sáu. Kato chỉ nhận chờ, chưa có giá mới. Nhánh trực tiếp S005: không nhập lời từ S006/S007.

### E02 đã checkpoint

- **S009 3459f641-c6a8-5e44-ac78-012eac2340f0** (routine, từ mở riêng): Nam hỏi ai cung cấp dữ liệu gốc. Kato dự kiến chọn mẫu trước ngày mười tháng Sáu. Chưa chốt lịch làm khi chưa biết cách và ngày nhận.
- **S010 35b56c5e-a77e-5746-9bb1-f37e846eefef** (misunderstanding, từ S009): Nam sửa hiểu lầm sẽ nhập toàn bộ. Kato kiểm việc phía mình. Nối S009: bên khách chọn mẫu, bên Nam chỉ thiết lập mẫu dùng thử.
- **S011 9bcc5c84-3647-53d4-a731-d535ecde1ee4** (conditional, từ S009): Nam nêu điều kiện nhận mẫu đúng ngày để giữ hạn dự kiến. Kato hỏi nếu trễ. とすると suy từ điều kiện, không là bảo đảm pháp lý hay hạn giao vô điều kiện.
- **S012 a61054bb-56c4-5a5d-bb77-4b0af42fac56** (problem, từ S011): Nam hỏi mẫu chưa tới và hứa kiểm tác động rồi báo ngày mới. Kato không coi ba mươi tháng Sáu còn chắc. Nối S011: ngày mười ba là dự kiến mới, không áp tự động ngày cũ.

### E03 đã checkpoint

- **S013 201dbb05-870d-53c2-9f65-c82db7700a9e** (routine, từ mở riêng): Nam báo nội bộ phản hồi tích cực có điều kiện. Aki hiểu chưa hợp nhất giá và hai buổi. Không gọi phản hồi của đầu mối là hợp đồng.
- **S014 7a9b27fd-8da3-5b95-8775-834f4ea8cc41** (declined, từ S013): Nam hỏi vì sao leader không duyệt giảm giá đủ hai buổi. Aki nói chuẩn bị lặp là vướng. Nối S013 theo sự kiện nội bộ: 首を縦に振れません chỉ quyết định phương án giá này.
- **S015 a1f96678-ec39-59ed-a4b4-a83f7bca1d63** (alternative, từ S014): Nam đưa phương án tài liệu chung, buổi hai hỏi đáp. Kato báo người mới có thể cần giải thích nền. Nối S014: giá phải tính lại, không nói phương án đã được duyệt.
- **S016 399f8114-6f86-5dd7-90c0-606d666f25d1** (follow_up, từ S015): Nam tách điểm nhận và hai điểm chưa quyết. Kato xác nhận cả hai mức giá vẫn mở. Nối S015: đồng ý tài liệu chung không đồng ý giá.

### E04 đã checkpoint

- **S017 e4f38145-8420-594b-ba2b-2156fbf480ee** (routine, từ mở riêng): Nam tóm bất đồng thật, ngoài nhãn giá cao. Kato xác nhận cần hai buổi đầy đủ. Câu hỏi bước sau dựa đúng ràng buộc.
- **S018 9cb2bd86-cbaf-5525-b8e5-f6d572e2c2eb** (alternative, từ S017): Nam đề nghị thử một buổi riêng. Kato cần giá và phạm vi một buổi. Nối S017: chưa bao gồm buổi hai.
- **S019 eafea729-13d7-58dd-9cb8-95b031486bdd** (declined, từ S018): Nam nhận từ chối thử một buổi và hỏi nội dung tối thiểu. Kato nêu hai mục đích của hai buổi. Nối S018: không ép buổi đơn lẻ.
- **S020 c6cac18d-da6b-5cf5-920e-22806ebf1943** (pending, từ S019): Nam đề nghị hai bên hỏi người quyết rồi gặp lại. Kato xác nhận chưa thể quyết. Nối S019: thứ Ba chỉ mang điều đã kiểm, không là ngày ký.

### E05 đã checkpoint

- **S021 339d4563-9162-533c-b02c-a188db41ee54** (routine, từ mở riêng): Nam đọc lại hướng chung và ba điểm mở. Kato xác nhận chưa chốt. Rà riêng đúng trạng thái từng điều kiện.
- **S022 35962d87-563a-5d8d-add3-9c0133247a61** (accepted, từ S021): Nam nhận duyệt nguyên tắc, nối hai người phụ trách. Kato nêu Sato bên khách. Nối S021: nguyên tắc thử được nhận, chi tiết cuối còn phải đọc lại.
- **S023 863686d3-508b-5054-8d91-1778deb67e26** (unresolved, từ S021): Nam nêu ai kiểm hỗ trợ sau thử và mốc trả lời. Kato sẽ gửi loại câu hỏi cần nhận. Nhánh khác S021: chưa thống nhất hỗ trợ.
- **S024 6aa6ff65-f904-5df3-814a-c7c0f4fb2f22** (follow_up, từ S023): Nam báo chỉ đáp được câu hỏi quy trình hai tuần. Kato hỏi xử lý sự cố; Nam giữ là điểm còn mở. Nối S023: chưa coi điều kiện cuối đã ký hoặc sự cố đã nằm trong giá.

### E06 đã checkpoint

## Tra cứu và điểm nối

Tra catalog27 bằng `交渉`, `契約`, `条件`, `費用`, `承認`, đọc nguồn B15 được liệt kê và chuyên đề trước `sj-thuong-03`. Trong thoại, điều khoản là đề xuất/điều kiện của hai bên trong trường hợp hư cấu; không đưa khẳng định về hiệu lực pháp lý chung. Đã đối chiếu lời hứa trả lời đúng hẹn với các nhánh chờ và từ chối.
