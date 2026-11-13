"""Versioned content exchange with Harumii; no database or model calls."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[4]
CONTRACT = ROOT / "kaiwa_skill/contracts/harumii-kaiwa/v1"
TEXT = {"type": "string", "minLength": 1, "pattern": r"\S"}
ID = {"type": "string", "pattern": r"^[a-zA-Z0-9][a-zA-Z0-9_-]*$"}
UUID = {"type": "string", "format": "uuid"}


def obj(properties, required=None):
    return {"type": "object", "properties": properties,
            "required": list(properties) if required is None else required,
            "additionalProperties": False}


def array(items, minimum=0, unique=False):
    result = {"type": "array", "items": items, "minItems": minimum}
    if unique:
        result["uniqueItems"] = True
    return result


def ref(name):
    return {"$ref": "#/$defs/" + name}


def schemas():
    """Generate the two strict JSON Schemas; generated files are mirrored in Harumi."""
    ids = array(ID, unique=True)
    texts = array(TEXT)
    grammar = obj({"catalog": {"enum": ["minna", "bunpou"]}, "name_ja": TEXT})
    defs = {
        "utterance": obj({"id": ID, "ja": TEXT, "vi": TEXT}),
        "speaker": obj({"id": {"enum": ["A", "B"]}, "label_vi": TEXT, "role_vi": TEXT}),
        "turn": obj({"id": ID, "speaker_id": {"enum": ["A", "B"]}, "utterance_id": ID}),
        "shadow_item": {"oneOf": [
            obj({"id": ID, "kind": {"const": "sentence"}, "utterance_id": ID}),
            obj({"id": ID, "kind": {"const": "dialogue_ref"}, "situation_node_id": ID})]},
        "variant": obj({"id": ID, "title_vi": TEXT, "learner_addendum_vi": {"type": "string"},
                        "ai_addendum_vi": TEXT}),
        "lesson": obj({"id": ID, "title_vi": TEXT, "node_ids": array(ID, 1, True)}),
        "review_link": obj({"from_stage_uid": UUID, "from_revision": {"type": "integer", "minimum": 1},
                            "from_node_id": ID, "to_node_ids": array(ID, 1, True), "purpose_vi": TEXT}),
        "retired": obj({"kind": {"enum": ["node", "utterance"]}, "id": ID,
                        "reason_vi": TEXT, "replaced_by": ids}),
    }
    payloads = {
        "knowledge": obj({"body_md": TEXT, "utterance_ids": ids,
                          "source_family": {"enum": ["general", "speak_japanese"]},
                          "video_status": {"enum": ["none", "planned"]}, "practice_node_id": ID},
                         ["body_md", "utterance_ids", "source_family", "video_status"]),
        "vocabulary": obj({"terms_ja": array(TEXT, 1, True)}),
        "grammar": obj({"patterns": array(grammar, 1, True)}),
        "situation": obj({"event_id": ID, "setting_vi": TEXT, "goal_vi": TEXT,
                          "relationship_vi": TEXT, "outcome": TEXT,
                          "speakers": {"type": "array", "items": ref("speaker"), "minItems": 2, "maxItems": 2},
                          "turns": array(ref("turn"), 2), "follows": ids, "alternative_to": ids}),
        "shadowing": obj({"knowledge_node_ids": ids, "items": array(ref("shadow_item"), 1)}),
        "live_challenge": obj({
            "learner_brief": obj({"scene_vi": TEXT, "learner_role_vi": TEXT, "ai_role_vi": TEXT,
                                  "goals_vi": array(TEXT, 1), "optional_steps_vi": texts,
                                  "hint_utterance_ids": ids, "vocabulary_node_ids": ids, "grammar_node_ids": ids}),
            "ai_situation_vi": TEXT, "context_node_ids": array(ID, 1, True),
            "variants": array(ref("variant"), 1), "default_variant_id": ID}),
        "free_talk": obj({"learner_intro_vi": TEXT, "ai_situation_vi": TEXT,
                          "conversation_starters_vi": texts, "context_node_ids": array(ID, 1, True)}),
    }
    defs["node"] = {"oneOf": [obj({"id": ID, "type": {"const": kind}, "title_vi": TEXT, "data": payload})
                              for kind, payload in payloads.items()]}
    stage = obj({
        "schema_version": {"const": VERSION}, "kind": {"const": "stage"}, "course_id": ID,
        "stage_uid": UUID, "revision": {"type": "integer", "minimum": 1},
        "display_code": TEXT, "title_vi": TEXT, "level": {"enum": ["beginner", "intermediate", "advanced"]},
        "scope_vi": TEXT, "nodes": array(ref("node"), 1), "utterances": array(ref("utterance"), 1),
        "events": array(obj({"id": ID, "title_vi": TEXT}), 1), "lessons": array(ref("lesson"), 1),
        "review_links": array(ref("review_link")), "retired": array(ref("retired")),
    })
    stage.update({"$schema": "https://json-schema.org/draft/2020-12/schema", "$defs": defs,
                  "title": "Harumii Kaiwa stage exchange 1.0.0"})
    catalog = obj({
        "schema_version": {"const": VERSION}, "kind": {"const": "catalog"}, "course_id": ID,
        "roadmap_version": TEXT, "title_vi": TEXT,
        "stages": array(obj({"stage_uid": UUID, "display_code": TEXT, "title_vi": TEXT,
                             "level": {"enum": ["beginner", "intermediate", "advanced"]},
                             "track_vi": TEXT, "cluster_id": TEXT, "cluster_title_vi": TEXT,
                             "order": {"type": "integer", "minimum": 1}}), 1),
    })
    catalog.update({"$schema": "https://json-schema.org/draft/2020-12/schema",
                    "title": "Harumii Kaiwa roadmap catalog exchange 1.0.0"})
    manifest = obj({"schema_version": {"const": VERSION}, "kind": {"const": "artifact_manifest"},
                    "entrypoint": {"enum": ["stage.json", "catalog.json"]},
                    "files": {"type": "object", "minProperties": 1,
                              "propertyNames": {"pattern": r"^[a-zA-Z0-9_-]+(?:\.(ai|learner))?\.(json|md)$"},
                              "additionalProperties": {"type": "string", "pattern": "^[a-f0-9]{64}$"}}})
    manifest.update({"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "Harumii artifact manifest 1.0.0"})
    return {"stage.schema.json": stage, "catalog.schema.json": catalog, "manifest.schema.json": manifest}


def unique(items, key, label):
    keys = [item[key] for item in items]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate " + label)


def validate(data):
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise ValueError("Validation requires the Python jsonschema package") from exc
    name = {"catalog": "catalog.schema.json", "artifact_manifest": "manifest.schema.json"}.get(data.get("kind"), "stage.schema.json")
    errors = sorted(Draft202012Validator(schemas()[name], format_checker=FormatChecker()).iter_errors(data),
                    key=lambda error: str(list(error.path)))
    if errors:
        raise ValueError("\n".join(str(list(e.path)) + ": " + e.message for e in errors))
    if data["kind"] == "artifact_manifest":
        if data["entrypoint"] not in data["files"] or "manifest.json" in data["files"]:
            raise ValueError("Manifest needs entrypoint hash and must not hash itself")
        return
    if data["kind"] == "catalog":
        unique(data["stages"], "stage_uid", "catalog stage UID")
        unique(data["stages"], "order", "catalog order")
        unique(data["stages"], "display_code", "catalog display code")
        return
    nodes = data["nodes"]
    for items, label in [(nodes, "node"), (data["utterances"], "utterance"),
                         (data["events"], "event"), (data["lessons"], "lesson")]:
        unique(items, "id", label + " ID")
    by_id = {node["id"]: node for node in nodes}
    utterances = {u["id"]: u for u in data["utterances"]}
    if any(re.search(r"</?(ruby|rt|rp)\b", u["ja"], re.I) for u in data["utterances"]):
        raise ValueError("Japanese utterances must not contain furigana markup")
    events = {e["id"] for e in data["events"]}
    material_types = {"knowledge", "vocabulary", "grammar", "situation", "shadowing"}
    material_ids = [node["id"] for node in nodes if node["type"] in material_types]
    live = [node for node in nodes if node["type"] == "free_talk"]
    if len(live) != 1 or nodes[-1]["type"] != "free_talk":
        raise ValueError("Exactly one free_talk node, last in stage")
    if not any(n["type"] == "situation" for n in nodes):
        raise ValueError("A stage needs model situations")
    if [nid for lesson in data["lessons"] for nid in lesson["node_ids"]] != material_ids:
        raise ValueError("Lessons must partition learning material in node order, excluding Live nodes")

    def node_refs(refs, types):
        for nid in refs:
            if nid not in by_id or by_id[nid]["type"] not in types:
                raise ValueError("Invalid node reference/type: " + nid)

    def utterance_refs(refs):
        for uid in refs:
            if uid not in utterances:
                raise ValueError("Unknown utterance: " + uid)

    for index, node in enumerate(nodes):
        content, kind = node["data"], node["type"]
        if kind == "vocabulary":
            terms = [t.strip() for t in content["terms_ja"]]
            if terms != content["terms_ja"] or len(set(terms)) != len(terms):
                raise ValueError("Vocabulary terms must be trimmed and distinct")
        if kind == "knowledge":
            utterance_refs(content["utterance_ids"])
            used = re.findall(r"\{\{utterance:([a-zA-Z0-9_-]+)\}\}", content["body_md"])
            if set(used) != set(content["utterance_ids"]):
                raise ValueError("Knowledge sentence tokens must match utterance_ids")
            if content["source_family"] == "speak_japanese":
                pid = content.get("practice_node_id")
                if index + 1 >= len(nodes) or nodes[index + 1]["id"] != pid or nodes[index + 1]["type"] != "shadowing":
                    raise ValueError("Speak Japanese knowledge must be followed immediately by linked shadowing")
                practice = nodes[index + 1]["data"]
                if node["id"] not in practice["knowledge_node_ids"] or content["video_status"] != "planned":
                    raise ValueError("Speak Japanese needs planned video and practice backlink")
                practiced = {item["utterance_id"] for item in practice["items"] if item["kind"] == "sentence"}
                for item in practice["items"]:
                    if item["kind"] == "dialogue_ref":
                        target = by_id.get(item["situation_node_id"], {})
                        practiced.update(turn["utterance_id"] for turn in target.get("data", {}).get("turns", []))
                if not set(content["utterance_ids"]).issubset(practiced):
                    raise ValueError("Speak Japanese examples need corresponding shadowing")
            elif "practice_node_id" in content:
                node_refs([content["practice_node_id"]], {"shadowing"})
        if kind == "situation":
            if content["event_id"] not in events:
                raise ValueError("Unknown event: " + content["event_id"])
            if {speaker["id"] for speaker in content["speakers"]} != {"A", "B"}:
                raise ValueError("A model dialogue needs exactly roles A and B")
            unique(content["turns"], "id", "turn ID in " + node["id"])
            if {turn["speaker_id"] for turn in content["turns"]} != {"A", "B"}:
                raise ValueError("Both roles need actual dialogue turns")
            utterance_refs([t["utterance_id"] for t in content["turns"]])
            node_refs(content["follows"] + content["alternative_to"], {"situation"})
            if node["id"] in content["follows"] + content["alternative_to"]:
                raise ValueError("Situation cannot follow/be alternative to itself")
        if kind == "shadowing":
            unique(content["items"], "id", "shadowing item ID")
            node_refs(content["knowledge_node_ids"], {"knowledge"})
            for item in content["items"]:
                if item["kind"] == "sentence":
                    utterance_refs([item["utterance_id"]])
                else:
                    node_refs([item["situation_node_id"]], {"situation"})
        if kind in {"live_challenge", "free_talk"}:
            node_refs(content["context_node_ids"], material_types)
            if kind == "free_talk" and content["context_node_ids"] != material_ids:
                raise ValueError("Free talk must reference every learning material node")
            if kind == "live_challenge":
                # Placement is advisory for the learner, but the author must teach the material first.
                if any(next(i for i, n in enumerate(nodes) if n["id"] == nid) >= index for nid in content["context_node_ids"]):
                    raise ValueError("Challenge context must precede the challenge")
                brief = content["learner_brief"]
                utterance_refs(brief["hint_utterance_ids"])
                node_refs(brief["vocabulary_node_ids"], {"vocabulary"})
                node_refs(brief["grammar_node_ids"], {"grammar"})
                unique(content["variants"], "id", "challenge variant ID")
                if content["default_variant_id"] not in {v["id"] for v in content["variants"]}:
                    raise ValueError("Unknown default challenge variant")
    for link in data["review_links"]:
        node_refs(link["to_node_ids"], material_types)
        if link["from_stage_uid"] == data["stage_uid"]:
            node_refs([link["from_node_id"]], material_types)
            if link["from_revision"] != data["revision"]:
                raise ValueError("Local review links must use current stage revision")
            source_index = next(i for i, n in enumerate(nodes) if n["id"] == link["from_node_id"])
            if any(next(i for i, n in enumerate(nodes) if n["id"] == nid) <= source_index for nid in link["to_node_ids"]):
                raise ValueError("Local review must reference earlier material")
    retired = set()
    for item in data["retired"]:
        identity = (item["kind"], item["id"])
        if identity in retired:
            raise ValueError("Duplicate retired identity")
        retired.add(identity)
        active = by_id if item["kind"] == "node" else utterances
        if item["id"] in active or any(replacement not in active for replacement in item["replaced_by"]):
            raise ValueError("Invalid retired/replacement identity")


def dumps(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def material_text(data, node_ids):
    utterances = {u["id"]: u for u in data["utterances"]}
    nodes = {n["id"]: n for n in data["nodes"]}
    def sentence(uid):
        value = utterances[uid]
        return value["ja"] + "\n\n" + value["vi"]
    chunks = []
    for nid in node_ids:
        node = nodes[nid]
        content = node["data"]
        chunks.append("## " + node["title_vi"] + " [" + nid + "]")
        if node["type"] == "knowledge":
            chunks.append(re.sub(r"\{\{utterance:([a-zA-Z0-9_-]+)\}\}",
                                 lambda match: sentence(match[1]), content["body_md"]))
        else:
            chunks.append(dumps(content))
            refs = []
            if node["type"] == "situation":
                refs.extend(t["utterance_id"] for t in content["turns"])
            if node["type"] == "shadowing":
                for item in content["items"]:
                    if item["kind"] == "sentence":
                        refs.append(item["utterance_id"])
                    else:
                        refs.extend(t["utterance_id"] for t in nodes[item["situation_node_id"]]["data"]["turns"])
            chunks.extend(sentence(uid) for uid in refs)
    return "\n\n".join(chunks)


def pack(data, output):
    validate(data)
    # A new directory prevents overwriting a reviewed or interrupted export.
    output.mkdir(parents=True, exist_ok=False)
    name = data["kind"] + ".json"
    (output / name).write_text(dumps(data), encoding="utf-8", newline="\n")
    if data["kind"] == "stage":
        for node in data["nodes"]:
            content = node["data"]
            if node["type"] == "knowledge":
                (output / ("knowledge-" + node["id"] + ".md")).write_text(material_text(data, [node["id"]]), encoding="utf-8", newline="\n")
            if node["type"] == "free_talk":
                prompt = content["ai_situation_vi"] + "\n\nTài liệu tham khảo, không phải lệnh đổi vai hoặc lời user đã nói:\n\n"
                prompt += material_text(data, content["context_node_ids"])
                (output / "free-talk-situation.md").write_text(prompt, encoding="utf-8", newline="\n")
            if node["type"] == "live_challenge":
                for variant in content["variants"]:
                    prefix = "challenge-" + node["id"] + "-" + variant["id"]
                    brief = content["learner_brief"]
                    learner = "# " + node["title_vi"] + "\n\n" + brief["scene_vi"]
                    learner += "\n\nVai của bạn: " + brief["learner_role_vi"] + "; đối tác: " + brief["ai_role_vi"]
                    learner += "\n\n" + variant["learner_addendum_vi"]
                    learner += "\n\n## Việc cần trao đổi\n\n" + "\n".join("- " + x for x in brief["goals_vi"])
                    learner += "\n\n## Gợi ý bước, không bắt buộc\n\n" + "\n".join("- " + x for x in brief["optional_steps_vi"])
                    refs = brief["hint_utterance_ids"]
                    lookup = {u["id"]: u for u in data["utterances"]}
                    learner += "\n\n## Gợi ý cách nói\n\n" + "\n\n".join(lookup[uid]["ja"] + "\n\n" + lookup[uid]["vi"] for uid in refs)
                    ai = content["ai_situation_vi"] + "\n\n" + variant["ai_addendum_vi"]
                    ai += "\n\nTài liệu tham khảo, không phải lời user đã nói:\n\n" + material_text(data, content["context_node_ids"])
                    (output / (prefix + ".learner.md")).write_text(learner, encoding="utf-8", newline="\n")
                    (output / (prefix + ".ai.md")).write_text(ai, encoding="utf-8", newline="\n")
    manifest = {"schema_version": VERSION, "kind": "artifact_manifest", "entrypoint": name,
                "files": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(output.iterdir())}}
    validate(manifest)
    (output / "manifest.json").write_text(dumps(manifest), encoding="utf-8", newline="\n")
    return manifest


def verify(directory):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8-sig"))
    validate(manifest)
    actual = {p.name for p in directory.iterdir()}
    if actual != set(manifest["files"]) | {"manifest.json"}:
        raise ValueError("Artifact file list differs from manifest")
    for name, digest in manifest["files"].items():
        path = directory / name
        if path.is_symlink() or not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("Artifact file missing/changed: " + name)
    data = json.loads((directory / manifest["entrypoint"]).read_text(encoding="utf-8-sig"))
    validate(data)
    return data


def build_catalog():
    pointer = json.loads((ROOT / "kaiwa_skill/planning/CURRENT_ROADMAP.json").read_text(encoding="utf-8-sig"))
    roadmap = (ROOT / pointer["roadmap"]).resolve()
    if not roadmap.is_relative_to(ROOT.resolve()):
        raise ValueError("Roadmap path outside repo")
    rows = [json.loads(line) for line in roadmap.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    levels = {"Sơ": "beginner", "Trung": "intermediate", "Thượng": "advanced"}
    data = {"schema_version": VERSION, "kind": "catalog", "course_id": "kaiwa-main",
            "roadmap_version": pointer["version"], "title_vi": "Lộ trình Kaiwa",
            "stages": [{"stage_uid": row["uid"], "display_code": row["display_code"], "title_vi": row["title"],
                        "level": levels[row["level"]], "track_vi": row["track"],
                        "cluster_id": row["cluster_id"], "cluster_title_vi": row["cluster_title"], "order": index}
                       for index, row in enumerate(rows, 1)]}
    validate(data)
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["write-schemas", "validate", "pack", "verify", "check-mirror", "catalog"])
    parser.add_argument("file", type=Path, nargs="?")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--mirror", type=Path)
    args = parser.parse_args()
    if args.command == "write-schemas":
        CONTRACT.mkdir(parents=True, exist_ok=True)
        for name, schema in schemas().items():
            (CONTRACT / name).write_text(dumps(schema), encoding="utf-8", newline="\n")
    elif args.command == "check-mirror":
        if not args.mirror:
            raise ValueError("--mirror required")
        for name in list(schemas()) + ["example-stage.json", "CONTRACT.md"]:
            if (CONTRACT / name).read_bytes() != (args.mirror / name).read_bytes():
                raise ValueError("Contract mirror differs: " + name)
    elif args.command == "verify":
        if not args.file:
            raise ValueError("Artifact directory required")
        verify(args.file)
    elif args.command == "catalog":
        if not args.output:
            raise ValueError("--output required; directory must not already exist")
        print(dumps(pack(build_catalog(), args.output)))
    else:
        if not args.file:
            raise ValueError("Content file required")
        data = json.loads(args.file.read_text(encoding="utf-8-sig"))
        validate(data)
        if args.command == "pack":
            if not args.output:
                raise ValueError("--output required; directory must not already exist")
            print(dumps(pack(data, args.output)))
    print("OK")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(2)
