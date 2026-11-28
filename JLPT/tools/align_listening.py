"""Build a listening review worksheet from one package and an optional full-file STT timeline."""

import argparse
import re
import sys
import unicodedata
from bisect import bisect_left
from pathlib import Path

from listening_stt import ROOT, fingerprint, read_json, save_json


NUMBER = r"[0-9一二三四五六七八九十]+"
MONDAI = re.compile(rf"^(?:これから[、。 ]*)?(?:第)?問題\s*({NUMBER})(?![0-9一二三四五六七八九十])")
QUESTION = re.compile(rf"^(?:第)?({NUMBER})\s*番(?:[。、「\s]|です|$)")


def number(text):
    if text.isdecimal():
        return int(text)
    digits = "〇一二三四五六七八九"
    if "十" in text:
        tens, units = text.split("十", 1)
        if tens in digits and units in digits:
            return (digits.index(tens) if tens else 1) * 10 + (digits.index(units) if units else 0)
    if len(text) == 1 and text in digits:
        return digits.index(text)
    return None


def normalized(text):
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"(?m)^\s*(?:男|女|男性|女性|[A-Z])\s*:\s*", "", text)
    return "".join(c for c in text if c.isalnum())


def marked_ranges(mondais, timeline):
    """Trust announced numbering only when it forms a complete, unambiguous sequence."""
    segments = timeline["segments"]
    groups = []
    for idx, segment in enumerate(segments):
        line = unicodedata.normalize("NFKC", segment["text"]).strip()
        marker = MONDAI.match(line)
        if marker:
            groups.append((number(marker[1]), idx))
    if [n for n, _ in groups] != [m["mondaiNumber"] for m in mondais]:
        return {}, {}
    mondai_ranges, question_ranges = {}, {}
    for pos, (m, (_, first)) in enumerate(zip(mondais, groups)):
        last = groups[pos + 1][1] if pos + 1 < len(groups) else len(segments)
        end = segments[last]["startMs"] if last < len(segments) else timeline["durationMs"]
        mondai_ranges[m["id"]] = (segments[first]["startMs"], end)
        questions = [q["id"] for block in m["blocks"] for q in block["questions"]]
        marks = []
        for segment in segments[first + 1:last]:
            match = QUESTION.match(unicodedata.normalize("NFKC", segment["text"]).strip())
            if match:
                marks.append((number(match[1]), segment["startMs"]))
        if [n for n, _ in marks] == list(range(1, len(questions) + 1)):
            cuts = [t for _, t in marks] + [end]
            question_ranges.update(zip(questions, zip(cuts, cuts[1:])))
    return mondai_ranges, question_ranges


class WordIndex:
    def __init__(self, words):
        self.words = words
        self.char_ends = []
        parts = []
        end = 0
        for word in words:
            part = normalized(word["text"])
            parts.append(part)
            end += len(part)
            self.char_ends.append(end)
        self.text = "".join(parts)

    def script_range(self, script, lower, upper):
        spoken = normalized(script)
        if len(spoken) < 20:
            return None
        left = len(spoken) // 2
        for length in (min(18, left), 10):
            prefix, suffix = spoken[:length], spoken[-length:]
            starts = [m.start() for m in re.finditer(re.escape(prefix), self.text)]
            ends = [m.end() for m in re.finditer(re.escape(suffix), self.text)]
            candidates = set()
            for start in starts:
                for end in ends:
                    if not 0.75 * len(spoken) <= end - start <= 1.25 * len(spoken):
                        continue
                    lo = self.words[bisect_left(self.char_ends, start + 1)]["startMs"]
                    hi = self.words[bisect_left(self.char_ends, end)]["endMs"]
                    if lower <= lo < hi <= upper:
                        candidates.add((lo, hi))
            if len(candidates) == 1:
                return candidates.pop()
        return None


def transcript_slice(timeline, lo, hi):
    lines = []
    for row in timeline["segments"]:
        if lo <= row["startMs"] and row["endMs"] <= hi:
            lines.append(row["text"])
        elif row["startMs"] < hi and row["endMs"] > lo:
            start, end = max(lo, row["startMs"]), min(hi, row["endMs"])
            words = [w["text"] for w in timeline["words"] if start <= (w["startMs"] + w["endMs"]) / 2 < end]
            if words:
                lines.append("".join(words))
    return "\n".join(lines)


