"""Export the reviewed, dated JLPT corpus for the Harumi admin folder picker."""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from uuid import uuid4

from build_catalog import approved_entries
from build_pilot_bundle import check_bundle, sha256
from listening_stt import master_lock
from verify_capture import verify


def export(root):
    root = root.resolve()
    if not (root / "packages").is_dir():
        raise ValueError("Missing authoring directory: packages")
    work = root / "work/evidence/publish"
    work.mkdir(parents=True, exist_ok=True)
    current = root / "publish-ready"
    previous = work / "previous"
    with master_lock(work, "Another release export is active."):
        if previous.exists():
            if current.exists():
                previous.rename(work / f"archive-{uuid4().hex}")
            else:
                previous.rename(current)
        with TemporaryDirectory(dir=work) as temp:
            scratch = Path(temp)
            stage = scratch / "publish-ready"
            stage.mkdir()
            version, entries = approved_entries(root)
            manifest = {}
            catalog = {"schemaVersion": version, "packages": entries}
            if entries:
                origin = scratch / "catalog.json"
                origin.write_text(json.dumps(catalog), encoding="utf-8")
                validator = Path(__file__).resolve().parents[1] / "contracts/v1/validate_package.py"
                subprocess.run([sys.executable, str(validator), str(origin), "--root", str(root),
                                "--release"], check=True)
            for entry in entries:
                source = root / entry["path"]
                package = json.loads(source.read_bytes())
                if package["schemaVersion"] != "1.3.0":
                    raise ValueError(f"Review a dated 1.3 package before release: {source}")
                receipt = json.loads(source.with_name("release-review.json").read_bytes())
                for key in ("packageId", "revision", "sha256"):
                    if receipt.get(key) != entry[key]:
                        raise ValueError(f"Review receipt mismatch: {source} ({key})")
                verify(package, root)
                level = package["exam"]["level"]
                period = package["exam"]["slug"].replace("/", "-")
                dest = f"{level}/JLPT-{level}-{period}-r{entry['revision']:02d}/package.json"
                inputs = [(source, dest, entry["sha256"])]
                inputs.extend((root / a["path"], a["path"], a["sha256"]) for a in package["assets"])
                for path, name, digest in inputs:
                    if name in manifest:
                        if manifest[name] != digest:
                            raise ValueError(f"Conflicting release file: {name}")
                        continue
                    target = stage / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(path, target)
                    manifest[name] = digest
                entry["path"] = dest
            if entries:
                index = stage / "catalog.json"
                index.write_bytes((json.dumps(catalog, ensure_ascii=False, indent=2) + "\n").encode())
                manifest["catalog.json"] = sha256(index)
            check_bundle(stage, manifest)
            if current.is_dir():
                try:
                    check_bundle(current, manifest)
                except ValueError:
                    current.rename(previous)
                else:
                    return len(entries)
            try:
                stage.rename(current)
            except OSError:
                if previous.exists() and not current.exists():
                    previous.rename(current)
                raise
            if previous.exists():
                previous.rename(work / f"archive-{uuid4().hex}")
    return len(entries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    try:
        args = parser.parse_args()
        count = export(args.root)
        print(f"{args.root.resolve() / 'publish-ready'}: {count} approved package(s)")
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
