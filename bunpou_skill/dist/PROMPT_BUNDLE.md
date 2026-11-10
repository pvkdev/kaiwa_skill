# BỘ PROMPT LÀM VIDEO NGỮ PHÁP TIẾNG NHẬT (chế độ chat)

Phiên bản quy tắc: 7.2.0

## Cách dùng file này
Người dùng tải file này lên (hoặc dán vào) một AI dạng chat, sau đó gửi: `ID: <ID>` (do `tools/nguon.py bat-dau` tạo trên máy) + bài giảng thô + cấp độ.

## Chỉ dẫn cho AI ở chế độ chat
Bạn KHÔNG có thư mục dự án và KHÔNG chạy được Python. Vì vậy:
1. Làm đúng QUY TRÌNH bên dưới, Chế độ C (Bước 2 → Bước 7), bỏ qua các thao tác nhập nguồn/tạo thư mục/chạy lệnh.
   Dùng đúng `<ID>` người dùng gửi (dạng `N2_<mẫu>_v01_r01`); thiếu ID thì xin ID trước khi viết. Tự chọn nhân vật theo rule 06.
2. Xuất lần lượt từng file trong MỘT câu trả lời, mỗi file đặt trong một khối code, ngay trước mỗi khối ghi dòng:
   `=== FILE: <tên file> ===`
   Chỉ 2 file, theo thứ tự: KichBan_<ID>.md → GhiChu_<ID>.md
3. KHÔNG xuất meta, TuyChinh, guide hay HTML (công cụ `tools/split_chat_output.py` trên máy người dùng tự sinh / dùng chung).
4. Trước khi trả lời, tự kiểm theo "Checklist tự kiểm" trong QUY TRÌNH và ghi kết quả vào GhiChu_<ID>.md mục 5 là "kiểm thủ công".
5. Nếu câu trả lời bị cắt giữa chừng, khi người dùng gõ "tiếp", hãy tiếp tục đúng từ file đang dở.

Tất cả các phần dưới đây là quy tắc bắt buộc.


---

## [Quy tắc tổng] `AGENTS.md`

````
# AGENTS.md – Quy tắc bắt buộc cho mọi AI làm việc trong dự án này

> File này là điểm vào chung cho Codex, Cursor, Gemini CLI, Claude Code và mọi AI agent khác.
> Phiên bản quy tắc: xem file `VERSION`.

## 1. Dự án này làm gì

Biến **một bài giảng ngữ pháp tiếng Nhật thô** + **cấp độ mục tiêu (N5–N1)** thành **bộ file đầu vào cho NotebookLM**
để NotebookLM dựng video bài giảng tiếng Việt: thân mật, hài hước, nhịp nhanh, **ví dụ phủ hết mọi cách dùng và mọi dạng cấu trúc**, nghe một lần là nhớ.
Thời lượng không giới hạn. Lộ trình video: intro → tình huống → **giới thiệu & mô tả mẫu** → **mỗi cách dùng một chương** Ý nghĩa (giảng kỹ) → Cách chia → toàn bộ ví dụ → bẫy → tổng kết.
**Sản xuất hàng loạt (kit 7):** bài giảng thô nằm ở `source/<cấp>/<cấp>_<mẫu>_vNN.md` (quản lý phiên bản + trạng thái trong
`source/<cấp>/_quan_ly.json`), output nằm ở `work/<cấp>/<ID>/` với `<ID>` = tên nguồn + `_rNN`. Mọi thao tác trên source/work
đi qua `tools/nguon.py` (nhập nguồn, hàng đợi, bắt đầu bài). Bài làm trước kit 7 nằm trong `old/` (không dùng nữa).
Mỗi bài AI chỉ viết **2 file**: `work/<cấp>/<ID>/KichBan_<ID>.md` (file duy nhất tải lên NotebookLM)
và `work/<cấp>/<ID>/_phu/GhiChu_<ID>.md`. Bài gốc do `nguon.py bat-dau` chép sẵn; các file phụ còn lại do `tools/validate.py` tự sinh.
Dùng chung cho mọi bài, nằm ở gốc dự án: `guide.md` (quy tắc dựng video, người dùng tải lên NotebookLM 1 lần) và
`HuongDan.html` (trang làm video: danh sách bài theo cấp độ, tìm kiếm, nút copy). Không chép 2 file này vào thư mục bài.

AI **không** làm video. AI chỉ nhập nguồn vào `source/` (qua `nguon.py them`) và sản xuất bộ file trong `work/<cấp>/<ID>/`.

**Chế độ tự quyết:** người dùng trao toàn quyền để sản xuất nhanh. AI không hỏi lại, không yêu cầu duyệt;
tự quyết theo phương án an toàn nhất, tự thẩm định độ chính xác, ghi quyết định vào Ghi chú biên tập.
Chỉ hỏi lại khi người dùng muốn nhập nguồn mà tin nhắn không có bài giảng.

## 2. Khi nào kích hoạt quy trình

- Người dùng dán bài giảng → **Chế độ A – Nhập nguồn** (chỉ lưu vào `source/`, chưa viết kịch bản – trừ khi người dùng nói "làm luôn").
- "chạy hàng đợi", "chạy hàng loạt", "chạy N2", `/bunpou-video chạy` → **Chế độ B – Hàng đợi**, rồi **Chế độ C** cho từng mẫu.
- Viết kịch bản cho một mẫu (Chế độ C) → **bắt buộc** làm đúng `core/WORKFLOW.md` từ Bước 1 đến Bước 7. Không rút gọn, không đổi thứ tự.

## 3. Thứ tự đọc file (bắt buộc trước khi viết bất cứ thứ gì)

1. `core/WORKFLOW.md` – quy trình từng bước
2. `core/rules/01_noi-dung.md` – độ chính xác nội dung
3. `core/rules/02_giong-van.md` – giọng giảng
4. `core/rules/03_vi-du.md` – định dạng ví dụ
5. `core/rules/04_tieng-nhat.md` – quy tắc câu tiếng Nhật
6. `core/rules/05_cap-do.md` – hồ sơ cấp độ N5–N1
7. `core/rules/06_nhan-vat.md` – chọn nhân vật mới cho mỗi bài (`nguon.py bat-dau` in sẵn gợi ý)
8. `core/templates/` – mọi template đầu ra
9. `core/examples/N3_tokoro-ni-he-wo-de/` – **ví dụ chuẩn (gold standard)**. Đầu ra phải ngang chất lượng và đúng định dạng như ví dụ này.

## 4. Mười điều KHÔNG BAO GIỜ được làm

1. Không thay, không viết lại ví dụ bài gốc. Chọn **4–6 ví dụ cho MỖI cách dùng** từ bài gốc, **mọi thẻ Cấu trúc có ít nhất 1 ví dụ**; chỉ viết `[MỚI]` khi bài gốc không đủ.
2. Không bịa ngữ pháp, không thêm cách dùng mà bài gốc không có (trừ mục "Bẫy dễ nhầm" theo `01_noi-dung.md`).
3. Không viết câu tiếng Nhật mà bản thân không chắc là tự nhiên và đúng ngữ pháp.
4. Không đổi tên tiêu đề, nhãn, thứ tự mục so với template.
5. Không để sót placeholder `{{...}}` trong file đầu ra.
6. Không đưa ghi chú biên tập vào file Kịch bản (ghi chú nằm ở `_phu/GhiChu_<ID>.md`). Không đưa câu đố, quiz, hỏi đáp vào Kịch bản.
7. Không dùng romaji trong file Kịch bản. Mọi câu Nhật trên màn hình đi theo 2 dòng: câu Nhật sạch → câu Việt; không dòng cách đọc, không furigana; mẫu cần tô màu ghi ở dòng `**Tô màu:**` (câu Nhật) và `**Tô màu Việt:**` (cụm nghĩa tương ứng trong câu Việt); không ký hiệu 《 》 【 】 hay ngoặc cách đọc; không gạch đầu dòng trước câu Nhật/Việt.
8. Không sửa file trong `core/`, `guide.md`, `HuongDan.html` khi đang làm một bài (chỉ sửa khi người dùng yêu cầu cập nhật quy tắc).
9. Không tự tạo/đổi tên/ghi đè thư mục trong `work/` (dùng `nguon.py bat-dau` – chạy lại tạo `_r02`, `_r03`…); không sửa/xóa file trong `source/`.
10. Không tuyên bố "xong" khi `tools/validate.py` còn báo LỖI.

