---
name: kaiwa-speak-japanese-roadmap
description: Lập bản đồ chuyên đề Speak Japanese V7 cho Harumii. Đọc chín sách, gom bài theo năng lực nói, đặt chuyên đề trước các tình huống sẽ dùng và đối soát với khung topic V6.5. Áp dụng khi lập kế hoạch, chạy pilot, phân bổ toàn bộ hoặc chỉnh vị trí một chuyên đề.
---

# Xây chặng chuyên đề Speak Japanese

V7 hướng tới hai loại chặng trong cùng một lộ trình. Chặng topic cho người học một việc cần giải quyết trong đời sống hoặc công việc. Chặng chuyên đề giúp người học biết chọn cách nói theo ý định, quan hệ và phản ứng của người nghe. Kết quả biên tập ở pha này là bản đồ chặng, nguồn kiến thức và cơ hội vận dụng. Chủ dự án sẽ quyết định cấu trúc bài bên trong chuyên đề ở pha sau.

Đọc [kế hoạch V7](../../../kaiwa_skill/planning/v7/PLAN.md) để xác định mốc đang làm và [quy ước dữ liệu](references/allocation.md) trước khi ghi quyết định. Lệnh chỉ yêu cầu thiết kế kết thúc ở kế hoạch và skill. Lệnh pilot chỉ chạy phạm vi pilot. Lệnh triển khai đầy đủ cho phép đi tiếp tới bản release đã nghiệm thu.

## Nhận diện chất liệu trong sách

1. Làm việc ở gốc repo. Đối chiếu chín catalog trong `kaiwa_skill/planning/v6_3/coverage` và `hidden_speak_japanese` trong `planning/v6_4/admin` dưới kaiwa_skill. Tra chặng và tình huống trong JSONL V6.5. Ghim hash đầu vào. Đọc bài hoặc dải dòng từ Markdown clean một lần rồi tái dùng ghi chú khi bài có nhiều vị trí cũ. Mã pack cũ dùng để tìm nguồn.
2. Với mỗi đơn vị, đọc lời giảng, ví dụ tương phản, hội thoại và ghi chú cần thiết để hiểu người Nhật dùng cách nói đó khi nào. Tóm tắt ngắn bằng tiếng Việt hành động người nói, điều người nghe hiểu, quan hệ, sắc thái và trường hợp dễ dùng sai. Gắn vị trí đủ chính xác để sau này mở được toàn bộ kiến thức và ví dụ. Metadata cũ có thể gợi ý, chỉ ghi đã đọc sau khi thực sự mở nội dung.
3. Nhận diện phần có giá trị sư phạm bên trong bảng, lời dẫn, cặp thành ngữ, từ tượng thanh hoặc mục chung track. Nếu một đơn vị chứa nhiều mục đích nói khác nhau, tách liên kết theo tiểu mục/dải dòng và giữ đường dẫn về toàn đơn vị. Nếu một ý được giảng qua nhiều ví dụ liền nhau, giữ quan hệ giữa chúng. Danh mục học, lời dẫn sử dụng, giới hạn do thiếu trang và chỗ scan đáng ngờ đều có trạng thái riêng trong báo cáo.
4. Gợi ý khi tìm chức năng qua sách: B05 có vai nhân viên phục vụ, B18 có quan hệ trong/ngoài và chiều kính ngữ, B19 giúp mô tả bằng từ tượng thanh, B20 có cách nói cố định, B24 có cách diễn đạt cảm xúc. B07/B11 gợi ý vùng sau Sơ tới đầu Trung, B06/B12 gợi ý sau Trung tới Thượng. Đọc yêu cầu thực của từng mục để quyết định. B08 必須700 đã dùng cho shadowing topic V6.5 và nằm ngoài chín sách V7.

## Gom bài và chọn vị trí

- Viết thử một câu mục tiêu quan sát được, chẳng hạn *khi nghe lời nhờ chưa rõ phạm vi, người học biết hỏi lại mà vẫn thể hiện thiện chí*. Thử giải thích mỗi bài nguồn đóng góp gì cho mục tiêu. Có thể gom khác sách, khác bối cảnh hoặc giữ chuyên đề một sách khi bài gốc đã đủ mạch. Tên learner bằng tiếng Việt tự nhiên, diễn tả được việc người học làm được.
- Khi hai ứng viên cùng tên, đối chiếu vai, mức thân mật, hậu quả khi dùng sai và thao tác nghe–đáp. Gộp nếu học chung giúp thấy khác biệt cần thiết. Tách khi người học phải chuyển sang một năng lực khác hoặc một quan hệ vượt xa độ khó hiện tại. Chuyên đề sau được dùng lại nguồn nếu thêm một nhiệm vụ giao tiếp hoặc sắc thái có ý nghĩa. Ghi sự tiến triển trong quyết định nội bộ.
- Tra các chặng từng dùng bài và các chặng khác có tình huống thích hợp. Mở tình huống cụ thể, thử hình dung một lượt nói mà người học có thể dùng kiến thức mới. Ghi UID chặng cùng ID tình huống tại chặng. Một cụm từ giống nhau trong tiêu đề chưa đủ chứng minh hợp vị trí.
- Đặt chuyên đề trước lần vận dụng thích hợp, khi người học đã có đủ chất liệu để hiểu. So với chặng topic ngay trước và ngay sau. Nếu nhiều chuyên đề dồn trước cùng một chặng, đọc cả đoạn lộ trình để cân nhắc gộp, dời sang cơ hội dùng tiếp theo hoặc giữ thứ tự từ nền tảng tới tinh tế. Không ấn định nhịp cứ N topic thêm một chuyên đề. Tên cấp của sách chỉ giúp tìm ứng viên.
- Chặng topic có thể tham khảo chuyên đề đã học khi AI soạn hội thoại ở pha sau. Ghi gợi ý dạng *ở lượt nào, người nói có thể vận dụng điều gì*. Đây là liên kết biên tập tùy chọn. Các ví dụ nguồn của chuyên đề vẫn có thể thuộc nhiều chủ đề đời sống.

## Phân công và phục hồi

Khi được giao chạy nhiều worker, lượt đọc chia theo sách để giảm số lần đọc lại. Root đối chiếu ứng viên cả chín sách trước khi chia lượt bố trí theo level. Mỗi worker ghi vào phạm vi riêng. Root sở hữu registry, thứ tự xen chặng, build và Git. Lưu quyết định hoàn tất bằng tệp tạm rồi thay thế nguyên tử. Khôi phục bằng cách đối chiếu trạng thái và hash, làm tiếp phần còn thiếu hoặc bị ảnh hưởng.

Khi chỉnh một chuyên đề, dùng UID để tìm nguồn và các chặng vận dụng, cập nhật lý do và so lại các hàng xóm ở cả vị trí cũ lẫn mới. Khi nguồn thay đổi, rà các chuyên đề cùng tham chiếu nguồn đó. Dựng lại thứ tự và chỉ mục từ quyết định đã lưu.

## Nghiệm thu

Kiểm tự động theo [quy ước dữ liệu](references/allocation.md). Đọc duyệt theo ba chiều: mở từ sách để tìm kiến thức chưa có nơi dùng, mở từ chuyên đề để kiểm mạch học của các nguồn gộp lại, mở từ đoạn lộ trình để kiểm cơ hội vận dụng sớm. Ghi rõ phần nào đã kiểm bằng máy, phần nào đã đọc. Bàn giao vị trí và nguồn cho người thiết kế nội dung chuyên đề. Video, cách triển khai shadowing bên trong chuyên đề, TTS và hội thoại mới thuộc lượt thiết kế nội dung riêng.
