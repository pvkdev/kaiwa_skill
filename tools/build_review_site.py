"""Compile the current Kaiwa JSON roadmap into one offline GitHub Pages reader."""
import hashlib
import json
from pathlib import Path

import roadmap_v6 as roadmap

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs"


def build_v8(source):
    entries = []
    for stage in roadmap.rows(source):
        data = stage["v6"]
        entries.append({
            "uid": stage["uid"], "code": stage["display_code"], "level": stage["level"],
            "number": stage["level_order"], "title": stage["title"],
            "cluster": stage["cluster_title"], "cluster_id": stage["cluster_id"],
            "objective": stage["objective"], "events": stage["events"], "situations": stage["situations"],
            "vocabulary": data["decision"]["vocabulary_topics"], "selections": [],
            "order": data["learning_order"], "shadowing": data["shadowing"],
        })
    payload = {"version": "8.0", "stages": entries, "content": {}, "branches": roadmap.BRANCH}
    directory = source.parent
    (directory / "learner.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf8", newline="\n")
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", encoded)
    for path in (directory / "ROADMAP.html", OUTPUT / "index.html"):
        path.write_text(html, encoding="utf8", newline="\n")


def build():
    pointer = roadmap.read(ROOT / "kaiwa_skill/planning/CURRENT_ROADMAP.json")
    if pointer["version"] == "9.0":
        from roadmap_v9 import build as build_v9
        build_v9(publish=True)
        return
    if pointer["version"] == "8.0":
        build_v8(ROOT / pointer["roadmap"])
        return
    if pointer['version'] == '7.0':
        from roadmap_v7 import build as build_v7
        build_v7(publish=True)
        return
    if pointer['version'] in ('6.4', '6.5'):
        from roadmap_topic_shadowing import build as build_topic
        build_topic(pointer['version'], publish=True)
        return
    source = ROOT / pointer["roadmap"]
    stages = roadmap.rows(source)
    directory = source.parent
    rendered = {}
    entries = []
    for stage in stages:
        data = stage["v6"]
        decision = data["decision"]
        selections = []
        manifest_path = directory / "stages" / stage["display_code"] / "manifest.json"
        manifest = roadmap.read(manifest_path) if decision and decision["selections"] else {"materials": []}
        records = {m["file"]: m for m in manifest["materials"]}
        for selection in decision["selections"] if decision else []:
            raw = (directory / selection["material_path"]).read_bytes()
            # A local manifest pins the bytes that were copied from the books.
            record = records[Path(selection["material_path"]).name]
            if hashlib.sha256(raw).hexdigest() != record["sha256"]:
                raise ValueError("Source snapshot changed: " + selection["material_path"])
            html = roadmap.render_excerpt(raw, selection)
            key = hashlib.sha256(html.encode("utf8")).hexdigest()
            rendered[key] = html
            selections.append({
                "book_id": selection["book_id"],
                "pack_id": selection["pack_id"],
                "title": roadmap.learner_title(selection),
                "kind": selection["kind"],
                "support": selection.get("pack_scope") == "educational_support",
                "content_key": key,
                "provenance": {
                    key: selection.get(key) for key in (
                        "book_title", "title_ja", "path", "unit_id", "start_line", "end_line",
                        "extra_parts", "boundary", "audio", "audio_note", "source_quality_note",
                        "fit_vi", "difficulty_vi", "situation_ids"
                    ) if selection.get(key) is not None
                }
            })
        entries.append({
            "uid": stage["uid"], "code": stage["display_code"], "level": stage["level"],
            "number": stage["level_order"], "title": stage["title"],
            "cluster": stage["cluster_title"], "cluster_id": stage["cluster_id"],
            "objective": stage["objective"], "events": stage["events"],
            "situations": stage["situations"],
            "vocabulary": decision["vocabulary_topics"] if decision else [],
            "selections": selections, "order": data["learning_order"]
        })
    payload = {
        "version": pointer["version"],
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "stages": entries, "content": rendered, "branches": roadmap.BRANCH
    }
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    if template.count("__COURSE_DATA__") != 1:
        raise ValueError("The reader template must contain one data placeholder.")
    OUTPUT.mkdir(exist_ok=True)
    (OUTPUT / "index.html").write_text(template.replace("__COURSE_DATA__", encoded),
                                      encoding="utf8", newline="\n")
    (OUTPUT / ".nojekyll").touch()
    print(f"{len(stages)} stages, {sum(len(s['selections']) for s in entries)} source placements, "
          f"{len(rendered)} deduplicated readings → docs/index.html")


if __name__ == "__main__":
    build()
