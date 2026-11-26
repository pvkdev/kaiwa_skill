"""Validate edited grammar Markdown against the Harumii export and package a local ZIP."""
import argparse
import json
import re
import tempfile
from pathlib import Path
from uuid import UUID
from zipfile import ZipFile, ZIP_DEFLATED

BASE = Path(__file__).resolve().parents[1] / "materials/grammar"
LEVELS = ("N4", "N5")
LIMITS = {"name": 256, "description": 2048, "conjugation": 1024}


def check(ok, msg):
    if not ok:
        raise ValueError(msg)


def parse(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    check(lines and lines[0] == "---" and "---" in lines[1:], f"{path}: missing front matter")
    end = lines.index("---", 1)
    header = {}
    for line in lines[1:end]:
        key, sep, value = line.partition(":")
        check(sep and key not in header, f"{path}: malformed/duplicate field {key}")
        value = value.strip()
        header[key] = json.loads(value) if value.startswith('"') else value
    return header, lines[end+1:]


def baseline():
    entries = {}
    for level in LEVELS:
        for file in (BASE / level).glob("*__*.md"):
            h, _ = parse(file)
            uid = str(UUID(h["id"]))
            check(uid not in entries, f"Duplicate export id in {file}")
            entries[uid] = (file.name, level, h["name"])
    return entries


def validate_body(body, name, path):
    while body and not body[0].strip():
        body.pop(0)
    lines = [s for s in body if s.strip()]
    check(len(lines) >= 5 and lines[0] == "# "+name and lines[1].startswith("> ")
          and lines[2] == "---" and sum(s.startswith("# ") for s in lines) == 1,
          f"{path}: H1, meaning or divider")
    heading = "## Cấu trúc ngữ pháp"
    check(lines.count(heading) == 1, f"{path}: structure section")
    k = lines.index(heading)+1
    structures = []
    while k < len(lines) and lines[k].startswith(">"):
        structures.append(lines[k])
        k += 1
    check(structures and all(re.fullmatch(r"> \*\*.+\*\*<br>", s) for s in structures[:-1])
          and re.fullmatch(r"> \*\*.+\*\*(?:<br>)?", structures[-1]), f"{path}: structure lines")
    next_example = 1
    for i, line in enumerate(body):
        check(not re.match(r"\s*(?:#{4}\s|~{3,}|\x60{3,})", line)
              and not re.search(r"</?[A-Za-z][^>]*>", line.replace("<br>", "")),
              f"{path}: unsupported heading, HTML or code block")
        if re.match(r"^#{2,3} ", line):
            next_example = 1
        if line.startswith("##### "):
            check(re.fullmatch(rf"##### {next_example}\. .+", line) and i+1 < len(body)
                  and body[i+1].startswith("###### → ") and body[i+1][9:].strip(),
                  f"{path}: example number or translation at {line}")
            next_example += 1
        if line.startswith("###### "):
            check(i and body[i-1].startswith("##### "), f"{path}: translation without example")
        if line.startswith(("##### ", "###### ")):
            check(not re.search(r"[*_\x60]", line), f"{path}: formatting in example")


def package(folder, out):
    check(folder.is_dir() and folder.resolve() != BASE.resolve(), "Select an edited batch")
    entries = baseline()
    names = {(level, name.casefold()) for _, level, name in entries.values()}
    seen_ids, added, files = set(), set(), []
    for path in sorted(folder.rglob("*.md")):
        if path.name.startswith("_") or path.name in {"README.md", "HUONG-DAN-AI.md"}:
            continue
        h, body = parse(path)
        check(set(h) <= {"id","jlpt",*LIMITS} and all(isinstance(x, str) for x in h.values()),
              f"{path}: unexpected front matter")
        for key, limit in LIMITS.items():
            check(len(h.get(key, "")) <= limit, f"{path}: {key} too long")
        uid = h.get("id")
        if uid == "new":
            level, name = h.get("jlpt"), h.get("name", "")
            key = (level, name.casefold())
            check(level in LEVELS and name.strip() and path.name.endswith("__new.md")
                  and key not in names and key not in added, f"{path}: invalid or duplicate new grammar")
            added.add(key)
        else:
            check(uid in entries and uid not in seen_ids, f"{path}: unknown or repeated ID")
            filename, level, original_name = entries[uid]
            check(path.name == filename and h.get("jlpt", level) == level, f"{path}: file or level changed")
            seen_ids.add(uid)
            name = h.get("name", original_name)
        validate_body(body, name, path)
        arcname = f"{level}/{path.name}"
        check(all(a != arcname for _, a in files), f"Repeated ZIP path: {arcname}")
        files.append((path, arcname))
    check(files, "No edited entries")
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
        draft = Path(tmp) / "bundle.zip"
        with ZipFile(draft, "w", ZIP_DEFLATED) as z:
            for file, arc in files:
                z.write(file, arc)
        with ZipFile(draft) as z:
            check(z.testzip() is None, "ZIP integrity check failed")
        out.hardlink_to(draft)
    return len(seen_ids), len(added)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("folder", type=Path)
    cli.add_argument("zip", type=Path)
    args = cli.parse_args()
    edits, additions = package(args.folder, args.zip)
    print(f"{edits} existing, {additions} new: {args.zip}")

