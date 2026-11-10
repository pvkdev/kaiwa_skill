# CHANGELOG

## 7.2.0 – 2026-11-04

- Mở màn là lời kể để nghe: rule 02 yêu cầu dựng cảnh từ ý muốn nói, kiểm nguyên nhân–diễn biến, thời điểm, chủ thể và sắc thái ngữ pháp;
  hài hước đến từ chính sự việc. Đối chiếu lời giới thiệu và câu kết để giữ cùng một chuyện.
- Rule 06 bỏ yêu cầu chèn ngoại hình vào lần giới thiệu đầu; nghề, người phụ và bối cảnh chỉ là gợi ý khi phục vụ câu nói.
  Tên người Việt chỉ dùng tên gọi. Template, workflow, guide, thông báo gợi ý nhân vật và ví dụ chuẩn cập nhật tương ứng.
- Rà soát và biên tập phần mở màn của toàn bộ 360 bài N3/N2/N1; cập nhật ghi chú thẩm định và dữ liệu sản xuất.

## 7.1.1 – 2026-11-04

- `HuongDan.html`: nút ở bước thêm Kịch bản đổi thành "Copy đường dẫn thư mục"; bấm để copy thư mục chứa Kịch bản của bài đang chọn.
  Đường dẫn hiển thị và hướng dẫn tải nguồn đổi tương ứng: mở thư mục rồi chọn file Kịch bản.

## 7.1.0 – 2026-11-04

- `guide.md` mục 2.1: tiếng Việt dùng giọng miền Nam Việt Nam tự nhiên, nhất quán; mọi phần tiếng Nhật đọc chậm hơn hội thoại một chút,
  ngắt nhẹ theo cụm nghĩa, giữ phát âm tự nhiên. Phân biệt rõ nhịp lời bình tiếng Việt với nhịp đọc tiếng Nhật.
- Rule 02 và template text tùy chỉnh tham chiếu quy tắc này; không đưa chỉ dẫn phát âm vào Kịch bản hay đổi chính tả để giả giọng.
- Dựng lại text tùy chỉnh và dữ liệu cho các bài hiện có để áp dụng ngay khi tạo video mới. Trong NotebookLM, xóa nguồn guide cũ
  và tải lại `guide.md`; video đã tạo không tự đổi giọng hoặc tốc độ.

## 7.0.0 – 2026-11-04

**Sản xuất hàng loạt: source/ → hàng đợi → work/.** Quy tắc nội dung, kịch bản, guide.md, text tùy chỉnh giữ nguyên như 6.4.

- **`source/N5…N1/`** – bài giảng thô nguyên văn, tên `<cấp>_<mẫu tiếng Nhật>_vNN.md` (vd `N2_にしろ・にせよ・にしても_v01.md`;
  bỏ 〜, ／ → ・, an toàn cho Windows). Mỗi cấp có `_quan_ly.json`: phiên bản hiện tại, mảng `lich_su` các phiên bản trước,
  `trang_thai` (chua_chay / dang_chay / da_co_output / loi), danh sách `output`, mã băm để bỏ qua bài trùng nguyên văn.
- **`work/N5…N1/<tên nguồn>_rNN/`** – output thay cho `output/`. Chạy lại cùng phiên bản → `_r02`, không ghi đè.
- **`tools/nguon.py`** (mới): `them` (nhập 1 hoặc nhiều bài, ngăn bằng `---BÀI N2---`), `dong-bo` (đăng ký file thả tay),
  `hang-doi` (mẫu chưa chạy / dở / lỗi / ghi có output mà work/ không có bài hợp lệ → `work/_hang_doi.json`),
  `bat-dau` (tạo thư mục bài, chép bài gốc, gợi ý nhân vật), `trang-thai`. Có khóa file khi ghi json (chạy song song an toàn).
- **validate.py** ghi kết quả vào `_quan_ly.json` (ĐẠT → da_co_output, LỖI → loi); kiểm tên thư mục `<cấp>_<mẫu>_vNN_rNN`;
  link "Mở nhanh" mã hóa đường dẫn có chữ Nhật.
