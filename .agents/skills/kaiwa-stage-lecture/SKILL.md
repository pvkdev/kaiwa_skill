---
name: kaiwa-stage-lecture
description: Soạn và nghiệm thu bài giảng Markdown V14 cho một chặng topic Kaiwa, truy ngược về chương sách trong knowledge và xuất một node gồm bài đọc cùng chỗ dành cho video.
---

# Bài giảng chặng Kaiwa

## Chọn điều người học cần hiểu

Đọc mục tiêu, sự kiện, tất cả tình huống và hội thoại V11, các nhóm từ V12 đã duyệt, câu shadowing V13 của chính chặng. Ưu tiên checkpoint V13 trong `stages`, dùng pilot đã duyệt nếu phần sản xuất chưa sẵn sàng. Kiểm checkpoint tương ứng trước khi dùng. Tìm ở hồ sơ biên tập V11 trong `planning/v11/stages/<code>` hoặc `pilot/<code>` các mã nguồn, ghi chú và dữ kiện đã kiểm. Cân nhắc gối đầu chặng chuyên đề nếu thực sự giúp người học.

Hình dung người học trước buổi luyện và lúc sắp gặp việc thật ở Nhật. Gom các cảnh có chung một quyết định. Lập bản đồ các nhóm sự kiện vào các mục sẽ giảng để phát hiện khoảng trống. Mỗi mục giải đáp một điều người học cần biết để hành động: cần chuẩn bị hay nói rõ điều gì, nghe ra dấu hiệu nào, hiểu sai thì hỏi lại ra sao, có những hướng xử lý nào và khi nào có thể kết thúc. Chọn thứ tự, số mục và độ dài theo chủ đề. Bài di chuyển đi theo hành trình, bài tình cảm có thể đi theo điều người nghe cần, bài họp có thể đi theo mức độ chắc chắn của quyết định.

## Truy nguồn và biên soạn

Dùng `kaiwa_skill/planning/catalog27/manifest.json` để giải mã sách, rồi mở trực tiếp phần liên quan của Markdown trong `kaiwa_skill/knowledge`. Lần theo con trỏ V11 trước, tìm thêm qua mục lục/rg khi cần. Đọc cả giải thích và ngữ cảnh của ví dụ. Xác định ý nào có căn cứ trong sách, ý nào do người viết tổng hợp cho chặng. Số sách dùng do nội dung quyết định. Mẫu do AI viết không gán là lời sách. Quy trình hay dữ kiện có thể thay đổi (chi phí, quy định, thủ tục địa phương) cần nguồn chính thức, địa bàn/phạm vi, ngày kiểm tra; hoặc dạy cách hỏi khi tại chỗ. Không suy ra quy tắc toàn Nhật từ một ví dụ.

Viết tiếng Việt tự nhiên, hướng thẳng tới người học. Dạy cách hiểu lời đối phương và cách đáp phù hợp. Đan từ, ngữ pháp và sắc thái quan hệ vào đúng quyết định cần dùng. Ví dụ Nhật–Việt đủ cặp, vừa sức; có thể chọn từ hội thoại chặng hoặc tự soạn để làm rõ một điểm. Độ khó đến từ việc người học phải xử lý trong giao tiếp. Bài đọc đứng độc lập với video, kết bằng vài điều đủ ngắn để tra ngay trước khi dùng. Trong phần hiển thị, bỏ mã, nguồn, tên sách, nhãn cấp, thuật ngữ sản xuất và hướng dẫn biên tập. Không đặt bài thi, điểm hoặc điều kiện mở bài.

## Định dạng pilot

Tại `kaiwa_skill/planning/v14/pilot/<code>/` soạn hai tệp UTF-8:

- `lesson.md` là bản đọc hoàn chỉnh. Dùng một tiêu đề H1, các mục H2, đoạn văn, danh sách gạch đầu dòng và nhấn mạnh Markdown khi cần. Viết mỗi ví dụ thành hai dòng trích dẫn liền nhau: dòng đầu `> câu Nhật`, dòng sau `> bản dịch Việt`. Chừa dòng trống giữa các cặp. Câu Nhật hoàn chỉnh để trong cặp; từ hoặc mẫu ngắn có thể nằm trong lời giải thích.
- `sources.json` là metadata nội bộ. Object có `code` và `sections` là mảng. Mỗi mục `{heading, scene_ids, sources}` khớp đúng một H2; các scene_ids hợp lại bao phủ tình huống V11 theo nội dung thực sự giảng. Mỗi nguồn sách dùng `{book_id, book_title, path, start_line, end_line, use_vi}` với tên từ manifest, đường dẫn Markdown tương đối từ gốc repo, số dòng bắt đầu/kết thúc tính từ 1, ghi rõ ý đã rút ra. Nguồn web dùng `{url, title, checked_on, use_vi}`. Ghi thêm `example_notes` ở cấp bài hoặc mục để phân biệt câu giữ nguyên/chuyển từ sách, câu dùng lại từ V11/V13 và ví dụ tự viết. Mục tổng kết có thể không có nguồn riêng. Không xuất metadata biên tập lên phần học.

Rà bài bằng một nhánh khó: chỉ đọc bài, người học có nhận biết tín hiệu, chọn hành động tiếp theo, nói được câu phù hợp không? Đọc riêng tiếng Việt và các cặp ví dụ, kiểm người nói, người nghe, ý định, mức lịch sự và độ chắc chắn. Người duyệt mở lại đoạn nguồn để kiểm chứng các ý chính và rà những cảnh tuy có mã nhưng chưa được giảng. Điều phối dựng `lecture.json` và HTML từ Markdown đã duyệt; node có section đọc và video trạng thái planned. Khi cập nhật, biên tập Markdown rồi dựng lại. Từ gốc repo dùng `py -B -X utf8 tools/roadmap_v14.py` để dựng preview cho ba pilot; thêm `--update-site` để cập nhật cả node trên `docs/index.html` khi đã duyệt. Chờ nội dung video ở giai đoạn riêng.
