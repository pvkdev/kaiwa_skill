"""Conservatively normalize legacy Harumii lessons with lossless example/image checks."""
import json
import re
from collections import Counter
from pathlib import Path

from grammar_upload import parse, validate_body

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar"
PREVIOUS = ROOT / "authored/grammar-upload/2026-11-25"
OUT = ROOT / "authored/grammar-upload/2026-11-25-structure"
REPORT = ROOT / "reports/grammar-upgrade-2026-11-25-structure-audit.json"
H1_EQUIVALENTS = {
    "6bd63e67", "51fec891", "55975be2", "0c06187e", "96897d8e",
    "d46cf19d", "6420a358", "62fb39ee", "05c92c3d", "cf464c6e",
    "c0023e20", "c8685c69", "89dc6908", "fdb89b70", "c35bdeff",
    "f0cb6e5c", "0a024652", "25673aa7",
}


def visible_text(s):
    return re.sub(r"\s+", "", s).strip("。 .")


def extract_pairs(body):
    pairs = []
    i = 0
    while i < len(body):
        line = body[i]
        if line.startswith("###### "):
            raise ValueError("orphan_H6")
        if not line.startswith("##### "):
            i += 1
            continue
        match = re.fullmatch(r"#####\s*([0-9]+)\.\s*(.+)", line)
        if not match:
            raise ValueError("non_sentence_H5")
        ja = match.group(2).strip()
        if re.search(r"[*_`]", ja):
            raise ValueError("formatted_H5")
        j = i + 1
        while j < len(body) and not body[j].strip():
            j += 1
        if j >= len(body):
            raise ValueError("missing_H6")
        m2 = re.fullmatch(r"######\s*→\s*(.+)", body[j])
        if not m2:
            raise ValueError("nonadjacent_H6")
        vi = m2.group(1).strip()
        if re.search(r"[*_`]", vi):
            raise ValueError("formatted_H6")
        pairs.append((ja, vi))
        i = j + 1
    return pairs


