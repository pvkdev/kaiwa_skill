#!/usr/bin/env python3
"""
package.py – Đóng gói dự án thành 1 file zip để mang sang máy khác.

Cách dùng:
    python tools/package.py              # gói quy tắc + công cụ (bỏ dữ liệu trong source/, work/, old/)
    python tools/package.py --all        # gói cả dữ liệu source/, work/, old/
Trước khi gói, tự chạy check_portable.py: còn đường dẫn tuyệt đối thì dừng (thêm --force để bỏ qua).
Kết quả: dist/bunpou_skill_v<VERSION>.zip
Giải nén ở máy mới là dùng được ngay.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
SKIP_PARTS = {"__pycache__", ".git"}


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    include_work = "--all" in argv
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import check_portable  # type: ignore
    hits = list(check_portable.scan(ROOT))
    if hits and "--force" not in argv:
        for where, label, hit in hits:
            print(f"LỖI [{where}] Đường dẫn tuyệt đối ({label}): {hit}")
        print("Dừng đóng gói: sửa các chỗ trên (hoặc thêm --force nếu chắc chắn).")
        return 1
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    out = ROOT / "dist" / f"bunpou_skill_v{version}.zip"
    out.parent.mkdir(exist_ok=True)
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob("*")):
            rel = p.relative_to(ROOT)
            if p.is_dir() or SKIP_PARTS & set(rel.parts):
                continue
            if rel.parts[0] == "dist" and p.suffix == ".zip":
                continue
            if p.name.startswith("tmp_chat"):
                continue
            if len(rel.parts) == 1 and p.suffix == ".zip":
                continue  # file zip tạm ở gốc dự án
            if rel.parts[0] == "draft":
                continue  # thư mục nháp riêng của người dùng
            if not include_work and rel.parts[0] in ("output", "work", "source", "old") and p.name != ".gitkeep":
                continue
            z.write(p, Path("bunpou_skill") / rel)
            count += 1
    print(f"Đã tạo {out.relative_to(ROOT)} – {count} file")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
