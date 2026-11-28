"""Audit active VNJPClub SingleFile captures without accessing the website."""

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path
from tempfile import NamedTemporaryFile


VOID = set("area base br col embed hr img input link meta param source track wbr".split())
JAPANESE = re.compile(r"[ぁ-んァ-ヺ一-龯]")
ANSWER = re.compile(r"đáp án(?: đúng)?\s*:\s*([1-9]\d*)", re.I)


def translated_value(value):
    text = (value or "").strip()
    if not text or re.search(r"</?[a-z][^>]*>", text, re.I) or "[chưa lấy được]" in text.casefold():
        return ""
    return text
# These two shared recordings have been reviewed against the numbered questions.
# Match both spoken prompts so a revised capture cannot inherit a link by position alone.
SHARED_PROMPTS = {
    ("N2", "2018-07"): (
        "男の人はどのグループのボランティアをしたいと言っていますか",
        "女の人はどのグループのボランティアをしたいと言っていますか",
    ),
    ("N2", "2018-12"): (
        "男の生徒はどの先輩の話を聞きに行きますか",
        "女の生徒はどの先輩の話を聞きに行きますか",
    ),
}


class Node:
    def __init__(self, tag, attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.classes = self.attrs.get("class", "").split()
        self.children = []

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def find(self, cls):
        return [node for node in self.walk() if cls in node.classes]

    def text(self):
        if self.tag in {"script", "style", "rt", "rp", "button"}:
            return ""
        return "".join(child if isinstance(child, str) else child.text()
                       for child in self.children).strip()


class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        if self.stack[-1].tag not in {"script", "style"}:
            self.stack[-1].children.append(data)


def explanation_text(node):
    if isinstance(node, str):
        return node
    if node.tag in {"script", "style", "button", "rt", "rp"}:
        return ""
    if node.tag == "br":
        return "\n"
    value = "".join(explanation_text(child) for child in node.children)
    if node.tag in {"p", "div", "li"}:
        return "\n" + value + "\n"
    return value


def appendix_answers(doc):
    notes = next((n for n in doc.walk() if n.attrs.get("id") == "jlpt-singlefile-notes"), None)
    answers = {}
    if notes:
        for row in notes.walk():
            key = row.attrs.get("data-key", "")
            if key.startswith("answer-"):
                # The bookmarklet stores a heading, a text node and an optional backlink.
                answers[key[7:]] = "".join(c for c in row.children if isinstance(c, str)).strip()
    return answers


def source_explanation(question, appendix):
    anchor = question.attrs["id"]
    candidates = [(explanation_text(n), "#" + anchor + " .complete-answer")
                  for n in question.find("complete-answer")]
    candidates.append((appendix.get(anchor, ""), f'#jlpt-singlefile-notes [data-key="answer-{anchor}"]'))
    for raw, locator in candidates:
        value = "\n".join(line.strip() for line in raw.strip().splitlines())
        if (value and not re.fullmatch(r"[.\s…]+|(?:đáp án(?: đúng)?\s*[:：]?\s*)?[1-9][.。]?", value, re.I)
                and not re.fullmatch(r"(?:đang tải|loading|vui lòng (?:chờ|đợi)|chưa có (?:lời giải|giải thích)|"
                                     r"(?:bạn cần|vui lòng) đăng nhập(?: để xem(?: (?:lời giải|giải thích|đáp án))?)?|\[chưa lấy được\])[.!…\s]*", value, re.I)):
            # The bookmarklet saves rendered innerText, including the actual line breaks.
            rendered = appendix.get(anchor, "")
            if rendered and rendered.split() == value.split():
                value = rendered
            return value, locator
    return "", None


def group_gaps(locations, missing):
    groups = {}
    for qid in missing:
        groups.setdefault(locations.get(qid, "?"), []).append(qid)
    return [{"mondai": group, "questions": questions} for group, questions in groups.items()]


def interval(player):
    try:
        start = Decimal(player.attrs["data-start"])
        end = Decimal(player.attrs["data-end"])
        if start.is_finite() and end.is_finite() and 0 <= start < end:
            return [int(round(start * 1000)), int(round(end * 1000))]
    except (KeyError, ValueError, InvalidOperation):
        pass
    return None


def audit_page(root, path, media):
    raw = path.read_bytes()
    parser = Document()
    parser.feed(raw.decode("utf-8-sig"))
    parser.close()
    doc = parser.root
    selected = [n.text() for n in doc.walk() if n.tag == "option" and "selected" in n.attrs]
    period = next((s for s in selected if re.fullmatch(r"\d{4}-\d{2}", s)), None)
    section = "listening" if "聴解" in selected else (
        "written" if any("読解" in s or "文字" in s or "文法" in s for s in selected) else None)
    level = path.relative_to(root).parts[0]
    qs = doc.find("q-item")
    page = {"path": path.relative_to(root).as_posix(), "sha256": hashlib.sha256(raw).hexdigest(),
            "level": level, "period": period, "section": section, "questionCount": len(qs)}
    if not period or not section or not qs:
        page["issue"] = "unrecognized_page_layout"
        return page

    locations = {}
    for block in doc.find("mondai-block"):
        titles = block.find("mondai-title")
        title = titles[0].text() if titles else "?"
        for q in block.find("q-item"):
            locations[q.attrs.get("id")] = title

    ids = [q.attrs.get("id") for q in qs]
    if not all(ids) or len(set(ids)) != len(ids):
        page["issue"] = "invalid_or_duplicate_question_ids"
        return page
    bad_keys, missing_explanations = [], []
    scripts, ranges = {}, {}
    appendix = appendix_answers(doc)
    for qid, q in zip(ids, qs):
        choices = q.find("choice")
        marked = [i for i, c in enumerate(choices, 1) if "choice-correct" in c.classes]
        results = [m.group(1) for line in q.find("result-line") for m in ANSWER.finditer(line.text())]
        if len(marked) != 1 or results != [str(marked[0])]:
            bad_keys.append(qid)
        if not source_explanation(q, appendix)[0]:
            missing_explanations.append(qid)
        for panel in q.find("vnjp-choukai-q-script-panel"):
            lines = panel.find("vnjp-jlpt-candich")
            value = "".join(n.text() for n in lines) if lines else panel.text()
            if JAPANESE.search(value):
                scripts[qid] = value
            cuts = [interval(n) for n in panel.find("vnjp-choukai-q-player")]
            if len(cuts) == 1 and cuts[0]:
                ranges[qid] = cuts[0]

    notes = next((n for n in doc.walk() if n.attrs.get("id") == "jlpt-singlefile-notes"), None)
    translations = Counter()
    missing_translations = []
    for entry in notes.walk() if notes else ():
        key = entry.attrs.get("data-key", "")
        if not key.startswith("["):
            continue
        try:
            group, qid, line_index, source_text = json.loads(key)
        except (ValueError, TypeError):
            continue
        if not isinstance(group, str) or not group.startswith("Dịch "):
            continue
        if translated_value(entry.attrs.get("data-vi")):
            translations["script" if group.startswith("Dịch script") else "exam"] += 1
        else:
            missing_translations.append({"group": group, "question": qid, "lineIndex": line_index,
                                         "sourceExcerpt": str(source_text)[:60]})

    page.update({
        "unverifiedKeys": group_gaps(locations, bad_keys),
        "missingSourceExplanations": group_gaps(locations, missing_explanations),
        "savedTranslationLines": dict(translations),
        "missingScannedTranslationLines": missing_translations,
    })
    if section != "listening":
        return page

    shared = []
    prompts = SHARED_PROMPTS.get((level, period))
    if (prompts and "q-29" in ids and "q-29" not in scripts and
            all(prompt in scripts.get("q-30", "") for prompt in prompts)):
        shared.append({"questions": ["q-29", "q-30"], "scriptOwner": "q-30",
                       "evidence": list(prompts), "intervalMs": ranges.get("q-30")})
    covered = set(scripts)
    timed = set(ranges)
    for pair in shared:
        covered.update(pair["questions"])
        if pair["intervalMs"]:
            timed.update(pair["questions"])
    page.update({
        "scriptPanelCountWithJapanese": len(scripts),
        "intervalCount": len(ranges),
        "sharedScripts": shared,
        "requestScript": group_gaps(locations, [qid for qid in ids if qid not in covered]),
        "unverifiedTiming": group_gaps(locations, [qid for qid in ids if qid not in timed]),
        "masterAudioCandidates": audio_candidates(root, path, page, media),
    })
    return page


def audio_candidates(root, path, page, media):
    pattern = f"{page['level']}-{page['period']}".casefold()
    return [p.relative_to(root).as_posix() for p in media if p.parent == path.parent or pattern in p.stem.casefold()]


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--root", type=Path, default=Path.cwd(), help="JLPT corpus root")
    args.add_argument("--out", type=Path, help="JSON report path, relative to root or absolute")
    opt = args.parse_args()
    root = opt.root.resolve(strict=True)
    media = sorted(p for level in root.glob("N[1-5]") for p in level.rglob("*") if p.is_file() and
                   p.suffix.lower() in {".mp3", ".m4a", ".aac", ".ogg", ".wav", ".opus", ".flac"})
    audit_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target = (root / opt.out).resolve() if opt.out else None
    cache = {}
    if target and target.is_file() and target.suffix.lower() == ".json":
        previous = json.loads(target.read_bytes())
        if previous.get("auditorSha256") == audit_hash:
            cache = {p["path"]: p for p in previous["pages"]}
    pages = []
    for level in sorted(root.glob("N[1-5]")):
        for f in sorted(level.rglob("*.html")):
            if any(name.lower() in {"old", "sample"} for name in f.relative_to(level).parts[:-1]):
                continue
            page = cache.get(f.relative_to(root).as_posix())
            if page is not None:
                with f.open("rb") as stream:
                    if hashlib.file_digest(stream, "sha256").hexdigest() != page["sha256"]:
                        page = None
            if page is None:
                page = audit_page(root, f, media)
            elif page.get("section") == "listening":
                page["masterAudioCandidates"] = audio_candidates(root, f, page, media)
            pages.append(page)
    if not pages:
        args.error("No active HTML under N1 through N5")
    counts = Counter((p["level"], p["period"], p["section"]) for p in pages)
    duplicates = [list(key) for key, count in counts.items() if count > 1]
    report = {
        "schemaVersion": 1,
        "auditorSha256": audit_hash,
        "scope": "N1…N5, bỏ qua thư mục old và sample khi đọc HTML. Đường dẫn tính từ JLPT.",
        "howToUse": {
            "requestScript": "Gửi người sưu tầm cấp, kỳ, mondai và số câu. Kiểm tra khả năng dùng chung đoạn trước khi yêu cầu lấy lại từng câu.",
            "missingSourceExplanations": "Báo số câu thiếu lời giải nguồn. Soạn từ bài đọc hoặc script nghe đã kiểm tra, giữ dấu vết giải thích biên tập riêng.",
            "unverifiedKeys": "Đối chiếu lại nguồn nếu dấu chọn đúng và dòng chấm kết quả chưa thống nhất.",
            "savedTranslationLines": "Chỉ đếm bản dịch có nội dung trong phụ lục bookmarklet. Số dòng bằng 0 cần kiểm tra thêm DOM.",
            "unverifiedTiming": "Chưa thấy cặp data-start/end hợp lệ. Xác nhận lại trên audio gốc hoặc dùng mốc mondai đã được duyệt.",
            "masterAudioCandidates": "File local cùng thư mục hoặc khớp tên cấp/kỳ. Đối chiếu nội dung và timeline trước khi ghép với bản phát RSS.",
            "duplicateSections": "Kiểm tra bản trùng hoặc trang tách phần trước khi chọn nguồn chính.",
        },
        "duplicateSections": duplicates,
        "pages": pages,
    }
    data = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if target:
        if target.suffix.lower() != ".json":
            args.error("Output path must end in .json")
        target.parent.mkdir(parents=True, exist_ok=True)
        with NamedTemporaryFile(dir=target.parent, delete=False) as stream:
            temp = Path(stream.name)
            stream.write(data.encode("utf-8"))
        try:
            temp.replace(target)
        finally:
            temp.unlink(missing_ok=True)
    else:
        sys.stdout.buffer.write(data.encode("utf-8"))


if __name__ == "__main__":
    main()
