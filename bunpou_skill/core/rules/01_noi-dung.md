# Rule 01 – Độ chính xác nội dung

Mục tiêu: người học tin tuyệt đối vào video. Một lỗi ngữ pháp sai lan ra 1000 video là thảm họa.

## PHẢI

1. **Ví dụ bài gốc là nguồn ví dụ chính – đã được chọn lọc kỹ.**
   - Video dùng **4–6 ví dụ cho mỗi cách dùng** và phủ **mọi dạng cấu trúc** – chọn từ ví dụ bài gốc theo mục 4.
   - Câu được chọn giữ **nguyên văn câu Nhật**; chỉ sửa khi có lỗi thật (định nghĩa ở mục 3), và phải ghi lại.
   - Câu Việt **dựa trên bản dịch bài gốc**: giữ ý, chỉ chỉnh cho tự nhiên với giọng giảng hoặc sửa chỗ dịch sai.
   - Không thay bằng câu khác, không viết lại câu, giữ thứ tự bài gốc.
   - Phần AI tự viết quanh mỗi ví dụ chỉ là: Tình huống, Tô màu, Cách ghép.
2. **Kiểm tra bài gốc trước khi viết.** Các lỗi hay gặp cần soát:
   - Dịch sai quan hệ gia đình/xưng hô (vd 妹 = em gái, 姉 = chị gái, 兄 = anh trai, 弟 = em trai).
   - Chính tả tiếng Việt (vd "cảm trở" → "cản trở").
   - Cấu trúc thiếu thành phần (vd `Aな + ところ` phải là `Aな + な + ところ`; `N + ところ` phải là `N + の + ところ`).
   - Câu tiếng Nhật thiếu tự nhiên, sai trợ từ, sai chia động từ.
   - Bản dịch lệch thì/thể so với câu Nhật (vd câu bị động dịch thành chủ động mất nghĩa "bị").
3. Mọi chỗ sửa → ghi vào `_phu/GhiChu_<ID>.md` dạng `trước → sau (lý do)`.

   **Thế nào là lỗi** (phải ghi): sai nghĩa khi dịch, sai chính tả, sai ngữ pháp/cấu trúc, câu Nhật không tự nhiên, thiếu dấu câu Nhật.
   **Không phải lỗi** (không cần ghi): chuẩn hóa xưng hô "tôi" → "mình", đổi câu dịch cho tự nhiên mà không đổi nghĩa,
   bỏ khoảng trắng thừa. Không có lỗi thật → ghi "Không phát hiện lỗi."
4. **Số ví dụ: 4–6 cho MỖI cách dùng** (bài 3 cách dùng → 12–18 ví dụ) và **phủ mọi dạng cấu trúc** (validate.py báo LỖI nếu sai).
   - **Phủ cấu trúc:** mỗi thẻ "Cấu trúc n" (phần Cách chia của các cách dùng) phải có ít nhất 1 ví dụ dùng đúng dạng đó (vd V る / V ている / V た,
     Aい / Aな, N の; なら / のだったら / んだったら / のであれば). Trong một cách dùng, ưu tiên các ví dụ khác dạng nhau.
     Một cách dùng có hơn 6 dạng cấu trúc thì được thêm ví dụ để mỗi dạng có 1 ví dụ.
   - **Bảng phủ ví dụ** (bắt buộc, trong Ghi chú biên tập): mỗi ví dụ một dòng `| Ví dụ | Phần | Cấu trúc | Nguồn |` (Phần = 3.1, 3.2…;
     ví dụ của chương Cách nói thường gặp ghi Cấu trúc là `–`);
     validate.py dùng bảng này để kiểm cách dùng nào thiếu ví dụ, dạng cấu trúc nào chưa có ví dụ.
   - **Cách ghép nói dạng:** mỗi ví dụ, ngay sau câu Nhật trong 「 」, nói rõ dạng cấu trúc đang dùng (vd "Đây là dạng N ＋ の ＋ ところを.");
     ví dụ của chương Cách nói thường gặp nói "Đây là cụm …".
   - **Chương Cách nói thường gặp:** 1–3 ví dụ mỗi cụm, không cần đủ 4.
   - Bài gốc có nhiều hơn số cần → AI tự chọn, giữ thứ tự bài gốc, theo thứ tự ưu tiên:
     (1) phủ dạng cấu trúc chưa có ví dụ; (2) điển hình nhất, thể hiện rõ dấu hiệu nhận biết; (3) nhiều sắc thái (vui, bất ngờ, tiếc…);
     (4) không trùng ý với ví dụ đã chọn; (5) dễ dựng tình huống, từ vựng hợp cấp độ. Câu bị lược ghi vào Ghi chú biên tập.
   - Câu **trùng hoặc gần trùng** (cùng tình huống, cùng dạng, chỉ khác vài chữ) tính là **một** câu.
   - Bài gốc **không đủ** (một cách dùng < 4 câu khác ý, hoặc một dạng cấu trúc không có câu nào) → viết thêm ví dụ `[MỚI]` **vừa đủ**
     để mỗi cách dùng đạt 4 và mỗi dạng cấu trúc có 1 ví dụ. Không viết [MỚI] chỉ để lên 5–6.
