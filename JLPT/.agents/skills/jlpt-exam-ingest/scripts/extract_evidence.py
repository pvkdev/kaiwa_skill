"""Split a saved VNJPClub result into readable source fragments; Python 3.10+."""
import argparse
import base64
import hashlib
import json
import os
import tempfile
from html import escape
from html.parser import HTMLParser
from pathlib import Path


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_bytes() == data:
        return
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        stream.write(data)
    os.replace(stream.name, path)


class Capture(HTMLParser):
    """Retain ordered source material, including questionless blocks and tables."""
    void = set("area base br col embed hr img input link meta param source track wbr".split())
    hidden = {"script", "style", "noscript", "svg", "iframe", "template"}
    keep = set("h2 h3 h4 h5 section div p span ruby rt rp u b strong i em del s sub sup small ol ul li table caption thead tbody tfoot tr th td br hr img a label audio source".split())
    attributes = set("class id lang rowspan colspan scope alt data-start data-end data-key data-vi".split())

    def __init__(self, folder):
        super().__init__(convert_charrefs=True)
        self.folder = folder
        self.stack = []
        self.current = None
        self.sections = []
        self.chunks = []
        self.images = {}
        self.missing_images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = (attrs.get("class") or "").split()
        if self.current is None:
            kind = None
            if "section-head" in classes:
                kind = "section"
            elif "mondai-block" in classes:
                kind = "mondai"
            elif attrs.get("id") == "jlpt-singlefile-notes":
                kind = "notes"
            if not kind:
                return
            self.current = {"kind": kind, "questionIds": []}
            self.chunks = []
        hidden = tag in self.hidden or bool(self.stack and self.stack[-1][1])
        visible = not hidden and tag in self.keep
        if visible:
            keep = {k: v for k, v in attrs.items() if k in self.attributes and v is not None}
            if tag == "a" and (attrs.get("href") or "").startswith("#"):
                keep["href"] = attrs["href"]
            if tag == "img":
                self.collect_image(attrs.get("src") or "", keep)
            if "q-item" in classes:
                self.current["questionIds"].append(attrs.get("id"))
            serial = "".join(f' {k}="{escape(v, quote=True)}"' for k, v in keep.items())
            self.chunks.append(f"<{tag}{serial}>")
        if tag not in self.void:
            self.stack.append((tag, hidden, visible))

    def collect_image(self, src, attrs):
        header, comma, payload = src.partition(",")
        formats = {"data:image/jpeg;base64": "jpg", "data:image/png;base64": "png",
                   "data:image/webp;base64": "webp", "data:image/gif;base64": "gif"}
        extension = formats.get(header.lower())
        if extension and comma:
            try:
                content = base64.b64decode("".join(payload.split()), validate=True)
            except ValueError:
                content = b""
            if content:
                digest = hashlib.sha256(content).hexdigest()
                name = f"images/{digest}.{extension}"
                save(self.folder / name, content)
                self.images[name] = len(content)
                attrs["src"] = name
                return
        attrs["data-image-status"] = "inspect-original"
        self.missing_images.append(len(self.sections) + 1)

    def handle_data(self, text):
        if self.current and self.stack and not self.stack[-1][1]:
            self.chunks.append(escape(text, quote=False))

    def handle_endtag(self, tag):
        if not self.current or not any(item[0] == tag for item in self.stack):
            return
        while self.stack:
            opened, _, visible = self.stack.pop()
            if visible:
                self.chunks.append(f"</{opened}>")
            if opened == tag:
                break
        if not self.stack:
            name = f"{len(self.sections) + 1:03}-{self.current['kind']}.html"
            save(self.folder / name, ('<meta charset="utf-8">\n' + "".join(self.chunks)).encode())
            self.sections.append({**self.current, "file": name})
            self.current = None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture", type=Path)
    parser.add_argument("--out", type=Path, default=Path("work/evidence"),
                        help="Parent of the per-SHA256 source directory")
    args = parser.parse_args()
    source = args.capture.read_bytes()
    digest = hashlib.sha256(source).hexdigest()
    folder = args.out / digest
    capture = Capture(folder)
    capture.feed(source.decode("utf-8-sig"))
    capture.close()
    if capture.current or not any(s["questionIds"] for s in capture.sections):
        parser.exit(1, "Capture incomplete or unrecognized; inspect the original HTML.\n")
    index = {"captureSha256": digest, "sourceFilename": args.capture.name, "sections": capture.sections,
             "imageBytes": capture.images, "unresolvedImageFragments": capture.missing_images}
    save(folder / "index.json", (json.dumps(index, ensure_ascii=False, indent=2) + "\n").encode())
    print(folder / "index.json")


if __name__ == "__main__":
    main()

