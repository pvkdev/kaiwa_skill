# Bàn giao nguồn Namachuukei Chuujoukyuu

- Quy ước đường dẫn: tương đối từ `kaiwa_skill/` trừ khi ghi rõ.
- Source: `book/Shadowing/Namachuukei Chuujoukyuu.pdf`, SHA-256 `f08dd9302ee64ea0b1b85a5ebb81bbab7fdf0391b61bcce87ffd53eed028547e`, 89 trang PDF vật lý.
- `book_id`: `namachuukei-chuujoukyuu-f08dd9302ee6`.
- Trạng thái lúc 2026-11-10 13:33 UTC: **89/89 verified**, `issue_count: 0`, `build_current: true`. `build.json` ghi `complete: true`; `book.md` và `search.jsonl` đã build từ đủ 89 trang. Acceptance vẫn là `coordinator_review_required` cho đến khi coordinator kiểm chéo.
- Checkpoint chuẩn: `corpus/namachuukei-chuujoukyuu-f08dd9302ee6/pages/`. Render tạm ở `.cache/renders/namachuukei-chuujoukyuu-f08dd9302ee6/`, scale 2 hoặc 2.5 tùy checkpoint; scratch/review JSON ở `.cache/work/production_book_04/`. Corpus và output chỉ chứa văn bản. Không xóa scratch vì có crop và evidence phục vụ audit.
- PDF scan không có text layer. OCR chỉ dùng làm nháp. Mỗi trang tiếp nối đã mở ảnh gốc render toàn trang, crop vùng nhỏ khi cần, so ảnh→Markdown để tìm thiếu và Markdown→ảnh để tìm phần tự thêm, rồi ghi evidence hash-bound reviewer `production_book_04_resume/gpt-6-sol-high`. Trước lượt tiếp nối này p0001–p0042 đã verified; giữ checkpoint, trừ các chỉnh sửa theo QA được record/verify lại.

## Những điểm nguồn và chỉnh sửa đã đối chiếu

- P0009 prompt in `①～⑥`, song ảnh chỉ có lời nhắn và hàng đáp án ①–⑤. Giữ nguyên cả hai phần đúng nguồn.
- P0005 metadata sửa `教師の方々へ`; p0010/p0012 running header bỏ dấu phẩy không in sau `今`; p0011 giữ hai ô trống tách biệt; p0013–p0018 rà furigana từng occurrence và bỏ các map không in. P0014 crop chặt sửa `一度＝いちど`, p0015 sửa span `斉藤君＝さいとうくん`. Những trang sửa đều reverify.
- P0024 crop xác nhận ví dụ (5) không in ruby 興味, đã bỏ; hai panel tiền tố và câu mời được trình bày thành hai nhóm lựa chọn, tránh gán cặp cố định. P0020–p0027 được coordinator QA; không thấy lỗi khác.
- P0035 sửa nhãn lời đáp nằm dưới hình 課長 theo QA. P0042 nhãn biên tập ở heading bảng/ô trống; p0043 bổ sung ruby 聞 ở occurrence đầu; p0044 bỏ ruby 言 không in; p0045 sửa thứ tự hai lượt thoại. Đã reverify.
- P0084 bổ sung ruby 他＝ほか trong Q/A; p0085 bổ sung 他＝ほか và ruby 相手 ở occurrence thứ hai. P0086 bỏ ruby 夫 không in tại ví dụ (3). P0088 sửa tên tác giả `椙本総子` theo ảnh/bìa và chấm câu tiếng Anh thành `U.S.A. ).`. Các trang đều mở lại crop, record/reverify theo QA hoặc tự đối chiếu.
- P0089 kết thúc sách: 著者紹介 và 奥付, không có số trang in; giữ tên `椙本総子`, thông tin xuất bản, copyright và ISBN theo ảnh.

Coordinator phụ trách audit cuối, Git/commit và acceptance. Nếu QA phát hiện lỗi cụ thể, claim lại, sửa đúng trang, mở lại ảnh/crop, record/verify hash-bound, build lại và cập nhật bàn giao.
