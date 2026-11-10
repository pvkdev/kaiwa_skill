"""Resumable PDF transcription ledger. Rendering is never evidence of review.

Run ``python kaiwa_skill/tools/ingest.py --help``. All persisted source paths
are relative to --root; corpus paths are relative to their book directory.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import uuid
from urllib.parse import unquote, urlparse

import pypdfium2 as pdfium

CHECKS = ("visual_review", "text_complete", "reading_order", "japanese_accuracy")


class IngestError(Exception):
    pass


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def atomic_bytes(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp-" + uuid.uuid4().hex)
    try:
        with temp.open("xb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def atomic_json(path, value):
    atomic_bytes(path, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise IngestError(f"Cannot read valid JSON at {path}: {exc}") from exc


def safe_child(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or path == root:
        raise IngestError(f"Path must stay inside {root}: {relative}")
    return path


def book_dir(root, book):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,100}", book):
        raise IngestError("Book id must contain only ASCII letters, digits, '-' or '_'.")
    return safe_child(Path(root) / "corpus", book)


def stable_id(source, digest):
    stem = re.sub(r"[^a-z0-9]+", "-", Path(source).stem.lower()).strip("-")[:55] or "book"
    return f"{stem}-{digest[:12]}"


def exclusive_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.flush()
            os.fsync(stream.fileno())
    except FileExistsError as exc:
        raise IngestError(f"Lock/claim already exists: {path}. Inspect it; explicit recover is required if stale.") from exc


@contextmanager
def writer(directory, token=None, ignore_claim=False):
    lock = directory / ".write.lock"
    own = uuid.uuid4().hex
    exclusive_json(lock, {"token": own, "pid": os.getpid(), "created_at": now()})
    try:
        claim = directory / "claim.json"
        if claim.exists() and not ignore_claim:
            if read_json(claim).get("token") != token:
                raise IngestError("Book is claimed; supply the matching --token.")
        yield
    finally:
        # Never delete another writer's lock after an explicit recovery.
        if lock.exists() and read_json(lock).get("token") == own:
            lock.unlink()


def load_book(root, book):
    directory = book_dir(root, book)
    manifest = read_json(directory / "manifest.json")
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1 or manifest.get("id") != book:
        raise IngestError("Invalid manifest schema or book id.")
    if not isinstance(manifest.get("page_count"), int) or manifest["page_count"] < 1:
        raise IngestError("Invalid manifest page count.")
    source = safe_child(root, manifest["source"])
    if not source.is_file() or sha(source) != manifest["source_sha256"]:
        raise IngestError("Source PDF changed or is missing; restore it or initialize a new book id.")
    return directory, manifest, source


def page_paths(directory, page):
    stem = f"p{page:04d}"
    return directory / "pages" / (stem + ".json"), directory / "pages" / (stem + ".md"), directory / "renders" / (stem + ".png")


def markdown_errors(directory, page, text):
    errors = []
    if f'<a id="p{page:04d}"></a>' not in text:
        errors.append("missing stable page anchor")
    anchors = re.findall(r'<a id="(p\d{4}-b\d{3})"></a>', text)
    if not anchors or len(anchors) != len(set(anchors)) or any(not a.startswith(f"p{page:04d}-") for a in anchors):
        errors.append("missing, duplicate, or wrong-page block anchors")
    # Inline Markdown and HTML asset references; reference-style Markdown is
    # rejected so unsupported references cannot silently evade validation.
    if re.search(r'^\s*\[[^\]]+\]:', text, re.M):
        errors.append("reference-style links unsupported; use inline links")
    links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text)
    links += re.findall(r'(?:src|href)=[\"\']([^\"\']+)', text)
    for link in links:
        target = link.strip().split(' "', 1)[0].strip("<>")
        if target.startswith("#") or urlparse(target).scheme in ("http", "https", "mailto", "data"):
            continue
        try:
            asset = safe_child(directory, "pages/" + unquote(target.split("#", 1)[0]))
            if not asset.is_file():
                errors.append("missing local asset: " + target)
        except IngestError:
            errors.append("local asset escapes book: " + target)
    return errors


def valid_page(manifest, page):
    if not 1 <= page <= manifest["page_count"]:
        raise IngestError(f"Page {page} outside 1..{manifest['page_count']}")


def page_integrity(directory, manifest, page):
    state_path, md, render = page_paths(directory, page)
    if not state_path.exists():
        return None, ["missing page checkpoint"]
    try:
        state = read_json(state_path)
        if not isinstance(state, dict):
            raise IngestError("Page checkpoint must be a JSON object.")
        errors = []
        if state.get("status") not in ("rendered", "draft", "verified", "needs_review", "invalid"):
            errors.append("unknown page status")
        if not state.get("render_sha256"):
            errors.append("missing render hash")
        if state.get("status") in ("draft", "verified") and not state.get("markdown_sha256"):
            errors.append("missing Markdown hash")
        if state.get("page") != page or state.get("source_sha256") != manifest["source_sha256"]:
            errors.append("page/source identity mismatch")
        for path, field in ((render, "render_sha256"), (md, "markdown_sha256")):
            if state.get(field) and (not path.exists() or sha(path) != state[field]):
                errors.append(f"{field} mismatch or missing file")
        if state.get("status") == "verified":
            if not state.get("render_sha256") or not state.get("markdown_sha256"):
                errors.append("verified page lacks content hashes")
            evidence = state.get("evidence", {})
            try:
                validate_evidence(evidence, manifest, state)
            except IngestError as exc:
                errors.append(str(exc))
            if md.exists():
                errors.extend(markdown_errors(directory, page, md.read_text(encoding="utf-8")))
        return state, errors
    except IngestError as exc:
        return None, [str(exc)]


def checkpoint(directory, manifest):
    counts = {"pending": 0, "rendered": 0, "draft": 0, "verified": 0, "needs_review": 0, "invalid": 0}
    pages = {}
    for page in range(1, manifest["page_count"] + 1):
        state, errors = page_integrity(directory, manifest, page)
        status = "pending" if state is None and errors == ["missing page checkpoint"] else "invalid" if errors else state.get("status", "invalid")
        if status not in counts:
            status = "invalid"
        counts[status] += 1
        pages[str(page)] = status
    manifest.update(updated_at=now(), counts=counts, pages=pages,
                    complete=counts["verified"] == manifest["page_count"],
                    transcription_complete=counts["verified"] == manifest["page_count"],
                    acceptance="coordinator_review_required")
    atomic_json(directory / "manifest.json", manifest)
    return manifest


def inventory(root):
    entries = []
    for category in ("book", "vocab"):
        folder = root / category
        for source in sorted(folder.rglob("*")):
            if source.is_file() and source.suffix.lower() == ".pdf":
                relative = source.relative_to(root).as_posix()
                digest = sha(source)
                entry = {"id": stable_id(relative, digest), "source": relative, "source_sha256": digest, "bytes": source.stat().st_size}
                try:
                    with pdfium.PdfDocument(source) as pdf:
                        entry["page_count"] = len(pdf)
                except Exception as exc:
                    entry["error"] = str(exc)
                entries.append(entry)
    catalog = {"schema_version": 1, "generated_at": now(), "books": entries}
    atomic_json(root / "corpus" / "catalog.json", catalog)
    return catalog


def initialize(root, source_name, requested_id=None):
    source = safe_child(root, source_name)
    relative = source.relative_to(root.resolve()).as_posix()
    if relative.split("/")[0] not in ("book", "vocab") or source.suffix.lower() != ".pdf":
        raise IngestError("Source must be a PDF inside book/ or vocab/.")
    digest = sha(source)
    book = requested_id or stable_id(relative, digest)
    directory = book_dir(root, book)
    with writer(directory):
        if (directory / "manifest.json").exists():
            _, manifest, _ = load_book(root, book)
            if manifest["source"] != relative or manifest["source_sha256"] != digest:
                raise IngestError("Book id already belongs to a different PDF.")
            return manifest
        with pdfium.PdfDocument(source) as pdf:
            count = len(pdf)
        manifest = {"schema_version": 1, "id": book, "source": relative,
                    "source_sha256": digest, "page_count": count, "created_at": now()}
        return checkpoint(directory, manifest)


def parse_pages(value, count):
    result = set()
    for part in value.split(","):
        if re.fullmatch(r"\d+-\d+", part):
            first, last = map(int, part.split("-"))
            if first > last:
                raise IngestError("Page range must be increasing.")
            result.update(range(first, last + 1))
        elif part.isdigit():
            result.add(int(part))
        else:
            raise IngestError("Use page numbers/ranges such as 1,3-5.")
    if not result or min(result) < 1 or max(result) > count:
        raise IngestError(f"Pages must be in 1..{count}.")
    return sorted(result)


def render_pages(directory, manifest, source, pages, scale=2.0):
    if not 0.5 <= scale <= 6:
        raise IngestError("Render scale must be between 0.5 and 6.")
    with pdfium.PdfDocument(source) as pdf:
        for number in pages:
            state_path, md, image = page_paths(directory, number)
            state, errors = page_integrity(directory, manifest, number)
            if state and not errors and state.get("render_sha256") and state.get("render_scale") == scale:
                continue
            page = pdf[number - 1]
            bitmap = page.render(scale=scale)
            import io
            buffer = io.BytesIO()
            bitmap.to_pil().save(buffer, format="PNG")
            bitmap.close()
            page.close()
            atomic_bytes(image, buffer.getvalue())
            state = {"page": number, "source_sha256": manifest["source_sha256"],
                     "status": "rendered", "render_sha256": sha(image), "render_scale": scale, "updated_at": now()}
            # A re-render invalidates review; an existing draft remains usable.
            if md.exists():
                state.update(status="draft", markdown_sha256=sha(md))
            atomic_json(state_path, state)
            checkpoint(directory, manifest)
    return manifest


def record_page(directory, manifest, page, markdown):
    valid_page(manifest, page)
    state_path, md, _ = page_paths(directory, page)
    state, errors = page_integrity(directory, manifest, page)
    if not state or errors:
        raise IngestError("Render/reconcile page before recording: " + "; ".join(errors))
    text = Path(markdown).read_text(encoding="utf-8-sig")
    if not text.strip():
        raise IngestError("Markdown cannot be empty; explicitly describe a blank page.")
    if f'<a id="p{page:04d}"></a>' not in text:
        text = f'<a id="p{page:04d}"></a>\n\n' + text
    if not re.search(r'<a id="p\d{4}-b\d{3}"></a>', text):
        text = text.replace(f'<a id="p{page:04d}"></a>', f'<a id="p{page:04d}"></a>\n\n<a id="p{page:04d}-b001"></a>', 1)
    errors = markdown_errors(directory, page, text)
    if errors:
        raise IngestError("; ".join(errors))
    atomic_bytes(md, text.encode("utf-8"))
    state.update(status="draft", markdown_sha256=sha(md), updated_at=now())
    state.pop("evidence", None)
    state.pop("invalid_reasons", None)
    state.pop("issues", None)
    atomic_json(state_path, state)
    return checkpoint(directory, manifest)


def evidence_template(directory, manifest, page):
    valid_page(manifest, page)
    state, errors = page_integrity(directory, manifest, page)
    if not state or errors or not state.get("markdown_sha256"):
        raise IngestError("A valid recorded draft is required before review.")
    return {"page": page, "source_sha256": manifest["source_sha256"],
            "render_sha256": state["render_sha256"], "markdown_sha256": state["markdown_sha256"],
            "reviewer": "", "reviewed_at": "", "checks": {key: False for key in CHECKS},
            "notes": "Describe actual visual comparison, uncertainty handling, and corrections."}


def validate_evidence(evidence, manifest, state):
    if not isinstance(evidence, dict) or not isinstance(evidence.get("checks"), dict):
        raise IngestError("Evidence and checks must be JSON objects.")
    for field in ("page", "source_sha256", "render_sha256", "markdown_sha256"):
        expected = state.get(field)
        if evidence.get(field) != expected or expected is None:
            raise IngestError(f"Review evidence {field} does not match this page.")
    if evidence.get("source_sha256") != manifest["source_sha256"]:
        raise IngestError("Review source hash mismatch.")
    if not isinstance(evidence.get("reviewer"), str) or not evidence["reviewer"].strip():
        raise IngestError("Evidence requires the actual reviewer's identity.")
    try:
        timestamp = datetime.fromisoformat(evidence.get("reviewed_at", "").replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("timezone required")
    except (ValueError, TypeError) as exc:
        raise IngestError("reviewed_at requires an ISO timestamp with timezone.") from exc
    if any(evidence.get("checks", {}).get(key) is not True for key in CHECKS):
        raise IngestError("Every explicit reviewer check must be true after actual visual review.")
    if not isinstance(evidence.get("notes"), str) or not evidence["notes"].strip():
        raise IngestError("Evidence requires concrete review notes.")


def verify_page(directory, manifest, page, evidence):
    valid_page(manifest, page)
    state_path, _, _ = page_paths(directory, page)
    state, errors = page_integrity(directory, manifest, page)
    if not state or errors or state.get("status") not in ("draft", "verified"):
        raise IngestError("Cannot verify page without a valid draft: " + "; ".join(errors))
    errors = markdown_errors(directory, page, page_paths(directory, page)[1].read_text(encoding="utf-8"))
    if errors:
        raise IngestError("; ".join(errors))
    validate_evidence(evidence, manifest, state)
    state.update(status="verified", evidence=evidence, updated_at=now())
    atomic_json(state_path, state)
    return checkpoint(directory, manifest)


def needs_review(directory, manifest, page, issue):
    valid_page(manifest, page)
    if not issue.strip():
        raise IngestError("An explicit review issue is required.")
    state_path, _, _ = page_paths(directory, page)
    state, errors = page_integrity(directory, manifest, page)
    if not state or errors:
        raise IngestError("Render or repair this page before recording an issue.")
    state.update(status="needs_review", updated_at=now())
    state.pop("evidence", None)
    state.setdefault("issues", []).append({"issue": issue, "created_at": now()})
    atomic_json(state_path, state)
    return checkpoint(directory, manifest)


def reconcile(directory, manifest):
    # Page checkpoints are authoritative; never reconstruct review from loose files.
    for page in range(1, manifest["page_count"] + 1):
        state, errors = page_integrity(directory, manifest, page)
        if state and errors:
            state.update(status="invalid", invalid_reasons=errors, updated_at=now())
            state.pop("evidence", None)
            atomic_json(page_paths(directory, page)[0], state)
    return checkpoint(directory, manifest)


def build(directory, manifest):
    reconcile(directory, manifest)
    complete = manifest["complete"]
    lines = [f"# {manifest['id']}", "", "Status: " + ("TRANSCRIPTION_COMPLETE_REVIEW_REQUIRED" if complete else "INCOMPLETE — only verified pages are included."),
             "Coordinator acceptance is separate from page verification coverage.",
             "", f"Source: `{manifest['source']}`", f"Source SHA-256: `{manifest['source_sha256']}`", ""]
    index = []
    for number in range(1, manifest["page_count"] + 1):
        state, errors = page_integrity(directory, manifest, number)
        if state and not errors and state["status"] == "verified":
            content = page_paths(directory, number)[1].read_text(encoding="utf-8")
            def rebase(match):
                target = match.group(2)
                if target.startswith("#") or urlparse(target).scheme:
                    return match.group(0)
                return match.group(1) + "pages/" + target + match.group(3)
            combined = re.sub(r'(!?\[[^\]]*\]\()([^)]*)(\))', rebase, content)
            combined = re.sub(r'((?:src|href)=[\"\'])([^\"\']+)([\"\'])', rebase, combined)
            lines.extend([f"## PDF page {number}", "", combined.rstrip(), ""])
            parts = re.split(r'<a id="(p\d{4}-b\d{3})"></a>', content)
            for position in range(1, len(parts), 2):
                index.append({"book_id": manifest["id"], "page": number, "block_id": parts[position], "source": manifest["source"],
                          "source_sha256": manifest["source_sha256"], "markdown_sha256": state["markdown_sha256"],
                          "complete_book": complete, "transcription_complete": complete, "text": parts[position + 1].strip()})
    # build.json is the final commit marker: readers must verify its output hashes.
    atomic_bytes(directory / "book.md", ("\n".join(lines) + "\n").encode("utf-8"))
    atomic_bytes(directory / "search.jsonl", ("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in index)).encode("utf-8"))
    result = {"generated_at": now(), "source_sha256": manifest["source_sha256"], "complete": complete,
              "verified_pages": sorted(set(row["page"] for row in index)), "book_sha256": sha(directory / "book.md"),
              "transcription_complete": complete, "acceptance": "coordinator_review_required",
              "page_hashes": {str(row["page"]): row["markdown_sha256"] for row in index},
              "search_sha256": sha(directory / "search.jsonl")}
    atomic_json(directory / "build.json", result)
    return result


def status(directory, manifest):
    result = {"id": manifest["id"], "page_count": manifest["page_count"], "pages": {}, "claim": None, "counts": {}, "issue_count": 0}
    if (directory / "claim.json").exists():
        result["claim"] = read_json(directory / "claim.json")
    for page in range(1, manifest["page_count"] + 1):
        state, errors = page_integrity(directory, manifest, page)
        pending = state is None and errors == ["missing page checkpoint"]
        page_status = "pending" if pending else "invalid" if errors else state.get("status")
        issues = state.get("issues", []) if state else []
        result["pages"][str(page)] = {"status": page_status, "errors": [] if pending else errors, "issues": issues}
        result["counts"][page_status] = result["counts"].get(page_status, 0) + 1
        result["issue_count"] += len(issues)
    build_path = directory / "build.json"
    result["build_current"] = False
    if build_path.exists():
        try:
            meta = read_json(build_path)
            verified = [int(n) for n, item in result["pages"].items() if item["status"] == "verified" and not item["errors"]]
            hashes = {str(n): page_integrity(directory, manifest, n)[0]["markdown_sha256"] for n in verified}
            result["build_current"] = (meta["source_sha256"] == manifest["source_sha256"] and meta.get("page_hashes") == hashes and meta["verified_pages"] == verified and sha(directory / "book.md") == meta["book_sha256"] and sha(directory / "search.jsonl") == meta["search_sha256"])
        except (IngestError, OSError, KeyError):
            pass
    return result


def status_all(root):
    catalog = read_json(root / "corpus" / "catalog.json")
    result = {"books": [], "total_pages": 0, "counts": {}, "issue_count": 0}
    for entry in catalog["books"]:
        row = {"id": entry["id"], "source": entry["source"], "page_count": entry.get("page_count", 0)}
        try:
            if entry.get("error"):
                raise IngestError(entry["error"])
            if (book_dir(root, entry["id"]) / "manifest.json").exists():
                directory, manifest, _ = load_book(root, entry["id"])
                row.update(status(directory, manifest))
                row.pop("pages")
            else:
                row.update(counts={"pending": row["page_count"]}, initialized=False, claim=None, issue_count=0)
        except (IngestError, OSError, KeyError, TypeError) as exc:
            row["error"] = str(exc)
        result["books"].append(row)
        result["total_pages"] += row["page_count"]
        result["issue_count"] += row.get("issue_count", 0)
        for key, value in row.get("counts", {}).items():
            result["counts"][key] = result["counts"].get(key, 0) + value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("inventory")
    commands.add_parser("status-all")
    init = commands.add_parser("init")
    init.add_argument("--source", required=True)
    init.add_argument("--id")
    for name in ("status", "claim", "release", "recover", "render", "record", "needs_review", "evidence-template", "verify", "reconcile", "build"):
        sub = commands.add_parser(name)
        sub.add_argument("book")
        sub.add_argument("--token")
        if name == "claim":
            sub.add_argument("--owner", required=True)
        if name == "recover":
            sub.add_argument("--kind", choices=("claim", "write"), required=True)
            choice = sub.add_mutually_exclusive_group(required=True)
            choice.add_argument("--expected-token")
            choice.add_argument("--expected-sha256")
            sub.add_argument("--confirm-writer-stopped", action="store_true")
            sub.add_argument("--reason", required=True)
        if name == "render":
            sub.add_argument("--pages", required=True)
            sub.add_argument("--scale", type=float, default=2.0)
        if name in ("record", "verify", "evidence-template", "needs_review"):
            sub.add_argument("--page", type=int, required=True)
        if name == "needs_review":
            sub.add_argument("--issue", required=True)
        if name == "record":
            sub.add_argument("--markdown", type=Path, required=True)
        if name == "verify":
            sub.add_argument("--evidence", type=Path, required=True)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "inventory":
            result = inventory(root)
        elif args.command == "status-all":
            result = status_all(root)
        elif args.command == "init":
            result = initialize(root, args.source, args.id)
        else:
            directory, manifest, source = load_book(root, args.book)
            if args.command == "status":
                result = status(directory, manifest)
            elif args.command == "evidence-template":
                result = evidence_template(directory, manifest, args.page)
            elif args.command == "recover":
                path = directory / ("claim.json" if args.kind == "claim" else ".write.lock")
                def recover():
                    if not args.confirm_writer_stopped:
                        raise IngestError("Recovery requires --confirm-writer-stopped after coordinator confirms the old worker is stopped.")
                    raw = path.read_bytes()
                    if args.expected_sha256:
                        if hashlib.sha256(raw).hexdigest() != args.expected_sha256.lower():
                            raise IngestError("Recovery SHA-256 mismatch.")
                        current = {"raw_hex": raw.hex(), "sha256": args.expected_sha256}
                    else:
                        current = read_json(path)
                        if current.get("token") != args.expected_token:
                            raise IngestError("Recovery token mismatch; inspect current lock/claim.")
                    if not args.reason.strip():
                        raise IngestError("Recovery reason cannot be empty.")
                    atomic_json(directory / "recovery" / (uuid.uuid4().hex + ".json"), {"kind": args.kind, "previous": current, "reason": args.reason, "recovered_at": now()})
                    path.unlink()
                    return {"recovered": args.kind}
                if args.kind == "claim":
                    with writer(directory, ignore_claim=True):
                        result = recover()
                else:
                    result = recover()
            else:
                with writer(directory, args.token, ignore_claim=args.command == "claim"):
                    # Recheck inside the lock, including source identity.
                    directory, manifest, source = load_book(root, args.book)
                    if args.command == "claim":
                        result = {"owner": args.owner, "token": args.token or uuid.uuid4().hex, "created_at": now()}
                        exclusive_json(directory / "claim.json", result)
                    elif args.command == "release":
                        if not args.token or not (directory / "claim.json").exists():
                            raise IngestError("Release requires an existing claim and its token.")
                        (directory / "claim.json").unlink()
                        result = {"released": args.book}
                    elif args.command == "render":
                        result = render_pages(directory, manifest, source, parse_pages(args.pages, manifest["page_count"]), args.scale)
                    elif args.command == "record":
                        result = record_page(directory, manifest, args.page, args.markdown)
                    elif args.command == "needs_review":
                        result = needs_review(directory, manifest, args.page, args.issue)
                    elif args.command == "verify":
                        result = verify_page(directory, manifest, args.page, read_json(args.evidence))
                    elif args.command == "reconcile":
                        result = reconcile(directory, manifest)
                    elif args.command == "build":
                        result = build(directory, manifest)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (IngestError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
