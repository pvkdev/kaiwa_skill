---
name: jlpt-exam-editorial
description: Biên tập lời giải, dịch câu hỏi và đối chiếu từng câu Nhật–Việt cho passage hoặc script của một kỳ JLPT. Dùng khi có HTML, ảnh, khóa nguồn hoặc bản nghe đã xác minh và cần bổ sung nội dung học vào gói Harumi.
---

# Biên tập câu hỏi và tài liệu dùng chung

Nhận cấp/kỳ, revision, SHA của nguồn, UUID/locator và tệp được phép sửa. Mở nguyên văn Nhật, lựa chọn theo thứ tự, dấu đánh đáp án, lời giải nguồn, tư liệu dùng chung và hình liên quan. Với nghe, đối chiếu lời thoại hoặc master ở đúng khoảng câu. [Quy tắc lời giải và ví dụ](../jlpt-exam-ingest/references/editorial.md)

## Các trường cần dịch

- Dùng N2 2018/12 hoặc N3 2025/12 làm mẫu cho cùng loại câu. Dịch câu dẫn có nội dung học, câu hỏi đọc hiểu, phương án là câu trả lời mang nghĩa và các câu ví dụ kiểm tra cách dùng từ. Giữ bản dịch đã có của nguồn nếu đúng. Với bài chọn cách đọc/chữ, phần Nhật trước đáp án vẫn phải giữ chính xác mục tiêu cần kiểm tra. Các số lựa chọn, vị trí lỗ trống như `[48]`, câu hỏi nghe chỉ có ảnh, dòng trống và ký hiệu thuần túy không cần tạo bản dịch giả.
- Bản Việt dùng sau khi nộp bài. Với câu điền khuyết, xếp từ hoặc đoạn có nhiều ô trống, điền đáp án đúng của từng câu trước khi dịch để câu Việt trọn nghĩa. Giữ bản Việt nguồn đã dịch đúng theo cách này. Giữ nguyên ký hiệu và thứ tự mảnh trong đề Nhật để làm bài và để neo bản dịch JAVI vào đúng câu.
- Với prompt có cả bảng và câu hỏi, giữ từng ô, tiêu đề, đơn vị, hướng đọc, dòng chú thích và dấu gạch chân. Lấy số câu hiển thị từ node annotation. Các số trùng ở phần khác là hợp lệ.
- Lưu dịch câu hỏi vào `prompt.textVi` và đồng bộ `translationVi` theo gói hiện tại. Lưu dịch lựa chọn vào `choices[].textVi`. Lời giải ghi riêng trong `explanation`. Bản Việt chưa đủ căn cứ để trống và ghi issue.

## Tách câu cho Đọc hiểu và Nghe hiểu

1. Tìm đúng target. Passage hoặc audio chung lấy UUID của media. Script riêng lấy UUID câu hỏi. Một đoạn chung nhiều câu dùng một bộ hàng.
2. Ghép anchor tooltip hoặc phụ lục vào chính câu gốc. Đối chiếu với JA hiển thị, bỏ ruby trợ đọc và markup điều khiển. Giữ thứ tự đoạn, tên người nói, điều kiện, phủ định, câu hỏi nhắc lại và số liệu. Nếu một lượt lời có ba câu, tách ra ba hàng và dịch đúng nghĩa từng câu. Gắn nhãn người nói với chính lời nói đó. Dấu câu nằm trong trích dẫn cần đọc theo ngữ cảnh. Hàng bảng và tiêu đề có thể là một đơn vị cấu trúc.
3. Ghi `annotations.sentencePairs[targetId] = [{ja,vi}, ...]`. Giữ nguyên văn Nhật ở trường JA đầy đủ. VI toàn đoạn luôn là các bản Việt theo thứ tự, nối bằng xuống dòng. Khi thiếu nghĩa của một hàng, giữ hàng Nhật và `vi:null` trong draft, đưa target và số hàng vào checklist. Tránh lặp cả đoạn Việt vào từng hàng. Đối chiếu toàn bộ ký tự có nghĩa trong JA đầy đủ với các hàng JA.
4. Khi nguồn đã có bản dịch cả đoạn, dùng nó kiểm tra thuật ngữ và đại từ, rồi biên tập lại theo câu. Khi chỉ có tiếng Nhật, AI tự dịch và ghi provenance. Nếu nguồn thiếu cả script, chuyển [worker nghe](../jlpt-listening/SKILL.md) từ đúng audio tổng trước khi soạn lời giải.

## Lời giải và bàn giao

Trước khi bàn giao, dựng thử JA, VI và JAVI theo [quy ước bố cục và nhãn nhân vật](../../../contracts/v1/CONTRACT.md#bố-cục-song-ngữ-và-nhãn-nhân-vật-quy-ước-biên-tập-13). Đọc hai bản theo từng đoạn, lượt thoại, tiêu đề, hàng bảng và chú thích. Ví dụ một lượt hai câu có hai hàng: `{"ja":"田中：はい。","vi":"**Tanaka**: Vâng."}` rồi `{"ja":"明日行きます。","vi":"Ngày mai tôi sẽ đi."}`. Đặt nhãn đúng ở câu mở đầu lượt; giữ nguyên chính tả tên trong bản Nhật và chỉ đậm tên trước dấu hai chấm. Dùng quy ước này cho cả script riêng, script chung và hội thoại trong bài đọc. Phân biệt nhãn nhân vật với giờ hẹn, URL, nhãn trường thông tin. Bản nháp thiếu dịch dùng `vi:null` và ghi đúng UUID, số hàng.

Chép nguyên văn toàn bộ lời giải từ HTML hoặc phụ lục đúng câu, kể cả khi chỉ có một câu ngắn. Đối chiếu trong cùng phần viết hoặc nghe, vì hai phần có thể cùng dùng `#q-1`. Chỉ giữ tiêu đề, thứ tự và nội dung có trong nguồn (`origin=source`). Khi nguồn thiếu, đọc ví dụ VNJPClub cùng dạng ở [hướng dẫn lời giải](../jlpt-exam-ingest/references/editorial.md), rồi viết đoạn giải thích từ bằng chứng riêng của câu (`origin=ai`). Nếu khóa hoặc lời giải mâu thuẫn với đề, lưu các bằng chứng và ghi issue theo UUID.

Ghi trường đã thay đổi, pointer, hash đầu vào, nguồn/tên model và người rà theo [hợp đồng](../../../contracts/v1/CONTRACT.md). Giữ lời giải nguồn đọc lại được từ HTML. Nộp patch với base revision, target UUID và locator. Mở lại JA, VI và JAVI ở summary để kiểm câu/dòng, lời dịch thiếu, dấu ngoặc và bố cục bảng. Giao file sau cùng cùng phạm vi đã kiểm cho [jlpt-exam-review](../jlpt-exam-review/SKILL.md). Khi UI chưa sẵn sàng, ghi rõ phần đã kiểm trên dữ liệu và phần còn chờ preview.
