---
name: kaiwa-topic-shadowing
description: Soạn và rà bài shadowing V13 cho một chặng topic đã có từ vựng V12 được duyệt. Tạo câu Nhật độc lập có bản Việt, vai và giọng TTS để chuẩn bị cho tình huống V11.
---

# Shadowing theo chủ đề

## Đọc trước khi soạn

Từ gốc repo, chạy `py -X utf8 .agents/skills/kaiwa-topic-shadowing/scripts/pilot.py brief S-011` với mã được giao. Công cụ chỉ nhận chặng topic có checkpoint từ vựng hợp lệ. Đọc các nhóm từ V12, mục tiêu, vai, mọi hội thoại V11 và shadowing cũ trong brief. Shadowing giáo trình giúp tham khảo cách diễn đạt. Viết các câu mới từ mục tiêu giao tiếp. Nguồn cũ và các bằng chứng mà V12 đang trỏ tới nằm nguyên trong phiên bản trước.

## Soạn bài

- Chọn khoảng 4–6 việc người học cần nói được và những từ giúp họ tự đổi chi tiết. Chọn vài mẫu có ích để gặp lại 2–3 lần. Lặp bằng cách đổi ý định, điều kiện, đối tượng hoặc mức thân mật khi tự nhiên. Đặt một vài lần gặp lại cách nhau trong bài.
- Một chặng có một node. Xếp câu dễ trước, rồi đến biến thể và lượt vận dụng. Gom thành các nhóm có tên Việt dễ hiểu. Thường thử 18–24 câu. Chủ đề hẹp có thể ngắn hơn, chủ đề rộng có thể dài hơn. Thêm câu khi nó giúp nói được một điều quan trọng. Loại câu chỉ đổi tên riêng hoặc thay số cho đủ số lượng.
- Một mục là **một người nói một câu độc lập**. Đọc riêng từng câu theo thứ tự ngẫu nhiên. Người học phải hình dung được việc mình đang nói. Tránh mẩu đáp phụ thuộc lượt trước. Có thể dùng mệnh đề phụ trong một câu. Viết cách đọc tự nhiên cho TTS và dùng chữ Nhật thông dụng. Bản Việt giữ đúng vai, độ lịch sự, dụng ý, phạm vi phủ định và mức chắc chắn. Vai đủ cụ thể để chọn giọng giao tiếp. Gán giọng TTS `male` hoặc `female` cho mỗi câu.
- **Sơ** ưu tiên vật, việc cụ thể và một ý ngắn nói được trong một hơi. Dùng mẫu quen thuộc với đúng vị trí của chặng. Nếu hội thoại nguồn có cách hỏi phức tạp, thử cách hỏi đơn giản hơn mà vẫn đạt mục tiêu. Cụm cố định thiết yếu có thể khó về cấu tạo nhưng vẫn vừa sức để dùng nguyên cụm.
- **Trung** luyện lựa chọn cách nói theo quan hệ, thêm lý do, điều kiện hoặc làm mềm lời nhờ. Giữ mạch xử lý vừa sức khi nghe một lần. **Thượng** luyện sắc thái lập trường, hàm ý, phản biện hoặc thương lượng đúng hoàn cảnh. Chọn câu ngắn nếu đó là cách nói thực tế, tránh dồn danh từ và kính ngữ để nâng độ khó.
- Đối chiếu câu với chặng trước/sau cùng cấp nếu phân vân về độ khó. Nội dung người học nhìn thấy chỉ có kiến thức và câu luyện. Mã nguồn, level, liên kết tình huống và nhận xét biên tập nằm trong metadata.

## Rà nhịp nói trước khi giao bài

