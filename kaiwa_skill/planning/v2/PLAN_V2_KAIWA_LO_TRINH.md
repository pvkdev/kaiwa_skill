> **⚠ ĐÃ THAY THẾ bởi PLAN_V2_1_LO_TRINH_RE_HON.md (2026-11-12).** Hướng đọc toàn văn 27 sách trong bản này tốn 4–6 triệu token nên đã bỏ; chỉ giữ để tham khảo.

# PLAN V2 — Từ 27 cuốn sách đến MỘT lộ trình kaiwa "độc cô cầu bại"

Ngày lập: 2026-11-12 · Trạng thái: **ĐỀ XUẤT, chờ duyệt — chưa chạy gì**
Phạm vi: chạy hoàn toàn mới, **không kế thừa và không sửa** `catalog27/`, `curriculum_outline/`, blueprint 16 topic, bản 25 topic của Codex. Các file đó chỉ được đọc để so sánh khi cần.

---

## 0. Mình hiểu bạn muốn gì (và chỗ mình KHÔNG tự suy diễn)

**Điều bạn đã nói rõ:**

1. Đọc **thật** 27 file Markdown clean (trừ 3 tập từ vựng MINATO/MIMIKARA, chỉ để tra cứu). Không phải đọc metadata như lần của Codex.
2. Mỗi sách phải ra: (a) topic + tình huống xuất hiện, (b) **dạng kiến thức** của sách (vd. 5500 = kaiwa theo tình huống đời sống; Roleplay = kaiwa business), (c) phân loại sơ/trung/thượng cho topic và tình huống.
3. Tổng hợp 27 sách + memo web S01–S22 thành **danh sách tổng thống kê đầy đủ**: topic, loại kiến thức, kiểu bài học, theo level.
4. Chỉ **sau khi có thống kê** mới quyết định cách phối hợp. Mục tiêu cuối: 3 level, mỗi level **≥ 50 chặng (topic) — càng nhiều càng tốt**, mỗi chặng phủ hết tình huống thực tế trong đời sống/công việc; topic được phép lặp qua các level với cách nói khác nhau.
5. Mỗi tình huống: hội thoại mẫu chất lượng (từ sách hoặc AI sinh), **chỉ mục** tới `bunpou_skill` cho ngữ pháp (chưa cần nội dung), **chỉ list** từ vựng theo chủ đề; lồng thêm Nama Chūkei, Shadowing, Speak Japanese… vào từng chặng.
6. Hành trình như một người trưởng thành dần: từ bập bẹ chào hỏi → chuyên gia đàm phán / nhân lực chủ chốt / người bản địa.
7. Cần **một skill** để kích hoạt các sub-agent con.

**Điều mình ghi nhận là rủi ro, không tự quyết:**
- File handoff từng ghi bạn đã hạ yêu cầu xuống "chỉ cần metadata để tiết kiệm quota". Lần này bạn nói rõ "đọc hết 27 md", nên plan này **đọc toàn văn** — chi phí ở mục 7.
- "Tận dụng toàn bộ tài nguyên" mình định nghĩa **có thể đo được** (mục 5.4) để không rơi vào cảnh chỉ nhắc tên sách cho có.

---

## 1. Số liệu thật của kho (đã đo trên máy bạn)

| Hạng mục | Giá trị |
|---|---|
| Sách đưa vào đọc | **27** (không tính MINATO 1160, MIMIKARA N1, MIMIKARA N3) |
| Số file chương/phần | **486** |
| Khối lượng chữ | **≈ 5,15 triệu ký tự** (Nhật + giải thích Việt) |
| Sách lớn nhất | B15 Roleplay thượng (≈270k ký tự), B04 điện thoại (≈282k), B09 なめらか (≈265k) |
| Chương đơn lớn nhất | 63k ký tự (必須700), 58k (超ミニ200), 48k (接客700) → cần cắt nhỏ |
| Memo web | `WEB_COURSE_TOPICS_MEMO.md` ≈ 116 KB, 22 nguồn S01–S22 |
| Ngữ pháp có sẵn để index | `bunpou_skill/work/`: **N3 = 118, N2 = 114, N1 = 128** bài. **N5 và N4 = 0 bài** |
| Audio | `AUDIO_INDEX.md` chỉ là inventory, chưa xác nhận có file nghe |

