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


def compile_stage(draft):
    wrapper = load(draft / "stage.json")
    if wrapper.get("authoring_mode") != "canonical":
        raise ValueError("Compilation requires canonical authoring mode")
    source = (draft / wrapper["harumii_export"]).resolve()
    if not source.is_relative_to(draft.resolve()):
        raise ValueError("Canonical source outside draft")
    data = load(source)
    path = Path(__file__).with_name("kaiwa_exchange.py")
    spec = importlib.util.spec_from_file_location("compile_exchange", path)
    exchange = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(exchange)
    exchange.validate(data)
    if data["stage_uid"] != wrapper["stage_uid"]:
        raise ValueError("Canonical stage UID mismatch")
    audit = load(draft / "source-map.json")
    source_ids = {entry["id"] for entry in load(draft / "sources.json").get("entries", [])}
    utterances = {u["id"]: u for u in data["utterances"]}
    material = {n["id"] for n in data["nodes"] if n["type"] not in {"live_challenge", "free_talk"}}
    if set(audit.get("nodes", {})) != material:
        raise ValueError("source-map must describe every material node exactly once")
    nodes = []
    for node in data["nodes"]:
        nid, kind, content = node["id"], node["type"], node["data"]
        if kind == "live_challenge":
            continue  # Authored once in canonical source; not a second knowledge lesson.
        metadata = audit.get("nodes", {}).get(nid, {})
        refs = metadata.get("source_refs", [])
        authorship = metadata.get("authorship", "original_extension")
        if kind != "free_talk" and authorship not in {"source_adaptation", "original_extension"}:
            raise ValueError("Invalid source-map authorship: " + nid)
        if any(ref not in source_ids for ref in refs) or (authorship == "source_adaptation" and not refs):
            raise ValueError("Source adaptation needs registered source references: " + nid)
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
            value["items"] = [{"id": item_id(nid, term), "ja": term,
                               "exposure": metadata.get("word_exposure", {}).get(term, "new"),
                               "source_refs": refs} for term in content["terms_ja"]]
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
                    value["items"].append({"id": item["id"], "kind": "situation_ref", "situation_id": item["situation_node_id"]})
                else:
                    u = utterances[item["utterance_id"]]
                    value["items"].append({"id": item["id"], "kind": "sentence", "example_id": u["id"],
                                           "ja": u["ja"], "vi": u["vi"], "authorship": authorship})
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
