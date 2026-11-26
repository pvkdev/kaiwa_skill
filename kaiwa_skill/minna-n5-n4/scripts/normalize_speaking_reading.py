"""Normalize saved speaking and passage sections, retaining clip and sentence provenance."""
import json
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_bytes())


def plain(node):
    return node.get_text().strip() if node else ""


def speech(doc, section_id, family, tracks):
    p = "mr" if family == "shadowing" else "mk"
    turns = []
    for el in doc.select(f".{p}-line"):
        key = el.get("data-track")
        times = el.get("data-t")
        clip = [float(t) for t in times.split(",")] if times else None
        if clip and (len(clip) != 2 or not 0 <= clip[0] < clip[1] or key not in tracks):
            raise ValueError(f"Bad track or time in {section_id} {el.attrs}")
        panel = el.find_parent(class_="mk-vpanel")
        turns.append({"source_id":el[f"data-{p}-line"], "ja":plain(el.select_one(f".{p}-ja")),
                      "vi":plain(el.select_one(f".{p}-vi")), "ruby":json.loads(el.get("data-ruby","null")),
                      "speaker_id":el.get("data-sp"), "speaker":el.get("data-sp-name"),
                      "variant_id":panel.get("id") if panel else None,
                      "media":{"track":key,"source_url":tracks.get(key),"clip_seconds":clip,
                               "tts_key":el.get("data-tts-key")}})
    if not turns or any(not t["ja"] or not t["vi"] for t in turns):
        raise ValueError(f"Missing spoken text or translation in {section_id}")
    row = {"id":section_id,"turns":turns}
    if family == "shadowing":
        row["frames"] = [[{"text":plain(td),"classes":td.get("class",[]),
                           "rowspan":int(td.get("rowspan",1)),"colspan":int(td.get("colspan",1))}
                          for td in tr.select("td,th")] for tr in doc.select(".mr-frame tr")]
    else:
        row["variants"] = [{"id":b["aria-controls"],"label":plain(b.select_one(".mk-vbtn-l")),
                            "cue":plain(b.select_one(".mk-vbtn-cue"))}
                           for b in doc.select(".mk-vbtn[aria-controls]")]
    return row


def passage(doc, family):
    prefix = "mx" if family == "short_reading" else "mtp"
    selector = ".mx-para" if prefix == "mx" else ".mtp-unit"
    result = []
    for unit in doc.select(selector):
        sentences = [{"ja":plain(s),"vi":s.get("data-vi")} for s in unit.select(f".{prefix}-sent")]
        item = {"source_id":unit.get("data-mx-line") or unit.get("data-mtp-block"),
                "ja":plain(unit.select_one(f".{prefix}-ja")),"vi":plain(unit.select_one(f".{prefix}-vi")),
                "sentences":sentences}
        if not item["ja"] or not item["vi"]:
            raise ValueError(f"Missing passage text in {item['source_id']}")
        result.append(item)
    return result


def main():
    ledger = read(ROOT/"reports/crawl-coverage.json")
    counts = {}
    for lesson, record in ledger.items():
        for family in ("shadowing","conversation","short_reading","long_reading"):
            entry = record.get(family,{})
            if entry.get("state") != "captured":
                continue
            data = read(ROOT/entry["snapshot"])
            ctx = data["media_context"]
            spoken = family in ("conversation","shadowing")
            tracks = json.loads(ctx.get("data-mk-tracks" if family == "conversation" else "data-mr-tracks","{}"))
            content = []
            for section in data["sections"]:
                doc = BeautifulSoup(section["html"],"html.parser")
                for tag in doc.select("rt,rp"):
                    tag.decompose()
                if spoken:
                    content.append(speech(doc, section["id"], family, tracks))
                else:
                    content.extend(passage(doc,family))
            if not content:
                raise ValueError(f"No data extracted in lesson {lesson} {family}")
            if family == "conversation":
                content.sort(key=lambda row: row["id"] == "mk-kaiwa")
            out = ROOT/f"normalized/lesson-{int(lesson):02}/{family}.json"
            out.parent.mkdir(parents=True,exist_ok=True)
            output = {"lesson":int(lesson),"family":family,"source_url":entry["url"],
                      "source_snapshot":entry["snapshot"],"media_context":ctx,
                      "sections" if spoken else "paragraphs":content}
            out.write_text(json.dumps(output,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
            size = sum(len(s["turns"]) for s in content) if spoken else len(content)
            counts[family] = counts.get(family,0) + size
    print(counts)


if __name__ == "__main__":
    main()
