# Rule 03 – Định dạng mỗi ví dụ (Việt trước, Nhật sau)

Mỗi ví dụ đi theo trình tự: **tình huống → câu Việt → "tiếng Nhật nói thế nào?" → câu Nhật → cách ghép câu**.
Định dạng **cố định tuyệt đối** (validate.py kiểm tra từng dòng):

```markdown
### Ví dụ 1
**Tình huống:** 1–3 câu kể tình huống cụ thể, sống động: ai, ở đâu, đang làm gì, cảm xúc gì.
**Câu Việt:** Câu tiếng Việt đầy đủ, tự nhiên – chính là điều nhân vật muốn nói.
**Câu Nhật:** 日本での生活がこんなに忙しいとは、夢にも思わなかった。
**Tô màu:** とは
**Tô màu Việt:** Không ngờ
**Cách ghép:** mở đầu bằng 「<Câu Nhật nguyên văn>」 rồi giảng cách tạo ra câu Nhật từ câu Việt + cách áp dụng mẫu + lưu ý (nếu có).
```

Ví dụ đánh số **liên tục cả bài** (Ví dụ 1, 2, 3… qua mọi cách dùng). Ví dụ viết thêm (hiếm, xem rule 01): `### Ví dụ 4 [MỚI]`.

## Quy tắc từng dòng

1. **Tình huống** – kể nhanh, có hình ảnh rõ để NotebookLM vẽ minh họa chính xác (nhân vật, nơi chốn, hành động, biểu cảm).
   Kết tình huống bằng một ý dẫn sang câu nói của nhân vật. Không tiết lộ câu Nhật.
2. **Câu Việt** – câu tiếng Việt **đầy đủ**, tự nhiên, đúng nghĩa câu Nhật. Với ví dụ bài gốc: dựa trên bản dịch gốc, giữ ý,
   chỉ chỉnh cho tự nhiên hoặc sửa chỗ sai. Giữ sắc thái (bị động → "bị", cảm thán → "!").
3. **Câu Nhật** – câu tiếng Nhật **đầy đủ, nguyên văn** (ví dụ bài gốc giữ nguyên văn), **sạch**: không ký hiệu, không cách đọc,
   không ngoặc, không romaji. NotebookLM chép nguyên dòng này lên màn hình.
4. **Tô màu** – chép **đúng y** phần mẫu ngữ pháp trong câu Nhật (vd `とは`, `ところへ`, `にかかわらず`). Chỉ chính mẫu;
   phần chia/nối phía trước (だ, な, の, đuôi động từ) không chép vào. Mẫu xuất hiện ở 2 chỗ tách rời → ngăn bằng ` / `.
   **Tô màu Việt** – chép **đúng y** cụm trong Câu Việt mang nghĩa của mẫu (vd `Dù`, `Đúng lúc… thì` → chép đoạn liền có thật trong câu,
   vd `Đúng lúc mình đang ngủ trưa thì`). Ngắn, ≤ 12 từ. Video tô cùng màu với đoạn Tô màu trong câu Nhật. Bắt buộc từ bản 6.4.
5. **Cách ghép** – **mở đầu bằng chính câu Nhật, chép nguyên văn trong 「 」**, sau đó 2–4 câu ngắn giảng như đang lắp ráp câu.
   Lý do: lời giảng của video được dựng từ dòng này; có sẵn trọn câu Nhật ở đầu thì video đọc to cả câu trước khi giải thích
   (người dùng yêu cầu: luôn đọc trọn câu ví dụ rồi mới giảng). validate.py báo LỖI nếu dòng không bắt đầu bằng `「<Câu Nhật>」`.
   Vd: `**Cách ghép:** 「同じ買うなら、少々高くても長持ちするものの方がいい。」 Đây là dạng 同じ ＋ Vる ＋ なら. "Đằng nào cũng mua" là 同じ買うなら…`
   Ngay sau câu trong 「 」, **nói rõ dạng cấu trúc** của ví dụ (vd "Đây là dạng V た ＋ ところで.") – khớp Bảng phủ ví dụ trong Ghi chú.
   validate.py báo LỖI nếu dòng Cách ghép không có chữ "dạng".
   Phần giảng:
   - Ý chính trong câu Việt ứng với phần nào trong câu Nhật.
   - Từ/động từ/tính từ được chia ở dạng nào để gắn với mẫu (vd "忙しい là tính từ い, giữ nguyên rồi gắn とは").
   - Mẫu ngữ pháp đem lại sắc thái gì cho câu.
   - Lưu ý nếu có (lỗi hay gặp, cách nói khác, thân mật/trang trọng). Có thể viết dạng chuỗi ghép: `忙しい + とは → 忙しいとは`.

## Thứ tự ví dụ

1. Ví dụ từ bài gốc: giữ đúng thứ tự trong bài gốc.
2. Ví dụ `[MỚI]` (nếu có) đặt cuối.

## Nơi khác có câu Nhật

- Câu mẫu (phần Ý nghĩa): `**Câu mẫu:**` → `**Nhật:**` → `**Tô màu:**` → `**Tô màu Việt:**` → `**Việt:**`.
- Bẫy ở mục 4: `**Nhật:**` → `**Việt:**`. Câu kết ở mục 5: `**Nhật:**` → `**Tô màu:**` → `**Tô màu Việt:**` → `**Việt:**`.
- "Người Nhật thường nói" ở mục 5: 1–4 nhóm `**Nhật:**` → `**Việt:**` → `**Ý:**`.
- **Không có dòng cách đọc hiragana, không furigana** ở bất kỳ đâu (quyết định của người dùng từ bản 5.0).
- **Không gạch đầu dòng trước câu Nhật / câu Việt** ở bất kỳ đâu: dùng dòng có nhãn `**Nhật:** …` / `**Việt:** …`
  (NotebookLM chép nguyên gạch đầu dòng thành dấu chấm tròn trên màn hình). Gạch đầu dòng chỉ dùng cho các ý ngắn tiếng Việt
  (các khối "Trên màn hình", mục 2 "Mô tả", mục 5 "Tóm lại", "Lưu ý", "Tình huống thực tế").
- **Không có câu đố, quiz, hỏi đáp** ở bất kỳ đâu trong Kịch bản.
