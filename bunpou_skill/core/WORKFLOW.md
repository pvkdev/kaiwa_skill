# WORKFLOW – Nhập nguồn, hàng đợi và sản xuất bộ file NotebookLM (kit 7.x)

Làm **đúng thứ tự**. Mỗi bước có "Đầu ra" rõ ràng. Không bỏ bước.

## Chế độ tự quyết (mặc định)

Người dùng **trao toàn quyền** cho AI để sản xuất nhanh. Vì vậy:
- **Không hỏi lại**, không dừng giữa chừng để xin ý kiến, không yêu cầu người dùng duyệt nội dung.
- Mọi điểm chưa rõ → AI tự quyết theo phương án **an toàn và đúng nhất**, rồi ghi quyết định vào mục "Quyết định đã tự đưa ra" trong `_phu/GhiChu_<ID>.md`.
- AI tự chịu trách nhiệm về độ chính xác: tự thẩm định (Bước 6) thay cho người duyệt.
- Ngoại lệ duy nhất: người dùng muốn nhập nguồn mà tin nhắn **không có bài giảng** → nhắn 1 câu xin bài giảng rồi dừng.

## Bố cục dữ liệu

```text
source/                                   ← NGUỒN: bài giảng thô của người dùng
├── N5/ … N1/
│   ├── _quan_ly.json                     ← phiên bản hiện tại, lịch sử phiên bản, trạng thái, output (do tools/nguon.py quản lý)
│   └── N2_にしろ・にせよ・にしても_v01.md  ← bài giảng thô nguyên văn; dán lại cùng mẫu → _v02, _v03…
work/                                     ← OUTPUT: mỗi lần chạy một thư mục
├── _index.js, _hang_doi.json             ← công cụ tự sinh
└── N5/ … N1/
    └── N2_にしろ・にせよ・にしても_v01_r01/   ← <ID> = tên nguồn + _rNN (lần chạy); chạy lại → _r02
        ├── KichBan_<ID>.md               ← AI viết. File DUY NHẤT tải lên NotebookLM cho bài này
        └── _phu/
            ├── BaiGoc_<ID>.md            ← công cụ chép từ source/ (nguon.py bat-dau)
            ├── GhiChu_<ID>.md            ← AI viết (nhật ký biên tập)
            └── meta_<ID>.json, TuyChinh_<ID>.txt, data.js   ← công cụ tự sinh
old/                                      ← bài làm trước kit 7 (chỉ để lưu, không còn dùng)
```

Dùng chung cho mọi bài, nằm ở gốc dự án, **không chép vào thư mục bài**: `guide.md` (người dùng tải lên NotebookLM 1 lần)
và `HuongDan.html` (trang làm video, đọc dữ liệu từ `work/`). **Không** tự viết meta, TuyChinh, data.js, HTML hay `_quan_ly.json`.
**Không sửa, không xóa file trong `source/`** (đó là bài giảng gốc của người dùng) – chỉ thêm qua `tools/nguon.py them`.

## Ba chế độ làm việc

| Người dùng nói / làm | Chế độ |
| --- | --- |
| Dán một hoặc nhiều bài giảng thô ("nhập nguồn", "thêm vào source", hoặc chỉ dán bài) | **A – Nhập nguồn** |
| "chạy hàng đợi", "chạy hàng loạt", "chạy N2", "/bunpou-video chạy" | **B – Hàng đợi** → lần lượt **C** cho từng mẫu |
| Dán bài + "làm video luôn" / "chạy luôn" | **A** rồi **C** cho đúng các bài vừa nhập |
| "chạy lại <mẫu>", "làm lại bài <ID>" | **C** với file nguồn của mẫu đó (tạo lần chạy mới `_rNN`) |

### Chế độ A – Nhập nguồn (không viết kịch bản)

