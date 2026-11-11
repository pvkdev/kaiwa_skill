"""Build clean reading/search derivatives without changing review claims."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contained(root: Path, relative: str) -> Path:
    result = (root / relative).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes book directory: {relative}")
    return result


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
    for relative in chapters:
        path = contained(book, relative)
        text = path.read_text(encoding="utf-8-sig").strip()
        if not text:
            raise ValueError(f"Empty chapter: {relative}")
        texts[relative] = text
        chapter_hashes[relative] = digest(path)
        # Chapters use ordinary headings, no code fences; keep source anchors stable.
        parts.append(re.sub(r"(?m)^(#{1,5}) ", r"\1# ", text))
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
