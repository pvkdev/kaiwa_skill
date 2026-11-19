---
name: kaiwa-stage-lecture
description: Soạn và rà bài đọc V14 dạy cách nói tiếng Nhật theo tình huống, lựa chọn từ và mẫu câu, nghe để đáp và duy trì cuộc thoại. Truy ngược kiến thức về chương sách để xuất node Markdown của chặng.
---

# Bài giảng chặng Kaiwa

## Đích của một bài

Soạn một bài dạy nói bằng tiếng Việt. Khi bước vào hội thoại, người học biết mở miệng bằng câu nào, vì sao dùng từ và cấu trúc đó, nghe lời đáp rồi tự nói được lượt kế tiếp. Lấy một cảnh tiêu biểu làm điểm tựa ngay đầu bài. Viết như đang kèm một người tập nói: cho họ nghe câu Nhật dễ dùng, giải thích một lựa chọn đáng học rồi cho họ thử chuyển sang ý khác. Các mục nối với nhau theo việc người học làm *bằng lời*. Chọn mạch hợp với chủ đề: xin nói xen và xác nhận, đón cảm xúc rồi để người kia chọn, hoặc ghi nhận một phần trước khi nêu ý kiến khác. Độ dài theo điều đáng giảng.

## Đọc nguồn theo câu hỏi ngôn ngữ

Đọc mục tiêu và mọi nhánh hội thoại V11, từ V12 đã duyệt và shadowing V13 của chính chặng. Kiểm checkpoint V13 trong stages, dùng bản pilot đã duyệt khi chưa có bản sản xuất. Xem hồ sơ nghiên cứu trong `planning/v11/stages/<code>` hoặc `planning/v11/pilot/<code>`. Từ các từ, mẫu câu và vấn đề ngữ dụng nổi bật, lần con trỏ qua `planning/catalog27/manifest.json` về đúng đoạn Markdown trong `kaiwa_skill/knowledge`. Mở cả ví dụ, lượt đáp và lời giải thích. Phân biệt ý sách dạy với ví dụ hoặc nhận xét mình phát triển. Gối đầu một mẫu từ chuyên đề cũ khi hợp. Chỉ đưa chi tiết thực tế vào nếu nó làm thay đổi câu phải nói hoặc cách hiểu lời đáp. Chi tiết thủ tục biến động cần nguồn chính thức có phạm vi áp dụng.

## Cách chọn chất liệu và triển khai

- Rút từ các cảnh ra vài việc nói có thể dùng lại ở nhiều nhánh. Mở bằng một trao đổi ngắn hoặc đặt ngay người học vào lượt nói đầu tiên. Cho thấy trình tự của cuộc nói bằng lời thật của cả hai vai. Đặt chỉ dẫn vai ở đoạn văn trước ví dụ nếu cần. Mạch hội thoại có thể ngắn, dừng đúng chỗ đáng phân tích.
- Giảng từ và ngữ pháp ở nơi người học phải **chọn cách nói**. Khi hai từ gần nghĩa dễ dùng lẫn, hoặc hai mẫu đều đúng nhưng gợi hai phản ứng khác nhau, đặt cặp ví dụ sát nhau, giải thích ngắn điều đổi về nghĩa, quan hệ hay mức cam kết. Viết rõ phần nào của khung câu có thể thay; cho ít nhất một cách nói hoàn chỉnh sau khi đổi. Tránh suy từ một cặp ví dụ ra quy tắc tuyệt đối. Chỉ giải thích điểm ngữ pháp đủ giúp dùng được câu trong chặng.
- Có luyện **nghe để đáp**: đưa ra lời người đối diện có thể thật sự nói, chỉ ra tín hiệu cần bắt, rồi cho lời đáp phù hợp. Dùng một ngã rẽ có hậu quả giao tiếp, chẳng hạn cùng một lời mở nhưng người kia từ chối, đồng tình một phần hoặc cần thêm thông tin. Khi hiểu nhầm, dạy chính câu để sửa hoặc nối lại cuộc nói. Chọn chỗ hữu ích để luyện nhịp ngắt, từ đệm, cuối câu, hoặc lược bỏ thành phần đã rõ.
- Dùng một lượt tự luyện ngắn ở chỗ có thể chuyển một mẫu đã biết sang ý mới. Nêu hoàn cảnh khác và mời người học nói trước khi xem một cách đáp khả dĩ. Đây là lời mời tập nói tự do, không chấm, không khóa bài. Phần kết giúp người học tự ráp lại mạch nói, thay vì liệt kê việc phải làm ngoài đời.
- Điều chỉnh theo cấp và vị trí. Với người mới, ưu tiên một ý trong một lượt, từ cụ thể và mẫu dễ thay. Khi tăng độ khó, cho thấy lựa chọn giọng theo quan hệ, thông tin được lược, hàm ý, cách phản biện hoặc sửa lời. Không bắt các bài mang cùng số mục, số mẫu, số ví dụ hay cùng một dàn bài. Giữ tên cấp, sách, mã nguồn và chỉ dẫn biên tập ở metadata nội bộ.

