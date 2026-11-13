# QA bucket daily — 2026-11-13

- Assignment hiện có **99 chặng**, **480 nhóm sự kiện**, **2.405 tình huống** (đếm đọc lại sau các bổ sung của root). Không sửa file chặng, assignment hoặc progress trong lượt QA metadata này.
- Kiểm cấu trúc đọc-only: đủ 99 file; key/UID đúng assignment; ID tình huống và tiêu đề không trùng trong chặng; tham chiếu event, `continues_from`, cross-stage và source ledger đều tồn tại. **0 lỗi cấu trúc**. Kiểm này không thay đánh giá biên tập tiếng Nhật hay độ đủ của sự kiện.
- `daily_web_sources.json`: DW01–DW09 chỉ xuất hiện qua **search excerpts**; DW10 chỉ có liên kết và tóm tắt trong V5 preview, nên là **index_only**. Không nguồn nào được đánh dấu `opened`; không dùng các snippet này như bằng chứng đã đọc toàn trang hoặc như quy định áp dụng khắp Nhật.
- Nội dung tình huống là **AI biên soạn**; B05 Unit 20–24, B08 Unit 21–22 và B26 bài マンション đã được đọc chọn trong bản knowledge và ghi ở `daily_research.md`/`source_findings` phù hợp. Khi viết bài học sau này cần kiểm lại dữ kiện cụ thể theo địa phương, nhà vận hành và cơ sở.
