"""Resolve one podcast RSS feed against the original filenames of local JLPT masters."""
import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "contracts/v1"))
from validate_package import check_package
from jlpt_coverage import checklist_issues

AUDIO = {".mp3", ".m4a", ".aac", ".flac", ".wav", ".ogg", ".opus"}
MAX_RSS = 16 * 1024 * 1024
BOOK = "JLPT_AUDIO.xlsx"


def normalize(value):
    return unicodedata.normalize("NFC", value.strip()).casefold()


def https(url):
    parts = urlsplit(url)
    return parts.scheme == "https" and bool(parts.hostname) and not parts.username and not parts.password


def get_workbook_feed(path):
    if not path.exists():
        return ""
    # One generated sheet. Excel may store the editable cell as shared or inline text.
    with zipfile.ZipFile(path) as archive:
        sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        cell = sheet.find(".//{*}c[@r='B4']")
        if cell is None:
            return ""
        if cell.find("{*}f") is not None:
            raise ValueError("Dán URL RSS dạng văn bản vào ô B4.")
        if cell.get("t") == "s":
            ss = ET.fromstring(archive.read("xl/sharedStrings.xml"))
            item = list(ss)[int(cell.findtext("{*}v"))]
            return "".join(t.text or "" for t in item.iterfind(".//{*}t")).strip()
        if cell.get("t") == "inlineStr":
            return "".join(t.text or "" for t in cell.iterfind(".//{*}t")).strip()
        return (cell.findtext("{*}v") or "").strip()


def fetch_feed(feed, snapshot):
    if not https(feed):
        raise ValueError("B4 phải là URL HTTPS của RSS.")
    if snapshot:
        with snapshot.open("rb") as stream:
            data = stream.read(MAX_RSS + 1)
        channel, following = read_channel(data)
        if following:
            raise ValueError("Bản XML offline còn phân trang. Chạy bằng URL RSS để đọc đủ các trang.")
        return data
    next_page = feed
    visited = set()
    remaining = MAX_RSS
    joined = ET.Element("rss")
    output = ET.SubElement(joined, "channel")
    while next_page:
        if next_page in visited or not https(next_page):
            raise ValueError("Liên kết phân trang RSS bị lặp hoặc thiếu HTTPS.")
        visited.add(next_page)
        request = Request(next_page, headers={"User-Agent": "Harumi-JLPT-local/1.0", "Accept": "application/rss+xml, application/xml, text/xml"})
        with urlopen(request, timeout=40) as response:
            if not https(response.url):
                raise ValueError("Feed chuyển hướng tới URL ngoài HTTPS.")
            data = response.read(remaining + 1)
            base = response.url
        remaining -= len(data)
        if remaining < 0:
            raise ValueError("Tổng dung lượng trang RSS vượt 16 MiB.")
        channel, following = read_channel(data)
        output.extend(channel.findall("{*}item"))
        next_page = urljoin(base, following) if following else None
    return ET.tostring(joined, encoding="utf-8", xml_declaration=True)


def read_channel(data):
    if len(data) > MAX_RSS or b"<!DOCTYPE" in data.upper():
        raise ValueError("Feed XML quá lớn hoặc chứa DOCTYPE.")
    channel = ET.fromstring(data).find("{*}channel")
    if channel is None:
        raise ValueError("RSS không có channel.")
    links = [node.get("href") for node in channel.findall("{*}link") if node.get("rel") == "next"]
    if len(links) > 1 or (links and not links[0]):
        raise ValueError("Liên kết trang RSS kế tiếp chưa rõ.")
    return channel, links[0] if links else None


