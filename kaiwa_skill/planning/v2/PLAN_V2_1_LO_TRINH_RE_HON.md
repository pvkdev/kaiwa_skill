# PLAN V2.1 — Lộ trình kaiwa 3 level, làm theo kiểu "index trước, đào sâu theo từng chặng"

Ngày: 2026-11-12 · **Thay thế PLAN_V2** (bản đọc toàn văn 27 sách, tốn 4–6 triệu token — đã bỏ).
Đi kèm: `TOPIC_CANDIDATES_V2.md` (danh sách topic ứng viên) và `index/TOC_27_BOOKS.md` + `index/HEADINGS_27.jsonl` (chỉ mục truy ngược).

---

## 1. Thay đổi so với plan trước

| | PLAN_V2 (bỏ) | PLAN_V2.1 (mới) |
|---|---|---|
| Đọc sách | đọc toàn văn 27 sách bằng ~125 sub-agent | **đọc mục lục/đầu mục + index bằng script**; đào sâu **chỉ khi dựng từng chặng** |
| Chi phí | 4–6 triệu token một lần | đã tiêu ≈ vài chục nghìn token cho cả bước tìm topic; phần còn lại trả dần theo từng chặng |
| Sub-agent | điều phối ~125 worker | chỉ dùng khi dựng chặng (mỗi worker 1 chặng, đọc đúng các chương đã trỏ) |
| Đầu ra | thống kê khổng lồ | danh sách chặng + con trỏ nguồn + khung bài học |

**Kết quả bước 1 (đã xong):** `TOPIC_CANDIDATES_V2.md` — **≈ 196 chặng đề xuất** (Sơ 86 · Trung 60 · Thượng 50), mỗi chặng có con trỏ nguồn `Bxx/Sxx`. Có ba cái bạn nên xem kỹ: bảng "27 sách có gì" (mục 1), bảng tổng (mục 5), và các dòng gắn **[AI]** (khoảng trống phải tự bổ sung).

---

## 2. Cấu trúc 5 tầng bạn mô tả → mình chốt thành khung

```
LEVEL (Sơ · Trung · Thượng)
 └ CHẶNG = 1 topic rộng, có mục tiêu thực + can-do        (≈ 196)
     └ TÌNH HUỐNG (8–12 / chặng; lõi 3–4, còn lại mở rộng)
         └ BÀI HỌC (3–4 loại / tình huống)
             └ BƯỚC trong một bài (10–15 phút)
```

### 2.1. Mỗi level có những topic gì
Xem `TOPIC_CANDIDATES_V2.md` mục 2–4. Nguyên tắc: chặng là **bối cảnh rộng** ("Nhà hàng", "Điện thoại công sở", "Xử lý khiếu nại"), không phải một câu chức năng ("Hỏi giá"). Chặng dạng chức năng (NHK 48) vẫn dùng, nhưng làm **xương sống Sơ** như bạn muốn, rồi các chặng bối cảnh đóng vai "tích hợp" sau mỗi họ chức năng (giống 総合タスク của bộ Roleplay).

### 2.2. Mỗi topic có nhiều tình huống để phủ
Một chặng = 8–12 tình huống, khung phủ:
**ai nói với ai** (quan hệ) × **muốn gì** (mục đích) × **trục trặc gì** (biến cố) × **ở đâu/khi nào**.
Nguồn tình huống: sách (ưu tiên, B13 một mình ≈ 210 tình huống có tên), memo web, rồi AI bổ sung cho chỗ thiếu (gắn [AI]).
Cùng topic ở level khác nhau đổi bằng 5 nút xoay: quan hệ · mục đích · biến cố · độ tự chủ · độ ngầm.

### 2.3. Mỗi tình huống có những bài học nào (gói bài)

| # | Bài | Nội dung | Công cụ app | Nguồn chính |
|---|---|---|---|---|
| 1 | **Hiểu tình huống** | Bối cảnh, quan hệ, phép tắc, chọn mức lịch sự, "người Nhật nghĩ gì" | đọc/nghe | B03, B18, B24, memo |
| 2 | **Từ vựng & cụm** | Danh sách theo chủ đề; nghe–lặp | nghe + chấm phát âm theo câu | list từ vựng theo chủ đề |
| 3 | **Mẫu câu / ngữ pháp** | Mẫu cần thiết để nói tình huống này | chọn mẫu từ `bunpou_skill` (N3–N1) · Sơ: **chờ danh sách Minna no Nihongo N5/N4 bạn cung cấp** | B11/B12, B08 P3, B06/B07 |
| 4 | **Hội thoại mẫu + Shadowing** | Nghe → đọc theo → đọc đồng thời | audio + chấm từng câu | B13/B14, B01, B21, B15–17, AI-gen |
| 5 | **Đóng vai có mẫu** | App phát nhân vật A, người học nói nhân vật B, đổi vai | audio vai + chấm phát âm | thẻ vai B15–17, B26/27/25 |
| 6 | **Live Kaiwa AI** | Trò chuyện trực tiếp với AI trong đúng tình huống, có biến cố tăng dần | Live Kaiwa AI | AI cấu hình theo tình huống |

Cấp **chặng**: thêm **Live Kaiwa AI mở rộng** (AI nhập vai trong cả chủ đề, tự do hơn), **can-do check**, **ôn cách quãng** các câu đã học.

