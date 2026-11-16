"""Publish the V9.2 reader using the released V9.1 curriculum."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "kaiwa_skill/planning"
BASE = PLANNING / "v9_1"
OUT = PLANNING / "v9_2"


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf8")


def build(publish=False):
    OUT.mkdir(exist_ok=True)
    payload = json.loads((BASE / "learner.json").read_text("utf8"))
    payload["version"] = "9.2"
    write_json(OUT / "learner.json", payload)
    roadmap = BASE / "KAIWA_CHANG_V9_1.jsonl"
    (OUT / "KAIWA_CHANG_V9_2.jsonl").write_bytes(roadmap.read_bytes())
    for name in ("chang_registry.json", "SO_CAP.md", "TRUNG_CAP.md", "THUONG_CAP.md"):
        (OUT / name).write_bytes((BASE / name).read_bytes())
    (OUT / "edits").mkdir(exist_ok=True)
    for edit in sorted((BASE / "edits").glob("*.json")):
        (OUT / "edits" / edit.name).write_bytes(edit.read_bytes())
    status = json.loads((BASE / "STATUS.json").read_text("utf8"))
    status.update(version="9.2", basis_sha256=hashlib.sha256(roadmap.read_bytes()).hexdigest())
    write_json(OUT / "STATUS.json", status)
    policy = json.loads((BASE / "SOURCE_POLICY.json").read_text("utf8"))
    policy.update(version="9.2", basis="../v9_1/KAIWA_CHANG_V9_1.jsonl")
    write_json(OUT / "SOURCE_POLICY.json", policy)
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", encoded)
    (OUT / "ROADMAP.html").write_text(html, encoding="utf8")
    if publish:
        (ROOT / "docs/index.html").write_text(html, encoding="utf8")
        pointer = {"version": "9.2"}
        for key, name in (("registry", "chang_registry.json"), ("roadmap", "KAIWA_CHANG_V9_2.jsonl"),
                          ("policy", "SOURCE_POLICY.json")):
            pointer[key] = (OUT / name).relative_to(ROOT).as_posix()
        write_json(PLANNING / "CURRENT_ROADMAP.json", pointer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    build(parser.parse_args().publish)
