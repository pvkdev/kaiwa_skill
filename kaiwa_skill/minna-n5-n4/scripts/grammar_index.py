"""Build an ordered 50-lesson syllabus from captured VNJPClub grammar headings."""
from html.parser import HTMLParser
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class Heading(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.reading = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if "mg-point-t" in dict(attrs).get("class", "").split():
            self.active = True
        if tag in ("rt", "rp"):
            self.reading = True

    def handle_endtag(self, tag):
        if tag in ("h2", "h3", "h4"):
            self.active = False
        if tag in ("rt", "rp"):
            self.reading = False

    def handle_data(self, value):
        if self.active and not self.reading:
            self.parts.append(value)


def build():
    ledger = json.loads((ROOT / "reports/crawl-coverage.json").read_bytes())
    result = []
    for n in range(1, 51):
        row = ledger[str(n)].get("grammar", {})
        if row.get("state") != "captured":
            raise ValueError(f"Lesson {n} needs capture")
        snapshot = json.loads((ROOT / row["snapshot"]).read_bytes())
        sections = {s["id"]:s["html"] for s in snapshot["sections"]}
        points = []
        for p in snapshot["points"]:
            parser = Heading()
            parser.feed(sections[p["id"]])
            title = "".join(parser.parts).strip()
            if not title:
                raise ValueError(f"Missing heading: {n}/{p['id']}")
            points.append({"id":p["id"], "title":title})
        result.append({"lesson":n, "url":row["url"], "points":points, "drills":row["drill_count"]})
    path = ROOT / "catalog/grammar-points.json"
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as fp:
        fp.write((json.dumps(result, ensure_ascii=False, indent=2)+"\n").encode())
        tmp = Path(fp.name)
    tmp.replace(path)
    print(f"{len(result)} lessons, {sum(len(r['points']) for r in result)} grammar entries")


if __name__ == "__main__":
    build()

