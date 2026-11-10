#!/usr/bin/env python3
"""
pick_cast.py – Gợi ý bộ nhân vật + bối cảnh cho tình huống mở màn của một bài, để mọi video KHÔNG dùng lại cùng một nhân vật.

Cách dùng:
    python tools/pick_cast.py <ID>          # vd N2_to-omou-to-to-omottara
    python tools/pick_cast.py <ID> --json

Cách chọn (không tốn token AI, kết quả cố định theo ID):
  - Đếm tên trong core/cast.json đã xuất hiện ở mục 1 (mở màn) của các bài đã có trong work/ (và old/output/).
  - Chọn tên ÍT được dùng nhất (hòa thì xáo theo ID), chọn thêm 1 nhân vật phụ, nghề, nét tính cách, ngoại hình, nơi chốn.
  - Chọn riêng nghề/nơi chốn/nét cũng tránh những cái các bài gần nhất đã dùng (nếu xuất hiện chữ đó trong mục 1).
AI dùng gợi ý này cho mục 1 và câu Kết; các Tình huống ví dụ có thể thêm người khác. Chỉ dùng thư viện chuẩn (Python 3.8+).
"""
from __future__ import annotations

import hashlib
import json
import random
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SCAN = [ROOT / "work" / c for c in ("N5", "N4", "N3", "N2", "N1")] + [ROOT / "old" / "output"]


def lesson_folders() -> list[Path]:
    """Mọi thư mục bài đã có (work/<cấp>/ và bài cũ trong old/output/)."""
    out = []
    for base in SCAN:
        if base.exists():
            out += sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))
    return out
CAST = ROOT / "core" / "cast.json"

LEGACY_NAMES = ["Lan", "Tanaka"]


def opening(folder: Path) -> str:
    kb = folder / f"KichBan_{folder.name}.md"
    if not kb.exists():
        return ""
    m = re.search(r"^## 1\..*?\n(.*?)(?=^## 2\.)", kb.read_text(encoding="utf-8", errors="replace"), re.S | re.M)
    return m.group(1) if m else ""


def used_counts(pool: dict, exclude: str) -> tuple[dict, dict]:
    """Đếm số bài đã dùng mỗi tên (theo mục 1) và mỗi mục nghề/nơi chốn/nét."""
    names = {n["ten"]: 0 for n in pool["ten"]}
    other = {}
    for d in lesson_folders():
        if d.name == exclude:
            continue
        text = opening(d)
        for n in names:
            if re.search(rf"(?<![\wÀ-ỹ])(?<!Việt ){re.escape(n)}(?![\wÀ-ỹ])", text):
                names[n] += 1
        for key in ("nghe", "net", "noi_chon"):
            for item in pool[key]:
                if item.lower() in text.lower():
                    other[item] = other.get(item, 0) + 1
    return names, other


def pick(fid: str) -> dict:
    pool = json.loads(CAST.read_text(encoding="utf-8"))
    rnd = random.Random(int(hashlib.sha256(fid.encode("utf-8")).hexdigest(), 16))
    names, other = used_counts(pool, fid)

    def least_used(items, counts, key=lambda x: x):
        pairs = [(counts.get(key(i), 0), rnd.random(), i) for i in items]
        pairs.sort(key=lambda t: (t[0], t[1]))
        return pairs[0][2]

    main = least_used(pool["ten"], names, key=lambda n: n["ten"])
    rest = [n for n in pool["ten"] if n["ten"] != main["ten"]]
    side = least_used(rest, names, key=lambda n: n["ten"])
    return {
        "id": fid,
        "nhan_vat_chinh": {
            "ten": main["ten"],
            "gioi": main["gioi"],
            "nghe": least_used([x for x in pool["nghe"] if (main["nhom"] == "viet" or "Việt" not in x)
                                 and not (x.startswith("bà ") and main["gioi"] == "nam")
                                 and not (x.startswith("ông ") and main["gioi"] == "nu")], other),
            "net": least_used(pool["net"], other),
            "ngoai_hinh": rnd.choice(pool["ngoai_hinh"]),
        },
        "nhan_vat_phu": {"ten": side["ten"], "vai": least_used(pool["nhan_vat_phu"], {})},
        "noi_chon": least_used(pool["noi_chon"], other),
        "da_dung": {k: v for k, v in sorted(names.items(), key=lambda kv: -kv[1]) if v},
    }


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print("Cách dùng: python tools/pick_cast.py <ID> [--json]")
        return 2
    r = pick(args[0])
    if "--json" in sys.argv:
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 0
    c, s = r["nhan_vat_chinh"], r["nhan_vat_phu"]
    print(f"Gợi ý nhân vật cho {r['id']} (dùng cho mục 1 mở màn và câu Kết):")
    print(f"  Nhân vật chính : {c['ten']} ({'nữ' if c['gioi'] == 'nu' else 'nam'}) – {c['nghe']}; nét: {c['net']}; ngoại hình: {c['ngoai_hinh']}")
    print(f"  Nhân vật phụ   : {s['ten']} – vai: {s['vai']}")
    print(f"  Bối cảnh       : {r['noi_chon']}")
    print("  Cách dùng gợi ý: theo rule 02 (Mở bài và kết bài) và rule 06; không chép danh sách ngoại hình/người phụ vào lời mở màn.")
    if r["da_dung"]:
        print("  Tên đã dùng ở các bài trước (tránh): " + ", ".join(f"{k}×{v}" for k, v in r["da_dung"].items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