- build_data / HuongDan.html đọc từ `work/` (`work/_index.js`), đầu trang hiện tổng hợp nguồn (số mẫu, đã có output, chờ chạy).
- WORKFLOW: 3 chế độ – A Nhập nguồn, B Hàng đợi, C Sản xuất một mẫu (Bước 1 = `nguon.py bat-dau`). AGENTS, skill, README, hướng dẫn cập nhật.
- `output/` cũ chuyển vào `old/output/` (lưu trữ). pick_cast tránh tên đã dùng ở cả work/ và old/output/.

## 6.4.0 – 2026-11-02

Giữ nguyên văn và thứ tự 6.3 (gốc 6.0), chỉ chèn thêm:

- **Bài chỉ có 1 cách dùng:** tiêu đề `## 3.1 Cách dùng: <tên>` – KHÔNG đánh số (tránh người học tưởng còn cách dùng 2).
  Text tùy chỉnh tự sinh câu khung chương theo số cách dùng ({{CHUONG}}); danh sách cách dùng không còn "(1)".
  validate.py: LỖI nếu bài 1 cách dùng vẫn ghi/nói "cách dùng 1", LỖI nếu bài nhiều cách dùng thiếu số. Bài nhiều cách dùng: không đổi.
- **Khung ví dụ bắt buộc đủ câu Nhật + câu Việt:** quy tắc 3 của text tùy chỉnh và guide.md mục 3.1 thêm câu
  "Mỗi ví dụ, câu mẫu, câu kết BẮT BUỘC có khung này, đủ cả câu Nhật và câu Việt; không có khung chỉ có câu Việt".
- **Highlight cả câu Việt:** nhãn mới `**Tô màu Việt:**` (cụm nghĩa tương ứng trong câu Việt, chép đúng y) ngay sau `**Tô màu:**`
  ở ví dụ, câu mẫu, câu kết. Quy tắc 5 + guide.md 3.2: tô cùng màu đoạn "Tô màu" (câu Nhật) và "Tô màu Việt" (câu Việt).
  Bắt buộc với bài làm từ 6.4; bài cũ vẫn ĐẠT. HuongDan.html tô cả hai đoạn trong phần xem trước.
- Ví dụ chuẩn N3 thêm 16 dòng Tô màu Việt.

## 6.3.0 – 2026-11-02

**Khôi phục phần trình bày của 6.0.0** (người dùng thấy đẹp nhất: câu Nhật + câu Việt trong bóng thoại, có highlight).
guide.md và mẫu text tùy chỉnh lấy lại nguyên văn bản 6.0.0, chỉ ghép thêm đúng các điểm cần:

- Từ 6.1: lộ trình video (intro → tình huống → giới thiệu & mô tả mẫu → từng cách dùng → bẫy → tổng kết), cấm khung mục lục,
  giới thiệu mẫu ngay sau tình huống, "Cách dùng 1" viết bằng chữ số; bảng mục 4 theo khung 3.x / 4 / 5; nhãn "Mô tả".
- Từ 6.2 (bản nhẹ nhất): bước "câu Việt" chỉ đọc thành tiếng, màn hình vẫn là hình minh họa.
- **Bỏ** các thay đổi hiển thị của 6.2: đảo thứ tự text tùy chỉnh (quy tắc màn hình lên đầu), viết lại quy tắc số 3,
  2 đoạn nhấn mạnh khung chữ trong guide.md – các thay đổi này làm video mất bóng thoại và highlight.
- Giữ nguyên khung Kịch bản 6.1, validate.py / build_data.py (gồm bản sửa lỗi "Cách dùng: ." của 6.2).

## 6.2.0 – 2026-11-02

Chỉ sửa phần hiển thị (lời giảng giữ nguyên).

- **Bỏ khung chữ chỉ có câu Việt.** Trình tự ví dụ cũ có bước "hiện câu Việt trên khung nền trơn", nên video 6.1 dựng khung chỉ có chữ Việt.
  Nay bước đó chỉ đọc câu Việt, màn hình vẫn là hình minh họa; khung chữ của ví dụ luôn có **cả câu Nhật và câu Việt**.
