"""Build clean reading/search derivatives without changing review claims."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root: Path, relative: str) -> Path:
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes book directory: {relative}")
    return result


FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(?:[^\r\n]*)$")


def escaped(text: str, index: int) -> bool:
    backslashes = 0
    while index - backslashes - 1 >= 0 and text[index - backslashes - 1] == "\\":
        backslashes += 1
    return backslashes % 2 == 1


def link_end(text: str, start: int) -> tuple[int, int] | None:
    """Return the destination bounds of an inline Markdown link at ``start``."""
    if escaped(text, start) or (start > 0 and text[start - 1] == "!"):
        return None
    depth = 1
    i = start + 1
    while i < len(text) and depth:
        if not escaped(text, i):
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
        i += 1
    if depth or i >= len(text) or text[i] != "(":
        return None
    destination_start = i + 1
    depth = 1
    i += 1
    quote = None
    angle = False
    title_zone = False
    while i < len(text):
        char = text[i]
        if escaped(text, i):
            i += 1
            continue
        if angle:
            angle = char != ">"
        elif quote:
            if char == quote:
                quote = None
        elif char == "<":
            angle = True
        elif char.isspace() and depth == 1:
            title_zone = True
        elif char in "\"'" and title_zone:
            quote = char
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if not depth:
                return destination_start, i
        i += 1
    return None


def rewrite_destination(body: str, chapter: str, chapters: set[str]) -> str:
    if body.startswith("<"):
        end = body.find(">")
        if end < 0:
            return body
        destination, suffix = body[1:end], body[end + 1:]
        wrapped = True
    else:
        match = re.match(r"(?:\\.|[^\s])+", body)
        if not match:
            return body
        destination, suffix = match[0], body[match.end():]
        wrapped = False
    if not destination or destination.startswith(("#", "/", "\\")):
        return body
    try:
        target = urlsplit(destination)
    except ValueError:
        return body
    if target.scheme or target.netloc or target.query or not target.path or not target.fragment:
        return body
    relative = unquote(target.path)
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(chapter), relative))
    if resolved not in chapters:
        return body
    fragment = "#" + destination.split("#", 1)[1]
    return ("<" + fragment + ">" if wrapped else fragment) + suffix


def rewrite_inline_links(text: str, chapter: str, chapters: set[str]) -> str:
    result = []
    i = 0
    while i < len(text):
        if text[i] == "`" and not escaped(text, i):
            run_end = i + 1
            while run_end < len(text) and text[run_end] == "`":
                run_end += 1
            marker = text[i:run_end]
            closing = re.search(r"(?<!`)" + re.escape(marker) + r"(?!`)", text[run_end:])
            if closing:
                end = run_end + closing.end()
                result.append(text[i:end])
                i = end
                continue
            result.append(marker)
            i = run_end
            continue
        if text[i] == "[":
            bounds = link_end(text, i)
            if bounds:
                start, end = bounds
                result.append(text[i:start])
                result.append(rewrite_destination(text[start:end], chapter, chapters))
                result.append(")")
                i = end + 1
                continue
        result.append(text[i])
        i += 1
    return "".join(result)


def compiled_links(text: str, chapter: str, chapters: set[str]) -> str:
    """Keep chapter links in source; target assembled anchors in book.md."""
    result = []
    prose = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = FENCE.match(line)
        if fence:
            result.append(line)
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not line[marker.end(1):].strip():
                fence = None
        elif marker:
            if prose:
                result.append(rewrite_inline_links("".join(prose), chapter, chapters))
                prose = []
            result.append(line)
            fence = marker[1][0], len(marker[1])
        else:
            prose.append(line)
    if prose:
        result.append(rewrite_inline_links("".join(prose), chapter, chapters))
    return "".join(result)


def assemble(book: Path) -> dict:
    meta_path = book / "_meta/book.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
    chapters = meta["scope"]["chapters"]
    if not chapters or len(chapters) != len(set(chapters)):
        raise ValueError("Expected a non-empty, unique ordered chapter list")
    units = [json.loads(line) for line in (book / "_meta/units.jsonl").read_text(
        encoding="utf-8-sig").splitlines() if line.strip()]
    if not units or len({unit["unit_id"] for unit in units}) != len(units):
        raise ValueError("Expected non-empty units with unique IDs")
    texts = {}
    parts = [f"# {meta['title']}\n"]
    chapter_hashes = {}
    chapter_paths = set(chapters)
    for relative in chapters:
        path = contained(book, relative)
        text = path.read_text(encoding="utf-8-sig").strip()
        if not text:
            raise ValueError(f"Empty chapter: {relative}")
        texts[relative] = text
        chapter_hashes[relative] = digest(path)
        compiled = compiled_links(text, relative, chapter_paths)
        parts.append(re.sub(r"(?m)^(#{1,5}) ", r"\1# ", compiled))
    search_rows = []
    for unit in units:
        chapter = unit["chapter"]
        if chapter not in texts:
            raise ValueError(f"Unit outside scope: {unit['unit_id']}")
        text = texts[chapter]
        markers = list(re.finditer(r'<a\s+id="(u-[^\"]+)"\s*></a>', text))
        positions = [i for i, match in enumerate(markers) if match[1] == unit["unit_id"]]
        if len(positions) != 1:
            raise ValueError(f"Unit must have exactly one anchor: {unit['unit_id']}")
        i = positions[0]
        start = markers[i].end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        clean = text[start:end].strip()
        search_rows.append({"unit_id": unit["unit_id"], "chapter": chapter,
                            "heading": unit["heading"], "text": clean,
                            "source": unit["source"]})
    # All input checks precede any output writes.
    (book / "book.md").write_text("\n\n".join(parts).rstrip() + "\n", encoding="utf-8")
    index = book / "_meta/search.jsonl"
    index.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in search_rows),
                     encoding="utf-8")
    meta["build"] = {"chapter_sha256": chapter_hashes,
                     "units_sha256": digest(book / "_meta/units.jsonl"),
                     "book_sha256": digest(book / "book.md"),
                     "search_sha256": digest(index), "unit_count": len(units),
                     "heading_transform": "demote chapter headings one level"}
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"chapters": len(chapters), "units": len(units), "status": meta["status"]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("book_dir", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(assemble(args.book_dir.resolve()), ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
