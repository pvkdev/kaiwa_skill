"""Local, single-writer stage drafts and immutable revisions. Python standard library."""
import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import uuid
from datetime import datetime, timezone


def now():
    return datetime.now(timezone.utc).isoformat()


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with temp.open("w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(root, relative):
    path = (root / relative).resolve()
    if path == root.resolve() or not path.is_relative_to(root.resolve()):
        raise ValueError("Path outside expected directory: " + str(relative))
    return path


def curriculum_spec(repo, pinned=None):
    """Resolve the published curriculum, or a draft's explicitly pinned version."""
    pointer = repo / "kaiwa_skill/planning/CURRENT_ROADMAP.json"
    spec = pinned or (read(pointer) if pointer.exists() else {
        "version": "4.1", "registry": "kaiwa_skill/planning/v2/chang_registry.json",
        "roadmap": "kaiwa_skill/planning/v2/KAIWA_CHANG_V4_1.jsonl",
        "policy": "kaiwa_skill/planning/v2/KAIWA_CHANG_V4_1_META.json"})
    for field in ["registry", "roadmap", "policy"]:
        if not isinstance(spec.get(field), str):
            raise ValueError("Curriculum pointer needs " + field)
        inside(repo, spec[field])
    return {k: spec[k] for k in ["version", "registry", "roadmap", "policy"]}


def hashes(draft):
    result = {}
    for path in sorted(draft.rglob("*")):
        if path.is_file():
            if path.is_symlink() or not path.resolve().is_relative_to(draft.resolve()):
                raise ValueError("Draft must not contain external links")
            if path.suffix not in {".md", ".json", ".jsonl"}:
                raise ValueError("Text content only: " + str(path))
            result[path.relative_to(draft).as_posix()] = sha(path)
    return result


@contextlib.contextmanager
def guard(stage):
    stage.mkdir(parents=True, exist_ok=True)
    path = stage / ".mutation.lock"
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        raise ValueError("Mutation lock exists; stop the old process before explicit recovery")
    try:
        with os.fdopen(fd, "w") as f:
            f.write(str(os.getpid()))
        yield
    finally:
        path.unlink(missing_ok=True)


def source_pins(repo, draft):
    pins = {}
    for entry in read(draft / "sources.json").get("entries", []):
        if entry.get("path"):
            p = inside(repo, entry["path"])
            actual = sha(p)
            if entry.get("sha256") != actual:
                raise ValueError("Source missing/stale hash: " + entry["path"])
            pins[entry["path"]] = actual
    return pins


def item_ids(value):
    """IDs of sentence/list items and dialogue turns, for content references."""
    if isinstance(value, dict):
        return ({value["id"]} if value.get("id") else set()) | set().union(*(item_ids(v) for v in value.values()))
    if isinstance(value, list):
        return set().union(*(item_ids(v) for v in value))
    return set()


def lesson_key(ref):
    return (ref["stage_uid"], ref.get("revision"), ref["lesson_id"])


def prior_lesson(ref, draft, stage, repo):
    uid, revision, lid = lesson_key(ref)
    if uid == stage["stage_uid"]:
        if revision is not None:
            raise ValueError("Local lesson references must use revision null")
        content, pins = draft, {}
    else:
        uid = str(uuid.UUID(uid))
        if not revision or not re.fullmatch(r"r\d{4,}", revision):
            raise ValueError("Earlier stage lesson needs a finalized revision")
        curriculum = curriculum_spec(repo, stage.get("curriculum"))
        registry = read(inside(repo, curriculum["registry"]))
        roadmap = inside(repo, curriculum["roadmap"])
        order = [json.loads(s)["uid"] for s in roadmap.read_text(encoding="utf-8-sig").splitlines() if s.strip()] if roadmap.exists() else list(registry)
        if uid not in registry or uid not in order or stage["stage_uid"] not in order or order.index(uid) >= order.index(stage["stage_uid"]):
            raise ValueError("Lookback must point to an earlier curriculum stage")
        previous = repo / "kaiwa_skill/courseware" / uid
        pointer = previous / "current.json"
        if read(pointer)["revision"] != revision:
            raise ValueError("Earlier lesson revision changed; reread and update lookback: " + uid)
        revision_root = previous / "revisions" / revision
        content = revision_root / "content"
        manifest_path = revision_root / "manifest.json"
        manifest = read(manifest_path)
        pins = {pointer.relative_to(repo).as_posix(): sha(pointer), manifest_path.relative_to(repo).as_posix(): sha(manifest_path)}
        for name in ["stage.json", "learning-map.json"]:
            path = content / name
            if manifest["files"].get(name) != sha(path):
                raise ValueError("Previous revision content changed: " + str(path))
            pins[path.relative_to(repo).as_posix()] = sha(path)
    previous_map = read(content / "learning-map.json")
    lesson = next((l for l in previous_map["lessons"] if l["id"] == lid), None)
    if lesson is None:
        raise ValueError("Unknown earlier lesson: " + lid)
    previous_stage = read(content / "stage.json")
    if previous_stage["stage_uid"] != uid or previous_map["stage_uid"] != uid:
        raise ValueError("Previous lesson stage UID mismatch")
    nodes = {n["id"]: n for n in previous_stage["nodes"]}
    if uid != stage["stage_uid"]:
        for nid in lesson["node_ids"]:
            path = inside(content, nodes[nid]["path"])
            if manifest["files"].get(nodes[nid]["path"]) != sha(path):
                raise ValueError("Previous lesson file changed: " + str(path))
            pins[path.relative_to(repo).as_posix()] = sha(path)
    return lesson, nodes, content, pins


def learning_pins(repo, draft):
    path = draft / "learning-map.json"
    if not path.exists():
        return {}
    stage = read(draft / "stage.json")
    pins, seen = {}, set()
    for lesson in read(path)["lessons"]:
        for ref in lesson.get("lookback", []):
            key = lesson_key(ref)
            if key not in seen:
                pins.update(prior_lesson(ref, draft, stage, repo)[3])
                seen.add(key)
    return pins


def validate_learning(draft, stage, repo, errors):
    learning = read(draft / "learning-map.json")
    lessons = learning.get("lessons", [])
    lids = [l["id"] for l in lessons]
    if learning.get("schema_version") != "1.0" or learning.get("stage_uid") != stage["stage_uid"]:
        errors.append("learning-map schema/stage UID mismatch")
    if not lessons or len(set(lids)) != len(lids):
        errors.append("Learning map needs distinct lessons")
    expected = [n["id"] for n in stage["nodes"] if n["type"] != "live_context"]
    if [nid for l in lessons for nid in l["node_ids"]] != expected:
        errors.append("Lesson node groups must partition all non-live nodes in order")
    nodes = {n["id"]: n for n in stage["nodes"]}
    review_targets = set()
    for i, lesson in enumerate(lessons):
        if not lesson.get("summary"):
            errors.append("Lesson needs a summary of new content: " + lesson["id"])
        if not lesson.get("reuse") and not lesson.get("reason_no_reuse") and not lesson.get("pending_previous"):
            errors.append("Missing reuse or an editorial reason: " + lesson["id"])
        looked = {}
        for ref in lesson.get("lookback", []):
            if ref["stage_uid"] == stage["stage_uid"] and (ref["lesson_id"] not in lids or lids.index(ref["lesson_id"]) >= i):
                errors.append("Lookback cannot point to the same/future lesson: " + lesson["id"])
                continue
            looked[lesson_key(ref)] = prior_lesson(ref, draft, stage, repo)
        for reuse in lesson.get("reuse", []):
            ref = reuse["from"]
            if lesson_key(ref) not in looked:
                errors.append("Reuse source must be in reviewed lookback: " + lesson["id"])
                continue
            old_lesson, old_nodes, old_content, _ = looked[lesson_key(ref)]
            if ref["node_id"] not in old_lesson["node_ids"]:
                errors.append("Reuse source node not in earlier lesson")
                continue
            old_node = old_nodes[ref["node_id"]]
            if ref.get("item_id"):
                if old_node["type"] == "knowledge" or ref["item_id"] not in item_ids(read(inside(old_content, old_node["path"]))):
                    errors.append("Unknown earlier vocabulary/example/turn ID")
            if not reuse.get("purpose") or not reuse.get("in"):
                errors.append("Reuse needs a purpose and actual target")
            for use in reuse.get("in", []):
                nid = use["node_id"]
                if nid not in lesson["node_ids"] or nid not in nodes:
                    errors.append("Reuse target must be in its current lesson")
                    continue
                target = nodes[nid]
                if use.get("item_id") and (target["type"] == "knowledge" or use["item_id"] not in item_ids(read(inside(draft, target["path"])))):
                    errors.append("Unknown reuse target item/turn ID")
                if old_node["type"] == "vocabulary" and ref.get("item_id"):
                    review_targets.add((nid, use.get("item_id")))
    for n in stage["nodes"]:
        if n["type"] == "vocabulary":
            for word in read(inside(draft, n["path"]))["items"]:
                if word.get("exposure") not in {"new", "review"}:
                    errors.append("Vocabulary item needs new/review exposure: " + word["id"])
                if word.get("exposure") == "review" and (n["id"], word["id"]) not in review_targets:
                    errors.append("Review word needs a link to its earlier vocabulary item: " + word["id"])


def check_dialogue(data, seen, label, errors):
    speakers = data.get("speakers", [])
    if len(speakers) != 2 or {s["id"] for s in speakers} != {"A", "B"}:
        errors.append("Dialogue must have exactly speakers A and B: " + label)
    turns = data.get("turns", [])
    if {t.get("speaker") for t in turns} != {"A", "B"}:
        errors.append("Both roles need speech: " + label)
    for turn in turns:
        tid = turn.get("id")
        if not tid or tid in seen or not turn.get("ja") or not turn.get("vi"):
            errors.append("Missing/duplicate turn ID or text: " + label)
        seen.add(tid)


def check(draft, uid, repo):
    errors = []
    stage = read(draft / "stage.json")
    if stage.get("stage_uid") != uid or stage.get("schema_version") not in {"3.0-draft", "3.1-draft"}:
        errors.append("stage_uid/schema_version mismatch")
    nodes = stage.get("nodes", [])
    ids = [n["id"] for n in nodes]
    paths = [n["path"] for n in nodes]
    if not nodes or len(ids) != len(set(ids)) or len(paths) != len(set(paths)):
        errors.append("Nodes must be nonempty with unique IDs and paths")
    retired = [x["id"] for x in stage.get("retired_ids", [])]
    if set(ids) & set(retired):
        errors.append("Retired node ID reused")
    types = {n["id"]: n["type"] for n in nodes}
    sources = read(draft / "sources.json")
    entries = sources.get("entries", [])
    source_ids = [e["id"] for e in entries]
    if len(source_ids) != len(set(source_ids)):
        errors.append("Duplicate source IDs")
    scan = sources.get("scan", [])
    if sorted(x.get("book_id", "") for x in scan) != [f"B{i:02}" for i in range(1, 28)]:
        errors.append("Source scan must account for B01..B27 once each")
    if any(x.get("status") not in {"index_only", "read"} for x in scan):
        errors.append("Source scan status must be index_only or read")
    for entry in entries:
        if entry.get("kind") == "book" and (entry.get("read_status") != "read" or not entry.get("locator")):
            errors.append("Book use needs actual read status and locator: " + entry["id"])
        for target in entry.get("used_for", []):
            if target not in ids:
                errors.append("Unknown used_for node: " + target)
    live = [n for n in nodes if n["type"] == "live_context"]
    if len(live) != 1:
        errors.append("Exactly one live_context node required")
    events = stage.get("events", [])
    event_ids = [e["id"] for e in events]
    if len(event_ids) != len(set(event_ids)):
        errors.append("Duplicate event IDs")
    for e in events:
        for sid in e.get("situation_ids", []):
            if types.get(sid) != "situation":
                errors.append("Event points to unknown situation: " + sid)
    turns_seen = set()
    for n in nodes:
        p = inside(draft, n["path"])
        if not p.exists() or not p.read_text(encoding="utf-8").strip():
            errors.append("Missing/empty node content: " + n["id"])
            continue
        if n["type"] == "knowledge":
            if p.suffix != ".md":
                errors.append("Knowledge must be Markdown")
            if n.get("source_family") == "speak_japanese":
                index = ids.index(n["id"])
                practice = n.get("practice_node_id")
                if index + 1 >= len(nodes) or ids[index + 1] != practice or types.get(practice) != "shadowing":
                    errors.append("Speak Japanese knowledge must be immediately followed by its shadowing: " + n["id"])
                video = n.get("video", {})
                if video.get("status") not in {"planned", "available"} or (video.get("status") == "planned" and video.get("asset_ref") is not None) or (video.get("status") == "available" and not video.get("asset_ref")):
                    errors.append("Speak Japanese knowledge needs honest planned/available video metadata")
            continue
        if n["type"] not in {"vocabulary", "grammar", "situation", "shadowing", "live_context"}:
            errors.append("Unknown node type: " + n["type"])
            continue
        data = read(p)
        if data.get("id") != n["id"]:
            errors.append("Node content ID mismatch: " + n["id"])
        for ref in data.get("source_refs", []):
            if ref not in source_ids:
                errors.append("Unknown source reference: " + ref)
        if n["type"] in {"vocabulary", "grammar"}:
            items = data.get("items", [])
            if not items or len({i["id"] for i in items}) != len(items):
                errors.append("Empty/duplicate list items: " + n["id"])
            fields = ["ja", "vi"] if n["type"] == "vocabulary" else ["name_ja"]
            if any(not i.get(k) for i in items for k in fields):
                errors.append("Missing vocabulary/grammar names: " + n["id"])
        if n["type"] == "live_context":
            expected = set(ids) - {n["id"]}
            selected = data.get("context_node_ids", [])
            if set(selected) != expected or len(selected) != len(expected):
                errors.append("Live context must include every other node exactly once")
            if data.get("context_export") != "live-context.md":
                errors.append("Live context_export must be live-context.md")
        if n["type"] == "situation":
            for key in ["title", "setting", "communication_goal", "relationship", "outcome"]:
                if not data.get(key):
                    errors.append("Missing situation field: " + n["id"] + "/" + key)
            if data.get("event_id") not in event_ids:
                errors.append("Unknown event_id: " + n["id"])
            else:
                event = next(e for e in events if e["id"] == data["event_id"])
                if n["id"] not in event.get("situation_ids", []):
                    errors.append("Situation not listed in its event: " + n["id"])
            check_dialogue(data, turns_seen, n["id"], errors)
            if data.get("authorship") not in {"source_adaptation", "original_extension"}:
                errors.append("Situation needs truthful authorship: " + n["id"])
            for field, wanted in [("knowledge_ids", "knowledge"), ("vocabulary_ids", "vocabulary"), ("grammar_ids", "grammar"), ("alternative_to", "situation"), ("follows", "situation")]:
                for target in data.get(field, []):
                    if types.get(target) != wanted or target == n["id"]:
                        errors.append("Broken situation relation: " + n["id"] + "/" + target)
        if n["type"] == "shadowing":
            items = data.get("items", [])
            if not items or len({x["id"] for x in items}) != len(items):
                errors.append("Shadowing needs distinct nonempty items: " + n["id"])
            knowledge = data.get("knowledge_ids", [])
            for kid in knowledge:
                if types.get(kid) != "knowledge":
                    errors.append("Unknown shadowing knowledge reference: " + kid)
            paired = [k for k in nodes if k.get("source_family") == "speak_japanese" and k.get("practice_node_id") == n["id"]]
            for k in paired:
                if k["id"] not in knowledge:
                    errors.append("Speak Japanese shadowing needs its knowledge backlink")
            for item in items:
                if item["kind"] == "sentence":
                    if not item.get("ja") or not item.get("vi"):
                        errors.append("Shadowing sentence needs Japanese and Vietnamese")
                elif item["kind"] == "dialogue":
                    check_dialogue(item, turns_seen, item["id"], errors)
                elif item["kind"] == "situation_ref":
                    if types.get(item.get("situation_id")) != "situation":
                        errors.append("Shadowing references unknown situation")
                else:
                    errors.append("Unknown shadowing item kind")
                if item["kind"] != "situation_ref" and item.get("authorship") not in {"source_adaptation", "original_extension"}:
                    errors.append("Shadowing item needs truthful authorship")
                for k in paired:
                    example = item.get("example_id", "")
                    if not example or not re.search(r'''id=["']''' + re.escape(example) + r'''["']''', inside(draft, k["path"]).read_text(encoding="utf-8")):
                        errors.append("Speak Japanese shadowing example missing from knowledge Markdown")
    if not any(n["type"] == "situation" for n in nodes):
        errors.append("A stage needs situations")
    if not (draft / "editorial.md").read_text(encoding="utf-8").strip():
        errors.append("Missing editorial record")
    source_pins(repo, draft)
    if stage.get("schema_version") == "3.1-draft":
        validate_learning(draft, stage, repo, errors)
    if errors:
        raise ValueError("\n".join(errors))
    return stage


def export_context(draft, stage):
    chunks = ["# " + stage["title"], json.dumps({k: v for k, v in stage.items() if k != "nodes"}, ensure_ascii=False, indent=2)]
    for node in stage["nodes"]:
        chunks.extend(["\n## " + node["title"] + " [" + node["id"] + "]", inside(draft, node["path"]).read_text(encoding="utf-8")])
    if (draft / "learning-map.json").exists():
        chunks.extend(["\n## Bài học và nội dung gối đầu", (draft / "learning-map.json").read_text(encoding="utf-8")])
    chunks.extend(["\n## Nguồn và phạm vi chứng cứ", (draft / "sources.json").read_text(encoding="utf-8")])
    (draft / "live-context.md").write_text("\n\n".join(chunks) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["begin", "status", "checkpoint", "pause", "resume", "recover", "validate", "finalize"])
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--stage", required=True, help="Immutable UUID from chang_registry.json")
    parser.add_argument("--run", help="Run UUID returned by begin/recover")
    parser.add_argument("--from-current", action="store_true", help="Begin an upgrade from current revision")
    parser.add_argument("--next", default="", help="Concrete next action for next worker")
    parser.add_argument("--note", default="")
    parser.add_argument("--editor-reviewed", action="store_true", help="Author has actually completed the editorial review")
    parser.add_argument("--ack-stopped", action="store_true", help="Old process has been stopped before recovery")
    parser.add_argument("--clear-stale-guard", action="store_true", help="Recovery only, after confirming old process stopped")
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    uid = str(uuid.UUID(args.stage))
    curriculum = curriculum_spec(repo)
    registry_path = inside(repo, curriculum["registry"])
    registry = read(registry_path)
    if uid not in registry:
        raise ValueError("Unknown stage UUID")
    stage = repo / "kaiwa_skill/courseware" / uid
    owner_path = stage / "owner.json"
    current_path = stage / "current.json"
    if args.command == "status":
        print(json.dumps({"current": read(current_path) if current_path.exists() else None,
                          "owner": read(owner_path) if owner_path.exists() else None,
                          "run": read(stage / "runs" / (str(uuid.UUID(args.run)) + ".json")) if args.run else None}, ensure_ascii=False, indent=2))
        return
    if args.clear_stale_guard:
        if args.command != "recover" or not args.ack_stopped:
            raise ValueError("Only explicit recovery after stopping the old worker may clear a guard")
        (stage / ".mutation.lock").unlink(missing_ok=True)
    with guard(stage):
        current = read(current_path) if current_path.exists() else None
        owner = read(owner_path) if owner_path.exists() else None
        if args.command in {"begin", "recover"}:
            previous = None
            if args.command == "recover":
                if not args.ack_stopped or not args.run:
                    raise ValueError("Recovery needs --run and --ack-stopped")
                previous = read(stage / "runs" / (str(uuid.UUID(args.run)) + ".json"))
                if owner and owner["run"] != args.run:
                    raise ValueError("Cannot replace another owner")
                if current and current.get("run") == previous["run"]:
                    revision = stage / "revisions" / current["revision"]
                    if hashes(revision / "content") != read(revision / "manifest.json")["files"]:
                        raise ValueError("Published revision changed; inspect manually")
                    previous["status"] = "finalized"
                    previous["revision"] = current["revision"]
                    atomic(stage / "runs" / (previous["run"] + ".json"), previous)
                    if owner:
                        owner_path.unlink()
                    print(json.dumps({"reconciled": "finalized", "revision": current["revision"]}))
                    return
                if previous["status"] not in {"drafting", "paused"}:
                    raise ValueError("Cannot recover a finalized or superseded run")
                if previous["base_revision"] != (current["revision"] if current else None):
                    raise ValueError("Current revision moved; inspect before recovery")
            elif owner:
                raise ValueError("Stage already owned; pause or recover that run")
            elif current and not args.from_current:
                raise ValueError("Use --from-current to upgrade; never restart an existing stage")
            run = str(uuid.uuid4())
            draft = stage / "drafts" / run
            if previous:
                shutil.copytree(stage / "drafts" / previous["run"], draft)
            elif current:
                revision = stage / "revisions" / current["revision"]
                if hashes(revision / "content") != read(revision / "manifest.json")["files"]:
                    raise ValueError("Current revision was modified")
                shutil.copytree(revision / "content", draft)
            else:
                draft.mkdir(parents=True)
                info = registry[uid]
                atomic(draft / "stage.json", {"schema_version": "3.1-draft", "stage_uid": uid,
                       "display_code": info["display_code"], "title": info["title"], "level": info["level"],
                        "scope": "", "nodes": [], "events": [], "retired_ids": [], "source_refs": [],
                        "curriculum": curriculum})
                atomic(draft / "sources.json", {"scan": [], "entries": []})
                atomic(draft / "learning-map.json", {"schema_version": "1.0", "stage_uid": uid, "lessons": []})
                (draft / "editorial.md").write_text("# Nhật ký biên tập\n\nChưa biên soạn.\n", encoding="utf-8")
            spec_paths = [registry_path, Path(__file__).resolve(),
                          Path(__file__).resolve().parents[1] / "SKILL.md",
                          Path(__file__).resolve().parents[1] / "references/content-contract.md",
                          Path(__file__).resolve().parents[1] / "references/progression.md",
                          Path(__file__).resolve().parents[1] / "references/editorial-workflow.md",
                           Path(__file__).resolve().parents[1] / "references/situation-coverage.md",
                           inside(repo, curriculum["roadmap"]), inside(repo, curriculum["policy"]),
                           repo / "kaiwa_skill/planning/CURRENT_ROADMAP.json"]
            state = {"run": run, "stage_uid": uid, "status": "drafting", "created_at": now(),
                     "base_revision": current["revision"] if current else None,
                     "recovered_from": previous["run"] if previous else None,
                     "next_action": args.next or (previous["next_action"] if previous else "Đọc phạm vi và tra nguồn"),
                     "checkpoints": [], "files": hashes(draft),
                     "source_pins": previous["source_pins"] if previous else {},
                     "context_pins": previous.get("context_pins", {}) if previous else {},
                     "spec_pins": {p.relative_to(repo).as_posix(): sha(p) for p in spec_paths if p.is_relative_to(repo) and p.exists()}}
            atomic(stage / "runs" / (run + ".json"), state)
            atomic(owner_path, {"run": run, "claimed_at": now()})
            if previous:
                previous["status"] = "superseded"
                atomic(stage / "runs" / (previous["run"] + ".json"), previous)
            print(json.dumps({"run": run, "draft": str(draft), "next_action": state["next_action"],
                              "review_required": "Recovery keeps all current draft bytes, including any uncheckpointed edits; inspect source/spec drift before continuing." if previous else None}, ensure_ascii=False))
            return
        if not args.run:
            raise ValueError("--run required")
        run = str(uuid.UUID(args.run))
        state_path = stage / "runs" / (run + ".json")
        state = read(state_path)
        draft = stage / "drafts" / run
        if state["status"] not in {"drafting", "paused"}:
            raise ValueError("Run is finalized or superseded")
        if state["base_revision"] != (current["revision"] if current else None):
            raise ValueError("Current revision changed; inspect before continuing")
        if args.command == "resume":
            if state["status"] != "paused" or owner:
                raise ValueError("Resume requires a paused run and no other owner")
            if hashes(draft) != state["files"]:
                raise ValueError("Draft changed since pause; recover to preserve/inspect changes")
            for path, digest in {**state["source_pins"], **state.get("context_pins", {}), **state["spec_pins"]}.items():
                if sha(inside(repo, path)) != digest:
                    raise ValueError("Pinned source/spec changed: " + path)
            atomic(owner_path, {"run": run, "claimed_at": now()})
            state["status"] = "drafting"
            atomic(state_path, state)
            print(json.dumps({"run": run, "draft": str(draft), "next_action": state["next_action"]}, ensure_ascii=False))
            return
        if not owner or owner["run"] != run or state["status"] != "drafting":
            raise ValueError("Run does not own this stage")
        if args.command in {"validate", "finalize"}:
            content = check(draft, uid, repo)
            if args.command == "validate":
                print("Structure OK; language, source reading and coverage still require editorial review")
                if (draft / "learning-map.json").exists():
                    pending = sum(len(l.get("pending_previous", [])) for l in read(draft / "learning-map.json")["lessons"])
                    if pending:
                        print("Editorial continuity pending: " + str(pending) + " unresolved predecessor notes")
                return
            if not args.editor_reviewed or not args.note.strip():
                raise ValueError("Finalize needs --editor-reviewed and an actual editorial summary via --note")
            for path, digest in state["spec_pins"].items():
                if sha(inside(repo, path)) != digest:
                    raise ValueError("Pinned spec changed; recover/review before finalizing: " + path)
            export_context(draft, content)
            revisions = stage / "revisions"
            numbers = [int(p.name[1:]) for p in revisions.glob("r*") if re.fullmatch(r"r\d+", p.name)] if revisions.exists() else []
            revision_id = "r" + str(max(numbers, default=0) + 1).zfill(4)
            revision = revisions / revision_id
            shutil.copytree(draft, revision / "content")
            manifest = {"revision": revision_id, "run": run, "stage_uid": uid,
                        "created_at": now(), "files": hashes(revision / "content"),
                        "source_pins": source_pins(repo, draft), "context_pins": learning_pins(repo, draft),
                        "continuity_pending": sum(len(l.get("pending_previous", [])) for l in read(draft / "learning-map.json")["lessons"]) if (draft / "learning-map.json").exists() else 0,
                        "editorial_summary": args.note}
            if manifest["files"] != hashes(draft):
                raise ValueError("Draft changed during snapshot; revision not published")
            atomic(revision / "manifest.json", manifest)
            atomic(current_path, {"revision": revision_id, "run": run, "stage_uid": uid, "updated_at": now()})
            state["status"] = "finalized"
            state["revision"] = revision_id
            state["continuity_pending"] = manifest["continuity_pending"]
            atomic(state_path, state)
            owner_path.unlink()
            print(json.dumps({"revision": revision_id, "content": str(revision / "content"), "continuity_pending": manifest["continuity_pending"]}, ensure_ascii=False))
            return
        if args.command not in {"checkpoint", "pause"}:
            raise ValueError("Unsupported command")
        if not args.next.strip():
            raise ValueError("Checkpoint/pause needs a concrete --next action")
        state["files"] = hashes(draft)
        try:
            state["source_pins"] = source_pins(repo, draft)
            state["source_warning"] = None
        except (ValueError, OSError, KeyError, TypeError) as exc:
            # Save incomplete editorial work too; finalization remains strict.
            state["source_warning"] = str(exc)
        try:
            state["context_pins"] = learning_pins(repo, draft)
            state["context_warning"] = None
        except (ValueError, OSError, KeyError, TypeError) as exc:
            state["context_warning"] = str(exc)
        state["next_action"] = args.next
        state["checkpoints"].append({"at": now(), "note": args.note, "next_action": args.next,
                                     "files": state["files"], "source_pins": state["source_pins"],
                                     "context_pins": state.get("context_pins", {}), "context_warning": state.get("context_warning")})
        if args.command == "pause":
            state["status"] = "paused"
        atomic(state_path, state)
        if args.command == "pause":
            owner_path.unlink()
        print(json.dumps({"run": run, "status": state["status"], "next_action": args.next,
                          "source_warning": state.get("source_warning"), "context_warning": state.get("context_warning")}, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        sys.exit(2)
