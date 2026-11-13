# KAIWA — Thiết kế skill dựng chặng (bản đề xuất V1, chưa chốt)

Ngày: 2026-11-12 · Đi kèm `KAIWA_CHANG_V4.md/.jsonl` (200 chặng). Tài liệu này là **đề xuất để thảo luận và review**, chưa phải quyết định cuối.

Mục tiêu: một skill chạy qua từng chặng trong 200 chặng, tạo một thư mục cho mỗi chặng, bên trong có tình huống, từ vựng, kiến thức, con trỏ ngữ pháp, hội thoại mẫu, thẻ đóng vai, persona Live Kaiwa AI, có quản lý status để chạy lại được khi bị ngắt. Đầu ra là Markdown + JSON, đủ cấu trúc để nạp vào app hoặc dựng DB.

Bước này gần như là bước tạo output cuối: thư mục chặng là nguồn dữ liệu gốc, app và DB chỉ đọc từ đó. Vì vậy schema phải chốt trước khi chạy hàng loạt.

## 1. Người học thấy gì trong một chặng

**Màn hình chặng:**
- Mục tiêu "Sau chặng này bạn làm được" (3–5 can-do).
- Bản đồ 8–12 tình huống, đánh dấu Lõi (4 tình huống, đường chính) và Mở rộng (phần còn lại, học thêm hoặc ôn).
- Cuối chặng có cụm "Chốt chặng": Live Kaiwa AI mở rộng, can-do check, ôn cách quãng.

**Một tình huống = một bài khoảng 12–15 phút, 7 bước:**

| Bước | Nội dung | Chấm phát âm | AI |
|---|---|---|---|
| 1. Nghe đoán ý | Nghe cả đoạn, trả lời 1–2 câu hỏi ý chính | không | không |
| 2. Hiểu | Thẻ kiến thức ngắn 150–250 chữ: bối cảnh, quan hệ, chọn mức lịch sự, người Nhật nghĩ gì, lỗi người Việt hay mắc | không | không |
| 3. Từ và mẫu | 5–8 câu then chốt, từ Lõi, 1–2 mẫu ngữ pháp | có (lặp từng câu) | không |
| 4. Shadowing | Nghe, đọc theo, đọc đồng thời | có, từng câu, phải đạt ngưỡng mới qua | không |
| 5. Đóng vai | App đóng vai A, người học vai B, rồi đổi vai | có, và chấm hoàn thành mục tiêu | không |
| 6. Tự nói | Đổi một yếu tố (người, việc, biến cố) rồi nói lại | có | gợi ý nhẹ |
| 7. Live mini | 2–3 phút với AI trong đúng tình huống, có 1 biến cố | có | có (từ Trung) |

Bước 4–7 chiếm hơn một nửa thời gian bài. Ở Sơ, bước 7 tùy chọn, AI nói chậm và có nút gợi ý.

**Đóng vai có 3 mức:** R1 có kịch bản (đọc đúng lời vai B, chủ yếu ở Sơ), R2 có gợi ý bằng tiếng Việt (người học tự nói, app so với các cách nói đúng, chủ yếu ở Trung), R3 tự do (chỉ có thẻ vai, mục tiêu và biến cố ngầm, AI chấm đạt hay không, chủ yếu ở Thượng).

**Live Kaiwa AI xuất hiện ở 3 chỗ:** mini cuối mỗi tình huống; mở rộng cuối chặng (AI nhập vai cả chủ đề, biến cố ngẫu nhiên, khóa đến khi xong Lõi); cuối cụm (trộn các chặng trong cụm, kiểm tra can-do).

**Chấm phát âm** ở bước 3–7, chấm từng câu: độ chính xác âm, độ trôi chảy và tốc độ, đủ ý. Cao độ (pitch accent) để giai đoạn sau nhưng dữ liệu phải chuẩn bị sẵn.

## 2. Mỗi chặng cần những tình huống nào để phủ

Skill lập **ma trận phủ** cho từng chặng: quan hệ × mục đích × biến cố × địa điểm. Quy tắc tối thiểu:
- 1 tình huống mở đầu hoặc vào việc.
- 3–4 luồng chính thường gặp (Lõi).
- Ít nhất 2 tình huống có biến cố.
- Ít nhất 1 tình huống nghe thông tin (thông báo, lời nhắn).
- Ít nhất 1 tình huống đổi quan hệ (cùng việc nhưng nói với cấp trên hoặc khách).
- 1 tình huống tích hợp để khép chặng.

Mỗi tình huống ghi rõ nguồn sách hay [AI]. Skill tự chấm điểm phủ và báo ô còn thiếu.

## 3. Từ vựng

- **Từ Lõi (20–30 từ/chặng):** phải xuất hiện trong hội thoại Lõi, được học, chấm, ôn.
- **Từ Mở rộng (80–150 từ/chặng):** nhóm theo nghĩa, dùng cho thẻ từ và ôn.
- **Thứ tự lấy:** hội thoại sách của chặng → 5500, Nama Chūkei, Roleplay → MINATO/MIMIKARA cùng chủ đề (lọc theo level: Sơ N5–N4, Trung N4–N3, Thượng N3–N2) → AI bổ sung.
- **Vòng kín:** từ Lõi phải có trong hội thoại, từ mới trong hội thoại phải có trong list. Script kiểm tra.
- **Không dạy lặp:** mỗi từ có một "chặng gốc" dạy lần đầu, các chặng khác chỉ tham chiếu. Cần `vocab_master.jsonl` dùng chung.
- **Mỗi từ lưu:** kana, kanji, nghĩa tiếng Việt, loại từ, level, câu ví dụ từ hội thoại, nguồn.