def convert(path):
    h, body = parse(path)
    nonblank = [(i, s) for i, s in enumerate(body) if s.strip()]
    if not nonblank or not (
        nonblank[0][1] == "# " + h["name"]
        or (h["id"][:8] in H1_EQUIVALENTS and nonblank[0][1].startswith("# "))
    ):
        raise ValueError("H1_not_exact_name")
    h1_index = nonblank[0][0]
    structure_heading = "## Cấu trúc ngữ pháp"
    if body.count(structure_heading) != 1:
        raise ValueError("structure_heading_missing_or_repeated")
    sh = body.index(structure_heading)
    if sh <= h1_index:
        raise ValueError("structure_before_H1")
    prelude = [s.strip() for s in body[h1_index + 1:sh] if s.strip()]
    if len(prelude) != 2 or prelude[1] != "---":
        raise ValueError("complex_prelude")
    if not h.get("description", "").strip():
        candidate = prelude[0]
        if candidate.startswith("**") and candidate.endswith("**"):
            candidate = candidate[2:-2]
        if not candidate or len(candidate) > 2048 or candidate.startswith(("#", "-", ">", "![")) or "![" in candidate:
            raise ValueError("empty_description")
        h["description"] = candidate
    if not re.fullmatch(r"\*\*(.+)\*\*", prelude[0]) and visible_text(prelude[0]) != visible_text(h["description"]):
        raise ValueError("complex_prelude")
    old_meaning = prelude[0][2:-2] if prelude[0].startswith("**") and prelude[0].endswith("**") else prelude[0]
    if visible_text(old_meaning) != visible_text(h["description"]):
        raise ValueError("meaning_differs_from_description")
    after = next((i for i in range(sh + 1, len(body)) if re.match(r"^#{1,3} ", body[i])), len(body))
    structure_source = body[sh + 1:after]
    structures = []
    for line in structure_source:
        s = line.strip()
        if not s or s in {">", "---"}:
            continue
        m = re.fullmatch(r">\s*\*\*(.+)\*\*(?:<br>)?", s)
        if not m:
            raise ValueError("complex_structure")
        value = m.group(1).strip()
        if "<" in value or ">" in value:
            raise ValueError("html_in_structure")
        structures.append(value)
    if not structures:
        raise ValueError("empty_structure")
    tail = body[after:]
    if not tail or any(s.startswith("# ") for s in tail):
        raise ValueError("body_missing_or_extra_H1")
    if any(re.match(r"^####\s", s) for s in tail):
        raise ValueError("H4_in_body")
    if any(re.search(r"</?[A-Za-z][^>]*>", s.replace("<br>", "")) for s in tail):
        raise ValueError("html_in_body")
    if any(re.match(r"^\s*(?:`{3,}|~{3,})", s) for s in tail):
        raise ValueError("code_fence")
    if any(re.search(r"[\U0001F000-\U0001FAFF]", s) for s in tail):
        raise ValueError("emoji")
    source_pairs = extract_pairs(tail)
    source_images = [s for s in body if "![" in s]
    result = ["---"]
    for key in ("id", "jlpt", "name", "description", "conjugation"):
        if key in h:
            result.append(f"{key}: {json.dumps(h[key], ensure_ascii=False)}")
    result += ["---", "", "# " + h["name"], "", "> " + h["description"], "", "---", "", structure_heading, ""]
    for idx, structure in enumerate(structures):
        result.append("> **" + structure + "**" + ("<br>" if idx + 1 < len(structures) else ""))
    result.append("")
    number = 1
    i = 0
    while i < len(tail):
        s = tail[i]
        if re.match(r"^#{2,3} ", s):
            number = 1
        if s.startswith("##### "):
            m = re.fullmatch(r"#####\s*([0-9]+)\.\s*(.+)", s)
            result.append(f"##### {number}. {m.group(2).strip()}")
            j = i + 1
            while j < len(tail) and not tail[j].strip():
                j += 1
            m2 = re.fullmatch(r"######\s*→\s*(.+)", tail[j])
            result.append("###### → " + m2.group(1).strip())
            result.append("")
            number += 1
            i = j + 1
            continue
        result.append(s)
        i += 1
    while result and not result[-1].strip():
        result.pop()
    new_body = result[result.index("---", 1) + 1:]
    validate_body(new_body, h["name"], path)
    if extract_pairs(new_body) != source_pairs:
        raise ValueError("pair_preservation")
    if [s for s in new_body if "![" in s] != source_images:
        raise ValueError("image_preservation")
    return "\n".join(result) + "\n", len(source_pairs), len(source_images)


def main():
    previous_ids = {parse(p)[0]["id"] for p in PREVIOUS.glob("N[45]/*.md")}
    entries = []
    for path in sorted(BASE.glob("N[45]/*.md")):
        h, _ = parse(path)
        if h["id"] in previous_ids:
            continue
        entry = {"file": str(path.relative_to(BASE)).replace("\\", "/"), "id": h["id"]}
        try:
            contents, pairs, images = convert(path)
        except (ValueError, AssertionError, KeyError, TypeError) as exc:
            entry.update(status="deferred", reason=str(exc).split(":", 1)[0])
        else:
            target = OUT / path.parent.name / path.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(contents, encoding="utf-8")
            entry.update(status="converted", pairs=pairs, images=images)
        entries.append(entry)
    assert len(entries) == 174
    summary = {"baseline_remaining": len(entries), "converted": sum(e["status"] == "converted" for e in entries), "deferred": sum(e["status"] == "deferred" for e in entries), "pairs_preserved": sum(e.get("pairs", 0) for e in entries), "images_preserved": sum(e.get("images", 0) for e in entries), "deferred_reasons": dict(Counter(e["reason"] for e in entries if e["status"] == "deferred"))}
    REPORT.write_text(json.dumps({"summary": summary, "entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