**Tính di động:** không bao giờ ghi đường dẫn tuyệt đối (`D:\…`, `/Users/…`, `/home/…`, `file:///…`) vào bất kỳ file nào của dự án.
Trong file chỉ dùng đường dẫn tương đối từ thư mục gốc dự án (vd `work/N2/<ID>/KichBan_<ID>.md`). Đường dẫn tuyệt đối chỉ được
xuất hiện trong báo cáo chat (khối "Mở nhanh" do validate.py tính lúc chạy). validate.py báo LỖI nếu vi phạm.

## 5. Kiểm tra trước khi bàn giao

- Chạy: `python tools/validate.py work/<cấp>/<ID>` (Windows có thể dùng `py`). Lệnh này kiểm tra, tự sinh file phụ trong `_phu/`
  ghi trạng thái vào `source/<cấp>/_quan_ly.json` và cập nhật dữ liệu cho `HuongDan.html`. Không tự viết meta, TuyChinh, data.js, HTML hay json.
- Có LỖI → sửa → chạy lại (tối đa 3 vòng). Còn lỗi sau 3 vòng → báo rõ cho người dùng.
- Không chạy được Python → tự kiểm theo "Checklist tự kiểm" trong `core/WORKFLOW.md` và nói rõ là đã kiểm thủ công.
- Báo cáo cuối luôn kèm khối link **"📂 Mở nhanh"** do `validate.py` in ra (xem Bước 7 của `core/WORKFLOW.md`),
  viết bằng markdown thường, không đặt trong khối code, để người dùng bấm vào mở file ngay.
- Không tự mở trình duyệt/thư mục: người dùng giữ sẵn trang `HuongDan.html`, chỉ cần F5 là thấy bài mới.

## 6. Ngôn ngữ

- Trao đổi với người dùng: tiếng Việt.
- File đầu ra: tiếng Việt + câu tiếng Nhật. Mọi file lưu UTF-8.

## 7. Khi người dùng muốn cập nhật quy tắc

Làm theo `docs/CAP_NHAT_QUY_TAC.md`: sửa đúng file rule liên quan, cập nhật ví dụ chuẩn nếu cần, tăng `VERSION`,
ghi `CHANGELOG.md`, chạy lại `python tools/validate.py core/examples/N3_tokoro-ni-he-wo-de` và `python tools/build_bundle.py`.
````


---

## [Quy trình] `core/WORKFLOW.md`

````
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
````


---

## [Rule 01] `core/rules/01_noi-dung.md`

````
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
````


---

## [Rule 02] `core/rules/02_giong-van.md`

````
# Rule 02 – Giọng giảng và văn phong

Mục tiêu: người xem thấy như được một anh/chị khóa trên vui tính kể chuyện, không phải nghe đọc giáo trình.

## Xưng hô và giọng

- Người giảng xưng **"mình"**, gọi người xem là **"các bạn"**. Không dùng "tôi", "quý vị", "em".
- Thân mật, hài hước, dí dỏm, có nhấn nhá. Dùng cảm thán tự nhiên: "ôi thôi xong", "chuẩn luôn", "nghe quen không?",
  "thấy chưa", "đấy, thế đấy". Mỗi cảm thán không lặp lại quá 2 lần trong một bài.
- Viết như lời nói: câu ngắn, **dưới 20 từ**. Không dùng câu bị động kiểu văn bản ("được thực hiện bởi").
- **Nhịp gọn, rõ:** thời lượng không giới hạn; phần ý nghĩa giảng kỹ, còn mỗi ví dụ thì gọn. Không lặp ý, không rào đón, mỗi câu phải có thông tin mới.
- Giọng vùng miền và nhịp đọc từng ngôn ngữ theo **`guide.md` mục 2.1**. Đây là chỉ dẫn phát âm cho NotebookLM;
  viết tiếng Việt đúng chính tả, không phiên âm giọng địa phương hay chèn chỉ dẫn giọng/tốc độ vào Kịch bản.
- Thuật ngữ ngữ pháp (bị động, thể て, liên từ…) phải được nói lại bằng lời thường ngay sau đó.

## Giảng ý nghĩa – phần quan trọng nhất của bài

Người học nắm bài hay không là ở phần `### Ý nghĩa và cách dùng` của từng cách dùng. Giảng **dễ hiểu, đúng trọng tâm, chi tiết**:

1. **Bản chất** – quan hệ giữa hai vế nói bằng lời thường ("thừa nhận A, nhưng B vẫn giữ nguyên"), kèm **một** hình ảnh so sánh
   đời thường khớp đúng cách dùng đó (không dùng một hình ảnh chung gượng ép cho mọi cách dùng). Giải thích *vì sao* mẫu có nghĩa này
   khi có thể (vd に／へ chỉ đích đến → có người "đi tới" khoảnh khắc đó).
2. **So với tiếng Việt** – giống câu tiếng Việt nào, khác ở đâu, dịch sao cho tự nhiên; chỉ ra chỗ người Việt hay dùng sai.
3. **Câu mẫu** – câu Nhật **ngắn nhất, đời thường nhất** làm lộ nghĩa ngay (tự viết, chắc chắn tự nhiên; không lấy câu ví dụ phía sau).
4. **Khi nào dùng** – hoàn cảnh, vế sau thường là gì (ý kiến, lời khuyên, mong muốn, sự việc…), văn nói hay văn viết.
5. **Không dùng khi** (nếu có) – giới hạn của mẫu, lỗi hay gặp, ranh giới với cách dùng khác.
6. **Sắc thái** (nếu có) – khác nhau giữa các biến thể, độ trang trọng.
7. **Dấu hiệu nhận biết** – từ, dạng câu đi kèm để nhận ra cách dùng này trong đề thi và đời thực.

Tự kiểm: chỉ nghe phần này, người học trả lời được "nghĩa là gì, dùng khi nào, khác cách dùng kia ở đâu" chưa? Chưa → viết lại.
Không viết trừu tượng kiểu "giữ nguyên kết luận dù điều kiện thay đổi" mà không có hình ảnh, câu mẫu cụ thể đi kèm.

## Giới thiệu mẫu ngữ pháp (mục 2)

Ngay sau tình huống, người học phải biết **hôm nay học mẫu gì**: dẫn từ tình huống ("câu đó trong tiếng Nhật dùng mẫu…"),
gọi tên mẫu bằng tiếng Nhật, nói nghĩa, giảng 2–4 ý "Mô tả" (mẫu diễn tả điều gì, bản chất chung), và một hình ảnh so sánh chung.
Có thể nói bằng lời "mẫu này có ba cách dùng", nhưng **không** liệt kê các phần của bài thành danh sách – không làm "mục lục".
Viết số bằng chữ số khi là tên phần: "Cách dùng 1", "Cách dùng 2", không viết "cách dùng một".
**Bài chỉ có một cách dùng:** tiêu đề `## 3.1 Cách dùng: <tên>` không số; lời giảng chỉ nói "cách dùng", không nói "cách dùng 1",
"cách dùng thứ nhất" hay "mẫu này có mấy cách dùng" (người học sẽ tưởng còn cách dùng khác).

## Hài hước

- Hài phục vụ việc nhớ: mỗi câu đùa phải bám vào đúng tình huống của ví dụ.
- Hài đến từ chính tình huống của ví dụ. Không có danh sách chủ đề định sẵn: tự nghĩ cái buồn cười nhất mà tình huống đó cho phép.
- **Cấm:** chế giễu người học, ngoại hình, vùng miền, giới tính, tôn giáo, chính trị, người khuyết tật; nội dung 18+; nói tục.
- Không lặp lại cùng một câu đùa trong một bài (được phép "callback" có chủ đích, tối đa 1 lần).

## Chọn tình huống

Không có danh sách bối cảnh định sẵn. Với mỗi câu, tự nghĩ ra tình huống **đúng nhất** cho câu đó, theo các tiêu chí:

1. **Câu Nhật tự nhiên nhất trong tình huống đó.** Đi từ nghĩa và sắc thái của câu để dựng cảnh, không ép câu vào một bối cảnh có sẵn.
2. **Làm lộ rõ điểm ngữ pháp.** Tình huống phải khiến người xem "thấy" vì sao dùng mẫu này (vd ところを → một cảnh bị bắt gặp đang làm dở).
3. **Hình dung được ngay.** Có ai, ở đâu, đang làm gì, có một chi tiết cụ thể đáng nhớ.
4. **Đa dạng.** Các ví dụ trong cùng một bài không lặp lại cùng một kiểu cảnh hay cùng một câu đùa.
5. **Hợp cấp độ người xem** (xem `05_cap-do.md`) và không thuộc nội dung bị cấm ở trên.

## Mở bài và kết bài

- Mở bài: vào thẳng tình huống. Cấm "Hôm nay chúng ta sẽ tìm hiểu…", "Xin chào các bạn, chào mừng đến với…".
- **Mục 1 là lời kể để nghe, không phải mô tả nhân vật để vẽ tranh.** Viết một cảnh đời thường 40–100 từ, mỗi chi tiết giúp người nghe hiểu chuyện gì xảy ra và vì sao nhân vật muốn nói câu sắp học.
- **Đi từ câu muốn nói rồi mới dựng cảnh:** đọc ý nghĩa, sắc thái, điều kiện dùng của mẫu; chọn một câu Nhật làm đích (ưu tiên câu kết khi cần quay lại cùng cảnh).
  Xác định ai nói với ai, vào lúc nào, muốn diễn đạt điều gì. Dựng hoàn cảnh → sự việc hoặc vướng mắc → ý muốn nói → câu hỏi dẫn vào bài.
- **Kiểm tra logic cụ thể:** nguyên nhân đủ dẫn tới kết quả; thời điểm hiện tại/quá khứ/giả định không lẫn; chủ thể, quan hệ người nói–người nghe,
  mức trang trọng và ý chí phù hợp mẫu. Câu Nhật đích phải là điều người trong cảnh ấy thực sự có thể nói, không chỉ trùng một từ dịch.
- Chỉ giữ nghề, nơi chốn, nhân vật phụ khi chúng làm rõ nguyên nhân hoặc quan hệ cần cho câu nói. Không kể tóc, áo, kính hay liệt kê lý lịch để giới thiệu người.
  Chi tiết ngoại hình chỉ được nhắc nếu chính nó gây ra sự việc và liên quan trực tiếp đến ý muốn nói; dữ liệu minh họa không cần đọc nằm ở Ghi chú biên tập.
- Có thể dí dỏm bằng phản ứng, một chi tiết trớ trêu hoặc hậu quả nhỏ ngay trong sự việc. Không thêm câu đùa, bạn đồng hành hay sự cố ngẫu nhiên chỉ để đủ màu sắc.
- Kết bằng một câu hỏi tự nhiên dẫn đúng ý muốn nói, như "Muốn nói … bằng tiếng Nhật thì nói thế nào?".
  Không ép một cảnh phải giới thiệu hết mọi cách dùng, không giảng trước cả bài.
- **Tự kiểm bằng tai:** đọc riêng mục 1, không nhìn tranh. Người nghe có hiểu chuyện và thấy câu muốn nói nảy ra tự nhiên không?
  Thử bỏ từng chi tiết: không ảnh hưởng cách hiểu thì bỏ. Đối chiếu lại Lời giảng mục 2 và câu Kết để không đổi người, đổi chuyện hoặc mâu thuẫn.
- Nhân vật theo `06_nhan-vat.md`; tính hợp lý của tình huống quyết định việc dùng các gợi ý về nghề, người phụ và bối cảnh.
- Kết bài: quay lại đúng tình huống mở màn, nói lại bằng tiếng Nhật với mẫu vừa học, rồi chào ngắn gọn.
- **Không có câu đố, quiz, hỏi đáp** ở bất kỳ phần nào.

## Độ dài gợi ý từng mục (tính bằng số từ tiếng Việt, không tính câu tiếng Nhật)

**Thời lượng video không giới hạn.** Các con số dưới đây là để lời văn gọn, không phải để video ngắn. Phần Ý nghĩa chỉ có sàn, không có trần.

| Mục | Số từ |
| --- | --- |
| 1. Mở màn | 40–100 |
| 2. Giới thiệu & mô tả mẫu (Mô tả + Lời giảng) | 40 trở lên |
| 3.x Ý nghĩa và cách dùng (Bản chất + So với tiếng Việt + Khi nào dùng + Không dùng khi + Sắc thái) | **≥ 100** (validate.py báo LỖI nếu < 60) |
| 3.x Cách chia – mỗi Giải thích | 15–50 |
| Mỗi ví dụ (Tình huống + Cách ghép) | 60–130 |
| 4. Bẫy | 25–120 |
| 5. Tổng kết | 50 trở lên |

## Không được nhắc đến

"tài liệu", "nguồn", "file", "kịch bản", "hướng dẫn phong cách", "AI", "NotebookLM".
````


---

## [Rule 03] `core/rules/03_vi-du.md`

````
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
````


---

## [Rule 04] `core/rules/04_tieng-nhat.md`

````
# Rule 04 – Quy tắc về câu tiếng Nhật

## Chữ viết

- Dùng chữ Nhật chuẩn: kanji + kana như sách giáo trình. Dấu câu Nhật: `。`, `、`, `？`, `！`, `「」`.
- Cấp N5–N4: hạn chế kanji ngoài danh sách cấp độ; có thể viết kana thay cho kanji khó (vd `ごはん`, `ともだち`).
- Ký hiệu mẫu: dùng `〜` (U+301C) và gạch chéo toàn góc `／` khi liệt kê biến thể: `〜ところに／へ／を／で`.
- Số trong câu: viết như bài gốc (vd `３億円`).

## Không ghi cách đọc – 2 dòng trên màn hình: câu Nhật / câu Việt

- Mọi câu Nhật hiện trên màn hình đi theo đúng 2 dòng: **câu Nhật gốc** ở trên → **câu Việt** ở dưới.
- **Không** dòng cách đọc hiragana, **không** furigana, **không** ghi cách đọc trong ngoặc sau kanji ở bất kỳ đâu.
- Kịch bản **không có ký hiệu ruby 《 》, ｜, 【 】** – NotebookLM chép nguyên ký hiệu lên màn hình (validate.py báo LỖI).
- Câu Nhật dùng kanji/kana như sách giáo trình theo cấp độ (mục "Chữ viết" ở trên); người xem nghe cách đọc qua lời giảng.

## Tô màu mẫu ngữ pháp

- Câu Nhật để sạch; phần cần tô màu ghi ở dòng riêng `**Tô màu:**` (câu mẫu, ví dụ và câu kết), chép **đúng y** đoạn mẫu trong câu Nhật.
- Chỉ ghi **chính mẫu ngữ pháp** (なんて, とは, ところに…), không ghi cả câu. Phần chia/nối phía trước (だ, な, の, đuôi động từ)
  không ghi: câu `静かだなんて` → Tô màu `なんて`.
- Kèm dòng `**Tô màu Việt:**`: cụm nghĩa tương ứng trong câu Việt, chép đúng y (video tô cùng màu). Có ở ví dụ, câu mẫu, câu kết.
- Câu mẫu trong phần Ý nghĩa có dòng Tô màu như ví dụ. Câu "Người Nhật thường nói" không cần Tô màu.
- Câu bẫy (mục 4) không có dòng Tô màu (mẫu của bẫy khác mẫu chính, không tô để khỏi nhầm).

## Tên mẫu khi giảng

- Tên mẫu luôn nói bằng tiếng Nhật, không phiên âm Việt hóa kiểu "tô cô rô ni".
- Dòng `**Mẫu:**` mục 2 ghi tên mẫu đúng như bài gốc (chuẩn hóa ký hiệu 〜 và ／).

## Romaji

- **Không có romaji trong file Kịch bản.** Romaji chỉ dùng cho ID thư mục và slug tên file.
- Được phép viết chữ Latin cho: tên nhân vật (Minh, Yuki, Tanaka…), tên riêng/thương hiệu, từ mượn đã quen trong tiếng Việt (flan, radar, karaoke), và "JLPT".
  Không được phiên âm câu hay từ tiếng Nhật bằng romaji.