## 4. Ngữ pháp

Chặng chỉ chứa **con trỏ**, không giảng lại: N3–N1 trỏ id trong `bunpou_skill`; N5/N4 trỏ bài Minna 1–50 (danh sách do người dùng cấp, trong lúc chờ để trống và có bước "gắn ngữ pháp" chạy lại được). Mỗi chặng 3–6 mẫu, đánh dấu "phải nói được" hoặc "chỉ cần nhận ra". Riêng Sơ có **trần ngữ pháp**: chặng thứ n chỉ dùng ngữ pháp Minna tới một bài nhất định.

## 5. Lồng ghép các bộ sách

| Bộ sách | Dùng ở đâu |
|---|---|
| 5500 (B01), B08, B06, B07 | Bước 3, câu phản xạ ngắn ở Sơ |
| Shadowing (B13, B14) | Bước 4; B13 còn là ngân hàng tình huống theo quan hệ |
| Speak Japanese (B11, B12) | Bước 3, dạy mẫu lõi trước hội thoại dài |
| Nama Chūkei (B25, B26, B27) | Bước 1 (nghe thực tế) và đóng vai R2/R3 |
| Business (B15–17, B21–23, B02–05, B10) | Thẻ vai, tình huống công việc, thẻ kiến thức |
| B09, B18, B19, B20, B24 | Ngân hàng cách nói, chèn vào bước 3 và Chốt chặng |

## 6. Cấu trúc thư mục và dữ liệu

JSON là bản gốc, Markdown là bản render để đọc và review. Mỗi mục có ID cố định (ví dụ `S-01.03.u05`).

```
kaiwa_content/
  _meta/  schema/, vocab_master.jsonl, run_state.json, coverage_report.md
  S-01_chao-hoi-theo-thoi-diem/
    chang.json        (manifest: can-do, danh sách tình huống, đếm)
    status.json       (trạng thái từng bước dựng)
    README.md         (render cho người đọc)
    sources.json      (con trỏ nguồn + ghi chú đã đọc)
    coverage.json     (ma trận phủ)
    vocab.jsonl, grammar_refs.json, banks.json, review_cards.json
    situations/01_.../ situation.json, knowledge.md, dialogue.json,
                       roleplay.json, live_ai.json
```

Mỗi câu hội thoại (utterance) lưu: người nói, kana, mức lịch sự, đáp án chấp nhận được, tham chiếu audio. Bảng DB tương ứng: chang, situation, utterance, vocab, vocab_occurrence, grammar_ref, source_ref, roleplay_card, ai_persona, srs_card.

## 7. Status và chạy lại khi bị ngắt

Các bước mỗi chặng: tạo thư mục → đọc nguồn → lập tình huống và ma trận phủ → từ vựng → ngữ pháp → thẻ kiến thức → hội thoại → đóng vai và persona AI → kiểm tra tự động → xong.

- Mỗi bước có trạng thái pending, running, done, failed hoặc needs_review, kèm thời điểm và hash đầu vào.
- Ghi file qua file tạm rồi đổi tên, nên bị ngắt giữa chừng không hỏng.
- Chạy lại tự tìm bước đầu tiên chưa done và tiếp tục. Sửa spec thì các bước sau tự đánh dấu stale.
- Script kèm skill: `init`, `next`, `mark`, `validate` (vòng kín từ vựng, schema, ma trận phủ, trần ngữ pháp), `render_md`, `export_db`.

Chi phí: 200 chặng × 40–80k token là 8–16 triệu token. Đề xuất dựng Lõi cho cả 200 chặng trước, Mở rộng sau; pilot 3 chặng để đo chi phí thật.

## 8. Quyết định cần chốt

1. Bài = 1 tình huống với 7 bước như trên?
2. Lõi 4 tình huống, phần còn lại là Mở rộng, dựng Lõi trước?
3. Hội thoại trong app: viết lại bằng lời của mình theo cấu trúc tình huống của sách và chỉ ghi con trỏ nguồn (đề xuất), hay chép nguyên văn? Nếu app bán thương mại, chép nguyên văn có rủi ro bản quyền.
4. Nơi chạy: máy người dùng bằng agent CLI (đọc sách tại chỗ, thư mục trong repo git, status lưu bền) hay cloud tạm thời?
5. Pilot 3 chặng (Sơ "Nhà hàng & quán ăn", Trung "Chuyển máy, gọi nhầm & để khách chờ", Thượng "Nhận khiếu nại & xin lỗi chính thức") trước khi chạy toàn bộ?
6. Cần người dùng cấp: danh sách 50 bài Minna (N5/N4) và cách hiển thị furigana, romaji, bản dịch tiếng Việt.