## Định dạng pilot

Tại `kaiwa_skill/planning/v14/pilot/<code>/` soạn hai tệp UTF-8:

- `lesson.md` là bản đọc hoàn chỉnh. Dùng một tiêu đề H1, các mục H2, đoạn văn, danh sách gạch đầu dòng và nhấn mạnh Markdown khi cần. Viết mỗi ví dụ thành hai dòng trích dẫn liền nhau: dòng đầu `> câu Nhật`, dòng sau `> bản dịch Việt`. Chừa dòng trống giữa các cặp. Câu Nhật hoàn chỉnh để trong cặp; từ hoặc mẫu ngắn có thể nằm trong lời giải thích.
- `sources.json` là metadata nội bộ. Object có `code` và `sections` là mảng. Mỗi mục `{heading, scene_ids, sources}` khớp đúng một H2; các scene_ids hợp lại bao phủ tình huống V11 theo nội dung thực sự giảng. Mỗi nguồn sách dùng `{book_id, book_title, path, start_line, end_line, use_vi}` với tên từ manifest, đường dẫn Markdown tương đối từ gốc repo, số dòng bắt đầu/kết thúc tính từ 1, ghi rõ ý đã rút ra. Nguồn web dùng `{url, title, checked_on, use_vi}`. Ghi thêm `example_notes` ở cấp bài hoặc mục để phân biệt câu giữ nguyên/chuyển từ sách, câu dùng lại từ V11/V13 và ví dụ tự viết. Mục tổng kết có thể không có nguồn riêng. Không xuất metadata biên tập lên phần học.

Nghiệm thu bằng cách đóng hai vai ở một nhánh khó và chuyển một chi tiết sang cảnh khác. Từ bài đọc, người học có nói được một câu mở, nghe ra chỗ cần phản hồi, tự thay từ/mẫu và nói tiếp đúng vai không? Với đoạn chủ yếu hướng dẫn di chuyển, tổ chức công việc hoặc ứng xử, giữ lại bối cảnh tối thiểu và dạy lượt lời cụ thể. Rà riêng các cặp sắc thái và bản Việt để không biến lời ngỏ ý thành mệnh lệnh hoặc câu hỏi thông tin. Đọc riêng tiếng Việt và các cặp ví dụ, kiểm người nói, người nghe, ý định, mức lịch sự và độ chắc chắn. Người duyệt mở lại đoạn nguồn để kiểm chứng các ý chính và rà những cảnh tuy có mã nhưng chưa được giảng. Điều phối dựng `lecture.json` và HTML từ Markdown đã duyệt; node có section đọc và video trạng thái planned. Khi cập nhật, biên tập Markdown rồi dựng lại. Từ gốc repo dùng `py -B -X utf8 tools/roadmap_v14.py` để dựng preview cho ba pilot; thêm `--update-site` để cập nhật cả node trên `docs/index.html` khi đã duyệt. Chờ nội dung video ở giai đoạn riêng.