- Đọc liền ba câu mở đầu như người mới bắt đầu luyện chủ đề. Ngay cả ở Thượng, mở bằng một hành động dễ hiểu và một câu có thể bắt chước ngay. Sau đó mới tăng độ tinh tế hoặc số vế. Nếu hai vế có thể luyện riêng, chọn ý người học thực sự cần nói nhất.
- Ở chặng Sơ đầu lộ trình, so sánh câu khó nhất với cách hỏi trực tiếp. Chẳng hạn, khi muốn biết quầy nào kiểm tra vé, có thể nói 「切符はどの窓口で見てもらえますか。」. Chỉ giữ kiểu hỏi lồng hoặc điều kiện khi chính cách nói đó là trọng tâm. Đọc bản Việt thành tiếng, tránh dịch máy móc trật tự tiếng Nhật.
- Hình dung người nói, người nghe và thời điểm nói cho từng câu. Với cảnh vốn diễn ra qua tin nhắn hoặc giấy tờ, chọn lời nói trực tiếp/điện thoại có cùng mục đích. Rà cảnh bị gắn vào câu chỉ vì có chung một từ. Ưu tiên các nhu cầu giao tiếp chính, cho phép nhiều cảnh dùng chung một cách nói và cho phép cảnh phụ không có câu riêng.

## Hai lượt đọc tách khỏi ngữ cảnh

1. Che tiêu đề nhóm, vai và mã cảnh. Đọc câu, trả lời “Người này nói để làm gì?”. Với những chặng thiên về quan hệ, câu nên thể hiện hành động như gỡ ngượng, chia sẻ gánh nặng, cho người nghe quyền lựa chọn. Nếu chỉ còn một chi tiết hậu cần, xem lại cách diễn đạt hoặc dành chỗ cho câu hữu ích hơn. Với câu chủ ý sửa nói nhầm, phải nghe thấy cách nói đúng ngay trong cùng câu.
2. Che tiếng Nhật, đọc thành tiếng câu Việt như đang nói với một người thật ở quầy, trong nhà, trên điện thoại hay trong cuộc họp. Sau đó mở tiếng Nhật, so lại ai làm gì, mức chắc chắn, lời hứa và độ lịch sự. Dịch ý tác nghiệp như yêu cầu bưu cục kiểm tra hành trình bằng từ người gửi hàng sẽ nói. Khi chủ thể bị lược, chỉ cụ thể hóa trong tiếng Việt nếu đúng ý. Giới tính giọng TTS là của người nói, không quyết định cách gọi người nghe.

## Bản thảo và nghiệm thu

Mỗi chặng có `kaiwa_skill/planning/v13/pilot/<code>/draft.json`. Tạo object `{code, pins, groups, items}`. Chép đúng object `pins` từ brief đã dùng để viết. Nếu nguồn thay đổi trong lúc làm, đọc lại phần đổi trước khi cập nhật pins. Groups là object ánh xạ mã nhóm ổn định sang tên Việt. Items là mảng theo thứ tự luyện. Mỗi mục có các trường:
- `id` dạng `<code>-V13-001`, `group` là mã nhóm, `role_vi`, `gender`, `ja`, `vi`.
- `terms` là mảng mặt chữ mục từ thực sự dùng trong câu theo danh sách V12, kể cả dạng chia. Có thể rỗng nếu câu cần thiết để luyện một mẫu. `scenes` là mảng mã tình huống V11 mà câu giúp chuẩn bị. `pattern` là nhãn nội bộ của mẫu thực sự có trong câu, dùng cùng nhãn khi luyện lại mẫu.
- Với mỗi nhóm, đọc toàn bộ câu theo thứ tự và đọc lại từng câu riêng. Đối chiếu chính tả, tiếng Việt, vai, giới tính, độ dài và ngữ pháp theo cấp. Dùng các liên kết nội bộ để kiểm có những việc giao tiếp nào chưa được luyện. Rà các cặp gần trùng và lý do mỗi lần lặp.
- Chạy `pilot.py check <code>`. Điều phối kiểm lại nội dung rồi dùng `pilot.py publish <code>` để xuất node theo định dạng roadmap và ghim hash V11, V12, skill, bản thảo. Khi đầu vào đổi, kiểm và duyệt lại trước khi xuất. Bản thảo và checkpoint nằm riêng từng chặng.
- Pilot hiệu chỉnh skill: lưu báo cáo chẩn đoán của vòng, sửa quy tắc nếu lỗi lặp lại, xóa bản thảo và bản xuất V13 của vòng trước rồi soạn mới từ nguồn. Giữ nguyên dữ liệu V11/V12. Trong đợt thử hiện tại tối đa ba vòng, lần lượt 3, 6 và 9 chặng nếu tiếp tục.