- guide.md mục 3.1: mỗi khung có câu ví dụ phải đủ câu Nhật + câu Việt; mục 5 ghi rõ màn hình của một ví dụ.
- **Sửa lỗi 6.1:** text tùy chỉnh ghi "Cách dùng: ." (không đọc được tên cách dùng ở chương 3.x); validate.py nay báo LỖI nếu xảy ra.
- Text tùy chỉnh: đưa **quy tắc chữ trên màn hình lên đầu** (trước trình tự cảnh) để NotebookLM ưu tiên; thêm lệnh cấm khung chỉ có câu Việt.

## 6.1.0 – 2026-11-02

Lộ trình video theo yêu cầu: intro → tình huống → giới thiệu & mô tả mẫu → từng cách dùng → bẫy → tổng kết. (Khung 6.0 chưa có bài nào dùng, thay hẳn.)

- **Bỏ mục "3. Tổng quan"** – video dựng nó thành khung mục lục ("1 Tổng quan, 2 Cách dùng Một…"). guide.md và text tùy chỉnh **cấm khung mục lục**;
  danh sách trình tự cảnh ghi rõ "chỉ để dàn dựng, không hiện lên màn hình" và không còn đánh số.
- **Mục 2 "Giới thiệu mẫu ngữ pháp" thành phần giới thiệu & mô tả** ngay sau tình huống: `Mẫu` (thật to) → `Nghĩa` → `Mô tả` (2–4 ý trên màn hình)
  → `Lời giảng` (dẫn từ tình huống, gọi tên mẫu bằng tiếng Nhật, nghĩa, bức tranh chung) → `Chìa khóa` (tùy chọn).
  validate.py báo LỖI nếu Mô tả liệt kê "Cách dùng 1, 2…" (dễ thành mục lục).
- Đánh số lại: chương cách dùng `## 3.x`, Bẫy `## 4.`, Tổng kết `## 5.`; Bảng phủ ghi Phần = 3.1, 3.2…
- **Số viết bằng chữ số:** "Cách dùng 1", không "Cách dùng một" (guide, text tùy chỉnh, rule 02; validate.py báo LỖI nếu Kịch bản viết "cách dùng một/hai…").
  Khung mở chương chỉ ghi "Cách dùng 1" + tên, không thêm số thứ tự chương riêng.
- Ví dụ chuẩn N3 chuyển sang khung 6.1.

## 6.0.0 – 2026-11-02

Đổi khung Kịch bản – bài làm theo 5.x vẫn ĐẠT theo luật cũ (kèm cảnh báo gợi ý làm lại thành <ID>-v2).

- **Mỗi cách dùng là một chương** `## 4.x Cách dùng x: …` gồm đúng thứ tự `### Ý nghĩa và cách dùng` → `### Cách chia` → các `### Ví dụ`.
  Bỏ mục "Ý nghĩa" và "Cấu trúc" chung cho cả bài (video bị NotebookLM bỏ mất phần cấu trúc, và người học phải nhớ cấu trúc từ rất xa).
  Mục 3 đổi thành **Tổng quan** (bản đồ các cách dùng, phân biệt nhanh). Bẫy thành mục 5, Tổng kết thành mục 6.
- **Phần Ý nghĩa giảng chi tiết:** nhãn bắt buộc Trên màn hình, Bản chất, So với tiếng Việt, Câu mẫu (Nhật / Tô màu / Việt), Khi nào dùng,
  Dấu hiệu nhận biết; tùy chọn Không dùng khi, Sắc thái. Lời giảng ≥ 100 từ (LỖI nếu < 60), không có trần. Rule 02 thêm mục "Giảng ý nghĩa".
- **Cách chia theo từng cách dùng:** thẻ Cấu trúc đánh số liên tục cả bài; cách dùng sau chia giống thì dùng `**Giống cách dùng n:**` và chỉ thêm thẻ cho phần khác;
  được gộp các dòng chỉ khác biến thể (にしろ／にせよ／にしても) thành một thẻ.
- **Chương "Cách nói thường gặp"** (tùy chọn, sau các cách dùng): `**Cụm:**` / `**Nghĩa:**` / `**Giải thích:**` + 1–3 ví dụ.
- **Mục 6 thêm 2 phần tùy chọn:** `**Tình huống thực tế:**` (công việc / cuộc sống / giao tiếp) và `**Người Nhật thường nói:**` (1–4 nhóm Nhật / Việt / Ý).
- **Bỏ mọi con số thời lượng:** text tùy chỉnh không còn "dự kiến X phút"; thay bằng **TRÌNH TỰ CẢNH BẮT BUỘC** tự sinh từ Kịch bản
  (mỗi cách dùng: Ý nghĩa → Cách chia (n thẻ) → Ví dụ a–b), kèm lệnh không bỏ, không gộp phần nào.
