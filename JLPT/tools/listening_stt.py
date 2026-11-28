"""Transcribe one exam master in resumable five-minute chunks; all output times are milliseconds."""

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import time
from contextlib import contextmanager
from pathlib import Path
from tempfile import NamedTemporaryFile, TemporaryDirectory


MODEL = "whisper-large-v3-turbo"
CHUNK_MS = 300_000
ROOT = Path(__file__).resolve().parents[1]
KEY_FILE = Path("D:/JLPT/groq/groq_api_key.txt")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8", newline="\n", dir=path.parent, delete=False) as stream:
        temp = Path(stream.name)
        try:
            json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
            stream.write("\n")
        except BaseException:
            stream.close()
            temp.unlink(missing_ok=True)
            raise
    try:
        temp.replace(path)
    finally:
        temp.unlink(missing_ok=True)


def fingerprint(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def duration_ms(audio):
    raw = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "default=noprint_wrappers=1:nokey=1", str(audio)])
    measured = round(float(raw) * 1000)
    if measured <= 0:
        raise ValueError("Audio has no measurable duration.")
    return measured


def split_ranges(duration):
    return [(start, min(start + CHUNK_MS, duration)) for start in range(0, duration, CHUNK_MS)]


def extract_chunk(audio, start, end, target):
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-ss", f"{start / 1000:.3f}",
                    "-i", str(audio), "-t", f"{(end - start) / 1000:.3f}", "-map", "0:a:0",
                    "-map_metadata", "-1", "-ac", "1", "-ar", "16000", "-c:a", "flac", str(target)], check=True)
    if not 0 < target.stat().st_size < 25_000_000:
        raise ValueError("Invalid chunk size for Groq free-tier upload.")


def load_key(key_file):
    key = os.environ.get("GROQ_API_KEY") or key_file.read_text(encoding="utf-8-sig").strip()
    if not key or any(char.isspace() for char in key):
        raise ValueError("Expected one Groq key in GROQ_API_KEY or the local key file.")
    return key


def request_chunk(path, key):
    import requests
    fields = [("model", MODEL), ("language", "ja"), ("temperature", "0"),
              ("response_format", "verbose_json"), ("timestamp_granularities[]", "word"),
              ("timestamp_granularities[]", "segment")]
    for attempt in range(3):
        with path.open("rb") as chunk:
            response = requests.post("https://api.groq.com/openai/v1/audio/transcriptions",
                                     headers={"Authorization": f"Bearer {key}"}, data=fields,
                                     files={"file": ("chunk.flac", chunk, "audio/flac")},
                                     allow_redirects=False, timeout=(15, 180))
        if response.status_code == 200:
            return response.json()
        retry_after = response.headers.get("Retry-After")
        if response.status_code == 429:
            try:
                delay = max(1, math.ceil(float(retry_after))) if retry_after else None
            except (ValueError, OverflowError):
                delay = None
            if delay is None or delay > 30 or attempt == 2:
                hint = f" Retry-After: {retry_after}." if retry_after else ""
                raise ValueError(f"Groq rate limit; resume the same command later.{hint}")
        elif response.status_code in (500, 502, 503, 504) and attempt < 2:
            delay = 2 ** attempt
        else:
            raise ValueError(f"Groq HTTP {response.status_code}. Cached chunks are reusable.")
        time.sleep(delay)


def absolute_rows(raw, field, start, end):
    key = "text" if field == "segments" else "word"
    items = raw.get(field)
    if not isinstance(items, list) or (raw.get("text", "").strip() and not items):
        raise ValueError(f"Groq omitted {field} timestamps. Chunk was not accepted.")
    results = []
    for item in items:
        lo, hi = item["start"], item["end"]
        if not all(type(n) in (int, float) and math.isfinite(n) for n in (lo, hi)) or not (0 <= lo <= hi):
            raise ValueError("Invalid chunk timestamp.")
        if hi * 1000 > end - start + 1000:
            raise ValueError("Timestamp exceeds its chunk by more than one second.")
        text = item[key].strip()
        if text:
            results.append({"text": text, "startMs": min(end, start + round(1000 * lo)),
                            "endMs": min(end, start + round(1000 * hi))})
    return results


@contextmanager
def master_lock(folder):
    # OS locks release on process exit, including an interrupted transcription.
    with (folder / ".running").open("a+b") as handle:
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise ValueError("Another STT process is already processing this audio.") from error
        yield


def transcribe(audio, work, key_file, max_chunks=None):
    digest = fingerprint(audio)
    duration = duration_ms(audio)
    folder = work / digest / f"{MODEL}-ja-300s-v1"
    folder.mkdir(parents=True, exist_ok=True)
    with master_lock(folder):
        return transcribe_chunks(audio, duration, digest, folder, key_file, max_chunks)


def transcribe_chunks(audio, duration, digest, folder, key_file, max_chunks):
    ranges = split_ranges(duration)
    words, segments = [], []
    calls = 0
    for index, (start, end) in enumerate(ranges):
        cached = folder / f"{index:03d}-{start}-{end}.json"
        if cached.is_file():
            raw = read_json(cached)
        else:
            if max_chunks is not None and calls >= max_chunks:
                print(f"Paused before chunk {index + 1}/{len(ranges)}. Cache: {folder}")
                return None
            key = load_key(key_file)
            with TemporaryDirectory() as scratch:
                chunk = Path(scratch) / "chunk.flac"
                extract_chunk(audio, start, end, chunk)
                raw = request_chunk(chunk, key)
            calls += 1
        if not isinstance(raw, dict) or not isinstance(raw.get("text"), str):
            raise ValueError("Invalid transcription response.")
        words.extend(absolute_rows(raw, "words", start, end))
        segments.extend(absolute_rows(raw, "segments", start, end))
        if not cached.is_file():
            save_json(cached, raw)
    target = folder / "timeline.json"
    save_json(target, {"formatVersion": 1, "model": MODEL, "language": "ja", "sourceSha256": digest,
                       "audioFile": audio.name, "durationMs": duration, "chunkMs": CHUNK_MS,
                       "words": words, "segments": segments})
    print(target)
    return target


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", type=Path)
    parser.add_argument("--work", type=Path, default=ROOT / "work/stt")
    parser.add_argument("--key-file", type=Path, default=KEY_FILE)
    parser.add_argument("--max-chunks", type=int, help="Limit new uploads this run. Cached chunks cost nothing.")
    args = parser.parse_args()
    if args.max_chunks is not None and args.max_chunks < 0:
        parser.error("--max-chunks must be nonnegative")
    try:
        transcribe(args.audio.resolve(strict=True), args.work, args.key_file, args.max_chunks)
    except (OSError, ValueError, ImportError, subprocess.SubprocessError) as error:
        sys.exit(f"STT: {error}")
