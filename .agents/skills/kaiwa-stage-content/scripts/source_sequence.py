"""Find book units suitable for a stage. Shared placements are editorial suggestions."""
import argparse
import json
from pathlib import Path
import re
import sys

PLAN_NAME = "SOURCE_SEQUENCE.json"
INDEX = "kaiwa_skill/planning/catalog27/source_index.jsonl"
FAMILIES = {"speak_japanese", "shadowing", "nama_chuukei", "nameraka"}
LEVELS = ["Sơ", "Trung", "Thượng"]
ASSIGNMENT_STATUS = {"planned", "provisional", "authored"}


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def inside(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Path outside repository: " + str(relative))
    return path


def curriculum_pointer(repo, curriculum=None):
    """The draft's pinned curriculum, else the published pointer, else nothing."""
    if curriculum:
        return curriculum
    pointer = repo / "kaiwa_skill/planning/CURRENT_ROADMAP.json"
    return read(pointer) if pointer.exists() else None


def plan_path(repo, curriculum=None):
    spec = curriculum_pointer(repo, curriculum)
    if not spec or not isinstance(spec.get("roadmap"), str):
        return None
    return inside(repo, spec["roadmap"]).parent / PLAN_NAME


def load_plan(repo, curriculum=None):
    """Return the plan, or None when this curriculum has no sequence plan yet."""
    path = plan_path(repo, curriculum)
    return read(path) if path and path.exists() else None


def stage_orders(repo, curriculum=None):
    """Stage UID -> (global order, level); registry insertion order is the fallback."""
    spec = curriculum_pointer(repo, curriculum)
    if not spec:
        raise ValueError("No curriculum pointer for the sequence plan")
    registry = read(inside(repo, spec["registry"]))
    return {uid: (info.get("order", index), info.get("level"))
            for index, (uid, info) in enumerate(registry.items(), 1)}


def unit_index(repo, books):
    """Book ID -> {anchor: (position, label)} in book order, from the 27-book index."""
    path = repo / INDEX
    if not path.exists():
        raise ValueError("Source index missing: " + INDEX)
    result = {book: {} for book in books}
    with path.open(encoding="utf-8-sig") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            anchors = result.get(row.get("book_id"))
            anchor = row.get("anchor")
            if anchors is not None and anchor and anchor not in anchors:
                anchors[anchor] = (len(anchors), row.get("label", ""))
    return result


def unit_key(item):
    return (item.get("book_id"), item.get("unit"), item.get("part") or "")


def check_plan(repo, plan, curriculum=None):
    """Return (errors, warnings, index, orders); never mutates the plan."""
    errors, warnings = [], []
    if plan.get("schema_version") != "1.0":
        errors.append("Sequence plan schema_version must be 1.0")
    approval = plan.get("approval", {}).get("status")
    if approval not in {"draft", "approved"}:
        errors.append("Sequence plan approval.status must be draft or approved")

    books = plan.get("books", {})
    active = {}
    for book, config in books.items():
        if config.get("family") not in FAMILIES:
            errors.append("Unknown family for " + book)
        if not config.get("levels") or any(level not in LEVELS for level in config["levels"]):
            errors.append("Book levels must be chosen from Sơ/Trung/Thượng: " + book)
        if config.get("status") == "excluded":
            if not config.get("reason"):
                errors.append("Excluded book needs a reason: " + book)
            continue
        if config.get("status") != "active":
            errors.append("Book status must be active or excluded: " + book)
            continue
        try:
            active[book] = re.compile(config.get("unit_pattern") or "(?!)")
        except re.error:
            errors.append("Invalid unit_pattern for " + book)
    index = unit_index(repo, active)
    for book, pattern in active.items():
        if not any(pattern.search(anchor) for anchor in index[book]):
            errors.append("unit_pattern matches no anchor in the source index: " + book)
    orders = stage_orders(repo, curriculum)
    seen = set()
    for item in plan.get("assignments", []):
        book, unit, part = unit_key(item)
        label = str(book) + ":" + str(unit) + ("#" + part if part else "")
        if book not in active:
            errors.append("Assignment uses a book that is not active in the plan: " + label)
            continue
        if unit not in index[book] or not active[book].search(unit):
            errors.append("Assignment unit is not a schedulable unit of the book: " + label)
            continue
        if item.get("status") not in ASSIGNMENT_STATUS:
            errors.append("Assignment status must be planned/provisional/authored: " + label)
        if item.get("stage_uid") not in orders:
            errors.append("Assignment points to an unknown stage: " + label)
            continue
        _, level = orders[item["stage_uid"]]
        if level not in books[book]["levels"]:
            errors.append("Stage level " + str(level) + " is outside the book levels: " + label)
        if part:
            errors.append("CD pack cannot be split into parts: " + label)
        if (book, unit, part) in seen:
            errors.append("Unit assigned twice: " + label)
        seen.add((book, unit, part))
    for book, unit, part in seen:
        if part and (book, unit, "") in seen:
            errors.append("A unit cannot be assigned both whole and in parts: " + book + ":" + unit)
    return errors, warnings, index, orders


def stage_assignments(plan, uid):
    return [item for item in plan.get("assignments", []) if item.get("stage_uid") == uid]


def check_stage(repo, plan, curriculum, uid, data, audit, source_entries):
    """Check one authored stage against the plan; return (errors, warnings)."""
    errors, warnings, index, orders = check_plan(repo, plan, curriculum)
    if errors:
        return ["Sequence plan is invalid; fix the plan before authoring: " + error for error in errors], warnings
    if uid not in orders:
        return ["Stage is not in the curriculum registry of the sequence plan"], warnings
    books = plan.get("books", {})
    active = {book for book, config in books.items() if config.get("status") == "active"}
    excluded = {book for book, config in books.items() if config.get("status") == "excluded"}
    nodes = {node["id"]: (position, node) for position, node in enumerate(data["nodes"])}
    declared = audit.get("sequence_units", {})
    if not isinstance(declared, dict):
        return ["source-map sequence_units must map node IDs to unit lists"], warnings
    books_declared = set()
    for nid, units in declared.items():
        if nid not in nodes or nodes[nid][1]["type"] in {"live_challenge", "free_talk"}:
            errors.append("sequence_units points to an unknown or Live node: " + nid)
            continue
        for unit in units:
            key = unit_key(unit)
            book, anchor, part = key
            label = str(book) + ":" + str(anchor) + ("#" + part if part else "")
            role = unit.get("role", "teach")
            if part:
                errors.append("CD pack cannot be split into parts: " + label)
            if book not in active or anchor not in index.get(book, {}):
                errors.append("sequence_units names an unknown unit or a book outside the plan: " + label)
                continue
            books_declared.add(book)
            if not re.search(books[book]["unit_pattern"], anchor):
                errors.append("Not a practice unit: " + label)
            if orders[uid][1] not in books[book]["levels"]:
                errors.append("Stage level outside the book levels: " + label)
            if role not in {"teach", "review"}:
                errors.append("sequence_units role must be teach or review: " + label)
    for node_position, node in nodes.values():
        if node["type"] == "knowledge" and node["data"].get("source_family") == "speak_japanese":
            units = declared.get(node["id"], [])
            if not any(unit.get("role", "teach") == "teach" and books.get(unit.get("book_id"), {}).get("family") == "speak_japanese"
                       for unit in units):
                errors.append("Speak Japanese knowledge needs its source book unit in sequence_units: " + node["id"])
    used = {entry.get("book_id") for entry in source_entries if entry.get("kind") == "book"}
    used |= {source.get("book_id") for source in data.get("source_registry", [])}
    for book in sorted((used & active) - books_declared):
        errors.append("Ordered book is used without sequence_units; declare the selected units: " + book)
    for book in sorted(used & excluded):
        warnings.append("Book is excluded as a practice source (" + books[book]["reason"] + "): " + book)
    return errors, list(dict.fromkeys(warnings))


def describe(item, index, orders, registry):
    info = registry.get(item["stage_uid"], {})
    label = index[item["book_id"]][item["unit"]][1] if item["unit"] in index.get(item["book_id"], {}) else "?"
    return {"book_id": item["book_id"], "unit": item["unit"], "part": item.get("part", ""), "label": label,
            "stage": info.get("display_code"), "status": item.get("status"), "note": item.get("note", "")}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["check", "units", "stage", "table"])
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--book", help="Book ID for units, e.g. B11")
    parser.add_argument("--stage", help="Stage UID for stage")
    parser.add_argument("--all", action="store_true", help="units: list every anchor, not only schedulable units")
    parser.add_argument("--level", choices=LEVELS, help="table: only stages of this level")
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    plan = load_plan(repo)
    if plan is None:
        raise ValueError("No " + PLAN_NAME + " next to the current roadmap")
    errors, warnings, index, orders = check_plan(repo, plan)
    registry = read(inside(repo, curriculum_pointer(repo)["registry"]))
    if args.command == "check":
        counts = {}
        for item in plan.get("assignments", []):
            counts[item.get("book_id")] = counts.get(item.get("book_id"), 0) + 1
        print(json.dumps({"errors": errors, "warnings": warnings, "assigned_units": counts,
                          "approval": plan.get("approval", {}).get("status")}, ensure_ascii=False, indent=2))
        if errors:
            sys.exit(2)
        return
    if args.command == "units":
        config = plan.get("books", {}).get(args.book or "")
        if not config:
            raise ValueError("--book must name a book in the plan")
        if config.get("status") != "active":
            raise ValueError("Book is excluded: " + config.get("reason", ""))
        pattern = re.compile(config["unit_pattern"])
        placed = {}
        for item in plan.get("assignments", []):
            if item.get("book_id") == args.book:
                placed.setdefault(item.get("unit"), []).append(
                    registry.get(item.get("stage_uid"), {}).get("display_code", "?") + ("#" + item["part"] if item.get("part") else ""))
        for anchor, (position, label) in index[args.book].items():
            if args.all or pattern.search(anchor):
                print("\t".join([anchor, ",".join(placed.get(anchor, [])) or "-", label]))
        return
    if args.command == "table":
        # A readable view of the allocation for the project owner's review; the JSON plan stays the source.
        by_stage = {}
        for item in plan.get("assignments", []):
            if item.get("stage_uid") in orders and item.get("unit") in index.get(item.get("book_id"), {}):
                by_stage.setdefault(item["stage_uid"], []).append(item)
        print("| Chặng | Tên | Đơn vị sách được xếp |\n|---|---|---|")
        for uid, (order, level) in sorted(orders.items(), key=lambda pair: pair[1][0]):
            if args.level and level != args.level:
                continue
            units = sorted(by_stage.get(uid, []), key=lambda item: (item["book_id"], index[item["book_id"]][item["unit"]][0]))
            cell = "<br>".join(item["book_id"] + " · " + index[item["book_id"]][item["unit"]][1].replace("|", "/")
                               + (" (" + item["part"] + ")" if item.get("part") else "")
                               + (" · tạm" if item.get("status") == "provisional" else "") for item in units)
            print("| " + str(registry[uid].get("display_code")) + " | " + str(registry[uid].get("title")).replace("|", "/") + " | " + (cell or "") + " |")
        return
    if not args.stage or args.stage not in orders:
        raise ValueError("--stage must be a stage UID of the current roadmap")
    if errors:
        raise ValueError("Sequence plan is invalid: " + "; ".join(errors))
    order = orders[args.stage][0]
    earlier = {}
    for item in plan.get("assignments", []):
        if item["stage_uid"] in orders and orders[item["stage_uid"]][0] < order:
            earlier[item["book_id"]] = earlier.get(item["book_id"], 0) + 1
    print(json.dumps({"stage": registry[args.stage].get("display_code"), "level": orders[args.stage][1],
                      "suggestions": [describe(item, index, orders, registry) for item in stage_assignments(plan, args.stage)],
                      "units_listed_earlier_per_book": earlier, "warnings": warnings}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        sys.exit(2)