### 2.4. Một bài học diễn ra thế nào (khung 10–15 phút)
1. **Khởi động nghe** (1–2′): nghe cả đoạn, đoán ý chính.
2. **Hiểu** (2′): 3–5 điểm cốt lõi, từ/cụm chính.
3. **Shadowing** (4′): nghe–đọc theo từng câu, app chấm điểm; lặp tới ngưỡng.
4. **Đóng vai** (4′): app phát vai A, người học nói vai B, chấm phát âm; đổi vai.
5. **Tự nói** (2–3′): đổi một yếu tố (người/việc/biến cố) và nói lại.
6. **Chốt & ôn** (1′): ghi các câu "phải thuộc" vào hàng ôn cách quãng.

Mục tiêu là **nghe và nói thật nhiều, lặp có nghĩa**, nên bước 3–5 chiếm phần lớn thời gian mọi bài.

### 2.5. Lồng ghép các bộ sách vào lộ trình (mỗi bộ có việc cụ thể)

| Bộ sách | Vai trò trong lộ trình |
|---|---|
| B01, B08, B06, B07 | **Ngân hàng câu** cho Sơ: câu phản xạ, mục tiêu "mở miệng được" |
| B26, B27, B25 (Nama Chūkei) | **Bài nghe thực tế + đóng vai** ở bước 1 và 5; B25 làm cầu nối Trung→Thượng |
| B13, B14 (Shadowing) | **Bước 3**; B13 còn là **ngân hàng tình huống** theo quan hệ |
| B11, B12 (Speak Japanese) | **Bước "mẫu câu"**; dạy lõi mẫu trước khi hội thoại dài |
| B15, B16, B17, B21–23 (Roleplay/business) | **Mạch hành trình công việc** và thẻ vai |
| B02, B03, B04, B05, B10 | Phép tắc, điện thoại, tiếp khách, dịch vụ |
| B09, B19, B20, B24, B18 | **Chặng giải lao ngôn ngữ** + mảnh nhỏ chèn vào mọi chặng |

---

## 3. Quy trình thực hiện (rẻ, tuần tự, từng chặng)

| Bước | Việc | Chi phí | Trạng thái |
|---|---|---|---|
| 0 | Chỉ mục đầu mục 27 sách bằng script | ~0 token AI | **xong** |
| 1 | Đọc mục lục, đề xuất ≈ 196 chặng + con trỏ nguồn | thấp | **xong** (chờ bạn duyệt) |
| 2 | **Bạn duyệt khung**: bỏ/thêm/tách/gộp chặng, số lượng, thứ tự arc | — | **đang chờ** |
| 3 | Chốt thứ tự & arc (hành trình, nhân vật xuyên suốt) | thấp | sau bước 2 |
| 4 | **Dựng blueprint chặng (pilot 3 chặng)** | ≈ 40–80k token/chặng | sau bước 3 |
| 5 | Nhân rộng theo thứ tự bạn muốn, dựng khi nào cần | trả dần | |

**Dựng blueprint một chặng** (skill nhỏ `kaiwa-chang`, sub-agent 1 chặng/lần):
1. Lấy con trỏ nguồn của chặng trong danh sách.
2. Đọc **đúng các chương đã trỏ** (thường 20–60k ký tự), `rg` thêm nếu thiếu.
3. Ra: danh sách tình huống (kèm nguồn hoặc [AI]), hội thoại mẫu trỏ tới sách hoặc spec cho AI-gen, mẫu ngữ pháp trỏ bunpou (Sơ để trống chờ N5/N4), list từ vựng, phân bổ lớp lồng ghép, Live Kaiwa AI persona.
4. Ghi 1 file `blueprint/Lx-Cxx.md` + `.json`.

**Pilot đề xuất (3 chặng khác tầng):** Sơ **S-08 Nhà hàng & quán cà phê** · Trung **T-37 Điện thoại công sở: nhận & chuyển máy** · Thượng **H-07 Xử lý khiếu nại & xin lỗi chính thức**.

---

## 4. Những con số cần nhìn thẳng

- Một chặng ≈ 8–12 tình huống × 3–4 bài ≈ **30–45 bài**. 196 chặng ≈ **6.000–8.800 bài** — không thể dựng hết một lần, và người học không thể học hết ở nhịp 1 bài/ngày.
- Đề xuất: mỗi chặng chia **Lõi** (3–4 tình huống, ≈ 8–10 bài, 1–2 tuần) và **Mở rộng** (các tình huống còn lại, tùy chọn/ôn). Lõi của 196 chặng ≈ 1.600–2.000 bài. Người học vẫn thấy một lộ trình đồ sộ, nhưng có đường chính rõ ràng.
- Chi phí dựng ≈ 40–80k token mỗi chặng đầy đủ; tính theo mức bạn muốn dựng (vd. 20 chặng đầu ≈ 1–1,5 triệu token).

---

## 5. Giới hạn đã biết

- Danh sách chặng và level là **suy ra từ mục lục**, chưa đọc nội dung sâu. Một số tình huống con (B14, B25, B26, B27) nằm trong thân bài, tên chỉ hiện khi đào chặng.
- Memo web chỉ là mục lục, không chứng minh có đủ bài học đằng sau.
- Audio chưa kiểm tra file thật.
- Không sửa nguồn, không commit, không đụng `bunpou_skill`.

---

## 6. Cần bạn quyết

1. **Duyệt/sửa danh sách chặng** trong `TOPIC_CANDIDATES_V2.md` (chặng nào bỏ, thêm, tách, gộp; có muốn tách B20/B24 thành nhiều chặng hơn).
2. **Sơ:** giữ 48 NHK làm xương sống + 38 chặng bối cảnh tích hợp, hay gộp NHK thành ít chặng hơn.
3. **Lõi + Mở rộng** cho mỗi chặng có ổn không (mục 4).
4. Có chạy **pilot 3 chặng** ở mục 3 không, và model cho worker dựng chặng.