1. Chép **nguyên văn** phần người dùng dán vào một file tạm (vd `tmp_nhap.md` ở gốc dự án). Nhiều bài trong một lần dán →
   chèn dòng `---BÀI N2---` (cấp độ của bài đó) trước mỗi bài. Không sửa chữ nào của bài giảng.
   - Cấp độ: theo lời người dùng; không có → dòng "Cấp độ: Nx" trong bài; vẫn không có → tự xác định theo JLPT và nói rõ trong báo cáo.
   - Tên mẫu: công cụ lấy dòng tiếng Nhật đầu tiên của bài (vd `～にしろ／にせよ／にしても`). Dòng đầu không phải tên mẫu → chèn
     tên mẫu làm dòng đầu của bài đó, hoặc dùng `--mau "〜…"` khi chỉ có 1 bài.
2. Chạy `python tools/nguon.py them tmp_nhap.md` (thêm `--cap N2` nếu mọi bài cùng cấp và không ghi ở dòng ngăn), rồi xóa file tạm.
   Công cụ tự đặt tên `<cấp>_<mẫu>_vNN.md`, bỏ qua bài trùng nguyên văn, đưa phiên bản cũ vào lịch sử, cập nhật `_quan_ly.json`.
3. Báo cáo: danh sách file đã thêm / bị bỏ qua (trùng), và số mẫu đang chờ trong hàng đợi (`python tools/nguon.py hang-doi`).

### Chế độ B – Hàng đợi

1. Chạy `python tools/nguon.py hang-doi` (có thể `--cap N2`, `--so 10`). Hàng đợi gồm: mẫu chưa chạy / đang chạy dở / lần trước còn lỗi,
   và mẫu ghi "đã có output" nhưng `work/` không có bài hợp lệ. Danh sách ghi ở `work/_hang_doi.json`.
2. Làm **lần lượt từng mẫu** theo Chế độ C. Một mẫu lỗi sau 3 vòng sửa → để trạng thái "lỗi", ghi lại, **chuyển sang mẫu tiếp theo**.
   (Công cụ hỗ trợ subagent / tác vụ song song: mỗi mẫu một thư mục riêng, `_quan_ly.json` có khóa ghi.)
3. Kết thúc: chạy `python tools/nguon.py trang-thai`, báo cáo bảng ngắn: mẫu đã xong (ID), mẫu lỗi (lý do), số mẫu còn lại.

### Chế độ C – Sản xuất một mẫu = Bước 1 → Bước 7 bên dưới

---

## Bước 1 – Bắt đầu bài (công cụ tạo thư mục)

- Chạy `python tools/nguon.py bat-dau source/<cấp>/<tên file nguồn>` (hoặc mã mẫu `N2_<mẫu>` → phiên bản hiện tại). Công cụ:
  - tạo `work/<cấp>/<ID>/_phu/` với `<ID>` = tên nguồn + `_rNN` (lần chạy tiếp theo, không ghi đè lần trước);
  - chép bài giảng vào `_phu/BaiGoc_<ID>.md` (dòng đầu `Cấp độ: <cấp>`);
  - đánh dấu nguồn "đang chạy" và in **gợi ý nhân vật** (`rules/06_nhan-vat.md`) cho mục 1 và câu Kết.
- Không tự đặt ID, không tự tạo thư mục trong `work/`. Đọc bài gốc từ `_phu/BaiGoc_<ID>.md`.

## Bước 2 – Phân tích bài gốc (ghi kết quả vào Ghi chú biên tập)

1. Tên mẫu, nghĩa ngắn gọn nhất (≤ 10 từ).
2. **Cấu trúc như bài gốc**: chép lại các dòng cấu trúc của bài gốc (V…/A…/N… + mẫu), chỉ chuẩn hóa 〜 ／ ＋ và sửa lỗi thật.
   Thuật ngữ Nhật (名詞, 動詞…) đổi sang tiếng Việt hoặc ký hiệu N, V, A.