> ⚠ **Phát hiện quan trọng:** bunpou_skill chưa có N5/N4. **Đã chốt:** danh sách ngữ pháp N5/N4 sẽ lấy từ danh sách ngữ pháp Minna no Nihongo trên web do bạn tự tìm và cung cấp khi cần. Giai đoạn này mình chỉ để chỗ trống `grammar_ref: pending-N5/N4` trong blueprint Sơ, không tự dựng danh sách.

---

## 2. Kiến trúc tổng thể: 6 pha, 5 cổng duyệt

```
PHA 0  Chốt quyết định (plan này)
PHA 1  Viết skill + công cụ + PILOT 3 sách ───────────► CỔNG A (bạn xem mẫu)
PHA 2  Đọc toàn văn 27 sách (chunk → book card)
PHA 3  Đọc memo web S01–S22 (cùng schema)
PHA 4  Tổng hợp: Master Inventory + thống kê ─────────► CỔNG B (bạn xem thống kê)
PHA 5  Quyết định kiến trúc lộ trình ─────────────────► CỔNG C (bạn chốt khung)
PHA 6  Topic Bank (≥ 50/level, mục tiêu 70+) ─────────► CỔNG D (bạn duyệt danh sách chặng)
PHA 7  Stage Blueprint từng chặng (mẫu 3 chặng → hàng loạt) ► CỔNG E
```

Nguyên tắc xuyên suốt: **thống kê trước, thiết kế sau**; mọi dòng dữ liệu có **neo nguồn** (sách + chương + tiêu đề/anchor) để tra ngược được.

---

## 3. PHA 1 — Skill kích hoạt sub-agent: `kaiwa-extract`

Đặt tại `.agents/skills/kaiwa-extract/` (theo quy ước AGENTS.md), tên đề xuất **`kaiwa-extract`**.

```
kaiwa-extract/
  SKILL.md                 điều phối: các bước, quy tắc, cách giao việc, resume
  scripts/
    chunk.py               cắt 27 sách thành chunk ≤ ~55–60k ký tự, theo ranh giới chương/đầu mục
    validate.py            kiểm JSON của worker: đủ trường, anchor có THẬT trong nguồn, không bỏ chương
    merge_book.py          gộp chunk → book card (số liệu), tạo bảng thống kê
    aggregate.py           gộp 27 book card + memo → Master Inventory
  references/
    schema.md              schema ChunkCard / BookCard (mục 4)
    level-rubric.md        thang chấm sơ/trung/thượng (mục 4.3)
    taxonomy.md            danh mục "dạng kiến thức" và "kiểu bài học"
    worker-prompt.md       prompt chuẩn giao cho worker
  state/manifest.json      trạng thái từng chunk (pending/done/failed) để resume
```

**Cách kích hoạt sub:** SKILL.md hướng dẫn root (a) chạy `chunk.py` → manifest, (b) bắn các wave worker song song (khuyến nghị 6–8/wave), mỗi worker nhận **đúng 1 chunk**, đọc hết, ghi 1 file JSON + 1 file notes, (c) chạy `validate.py` — chunk fail thì chạy lại riêng chunk đó, (d) khi đủ chunk của một sách mới gọi worker gộp sách.

Chạy trong Claude: dùng `Agent` (general-purpose), hoặc `Workflow` nếu bạn nói "dùng workflow". SKILL.md viết trung tính để Codex vẫn đọc được (AGENTS.md hiện nói về `spawn_agent`; mình **không sửa AGENTS.md** trừ khi bạn đồng ý).

**Chỗ chạy:** sub-agent chạy ở cloud nên cần có file nguồn trong cloud. Cách làm rẻ nhất: nén 27 sách (≈ 2 MB nén) trên máy bạn → stage **một lần** → giải nén ở cloud; kết quả gộp lại thành vài chục file rồi commit về `kaiwa_skill/planning/v2/`. Không đụng nguồn gốc.