5. **Ví dụ `[MỚI]` phải:**
   - Đúng cách dùng của mục đó, đúng dấu hiệu nhận biết đã nêu, đúng dạng cấu trúc ghi trong Bảng phủ.
   - Là câu người Nhật thật sự nói/viết. Ưu tiên mẫu câu quen thuộc trong giáo trình JLPT.
   - Dùng từ vựng không vượt cấp độ mục tiêu (xem `05_cap-do.md`).
   - Không trùng tình huống với ví dụ khác trong cùng bài.
6. **Câu tự viết ngoài ví dụ** – câu mẫu trong phần Ý nghĩa, câu "Người Nhật thường nói", nội dung "Tình huống thực tế":
   phải chắc chắn đúng và tự nhiên như người bản xứ nói thật. Không chắc thì bỏ – hai phần ở mục 5 là **tùy chọn**.
   "Người Nhật thường nói" ưu tiên câu cửa miệng, cụm cố định, cách nói tắt có thật (vd お忙しいところ、すみません), kèm dòng "Ý" nói rõ dùng lúc nào.
7. **Mục "Bẫy dễ nhầm"** được phép thêm kiến thức ngoài bài gốc, gồm 2 loại:
   - **Giống hình thức:** mẫu/từ viết giống hoặc gần giống (vd ところで liên từ đầu câu; 〜たところで "dù có… cũng vô ích"; うち = "nhà").
   - **Gần nghĩa:** mẫu dễ dùng nhầm thay cho nhau (vd うちに và 間に). Chỉ nêu điểm khác biệt chắc chắn, dùng "thường" thay cho "luôn".
   - Loại nào ưu tiên và số lượng: theo `05_cap-do.md`. Mỗi bẫy có 1 câu Nhật mẫu + dịch + cách phân biệt.
   - Phải chính xác; không chắc thì không đưa vào – chọn bẫy khác chắc chắn hơn.

## KHÔNG

- Không thêm cách dùng mới (chương 3.x) mà bài gốc không có. Chương "Cách nói thường gặp" chỉ dành cho cụm bài gốc đã nêu.
- Không khẳng định quy tắc tuyệt đối ("luôn luôn", "không bao giờ") khi tiếng Nhật thực tế có ngoại lệ. Dùng "thường", "hay".
- Không đưa thông tin văn hóa/lịch sử khó kiểm chứng làm "chốt vui".

## Khi không chắc

AI tự quyết, không hỏi người dùng. Nếu nghi ngờ một câu tiếng Nhật do mình viết hay một giải thích:
**thay bằng phương án đơn giản hơn mà chắc chắn đúng** (hoặc bỏ phần không bắt buộc như một bẫy).
Ghi quyết định vào mục "Quyết định đã tự đưa ra" trong `_phu/GhiChu_<ID>.md`. Không để lại điểm nghi ngờ trong Kịch bản.