3. Các **cách dùng** riêng biệt. Mỗi cách dùng → 1 chương `## 3.x Cách dùng x: <tên>` (luôn viết số bằng chữ số: Cách dùng 1, 2, 3…).
   **Chỉ có MỘT cách dùng** → `## 3.1 Cách dùng: <tên>`, không đánh số, không nói "cách dùng 1" ở bất kỳ đâu. Đặt tên cách dùng:
   - Các cách dùng khác nhau về hình thức (vd ところに／へ, ところを) → `<hình thức> – <mô tả ngắn>`.
   - Cùng một hình thức (vd 2 cách dùng của うちに) → chỉ `<mô tả ngắn>`.
   - Mẫu có nhiều biến thể cùng một nghĩa (vd なんて／とは, にしろ／にせよ／にしても) → gộp thành một cách dùng, khác biệt ở dòng "Sắc thái".
   - Ghi chú nhỏ của bài gốc (bỏ lửng vế sau, có/không だ, thân mật/trang trọng) **không** tách thành cách dùng riêng:
     đưa vào phần Ý nghĩa (Khi nào dùng / Không dùng khi / Sắc thái) hoặc phần Cách chia của cách dùng đó, nhắc lại ở mục 5.
   - Phần **"cách nói thường gặp"** của bài gốc (cụm cố định như いずれにせよ, nghi vấn từ ＋ mẫu) → mỗi cụm 1 chương
     `## 3.x Cách nói thường gặp: <cụm>`, đặt sau mọi cách dùng, 1–3 ví dụ. Không ép thành cách dùng hay thẻ cấu trúc.
4. **Gán cấu trúc cho từng cách dùng** (thẻ Cấu trúc đánh số liên tục cả bài):
   - Bài gốc ghi cấu trúc riêng cho từng cách dùng → mỗi cách dùng giữ đúng các dòng của nó.
   - Cấu trúc dùng chung → thẻ đầy đủ ở cách dùng đầu tiên; cách dùng sau mở đầu Cách chia bằng `**Giống cách dùng n:**` + nhắc lại ngắn,
     rồi chỉ thêm thẻ cho phần **khác** (vd ところで gần như luôn V た).
   - **Được gộp** các dòng chỉ khác nhau ở biến thể (vd 3 dòng `A ＋ にしろ、B ＋ にしろ` / `…にせよ` / `…にしても` → 1 thẻ
     `A ＋ にしろ／にせよ／にしても、B ＋ (cùng dạng)`). Ghi việc gộp vào Ghi chú. Mục tiêu: mỗi cách dùng 1–4 thẻ dễ nhớ.
5. Toàn bộ ví dụ trong bài gốc, gán vào đúng chương, giữ thứ tự bài gốc. Câu trùng hoặc gần trùng chỉ tính **một** lần.
6. **Lỗi trong bài gốc** theo định nghĩa ở `rules/01_noi-dung.md` (mục "Thế nào là lỗi") → tự sửa.
7. **Chọn 4–6 ví dụ cho MỖI cách dùng** (chương cách nói thường gặp: 1–3) và **phủ mọi thẻ cấu trúc** theo `rules/01_noi-dung.md` mục 4.
   Không đủ → viết thêm `[MỚI]` vừa đủ. Câu bị lược ghi vào Ghi chú biên tập.
   Lập **Bảng phủ ví dụ** trong Ghi chú (ví dụ nào → phần 3.x nào → thẻ cấu trúc nào) **trước** khi viết Kịch bản.
8. **Chuẩn bị phần Ý nghĩa của từng cách dùng** (`rules/02_giong-van.md` mục "Giảng ý nghĩa"): bản chất, so với tiếng Việt,
   câu mẫu ngắn, khi nào dùng, không dùng khi, sắc thái. Tự hỏi: chỉ đọc phần này, người học có trả lời được
   "nghĩa là gì, dùng khi nào, khác cách dùng kia ở đâu" không? Chưa được → viết lại.

## Bước 3 – Viết Kịch bản