- Món ăn, đồ vật Nhật trong phần tiếng Việt: dùng tên tiếng Việt ("tôm chiên") hoặc chữ Nhật (`天ぷら`), không viết romaji.

## Câu tự nhiên

- Chọn thể thường hay thể lịch sự (です・ます) theo quan hệ giữa các nhân vật và hoàn cảnh nói trong tình huống, như người Nhật thật sẽ nói.
- Không pha thể thường và thể lịch sự trong cùng một câu.
- Ví dụ `[MỚI]` phải qua tự kiểm: "Người Nhật bản ngữ có nói đúng câu này trong tình huống này không?" Không chắc → viết câu khác.
````


---

## [Rule 05] `core/rules/05_cap-do.md`

````
# Rule 05 – Hồ sơ cấp độ (N5–N1)

Cấp độ do người dùng cung cấp. Cấp độ quyết định từ vựng của ví dụ `[MỚI]`, độ sâu giải thích, nhịp giảng và số bẫy. Cấp độ **không** giới hạn bối cảnh tình huống (xem "Chọn tình huống" ở `02_giong-van.md`).

| Thông số | N5 | N4 | N3 | N2 | N1 |
| --- | --- | --- | --- | --- | --- |
| Từ vựng ví dụ [MỚI] | N5 | ≤ N4 | ≤ N3 | ≤ N2 | ≤ N1 |
| Giải thích thuật ngữ | rất kỹ, so sánh với tiếng Việt | kỹ | vừa | ngắn | ngắn, nêu sắc thái |
| Số ví dụ mỗi cách dùng (+ phủ mọi dạng cấu trúc) | 4–6 | 4–6 | 4–6 | 4–6 | 4–6 |
| Số bẫy (mục 4) | 1 | 1 | 1–2 | 1–2 | 1–2 |
| Phần "Ý nghĩa" mỗi cách dùng | hình ảnh + so sánh tiếng Việt | hình ảnh | hình ảnh + bản chất | bản chất + sắc thái | sắc thái + văn phong (nói/viết) |
| Bẫy ưu tiên (cả 2 loại ở rule 01 đều được) | nhầm với mẫu đã học ở N5 | nhầm với mẫu N5–N4 | giống hình thức hoặc gần nghĩa | giống hình thức, gần nghĩa, đề thi JLPT | sắc thái, văn phong, đề thi JLPT |

## Ghi chú

- Ví dụ trong bài gốc vượt cấp độ: được chọn nếu điển hình, nhưng ở "Cách ghép" giải thích ngắn từ khó.
- Cấp độ nằm ở ID thư mục và dòng `- Cấp độ:` của `_phu/GhiChu_<ID>.md`; công cụ tự đưa vào meta và text tùy chỉnh (tiêu đề Kịch bản không cần).
````


---

## [Rule 06] `core/rules/06_nhan-vat.md`

````
# Rule 06 – Nhân vật: mỗi video một bộ mặt mới

Mỗi video có nhân vật riêng, **không có nhân vật chính cố định**. Người xem gặp người mới ở mỗi bài, cảnh đời thường đa dạng
(văn phòng, ga tàu, tiệm ramen, phòng gym, bệnh viện…), không phải lúc nào cũng "du học sinh Việt ở Nhật".

## Cách chọn nhân vật (bắt buộc, không tốn token)

1. `python tools/nguon.py bat-dau …` (Bước 1 của `WORKFLOW.md`) in sẵn gợi ý; muốn xem lại thì chạy `python tools/pick_cast.py <ID>`.
   Công cụ chọn từ kho `core/cast.json` bộ gồm: nhân vật chính (tên, giới, nghề, nét tính cách, ngoại hình), một nhân vật phụ và bối cảnh;
   nó tự tránh những tên đã dùng ở mục 1 của các bài trước.
2. Dùng tên nhân vật chính cho **mục 1 (mở màn) và câu Kết**. Các gợi ý khác là lựa chọn tham khảo, không phải danh sách phải đưa vào lời kể.
   Không dùng lại tên ở mục "đã dùng" mà công cụ in ra.
3. Đổi hoặc bỏ gợi ý về nghề, người phụ, bối cảnh khi nó **không phục vụ logic và ý muốn nói** của bài (vd không đưa bà chủ nhà vào cuộc phỏng vấn chỉ vì được gợi ý).
   Nếu cần đổi cả tên nhân vật chính, chọn tên khác trong `core/cast.json` hoặc tự đặt tên **chưa từng dùng**; ghi lý do vào Ghi chú biên tập.
4. Không có Python → tự chọn một tên trong `core/cast.json` chưa xuất hiện ở mục 1 của bất kỳ bài nào trong `work/`.

Tên trong ví dụ chuẩn (`core/examples/…`) chỉ là minh họa định dạng – **không chép lại** tên, nghề hay bối cảnh của nó.

## Quy tắc viết

- Tình huống mở màn và câu Kết dùng cùng một nhân vật chính.
- Cách đưa nhân vật vào lời kể theo `02_giong-van.md`, mục "Mở bài và kết bài". Không bắt buộc giới thiệu nghề, ngoại hình hoặc nhân vật phụ.
  Nếu cần giữ gợi ý ngoại hình cho biên tập, ghi trong Ghi chú; NotebookLM tự dựng hình từ hành động và hoàn cảnh có trong Kịch bản.
- Tên người Việt chỉ dùng tên gọi ngắn (vd "Yến", không "Trần Hải Yến"), nhất quán trong cả bài; không viết họ tên đầy đủ để giới thiệu nhân vật.
- Các Tình huống của từng ví dụ có thể đổi người, đổi nơi; tên mới tự đặt, tránh trùng với nhân vật chính của chính bài đó.
- Không ép tình huống cho vừa nhân vật; nét tính cách phải phục vụ ngữ pháp của bài.
- Không gán tính cách tiêu cực nặng nề (gian dối, bạo lực) cho nhân vật.
- Câu tiếng Nhật trong bài gốc có tên riêng (vd 山田さん) → giữ nguyên tên trong câu Nhật.
- Tên chỉ viết chữ Latin trong phần tiếng Việt (được phép theo `04_tieng-nhat.md`); trong câu Nhật theo bài gốc.
````


---

## [Template Kịch bản] `core/templates/KichBan.template.md`

````
# {{MAU}} – {{NGHIA}}

## 1. Mở màn: tình huống
{{Lời kể tự nhiên 40–100 từ theo rule 02 "Mở bài và kết bài": đi từ câu muốn nói để dựng một tình huống có nguyên nhân và diễn biến hợp lý, dẫn trực tiếp vào mẫu. Hài nhẹ từ chính sự việc. Nhân vật theo rule 06; chỉ giữ chi tiết phục vụ câu nói. Câu hỏi cuối dẫn vào bài; cảnh phải khớp Lời giảng mục 2 và câu Kết.}}

## 2. Giới thiệu mẫu ngữ pháp
**Mẫu:** {{MAU – đúng như bài gốc, chuẩn hóa 〜 và ／ – hiện thật to trên màn hình}}
**Nghĩa:** {{Nghĩa tiếng Việt ngắn gọn – hiện ngay dưới tên mẫu}}
**Mô tả:**
- {{2–4 ý ngắn ≤ 15 từ hiện trên màn hình: mẫu diễn tả điều gì, bản chất chung, dùng trong văn nói hay viết…}}
- {{KHÔNG liệt kê "Cách dùng 1, Cách dùng 2…" – video sẽ dựng thành khung mục lục}}

**Lời giảng:** {{Dẫn từ tình huống vừa kể sang mẫu: "câu đó dùng mẫu …". Gọi tên mẫu bằng tiếng Nhật, nói nghĩa, giảng các ý mô tả,
bức tranh chung (một hình ảnh so sánh), nói bằng lời mẫu có mấy cách dùng rồi vào cách dùng 1.}}

**Chìa khóa:** {{TÙY CHỌN – 1 câu: dấu hiệu quyết định chọn cách dùng nào. Không có thì xóa dòng}}

## 3.1 Cách dùng 1: {{TÊN CÁCH DÙNG – bài chỉ có MỘT cách dùng thì viết "## 3.1 Cách dùng: <tên>", KHÔNG số}}

