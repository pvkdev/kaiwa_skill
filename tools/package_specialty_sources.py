"""Bundle V9.2 specialty source excerpts and edited lessons for video preparation."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLANNING = ROOT / "kaiwa_skill/planning"
RELEASE = PLANNING / "v9_2"
OUTPUT = RELEASE / "stages"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(path.read_text("utf8"))


def relative(path):
    return path.relative_to(ROOT).as_posix()


def write_json(path, data):
    path.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf8"))


def source_excerpt(span):
    path = ROOT / span["path"]
    data = path.read_bytes()
    if digest(data) != span["sha256"]:
        raise ValueError("Source book changed: " + span["path"])
    lines = data.decode("utf-8-sig").splitlines()
    start, end = span["start_line"], span["end_line"]
    if not 1 <= start <= end <= len(lines):
        raise ValueError("Invalid source lines: " + span["path"])
    excerpt = "\n".join(lines[start - 1:end])
    if digest(excerpt.encode("utf8")) != span["excerpt_sha256"]:
        raise ValueError("Source excerpt changed: " + span["path"])
    return excerpt


def append_section(lines, heading, text):
    lines.extend(heading.splitlines() + [""])
    start = len(lines) + 1
    lines.extend(text.split("\n"))
    end = len(lines)
    lines.extend(["", "---", ""])
    return {"start_line": start, "end_line": end, "sha256": digest(text.encode("utf8"))}


def package(stage):
    key = stage["code"]
    admin_path = PLANNING / "v9/admin" / (key + ".json")
    admin = read(admin_path)
    if admin["uid"] != stage["uid"]:
        raise ValueError("Specialty UID mismatch: " + key)
    records = {m["id"]: m for m in admin["materials"]}
    folder = OUTPUT / key
    folder.mkdir(parents=True, exist_ok=True)
    raw = ["# Nguồn nguyên văn · " + stage["title"], ""]
    edited = ["# " + stage["title"], ""]
    items = []
    for selection in stage["selections"]:
        material = records[selection["id"]]
        source_material = PLANNING / "v9" / material["file"]
        material_bytes = source_material.read_bytes()
        if digest(material_bytes) != material["sha256"]:
            raise ValueError("Edited material changed: " + material["id"])
        edited_text = "\n".join(material_bytes.decode("utf8").splitlines()).rstrip("\n")
        edited_range = append_section(edited, "## " + selection["title"], edited_text)
        excerpts = []
        for span in material["source_spans"]:
            excerpt = source_excerpt(span)
            heading = ("## " + selection["title"] + "\n\n"
                       + span["book_title"] + " · Dòng " + str(span["start_line"])
                       + "–" + str(span["end_line"]))
            excerpt_range = append_section(raw, heading, excerpt)
            excerpts.append(dict(span, bundled_excerpt=excerpt_range))
        items.append({"id": selection["id"], "title": selection["title"],
                      "category": selection["category"], "section_title": selection["section_title"],
                      "source_material": relative(source_material), "source_material_sha256": material["sha256"],
                      "edited_excerpt": edited_range, "source_spans": excerpts,
                      "summary_vi": material["summary_vi"], "reading_note_vi": material["reading_note_vi"]})
    for name, lines in (("source_raw.md", raw), ("lesson.md", edited)):
        (folder / name).write_bytes(("\n".join(lines).rstrip("\n") + "\n").encode("utf8"))
    manifest = {"schema_version": "1.0", "roadmap_version": "9.2", "stage_uid": stage["uid"],
                "stage_code": key, "title": stage["title"], "level": stage["level"],
                "roadmap_number": stage["number"], "purpose": "video_lecture_preparation",
                "source_admin": relative(admin_path), "source_admin_sha256": digest(admin_path.read_bytes()),
                "path_conventions": "source paths are repository-relative; bundled files are manifest-relative",
                "excerpt_conventions": "inclusive 1-based lines; raw text preserves source characters with LF newlines",
                "scope": "Only source spans already selected for this specialty; edited text is the existing learner material.",
                "files": {name: {"path": name, "sha256": digest((folder / name).read_bytes())}
                          for name in ("source_raw.md", "lesson.md")}, "items": items}
    write_json(folder / "manifest.json", manifest)
    return manifest


def verify(stage):
    folder = OUTPUT / stage["code"]
    manifest = read(folder / "manifest.json")
    assert manifest["stage_uid"] == stage["uid"]
    assert [m["id"] for m in manifest["items"]] == [s["id"] for s in stage["selections"]]
    for record in manifest["files"].values():
        assert digest((folder / record["path"]).read_bytes()) == record["sha256"]
    raw = (folder / "source_raw.md").read_text("utf8").splitlines()
    edited = (folder / "lesson.md").read_text("utf8").splitlines()
    for item in manifest["items"]:
        reference = item["edited_excerpt"]
        bundled = "\n".join(edited[reference["start_line"] - 1:reference["end_line"]])
        original = (ROOT / item["source_material"]).read_bytes()
        assert digest(original) == item["source_material_sha256"]
        assert bundled == "\n".join(original.decode("utf8").splitlines()).rstrip("\n")
        assert digest(bundled.encode("utf8")) == reference["sha256"]
        for span in item["source_spans"]:
            reference = span["bundled_excerpt"]
            bundled = "\n".join(raw[reference["start_line"] - 1:reference["end_line"]])
            assert bundled == source_excerpt(span), (stage["code"], item["id"])
            assert digest(bundled.encode("utf8")) == reference["sha256"]
    return manifest


def write_index(stages):
    entries = []
    for stage in stages:
        folder = OUTPUT / stage["code"]
        manifest_path = folder / "manifest.json"
        manifest = read(manifest_path)
        entries.append({"stage_uid": stage["uid"], "stage_code": stage["code"],
                        "title": stage["title"], "level": stage["level"],
                        "roadmap_number": stage["number"], "item_count": len(manifest["items"]),
                        "manifest": stage["code"] + "/manifest.json",
                        "manifest_sha256": digest(manifest_path.read_bytes())})
    write_json(OUTPUT / "index.json", {"schema_version": "1.0", "roadmap_version": "9.2",
                                     "stage_count": len(entries),
                                     "item_count": sum(e["item_count"] for e in entries), "stages": entries})
    lines = ["# Tài nguyên chuyên đề để chuẩn bị video", "",
             "Mỗi thư mục ứng với một chặng chuyên đề trong V9.2, theo đúng thứ tự lộ trình.", "",
             "- `source_raw.md` gom nguyên văn các đoạn đã chọn từ bản sách Markdown trong knowledge.",
             "- `lesson.md` gom các bài đã biên tập đang dùng trong lộ trình.",
             "- `manifest.json` ghi tên/mã sách, đường dẫn, dòng nguồn, hash và vị trí đoạn trong hai file.",
             "", "Phạm vi raw là các đoạn nguồn đã chọn cho chặng. Các tiêu đề phân cách do công cụ đóng gói thêm.",
             "Nội dung bên trong từng đoạn giữ nguyên chữ, chuẩn hóa xuống dòng LF. Dải dòng bắt đầu và kết thúc tính từ 1, bao gồm cả hai đầu.",
             "Đường dẫn nguồn trong manifest tính từ gốc repo. Đường dẫn file đóng gói tính từ thư mục chứa manifest.",
             "", "Có thể dùng raw cùng bản biên tập để soạn video. Hồ sơ tuyển chọn gốc ở `planning/v9/admin`.",
             "", "Tạo lại bằng `py -X utf8 tools/package_specialty_sources.py --index` tại gốc repo.",
             "Kiểm tra lại bằng `py -X utf8 tools/package_specialty_sources.py --verify-only --index`.", ""]
    level = None
    for entry in entries:
        if entry["level"] != level:
            level = entry["level"]
            lines.extend(["", "## " + level, ""])
        code = entry["stage_code"]
        lines.append("- **" + entry["title"] + "** · " + str(entry["item_count"])
                     + " bài · [Raw](" + code + "/source_raw.md) · [Bản biên tập]("
                     + code + "/lesson.md) · [Nguồn](" + code + "/manifest.json)")
    (OUTPUT / "README.md").write_bytes(("\n".join(lines) + "\n").encode("utf8"))


def run(level=None, verify_only=False, index=False):
    stages = [s for s in read(RELEASE / "learner.json")["stages"]
              if s["stage_kind"] == "speak_japanese" and (level is None or s["level"] == level)]
    for stage in stages:
        if not verify_only:
            package(stage)
        verify(stage)
    if index:
        write_index(stages)
    print(json.dumps({"level": level or "all", "stages": len(stages),
                      "items": sum(len(s["selections"]) for s in stages)}, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=["Sơ", "Trung", "Thượng"])
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--index", action="store_true", help="Write the full specialty catalogue after verification")
    arguments = parser.parse_args()
    if arguments.index and arguments.level:
        parser.error("--index requires all levels")
    run(arguments.level, arguments.verify_only, arguments.index)
