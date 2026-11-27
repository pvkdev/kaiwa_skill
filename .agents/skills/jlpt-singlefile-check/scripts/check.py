"""Inspect local VNJPCLUB SingleFile snapshots without loading the page."""

import argparse
import base64
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import parse_qs, unquote, urlsplit


VOID = set("area base br col embed hr img input link meta param source track wbr".split())
BLOCKS = set("address article aside blockquote div dl fieldset footer form h1 h2 h3 h4 h5 h6 header hr main nav ol p pre section table ul".split())
UNREAD = {"style", "script", "template", "iframe"}
TOOLTIP = "vnjp-jlpt-kqdich"
SOURCE = "vnjp-jlpt-candich"
PANEL = "vnjp-choukai-q-script-panel"
PARTS = ("moji_bunpo_dokkai", "choukai")
SKIP_SOURCE = {"rt", "rp", "button", "audio"}


@dataclass
class Node:
    tag: str
    attrs: dict
    line: int
    parent: "Node | None" = None
    children: list = field(default_factory=list)

    def has(self, name):
        return name in (self.attrs.get("class") or "").split()

    def inside(self, name):
        node = self
        while node:
            if node.has(name):
                return node
            node = node.parent
        return None

    def find(self, name):
        for child in self.children:
            if isinstance(child, Node):
                if child.has(name):
                    return child
                if match := child.find(name):
                    return match
        return None

    def content(self, source=False):
        if self.tag in UNREAD:
            return ""
        if source and (self.tag in SKIP_SOURCE or self.has(TOOLTIP) or self.has("vnjp-choukai-q-player") or self.attrs.get("role") == "tooltip"):
            return ""
        if self.tag == "br":
            return "\n"
        text = "".join(x.content(source) if isinstance(x, Node) else x for x in self.children)
        return text + "\n" if source and self.tag in {"div", "li", "p"} else text


class Snapshot(HTMLParser):
    def __init__(self, raw):
        super().__init__()
        self.nodes = []
        self.stack = []
        self.feed(raw)
        self.close()

    def close_open(self, tags, boundaries=()):
        for i in range(len(self.stack) - 1, -1, -1):
            tag = self.stack[i].tag
            if tag in tags:
                del self.stack[i:]
                return
            if tag in boundaries:
                return

    def handle_starttag(self, tag, attrs):
        if tag in BLOCKS:
            self.close_open({"p"}, {"table", "td", "th", "template"})
        if tag in {"td", "th", "tr"}:
            self.close_open({"td", "th"}, {"table", "tr"})
        if tag == "tr":
            self.close_open({"tr"}, {"table"})
        if tag == "li":
            self.close_open({"li"}, {"ul", "ol"})
        parent = self.stack[-1] if self.stack else None
        node = Node(tag, dict(attrs), self.getpos()[0], parent)
        self.nodes.append(node)
        if parent:
            parent.children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        self.close_open({tag})

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_data(self, text):
        if self.stack and self.stack[-1].tag not in UNREAD:
            self.stack[-1].children.append(text)


def plain(value):
    return " ".join((value or "").split())


def question_id(node):
    question = node.inside("q-item")
    return question.attrs.get("id") if question else None


def image_source(value):
    if not value:
        return "missing"
    if value.startswith("data:image/"):
        try:
            head, data = value.split(",", 1)
            if not data or ";base64" in head and not base64.b64decode(data, validate=True):
                return "invalid data URI"
            return "embedded"
        except ValueError:
            return "invalid data URI"
    return "blob" if value.startswith("blob:") else "external or relative"


