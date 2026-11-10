#!/usr/bin/env python3
"""
validate.py – Kiểm tra một bài + tự sinh file phụ + cập nhật trang HuongDan.html (định dạng 2.1+).

Cách dùng:
    python tools/validate.py work/<cấp>/<ID>
    python tools/validate.py core/examples/N3_tokoro-ni-he-wo-de
    python tools/validate.py work/<cấp>/<ID> --links     # chỉ in khối link "Mở nhanh"

Mỗi lần chạy: kiểm tra KichBan_<ID>.md + _phu/GhiChu_<ID>.md, rồi sinh _phu/meta_<ID>.json, _phu/TuyChinh_<ID>.txt,
_phu/data.js, dựng lại work/_index.js và ghi trạng thái vào source/<cấp>/_quan_ly.json (xem tools/build_data.py). Tải lại HuongDan.html là thấy bài mới.

Chỉ dùng thư viện chuẩn của Python (3.8+). Thoát với mã 0 nếu ĐẠT, 1 nếu có LỖI, 2 nếu sai cách gọi.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # không tạo __pycache__ trong thư mục dự án

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_data  # noqa: E402  (cùng thư mục tools/)

# ---------------------------------------------------------------- cấu hình quy tắc
H2_FIXED_BEFORE = [
    "## 1. Mở màn: tình huống",
    "## 2. Giới thiệu mẫu ngữ pháp",
    "## 3. Ý nghĩa",
    "## 4. Cấu trúc và cách chia",
]
H2_FIXED_AFTER = [
    "## 6. Bẫy dễ nhầm",
    "## 7. Tổng kết, mẹo nhớ và lưu ý",
]
USAGE_RE = re.compile(r"^## 5\.(\d+) Cách dùng (\d+): (.+)$")
EXAMPLE_RE = re.compile(r"^### Ví dụ (\d+)( \[MỚI\])?$")
LABELS = ["Tình huống", "Câu Việt", "Câu Nhật", "Tô màu", "Cách ghép"]
LABELS_V64 = ["Tình huống", "Câu Việt", "Câu Nhật", "Tô màu", "Tô màu Việt", "Cách ghép"]   # từ 6.4.0
V64_VERSION = (6, 4, 0)
MAX_VI_COLOR_WORDS = 12
MIN_PER_USAGE = 4          # từ 5.3.0: 4–6 ví dụ cho MỖI cách dùng
MAX_PER_USAGE = 6          # được vượt khi cần thêm ví dụ để phủ đủ các dạng cấu trúc của cách dùng đó
NEW_RULE_VERSION = (5, 3, 0)
LEGACY_MIN_TOTAL, LEGACY_MAX_TOTAL = 4, 6  # bài làm theo quy tắc < 5.3.0
MAX_EXAMPLE_WORDS = 130    # Tình huống + Cách ghép của một ví dụ (giữ nhịp nhanh)
MAX_SCREEN_BULLET_WORDS = 20
FORBIDDEN_PHRASES = [
    "tài liệu", "nguồn", "kịch bản", "notebooklm", "hướng dẫn phong cách", "guide",
    "ghi chú biên tập", "TODO", " file ",
]
QUIZ_RE = re.compile(r"đáp án|đố nhanh|câu đố|\bquiz\b|câu hỏi kiểm tra|kiểm tra nhanh", re.I)
WORD_RANGES = {  # số từ tiếng Việt gợi ý cho từng mục (cảnh báo nếu lệch xa)
    "1": (30, 140),
    "2": (5, 80),
    "3": (30, 220),
    "6": (15, 170),
    "7": (30, 220),
}
SUB = build_data.SUB


KANJI_RE = re.compile(r"[㐀-䶿一-鿿豈-﫿々〆ヶ]")
JAPANESE_RE = re.compile(r"[぀-ヿ㐀-䶿一-鿿]")
LATIN_RE = re.compile(r"[A-Za-z]")
# phần cần đọc thành kana: cụm kanji / số / chữ Latin (vd 日本, ３億円, NHK)
MARKUP_RE = re.compile(r"[《》｜【】]")
OLD_PAREN_RE = re.compile(r"[㐀-䶿一-鿿豈-﫿々〆ヶ]（[ぁ-ゖーゝゞ]+）")

class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, where: str, msg: str) -> None:
        self.errors.append(f"LỖI      [{where}] {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"CẢNH BÁO [{where}] {msg}")


def vi_words(text: str) -> int:
    """Đếm từ tiếng Việt (bỏ chữ Nhật và ký hiệu markdown)."""
    text = re.sub(r"[぀-ヿ㐀-鿿（）「」。、！？【】]+", " ", text)
    text = re.sub(r"[*#|`>\-]+", " ", text)
    return len([w for w in text.split() if re.search(r"\w", w)])


def read(path: Path, rep: Report) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        rep.err(path.name, "File không phải UTF-8")
        return path.read_text(encoding="utf-8", errors="replace")


def check_placeholders(name: str, text: str, rep: Report) -> None:
    for i, line in enumerate(text.splitlines(), 1):
        if "{{" in line or "}}" in line:
            rep.err(f"{name}:{i}", f"Còn placeholder chưa điền: {line.strip()[:80]}")


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s)


# ---------------------------------------------------------------- kiểm tra Kịch bản
def check_common_lines(name: str, lines: list[str], rep: Report) -> None:
    """Cấm quiz, từ cấm, ký hiệu cũ, gạch đầu dòng trước câu – dùng cho mọi phiên bản Kịch bản."""
    for i, line in enumerate(lines, 1):
        if MARKUP_RE.search(line):
            rep.err(f"{name}:{i}", "Không dùng ký hiệu 《 》 ｜ 【 】 trong Kịch bản (NotebookLM hiện nguyên lên màn hình) – "
                    "không ghi cách đọc; mẫu cần tô màu để ở dòng `**Tô màu:**`")
        if OLD_PAREN_RE.search(line):
            rep.err(f"{name}:{i}", "Không ghi cách đọc trong ngoặc sau kanji (NotebookLM hiện nguyên lên màn hình)")
        if line.startswith("**Cách đọc:**"):
            rep.err(f"{name}:{i}", "Bỏ dòng `**Cách đọc:**` – từ bản 5.0 không ghi cách đọc hiragana")
        if re.match(r"^\s*([-*+]|\d+\.)\s+(\*\*)?(Nhật|Việt|Câu Nhật|Câu Việt)(:\*\*|\s*:)", line):
            rep.err(f"{name}:{i}", "Không gạch đầu dòng trước câu Nhật/Việt – viết `**Nhật:** …` ở đầu dòng")
    for i, line in enumerate(lines, 1):
        if QUIZ_RE.search(line):
            rep.err(f"{name}:{i}", "Không được có câu đố / quiz / đáp án trong bài giảng")
        low = line.lower()
        for ph in FORBIDDEN_PHRASES:
            if (ph.lower() in low) if ph != "TODO" else (ph in line):
                rep.err(f"{name}:{i}", f"Có cụm bị cấm `{ph.strip()}` (người xem sẽ nghe thấy)")
        if re.search(r"\bAI\b", line):
            rep.err(f"{name}:{i}", "Có từ `AI` – không nhắc đến AI trong Kịch bản")
        if re.search(r"\b(GHI CHÚ|Ghi chú)\b", line):
            rep.err(f"{name}:{i}", "Ghi chú biên tập phải nằm ở _phu/GhiChu_<ID>.md, không ở Kịch bản")


def check_kichban(path: Path, text: str, rep: Report) -> dict:
    name = path.name
    lines = text.splitlines()
    stats = {"examples": 0, "new": 0, "usages": [], "title": "", "ex": [], "n_struct": 0}

    check_placeholders(name, text, rep)

    if not lines or not lines[0].startswith("# "):
        rep.err(f"{name}:1", "Dòng đầu phải là tiêu đề `# <mẫu> – <nghĩa>`")
    else:
        stats["title"] = lines[0][2:].strip()
        if " – " not in stats["title"]:
            rep.warn(f"{name}:1", "Tiêu đề nên có dạng `<mẫu> – <nghĩa>` (gạch ngang dài –)")

    # --- tách các mục H2
    sections: list[tuple[str, int, list[tuple[int, str]]]] = []
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            sections.append((line.rstrip(), i, []))
        elif line.startswith("# ") and i != 1:
            rep.err(f"{name}:{i}", "Chỉ được có 1 tiêu đề cấp 1 (#)")
        elif sections:
            sections[-1][2].append((i, line))

    heads = [s[0] for s in sections]
    usage_secs = [s for s in sections if USAGE_RE.match(s[0])]
    expected_order = H2_FIXED_BEFORE + ["<5.x>"] * len(usage_secs) + H2_FIXED_AFTER
    actual_order = ["<5.x>" if USAGE_RE.match(h) else h for h in heads]

    n_err = len(rep.errors)
    for h in H2_FIXED_BEFORE + H2_FIXED_AFTER:
        if h not in heads:
            rep.err(name, f"Thiếu tiêu đề bắt buộc: `{h}`")
    if not usage_secs:
        rep.err(name, "Không có mục cách dùng nào (`## 5.1 Cách dùng 1: …`)")
    for h, ln, _ in sections:
        if h not in H2_FIXED_BEFORE + H2_FIXED_AFTER and not USAGE_RE.match(h):
            rep.err(f"{name}:{ln}", f"Tiêu đề lạ, không có trong template: `{h}`")
    if len(rep.errors) == n_err and actual_order != expected_order:
        rep.err(name, "Thứ tự các mục sai. Đúng: 1 → 2 → 3 → 4 → 5.x… → 6 → 7")

    sec_by_head = {h: (ln, body) for h, ln, body in sections}

    def body_lines(head: str) -> list[tuple[int, str]]:
        return sec_by_head.get(head, (0, []))[1]

    def body_text(head: str) -> str:
        return "\n".join(l for _, l in body_lines(head))

    def block_after(head: str, label: str) -> list[tuple[int, str]]:
        """Các dòng gạch đầu dòng ngay sau nhãn `**label:**` trong một mục."""
        out, on = [], False
        for i, l in body_lines(head):
            if l.startswith(f"**{label}:**"):
                on = True
                continue
            if on:
                if l.startswith("- "):
                    out.append((i, l[2:].strip()))
                elif l.strip() == "" and not out:
                    continue
                else:
                    break
        return out

    def labelled(lines_: list[tuple[int, str]]) -> list[tuple[int, str, str]]:
        out = []
        for i, l in lines_:
            mm = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", l)
            out.append((i, mm.group(1), mm.group(2).strip()) if mm else (i, "", l.strip()))
        return out

    def check_nvb_block(where: str, rest: list[tuple[int, str]], need_color: bool, what: str) -> None:
        """Khối câu Nhật trên màn hình: Nhật / (Tô màu) / Việt."""
        want = ["Nhật"] + (["Tô màu"] if need_color else []) + ["Việt"]
        got = labelled(rest)
        if [g[1] for g in got] != want:
            rep.err(where, f"{what}: phải là đúng các dòng " + " → ".join(f"`**{w}:**`" for w in want)
                    + " (không gạch đầu dòng, không dòng thừa)")
            return
        v = {g[1]: (g[0], g[2]) for g in got}
        if need_color and v["Tô màu"][1] and v["Tô màu"][1] not in v["Nhật"][1]:
            rep.err(f"{name}:{v['Tô màu'][0]}", "Tô màu phải chép đúng y một đoạn có trong dòng Nhật")
        if JAPANESE_RE.search(v["Việt"][1]):
            rep.err(f"{name}:{v['Việt'][0]}", "Dòng Việt không được chứa chữ Nhật")

    # --- độ dài các mục + tổng
    for key, (lo, hi) in WORD_RANGES.items():
        head = next((h for h in heads if h.startswith(f"## {key}.")), None)
        if head:
            n = vi_words(body_text(head))
            if n < lo or n > hi:
                rep.warn(name, f"Mục {key} có ~{n} từ (gợi ý {lo}–{hi})")

    # --- mục 1
    if "?" not in body_text("## 1. Mở màn: tình huống"):
        rep.warn(name, "Mục 1 nên kết bằng một câu hỏi dẫn vào bài")

    # --- mục 2
    h2 = "## 2. Giới thiệu mẫu ngữ pháp"
    lab2 = {}
    for i, lab, val in labelled(body_lines(h2)):
        if lab in ("Mẫu", "Nghĩa"):
            lab2[lab] = (i, val)
    for lab in ("Mẫu", "Nghĩa"):
        if not lab2.get(lab, (0, ""))[1]:
            rep.err(name, f"Mục 2 cần dòng `**{lab}:** …` (chữ hiện trên màn hình, không gạch đầu dòng)")
    if "**Trên màn hình:**" in body_text(h2):
        rep.err(name, "Mục 2 dùng các dòng `**Mẫu:**` / `**Nghĩa:**` thay cho `**Trên màn hình:**` + gạch đầu dòng")
    if "**Lời giảng:**" not in body_text(h2):
        rep.err(name, "Mục 2 thiếu `**Lời giảng:**`")

    # --- mục 3
    h3 = "## 3. Ý nghĩa"
    scr3 = block_after(h3, "Trên màn hình")
    if not 2 <= len(scr3) <= 5:
        rep.err(name, f"Mục 3 cần `**Trên màn hình:**` với 2–5 ý gạch đầu dòng (đang có {len(scr3)})")
    for i, s in scr3:
        if vi_words(s) > MAX_SCREEN_BULLET_WORDS:
            rep.warn(f"{name}:{i}", f"Ý trên màn hình dài {vi_words(s)} từ (nên ≤ {MAX_SCREEN_BULLET_WORDS})")
    for lab in ("**Lời giảng:**", "**Chìa khóa:**"):
        if lab not in body_text(h3):
            rep.err(name, f"Mục 3 thiếu `{lab}`")

    # --- mục 4
    h4 = "## 4. Cấu trúc và cách chia"
    blocks4: list[tuple[int, int, str, list[tuple[int, str]]]] = []
    for i, l in body_lines(h4):
        bm = re.match(r"^\*\*Cấu trúc (\d+):\*\*\s*(.*)$", l)
        if bm:
            blocks4.append((i, int(bm.group(1)), bm.group(2).strip(), []))
        elif blocks4 and l.strip():
            blocks4[-1][3].append((i, l))
        elif l.strip():
            rep.err(f"{name}:{i}", "Mục 4 chỉ gồm các khối `**Cấu trúc <n>:** …` + `**Giải thích:** …` (không bảng, không gạch đầu dòng)")
    stats["n_struct"] = len(blocks4)
    if not blocks4:
        rep.err(name, "Mục 4 cần ít nhất 1 khối `**Cấu trúc 1:** <dòng cấu trúc như bài gốc>` + `**Giải thích:** …`")
    for k, (i, n, val, rest) in enumerate(blocks4, 1):
        if n != k:
            rep.err(f"{name}:{i}", f"Cấu trúc đánh số sai: là {n}, phải là {k}")
        if not val:
            rep.err(f"{name}:{i}", "Dòng Cấu trúc đang trống")
        got = labelled(rest)
        if [g[1] for g in got] != ["Giải thích"]:
            rep.err(f"{name}:{i}", "Sau dòng Cấu trúc phải là đúng 1 dòng `**Giải thích:** …`")
            continue
        v = {g[1]: (g[0], g[2]) for g in got}
        if vi_words(v["Giải thích"][1]) < 8:
            rep.warn(f"{name}:{v['Giải thích'][0]}", "Giải thích cấu trúc quá ngắn – nói đủ: gắn thế nào (chia dạng gì) + nghĩa/sắc thái")

    # --- mục 5.x
    for idx, (head, ln, body) in enumerate(usage_secs, 1):
        m = USAGE_RE.match(head)
        if int(m.group(1)) != idx or int(m.group(2)) != idx:
            rep.err(f"{name}:{ln}", f"Số thứ tự cách dùng phải là `5.{idx} Cách dùng {idx}`")
        stats["usages"].append(m.group(3).strip())
        nonblank = [(i, l) for i, l in body if l.strip()]
        if not nonblank or not nonblank[0][1].startswith("**Dấu hiệu nhận biết:**"):
            rep.err(f"{name}:{ln}", "Dòng đầu của mỗi cách dùng phải là `**Dấu hiệu nhận biết:** …`")

        examples: list[tuple[int, str, list[tuple[int, str]]]] = []
        for i, l in nonblank:
            if l.startswith("### "):
                examples.append((i, l.rstrip(), []))
            elif examples:
                examples[-1][2].append((i, l))
        if not examples:
            rep.err(f"{name}:{ln}", f"Cách dùng {idx} chưa có ví dụ nào (mỗi cách dùng ít nhất 1)")
        seen_new = False
        for eln, ehead, elines in examples:
            k = stats["examples"] + 1  # đánh số liên tục cả bài
            em = EXAMPLE_RE.match(ehead)
            where = f"{name}:{eln}"
            if not em:
                rep.err(where, f"Tiêu đề ví dụ sai định dạng: `{ehead}` (đúng: `### Ví dụ {k}` hoặc `### Ví dụ {k} [MỚI]`)")
                stats["examples"] += 1
                continue
            if int(em.group(1)) != k:
                rep.err(where, f"Ví dụ đánh số sai: là {em.group(1)}, phải là {k} (đánh số liên tục 1, 2, 3… cả bài)")
            if em.group(2):
                seen_new = True
                stats["new"] += 1
            else:
                if seen_new:
                    rep.warn(where, "Ví dụ [MỚI] nên đặt cuối mỗi cách dùng")
            stats["examples"] += 1

            got = []
            for li, l in elines:
                mm = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", l)
                if mm:
                    got.append((li, mm.group(1), mm.group(2).strip()))
                else:
                    rep.warn(f"{name}:{li}", "Dòng thừa trong ví dụ (không thuộc các nhãn quy định)")
            labels = [g[1] for g in got]
            if labels != LABELS:
                rep.err(where, f"Ví dụ phải có đúng {len(LABELS)} nhãn theo thứ tự {LABELS}, đang có {labels}")
                continue
            vals = {g[1]: (g[0], g[2]) for g in got}
            for lab in LABELS:
                if not vals[lab][1]:
                    rep.err(f"{name}:{vals[lab][0]}", f"Nhãn `{lab}` đang trống")

            vi_ln, vi = vals["Câu Việt"]
            if JAPANESE_RE.search(vi):
                rep.err(f"{name}:{vi_ln}", "Câu Việt không được chứa chữ Nhật – câu Nhật để ở dòng riêng")
            jp_ln, jp = vals["Câu Nhật"]
            co_ln, co = vals["Tô màu"]
            if not JAPANESE_RE.search(jp):
                rep.err(f"{name}:{jp_ln}", "Câu Nhật không có chữ Nhật")
            if LATIN_RE.search(jp):
                rep.warn(f"{name}:{jp_ln}", "Câu Nhật có chữ Latin (romaji?)")
            if co and co not in jp:
                rep.err(f"{name}:{co_ln}", "Tô màu phải chép đúng y phần mẫu ngữ pháp có trong Câu Nhật")
            gh_ln, gh = vals["Cách ghép"]
            if jp and not gh.startswith(f"「{jp}」"):
                rep.err(f"{name}:{gh_ln}", "Cách ghép phải mở đầu bằng 「<Câu Nhật>」 chép y nguyên (để video đọc trọn câu trước khi giảng)")
            n_words = vi_words(vals["Tình huống"][1]) + vi_words(gh)
            if n_words > MAX_EXAMPLE_WORDS:
                rep.warn(where, f"Ví dụ dài ~{n_words} từ (Tình huống + Cách ghép, nên ≤ {MAX_EXAMPLE_WORDS}) – bài nhiều ví dụ cần nhịp gọn")
            stats["ex"].append({"n": k, "usage": idx, "new": bool(em.group(2)), "ghep": gh, "ghep_ln": gh_ln})

    # (số ví dụ + phủ cấu trúc: kiểm ở check_counts – cần Bảng phủ trong Ghi chú biên tập)

    # --- mục 6
    h6 = "## 6. Bẫy dễ nhầm"
    traps: list[tuple[int, int, list[tuple[int, str]]]] = []
    for i, l in body_lines(h6):
        tm = re.match(r"^\*\*Bẫy (\d+) – .+?:\*\*", l)
        if tm:
            traps.append((i, int(tm.group(1)), []))
        elif traps and l.strip():
            traps[-1][2].append((i, l))
        elif l.strip():
            rep.err(f"{name}:{i}", "Mục 6: mỗi bẫy bắt đầu bằng `**Bẫy <n> – <tên>:** …`")
    if not traps:
        rep.err(name, "Mục 6 cần ít nhất 1 bẫy dạng `**Bẫy 1 – <tên>:** …` + `**Nhật:**` + `**Việt:**`")
    for k, (i, n, rest) in enumerate(traps, 1):
        if n != k:
            rep.err(f"{name}:{i}", f"Bẫy đánh số sai: là {n}, phải là {k}")
        check_nvb_block(f"{name}:{i}", rest, False, "Bẫy")

    # --- mục 7
    h7 = "## 7. Tổng kết, mẹo nhớ và lưu ý"
    sec7 = body_text(h7)
    for lab in ["**Tóm lại:**", "**Mẹo nhớ:**", "**Lưu ý:**", "**Kết:**"]:
        if lab not in sec7:
            rep.err(name, f"Mục 7 thiếu `{lab}`")
    k_lines = body_lines(h7)
    k_idx = next((n for n, (_, l) in enumerate(k_lines) if l.startswith("**Kết:**")), None)
    if k_idx is not None:
        rest = [(i, l) for i, l in k_lines[k_idx + 1:] if l.strip()]
        check_nvb_block(f"{name}:{k_lines[k_idx][0]}", rest, True, "Phần Kết")

    check_common_lines(name, lines, rep)
    return stats


# ================================================================ Kịch bản định dạng 6.1 (chương theo từng cách dùng)
V6_VERSION = (6, 1, 0)   # khung chương: 1 Mở màn · 2 Giới thiệu & mô tả · 3.x chương · 4 Bẫy · 5 Tổng kết
CH = "3"                 # số mục của các chương cách dùng / cách nói thường gặp
V6_HEAD_BEFORE = [
    "## 1. Mở màn: tình huống",
    "## 2. Giới thiệu mẫu ngữ pháp",
]
V6_HEAD_AFTER = [
    "## 4. Bẫy dễ nhầm",
    "## 5. Tổng kết, mẹo nhớ và lưu ý",
]
V6_USAGE_RE = re.compile(r"^## 3\.(\d+) Cách dùng(?: (\d+))?: (.+)$")   # 1 cách dùng: không số (từ 6.4)
V6_PHRASE_RE = re.compile(r"^## 3\.(\d+) Cách nói thường gặp: (.+)$")
V6_MEANING_HEAD = "### Ý nghĩa và cách dùng"
V6_CHIA_HEAD = "### Cách chia"
# nhãn của phần Ý nghĩa: (tên, bắt buộc)
V6_MEANING_LABELS = [
    ("Trên màn hình", True), ("Bản chất", True), ("So với tiếng Việt", True), ("Câu mẫu", True),
    ("Khi nào dùng", True), ("Không dùng khi", False), ("Sắc thái", False), ("Dấu hiệu nhận biết", True),
]
V6_MEANING_NARR = ["Bản chất", "So với tiếng Việt", "Khi nào dùng", "Không dùng khi", "Sắc thái"]
V6_MEANING_MIN_ERR, V6_MEANING_MIN_WARN = 60, 100   # số từ lời giảng tối thiểu của phần Ý nghĩa (không có trần)
V6_PHRASE_MIN, V6_PHRASE_MAX = 1, 3
V6_SUMMARY_LABELS = ["Tóm lại", "Mẹo nhớ", "Lưu ý", "Tình huống thực tế", "Người Nhật thường nói", "Kết"]
V6_SUMMARY_OPTIONAL = {"Tình huống thực tế", "Người Nhật thường nói"}


def _labelled(lines_: list[tuple[int, str]]) -> list[tuple[int, str, str]]:
    out = []
    for i, l in lines_:
        mm = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", l)
        out.append((i, mm.group(1), mm.group(2).strip()) if mm else (i, "", l.strip()))
    return out


def _check_nvb(name: str, where: str, rest: list[tuple[int, str]], want: list[str], rep: Report, what: str) -> dict:
    """Khối câu Nhật trên màn hình: các nhãn đúng thứ tự `want` (vd Nhật / Tô màu / Việt)."""
    got = _labelled([(i, l) for i, l in rest if l.strip()])
    if [g[1] for g in got] != want:
        rep.err(where, f"{what}: phải là đúng các dòng " + " → ".join(f"`**{w}:**`" for w in want)
                + " (không gạch đầu dòng, không dòng thừa)")
        return {}
    v = {g[1]: (g[0], g[2]) for g in got}
    for w in want:
        if not v[w][1]:
            rep.err(f"{name}:{v[w][0]}", f"{what}: dòng `{w}` đang trống")
    if "Tô màu" in v and v["Tô màu"][1] and v["Tô màu"][1] not in v["Nhật"][1]:
        rep.err(f"{name}:{v['Tô màu'][0]}", "Tô màu phải chép đúng y một đoạn có trong dòng Nhật")
    if "Tô màu Việt" in v and v["Tô màu Việt"][1] and v["Tô màu Việt"][1] not in v.get("Việt", (0, ""))[1]:
        rep.err(f"{name}:{v['Tô màu Việt'][0]}", "Tô màu Việt phải chép đúng y một đoạn có trong dòng Việt")
    if "Nhật" in v and not JAPANESE_RE.search(v["Nhật"][1]):
        rep.err(f"{name}:{v['Nhật'][0]}", f"{what}: dòng Nhật không có chữ Nhật")
    if "Việt" in v and JAPANESE_RE.search(v["Việt"][1]):
        rep.err(f"{name}:{v['Việt'][0]}", f"{what}: dòng Việt không được chứa chữ Nhật")
    return v


def _check_example(name: str, ehead: str, eln: int, elines: list[tuple[int, str]], k: int, sec_idx: int,
                   kind: str, rep: Report, stats: dict, need_vi: bool = False) -> None:
    em = EXAMPLE_RE.match(ehead)
    where = f"{name}:{eln}"
    if not em:
        rep.err(where, f"Tiêu đề ví dụ sai định dạng: `{ehead}` (đúng: `### Ví dụ {k}` hoặc `### Ví dụ {k} [MỚI]`)")
        return
    if int(em.group(1)) != k:
        rep.err(where, f"Ví dụ đánh số sai: là {em.group(1)}, phải là {k} (đánh số liên tục 1, 2, 3… cả bài)")
    got = []
    for li, l in elines:
        mm = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", l)
        if mm:
            got.append((li, mm.group(1), mm.group(2).strip()))
        else:
            rep.warn(f"{name}:{li}", "Dòng thừa trong ví dụ (không thuộc các nhãn quy định)")
    allowed = [LABELS_V64] if need_vi else [LABELS, LABELS_V64]
    labs = [g[1] for g in got]
    if labs not in allowed:
        rep.err(where, f"Ví dụ phải có đúng {len(allowed[0])} nhãn theo thứ tự {allowed[0]}, đang có {labs}")
        stats["ex"].append({"n": k, "sec": sec_idx, "kind": kind, "new": bool(em.group(2)), "ghep": "", "ghep_ln": eln})
        return
    vals = {g[1]: (g[0], g[2]) for g in got}
    for lab in labs:
        if not vals[lab][1]:
            rep.err(f"{name}:{vals[lab][0]}", f"Nhãn `{lab}` đang trống")
    vi_ln, vi = vals["Câu Việt"]
    if JAPANESE_RE.search(vi):
        rep.err(f"{name}:{vi_ln}", "Câu Việt không được chứa chữ Nhật – câu Nhật để ở dòng riêng")
    jp_ln, jp = vals["Câu Nhật"]
    co_ln, co = vals["Tô màu"]
    if not JAPANESE_RE.search(jp):
        rep.err(f"{name}:{jp_ln}", "Câu Nhật không có chữ Nhật")
    if LATIN_RE.search(jp):
        rep.warn(f"{name}:{jp_ln}", "Câu Nhật có chữ Latin (romaji?)")
    if co and co not in jp:
        rep.err(f"{name}:{co_ln}", "Tô màu phải chép đúng y phần mẫu ngữ pháp có trong Câu Nhật")
    if "Tô màu Việt" in vals:
        cv_ln, cv = vals["Tô màu Việt"]
        if cv and cv not in vi:
            rep.err(f"{name}:{cv_ln}", "Tô màu Việt phải chép đúng y cụm nghĩa tương ứng có trong Câu Việt")
        if JAPANESE_RE.search(cv):
            rep.err(f"{name}:{cv_ln}", "Tô màu Việt chỉ chứa chữ Việt")
        if vi_words(cv) > MAX_VI_COLOR_WORDS:
            rep.warn(f"{name}:{cv_ln}", f"Tô màu Việt dài {vi_words(cv)} từ – chỉ tô cụm nghĩa ứng với mẫu (nên ≤ {MAX_VI_COLOR_WORDS})")
    gh_ln, gh = vals["Cách ghép"]
    if jp and not gh.startswith(f"「{jp}」"):
        rep.err(f"{name}:{gh_ln}", "Cách ghép phải mở đầu bằng 「<Câu Nhật>」 chép y nguyên (để video đọc trọn câu trước khi giảng)")
    n_words = vi_words(vals["Tình huống"][1]) + vi_words(gh)
    if n_words > MAX_EXAMPLE_WORDS:
        rep.warn(where, f"Ví dụ dài ~{n_words} từ (Tình huống + Cách ghép, nên ≤ {MAX_EXAMPLE_WORDS}) – giữ lời văn gọn")
    stats["ex"].append({"n": k, "sec": sec_idx, "kind": kind, "new": bool(em.group(2)), "ghep": gh, "ghep_ln": gh_ln})


def check_kichban_v6(path: Path, text: str, rep: Report, ver: tuple = V6_VERSION) -> dict:
    """Kịch bản 6.1: 1 Mở màn · 2 Giới thiệu & mô tả mẫu · 3.x chương cách dùng (Ý nghĩa → Cách chia → Ví dụ)
    · 3.x Cách nói thường gặp (tùy chọn) · 4 Bẫy · 5 Tổng kết."""
    name = path.name
    lines = text.splitlines()
    need_vi = ver >= V64_VERSION
    stats = {"examples": 0, "new": 0, "usages": [], "phrases": [], "title": "", "ex": [],
             "n_struct": 0, "struct_sec": {}, "sections": []}
    check_placeholders(name, text, rep)
    if not lines or not lines[0].startswith("# "):
        rep.err(f"{name}:1", "Dòng đầu phải là tiêu đề `# <mẫu> – <nghĩa>`")
    else:
        stats["title"] = lines[0][2:].strip()
        if " – " not in stats["title"]:
            rep.warn(f"{name}:1", "Tiêu đề nên có dạng `<mẫu> – <nghĩa>` (gạch ngang dài –)")

    sections: list[tuple[str, int, list[tuple[int, str]]]] = []
    for i, line in enumerate(lines, 1):
        if line.startswith("## "):
            sections.append((line.rstrip(), i, []))
        elif line.startswith("# ") and i != 1:
            rep.err(f"{name}:{i}", "Chỉ được có 1 tiêu đề cấp 1 (#)")
        elif sections:
            sections[-1][2].append((i, line))
    heads = [s_[0] for s_ in sections]
    ch_secs = [s_ for s_ in sections if V6_USAGE_RE.match(s_[0]) or V6_PHRASE_RE.match(s_[0])]

    n_err = len(rep.errors)
    for h in V6_HEAD_BEFORE + V6_HEAD_AFTER:
        if h not in heads:
            rep.err(name, f"Thiếu tiêu đề bắt buộc: `{h}`")
    if not any(V6_USAGE_RE.match(h) for h in heads):
        rep.err(name, "Không có chương cách dùng nào (`## 3.1 Cách dùng 1: …`)")
    for h, ln, _ in sections:
        if h not in V6_HEAD_BEFORE + V6_HEAD_AFTER and not (V6_USAGE_RE.match(h) or V6_PHRASE_RE.match(h)):
            rep.err(f"{name}:{ln}", f"Tiêu đề lạ, không có trong template: `{h}`"
                    + (" – khung 6.1 bỏ mục Tổng quan, gộp vào mục 2" if "Tổng quan" in h else ""))
    actual = ["<3.x>" if (V6_USAGE_RE.match(h) or V6_PHRASE_RE.match(h)) else h for h in heads]
    if len(rep.errors) == n_err and actual != V6_HEAD_BEFORE + ["<3.x>"] * len(ch_secs) + V6_HEAD_AFTER:
        rep.err(name, "Thứ tự các mục sai. Đúng: 1 → 2 → 3.1, 3.2… → 4 → 5")

    sec_by_head = {h: (ln, body) for h, ln, body in sections}

    def body_lines(head: str) -> list[tuple[int, str]]:
        return sec_by_head.get(head, (0, []))[1]

    def body_text(head: str) -> str:
        return "\n".join(l for _, l in body_lines(head))

    def bullets_after(lines_: list[tuple[int, str]], label: str) -> list[tuple[int, str]]:
        out, on = [], False
        for i, l in lines_:
            if l.startswith(f"**{label}:**"):
                on = True
                continue
            if on:
                if l.startswith("- "):
                    out.append((i, l[2:].strip()))
                elif l.strip() == "" and not out:
                    continue
                else:
                    break
        return out

    # --- độ dài (chỉ sàn cho phần quan trọng; trần nhẹ cho mở màn để vào bài nhanh)
    for key, lo, hi in (("1", 30, 160), ("2", 40, None), ("4", 15, None), ("5", 30, None)):
        head = next((h for h in heads if h.startswith(f"## {key}.")), None)
        if head:
            n = vi_words(body_text(head))
            if n < lo or (hi and n > hi):
                rep.warn(name, f"Mục {key} có ~{n} từ (gợi ý {lo}–{hi or '∞'})")
    if "?" not in body_text("## 1. Mở màn: tình huống"):
        rep.warn(name, "Mục 1 nên kết bằng một câu hỏi dẫn vào bài")

    # --- mục 2
    h2 = "## 2. Giới thiệu mẫu ngữ pháp"
    got2 = [(i, lab, val) for i, lab, val in _labelled([(i, l) for i, l in body_lines(h2) if l.strip()]) if lab]
    order2 = [g[1] for g in got2]
    want2 = ["Mẫu", "Nghĩa", "Mô tả", "Lời giảng"] + (["Chìa khóa"] if "Chìa khóa" in order2 else [])
    if order2 != want2:
        rep.err(name, "Mục 2 (giới thiệu & mô tả mẫu): các nhãn theo thứ tự `Mẫu` → `Nghĩa` → `Mô tả` (+ 2–4 ý gạch đầu dòng) "
                f"→ `Lời giảng` → `Chìa khóa` (tùy chọn); đang có {order2}")
    v2 = {lab: (i, val) for i, lab, val in got2}
    for lab in ("Mẫu", "Nghĩa", "Lời giảng"):
        if lab in v2 and not v2[lab][1]:
            rep.err(f"{name}:{v2[lab][0]}", f"Mục 2: dòng `{lab}` đang trống")
    desc = bullets_after(body_lines(h2), "Mô tả")
    if not 2 <= len(desc) <= 4:
        rep.err(name, f"Mục 2 cần `**Mô tả:**` với 2–4 ý gạch đầu dòng hiện trên màn hình (đang có {len(desc)})")
    for i, s_ in desc:
        if vi_words(s_) > MAX_SCREEN_BULLET_WORDS:
            rep.warn(f"{name}:{i}", f"Ý mô tả dài {vi_words(s_)} từ (nên ≤ {MAX_SCREEN_BULLET_WORDS})")
        if re.match(r"^(Cách dùng|Phần|Mục|Chương)\s*\d", s_):
            rep.err(f"{name}:{i}", "Mô tả không liệt kê các phần/cách dùng của bài (video sẽ dựng thành khung mục lục) – mô tả chính mẫu ngữ pháp")
    if "Lời giảng" in v2 and vi_words(v2["Lời giảng"][1]) < 30:
        rep.warn(f"{name}:{v2['Lời giảng'][0]}", "Lời giảng mục 2 ngắn – dẫn từ tình huống, gọi tên mẫu, nói nghĩa và mô tả")

    # --- chương 3.x
    k_ex = 0
    usage_no = 0
    seen_phrase = False
    for idx, (head, ln, body) in enumerate(ch_secs, 1):
        mu, mp = V6_USAGE_RE.match(head), V6_PHRASE_RE.match(head)
        if int((mu or mp).group(1)) != idx:
            rep.err(f"{name}:{ln}", f"Số thứ tự chương phải là `{CH}.{idx}`")
        stats["sections"].append({"idx": idx, "kind": "usage" if mu else "phrase",
                                  "title": (mu.group(3) if mu else mp.group(2)).strip(), "cards": 0, "same": 0})
        # tách khối H3
        blocks: list[tuple[str, int, list[tuple[int, str]]]] = [("", ln, [])]
        for i, l in body:
            if l.startswith("### "):
                blocks.append((l.rstrip(), i, []))
            else:
                blocks[-1][2].append((i, l))
        pre = [(i, l) for i, l in blocks[0][2] if l.strip()]
        h3s = blocks[1:]
        if mu:
            if seen_phrase:
                rep.err(f"{name}:{ln}", "Chương `Cách nói thường gặp` phải đặt sau tất cả các chương Cách dùng")
            usage_no += 1
            n_usage_total = sum(1 for h in heads if V6_USAGE_RE.match(h))
            if mu.group(2) is None:
                if n_usage_total > 1:
                    rep.err(f"{name}:{ln}", f"Bài có {n_usage_total} cách dùng – phải đánh số: `Cách dùng {usage_no}: …`")
            elif n_usage_total == 1 and need_vi:
                rep.err(f"{name}:{ln}", "Bài chỉ có 1 cách dùng – viết `## 3.1 Cách dùng: <tên>`, KHÔNG đánh số (tránh người học tưởng còn cách dùng 2)")
            elif int(mu.group(2)) != usage_no:
                rep.err(f"{name}:{ln}", f"Đánh số cách dùng sai: phải là `Cách dùng {usage_no}`")
            stats["usages"].append(mu.group(3).strip())
            if pre:
                rep.err(f"{name}:{pre[0][0]}", "Ngay sau tiêu đề cách dùng phải là `### Ý nghĩa và cách dùng`")
            names_ = [b[0] for b in h3s]
            if len(names_) < 3 or names_[0] != V6_MEANING_HEAD or names_[1] != V6_CHIA_HEAD:
                rep.err(f"{name}:{ln}", "Mỗi cách dùng gồm đúng thứ tự: `### Ý nghĩa và cách dùng` → `### Cách chia` → `### Ví dụ …`")
            # Ý nghĩa
            mb = next((b for b in h3s if b[0] == V6_MEANING_HEAD), None)
            if mb:
                got = [(i, lab, val) for i, lab, val in _labelled(mb[2]) if lab]
                order = [g[1] for g in got if g[1] in dict(V6_MEANING_LABELS)]
                want = [lab for lab, _ in V6_MEANING_LABELS if lab in order or dict(V6_MEANING_LABELS)[lab]]
                if order != want:
                    rep.err(f"{name}:{mb[1]}", "Ý nghĩa và cách dùng: cần các nhãn theo thứ tự "
                            + " → ".join(f"`{lab}`{'' if req else ' (tùy chọn)'}" for lab, req in V6_MEANING_LABELS)
                            + f"; đang có {order}")
                scr = bullets_after(mb[2], "Trên màn hình")
                if not 2 <= len(scr) <= 5:
                    rep.err(f"{name}:{mb[1]}", f"Ý nghĩa: `**Trên màn hình:**` cần 2–5 ý gạch đầu dòng (đang có {len(scr)})")
                for i, s_ in scr:
                    if vi_words(s_) > MAX_SCREEN_BULLET_WORDS:
                        rep.warn(f"{name}:{i}", f"Ý trên màn hình dài {vi_words(s_)} từ (nên ≤ {MAX_SCREEN_BULLET_WORDS})")
                narr = sum(vi_words(val) for _, lab, val in got if lab in V6_MEANING_NARR)
                if narr < V6_MEANING_MIN_ERR:
                    rep.err(f"{name}:{mb[1]}", f"Phần Ý nghĩa quá ngắn (~{narr} từ, tối thiểu {V6_MEANING_MIN_ERR}) – giảng kỹ bản chất, so với tiếng Việt, khi nào dùng")
                elif narr < V6_MEANING_MIN_WARN:
                    rep.warn(f"{name}:{mb[1]}", f"Phần Ý nghĩa hơi ngắn (~{narr} từ, nên ≥ {V6_MEANING_MIN_WARN})")
                for _, lab, val in got:
                    if lab in ("Bản chất", "So với tiếng Việt", "Khi nào dùng", "Dấu hiệu nhận biết") and not val:
                        rep.err(f"{name}:{mb[1]}", f"Ý nghĩa: nhãn `{lab}` đang trống")
                # Câu mẫu → Nhật / Tô màu / Việt ngay sau
                lines_m = [(i, l) for i, l in mb[2] if l.strip()]
                cm = next((n for n, (_, l) in enumerate(lines_m) if l.startswith("**Câu mẫu:**")), None)
                if cm is not None:
                    has_vi = cm + 3 < len(lines_m) and lines_m[cm + 3][1].startswith("**Tô màu Việt:**")
                    want_cm = ["Nhật", "Tô màu", "Tô màu Việt", "Việt"] if (need_vi or has_vi) else ["Nhật", "Tô màu", "Việt"]
                    _check_nvb(name, f"{name}:{lines_m[cm][0]}", lines_m[cm + 1: cm + 1 + len(want_cm)], want_cm, rep, "Câu mẫu")
            # Cách chia
            cb = next((b for b in h3s if b[0] == V6_CHIA_HEAD), None)
            if cb:
                items = [(i, lab, val) for i, lab, val in _labelled([(i, l) for i, l in cb[2] if l.strip()])]
                k = 0
                same = 0
                j = 0
                while j < len(items):
                    i, lab, val = items[j]
                    gm = re.fullmatch(r"Giống cách dùng (\d+)", lab)
                    sm = re.fullmatch(r"Cấu trúc (\d+)", lab)
                    if gm:
                        same += 1
                        if not 1 <= int(gm.group(1)) < usage_no:
                            rep.err(f"{name}:{i}", f"`Giống cách dùng {gm.group(1)}` phải trỏ tới một cách dùng đứng trước")
                        if not val:
                            rep.err(f"{name}:{i}", "Dòng `Giống cách dùng n` cần nhắc lại ngắn cách chia")
                        if k:
                            rep.err(f"{name}:{i}", "Dòng `Giống cách dùng n` đặt trước các thẻ Cấu trúc")
                        j += 1
                    elif sm:
                        k += 1
                        stats["n_struct"] += 1
                        if int(sm.group(1)) != stats["n_struct"]:
                            rep.err(f"{name}:{i}", f"Cấu trúc đánh số sai: là {sm.group(1)}, phải là {stats['n_struct']} (đánh số liên tục cả bài)")
                        stats["struct_sec"][stats["n_struct"]] = idx
                        if not val:
                            rep.err(f"{name}:{i}", "Dòng Cấu trúc đang trống")
                        nxt = items[j + 1] if j + 1 < len(items) else None
                        if not nxt or nxt[1] != "Giải thích":
                            rep.err(f"{name}:{i}", "Sau mỗi dòng Cấu trúc phải là 1 dòng `**Giải thích:** …`")
                            j += 1
                        else:
                            if vi_words(nxt[2]) < 10:
                                rep.warn(f"{name}:{nxt[0]}", "Giải thích cấu trúc quá ngắn – nói đủ: gắn thế nào, chia dạng gì, sắc thái")
                            j += 2
                    else:
                        rep.err(f"{name}:{i}", "Cách chia chỉ gồm `**Giống cách dùng n:** …` (tùy chọn) và các khối `**Cấu trúc n:**` + `**Giải thích:**`")
                        j += 1
                if not k and not same:
                    rep.err(f"{name}:{cb[1]}", "Cách chia cần ít nhất 1 thẻ `**Cấu trúc n:**` hoặc dòng `**Giống cách dùng n:**`")
                if usage_no == 1 and not k:
                    rep.err(f"{name}:{cb[1]}", "Cách dùng 1 phải có thẻ Cấu trúc đầy đủ")
                stats["sections"][-1]["cards"] = k
                stats["sections"][-1]["same"] = same
            ex_blocks = [b for b in h3s if b[0] not in (V6_MEANING_HEAD, V6_CHIA_HEAD)]
        else:
            seen_phrase = True
            stats["phrases"].append(mp.group(2).strip())
            got = _labelled(pre)
            if [g[1] for g in got] != ["Cụm", "Nghĩa", "Giải thích"]:
                rep.err(f"{name}:{ln}", "Cách nói thường gặp: ngay sau tiêu đề là `**Cụm:**` → `**Nghĩa:**` → `**Giải thích:**`, rồi các `### Ví dụ`")
            ex_blocks = h3s
        if not ex_blocks:
            rep.err(f"{name}:{ln}", "Chương chưa có ví dụ nào")
        seen_new = False
        for ehead, eln, elines in ex_blocks:
            k_ex += 1
            el = [(i, l) for i, l in elines if l.strip()]
            _check_example(name, ehead, eln, el, k_ex, idx, "usage" if mu else "phrase", rep, stats, need_vi)
            em = EXAMPLE_RE.match(ehead)
            if em and em.group(2):
                seen_new = True
                stats["new"] += 1
            elif em and seen_new:
                rep.warn(f"{name}:{eln}", "Ví dụ [MỚI] nên đặt cuối chương")
    stats["examples"] = k_ex

    # --- mục 5 Bẫy
    h5 = "## 4. Bẫy dễ nhầm"
    traps: list[tuple[int, int, list[tuple[int, str]]]] = []
    for i, l in body_lines(h5):
        tm = re.match(r"^\*\*Bẫy (\d+) – .+?:\*\*", l)
        if tm:
            traps.append((i, int(tm.group(1)), []))
        elif traps and l.strip():
            traps[-1][2].append((i, l))
        elif l.strip():
            rep.err(f"{name}:{i}", "Mục 4: mỗi bẫy bắt đầu bằng `**Bẫy <n> – <tên>:** …`")
    if not traps:
        rep.err(name, "Mục 4 cần ít nhất 1 bẫy dạng `**Bẫy 1 – <tên>:** …` + `**Nhật:**` + `**Việt:**`")
    for k, (i, n, rest) in enumerate(traps, 1):
        if n != k:
            rep.err(f"{name}:{i}", f"Bẫy đánh số sai: là {n}, phải là {k}")
        _check_nvb(name, f"{name}:{i}", rest, ["Nhật", "Việt"], rep, "Bẫy")

    # --- mục 6 Tổng kết
    h6 = "## 5. Tổng kết, mẹo nhớ và lưu ý"
    l6 = [(i, l) for i, l in body_lines(h6) if l.strip()]
    tops = [(n, i, lab) for n, (i, lab, _) in enumerate(_labelled(l6)) if lab in V6_SUMMARY_LABELS]
    order = [t[2] for t in tops]
    want = [lab for lab in V6_SUMMARY_LABELS if lab in order or lab not in V6_SUMMARY_OPTIONAL]
    if order != want:
        rep.err(name, "Mục 5: các nhãn theo thứ tự " + " → ".join(
            f"`{lab}`{' (tùy chọn)' if lab in V6_SUMMARY_OPTIONAL else ''}" for lab in V6_SUMMARY_LABELS) + f"; đang có {order}")
    else:
        bounds = [t[0] for t in tops] + [len(l6)]
        for (n, i, lab), end in zip(tops, bounds[1:]):
            seg = l6[n + 1:end]
            if lab == "Kết":
                has_vi = any(l.startswith("**Tô màu Việt:**") for _, l in seg)
                want_k = ["Nhật", "Tô màu", "Tô màu Việt", "Việt"] if (need_vi or has_vi) else ["Nhật", "Tô màu", "Việt"]
                _check_nvb(name, f"{name}:{i}", seg, want_k, rep, "Phần Kết")
            elif lab == "Tình huống thực tế":
                if not seg or any(not l.startswith("- ") for _, l in seg):
                    rep.err(f"{name}:{i}", "Tình huống thực tế: các ý gạch đầu dòng (vd `- Công việc: …`)")
            elif lab == "Người Nhật thường nói":
                if not seg or len(seg) % 3 or len(seg) > 12:
                    rep.err(f"{name}:{i}", "Người Nhật thường nói: 1–4 nhóm `**Nhật:**` → `**Việt:**` → `**Ý:**`")
                else:
                    for g in range(0, len(seg), 3):
                        _check_nvb(name, f"{name}:{seg[g][0]}", seg[g:g + 3], ["Nhật", "Việt", "Ý"], rep, "Người Nhật thường nói")

    for i, line in enumerate(lines, 1):
        if need_vi and len(stats["usages"]) == 1 and re.search(r"[Cc]ách dùng (1|một)\b|cách dùng thứ nhất", line):
            rep.err(f"{name}:{i}", "Bài chỉ có 1 cách dùng – không viết/nói \"cách dùng 1\", chỉ \"cách dùng\"")
        elif re.search(r"[Cc]ách dùng (một|hai|ba|bốn|năm|sáu|bảy)\b", line):
            rep.err(f"{name}:{i}", "Viết số bằng chữ số: `Cách dùng 1`, `Cách dùng 2`… (không viết \"cách dùng một/hai\")")
    check_common_lines(name, lines, rep)
    return stats


def check_counts_v6(stats: dict, gc: str, rep: Report, kb_name: str, gc_name: str) -> None:
    """Quy tắc 6.1: chương cách dùng 4–6 ví dụ, chương cách nói 1–3; mọi thẻ Cấu trúc có ví dụ; giới hạn [MỚI]."""
    ex = stats["ex"]
    secs = {s_["idx"]: s_ for s_ in stats["sections"]}
    n_struct = stats["n_struct"]
    cov = parse_coverage(gc)
    if cov is None:
        rep.err(gc_name, "Thiếu mục `### Bảng phủ ví dụ` (| Ví dụ | Phần | Cấu trúc | Nguồn |, Phần = 3.1, 3.2…) – xem template Ghi chú")
        cov = []
    by_ex: dict[int, tuple[int, int, list[int]]] = {}
    for ln, e, sec, st in cov:
        if e in by_ex:
            rep.err(f"{gc_name}:{ln}", f"Bảng phủ: ví dụ {e} xuất hiện 2 lần")
        by_ex[e] = (ln, sec, st)
        for s_ in st:
            if not 1 <= s_ <= n_struct:
                rep.err(f"{gc_name}:{ln}", f"Bảng phủ: ví dụ {e} ghi Cấu trúc {s_} nhưng bài chỉ có {n_struct} thẻ cấu trúc")
    for x in ex:
        row = by_ex.get(x["n"])
        if cov and row is None:
            rep.err(gc_name, f"Bảng phủ thiếu dòng cho Ví dụ {x['n']}")
            continue
        if row is None:
            continue
        if row[1] != x["sec"]:
            rep.err(f"{gc_name}:{row[0]}", f"Bảng phủ: Ví dụ {x['n']} nằm ở phần {CH}.{x['sec']} trong Kịch bản, bảng ghi {CH}.{row[1]}")
        if x["kind"] == "usage" and not row[2]:
            rep.err(f"{gc_name}:{row[0]}", f"Bảng phủ: ví dụ {x['n']} chưa ghi số Cấu trúc")
    if cov:
        extra = sorted(set(by_ex) - {x["n"] for x in ex})
        if extra:
            rep.err(gc_name, f"Bảng phủ có ví dụ không tồn tại trong Kịch bản: {extra}")
        covered = {s_ for _, _, st in by_ex.values() for s_ in st}
        missing = [k for k in range(1, n_struct + 1) if k not in covered]
        if missing:
            rep.err(kb_name, "Chưa có ví dụ cho " + ", ".join(f"Cấu trúc {k}" for k in missing)
                    + " – mỗi thẻ Cấu trúc cần ít nhất 1 ví dụ")

    allowed_new = 0
    for idx, sec in secs.items():
        mine = [x for x in ex if x["sec"] == idx]
        non_new = sum(1 for x in mine if not x["new"])
        if sec["kind"] == "usage":
            own = [k for k, s_ in stats["struct_sec"].items() if s_ == idx]
            hi = max(MAX_PER_USAGE, len(own))
            if not MIN_PER_USAGE <= len(mine) <= hi:
                rep.err(kb_name, f"Phần {CH}.{idx} (cách dùng) có {len(mine)} ví dụ – phải {MIN_PER_USAGE}–{MAX_PER_USAGE}"
                        + (f" (được tới {hi} để phủ {len(own)} thẻ cấu trúc)" if hi > MAX_PER_USAGE else ""))
            allowed_new += max(0, MIN_PER_USAGE - non_new)
        else:
            if not V6_PHRASE_MIN <= len(mine) <= V6_PHRASE_MAX:
                rep.err(kb_name, f"Phần {CH}.{idx} (cách nói thường gặp) có {len(mine)} ví dụ – phải {V6_PHRASE_MIN}–{V6_PHRASE_MAX}")
            allowed_new += max(0, V6_PHRASE_MIN - non_new)
    only_new = [k for k in range(1, n_struct + 1)
                if any(k in by_ex.get(x["n"], (0, 0, []))[2] for x in ex)
                and not any(k in by_ex.get(x["n"], (0, 0, []))[2] for x in ex if not x["new"])]
    allowed_new += len(only_new)
    if stats["new"] > allowed_new:
        rep.err(kb_name, f"Có {stats['new']} ví dụ [MỚI] nhưng chỉ cần tối đa {allowed_new} – ưu tiên ví dụ bài gốc")
    for x in ex:
        if x["ghep"] and not re.search(r"\b(dạng|cụm)\b", x["ghep"], re.I):
            rep.err(f"{kb_name}:{x['ghep_ln']}", "Cách ghép phải nói ví dụ dùng dạng cấu trúc nào (vd \"Đây là dạng V た ＋ ところで.\") "
                    "hoặc cụm nào (chương Cách nói thường gặp)")


# ---------------------------------------------------------------- kiểm tra cả thư mục
def rule_version(gc: str) -> tuple:
    m = re.search(r"^- Phiên bản quy tắc:\s*(\d+)\.(\d+)\.(\d+)", gc, re.M)
    return tuple(int(x) for x in m.groups()) if m else NEW_RULE_VERSION


def parse_coverage(gc: str) -> list[tuple[int, int, int, list[int]]] | None:
    """Bảng phủ ví dụ trong Ghi chú: | Ví dụ | Cách dùng | Cấu trúc | … |  → [(dòng, ví dụ, cách dùng, [cấu trúc…])]."""
    lines = gc.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("#") and "Bảng phủ ví dụ" in l), None)
    if start is None:
        return None
    rows = []
    for i in range(start + 1, len(lines)):
        l = lines[i]
        if l.startswith("#"):
            break
        cells = [c.strip() for c in l.strip().strip("|").split("|")] if l.strip().startswith("|") else []
        m2 = re.fullmatch(r"(?:3\.)?(\d+)", cells[1]) if len(cells) >= 3 else None
        if m2 and re.fullmatch(r"\d+", cells[0]):
            st = [int(x) for x in re.findall(r"\d+", cells[2])]
            rows.append((i + 1, int(cells[0]), int(m2.group(1)), st))
    return rows


def check_counts(stats: dict, gc: str, rep: Report, kb_name: str, gc_name: str) -> None:
    """Số ví dụ theo từng cách dùng + phủ mọi dạng cấu trúc (quy tắc 5.3.0) hoặc quy tắc cũ cho bài < 5.3.0."""
    ex = stats["ex"]
    n_usage = len(stats["usages"])
    n_struct = stats["n_struct"]
    ver = rule_version(gc)
    if ver < NEW_RULE_VERSION:
        if not LEGACY_MIN_TOTAL <= len(ex) <= LEGACY_MAX_TOTAL:
            rep.err(kb_name, f"Tổng {len(ex)} ví dụ – bài theo quy tắc cũ phải 4–6 ví dụ cả bài")
        rep.warn(kb_name, f"Bài làm theo quy tắc {'.'.join(map(str, ver))} (4–6 ví dụ cả bài). Quy tắc mới: 4–6 ví dụ MỖI cách dùng "
                 "và phủ mọi dạng cấu trúc – muốn nâng cấp thì làm lại thành <ID>-v2")
        return

    # --- bảng phủ
    cov = parse_coverage(gc)
    if cov is None:
        rep.err(gc_name, "Thiếu mục `## … Bảng phủ ví dụ` (| Ví dụ | Cách dùng | Cấu trúc | Nguồn |) – xem template Ghi chú")
        cov = []
    by_ex: dict[int, tuple[int, int, list[int]]] = {}
    for ln, e, u, st in cov:
        if e in by_ex:
            rep.err(f"{gc_name}:{ln}", f"Bảng phủ: ví dụ {e} xuất hiện 2 lần")
        by_ex[e] = (ln, u, st)
        if not st:
            rep.err(f"{gc_name}:{ln}", f"Bảng phủ: ví dụ {e} chưa ghi số Cấu trúc")
        for s_ in st:
            if not 1 <= s_ <= n_struct:
                rep.err(f"{gc_name}:{ln}", f"Bảng phủ: ví dụ {e} ghi Cấu trúc {s_} nhưng mục 4 chỉ có {n_struct} cấu trúc")
    if cov:
        for x in ex:
            row = by_ex.get(x["n"])
            if row is None:
                rep.err(gc_name, f"Bảng phủ thiếu dòng cho Ví dụ {x['n']}")
            elif row[1] != x["usage"]:
                rep.err(f"{gc_name}:{row[0]}", f"Bảng phủ: Ví dụ {x['n']} nằm ở Cách dùng {x['usage']} trong Kịch bản, bảng ghi {row[1]}")
        extra = sorted(set(by_ex) - {x["n"] for x in ex})
        if extra:
            rep.err(gc_name, f"Bảng phủ có ví dụ không tồn tại trong Kịch bản: {extra}")
        covered = {s_ for _, _, st in by_ex.values() for s_ in st}
        missing = [k for k in range(1, n_struct + 1) if k not in covered]
        if missing:
            rep.err(kb_name, "Chưa có ví dụ cho " + ", ".join(f"Cấu trúc {k}" for k in missing)
                    + " – mỗi dòng Cấu trúc ở mục 4 cần ít nhất 1 ví dụ")

    # --- số ví dụ mỗi cách dùng
    allowed_new = 0
    for u in range(1, n_usage + 1):
        mine = [x for x in ex if x["usage"] == u]
        structs = {s_ for x in mine for s_ in by_ex.get(x["n"], (0, 0, []))[2]}
        hi = max(MAX_PER_USAGE, len(structs))
        if not MIN_PER_USAGE <= len(mine) <= hi:
            rep.err(kb_name, f"Cách dùng {u} có {len(mine)} ví dụ – phải {MIN_PER_USAGE}–{MAX_PER_USAGE} ví dụ mỗi cách dùng"
                    + (f" (được tới {hi} để phủ {len(structs)} dạng cấu trúc)" if hi > MAX_PER_USAGE else ""))
        allowed_new += max(0, MIN_PER_USAGE - sum(1 for x in mine if not x["new"]))
    only_new = [k for k in range(1, n_struct + 1)
                if any(k in by_ex.get(x["n"], (0, 0, []))[2] for x in ex)
                and not any(k in by_ex.get(x["n"], (0, 0, []))[2] for x in ex if not x["new"])]
    allowed_new += len(only_new)
    if stats["new"] > allowed_new:
        rep.err(kb_name, f"Có {stats['new']} ví dụ [MỚI] nhưng chỉ cần tối đa {allowed_new} (bù cho đủ {MIN_PER_USAGE} ví dụ mỗi cách dùng "
                "+ phủ dạng cấu trúc bài gốc không có ví dụ) – ưu tiên ví dụ bài gốc")

    # --- Cách ghép phải nói dạng cấu trúc
    for x in ex:
        if not re.search(r"\bdạng\b", x["ghep"], re.I):
            rep.err(f"{kb_name}:{x['ghep_ln']}", "Cách ghép phải nói ví dụ dùng dạng cấu trúc nào (vd \"dạng V た ＋ ところで\")")


def check_folder(folder: Path, write: bool = True) -> Report:
    """Kiểm tra 1 bài. write=True: sinh file phụ (_phu/) và, với bài trong work/, cập nhật work/_index.js + trạng thái nguồn."""
    rep = Report()
    folder = folder.resolve()
    fid = folder.name
    f = build_data.files_of(folder)

    work_id = re.match(r"^N[1-5]_[^\\/:*?\"<>|\s]+_v\d{2,}_r\d{2,}$", fid)
    if build_data.in_work(folder):
        if not work_id:
            rep.err("thư mục", f"Tên thư mục `{fid}` sai quy ước `<cấp>_<mẫu>_vNN_rNN` – tạo thư mục bằng `python tools/nguon.py bat-dau <file nguồn>`")
        elif not fid.startswith(folder.parent.name + "_"):
            rep.err("thư mục", f"`{fid}` nằm trong work/{folder.parent.name}/ nhưng cấp độ trong tên khác")
    elif not (work_id or re.match(r"^N[1-5](-\d+)?_[a-z0-9-]+$", fid)):
        rep.err("thư mục", f"Tên thư mục `{fid}` sai quy ước `<cấp>_<mẫu>_vNN_rNN` (hoặc kiểu cũ `<N?>_<slug>`)")

    # --- file ở gốc thư mục bài: chỉ có Kịch bản (file duy nhất cần tải lên NotebookLM)
    stray = sorted(p.name for p in folder.iterdir() if p.is_file() and p.name != f["kichban"].name)
    if stray:
        rep.warn("thư mục", "Gốc thư mục bài chỉ nên có KichBan_<ID>.md; file khác (định dạng cũ?) nên xóa "
                 f"hoặc chuyển vào {SUB}/: {', '.join(stray)}")

    gc = read(f["ghichu"], rep) if f["ghichu"].exists() else ""
    stats = None
    is_v6 = False
    if f["kichban"].exists():
        kb_text = read(f["kichban"], rep)
        is_v6 = bool(re.search(r"^### Ý nghĩa và cách dùng\s*$", kb_text, re.M))
        ver = rule_version(gc) if gc else (V6_VERSION if is_v6 else NEW_RULE_VERSION)
        if is_v6 and ver < V6_VERSION:
            rep.err(f["ghichu"].name, f"Kịch bản theo khung chương (6.1) nhưng Ghi chú ghi phiên bản quy tắc {'.'.join(map(str, ver))}")
        if not is_v6 and ver >= V6_VERSION:
            rep.err(f["kichban"].name, "Ghi chú ghi quy tắc ≥ 6.1 nhưng Kịch bản chưa theo khung chương "
                    "(1 Mở màn · 2 Giới thiệu & mô tả mẫu · 3.x chương cách dùng · 4 Bẫy · 5 Tổng kết) – xem core/templates/KichBan.template.md")
        stats = check_kichban_v6(f["kichban"], kb_text, rep, ver) if is_v6 else check_kichban(f["kichban"], kb_text, rep)
    else:
        rep.err("thư mục", f"Thiếu file `{f['kichban'].name}` ở gốc thư mục bài")

    if f["ghichu"].exists():
        check_placeholders(f"{SUB}/{f['ghichu'].name}", gc, rep)
        if "KHÔNG tải lên NotebookLM" not in gc:
            rep.warn(f["ghichu"].name, "Thiếu dòng nhắc `KHÔNG tải lên NotebookLM`")
        for label in ("Ngày tạo", "Công cụ AI / model"):
            if not build_data.ghichu_field(gc, label):
                rep.err(f["ghichu"].name, f"Phần đầu thiếu dòng `- {label}: …` (dùng để sinh meta)")
        if not re.search(r"^- Ngày tạo:\s*\d{4}-\d{2}-\d{2}\s*$", gc, re.M):
            rep.warn(f["ghichu"].name, "`- Ngày tạo:` nên có dạng YYYY-MM-DD")
    else:
        rep.err("thư mục", f"Thiếu file `{SUB}/{f['ghichu'].name}`")
    if not f["baigoc"].exists():
        rep.warn("thư mục", f"Thiếu `{SUB}/{f['baigoc'].name}` (bài giảng gốc đã lưu)")

    if stats is not None:
        if is_v6:
            check_counts_v6(stats, gc, rep, f["kichban"].name, f["ghichu"].name)
        else:
            check_counts(stats, gc, rep, f["kichban"].name, f["ghichu"].name)
            if rule_version(gc) >= NEW_RULE_VERSION:
                rep.warn(f["kichban"].name, "Kịch bản theo khung cũ (trước 6.1): ý nghĩa và cấu trúc chung cho cả bài. "
                         "Khung mới trình bày từng cách dùng: Ý nghĩa → Cách chia → Ví dụ – muốn nâng cấp thì làm lại thành <ID>-v2")

    # --- meta sinh tự động: kiểm tra những gì lấy được từ Kịch bản / Ghi chú
    if stats is not None:
        meta, tuychinh = build_data.derive(folder)
        if meta["cap_do"] not in {"N5", "N4", "N3", "N2", "N1"}:
            rep.err("meta", f"Không xác định được cấp độ N5–N1 (đang là `{meta['cap_do']}`)")
        lv = build_data.ghichu_field(gc, "Cấp độ")
        if lv and lv != meta["cap_do"]:
            rep.err(f["ghichu"].name, f"Cấp độ trong Ghi chú ({lv}) khác ID thư mục ({meta['cap_do']})")
        if not meta["cach_dung"]:
            rep.err("meta", "Không đọc được tên cách dùng từ Kịch bản – text tùy chỉnh sẽ ghi \"Cách dùng: .\"")
        if not meta["mau"] or not meta["nghia"]:
            rep.err(f["kichban"].name, "Không tách được mẫu / nghĩa từ tiêu đề `# <mẫu> – <nghĩa>`")
        if "{{" in tuychinh:
            rep.err("TuyChinh", "Template core/templates/TuyChinh.template.txt có placeholder lạ chưa được điền")
        if len(tuychinh) > 4000:
            rep.warn("TuyChinh", f"Dài {len(tuychinh)} ký tự – ô tùy chỉnh của NotebookLM có thể giới hạn độ dài")

    # --- đường dẫn tuyệt đối làm hỏng tính di động của dự án
    try:
        import check_portable  # type: ignore
        for where, label, hit in check_portable.scan(folder):
            rep.err(where.split("/")[-1], f"Có đường dẫn tuyệt đối ({label}): {hit} – dùng đường dẫn tương đối")
    except ImportError:
        rep.warn("thư mục", "Không tìm thấy tools/check_portable.py để kiểm tra đường dẫn tuyệt đối")

    # --- sinh file phụ + cập nhật danh sách cho HuongDan.html
    if write and stats is not None:
        build_data.write_lesson(folder, len(rep.errors), len(rep.warnings))
        if build_data.in_work(folder):
            try:
                import nguon  # type: ignore
                note = nguon.danh_dau(folder, not rep.errors)
                if note:
                    rep.note = note  # type: ignore[attr-defined]
            except SystemExit as e:
                rep.warn("nguồn", str(e))
            build_data.write_index()

    rep.stats = stats  # type: ignore[attr-defined]
    return rep


def _link(folder_rel: str | None, p: Path, label: str, desc: str) -> tuple[str, str]:
    from urllib.parse import quote
    target = quote(folder_rel, safe="/") if folder_rel is not None else p.as_uri()
    return f"- [{label}]({target}) – {desc}", f"- {p.as_uri()}{'/' if p.is_dir() else ''}"


def links_block(folder: Path) -> str:
    """Khối link bấm được: link markdown (đường dẫn tương đối từ gốc dự án) + file:/// tuyệt đối."""
    folder = folder.resolve()
    f = build_data.files_of(folder)

    def rel(p: Path) -> str | None:
        try:
            return p.relative_to(ROOT).as_posix() + ("/" if p.is_dir() else "")
        except ValueError:
            return None

    items = [
        (ROOT / "HuongDan.html", "HuongDan.html", "👉 trang làm video (F5 nếu đang mở) – bài mới được chọn sẵn"),
        (f["kichban"], f["kichban"].name, "nguồn tải lên NotebookLM cho bài này"),
        (folder, f"📁 {folder.name}/", "thư mục bài"),
        (ROOT / "guide.md", "guide.md", "nguồn chung – chỉ tải lên NotebookLM 1 lần"),
    ]
    md, uri = [], []
    for p, label, desc in items:
        if not p.exists():
            continue
        a, b = _link(rel(p), p, label, desc)
        md.append(a)
        uri.append(b)
    return "\n".join(
        ["### 📂 Mở nhanh", ""] + md
        + ["", "Đường dẫn đầy đủ (Ctrl/Cmd + click nếu link ở trên không bấm được):", ""] + uri
    )