### Ý nghĩa và cách dùng
**Trên màn hình:**
- {{2–5 ý ngắn, ≤ 15 từ – chữ hiện trên màn hình}}

**Bản chất:** {{A và B quan hệ thế nào, nói bằng lời thường; một hình ảnh so sánh đời thường. Đây là phần quan trọng nhất – giảng kỹ.}}
**So với tiếng Việt:** {{giống câu tiếng Việt nào ("dù… thì vẫn…"), chỗ nào khác, dịch sao cho tự nhiên}}
**Câu mẫu:** {{1 câu dẫn ngắn}}
**Nhật:** {{câu Nhật ngắn nhất thể hiện rõ nghĩa}}
**Tô màu:** {{phần mẫu trong câu mẫu}}
**Tô màu Việt:** {{cụm nghĩa tương ứng trong câu Việt bên dưới, chép đúng y}}
**Việt:** {{câu Việt}}
**Khi nào dùng:** {{hoàn cảnh dùng; vế sau thường là gì (ý kiến, lời khuyên, mong muốn…); văn nói hay văn viết}}
**Không dùng khi:** {{TÙY CHỌN – điểm hay dùng sai, giới hạn của mẫu. Không có thì xóa dòng}}
**Sắc thái:** {{TÙY CHỌN – khác nhau giữa các biến thể, trang trọng/thân mật. Không có thì xóa dòng}}
**Dấu hiệu nhận biết:** {{dạng câu, từ hay đi kèm}}

### Cách chia
**Cấu trúc 1:** {{dòng cấu trúc của cách dùng này, như bài gốc; được gộp các dòng chỉ khác biến thể (vd ＋ にしろ／にせよ／にしても)}}
**Giải thích:** {{gắn thế nào, chia dạng gì (có/không だ, の, な), 1–2 cụm ví dụ ngắn}}

{{Lặp lại "Cấu trúc n" + "Giải thích" cho mỗi dạng; đánh số liên tục CẢ BÀI. Cách dùng sau chia giống cách dùng trước thì mở đầu phần Cách chia bằng
**Giống cách dùng 1:** <nhắc lại ngắn cách chia>
rồi chỉ thêm thẻ Cấu trúc cho phần KHÁC (không có phần khác thì chỉ dòng này).}}

### Ví dụ 1
**Tình huống:** {{…}}
**Câu Việt:** {{…}}
**Câu Nhật:** {{câu Nhật nguyên văn, KHÔNG thêm ký hiệu hay cách đọc nào}}
**Tô màu:** {{phần mẫu ngữ pháp trong câu Nhật, chép đúng y từng chữ}}
**Tô màu Việt:** {{cụm nghĩa ứng với mẫu trong Câu Việt, chép đúng y (vd "Dù", "Đúng lúc… thì")}}
**Cách ghép:** 「{{Câu Nhật ở trên, chép y nguyên}}」 Đây là dạng {{thẻ cấu trúc đang dùng}}. {{giảng cách ghép: 2–4 câu ngắn}}

{{… 4–6 ví dụ cho cách dùng này, phủ mọi thẻ Cấu trúc, đánh số liên tục cả bài. Rồi chương "## 3.2 Cách dùng 2: …" với đủ 3 phần y như trên …}}

{{CHƯƠNG TÙY CHỌN – chỉ khi bài gốc có phần "cách nói thường gặp" (vd いずれにせよ, nghi vấn từ ＋ mẫu). Mỗi cụm một chương, đặt sau mọi cách dùng:}}
## 3.{{n}} Cách nói thường gặp: {{CỤM}}
**Cụm:** {{cụm, vd いずれにしろ／いずれにせよ／いずれにしても}}
**Nghĩa:** {{nghĩa ngắn}}
**Giải thích:** {{cụm được tạo thế nào, dùng khi nào, khác gì cách dùng chính}}

### Ví dụ {{k}}
{{1–3 ví dụ, cùng 5 nhãn như trên; Cách ghép nói "Đây là cụm …"}}

## 4. Bẫy dễ nhầm
**Bẫy 1 – {{Tên bẫy}}:** {{giải thích ngắn + cách phân biệt}}
**Nhật:** {{câu Nhật nguyên văn}}
**Việt:** {{câu Việt}}

{{Bẫy thứ 2 (nếu có): cách 1 dòng trống, đánh số Bẫy 2}}

## 5. Tổng kết, mẹo nhớ và lưu ý
**Tóm lại:**
- {{ý chính của từng cách dùng}}
- {{…}}

**Mẹo nhớ:** "{{câu vè / hình ảnh ngắn}}"

**Lưu ý:**
- {{điều cần chú ý 1}}
- {{điều cần chú ý 2}}

**Tình huống thực tế:**
- Công việc: {{TÙY CHỌN – mẫu hay dùng ở đâu, khi nào}}
- Cuộc sống: {{…}}
- Giao tiếp hằng ngày: {{…}}

**Người Nhật thường nói:**
**Nhật:** {{TÙY CHỌN – câu nói tự nhiên, hay gặp của người bản xứ}}
**Việt:** {{câu Việt}}
**Ý:** {{1 câu: dùng lúc nào, sắc thái, cách nói tắt}}

{{1–4 nhóm Nhật / Việt / Ý. Hai phần "Tình huống thực tế" và "Người Nhật thường nói" là TÙY CHỌN: không có nội dung chắc chắn thì xóa cả nhãn.}}

**Kết:** {{Quay lại tình huống mở màn, nói lại bằng mẫu vừa học, chào hẹn bài sau.}}
**Nhật:** {{câu Nhật nguyên văn}}
**Tô màu:** {{phần mẫu ngữ pháp trong câu Nhật}}
**Tô màu Việt:** {{cụm nghĩa tương ứng trong câu Việt}}
**Việt:** {{câu Việt}}
````


---

## [Template Ghi chú biên tập] `core/templates/GhiChuBienTap.template.md`

````
# Ghi chú biên tập – {{ID}}

> Nhật ký sản xuất do AI tự ghi. Người dùng **không cần đọc**. **KHÔNG tải lên NotebookLM.**

- Mẫu: {{MAU}} – {{NGHIA}}
- Cấp độ: {{CAP_DO}}
- Phiên bản quy tắc: {{VERSION}}
- Ngày tạo: {{YYYY-MM-DD}}
- Công cụ AI / model: {{vd Claude Code – claude-sonnet / Codex – gpt-…}}

<!-- 4 dòng Cấp độ / Phiên bản quy tắc / Ngày tạo / Công cụ AI là BẮT BUỘC: công cụ đọc chúng để sinh meta. -->

## 1. Phân tích bài gốc

- Mẫu, nghĩa ngắn: {{…}}
- Các dòng cấu trúc trong bài gốc: {{…}}
- Gán thẻ cấu trúc cho từng cách dùng (gộp dòng nào, cách dùng nào "giống cách dùng n"): {{…}}
- Cách nói thường gặp (nếu có): {{…}}

| Cách dùng | Ví dụ bài gốc | Đã chọn | Ví dụ [MỚI] | Tổng |
| --- | --- | --- | --- | --- |
| {{3.1 …}} | {{n}} | {{k}} | {{m}} | {{k+m}} |

### Bảng phủ ví dụ

<!-- BẮT BUỘC: mỗi ví dụ của Kịch bản một dòng. "Phần" = chương 3.x chứa ví dụ. "Cấu trúc" = số thẻ "Cấu trúc n" ví dụ dùng
     (nhiều số thì cách bằng dấu phẩy; ví dụ của chương Cách nói thường gặp ghi –).
     validate.py dùng bảng này để kiểm: mỗi cách dùng 4–6 ví dụ, mọi thẻ cấu trúc có ít nhất 1 ví dụ. -->

| Ví dụ | Phần | Cấu trúc | Nguồn |
| --- | --- | --- | --- |
| 1 | 3.1 | {{n}} | {{Bài gốc câu k / MỚI – lý do}} |

## 2. Lỗi đã tự sửa trong bài gốc

| # | Trước | Sau | Lý do |
| --- | --- | --- | --- |
| 1 | {{…}} | {{…}} | {{…}} |

(Không có lỗi → ghi "Không phát hiện lỗi.")

