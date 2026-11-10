#!/usr/bin/env python3
"""
nguon.py – Quản lý NGUỒN bài giảng (source/) và HÀNG ĐỢI sản xuất (work/) – kit 7.x.

    source/<cấp>/<cấp>_<mẫu>_vNN.md     bài giảng thô (nguyên văn), mỗi lần dán lại cùng mẫu → phiên bản mới
    source/<cấp>/_quan_ly.json          phiên bản hiện tại, lịch sử phiên bản, trạng thái, các output
    work/<cấp>/<cấp>_<mẫu>_vNN_rNN/     output của một lần chạy (KichBan + _phu/)

Cách dùng:
    python tools/nguon.py them <file> [--cap N2] [--mau "〜…"]
        Nhập 1 hoặc nhiều bài giảng từ một file văn bản. Nhiều bài: ngăn bằng dòng  ---BÀI---  hoặc  ---BÀI N2---
        (cấp ghi ở dòng ngăn > --cap > dòng "Cấp độ: Nx" trong bài). Tên mẫu lấy từ dòng tiếng Nhật đầu tiên (hoặc --mau).
        Bài trùng nguyên văn với một phiên bản đã có → bỏ qua.
    python tools/nguon.py dong-bo
        Đăng ký các file .md thả tay vào source/<cấp>/, cập nhật danh sách output thật trong work/.
    python tools/nguon.py hang-doi [--cap N2] [--so 10]
        Liệt kê mẫu cần chạy (chưa có output, hoặc ghi "đã có output" nhưng work/ không có bài hợp lệ) → work/_hang_doi.json.
    python tools/nguon.py bat-dau <file nguồn | mã mẫu>
        Tạo work/<cấp>/<ID>/ (ID = tên nguồn + _rNN), chép bài gốc vào _phu/, chọn nhân vật, đánh dấu "đang chạy".
    python tools/nguon.py trang-thai [--cap N2]
        Tổng hợp theo cấp độ.

validate.py tự gọi danh_dau() khi kiểm tra một bài trong work/: ĐẠT → "da_co_output", còn LỖI → "loi".
Chỉ dùng thư viện chuẩn của Python (3.8+).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "source"
WORK = ROOT / "work"
LEVELS = ["N5", "N4", "N3", "N2", "N1"]
MANIFEST = "_quan_ly.json"
QUEUE = WORK / "_hang_doi.json"

SRC_RE = re.compile(r"^(N[1-5])_(.+)_v(\d{2,})\.md$")
ID_RE = re.compile(r"^(N[1-5])_(.+)_v(\d{2,})_r(\d{2,})$")
SPLIT_RE = re.compile(r"^\s*-{3,}\s*B[ÀA]I(?:\s+(N[1-5]))?\s*-{3,}\s*$", re.M | re.I)
CAP_LINE_RE = re.compile(r"^\s*Cấp độ\s*:\s*(N[1-5])\s*$", re.M)
JP_RE = re.compile(r"[぀-ヿ㐀-鿿]")
WIN_BAD = {"\\": "＼", "/": "・", ":": "：", "*": "＊", "?": "？", '"': "＂", "<": "＜", ">": "＞", "|": "｜"}
STATUS_TEXT = {"chua_chay": "chưa chạy", "dang_chay": "đang chạy", "da_co_output": "đã có output", "loi": "lỗi"}


# ---------------------------------------------------------------- tên file, mã mẫu
def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def safe_name(mau: str) -> str:
    """〜にしろ／にせよ／にしても → にしろ・にせよ・にしても (giữ chữ Nhật, an toàn cho tên file Windows)."""
    s = mau.strip()
    s = re.sub(r"^[〜～~\s]+", "", s)
    s = s.replace("／", "・").replace("～", "〜").replace("~", "〜")
    s = re.sub(r"[\s\u3000]+", "", s)
    s = "".join(WIN_BAD.get(c, c) for c in s)
    s = re.sub(r"・{2,}", "・", s).strip("・.")
    return s[:60] or "khong-ten"


def norm_mau(mau: str) -> str:
    s = re.sub(r"\s+", "", mau.strip()).replace("～", "〜").replace("~", "〜")
    return s if s.startswith("〜") else "〜" + s


def text_hash(text: str) -> str:
    return hashlib.sha1(re.sub(r"\s+", " ", text).strip().encode("utf-8")).hexdigest()[:16]


def detect_mau(text: str) -> str:
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line and JP_RE.search(line) and not CAP_LINE_RE.match(line):
            return line
    return ""


def ver_str(n: int) -> str:
    return f"v{n:02d}"


def ver_num(v: str) -> int:
    return int(v.lstrip("v"))


# ---------------------------------------------------------------- khóa + đọc/ghi manifest
class Lock:
    """Khóa ghi bằng khóa hệ điều hành trên file source/<cấp>/.lock (an toàn khi nhiều tác vụ chạy song song).
    Không xóa file khóa – dùng được cả ở thư mục không cho phép xóa file."""

    def __init__(self, cap: str) -> None:
        self.path = SOURCE / cap / ".lock"
        self.f = None

    def _try(self) -> bool:
        try:
            if os.name == "nt":
                import msvcrt
                self.f.seek(0)
                msvcrt.locking(self.f.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except OSError:
            return False

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.f = open(self.path, "a+")
        deadline = time.time() + 60
        while not self._try():
            if time.time() > deadline:
                self.f.close()
                raise SystemExit(f"Không lấy được khóa {self.path} – có tác vụ khác đang ghi nguồn {self.path.parent.name}; thử lại sau.")
            time.sleep(0.2)
        return self

    def __exit__(self, *exc) -> None:
        try:
            if os.name == "nt":
                import msvcrt
                self.f.seek(0)
                msvcrt.locking(self.f.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.f.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        self.f.close()


def load(cap: str) -> dict:
    p = SOURCE / cap / MANIFEST
    if p.exists():
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            data.setdefault("mau", [])
            return data
        except json.JSONDecodeError as e:
            raise SystemExit(f"{p.relative_to(ROOT).as_posix()} hỏng JSON ({e}) – sửa tay hoặc xóa rồi chạy `nguon.py dong-bo`.")
    return {"cap_do": cap, "mau": []}


def save(cap: str, data: dict) -> None:
    data["cap_do"] = cap
    data["cap_nhat"] = now()
    data["_ghi_chu"] = "Do tools/nguon.py quản lý. Đọc thoải mái; muốn sửa thì chạy lại `python tools/nguon.py dong-bo`."
    data["mau"].sort(key=lambda e: e["ma"])
    p = SOURCE / cap / MANIFEST
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")  # đang giữ khóa


def find(data: dict, ma: str) -> dict | None:
    return next((e for e in data["mau"] if e["ma"] == ma), None)


def versions(entry: dict) -> list[dict]:
    """Mọi phiên bản của một mẫu (hiện tại + lịch sử), mỗi phần tử là dict có phien_ban/file/trang_thai/output."""
    return [entry] + entry.get("lich_su", [])


def version_rec(entry: dict, ver: str) -> dict | None:
    return next((v for v in versions(entry) if v["phien_ban"] == ver), None)


def push_history(entry: dict) -> None:
    rec = {k: entry[k] for k in ("phien_ban", "file", "them_luc", "bam", "trang_thai", "output") if k in entry}
    entry.setdefault("lich_su", []).insert(0, rec)


# ---------------------------------------------------------------- work/
def work_dirs(cap: str, ma: str, ver: str) -> list[Path]:
    d = WORK / cap
    if not d.exists():
        return []
    pat = re.compile(re.escape(f"{ma}_{ver}_r") + r"(\d{2,})$")
    return sorted((p for p in d.iterdir() if p.is_dir() and pat.match(p.name)), key=lambda p: int(pat.match(p.name).group(1)))


def valid_output(folder: Path) -> bool:
    """Bài có Kịch bản và lần kiểm tra gần nhất 0 lỗi."""
    if not (folder / f"KichBan_{folder.name}.md").exists():
        return False
    meta = folder / "_phu" / f"meta_{folder.name}.json"
    if not meta.exists():
        return False
    try:
        return json.loads(meta.read_text(encoding="utf-8")).get("kiem_tra", {}).get("loi", 1) == 0
    except json.JSONDecodeError:
        return False


# ---------------------------------------------------------------- them
def add_one(cap: str, text: str, mau: str, quiet: bool = False) -> str:
    text = CAP_LINE_RE.sub("", text, count=1).strip("\n") + "\n"
    mau = norm_mau(mau)
    ma = f"{cap}_{safe_name(mau)}"
    h = text_hash(text)
    with Lock(cap):
        data = load(cap)
        entry = find(data, ma)
        if entry:
            dup = next((v for v in versions(entry) if v.get("bam") == h), None)
            if dup:
                return f"  = {ma}: trùng nguyên văn {dup['phien_ban']} – bỏ qua"
            n = max(ver_num(v["phien_ban"]) for v in versions(entry)) + 1
        else:
            n = 1
        while (SOURCE / cap / f"{ma}_{ver_str(n)}.md").exists():
            n += 1
        fname = f"{ma}_{ver_str(n)}.md"
        (SOURCE / cap).mkdir(parents=True, exist_ok=True)
        (SOURCE / cap / fname).write_text(text, encoding="utf-8")
        rec = {"phien_ban": ver_str(n), "file": fname, "them_luc": now(), "bam": h, "trang_thai": "chua_chay", "output": []}
        if entry:
            old = entry["phien_ban"]
            push_history(entry)
            entry.update(rec)
            entry["mau"] = mau
            msg = f"  + source/{cap}/{fname}  (phiên bản mới; {old} chuyển vào lịch sử)"
        else:
            data["mau"].append(dict(ma=ma, mau=mau, **rec, lich_su=[]))
            msg = f"  + source/{cap}/{fname}"
        save(cap, data)
    return msg


def cmd_them(args: list[str]) -> int:
    opts, rest = parse_opts(args, ("--cap", "--mau"))
    if not rest:
        print("Thiếu file: python tools/nguon.py them <file> [--cap N2] [--mau \"〜…\"]")
        return 2
    raw = Path(rest[0]).read_text(encoding="utf-8")
    marks = list(SPLIT_RE.finditer(raw))
    chunks: list[tuple[str | None, str]] = []
    if marks:
        if raw[:marks[0].start()].strip():
            chunks.append((None, raw[:marks[0].start()]))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(raw)
            chunks.append((m.group(1), raw[m.end():end]))
    else:
        chunks.append((None, raw))
    chunks = [(c, t) for c, t in chunks if t.strip()]
    bad = 0
    print(f"Nhập {len(chunks)} bài:")
    for i, (cap_mark, text) in enumerate(chunks, 1):
        m = CAP_LINE_RE.search(text)
        cap = (cap_mark or opts.get("--cap") or (m.group(1) if m else "")).upper()
        mau = (opts.get("--mau") if len(chunks) == 1 else None) or detect_mau(text)
        if cap not in LEVELS:
            print(f"  ! bài {i}: không biết cấp độ – ghi ---BÀI N2--- hoặc --cap N2")
            bad += 1
            continue
        if not mau:
            print(f"  ! bài {i}: không tìm thấy tên mẫu (dòng tiếng Nhật đầu tiên) – dùng --mau")
            bad += 1
            continue
        print(add_one(cap, text, mau))
    print("Xem hàng đợi: python tools/nguon.py hang-doi")
    return 1 if bad else 0


# ---------------------------------------------------------------- dong-bo
def sync(quiet: bool = False) -> list[str]:
    notes: list[str] = []
    for cap in LEVELS:
        d = SOURCE / cap
        if not d.exists():
            continue
        with Lock(cap):
            data = load(cap)
            known = {(e["ma"], v["phien_ban"]) for e in data["mau"] for v in versions(e)}
            for f in sorted(d.glob("*.md")):
                m = SRC_RE.match(f.name)
                if not m:
                    if not f.name.startswith(("_", ".")):
                        notes.append(f"  ! source/{cap}/{f.name}: tên không đúng dạng <cấp>_<mẫu>_vNN.md – bỏ qua (dùng `nguon.py them` để nhập)")
                    continue
                if m.group(1) != cap:
                    notes.append(f"  ! source/{cap}/{f.name}: cấp trong tên khác thư mục – bỏ qua")
                    continue
                ma, ver = f"{cap}_{m.group(2)}", ver_str(int(m.group(3)))
                if (ma, ver) in known:
                    continue
                text = f.read_text(encoding="utf-8", errors="replace")
                rec = {"phien_ban": ver, "file": f.name, "them_luc": now(), "bam": text_hash(text), "trang_thai": "chua_chay", "output": []}
                entry = find(data, ma)
                if not entry:
                    data["mau"].append(dict(ma=ma, mau=norm_mau(detect_mau(text) or m.group(2)), **rec, lich_su=[]))
                elif ver_num(ver) > ver_num(entry["phien_ban"]):
                    push_history(entry)
                    entry.update(rec)
                else:
                    entry.setdefault("lich_su", []).append(rec)
                    entry["lich_su"].sort(key=lambda v: -ver_num(v["phien_ban"]))
                known.add((ma, ver))
                notes.append(f"  + đăng ký source/{cap}/{f.name}")
            for e in data["mau"]:
                for v in versions(e):
                    if not (d / v["file"]).exists():
                        notes.append(f"  ! thiếu file nguồn source/{cap}/{v['file']}")
                    found = [p.name for p in work_dirs(cap, e["ma"], v["phien_ban"]) if (p / f"KichBan_{p.name}.md").exists()]
                    v["output"] = sorted(set(v.get("output", [])) & set(found) | set(found))
            save(cap, data)
    return notes


def cmd_dong_bo(args: list[str]) -> int:
    notes = sync()
    print("\n".join(notes) if notes else "Đồng bộ xong – không có gì mới.")
    return 0


# ---------------------------------------------------------------- hang-doi
def queue(cap_filter: str | None = None) -> list[dict]:
    out = []
    for cap in LEVELS:
        if cap_filter and cap != cap_filter:
            continue
        data = load(cap)
        for e in data["mau"]:
            outs = [p for p in work_dirs(cap, e["ma"], e["phien_ban"]) if valid_output(p)]
            st = e.get("trang_thai", "chua_chay")
            if st != "da_co_output":
                reason = {"chua_chay": "chưa chạy", "dang_chay": "đang chạy dở / chưa đạt kiểm tra", "loi": "lần chạy trước còn lỗi"}.get(st, st)
            elif not outs:
                reason = "ghi đã có output nhưng work/ không có bài hợp lệ"
            else:
                continue
            out.append({"cap": cap, "ma": e["ma"], "mau": e["mau"], "phien_ban": e["phien_ban"],
                        "file": f"source/{cap}/{e['file']}", "ly_do": reason})
    return out


def cmd_hang_doi(args: list[str]) -> int:
    opts, _ = parse_opts(args, ("--cap", "--so"))
    notes = sync()
    if notes:
        print("Đồng bộ nguồn:\n" + "\n".join(notes))
    q = queue(opts.get("--cap"))
    limit = int(opts["--so"]) if opts.get("--so") else None
    shown = q[:limit] if limit else q
    WORK.mkdir(exist_ok=True)
    QUEUE.write_text(json.dumps({"tao_luc": now(), "tong": len(q), "hang_doi": q}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not q:
        print("Hàng đợi trống – mọi mẫu trong source/ đều đã có output hợp lệ.")
        return 0
    print(f"Hàng đợi: {len(q)} mẫu" + (f" (hiện {len(shown)})" if limit and limit < len(q) else "") + " – ghi ở work/_hang_doi.json")
    for i, it in enumerate(shown, 1):
        print(f"  {i:>3}. [{it['cap']}] {it['file']}  – {it['ly_do']}")
    print("Bắt đầu một mẫu: python tools/nguon.py bat-dau <file nguồn>")
    return 0


# ---------------------------------------------------------------- bat-dau
def resolve(arg: str) -> tuple[str, dict, str]:
    """→ (cấp, entry, phiên bản) từ đường dẫn / tên file nguồn / mã mẫu."""
    name = Path(arg).name
    m = SRC_RE.match(name)
    if m:
        cap, ma, ver = m.group(1), f"{m.group(1)}_{m.group(2)}", ver_str(int(m.group(3)))
    else:
        mm = re.match(r"^(N[1-5])_", name)
        if not mm:
            raise SystemExit(f"Không hiểu `{arg}` – đưa đường dẫn file nguồn (source/N2/…_v01.md) hoặc mã mẫu (N2_…).")
        cap, ma, ver = mm.group(1), name, None
    entry = find(load(cap), ma)
    if not entry:
        raise SystemExit(f"Không có mẫu `{ma}` trong source/{cap}/{MANIFEST} – chạy `nguon.py dong-bo` hoặc `nguon.py them`.")
    ver = ver or entry["phien_ban"]
    if not version_rec(entry, ver):
        raise SystemExit(f"Mẫu `{ma}` không có phiên bản {ver}.")
    return cap, entry, ver


def cmd_bat_dau(args: list[str]) -> int:
    if not args:
        print("Cách dùng: python tools/nguon.py bat-dau <source/N2/…_v01.md | mã mẫu>")
        return 2
    sync(quiet=True)
    cap, entry, ver = resolve(args[0])
    ma = entry["ma"]
    with Lock(cap):
        data = load(cap)
        entry = find(data, ma)
        rec = version_rec(entry, ver)
        src = SOURCE / cap / rec["file"]
        if not src.exists():
            raise SystemExit(f"Thiếu file nguồn source/{cap}/{rec['file']}")
        r = 1 + max((int(ID_RE.match(p.name).group(4)) for p in work_dirs(cap, ma, ver)), default=0)
        fid = f"{ma}_{ver}_r{r:02d}"
        folder = WORK / cap / fid
        (folder / "_phu").mkdir(parents=True)
        (folder / "_phu" / f"BaiGoc_{fid}.md").write_text(
            f"Cấp độ: {cap}\n\n" + src.read_text(encoding="utf-8"), encoding="utf-8")
        rec["trang_thai"] = "dang_chay"
        rec["dang_lam"] = fid
        save(cap, data)
    rel = f"work/{cap}/{fid}"
    print(f"ID bài: {fid}")
    print(f"Thư mục: {rel}/  (đã chép bài gốc vào {rel}/_phu/BaiGoc_{fid}.md)")
    if ver != entry["phien_ban"]:
        print(f"Lưu ý: đang chạy phiên bản cũ {ver} (hiện tại là {entry['phien_ban']}).")
    print("AI viết 2 file:")
    print(f"  {rel}/KichBan_{fid}.md")
    print(f"  {rel}/_phu/GhiChu_{fid}.md")
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import pick_cast  # type: ignore
        c = pick_cast.pick(fid)
        mc, sc = c["nhan_vat_chinh"], c["nhan_vat_phu"]
        print(f"Nhân vật gợi ý: {mc['ten']} ({'nữ' if mc['gioi'] == 'nu' else 'nam'}) – {mc['nghe']}; nét: {mc['net']}; "
              f"ngoại hình: {mc['ngoai_hinh']} · phụ: {sc['ten']} ({sc['vai']}) · bối cảnh: {c['noi_chon']}")
        print("  Dùng gợi ý theo rule 02 (Mở bài và kết bài) và rule 06; không chép danh sách ngoại hình/người phụ vào lời mở màn.")
    except Exception as e:  # pragma: no cover
        print(f"(không chạy được pick_cast: {e})")
    print(f"Xong thì chạy: python tools/validate.py {rel}")
    return 0


# ---------------------------------------------------------------- đánh dấu kết quả (validate.py gọi)
def in_work(folder: Path) -> bool:
    folder = folder.resolve()
    return folder.parent.parent == WORK.resolve() and folder.parent.name in LEVELS


def danh_dau(folder: Path, ok: bool) -> str:
    """Ghi kết quả kiểm tra của một bài trong work/ vào source/<cấp>/_quan_ly.json."""
    m = ID_RE.match(folder.name)
    if not m or not in_work(folder):
        return ""
    cap, ma, ver = m.group(1), f"{m.group(1)}_{m.group(2)}", ver_str(int(m.group(3)))
    if not (SOURCE / cap).exists():
        return ""
    with Lock(cap):
        data = load(cap)
        entry = find(data, ma)
        rec = version_rec(entry, ver) if entry else None
        if not rec:
            return f"(chưa có {ma} {ver} trong source/{cap}/{MANIFEST} – chạy `nguon.py dong-bo` nếu cần theo dõi)"
        if ok:
            rec["trang_thai"] = "da_co_output"
            rec["output"] = sorted(set(rec.get("output", [])) | {folder.name})
            rec.pop("dang_lam", None)
            rec["xong_luc"] = now()
        else:
            rec["trang_thai"] = "loi"
            rec["dang_lam"] = folder.name
            rec["loi_luc"] = now()
        save(cap, data)
    return f"Nguồn {ma} {ver}: {STATUS_TEXT[rec['trang_thai']]}"


# ---------------------------------------------------------------- trang-thai
def tong_hop() -> dict:
    res = {}
    for cap in LEVELS:
        if not (SOURCE / cap / MANIFEST).exists():
            continue
        data = load(cap)
        cnt = {k: 0 for k in STATUS_TEXT}
        for e in data["mau"]:
            cnt[e.get("trang_thai", "chua_chay")] = cnt.get(e.get("trang_thai", "chua_chay"), 0) + 1
        res[cap] = {"tong": len(data["mau"]), **cnt}
    return res


def cmd_trang_thai(args: list[str]) -> int:
    opts, _ = parse_opts(args, ("--cap",))
    sync(quiet=True)
    th = tong_hop()
    if not th:
        print("Chưa có nguồn nào trong source/. Nhập bằng: python tools/nguon.py them <file> --cap N2")
        return 0
    print("Cấp  Tổng  Đã có output  Chưa chạy  Đang chạy  Lỗi")
    for cap, c in th.items():
        if opts.get("--cap") and cap != opts["--cap"]:
            continue
        print(f"{cap}   {c['tong']:>4}  {c['da_co_output']:>12}  {c['chua_chay']:>9}  {c['dang_chay']:>9}  {c['loi']:>4}")
    q = queue(opts.get("--cap"))
    print(f"Hàng đợi: {len(q)} mẫu (python tools/nguon.py hang-doi)")
    return 0


# ---------------------------------------------------------------- tiện ích
def parse_opts(args: list[str], keys: tuple) -> tuple[dict, list[str]]:
    opts, rest, i = {}, [], 0
    while i < len(args):
        if args[i] in keys and i + 1 < len(args):
            opts[args[i]] = args[i + 1]
            i += 2
        else:
            rest.append(args[i])
            i += 1
    if "--cap" in opts:
        opts["--cap"] = opts["--cap"].upper()
    return opts, rest


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    cmds = {"them": cmd_them, "dong-bo": cmd_dong_bo, "hang-doi": cmd_hang_doi, "bat-dau": cmd_bat_dau, "trang-thai": cmd_trang_thai}
    if len(argv) < 2 or argv[1] not in cmds:
        print(__doc__)
        return 2
    return cmds[argv[1]](argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