def main(argv: list[str]) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows console
    except Exception:
        pass
    links_only = "--links" in argv
    argv = [a for a in argv if a != "--links"]
    if len(argv) != 2:
        print(__doc__)
        return 2
    folder = Path(argv[1])
    if not folder.is_dir():
        print(f"Không tìm thấy thư mục: {folder}")
        return 2
    if links_only:
        print(links_block(folder))
        return 0

    rep = check_folder(folder)
    print(f"Kiểm tra: {folder}")
    print("-" * 60)
    for line in rep.errors + rep.warnings:
        print(line)
    st = getattr(rep, "stats", None)
    print("-" * 60)
    if st:
        print(f"Cách dùng: {len(st['usages'])} | Ví dụ: {st['examples']} (MỚI: {st['new']})")
    if getattr(rep, "note", ""):
        print(rep.note)
    verdict = "ĐẠT" if not rep.errors else "KHÔNG ĐẠT"
    print(f"Kết quả: {verdict} – {len(rep.errors)} lỗi, {len(rep.warnings)} cảnh báo")
    if not rep.errors:
        print()
        print("=" * 60)
        print("Dán NGUYÊN VĂN khối dưới đây vào cuối báo cáo (KHÔNG đặt trong khối code):")
        print("=" * 60)
        print(links_block(folder))
    return 0 if not rep.errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
