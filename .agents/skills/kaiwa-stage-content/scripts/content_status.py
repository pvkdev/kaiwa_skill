"""Derived curriculum authoring status; the per-stage run files remain authoritative."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[4])
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    pointer = read(repo / "kaiwa_skill/planning/CURRENT_ROADMAP.json")
    registry = read(repo / pointer["registry"])
    root = repo / "kaiwa_skill/courseware"
    rows = []
    for uid, info in registry.items():
        folder = root / uid
        current = read(folder / "current.json") if (folder / "current.json").exists() else None
        owner = read(folder / "owner.json") if (folder / "owner.json").exists() else None
        runs = [read(p) for p in (folder / "runs").glob("*.json")]
        latest = max(runs, key=lambda r: r["created_at"]) if runs else None
        status = "outline_only"
        if current:
            status = "finalized"
        if latest and latest["status"] in {"drafting", "paused"}:
            status = latest["status"]
        if owner:
            status = "owned"
        rows.append({"stage_uid": uid, "display_code": info["display_code"], "title": info["title"],
                     "status": status, "current_revision": current["revision"] if current else None,
                     "run": owner["run"] if owner else latest["run"] if latest else None,
                     "next_action": "Đã chốt; chờ feedback. Nâng cấp bằng begin --from-current khi được giao." if status == "finalized"
                                    else latest.get("next_action") if latest else None})
    summary = dict(Counter(row["status"] for row in rows))
    output = {"generated_at": datetime.now(timezone.utc).isoformat(), "derived_not_authoritative": True,
              "roadmap_version": pointer["version"], "counts": summary, "stages": rows}
    root.mkdir(parents=True, exist_ok=True)
    temporary = root / "STATUS.json.tmp"
    temporary.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(root / "STATUS.json")
    lines = ["# Trạng thái biên soạn Kaiwa", "Bản dẫn xuất; run/checkpoint từng chặng là nguồn chuẩn.",
             ", ".join(key + ": " + str(value) for key, value in summary.items())]
    for row in rows:
        if row["status"] != "outline_only":
            lines.extend(["## " + row["display_code"] + " — " + row["title"],
                          "Status: " + row["status"] + "; revision: " + str(row["current_revision"]),
                          "UID: " + row["stage_uid"] + "; run: " + str(row["run"]),
                          "Tiếp theo: " + str(row["next_action"])])
    (root / "STATUS.md").write_text("\n\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