## 3. Ví dụ được chọn, bị lược, [MỚI]

| Loại | Câu Nhật | Lý do |
| --- | --- | --- |
| {{Chọn / Lược / MỚI}} | {{…}} | {{điển hình, phủ dạng V/A/N, sắc thái khác… / trùng ý, khó dựng tình huống… / bù cho đủ}} |

## 4. Quyết định đã tự đưa ra

- {{vd: chọn bẫy …; …}}

## 5. Kết quả kiểm tra

- Tự thẩm định: {{số câu Nhật đã soát; số câu đã thay vì không chắc}}
- validate.py: {{ĐẠT / kiểm thủ công}} – {{số cảnh báo}} cảnh báo
- Cảnh báo được giữ lại và lý do: {{…}}
````


---

## [VÍ DỤ CHUẨN – Kịch bản] `core/examples/N3_tokoro-ni-he-wo-de/KichBan_N3_tokoro-ni-he-wo-de.md`

````
# 〜ところに／へ／を／で – Đúng lúc…, đang… thì…, vừa… thì…

## 1. Mở màn: tình huống
Tưởng bạn cùng phòng còn lâu mới về, Hạnh tranh thủ hát một mình. Cô cầm chiếc lược làm micro, nhắm mắt diễn như đang đứng trên sân khấu.
Đúng lúc lên nốt cao, cửa mở: bạn đã về và đang đứng nhìn. Khán giả đầu tiên xuất hiện, mà Hạnh chỉ muốn tắt chương trình!
Đang hát thì bạn về tới; đang hát thì bị bạn nhìn thấy. Muốn kể chính xác những khoảnh khắc ấy bằng tiếng Nhật, mình nói thế nào?

## 2. Giới thiệu mẫu ngữ pháp
**Mẫu:** 〜ところに／へ／を／で
**Nghĩa:** Đúng lúc… thì… / Đang… thì… / Vừa… xong thì…
**Mô tả:**
- ところ = một khoảnh khắc trên dòng thời gian
- Trợ từ sau ところ cho biết chuyện gì xảy ra ở khoảnh khắc đó
- Động từ ở vế sau quyết định chọn に／へ, を hay で

**Lời giảng:** Cả đêm karaoke của Hạnh gói gọn trong một mẫu ngữ pháp N3: ところに、ところへ、ところを、ところで – "đúng lúc… thì…", "đang… thì…", "vừa… xong thì…". ところ vốn là "chỗ", ở đây là một "chỗ" trên dòng thời gian. Hãy tưởng tượng cuộc sống là bộ phim đang dừng ở một khung hình. Có người bước vào khung hình thì dùng に hoặc へ. Có người chộp được khung hình đó, tức là bắt gặp mình đang làm dở, thì dùng を. Khung hình vừa khép lại một đoạn và cảnh mới bắt đầu ngay thì dùng で. Mẫu này có ba cách dùng, mình đi lần lượt từng cách nhé.

**Chìa khóa:** nhìn động từ ở vế sau – nó quyết định trợ từ đi sau ところ.

## 3.1 Cách dùng 1: ところに／ところへ – đang dở dang thì có người/việc ập tới

### Ý nghĩa và cách dùng
**Trên màn hình:**
- Việc A đang dở dang: sắp làm, đang làm, vừa xong
- Đúng lúc đó, người hay việc B xuất hiện, chen vào
- B thường làm A bị gián đoạn

**Bản chất:** A là khoảnh khắc mình đang ở, B là thứ "bước vào" khoảnh khắc đó từ bên ngoài. に và へ vốn là trợ từ chỉ đích đến: B đi tới và rơi đúng vào "chỗ" thời gian của A. Vì vậy vế sau gần như luôn là động từ chỉ sự xuất hiện, sự tới nơi. Hình dung bạn đang ăn mì dở thì chuông cửa reo: người khách "đi đến" đúng khung hình đó.
**So với tiếng Việt:** giống "đúng lúc… thì…", "đang… thì…". Khác ở chỗ câu tiếng Việt dùng cho mọi chuyện xảy ra, còn ところに／へ chủ yếu dùng khi có ai đó, cái gì đó xuất hiện, ập tới. Chuyện "đang làm thì bị nhìn thấy" lại phải dùng ところを ở cách dùng 2.
**Câu mẫu:** câu ngắn nhất để thấy nghĩa ngay.
**Nhật:** シャワーを浴びているところに、電話がかかってきた。
**Tô màu:** ところに
**Tô màu Việt:** Đang tắm thì
**Việt:** Đang tắm thì có điện thoại gọi tới.
**Khi nào dùng:** kể lại chuyện bị chen ngang, thường bất ngờ, hơi phiền; hoặc khen ai đó đến đúng lúc. Vế sau hay là 来る、帰ってくる、入ってくる、電話がかかってくる、通りかかる. Dùng được cả khi nói lẫn khi viết.
**Không dùng khi:** vế sau là hành động tác động thẳng vào việc đang diễn ra như nhìn thấy, bắt, giúp – lúc đó dùng ところを.
**Sắc thái:** ところに và ところへ gần như thay nhau được; へ nhấn hướng di chuyển, "đi tới" rõ hơn.
**Dấu hiệu nhận biết:** vế sau là động từ chỉ sự xuất hiện; việc ở vế sau chen ngang việc đang làm.

### Cách chia
**Cấu trúc 1:** Vる／ている／た ＋ ところに／へ
**Giải thích:** Ba dạng động từ là ba thời điểm: Vる là sắp làm, Vている là đang làm, Vた là vừa làm xong. Gắn thẳng vào ところ: 出かけるところに, 寝ているところに, 終わったところに.

**Cấu trúc 2:** Aい／Aな ＋ ところに／へ
**Giải thích:** Tính từ い giữ nguyên: いいところへ, 悪いところに. Tính từ な phải giữ な: 大事なところに. Dạng này hay gặp trong các cụm cố định như "đến đúng lúc", "đến không đúng lúc".

### Ví dụ 1
**Tình huống:** Ngày chuyển nhà, Phong một mình kéo thùng sách nặng như đá lên cầu thang tầng ba, mồ hôi nhễ nhại. Đúng lúc đó, cậu bạn hàng xóm mở cửa thò đầu ra. Phong mừng rỡ gọi ngay.
**Câu Việt:** Cậu đến đúng lúc lắm! Giúp mình chuyển đống hành lý này với.
**Câu Nhật:** いいところへ来た。この荷物運ぶの、手伝って。
**Tô màu:** ところへ
**Tô màu Việt:** đúng lúc
**Cách ghép:** 「いいところへ来た。この荷物運ぶの、手伝って。」 Đây là dạng tính từ い ＋ ところへ. "Đúng lúc" là いいところ – một thời điểm tốt. Vế sau là 来た, động từ "đi tới", nên gắn へ. "Giúp mình chuyển đống này" là この荷物運ぶの、手伝って, thể て dùng để nhờ thân mật. Câu cửa miệng, học thuộc cả cụm nhé.

### Ví dụ 2
**Tình huống:** Ngày nghỉ hiếm hoi, mình lăn ra ngủ trưa giữa sàn, tóc dựng ngược, má in hằn vết chiếu. "Kinh koong" – có khách.
**Câu Việt:** Đúng lúc mình đang ngủ trưa thì khách đến nhà.
**Câu Nhật:** 私が昼寝をしているところに、お客さんが来た。
**Tô màu:** ところに
**Tô màu Việt:** Đúng lúc mình đang ngủ trưa thì
**Cách ghép:** 「私が昼寝をしているところに、お客さんが来た。」 Đây là dạng V ている ＋ ところに. "Đang ngủ trưa" là 昼寝をしている, gắn ところに thành "đúng lúc đang ngủ trưa". Vế sau お客さんが来た là có người ập tới chen ngang, nên chọn に.

