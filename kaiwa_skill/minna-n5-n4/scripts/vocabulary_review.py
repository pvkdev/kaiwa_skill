"""Find vocabulary already taught and later Minna vocabulary used in authored Japanese."""
import argparse
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path
import re

from sudachipy import dictionary

from course_coverage import coverage

ROOT = Path(__file__).resolve().parents[1]
LEXICAL = {"名詞","動詞","形容詞","形状詞","副詞"}
SUFFIX = {"為る","成る","居る","有る","下さる","物","事","人","方"}
JP = re.compile(r"[ぁ-んァ-ヺ一-鿿]")


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--lesson", type=int, choices=range(1,51))
    args = cli.parse_args()
    tokenizer = dictionary.Dictionary(dict="small").create()

    @lru_cache(maxsize=24000)
    def lemmas(text):
        return tuple(w.normalized_form() for w in tokenizer.tokenize(text)
                     if w.part_of_speech()[0] in LEXICAL and w.part_of_speech()[1] not in {"数詞","固有名詞"}
                     and JP.search(w.surface()) and w.normalized_form() not in SUFFIX)

    by_lemma = defaultdict(list)
    rows = coverage()
    for row in rows:
        for line in (ROOT/row["vocab"]).read_text(encoding="utf-8-sig").splitlines():
            fields = [s.strip() for s in line.strip("|").split("|")]
            if len(fields)!=5 or not fields[0].isdigit():
                continue
            term = re.sub(r"[\[［「].*?[\]］」]|[（(].*?[)）]", "", fields[1])
            keys = lemmas(term)
            # A word embedded in a whole example/phrase is not evidence it has been taught independently.
            if len(keys) == 1:
                by_lemma[keys[0]].append((row["lesson"],int(fields[0]),fields[1],fields[4]))
    summary = []
    for row in rows:
        n = row["lesson"]
        if args.lesson and n!=args.lesson:
            continue
        future = defaultdict(set)
        matched, total = set(),0
        for bank in ("quick-checks","renshuu","renshuu-drills"):
            file = ROOT/f"authored/{bank}/lesson-{n:02}.json"
            if not file.is_file():
                continue
            for item in json.loads(file.read_bytes())["items"]:
                total += 1
                lines = [item["prompt_ja"],*[c["text"] for c in item.get("choices",[])]]
                if item["kind"]=="manualFillInBlank":
                    lines.append(item["correct"])
                for key in {k for s in lines for k in lemmas(s)}:
                    entries = by_lemma.get(key)
                    if not entries:
                        continue
                    first = entries[0]
                    if first[0]>n:
                        future[first].add(item["id"])
                    if any(entry[0]==n for entry in entries):
                        matched.add(key)
        summary.append({"lesson":n,"vocabulary_file":row["vocab"],"exercise_count":total,
                        "matched_current_lesson_lemmas":sorted(matched),
                        "later_vocabulary_to_check":[{"first_lesson":first,"row":i,"entry":v,"gloss":gloss,
                            "exercise_ids":sorted(ids)} for (first,i,v,gloss),ids in sorted(future.items())]})
    if args.lesson:
        print(json.dumps(summary[0],ensure_ascii=False,indent=2))
    else:
        path = ROOT/"reports/vocabulary-review.json"
        path.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(f"Reviewed vocabulary against {sum(r['exercise_count'] for r in summary)} exercise prompts and option sets")


if __name__ == "__main__":
    main()
