"""Inspect ingest readiness and keep resumable, page-scoped clean checkpoints."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import uuid


def sha(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def inside(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError(f"Expected relative path: {relative!r}")
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes root: {relative}")
    return target


def relative(root: Path, target: Path) -> str:
    return target.resolve().relative_to(root.resolve()).as_posix()


def atomic_json(path: Path, data: dict) -> None:
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temp.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)
    # fsync of directories is not portable on Windows; replace is atomic there.


def atomic_bytes(path: Path, data: bytes) -> None:
    temp = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    with temp.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


@contextmanager
def exclusive(meta_dir: Path):
    lock = meta_dir / "clean-progress.lock"
    token = uuid.uuid4().hex
    try:
        with lock.open("x", encoding="utf-8") as stream:
            json.dump({"token": token, "pid": os.getpid(), "created_at": now()}, stream)
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError as error:
        raise ValueError(f"Clean lock exists: {lock}; inspect owner before manual recovery") from error
    try:
        yield
    finally:
        if lock.exists() and read_json(lock).get("token") == token:
            lock.unlink()


def scan_one(repo: Path, corpus: Path) -> dict:
    reasons: list[str] = []
    status = "waiting"
    try:
        manifest = read_json(corpus / "manifest.json")
        page_count = manifest["page_count"]
        source = inside(repo / "kaiwa_skill", manifest["source"])
        if not source.is_file() or sha(source) != manifest["source_sha256"]:
            raise ValueError("PDF missing or source hash changed")
        if not (corpus / "build.json").is_file():
            return {"corpus": relative(repo, corpus), "source_pdf": relative(repo, source),
                    "status": "waiting", "reasons": ["Ingest build not yet present"],
                    "acceptance": manifest.get("acceptance", "coordinator_review_required")}
        build = read_json(corpus / "build.json")
        if build.get("source_sha256") != manifest["source_sha256"]:
            reasons.append("Build source hash differs from manifest")
        if (corpus / "claim.json").exists() or (corpus / ".write.lock").exists():
            reasons.append("Ingest claim or write lock exists")
        if not (build.get("complete") is True and build.get("transcription_complete") is True):
            reasons.append("Ingest build is not complete")
        if manifest.get("counts", {}).get("verified") != page_count:
            reasons.append("Manifest verified count differs from page count")
        if any(manifest.get("counts", {}).get(name, 0) != 0 for name in
               ("pending", "rendered", "draft", "needs_review", "invalid")):
            reasons.append("Manifest has non-verified page counts")
        expected = set(range(1, page_count + 1))
        states = manifest.get("pages", {})
        if set(map(int, states)) != expected or any(states.get(str(i)) != "verified" for i in expected):
            reasons.append("Not all manifest pages are verified")
        if set(build.get("verified_pages", [])) != expected:
            reasons.append("Build verified pages incomplete")
        page_hashes = build.get("page_hashes", {})
        if set(map(int, page_hashes)) != expected:
            reasons.append("Build page hashes incomplete")
        for i in expected:
            page = corpus / "pages" / f"p{i:04d}.md"
            evidence_file = corpus / "pages" / f"p{i:04d}.json"
            if not page.is_file() or not evidence_file.is_file():
                reasons.append(f"Page {i}: Markdown/evidence missing")
                continue
            current = sha(page)
            item = read_json(evidence_file)
            evidence = item.get("evidence") or {}
            checks = evidence.get("checks") or {}
            if (item.get("status") != "verified" or item.get("issues") or
                item.get("source_sha256") != manifest["source_sha256"] or
                item.get("markdown_sha256") != current or
                evidence.get("source_sha256") != manifest["source_sha256"] or
                evidence.get("markdown_sha256") != current or
                not evidence.get("render_sha256") or
                evidence.get("render_sha256") != item.get("render_sha256") or
                evidence.get("asset_sha256", {}) != item.get("asset_sha256", {}) or
                not all(checks.get(key) is True for key in
                        ("visual_review", "text_complete", "reading_order", "japanese_accuracy")) or
                page_hashes.get(str(i)) != current):
                reasons.append(f"Page {i}: verification evidence/hash/issue mismatch")
        for name, key in (("book.md", "book_sha256"), ("search.jsonl", "search_sha256")):
            path = corpus / name
            if not path.is_file() or sha(path) != build.get(key):
                reasons.append(f"{name} missing or build hash stale")
        status = "ready_for_fork" if not reasons else "waiting"
        return {"corpus": relative(repo, corpus), "source_pdf": relative(repo, source),
                "status": status, "reasons": reasons,
                "acceptance": manifest.get("acceptance", "coordinator_review_required")}
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        return {"corpus": relative(repo, corpus), "status": "invalid",
                "reasons": [str(error)], "acceptance": "unknown"}


def scan(repo: Path) -> dict:
    corpus_root = repo / "kaiwa_skill" / "corpus"
    books = [scan_one(repo, path.parent) for path in
             sorted(corpus_root.glob("*/manifest.json"))]
    by_source = {f"{row['corpus']}/book.md": row for row in books}
    for meta_path in (repo / "kaiwa_skill" / "knowledge").glob("*/_meta/book.json"):
        row = None
        try:
            meta = read_json(meta_path)
            row = by_source.get(meta["source_markdown"]["path"])
            if row is None or not (meta_path.parent / "clean-state.json").is_file():
                continue
            book = meta_path.parent.parent
            progress = resume(repo, book)
            row["output_folder"] = relative(repo, book)
            row["clean_progress"] = {key: progress[key] for key in
                                     ("completed", "draft", "pending", "stale", "needs_rebase",
                                      "snapshot_errors", "next", "scope_changed", "blocked")}
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            if row is not None:
                row["clean_progress_error"] = str(error)
    return {"books": books}


def book_info(repo: Path, book: Path) -> tuple[dict, list[str], dict[str, str]]:
    meta = read_json(book / "_meta" / "book.json")
    source = {}
    for name in ("source_pdf", "source_markdown"):
        info = meta[name]
        path = inside(repo, info["path"])
        if not path.is_file():
            raise ValueError(f"Missing {name}: {info['path']}")
        if sha(path) != info["sha256"]:
            raise ValueError(f"{name} hash differs from _meta/book.json")
        source["pdf" if name == "source_pdf" else "markdown"] = info
    scope = meta["scope"]
    pages = scope["pdf_pages"]
    chapters = scope["chapters"]
    if (not pages or len(pages) != len(set(pages)) or
        any(not isinstance(n, int) or n < 1 for n in pages) or
        not chapters or len(chapters) != len(set(chapters))):
        raise ValueError("Invalid scope pages or chapters")
    corpus = inside(repo, meta["source_markdown"]["path"]).parent
    files = [inside(repo, source["markdown"]["path"])]
    files.extend(corpus / "pages" / f"p{n:04d}.md" for n in pages)
    files.extend(path for path in (corpus / "manifest.json", corpus / "build.json") if path.is_file())
    raw = {}
    for path in files:
        if not path.is_file() or not path.resolve().is_relative_to(corpus.resolve()):
            raise ValueError(f"Missing raw scope file: {path}")
        raw[relative(repo, path)] = sha(path)
    return meta, chapters, raw


def init(repo: Path, book: Path) -> dict:
    meta_dir = book / "_meta"
    with exclusive(meta_dir):
        state_path = meta_dir / "clean-state.json"
        meta, chapters, before = book_info(repo, book)
        corpus_id = inside(repo, meta["source_markdown"]["path"]).parent.name
        scope_hash = hashlib.sha256(json.dumps(meta["scope"], sort_keys=True).encode()).hexdigest()[:8]
        snapshot_rel = (Path("kaiwa_skill/source_snapshots") / corpus_id /
                        meta["source_markdown"]["sha256"][:16] / scope_hash).as_posix()
        snapshot = inside(repo, snapshot_rel)
        if state_path.exists():
            raise ValueError("Clean ledger already exists; use resume, do not overwrite")
        if snapshot.exists():
            if snapshot_errors(repo, {"root": snapshot_rel, "files": before}):
                raise ValueError("Orphan snapshot differs from current source; inspect manually")
        else:
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            temp = snapshot.with_name(f".{snapshot.name}.{uuid.uuid4().hex}.tmp")
            temp.mkdir()
            try:
                for rel in before:
                    target = inside(temp, rel)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(inside(repo, rel), target)
                _, _, after = book_info(repo, book)
                if before != after or snapshot_errors(repo, {"root": relative(repo, temp), "files": before}):
                    raise ValueError("Source changed during snapshot; no clean state committed")
                os.replace(temp, snapshot)
            finally:
                if temp.exists():
                    shutil.rmtree(temp)
        _, _, after = book_info(repo, book)
        if before != after or snapshot_errors(repo, {"root": snapshot_rel, "files": before}):
            raise ValueError("Source changed before ledger commit; no clean state committed")
        state = {"schema_version": 1, "created_at": now(),
                 "source": {"pdf": meta["source_pdf"], "markdown": meta["source_markdown"]},
                 "scope": {"pdf_pages": meta["scope"]["pdf_pages"], "chapters": chapters},
                 "snapshot": {"root": snapshot_rel, "files": before},
                 "checkpoints": {chapter: {"status": "pending"} for chapter in chapters}}
        atomic_json(state_path, state)
        return {"status": "initialized", "chapters": chapters,
                "snapshot_files": len(before), "state": relative(repo, state_path)}


def snapshot_errors(repo: Path, snapshot: dict) -> list[str]:
    root = inside(repo, snapshot["root"])
    files = snapshot["files"]
    errors = []
    if not root.is_dir():
        return [f"Snapshot root missing: {snapshot['root']}"]
    actual = {path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()}
    if actual != set(files):
        errors.append("Snapshot file set differs from ledger")
    for rel, expected in files.items():
        path = inside(root, rel)
        if not path.is_file() or sha(path) != expected:
            errors.append(f"Snapshot missing or changed: {rel}")
    return errors


def chapter_inputs(repo: Path, book: Path, chapter: str, snapshot: dict) -> dict:
    units_path = book / "_meta" / "units.jsonl"
    units = [json.loads(line) for line in units_path.read_text(encoding="utf-8-sig").splitlines()
             if line.strip()]
    return chapter_inputs_rows(repo, book, chapter, snapshot, units)


def chapter_inputs_rows(repo: Path, book: Path, chapter: str,
                        snapshot: dict, units: list[dict]) -> dict:
    chapter_path = inside(book, chapter)
    if not chapter_path.is_file():
        raise ValueError(f"Missing chapter: {chapter}")
    relevant = [unit for unit in units if unit.get("chapter") == chapter]
    if not relevant:
        raise ValueError(f"No units for chapter: {chapter}")
    pages = {}
    files = snapshot["files"]
    prefix = snapshot["root"].rstrip("/") + "/"
    for unit in relevant:
        for item in unit["source"]:
            rel = item["raw_page"]
            original = rel[len(prefix):] if rel.startswith(prefix) else rel
            if original not in files:
                raise ValueError(f"Unit source page outside snapshot: {rel}")
            pages[original] = files[original]
    encoded = json.dumps(relevant, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {"chapter_sha256": sha(chapter_path),
            "units_sha256": hashlib.sha256(encoded.encode("utf-8")).hexdigest(),
            "source_pages": pages}


def same_scope(declared: dict, recorded: dict) -> bool:
    return (declared.get("pdf_pages") == recorded.get("pdf_pages") and
            declared.get("chapters") == recorded.get("chapters"))


def checkpoint(repo: Path, book: Path, chapter: str, status: str, note: str) -> dict:
    meta_dir = book / "_meta"
    with exclusive(meta_dir):
        state_path = meta_dir / "clean-state.json"
        state = read_json(state_path)
        metadata = read_json(meta_dir / "book.json")
        if not same_scope(metadata["scope"], state["scope"]):
            raise ValueError("Book scope differs from clean ledger; coordinate a new scope plan")
        if chapter not in state["scope"]["chapters"]:
            raise ValueError(f"Chapter not in clean scope: {chapter}")
        if status == "author_checked" and not note.strip():
            raise ValueError("author_checked requires --note describing source comparison")
        errors = snapshot_errors(repo, state["snapshot"])
        if errors:
            raise ValueError("Snapshot changed; checkpoint refused: " + "; ".join(errors))
        declared = metadata["source_markdown"]
        declared_path = inside(repo, declared["path"])
        original = state["source"]["markdown"]
        pinned_path = state["snapshot"]["root"].rstrip("/") + "/" + original["path"]
        if (declared["path"] not in (original["path"], pinned_path) or
            declared["sha256"] != original["sha256"] or
            not declared_path.is_file() or sha(declared_path) != declared["sha256"]):
            raise ValueError("Declared source Markdown differs from clean baseline/snapshot")
        data = chapter_inputs(repo, book, chapter, state["snapshot"])
        if sha(inside(repo, state["source"]["pdf"]["path"])) != state["source"]["pdf"]["sha256"]:
            raise ValueError("Source PDF changed; checkpoint refused")
        state["checkpoints"][chapter] = {"status": status, **data,
                                         "note": note, "updated_at": now()}
        atomic_json(state_path, state)
        return {"chapter": chapter, "status": status, "updated_at": state["checkpoints"][chapter]["updated_at"]}


def resume(repo: Path, book: Path) -> dict:
    state = read_json(book / "_meta" / "clean-state.json")
    metadata = read_json(book / "_meta" / "book.json")
    snapshot = inside(repo, state["snapshot"]["root"])
    result = {"completed": [], "draft": [], "pending": [], "stale": [],
              "needs_rebase": [], "snapshot_errors": snapshot_errors(repo, state["snapshot"]),
              "next": None, "scope": state["scope"], "scope_changed": False,
              "blocked": False}
    if not same_scope(metadata["scope"], state["scope"]):
        result.update(scope_changed=True, blocked=True, declared_scope=metadata["scope"])
        return result
    pdf = state["source"]["pdf"]
    if not inside(repo, pdf["path"]).is_file() or sha(inside(repo, pdf["path"])) != pdf["sha256"]:
        result["needs_rebase"].append("source PDF changed")
        pdf_changed = True
    else:
        pdf_changed = False
    for rel, expected in state["snapshot"]["files"].items():
        live = inside(repo, rel)
        if not live.is_file() or sha(live) != expected:
            result["needs_rebase"].append(rel)
    for chapter in state["scope"]["chapters"]:
        entry = state["checkpoints"].get(chapter, {"status": "pending"})
        if entry["status"] == "pending":
            result["pending"].append(chapter)
            continue
        reasons = []
        try:
            current = chapter_inputs(repo, book, chapter, state["snapshot"])
            if any(current[key] != entry.get(key) for key in
                   ("chapter_sha256", "units_sha256", "source_pages")):
                reasons.append("chapter, units, or source dependencies changed")
            for rel, expected in entry.get("source_pages", {}).items():
                path = inside(snapshot, rel)
                if not path.is_file() or sha(path) != expected:
                    reasons.append(f"snapshot changed: {rel}")
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            reasons.append(str(error))
        if pdf_changed:
            reasons.append("source PDF changed")
        if result["snapshot_errors"]:
            reasons.append("snapshot changed")
        if reasons:
            result["stale"].append({"chapter": chapter, "reasons": reasons})
        else:
            result["completed" if entry["status"] == "author_checked" else "draft"].append(chapter)
    result["next"] = next((chapter for chapter in state["scope"]["chapters"] if
                           chapter in result["pending"] or chapter in result["draft"] or
                           any(x["chapter"] == chapter for x in result["stale"])), None)
    return result


ANCHOR_LINE = re.compile(r"^\s*<a\s+id=[\"']([^\"']+)[\"']\s*></a>\s*$", re.I)
PAGE_ANCHOR = re.compile(r"p(\d{4})(?:-b\d{3})?")


def compiled_parts(path: Path) -> tuple[list[str], list[str], int]:
    """Only standalone HTML anchors and wholly blank lines are layout drift."""
    meaningful, anchors, blank_count = [], [], 0
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            blank_count += 1
            continue
        match = ANCHOR_LINE.fullmatch(line)
        if match:
            anchors.append(match[1])
        else:
            meaningful.append(line)
    return meaningful, anchors, blank_count


def pdf_page_count(pdf: Path) -> int:
    result = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode:
        raise ValueError(f"pdfinfo failed: {result.stderr.strip()}")
    match = re.search(r"(?m)^Pages:\s+(\d+)\s*$", result.stdout)
    if not match:
        raise ValueError("pdfinfo did not report a physical page count")
    return int(match[1])


def rebase_identical_pages(repo: Path, book: Path, note: str) -> dict:
    """Re-pin an anchor/layout-only compiled raw book after exact page comparison."""
    if not note.strip():
        raise ValueError("Rebase requires --note explaining the observed source drift")
    meta_dir = book / "_meta"
    with exclusive(meta_dir):
        meta_path, state_path, units_path = (meta_dir / name for name in
                                             ("book.json", "clean-state.json", "units.jsonl"))
        old_bytes = {"book.json": meta_path.read_bytes(), "clean-state.json": state_path.read_bytes(),
                     "units.jsonl": units_path.read_bytes()}
        metadata, state = read_json(meta_path), read_json(state_path)
        if not same_scope(metadata["scope"], state["scope"]):
            raise ValueError("Book scope differs from clean ledger")
        if metadata["source_pdf"] != state["source"]["pdf"]:
            raise ValueError("PDF identity differs between metadata and ledger")
        pdf_info = state["source"]["pdf"]
        pdf = inside(repo, pdf_info["path"])
        if not pdf.is_file() or sha(pdf) != pdf_info["sha256"]:
            raise ValueError("Source PDF changed")
        old_snapshot = state["snapshot"]
        errors = snapshot_errors(repo, old_snapshot)
        if errors:
            raise ValueError("Old snapshot changed: " + "; ".join(errors))
        old_root = old_snapshot["root"].rstrip("/")
        source = state["source"]["markdown"]
        source_rel = source["path"]
        old_compiled_rel = old_root + "/" + source_rel
        if (metadata["source_markdown"] != {"path": old_compiled_rel, "sha256": source["sha256"]} or
                old_snapshot["files"].get(source_rel) != source["sha256"]):
            raise ValueError("Declared compiled raw book differs from old pinned source")
        live_book, old_book = inside(repo, source_rel), inside(repo, old_compiled_rel)
        if not live_book.is_file() or sha(old_book) != source["sha256"]:
            raise ValueError("Old compiled source missing or changed")
        corpus = live_book.parent
        if not corpus.is_relative_to((repo / "kaiwa_skill/corpus").resolve()):
            raise ValueError("Live source is outside kaiwa_skill/corpus")
        manifest = read_json(corpus / "manifest.json")
        physical_count = pdf_page_count(pdf)
        if (manifest.get("page_count") != physical_count or
                manifest.get("source_sha256") != pdf_info["sha256"] or
                max(state["scope"]["pdf_pages"]) > physical_count):
            raise ValueError("PDF physical page count/hash differs from raw manifest or scope")
        readiness = scan_one(repo, corpus)
        if readiness["status"] != "ready_for_fork":
            raise ValueError("Live raw corpus is not verified: " + "; ".join(readiness["reasons"]))
        old_text, old_anchors, old_blank = compiled_parts(old_book)
        new_text, new_anchors, new_blank = compiled_parts(live_book)
        if old_text != new_text:
            raise ValueError("Compiled raw learning text changed beyond standalone anchors/blank lines")
        if len(new_anchors) != len(set(new_anchors)) or not set(old_anchors).issubset(new_anchors):
            raise ValueError("Compiled raw anchors were removed or duplicated")
        page_rels = {relative(repo, corpus / "pages" / f"p{p:04d}.md")
                     for p in state["scope"]["pdf_pages"]}
        snapshot_pages = {rel for rel in old_snapshot["files"] if
                          rel.startswith(relative(repo, corpus) + "/pages/") and rel.endswith(".md")}
        if snapshot_pages != page_rels:
            raise ValueError("Snapshot page set differs from declared PDF page scope")
        for rel in sorted(page_rels):
            live = inside(repo, rel)
            if not live.is_file() or sha(live) != old_snapshot["files"][rel]:
                raise ValueError(f"Raw page body changed: {rel}")
        added_anchors = sorted(set(new_anchors) - set(old_anchors))
        for anchor in added_anchors:
            match = PAGE_ANCHOR.fullmatch(anchor)
            if not match:
                raise ValueError(f"New compiled anchor is not a PDF page/block ID: {anchor}")
            rel = relative(repo, corpus / "pages" / f"p{match[1]}.md")
            if rel not in page_rels or anchor not in compiled_parts(inside(repo, rel))[1]:
                raise ValueError(f"New compiled anchor absent from identical raw page: {anchor}")
        old_units = [json.loads(line) for line in units_path.read_text(encoding="utf-8-sig").splitlines()
                     if line.strip()]
        for chapter in state["scope"]["chapters"]:
            entry = state["checkpoints"].get(chapter, {"status": "pending"})
            if entry["status"] == "pending":
                continue
            current = chapter_inputs_rows(repo, book, chapter, old_snapshot, old_units)
            if any(current[key] != entry.get(key) for key in
                   ("chapter_sha256", "units_sha256", "source_pages")):
                raise ValueError(f"Stale chapter/units/source checkpoint: {chapter}")
        # Keep all snapshot files, including the new corpus manifest/build; pages stay byte-identical.
        live_hashes = {}
        for rel in old_snapshot["files"]:
            live = inside(repo, rel)
            if not live.is_file() or not live.is_relative_to(corpus):
                raise ValueError(f"Missing live corpus file: {rel}")
            live_hashes[rel] = sha(live)
        new_book_hash = live_hashes[source_rel]
        scope_hash = hashlib.sha256(json.dumps(state["scope"], sort_keys=True).encode()).hexdigest()[:8]
        token = uuid.uuid4().hex
        snapshot_rel = (Path("kaiwa_skill/source_snapshots") / corpus.name /
                        new_book_hash[:16] / f"{scope_hash}-rebase-{token[:8]}").as_posix()
        snapshot_dir = inside(repo, snapshot_rel)
        if snapshot_dir.exists():
            raise ValueError("New snapshot destination already exists")
        new_snapshot = {"root": snapshot_rel, "files": live_hashes}
        new_units = json.loads(json.dumps(old_units, ensure_ascii=False))
        changed_refs = 0
        for unit in new_units:
            for item in unit["source"]:
                raw = item["raw_page"]
                original = raw[len(old_root) + 1:] if raw.startswith(old_root + "/") else raw
                if original not in page_rels:
                    raise ValueError(f"Unit raw_page is outside identical snapshot pages: {raw}")
                if raw not in (original, old_root + "/" + original):
                    raise ValueError(f"Unexpected raw_page prefix: {raw}")
                item["raw_page"] = snapshot_rel + "/" + original
                changed_refs += raw != item["raw_page"]
        new_units_bytes = ("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in new_units)).encode("utf-8")
        updated_state = json.loads(json.dumps(state, ensure_ascii=False))
        updated_meta = json.loads(json.dumps(metadata, ensure_ascii=False))
        updated_state["source"]["markdown"] = {"path": source_rel, "sha256": new_book_hash}
        updated_state["snapshot"] = new_snapshot
        updated_meta["source_markdown"] = {"path": snapshot_rel + "/" + source_rel,
                                            "sha256": new_book_hash}
        updated_meta.pop("build", None)
        history_rel = (Path("_meta/rebase-history") / token).as_posix()
        stamp = now()
        for chapter in state["scope"]["chapters"]:
            entry = updated_state["checkpoints"].get(chapter, {"status": "pending"})
            if entry["status"] == "pending":
                continue
            new_inputs = chapter_inputs_rows(repo, book, chapter, new_snapshot, new_units)
            entry.update(new_inputs)
            entry.setdefault("provenance_rebases", []).append({
                "at": stamp, "history": history_rel,
                "note": "Provenance-only rebase; raw pages byte-identical; no content review was added."})
        updated_state.setdefault("rebase_history", []).append(history_rel)
        # Snapshot first; check live source a second time before touching book metadata.
        snapshot_dir.parent.mkdir(parents=True, exist_ok=True)
        temp_snapshot = snapshot_dir.with_name(f".{snapshot_dir.name}.{token}.tmp")
        temp_snapshot.mkdir()
        try:
            for rel in live_hashes:
                target = inside(temp_snapshot, rel)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(inside(repo, rel), target)
            if snapshot_errors(repo, {"root": relative(repo, temp_snapshot), "files": live_hashes}):
                raise ValueError("Live source changed while new snapshot was copied")
            os.replace(temp_snapshot, snapshot_dir)
        finally:
            if temp_snapshot.exists():
                cleanup = temp_snapshot.resolve()
                allowed = (repo / "kaiwa_skill/source_snapshots").resolve()
                if cleanup == allowed or not cleanup.is_relative_to(allowed):
                    raise ValueError("Refusing snapshot cleanup outside source_snapshots")
                shutil.rmtree(cleanup)
        if any(not inside(repo, rel).is_file() or sha(inside(repo, rel)) != digest
               for rel, digest in live_hashes.items()) or sha(pdf) != pdf_info["sha256"]:
            raise ValueError("Live source changed before rebase commit")
        if any(path.read_bytes() != old_bytes[name] for name, path in
               (("book.json", meta_path), ("clean-state.json", state_path), ("units.jsonl", units_path))):
            raise ValueError("Book metadata changed before rebase commit")
        history_dir = inside(book, history_rel)
        history_dir.parent.mkdir(parents=True, exist_ok=True)
        history_dir.mkdir()
        for name, data in old_bytes.items():
            atomic_bytes(history_dir / name, data)
        audit = {"schema_version": 1, "at": stamp, "note": note,
                 "old_files_sha256": {name: hashlib.sha256(data).hexdigest() for name, data in old_bytes.items()},
                 "old_snapshot": old_root, "new_snapshot": snapshot_rel,
                 "old_compiled_sha256": source["sha256"], "new_compiled_sha256": new_book_hash,
                 "pdf_sha256": pdf_info["sha256"], "physical_pdf_pages": physical_count,
                 "identical_page_count": len(page_rels), "changed_raw_page_count": 0,
                 "added_compiled_anchors": added_anchors, "removed_compiled_anchors": [],
                 "old_blank_lines": old_blank, "new_blank_lines": new_blank,
                 "relocated_unit_references": changed_refs,
                 "live_file_hashes": live_hashes}
        atomic_json(history_dir / "audit.json", audit)
        try:
            atomic_bytes(units_path, new_units_bytes)
            atomic_json(meta_path, updated_meta)
            atomic_json(state_path, updated_state)
            progress = resume(repo, book)
            if progress["snapshot_errors"] or progress["needs_rebase"] or progress["stale"]:
                raise ValueError("Post-rebase guards failed; original metadata restored")
        except Exception:
            for name, path in (("units.jsonl", units_path), ("book.json", meta_path),
                               ("clean-state.json", state_path)):
                atomic_bytes(path, old_bytes[name])
            raise
        return {"status": "rebased_provenance_only", "history": history_rel,
                "new_snapshot": snapshot_rel, "identical_pages": len(page_rels),
                "added_anchors": added_anchors, "relocated_unit_references": changed_refs,
                "completed_chapters": len(progress["completed"]), "draft_chapters": len(progress["draft"]),
                "next_action": "rebuild book/search and validate; semantic QA remains independent"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("scan", "init", "checkpoint", "resume", "rebase-identical-pages"):
        sub = commands.add_parser(name)
        if name != "scan":
            sub.add_argument("book_dir", type=Path)
        sub.add_argument("--repo-root", required=True, type=Path)
        if name == "checkpoint":
            sub.add_argument("--chapter", required=True)
            sub.add_argument("--status", choices=("draft", "author_checked"), required=True)
            sub.add_argument("--note", default="")
        if name == "rebase-identical-pages":
            sub.add_argument("--note", required=True,
                             help="Auditable explanation of anchor/layout-only compiled raw drift")
    args = parser.parse_args()
    try:
        repo = args.repo_root.resolve()
        if args.command == "scan":
            output = scan(repo)
        else:
            book = args.book_dir.resolve()
            if not book.is_relative_to(repo) or not (book / "_meta").is_dir():
                raise ValueError("Book directory must be inside repo and contain _meta")
            if args.command == "init":
                output = init(repo, book)
            elif args.command == "checkpoint":
                output = checkpoint(repo, book, args.chapter, args.status, args.note)
            elif args.command == "rebase-identical-pages":
                output = rebase_identical_pages(repo, book, args.note)
            else:
                output = resume(repo, book)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        parser.exit(1, f"clean_progress: {error}\n")


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    main()
