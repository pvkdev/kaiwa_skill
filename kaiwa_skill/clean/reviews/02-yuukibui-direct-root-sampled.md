# Nghiệm thu phạm vi PDF đầu vào

Bản direct đủ148trang,21chương,143unit. Tác giả mở từng ảnh và sauQA đã rà lại toàn chú từPDF8–147, giữ headword/dạng từ điển, nghĩaViệt và mã bài; PDF148 trắng. Mọi page/chapter checkpoint current, khôngdraft/pending/stale. Rootbuild và validator0.4.6:0lỗi/0cảnh báo.

Root đọc toàn chương12 và mở5trang mẫu86/89/90/91/92: đối chiếu mẫu5–6 tại86, khung6lượt cùng4tìnhhuống/cue/B₃ tại89–90, gloss phục hồi tại86/90 và20headword tại91–92. Sửa sắc thái非過去 củaつい…てしまうんです thành hay vô ý nhầm; crop xác nhận確認すればよかった đúng nguồn, không tạo issue phủ định giả. Bỏ汚れ khỏi danh sách footer90 vì không được in làm headword ở đó. Chưa rà độc lập mọi cue/thoại/footnote toàn148trang.

Lần build đầu có33lỗi do parser chỉ nhận cặp nhãn một dòng; công cụ đã được sửa và thử cả12bản đã viết đủ, không đổi bố cục sách để né lỗi. Negative tests vẫn bắt thiếu dịch/marker rỗng thật/sai vai/ôtrống;55test fork và17test direct đạt. Đây chỉ là kiểm cấu trúc, không chứng minh đầy đủ ngữ nghĩa ngoài những ảnh đã mở.

Hai chênh lệch nguồn do tác giả ghi ởPDF13/14 được giữ trongeditorial-log, không âm thầm sửa câu Nhật. Audio ghi hướng dẫn dùng băng trongPDF4–5, thông tin ấn bản1987 và nhà phát hành theoPDF3, không thấy mã track trong phạm vi tác giả rà; chưa kiểm file nghe thực tế.

Nguồn/hash và hashchapter/book trongcoordinator-review.json. Bản này chưa là full independent semantic review và chưa thiết kế lộ trình mới.
