# bunpou_skill – Bộ skill làm video ngữ pháp tiếng Nhật với NotebookLM

Dán **bài giảng ngữ pháp thô** + **cấp độ (N5–N1)** cho AI → nhận về **bộ file sẵn sàng đưa vào NotebookLM**
để làm video bài giảng tiếng Việt: thân mật, hài hước, nhiều ví dụ, nghe một lần là nhớ.

Dùng được với **Claude Code, Codex, Gemini CLI, Cursor** và cả **AI dạng chat** (ChatGPT, Gemini, Claude.ai).
Mọi công cụ đọc chung một bộ quy tắc, nên đổi máy, đổi model vẫn cho đầu ra cùng định dạng và chất lượng.

## Bắt đầu nhanh (Claude Code / Codex / Gemini CLI)

```bash
cd <đường-dẫn-tới>/bunpou_skill
claude        # hoặc: codex   /   gemini
```

**Sản xuất hàng loạt (kit 7) – 3 bước:**

1. **Nhập nguồn:** dán một hoặc nhiều bài giảng thô (kèm cấp độ, vd "N2") → AI lưu vào `source/<cấp>/<cấp>_<mẫu>_v01.md`.
   Dán lại cùng mẫu → `_v02`; trùng nguyên văn → bỏ qua. Phiên bản + trạng thái nằm ở `source/<cấp>/_quan_ly.json`.
2. **Xem hàng đợi:** nói "chạy hàng đợi" (hoặc "chạy N2", "chạy 10 bài") → AI liệt kê mẫu chưa có output
   (hoặc ghi có nhưng `work/` không có bài hợp lệ).
3. **Sản xuất:** AI làm lần lượt từng mẫu → `work/<cấp>/<cấp>_<mẫu>_v01_r01/`. Chạy lại cùng phiên bản → `_r02`.

AI tự làm hết. Mở **`HuongDan.html`** ở thư mục gốc (để sẵn 1 tab), bấm **F5** sau mỗi lần AI làm xong: bài mới được chọn sẵn,
kèm 4 bước làm video và nút copy nhanh. Trang có tab theo cấp độ N5–N1 và ô tìm kiếm cho cả thư viện bài.

Hướng dẫn đầy đủ cho từng công cụ: [docs/HUONG_DAN_SU_DUNG.md](docs/HUONG_DAN_SU_DUNG.md)

## File nào dùng để làm gì

| File | Dùng để | Tải lên NotebookLM? |
| --- | --- | --- |
| `guide.md` (gốc dự án, dùng chung) | Quy tắc giảng + trình bày màn hình (2 dòng Nhật / Việt, tô màu mẫu, ngắt dòng…) | ✅ **1 lần duy nhất** |
| `HuongDan.html` (gốc dự án, dùng chung) | Trang làm video: danh sách bài theo cấp độ, tìm kiếm, 4 bước, nút copy | ❌ (mở bằng trình duyệt) |
| `source/<cấp>/…_vNN.md` + `_quan_ly.json` | Bài giảng thô của bạn + quản lý phiên bản, trạng thái | ❌ |
| `work/<cấp>/<ID>/KichBan_<ID>.md` | Kịch bản của bài – file duy nhất trong thư mục bài | ✅ mỗi bài |
| `work/<cấp>/<ID>/_phu/` | File phụ: bài gốc, nhật ký AI, text tùy chỉnh, meta, dữ liệu cho HuongDan.html | ❌ (copy text tùy chỉnh từ trang) |

## Cấu trúc dự án

