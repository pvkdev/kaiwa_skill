#!/usr/bin/env python3
"""
split_chat_output.py – Tách câu trả lời của AI dạng chat (dùng dist/PROMPT_BUNDLE.md) thành các file thật.

Cách dùng:
    1. Copy toàn bộ câu trả lời của AI, lưu thành 1 file văn bản, vd: tmp_chat.txt
    2. python tools/split_chat_output.py tmp_chat.txt
Trước đó tạo thư mục bài bằng `python tools/nguon.py bat-dau <file nguồn>` (cho biết <ID> để đưa vào AI chat).
Kết quả: work/<cấp>/<ID>/KichBan_<ID>.md + work/<cấp>/<ID>/_phu/GhiChu_<ID>.md; validate.py tự sinh các file còn lại
và cập nhật HuongDan.html (tải lại trang là thấy bài mới).
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARK = re.compile(r"^=== FILE: (.+?) ===\s*$", re.M)
FENCE = re.compile(r"^(`{3,}|~{3,})[^\n]*\n(.*?)\n\1\s*$", re.S | re.M)


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    if len(argv) != 2:
        print(__doc__)
        return 2
    text = Path(argv[1]).read_text(encoding="utf-8")
    marks = list(MARK.finditer(text))
    if not marks:
        print("Không tìm thấy dòng `=== FILE: <tên> ===` nào.")
        return 1

    files: dict[str, str] = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        chunk = text[m.end():end]
        fm = FENCE.search(chunk)
        files[m.group(1).strip()] = (fm.group(2) if fm else chunk.strip()) + "\n"

    kb = next((n for n in files if n.startswith("KichBan_") and n.endswith(".md")), None)
    if not kb:
        print("Không có file KichBan_<ID>.md trong câu trả lời.")
        return 1
    file_id = kb[len("KichBan_"):-3]
    m = re.match(r"^(N[1-5])_(.+)_v(\d{2,})_r(\d{2,})$", file_id)
    if not m:
        print(f"ID `{file_id}` sai dạng <cấp>_<mẫu>_vNN_rNN – tạo thư mục bằng `python tools/nguon.py bat-dau <file nguồn>` trước.")
        return 1
    out = ROOT / "work" / m.group(1) / file_id
    if (out / f"KichBan_{file_id}.md").exists():
        print(f"{out.relative_to(ROOT).as_posix()} đã có Kịch bản – chạy `nguon.py bat-dau` để lấy lần chạy mới (_rNN tiếp theo).")
        return 1
    sub = out / "_phu"
    sub.mkdir(parents=True, exist_ok=True)
    for name, body in files.items():
        safe = Path(name).name
        if not safe.startswith(("KichBan_", "GhiChu_", "BaiGoc_")):
            print(f"  - bỏ qua {safe} (file này do công cụ tự sinh)")
            continue
        dest = out / safe if safe.startswith("KichBan_") else sub / safe
        dest.write_text(body, encoding="utf-8")
        print(f"  + {dest.relative_to(ROOT).as_posix()}")

    print()
    return subprocess.call([sys.executable, str(ROOT / "tools/validate.py"), str(out)])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
