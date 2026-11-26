"""Join reviewed keys to the exact observed quick checks, by lesson and source question ID."""
import json
from pathlib import Path
from tempfile import NamedTemporaryFile

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "authored/quick-checks"


def read(path):
    return json.loads(path.read_bytes())


def save(path, data):
    with NamedTemporaryFile(dir=path.parent, delete=False) as file:
        file.write((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode())
        temp = Path(file.name)
    temp.replace(path)


def keyed(rows):
    result = {}
    for row in rows:
        key = (row["lesson"], row["source_id"])
        if key in result:
            raise ValueError(f"Duplicate review {key}")
        result[key] = row
    return result


def main():
    keys = keyed(row for f in sorted(DIR.glob("keys-*.json")) for row in read(f))
    updates = keyed(read(DIR / "revisions.json"))
    revisions = read(DIR / "source-revisions.json")
    if not updates.keys() <= keys.keys():
        raise ValueError("Revision without reviewed source question")
    output = {}
    expected = set()
    for n in range(1, 51):
        doc = read(ROOT / f"normalized/lesson-{n:02}/grammar.json")
        if revisions[str(n)] != doc["source_snapshot"]:
            raise ValueError(f"Source revision changed: re-review lesson {n}")
        items = []
        for point in doc["points"]:
            for q in point["questions"]:
                k = (n, q["id"])
                if k in expected:
                    raise ValueError(f"Duplicate question {k}")
                expected.add(k)
                row = {**keys[k], **updates.get(k, {})}
                correct = row.get("correct")
                choices = q["choices"]
                ids = [choice["id"] for choice in choices]
                if (correct not in ids or len(set(ids)) != len(ids) or len(choices) < 2
                        or not row.get("explanation_vi", "").strip()):
                    raise ValueError(f"Unresolved key or explanation: {k}")
                items.append({
                    "id": f"minna.l{n:02}.quiz.{q['id']}", "kind": "manualQnA",
                    "source_id": q["id"], "grammar_refs": [point["id"]],
                    "prompt_ja": row.get("prompt_override", q["prompt"]),
                    "instruction_vi": "Chọn một đáp án.", "choices": choices,
                    "correct": correct, "explanation_vi": row["explanation_vi"],
                    "provenance": {"question": "ai_adapted" if row.get("prompt_override") else "source",
                                   "answer": "ai_editorial", "explanation": "ai_editorial",
                                   "official_key": "not_verified"},
                })
        output[n] = {"lesson": n, "source_snapshot": doc["source_snapshot"],
                     "source_url": doc["source_url"], "items": items}
    if expected != keys.keys():
        raise ValueError("Keys and observed questions do not cover exactly the same IDs")
    for n, doc in output.items():
        save(DIR / f"lesson-{n:02}.json", doc)
    print(f"{len(expected)} keyed questions for {len(output)} lessons")


if __name__ == "__main__":
    main()
