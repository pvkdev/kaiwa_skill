# Hướng dẫn sử dụng

## 0. Thiết lập 1 lần

1. Mở file `series.json` ở thư mục gốc dự án, điền kiểu hình ảnh bạn chọn cho cả series (vd `"Whiteboard"`, `"Anime"`).

   ```json
   {
     "ngon_ngu": "Tiếng Việt",
     "dinh_dang": "Explainer",
     "phong_cach_hinh_anh": "Anime"
   }
   ```

2. Mở **`HuongDan.html`** (thư mục gốc dự án) bằng trình duyệt và để sẵn 1 tab. Phần **"Thiết lập NotebookLM – chỉ làm 1 lần"** ở đầu trang:
   - Tạo 1 notebook dùng chung cho mọi bài.
   - Tải lên **`guide.md`** (nút "Copy đường dẫn guide.md" → dán vào hộp chọn file). Nguồn này giữ cố định.
   Bấm vào tiêu đề phần thiết lập để thu gọn; trang nhớ lựa chọn này.

## 1. Quy trình sản xuất (kit 7: source → hàng đợi → work)

1. **Nhập nguồn** – gửi cho AI một hoặc nhiều bài giảng thô, nói rõ cấp độ:

   ```text
   N2 – nhập nguồn:
   <dán bài giảng 1>
   <dán bài giảng 2>   ← nhiều bài: AI tự tách (có thể tự ghi dòng ---BÀI N2--- giữa các bài)
   ```

   AI lưu vào `source/N2/N2_<mẫu>_v01.md` và cập nhật `source/N2/_quan_ly.json`. Dán lại cùng mẫu (đã sửa) → `_v02`,
   bản cũ vào lịch sử; trùng nguyên văn → bỏ qua. Bạn cũng có thể tự thả file `N2_<mẫu>_v01.md` vào `source/N2/`
   (AI chạy `python tools/nguon.py dong-bo` để đăng ký).
2. **Chạy hàng đợi** – gửi "chạy hàng đợi" (hoặc "chạy N2", "chạy 5 bài"). AI chạy `python tools/nguon.py hang-doi`:
   mẫu chưa có output, đang dở, lỗi, hoặc ghi "đã có output" mà `work/` không có bài hợp lệ → vào hàng đợi.
3. AI làm **lần lượt từng mẫu** (chế độ tự quyết – tự sửa lỗi bài gốc, tự chọn 4–6 ví dụ mỗi cách dùng, tự thẩm định):
   mỗi mẫu một thư mục `work/<cấp>/<cấp>_<mẫu>_vNN_rNN/`. **Bạn không cần duyệt gì.**
   Xem tổng hợp bất cứ lúc nào: `python tools/nguon.py trang-thai`.
4. AI xong → bấm **F5** trang `HuongDan.html`. Bài mới được chọn sẵn (có nhãn "Mới nhất"). Làm theo 4 bước bên trái:
   - **Bước 1:** "Copy đường dẫn file" → NotebookLM: Add sources → Upload → dán vào ô tên file của hộp chọn file, Enter.
     (Hoặc "Copy nội dung Kịch bản" → Add sources → Copied text.)
   - **Bước 2:** trong cột Sources chỉ tick `guide.md` và Kịch bản của bài này.
   - **Bước 3:** Studio → Video Overview → Customize → "Copy text tùy chỉnh", dán vào ô mô tả trọng tâm → Generate.
   - **Bước 4:** tải video ("Copy tên file video"), rồi **xóa nguồn Kịch bản** vừa dùng khỏi notebook (giữ guide.md).
   Tick "Xong" từng bước; đủ 4 bước thì bài được đánh dấu "✓ Đã làm" trong danh sách (lưu trên trình duyệt này).
   Bên phải là tab xem trước Kịch bản (câu Nhật, tô màu mẫu), Text tùy chỉnh, Guide chung, Nhật ký AI.

**Tìm bài cũ:** chọn tab cấp độ (N5–N1 hoặc Tất cả), gõ vào ô tìm kiếm (mẫu tiếng Nhật, nghĩa tiếng Việt có dấu hoặc không dấu, ID, romaji).
Phím `/` để nhảy vào ô tìm kiếm, Enter để mở kết quả đầu tiên. Tick "Ẩn bài đã làm video" để chỉ còn bài chưa làm.

**Thư mục một bài** (`work/<cấp>/<ID>/`) chỉ có `KichBan_<ID>.md` – file cần tải lên. Mọi file khác nằm trong `_phu/`, không cần mở.

## 2. Mở AI theo từng công cụ

### Claude Code

```bash
cd <đường-dẫn-tới>/bunpou_skill
claude
```
Gõ `/bunpou-video` rồi dán tin nhắn ở mục 1 (hoặc dán thẳng tin nhắn, Claude tự nhận ra).

### Codex (OpenAI)

```bash
cd <đường-dẫn-tới>/bunpou_skill
codex
```
Codex tự đọc `AGENTS.md`. Dán tin nhắn ở mục 1.

### Gemini CLI

```bash
cd <đường-dẫn-tới>/bunpou_skill
gemini
```
Gemini CLI tự đọc `GEMINI.md`. Dán tin nhắn ở mục 1.

### Cursor, Windsurf, VS Code Copilot hoặc agent khác

Mở thư mục dự án. Nếu công cụ không tự đọc `AGENTS.md`, gửi kèm câu đầu tiên:
`Đọc AGENTS.md và làm đúng core/WORKFLOW.md cho bài sau.`