def review(package, timeline=None):
    mondais = package["content"]["choukai"]["mondais"]
    cues = package["annotations"]["audioSegments"]
    master = package.get("masterAudio") or {}
    duration = master.get("durationMs")
    by_mondai, by_question = {}, {}
    if timeline:
        digest = timeline["sourceSha256"]
        if master.get("assetId"):
            if master["assetId"] != "sha256:" + digest:
                raise ValueError("Timeline fingerprint differs from package master audio.")
        else:
            exam = package["exam"]
            expected = f"JLPT-{exam['level']}-{exam['year']:04d}-{exam['month']:02d}"
            if Path(timeline["audioFile"]).stem.casefold() != expected.casefold():
                raise ValueError("Master is unbound. Match the configured source filename or bind its SHA first.")
        if duration and abs(duration - timeline["durationMs"]) > 1000:
            raise ValueError("Master durations differ by more than one second. Verify the recording.")
        duration = timeline["durationMs"]
        by_mondai, by_question = marked_ranges(mondais, timeline)
    index = WordIndex(timeline["words"] if timeline else [])
    rows = []

    def add(mid, role, ids, number_in_exam, script=None, owner=None, proposal=None, method=None):
        matches = [c for c in cues if c["mondaiId"] == mid and c["role"] == role
                   and set(c["questionIds"]) == set(ids)]
        row = dict(mondaiId=mid, role=role, questionIds=ids, number=number_in_exam,
                   sourceCues=matches, timelineCandidate=None, needs=[])
        source_bounds = {(c["startMs"], c["endMs"]) for c in matches}
        bounds = next(iter(source_bounds)) if len(source_bounds) == 1 else None
        if len(source_bounds) > 1:
            row["needs"].append("resolve-conflicting-source-cues")
        elif not bounds or bounds[1] is None:
            if proposal and (not bounds or bounds[0] < proposal[1]):
                start = bounds[0] if bounds else proposal[0]
                bounds = (start, proposal[1])
                row["timelineCandidate"] = dict(startMs=start, endMs=proposal[1], method=method)
                row["needs"].append("verify-cue-on-master")
            else:
                row["needs"].append("locate-end" if bounds else "locate-cue")
        if role != "mondai":
            row["scriptOwnerId"] = owner
            row["hasScript"] = bool(script)
            if not script:
                if timeline and bounds and bounds[1] is not None:
                    excerpt = transcript_slice(timeline, *bounds)
                    if excerpt:
                        row["scriptJaCandidate"] = excerpt
                row["needs"].append("verify-stt-script" if row.get("scriptJaCandidate") else "locate-script")
        rows.append(row)

    ordinal = 0
    for m in mondais:
        mid = m["id"]
        group = by_mondai.get(mid)
        add(mid, "mondai", [], m["mondaiNumber"], proposal=group, method="spoken-mondai-markers")
        lower, upper = group or (0, duration or 0)
        source_group = {(c["startMs"], c["endMs"]) for c in rows[-1]["sourceCues"]}
        if len(source_group) == 1:
            source_start, source_end = source_group.pop()
            lower, upper = source_start, source_end if source_end is not None else (duration or 0)
        for block in m["blocks"]:
            questions = block["questions"]
            ids = [q["id"] for q in questions]
            shared = next((i for i in block["mediaItems"] if i["kind"] == "audio"), None)
            shared_script = (shared["audio"]["scriptJaMd"].strip() if shared else "")
            shared_cues = [c for c in cues if c["role"] == "shared" and c["mondaiId"] == mid
                           and set(c["questionIds"]) == set(ids)]
            if len(ids) > 1 and (shared or shared_cues):
                add(mid, "shared", ids, [ordinal + 1, ordinal + len(ids)], script=shared_script,
                    owner=shared["id"] if shared else block["id"],
                    proposal=index.script_range(shared_script, lower, upper), method="script-word-anchors")
            for q in questions:
                ordinal += 1
                qid = q["id"]
                own_script = (q.get("jlptListenScript") or {}).get("scriptJaMd", "").strip()
                # A shared passage has its own cue. It cannot establish the boundaries of a child question.
                single_script = own_script or (shared_script if len(ids) == 1 else "")
                candidate = by_question.get(qid)
                if candidate and not (lower <= candidate[0] < candidate[1] <= upper):
                    candidate = None
                method = "spoken-question-markers" if candidate else "script-word-anchors"
                add(mid, "question", [qid], ordinal, script=own_script or shared_script,
                    owner=qid if own_script or not shared else shared["id"],
                    proposal=candidate or index.script_range(single_script, lower, upper), method=method)
    return dict(packageId=package["packageId"], revision=package["revision"],
                audioSha256=timeline["sourceSha256"] if timeline else None,
                durationMs=duration, rows=rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--timeline", type=Path, help="Optional timeline.json from listening_stt.py")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    try:
        report = review(read_json(args.package), read_json(args.timeline) if args.timeline else None)
        report["packageSha256"] = fingerprint(args.package)
        report["timelineSha256"] = fingerprint(args.timeline) if args.timeline else None
        target = args.out or ROOT / "work/stt" / report["packageId"] / "alignment-review.json"
        save_json(target, report)
        print(target)
    except (OSError, ValueError) as error:
        sys.exit(f"Alignment: {error}")