def index_episodes(data):
    channel, _ = read_channel(data)
    entries = []
    for item in channel.findall("{*}item"):
        title = (item.findtext("{*}title") or "").strip()
        guid = (item.findtext("{*}guid") or "").strip()
        urls = set()
        keys = {normalize(title)}
        for node in item.findall("{*}enclosure"):
            mime = node.get("type", "").lower()
            url = node.get("url", "").strip()
            if mime and not mime.startswith("audio/") and mime != "application/octet-stream":
                continue
            if url:
                urls.add(url)
                keys.add(normalize(unquote(urlsplit(url).path.rpartition("/")[2])))
        duration = (item.findtext("{http://www.itunes.com/dtds/podcast-1.0.dtd}duration") or "").strip()
        seconds = None
        if re.fullmatch(r"\d+(?::[0-5]\d){0,2}", duration):
            seconds = 0
            for part in duration.split(":"):
                seconds = seconds * 60 + int(part)
        entries.append((keys - {""}, title, guid, urls, seconds))
    by_key = defaultdict(set)
    for idx, (keys, *_) in enumerate(entries):
        for key in keys:
            by_key[key].add(idx)
    guid_counts = Counter(row[2] for row in entries if row[2])
    url_counts = Counter(url for row in entries for url in row[3])
    return entries, by_key, guid_counts, url_counts


def inventory(root):
    recordings = defaultdict(set)
    packages = {}
    for level in sorted(root.glob("N[1-5]")):
        for folder in level.iterdir():
            match = re.fullmatch(r"(\d{2})(0[1-9]|1[0-2])(?:_\d+)?", folder.name)
            if folder.is_dir() and match:
                key = (level.name, f"20{match[1]}-{match[2]}")
                files = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in AUDIO]
                if files or not (folder / ".defer-audio-rss").is_file():
                    recordings[key].update(files)
    for path in sorted((root / "packages").glob("*/*/package.json")):
        if (path.parent.parent.name, path.parent.name) not in recordings:
            continue
        raw = path.read_bytes()
        data = json.loads(raw)
        exam = data["exam"]
        key = (exam["level"], f"{exam['year']:04}-{exam['month']:02}")
        if key in packages or key != (path.parent.parent.name, path.parent.name):
            raise ValueError(f"Khóa kỳ thi mâu thuẫn: {path}")
        packages[key] = (path, raw, data)
    return recordings, packages


def atomic_bytes(path, raw):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temp = Path(stream.name)
        stream.write(raw)
    try:
        os.replace(temp, path)
    finally:
        temp.unlink(missing_ok=True)


