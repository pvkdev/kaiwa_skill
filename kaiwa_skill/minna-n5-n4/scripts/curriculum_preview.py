"""Package the local, reviewed curriculum material for migration preview (no network)."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

from grammar_practice_order import make_order
from course_coverage import coverage

ROOT = Path(__file__).resolve().parents[1]
NATIVE = ROOT / "exports/curriculum-exercises"


def read(path):
    return json.loads(path.read_bytes())


def payload(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()


def roadmap(lesson, inventory):
    n = lesson["lesson"]
    prefix = f"minna.l{n:02}"
    nodes = [
        {"id": f"{prefix}.v01.vocabulary_video", "kind": "vocabulary_video",
         "status": "planned", "source_rows": [1, inventory["words"]]},
        {"id": f"{prefix}.v01.vocabulary_learning", "kind": "vocabulary_learning",
         "status": "needs_harumii_binding", "source_rows": [1, inventory["words"]]},
    ]
    for group in lesson["groups"]:
        ref = group["grammar_ref"]
        nodes.append({"id":group["video_asset"],"kind":"grammar_video","status":"planned",
                      "grammar_ref":ref,"text_available":True})
        nodes.append({"id":group["video_asset"].removesuffix(".video")+".practice","kind":"grammar_practice",
                      "status":"authored_preview","grammar_ref":ref})
    available = lesson.get("supplements",{})
    for family in ("shadowing","listening","short_reading","long_reading",
                   "conversation_video","renshuu_c","kaiwa","assessment"):
        source = "conversation" if family in {"renshuu_c","kaiwa"} else family
        status = "planned" if family == "conversation_video" else inventory["states"].get(source,"pending")
        if source in ("assessment","listening") and source+"_exercises" in available:
            status = "authored_preview"
        elif source in available:
            status = "authored_preview" if family.endswith("reading") and "reading_exercises" in available else "normalized"
        nodes.append({"id":f"{prefix}.{family}","kind":family,"status":status,
                      "optional":family in {"listening","short_reading","long_reading"}})
    return nodes


def collect_lesson(row, totals):
    n = row["lesson"]
    folder = f"lesson-{n:02}"
    pairs = row["grammar_practice_pairs"]
    rank = {p["grammar_ref"]:i for i,p in enumerate(pairs)}
    groups = [[] for _ in pairs]
    for bank in ("quick-checks","renshuu","renshuu-drills"):
        author_file = ROOT/f"authored/{bank}/{folder}.json"
        if bank == "renshuu-drills" and not author_file.exists():
            continue
        author = read(author_file)
        index_path = NATIVE/bank/folder/"index.json"
        rows = {s["id"]:s for s in read(index_path)["sections"]}
        if len(rows) != len(author["items"]):
            raise ValueError(f"{index_path}: regenerate for the current number of items")
        for q in author["items"]:
            native = rows[q["id"]+".section"]
            refs = q["grammar_refs"]
            if native["placement_after_grammar_refs"] != refs:
                raise ValueError(f"{q['id']}: native placement mismatch")
            storage = read(index_path.parent/native["storage_file"])
            [dto] = storage["content"]["questions"]
            if dto.get("explanation") != q["explanation_vi"]:
                raise ValueError(f"{q['id']}: stale explanation")
            if q["kind"] == "manualQnA":
                correct = next(c["text"] for c in q["choices"] if c["id"] == q["correct"])
                i = dto["correct_index"]
                if not (0 <= i < len(dto["choices"]) and dto["choices"][i] == correct):
                    raise ValueError(f"{q['id']}: stale single-choice key")
            elif q["kind"] == "manualFillInBlank" and dto["blank_answers"] != [q["correct"]]:
                raise ValueError(f"{q['id']}: stale blank answer")
            elif q["kind"] == "manualMultiSelect":
                expected = {c["text"] for c in q["choices"] if c["id"] in q["correct"]}
                actual = {dto["choices"][i] for i in dto["correct_indices"]}
                if expected != actual or len(expected) != len(q["correct"]):
                    raise ValueError(f"{q['id']}: stale multi-select answers")
            pos = max(rank[r] for r in refs)
            groups[pos].append({"id":q["id"], "bank":bank, "kind":native["kind"],
                                "source_id":q["source_id"], "grammar_refs":refs,
                                "provenance":q["provenance"], "storage":storage})
            totals[bank] += 1
    doc = read(ROOT / row["normalized"])
    for i,p in enumerate(pairs):
        teaching = doc["points"][i]
        if teaching["id"] != p["grammar_ref"]:
            raise ValueError(f"Lesson {n}: source order mismatch")
        groups[i] = {"grammar_ref":teaching["id"], "title":teaching["title"],
                     "video_asset":p["video_asset"], "video_status":"planned",
                     "formula":teaching["formula"], "meaning":teaching["meaning"], "usage":teaching["usage"],
                     "examples":teaching["examples"], "practice":groups[i]}
    totals["grammar_video_practice_pairs"] += len(groups)
    return {"lesson":n, "grammar_source":doc["source_url"], "source_snapshot":doc["source_snapshot"],
            "media_context":doc["media_context"], "groups":groups}


def main():
    order,_ = make_order()
    inventory = {r["lesson"]:r for r in coverage()}
    files, totals = {},Counter()
    for row in order:
        n = row["lesson"]
        lesson = collect_lesson(row,totals)
        for family in ("shadowing","conversation","short_reading","long_reading"):
            path = ROOT/f"normalized/lesson-{n:02}/{family}.json"
            if path.is_file():
                name = f"supplements/{n:02}/{family}.json"
                files[name] = path.read_bytes()
                lesson.setdefault("supplements",{})[family] = name
        if n == 39:
            name = "supplements/39/reading-exercises.json"
            reading_dir = NATIVE/"reading"/"lesson-39"
            idx = read(reading_dir/"index.json")
            sources = read(ROOT/"authored/lesson-39/reading.json")["sections"]
            sections = []
            for source, native in zip(sources, idx["sections"], strict=True):
                if source["id"] != native["id"]:
                    raise ValueError("Outdated reading export")
                sections.append({"id":source["id"],"optional":True,"source_snapshot":source["source_snapshot"],
                                 "question_provenance":source["question_provenance"],
                                 "answer_provenance":"ai_editorial",
                                 "evidence":{q["id"]:q["evidence_paragraph_id"] for q in source["questions"]},
                                 "storage":read(reading_dir/native["storage_file"])})
            files[name] = payload(sections)
            lesson.setdefault("supplements",{})["reading_exercises"] = name
        for family in ("assessment","listening"):
            source_path = ROOT/f"authored/lesson-{n:02}/{family}.json"
            if not source_path.exists():
                continue
            source_doc = read(source_path)
            native_dir = NATIVE/family/f"lesson-{n:02}"
            native_rows = read(native_dir/"index.json")["sections"]
            sections = []
            for src, native in zip(source_doc["sections"], native_rows, strict=True):
                if src["id"] != native["id"]:
                    raise ValueError(f"Outdated {family} export {n}")
                sec = {"id":src["id"],"kind":native["kind"],"question_count":native["question_count"],
                       "answer_provenance":"ai_editorial","source_section":src,
                       "storage":read(native_dir/native["storage_file"])}
                local = src.get("media",{}).get("local_asset")
                if local:
                    audio_file = (ROOT/local).resolve()
                    audio_file.relative_to(ROOT/"authored")
                    audio_member = f"supplements/{n:02}/audio/{audio_file.name}"
                    files[audio_member] = audio_file.read_bytes()
                    sec["audio_file"] = audio_member
                    sec["pending_audio_media_ids"] = native.get("pending_audio_media_ids",[])
                sections.append(sec)
            name = f"supplements/{n:02}/{family}-exercises.json"
            files[name] = payload({"source_snapshot":source_doc.get("source_snapshot"),"sections":sections})
            lesson.setdefault("supplements",{})[family+"_exercises"] = name
        vocab = inventory[n]
        vocab_ref = f"references/vocabulary/{n:02}.md"
        files[vocab_ref] = (ROOT/vocab["vocab"]).read_bytes()
        lesson["vocabulary"] = {"origin":"harumii_export","source_file":vocab["vocab"],"path":vocab_ref,
                                "word_count":vocab["words"],"binding_status":"needs_target_ids"}
        lesson["nodes"] = roadmap(lesson,vocab)
        files[f"lessons/{n:02}.json"] = payload(lesson)
    sample_dir = NATIVE/"lesson-39"
    sample = read(sample_dir/"index.json")
    files["samples/lesson-39/templates.json"] = payload([
        {**{k:v for k,v in section.items() if k not in ("storage_file","paste_file")},
         "storage":read(sample_dir/section["storage_file"])} for section in sample["sections"]])
    sample_audio = "authored/lesson-39/templates/audio/earthquake-news.mp3"
    files["samples/lesson-39/earthquake-news.mp3"] = (ROOT/sample_audio).read_bytes()
    pilot = ROOT/"authored/lesson-39/grammar-practice.json"
    files["samples/lesson-39/pilot-r3.json"] = pilot.read_bytes()
    manifest = {"format":"minna-curriculum-preview/v1", "status":"draft", "lesson_count":len(order),
                "counts":dict(totals), "supplements":{"lesson_39_five_templates":"samples/lesson-39/templates.json",
                "pending_listening_asset":"samples/lesson-39/earthquake-news.mp3",
                "lesson_39_pilot":"samples/lesson-39/pilot-r3.json"},
                "sha256":{k:sha256(v).hexdigest() for k,v in files.items()}}
    files["manifest.json"] = payload(manifest)
    bundle_dir = ROOT/"exports/harumii"
    bundle_dir.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=bundle_dir) as tmp:
        draft = Path(tmp)/"preview.zip"
        with ZipFile(draft,"w") as z:
            for name, value in files.items():
                z.writestr(ZipInfo(name,(1980,1,1,0,0,0)),value,compress_type=ZIP_DEFLATED)
        with ZipFile(draft) as z:
            if z.testzip() or any(z.read(k) != v for k,v in files.items()):
                raise ValueError("Export bytes mismatch")
        target = bundle_dir/"minna-50-exercises-preview.zip"
        draft.replace(target)
    print(f"{target}: {dict(totals)}")


if __name__ == "__main__":
    main()