### Ví dụ 3
**Tình huống:** Khoa đã xỏ giày, xịt nước hoa, tay đặt lên nắm cửa để đi hẹn hò. "Kinh koong" – ông anh họ đứng ngoài cửa, kéo theo cả một cái vali to.
**Câu Việt:** Đúng lúc mình sắp ra ngoài thì anh ấy đến.
**Câu Nhật:** 私が出かけるところに、彼が来た。
**Tô màu:** ところに
**Tô màu Việt:** Đúng lúc mình sắp ra ngoài thì
**Cách ghép:** 「私が出かけるところに、彼が来た。」 Đây là dạng V る ＋ ところに. 出かける để nguyên thể từ điển nghĩa là "sắp ra ngoài", chân chưa bước khỏi nhà. Vế sau 彼が来た – có người xuất hiện chen ngang, nên dùng に.

### Ví dụ 4
**Tình huống:** Cả nhà vừa ăn tối xong, bát đĩa đã rửa sạch bóng. Cửa mở, cậu bạn thân bước vào, tay xoa bụng: "Có gì ăn không?"
**Câu Việt:** Vừa ăn tối xong thì bạn mình đến.
**Câu Nhật:** 夕食が終わったところに、友だちが来た。
**Tô màu:** ところに
**Tô màu Việt:** Vừa ăn tối xong thì
**Cách ghép:** 「夕食が終わったところに、友だちが来た。」 Đây là dạng V た ＋ ところに. 終わった là "vừa xong". Bạn tới đúng khoảnh khắc đó; vế sau là 来た nên vẫn dùng に. Thấy chưa, る – ている – た đổi thời điểm, còn trợ từ vẫn do động từ vế sau quyết định.

## 3.2 Cách dùng 2: ところを – đang làm thì bị bắt gặp, bị tác động

### Ý nghĩa và cách dùng
**Trên màn hình:**
- Việc A đang diễn ra
- Có người tác động thẳng vào cảnh A: nhìn thấy, bắt, gọi lại, làm phiền
- Rất hay đi với thể bị động

**Bản chất:** を là trợ từ chỉ đối tượng của hành động. Với ところを, chính "cảnh A đang diễn ra" trở thành đối tượng: ai đó nhìn thấy cảnh đó, chộp lấy cảnh đó, cắt ngang cảnh đó. Hình dung một chiếc máy ảnh chụp đúng lúc mình đang làm dở – bị chụp là bị "tóm". Vì vậy câu thường mang cảm giác bị bắt quả tang, hoặc làm phiền người khác giữa chừng.
**So với tiếng Việt:** dịch là "đang… thì bị…", "bị bắt gặp đang…". Tiếng Việt đặt chữ "bị" ở vế sau; tiếng Nhật đặt ところを sau cảnh đang diễn ra, rồi chia động từ vế sau ở thể bị động như 見られる, hoặc dùng động từ tự mang nghĩa "bị" như 見つかる, 捕まる.
**Câu mẫu:** cảnh quen thuộc nhất của ところを.
**Nhật:** つまみ食いしているところを母に見られた。
**Tô màu:** ところを
**Tô màu Việt:** Đang ăn vụng thì bị
**Việt:** Đang ăn vụng thì bị mẹ nhìn thấy.
**Khi nào dùng:** kể chuyện bị bắt gặp, bị phát hiện, bị bắt – thường xấu hổ hoặc không may; kể chuyện được cứu, bị gọi lại giữa chừng; và trong lời xin lỗi lịch sự vì làm phiền người đang bận, đang nghỉ.
**Không dùng khi:** vế sau chỉ là có người đến, có chuyện xảy ra mà không tác động vào cảnh A – lúc đó dùng ところに／へ.
**Dấu hiệu nhận biết:** vế sau là 見られる、見つかる、捕まる、助ける、呼び止める、邪魔する; người tác động đi với に.

### Cách chia
**Giống cách dùng 1:** động từ và tính từ gắn vào ところ y như cách dùng 1, chỉ đổi trợ từ thành を: 逃げているところを, お忙しいところを.
**Cấu trúc 3:** N ＋ の ＋ ところを
**Giải thích:** Danh từ cần の trước ところ: お休みのところを, 食事中のところを. Dạng này hay gặp nhất trong lời xin lỗi lịch sự vì làm phiền người khác giữa chừng.

### Ví dụ 5
**Tình huống:** Tên trộm ôm túi đồ chạy thục mạng, rẽ trái rẽ phải, rồi đâm sầm vào chiếc xe cảnh sát đang đỗ ở đầu ngõ.
**Câu Việt:** Đang bỏ trốn thì bị cảnh sát bắt.
**Câu Nhật:** 逃げているところを警察に捕まりました。
**Tô màu:** ところを
**Tô màu Việt:** Đang bỏ trốn thì bị
**Cách ghép:** 「逃げているところを警察に捕まりました。」 Đây là dạng V ている ＋ ところを. "Đang bỏ trốn" là 逃げている. Vế sau 警察に捕まりました – "bị cảnh sát bắt" – tóm gọn cả cảnh đang trốn, nên dùng ところを. Lưu ý: 捕まる tự nó đã là "bị bắt", không cần chia bị động.

### Ví dụ 6
**Tình huống:** Trang nhắn mẹ: "Con ở thư viện đến chín giờ nha." Tám giờ tối, cô đang tay trong tay với bạn trai đi ngang sạp rau, đúng chỗ mẹ đang đứng chọn bí.
**Câu Việt:** Mình bị mẹ nhìn thấy lúc đang đi về cùng bạn trai.
**Câu Nhật:** 母に彼氏と一緒に帰っているところを見られた。
**Tô màu:** ところを
**Tô màu Việt:** lúc đang
**Cách ghép:** 「母に彼氏と一緒に帰っているところを見られた。」 Đây là dạng V ている ＋ ところを. "Đang đi về cùng bạn trai" là 彼氏と一緒に帰っている. "Bị mẹ nhìn thấy" là 母に見られた, thể bị động của 見る. Công thức nên nhớ: [ai]に + [cảnh đang diễn ra]ところを + 見られる.

### Ví dụ 7
**Tình huống:** Tiết lịch sử sau bữa trưa. Ren gục đầu sau chồng sách, ngáy khe khẽ. Thầy giáo rón rén đi xuống, đứng ngay sau lưng.
**Câu Việt:** Mình đang ngủ gật trong giờ học thì bị thầy phát hiện.
**Câu Nhật:** 授業中に居眠りしているところを先生に見つかってしまった。
**Tô màu:** ところを
**Tô màu Việt:** đang ngủ gật trong giờ học thì bị
**Cách ghép:** 「授業中に居眠りしているところを先生に見つかってしまった。」 Đây là dạng V ている ＋ ところを. 居眠りしている là "đang ngủ gật". 見つかる là "bị phát hiện", người phát hiện đi với に: 先生に見つかる. Thêm てしまった cho đúng cảm giác "toang rồi".

### Ví dụ 8 [MỚI]
**Tình huống:** Chủ nhật, Tuấn phải mang hồ sơ gấp tới nhà trưởng phòng. Cửa mở: trưởng phòng mặc bộ đồ ngủ in hình gấu, tay còn cầm bát mì. Tuấn cúi gập người.
**Câu Việt:** Xin lỗi đã làm phiền lúc anh đang nghỉ ngơi.
**Câu Nhật:** お休みのところをお邪魔して、すみません。
**Tô màu:** ところを
**Tô màu Việt:** lúc anh đang nghỉ ngơi
**Cách ghép:** 「お休みのところをお邪魔して、すみません。」 Đây là dạng N ＋ の ＋ ところを. お休み là danh từ "lúc nghỉ", nên phải có の trước ところ. Vế sau お邪魔して – mình chen vào làm phiền đúng cảnh người ta đang nghỉ, đúng chất ところを. Câu xin lỗi lịch sự cực hay dùng; tương tự có お忙しいところを, dạng tính từ い.

## 3.3 Cách dùng 3: ところで – vừa tới mốc đó thì chuyện tiếp theo xảy ra

### Ý nghĩa và cách dùng
**Trên màn hình:**
- Việc A vừa xong, vừa chạm một mốc
- Ngay tại mốc đó, chuyện B xảy ra hoặc bắt đầu
- Thường là V たところで

