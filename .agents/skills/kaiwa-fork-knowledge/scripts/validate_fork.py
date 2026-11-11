#!/usr/bin/env python3
"""Read-only structural checks for a forked kaiwa knowledge book.

This cannot verify the PDF image, transcription, translation, or editorial choices.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


ANCHOR = re.compile(r'<a\s+id=["\']([^"\']+)["\']\s*></a>', re.I)
UNIT_ID = re.compile(r'u-[a-z0-9]+(?:-[a-z0-9]+)*')
RAW_PAGE = re.compile(r'p(\d{4})')
SHA256 = re.compile(r'[0-9a-f]{64}')
PAIR = re.compile(r'^\s*(?:(?:[-+*]|\d+[.)])\s+)?(?:[（(][\s\u3000]*[）)]\s+)?\*\*([^*\n]+?):\*\*\s*(.*?)\s*$')
PAIR_ROLE = re.compile(r'^(.+?)\s+\((JP|VI)(?:,\s*[^)]+)?\)$')
EXERCISE_BLANK = re.compile(r'_{3,}|＿{2,}|[（(][\s\u3000]*[）)]')
REMAINS = [
    (re.compile(r'<\s*/?\s*(?:ruby|rt|rp)\b', re.I), 'ruby/furigana HTML'),
    (re.compile(r'(?im)^\s*(?:furigana\s*\(nguồn\)|furigana\s*:|ふりがな\s*[:：])'), 'furigana marker'),
    (re.compile(r'!\[[^\]]*\]\([^)]*\)|<\s*img\b', re.I), 'image embed'),
    (re.compile(r'(?im)^\s*(?:mô tả hình|ảnh minh họa|hình minh họa|chỉ dẫn ảnh|image description)\s*[:：]'), 'image instruction'),
    (re.compile(r'(?im)^\s*(?:hình|sơ đồ|nhấn mạnh nguồn|tiếng anh|tiếng trung)\s*\(biên tập\)\s*[:：]'), 'raw editorial marker'),
    (re.compile(r'(?im)^\s*#{1,6}\s+panel\s+(?:trái|phải)\b'), 'raw panel heading'),
    (re.compile(r'(?im)^\s*(?:trang in|đường dẫn nội dung|chân trang|chữ nền của bản PDF|chữ ở lề dưới)\s*[:：]'), 'raw page scaffold'),
    (re.compile(r'(?im)^\s*#{1,6}\s+.*\bPDF\s+p\d{4}\b|<a\s+id=["\']p\d{4}(?:-b\d{3})?["\']', re.I), 'raw page anchor/header'),
    (re.compile(r'\bp\d{4}-b\d{3}\b'), 'raw block id in prose'),
]
LANGUAGE_HINTS = [
    (re.compile(r'(?im)^\s*(?:Chinese|English|中文|中国語|英語|拼音|Pinyin)\s*[:：]'), 'possible extra language'),
    (re.compile(r'(?m)^\s*[A-Za-z][A-Za-z ,;:.!?()\'"-]{45,}\s*$'), 'possible English prose'),
]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, message: str) -> None:
        self.errors.append(f'ERROR {where}: {message}')

    def warn(self, where: str, message: str) -> None:
        self.warnings.append(f'WARN  {where}: {message}')

    def show(self) -> int:
        for item in self.errors + self.warnings:
            print(item)
        print(f'Validation: {len(self.errors)} error(s), {len(self.warnings)} warning(s)')
        return 1 if self.errors else 0


def read_text(path: Path, report: Report, label: str) -> str | None:
    if not path.is_file():
        report.error(label, f'missing file: {path}')
        return None
    try:
        return path.read_text(encoding='utf-8-sig')
    except (OSError, UnicodeError) as exc:
        report.error(label, f'cannot read UTF-8: {exc}')
        return None


def parse_json(path: Path, report: Report, label: str) -> dict | None:
    content = read_text(path, report, label)
    if content is None:
        return None
    try:
        data = json.loads(content)
    except json.JSONDecodeError as exc:
        report.error(label, f'invalid JSON: {exc}')
        return None
    if not isinstance(data, dict):
        report.error(label, 'expected JSON object')
        return None
    return data


def relative_file(root: Path, value: object, report: Report, label: str) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        report.error(label, 'expected nonempty relative path')
        return None
    raw = Path(value)
    if raw.is_absolute():
        report.error(label, 'path must be relative')
        return None
    resolved = (root / raw).resolve()
    if not resolved.is_relative_to(root.resolve()):
        report.error(label, 'path escapes its declared root')
        return None
    if not resolved.is_file():
        report.error(label, f'missing file: {resolved}')
        return None
    return resolved


def source_file(manifest: dict, key: str, repo: Path, report: Report) -> tuple[Path | None, str | None]:
    value = manifest.get(key)
    if not isinstance(value, dict):
        report.error(key, 'expected {path, sha256}')
        return None, None
    path = relative_file(repo, value.get('path'), report, f'{key}.path')
    digest = value.get('sha256')
    if not isinstance(digest, str) or not SHA256.fullmatch(digest):
        report.error(f'{key}.sha256', 'expected lowercase 64-character SHA-256')
        return path, None
    if path:
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            report.error(key, f'source hash changed: recorded {digest}, actual {actual}')
    return path, digest


def page_scope(value: object, report: Report) -> set[int]:
    if not isinstance(value, list) or not value or any(type(x) is not int or x < 1 for x in value):
        report.error('scope.pdf_pages', 'expected nonempty list of positive 1-based PDF page numbers')
        return set()
    if len(set(value)) != len(value):
        report.error('scope.pdf_pages', 'duplicate page number')
    if value != sorted(value):
        report.error('scope.pdf_pages', 'pages must be ascending')
    return set(value)


def check_build(book: Path, manifest: dict, chapters: list[str], report: Report) -> None:
    build = manifest.get('build')
    if not isinstance(build, dict):
        report.error('_meta/book.json', 'missing build hashes; run build_fork.py after editing chapters/units')
        return
    chapter_hashes = build.get('chapter_sha256')
    if not isinstance(chapter_hashes, dict) or set(chapter_hashes) != set(chapters):
        report.error('build.chapter_sha256', 'must contain exactly the manifest chapters')
    else:
        for chapter in chapters:
            check_digest(book / chapter, chapter_hashes[chapter], report, f'build.chapter_sha256[{chapter}]')
    check_digest(book / '_meta/units.jsonl', build.get('units_sha256'), report, 'build.units_sha256')
    check_digest(book / 'book.md', build.get('book_sha256'), report, 'build.book_sha256')
    check_digest(book / '_meta/search.jsonl', build.get('search_sha256'), report, 'build.search_sha256')
    units_path = book / '_meta/units.jsonl'
    if units_path.is_file():
        count = sum(bool(line.strip()) for line in units_path.read_text(encoding='utf-8-sig').splitlines())
        if build.get('unit_count') != count:
            report.error('build.unit_count', f'expected {count}, got {build.get("unit_count")!r}')


def check_digest(path: Path, expected: object, report: Report, label: str) -> None:
    if not isinstance(expected, str) or not SHA256.fullmatch(expected):
        report.error(label, 'expected lowercase SHA-256')
    elif path.is_file() and hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        report.error(label, f'stale build hash for {path}')
    elif not path.is_file():
        report.error(label, f'missing file: {path}')


def pair_label(label: str) -> tuple[str, str | None] | None:
    if label in ('JP', 'VI'):
        return label, None
    match = PAIR_ROLE.fullmatch(label)
    if not match:
        return None
    return match[2], match[1].strip()


def labels_correspond(japanese: str, vietnamese: str) -> bool:
    """Check adjacent language tags, without pretending to translate role names.

    A Japanese role can be translated or romanized in its Vietnamese turn.
    Semantic role identity still needs review; ASCII A/B mismatches stay errors.
    """
    source, target = pair_label(japanese), pair_label(vietnamese)
    if source is None or target is None or source[0] != 'JP' or target[0] != 'VI':
        return False
    def role(label: str) -> str:
        label = re.sub(r'^(?:例\s*)?[0-9０-９]+\s+', '', label).strip()
        return re.sub(r'\s+in sẵn$', '', label, flags=re.I).strip()
    if source[1] is None:
        return target[1] is None
    if target[1] is None:
        # A descriptive JP header can use a plain VI gloss; an A/B dialogue
        # turn still needs a role-bearing translation to check the speaker.
        return not re.fullmatch(r'[A-ZＡ-Ｚ](?:[0-9０-９₀-₉]+)?', role(source[1]))
    source_role, target_role = role(source[1]), role(target[1])
    if not source_role or not target_role:
        return False
    if source_role == target_role:
        return True
    japanese_script = r'[\u3040-\u30ff\u3400-\u9fff]'
    return bool(re.search(japanese_script, source_role) and
                not re.search(japanese_script, target_role) and
                re.search(r'[^\W\d_]', target_role, re.UNICODE))


def pair_boundary(line: str) -> bool:
    stripped = line.lstrip()
    return bool(re.match(r'#{1,6}\s|<a\s+id=|<!--\s*unit_id:', stripped, re.I))


def pair_marker(line: str) -> tuple[str, str] | None:
    match = PAIR.match(line)
    if match and pair_label(match[1]) is not None:
        return match[1], match[2]
    return None


def language_lines(lines: list[str]) -> tuple[list[str], list[int]]:
    """Tokenize explicit inline labels without changing the book or line refs."""
    expanded: list[str] = []
    source_lines: list[int] = []
    inline = re.compile(r'\*\*([^*\n]+?):\*\*')
    for number, line in enumerate(lines, 1):
        matches = [] if line.lstrip().startswith('|') else [
            match for match in inline.finditer(line) if pair_label(match[1]) is not None]
        if not matches or (len(matches) == 1 and pair_marker(line) is not None):
            expanded.append(line)
            source_lines.append(number)
            continue
        prefix = line[:matches[0].start()]
        if prefix.strip():
            expanded.append(prefix)
            source_lines.append(number)
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(line)
            expanded.append(line[match.start():end].strip())
            source_lines.append(number)
    return expanded, source_lines


def block_content(value: str, continuation: list[str]) -> str:
    parts = [value]
    inline = bool(value.strip())
    continuing = False
    for line in continuation:
        stripped = line.strip()
        if not stripped:
            continue
        if (stripped.startswith(('|', '```', '<!--')) or
                re.match(r'^(?:[-+*]|\d+[.)])\s+\*\*(?!JP:|VI:)', stripped)):
            break
        # An inline pair is complete unless a visible arrow/quote starts its
        # continuation. An empty header can own the following list/dialogue.
        if inline and not continuing and not stripped.startswith(('→', '>')):
            break
        if inline and continuing and not stripped.startswith(('→', '>')):
            break
        continuing = True
        text = re.sub(r'^\s*(?:>\s*|(?:[-+*]|\d+[.)])\s+|→\s*)', '', line).strip()
        text = re.sub(r'^[A-Za-zＡ-Ｚａ-ｚ][\w₀-₉]*\s*[:：]\s*', '', text)
        parts.append(text)
    return '\n'.join(parts)


def has_block_content(value: str) -> bool:
    return bool(re.search(r'[^\W_]', value, re.UNICODE) or EXERCISE_BLANK.search(value) or
                re.search(r'(?:…|⋯){1,}|[.．・]{3,}|[!?！？○◯×◎△]', value))


def validate_chapter(path: Path, report: Report) -> set[str]:
    content = read_text(path, report, str(path))
    if content is None:
        return set()
    if not content.strip():
        report.error(str(path), 'empty chapter')
    anchors = ANCHOR.findall(content)
    seen: set[str] = set()
    for anchor in anchors:
        if anchor in seen:
            report.error(str(path), f'duplicate anchor: {anchor}')
        seen.add(anchor)
        if not UNIT_ID.fullmatch(anchor):
            report.error(str(path), f'unexpected anchor in chapter: {anchor}')
    if not anchors:
        report.error(str(path), 'no unit anchors')
    for pattern, label in REMAINS:
        for match in pattern.finditer(content):
            line = content.count('\n', 0, match.start()) + 1
            report.error(f'{path}:{line}', label)
    for pattern, label in LANGUAGE_HINTS:
        for match in pattern.finditer(content):
            line = content.count('\n', 0, match.start()) + 1
            report.warn(f'{path}:{line}', label)
    lines, source_lines = language_lines(content.splitlines())
    markers = {i: marker for i, line in enumerate(lines)
               if (marker := pair_marker(line)) is not None}

    def next_marker(start: int) -> tuple[int, tuple[str, str]] | None:
        for i in range(start + 1, len(lines)):
            if pair_boundary(lines[i]):
                return None
            if i in markers:
                return i, markers[i]
        return None

    def previous_marker(start: int) -> tuple[int, tuple[str, str]] | None:
        for i in range(start - 1, -1, -1):
            if pair_boundary(lines[i]):
                return None
            if i in markers:
                return i, markers[i]
        return None

    for index, (label, value) in markers.items():
        tag, role = pair_label(label)
        following = next_marker(index)
        end = following[0] if following else next(
            (i for i in range(index + 1, len(lines)) if pair_boundary(lines[i])), len(lines))
        block = block_content(value, lines[index + 1:end])
        if not has_block_content(block):
            report.error(f'{path}:{source_lines[index]}', f'empty {label} text')
        if tag == 'JP':
            expected = 'VI' if role is None else f'{role} (VI)'
            if following is None or not labels_correspond(label, following[1][0]):
                report.error(f'{path}:{source_lines[index]}', f'{label} must be followed by {expected} before the next section')
            else:
                vi_index, (_, vi_value) = following
                vi_following = next_marker(vi_index)
                vi_end = vi_following[0] if vi_following else next(
                    (i for i in range(vi_index + 1, len(lines)) if pair_boundary(lines[i])), len(lines))
                translated = block_content(vi_value, lines[vi_index + 1:vi_end])
                source_blanks = len(EXERCISE_BLANK.findall(block))
                translated_blanks = len(EXERCISE_BLANK.findall(translated))
                if source_blanks != translated_blanks:
                    report.warn(f'{path}:{source_lines[index]}',
                                f'possible exercise placeholder mismatch: JP {source_blanks}, VI {translated_blanks}; '
                                'review against source, including intentional placeholder notation changes')
        else:
            expected = 'JP' if role is None else f'{role} (JP)'
            previous = previous_marker(index)
            previous_line = next((earlier for earlier in reversed(lines[:index]) if earlier.strip()), '')
            # A book may use an unlabelled Japanese paragraph or speaker before
            # a Vietnamese gloss. Do not force a new lesson layout to add JP tags.
            previous_is_translation = previous is not None and pair_label(previous[1][0])[0] == 'VI'
            unlabelled_source = (label == 'VI' and (previous is None or previous_is_translation) and
                                 pair_marker(previous_line) is None and
                                 not previous_line.lstrip().startswith(('#', '<')) and
                                 re.search(r'[\u3040-\u30ff\u3400-\u9fff]', previous_line))
            if (previous is None or not labels_correspond(previous[1][0], label)) and not unlabelled_source:
                report.error(f'{path}:{source_lines[index]}', f'{label} lacks preceding {expected}')
    return seen


def validate_units(book: Path, repo: Path, raw_text: str | None,
                   raw_book: Path | None, chapter_anchors: dict[str, set[str]],
                   allowed_pages: set[int], report: Report) -> None:
    path = book / '_meta' / 'units.jsonl'
    content = read_text(path, report, '_meta/units.jsonl')
    if content is None:
        return
    if not content.strip():
        report.error('_meta/units.jsonl', 'empty provenance file')
        return
    ids: set[str] = set()
    mapped: set[str] = set()
    raw_book_anchors = set(ANCHOR.findall(raw_text)) if raw_text is not None else set()
    for line_no, line in enumerate(content.splitlines(), 1):
        loc = f'_meta/units.jsonl:{line_no}'
        try:
            unit = json.loads(line)
        except json.JSONDecodeError as exc:
            report.error(loc, f'invalid JSON: {exc}')
            continue
        if not isinstance(unit, dict):
            report.error(loc, 'expected JSON object')
            continue
        unit_id = unit.get('unit_id')
        if not isinstance(unit_id, str) or not UNIT_ID.fullmatch(unit_id):
            report.error(loc, 'invalid unit_id')
            continue
        if unit_id in ids:
            report.error(loc, f'duplicate unit_id: {unit_id}')
        ids.add(unit_id)
        chapter = unit.get('chapter')
        if not isinstance(chapter, str) or chapter not in chapter_anchors:
            report.error(loc, f'chapter outside manifest: {chapter!r}')
        elif unit_id not in chapter_anchors[chapter]:
            report.error(loc, f'unit anchor {unit_id} absent from {chapter}')
        else:
            mapped.add(unit_id)
        if not isinstance(unit.get('heading'), str) or not unit['heading'].strip():
            report.error(loc, 'missing heading')
        if not isinstance(unit.get('review_status'), str) or not unit['review_status'].strip():
            report.error(loc, 'missing review_status')
        if not isinstance(unit.get('issues'), list):
            report.error(loc, 'issues must be a list')
        sources = unit.get('source')
        if not isinstance(sources, list) or not sources:
            report.error(loc, 'source must be a nonempty list')
            continue
        for index, src in enumerate(sources, 1):
            src_loc = f'{loc}.source[{index}]'
            if not isinstance(src, dict):
                report.error(src_loc, 'expected object')
                continue
            page = src.get('pdf_page')
            raw_page = src.get('raw_page')
            if type(page) is not int or page < 1 or page not in allowed_pages:
                report.error(src_loc, f'pdf_page {page!r} outside scope')
            page_file = relative_file(repo, raw_page, report, src_loc + '.raw_page')
            page_name = page_file.stem if page_file else None
            if page_file and page_file.suffix.lower() != '.md':
                report.error(src_loc, f'raw_page must be Markdown: {raw_page}')
            if page_name is not None and not RAW_PAGE.fullmatch(page_name):
                report.error(src_loc, f'raw_page filename must be pNNNN.md: {raw_page}')
            if page_name is not None and RAW_PAGE.fullmatch(page_name) and type(page) is int and int(page_name[1:]) != page:
                report.error(src_loc, f'raw_page {page_name} does not match PDF page {page}')
            if page_file and raw_book and not page_file.is_relative_to(raw_book.parent / 'pages'):
                report.error(src_loc, 'raw_page outside source Markdown pages directory')
            page_text = read_text(page_file, report, src_loc + '.raw_page') if page_file else None
            raw_anchors = set(ANCHOR.findall(page_text)) if page_text is not None else set()
            if page_name and page_text is not None and page_name not in raw_anchors:
                report.error(src_loc, f'raw page anchor absent: {page_name}')
            anchors = src.get('raw_anchors')
            if not isinstance(anchors, list) or not anchors or any(not isinstance(a, str) for a in anchors):
                report.error(src_loc, 'raw_anchors must be nonempty string list')
            elif page_text is not None:
                for anchor in anchors:
                    if anchor not in raw_anchors:
                        report.error(src_loc, f'raw anchor absent: {anchor}')
                    if raw_text is not None and anchor not in raw_book_anchors:
                        report.error(src_loc, f'raw anchor absent from source Markdown book: {anchor}')
                    if page_name and not anchor.startswith(page_name + '-'):
                        report.error(src_loc, f'raw anchor {anchor} outside {page_name}')
    for chapter, anchors in chapter_anchors.items():
        for anchor in sorted(anchors - mapped):
            report.error(chapter, f'unit anchor lacks provenance: {anchor}')


def validate(book: Path, repo: Path) -> int:
    report = Report()
    if not book.is_dir() or not any(book.iterdir()):
        report.error(str(book), 'book directory missing or empty')
        return report.show()
    manifest = parse_json(book / '_meta' / 'book.json', report, '_meta/book.json')
    if manifest is None:
        return report.show()
    if manifest.get('schema_version') != 1:
        report.error('_meta/book.json', 'schema_version must be 1')
    if not isinstance(manifest.get('title'), str) or not manifest['title'].strip():
        report.error('_meta/book.json', 'missing real book title')
    if manifest.get('paths_relative_to') != 'repository_root':
        report.error('_meta/book.json', 'paths_relative_to must be repository_root')
    if not isinstance(manifest.get('status'), str) or not manifest['status'].strip():
        report.error('_meta/book.json', 'missing partial/full status')
    pdf, _ = source_file(manifest, 'source_pdf', repo, report)
    raw, _ = source_file(manifest, 'source_markdown', repo, report)
    if pdf and pdf.suffix.lower() != '.pdf':
        report.error('source_pdf.path', 'source is not a PDF')
    if raw and raw.suffix.lower() != '.md':
        report.error('source_markdown.path', 'source is not Markdown')
    scope = manifest.get('scope')
    if not isinstance(scope, dict):
        report.error('_meta/book.json', 'scope must be an object')
        scope = {}
    pages = page_scope(scope.get('pdf_pages'), report)
    raw_page_hashes = manifest.get('raw_page_sha256')
    if raw and raw_page_hashes is not None:
        if not isinstance(raw_page_hashes, dict) or set(raw_page_hashes) != {str(p) for p in pages}:
            report.error('raw_page_sha256', 'must contain exactly the scope PDF pages')
        else:
            for page in sorted(pages):
                page_file = raw.parent / 'pages' / f'p{page:04d}.md'
                check_digest(page_file, raw_page_hashes[str(page)], report, f'raw_page_sha256[{page}]')
    if raw:
        corpus_manifest_path = raw.parent / 'manifest.json'
        if corpus_manifest_path.is_file():
            corpus_manifest = parse_json(corpus_manifest_path, report, 'raw corpus manifest')
            if corpus_manifest:
                count = corpus_manifest.get('page_count')
                if type(count) is int and any(page > count for page in pages):
                    report.error('scope.pdf_pages', f'page outside source PDF page_count {count}')
                corpus_digest = corpus_manifest.get('source_sha256')
                pdf_record = manifest.get('source_pdf')
                if isinstance(pdf_record, dict) and isinstance(corpus_digest, str) and corpus_digest != pdf_record.get('sha256'):
                    report.error('raw corpus manifest', 'raw corpus PDF hash differs from fork source PDF hash')
    chapters = scope.get('chapters')
    if not isinstance(chapters, list) or not chapters or any(not isinstance(c, str) for c in chapters):
        report.error('scope.chapters', 'expected nonempty list of chapter paths')
        chapters = []
    if len(set(chapters)) != len(chapters):
        report.error('scope.chapters', 'duplicate chapter path')
    check_build(book, manifest, chapters, report)
    chapter_anchors: dict[str, set[str]] = {}
    all_anchors: set[str] = set()
    for name in chapters:
        path = relative_file(book, name, report, 'scope.chapters')
        if path is None:
            continue
        anchors = validate_chapter(path, report)
        for anchor in anchors & all_anchors:
            report.error(name, f'duplicate unit anchor across chapters: {anchor}')
        all_anchors.update(anchors)
        chapter_anchors[name] = anchors
    assembled = read_text(book / 'book.md', report, 'book.md')
    if assembled is not None and not assembled.strip():
        report.error('book.md', 'empty assembled book')
    raw_text = read_text(raw, report, 'source_markdown.path') if raw else None
    validate_units(book, repo, raw_text, raw, chapter_anchors, pages, report)
    return report.show()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('book_dir', type=Path, help='forked knowledge book directory')
    parser.add_argument('--repo-root', type=Path, required=True, help='repository root for manifest source paths')
    args = parser.parse_args()
    return validate(args.book_dir.resolve(), args.repo_root.resolve())


if __name__ == '__main__':
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    sys.exit(main())
