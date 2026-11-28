"""Check a corpus package or catalog without writing files or contacting external services."""
import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker
from jlpt_coverage import checklist_issues


HERE = Path(__file__).resolve().parent


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def ensure(condition, message):
    if not condition:
        raise ValueError(message)


def relative_file(root, relative):
    candidate = (root / relative).resolve()
    ensure(not Path(relative).is_absolute() and candidate.is_relative_to(root),
           f"Path outside root: {relative}")
    ensure(candidate.is_file(), f"Missing file: {relative}")
    return candidate


def source_snapshot(root, source):
    relative = Path(source["localPath"])
    candidate = (root / relative).resolve()
    ensure(not relative.is_absolute() and candidate.is_relative_to(root) and ".." not in relative.parts,
           f"Path outside root: {relative}")
    if candidate.is_file():
        return candidate
    if relative.parts and relative.parts[0] in ("N1", "N2", "N3", "N4", "N5"):
        archive = root / relative.parts[0] / "old"
        for path in archive.rglob("*"):
            if (path.name == relative.name and path.is_file() and path.resolve().is_relative_to(root)
                    and sha256(path) == source["sha256"]):
                return path
    raise ValueError(f"Missing source snapshot: {relative}")


def unique(values, label):
    counts = Counter(values)
    duplicates = [key for key, count in counts.items() if count > 1]
    ensure(not duplicates, f"Duplicate {label}: {duplicates}")
    return set(counts)


def schema_check(data, filename):
    schema = read(HERE / filename)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    error = next(validator.iter_errors(data), None)
    ensure(error is None, f"{error.json_path}: {error.message}" if error else "")


