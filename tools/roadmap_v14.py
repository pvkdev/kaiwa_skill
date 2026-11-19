"""Compile V14 Markdown lectures, validate source locators and render the pilot in the roadmap."""
import argparse
import copy
import hashlib
import json
import re
import runpy
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "kaiwa_skill/planning"
PILOT = PLAN / "v14/pilot"
PAGE = ROOT / "docs/index.html"
TEMPLATE = ROOT / "tools/review_site.html"
CODES = ("S-011", "T-008", "H-020")
COURSE_SCRIPT = re.compile(r'<script id="course-data" type="application/json">(.*?)</script>', re.S)
JP = re.compile(r"[ぁ-ヿ一-鿿]")


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, text):
    tmp = path.with_suffix(path.suffix + ".v14.tmp")
    tmp.write_text(text, encoding="utf8", newline="\n")
    tmp.replace(path)


def parse_lesson(md):
    lines = iter(md.strip().splitlines())
    first = next(lines, "")
    if not first.startswith("# ") or not first[2:].strip():
        raise ValueError("Expected one Markdown title")
    body, headings, examples = [], [], []
    for line in lines:
        if line.startswith("# "):
            raise ValueError("Duplicate title")
        if line.startswith("## "):
            headings.append(line[3:].strip())
        if line.startswith(">"):
            second = next(lines, "")
            ja, vi = line[1:].strip(), second[1:].strip()
            if not JP.search(ja) or not second.startswith(">") or not vi or not re.search(r"[A-Za-zÀ-ỹ]", vi):
                raise ValueError("Expected consecutive Japanese and Vietnamese example lines: " + line)
            key = f"ex{len(examples) + 1:02}"
            examples.append({"id": key, "ja": ja, "vi": vi})
            body.append("{{utterance:" + key + "}}")
        else:
            body.append(line)
    if not examples or not headings or len(set(headings)) != len(headings):
        raise ValueError("Missing examples, missing sections or repeated heading")
    return first[2:].strip(), "\n".join(body).strip(), headings, examples


def verify_sources(manifest, headings, stage, books):
    code = stage["code"]
    sections = manifest["sections"]
    if manifest["code"] != code or [s["heading"] for s in sections] != headings:
        raise ValueError(f"{code}: source map must match the Markdown sections")
    covered, book_ids = set(), set()
    registry = []
    for section in sections:
        covered.update(section["scene_ids"])
        for source in section["sources"]:
            if not source["use_vi"].strip():
                raise ValueError(f"{code}: missing editorial use")
            if "book_id" in source:
                book = books[source["book_id"]]
                base = (ROOT / book["directory"]).resolve()
                path = (ROOT / source["path"]).resolve()
                if not path.is_relative_to(base) or path.suffix != ".md" or source["book_title"] != book["title"]:
                    raise ValueError(f"{code}: book title or locator mismatch: {path}")
                lines = path.read_text(encoding="utf-8-sig").splitlines()
                lo, hi = source["start_line"], source["end_line"]
                if not 1 <= lo <= hi <= len(lines):
                    raise ValueError(f"{code}: invalid source lines: {path}")
                excerpt = "\n".join(lines[lo - 1:hi]).encode("utf8")
                source = {**source, "excerpt_sha256": hashlib.sha256(excerpt).hexdigest()}
                book_ids.add(source["book_id"])
            elif not (urlsplit(source.get("url", "")).scheme in {"http", "https"} and source.get("title") and source.get("checked_on")):
                raise ValueError(f"{code}: invalid external source")
            registry.append({"id": f"src{len(registry)+1:02}", "heading": section["heading"], **source})
    if not book_ids or covered != {scene["id"] for scene in stage["situations"]}:
        raise ValueError(f"{code}: missing knowledge or incomplete situation map")
    return registry