**Bản chất:** で đánh dấu nơi và lúc sự việc diễn ra. ところで biến "lúc A vừa xong" thành một cột mốc, và B xảy ra ngay tại cột mốc đó. Khác cách dùng 1 và 2: không ai chen vào việc đang làm dở – A đã đi hết một chặng rồi chuyện tiếp theo nối vào. Hình dung vạch đích: vừa chạm vạch thì pháo hoa nổ.
**So với tiếng Việt:** giống "vừa… xong thì…", "đúng lúc vừa… thì…". Câu Việt thường có chữ "vừa", câu Nhật có V た.
**Câu mẫu:** một câu rất hay nghe trong cuộc họp.
**Nhật:** 話が一段落したところで、お茶にしましょうか。
**Tô màu:** ところで
**Tô màu Việt:** tạm xong một đoạn rồi
**Việt:** Câu chuyện tạm xong một đoạn rồi, mình nghỉ uống trà nhé.
**Khi nào dùng:** kể việc xảy ra đúng lúc vừa xong một việc, thường bất ngờ như vừa lên tàu thì cửa đóng; hoặc đề nghị chuyển sang việc tiếp theo khi đã tới mốc, như đủ người thì bắt đầu. Vế sau có thể là lời rủ, lời đề nghị.
**Không dùng khi:** vế sau mang nghĩa "cũng vô ích", thường có いくら, どんなに đi trước – đó là mẫu khác, "dù có… cũng không…".
**Dấu hiệu nhận biết:** V たところで; vế sau là chuyện xảy ra ngay tại mốc: 気がつく、閉まる、始める、乾杯する.

### Cách chia
**Giống cách dùng 1:** cách gắn vào ところ giống cách dùng 1, chỉ đổi trợ từ thành で.
**Cấu trúc 4:** Vた ＋ ところで
**Giải thích:** Với nghĩa "vừa tới mốc", gần như luôn dùng V た: 着いたところで, 書いたところで, そろったところで. Vる hay Vている ít gặp vì chưa có mốc nào để chạm tới.

### Ví dụ 9
**Tình huống:** Mưa tầm tã, Somchai chạy mười lăm phút tới ga, áo ướt sũng. Tới cửa soát vé, anh thò tay vào túi lấy ví… chỉ thấy một gói khăn giấy.
**Câu Việt:** Vừa đến nhà ga thì mình phát hiện đã bỏ quên ví.
**Câu Nhật:** 駅に着いたところで財布を忘れてきたことに気がついた。
**Tô màu:** ところで
**Tô màu Việt:** Vừa đến nhà ga thì
**Cách ghép:** 「駅に着いたところで財布を忘れてきたことに気がついた。」 Đây là dạng V た ＋ ところで. "Vừa đến ga" là 駅に着いた, gắn ところで thành một cái mốc. Vế sau 財布を忘れてきたことに気がついた – việc nhận ra xảy ra ngay tại mốc đó. Lưu ý: 忘れてきた là "quên ở nhà rồi mới đi".

### Ví dụ 10
**Tình huống:** Chuông báo tàu reo inh ỏi. Mai xách túi chạy bán sống bán chết dọc sân ga, nhảy phắt lên toa cuối. Vừa đặt chân vào – "xịch", cửa đóng sau lưng.
**Câu Việt:** Mình chạy bán sống bán chết, vừa nhảy lên tàu thì cửa đóng lại.
**Câu Nhật:** 必死で走り、飛び乗ったところで電車のドアが閉まった。
**Tô màu:** ところで
**Tô màu Việt:** vừa nhảy lên tàu thì
**Cách ghép:** 「必死で走り、飛び乗ったところで電車のドアが閉まった。」 Đây là dạng V た ＋ ところで. 飛び乗った là "vừa nhảy lên tàu" – cái mốc. Vế sau ドアが閉まった xảy ra ngay tại mốc đó. 必死で走り là thể ます bỏ ます để nối hai hành động, kiểu văn viết.

### Ví dụ 11
**Tình huống:** Bốn giờ sáng, hạn nộp là tám giờ. Năm lon cà phê rỗng xếp hàng trên bàn. Gõ xong dấu chấm cuối cùng… mắt tối sầm.
**Câu Việt:** Vừa viết xong dòng cuối cùng của báo cáo thì mình đột nhiên ngất đi.
**Câu Nhật:** レポートの最後の一行を書いたところで、突然気絶した。
**Tô màu:** ところで
**Tô màu Việt:** Vừa viết xong dòng cuối cùng của báo cáo thì
**Cách ghép:** 「レポートの最後の一行を書いたところで、突然気絶した。」 Đây là dạng V た ＋ ところで. "Vừa viết xong dòng cuối" là 最後の一行を書いた, gắn ところで. Vế sau 突然気絶した xảy ra đúng tại mốc đó. Lưu ý cách đọc: 一行 là いちぎょう.

### Ví dụ 12 [MỚI]
**Tình huống:** Tiệc tất niên của công ty. Người cuối cùng thở hổn hển chạy vào, bàn đã đủ mười hai ghế. Sếp đứng dậy, nâng cốc bia.
**Câu Việt:** Mọi người đã đông đủ rồi, mình cùng nâng ly nào!
**Câu Nhật:** 全員そろったところで、乾杯しましょう。
**Tô màu:** ところで
**Tô màu Việt:** đã đông đủ rồi
**Cách ghép:** 「全員そろったところで、乾杯しましょう。」 Đây là dạng V た ＋ ところで. そろった là "đã đủ mặt" – cái mốc. Vế sau là việc bắt đầu ngay tại mốc đó, ở đây là lời rủ 乾杯しましょう. Câu này hay gặp ở tiệc và cuộc họp: 全員そろったところで、始めましょう.

## 4. Bẫy dễ nhầm
**Bẫy 1 – ところで đứng đầu câu:** đây là liên từ "à mà này", dùng để đổi chủ đề; phía trước không có động từ hay tính từ nào.
**Nhật:** ところで、週末は何をするの？
**Việt:** À mà này, cuối tuần cậu làm gì?

**Bẫy 2 – 〜ところです ở cuối câu:** chỉ nói mình đang ở giai đoạn nào của việc, không có ai chen vào và không có vế sau.
**Nhật:** 今、ご飯を食べているところです。
**Việt:** Mình đang ăn cơm đây.

## 5. Tổng kết, mẹo nhớ và lưu ý
**Tóm lại:**
- Có người, có việc chen vào → ところに／へ
- Bị bắt gặp, bị tác động đang làm dở → ところを
- Vừa chạm mốc thì chuyện khác xảy ra → ところで

**Mẹo nhớ:** "Ai ghé thì に・へ, ai tóm thì を, xong mốc thì で."

**Lưu ý:**
- Luôn nhìn động từ ở vế sau để chọn trợ từ.
- Vる là sắp làm, Vている là đang làm, Vた là vừa xong.
- Tính từ な giữ な, danh từ thêm の trước ところ.
- ところで đứng đầu câu là "à mà này" – khác hẳn mẫu hôm nay.

**Tình huống thực tế:**
- Công việc: xin lỗi khi làm phiền sếp, khách hàng đang bận; bắt đầu cuộc họp khi đã đủ người.
- Cuộc sống: kể chuyện đang làm dở thì có khách, có điện thoại; bị người nhà bắt gặp.
- Giao tiếp hằng ngày: khen bạn đến đúng lúc mình đang cần người giúp.

**Người Nhật thường nói:**
**Nhật:** お忙しいところ、すみません。
**Việt:** Xin lỗi đã làm phiền lúc anh đang bận.
**Ý:** Câu mở đầu cực quen khi gọi điện, nhắn tin, bắt chuyện với người đang bận; を thường được lược.
**Nhật:** いいところに来た！
**Việt:** Đến đúng lúc lắm!
**Ý:** Câu cửa miệng khi đang cần người giúp; nói nhanh, thân mật.
**Nhật:** きりのいいところで、休憩しましょう。
**Việt:** Làm tới đoạn tròn trịa thì mình nghỉ nhé.
**Ý:** Hay nghe ở công sở, lớp học: ところで ở đây là cái mốc tròn trịa của công việc.

**Kết:** Quay lại đêm karaoke của Hạnh – giờ các bạn nói được rồi. Hẹn gặp lại các bạn ở bài sau!
**Nhật:** 一人で歌っているところを、ルームメイトに見られた。
**Tô màu:** ところを
**Tô màu Việt:** Đang hát một mình thì bị
**Việt:** Đang hát một mình thì bị bạn cùng phòng nhìn thấy.
````
