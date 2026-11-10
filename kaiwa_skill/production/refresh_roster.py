"""Coordinator-only snapshot. Reads ingest state; never launches or verifies work."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def ranges(numbers):
    groups = []
    for value in numbers:
        if groups and value == groups[-1][-1] + 1:
            groups[-1].append(value)
        else:
            groups.append([value])
    return ",".join(str(g[0]) if len(g) == 1 else f"{g[0]}-{g[-1]}" for g in groups)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assign", nargs=2, metavar=("BOOK_ID", "AGENT_ID"))
    parser.add_argument("--worker-state", nargs=2, metavar=("BOOK_ID", "STATE"))
    parser.add_argument("--run-status", choices=("active", "handoff", "complete"))
    args = parser.parse_args()
    production = Path(__file__).resolve().parent
    root = production.parent
    spec = importlib.util.spec_from_file_location("ingest", root / "tools" / "ingest.py")
    ingest = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ingest)
    roster = ingest.read_json(production / "roster.json")
    if args.assign:
        row = next(b for b in roster["books"] if b["book_id"] == args.assign[0])
        row["agent_id"] = args.assign[1]
        row["worker_state"] = "running"
    if args.worker_state:
        row = next(b for b in roster["books"] if b["book_id"] == args.worker_state[0])
        row["worker_state"] = args.worker_state[1]
    snapshot = ingest.status_all(root)
    for row in roster["books"]:
        current = next(b for b in snapshot["books"] if b["id"] == row["book_id"])
        row["counts"] = current.get("counts", {})
        row["issue_count"] = current.get("issue_count", 0)
        row["build_current"] = current.get("build_current", False)
        row["claim_owner"] = (current.get("claim") or {}).get("owner")
        row["status_error"] = current.get("error")
        if (root / "corpus" / row["book_id"] / "manifest.json").exists():
            directory, manifest, _ = ingest.load_book(root, row["book_id"])
            detail = ingest.status(directory, manifest)
            row["pending_pages"] = ranges([int(p) for p, state in detail["pages"].items() if state["status"] != "verified"])
        else:
            row["pending_pages"] = f"1-{row['total_pages']}"
        if row["coordinator_acceptance"] == "accepted" and row["counts"].get("verified") == row["total_pages"] and row["build_current"] and not row["issue_count"]:
            row["status"] = "accepted"
        elif row.get("worker_state") == "running":
            row["status"] = "in_progress"
        elif row["issue_count"] or row["status_error"]:
            row["status"] = "needs_review"
        elif row["counts"].get("verified") == row["total_pages"]:
            row["status"] = "awaiting_coordinator_audit"
        elif row["counts"].get("verified", 0):
            row["status"] = "partial"
        else:
            row["status"] = "queued"
    roster["updated_at"] = ingest.now()
    roster["counts"] = snapshot["counts"]
    roster["issue_count"] = snapshot["issue_count"]
    if args.run_status:
        roster["run_status"] = args.run_status
    ingest.atomic_json(production / "roster.json", roster)
    lines = ["PRODUCTION ROSTER — toàn bộ PDF", f"Snapshot UTC: {roster['updated_at']}",
             "Đường dẫn nguồn tương đối từ kaiwa_skill/.",
             "Coordinator: gpt-6-astra/high; worker: gpt-6-sol/high; tối đa 2 PDF đồng thời.",
             f"{roster['total_books']} PDF; {snapshot['total_pages']} trang; {json.dumps(snapshot['counts'], ensure_ascii=False)}.",
             "Mọi số đếm lấy từ ingest.status_all và kiểm hash file thực tế.",
             "Roster là trạng thái bền vững; không phải daemon. Không có tiến trình bảo đảm tiếp tục khi agents dừng.", ""]
    for row in roster["books"]:
        lines.extend([f"{row['queue_order']:02}. {row['book_id']} | {row['total_pages']} trang | {row['status']}",
                      f"    Nguồn: {row['source']}",
                      f"    Worker: {row['worker_id']}; {row['model']}/{row['reasoning_effort']}; agent_id: {row['agent_id'] or 'chưa cấp'}",
                      f"    Status thực: {json.dumps(row['counts'], ensure_ascii=False)}; issue: {row['issue_count']}; build_current: {row['build_current']}",
                      f"    Chưa verified: {row['pending_pages'] or 'không'}; nghiệm thu coordinator: {row['coordinator_acceptance']}"])
    ingest.atomic_bytes(production / "ROSTER.txt", ("\n".join(lines) + "\n").encode("utf-8"))
    print(json.dumps({"total_pages": snapshot["total_pages"], "counts": snapshot["counts"], "issue_count": snapshot["issue_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