- Bảng phủ ví dụ đổi cột thành `| Ví dụ | Phần | Cấu trúc | Nguồn |` (Phần = 4.1, 4.2…).
- guide.md mục 4 viết lại theo khung chương; HuongDan.html nhận nhãn mới; ví dụ chuẩn N3 viết lại theo khung 6.0
  (3 chương, câu mẫu, Tình huống thực tế, Người Nhật thường nói).

## 5.3.0 – 2026-10-30

- **4–6 ví dụ cho MỖI cách dùng** (trước: 4–6 cả bài). Bài 3 cách dùng → 12–18 ví dụ.
- **Phủ mọi dạng cấu trúc:** mỗi dòng "Cấu trúc n" ở mục 4 phải có ít nhất 1 ví dụ; một cách dùng có hơn 6 dạng thì được thêm ví dụ cho đủ dạng.
- **Bảng phủ ví dụ** (bắt buộc) trong Ghi chú biên tập: | Ví dụ | Cách dùng | Cấu trúc | Nguồn |. validate.py dùng bảng để kiểm số ví dụ mỗi cách dùng,
  cấu trúc chưa có ví dụ, và giới hạn [MỚI] (chỉ để bù đủ 4 ví dụ mỗi cách dùng + phủ dạng bài gốc không có).
- **Cách ghép nói rõ dạng cấu trúc** ngay sau câu Nhật (vd "Đây là dạng V た ＋ ところで."); validate.py báo LỖI nếu thiếu chữ "dạng".
- **Bỏ giới hạn 10 phút:** guide.md và text tùy chỉnh yêu cầu giảng đủ mọi ví dụ, không bỏ/gộp/rút gọn; text tùy chỉnh có thời lượng dự kiến (tự tính).
  Thay cảnh báo tổng số từ bằng cảnh báo từng ví dụ (Tình huống + Cách ghép ≤ 130 từ).
- Câu gần trùng trong bài gốc tính là một câu.
- Ví dụ chuẩn nâng lên 12 ví dụ (4 mỗi cách dùng, có [MỚI] cho dạng N の), nhân vật đổi tên (không còn Lan).
- Bài làm theo quy tắc < 5.3.0 vẫn ĐẠT theo luật cũ, kèm 1 cảnh báo gợi ý làm lại thành <ID>-v2.

## 5.2.0 – 2026-10-30

- **Video phải đọc to trọn vẹn câu ví dụ tiếng Nhật trước khi giảng.** Video cũ chỉ hiện câu Nhật rồi giảng luôn, không đọc câu.
  - guide.md mục 2 + mục 5: bắt buộc đọc to trọn câu Nhật (ví dụ, bẫy, câu kết) từ chữ đầu đến chữ cuối, có ví dụ SAI/ĐÚNG; giảng sau khi đọc xong.
  - Text tùy chỉnh (TuyChinh) thêm khối "LỜI ĐỌC – BẮT BUỘC" và trình tự ví dụ có bước "ĐỌC TRỌN câu Nhật".
  - Kịch bản: dòng `**Cách ghép:**` mở đầu bằng chính câu Nhật trong 「 」 – lời giảng được dựng từ dòng này nên video sẽ đọc trọn câu trước.
    validate.py báo LỖI nếu thiếu. Ví dụ chuẩn và các bài đã làm đã được chuyển tự động.

## 5.1.0 – 2026-10-30

- **Nhân vật đa dạng, bỏ dàn nhân vật cố định.** Trước đây rule 06 ghi sẵn Lan / Tanaka / mẹ / thầy Suzuki / sếp Yamada và ví dụ chuẩn cũng mở màn bằng Lan,
  nên bài nào cũng ra Lan. Nay mỗi bài một nhân vật mới: kho `core/cast.json` (tên Việt – Nhật – quốc tế, nghề, nét tính cách, ngoại hình, bối cảnh)
  và công cụ `tools/pick_cast.py <ID>` tự chọn, tự tránh tên đã dùng ở mục 1 của các bài trước. Không tốn token AI.
