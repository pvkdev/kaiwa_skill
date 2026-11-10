#!/usr/bin/env python3
"""
open_output.py – Mở trang HuongDan.html (gốc dự án) và/hoặc thư mục một bài trên máy người dùng.
Quy trình KHÔNG tự gọi lệnh này (tránh mở chồng nhiều tab khi làm hàng loạt) – chỉ chạy khi người dùng nhờ mở.

Cách dùng:
    python tools/open_output.py                 # mở trang HuongDan.html
    python tools/open_output.py work/<cấp>/<ID>  # mở thư mục bài (File Explorer / Finder)

Không mở được (máy chủ, môi trường không có giao diện…) → chỉ in đường dẫn, không báo lỗi.
Đặt biến môi trường BUNPOU_NO_OPEN=1 để tắt hẳn việc tự mở.
"""
from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


def open_path(p: Path) -> bool:
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(str(p))  # type: ignore[attr-defined]
            return True
        if system == "Darwin":
            return subprocess.call(["open", str(p)]) == 0
        if "microsoft" in platform.release().lower() and shutil.which("explorer.exe"):  # WSL
            win = subprocess.run(["wslpath", "-w", str(p)], capture_output=True, text=True).stdout.strip()
            subprocess.call(["explorer.exe", win])
            return True
        if shutil.which("xdg-open") and (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
            return subprocess.Popen(["xdg-open", str(p)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) is not None
    except Exception:
        pass
    return False


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) > 1:
        print(__doc__)
        return 2
    root = Path(__file__).resolve().parent.parent
    if args:
        target, label = Path(args[0]).resolve(), "thư mục"
        if not target.is_dir():
            print(f"Không tìm thấy thư mục: {target}")
            return 2
    else:
        target, label = root / "HuongDan.html", "trang hướng dẫn"
    ok = os.environ.get("BUNPOU_NO_OPEN") != "1" and open_path(target)
    print(f"{'Đã mở' if ok else 'Không tự mở được'} {label}: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