```text
bunpou_skill/
├── AGENTS.md                 # Quy tắc tổng – điểm vào cho mọi AI (Codex, Cursor…)
├── CLAUDE.md                 # Điểm vào cho Claude Code (nạp AGENTS.md)
├── GEMINI.md                 # Điểm vào cho Gemini CLI (nạp AGENTS.md)
├── VERSION / CHANGELOG.md    # Phiên bản bộ quy tắc
├── HuongDan.html             # ★ Trang làm video cho MỌI bài (mở bằng trình duyệt, F5 để cập nhật)
├── guide.md                  # ★ Quy tắc dựng video – tải lên NotebookLM 1 lần
├── series.json               # Thiết lập chung của series (ngôn ngữ, kiểu hình ảnh…)
├── .claude/skills/bunpou-video/SKILL.md   # Skill cho Claude Code (/bunpou-video)
├── .agents/skills/bunpou-video/SKILL.md   # Cùng skill, cho công cụ theo chuẩn Agent Skills
├── core/                     # ★ NGUỒN QUY TẮC DUY NHẤT
│   ├── WORKFLOW.md           #   Quy trình 8 bước
│   ├── rules/                #   01 nội dung · 02 giọng văn · 03 ví dụ · 04 tiếng Nhật · 05 cấp độ · 06 nhân vật (kho: core/cast.json)
│   ├── templates/            #   Khuôn cho từng file đầu ra
│   └── examples/             #   Ví dụ chuẩn: N3_tokoro-ni-he-wo-de
├── tools/
│   ├── nguon.py              # Nhập nguồn, quản lý phiên bản, hàng đợi, bắt đầu bài (source/ ↔ work/)
│   ├── validate.py           # Kiểm tra 1 bài + tự sinh file phụ + ghi trạng thái nguồn + cập nhật HuongDan.html
│   ├── build_data.py         # Dựng lại dữ liệu cho mọi bài (sau khi sửa tay / đổi series.json, guide.md)
│   ├── build_bundle.py       # Gộp quy tắc → dist/PROMPT_BUNDLE.md cho AI dạng chat
│   ├── open_output.py        # Mở HuongDan.html hoặc thư mục một bài (khi cần)
│   ├── split_chat_output.py  # Tách câu trả lời của AI chat thành file + tự kiểm tra
│   └── package.py            # Đóng gói thành dist/bunpou_skill_v<VERSION>.zip
├── dist/PROMPT_BUNDLE.md     # 1 file prompt duy nhất cho ChatGPT/Gemini/Claude.ai
├── docs/                     # Hướng dẫn sử dụng, hướng dẫn cập nhật quy tắc
├── source/N5 … N1/           # ★ Bài giảng thô: <cấp>_<mẫu>_vNN.md + _quan_ly.json (phiên bản, trạng thái)
├── work/                     # ★ Output
│   ├── _index.js, _hang_doi.json   # tự sinh
│   └── N5 … N1/<cấp>_<mẫu>_vNN_rNN/
│       ├── KichBan_<ID>.md   # ← tải lên NotebookLM
│       └── _phu/             # BaiGoc, GhiChu, TuyChinh, meta, data.js
└── old/                      # Bài làm trước kit 7 (lưu trữ)
```

## Vì sao đầu ra ổn định giữa các model

1. **Một nguồn quy tắc** (`core/`) – mọi công cụ đều trỏ về đây.
2. **Template cố định** – tiêu đề, nhãn, thứ tự không đổi.
3. **Ví dụ chuẩn** – model bắt chước một mẫu cụ thể, không tự sáng tạo định dạng.
4. **Máy kiểm tra** `tools/validate.py` – chặn đầu ra sai định dạng, thiếu ví dụ, ký hiệu lọt lên màn hình, lộ từ "tài liệu/nguồn"…
5. **Nhân vật đa dạng** – `tools/pick_cast.py` chọn nhân vật, nghề, bối cảnh mới cho mỗi bài từ `core/cast.json`, tự tránh tên đã dùng.

## Yêu cầu

- Python 3.8+ (chỉ để chạy công cụ kiểm tra; không cần cài thêm thư viện). Windows có thể gõ `py` thay cho `python`.
- Một trong các công cụ AI ở trên.

## Mang sang máy khác

Cách 1 – file zip: chạy `python tools/package.py` (thêm `--all` để gói cả các bài đã làm) → copy
`dist/bunpou_skill_v<VERSION>.zip` sang máy mới và giải nén.

Cách 2 – copy nguyên thư mục.

Cách 3 – git (khuyên dùng, có lịch sử thay đổi quy tắc):

```bash
git init && git add . && git commit -m "bunpou_skill v1.0.0"
```

Không phụ thuộc đường dẫn tuyệt đối, không cần cài đặt gì thêm.

## Cập nhật quy tắc

Xem [docs/CAP_NHAT_QUY_TAC.md](docs/CAP_NHAT_QUY_TAC.md). Cách nhanh nhất: mở AI trong thư mục dự án và nói
"Cập nhật quy tắc: <điều muốn đổi>" – AI sẽ làm theo quy trình cập nhật.