- Rule 06 viết lại; WORKFLOW Bước 1 thêm lệnh pick_cast; ví dụ chuẩn chỉ để tham khảo định dạng, không chép tên/bối cảnh.
- Nhân vật gắn một cụm ngoại hình ngắn ở lần nhắc đầu để hình minh họa của NotebookLM khác nhau giữa các bài.

## 5.0.0 – 2026-10-30

- **Bỏ dòng cách đọc hiragana** (theo quyết định của người dùng): câu Nhật trên màn hình chỉ còn 2 dòng xếp dọc – câu Nhật trên, câu Việt dưới.
  Bỏ nhãn `**Cách đọc:**` khỏi template, ví dụ, bẫy, câu kết, mục 2, mục 4; validate.py báo LỖI nếu còn dòng Cách đọc.
  Bỏ luôn quy định "không kanji" ở các ý ngắn trên màn hình (chỉ có vì trước đây không có chỗ ghi cách đọc).
- **Cấm hiện tên nhãn** "Câu Nhật:", "Câu Việt:", "Nhật:", "Việt:", "Tô màu:", "Giải thích:" (video bị hiện nhãn); có ví dụ đúng/sai trong guide.md.
- **Cấm đặt câu Nhật và câu Việt cạnh nhau** thành 2 ô trái – phải; luôn xếp dọc trong một khung, câu Nhật chép đúng từng chữ.
- Ví dụ chuẩn và 3 bài đã làm chuyển sang định dạng mới.

## 4.0.0 – 2026-10-30

Đổi cách hiển thị chữ Nhật – bài làm theo 3.x cần chuyển định dạng (bài có sẵn đã được chuyển).

- **Câu Nhật hiện đúng 3 dòng:** câu Nhật gốc → cả câu viết bằng hiragana → câu Việt. Bỏ hẳn furigana: NotebookLM chép nguyên ký hiệu
  《 》 và 【 】 lên màn hình. Kịch bản không còn ký hiệu nào trong câu Nhật.
- **Nhãn mới:** `**Cách đọc:**` (hiragana, katakana giữ nguyên) sau mọi câu Nhật, sau Mẫu / Cấu trúc có kanji; `**Tô màu:**` ghi đoạn mẫu cần tô màu.
  validate.py đối chiếu Cách đọc với câu Nhật (phần kana, dấu câu phải khớp, không còn kanji/số/Latin) và Tô màu phải nằm trong câu Nhật.
- **Mục 4 không còn bảng:** mỗi dòng cấu trúc của bài gốc là một khối `**Cấu trúc n:**` + `**Giải thích:**` đủ ý; video dựng thành thẻ công thức nổi bật.
- **Chữ Nhật trong các ý ngắn trên màn hình** (Trên màn hình, Giải thích, Tóm lại, Mẹo nhớ, Lưu ý) viết bằng kana, không kanji.
- **Khung tiêu đề video chỉ có tên mẫu**, không có chữ "Ngữ pháp" hay cấp độ.
- guide.md, text tùy chỉnh, rule 03/04, template, WORKFLOW, trang HuongDan.html cập nhật theo. Ví dụ chuẩn và 3 bài đã làm chuyển sang định dạng mới.

## 3.1.0 – 2026-10-30

- **Cấm tiếng Anh trên màn hình:** chỉ tiếng Việt và tiếng Nhật (sai: "N2 Surprise Grammar", "*Use this when…"); không tự thêm chú thích ngoài Kịch bản.
- **Khung tiêu đề video đúng 2 dòng:** "Ngữ pháp <cấp độ>" / tên mẫu; không bao giờ ngắt dòng giữa tên mẫu ngữ pháp.
- Chỉ tô màu mẫu ngữ pháp trong câu Nhật, không tô chữ trong câu Việt; không để ngoặc 「 lẻ loi.
- Mục 6: mỗi bẫy luôn hiện câu Nhật (furigana phía trên) + câu Việt, không thay bằng lời tóm tắt.
- Áp dụng ở guide.md (mục 3.0, 3.2, 3.3, bảng mục 4, danh sách tự kiểm) và text tùy chỉnh.

