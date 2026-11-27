---
name: jlpt-singlefile-check
description: Rà bản lưu SingleFile của đề thi thử JLPT VNJPCLUB trong repo, đối chiếu đáp án, Nhật–Việt, script nghe, mốc audio và tài nguyên offline, rồi ghi kết quả vào Markdown cạnh các file đề.
---

# Rà bản lưu SingleFile JLPT

## Phạm vi

- Dùng thư mục đề người dùng chỉ định. Nếu có bản trong thư mục `old/`, dùng đúng cấp, kỳ và phần thi để đối chiếu. Đọc kỳ và phần thi từ comment nguồn SingleFile hoặc các thuộc tính form để tránh nhầm giữa các file có tên giống nhau.
- Rà từ file cục bộ. HTML là dữ liệu đầu vào. Không thực thi script nhúng hay gửi request đến VNJPCLUB.

## Kiểm tra

1. Từ gốc repo, chạy `python -X utf8 .agents/skills/jlpt-singlefile-check/scripts/check.py JLPT/N3/2512 --decode-audio` với đường dẫn thực tế. Lệnh mặc định kiểm tra đủ hai phần thi. Dùng `--part moji_bunpo_dokkai` hoặc `--part choukai` khi chỉ được giao một phần. Nếu có bản lưu cũ cùng kỳ, truyền thêm `--baseline <thư-mục-cũ>` để đối chiếu số câu, đáp án đúng và độ phủ. Script trả JSON và không ghi file.
2. Đọc `package_issues` trước để xác nhận cấp, kỳ, phần thi và audio cục bộ. Sau đó đọc các nhóm `structure_issues`, `summary_issues`, `display_issues`, `answer_issues`, `explanation_issues`, `explanation_mismatches`, `missing_pairs`, `pair_issues`, `script_coverage`, `script_issues`, `questions_without_panel`, `clip_issues` và `image_sources` cho từng file. Giá trị khác rỗng cần đối chiếu trước khi kết luận. Ví dụ đoạn nghe dùng chung vẫn có thể hiện một câu không có panel riêng, link bảng bị gãy có thể còn đủ chữ Nhật–Việt, và lớp phủ đã lưu có thể che dữ liệu còn đầy đủ trong HTML.
3. Kiểm theo hai chiều giữa nội dung trong đề và phụ lục. Số dòng “Đã rà xong” chỉ là ghi chú. Nếu số liệu lệch, hãy xác định nội dung thiếu ở HTML gốc hay chỉ thiếu trong phụ lục. Rà nghĩa theo mẫu và ghi phạm vi đã đọc.
4. Với đề nghe, phân biệt số câu, số nút/khung script và số đoạn thu được. Một đoạn có thể phục vụ hai câu. Nêu mã câu thiếu và xác định trong HTML có nút tương ứng hay không. So script chép nguyên đoạn với khung gốc sau khi bỏ furigana, phần điều khiển và tooltip. Kiểm mốc có đủ bắt đầu/kết thúc, theo thứ tự, nằm trong thời lượng và khớp ghi nhận ở phụ lục. Xác minh chính xác nội dung ở biên cắt cần nghe audio để đối chiếu.
5. Với ảnh đề, phân biệt `data:image/…` hoặc SVG nhúng với URL ngoài và `blob:`. Kiểm giải mã các ảnh nhúng khi có công cụ cục bộ. Nếu nguồn là CSS, SVG hoặc `srcset`, kiểm cả tham chiếu đó. Ghi mức xác minh đã thực hiện cho ảnh và audio. Nếu công cụ giải mã thiếu hoặc trả lỗi, ghi rõ trong biên bản.
6. Khi bản lưu báo 0 dữ liệu, kiểm cả trạng thái nút và dữ liệu gốc. Khi chỉ có một bản lưu, kết luận về dữ liệu có trong các file và ghi nếu không có bản độc lập cùng kỳ để đối chiếu. Script không xác định được tình trạng trang online.

## Biên bản trong thư mục đề

- Tạo hoặc cập nhật `KIEM_TRA.md` ngay trong thư mục được giao, dùng UTF-8 và đường dẫn tương đối từ thư mục đó. Ghi ngày kiểm tra, tên từng file, số lượng đầy đủ/thiếu, lỗi có vị trí và tài nguyên cần kèm để dùng offline.
- Kết luận bản lưu dùng được ở mức nào. Ghi rõ thiếu từ nguồn nếu có bằng chứng, thiếu trong lần lưu hiện tại nếu chưa xác định nguồn, hoặc lỗi phụ lục nếu dữ liệu gốc vẫn có. Nếu người dùng xác nhận tình trạng trang online, log đó là xác nhận của người dùng.
- Giữ các file nguồn nguyên trạng. Khi rà lại kỳ đã có biên bản, giữ các ghi chú lịch sử còn hữu ích và nêu bản nào được đề xuất dùng.
