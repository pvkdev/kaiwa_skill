"""Validate specialty practice, merge it into the V10 export and build the reader."""
import argparse
import hashlib
import json
import runpy
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "kaiwa_skill/planning"
BASE = PLANNING / "v9_2"
OUT = PLANNING / "v10"
HELPER = runpy.run_path(str(ROOT / ".agents/skills/kaiwa-luyen-chuyen-de/scripts/practice.py"))


def read(path):
    return json.loads(path.read_text("utf8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf8"))


def build(publish=False):
    payload = read(BASE / "learner.json")
    payload["version"] = "10.0"
    specialties = [s for s in payload["stages"] if s["stage_kind"] == "speak_japanese"]
    loaded = {}
    for stage in specialties:
        code = stage["code"]
        data = read(OUT / "stages" / code / "practice.json")
        context = HELPER["context"](code, data.get("extra_topic_reasons", {}).keys())
        HELPER["check"](data, context)
        loaded[stage["uid"]] = data
    assert len(specialties) == 72 and sum(len(s["selections"]) for s in specialties) == 322
    totals = Counter()
    counts = Counter()
    scripts = {}
    repeated = []
    catalogue = []
    for stage in specialties:
        code = stage["code"]
        folder = OUT / "stages" / code
        data = loaded[stage["uid"]]
        write(folder / "practice.json", data)
        by_item = {item["item_id"]: item["practice"] for item in data["items"]}
        for selection in stage["selections"]:
            examples = by_item[selection["id"]]
            selection["practice"] = examples
            counts[len(examples)] += 1
            for example in examples:
                script = tuple("".join(t["ja"].split()) for t in example["turns"])
                if script in scripts:
                    repeated.append({"first": scripts[script], "next": example["id"]})
                scripts[script] = example["id"]
                totals[example["type"]] += 1
                totals["examples"] += 1
                totals["turns"] += len(example["turns"])
        source = BASE / "stages" / code
        manifest = read(source / "manifest.json")
        for name in ("source_raw.md", "lesson.md"):
            (folder / name).write_bytes((source / name).read_bytes())
        manifest.update(roadmap_version="10.0",
                        origin_bundle=source.relative_to(ROOT).as_posix())
        manifest["files"]["practice.json"] = {"path": "practice.json", "sha256": digest(folder / "practice.json")}
        write(folder / "manifest.json", manifest)
        catalogue.append({"stage_code": code, "stage_uid": stage["uid"], "level": stage["level"],
                          "title": stage["title"], "items": len(stage["selections"]),
                          "examples": sum(len(v) for v in by_item.values()),
                          "manifest": code + "/manifest.json", "manifest_sha256": digest(folder / "manifest.json")})
    if repeated:
        write(OUT / "QA_DUPLICATES.json", repeated)
        raise ValueError("Repeated practice scripts require review; see QA_DUPLICATES.json")
    rows = [json.loads(line) for line in (BASE / "KAIWA_CHANG_V9_2.jsonl").read_text("utf8").splitlines()]
    for row in rows:
        if row["uid"] in loaded:
            row["practice_by_item"] = loaded[row["uid"]]["items"]
    (OUT / "KAIWA_CHANG_V10.jsonl").write_bytes(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows).encode("utf8"))
    write(OUT / "learner.json", payload)
    (OUT / "chang_registry.json").write_bytes((BASE / "chang_registry.json").read_bytes())
    (OUT / "edits").mkdir(exist_ok=True)
    for source in (BASE / "edits").glob("*.json"):
        (OUT / "edits" / source.name).write_bytes(source.read_bytes())
    policy = read(BASE / "SOURCE_POLICY.json")
    policy.update(version="10.0", basis="../v9_2/KAIWA_CHANG_V9_2.jsonl",
                  additional_practice="ai_authored; linked to following topic situations")
    write(OUT / "SOURCE_POLICY.json", policy)
    write(OUT / "stages/index.json", {"version": "10.0", "stages": catalogue})
    status = read(BASE / "STATUS.json")
    status.update(version="10.0", specialty_items=322, practice=dict(totals),
                  examples_per_item=dict(counts), basis_sha256=digest(BASE / "KAIWA_CHANG_V9_2.jsonl"))
    write(OUT / "STATUS.json", status)
    lines = ["# V10 · Ví dụ luyện nói trong chuyên đề", "",
             f"{len(specialties)} chặng chuyên đề, 322 bài, {totals['examples']} ví dụ mới và {totals['turns']} lượt nói.",
             "", "Phần luyện mới được biên soạn bằng AI dựa vào cách dùng trong bài và các tình huống topic phía sau.",
             "Raw và bản biên tập nguồn nằm trong từng thư mục stages cùng manifest và practice.json.",
             "", "## Số liệu theo cấp", ""]
    for level in ("Sơ", "Trung", "Thượng"):
        group = [s for s in catalogue if s["level"] == level]
        lines.append(f"- {level} có {len(group)} chuyên đề, {sum(s['items'] for s in group)} bài và {sum(s['examples'] for s in group)} ví dụ mới.")
    lines += ["", "## Kiểm tra trước phát hành", "",
              "- Kiểm cấu trúc, ID và liên kết tình huống của từng file practice.json bằng công cụ của skill.",
              "- Giữ đúng thứ tự 365 chặng và thứ tự 322 bài từ V9.2.",
              "- Đối chiếu raw và bản biên tập với gói nguồn V9.2.",
              "- Kiểm kịch bản luyện trùng nguyên chuỗi trên toàn bộ phần mới.",
              "", "Công cụ xác nhận cấu trúc và tính toàn vẹn dữ liệu. Lượt đọc biên tập kiểm cách dùng, lời đáp và bản dịch.",
              ""]
    (OUT / "REPORT_V10.md").write_bytes("\n".join(lines).encode("utf8"))
    template = (ROOT / "tools/review_site.html").read_text("utf8")
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
    html = template.replace("__COURSE_DATA__", encoded)
    (OUT / "ROADMAP.html").write_bytes(html.encode("utf8"))
    if publish:
        (ROOT / "docs/index.html").write_bytes(html.encode("utf8"))
        write(PLANNING / "CURRENT_ROADMAP.json", {
            "version": "10.0", "registry": "kaiwa_skill/planning/v10/chang_registry.json",
            "roadmap": "kaiwa_skill/planning/v10/KAIWA_CHANG_V10.jsonl",
            "policy": "kaiwa_skill/planning/v10/SOURCE_POLICY.json"})
    print(json.dumps(status, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    build(parser.parse_args().publish)