### AI dạng chat (ChatGPT, Gemini, Claude.ai web/app)

1. Tải lên file `dist/PROMPT_BUNDLE.md` (hoặc dán nội dung vào phần hướng dẫn của Project/GPT/Gem để dùng lâu dài).
2. Trên máy, tự chạy `python tools/nguon.py hang-doi` rồi `python tools/nguon.py bat-dau <file nguồn>` → ghi lại `<ID>` nó in ra.
3. Gửi cho AI chat: `ID: <ID>` + nội dung file nguồn (bài giảng) + cấp độ.
4. Copy toàn bộ câu trả lời, lưu thành `tmp_chat.txt` trong thư mục dự án.
5. Chạy: `python tools/split_chat_output.py tmp_chat.txt` → ghi vào `work/<cấp>/<ID>/`, tự kiểm tra, ghi trạng thái nguồn, cập nhật HuongDan.html (F5 để xem).
6. Báo LỖI → gửi danh sách lỗi lại cho AI và yêu cầu sửa.

## 3. Mở file từ báo cáo của AI

Cuối báo cáo có khối **"📂 Mở nhanh"** (link tới HuongDan.html, Kịch bản, thư mục bài, guide.md):

| Bạn đang dùng | Cách mở |
| --- | --- |
| Claude Code / Codex trong VS Code, Cursor, Claude desktop | Bấm thẳng vào link `[tên file](…)` |
| Claude Code / Codex / Gemini CLI trong terminal | Ctrl + click (macOS: Cmd + click) vào dòng `file:///…` |

Mất khối link: `python tools/validate.py work/<cấp>/<ID> --links`. Mở trang nhanh: `python tools/open_output.py`.

**Sửa tay file Kịch bản** (hoặc đổi `series.json`, `guide.md`) → chạy `python tools/build_data.py` rồi F5 trang, nếu không trang vẫn hiện nội dung cũ.

## 4. Kiểm tra thủ công một bộ file

```bash
python tools/validate.py work/<cấp>/<ID>
```

- `LỖI` = phải sửa (có thể nhờ AI: "sửa các lỗi validate của work/<cấp>/<ID>").
- `CẢNH BÁO` = nên xem, không bắt buộc.

## 5. Các yêu cầu hay dùng với AI

| Muốn | Nói với AI |
| --- | --- |
| Video vẫn quá dài | `Giảm ví dụ của work/<cấp>/<ID> còn 4 câu` |
| Bài báo lỗi trên trang (nhãn đỏ "x lỗi") | `Sửa lỗi bài <ID>` |
| Làm lại phần hài cho vui hơn | `Viết lại Tình huống và Cách ghép của work/<cấp>/<ID>, giữ nguyên câu Nhật` |
| Đổi cấp độ | `Làm lại bài <ID> cho cấp độ N2` (tạo thư mục mới, không ghi đè) |
| Sửa một ví dụ sai | `Ở work/<cấp>/<ID>, mục 5.2 ví dụ 3: <vấn đề>. Sửa và chạy lại validate` |

## 6. Khi video NotebookLM chưa đạt

| Vấn đề | Nguyên nhân thường gặp | Cách xử lý |
| --- | --- | --- |
| Bỏ bớt ví dụ | Bài quá dài | Tạo lại; vẫn bỏ thì nhờ AI giảm số ví dụ |
| Giọng khô | NotebookLM tạo ngẫu nhiên mỗi lần | Tạo lại 1–2 lần |
| Đọc câu Nhật sai/giọng lơ lớ | Giọng đọc tiếng Việt đọc câu Nhật | Lồng tiếng câu Nhật bằng TTS tiếng Nhật ở bước hậu kỳ |
| Nhắc "theo tài liệu…" | Thiếu prompt tùy chỉnh | Kiểm tra đã dán text tùy chỉnh (nút "Copy text tùy chỉnh") chưa |
| Hiện chữ "Câu Nhật:", "Câu Việt:" hoặc cách đọc trong ngoặc | NotebookLM bỏ qua quy tắc hiển thị | Kiểm tra đã dán text tùy chỉnh; tải lại `guide.md` bản mới; tạo lại video |
| Hình minh họa / nền che chữ | Như trên | Tạo lại; nếu vẫn bị, thêm vào ô tùy chỉnh câu "Khung chữ nền trắng trơn, hình đặt bên cạnh" |
| Video trộn nội dung bài khác | Notebook còn tick Kịch bản cũ | Chỉ tick guide.md + Kịch bản bài này; làm xong thì xóa Kịch bản cũ |

## 7. Mang dự án sang máy khác / ổ đĩa khác

Dự án **không phụ thuộc vị trí**: copy cả thư mục `bunpou_skill` đi đâu cũng chạy (Windows, macOS, Linux, ổ USB, Google Drive…).

- Công cụ trong `tools/` tự tìm thư mục gốc dựa vào vị trí của chính nó.
- Mọi file chỉ dùng đường dẫn tương đối; `python tools/check_portable.py` kiểm tra điều này (package.py và validate.py tự chạy).
- Trang `HuongDan.html` tự tính đường dẫn **lúc mở**, nên copy cả dự án sang máy mới vẫn hiện đúng đường dẫn mới.
  Tiến độ "Đã làm" lưu trên trình duyệt nên không đi theo thư mục.
- Máy mới chỉ cần Python 3.8+ (Windows: gõ `py` nếu `python` không chạy) và một công cụ AI.

Cách mang đi: `python tools/package.py --all` → copy `dist/bunpou_skill_v<VERSION>.zip` → giải nén ở đâu cũng được.