def check_package(p, root, release):
    schema_check(p, "exam-package.schema.json")
    if p["schemaVersion"] == "1.3.0":
        exam = p["exam"]
        ensure(exam["slug"] == f"{exam['year']:04}/{exam['month']:02}", "Slug disagrees with exam date")
        if release or p["review"]["status"] == "approved":
            gaps = checklist_issues(p)
            ensure(not gaps, f"Missing release material ({len(gaps)} checks): {gaps[:3]}")
    source_ids = unique((s["sourceId"] for s in p["sources"]), "sourceId")
    for s in p["sources"]:
        if s["status"] == "available" and s["kind"] != "synthetic":
            ensure(s["localPath"] and s["sha256"], f"Missing source snapshot/hash: {s['sourceId']}")
        if s["localPath"] and s["status"] == "available":
            ensure(sha256(source_snapshot(root, s)) == s["sha256"], f"Source changed: {s['localPath']}")

    unique((a["assetId"] for a in p["assets"]), "assetId")
    assets = {a["assetId"]: a for a in p["assets"]}
    for a in assets.values():
        digest = a["sha256"]
        ensure(a["assetId"] == "sha256:" + digest and a["path"].rsplit(".", 1)[0] == f"assets/sha256/{digest[:2]}/{digest}",
               f"Asset identity/path mismatch: {a['path']}")
        local = relative_file(root, a["path"])
        ensure(local.stat().st_size == a["byteLength"] and sha256(local) == digest, f"Damaged asset: {local}")
        ensure(all(o["sourceId"] in source_ids for o in a["origins"]), f"Unknown origin: {local}")
        ensure(a["derivedFromAssetId"] is None or a["derivedFromAssetId"] in assets, f"Unknown parent asset: {local}")

    def media_ref(url, mime):
        if url:
            asset = assets.get("sha256:" + url.removeprefix("asset://"))
            ensure(asset and asset["mediaType"].startswith(mime + "/"), f"Invalid {mime} reference: {url}")

    ids = []
    node_data = {}
    questions = {}
    mondais = {}
    by_question = {}
    shared_script = set()
    for section, paper in p["content"].items():
        for m in paper["mondais"]:
            ensure(m["section"] == section, f"Wrong section: {m['id']}")
            mondais[m["id"]] = m
            ids.append(m["id"])
            node_data[m["id"]] = m
            for b in m["blocks"]:
                ids.append(b["id"])
                node_data[b["id"]] = b
                for i in b["mediaItems"]:
                    ids.append(i["id"])
                    node_data[i["id"]] = i
                    if i["kind"] in ("audio", "image"):
                        media_ref(i[i["kind"]]["url"], i["kind"])
                    if i["kind"] == "audio" and i["audio"]["scriptJaMd"].strip():
                        shared_script.update(q["id"] for q in b["questions"])
                for q in b["questions"]:
                    qid = q["id"]
                    ids.append(qid)
                    node_data[qid] = q
                    questions[qid] = q
                    by_question[qid] = m["id"]
                    choices = [c["id"] for c in q["choices"]]
                    ensure(choices == [chr(97 + n) for n in range(b["choiceCount"])], f"Choice IDs/count: {qid}")
                    ensure(q["correctChoiceId"] is None or q["correctChoiceId"] in choices, f"Unknown answer: {qid}")
                    media_ref(q.get("audioUrl"), "audio")
                    media_ref(q.get("imageUrl"), "image")
                    if release:
                        ensure(q["correctChoiceId"] and (q["explanation"] or "").strip(), f"Missing key/explanation: {qid}")
                        if section == "choukai":
                            ensure(qid in shared_script or q.get("jlptListenScript", {}).get("scriptJaMd", "").strip(),
                                   f"Missing listening script: {qid}")
    node_ids = unique(ids, "content UUID")
    ensure(p["packageId"] not in node_ids, "Package UUID reused by a content node")
    ann = p["annotations"]
    for target, rows in ann.get("sentencePairs", {}).items():
        node = node_data.get(target, {})
        if node.get("kind") == "passage":
            payload, key = node["passage"], "viMd"
        elif node.get("kind") == "audio" and node["audio"].get("scriptJaMd"):
            payload, key = node["audio"], "scriptViMd"
        else:
            payload, key = node.get("jlptListenScript", {}), "scriptViMd"
        ensure(key in payload, f"Unknown passage/script target: {target}")
        ensure(all(r["ja"].strip() and (r["vi"] is None or r["vi"].strip()) for r in rows),
               f"Blank sentence pair: {target}")
        ensure(payload[key] == "\n".join(r["vi"] for r in rows if r["vi"] is not None),
               f"Full translation differs from sentence pairs: {target}")
    node_annotations = unique((a["nodeId"] for a in ann["nodes"]), "node annotation")
    ensure(node_annotations == node_ids, "Missing or orphan node annotation")
    for a in ann["nodes"]:
        ensure(a["sourceId"] is None or a["sourceId"] in source_ids, "Unknown node source")
        if a["nodeId"] in questions:
            expected = [c["id"] for c in questions[a["nodeId"]]["choices"]]
            ensure([c["choiceId"] for c in a["sourceChoiceLabels"]] == expected,
                   f"Source choice labels: {a['nodeId']}")
    for a in ann["fields"]:
        ensure(a["targetId"] in node_ids and (a["sourceId"] is None or a["sourceId"] in source_ids),
               f"Unknown field target/source: {a['targetId']}")
        if a["origin"] == "ai":
            ensure(all(a[key] for key in ("runId", "model", "skillVersion", "inputSha256")),
                   f"Incomplete AI provenance: {a['targetId']} {a['fieldPointer']}")
        value = node_data[a["targetId"]]
        for key in a["fieldPointer"][1:].split("/"):
            key = key.replace("~1", "/").replace("~0", "~")
            if isinstance(value, list):
                ensure(key.isdecimal() and (key == "0" or not key.startswith("0")) and int(key) < len(value),
                       f"Invalid field pointer: {a['fieldPointer']}")
                value = value[int(key)]
            else:
                ensure(isinstance(value, dict) and key in value, f"Invalid field pointer: {a['fieldPointer']}")
                value = value[key]
    if release:
        explanation_ids = {a["targetId"] for a in ann["fields"] if a["fieldPointer"] == "/explanation"}
        ensure(set(questions) <= explanation_ids, "Missing explanation provenance")
    ensure(unique((a["questionId"] for a in ann["answers"]), "answer annotation") == set(questions),
           "Missing or orphan answer annotation")
    for a in ann["answers"]:
        q = questions[a["questionId"]]
        choices = {c["id"] for c in q["choices"]} | {None}
        ensure(all(a[key] in choices for key in ("aiChoiceId", "sourceChoiceId", "resolvedChoiceId")),
               f"Unknown annotated answer: {q['id']}")
        ensure(a["sourceId"] is None or a["sourceId"] in source_ids, f"Unknown answer source: {q['id']}")
        ensure(a["resolvedChoiceId"] == q["correctChoiceId"], f"Answer mismatch: {q['id']}")
        if a["resolution"] == "source_confirmed":
            ensure(a["sourceId"] and a["resolvedChoiceId"] and a["resolvedChoiceId"] == a["sourceChoiceId"],
                   f"Source-confirmed mismatch: {q['id']}")
        if release:
            ensure(a["resolution"] != "unresolved", f"Unresolved answer: {q['id']}")
    expectations = p["structure"]["expectations"]
    ensure(unique((e["mondaiId"] for e in expectations), "expectation") == set(mondais), "Mondai expectation mismatch")
    for e in expectations:
        size = sum(len(b["questions"]) for b in mondais[e["mondaiId"]]["blocks"])
        ensure(e["questionCount"] in (None, size), f"Expected {e['questionCount']} questions, got {size}: {e['mondaiId']}")
    for timing in p["structure"]["timings"]:
        ensure(timing["sourceId"] is None or timing["sourceId"] in source_ids, "Unknown exam timing source")
    for g in ann.get("grammarRefs", []):
        ensure(g["questionId"] in questions, f"Unknown grammar target: {g['questionId']}")
        ensure("\\" not in g["path"] and ":" not in g["path"] and not g["path"].startswith("/")
               and all(part not in ("", ".", "..") for part in g["path"].split("/")), f"Invalid grammar path: {g['path']}")
    master = p["masterAudio"]
    if master and master["assetId"]:
        audio = assets.get(master["assetId"])
        ensure(audio and audio["mediaType"].startswith("audio/"), "Missing master audio asset")
        ensure(not (master["durationMs"] and audio["durationMs"] and master["durationMs"] != audio["durationMs"]),
               "Master duration differs from its source asset")
    if release and p["content"]["choukai"]["mondais"]:
        ensure(master and (master["assetId"] or master["rss"]), "Missing playable master")
    for m in p["content"]["choukai"]["mondais"]:
        for b in m["blocks"]:
            urls = [q.get("audioUrl") for q in b["questions"]]
            urls.extend(i["audio"]["url"] for i in b["mediaItems"] if i["kind"] == "audio")
            for url in filter(None, urls):
                ensure(master and "sha256:" + url.removeprefix("asset://") == master["assetId"],
                       "Listening blocks and questions must use the exam master")
    for segment in ann["audioSegments"]:
        mid, qids = segment["mondaiId"], segment["questionIds"]
        ensure(master and mid in mondais and mondais[mid]["section"] == "choukai", "Missing master/listening mondai")
        ensure(segment["sourceId"] in source_ids, "Unknown cue source")
        ensure(all(by_question.get(qid) == mid for qid in qids), "Cue references another mondai")
        role = segment["role"]
        ensure((role == "question" and len(qids) == 1) or (role == "shared" and len(qids) > 1)
               or (role in ("mondai", "intro", "example") and not qids), "Cue targets do not match role")
        start, end, duration = segment["startMs"], segment["endMs"], master["durationMs"]
        ensure(end is None or start < end, "Cue end must follow start")
        ensure(duration is None or (start < duration and (end is None or end <= duration)), "Cue outside master")
    review = p["review"]
    ensure(all(i["targetId"] is None or i["targetId"] in node_ids or i["targetId"] == p["packageId"] for i in review["issues"]),
           "Unknown review target")
    if release:
        ensure(questions and review["status"] == "approved" and review["reviewedBy"] and review["reviewedAt"],
               "Package awaiting review")
        ensure(not any(i["severity"] == "error" for i in review["issues"]), "Review has open errors")
        ensure(all(f["reviewStatus"] == "approved" for f in ann["fields"]), "Unapproved field")
    return node_ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="JLPT corpus root")
    parser.add_argument("--release", action="store_true", help="Apply editorial release checks")
    args = parser.parse_args()
    root = args.root.resolve()
    data = read(args.path)
    if "packages" not in data:
        check_package(data, root, args.release)
    else:
        schema_check(data, "catalog.schema.json")
        package_ids = unique((e["packageId"] for e in data["packages"]), "catalog package")
        unique((e["path"] for e in data["packages"]), "catalog path")
        all_nodes = set()
        slugs = set()
        for e in data["packages"]:
            path = relative_file(root, e["path"])
            ensure(sha256(path) == e["sha256"], f"Catalog checksum: {path}")
            p = read(path)
            ensure((p["packageId"], p["revision"]) == (e["packageId"], e["revision"]), f"Catalog identity: {path}")
            nodes = check_package(p, root, args.release)
            ensure(not package_ids.intersection(nodes), f"Package UUID reused by a content node: {path}")
            ensure(not all_nodes.intersection(nodes), f"UUID shared between packages: {path}")
            all_nodes.update(nodes)
            slug = (p["exam"]["level"], p["exam"]["slug"].replace("/", "-"))
            ensure(slug not in slugs, f"Duplicate level/slug: {slug}")
            slugs.add(slug)
    print(f"OK {args.path}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        sys.exit(str(error))

