"""Build a standalone reading preview from reviewed V13 pilot exports."""
from collections import defaultdict
from html import escape

from pilot import PLAN, V, digest, inputs


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


def render():
    root = PLAN / "v13/pilot"
    sections, links = [], defaultdict(list)
    paths = sorted(root.glob("*/status.json"), key=lambda path: ("STH".index(path.parent.name[0]), path.parent.name))
    for path in paths:
        folder = path.parent
        code = folder.name
        ctx = inputs(code)
        reviewed = V["read"](path)
        expected = {**ctx["pins"], "draft": digest(folder / "draft.json"), "output": digest(folder / "shadowing.json")}
        if reviewed.get("state") != "reviewed" or any(reviewed.get(k) != v for k, v in expected.items()):
            raise ValueError(f"{code}: review is stale")
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
        raise ValueError("No reviewed pilots")
    navigation = "".join(f'<h2>{escape(level)}</h2><p>{" ".join(entries)}</p>' for level, entries in links.items())
    html = ('<!doctype html><html lang="vi"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>Shadowing V13</title><style>{STYLE}</style></head><body><h1 id="muc-luc">Shadowing V13</h1>'
            f'<nav aria-label="Chọn chặng">{navigation}</nav><main>{"".join(sections)}</main></body></html>')
    (root / "PREVIEW.html").write_text(html, encoding="utf8", newline="\n")


if __name__ == "__main__":
    render()