**PILOT (bắt buộc trước khi nhân rộng):** chạy 3 sách khác dạng nhau để chốt schema:
- **B01 — 5500 câu** (kaiwa theo tình huống, câu ngắn, nhiều topic nhỏ)
- **B17 — Roleplay sơ-trung** (câu chuyện nhân viên mới, thẻ vai, bài tập)
- **B14 — Shadowing sơ-trung** (đoạn đối thoại đánh số, luyện bám mẫu)

Bạn xem 3 book card đó ở **Cổng A**; không vừa ý thì sửa schema khi mới tốn ~6–8 worker, chưa tốn cả kho.

---

## 4. PHA 2 — Đọc 27 sách: đơn vị công việc và đầu ra

### 4.1. Đơn vị đọc
- **Chunk** ≈ 55–60k ký tự (≈ 90 chunk toàn kho). Không để worker đọc nguyên sách lớn: đọc đủ sâu mới đáng tin, context quá lớn thì sót.
- Mỗi worker **đọc hết** chunk của mình và phải báo `chapters_read` (liệt kê từng file). Validator đối chiếu với manifest — thiếu chương là fail.
- Chương kiểu đáp án / mục lục / bìa vẫn được đọc nhưng chỉ ghi nhận "loại nội dung" (không bắt trích tình huống).

### 4.2. Đầu ra mỗi chunk (ChunkCard) — những gì bạn yêu cầu

1. **Tình huống & topic** — mỗi dòng: `id`, tên (JA + VI), lĩnh vực, bối cảnh, **vai và quan hệ**, mục tiêu giao tiếp, **chức năng ngôn ngữ** (nhờ, từ chối, xin lỗi, đề xuất…), mức lịch sự (thân mật / lịch sự / kính ngữ / hỗn hợp), **loại học liệu** (hội thoại mẫu / roleplay / nghe / câu mẫu / bài tập), **neo nguồn** (file + đầu mục), `level` + `bằng chứng` + độ tin cậy.
2. **Dạng kiến thức** — mẫu câu, câu cố định, aizuchi, biến âm khẩu ngữ, kính ngữ, từ tượng thanh/hình, thành ngữ, biểu đạt cảm xúc, văn hóa/phép tắc, chiến lược nghe, quy tắc phát âm… (danh mục ở `taxonomy.md`).
3. **Kiểu bài học** — hội thoại mẫu, thẻ roleplay, bài nghe có câu hỏi, shadowing, luyện mẫu câu, điền khuyết, can-do checklist, cột văn hóa…
4. **Giá trị tái dùng** — hội thoại nào có chất lượng "lấy dùng được" (tự nhiên, đủ lượt, có biến cố); nội dung **độc đáo** cần giữ (một mẹo, một bài luyện riêng).
5. **Cờ**: `needs_review`, phần mờ/thiếu theo `_meta/source-issues.md` của sách.

### 4.3. Thang chia level — không chia theo bìa
Mỗi tình huống chấm trên **5 trục**, level = tổng hợp có bằng chứng (ghi lại lý do):

| Trục | Sơ | Trung | Thượng |
|---|---|---|---|
| Ngôn ngữ | mẫu cơ bản, câu ngắn (≈ N5–N4) | mẫu mở rộng, nối ý (≈ N3) | diễn đạt tinh tế, khẩu ngữ, thành ngữ (≈ N2–N1) |
| Quan hệ / lịch sự | 1 quan hệ đơn, chủ yếu です・ます | đổi mức lịch sự theo đối tượng | kính ngữ chuẩn, đối ngoại, nhiều bên |
| Nhiệm vụ | 1 hành động 1 lượt | nhiều lượt, có lý do/ý kiến | thuyết phục, đàm phán, điều hướng |
| Biến cố | không | có trục trặc nhỏ | xung đột, khủng hoảng, từ chối khéo |
| Độ ngầm / văn hóa | nói thẳng | ngầm định cơ bản | ám chỉ, giữ thể diện, văn hóa sâu |