- File: `work/<cấp>/<ID>/KichBan_<ID>.md`
- Chép `core/templates/KichBan.template.md`, điền theo đúng các rule `01`–`06` (nhân vật theo gợi ý in ra ở Bước 1) và hồ sơ cấp độ trong `05_cap-do.md`.
- Giữ nguyên **tất cả** tiêu đề, nhãn in đậm, thứ tự.
- Khung 6.1 (lộ trình video: intro → tình huống → giới thiệu & mô tả mẫu → từng cách dùng → bẫy → tổng kết):
  1 Mở màn: tình huống → 2 Giới thiệu mẫu ngữ pháp (Mẫu, Nghĩa, Mô tả 2–4 ý trên màn hình, Lời giảng dẫn từ tình huống, gọi tên mẫu) →
  **mỗi cách dùng một chương** `## 3.x` gồm `### Ý nghĩa và cách dùng` → `### Cách chia` → các `### Ví dụ` → (tùy chọn) chương `Cách nói thường gặp` → 4 Bẫy → 5 Tổng kết.
  Không có mục "Tổng quan"; mục 2 không liệt kê các cách dùng thành danh sách (video sẽ dựng thành khung mục lục).
- Trước khi viết mục 1, làm theo `rules/02_giong-van.md` mục "Mở bài và kết bài": chọn câu muốn nói, dựng logic tình huống,
  đọc thử như lời giảng và đối chiếu câu Kết. Gợi ý ngoại hình không phải nội dung bắt buộc để đọc lên.
- Mục 5 có thể thêm `**Tình huống thực tế:**` (công việc / cuộc sống / giao tiếp) và `**Người Nhật thường nói:**` (1–4 câu Nhật / Việt / Ý).
  Chỉ viết khi chắc chắn tự nhiên; không có thì bỏ cả nhãn.
- Mỗi ví dụ theo trình tự **Tình huống → Câu Việt → Câu Nhật (sạch) → Tô màu → Tô màu Việt → Cách ghép** (`rules/03_vi-du.md`).
  Dòng Cách ghép **mở đầu bằng 「<Câu Nhật nguyên văn>」** để video đọc trọn câu ví dụ trước khi giảng,
  rồi **nói rõ ví dụ dùng dạng cấu trúc nào** (vd "Đây là dạng V た ＋ ところで.") – khớp với Bảng phủ ví dụ.
- Câu mẫu, bẫy, câu người Nhật thường nói, câu kết cũng theo dòng Nhật / Việt (`rules/04_tieng-nhat.md`).
- Không dòng cách đọc, không furigana, không ký hiệu ruby 《 》, ngoặc cách đọc, 【 】 ở bất kỳ đâu. Không gạch đầu dòng trước câu Nhật/Việt.
- **Không** viết câu đố, quiz, hỏi đáp ở bất kỳ mục nào.
- Đối chiếu với ví dụ chuẩn `core/examples/N3_tokoro-ni-he-wo-de/KichBan_N3_tokoro-ni-he-wo-de.md` về độ dài, nhịp, độ hài.
  Chỉ học định dạng và chất lượng; tình huống, mở màn luôn viết mới (kể cả khi làm lại đúng bài của ví dụ chuẩn).

## Bước 4 – Viết Ghi chú biên tập (nhật ký, người dùng không cần đọc)

- File: `work/<cấp>/<ID>/_phu/GhiChu_<ID>.md` theo `core/templates/GhiChuBienTap.template.md`.
- Phần đầu **bắt buộc** đủ các dòng `- Cấp độ:`, `- Phiên bản quy tắc:` (đọc file `VERSION`), `- Ngày tạo: YYYY-MM-DD`,
  `- Công cụ AI / model:` – công cụ đọc các dòng này để sinh meta.
- Ghi: phân tích, lỗi đã sửa, ví dụ được chọn / bị lược / `[MỚI]`, quyết định đã tự đưa ra, kết quả tự thẩm định.

## Bước 5 – Chạy kiểm tra (tự sinh file phụ + cập nhật trang HuongDan.html)

