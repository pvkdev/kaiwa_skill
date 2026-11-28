"""Build one JLPT N5–N1 package from audited offline SingleFile snapshots.

Run audit_sources.py first. Existing edited packages are never overwritten. To stage a
new revision in a separate tree, use --output-root. References remain relative to JLPT.
"""
import argparse
import base64
from collections import Counter
from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unicodedata
from uuid import NAMESPACE_URL, uuid5

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents/skills/jlpt-exam-ingest/scripts"))
from audit_sources import ANSWER, Document, Node, interval, translated_value
sys.path.insert(0, str(ROOT / "contracts/v1"))
from jlpt_coverage import checklist_issues
from jlpt_sentences import sentence_units

SECTIONS = ["mojigoi", "bunpou", "dokkai", "choukai"]


class SingleFileDocument(Document):
    """Expand the optional HTML end tags that SingleFile removes in table layouts."""
    def handle_starttag(self, tag, attrs):
        if tag in {"td", "th", "tr", "tbody", "thead", "tfoot"}:
            close = {"td", "th"} if tag in {"td", "th"} else {"tr", "caption"}
            if tag in {"tbody", "thead", "tfoot"}:
                close |= {"tbody", "thead", "tfoot"}
            for i in range(len(self.stack) - 1, 0, -1):
                if self.stack[i].tag == "table":
                    break
                if self.stack[i].tag in close:
                    del self.stack[i:]
        if tag in {"rp", "rt"} and self.stack[-1].tag in {"rp", "rt"}:
            self.stack.pop()
        super().handle_starttag(tag, attrs)


def digest(data):
    return sha256(data).hexdigest()