Level bìa sách chỉ là **một bằng chứng**; vị trí trong sách (đầu/cuối) và 4 trục kia mới quyết định. Mức này cho phép một sách "trung" vẫn có tình huống chấm "sơ" hoặc "thượng".

### 4.4. Gộp thành BookCard (27 file)
Mỗi sách ra: hồ sơ sách (dạng kiến thức chính, kiểu bài học chính, thế mạnh, người học), danh sách tình huống + topic **đã chia sơ/trung/thượng**, thống kê (số hội thoại, số bài nghe, số mẫu câu…), danh sách "tài sản tái dùng", các cờ. Dạng `Bxx.json` (máy đọc) + `Bxx.md` (người đọc).

### 4.5. Kiểm soát chất lượng — chống "đọc cho có"
- `validate.py` kiểm: mọi anchor **tồn tại thật** trong file nguồn; đủ chương; tỷ lệ tình huống có bằng chứng level.
- **QA chéo ngẫu nhiên:** một worker khác đọc lại ~10% chunk (chọn đủ dạng sách) và so với card; sai lệch lớn → chạy lại chunk.
- Root không tuyên bố "đã đọc hiểu từng câu"; ghi rõ mức đã làm và các chương bỏ qua (nếu có).

---

## 5. PHA 3–4 — Memo web và Master Inventory

### 5.1. Memo S01–S22
Cùng schema nhưng gắn nhãn `source_kind = web/mục lục` (không có toàn văn → độ tin cậy thấp hơn, không cam kết có bài học đủ). 2 worker là đủ (≈ 116 KB). S18 trùng B10 → không đếm lại; S20–S22 giữ nguồn tạm, không đoán tên sách.

### 5.2. Master Inventory (tổng hợp)
Gộp bằng máy + AI, đầu ra gồm:

1. **Bảng topic chuẩn hóa (canonical):** mỗi dòng là một cụm tình huống/topic, kèm *tất cả* nguồn (sách + chương + web) và *level từng nguồn* → thấy ngay topic nào "dày" (nhiều sách) và topic nào "mỏng".
2. **Ma trận sách × dạng kiến thức**, **sách × kiểu bài học**, **topic × level**, **chức năng ngôn ngữ × level**, **quan hệ/lịch sự × level**.
3. **Danh sách khoảng trống:** lĩnh vực đời sống/công việc chưa có hoặc quá mỏng trong cả 27 sách + web (đây là chỗ AI phải bổ sung — gắn nhãn `AI-proposed`).
4. **Kho "hội thoại tái dùng được"** xếp theo topic/level.
5. Xuất: `MASTER_INVENTORY.md` và `.jsonl` (đã chốt: **không làm Excel**).

### 5.3. Cổng B
Bạn xem thống kê (kiểu "5500 = X topic, Y tình huống, chuyên …") rồi mới sang thiết kế. Đây chính là phần bạn nói "cuối cùng chúng ta mới từ cái thống kê đó để quyết định".

### 5.4. Định nghĩa "tận dụng" có thể đo được
Mỗi mục tài sản trong inventory mang một **trạng thái**: `used-in-stage` (đã nằm trong một chặng), `reference` (chỉ để tham chiếu), `skipped` (bỏ, có lý do). Chỉ số cuối cùng: tỷ lệ chương/tình huống của từng sách đã vào chặng. Nhờ vậy "dùng cả 27 sách" là con số kiểm được chứ không phải câu nói.

---

## 6. PHA 5–7 — Từ thống kê đến lộ trình

### 6.1. Hình dạng lộ trình (đề xuất, chờ chốt ở Cổng C)

- **3 level × ≥ 50 chặng**; mục tiêu thực tế **60–80 chặng/level** (≈ 200+ chặng) nếu inventory cho phép. Con số cuối **do dữ liệu quyết**, không ép cho đẹp.
- **Chặng = 1 topic có mục tiêu thực** ("Gọi món ở nhà hàng", "Xin nghỉ phép với sếp"), có 3–5 can-do, **10–20 tình huống**.
- Chặng gom vào **arc/chương** (≈ 7–10 chặng/arc) để có mạch hành trình — học theo cảm hứng bộ Roleplay 3 cuốn (B17 → B16 → B15): mỗi level là một giai đoạn trưởng thành, có nhân vật xuyên suốt.