- Chạy `python tools/validate.py work/<cấp>/<ID>` (Windows có thể dùng `py`). Lệnh này:
  1. kiểm tra Kịch bản + Ghi chú;
  2. tự sinh `_phu/meta_<ID>.json`, `_phu/TuyChinh_<ID>.txt` (từ `core/templates/TuyChinh.template.txt`), `_phu/data.js`;
  3. ghi trạng thái vào `source/<cấp>/_quan_ly.json` (ĐẠT → "đã có output", còn lỗi → "lỗi");
  4. dựng lại `work/_index.js` → người dùng chỉ cần tải lại (F5) trang `HuongDan.html` là thấy bài mới, được chọn sẵn.
- Không chạy được Python → tự kiểm theo **Checklist tự kiểm** bên dưới, tự điền `_phu/TuyChinh_<ID>.txt` theo template,
  và ghi trong báo cáo: "cần chạy `python tools/build_data.py` để bài hiện trên HuongDan.html".

## Bước 6 – Tự thẩm định và sửa (thay cho người duyệt)

1. **Tự thẩm định nội dung** – đọc lại Kịch bản với vai một giáo viên tiếng Nhật khó tính:
   - Mở màn: người nghe có hiểu nguyên nhân, sự việc và ý muốn nói khi không nhìn hình? Câu Nhật đích có đúng thời điểm, chủ thể,
     quan hệ giao tiếp và sắc thái? Mục 2 và câu Kết có quay lại đúng chuyện ấy? Theo checklist tại `rules/02_giong-van.md`.
   - Từng câu tiếng Nhật do AI tự viết (ví dụ `[MỚI]`, câu mẫu, cụm trong Giải thích, bẫy, câu người Nhật thường nói, câu kết): có tự nhiên, đúng ngữ pháp, đúng cách dùng không?
   - Dòng `Tô màu` có chép đúng và chỉ đúng phần mẫu ngữ pháp không? Dòng `Tô màu Việt` có đúng cụm nghĩa tương ứng trong câu Việt không?
   - Câu Việt có đúng nghĩa, đầy đủ, tự nhiên không? "Cách ghép" có giải thích đúng cách chia không?
   - Câu nào **không chắc 100% → thay bằng câu đơn giản hơn mà chắc chắn đúng** (hoặc bỏ bẫy đó). Không để lại điểm nghi ngờ cho người dùng.
2. Có `LỖI` → sửa → chạy lại `python tools/validate.py work/<cấp>/<ID>`. Tối đa 3 vòng.
3. `CẢNH BÁO` → tự quyết sửa hay giữ; nếu giữ thì ghi lý do vào Ghi chú biên tập.
4. Sau lần chạy cuối: cập nhật mục "Kết quả kiểm tra" của `_phu/GhiChu_<ID>.md` bằng kết quả thật, rồi chạy validate thêm 1 lần.
5. **Không** tự mở trình duyệt hay thư mục (người dùng giữ sẵn trang HuongDan.html và chỉ cần F5).

## Bước 7 – Báo cáo cho người dùng (trong chat, ngắn gọn)

Viết bằng **markdown thường – KHÔNG đặt báo cáo trong khối code** (trong khối code, link không bấm được). Theo đúng mẫu:

> ✅ **Đã tạo:** `work/<cấp>/<ID>/KichBan_<ID>.md` – F5 trang HuongDan.html để làm video
> - Mẫu: <mẫu> – <nghĩa> | Cấp độ: <CAP_DO>
> - Cách dùng: <n> | Ví dụ: <tổng> (trong đó [MỚI]: <m>, đã lược: <l> = số ví dụ bài gốc không được chọn)
> - Đã tự sửa trong bài gốc: <k> điểm | Quyết định đã tự đưa ra: <q> (= số gạch đầu dòng ở mục 4 của Ghi chú biên tập)
> - Kiểm tra: tự thẩm định xong, validate.py ĐẠT (<số cảnh báo> cảnh báo)
>
> <KHỐI "📂 Mở nhanh">

