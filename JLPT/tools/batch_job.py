"""Coordinator checkpoint for a single audited JLPT exam. Never starts workers or edits packages."""
import argparse
import json
import re
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from build_pilot_bundle import sha256


def inputs(root, level, period):
    report = json.loads((root / "reports/source-gaps.json").read_bytes())
    pages = [p for p in report["pages"] if (p["level"], p["period"]) == (level, period)]
    if not pages:
        raise ValueError("Exam not present in the source audit")
    sections = [p["section"] for p in pages]
    if len(set(sections)) != len(sections) or any(s not in ("written", "listening") for s in sections):
        raise ValueError("Resolve the ambiguous exam captures in the audit first")
    files = {}
    for page in pages:
        source = (root / page["path"]).resolve()
        if not source.is_relative_to(root) or sha256(source) != page["sha256"]:
            raise ValueError("Refresh source audit: " + page["path"])
        for f in source.parent.rglob("*"):
            if f.is_file():
                files[f.relative_to(root).as_posix()] = sha256(f)
    canonical = root / "packages" / level / period / "package.json"
    base = None
    if canonical.is_file():
        base = {"revision": json.loads(canonical.read_bytes())["revision"], "sha256": sha256(canonical)}
    return {"level": level, "period": period, "files": files, "base": base}


def checkpoint(root, level, period, owner):
    if level not in ("N5", "N4", "N3", "N2", "N1") or not re.fullmatch(r"[0-9]{4}-(07|12)", period):
        raise ValueError("Expected level N5–N1 and period YYYY-MM")
    state = inputs(root, level, period)
    folder = root / "work/evidence/batch" / level / period
    record = folder / "job.json"
    if owner and not folder.exists():
        folder.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(dir=folder.parent) as scratch:
            stage = Path(scratch) / "job"
            stage.mkdir()
            (stage / "job.json").write_text(json.dumps(dict(**state, owner=owner), ensure_ascii=False, indent=2),
                                           encoding="utf-8")
            stage.rename(folder)
    if not record.is_file():
        raise ValueError("No checkpoint yet. Claim this exam with --owner.")
    saved = json.loads(record.read_bytes())
    if owner and saved["owner"] != owner:
        raise ValueError(f"Already assigned to {saved['owner']}: {folder}")
    if any(saved[key] != value for key, value in state.items()):
        raise ValueError(f"Inputs or canonical package changed. Reconcile and archive the previous job: {folder}")
    print(f"{folder} ({saved['owner']})")
    return folder


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--root", type=Path, default=Path.cwd())
    cli.add_argument("--level", required=True)
    cli.add_argument("--period", required=True)
    cli.add_argument("--owner")
    try:
        args = cli.parse_args()
        checkpoint(args.root.resolve(), args.level, args.period, args.owner)
    except (ValueError, KeyError, OSError) as exc:
        sys.exit(str(exc))
