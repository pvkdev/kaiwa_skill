"""Check lesson/vocabulary joins and captured material locally; optionally require a crawl stage."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from build_catalog import SUFFIXES

ROOT = Path(__file__).resolve().parents[1]


def check(ok, message):
    if not ok:
        raise ValueError(message)


def coverage():
    lessons = json.loads((ROOT / "catalog/sources.json").read_bytes())["lessons"]
    check(set(lessons) == {f"{n:02}" for n in range(1, 51)}, "Expected lessons 01–50 exactly")
    files = {}
    for path in (ROOT / "materials/vocabulary").glob("*/*-Bài-*.md"):
        text = path.read_text(encoding="utf-8-sig")
        m = re.match(r"# Bài (\d+): Bài (\d+)\s*\n", text)
        check(m, f"Review vocabulary heading in {path}")
        unit, n = map(int, m.groups())
        check(n not in files and 1 <= n <= 50 and path.name == f"{unit:02}-Bài-{n}.md",
              f"Duplicate or inconsistent vocabulary file: {path}")
        count = re.search(r"· (\d+) từ", text)
        rows = [int(i) for i in re.findall(r"(?m)^\|\s*(\d+)\s*\|", text)]
        check(count and rows == list(range(1, int(count[1])+1)) and rows, f"Review word count: {path}")
        files[n] = (path, len(rows))
    evidence = ROOT / "reports/crawl-coverage.json"
    crawl = json.loads(evidence.read_bytes()) if evidence.exists() else {}
    report = []
    for n in range(1, 51):
        lesson = lessons[f"{n:02}"]
        check(lesson["lesson_number"] == n and set(lesson["pages"]) == set(SUFFIXES), f"Bad catalog: {n}")
        check(n in files and files[n][0].parent.name == lesson["target_level"], f"Missing vocabulary: {n}")
        path, words = files[n]
        states = {}
        b_expected, b_received = None, 0
        for family in SUFFIXES.keys() - {"lesson"}:
            item = crawl.get(str(n), {}).get(family, {})
            state = item.get("state", "pending")
            if state == "captured":
                blob = ROOT / item["snapshot"]
                if not blob.is_file():
                    state = "snapshot_missing"
                else:
                    data = json.loads(blob.read_bytes())
                    digest = hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
                    check(data["lesson"] == n and data["family"] == family and blob.stem == digest
                          and data["url"] == item["url"] and data["sections"], f"Snapshot mismatch: {blob}")
                    if family == "grammar":
                        check(data["points"] == item["points"] and len(data["drill_ids"]) == item["drill_count"],
                              f"Grammar evidence mismatch: {blob}")
                        b_expected = len(data["drill_ids"])
                        answers_path = blob.with_suffix(".answers.json")
                        if answers_path.exists():
                            answers = json.loads(answers_path.read_bytes())
                            check(set(answers) <= set(data["drill_ids"]), f"Foreign answer ID: {answers_path}")
                            b_received = sum(bool(x.get("answer") and x["answer"].strip()) for x in answers.values())
            states[family] = state
        report.append({"lesson":n, "vocab":path.relative_to(ROOT).as_posix(), "words":words,
                       "b_expected":b_expected, "b_received":b_received, "states":states})
    return report


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--require", choices=["grammar", "b-answers", "all"])
    cli.add_argument("--lesson", type=int, choices=range(1, 51))
    args = cli.parse_args()
    report = coverage()
    print(f"{len(report)} vocabulary files, {sum(r['words'] for r in report)} entries")
    print(f"Renshuu B answers in current snapshots: {sum(r['b_received'] for r in report)}/"
          f"{sum(r['b_expected'] or 0 for r in report)} observed IDs")
    for family in sorted(report[0]["states"]):
        print(f"{family}: {sum(r['states'][family]=='captured' for r in report)}/50 captured")
    if args.lesson:
        print(json.dumps(report[args.lesson-1], ensure_ascii=False, indent=2))
    if args.require:
        missing = [r["lesson"] for r in report if any(state != "captured" for f,state in r["states"].items()
                   if args.require in ("all",f))]
        if args.require == "b-answers":
            missing = [r["lesson"] for r in report if r["b_expected"] != r["b_received"]]
        if missing:
            raise SystemExit(f"Missing captures in lessons {missing}")

