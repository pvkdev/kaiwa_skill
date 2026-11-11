#!/usr/bin/env python3
"""Build and check page-scoped PDF-to-knowledge work without a raw corpus."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import uuid

OLD = Path(__file__).resolve().parents[2] / "kaiwa-fork-knowledge" / "scripts"
sys.path.insert(0, str(OLD))
from build_fork import assemble  # noqa: E402
from validate_fork import (Report, SHA256, UNIT_ID, check_build,  # noqa: E402
                           validate_chapter)

BLOCK = re.compile(r"p(\d{4})-b\d{3}")
STATUSES = ("draft", "needs_review", "author_checked")
CHECKS = ("visual_review", "text_complete", "reading_order", "japanese_accuracy")


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def inside(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError(f"Expected relative path: {relative!r}")
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes root: {relative}")
    return target


def pages_arg(value: str) -> list[int]:
    pages: set[int] = set()
    for part in value.split(","):
        endpoints = part.strip().split("-")
        if len(endpoints) not in (1, 2) or not all(x.isdigit() for x in endpoints):
            raise ValueError(f"Invalid page range: {part}")
        first, last = int(endpoints[0]), int(endpoints[-1])
        if first < 1 or last < first:
            raise ValueError(f"Invalid page range: {part}")
        pages.update(range(first, last + 1))
    return sorted(pages)


def pdf_page_count(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        raise ValueError(f"pdfinfo failed: {result.stderr.strip()}")
    match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result.stdout)
    if not match:
        raise ValueError("pdfinfo did not report Pages")
    return int(match[1])


def meta_and_pdf(repo: Path, book: Path):
    meta = read(book / "_meta/book.json")
    if meta.get("source", {}).get("mode") != "pdf_direct":
        raise ValueError("Book source.mode must be pdf_direct")
    source = meta["source_pdf"]
    pdf = inside(repo, source["path"])
    if not pdf.is_file() or sha(pdf) != source["sha256"]:
        raise ValueError("Source PDF missing or SHA-256 changed")
    return meta, pdf


def init(repo: Path, book: Path, source_path: str, title: str, pages: list[int],
         chapters: list[str], status: str) -> dict:
    if not book.resolve().is_relative_to((repo / "kaiwa_skill/knowledge").resolve()):
        raise ValueError("Book must be inside kaiwa_skill/knowledge")
    pdf = inside(repo, source_path)
    if not pdf.is_file() or pdf.suffix.lower() != ".pdf":
        raise ValueError("Source must be an existing PDF")
    count = pdf_page_count(pdf)
    if not title.strip() or not pages or pages[-1] > count:
        raise ValueError("Missing title or pages outside PDF")
    if status == "full" and pages != list(range(1, count + 1)):
        raise ValueError("Full scope must cover every physical PDF page")
    if not chapters or len(set(chapters)) != len(chapters) or any(
            not c.startswith("chapters/") or not c.endswith(".md") or
            inside(book, c).suffix.lower() != ".md" for c in chapters):
        raise ValueError("Expected unique chapter paths under chapters/")
    meta_dir = book / "_meta"
    if (meta_dir / "book.json").exists() or (meta_dir / "direct-state.json").exists():
        raise ValueError("Direct book already initialized; use resume")
    meta_dir.mkdir(parents=True, exist_ok=True)
    (book / "chapters").mkdir(exist_ok=True)
    source = {"path": source_path, "sha256": sha(pdf)}
    meta = {"schema_version": 1, "title": title, "status": status,
            "paths_relative_to": "repository_root", "source": {"mode": "pdf_direct"},
            "source_pdf": source, "pdf_page_count": count,
            "scope": {"pdf_pages": pages, "chapters": chapters}}
    state = {"schema_version": 1, "created_at": now(), "source_pdf": source,
             "pdf_page_count": count, "scope": meta["scope"],
             "pages": {str(p): {"status": "pending"} for p in pages},
             "chapters": {c: {"status": "pending"} for c in chapters}}
    audio = {"schema_version": 1, "book_title": title, "source_pdf": source,
             "book_identity": {"title": title, "edition": "unknown", "contributors": [],
                               "publisher": "unknown", "isbn": "unknown", "evidence_pages": []},
             "checked_pdf_pages": [], "supplemental_evidence_pages": [],
             "inventory_status": "unknown",
             "discs": [], "tracks": [], "locations": [],
             "actual_files_status": "not_checked", "notes": "Chưa kiểm kê audio/CD từ PDF."}
    write(meta_dir / "book.json", meta)
    write(meta_dir / "direct-state.json", state)
    write(meta_dir / "audio.json", audio)
    (meta_dir / "audio.md").write_text(
        f"# Audio/CD — {title}\n\nTrạng thái: chưa kiểm kê. Xem `audio.json` để cập nhật nguồn trang và block.\n",
        encoding="utf-8")
    return {"status": "initialized", "pdf_page_count": count,
            "scope_pages": len(pages), "chapters": chapters}


def extend_scope(repo: Path, book: Path, pages: list[int], chapters: list[str],
                 status: str, note: str) -> dict:
    """Audited additive scope change; existing content/checkpoints stay untouched."""
    meta, pdf = meta_and_pdf(repo, book)
    progress = resume(repo, book)
    if progress["blocked"] or progress["pages"]["stale"] or progress["chapters"]["stale"]:
        raise ValueError("Resolve stale source/content before extending scope")
    old_scope = meta["scope"]
    if (not note.strip() or not pages or pages != sorted(set(pages)) or
            not set(old_scope["pdf_pages"]).issubset(pages) or
            pages[-1] > pdf_page_count(pdf)):
        raise ValueError("Scope extension needs a note and an additive valid page scope")
    if status == "full" and pages != list(range(1, meta["pdf_page_count"] + 1)):
        raise ValueError("Full scope must cover every physical PDF page")
    if (not chapters or len(chapters) != len(set(chapters)) or
            any(not c.startswith("chapters/") or not c.endswith(".md") or
                inside(book, c).suffix.lower() != ".md" for c in chapters) or
            [c for c in chapters if c in old_scope["chapters"]] != old_scope["chapters"]):
        raise ValueError("Preserve existing chapters and their relative order")
    new_scope = {"pdf_pages": pages, "chapters": chapters}
    if new_scope == old_scope:
        raise ValueError("Scope extension adds no pages or chapters")
    state_path = book / "_meta/direct-state.json"
    audio_path = book / "_meta/audio.json"
    state, audio = read(state_path), read(audio_path)
    stamp = now()
    history_path = book / "_meta/scope-history" / f"{uuid.uuid4().hex}.json"
    write(history_path, {"changed_at": stamp, "note": note, "book_before": meta,
                         "state_before": state, "audio_before": audio,
                         "scope_after": new_scope,
                         "new_scope_is_not_completion": True})
    # No existing checkpoint or source identity is re-certified by extension.
    state["scope"] = new_scope
    for page in pages:
        state["pages"].setdefault(str(page), {"status": "pending"})
    for chapter in chapters:
        state["chapters"].setdefault(chapter, {"status": "pending"})
    state["last_scope_extension"] = {"changed_at": stamp, "note": note,
                                    "history": history_path.relative_to(book).as_posix()}
    meta["scope"], meta["status"] = new_scope, status
    audio["supplemental_evidence_pages"] = [
        p for p in audio.get("supplemental_evidence_pages", []) if p not in pages]
    # Readers must build again; old pilot output/review remain historical evidence.
    meta.pop("build", None)
    write(book / "_meta/book.json", meta)
    write(audio_path, audio)
    write(state_path, state)
    return {"status": "scope_extended_not_completed", "scope": new_scope,
            "history": history_path.relative_to(book).as_posix(),
            "next_action": "resume; process pending pages/chapters; rebuild and validate"}


def units(book: Path) -> list[dict]:
    path = book / "_meta/units.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines()
            if line.strip()]


def page_path(book: Path, page: int) -> Path:
    return book / "_meta/pdf-pages" / f"p{page:04d}.json"


def page_refs(rows: list[dict], page: int) -> dict[str, set[str]]:
    refs: dict[str, set[str]] = {}
    for unit in rows:
        sources = unit.get("source")
        for source in sources if isinstance(sources, list) else []:
            if not isinstance(source, dict):
                continue
            if source.get("pdf_page") == page:
                blocks = source.get("pdf_blocks")
                for block in blocks if isinstance(blocks, list) else []:
                    if isinstance(block, str) and isinstance(unit.get("unit_id"), str):
                        refs.setdefault(block, set()).add(unit["unit_id"])
    return refs


def issue_description(issue: object) -> str:
    return issue.get("description", "").strip() if isinstance(issue, dict) and isinstance(
        issue.get("description"), str) else ""


def unit_issue_errors(unit: dict) -> list[str]:
    """Source issues must identify a page and block already mapped to the unit."""
    if unit.get("review_status") != "needs_review":
        return []
    uid = unit.get("unit_id", "<unknown>")
    issues = unit.get("issues")
    if not isinstance(issues, list) or not issues:
        return [f"{uid}: needs_review requires concrete source issues"]
    sources = unit.get("source")
    mapped = set()
    for src in sources if isinstance(sources, list) else []:
        if isinstance(src, dict) and isinstance(src.get("pdf_blocks"), list):
            mapped.update((src.get("pdf_page"), block) for block in src["pdf_blocks"])
    errors = []
    for issue in issues:
        if not issue_description(issue) or (issue.get("pdf_page"), issue.get("pdf_block")) not in mapped:
            errors.append(f"{uid}: issue needs description and mapped pdf_page/pdf_block")
    return errors


def source_issue_errors(book: Path, rows: list[dict]) -> list[str]:
    errors = [error for unit in rows for error in unit_issue_errors(unit)]
    by_id = {unit.get("unit_id"): unit for unit in rows}
    pages = {source.get("pdf_page") for unit in rows
             for source in (unit.get("source") if isinstance(unit.get("source"), list) else [])
             if isinstance(source, dict) and type(source.get("pdf_page")) is int}
    for page in pages:
        try:
            evidence = read(page_path(book, page))
        except (OSError, ValueError):
            continue
        if not isinstance(evidence, dict):
            continue
        if evidence.get("review_status") != "needs_review":
            continue
        raw_blocks = evidence.get("blocks")
        blocks = {block.get("id"): block for block in raw_blocks if isinstance(block, dict)} if isinstance(raw_blocks, list) else {}
        raw_issues = evidence.get("issues")
        for issue in raw_issues if isinstance(raw_issues, list) else []:
            if not isinstance(issue, dict):
                continue
            bid = issue.get("pdf_block")
            block = blocks.get(bid, {})
            if block.get("disposition") != "included":
                continue
            raw_ids = block.get("unit_ids")
            for uid in raw_ids if isinstance(raw_ids, list) else []:
                unit = by_id.get(uid, {})
                unit_issues = unit.get("issues")
                if (unit.get("review_status") != "needs_review" or not any(
                        isinstance(x, dict) and x.get("pdf_page") == page and
                        x.get("pdf_block") == bid and issue_description(x)
                        for x in (unit_issues if isinstance(unit_issues, list) else []))):
                    errors.append(f"{uid}: source issue {bid} requires matching needs_review unit")
    for unit in rows:
        if unit.get("review_status") != "needs_review":
            continue
        unit_issues = unit.get("issues")
        for issue in unit_issues if isinstance(unit_issues, list) else []:
            if not isinstance(issue, dict) or not issue_description(issue):
                continue
            page, block = issue.get("pdf_page"), issue.get("pdf_block")
            if type(page) is not int:
                continue
            try:
                evidence = read(page_path(book, page))
                page_issues = evidence.get("issues", [])
                if (evidence.get("review_status") != "needs_review" or
                    not isinstance(page_issues, list) or not any(
                        isinstance(x, dict) and x.get("pdf_block") == block and issue_description(x)
                        for x in page_issues)):
                    errors.append(f"{unit['unit_id']}: source issue {block} lacks matching needs_review page evidence")
            except (OSError, ValueError, TypeError):
                errors.append(f"{unit['unit_id']}: source issue page evidence unavailable")
    return errors


def source_issues(book: Path, meta: dict, rows: list[dict]) -> list[str]:
    issues = []
    for page in meta["scope"]["pdf_pages"]:
        evidence = read(page_path(book, page))
        if evidence.get("review_status") == "needs_review":
            for issue in evidence.get("issues", []):
                issues.append(f"PDF p{page}, {issue['pdf_block']}: {issue['description'].strip()}")
    for unit in rows:
        if unit.get("review_status") == "needs_review":
            for issue in unit.get("issues", []):
                issues.append(f"Unit {unit['unit_id']}, PDF p{issue['pdf_page']}, {issue['pdf_block']}: {issue['description'].strip()}")
    return issues


def page_errors(book: Path, meta: dict, page: int, rows: list[dict],
                *, require_checked: bool, allow_source_issues: bool = False) -> list[str]:
    path = page_path(book, page)
    if not path.is_file():
        return [f"p{page:04d}: missing page evidence"]
    try:
        item = read(path)
    except (ValueError, OSError) as error:
        return [f"p{page:04d}: invalid page evidence: {error}"]
    if not isinstance(item, dict):
        return [f"p{page:04d}: page evidence must be an object"]
    errors = []
    loc = f"p{page:04d}"
    if item.get("schema_version") != 1 or item.get("pdf_page") != page:
        errors.append(f"{loc}: schema/page mismatch")
    if item.get("source_pdf_sha256") != meta["source_pdf"]["sha256"]:
        errors.append(f"{loc}: source PDF hash mismatch")
    if not isinstance(item.get("render_sha256"), str) or not SHA256.fullmatch(item["render_sha256"]):
        errors.append(f"{loc}: missing render SHA-256")
    if item.get("review_status") not in STATUSES:
        errors.append(f"{loc}: review_status must be draft, needs_review or author_checked")
    if require_checked and item.get("review_status") not in (("author_checked", "needs_review") if allow_source_issues else ("author_checked",)):
        errors.append(f"{loc}: page has not been author checked")
    if item.get("review_status") in ("author_checked", "needs_review"):
        if not isinstance(item.get("review_note"), str) or not item["review_note"].strip():
            errors.append(f"{loc}: reviewed page requires review_note about opened image")
        checks = item.get("checks")
        if not isinstance(checks, dict):
            errors.append(f"{loc}: reviewed page requires explicit checks")
        elif item.get("review_status") == "author_checked" and not all(checks.get(key) is True for key in CHECKS):
            errors.append(f"{loc}: author_checked requires explicit visual/content checks")
        elif item.get("review_status") == "needs_review" and (
                checks.get("visual_review") is not True or checks.get("reading_order") is not True or
                any(type(checks.get(key)) is not bool for key in CHECKS)):
            errors.append(f"{loc}: needs_review requires visual/reading checks true and all checks boolean")
    blocks = item.get("blocks")
    if not isinstance(blocks, list):
        return errors + [f"{loc}: blocks must be a list"]
    if not blocks and item.get("page_disposition") != "blank":
        errors.append(f"{loc}: empty blocks require page_disposition=blank")
    if not blocks and not str(item.get("review_note", "")).strip():
        errors.append(f"{loc}: blank page requires explanatory note")
    refs = page_refs(rows, page)
    seen = set()
    for block in blocks:
        if not isinstance(block, dict):
            errors.append(f"{loc}: block must be object")
            continue
        bid = block.get("id")
        if not isinstance(bid, str) or not BLOCK.fullmatch(bid) or int(bid[1:5]) != page:
            errors.append(f"{loc}: invalid block ID {bid!r}")
            continue
        if bid in seen:
            errors.append(f"{loc}: duplicate block {bid}")
        seen.add(bid)
        if not str(block.get("label", "")).strip():
            errors.append(f"{loc}/{bid}: missing source block label")
        disposition = block.get("disposition")
        if disposition == "included":
            ids = block.get("unit_ids")
            if not isinstance(ids, list) or not ids or any(not isinstance(x, str) for x in ids) or set(ids) != refs.get(bid, set()):
                errors.append(f"{loc}/{bid}: unit_ids differ from units.jsonl source references")
        elif disposition == "excluded":
            if refs.get(bid):
                errors.append(f"{loc}/{bid}: excluded block is referenced by a unit")
            if not str(block.get("reason", "")).strip():
                errors.append(f"{loc}/{bid}: excluded block requires reason")
        elif disposition == "audio_evidence":
            if refs.get(bid):
                errors.append(f"{loc}/{bid}: audio evidence block is referenced by a learning unit")
        else:
            errors.append(f"{loc}/{bid}: disposition must be included, excluded or audio_evidence")
    for bid in refs.keys() - seen:
        errors.append(f"{loc}: unit references missing source block {bid}")
    if item.get("review_status") == "needs_review":
        issues = item.get("issues")
        if not isinstance(issues, list) or not issues:
            errors.append(f"{loc}: needs_review requires concrete source issues")
        else:
            for issue in issues:
                if (not issue_description(issue) or issue.get("pdf_block") not in seen):
                    errors.append(f"{loc}: issue needs description and existing pdf_block")
    return errors


def chapter_deps(book: Path, chapter: str, rows: list[dict], meta: dict) -> dict:
    chapter_file = inside(book, chapter)
    relevant = [u for u in rows if u.get("chapter") == chapter]
    if not chapter_file.is_file() or not relevant:
        raise ValueError(f"Chapter or units missing: {chapter}")
    pages = sorted({s["pdf_page"] for u in relevant for s in u["source"]})
    encoded = json.dumps(relevant, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return {"chapter_sha256": sha(chapter_file),
            "units_sha256": hashlib.sha256(encoded.encode("utf-8")).hexdigest(),
            "page_evidence_sha256": {str(p): sha(page_path(book, p)) for p in pages},
            "source_pdf_sha256": meta["source_pdf"]["sha256"]}


def checkpoint(repo: Path, book: Path, page: int | None, chapter: str | None,
               status: str, note: str) -> dict:
    meta, _ = meta_and_pdf(repo, book)
    state_path = book / "_meta/direct-state.json"
    state = read(state_path)
    if state["scope"] != meta["scope"] or state["source_pdf"] != meta["source_pdf"]:
        raise ValueError("Scope/source changed since init; rebase required")
    if status in ("author_checked", "needs_review") and not note.strip():
        raise ValueError(f"{status} requires a note describing actual visual comparison")
    rows = units(book)
    if page is not None:
        if page not in state["scope"]["pdf_pages"]:
            raise ValueError("Page outside declared scope")
        errors = page_errors(book, meta, page, rows,
                             require_checked=status in ("author_checked", "needs_review"),
                             allow_source_issues=status == "needs_review")
        evidence_status = read(page_path(book, page)).get("review_status") if page_path(book, page).is_file() else None
        if status != "draft" and evidence_status != status:
            errors.append(f"Page evidence status {evidence_status!r} differs from checkpoint {status!r}")
        if errors:
            raise ValueError("; ".join(errors))
        state["pages"][str(page)] = {"status": status,
                                    "evidence_sha256": sha(page_path(book, page)),
                                    "note": note, "updated_at": now()}
        target = f"p{page:04d}"
    else:
        if chapter not in state["scope"]["chapters"]:
            raise ValueError("Chapter outside declared scope")
        deps = chapter_deps(book, chapter, rows, meta)
        relevant = [u for u in rows if u.get("chapter") == chapter]
        issue_errors = [error for unit in relevant for error in unit_issue_errors(unit)]
        if issue_errors:
            raise ValueError("; ".join(issue_errors))
        if status in ("author_checked", "needs_review"):
            page_statuses = []
            for p in map(int, deps["page_evidence_sha256"]):
                entry = state["pages"][str(p)]
                page_statuses.append(entry["status"])
                if (entry["status"] not in ("author_checked", "needs_review") or
                        entry.get("evidence_sha256") != sha(page_path(book, p)) or
                        page_errors(book, meta, p, rows, require_checked=True,
                                    allow_source_issues=status == "needs_review")):
                    raise ValueError(f"Page {p} must have a current reviewed checkpoint compatible with {status}")
            unit_statuses = [u.get("review_status") for u in relevant]
            if status == "author_checked" and any(x != "author_checked" for x in unit_statuses + page_statuses):
                raise ValueError("author_checked chapter cannot include unresolved unit/page")
            if status == "needs_review" and (
                    any(x not in ("author_checked", "needs_review") for x in unit_statuses) or
                    "needs_review" not in unit_statuses + page_statuses):
                raise ValueError("needs_review chapter requires a mapped source issue and no draft units/pages")
        state["chapters"][chapter] = {"status": status, **deps,
                                      "note": note, "updated_at": now()}
        target = chapter
    write(state_path, state)
    return {"checkpoint": target, "status": status}


def resume(repo: Path, book: Path) -> dict:
    state = read(book / "_meta/direct-state.json")
    meta = read(book / "_meta/book.json")
    result = {"blocked": False, "needs_rebase": [], "pages": {k: [] for k in
              ("completed", "needs_review", "draft", "pending", "stale")},
              "chapters": {k: [] for k in ("completed", "needs_review", "draft", "pending", "stale")}}
    if state["scope"] != meta.get("scope") or state["source_pdf"] != meta.get("source_pdf"):
        result["blocked"] = True
        result["needs_rebase"].append("declared scope or PDF identity changed")
    try:
        meta_and_pdf(repo, book)
    except (OSError, ValueError, KeyError) as error:
        result["blocked"] = True
        result["needs_rebase"].append(str(error))
    try:
        rows = units(book)
    except (OSError, ValueError, KeyError) as error:
        rows = []
        result["needs_rebase"].append(f"units unavailable: {error}")
    for page in state["scope"]["pdf_pages"]:
        entry = state["pages"].get(str(page), {"status": "pending"})
        if entry["status"] == "pending":
            group = "pending"
        elif (not page_path(book, page).is_file() or
              sha(page_path(book, page)) != entry.get("evidence_sha256") or
              page_errors(book, meta, page, rows,
                          require_checked=entry["status"] in ("author_checked", "needs_review"),
                          allow_source_issues=entry["status"] == "needs_review") or
              result["blocked"]):
            group = "stale"
        else:
            group = {"author_checked": "completed", "needs_review": "needs_review"}.get(entry["status"], "draft")
        result["pages"][group].append(page)
    for chapter in state["scope"]["chapters"]:
        entry = state["chapters"].get(chapter, {"status": "pending"})
        if entry["status"] == "pending":
            group = "pending"
        else:
            try:
                fresh = chapter_deps(book, chapter, rows, meta)
                current = all(entry.get(k) == value for k, value in fresh.items())
            except (OSError, ValueError, KeyError, TypeError):
                current = False
            mapped_pages = set(map(int, entry.get("page_evidence_sha256", {})))
            related_stale = bool(mapped_pages.intersection(result["pages"]["stale"]))
            related_unreviewed = (entry["status"] in ("author_checked", "needs_review") and
                                  bool(mapped_pages.intersection(result["pages"]["pending"] + result["pages"]["draft"])))
            relevant = [u for u in rows if u.get("chapter") == chapter]
            issue_invalid = any(unit_issue_errors(u) for u in relevant)
            unit_statuses = [u.get("review_status") for u in relevant]
            if entry["status"] == "author_checked":
                incompatible = ("needs_review" in unit_statuses or bool(mapped_pages.intersection(result["pages"]["needs_review"])))
            elif entry["status"] == "needs_review":
                incompatible = (not relevant or any(s not in ("author_checked", "needs_review") for s in unit_statuses) or
                                not ("needs_review" in unit_statuses or bool(mapped_pages.intersection(result["pages"]["needs_review"]))))
            else:
                incompatible = False
            group = {"author_checked": "completed", "needs_review": "needs_review"}.get(entry["status"], "draft") if (
                current and not result["blocked"] and not related_stale and not related_unreviewed and
                not issue_invalid and not incompatible
            ) else "stale"
        result["chapters"][group].append(chapter)
    result["next_page"] = next((p for p in state["scope"]["pdf_pages"] if p in
                                   result["pages"]["pending"] + result["pages"]["draft"] +
                                   result["pages"]["stale"] + result["pages"]["needs_review"]), None)
    result["next_chapter"] = next((c for c in state["scope"]["chapters"] if c in
                                      result["chapters"]["pending"] + result["chapters"]["draft"] +
                                      result["chapters"]["stale"] + result["chapters"]["needs_review"]), None)
    return result


def audio_errors(audio: dict, meta: dict, rows: list[dict], book: Path) -> list[str]:
    errors = []
    if audio.get("schema_version") != 1 or audio.get("book_title") != meta["title"] or audio.get("source_pdf") != meta["source_pdf"]:
        errors.append("audio.json identity/source mismatch")
    status = audio.get("inventory_status")
    if status not in ("unknown", "not_seen", "documented"):
        errors.append("audio.json inventory_status invalid")
    identity = audio.get("book_identity")
    if not isinstance(identity, dict) or identity.get("title") != meta["title"] or not isinstance(identity.get("evidence_pages"), list):
        errors.append("audio.json book_identity/title/evidence_pages invalid")
    elif not identity["evidence_pages"]:
        errors.append("audio.json book identity requires at least one checked PDF evidence page")
    supplemental = audio.get("supplemental_evidence_pages")
    if not isinstance(supplemental, list) or len(set(supplemental)) != len(supplemental) or any(
            type(p) is not int or p < 1 or p > meta["pdf_page_count"] or p in meta["scope"]["pdf_pages"]
            for p in supplemental):
        errors.append("audio.json supplemental_evidence_pages invalid")
        supplemental = []
    checked = audio.get("checked_pdf_pages")
    if not isinstance(checked, list) or len(set(checked)) != len(checked) or any(
            type(p) is not int or p not in meta["scope"]["pdf_pages"] + supplemental for p in checked):
        errors.append("audio.json checked_pdf_pages invalid")
        checked = []
    for page in supplemental:
        for error in page_errors(book, meta, page, [], require_checked=True):
            errors.append(f"audio supplemental {error}")
    if isinstance(identity, dict):
        for page in identity.get("evidence_pages", []):
            if page not in checked:
                errors.append("audio.json identity evidence page not checked")
    if audio.get("actual_files_status") not in ("not_checked", "not_provided", "found"):
        errors.append("audio.json actual_files_status invalid")
    if not isinstance(audio.get("notes"), str):
        errors.append("audio.json notes required")
    refs = page_refs
    for collection in ("discs", "tracks", "locations"):
        items = audio.get(collection)
        if not isinstance(items, list):
            errors.append(f"audio.json {collection} must be list")
            continue
        for index, item in enumerate(items):
            loc = f"audio.json {collection}[{index}]"
            if not isinstance(item, dict) or not str(item.get("label", "")).strip():
                errors.append(f"{loc}: label required")
                continue
            page, block = item.get("pdf_page"), item.get("pdf_block")
            if type(page) is not int or page not in (checked or []):
                errors.append(f"{loc}: referenced page must be checked")
                continue
            try:
                evidence = read(page_path(book, page))
                if block not in {b.get("id") for b in evidence["blocks"]}:
                    errors.append(f"{loc}: source block absent from page evidence")
            except (OSError, ValueError, KeyError, TypeError):
                errors.append(f"{loc}: page evidence unavailable")
    if status == "not_seen" and (set(checked) != set(range(1, meta["pdf_page_count"] + 1)) or
                                  any(audio.get(x) for x in ("discs", "tracks", "locations"))):
        errors.append("audio.json not_seen requires the entire PDF checked and no references")
    if status == "documented" and not any(audio.get(x) for x in ("discs", "tracks", "locations")):
        errors.append("audio.json documented requires at least one source reference")
    if status == "unknown" and any(audio.get(x) for x in ("discs", "tracks", "locations")):
        errors.append("audio.json known references require inventory_status=documented")
    if audio.get("actual_files_status") == "found":
        files = audio.get("actual_files")
        if not isinstance(files, list) or not files or any(not isinstance(x, dict) or
            not isinstance(x.get("path"), str) or not isinstance(x.get("sha256"), str) or
            not SHA256.fullmatch(x["sha256"]) for x in files):
            errors.append("audio.json found requires actual_files with path and SHA-256")
        else:
            repo = book.parents[2]
            for item in files:
                try:
                    path = inside(repo, item["path"])
                    if not path.is_file() or sha(path) != item["sha256"]:
                        errors.append(f"audio.json actual file missing/changed: {item['path']}")
                except (ValueError, OSError):
                    errors.append(f"audio.json actual file path invalid: {item['path']}")
    audio_md = book / "_meta/audio.md"
    if not audio_md.is_file() or not audio_md.read_text(encoding="utf-8-sig").strip():
        errors.append("audio.md missing or empty")
    return errors


def build(repo: Path, book: Path) -> dict:
    meta, pdf = meta_and_pdf(repo, book)
    rows = units(book)
    errors = [error for p in meta["scope"]["pdf_pages"] for error in
              page_errors(book, meta, p, rows, require_checked=False)]
    errors += source_issue_errors(book, rows)
    audio = read(book / "_meta/audio.json")
    errors += audio_errors(audio, meta, rows, book)
    if errors:
        raise ValueError("; ".join(errors))
    if pdf_page_count(pdf) != meta["pdf_page_count"]:
        raise ValueError("PDF physical page count changed")
    coverage = {"schema_version": 1, "source_pdf_sha256": meta["source_pdf"]["sha256"],
                "scope_pdf_pages": meta["scope"]["pdf_pages"],
                "pages": [{"pdf_page": p, "evidence_sha256": sha(page_path(book, p)),
                           "review_status": read(page_path(book, p))["review_status"],
                           "blocks": read(page_path(book, p))["blocks"]}
                          for p in meta["scope"]["pdf_pages"]]}
    write(book / "_meta/page-coverage.json", coverage)
    result = assemble(book)
    issues = source_issues(book, meta, rows)
    issue_path = book / "_meta/source-issues.md"
    if issues:
        issue_path.write_text("# Vấn đề nguồn chưa giải quyết\n\n" +
                              "\n".join(f"- {issue.replace(chr(10), ' ')}" for issue in issues) + "\n",
                              encoding="utf-8")
        book_path = book / "book.md"
        text = book_path.read_text(encoding="utf-8")
        heading, rest = text.split("\n", 1)
        notice = ("\n> **Lưu ý nguồn:** Một số chữ/chi tiết trên PDF chưa xác nhận được. "
                  "Xem [vấn đề nguồn chưa giải quyết](_meta/source-issues.md). "
                  "Bản này chưa hoàn tất xác nhận nội dung.\n")
        book_path.write_text(heading + "\n" + notice + rest, encoding="utf-8")
    elif issue_path.exists():
        issue_path.unlink()
    meta = read(book / "_meta/book.json")
    meta["build"]["book_sha256"] = sha(book / "book.md")
    meta["build"].update({"source_pdf_sha256": sha(pdf),
                          "page_coverage_sha256": sha(book / "_meta/page-coverage.json"),
                          "audio_sha256": sha(book / "_meta/audio.json"),
                          "audio_md_sha256": sha(book / "_meta/audio.md"),
                          "review_state": "source_issues_unresolved" if issues else "no_recorded_source_issues",
                          "source_issues_sha256": sha(issue_path) if issues else None})
    write(book / "_meta/book.json", meta)
    if issues:
        result["completion_status"] = "source_issues_unresolved"
        result["warnings"] = issues
    return result


def validate(repo: Path, book: Path, allow_draft: bool = False,
             allow_source_issues: bool = False) -> int:
    report = Report()
    try:
        meta, pdf = meta_and_pdf(repo, book)
        state = read(book / "_meta/direct-state.json")
    except (OSError, ValueError, KeyError, TypeError) as error:
        report.error("book", str(error))
        return report.show()
    if meta.get("schema_version") != 1 or meta.get("paths_relative_to") != "repository_root":
        report.error("book.json", "invalid schema/path convention")
    if meta.get("status") not in ("pilot_partial", "partial", "full"):
        report.error("book.json", "invalid scope status")
    pages, chapters = meta["scope"]["pdf_pages"], meta["scope"]["chapters"]
    if not pages or pages != sorted(set(pages)) or any(type(p) is not int or p < 1 for p in pages):
        report.error("book.json", "invalid ordered PDF page scope")
    if meta["pdf_page_count"] != pdf_page_count(pdf) or pages[-1] > meta["pdf_page_count"]:
        report.error("book.json", "PDF page count/scope differs from physical source")
    if meta["status"] == "full" and pages != list(range(1, meta["pdf_page_count"] + 1)):
        report.error("book.json", "full scope omits physical PDF pages")
    if not chapters or len(set(chapters)) != len(chapters):
        report.error("book.json", "invalid chapter scope")
    if state.get("scope") != meta["scope"] or state.get("source_pdf") != meta["source_pdf"]:
        report.error("direct-state.json", "scope/source differs from book.json")
    try:
        rows = units(book)
    except (OSError, ValueError, KeyError) as error:
        report.error("units.jsonl", str(error))
        return report.show()
    ids = set()
    chapter_anchors = {}
    for chapter in chapters:
        try:
            path = inside(book, chapter)
            chapter_anchors[chapter] = validate_chapter(path, report)
        except (OSError, ValueError) as error:
            report.error(chapter, str(error))
    for unit in rows:
        uid, chapter = unit.get("unit_id"), unit.get("chapter")
        if not isinstance(uid, str) or not UNIT_ID.fullmatch(uid) or uid in ids:
            report.error("units.jsonl", f"invalid/duplicate unit ID: {uid!r}")
            continue
        ids.add(uid)
        if chapter not in chapter_anchors or uid not in chapter_anchors[chapter]:
            report.error("units.jsonl", f"{uid}: chapter anchor absent")
        if not str(unit.get("heading", "")).strip() or unit.get("review_status") not in STATUSES or not isinstance(unit.get("issues"), list):
            report.error("units.jsonl", f"{uid}: heading/review_status/issues invalid")
        sources = unit.get("source")
        if not isinstance(sources, list) or not sources:
            report.error("units.jsonl", f"{uid}: source required")
            continue
        for source in sources:
            if not isinstance(source, dict):
                report.error("units.jsonl", f"{uid}: source entry must be an object")
                continue
            page, blocks = source.get("pdf_page"), source.get("pdf_blocks")
            if type(page) is not int or page not in pages or not isinstance(blocks, list) or not blocks or any(
                    not isinstance(b, str) or not BLOCK.fullmatch(b) or int(b[1:5]) != page for b in blocks):
                report.error("units.jsonl", f"{uid}: invalid PDF page/block mapping")
    for chapter, anchors in chapter_anchors.items():
        for uid in anchors - ids:
            report.error(chapter, f"anchor lacks provenance: {uid}")
    issue_errors = source_issue_errors(book, rows)
    for error in issue_errors:
        report.error("source issue", error)
    page_error_count = 0
    for page in pages:
        errors = page_errors(book, meta, page, rows, require_checked=not allow_draft,
                             allow_source_issues=allow_source_issues)
        page_error_count += len(errors)
        for error in errors:
            report.error("page evidence", error)
    try:
        audio = read(book / "_meta/audio.json")
        for error in audio_errors(audio, meta, rows, book):
            report.error("audio", error)
    except (OSError, ValueError) as error:
        report.error("audio.json", str(error))
    check_build(book, meta, chapters, report)
    build_meta = meta.get("build", {})
    for name, path in (("source_pdf_sha256", pdf),
                       ("page_coverage_sha256", book / "_meta/page-coverage.json"),
                       ("audio_sha256", book / "_meta/audio.json"),
                       ("audio_md_sha256", book / "_meta/audio.md")):
        if not path.is_file() or build_meta.get(name) != sha(path):
            report.error("build", f"missing/stale {name}")
    if not issue_errors and not page_error_count:
        issues = source_issues(book, meta, rows)
        if issues:
            issue_path = book / "_meta/source-issues.md"
            book_text = (book / "book.md").read_text(encoding="utf-8-sig") if (book / "book.md").is_file() else ""
            if (not issue_path.is_file() or build_meta.get("source_issues_sha256") != sha(issue_path) or
                    build_meta.get("review_state") != "source_issues_unresolved" or
                    "(_meta/source-issues.md)" not in book_text):
                report.error("build", "source issue notice missing/stale")
            for issue in issues:
                if allow_source_issues or allow_draft:
                    report.warn("source issue", issue + " (chưa xác nhận nội dung)")
                else:
                    report.error("source issue", issue + " (chưa giải quyết)")
        else:
            legacy_clean_build = (
                "review_state" not in build_meta and
                "source_issues_sha256" not in build_meta and
                not (book / "_meta/source-issues.md").exists()
            )
            if not legacy_clean_build and (
                build_meta.get("review_state") != "no_recorded_source_issues" or
                build_meta.get("source_issues_sha256") is not None
            ):
                report.error("build", "source issue state stale")
    if (book / "_meta/page-coverage.json").is_file():
        coverage = read(book / "_meta/page-coverage.json")
        if coverage.get("scope_pdf_pages") != pages or coverage.get("source_pdf_sha256") != meta["source_pdf"]["sha256"]:
            report.error("page-coverage.json", "scope/source mismatch")
        actual = coverage.get("pages", [])
        if [x.get("pdf_page") for x in actual] != pages:
            report.error("page-coverage.json", "missing/out-of-order pages")
        else:
            for item in actual:
                p = item["pdf_page"]
                if not page_path(book, p).is_file() or item.get("evidence_sha256") != sha(page_path(book, p)):
                    report.error("page-coverage.json", f"p{p:04d} evidence changed")
    progress = resume(repo, book)
    if progress["blocked"] or progress["pages"]["stale"] or progress["chapters"]["stale"]:
        report.error("direct-state.json", "source/content/evidence checkpoint stale")
    if not allow_draft:
        allowed_pages = progress["pages"]["completed"] + (progress["pages"]["needs_review"] if allow_source_issues else [])
        allowed_chapters = progress["chapters"]["completed"] + (progress["chapters"]["needs_review"] if allow_source_issues else [])
        if len(allowed_pages) != len(pages) or len(allowed_chapters) != len(chapters):
            report.error("direct-state.json", "scope lacks current reviewed checkpoints; pending/draft/stale are not accepted")
    return report.show()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "extend-scope", "checkpoint", "resume", "build", "validate"):
        cmd = sub.add_parser(name)
        cmd.add_argument("book_dir", type=Path)
        cmd.add_argument("--repo-root", type=Path, required=True)
        if name == "init":
            cmd.add_argument("--source-pdf", required=True, help="PDF path relative to repository root")
            cmd.add_argument("--title", required=True)
            cmd.add_argument("--pages", required=True, help="physical pages, e.g. 1-12,15")
            cmd.add_argument("--chapters", required=True, help="comma-separated ordered chapter paths")
            cmd.add_argument("--status", choices=("pilot_partial", "partial", "full"), default="pilot_partial")
        if name == "checkpoint":
            target = cmd.add_mutually_exclusive_group(required=True)
            target.add_argument("--page", type=int)
            target.add_argument("--chapter")
            cmd.add_argument("--status", choices=STATUSES, required=True)
            cmd.add_argument("--note", default="")
        if name == "extend-scope":
            cmd.add_argument("--pages", required=True)
            cmd.add_argument("--chapters", required=True)
            cmd.add_argument("--status", choices=("partial", "full"), required=True)
            cmd.add_argument("--note", required=True)
        if name == "validate":
            mode = cmd.add_mutually_exclusive_group()
            mode.add_argument("--allow-draft", action="store_true")
            mode.add_argument("--allow-source-issues", action="store_true")
    args = parser.parse_args()
    repo, book = args.repo_root.resolve(), args.book_dir.resolve()
    if not book.is_relative_to(repo):
        parser.error("book_dir must be inside repository")
    try:
        if args.command == "init":
            output = init(repo, book, args.source_pdf, args.title, pages_arg(args.pages),
                          [x.strip() for x in args.chapters.split(",")], args.status)
        elif args.command == "extend-scope":
            output = extend_scope(repo, book, pages_arg(args.pages),
                                  [x.strip() for x in args.chapters.split(",")],
                                  args.status, args.note)
        elif args.command == "checkpoint":
            output = checkpoint(repo, book, args.page, args.chapter, args.status, args.note)
        elif args.command == "resume":
            output = resume(repo, book)
        elif args.command == "build":
            output = build(repo, book)
        else:
            return validate(repo, book, args.allow_draft, args.allow_source_issues)
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        parser.exit(1, f"direct_progress: {error}\n")


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    sys.exit(main())