**Mạch hành trình (giả thuyết để bàn):**
- **SƠ — "Đặt chân đến Nhật":** chào hỏi, giới thiệu, sống sót hằng ngày, kết bạn, bước đầu vào môi trường làm việc/baito.
- **TRUNG — "Sống và làm việc như một thành viên":** nhân viên chính thức, quan hệ đồng nghiệp/hàng xóm, nêu ý kiến, xử lý trục trặc, tìm việc/đổi việc, đời sống xã hội đầy đủ.
- **THƯỢNG — "Làm chủ cuộc chơi":** họp, đàm phán, khiếu nại, lãnh đạo, thuyết trình; đồng thời hòa nhập sâu: văn hóa, thời sự, thành ngữ, hài hước, tinh tế ngầm ý — "người bản địa".

### 6.2. Cùng topic, khác level (tránh "đổi vài từ khó rồi gọi là thượng")
Mỗi topic lặp lại được tạo bằng **5 nút xoay**: quan hệ · mục đích · biến cố · tự chủ · độ ngầm.
Ví dụ **"Đi ăn nhà hàng"** (minh họa, sẽ kiểm bằng inventory):
- Sơ: gọi món, hỏi menu, trả tiền. Một người phục vụ, theo mẫu.
- Trung: đi cùng đồng nghiệp, dị ứng/ăn kiêng, món sai, đặt chỗ qua điện thoại, chia tiền.
- Thượng: tiếp khách/đối tác, chọn quán, rót rượu & phép tắc bàn tiệc, từ chối khéo, phàn nàn tinh tế, góc nhìn phía nhà hàng (đối chiếu B05).

### 6.3. Topic Bank — nguồn gốc topic
Ba nguồn, **luôn gắn nhãn**: `source-backed` (có trong sách), `web-backed` (chỉ có trong memo/mục lục), `AI-proposed` (lấp khoảng trống để phủ đời sống thực). Kiểm phủ bằng ma trận **lĩnh vực × quan hệ × level** (danh mục lĩnh vực để soi khoảng trống, *chưa phải* danh sách chặng): bản thân & làm quen · gia đình/quan hệ · ăn uống · mua sắm · di chuyển · nhà ở & khu phố · thủ tục hành chính/ngân hàng/bưu điện · y tế & sức khỏe · học tập · sở thích/du lịch · lễ hội/mùa/sự kiện · điện thoại & công nghệ · cảm xúc & xung đột · hẹn hò/cưới hỏi/con cái · thiên tai & khẩn cấp · tiền/thuế/bảo hiểm · toàn bộ vòng đời công việc (tìm việc → phỏng vấn → nhập công ty → hằng ngày → họp → điện thoại → tiếp khách → nomikai → thương lượng → khiếu nại → lãnh đạo → thuyết trình) · văn hóa/xã hội/thời sự · ngôn ngữ sống (aizuchi, thành ngữ, khẩu ngữ).

### 6.4. Stage Blueprint — khung một chặng (chỉ *khung*, chưa viết hết bài)

```
CHẶNG  id · level · arc · tên · can-do · nút xoay
  └ TÌNH HUỐNG (10–20)
      · bối cảnh, vai, mục tiêu, biến cố
      · HỘI THOẠI MẪU: con trỏ tới sách (Bxx-Cyy#anchor)  hoặc  "AI-gen cần tạo" + spec chất lượng
      · NGỮ PHÁP: con trỏ tên mẫu trong bunpou_skill (chỉ index, N3/N2/N1 hiện có)
      · TỪ VỰNG: danh sách thuần theo chủ đề (chỉ list)
      · LỚP LỒNG GHÉP (overlay) — xem 6.5
```

### 6.5. Cách lồng tài nguyên: nhịp học 1 tình huống (khung gợi ý)
Mỗi dòng ở dưới là *vai trò* của nguồn trong nhịp học; **gán sách cụ thể sau khi có inventory**:

