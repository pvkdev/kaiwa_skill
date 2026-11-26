"""Normalize grammar examples and in-page questions from the verified local snapshots."""
import json
import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


def text_of(node):
    if node is None:
        return ""
    return re.sub(r"\s+", " ", node.get_text()).strip()


def extract(n, entry, index):
    raw = json.loads((ROOT / entry["snapshot"]).read_bytes())
    by_id = {s["id"]:s["html"] for s in raw["sections"]}
    points = []
    for p in index["points"]:
        doc = BeautifulSoup(by_id[p["id"]], "html.parser")
        for rt in doc.select("rt,rp"):
            rt.decompose()
        examples = []
        for line in doc.select(".mg-examples .mg-line"):
            jp, vi = text_of(line.select_one(".mg-ja")), text_of(line.select_one(".mg-vi"))
            if not jp or not vi:
                raise ValueError(f"Incomplete example in lesson {n}, {p['id']}")
            btn = line.select_one(".mg-say")
            media = {k:v for k,v in (btn.attrs.items() if btn else [])
                     if k in {"data-track","data-t","data-tts-key","data-tts-ready"}}
            examples.append({"ja":jp, "vi":vi, "media":media})
        questions = []
        for q in doc.select(".mg-q"):
            opts = [{"id":str(b["data-option"]), "text":text_of(b.select_one(".mg-opt-t"))}
                    for b in q.select("[data-option]")]
            questions.append({"id":q["data-q"], "prompt":text_of(q.select_one(".mg-q-text")), "choices":opts})
        points.append({**p, "formula":[text_of(x) for x in doc.select(".mg-formula-line")],
                       "meaning":text_of(doc.select_one(".mg-meaning")),
                       "usage":[text_of(x) for x in doc.select(".mg-usage li")],
                       "examples":examples,"questions":questions})
    return {"lesson":n, "source_snapshot":entry["snapshot"], "source_url":entry["url"],
            "media_context":raw["media_context"], "points":points}


if __name__ == "__main__":
    ledger=json.loads((ROOT/"reports/crawl-coverage.json").read_bytes())
    index=json.loads((ROOT/"catalog/grammar-points.json").read_bytes())
    count = 0
    for entry in index:
        n=entry["lesson"]
        out=ROOT/f"normalized/lesson-{n:02}/grammar.json"
        out.parent.mkdir(parents=True,exist_ok=True)
        data=extract(n,ledger[str(n)]["grammar"],entry)
        out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
        count+=sum(len(p["questions"]) for p in data["points"])
    print(f"{len(index)} lessons; {count} source quick checks")
