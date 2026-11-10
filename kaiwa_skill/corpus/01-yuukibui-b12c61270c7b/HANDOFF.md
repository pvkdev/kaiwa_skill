# Bàn giao book11 — WIP

- Cập nhật: 2026-11-10T23:52Z (2026-11-11 JST).
- Worker: `production_book_11_sol`, model `gpt-6-sol/high`, skill 0.2.4.
- Book ID mặc định: `01-yuukibui-b12c61270c7b`.
- Nguồn tương đối từ `kaiwa_skill/`: `book/BJT/01.日本語でビジネス会話 中級編 ー本文冊 YUUKIBUI.pdf`.
- SHA-256 nguồn: `b12c61270c7b14d537a3782e61da6898fff8466fae361b50de717087199afc0a`.
- 138 trang vật lý. Đã mở ảnh thật toàn trang và crop, chép/đối chiếu/verify **p1–15**. **15 verified, 123 pending (p16–138), 0 draft, 0 rendered, 0 needs_review, 0 invalid** tại checkpoint này. Không có source blocker đã biết trong phạm vi đã chuyển đổi.
- Đã reconcile và build partial; không phải completed/accepted. `book.md` và `search.jsonl` chỉ chứa p1–15. Sau release, CLI xác nhận `claim=null`, `build_current=true`, `issue_count=0`; build.json SHA-256 `059e1926a514632b8bbaa2b96995b6efbd907fdcaabd4b0259cc47a1828dc514`.

## Phạm vi và bằng chứng

- p1 bìa; p2 trang tên sách và dấu thư viện Trung `江苏工业学院图书馆 / 藏书章`; p3 xuất bản; p4 lời tựa Nhật; p5–6 đặc điểm/nội dung Nhật; p7 lời tựa Anh; p8–9 đặc điểm/nội dung Anh; p10–11 hướng dẫn; p12–13 mục lục; p14–15 bài1 tự giới thiệu.
- Mỗi page checkpoint có source/render/Markdown hashes và evidence cụ thể. Render chuẩn CLI scale2; đã mở crop phóng to hoặc direct PDF scale4/8 để kiểm chữ nhỏ. Cache và scratch trong `kaiwa_skill/.cache/renders/01-yuukibui-b12c61270c7b/` chỉ phục vụ đọc ảnh, không thuộc output và không commit.
- Không dùng OCR/text layer làm chứng cứ hoặc để tạo bản chép. Chữ Nhật/Anh/Trung và watermark `JLPT Mogi / Yuuki Bùi` đọc từ ảnh. Mọi hình có nghĩa trong phạm vi đã mô tả text; không nhúng ảnh.
- QA coordinator phát hiện kiểu chữ ngày ở p4: đã sửa `1987年５月` thành `1987年 5 月`, re-record và fresh verify. Cũng sửa chữ số mảnh ở p3 sang ASCII trong ngày/địa chỉ rồi fresh verify. Báo cáo QA coordinator nằm riêng, không ghi nhận là nghiệm thu toàn sách.

## Điểm cần giữ đúng theo nguồn

- p4 in `適確`, không đổi sang 適切; p6 in `話しの`, không sửa thành 話の.
- p6 chỉ lần `類話` đầu trong đoạn 一つの課 có furigana `るいわ`; không tự thêm ở lần lặp.
- p7 giữ ngắt từ `associat-` / `ing`; p8 `congratula-` / `tions`, `appro-` / `priate`, `drink-` / `ing`; p9 `Dis-` / `course`.
- p12 in `同音意義語`, không sửa thành 同音異義語; `5.6.漢字の発音` giữ số như in. Crop focused8 xác nhận `本人不在` có `ほんにん` / `ふざい`.
- p13 crop focused8 xác nhận 第十課 đọc `だいじっか`, 第二十課 đọc `だいにじっか`; không thay bằng dạng từ điển khác.
- p14 khung có ba chỗ trống, không điền. p15 tên in `ウイチャイ・プラモー`; tên vai trong Markdown được chú thích là nhãn biên tập từ dòng giới thiệu, nguồn không gắn nhãn vai cho đoạn phát biểu. Dòng `タイ人研修生` có ruby riêng `人＝じん` cùng `研修生＝けんしゅうせい`.
- Số trang in chuyển v (p6) sang vii (p7) đúng chuỗi PDF; không tạo trang vi.

## Nối trang và trang kế tiếp

- p5→6 nối bảng từ 第十五課 sang 第十六課; phần hướng dẫn sau bảng kết trọn câu tại p6.
- p8→9 nối bảng từ Lesson17 sang Lesson18; không câu bị cắt ở các hàng.
- p10→11 tiếp nội dung hướng dẫn: p11 bắt đầu `語句の使い方`, không lặp tiêu đề 本書の使い方 như nguồn.
- p12→13 nối mục lục từ 第八課 sang 第九課; p14 mở 第一課 bài tự giới thiệu.
- p14 là khung 談話型, p15 là 本文会話; không câu nối cần tự hoàn thành.
- p15 kết thúc `どうぞ、よろしくお願いいたします。`. Đã mở preview trực tiếp p16 để kiểm nối: p16 là `《語句の使い方》` và tham chiếu lại câu p2. Preview này chưa được record/render vào ledger; **trang cần chuyển đổi tiếp theo là physical PDF p16 (trang in3)**.

## Tiếp tục

Đọc AGENTS/core/skill/USAGE và handoff này, kiểm claim/status thật, claim bằng token mới. Tiếp tục p16–138, giữ nguyên các trang verified còn hợp lệ. Không sửa PDF nguồn, tools/config/roster hoặc Git index. Coordinator kiểm mẫu và commit tuần tự.