def inspect_html(path):
    raw = path.read_text(encoding="utf-8-sig")
    nodes = Snapshot(raw).nodes
    source = re.search(r"(?m)^\s*url:\s*(\S+)", raw)
    params = parse_qs(urlsplit(source[1]).query) if source else {}
    ids = {}
    id_counts = Counter()
    for node in nodes:
        if ident := node.attrs.get("id"):
            ids.setdefault(ident, node)
            id_counts[ident] += 1
    exam = [node for node in nodes if node.inside("vnjp-jlpt-root")]
    rows = [node for node in exam if node.has("q-item")]
    form = ids.get("vnjp-jlpt-exam-form")
    form_attrs = form.attrs if form else {}
    identity = {
        "level": params.get("vnjp_jlpt_level", [form_attrs.get("data-draft-level")])[0],
        "period": params.get("giaotrinh", [form_attrs.get("data-draft-giaotrinh")])[0],
        "part": params.get("theloai", [form_attrs.get("data-draft-theloai")])[0],
    }
    structure_issues = []
    display_issues = []
    overlay = ids.get("vnjp-devtools-overlay")
    if overlay and "hidden" not in overlay.attrs and not overlay.has("sf-hidden") and not re.search(
        r"display\s*:\s*none\b|visibility\s*:\s*hidden\b", overlay.attrs.get("style") or "", re.I
    ):
        display_issues.append([overlay.line, "saved Developer Tools overlay may obscure the page"])
    body = next((node for node in nodes if node.tag == "body"), None)
    if body and re.search(r"(?:^|;)\s*filter\s*:\s*[^;]*\bblur\(", body.attrs.get("style") or "", re.I):
        display_issues.append([body.line, "saved body has an inline blur filter"])
    for field_name, attr in (("level", "data-draft-level"), ("period", "data-draft-giaotrinh"), ("part", "data-draft-theloai")):
        if form_attrs.get(attr) and form_attrs[attr] != identity[field_name]:
            structure_issues.append(f"{field_name} differs between the saved URL and form")
    if not rows:
        structure_issues.append("no question rows found")
    question_ids = Counter(q.attrs.get("id") for q in rows)
    for qid, count in question_ids.items():
        if not qid or count != 1:
            structure_issues.append(f"missing or duplicated question ID: {qid}")
    grid = [n for n in exam if n.has("vnjp-jlpt-answer-item")]
    if grid and len(grid) != len(rows):
        structure_issues.append(f"answer grid has {len(grid)} entries for {len(rows)} question rows")
    appendix = ids.get("jlpt-singlefile-notes")
    keyed = {}
    if appendix:
        for container in appendix.children:
            if isinstance(container, Node):
                for node in container.children:
                    if isinstance(node, Node) and node.attrs.get("data-key"):
                        key = node.attrs["data-key"]
                        if key in keyed:
                            structure_issues.append(f"duplicate appendix entry at HTML line {node.line}")
                        keyed[key] = node

    def link(node):
        anchor = next((c for c in node.children if isinstance(c, Node) and c.tag == "a"), None)
        href = anchor.attrs.get("href", "") if anchor else ""
        target = unquote(href[1:]) if href.startswith("#") else ""
        return ids.get(target) if id_counts[target] == 1 else None

    marked = {}
    for node in exam:
        if node.tag == "input" and node.attrs.get("type") == "radio" and node.inside("choice-correct"):
            marked.setdefault(question_id(node), []).append(node.attrs.get("value"))
    answer_keys = {}
    answer_details = []
    explanations = {}
    for q in rows:
        qid = q.attrs.get("id")
        choices = marked.get(qid, [])
        if len(choices) != 1 or not choices[0]:
            answer_details.append([qid, "expected exactly one marked correct choice"])
        else:
            answer_keys[qid] = choices[0]
            feedback = q.find("result-line")
            number = re.search(r"Đáp án(?: đúng)?\s*:\s*(\d+)", feedback.content(), re.I) if feedback else None
            if number and number[1] != choices[0]:
                answer_details.append([qid, "marked choice conflicts with answer feedback"])
        answer = q.find("complete-answer")
        if answer and (copy := plain(answer.content())):
            explanations[qid] = copy
    appendix_answers = {key.removeprefix("answer-"): node for key, node in keyed.items() if key.startswith("answer-")}
    explanation_issues = []
    for qid in question_ids:
        if qid not in explanations or qid not in appendix_answers:
            explanation_issues.append([qid, "missing explanation in the question or appendix"])
    for qid in appendix_answers.keys() - explanations.keys():
        explanation_issues.append([qid, "appendix explanation has no source"])

    pairs, pair_issues = Counter(), []
    script_issues = []
    paired_origins = set()
    script_origins = set()
    for key, node in keyed.items():
        if key.startswith("["):
            try:
                group, qid, index, japanese = json.loads(key)
                if not isinstance(group, str) or not isinstance(japanese, str) or not isinstance(index, int):
                    raise ValueError("Unexpected appendix fields")
            except (ValueError, TypeError):
                pair_issues.append([f"HTML line {node.line}", "invalid appendix pair key"])
                continue
            vietnamese = plain(node.attrs.get("data-vi"))
            label = f"{qid or 'phần chung'} · {group} · {index + 1}"
            pairs["script" if group.startswith("Dịch script") else "exam"] += 1
            origin = link(node)
            if not vietnamese:
                pair_issues.append([label, "missing translation"])
            if not origin:
                pair_issues.append([label, "missing origin link"])
                continue
            if id(origin) in paired_origins:
                pair_issues.append([label, "another appendix pair points to the same source"])
            paired_origins.add(id(origin))
            if (qid and qid != question_id(origin)) or plain(origin.content(source=True)) != plain(japanese):
                pair_issues.append([label, "Japanese or question ID differs"])
            wrapper = origin.inside("vnjp-jlpt-tudich")
            tip = wrapper.find(TOOLTIP) if wrapper else origin.find(TOOLTIP)
            known = plain(tip.content()) if tip else plain(origin.attrs.get("title"))
            if not known or vietnamese != known:
                pair_issues.append([label, "translation source unavailable or differs"])
            if plain("Nhật · " + japanese + "\nViệt · " + vietnamese) not in plain(node.content()):
                pair_issues.append([label, "visible appendix pair differs"])
        if key.startswith("script-"):
            origin = link(node)
            body = plain("".join(c for c in node.children if isinstance(c, str)))
            if not origin or not origin.has(PANEL) or not body or body != plain(origin.content(source=True)):
                script_issues.append([key, "missing origin link or transcript differs"])
            elif id(origin) in script_origins:
                script_issues.append([key, "another appendix script points to the same panel"])
            if origin and origin.has(PANEL):
                script_origins.add(id(origin))

    missing_pairs = [[question_id(node), node.line]
                     for node in exam if node.has(SOURCE) and plain(node.content(source=True)) and id(node) not in paired_origins]
    panels = [node for node in exam if node.has(PANEL)]
    toggles = [node for node in exam if node.has("vnjp-choukai-q-script-toggle")]
    script_coverage = []
    for node in toggles:
        group = node.inside("vnjp-choukai-q-script")
        if not group or not group.find(PANEL):
            script_coverage.append([question_id(node), node.line, "script toggle has no panel"])
    for panel in panels:
        if not plain(panel.content(source=True)):
            script_coverage.append([question_id(panel), panel.line, "script panel is empty"])
        if id(panel) not in script_origins:
            script_coverage.append([question_id(panel), panel.line, "script panel is missing from appendix"])
        if not panel.find("vnjp-choukai-q-player"):
            script_coverage.append([question_id(panel), panel.line, "script panel has no audio player"])

    clips = []
    for player in (node for node in exam if node.has("vnjp-choukai-q-player")):
        clips.append({"question": question_id(player), "line": player.line,
                      "start": player.attrs.get("data-start"), "end": player.attrs.get("data-end")})
    audio_rows = [node for key, node in keyed.items() if key.startswith("audio|")]
    audio_notes = "\n".join(node.content() for node in audio_rows if node.attrs["data-key"].startswith("audio|đề|"))
    duration = re.search(r"Thời lượng = ([\d.]+) s", audio_notes)
    refs = re.findall(r"(?m)^(?:src|currentSrc) = (\S+)", audio_notes)
    audio_sources = [(node.attrs.get("src") or "") for node in exam if node.tag in {"audio", "source"}]
    refs.extend(ref for ref in audio_sources if ref and not ref.startswith("data:"))
    clip_issues = []
    end_before = 0
    for clip in clips:
        qid = clip["question"]
        try:
            start, end = float(clip["start"]), float(clip["end"])
            if not math.isfinite(end) or not 0 <= end_before <= start < end or duration and end > float(duration[1]):
                clip_issues.append([qid, "clip timing outside range or overlapping"])
            end_before = end
        except (ValueError, TypeError):
            clip_issues.append([qid, "clip timing missing or invalid"])
        if not any(re.search(r"^Câu " + re.escape((qid or "").removeprefix("q-")) + r"\b", row.content().strip())
                   and f"data-start = {clip['start']}\ndata-end = {clip['end']}" in row.content() for row in audio_rows):
            clip_issues.append([qid, "clip timing missing from appendix"])

    media = Counter(image_source(node.attrs.get("src") or node.attrs.get("href") or node.attrs.get("xlink:href")) for node in exam if node.tag in {"img", "image"})
    status = next((plain(node.content()) for node in nodes if node.attrs.get("role") == "status" and plain(node.content()).startswith(("Đã rà xong", "Đã dừng", "Thu thập bị gián đoạn"))), None)
    summary_issues = [] if (status or "").startswith("Đã rà xong") else ["appendix has no successful completion status"]
    figures = [
        ("Bản dịch", sum(pairs.values()), sum(bool(plain(node.attrs.get("data-vi"))) for key, node in keyed.items() if key.startswith("["))),
        ("Giải thích", len(rows), len(appendix_answers)),
        ("Script", len(toggles), sum(key.startswith("script-") for key in keyed)),
    ]
    for label, total, filled in figures:
        found = re.search(rf"{label}\s+(\d+)/(\d+)", status or "")
        if found and (int(found[1]), int(found[2])) != (filled, total):
            summary_issues.append(f"{label}: saved status differs from the counted data")
    return {
        "file": path.name, **identity, "structure_issues": structure_issues, "summary_issues": summary_issues, "display_issues": display_issues,
        "status": status, "questions": len(rows), "correct": len(answer_keys), "answer_keys": answer_keys,
        "answer_issues": answer_details, "explanation_issues": explanation_issues,
        "explanations": len(explanations), "explanations_in_appendix": sum(key.startswith("answer-") for key in keyed),
        "explanation_mismatches": [qid for qid, value in explanations.items() if (node := keyed.get(f"answer-{qid}")) and plain("".join(c for c in node.children if isinstance(c, str))) != value],
        "translation_slots": sum(node.has(TOOLTIP) for node in exam), "pairs": pairs, "pair_issues": pair_issues, "missing_pairs": missing_pairs,
        "scripts": len(panels), "scripts_with_text": sum(bool(plain(node.content(source=True))) for node in panels),
        "scripts_in_appendix": sum(key.startswith("script-") for key in keyed), "script_issues": script_issues,
        "script_toggles": len(toggles), "script_coverage": script_coverage,
        "questions_without_panel": [q.attrs.get("id") for q in rows if (panels or identity["part"] == "choukai") and not q.find(PANEL)],
        "clips": clips, "clip_issues": clip_issues, "audio_notes": len(audio_rows),
        "audio_duration_seconds": float(duration[1]) if duration else None, "audio_sources": sorted(set(refs)),
        "audio_embedded": any(ref.startswith("data:audio/") for ref in audio_sources),
        "image_sources": media, "tables": sum(node.tag == "table" for node in exam),
        "toggles": {name: ids[f"vnjp-jlpt-toggle-{name}"].attrs.get("aria-pressed") for name in ("dich", "giaithich") if f"vnjp-jlpt-toggle-{name}" in ids},
    }


