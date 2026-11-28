"""Build the local release catalog from approved packages, validating before replacement."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def build(root):
    entries = []
    version = "1.2.0"
    for path in sorted((root / "packages").glob("*/*/package.json")):
        raw = path.read_bytes()
        data = json.loads(raw.decode("utf-8-sig"))
        state = data["review"]["status"]
        relative = path.relative_to(root).as_posix()
        if state != "approved":
            print(f"Skipped {relative} ({state})", file=sys.stderr)
            continue
        if data["schemaVersion"] == "1.3.0":
            version = "1.3.0"
        entries.append({"packageId": data["packageId"], "revision": data["revision"],
                        "path": relative, "sha256": hashlib.sha256(raw).hexdigest()})
    if not entries:
        raise ValueError("No approved package found. No new catalog was generated.")
    content = json.dumps({"schemaVersion": version, "packages": entries},
                         indent=2, ensure_ascii=False) + "\n"
    with tempfile.NamedTemporaryFile(dir=root, prefix=".catalog-", suffix=".json",
                                     delete=False) as output:
        temp = Path(output.name)
        output.write(content.encode("utf-8"))
    try:
        validator = Path(__file__).resolve().parents[1] / "contracts/v1/validate_package.py"
        subprocess.run([sys.executable, str(validator), str(temp), "--root", str(root),
                        "--release"], check=True)
        os.replace(temp, root / "catalog.json")
    finally:
        temp.unlink(missing_ok=True)
    print(f"{root / 'catalog.json'} ({len(entries)} packages)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    try:
        build(parser.parse_args().root.resolve())
    except (KeyError, TypeError, ValueError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