def compile_stage(stage, books, shadowing):
    code = stage["code"]
    folder = PILOT / code
    md = (folder / "lesson.md").read_text(encoding="utf-8-sig")
    manifest = read(folder / "sources.json")
    title, body, headings, examples = parse_lesson(md)
    registry = verify_sources(manifest, headings, stage, books)
    target = "stages" if (PLAN / "v13/stages" / code / "status.json").exists() else "pilot"
    shadowing["build"](code, "checkpoint", target=target)
    digest = shadowing["digest"]
    shadow = PLAN / "v13" / target / code / "shadowing.json"
    node_id = stage["uid"] + "-lecture"
    data = {"body_md": body, "utterance_ids": [e["id"] for e in examples],
            "video_status": "planned", "source_family": "general"}
    public = {"id": node_id, "type": "knowledge", "title_vi": title, "data": data, "utterances": examples}
    pins = {"v11": digest(PLAN / "v11/learner.json"),
            "v12": digest(PLAN / "v12/stages" / code / "vocabulary.json"),
            "v13": digest(shadow), "shadowing_path": shadow.relative_to(ROOT).as_posix(),
            "markdown": digest(folder / "lesson.md"), "sources": digest(folder / "sources.json")}
    package = copy.deepcopy(public)
    package["data"]["admin_provenance"] = {"authorship": "source_adaptation",
                                           "source_refs": [s["id"] for s in registry], "cd_refs": []}
    package["source_registry"] = registry
    package["section_notes"] = [{k: value for k, value in section.items() if k != "sources"}
                                for section in manifest["sections"]]
    if "example_notes" in manifest:
        package["example_notes"] = manifest["example_notes"]
    package["inputs"] = pins
    return public, package, read(shadow)


def attach_published_lectures(course):
    """Preserve pilot lectures when a newer vocabulary snapshot rebuilds the course."""
    for stage in course["stages"]:
        path = PILOT / stage["code"] / "lecture.json"
        if path.is_file():
            node = read(path)
            stage["lecture"] = {k: node[k] for k in ("id", "type", "title_vi", "utterances")}
            stage["lecture"]["data"] = {k: v for k, v in node["data"].items() if k != "admin_provenance"}


def html(template, course):
    if template.count("__COURSE_DATA__") != 1:
        raise ValueError("Missing course template marker")
    payload = json.dumps(course, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    return template.replace("__COURSE_DATA__", payload)


def build(update_site=False):
    original = PAGE.read_bytes()
    match = COURSE_SCRIPT.search(original.decode("utf-8-sig"))
    if not match:
        raise ValueError("Published roadmap is missing its course data")
    course = json.loads(match.group(1))
    books = {b["book_id"]: b for b in read(PLAN / "catalog27/manifest.json")["books"]}
    stages = {s["code"]: s for s in course["stages"]}
    shadowing = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-topic-shadowing/scripts/pilot.py"))
    preview_stages, packages = [], {}
    for code in CODES:
        stage = stages[code]
        node, packages[code], shadow = compile_stage(stage, books, shadowing)
        stage["lecture"] = node
        preview = copy.deepcopy(stage)
        preview["shadowing"] = shadow
        if not any(entry["type"] == "merged_shadowing" for entry in preview["order"]):
            before_lecture = next(i for i, entry in enumerate(preview["order"]) if entry["type"] == "stage_lecture")
            preview["order"].insert(before_lecture, {"type": "merged_shadowing", "id": shadow["id"]})
        preview_stages.append(preview)
    template = TEMPLATE.read_text(encoding="utf8")
    pilot_course = {"version": "14.0-pilot", "stages": preview_stages, "content": {},
                    "pilot_stages": [s["uid"] for s in preview_stages], "branches": course["branches"]}
    if update_site and PAGE.read_bytes() != original:
        raise RuntimeError("Roadmap changed during compilation. Rerun on the latest snapshot.")
    for code, package in packages.items():
        write(PILOT / code / "lecture.json", json.dumps(package, ensure_ascii=False, indent=2) + "\n")
    write(PILOT / "PREVIEW.html", html(template, pilot_course))
    if update_site:
        write(PAGE, html(template, course))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--update-site", action="store_true", help="Also overlay lectures on the current docs/index.html")
    build(ap.parse_args().update_site)
