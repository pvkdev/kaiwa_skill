#!/usr/bin/env python3
"""
build_data.py – Sinh các file phụ của một bài và dữ liệu cho trang HuongDan.html ở gốc dự án.

AI chỉ viết 2 file: KichBan_<ID>.md và _phu/GhiChu_<ID>.md. Mọi file còn lại do công cụ này sinh:
    work/<cấp>/<ID>/_phu/meta_<ID>.json      thông tin quản lý (lấy từ Kịch bản + Ghi chú)
    work/<cấp>/<ID>/_phu/TuyChinh_<ID>.txt   text dán vào ô tùy chỉnh video (từ core/templates/TuyChinh.template.txt)
    work/<cấp>/<ID>/_phu/data.js             nội dung bài cho trang HuongDan.html
    work/_index.js                           danh sách mọi bài + tổng hợp nguồn cho trang HuongDan.html

Cách dùng:
    python tools/build_data.py           # dựng lại TOÀN BỘ (kiểm tra từng bài + danh sách) – dùng sau khi sửa tay
    (validate.py tự gọi phần dựng cho bài đang kiểm tra, nên quy trình thường không cần chạy lệnh này.)

Trang HuongDan.html mở trực tiếp từ ổ đĩa (file://) nên không được phép đọc file .md; vì vậy dữ liệu được
đóng gói thành file .js – trình duyệt nạp được bằng thẻ <script>. Chạy xong chỉ cần tải lại trang (F5).
Chỉ dùng thư viện chuẩn của Python (3.8+).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
INDEX = WORK / "_index.js"
LEVELS = ["N5", "N4", "N3", "N2", "N1"]
GUIDE = ROOT / "guide.md"
SERIES = ROOT / "series.json"
TUYCHINH_TPL = ROOT / "core" / "templates" / "TuyChinh.template.txt"
SUB = "_phu"

USAGE_RE = re.compile(r"^## [345]\.\d+ Cách dùng(?: \d+)?: (.+)$", re.M)
PHRASE_RE = re.compile(r"^## [34]\.\d+ Cách nói thường gặp: (.+)$", re.M)
EXAMPLE_RE = re.compile(r"^### Ví dụ \d+( \[MỚI\])?\s*$", re.M)
LEVEL_RE = re.compile(r"^(N[1-5])")


def files_of(folder: Path) -> dict:
    fid = folder.name
    sub = folder / SUB
    return {
        "kichban": folder / f"KichBan_{fid}.md",
        "ghichu": sub / f"GhiChu_{fid}.md",
        "baigoc": sub / f"BaiGoc_{fid}.md",
        "meta": sub / f"meta_{fid}.json",
        "tuychinh": sub / f"TuyChinh_{fid}.txt",
        "data": sub / "data.js",
    }


def version() -> str:
    return (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def ghichu_field(text: str, label: str) -> str:
    m = re.search(rf"^- {re.escape(label)}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def derive(folder: Path) -> tuple[dict, str]:
    """Tạo meta + text tùy chỉnh từ Kịch bản và Ghi chú. Trả về (meta, tuychinh)."""
    f = files_of(folder)
    fid = folder.name
    kb = read(f["kichban"])
    gc = read(f["ghichu"])
    first = kb.splitlines()[0] if kb else ""
    title = first[2:].strip() if first.startswith("# ") else ""
    mau_raw, _, nghia = title.partition(" – ")
    lv = LEVEL_RE.match(fid)
    examples = EXAMPLE_RE.findall(kb)
    meta = {
        "id": fid,
        "mau": mau_raw.strip(),
        "mau_doc": mau_raw.strip(),
        "nghia": nghia.strip(),
        "cap_do": lv.group(1) if lv else ghichu_field(gc, "Cấp độ"),
        "cach_dung": [u.strip() for u in USAGE_RE.findall(kb)],
        "cach_noi": [u.strip() for u in PHRASE_RE.findall(kb)],
        "so_vi_du": len(examples),
        "so_vi_du_moi": sum(1 for e in examples if e),
        "phien_ban_quy_tac": ghichu_field(gc, "Phiên bản quy tắc") or version(),
        "ngay_tao": ghichu_field(gc, "Ngày tạo"),
        "cong_cu_ai": ghichu_field(gc, "Công cụ AI / model"),
    }
    tpl = TUYCHINH_TPL.read_text(encoding="utf-8")
    rep = {
        "{{ID}}": fid,
        "{{MAU}}": meta["mau"],
        "{{NGHIA}}": meta["nghia"],
        "{{CAP_DO}}": meta["cap_do"],
        "{{DS_CACH_DUNG}}": (meta["cach_dung"][0] if len(meta["cach_dung"]) == 1
                             else "; ".join(f"({i}) {u}" for i, u in enumerate(meta["cach_dung"], 1))),
        "{{CHUONG}}": (CHUONG_ONE if len(meta["cach_dung"]) == 1 else CHUONG_MANY),
        "{{SO_VI_DU}}": str(meta["so_vi_du"]),
        "{{TRINH_TU}}": scene_order(kb),
    }
    for k, v in rep.items():
        tpl = tpl.replace(k, v)
    return meta, tpl


CHUONG_MANY = ('Mỗi cách dùng là một chương trọn vẹn: giảng xong Ý nghĩa → Cách chia → toàn bộ ví dụ của cách dùng đó rồi mới sang '
               'cách dùng tiếp theo. Khung mở chương chỉ ghi "Cách dùng 1" + tên cách dùng – luôn viết số bằng chữ số (1, 2, 3…), '
               'không viết "một, hai, ba".')
CHUONG_ONE = ('Bài chỉ có MỘT cách dùng: chương cách dùng trọn vẹn gồm Ý nghĩa → Cách chia → toàn bộ ví dụ. Khung mở chương chỉ ghi '
              '"Cách dùng" + tên cách dùng, KHÔNG đánh số (không viết, không nói "Cách dùng 1" hay "cách dùng thứ nhất").')


def scene_order(kb: str) -> str:
    """Trình tự cảnh bắt buộc, sinh từ Kịch bản (đưa vào text tùy chỉnh để NotebookLM không bỏ phần nào)."""
    out: list[str] = []
    cur: dict | None = None

    def flush() -> None:
        nonlocal cur
        if not cur:
            return
        ex = cur["ex"]
        rng = (f"Ví dụ {ex[0]}" if len(ex) == 1 else f"Ví dụ {ex[0]}–{ex[-1]}") if ex else ""
        if cur["kind"] == "usage" and cur["meaning"]:
            chia = []
            if cur["same"]:
                chia.append(f"nhắc lại cách chia của cách dùng {cur['same']}")
            if cur["cards"]:
                chia.append(f"{cur['cards']} thẻ công thức")
            parts = ["Ý nghĩa và cách dùng (có câu mẫu)", "Cách chia (" + " + ".join(chia) + ")", rng]
            out.append(f"{cur['title']}: " + " → ".join(p for p in parts if p))
        elif cur["kind"] == "phrase":
            out.append(f"{cur['title']}: cụm + nghĩa + giải thích → {rng}")
        elif cur["kind"] == "usage":
            out.append(f"{cur['title']}: {rng}")
        elif cur["kind"] == "struct5":
            out.append(f"Cấu trúc và cách chia ({cur['cards']} thẻ công thức)")
        elif cur["kind"] == "traps":
            out.append(f"Bẫy dễ nhầm ({cur['cards']} bẫy)")
        elif cur["kind"] == "sum":
            extra = []
            if cur["real"]:
                extra.append("tình huống thực tế")
            if cur["native"]:
                extra.append(f"người Nhật thường nói ({cur['native']} câu)")
            out.append("Tổng kết, mẹo nhớ, lưu ý" + ("".join(", " + e for e in extra)) + " → câu kết")
        else:
            out.append(cur["title"])
        cur = None

    for line in kb.splitlines():
        if line.startswith("## "):
            flush()
            h = line[3:].strip()
            mu = re.match(r"\d\.\d+ (Cách dùng(?: \d+)?): (.+)", h)
            mp = re.match(r"\d\.\d+ Cách nói thường gặp: (.+)", h)
            base = {"ex": [], "cards": 0, "same": 0, "real": False, "native": 0, "meaning": False, "desc": False}
            if mu:
                cur = dict(base, kind="usage", title=f"{mu.group(1)} – {mu.group(2)}")
            elif mp:
                cur = dict(base, kind="phrase", title=f"Cách nói thường gặp – {mp.group(1)}")
            elif h.startswith("4. Cấu trúc"):
                cur = dict(base, kind="struct5", title=h)
            elif "Bẫy" in h:
                cur = dict(base, kind="traps", title=h)
            elif "Tổng kết" in h:
                cur = dict(base, kind="sum", title=h)
            else:
                cur = dict(base, kind="plain", title=re.sub(r"^\d+\.\s*", "", h))
            continue
        if not cur:
            continue
        m = re.match(r"^### Ví dụ (\d+)", line)
        if line.startswith("### Ý nghĩa và cách dùng"):
            cur["meaning"] = True
        elif line.startswith("**Mô tả:**"):
            cur["title"] = "Giới thiệu & mô tả mẫu ngữ pháp: tên mẫu thật to, nghĩa, các ý mô tả"
        elif m:
            cur["ex"].append(int(m.group(1)))
        elif re.match(r"^\*\*(Cấu trúc \d+|Bẫy \d+ – .+?):\*\*", line):
            cur["cards"] += 1
        elif (g := re.match(r"^\*\*Giống cách dùng (\d+):\*\*", line)):
            cur["same"] = int(g.group(1))
        elif line.startswith("**Tình huống thực tế:**"):
            cur["real"] = True
        elif line.startswith("**Người Nhật thường nói:**"):
            cur["in_native"] = True
        elif line.startswith("**Kết:**"):
            cur["in_native"] = False
        elif cur.get("in_native") and line.startswith("**Nhật:**"):
            cur["native"] += 1
    flush()
    out.insert(0, "Intro: khung tiêu đề – chỉ tên mẫu")
    return "\n".join(f"▸ {o}" for o in out)


def js_payload(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1).replace("</", "<\\/")


def write_lesson(folder: Path, n_err: int, n_warn: int) -> dict:
    """Ghi meta, TuyChinh và (với bài trong work/) data.js. Trả về meta."""
    folder = folder.resolve()
    f = files_of(folder)
    f["meta"].parent.mkdir(exist_ok=True)
    meta, tuychinh = derive(folder)
    f["tuychinh"].write_text(tuychinh, encoding="utf-8")
    kb_mtime = f["kichban"].stat().st_mtime if f["kichban"].exists() else 0
    meta["kiem_tra"] = {
        "loi": n_err,
        "canh_bao": n_warn,
        "luc": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "kichban_sua_luc": datetime.fromtimestamp(kb_mtime).strftime("%Y-%m-%d %H:%M:%S") if kb_mtime else "",
    }
    f["meta"].write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if in_work(folder):
        meta["thu_muc"] = folder.relative_to(ROOT).as_posix()
        f["meta"].write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        data = {
            "id": meta["id"],
            "kichban": read(f["kichban"]),
            "tuychinh": tuychinh,
            "ghichu": read(f["ghichu"]),
        }
        f["data"].write_text(
            "// Sinh tự động bởi tools/build_data.py – KHÔNG sửa tay.\n"
            "(window.BUNPOU_LESSON = window.BUNPOU_LESSON || {})[" + json.dumps(meta["id"]) + "] = "
            + js_payload(data) + ";\n",
            encoding="utf-8",
        )
    return meta


def in_work(folder: Path) -> bool:
    folder = folder.resolve()
    return folder.parent.parent == WORK.resolve() and folder.parent.name in LEVELS


def lesson_dirs() -> list[Path]:
    """Mọi thư mục bài trong work/<cấp>/ (N5 → N1)."""
    out = []
    for cap in LEVELS:
        d = WORK / cap
        if d.exists():
            out += sorted(p for p in d.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))
    return out


def nguon_summary() -> dict:
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import nguon  # type: ignore
        return nguon.tong_hop()
    except Exception:
        return {}


def write_index() -> int:
    """Dựng lại work/_index.js từ meta của mọi bài. Trả về số bài."""
    lessons, missing = [], []
    for d in lesson_dirs():
        m = files_of(d)["meta"]
        if not m.exists():
            missing.append(d.name)
            continue
        try:
            meta = json.loads(m.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            missing.append(d.name)
            continue
        meta["kichban"] = f"KichBan_{d.name}.md"
        meta["thu_muc"] = d.relative_to(ROOT).as_posix()
        lessons.append(meta)
    series = {}
    if SERIES.exists():
        try:
            series = {k: v for k, v in json.loads(SERIES.read_text(encoding="utf-8")).items() if not k.startswith("_")}
        except json.JSONDecodeError:
            pass
    newest = max(lessons, key=lambda x: x.get("kiem_tra", {}).get("kichban_sua_luc", ""), default=None)
    index = {
        "phien_ban": version(),
        "dung_luc": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "moi_nhat": newest["id"] if newest else "",
        "moi_nhat_luc": newest.get("kiem_tra", {}).get("kichban_sua_luc", "") if newest else "",
        "chua_co_du_lieu": missing,
        "nguon": nguon_summary(),
        "series": series,
        "guide": read(GUIDE),
        "bai": lessons,
    }
    WORK.mkdir(exist_ok=True)
    INDEX.write_text(
        "// Sinh tự động bởi tools/build_data.py – KHÔNG sửa tay. Danh sách bài cho HuongDan.html.\n"
        "window.BUNPOU_INDEX = " + js_payload(index) + ";\n",
        encoding="utf-8",
    )
    return len(lessons)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import validate  # type: ignore

    dirs = lesson_dirs()
    bad = 0
    for d in dirs:
        if not files_of(d)["kichban"].exists():
            print(f"  bỏ qua {d.name}/ (chưa có KichBan_{d.name}.md)")
            continue
        rep = validate.check_folder(d)
        bad += bool(rep.errors)
        print(f"  {'ĐẠT ' if not rep.errors else 'LỖI '} {d.name} – {len(rep.errors)} lỗi, {len(rep.warnings)} cảnh báo")
    n = write_index()
    print(f"Đã dựng {INDEX.relative_to(ROOT).as_posix()} – {n} bài. Tải lại trang HuongDan.html (F5) để xem.")
    if bad:
        print(f"{bad} bài còn LỖI – chạy python tools/validate.py work/<cấp>/<ID> để xem chi tiết.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