def write_exact(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() == data:
            return
        raise ValueError(f"Existing content differs, stage the next revision separately: {path}")
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        stream.write(data)
    os.replace(stream.name, path)


def first(node, cls):
    return next((n for n in node.walk() if cls in n.classes), None)


def tidy(value):
    return "\n".join(line.strip(" \t\r") for line in value.splitlines() if line.strip()).strip()


def table_rows(node):
    for child in node.children:
        if not isinstance(child, Node) or child.tag == "table":
            continue
        if child.tag == "tr":
            yield [c for c in child.children if isinstance(c, Node) and c.tag in {"td","th"}]
        else:
            yield from table_rows(child)


def layout_cells(table):
    # Single-column layout tables can wrap a real data table between paragraphs.
    rows = list(table_rows(table))
    if (rows and all(len(row) == 1 and row[0].attrs.get("colspan", "1") == "1" for row in rows)
            and any(n.tag == "table" and n is not table for n in table.walk())):
        return [row[0] for row in rows]
    return None


def markdown_table(node, renderer):
    """Flatten spans into a rectangular grid, including CSS-circled calendar days."""
    cells = {}
    for row, children in enumerate(table_rows(node)):
        col = 0
        for td in children:
            while (row, col) in cells:
                col += 1
            value = tidy(renderer(td)).replace("|", "\\|").replace("\n", " / ")
            width = max(1, int(td.attrs.get("colspan", "1")))
            height = max(1, int(td.attrs.get("rowspan", "1")))
            for i in range(height):
                for j in range(width):
                    cells[row + i, col + j] = value if not j else ""
            col += width
    if not cells:
        return ""
    width = 1 + max(c for r, c in cells)
    rows = ["| " + " | ".join(cells.get((r, c), "") for c in range(width)) + " |"
            for r in range(1 + max(r for r, c in cells))]
    rows.insert(1, "| " + " | ".join(["---"] * width) + " |")
    caption = next((renderer(n).strip() for n in node.children
                    if isinstance(n, Node) and n.tag == "caption"), "")
    return "\n" + (caption + "\n" if caption else "") + "\n".join(rows) + "\n"


def ja(node):
    if isinstance(node, str):
        return re.sub(r"[\r\n\t]+", " ", node)
    if node is None or node.tag in {"rt", "rp", "script", "style", "svg", "button"}:
        return ""
    if "vnjp-jlpt-kqdich" in node.classes or "vnjp-jlpt-nddich" in node.classes:
        return ""
    if node.tag == "table":
        if cells := layout_cells(node):
            return "\n" + "\n".join(ja(cell) for cell in cells) + "\n"
        return markdown_table(node, ja)
    if node.tag == "br":
        return "\n"
    val = "".join(ja(c) for c in node.children)
    if node.tag == "u" and val.strip():
        return f"【{val.strip()}】"
    if "border-radius:50%" in node.attrs.get("style", "") and val.strip():
        return "◯" + val.strip()
    if node.tag in {"div", "p", "h3", "h4", "li"}:
        return "\n" + val + "\n"
    return val


def translation_index(doc):
    notes = next((n for n in doc.walk() if n.attrs.get("id") == "jlpt-singlefile-notes"), None)
    index = {}
    if notes:
        for row in notes.walk():
            key = row.attrs.get("data-key", "")
            value = translated_value(row.attrs.get("data-vi"))
            if not key.startswith("[") or not value:
                continue
            anchor = next((n.attrs["href"][1:] for n in row.walk()
                           if n.tag == "a" and n.attrs.get("href", "").startswith("#")), None)
            if anchor:
                index[anchor] = value
            group, qid, _, source_text = json.loads(key)
            if group == "Dịch đề" and qid:
                index.setdefault((qid, source_text.strip()), set()).add(value)
    return index


def translations(node, index):
    if not node:
        return ""
    rows = []
    for holder in node.find("vnjp-jlpt-tudich"):
        src = first(holder, "vnjp-jlpt-candich")
        text = index.get(src.attrs.get("id")) if src else None
        inline = first(holder, "vnjp-jlpt-kqdich")
        if not text and inline:
            text = translated_value(inline.text())
        if text:
            rows.append(text.strip())
    return "\n".join(rows)


def source_record(source, path, raw):
    return dict(sourceId=source, kind="local", url=None, localPath=path, sha256=digest(raw),
                capturedAt=None, status="available", note="Bản nguồn lưu trên máy.")


def aligned_rows(node, index):
    """Keep HTML translation anchors intact, including gaps and unwrapped speaker labels."""
    rows = []
    pending = []
    speakers = {"男": "Nam", "女": "Nữ", "男の人": "Nam", "女の人": "Nữ", "先生": "Giáo viên",
                "学生": "Sinh viên", "卒業生": "Cựu học sinh", "アナウンサー": "Phát thanh viên",
                "レポーター": "Phóng viên", "上司": "Cấp trên"}

    def flush():
        value = tidy("".join(pending))
        pending.clear()
        if value:
            rows.append(dict(ja=value, vi=unwrapped_vi(value)))

    def walk(item):
        if isinstance(item, str):
            pending.append(ja(item))
            return
        if item.tag in {"rt", "rp", "button", "style", "script", "svg"} or set(item.classes) & {"vnjp-jlpt-kqdich", "vnjp-jlpt-nddich"}:
            return
        if "vnjp-jlpt-tudich" in item.classes:
            original = first(item, "vnjp-jlpt-candich")
            source = tidy(ja(original))
            if not source:
                return
            prefix = tidy("".join(pending))
            match = re.fullmatch(r"(" + "|".join(speakers) + r")([１-９1-9]?)\s*[:：]", prefix)
            text = translations(item, index) or None
            if match:
                pending.clear()
                source = prefix + source
                if text and not re.match(r"(?:Nam|Nữ|Người đàn ông|Người phụ nữ|Giáo viên|Sinh viên|Cựu học sinh|Phát thanh viên|Phóng viên|Cấp trên)\s*\d*\s*:", text, re.I):
                    digit = unicodedata.normalize("NFKC", match[2])
                    text = speakers[match[1]] + (" " + digit if digit else "") + ": " + text
            else:
                flush()
            rows.append(dict(ja=source, vi=text))
            return
        if item.tag == "table":
            flush()
            if layout := layout_cells(item):
                for cell in layout:
                    walk(cell)
                return
            if any(n is not item and n.tag == "table" for n in item.walk()):
                raise ValueError("Nested data tables need a reviewed layout before conversion.")
            cells = {cell: aligned_rows(cell, index) for cell in item.walk()
                     if cell.tag in {"td", "th", "caption"}}
            if any(row["vi"] is None for aligned in cells.values() for row in aligned):
                # A partially translated form retains its cells and explicit missing translations.
                for aligned in cells.values():
                    rows.extend(aligned)
                return
            # Both grids come from the same DOM rows, spans and cells.
            source_lines = tidy(markdown_table(item, ja)).splitlines()
            target_lines = tidy(markdown_table(item, lambda cell: joined_vi(cells[cell]))).splitlines()
            for source, target in zip(source_lines, target_lines, strict=True):
                if re.fullmatch(r"\|(?:\s*-+\s*\|)+", source):
                    rows[-1]["ja"] += "\n" + source
                    rows[-1]["vi"] += "\n" + target
                else:
                    rows.append(dict(ja=source, vi=target))
            return
        if item.tag in {"br", "div", "p", "td", "th", "li", "h3", "h4"}:
            flush()
        if item.tag == "u" or "border-radius:50%" in item.attrs.get("style", ""):
            if not item.find("vnjp-jlpt-tudich"):
                pending.append(ja(item))
                return
        for child in item.children:
            walk(child)
        if item.tag in {"div", "p", "td", "th", "li", "h3", "h4"}:
            flush()

    walk(node)
    flush()
    return rows


def unwrapped_vi(value):
    """Reviewed unanchored catalog cells; other Japanese stays explicitly untranslated."""
    text = unicodedata.normalize("NFKC", value)
    fixed = {"種目": "Nội dung thi", "参加できる人": "Đối tượng tham gia",
             "スタート予定時間": "Giờ xuất phát dự kiến", "参加費": "Phí tham gia",
             "S:50リットル / M:64リットル / L:81リットル": "S: 50 lít / M: 64 lít / L: 81 lít"}
    if text in fixed:
        return fixed[text]
    if re.fullmatch(r"(?:[SML])※1サイズ", text):
        return "Cỡ " + text[0] + " (chú thích 1)"
    if match := re.fullmatch(r"(\d+)日間まで", text):
        return "Tối đa " + match[1] + " ngày"
    if match := re.fullmatch(r"(\d+)円", text):
        return match[1] + " yên"
    if "@" in text or text.startswith(("https://", "http://")) or re.fullmatch(r"[\d\s:~\-]+", text):
        return value
    return None


def joined_vi(rows):
    return "\n".join(row["vi"] for row in rows if row["vi"])


def source_times(player):
    if not player:
        return None
    full = interval(player)
    if full:
        return full
    if not (player.attrs.get("data-end") or "").strip():
        try:
            value = Decimal(player.attrs["data-start"])
            if value.is_finite() and value >= 0:
                return [round(1000 * value), None]
        except (KeyError, InvalidOperation):
            pass
    return None


class Package:
    def __init__(self, level, period, output, revision, layout=None):
        self.level, self.period, self.output = level, period, output
        self.revision, self.layout = revision, layout
        self.written_sections = {}
        self.namespace = uuid5(NAMESPACE_URL, f"urn:harumi-pilot:vnjpclub:{level}:{period}")
        self.assets = {}
        self.sources = []
        self.content = {section: {"mondais": []} for section in SECTIONS}
        self.annotations = dict(nodes=[], answers=[], fields=[], audioSegments=[], grammarRefs=[], sentencePairs={})
        self.issues = []
        self.master = None
        self.source = None
        self.translations = {}
        self.expected = {}
        self.shared = {}
        self.editorial = {}
        self.editorial_hash = None
        self.editorial_passages = {}
        self.question_translations = {}
        self.handled_images = set()
        self.sentence_edits = {}
        self.written_only = False

    def uid(self, key):
        return str(uuid5(self.namespace, key))

    def node(self, key, locator, number=None, labels=None):
        uid = self.uid(key)
        self.annotations["nodes"].append(dict(nodeId=uid, sourceId=self.source, locator=locator,
                                              sourceNumber=number, sourceChoiceLabels=labels or []))
        return uid

    def issue(self, code, message, target=None, severity="warning"):
        self.issues.append(dict(code=code, targetId=target, severity=severity, message=message))

    def asset(self, raw, ext, media_type, locator, duration=None):
        checksum = digest(raw)
        path = f"assets/sha256/{checksum[:2]}/{checksum}.{ext}"
        write_exact(self.output / path, raw)
        item = self.assets.setdefault(checksum, dict(assetId="sha256:" + checksum, path=path,
            sha256=checksum, mediaType=media_type, byteLength=len(raw), durationMs=duration,
            width=None, height=None, origins=[], derivedFromAssetId=None, transform=None))
        item["origins"].append(dict(sourceId=self.source, locator=locator))
        return checksum

    def prepare_master(self, doc, page):
        duration_node = first(doc, "vnjp-jlpt-choukai-time-duration")
        duration = None
        if duration_node and re.fullmatch(r"\d+:\d{2}", duration_node.text()):
            mins, secs = map(int, duration_node.text().split(":"))
            duration = (mins * 60 + secs) * 1000
        self.master = dict(assetId=None, durationMs=duration, rss=None)
        name = f"JLPT-{self.level}-{self.period}"
        types = {".mp3":"audio/mpeg", ".m4a":"audio/mp4", ".ogg":"audio/ogg", ".wav":"audio/wav"}
        matching = [p for p in page["masterAudioCandidates"]
                    if Path(p).stem.casefold() == name.casefold() and Path(p).suffix.lower() in types]
        adjacent = [p for p in matching if Path(p).parent == Path(page["path"]).parent]
        candidates = adjacent or matching
        local = candidates[0] if len(candidates) == 1 else None
        if not local:
            if matching:
                self.issue("AMBIGUOUS_MASTER", f"Nhiều bản {name}. Cần xác định MP3 đúng với HTML nghe.", severity="error")
                return
            self.issue("MISSING_MASTER", "Cần MP3 tổng hoặc binding RSS khớp bản thu của đề.", severity="error")
            return
        raw = (ROOT / local).read_bytes()
        seconds = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=nw=1:nk=1", str(ROOT / local)], text=True).strip()
        measured = int(round(Decimal(seconds) * 1000))
        if duration and abs(duration - measured) >= 1000:
            raise ValueError(f"Master duration differs from capture: {local}")
        self.sources.append(source_record("master", local, raw))
        self.source = "master"
        ext = Path(local).suffix.lower()
        checksum = self.asset(raw, ext[1:], types[ext], local, measured)
        self.master.update(assetId="sha256:" + checksum, durationMs=measured)
        self.source = "listening"
        self.issue("CHECK_MASTER_ALIGNMENT", "Đã đối chiếu tên kỳ và thời lượng. Cần nghe đối chiếu mốc đầu, giữa, cuối trước phát hành.")

    def map_written(self, doc, page):
        sidecar = Path(page["path"]).parent / "written-layout.json"
        path = self.layout or (ROOT / sidecar)
        if self.layout and not path.is_file():
            raise ValueError(f"Layout file does not exist: {path}")
        if path.is_file():
            profile = json.loads(path.read_bytes())
        else:
            profiles = json.loads((ROOT / "tools/written-layouts.json").read_bytes())
            profile = profiles.get(f"{self.level}/{self.period}")
        if not profile or profile.get("captureSha256") != page["sha256"]:
            raise ValueError(f"Written layout needs review. Run --inspect-layout, then supply {sidecar} "
                             "with captureSha256 and sectionStarts.")
        if evidence := profile.get("writtenOnlyEvidence"):
            path = (ROOT / evidence["path"]).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file():
                raise ValueError("Missing local evidence for written-only scope")
            raw = path.read_bytes()
            if digest(raw) != evidence["sha256"]:
                raise ValueError("Changed evidence for written-only scope")
            self.sources.append(source_record("written-only-scope", path.relative_to(ROOT).as_posix(), raw))
            self.written_only = True
        starts = profile["sectionStarts"]
        if set(starts) != set(SECTIONS[:3]) or len(set(starts.values())) != 3:
            raise ValueError("Written sectionStarts must identify three distinct source question IDs.")
        by_anchor = {anchor: section for section, anchor in starts.items()}
        section, seen = None, []
        for block in doc.find("mondai-block"):
            questions = block.find("q-item")
            if not questions:
                continue
            anchor = questions[0].attrs["id"]
            if anchor in by_anchor:
                if not first(block, "mondai-title"):
                    raise ValueError(f"Section boundary at {anchor} has no source mondai title")
                section = by_anchor[anchor]
                seen.append(section)
            if section is None:
                raise ValueError(f"Written layout omits first question {anchor}")
            self.written_sections[anchor] = section
        if seen != SECTIONS[:3]:
            raise ValueError("Written section anchors are missing, out of order, or inside a question group.")

    def passage(self, block, original, locator):
        jp = tidy(ja(original))
        if not jp:
            return
        media_id = self.node(f"{block['id']}/passage/{len(block['mediaItems'])}", locator)
        if media_id in self.editorial_passages:
            rows = self.editorial_passages.pop(media_id)
            # Ignore only layout-only Markdown separators and whitespace during coverage checks.
            normalized = lambda text: re.sub(r"\s+", "", re.sub(r"(?m)^\|(?:\s*:?-+:?\s*\|)+\s*$", "", text))
            if normalized(jp) != normalized("\n".join(r["ja"] for r in rows)):
                raise ValueError(f"Stale Japanese passage in editorial translation: {media_id}")
            self.annotations["fields"].append(dict(targetId=media_id, fieldPointer="/passage/viMd",
                origin="ai", sourceId="editorial-passages", runId=f"{self.level}-{self.period}-passages",
                model="Codex", skillVersion="jlpt-exam-ingest-1.3", inputSha256=self.capture_hash,
                reviewStatus="pending", note=locator))
        else:
            rows = aligned_rows(original, self.translations)
        rows = self.edit_pairs(media_id, rows, "/passage/viMd", locator)
        self.annotations["sentencePairs"][media_id] = rows
        block["mediaItems"].append(dict(id=media_id, kind="passage", passage=dict(
            jaMd=jp, viMd=joined_vi(rows))))

    def edit_pairs(self, owner, rows, field, locator):
        edits = self.sentence_edits.pop(owner, None)
        if edits is None:
            return rows
        result = []
        edits = dict(edits)
        for idx, row in enumerate(rows, 1):
            entry = edits.pop(str(idx), None)
            if entry is None:
                result.append(row)
                continue
            units = entry.get("ja") or sentence_units(row["ja"])
            values = entry["vi"]
            if (not isinstance(units, list) or not isinstance(values, list) or len(units) != len(values)
                    or not units or not all(isinstance(v, str) and v.strip() for v in units + values)
                    or re.sub(r"\s", "", "".join(units)) != re.sub(r"\s", "", row["ja"])):
                raise ValueError(f"Invalid JA/VI sentence edit {owner} row {idx}")
            result.extend(dict(ja=ja, vi=vi) for ja,vi in zip(units, values))
        if edits:
            raise ValueError(f"Unknown source row(s) for {owner}: {sorted(edits)}")
        self.annotations["fields"].append(dict(targetId=owner, fieldPointer=field, origin="ai",
            sourceId=f"sentence-edits-{self.source}", runId=f"sentence-edits-{self.level}-{self.period}-{self.source}",
            model="Codex", skillVersion="jlpt-exam-ingest-1.3", inputSha256=self.capture_hash,
            reviewStatus="pending", note=locator))
        return result

    def question(self, original):
        anchor = original.attrs["id"]
        key = f"{self.source}/{anchor}"
        selector = "#" + anchor
        prompt = first(original, "vnjp-quiz-q")
        choices = []
        for i, ch in enumerate(original.find("choice")):
            text = first(ch, "choice-text")
            if text is None:
                raise ValueError(f"Missing choice DOM: {self.source} {selector}")
            choice = dict(id=chr(97+i), text=tidy(ja(text)))
            vi = translations(text, self.translations)
            if vi:
                choice["textVi"] = vi
            choices.append(choice)
        labels = [dict(choiceId=c["id"], label=str(i+1)) for i,c in enumerate(choices)]
        uid = self.node(key, selector, first(original, "q-no").text(), labels)
        qprompt = {"text": tidy(ja(prompt))}
        vi = translations(prompt, self.translations)
        # In N2 July 2018 SingleFile preserved the Japanese Excel table but stripped
        # its per-cell DOM anchors. Reattach the appendix only on exact same-question text.
        if prompt:
            for table in (n for n in prompt.walk() if n.tag == "table" and not n.find("vnjp-jlpt-tudich")):
                cells = [n for n in table.walk() if n.tag in ("th", "td")]
                lookup = {c: self.translations.get((anchor, tidy(ja(c))), set()) for c in cells}
                if cells and all(len(v) == 1 for v in lookup.values()):
                    vi = tidy(vi + "\n" + markdown_table(table, lambda c: next(iter(lookup[c]))))
        if vi:
            qprompt["textVi"] = vi
        marked = [c["id"] for c,ch in zip(choices,original.find("choice")) if "choice-correct" in ch.classes]
        graded = [int(m[1]) for line in original.find("result-line") for m in ANSWER.finditer(line.text())]
        ans = marked[0] if len(marked)==1 and graded==[ord(marked[0])-96] else None
        self.annotations["answers"].append(dict(questionId=uid, sourceChoiceId=ans,
            aiChoiceId=None, resolvedChoiceId=ans, resolution="source_confirmed" if ans else "unresolved",
            sourceId=self.source, note=f"{selector} .choice-correct / .result-line"))
        if not ans:
            self.issue("VERIFY_KEY", f"{self.source} {selector} · Cần đối chiếu đáp án.", uid, "error")
        exp = first(original, "complete-answer")
        explanation = tidy(exp.text()) if exp else ""
        q = dict(id=uid, prompt=qprompt, choices=choices, correctChoiceId=ans,
                 explanation=explanation or None, translationVi=vi or None,
                 vocabNotes=None, grammarNotes=None)
        if anchor in self.question_translations:
            edit = self.question_translations.pop(anchor)
            changed = []
            if text := edit.get("prompt"):
                if not qprompt["text"]:
                    raise ValueError(f"Cannot translate an empty question prompt: {selector}")
                qprompt["textVi"] = q["translationVi"] = text
                changed.append("/prompt/textVi")
            if edit.get("choices"):
                for idx, (choice, text) in enumerate(zip(choices, edit["choices"], strict=True)):
                    choice["textVi"] = text
                    changed.append(f"/choices/{idx}/textVi")
            for pointer in changed:
                self.annotations["fields"].append(dict(targetId=uid, fieldPointer=pointer, origin="ai",
                    sourceId=f"translations-{self.source}", runId=f"{self.level}-{self.period}-{self.source}-questions",
                    model="Codex", skillVersion="jlpt-exam-ingest-1.3", inputSha256=self.capture_hash,
                    reviewStatus="pending", note=selector))
        if anchor in self.editorial:
            edit = self.editorial.pop(anchor)
            if ans != chr(96 + edit["key"]) or not edit["explanation"].strip():
                raise ValueError(f"Unverified editorial patch: {selector}")
            q["explanation"] = edit["explanation"].strip()
            if edit.get("sourceIssue"):
                self.issue("VERIFY_SOURCE_TEXT", f"{self.source} {selector} · {edit['sourceIssue']}", uid, "error")
            self.annotations["fields"].append(dict(targetId=uid, fieldPointer="/explanation",
                origin="ai", sourceId=f"editorial-{self.source}", runId=f"{self.level}-{self.period}-{self.source}",
                model="Codex", skillVersion="jlpt-exam-ingest-1.3", inputSha256=self.capture_hash,
                reviewStatus="pending", note=f"{selector}; source bytes {self.capture_hash}; patch SHA-256 {self.editorial_hash}."))
        elif explanation:
            self.annotations["fields"].append(dict(targetId=uid, fieldPointer="/explanation",
                origin="source", sourceId=self.source, runId=None, model=None, skillVersion=None,
                inputSha256=None, reviewStatus="pending", note=selector + " .complete-answer"))
        else:
            self.issue("EXPLANATION_TO_AUTHOR", f"{self.source} {selector} · AI cần soạn lời giải khi đủ căn cứ.", uid)
        images = [img for n in original.find("vnjp-q-image") for img in n.walk() if img.tag == "img"]
        if len(images) > 1:
            raise ValueError(f"Multiple question images: {selector}")
        if images:
            self.handled_images.add(images[0])
            header, _, payload = images[0].attrs.get("src", "").partition(",")
            media = {"data:image/jpeg;base64": ("jpg", "image/jpeg"),
                     "data:image/png;base64": ("png", "image/png"),
                     "data:image/webp;base64": ("webp", "image/webp")}.get(header)
            if not media or not payload:
                raise ValueError(f"Missing or unsupported embedded question image: {self.source} {selector}")
            checksum = self.asset(base64.b64decode(payload, validate=True), *media, selector+" img")
            q["imageUrl"] = "asset://" + checksum
        return q

    def read_blocks(self, doc):
        current = None
        processed = []
        grouped = {}
        for idx, element in enumerate(doc.find("mondai-block"), 1):
            loc = f"(.mondai-block)[{idx}]"
            original_qs = element.find("q-item")
            if not original_qs:
                extra = first(element, "vnjp-dokkai-thongtindich")
                if extra is None or current is None:
                    raise ValueError(f"Unassociated source block at {loc}")
                self.passage(current["blocks"][-1], extra, loc+" .vnjp-dokkai-thongtindich")
                continue
            heading = first(element, "mondai-title")
            if heading:
                number = int(re.search(r"問題\s*(\d+)", heading.text())[1])
                section = "choukai" if self.source == "listening" else self.written_sections[original_qs[0].attrs["id"]]
                key = (section, number)
                current = grouped.get(key)
                if not current:
                    label = re.split(r"\s*[−-]\s*[(（]", heading.text())[0]
                    current = dict(id=self.node(f"{section}/m{number}", loc, heading.text()),
                        section=section, mondaiNumber=number, label=label,
                        instruction=tidy(ja(first(element, "tieude"))), blocks=[])
                    self.content[section]["mondais"].append(current)
                    grouped[key] = current
                if section == "choukai" and (player := first(element, "vnjp-choukai-mondai-player")):
                    if marks := source_times(player):
                        self.annotations["audioSegments"].append(dict(mondaiId=current["id"],
                            questionIds=[], startMs=marks[0], endMs=marks[1], role="mondai",
                            sourceId=self.source, locator=loc+" .vnjp-choukai-mondai-player[data-start]"))
            if current is None:
                raise ValueError(f"Unassociated questions at {loc}")
            # Passage groups come from the DOM. Audio blocks follow a single recorded exchange.
            groups = []
            for q in original_qs:
                anchor = q.attrs["id"]
                processed.append(anchor)
                count = len(q.find("choice"))
                if self.source == "listening":
                    group = self.shared.get(anchor, anchor)
                else:
                    group = "written"
                if not groups or groups[-1][:2] != (group,count):
                    groups.append((group,count,[]))
                groups[-1][2].append(q)
            for group,count,nodes in groups:
                owner = nodes[0].attrs["id"]
                block_key = f"{self.source}/block/{owner}"
                block = dict(id=self.node(block_key, loc+" #"+owner), choiceCount=count, mediaItems=[],
                             questions=[self.question(q) for q in nodes])
                current["blocks"].append(block)
                for p in element.find("passage-content"):
                    self.passage(block,p,loc+" .passage-content")
                if self.source == "listening":
                    self.listening(current,block,nodes,group)
        expected = [n.attrs["id"] for n in doc.find("q-item")]
        if processed != expected or len(set(processed)) != len(processed):
            raise ValueError(f"Question identity/order mismatch: {self.source}")
        for idx, block in enumerate(doc.find("mondai-block"), 1):
            for image in block.walk():
                if image.tag == "svg" and "vnjp-choukai-q-player__ico" in image.classes:
                    continue
                if image.tag in {"img", "svg", "canvas", "object", "picture"} and image not in self.handled_images:
                    raise ValueError(f"Unmapped {image.tag}: {self.source} .mondai-block {idx}. Inspect source before export.")

    def listening(self, mondai, block, originals, owner):
        script_owner = next((n for n in originals if n.attrs["id"] == owner), None)
        if script_owner is None:
            raise ValueError("Shared audio group crosses source blocks")
        loc = "#" + owner
        script = first(script_owner, "vnjp-choukai-script-inner")
        targets = [q["id"] for q in block["questions"]]
        if script and tidy(ja(script)):
            rows = aligned_rows(script, self.translations)
            if len(targets) > 1:
                media_id = self.node(block["id"]+"/audio",loc+" .vnjp-choukai-script-inner")
                rows = self.edit_pairs(media_id, rows, "/audio/scriptViMd", loc)
                media = dict(id=media_id, kind="audio", audio=dict(url=None,
                    scriptJaMd=tidy(ja(script)), scriptViMd=joined_vi(rows)))
                block["mediaItems"].append(media)
                self.annotations["sentencePairs"][media["id"]] = rows
            else:
                rows = self.edit_pairs(targets[0], rows, "/jlptListenScript/scriptViMd", loc)
                block["questions"][0]["jlptListenScript"] = dict(scriptJaMd=tidy(ja(script)), scriptViMd=joined_vi(rows))
                self.annotations["sentencePairs"][targets[0]] = rows
        else:
            self.issue("MISSING_SCRIPT", f"{self.level} {self.period}, {mondai['label']}, {loc} · Cần script tiếng Nhật.", targets[0], "error")
        player = first(script_owner, "vnjp-choukai-q-player")
        times = source_times(player)
        if times:
            self.annotations["audioSegments"].append(dict(mondaiId=mondai["id"], questionIds=targets,
                startMs=times[0], endMs=times[1], role="shared" if len(targets)>1 else "question",
                sourceId=self.source,locator=loc+" .vnjp-choukai-q-player[data-start]"))

    def mondai_ranges(self):
        segments = self.annotations["audioSegments"]
        for m in self.content["choukai"]["mondais"]:
            present = [s for s in segments if s["mondaiId"] == m["id"]]
            if any(s["role"] == "mondai" for s in present):
                continue
            intervals = [s for s in present if s["role"] in {"question", "shared"} and s["endMs"] is not None]
            expected = [q["id"] for b in m["blocks"] for q in b["questions"]]
            if not intervals or [q for s in intervals for q in s["questionIds"]] != expected:
                continue
            if any(a["endMs"] > b["startMs"] for a,b in zip(intervals,intervals[1:])):
                self.issue("CHECK_MONDAI_TIMES", "Mốc câu chồng lấn. Rà lại biên luyện mondai.", m["id"])
                continue
            first_cue, last_cue = intervals[0], intervals[-1]
            segments.append(dict(mondaiId=m["id"], questionIds=[], role="mondai",
                startMs=first_cue["startMs"], endMs=last_cue["endMs"], sourceId="listening",
                locator=f"Question span: {first_cue['locator']} to {last_cue['locator']} (intro not measured)"))

    def load_page(self, page):
        self.source = page["section"]
        raw = (ROOT / page["path"]).read_bytes()
        if digest(raw) != page["sha256"] or page.get("issue"):
            raise ValueError("Refresh/review audit for " + page["path"])
        self.sources.append(source_record(self.source,page["path"],raw))
        self.capture_hash = digest(raw)
        overlay = Path(page["path"]).parent / f"editorial-sentence-rows-{self.source}.vi.json"
        if (ROOT / overlay).is_file():
            patch = (ROOT / overlay).read_bytes()
            data = json.loads(patch)
            if data["captureSha256"] != self.capture_hash:
                raise ValueError(f"Source changed since sentence edit: {overlay}")
            self.sentence_edits = dict(data["edits"])
            self.sources.append(source_record(f"sentence-edits-{self.source}",overlay.as_posix(),patch))
        overlay = Path(page["path"]).parent / f"editorial-questions-{self.source}.vi.json"
        if (ROOT / overlay).is_file():
            patch = (ROOT / overlay).read_bytes()
            data = json.loads(patch)
            if data["captureSha256"] != self.capture_hash:
                raise ValueError(f"Question source changed since translation: {overlay}")
            self.question_translations = dict(data["questions"])
            self.sources.append(source_record(f"translations-{self.source}", overlay.as_posix(), patch))
        overlay = Path(page["path"]).parent / "editorial-passages.vi.json"
        if self.source == "written" and (ROOT / overlay).is_file():
            patch = (ROOT / overlay).read_bytes()
            data = json.loads(patch)
            if data["captureSha256"] != self.capture_hash:
                raise ValueError(f"Passage source changed since translation: {overlay}")
            self.editorial_passages = dict(data["passages"])
            self.sources.append(source_record("editorial-passages", overlay.as_posix(), patch))
        overlay = Path(page["path"]).parent / f"editorial-{self.source}.vi.json"
        if (ROOT / overlay).is_file():
            patch = (ROOT / overlay).read_bytes()
            data = json.loads(patch)
            if data["captureSha256"] != self.capture_hash:
                raise ValueError(f"Source changed since explanation review: {overlay}")
            self.editorial_hash = digest(patch)
            self.editorial = dict(data["questions"])
            self.sources.append(source_record(f"editorial-{self.source}",overlay.as_posix(),patch))
        parser = SingleFileDocument()
        parser.feed(raw.decode("utf-8-sig"))
        parser.close()
        self.translations = translation_index(parser.root)
        self.shared = {q:g["scriptOwner"] for g in page.get("sharedScripts",[]) for q in g["questions"]}
        if self.source == "listening":
            self.prepare_master(parser.root,page)
        else:
            self.map_written(parser.root, page)
        self.read_blocks(parser.root)
        if (self.level, self.period, self.source) == ("N1", "2018-12", "written"):
            q46 = self.uid("written/q-46")
            self.issue("VERIFY_PASSAGE_START", "Bài đọc của #q-46 mở đầu bằng 人間だとすれば; đối chiếu bản gốc xem có thiếu phần mở đầu.", q46)
        unknown = self.editorial.keys() | self.editorial_passages.keys() | self.question_translations.keys() | self.sentence_edits.keys()
        if unknown:
            raise ValueError(f"Unknown editorial targets: {sorted(unknown)}")
        self.expected[self.source] = page["questionCount"]

    def finish(self):
        year, month = map(int,self.period.split("-"))
        self.mondai_ranges()
        if self.written_only and "listening" in self.expected:
            raise ValueError("Listening capture found for edition marked written-only. Review its scope evidence.")
        for source in ("written", "listening"):
            if source not in self.expected and not (source == "listening" and self.written_only):
                self.issue("MISSING_" + source.upper(), f"Thiếu nguồn {source} cho {self.level} {self.period}.", severity="error")
        self.issue("EDITORIAL_REVIEW", "Rà nghĩa, lời giải, ghi chú ngữ pháp và các bảng so với HTML trước phát hành.")
        expectations = [dict(mondaiId=m["id"], questionCount=sum(len(b["questions"]) for b in m["blocks"]))
                        for paper in self.content.values() for m in paper["mondais"]]
        if sum(e["questionCount"] for e in expectations) != sum(self.expected.values()):
            raise ValueError("Coverage mismatch")
        package = dict(schemaVersion="1.3.0", packageId=str(self.namespace),revision=self.revision,
                       exam=dict(level=self.level,slug=f"{year:04d}/{month:02d}",
                                 name=f"JLPT {self.level} · {month:02d}/{year}",kind="practice",year=year,month=month),
                       structure=dict(profileKey=f"vnjpclub-{self.level.lower()}-{self.period}",
                                      description="Thứ tự và số mondai từ các bản SingleFile đang có.",
                                      sectionOrder=SECTIONS,timings=[],expectations=expectations),
                       sources=self.sources, assets=list(self.assets.values()),content=self.content,
                       annotations=self.annotations,masterAudio=self.master,
                       review=dict(status="draft",reviewedBy=None,reviewedAt=None,issues=self.issues))
        self.issues.extend(checklist_issues(package))
        target = self.output / "packages" / self.level / self.period
        write_exact(target / "package.json",(json.dumps(package,indent=2,ensure_ascii=False)+"\n").encode())
        details = [f"# Pilot {self.level} {self.period}", "", "Đã chuyển nguyên dữ liệu có trong nguồn. Trạng thái draft.",
                   "", *(f"- {s['sourceId']} · `{s['localPath']}` · SHA-256 `{s['sha256']}`" for s in self.sources),
                   "", "## Kiểm kê", "", *(f"- {k} · {len(p['mondais'])} mondai, "
                       f"{sum(len(b['questions']) for m in p['mondais'] for b in m['blocks'])} câu."
                       for k,p in self.content.items()), "", f"Mốc audio có bằng chứng: {len(self.annotations['audioSegments'])}.",
                   "", "## Việc còn lại", "", *(f"- {k} · {v}" for k,v in Counter(i["code"] for i in self.issues).items()),
                   "", "Xem `review.issues` trong gói để tìm UUID và locator từng câu. Bước tiếp là rà bài giải, bổ sung script/audio rồi tăng revision; giữ lại ID hiện tại.", ""]
        write_exact(target/"checkpoint.md","\n".join(details).encode())
        return target / "package.json"


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--level", required=True, choices=["N1", "N2", "N3", "N4", "N5"])
    cli.add_argument("--period", required=True, help="YYYY-MM")
    cli.add_argument("--revision", type=int, help="Positive revision to stage")
    cli.add_argument("--layout", type=Path, help="Reviewed written-layout.json bound to the written capture SHA")
    cli.add_argument("--inspect-layout", action="store_true", help="Print written block boundaries and instructions only")
    cli.add_argument("--output-root", type=Path, default=ROOT)
    args = cli.parse_args()
    if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", args.period):
        cli.error("--period must be YYYY-MM")
    if not args.inspect_layout and (args.revision is None or args.revision < 1):
        cli.error("--revision must be a positive integer")
    report = json.loads((ROOT/"reports/source-gaps.json").read_bytes())
    pages = [p for p in report["pages"] if p["level"] == args.level and p["period"] == args.period]
    if not pages or any(p["section"] not in {"listening","written"} for p in pages):
        cli.error("No recognized audited pages for this exam. Inspect the captures and rerun audit_sources.py.")
    if len({p["section"] for p in pages}) != len(pages):
        cli.error("Multiple audited captures for the same section. Resolve active/archive selection first.")
    if args.inspect_layout:
        for page in pages:
            if page["section"] != "written":
                continue
            raw = (ROOT / page["path"]).read_bytes()
            if digest(raw) != page["sha256"]:
                cli.error("Written capture changed since audit")
            print("captureSha256", page["sha256"])
            doc = SingleFileDocument()
            doc.feed(raw.decode("utf-8-sig"))
            doc.close()
            for block in doc.root.find("mondai-block"):
                questions = block.find("q-item")
                if questions:
                    title = first(block, "mondai-title")
                    print(questions[0].attrs["id"], title.text() if title else "-", tidy(ja(first(block,"tieude"))))
        return
    pack = Package(args.level, args.period, args.output_root.resolve(), args.revision, args.layout)
    for page in sorted(pages, key=lambda p:p["section"] != "written"):
        pack.load_page(page)
    print(pack.finish(), flush=True)


if __name__ == "__main__":
    main()