def install_rss(record, rss, root, file, replace, seconds):
    path, raw, data = record
    master = data.get("masterAudio") or {"assetId": None, "durationMs": None, "rss": None}
    old = master["rss"]
    if seconds and master["durationMs"] and abs(master["durationMs"] - seconds * 1000) >= 2000:
        raise ValueError("Thời lượng RSS khác master từ 2 giây. Kiểm tra bản thu và timeline.")
    if old == rss:
        return f"Đã đồng bộ · r{data['revision']}"
    if old and (old["episodeGuid"], old["feedUrl"]) != (rss["episodeGuid"], rss["feedUrl"]) and not replace:
        raise ValueError("Đã gắn tập/feed khác. Đối chiếu lại bản thu trước khi đổi.")
    if master["assetId"]:
        with file.open("rb") as stream:
            if master["assetId"] != "sha256:" + hashlib.file_digest(stream, "sha256").hexdigest():
                raise ValueError("File local khác master trong gói.")
    elif master["durationMs"]:
        # A legacy package may have cues and an HTML duration but no master digest.
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "default=nk=1:nw=1", str(file)], capture_output=True, text=True)
        if probe.returncode:
            raise ValueError("ffprobe không đọc được thời lượng file nguồn.")
        local_ms = round(float(probe.stdout) * 1000)
        if abs(local_ms - master["durationMs"]) >= 2000:
            raise ValueError("File nguồn khác thời lượng gốc của đề từ 2 giây. Kiểm tra bản thu và timeline.")
    data["masterAudio"] = {**master, "rss": rss}
    if data["schemaVersion"] == "1.3.0":
        editorial = [issue for issue in data["review"]["issues"] if not issue["code"].startswith("COVERAGE_")]
        data["review"]["issues"] = editorial + checklist_issues(data)
    data["revision"] += 1
    check_package(data, root, False)
    if path.read_bytes() != raw:
        raise ValueError("Gói vừa được thay đổi. Chạy lại đồng bộ.")
    atomic_bytes(path, (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return f"Đã đồng bộ · r{data['revision']}"


def reconcile(root, feed, index, replace=False):
    recordings, packages = inventory(root)
    rows = []
    issues = []
    if index is not None:
        entries, by_key, guid_counts, url_counts = index
        owners = defaultdict(set)
        candidates = {}
        for key, files in recordings.items():
            for file in files:
                hits = by_key[normalize(file.name)] | by_key[normalize(file.stem)]
                candidates[file] = hits
                for hit in hits:
                    owners[hit].add(key)
    for key, files in sorted(recordings.items()):
        package = packages.get(key)
        for file in sorted(files) or [None]:
            rss, title = None, None
            state = "Chờ RSS"
            migration = f"r{package[2]['revision']}" if package else "Chờ tạo gói"
            if not file:
                state = "Chưa có tệp local"
            elif len(files) > 1:
                state = "Nhiều tệp trong cùng kỳ"
            elif (stamp := re.fullmatch(r"JLPT[-_ ](N[1-5])[-_ ](\d{4})[-_ ](\d{2})", file.stem, re.I)) and (
                    stamp[1].upper(), stamp[2] + "-" + stamp[3]) != key:
                state = "Tên file khác cấp/kỳ của đề"
            elif index is not None:
                hits = candidates[file]
                if len(hits) != 1:
                    state = "Trùng tên trên RSS" if hits else "Chưa thấy trên RSS"
                else:
                    hit = next(iter(hits))
                    _, title, guid, urls, seconds = entries[hit]
                    if owners[hit] != {key}:
                        state = "Một tập khớp nhiều kỳ"
                    elif not guid or len(urls) != 1 or not https(next(iter(urls))):
                        state = "Kiểm tra GUID/enclosure"
                    elif guid_counts[guid] != 1 or url_counts[next(iter(urls))] != 1:
                        state = "GUID/URL dùng nhiều lần"
                    else:
                        state = "Khớp tên"
                        rss = {"feedUrl": feed, "episodeGuid": guid, "enclosureUrl": next(iter(urls))}
                        if package:
                            try:
                                migration = install_rss(package, rss, root, file, replace, seconds)
                            except (ValueError, OSError) as exc:
                                migration = "Cần kiểm tra gói"
                                issues.append(f"{key[0]} {key[1]}: {exc}")
            if index is None and package:
                rss = (package[2].get("masterAudio") or {}).get("rss")
                if rss and state == "Chờ RSS":
                    state = "URL đã lưu trong gói"
            rows.append([key[0] + " · " + key[1].replace("-", "/"), file.name if file else None,
                         state, rss["enclosureUrl"] if rss else None, title, migration,
                         file.relative_to(root).as_posix() if file else None])
    return rows, issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--feed-url", help="Override and save workbook B4")
    cache_options = parser.add_mutually_exclusive_group()
    cache_options.add_argument("--rss-file", type=Path, help="Read offline copy of the specified HTTPS feed")
    cache_options.add_argument("--use-saved-feed", action="store_true", help="Reuse the last successful feed snapshot for B4")
    parser.add_argument("--replace-episode", action="store_true")
    parser.add_argument("--output", type=Path, required=True, help="Intermediate workbook rows JSON")
    args = parser.parse_args()
    root = args.root.resolve()
    feed = args.feed_url or get_workbook_feed(root / BOOK)
    if (args.rss_file or args.use_saved_feed) and not feed:
        parser.error("An offline snapshot still needs its original HTTPS feed URL in B4 or --feed-url.")
    index = None
    if feed:
        cache = root / "work/rss" / (hashlib.sha256(feed.encode()).hexdigest() + ".xml")
        data = fetch_feed(feed, cache if args.use_saved_feed else args.rss_file)
        index = index_episodes(data)
        if not args.use_saved_feed:
            cache.parent.mkdir(parents=True, exist_ok=True)
            atomic_bytes(cache, data)
    rows, issues = reconcile(root, feed, index, args.replace_episode)
    args.output.write_text(json.dumps({"feed": feed, "rows": rows, "issues": issues}, ensure_ascii=False), encoding="utf-8")
    for issue in issues:
        print(issue, file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, ET.ParseError, zipfile.BadZipFile) as error:
        sys.exit(str(error))
