"""Read-only V13 checkpoint census in V11 topic order (JSON on stdout)."""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json

from pilot import PLAN, V, build, inputs


def chat_owner(code):
    if code.startswith("S-") or (code.startswith("T-") and 99 <= int(code[2:]) <= 115):
        return "so"
    if code.startswith("H-") or (code.startswith("T-") and int(code[2:]) >= 116):
        return "thuong"
    return "trung"


def audit(scope="all"):
    course = V["read"](PLAN / "v11/learner.json")
    topics = [s for s in course["stages"] if s.get("stage_kind") == "topic"]
    codes = [s["code"] for s in topics]
    if len(codes) != 293 or len(set(codes)) != 293:
        raise ValueError("Expected exactly 293 distinct V11 topic codes")
    rows = []
    for code in codes:
        owner = chat_owner(code)
        if scope != "all" and owner != scope:
            continue
        folder = PLAN / "v13/stages" / code
        row = {"code": code, "owner": owner, "state": "missing", "count": 0}
        if (folder / "status.json").exists():
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    build(code, "checkpoint", target="stages")
                row.update(state="reviewed", count=V["read"](folder / "status.json")["count"])
            except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
                row.update(state="invalid_checkpoint", reason=str(exc))
        else:
            try:
                inputs(code)
                if (folder / "draft.json").exists():
                    with contextlib.redirect_stdout(io.StringIO()):
                        build(code, "check", target="stages")
                    row["state"] = "draft_ready_for_review"
                else:
                    row["reason"] = "No production draft/checkpoint"
            except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
                row.update(state="blocked_or_stale_draft", reason=str(exc))
        rows.append(row)
    expected = set(codes)
    unexpected = sorted(p.name for p in (PLAN / "v13/stages").glob("*")
                        if p.is_dir() and p.name not in expected)
    return {"checked_at_utc": datetime.now(timezone.utc).isoformat(), "scope": scope,
            "expected_total": len(codes), "scope_total": len(rows),
            "reviewed": sum(r["state"] == "reviewed" for r in rows),
            "sentences": sum(r["count"] for r in rows),
            "unexpected_codes": unexpected,
            "remaining_codes": [r["code"] for r in rows if r["state"] != "reviewed"],
            "rows": rows}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scope", choices=["all", "so", "trung", "thuong"], default="all")
    args = parser.parse_args()
    print(json.dumps(audit(args.scope), ensure_ascii=False, indent=2))