(Dấu `>` ở trên chỉ để trình bày mẫu trong file này; khi báo cáo thì không cần.)
Không viết "cần duyệt", không hỏi người dùng có muốn sửa gì không.

**Khối "📂 Mở nhanh" – bắt buộc:**
- Lấy **nguyên văn** khối mà `validate.py` in ra sau dòng "Dán NGUYÊN VĂN…" (hoặc chạy `python tools/validate.py work/<cấp>/<ID> --links`).
- Không tự sửa đường dẫn, không rút gọn, không bọc trong khối code.
- Không chạy được Python → tự viết theo đúng định dạng validate.py in ra:
  - `- [HuongDan.html](HuongDan.html) – trang làm video`
  - `- [KichBan_<ID>.md](work/<cấp>/<ID>/KichBan_<ID>.md) – nguồn tải lên NotebookLM cho bài này`
  - `- [📁 <ID>/](work/<cấp>/<ID>/) – thư mục bài`
  - `- [guide.md](guide.md) – nguồn chung – chỉ tải lên NotebookLM 1 lần`

---

## Checklist tự kiểm (khi không chạy được validate.py)

- [ ] Kịch bản theo khung 6.1: mục 1, mục 2 (Mẫu, Nghĩa, Mô tả, Lời giảng), các chương `## 3.x Cách dùng x:` (mỗi chương: `### Ý nghĩa và cách dùng` → `### Cách chia` → `### Ví dụ`), chương `Cách nói thường gặp` (nếu có), 4 Bẫy, 5 Tổng kết
- [ ] Mở màn đã kiểm logic và đọc thử theo rule 02; câu muốn nói nảy sinh trực tiếp từ tình huống, khớp Lời giảng mục 2 và câu Kết
- [ ] Ý nghĩa mỗi cách dùng có: Trên màn hình, Bản chất, So với tiếng Việt, Câu mẫu (Nhật / Tô màu / Tô màu Việt / Việt), Khi nào dùng, (Không dùng khi), (Sắc thái), Dấu hiệu nhận biết; lời giảng ≥ 100 từ
- [ ] Cách chia: thẻ `**Cấu trúc n:**` + `**Giải thích:**` đánh số liên tục cả bài; cách dùng sau dùng `**Giống cách dùng n:**` khi chia giống
- [ ] Mỗi chương cách dùng 4–6 ví dụ; chương cách nói thường gặp 1–3; Bảng phủ (| Ví dụ | Phần | Cấu trúc | Nguồn |) đủ mọi ví dụ, mọi thẻ cấu trúc có ví dụ
- [ ] Mỗi ví dụ có đủ 6 nhãn: Tình huống, Câu Việt, Câu Nhật, Tô màu, Tô màu Việt, Cách ghép
- [ ] Bài chỉ có 1 cách dùng: tiêu đề `## 3.1 Cách dùng: …` không số, không có chữ "cách dùng 1" ở đâu cả
- [ ] Câu Nhật sạch; Tô màu là đoạn có trong câu Nhật; Tô màu Việt là đoạn có trong câu Việt; không dòng Cách đọc; không 《 》 【 】 ｜
- [ ] Mỗi dòng Cách ghép mở đầu bằng 「<Câu Nhật>」 chép y nguyên, rồi nói "Đây là dạng …" (hoặc "Đây là cụm …")
- [ ] Không có câu đố, quiz, "Đáp án"; không còn `{{`; không romaji trong Kịch bản
- [ ] Gốc thư mục bài chỉ có `KichBan_<ID>.md`; `_phu/` có `BaiGoc_<ID>.md`, `GhiChu_<ID>.md` (đủ dòng Cấp độ, Phiên bản quy tắc, Ngày tạo, Công cụ AI / model), `TuyChinh_<ID>.txt`
- [ ] Không chép `guide.md` hay HTML vào thư mục bài