def inspect_audio(path, decode):
    data = {"file": path.name, "bytes": path.stat().st_size}
    if shutil.which("ffprobe"):
        result = subprocess.run(["ffprobe", "-v", "error", "-protocol_whitelist", "file,pipe", "-select_streams", "a:0", "-show_entries",
                                 "format=duration:stream=codec_name", "-of", "json", str(path)],
                                capture_output=True, text=True, errors="replace")
        data["probe"] = json.loads(result.stdout) if result.returncode == 0 else {"error": result.stderr.strip()}
    if decode and shutil.which("ffmpeg"):
        result = subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-xerror", "-protocol_whitelist", "file,pipe", "-i", str(path),
                                 "-map", "0:a:0", "-f", "null", "-"], capture_output=True, text=True, errors="replace")
        data["decode"] = "passed" if result.returncode == 0 else result.stderr.strip()
    return data


def html_reports(folder):
    return [inspect_html(path) for path in sorted(folder.iterdir()) if path.is_file() and path.suffix.lower() in {".htm", ".html"}]


def inspect_package(folder, reports, audio, expected_parts, baseline=None):
    findings = []
    volume = re.match(r"^(\d{2})(0[1-9]|1[0-2])(?:_\d+)?$", folder.name)
    period = f"20{volume[1]}-{volume[2]}" if volume else None
    level = next((parent.name.lower() for parent in folder.parents if re.fullmatch(r"n[1-5]", parent.name, re.I)), None)
    for part in expected_parts:
        copies = [item for item in reports if item["part"] == part and (not level or item["level"] == level) and (not period or item["period"] == period)]
        if not copies:
            findings.append(f"missing HTML for {part}")
        elif len(copies) > 1:
            findings.append(f"multiple HTML files for {part}; identify the intended copy")
    for item in reports:
        if item["part"] not in PARTS or level and item["level"] != level or period and item["period"] != period:
            findings.append(f"{item['file']}: unknown or unexpected exam identity")
        prior = next((old for old in (baseline or ()) if all(item[key] == old[key] for key in ("level", "period", "part"))), None)
        if baseline is not None and prior is None:
            findings.append(f"{item['file']}: no baseline file matched this exam and part")
        if prior:
            if item["questions"] != prior["questions"] or item["answer_keys"] != prior["answer_keys"]:
                findings.append(f"{item['file']}: question count or answer key differs from baseline {prior['file']}")
            if prior["scripts_with_text"] > item["scripts_with_text"] or sum(prior["pairs"].values()) > sum(item["pairs"].values()):
                findings.append(f"{item['file']}: script or translation count fell compared with baseline {prior['file']}")
        if item["part"] != "choukai" or item["audio_embedded"]:
            continue
        source_names = {Path(urlsplit(ref).path).stem.casefold() for ref in item["audio_sources"] if not ref.startswith(("[", "blob:"))}
        names = source_names | {name.casefold() for name in (item["period"], f"JLPT-{item['level']}-{item['period']}") if item["period"]}
        candidates = [file for file in audio if Path(file["file"]).stem.casefold() in names]
        if not candidates:
            findings.append(f"{item['file']}: matching offline audio file not found")
            continue
        if len(candidates) > 1:
            findings.append(f"{item['file']}: multiple matching audio files")
        expected = item["audio_duration_seconds"]
        for file in candidates:
            minimum = []
            for clip in item["clips"]:
                try:
                    minimum.append(float(clip["end"]))
                except (ValueError, TypeError):
                    pass
            seconds = file.get("probe", {}).get("format", {}).get("duration")
            if seconds is None:
                findings.append(f"{file['file']}: audio duration could not be verified")
            elif (expected and abs(float(seconds) - expected) > 1) or (minimum and float(seconds) < max(minimum)):
                findings.append(f"{file['file']}: audio duration does not match the HTML or clip bounds")
            if file.get("decode") not in (None, "passed"):
                findings.append(f"{file['file']}: audio failed to decode")
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--decode-audio", action="store_true")
    parser.add_argument("--part", choices=PARTS, action="append", help="Expected part when auditing only one section")
    parser.add_argument("--baseline", type=Path, help="Directory with an earlier save of this exam")
    args = parser.parse_args()
    if not args.folder.is_dir():
        parser.error(f"folder not found: {args.folder}")
    files = sorted(args.folder.iterdir())
    if args.baseline and not args.baseline.is_dir():
        parser.error(f"baseline folder not found: {args.baseline}")
    reports = html_reports(args.folder)
    audio = [inspect_audio(p, args.decode_audio) for p in files if p.is_file() and p.suffix.lower() in {".mp3", ".m4a", ".wav", ".ogg", ".aac"}]
    previous = html_reports(args.baseline) if args.baseline else None
    findings = inspect_package(args.folder.resolve(), reports, audio, args.part or PARTS, previous)
    print(json.dumps({"html": reports, "audio": audio, "package_issues": findings}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