## 3.0.0 – 2026-10-30

Sửa lỗi hiển thị trong video NotebookLM (furigana nằm trong ngoặc cạnh kanji, chấm tròn trước câu, hình nền che chữ).

- **Furigana dạng ký hiệu ruby `漢字《かな》`** thay cho `漢字（かな）` (ngoặc tròn khiến NotebookLM chép nguyên vào màn hình).
  Số + kanji: `｜３億円《さんおくえん》`. validate.py báo LỖI nếu còn dùng `（ ）` cho furigana.
- **Không gạch đầu dòng trước câu Nhật/Việt:** mục 2 thành 2 dòng `**Mẫu:**` / `**Nghĩa:**`; mục 6 thành `**Bẫy 1 – <tên>:**` + `**Nhật:**` + `**Việt:**`;
  câu kết mục 7 dùng `**Nhật:**` / `**Việt:**`. validate.py kiểm tra.
- **guide.md mục 3 viết lại thành quy tắc bắt buộc tuyệt đối:** furigana in nhỏ phía trên kanji (có ví dụ đúng/sai), phương án dự phòng duy nhất
  (dòng hiragana bên dưới), cấm chấm tròn trước câu, cấm ngắt giữa từ, chữ luôn trên khung nền trơn – hình minh họa không được chồng lên chữ,
  danh sách tự kiểm từng khung hình.
- **Text tùy chỉnh** (kênh chỉ dẫn mạnh nhất của NotebookLM) thêm 6 quy tắc hiển thị bắt buộc.
- Ví dụ chuẩn N3 và bài N2 〜なんて／とは chuyển sang định dạng mới. Trang HuongDan.html hiển thị ký hiệu mới thành furigana.

## 2.1.0 – 2026-10-30

Gọn hơn cho sản xuất hàng loạt. Quy tắc nội dung và định dạng Kịch bản giữ nguyên.

- **1 guide dùng chung:** `guide.md` ở gốc dự án (thay cho `core/notebooklm/guide.md` + bản chép `guide_<ID>.md` mỗi bài).
  Tải lên NotebookLM 1 lần; mỗi bài chỉ thêm Kịch bản.
- **1 trang HTML dùng chung:** `HuongDan.html` ở gốc dự án (thay cho `HuongDan_<ID>.html` mỗi bài). Tab cấp độ N5–N1, tìm kiếm
  (có dấu/không dấu, kana, romaji), sắp xếp, đánh dấu bài đã làm video, tự chọn bài mới nhất sau F5.
  Dữ liệu đọc từ `output/_index.js` + `output/<ID>/_phu/data.js` (trình duyệt không cho trang mở từ ổ đĩa đọc file .md).
- **Thư mục bài gọn:** gốc chỉ có `KichBan_<ID>.md`; file phụ vào `_phu/` (BaiGoc, GhiChu, TuyChinh, meta, data.js).
  Bỏ thư mục `input/` – bài gốc lưu ở `_phu/BaiGoc_<ID>.md`.
- **AI viết ít hơn:** chỉ viết Kịch bản + Ghi chú (+ lưu bài gốc). `validate.py` tự sinh meta, TuyChinh, data.js và cập nhật danh sách.
- Thêm `tools/build_data.py` (dựng lại dữ liệu mọi bài); bỏ `tools/build_html.py`, `HuongDan.template.html`, `HuongDanThaoTac.template.md`, `meta.template.json`.
- Không tự mở trình duyệt/thư mục sau mỗi bài (tránh chồng tab khi làm hàng loạt); `open_output.py` chỉ chạy khi cần.
- WORKFLOW còn 8 bước (0–7). check_portable.py hết báo nhầm chuỗi kiểu `tạo:\s`.

## 2.0.0 – 2026-10-30

Định dạng mới – bài làm theo bản 1.x cần làm lại.

