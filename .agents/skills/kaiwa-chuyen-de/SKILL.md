---
name: kaiwa-chuyen-de
description: Lập kế hoạch và tuyển bài đã đọc từ bảy sách Speak Japanese để đặt chuyên đề trước các cụm topic trên nền V8. Dùng khi chọn vị trí, rà nguồn, pilot hoặc điều chỉnh một chuyên đề cho lộ trình hiện hành.
---

# Tuyển chuyên đề cho lộ trình Kaiwa

Đọc thứ tự topic, sự kiện và tình huống trong `kaiwa_skill/planning/v8/KAIWA_CHANG_V8.jsonl`. Giữ nguyên UID, thứ tự và nội dung của 289 topic. Làm theo phạm vi của lượt giao việc (thiết kế, pilot hoặc phân bổ). Bản V7 và danh mục pack cũ có thể giúp tìm kiếm. Mọi quyết định đưa nội dung vào bài dùng bản Markdown trong `kaiwa_skill/knowledge/<tên sách>/book.md`.

## 1. Tìm nơi người học cần chuyên đề

Đi theo thứ tự từng cấp. Mở đầu cấp bằng 2–3 topic và kết thúc bằng topic. Đọc qua ranh giới các cụm lớn, rồi đọc tình huống trong khoảng ba topic ngay sau mỗi điểm dự kiến chèn. Ghi lại người học đang nói với ai, cần nghe ra điều gì, đến lượt mình dễ bí ở đâu. Chọn một việc các tình huống có thể cùng luyện và đặt tên chuyên đề bằng tiếng Việt theo việc đó.

Lấy trung bình khoảng bốn topic cho một chuyên đề làm mốc xem toàn tuyến. Có thể đặt sớm khi một cụm mới cần kiến thức ngay, hoặc để xa hơn khi vài topic đang tiếp nối cùng một kỹ năng. Xét cả ba topic kế tiếp, ghi các tình huống dùng được thật và giải thích ngắn nếu phạm vi chỉ đến một phần cụm. Khi khó tìm ứng dụng, thử dời điểm chèn hoặc bỏ đề xuất. Số 72, số chặng từng cấp, khoảng cách và số mẫu mỗi chặng đều là ước lượng.

## 2. Tìm bài trong đúng bảy sách

- **Mẫu câu hội thoại** — B11 基本文型88 và B12 発展文型125. Tìm theo chức năng của mẫu trong lượt lời. Đọc cả hội thoại và phần phân biệt sắc thái. Hai tiểu từ gần nghĩa có thể đủ thành một chuyên đề nếu việc phân biệt chúng cần luyện ở nhiều vai.
- **Cụm ngắn dùng ngay** — B07 超ミニフレーズ200 và B06 発展210. B07 có nhóm chức năng, B06 tra theo âm kana. Đọc các cặp lời để nhận ra cùng một câu có thể là lời cảm thán, lời đáp xã giao hoặc một lời từ chối, tùy câu đi trước.
- **Kính ngữ** — B18 基本表現85. Chỉ tuyển từ ba chương Part 1 基礎編 (丁寧語・美化語, 尊敬語, 謙譲語・丁重語). Có 19 + 25 + 31 = 75 mục đánh số. Mục 14 存じる②（思う） ở nhóm 謙譲語 chỉ còn dấu vết trong mục lục, thiếu thân bài. Ghi thiếu nguồn. Part 2 có cả phần theo chức năng và theo tình huống, nằm ngoài phạm vi chuyên đề này. Khi đọc Part 1, xác định ai thực hiện hành động, ai nghe, ai được nhắc tới và người học cần hiểu hay cần tự nói cách đó.
- **Quán ngữ** — B20 お決まり表現180. Đọc tình huống để phân biệt biểu đạt người học có thể chủ động dùng với lời mang tính đánh giá, mỉa mai hoặc chỉ cần nghe hiểu.
- **Truyền đạt cảm xúc** — B24 気持ちが伝わる 基本表現180. Dùng 19 phần A–S để tìm, đọc hai biểu đạt trong Unit và giữ phần đối chiếu khi nó giúp lựa lời. Có thể nối hai phần như lo lắng và an tâm nếu tình huống sau chuyên đề cần cả hai.

Năm nhóm trên là cách tìm bài. Một chuyên đề có thể dùng một hoặc vài nhóm. B19 onomatope và các sách ngoài danh sách vẫn thuộc kho kiến thức chung của dự án.

## 3. Đọc rồi mới chọn

