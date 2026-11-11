# Chuyển pilot raw-fork sang PDF-direct có lịch sử

Root đã mở lại bìa và ảnh nguồn7–9, đối chiếu các ảnh10–12 đã xem trong lượt này, kiểm hash toàn4chapter với bản pilot đã nghiệm thu. Giữ nguyên byte cả4chapter và9unit nội dung; không viết lại hoặc mở rộng phạm vi6trang.

Bản gốc gồm book/metadata/ledger/units/search/audio/reviews/chapters được sao byte-exact vào migration-history trước khi chuyển. Snapshot raw và corpus không sửa. clean-state.json cũ được giữ nguyên như ledger lịch sử inactive; từ đây dùng direct-state.json và skill PDF-direct để resume. Raw pointers cũ còn trong legacy_raw_source/history; nguồn chính mới là PDF/hash/pageblock.

Mọi block nguồn7–12 đã có mapping từ kiểm trước; ba block điều hướng lề phải lặp ở10/11/12 được ghi excluded rõ. CD付 ở bìa và mã CD1/2/3 được ghi có dẫn trang; không suy số đĩa hoặc file nghe thực tế.

Vấn đề công thức nguồnPDF9 đã biết trước vẫn giữ, nay có needs_review cấu trúc và notice/source-issues.md. Bản học giữ ví dụ, không dạy công thức mâu thuẫn; hai chapter chia sẻ trang9 được giữ cờ trang thận trọng. Không có pending/draft/stale trong phạm vi pilot; validate --allow-source-issues0lỗi,2warning nguồn (cùng một vấn đề được gắn page/unit). Strict validate chưa đạt vì vấn đề nguồn này.

Đây là chuyển provenance, không phải nghiệm thu full96trang. Khi nhận fullscope phải dùng extend-scope giữ history và toàn bộ nội dung cũ, đọc các trang còn lại, đặc biệt trang28 đã có vấn đề scan trong raw.