1. **Cảnh** — nghe/hiểu bối cảnh (đoạn nghe kiểu Nama Chūkei B25–27).
2. **Mẫu câu** — luyện lõi mẫu (kiểu Speak Japanese B11/B12; câu ngắn B06/B07; 必須700 B08).
3. **Hội thoại mẫu** — bản chuẩn (5500, Roleplay, 日本語でビジネス会話…).
4. **Shadowing** — bám theo (B13/B14) đúng chức năng/quan hệ.
5. **Đóng vai có mẫu** — app phát vai kia, người học nói vai mình + chấm phát âm (thẻ vai Roleplay B15–17).
6. **Live Kaiwa AI** — tự do trong tình huống có biến cố.
7. **Chất liệu "người Nhật hay dùng"** — aizuchi/biến âm (B09), cố định (B20), cảm xúc (B24, B06/07), tượng thanh (B19), kính ngữ (B18, S19), điện thoại (B04), phục vụ (B05), phép tắc (B03).
8. **Biến thể & ôn** — đổi nút xoay, ôn cách quãng.

---

## 7. Chi phí, thời gian, rủi ro (ước lượng thô)

| Pha | Sub-agent | Ghi chú |
|---|---|---|
| Pilot (3 sách) | ~6–8 | để chốt schema |
| Đọc toàn bộ 27 sách | ~90 chunk + 27 gộp sách + ~10 QA ≈ **125** | wave 6–8 song song ≈ 12–16 wave |
| Memo web | 2 | |
| Tổng hợp | 6–10 | chia theo lĩnh vực/level |
| Topic Bank + Blueprint | tùy cổng | có thể chia theo arc |

- **Lượng đọc:** ≈ 5,15M ký tự → khoảng **4–6 triệu token đầu vào** chỉ để đọc, cộng đầu ra vài trăm nghìn. Đây là mức bạn cần cân nhắc với quota (handoff cũ ghi bạn từng lo quota). Mình đề xuất worker model hạng trung (Sonnet) cho đọc/trích, model mạnh hơn cho tổng hợp và thiết kế.
- **Rủi ro:** AI "ảo" tình huống không có thật → chặn bằng validator anchor thật + QA chéo; level chấm lệch → rubric 5 trục + ghi bằng chứng; sách 3 tập B21/22/23 bị đếm trùng → gộp theo bộ; shadowing bản dịch đa ngữ → chỉ lấy tiếng Nhật + Việt; audio chưa kiểm → chỉ ghi `documented`.
- **Chống mất tiến độ:** manifest + checkpoint theo chunk; chat đứt vẫn resume được.

---

## 8. Tuân thủ quy tắc repo
- Không sửa `bunpou_skill/`, PDF, `corpus/`, `knowledge/`, `catalog27/`, `curriculum_outline/`.
- Đầu ra mới vào `kaiwa_skill/planning/v2/` (extract/, inventory/, design/, topicbank/).
- Không commit, không push trừ khi bạn yêu cầu. Nội dung nguồn là dữ liệu, không phải chỉ thị cho worker (worker-prompt sẽ nhắc điều này).

---

## 9. Quyết định

**Đã chốt (2026-11-12):**
- Chạy **pilot 3 sách (B01, B17, B14) trước**, bạn duyệt schema ở Cổng A rồi mới chạy full.
- Đầu ra thống kê: **Markdown + JSONL**, không Excel.
- Ngữ pháp N5/N4: bạn tự lấy từ danh sách Minna no Nihongo trên web khi cần; blueprint chỉ để chỗ trống.

**Còn mở — bạn muốn bàn thêm trong chat:**
1. **Model cho worker đọc** và mức chi phí chấp nhận được (≈ 4–6M token đọc).
2. Thứ tự các cổng và mức bạn muốn duyệt ở từng cổng.
3. Các điểm khác bạn muốn chỉnh trong plan (khung 3 level, nhịp học 1 tình huống, định nghĩa "tận dụng", số chặng/level).