1. Dùng mục lục, tiêu đề, anchor hoặc tìm kiếm để lập danh sách ứng viên. Với **từng đoạn định đưa vào**, mở và đọc hết bài chứa đoạn đó, gồm các ví dụ, vai và ghi chú liên quan. Xem cả ranh giới đầu–cuối và những tiểu mục lồng bên trong. Tiêu đề khớp, kết quả tìm kiếm, hash hay trạng thái đã đọc ở V7 đều chưa đủ để chọn.
2. Giữ phần dạy một cách nghe/nói cụ thể, ví dụ cần thiết và ngữ cảnh giúp hiểu đúng lời Nhật. Với hội thoại, giữ đủ lời dẫn và lời đáp để hiểu ý. Nếu chỉ một phần bài phù hợp, ghi đúng phạm vi đã chọn. Rà cả chương để phát hiện các bài có giá trị dễ bị bỏ qua vì tiêu đề khác từ khóa topic.
3. Loại lời tựa, lời giới thiệu sách, hướng dẫn dùng sách/CD, quảng bá, mục lục, chỉ mục, đáp án, thông tin xuất bản, thẻ kỹ thuật và chú thích biên tập. Một bài trong phần nhập môn có thể có kiến thức nói thật. Đọc và lấy đúng đoạn dạy kiến thức đó. Ví dụ minh họa bố cục trang phải được tìm lại ở bài chính trước khi cân nhắc dùng. Với đoạn thiếu, lỗi hoặc chỉ còn đáp án, ghi nhận tình trạng và để ngoài bài học.
4. Với từng phần chọn, lưu nội bộ mã và tên sách, file cùng anchor hoặc dải dòng, dấu vân tay của nguồn, một câu tóm tắt về cách dùng **rút ra sau khi đọc**, và tình huống V8 sẽ dùng được. Đường dẫn nguồn và ghi chú QA chỉ dành cho quản trị. Khi chuyển giao cho bước soạn, chỉ chuyển các đoạn đã chọn sang phần học viên.

## 4. Cân tải và tránh dạy trùng

Xếp phần người học cần chủ động nói trước. Cân nhắc thêm biến thể nghe hiểu, ví dụ đối chiếu hoặc một cặp lời khác vai. Một mẫu có ba sắc thái có thể nặng hơn vài câu đáp ngắn. Dừng khi người học đã có đủ chất liệu cho cụm topic kế tiếp hoặc khi nội dung mới đòi một mục tiêu nói riêng. Thử đổi vị trí hoặc tách chuyên đề khi dạy gộp làm mờ điểm khác biệt.

Tra các biểu đạt đã chọn ở những sách và chặng khác. Nếu cùng cách nói, ý và vai, chọn nơi dạy chính. Giữ thêm ví dụ hoặc cho xuất hiện lại khi có nét nghĩa, quan hệ hoặc lượt đáp mới đáng học. Lưu lý do ngắn. Mục đã đọc nhưng trùng, quá chuyên biệt hoặc chưa có nơi hợp lý có thể để dành. Chỉ báo tỷ lệ đọc/tuyển trên phạm vi thực sự kiểm kê.

## 5. Bàn giao và nghiệm thu

V9 chạy theo [hợp đồng worker](../../../kaiwa_skill/planning/v9/WORKER_CONTRACT.md). Root dùng `py -X utf8 tools/roadmap_v9.py` để dựng bản review từ các decision. Sau khi đọc rà và kiểm preview, chạy cùng lệnh với `--publish` để cập nhật con trỏ hiện hành và trang docs. Checkpoint mỗi cấp nằm trong planning/v9/work, quyết định và nội dung học viên nằm trong planning/v9/decisions. Dùng registry UID topic V8 và UID chuyên đề sinh ổn định từ key, giữ nguyên key khi sửa.

- **Bước lập bản đồ** tạo danh sách điểm chèn theo cấp, UID topic liền sau, tên tạm, mục tiêu nói và các tình huống làm căn cứ. Ở bước này có thể nêu hướng tìm nguồn. Chỉ đánh dấu bài nguồn đã chọn sau bước đọc.
- **Bước pilot** thử cụm có tình huống thực từ mỗi cấp khi được giao. Bàn giao cho từng chuyên đề một phiếu gồm vị trí, việc sẽ nói được, tình huống hỗ trợ, danh sách phần chọn theo thứ tự, trọng tâm/biến thể và dẫn nguồn nội bộ. Mở phần học viên để so với phiếu, xem người học có hiểu khi tách khỏi sách và có gặp lại đúng việc đó trong các topic sau hay không.
- **Bước phân bổ toàn tuyến** lưu tiến độ sau từng cụm. Phân biệt ứng viên chưa đọc, đã chọn, đã đọc để dành, trùng, tài liệu phụ và nguồn thiếu. Có thể ghi một quyết định cho cả phần phụ liên tục. Khi tiếp tục, chỉ mở lại phần đang dở hoặc nguồn đã thay đổi. Trước bàn giao, rà từng sách để tìm kiến thức còn dùng được, đối chiếu các chặng liền kề để gộp/tách và báo phân bố, khoảng cách, lý do để dành. Kiểm 289 UID topic theo đúng thứ tự V8, nguồn của mọi phần đã chọn và nội dung thực trong preview. Kiểm đếm hoặc quét từ khóa chỉ hỗ trợ lượt đọc biên tập.
