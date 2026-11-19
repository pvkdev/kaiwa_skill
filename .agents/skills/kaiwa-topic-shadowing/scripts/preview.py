"""Build a standalone reading preview from reviewed V13 exports."""
import argparse
from collections import defaultdict
from html import escape
from pathlib import Path

from pilot import PLAN, V, build, inputs


STYLE = """
:root{color-scheme:light dark;font-family:system-ui,sans-serif;line-height:1.55}
body{margin:0 auto;max-width:48rem;padding:1rem clamp(.65rem,3vw,1.5rem) 3rem}
nav{border-block:1px solid #8886;padding:.65rem 0}
nav p{display:flex;gap:.4rem 1rem;flex-wrap:wrap}
a{color:LinkText;text-underline-offset:.16em}
section{margin:3rem 0}article{border-bottom:1px solid #8885;padding:.65rem 0}
h3{margin:1.6rem 0 .35rem}p{margin:.2rem 0}p[lang=ja]{font-size:1.18rem}
small{color:GrayText}
"""


def render(target="pilot", codes=None, output=None):
    root = PLAN / "v13" / target
    sections, links = [], defaultdict(list)
    course = V["read"](PLAN / "v11/learner.json")
    paths = [root / s["code"] / "status.json" for s in course["stages"]
             if s.get("stage_kind") == "topic" and (codes is None or s["code"] in codes)
             and (root / s["code"] / "status.json").exists()]
    for path in paths:
        folder = path.parent
        code = folder.name
        ctx = inputs(code)
        build(code, "checkpoint", target=target)
        draft = V["read"](folder / "draft.json")
        node = V["read"](folder / "shadowing.json")
        title = escape(ctx["title"])
        links[ctx["level"]].append(f'<a href="#{code}">{code} · {title}</a>')
        sections.append(f'<section id="{code}"><h2>{code} · {title}</h2><p>{len(node["items"])} câu</p>')
        previous = None
        for number, (row, item) in enumerate(zip(draft["items"], node["items"], strict=True), start=1):
            if row["id"] != item["id"]:
                raise ValueError(f"{code}: draft and export are out of order")
            if row["group"] != previous:
                sections.append(f'<h3>{escape(draft["groups"][row["group"]])}</h3>')
                previous = row["group"]
            turn, = item["turns"]
            speaker, = item["speakers"]
            voice = {"male": "Nam", "female": "Nữ"}[speaker["gender"]]
            sections.append(f'<article><small>{number}. {escape(speaker["role_vi"])} · Giọng {voice.lower()}</small>'
                            f'<p lang="ja">{escape(turn["ja"])}</p><p>{escape(turn["vi"])}</p></article>')
        sections.append('<p><a href="#muc-luc">Về mục lục</a></p></section>')
    if not sections:
        raise ValueError("No reviewed exports")
    navigation = "".join(f'<h2>{escape(level)}</h2><p>{" ".join(entries)}</p>' for level, entries in links.items())
    html = ('<!doctype html><html lang="vi"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Shadowing V13</title><style>{STYLE}</style></head><body><h1 id="muc-luc">Shadowing V13</h1>'
            f'<nav aria-label="Chọn chặng">{navigation}</nav><main>{"".join(sections)}</main></body></html>')
    destination = Path(output) if output else root / "PREVIEW.html"
    destination.write_text(html, encoding="utf8", newline="\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=["pilot", "stages"], default="pilot")
    parser.add_argument("--codes", nargs="+", help="Only include these topic codes")
    parser.add_argument("--output", type=Path, help="Separate preview destination")
    args = parser.parse_args()
    render(args.target, args.codes, args.output)
