"""Derive the editorial workspace from one authored Harumii payload; no model calls."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n" if not isinstance(value, str) else value
    temporary = path.with_name(path.name + ".compile.tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    temporary.replace(path)


def item_id(node_id, text, kind="w"):
    return node_id + "-" + kind + "-" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def sibling(name):
    spec = importlib.util.spec_from_file_location("compile_" + name, Path(__file__).with_name(name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CD_BOOKS = {"B09", "B11", "B12", "B13", "B14", "B25", "B26", "B27"}


PACK_ROOT = "kaiwa_skill/planning/catalog27/audio_packs"


def shadow_sequence(node, nodes):
    sequence = []
    for item in node["data"]["items"]:
        if item["kind"] == "sentence":
            sequence.append(item["utterance_id"])
        else:
            dialogue = nodes[item["situation_node_id"]]["data"] if item["kind"] == "dialogue_ref" else item
            sequence.extend(t["utterance_id"] for t in dialogue["turns"])
    return sequence


def read_pack(repo, pack, sources, source_texts):
    """Resolve a complete, independently inventoried pack against pinned script bytes."""
    key = pack.get("pack_id", "")
    if not re.fullmatch(r"B[0-9]{2}/[a-zA-Z0-9_-]+", key):
        raise ValueError("Use a catalog pack_id (book/unit)")
    path = repo / PACK_ROOT / (key + ".json")
    if not path.is_file() or not path.resolve().is_relative_to(repo):
        raise ValueError("Missing reviewed CD inventory: " + key)
    manifest = load(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != pack.get("manifest_sha256") or manifest.get("pack_id") != key:
        raise ValueError("CD inventory changed or pack_id mismatch: " + key)
    book = key.split("/")[0]
    if not manifest.get("boundary_evidence") or not manifest.get("tracks") or not manifest.get("edition"):
        raise ValueError("Inventory needs source boundaries, edition and complete track order: " + key)
    scripts = {}
    for sid, entry in sources.items():
        if entry.get("book_id") == book and sid in source_texts:
            scripts.setdefault((entry.get("path"), entry.get("sha256")), []).append(sid)
    turns = []
    units = set()
    for track in manifest["tracks"]:
        if not all(track.get(k) for k in ("disc", "track", "locator", "parts")):
            raise ValueError("Missing CD track evidence: " + key)
        for part in track["parts"]:
            script_refs = scripts.get((part["path"], part["sha256"]))
            if not script_refs:
                raise ValueError("CD inventory needs its pinned source script: " + part["path"])
            lines = source_texts[script_refs[0]].splitlines()
            marker = '<a id="' + part["unit"] + '"></a>'
            if lines.count(marker) != 1 or not part.get("turns"):
                raise ValueError("Missing unique unit anchor or transcript: " + key)
            first = lines.index(marker) + 2
            last = next((i for i in range(first - 1, len(lines)) if lines[i].startswith('<a id="')), len(lines))
            units.add(part["unit"])
            for line, start, end in part["turns"]:
                if not first <= line <= last or not 0 <= start < end <= len(lines[line-1]):
                    raise ValueError("CD turn outside its source unit: " + key)
                turns.append((script_refs, lines[line-1][start:end]))
    return manifest, turns, units


def check_audio_packs(repo, data, audit, sources, source_texts):
    nodes = {n["id"]: n for n in data["nodes"]}
    utterances = {u["id"]: u for u in data["utterances"]}
    required = set()
    for uid, u in utterances.items():
        if any(sources.get(s, {}).get("book_id") in CD_BOOKS for s in u.get("source_refs", [])):
            if u.get("authorship") == "source_adaptation":
                raise ValueError("Keep original Japanese for CD practice: " + uid)
            if u.get("authorship") == "source_quote":
                required.add(uid)
    covered = set()
    seen = set()
    by_shadow = {}
    inventory = []
    for pack in audit.get("audio_packs", []):
        nid = pack["shadowing_node_id"]
        ids = pack["utterance_ids"]
        if nodes.get(nid, {}).get("type") != "shadowing" or not ids or pack.get("pack_id") in seen:
            raise ValueError("A complete CD pack must occur once in one shadowing node")
        manifest, turns, units = read_pack(repo, pack, sources, source_texts)
        key = manifest["pack_id"]
        seen.add(key)
        inventory.append(dict(manifest, shadowing_node_id=nid, utterance_ids=ids, manifest_sha256=pack["manifest_sha256"]))
        sequence = shadow_sequence(nodes[nid], nodes)
        if not any(sequence[i:i+len(ids)] == ids for i in range(len(sequence))):
            raise ValueError("Audio pack must be contiguous in shadowing order")
        if len(ids) != len(turns):
            raise ValueError("CD pack must contain every source turn: " + key)
        for uid, (script_refs, ja) in zip(ids, turns):
            u = utterances[uid]
            if u.get("authorship") != "source_quote" or set(script_refs).isdisjoint(u["source_refs"]) or u["ja"] != ja:
                raise ValueError("CD pack must reproduce each catalog turn verbatim in order: " + key)
        covered.update(ids)
        by_shadow.setdefault(nid, []).append((key.split("/")[0], units, ids))
    if required - covered:
        raise ValueError("Missing audio pack lookup for: " + ", ".join(sorted(required - covered)))
    # Original practice may be followed by new exercises. Never repeat a fragment
    # of the source pack in another shadowing node or surround it with extra copies.
    for n in nodes.values():
        if n["type"] == "shadowing":
            actual = [uid for uid in shadow_sequence(n, nodes) if uid in required or uid in covered]
            expected = [uid for _, _, ids in by_shadow.get(n["id"], []) for uid in ids]
            if actual != expected:
                raise ValueError("Shadowing must use complete catalog packs in declared order: " + n["id"])
    for n in nodes.values():
        if n["type"] != "knowledge" or n["data"]["source_family"] != "speak_japanese":
            continue
        declared = {(u["book_id"], u["unit"]) for u in audit.get("sequence_units", {}).get(n["id"], [])
                    if u["book_id"] in {"B11", "B12"} and u.get("role", "teach") == "teach"}
        lesson = n["data"]
        tokens = re.findall(r"\{\{utterance:([a-zA-Z0-9_-]+)\}\}", lesson["body_md"])
        taught = set()
        for book, units, ids in by_shadow.get(lesson["practice_node_id"], []):
            if book not in {"B11", "B12"}:
                continue
            if not any(tokens[i:i+len(ids)] == ids for i in range(len(tokens))):
                raise ValueError("Speak Japanese knowledge must include the complete source pack in order")
            taught.update((book, unit) for unit in units)
        if not declared or taught != declared:
            raise ValueError("Speak Japanese needs its source book unit and complete matching CD pack: " + n["id"])
    return inventory


def compile_stage(draft, repo=None, notes=None):
    """Derive workspace files; `notes` collects non-blocking remarks for the author."""
    repo = (repo or Path(__file__).resolve().parents[4]).resolve()
    wrapper = load(draft / "stage.json")
    if wrapper.get("authoring_mode") != "canonical":
        raise ValueError("Compilation requires canonical authoring mode")
    source = (draft / wrapper["harumii_export"]).resolve()
    if not source.is_relative_to(draft.resolve()):
        raise ValueError("Canonical source outside draft")
    data = load(source)
    exchange = sibling("kaiwa_exchange")
    exchange.validate(data)
    if data["stage_uid"] != wrapper["stage_uid"]:
        raise ValueError("Canonical stage UID mismatch")
    audit = load(draft / "source-map.json")
    source_entries = load(draft / "sources.json").get("entries", [])
    source_ids = {entry["id"] for entry in source_entries}
    source_by_id = {entry["id"]: entry for entry in source_entries}
    utterances = {u["id"]: u for u in data["utterances"]}
    source_texts = {}
    for utterance in data["utterances"]:
        if utterance.get("authorship") != "source_quote":
            continue
        matched = False
        for sid in utterance.get("source_refs", []):
            entry = source_by_id.get(sid, {})
            if entry.get("path"):
                path = (repo / entry["path"]).resolve()
                if not path.is_relative_to(repo):
                    raise ValueError("Quote source outside repository")
                if sid not in source_texts:
                    source_texts[sid] = path.read_text(encoding="utf-8-sig")
                matched |= utterance["ja"] in source_texts[sid]
        if not matched:
            raise ValueError("Source_quote Japanese must match a registered local source: " + utterance["id"])
    inventory = check_audio_packs(repo, data, audit, source_by_id, source_texts)
    for utterance in data["utterances"]:
        # "Reference" marks book material above the stage's active level; new writing is simplified instead.
        if utterance.get("learning_scope") == "source_reference" and utterance.get("authorship") == "original_extension":
            raise ValueError("Only source material may be source_reference; simplify newly written lines: " + utterance["id"])
    material = {n["id"] for n in data["nodes"] if n["type"] not in {"live_challenge", "free_talk"}}
    if set(audit.get("nodes", {})) != material:
        raise ValueError("source-map must describe every material node exactly once")
    sequence = sibling("source_sequence")
    plan = sequence.load_plan(repo, wrapper.get("curriculum"))
    if plan is not None:
        # Check selected units and levels independently of their position in the book.
        problems, remarks = sequence.check_stage(repo, plan, wrapper.get("curriculum"), data["stage_uid"], data, audit, source_entries)
        if notes is not None:
            notes.extend(remarks)
        if problems:
            raise ValueError("\n".join(problems))
    elif audit.get("sequence_units"):
        raise ValueError("sequence_units declared but this curriculum has no SOURCE_SEQUENCE.json")
    if "source_registry" in data:
        spoken = {t["utterance_id"] for n in data["nodes"] if n["type"] == "situation" for t in n["data"]["turns"]}
        spoken.update(i["utterance_id"] for n in data["nodes"] if n["type"] == "shadowing"
                      for i in n["data"]["items"] if i["kind"] == "sentence")
        spoken.update(t["utterance_id"] for n in data["nodes"] if n["type"] == "shadowing"
                      for i in n["data"]["items"] if i["kind"] == "dialogue" for t in i["turns"])
        for node in data["nodes"]:
            if node["type"] != "vocabulary":
                continue
            evidence = audit.get("vocabulary_evidence", {}).get(node["id"], [])
            if [entry["term"] for entry in evidence] != node["data"]["terms_ja"]:
                raise ValueError("Vocabulary needs backward evidence in term order: " + node["id"])
            for entry in evidence:
                term = entry["term"]
                if not entry.get("dictionary_form_reviewed") or not entry.get("evidence"):
                    raise ValueError("Vocabulary needs dictionary-form review and spoken evidence: " + term)
                if entry.get("kind") == "verb" and (term[-1] not in "うくぐすつぬぶむる" or re.search(r"ます$|ました$|ません$", term)):
                    raise ValueError("Vocabulary verb must be dictionary form: " + term)
                if entry.get("kind") == "adjective_i" and not term.endswith("い"):
                    raise ValueError("Vocabulary i-adjective must be base form: " + term)
                for occurrence in entry["evidence"]:
                    uid = occurrence["utterance_id"]
                    if uid not in spoken or not occurrence["surface"] or occurrence["surface"] not in utterances[uid]["ja"]:
                        raise ValueError("Vocabulary evidence must occur in an actual spoken example: " + term)
    write(draft / "audio-index.json", inventory)
    nodes = []
    for node in data["nodes"]:
        nid, kind, content = node["id"], node["type"], node["data"]
        if kind == "live_challenge":
            continue  # Authored once in canonical source; not a second knowledge lesson.
        metadata = audit.get("nodes", {}).get(nid, {})
        refs = metadata.get("source_refs", [])
        authorship = metadata.get("authorship", "original_extension")
        if kind != "free_talk" and authorship not in {"source_quote", "source_adaptation", "original_extension"}:
            raise ValueError("Invalid source-map authorship: " + nid)
        if any(ref not in source_ids for ref in refs) or (authorship in {"source_quote", "source_adaptation"} and not refs):
            raise ValueError("Source adaptation needs registered source references: " + nid)
        if kind == "knowledge":
            if any(s["id"] in refs and s.get("book_id") in {"B11", "B12"} for s in source_entries) and content["source_family"] != "speak_japanese":
                raise ValueError("Knowledge teaching B11/B12 needs Speak Japanese video/practice structure")
        relative = ("knowledge/" + nid + ".md" if kind == "knowledge" else
                    ("live/" if kind == "free_talk" else kind + "/") + nid + ".json")
        # Keep existing plural workspace directory names.
        if kind in {"situation", "shadowing"}:
            relative = ("situations/" if kind == "situation" else "shadowing/") + nid + ".json"
        desc = {"id": nid, "type": "live_context" if kind == "free_talk" else kind,
                "title": node["title_vi"], "path": relative, "source_refs": refs}
        value = {"id": nid, "source_refs": refs}
        if kind == "knowledge":
            def render(match):
                uid = match[1]
                u = utterances[uid]
                return '<a id="' + uid + '"></a>\n' + u["ja"] + "\n\n" + u["vi"]
            value = re.sub(r"\{\{utterance:([a-zA-Z0-9_-]+)\}\}", render, content["body_md"])
            desc.update(source_family=content["source_family"])
            if "practice_node_id" in content:
                desc["practice_node_id"] = content["practice_node_id"]
            if content["video_status"] == "planned":
                desc["video"] = {"status": "planned", "asset_ref": None}
        elif kind == "vocabulary":
            value["items"] = [{"id": item_id(nid, term), "ja": term, "source_refs": refs,
                               **({"exposure": metadata["word_exposure"][term]} if term in metadata.get("word_exposure", {}) else {})}
                              for term in content["terms_ja"]]
        elif kind == "grammar":
            value["items"] = [{"id": item_id(nid, p["catalog"] + ":" + p["name_ja"], "g"),
                               "name_ja": p["name_ja"], "jlpt_level": p["jlpt_level"],
                               "reference": {"kind": p["catalog"]}} for p in content["patterns"]]
        elif kind == "situation":
            value.update(title=node["title_vi"], event_id=content["event_id"], setting=content["setting_vi"],
                         communication_goal=content["goal_vi"], relationship=content["relationship_vi"],
                         outcome=content["outcome"], follows=content["follows"], alternative_to=content["alternative_to"],
                         speakers=[{"id": s["id"], "role": s["role_vi"]} for s in content["speakers"]],
                         turns=[{"id": nid + "--" + t["id"], "speaker": t["speaker_id"],
                                 "ja": utterances[t["utterance_id"]]["ja"], "vi": utterances[t["utterance_id"]]["vi"]}
                                for t in content["turns"]], authorship=authorship)
        elif kind == "shadowing":
            value.update(knowledge_ids=content["knowledge_node_ids"], items=[])
            for item in content["items"]:
                if item["kind"] == "dialogue_ref":
                    target = next(n for n in data["nodes"] if n["id"] == item["situation_node_id"])
                    value["items"].append({"id": item["id"], "kind": "situation_ref", "situation_id": item["situation_node_id"],
                                           "example_id": target["data"]["turns"][0]["utterance_id"]})
                elif item["kind"] == "dialogue":
                    ids = [t["utterance_id"] for t in item["turns"]]
                    categories = {utterances[uid].get("authorship", authorship) for uid in ids}
                    category = next(iter(categories)) if len(categories) == 1 else "source_adaptation"
                    value["items"].append({"id": item["id"], "kind": "dialogue", "example_id": ids[0],
                                           "speakers": [{"id": s["id"], "role": s["role_vi"]} for s in item["speakers"]],
                                           "turns": [{"id": nid + "--" + item["id"] + "--" + t["id"], "speaker": t["speaker_id"],
                                                      "ja": utterances[t["utterance_id"]]["ja"], "vi": utterances[t["utterance_id"]]["vi"]}
                                                     for t in item["turns"]], "authorship": category})
                else:
                    u = utterances[item["utterance_id"]]
                    value["items"].append({"id": item["id"], "kind": "sentence", "example_id": u["id"],
                                           "ja": u["ja"], "vi": u["vi"], "authorship": u.get("authorship", authorship),
                                           "source_refs": u.get("source_refs", refs)})
        elif kind == "free_talk":
            value.update(context_node_ids=content["context_node_ids"], overview_vi=data["scope_vi"], optional_extensions=[],
                         context_export="live-context.md", free_talk={**{k: v for k, v in content.items() if k != "context_node_ids"},
                         "mode": "free_talk", "content_origin": "curriculum_authored", "situation_export": "free-talk-situation.md"})
        write(draft / relative, value)
        nodes.append(desc)
    wrapper.update(title=data["title_vi"], display_code=data["display_code"],
                   level={"beginner": "Sơ", "intermediate": "Trung", "advanced": "Thượng"}[data["level"]],
                   scope=data["scope_vi"], nodes=nodes,
                   events=[{"id": e["id"], "title": e["title_vi"], "situation_ids": [n["id"] for n in data["nodes"]
                            if n["type"] == "situation" and n["data"]["event_id"] == e["id"]]} for e in data["events"]],
                   retired_ids=[{"id": r["id"], "reason": r["reason_vi"], "replacement_ids": r["replaced_by"]}
                                for r in data["retired"] if r["kind"] == "node"])
    write(draft / "stage.json", wrapper)
    return data
