"""Capture public rendered lesson sections and their source IDs for Minna 1–50."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import urlsplit
from playwright.sync_api import sync_playwright, Error as BrowserError

from build_catalog import SUFFIXES

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://www.vnjpclub.com"
INDEXES = ["ngu-phap-minna-so-cap-1-n5", "ngu-phap-minna-so-cap-2-n4"]
SECTIONS = {
    "grammar": "#mg-panel-grammar .mg-point, #mg-panel-grammar .mg-q, #mg-panel-practice .mg-part",
    "shadowing": "#mr-bunkei, [id^=mr-a]",
    "conversation": "[id^=mk-c], #mk-kaiwa",
    "listening": "#ml-panel-practice",
    "short_reading": ".mx-sec--read",
    "long_reading": "#mtp-panel-read, #mtp-panel-questions",
    "assessment": ".mt-sec[data-section]",
}
CAPTURE = r"""(family) => {
 const sel = SELECTOR;
 const top = [...document.querySelectorAll(sel)].filter(e=>!e.parentElement.closest(sel));
 const sections = [];
 for (const e of top) {
   let mondai = null;
   if (family === 'shadowing' && !/^(mr-bunkei|mr-a\d+)$/.test(e.id)) continue;
   if (family === 'conversation' && !/^(mk-kaiwa|mk-c\d+)$/.test(e.id)) continue;
   if (family === 'assessment') {
     const heading = e.querySelector('h2,h3,h4,.mt-sec-h');
     const n = (heading?.textContent || '').match(/(?:mondai|問題|もんだい|mônđai)\s*([0-9０-９]+)/i);
     mondai = n ? Number(n[1].normalize('NFKC')) : null;
     if (!mondai || mondai > 6) continue;
   }
   const c = e.cloneNode(true);
   c.querySelectorAll('script,style,iframe,ins,form input,template').forEach(x=>x.remove());
   for (const x of [c,...c.querySelectorAll('*')]) {
     for (const a of [...x.attributes]) if (/^(on|style$|nonce$)/i.test(a.name)) x.removeAttribute(a.name);
   }
   sections.push({id:e.id || e.dataset.mgItem || e.querySelector('[data-mg-item]')?.dataset.mgItem || null,
                  ...(mondai ? {mondai} : {}), html:c.outerHTML});
 }
 const points = [...document.querySelectorAll('#mg-panel-grammar .mg-point')].map(e=>({
   id:e.id,title:e.querySelector('.mg-point-t')?.textContent.trim()
 }));
 const attrs = {};
 for (const e of document.querySelectorAll('[id^=vnjp-]')) {
   for (const a of e.attributes) if (/^data-.*(tracks|tts-base)$/.test(a.name)) attrs[a.name]=a.value;
 }
 return {sections,points,media_context:attrs,
   drill_ids:[...document.querySelectorAll('#mg-panel-practice [data-mg-drill]')].map(e=>e.dataset.mgDrill),
   declared_drills:document.querySelector('#vnjp-mg')?.getAttribute('data-mg-drills'),
   grammar_lesson:document.querySelector('#vnjp-mg')?.getAttribute('data-mg-lesson')};
}"""


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode()
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as fp:
        fp.write(payload)
        tmp = Path(fp.name)
    tmp.replace(path)


class AccessStopped(Exception):
    pass


def visit(page, url):
    page.wait_for_timeout(2000)
    response = page.goto(url, wait_until="domcontentloaded", timeout=45000)
    title = page.title().casefold()
    if (response and response.status in (401, 403, 429)) or any(
            x in title for x in ("just a moment", "xác minh", "xác nhận truy cập", "one moment")):
        raise AccessStopped(f"Access check or rate limit at {url}")
    if not response or response.status != 200 or page.url.rstrip("/") != url.rstrip("/"):
        raise ValueError(f"Review response for {url}: {response.status if response else None}, {page.url}")


def links(page):
    return page.locator("a[href]").evaluate_all("(xs)=>xs.map(a=>a.href.split('#')[0].split('?')[0])")


def indexes(page):
    found = {}
    for slug in INDEXES:
        url = f"{DOMAIN}/{slug}/"
        visit(page, url)
        page.wait_for_selector('a[href*="-ngu-phap.html"]', state="attached")
        for href in links(page):
            match = re.fullmatch(re.escape(DOMAIN) + r"/minna-no-nihongo/bai-(\d+)-ngu-phap\.html", href)
            if match:
                n = int(match[1])
                if n in range(1, 51):
                    found[n] = href
    return found


def lesson_links(page, number, url):
    visit(page, url)
    page.wait_for_selector("#vnjp-mlh a[href]", state="attached", timeout=12000)
    hrefs = set(page.locator("#vnjp-mlh a[href]").evaluate_all("(xs)=>xs.map(a=>a.href.split('#')[0])"))
    pages = {}
    for family in SECTIONS:
        expected = f"/minna-no-nihongo/bai-{number}{SUFFIXES[family]}.html"
        for href in hrefs:
            if href.startswith(DOMAIN + "/") and urlsplit(href).path == expected:
                pages[family] = href
    return pages


def capture(page, number, family, url):
    visit(page, url)
    page.wait_for_selector(SECTIONS[family], state="attached", timeout=12000)
    data = page.evaluate(CAPTURE.replace("SELECTOR", json.dumps(SECTIONS[family])), family)
    if not data["sections"]:
        raise ValueError("No scoped sections in the rendered page")
    ids = [section["id"] for section in data["sections"]]
    if family == "long_reading" and set(ids) != {"mtp-panel-read", "mtp-panel-questions"}:
        raise ValueError("Missing passage or questions panel")
    if family == "conversation" and ("mk-kaiwa" not in ids or not any(re.fullmatch(r"mk-c\d+", i or "") for i in ids)):
        raise ValueError("Missing Kaiwa or Renshuu C")
    if family == "shadowing" and ("mr-bunkei" not in ids or not any(re.fullmatch(r"mr-a\d+", i or "") for i in ids)):
        raise ValueError("Missing bunkei or Renshuu A")
    if family == "assessment" and sorted(s["mondai"] for s in data["sections"]) != list(range(1, 7)):
        raise ValueError("Review Mondai 1–6 sections in this lesson")
    if family == "grammar":
        ids = [p["id"] for p in data["points"]]
        drills = data["drill_ids"]
        if (str(number) != data["grammar_lesson"] or not ids or len(set(ids)) != len(ids)
                or not all(p["id"] and p["title"] for p in data["points"])
                or len(set(drills)) != len(drills) or not all(drills)
                or data["declared_drills"] is None or int(data["declared_drills"]) != len(drills)):
            raise ValueError("Grammar headings or drill IDs need layout review")
    snapshot = {"lesson": number, "family": family, "url": url, **data}
    digest = hashlib.sha256(json.dumps(snapshot, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    dest = ROOT / f"sources/lesson-{number:02}/{family}/{digest}.json"
    if not dest.exists():
        write_json(dest, snapshot)
    row = {"url": url, "state": "captured", "snapshot": dest.relative_to(ROOT).as_posix(),
           "sections": len(data["sections"]), "time_utc": datetime.now(timezone.utc).isoformat()}
    if family == "grammar":
        row.update(points=data["points"], drill_count=len(data["drill_ids"]))
    return row


def main(args):
    selected = args.family or ["grammar"]
    families = list(SECTIONS) if "all" in selected else list(dict.fromkeys(selected))
    report = ROOT / "reports/crawl-coverage.json"
    ledger = json.loads(report.read_bytes()) if report.exists() else {}
    for n in range(1, 51):
        ledger.setdefault(str(n), {})
    write_json(report, ledger)
    with sync_playwright() as engine:
        browser = engine.chromium.launch(channel=args.browser)
        page = browser.new_page()
        grammar = indexes(page) if "grammar" in families else {}
        for n in range(args.start, args.end+1):
            row = ledger[str(n)]
            hub = None
            for family in families:
                old = row.get(family, {})
                if old.get("state") == "captured" and (ROOT / old["snapshot"]).is_file() and not args.refresh:
                    continue
                url = None
                try:
                    if family == "grammar":
                        url = grammar.get(n)
                    else:
                        if hub is None:
                            hub = lesson_links(page, n, f"{DOMAIN}/minna-no-nihongo/bai-{n}.html")
                        url = hub.get(family)
                    if not url:
                        raise ValueError("Missing source link; inspect the lesson hub for a variant")
                    row[family] = capture(page, n, family, url)
                except (ValueError, BrowserError, AccessStopped) as err:
                    row[family] = {**old, "state":"needs_review", "attempted_url":url,
                                   "reason":str(err).splitlines()[0]}
                    if isinstance(err, AccessStopped):
                        write_json(report, ledger)
                        raise
                write_json(report, ledger)
                print(n, family, row[family]["state"], flush=True)
        return int(any(ledger[str(n)].get(f, {}).get("state") != "captured"
                       for n in range(args.start, args.end+1) for f in families))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, choices=range(1, 51), default=1)
    parser.add_argument("--end", type=int, choices=range(1, 51), default=50)
    parser.add_argument("--family", choices=["all", *SECTIONS], action="append")
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--browser", default="msedge")
    args = parser.parse_args()
    if args.end < args.start:
        parser.error("--end must be at least --start")
    try:
        sys.exit(main(args))
    except AccessStopped as err:
        sys.exit(str(err))

