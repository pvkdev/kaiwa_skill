#!/usr/bin/env python3
"""
check_portable.py – Kiểm tra dự án không chứa đường dẫn tuyệt đối, để copy thư mục sang máy/ổ đĩa khác vẫn chạy.

Cách dùng:
    python tools/check_portable.py               # quét toàn bộ dự án
    python tools/check_portable.py work/<cấp>/<ID>   # chỉ quét một thư mục

Thoát mã 0 nếu sạch, 1 nếu phát hiện đường dẫn tuyệt đối (in ra file:dòng).
package.py và validate.py tự gọi kiểm tra này.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEXT_EXT = {".md", ".txt", ".json", ".py", ".html", ".yml", ".yaml", ".toml", ".cfg", ".ini"}
SKIP_DIRS = {".git", "dist", "__pycache__", "node_modules", "old", "source"}
PATTERNS = [
    ("ổ đĩa Windows", re.compile(r"(?<![\w])[A-Za-z]:\\[^\s\\]")),
    ("ổ đĩa Windows", re.compile(r"(?<![\w/])[A-Za-z]:/(?:[^\s/]+/)+")),
    ("thư mục người dùng", re.compile(r"(?<![\w./])/(?:home|Users|sessions|root|mnt|tmp|var/folders)/[\w.-]+")),
    ("UNC", re.compile(r"\\\\[A-Za-z0-9.-]+\\[^\s]")),
    ("file:///", re.compile(r"file:///(?!…|\.\.\.)[^\s`)]+")),
]
HTML_DATA_RE = re.compile(r'<script id="bunpou-data" type="application/json">(.*?)</script>', re.S)
SELF = Path(__file__).resolve()


def scan_text(text: str):
    for i, line in enumerate(text.splitlines(), 1):
        for label, rx in PATTERNS:
            m = rx.search(line)
            if m and "…" not in m.group(0) and "<" not in m.group(0):  # bỏ qua ví dụ minh họa trong tài liệu
                yield i, label, m.group(0)
                break


def scan_file(p: Path):
    if p.resolve() == SELF:
        return
    try:
        text = p.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return
    if p.suffix == ".html":
        m = HTML_DATA_RE.search(text)
        if m:  # chỉ quét dữ liệu nhúng; mã JS của template không chứa đường dẫn cố định
            try:
                data = json.loads(m.group(1))
                vals = [str(v) for k, v in data.items() if k not in ("content", "series")]
                vals += [str(v) for v in (data.get("content") or {}).values()]
                vals += [str(v) for v in (data.get("series") or {}).values()]
                text = "\n".join(vals)
            except (json.JSONDecodeError, AttributeError):
                pass
    for i, label, hit in scan_text(text):
        try:
            where = p.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            where = str(p)
        yield f"{where}:{i}", label, hit


def scan(target: Path):
    files = [target] if target.is_file() else sorted(
        f for f in target.rglob("*")
        if f.is_file() and f.suffix in TEXT_EXT and not (SKIP_DIRS & set(f.relative_to(target).parts))
    )
    for f in files:
        yield from scan_file(f)


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    target = Path(argv[1]).resolve() if len(argv) > 1 else ROOT
    hits = list(scan(target))
    for where, label, hit in hits:
        print(f"LỖI [{where}] Đường dẫn tuyệt đối ({label}): {hit}")
    if hits:
        print(f"→ {len(hits)} chỗ. Đổi sang đường dẫn tương đối từ thư mục gốc dự án (vd work/<cấp>/<ID>/…).")
        return 1
    print("Sạch: không có đường dẫn tuyệt đối – mang thư mục đi đâu cũng chạy.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
