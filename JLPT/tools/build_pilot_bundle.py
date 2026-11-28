"""Build a standalone folder for a Harumi developer's draft import (Python 3.11+)."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def check_bundle(folder, files):
    actual = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
    if actual != set(files):
        raise ValueError(f"Unexpected contents in {folder}")
    for name, expected in files.items():
        if sha256(folder / name) != expected:
            raise ValueError(f"Bundle checksum mismatch: {name}")


def build(root, selected=None):
    packages = []
    version = "1.2.0"
    files = {}
    paths = sorted((root / "packages").glob("*/*/package.json"))
    if selected is not None:
        path = (root / selected).resolve()
        if path not in paths:
            raise ValueError("--package must identify an existing packages/<level>/<period>/package.json under --root")
        paths = [path]
    for path in paths:
        raw = path.read_bytes()
        package = json.loads(raw)
        if package["schemaVersion"] == "1.3.0":
            version = "1.3.0"
        relative = path.relative_to(root).as_posix()
        digest = hashlib.sha256(raw).hexdigest()
        files[relative] = digest
        packages.append({"packageId": package["packageId"], "revision": package["revision"],
                         "path": relative, "sha256": digest})
        for asset in package["assets"]:
            files[asset["path"]] = asset["sha256"]
    if not packages:
        raise ValueError("No packages/*/*/package.json found.")
    catalog = json.dumps({"schemaVersion": version, "packages": packages},
                         ensure_ascii=False, indent=2).encode() + b"\n"
    bundle_id = hashlib.sha256(catalog).hexdigest()
    parent = root / "pilot-upload"
    parent.mkdir(exist_ok=True)
    final = parent / bundle_id[:16]
    # The validator reads the raw captures in the authoring tree before packaging.
    with tempfile.TemporaryDirectory(prefix="building-", dir=parent) as scratch:
        stage = Path(scratch) / "bundle"
        stage.mkdir()
        index = stage / "catalog.json"
        index.write_bytes(catalog)
        validator = Path(__file__).resolve().parents[1] / "contracts/v1/validate_package.py"
        subprocess.run([sys.executable, str(validator), str(index), "--root", str(root)], check=True)
        if not final.exists():
            for name in files:
                dest = stage / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / name, dest)
        files["catalog.json"] = bundle_id
        if not final.exists():
            check_bundle(stage, files)
            try:
                stage.rename(final)
            except OSError:
                if not final.is_dir():
                    raise
        check_bundle(final, files)
    print(f"{final} ({len(packages)} packages, {len(files) - len(packages) - 1} assets)")
    return final


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--package", type=Path, help="Bundle a single exam, including all referenced assets")
    try:
        args = parser.parse_args()
        build(args.root.resolve(), args.package)
    except (KeyError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        sys.exit(str(exc))
