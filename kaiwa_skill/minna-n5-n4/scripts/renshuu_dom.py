"""Small, dependency-free reader for the saved VNJPClub section HTML."""

from html.parser import HTMLParser
import json


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


def reviewed_snapshots(root):
    ledger = json.loads((root/"reports/crawl-coverage.json").read_bytes())
    checked = json.loads((root/"authored/quick-checks/source-revisions.json").read_bytes())
    paths = {}
    for lesson in range(1,51):
        entry = ledger[str(lesson)]["grammar"]
        if entry["state"] != "captured" or entry["snapshot"] != checked[str(lesson)]:
            raise ValueError(f"Review B exercises and quick checks against current grammar snapshot for lesson {lesson}")
        paths[lesson] = root/entry["snapshot"]
    return paths


class Node:
    def __init__(self, tag="", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []

    def all(self, cls):
        found = [self] if cls in self.attrs.get("class", "").split() else []
        for child in self.children:
            if isinstance(child, Node):
                found.extend(child.all(cls))
        return found

    def text(self, skip_rt=True):
        if skip_rt and self.tag == "rt":
            return ""
        return "".join(child.text(skip_rt) if isinstance(child, Node) else child for child in self.children).strip()


class Reader(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for idx in range(len(self.stack) - 1, 0, -1):
            if self.stack[idx].tag == tag:
                self.stack = self.stack[:idx]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def parse(html):
    reader = Reader()
    reader.feed(html)
    return reader.root
