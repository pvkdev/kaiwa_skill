import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PLAN = ROOT / "kaiwa_skill/planning"
manifest = json.loads((PLAN / "catalog27/manifest.json").read_text(encoding="utf8"))
allowed = {"B01", "B05", "B06", "B07", "B08", "B11", "B12", "B13", "B14", "B18", "B19", "B20", "B24"}
records = []
for book in manifest["books"]:
    if book["book_id"] not in allowed:
        continue
    meta_path = ROOT / book["directory"] / "_meta/units.jsonl"
    metas = {x["unit_id"]: x for x in (json.loads(s) for s in meta_path.read_text(encoding="utf8").splitlines() if s.strip())}
    for ch in book["chapters"]:
        path = ROOT / ch["path"]
        data = path.read_bytes()
        lines = data.decode("utf-8-sig").splitlines()
        anchors = [(i, m.group(1)) for i, line in enumerate(lines, 1) if (m := re.search(r'<a id="([^"]+)"', line))]
        for a, (start, uid) in enumerate(anchors):
            if uid not in metas:
                continue
            end = anchors[a + 1][0] - 1 if a + 1 < len(anchors) else len(lines)
            heading = next((re.sub(r"^#{2,3} ", "", x).strip() for x in lines[start:end]
                            if re.match(r"^#{2,3} ", x)), "")
            body = "\n".join(lines[start - 1:end])
            records.append({"book_id": book["book_id"], "book_title": book["title"],
                            "unit_id": uid, "meta_heading": metas[uid]["heading"], "heading": heading,
                            "path": ch["path"], "sha256": hashlib.sha256(data).hexdigest(),
                            "start_line": start, "end_line": end, "text": body})
out = Path(__file__).with_name("unit_index.json")
out.write_text(json.dumps(records, ensure_ascii=False), encoding="utf8")
print(len(records), "records ->", out)
