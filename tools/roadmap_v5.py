"""Validate, assemble and render the V5 Kaiwa roadmap; source books remain read-only."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata
import uuid

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "kaiwa_skill/planning/v5"
LEVELS = ["Sơ", "Trung", "Thượng"]
BRANCHES = {"routine", "accepted", "declined", "conditional", "pending", "alternative", "misunderstanding", "problem", "resolved", "unresolved", "follow_up"}
BRANCH_VI = dict(zip(["routine", "accepted", "declined", "conditional", "pending", "alternative", "misunderstanding", "problem", "resolved", "unresolved", "follow_up"], ["Tiến hành", "Đồng ý", "Từ chối", "Có điều kiện", "Chờ xác nhận", "Phương án khác", "Hiểu khác nhau", "Phát sinh", "Đã làm rõ/xử lý", "Còn vướng", "Liên hệ tiếp"]))

def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf8", newline="\n")
    temp.replace(path)

def write_text(path, value):
    path.write_text("\n".join(line.rstrip() for line in value.splitlines()).rstrip() + "\n", encoding="utf8", newline="\n")

def fold(value):
    value = unicodedata.normalize("NFD", value.casefold()).replace("đ", "d")
    return " ".join("".join(c for c in value if not unicodedata.combining(c)).split())

def collect():
    manifest = read(OUT / "BUILD_MANIFEST.json")
    stages, errors, pending = [], [], []
    assigned = Counter(s["owner"] for s in manifest["stages"])
    completed = Counter()
    for spec in manifest["stages"]:
        path = OUT / "work/stages" / (spec["key"] + ".json")
        if not path.exists():
            pending.append(spec["key"])
            continue
        try:
            body = read(path)
            if body["stage_key"] != spec["key"] or body["uid"] != spec["uid"] or body["worker"] != spec["owner"]:
                raise ValueError("stage identity/ownership mismatch")
            stages.append({**spec, **{k: v for k, v in body.items() if k not in ["stage_key", "uid", "worker", "status"]},
                           "roadmap_status": "authored", "lesson_status": "not_authored", "authorship": "ai_authored",
                           "author_file": path.relative_to(ROOT).as_posix(), "author_sha256": digest(path)})
            completed[spec["owner"]] += 1
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f"{spec['key']}: {exc}")
    state = {"version": "5.0", "status": "authoring" if pending or errors else "awaiting_editorial_review",
             "updated_at": datetime.now(timezone.utc).isoformat(), "total_stages": len(manifest["stages"]),
             "complete_stage_files": len(stages), "assigned": dict(assigned), "completed_by_owner": dict(completed),
             "pending_keys": pending, "errors": errors, "next_action": "Continue the first missing stage in each owner assignment; never reset finished files.",
             "checkpoint_rule": "Stage files are atomic checkpoints; their existence is not a claim that lessons or dialogues have been authored."}
    published_meta = OUT / "KAIWA_CHANG_V5_META.json"
    pointer = ROOT / "kaiwa_skill/planning/CURRENT_ROADMAP.json"
    if not pending and not errors and published_meta.exists() and pointer.exists() and read(pointer).get("version") == "5.0":
        hashes = {s["key"]: s["author_sha256"] for s in stages}
        if read(published_meta).get("status") == "roadmap_published" and read(published_meta).get("author_stage_hashes") == hashes:
            state["status"] = "roadmap_published"
            state["next_action"] = "Author or upgrade lessons by UID; use the existing roadmap and preserve IDs."
    atomic(OUT / "BUILD_STATE.json", state)
    return manifest, stages, state

def external_sources():
    result = []
    for owner, name in [("daily", "daily_web_sources.json"), ("support", "support_web_sources.json"), ("work", "work_web_sources.json")]:
        path = OUT / "work" / name
        if not path.exists():
            continue
        for entry in read(path)["sources"]:
            result.append({**entry, "id": owner + ":" + entry["id"], "reported_by": owner,
                           "ledger": path.relative_to(ROOT).as_posix(), "scope": "Research context; newly authored scenarios remain AI-authored."})
    return result

def validate(manifest, stages, state, partial=False):
    errors, warnings = list(state["errors"]), []
    source = ROOT / "kaiwa_skill/planning/v2/KAIWA_CHANG_V4_1.jsonl"
    normalized_source = hashlib.sha256(source.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    if digest(source) != manifest["source_base_sha256"] and normalized_source != manifest.get("source_base_sha256_lf"):
        errors.append("V4.1 changed since the V5 manifest was composed")
    if state["pending_keys"] and not partial:
        errors.append(f"{len(state['pending_keys'])} stages have no authored situation file")
    specs = {x["key"]: x for x in manifest["stages"]}
    retired = {x["legacy_id"]: x for x in manifest["retired"]}
    active_uids = {x["uid"] for x in manifest["stages"]}
    if len(active_uids) != len(specs) or len(specs) != len(manifest["stages"]):
        errors.append("Duplicate stage UID/key")
    if len({s["code"] for s in manifest["stages"]}) != len(specs):
        errors.append("Duplicate display code")
    ordered = [k for g in manifest["groups"] for k in g["keys"]]
    if ordered != [s["key"] for s in manifest["stages"]]:
        errors.append("Cluster/order manifest mismatch")
    base = [json.loads(s) for s in source.read_text(encoding="utf8").splitlines() if s.strip()]
    aliases = {a: s for s in manifest["stages"] for a in s["legacy_ids"]}
    if set(aliases) | set(retired) != {s["id"] for s in base} or set(aliases) & set(retired):
        errors.append("A legacy stage is missing or simultaneously active and retired")
    for s in base:
        if s["id"] in aliases and aliases[s["id"]]["uid"] != s["uid"]:
            errors.append("Legacy UID changed: " + s["id"])
    for r in retired.values():
        if not r["redirect_keys"] or not set(r["redirect_keys"]) <= set(specs):
            errors.append("Broken retired redirect: " + r["legacy_id"])
    ledgers = {x["id"] for x in external_sources()}
    book_evidence = {x["id"] for x in read(ROOT / "kaiwa_skill/planning/v5_preview/sources.json")["book_evidence"]}
    duplicate_titles, nonoral = defaultdict(list), []
    for s in stages:
        key = s["key"]
        for f in ["objective", "coverage_note"]:
            if not isinstance(s.get(f), str) or not s[f].strip():
                errors.append(key + ": missing " + f)
        if not isinstance(s.get("knowledge_focus"), list) or len(s["knowledge_focus"]) < 2:
            errors.append(key + ": missing knowledge focus")
        events = {e["id"]: e for e in s.get("events", [])}
        cases = s.get("situations", [])
        ids = {c["id"] for c in cases}
        if len(events) != len(s.get("events", [])) or not events:
            errors.append(key + ": duplicate or absent events")
        if len(ids) != len(cases) or len(cases) < 8:
            errors.append(key + ": duplicate/absent/thin situation file")
        if len({fold(c["title"]) for c in cases}) != len(cases):
            errors.append(key + ": duplicate scenario title within stage")
        seen = set()
        for c in cases:
            if c.get("event_id") not in events or c.get("branch") not in BRANCHES:
                errors.append(key + ": invalid event/branch at " + c["id"])
            if c.get("origin") != "ai_authored":
                errors.append(key + ": new scenarios must not inherit book attribution")
            for parent in c.get("continues_from", []):
                if parent not in seen:
                    errors.append(key + ": continuation not earlier in same stage: " + c["id"])
            seen.add(c["id"])
            duplicate_titles[fold(c["title"])].append(key + ":" + c["id"])
            if re.search(r"\b(viết email|soạn email|điền đơn|điền form|viết CV|viết báo cáo|luyện viết|gõ văn bản)\b", c["title"], re.I):
                nonoral.append({"stage": key, "id": c["id"], "title": c["title"]})
        if set(s.get("cross_stage_refs", [])) - (set(specs) | set(retired)):
            errors.append(key + ": unknown cross-stage reference")
        for ref in s.get("source_refs", []):
            if not isinstance(ref, str):
                errors.append(key + ": source_ref must be a string")
                continue
            canonical = ref if ":" in ref else s["owner"] + ":" + ref
            if canonical not in ledgers and ref not in book_evidence and not re.fullmatch(r"B\d{2}(?::.*)?", ref):
                warnings.append({"stage": key, "source_ref": ref, "issue": "unresolved; inspect as research note, not confirmed citation"})
        if len(events) < 3 or len(cases) < 12:
            warnings.append({"stage": key, "issue": "review depth in context", "events": len(events), "situations": len(cases)})
    repeated = [{"title_normalized": title, "locations": locations} for title, locations in duplicate_titles.items() if len(locations) > 1]
    audit = {"errors": errors, "warnings": warnings, "possible_nonoral_tasks": nonoral,
             "exact_titles_repeated_across_stages": repeated,
             "limits": ["Automated checks prove structural integrity, not exhaustive real-world coverage, naturalness or semantic nonduplication.",
                        "All new scenario summaries are editorial AI-authored proposals for future dialogue lessons; books/web supply separate inspiration and factual support."]}
    atomic(OUT / "STRUCTURAL_AUDIT.json", audit)
    if errors:
        raise ValueError("\n".join(errors[:25]))
    return audit

def normalize_stage(s, specs, retired):
    out = dict(s)
    links = []
    for key in s.get("cross_stage_refs", []):
        links.extend(retired[key]["redirect_keys"] if key in retired else [key])
    out["related_stage_uids"] = list(dict.fromkeys(specs[k]["uid"] for k in links if k != s["key"]))
    out["display_code"] = out.pop("code")
    out.pop("scenario_status", None)
    out["legacy_seed_situations"] = out.pop("seed_situations", [])
    if "preview_situations" in out:
        out["preview_seed_situations"] = out.pop("preview_situations")
    ledgers = {x["id"] for x in external_sources()}
    book_evidence = {x["id"] for x in read(ROOT / "kaiwa_skill/planning/v5_preview/sources.json")["book_evidence"]}
    refs = [r if ":" in r else s["owner"] + ":" + r for r in s.get("source_refs", [])]
    out["source_basis"] = {"legacy_seed_tokens": out.pop("source_seed_tokens", []),
                           "legacy_bank_tokens": out.pop("source_bank_tokens", []),
                           "lookup_books_not_verified": out.pop("lookup_books", []),
                           "external_research": [r for r in refs if r in ledgers],
                           "book_evidence_from_preview": ["preview:" + r for r in s.get("source_refs", []) if r in book_evidence],
                           "book_research_notes_not_dialogue_attribution": [r for r in s.get("source_refs", []) if r.startswith("B")],
                           "unresolved_research_notes": [raw for raw, canon in zip(s.get("source_refs", []), refs) if canon not in ledgers and raw not in book_evidence and not raw.startswith("B")],
                           "new_scenario_authorship": "ai_authored"}
    for c in out["situations"]:
        c["uid"] = str(uuid.uuid5(uuid.UUID(s["uid"]), c["id"]))
        c["level"] = s["level"]
    out["learner_access"] = "open"
    return out

def render(manifest, stages, audit, published=False):
    specs = {x["key"]: x for x in manifest["stages"]}
    retired = {x["legacy_id"]: x for x in manifest["retired"]}
    course = [normalize_stage(s, specs, retired) for s in stages]
    scenario_count = sum(len(s["situations"]) for s in course)
    stats = {"stages": len(course), "levels": dict(Counter(s["level"] for s in course)),
             "clusters": len(manifest["groups"]), "events": sum(len(s["events"]) for s in course),
             "situations": scenario_count, "branches": dict(Counter(c["branch"] for s in course for c in s["situations"])),
             "linked_continuations": sum(bool(c.get("continues_from")) for s in course for c in s["situations"]),
             "preserved_legacy_stages": sum(bool(s["legacy_ids"]) for s in course), "retired_legacy_stages": len(retired),
             "new_stages": sum(not s["legacy_ids"] for s in course),
             "scenario_count_range": [min(len(s["situations"]) for s in course), max(len(s["situations"]) for s in course)],
             "external_research_entries": len(external_sources()), "dialogue_lessons_authored": 0,
             "scope": "Roadmap and detailed speaking-situation plans, not a finished lesson corpus."}
    atomic(OUT / "STATS.json", stats)
    path = OUT / "KAIWA_CHANG_V5.jsonl"
    write_text(path, "\n".join(json.dumps(s, ensure_ascii=False) for s in course))
    registry = {s["uid"]: {"display_code": s["display_code"], "title": s["title"], "level": s["level"],
                           "order": s["order"], "stage_key": s["key"], "cluster_id": s["cluster_id"], "status": "active"} for s in course}
    atomic(OUT / "chang_registry.json", registry)
    migration = {s["legacy_ids"][0]: {"status": "active", "uid": s["uid"], "display_code": s["display_code"], "title": s["title"],
                    "changed_scope": s["scope_note"], "redirect_uids": [s["uid"]]} for s in course if s["legacy_ids"]}
    for key, r in retired.items():
        migration[key] = {**r, "status": "retired_redirect", "redirect_uids": [specs[k]["uid"] for k in r["redirect_keys"]]}
    atomic(OUT / "MIGRATION_V4_1.json", migration)
    atomic(OUT / "SOURCES_EXTERNAL.json", {"entries": external_sources(), "note": "Research was reported by the named worker. Read scope/limits per source. No source count is a dialogue quality score."})
    resource_roles = read(ROOT / "kaiwa_skill/planning/v5_preview/book_audit.json")
    meta = {"schema_version": "5.0-roadmap", "status": "roadmap_published" if published else "rendered_draft", "slogan": manifest["slogan"],
            "stats": stats, "clusters": manifest["groups"], "source_policy": manifest["source_policy"],
            "author_stage_hashes": {s["key"]: s["author_sha256"] for s in course},
            "resource_roles": resource_roles,
            "resource_roles_basis": "Inherited catalog/preview audit, not a fresh full-text reread of all 27 PDFs in this build.",
            "learning_design": {"oral_only": True, "learner_tests": False, "gates": False,
                "knowledge": "Markdown; selected Speak Japanese knowledge/video immediately followed by shadowing its examples.",
                "vocabulary": "Topic/event lists with new and reused items; app owns drills.",
                "grammar": "Names/references from bunpou/Minna when useful; do not invent IDs.",
                "practice": "Dialogue and grouped sentence shadowing, full and role-swapped, plus one Live AI context node per stage.",
                "cumulative": "Read the preceding two actual lessons and relevant older content when authoring; roadmap order is advisory, not proof lessons exist.",
                "authorship": "Books, external research and original AI-authored knowledge/dialogue all contribute; factual support and dialogue authorship remain distinct."}}
    atomic(OUT / "KAIWA_CHANG_V5_META.json", meta)
    render_markdown(course, manifest, migration, stats, audit)
    render_html(course, manifest, migration, stats)
    return course, stats

def render_markdown(course, manifest, migration, stats, audit):
    main = ["# Kaiwa V5 — lộ trình nghe và nói", "", '> **“Bạn chỉ giỏi kaiwa khi bạn nói đủ nhiều.”**', "",
            f"**{stats['stages']} chặng · {stats['clusters']} cụm · {stats['events']} họ sự kiện · {stats['situations']} tình huống nói.**", "",
            "Đây là khung lộ trình và bản thiết kế tình huống chi tiết. Chưa phải toàn bộ bài học, danh sách từ/ngữ pháp hay hội thoại Nhật–Việt đã được biên soạn.", "",
            "27 sách là nền tài nguyên; nghiên cứu ngoài và AI viết mới có vai trò thiết yếu. Mọi tình huống mới ở bản này đều ghi AI biên soạn. Token sách kế thừa và đầu mối tra tiếp không được coi là nguồn xác nhận cho mọi tình huống mới.", "",
            "Thứ tự là gợi ý từ dễ đến khó; người học mở tự do theo nhu cầu. Sơ luyện thông tin cụ thể và nhận hỗ trợ; Trung giải thích, điều chỉnh và xử lý nhánh; Thượng thương lượng, điều phối và quan hệ phức tạp. Không bài viết/email/điền form, không kiểm tra, điểm hay cổng mở bài.", "",
            f"Giữ UID của **{stats['preserved_legacy_stages']}** chặng cũ, phân lại nội dung **{stats['retired_legacy_stages']}** chặng quá rộng/tổng hợp, thêm **{stats['new_stages']}** chặng. Mã hiển thị được đánh lại; dùng UID hoặc stage key khi chỉnh sửa.", "",
            "- [Đọc đầy đủ Sơ cấp](SO_CAP.md)", "- [Đọc đầy đủ Trung cấp](TRUNG_CAP.md)", "- [Đọc đầy đủ Thượng cấp](THUONG_CAP.md)",
            "- [Tra cứu và lọc tương tác](ROADMAP.html)", "- [Phạm vi, nguồn, kế thừa và kế hoạch biên soạn](DESIGN_AND_MIGRATION.md)",
            "- [16 bối cảnh du lịch để lồng ghép](TRAVEL_CONTEXTS.md)",
            "- [Kiểm tra biên tập và giới hạn](EDITORIAL_REVIEW.md)", ""]
    bykey = {s["key"]: s for s in course}
    for level in LEVELS:
        selected = [s for s in course if s["level"] == level]
        main += [f"## {level} — {len(selected)} chặng", ""]
        detail = [f"# Kaiwa V5 — {level}", "", "[Mục lục toàn lộ trình](KAIWA_CHANG_V5.md) · [Tra cứu tương tác](ROADMAP.html)", "",
                  "Các cảnh là kế hoạch cuộc nói, chưa có hội thoại mẫu hoàn chỉnh. ID S001... là ID cục bộ trong UID chặng; không phải mã cấp Sơ. Nhánh nối tiếp ghi tình huống cha. Vai và điều kiện có thể đổi theo sự kiện, không có cổng học.", ""]
        for group in [g for g in manifest["groups"] if g["level"] == level]:
            main += [f"### {group['id']} — {group['title']}", ""]
            detail += [f"## {group['id']} — {group['title']}", ""]
            for key in group["keys"]:
                s = bykey[key]
                main.append(f"- **{s['display_code']} — {s['title']}** · {s['track']} · {len(s['events'])} sự kiện / {len(s['situations'])} tình huống · key `{s['key']}`")
                detail += [f"### {s['display_code']} — {s['title']}", "", f"**Key:** `{s['key']}` · **UID:** `{s['uid']}` · **Nhánh:** {s['track']}", "",
                           "**Mục tiêu nói:** " + s["objective"], "", "**Kiến thức cần lồng ghép khi soạn bài:**", ""]
                detail.extend("- " + p for p in s["knowledge_focus"])
                detail.append("")
                for e in s["events"]:
                    detail += [f"#### {e['id']} — {e['name']}", "", "Vai: " + " ↔ ".join(e["roles"]) + ".", ""]
                    for c in s["situations"]:
                        if c["event_id"] != e["id"]:
                            continue
                        parent = " · tiếp từ " + ", ".join(c["continues_from"]) if c.get("continues_from") else ""
                        detail.append(f"- **{c['id']} [{BRANCH_VI[c['branch']]}]** {c['title']}{parent}")
                    detail.append("")
                detail += ["**Ranh giới/bao phủ:** " + s["coverage_note"], ""]
                if s["scope_note"]:
                    detail += ["**Phân ranh với bản cũ:** " + s["scope_note"], ""]
                if s["cross_stage_refs"]:
                    detail += ["**Liên quan:** " + ", ".join(s["cross_stage_refs"]) + ".", ""]
                detail += ["**Nguồn:** tình huống AI biên soạn; tra sách " + (", ".join(s["source_basis"]["lookup_books_not_verified"]) or "theo chức năng phù hợp") +
                           "; nghiên cứu ngoài: " + (", ".join(s["source_basis"]["external_research"]) or "chưa gắn riêng cho chặng") + ". Không gán audio gốc cho hội thoại viết mới.", ""]
            main.append("")
        write_text(OUT / {"Sơ": "SO_CAP.md", "Trung": "TRUNG_CAP.md", "Thượng": "THUONG_CAP.md"}[level], "\n".join(detail))
    write_text(OUT / "KAIWA_CHANG_V5.md", "\n".join(main))
    design = ["# Thiết kế và chuyển tiếp V4.1 → V5", "", "## Chặng cũ phân nội dung sang nơi rõ mục tiêu hơn", ""]
    for key, item in migration.items():
        if item["status"] == "retired_redirect":
            design += [f"- **{key}** → " + "; ".join(k + " (" + bykey[k]["title"] + ")" for k in item["redirect_keys"]) + "."]
    editorial = OUT / "DESIGN_NOTES.md"
    if editorial.exists():
        design += ["", editorial.read_text(encoding="utf8")]
    design += ["", "## Nguồn ngoài", "", "Các nguồn sau cung cấp bối cảnh/nhu cầu hoặc dữ kiện cần hỏi; không tự biến thành mẫu hội thoại nguyên văn. Xem ledger theo worker để biết giới hạn và độ sâu đọc.", ""]
    for w in external_sources():
        title = w.get("title") or w.get("publisher") or w.get("owner") or w["id"]
        status = w.get("read_status") or ("opened_reported" if w.get("read") else "unspecified")
        design.append(f"- **{w['id']}** [{title}]({w['url']}) · đọc: **{status}**. {w.get('supports') or w.get('use') or ''} Giới hạn: {w.get('limit') or w.get('does_not_establish') or 'cần xác minh theo ngữ cảnh khi soạn bài.'}")
    write_text(OUT / "DESIGN_AND_MIGRATION.md", "\n".join(design))
    travel = read(OUT / "TRAVEL_CONTEXTS.json")
    lines = ["# Bối cảnh du lịch cho V5", "", "16 lớp bối cảnh, không cộng thành 16 chặng. Đây là gợi ý mở rộng khi soạn hội thoại, chưa kiểm đầy đủ dữ kiện từng địa danh hoặc hoạt động hiện hành.", ""]
    for t in travel:
        lines += ["## " + t["id"] + " — " + t["title"], "", t["recommendation"], "", "**Gắn vào:** " + "; ".join(bykey[k]["display_code"] + " — " + bykey[k]["title"] for k in t["host_refs"]) + ".", ""]
        lines += ["- " + text for text in t["situations"]] + [""]
    write_text(OUT / "TRAVEL_CONTEXTS.md", "\n".join(lines))

def render_html(course, manifest, migration, stats):
    template = (OUT / "work/roadmap_template.html").read_text(encoding="utf8")
    payload = json.dumps({"stages": [{k: s[k] for k in ["key", "uid", "display_code", "level", "track", "title", "cluster_id", "cluster_title", "order", "objective", "knowledge_focus", "events", "situations", "coverage_note", "scope_note", "cross_stage_refs", "source_basis"]} for s in course],
                          "stats": stats, "migration": migration, "branch_labels": BRANCH_VI}, ensure_ascii=False).replace("<", "\\u003c")
    write_text(OUT / "ROADMAP.html", template.replace("__DATA__", payload))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=["status", "validate", "render", "publish"])
    p.add_argument("--partial", action="store_true")
    args = p.parse_args()
    manifest, stages, state = collect()
    if args.command == "status":
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return
    audit = validate(manifest, stages, state, partial=args.partial)
    if args.command == "validate":
        print(json.dumps({"valid": True, "complete_stages": len(stages), "pending": len(state["pending_keys"]),
                          "warnings": len(audit["warnings"]), "duplicate_title_groups": len(audit["exact_titles_repeated_across_stages"]),
                          "possible_nonoral_tasks": len(audit["possible_nonoral_tasks"])}, ensure_ascii=False))
        return
    if args.partial or state["pending_keys"]:
        raise ValueError("Do not render/publish partial data as a complete V5")
    if args.command == "publish":
        review = read(OUT / "EDITORIAL_REVIEW.json")
        if review.get("status") != "reviewed_for_roadmap" or review.get("manifest_sha256") != digest(OUT / "BUILD_MANIFEST.json"):
            raise ValueError("Current manifest needs a documented editorial review before publication")
        if review.get("reviewed_stage_hashes") != {s["key"]: s["author_sha256"] for s in stages}:
            raise ValueError("Situation files changed after editorial review; inspect changed stages")
        for relative, pinned in review.get("source_ledger_hashes", {}).items():
            if digest(ROOT / relative) != pinned:
                raise ValueError("Research ledger changed after review: " + relative)
    course, stats = render(manifest, stages, audit, published=args.command == "publish")
    if args.command == "publish":
        atomic(ROOT / "kaiwa_skill/planning/CURRENT_ROADMAP.json", {"version": "5.0", "registry": "kaiwa_skill/planning/v5/chang_registry.json",
               "roadmap": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5.jsonl", "policy": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5_META.json"})
        state.update(status="roadmap_published", stats=stats, next_action="Author/upgrade lessons by UID under kaiwa-stage-content; roadmap scenarios are not dialogue lessons.")
        atomic(OUT / "BUILD_STATE.json", state)
    print(json.dumps({"command": args.command, "stats": stats, "warnings": len(audit["warnings"])}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