- **Video dưới 10 phút:** tổng 4–6 ví dụ cả bài (chọn từ bài gốc, mỗi cách dùng ít nhất 1), nhịp nói nhanh, gọn.
- **Ví dụ Việt trước, Nhật sau:** Tình huống → Câu Việt → Câu Nhật (mẫu trong 【 】 để highlight) → Furigana → Cách ghép.
- **Furigana bắt buộc** cho mọi câu Nhật, dạng 漢字（かな）; validate.py kiểm tra từng cụm kanji và đối chiếu với câu Nhật.
- **Màn hình:** mục 2 hiện mẫu thật to; mục 3 có "Trên màn hình" (ý ngắn) song song "Lời giảng"; mục 4 là bảng cấu trúc đúng như bài gốc.
- **Bỏ hẳn câu đố/quiz;** mục 7 thành "Tổng kết, mẹo nhớ và lưu ý". validate.py báo LỖI nếu có câu đố.
- **guide.md** thay cho 00_HuongDan_PhongCach.md: quy tắc ngắt dòng theo cụm nghĩa, Nhật/Việt 2 dòng riêng, câu đầy đủ, furigana trên kanji,
  highlight mẫu, chữ nhỏ – hình minh họa lớn, sống động, đúng tình huống.
- **Tên file mang đuôi <ID>:** KichBan_<ID>.md, guide_<ID>.md, TuyChinh_<ID>.txt, GhiChu_<ID>.md, meta_<ID>.json, HuongDan_<ID>.html.
- Trang HuongDan_<ID>.html: xem trước có furigana thật phía trên kanji và highlight mẫu ngữ pháp.
- Ví dụ chuẩn N3_tokoro-ni-he-wo-de viết lại theo định dạng mới (6 ví dụ).

## 1.6.1 – 2026-10-29

- Làm rõ sau lần chạy thật bài N2 〜なんて／とは: slug theo đúng chữ kana (は→ha); câu ví dụ lặp lại trong bài gốc chỉ tính một lần;
  biến thể cùng nghĩa gộp thành một cách dùng; mẫu thuần kana bỏ ngoặc cách đọc; câu đố được dùng nhiều dạng nhưng chỉ một đáp án đúng.

## 1.6.0 – 2026-10-29

