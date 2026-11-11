# Nghiệm thu phạm vi PDF — 必須700

Đã nhận đủ 208 trang vật lý, 8 chương, 110 unit. Writer mở và rà toàn nguồn; root đối chiếu 26 trang mẫu được liệt kê trong JSON. Đây không phải rà ngữ nghĩa độc lập toàn sách.

Root kiểm trọn bốn cột Features of the Japanese Spoken Language, toàn bảng Basic phrases 70, các mẫu bài ở Part1/2/4/5 và phần hướng dẫn/ấn bản. Đã đọc lại các sửa về cue romaji, nghĩa ví dụ ngắn trong advice, phạm vi thời gian, cách viết kana và số trang tra cứu. Bảng có đủ 35+35 hàng; mục はじめまして giữ số29 mà chỉ mục in, đồng thời dẫn vị trí thật27 đã xác nhận bằng PDF26/28. Cue any/other in lạc ở177 được lưu nguyên văn trong metadata và có coverage excluded riêng; không dùng để dựng câu Nhật.

Sau handoff, root sửa đúng một câu ở advice28: nguồn nối hai ví dụ English bằng “or”, nên giữ hai ví dụ thay thế thay vì tự gán một cuộc hỏi đáp. Root mở toàn PDF28, kiểm lại các câu mẫu, refresh checkpoint28/chương2 và build/validate lại. Hash handoff và hash sau sửa đều được ghi trong JSON; các nội dung chương khác không đổi. Chi tiết QA tại clean/reviews/essential700-root-sampled.md.

Kiểm đếm đầu ra xác nhận 91 bài, 727 ô prompt và 727 hàng mẫu Nhật tương ứng; không lấy nhan đề700 làm số câu. Một hàng có thể gồm các cách nói/lượt thoại, nên đây là số hàng luyện, không phải số câu ngôn ngữ học. Audio có haiCD,91 cặp mã bài học CD-1/2–46 vàCD-2/1–46; guide12 lặpCD-1/6 được ghi riêng, không cộng mã độc nhất. Không suy nội dungCD-1/1. Tệp nghe thực tế not_checked, chưa tìm/tải.

Nguồn còn hai giới hạn: trang in2 của lời đầu vắng khỏi PDF; colophon207 ghi 平成30年（2019年）4月10日 không nhất quán. Không dựng phần thiếu hoặc tự chọn một năm xuất bản. Root validate --allow-source-issues đạt0lỗi/4cảnh báo cho hai vấn đề này. Có206pages/6chapters/108units checked và2pages/2chapters/2units needs_review; khôngpending/draft/stale. Toàn phạm vi là toànPDF được cung cấp, không chứng nhận nguồn hoàn hảo.
