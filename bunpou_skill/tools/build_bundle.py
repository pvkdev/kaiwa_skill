#!/usr/bin/env python3
"""
build_bundle.py – Gộp toàn bộ quy tắc thành 1 file prompt cho các AI chỉ có giao diện chat
(ChatGPT, Gemini, Claude.ai web…), không đọc được thư mục dự án.

Cách dùng:
    python tools/build_bundle.py
Kết quả: dist/PROMPT_BUNDLE.md

Chạy lại lệnh này MỖI KHI sửa bất kỳ file nào trong core/ hoặc AGENTS.md.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "PROMPT_BUNDLE.md"
GOLD = ROOT / "core" / "examples" / "N3_tokoro-ni-he-wo-de"

PARTS = [
    ("AGENTS.md", "Quy tắc tổng"),
    ("core/WORKFLOW.md", "Quy trình"),
    ("core/rules/01_noi-dung.md", "Rule 01"),
    ("core/rules/02_giong-van.md", "Rule 02"),
    ("core/rules/03_vi-du.md", "Rule 03"),
    ("core/rules/04_tieng-nhat.md", "Rule 04"),
    ("core/rules/05_cap-do.md", "Rule 05"),
    ("core/rules/06_nhan-vat.md", "Rule 06"),
    ("core/templates/KichBan.template.md", "Template Kịch bản"),
    ("core/templates/GhiChuBienTap.template.md", "Template Ghi chú biên tập"),
    ("core/examples/N3_tokoro-ni-he-wo-de/KichBan_N3_tokoro-ni-he-wo-de.md", "VÍ DỤ CHUẨN – Kịch bản"),
]

CHAT_MODE = """# BỘ PROMPT LÀM VIDEO NGỮ PHÁP TIẾNG NHẬT (chế độ chat)

Phiên bản quy tắc: {version}

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
"""


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    chunks = [CHAT_MODE.format(version=version)]
    for rel, title in PARTS:
        p = ROOT / rel
        if not p.exists():
            print(f"LỖI: thiếu {rel}")
            return 1
        body = p.read_text(encoding="utf-8").rstrip()
        fence = "````"
        chunks.append(f"\n\n---\n\n## [{title}] `{rel}`\n\n{fence}\n{body}\n{fence}\n")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(chunks), encoding="utf-8")

    # kiểm tra 2 bản SKILL.md đồng bộ
    a = ROOT / ".claude/skills/bunpou-video/SKILL.md"
    b = ROOT / ".agents/skills/bunpou-video/SKILL.md"
    if a.exists() and b.exists() and a.read_text(encoding="utf-8") != b.read_text(encoding="utf-8"):
        print("CẢNH BÁO: .claude/skills và .agents/skills có SKILL.md khác nhau – hãy chép cho giống nhau.")

    print(f"Đã tạo {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB, phiên bản {version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
