"""Build or verify a reproducible Harumii grammar/practice draft (Python 3.10+)."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import tempfile
from zipfile import ZipFile, ZipInfo

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "contracts/harumii-minna/v1"


def require(test, message):
    if not test:
        raise ValueError(message)


def as_bytes(obj):
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def schema_check(data, name):
    schema = json.loads((SCHEMAS / (name + ".schema.json")).read_bytes())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(data)


def project(lesson):
    schema_check(lesson, "grammar-practice")
    seen = set()
    prefix = f"minna.l{lesson['lesson_number']:02d}."

    def register(key):
        require(key.startswith(prefix) and key not in seen, f"Invalid/duplicate ID: {key}")
        seen.add(key)

    assets = {}
    for asset in lesson["assets"]:
        register(asset["id"])
        require((asset["status"] == "available") == bool(asset["playback_url"]), asset["id"])
        assets[asset["id"]] = asset

    tasks, exercises, taught, used_media, source_ids = [], [], set(), set(), set()
    nodes = lesson["nodes"]
    require(len(nodes) % 2 == 0, "Each grammar video needs a practice node")
    for grammar, practice in zip(nodes[::2], nodes[1::2]):
        require(grammar["kind"] == "grammar_video" and practice["kind"] == "grammar_practice",
                "Expected alternating grammar video and practice")
        gid = grammar["id"]
        register(gid)
        register(practice["id"])
        require(practice["after"] == gid, "Practice must follow its grammar video")
        vid = grammar["video_asset_id"]
        require(vid in assets and vid not in used_media, f"Missing/shared grammar video: {vid}")
        used_media.add(vid)
        taught.add(gid)
        tasks.append({"node_id": gid, "task_type": "Grammar", "relative_order": len(tasks)+1,
                      "grammar_entry_binding": gid, "video_asset_id": vid})
        refs = []
        for group in practice["groups"]:
            register(group["id"])
            targets = set(group["grammar_refs"])
            require(gid in targets and targets <= taught, f"Misplaced group: {group['id']}")
            questions = []
            for item in group["items"]:
                register(item["id"])
                sid = item["source_item_id"]
                if item["edit"] == "new_practice":
                    require(sid is None and group["source_group_id"] is None and
                            item["ai_note_for_source_vi"] is None, "Supplement attributed to source")
                else:
                    require(sid and group["source_group_id"] and sid.startswith(group["source_group_id"]+"-")
                            and sid not in source_ids, f"Invalid source item {sid}")
                    source_ids.add(sid)
                choices = item["choices"]
                ids = [c["id"] for c in choices]
                texts = [c["text"] for c in choices]
                require(len(set(ids)) == len(set(t.strip() for t in texts)) == len(ids)
                        and item["correct_choice_id"] in ids, f"Invalid answers in {item['id']}")
                questions.append({"type": "jaToVi", "question_ja": item["prompt_ja"],
                                  "question": item["instruction_vi"], "choices": texts,
                                  "correct_index": ids.index(item["correct_choice_id"]),
                                  "explanation": item["explanation_vi"]})
            refs.append(group["id"])
            exercises.append({"exercise_id": group["id"], "template_format": "QuizMultipleChoice",
                              "item_ids": [q["id"] for q in group["items"]],
                              "content": {"section_type": "QnA4Answer", "variant": "jaToVi",
                                          "is_manual": True, "choice_count": 4, "questions": questions}})
        tasks.append({"node_id": practice["id"], "task_type": "Exercise",
                      "relative_order": len(tasks)+1, "grammar_exercise_refs": refs})
    require(used_media == set(assets), "Orphaned video asset")
    return {"tasks": tasks, "exercises": exercises}


def package_parts(lesson):
    projection = project(lesson)
    files = {"lesson.json": as_bytes(lesson), "projection.json": as_bytes(projection)}
    manifest = {k: lesson[k] for k in ("format_version", "course_id", "lesson_number",
                                       "revision", "state", "scope")}
    manifest["files"] = {name: sha256(blob).hexdigest() for name, blob in files.items()}
    schema_check(manifest, "manifest")
    return {"manifest.json": as_bytes(manifest), **files}


def verify(path):
    with ZipFile(path) as archive:
        require(sorted(archive.namelist()) == ["lesson.json", "manifest.json", "projection.json"],
                "Invalid file list or duplicate entry")
        require(all(i.file_size <= 16_000_000 for i in archive.infolist()), "Oversized lesson")
        lesson = json.loads(archive.read("lesson.json"))
        for name, expected in package_parts(lesson).items():
            require(archive.read(name) == expected, f"{name} differs from canonical output")
    return lesson


def build(source, dest):
    lesson = json.loads(source.read_bytes())
    parts = package_parts(lesson)
    out = dest / f"lesson-{lesson['lesson_number']:02d}" / lesson["scope"]
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"r{lesson['revision']:04d}.zip"
    with tempfile.TemporaryDirectory(dir=out) as tmp:
        draft = Path(tmp) / "new.zip"
        with ZipFile(draft, "w") as archive:
            for name, value in parts.items():
                info = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, value)
        verify(draft)
        try:
            target.hardlink_to(draft)
        except FileExistsError:
            require(target.read_bytes() == draft.read_bytes(),
                    f"Revision conflict: {target}. Increase revision for an edited lesson.")
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    cmds = parser.add_subparsers(dest="command", required=True)
    builder = cmds.add_parser("build")
    builder.add_argument("lesson", type=Path)
    builder.add_argument("--out", type=Path, default=ROOT / "exports/harumii")
    checker = cmds.add_parser("verify")
    checker.add_argument("package", type=Path)
    args = parser.parse_args()
    if args.command == "build":
        print(build(args.lesson, args.out))
    else:
        data = verify(args.package)
        print(f"Verified {data['course_id']} / {data['lesson_number']} / {data['scope']} / r{data['revision']}")