- Tính di động: thêm tools/check_portable.py – quét đường dẫn tuyệt đối (ổ đĩa Windows, /Users, /home, UNC, file:///).
  validate.py báo LỖI nếu file output chứa đường dẫn tuyệt đối; package.py dừng đóng gói nếu dự án còn đường dẫn tuyệt đối.
- AGENTS.md: quy tắc chỉ dùng đường dẫn tương đối trong file.
- Tài liệu: bỏ đường dẫn ổ đĩa ghi cứng; thêm mục "Mang dự án sang máy khác".
- HuongDan.html: đường dẫn tính lúc mở (Windows, macOS, Linux, ổ mạng), hiện đường dẫn tương đối trong dự án,
  cảnh báo khi trang bị tách khỏi thư mục của bài.

## 1.5.1 – 2026-10-29

- HuongDan.html: nút chuyển giao diện sáng/tối (nhớ lựa chọn, mặc định theo hệ điều hành).
- HuongDan.html: tăng độ rộng trang lên 1680px, cột "Các bước" rộng 400–560px.

## 1.5.0 – 2026-10-29

- Thay HuongDan_ThaoTac.md bằng trang **HuongDan.html** cho từng bài: 4 bước có tick tiến độ, xem trước Kịch bản/Phong cách/Tùy chỉnh,
  nút copy nhanh (Kịch bản, Phong cách, text tùy chỉnh, tên notebook, tên file video, đường dẫn thư mục).
- Thêm tools/build_html.py (sinh trang từ template, nhúng sẵn nội dung) và tools/open_output.py (tự mở thư mục + trang khi AI làm xong).
- Thêm series.json: ngôn ngữ, định dạng, kiểu hình ảnh dùng chung cho cả series.
- validate.py: bắt buộc HuongDan.html, báo LỖI khi trang đã cũ so với file; khối "Mở nhanh" có thêm link thư mục.
- split_chat_output.py tự sinh HuongDan.html và mở thư mục; bundle cho AI chat không còn xuất file hướng dẫn.

## 1.4.1 – 2026-10-29

- Làm rõ sau lần chạy thật: file input dùng đúng ID kể cả `-v2`; cách đếm "quyết định đã tự đưa ra"; luôn viết mới dẫn cảnh khi làm lại bài ví dụ chuẩn.
- Rule 05: bẫy N3 được dùng cả loại giống hình thức lẫn gần nghĩa. Rule 04: liệt kê chữ Latin được phép (tên nhân vật, từ mượn, JLPT).
- validate.py: thêm "file" vào danh sách từ cấm trong Kịch bản.

## 1.4.0 – 2026-10-29

- Chế độ tự quyết (mặc định): AI không hỏi lại, không yêu cầu người dùng duyệt; tự quyết theo phương án an toàn nhất và ghi lại.
- Thiếu cấp độ → AI tự xác định theo JLPT. Chỉ hỏi lại khi không có bài giảng.
- Bước 8 mới: AI tự thẩm định như giáo viên khó tính; câu không chắc → thay bằng câu chắc chắn đúng.
- Số ví dụ mỗi cách dùng: 4–10. Bài gốc > 10 → AI tự chọn 10 ví dụ theo tiêu chí; validate.py báo LỖI nếu > 10.
- Bỏ khuyến nghị/hỏi tách tập. Ghi chú biên tập thành nhật ký AI (không còn mục "Cần duyệt").

## 1.3.0 – 2026-10-29

- Báo cáo cuối luôn có khối link "📂 Mở nhanh" tới từng file đầu ra (link markdown + đường dẫn file:/// tuyệt đối).
- validate.py tự in khối link khi ĐẠT; thêm tùy chọn `--links` để in lại.
- Bước 9: báo cáo viết bằng markdown thường, không đặt trong khối code (để link bấm được).
- docs/HUONG_DAN_SU_DUNG.md: thêm mục "Mở file từ báo cáo của AI".

## 1.2.0 – 2026-10-29

- Ví dụ bài gốc là ví dụ chính: dùng toàn bộ, giữ nguyên văn câu Nhật, giữ thứ tự, bản dịch dựa trên bản dịch gốc.
- Ví dụ [MỚI] chỉ để bù cho đủ 4 ví dụ mỗi cách dùng; bỏ quy định "thêm tối đa 2 ví dụ vượt mức".
- Bảng mục 4 ưu tiên trích cụm từ ví dụ bài gốc.
- validate.py: báo LỖI nếu cách dùng có [MỚI] mà tổng ví dụ khác 4.
- Ví dụ chuẩn: bỏ 2 ví dụ [MỚI] ở mục ところで (còn 19 ví dụ, toàn bộ từ bài gốc); mẹo nhớ bỏ romaji.

## 1.1.0 – 2026-10-29

- Bỏ mọi danh sách bối cảnh định sẵn (nhà, lớp, ga tàu, công ty…): AI tự chọn tình huống đúng nhất cho từng câu.
- Rule 02: thêm mục "Chọn tình huống" với 5 tiêu chí; bỏ danh sách "nguồn hài khuyến khích".
- Rule 05: bỏ dòng "Bối cảnh ví dụ ưu tiên"; cấp độ không giới hạn bối cảnh.
- Rule 04: chọn thể thường/lịch sự theo quan hệ nhân vật, không theo loại bối cảnh.
- Rule 06: dàn nhân vật chuyển thành gợi ý, không bắt buộc; bỏ cột "hay xuất hiện trong".
- 00_HuongDan_PhongCach.md: hình minh họa bám theo tình huống của từng ví dụ thay vì danh sách cảnh cố định.

## 1.0.0 – 2026-10-29

- Phiên bản đầu tiên.
- Sườn bài giảng 7 phần; ví dụ 5 nhịp (thêm dòng Cách đọc kana cho máy đọc).
- Rules 01–06: nội dung, giọng văn, ví dụ, tiếng Nhật, cấp độ N5–N1, dàn nhân vật cố định.
- Templates: Kịch bản, Tùy chỉnh, Ghi chú biên tập, Hướng dẫn thao tác, meta.json.
- Ví dụ chuẩn: N3_tokoro-ni-he-wo-de (21 ví dụ).
- Công cụ: validate.py, build_bundle.py, split_chat_output.py, package.py.
- Điểm vào: AGENTS.md (Codex/Cursor/…), CLAUDE.md, GEMINI.md, skill `bunpou-video`.
