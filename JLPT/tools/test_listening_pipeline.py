"""Offline regression checks for the listening pipeline."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import align_listening as align
import listening_stt as stt


def package():
    return {
        "packageId": "test", "revision": 1, "exam": {"level": "N3", "year": 2018, "month": 12},
        "masterAudio": {"durationMs": 310000, "assetId": "sha256:abc"},
        "content": {"choukai": {"mondais": [{"id": "m1", "mondaiNumber": 1, "blocks": [
            {"id": "b", "mediaItems": [], "questions": [{"id": "q1"}, {"id": "q2"}]}
        ]}]}},
        "annotations": {"audioSegments": [{"role": "question", "mondaiId": "m1",
                                           "questionIds": ["q1"], "startMs": 1200, "endMs": 5000}]},
    }


def timeline():
    lines = ["問題一", "一番。", "お店に行きます。", "二番。", "明日は休みです。"]
    stamps = [(0, 1000), (1000, 1400), (1400, 4800), (6000, 6800), (6800, 7000)]
    segments = [dict(text=text, startMs=lo, endMs=hi) for text, (lo, hi) in zip(lines, stamps)]
    return dict(segments=segments, words=segments, sourceSha256="abc", durationMs=310000)


class ListeningPipelineTests(unittest.TestCase):
    def test_partial_run_resumes_once_and_offsets_both_clocks(self):
        raw = dict(text="です", words=[dict(word="です", start=0.1, end=0.4)],
                   segments=[dict(text="です", start=0.0, end=0.5)])
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            audio = folder / "master.mp3"
            audio.write_bytes(b"fake input for hashing")
            with patch.object(stt, "duration_ms", return_value=300700), \
                    patch.object(stt, "load_key", return_value="offline"), \
                    patch.object(stt, "extract_chunk"), patch.object(stt, "request_chunk", return_value=raw) as api:
                self.assertIsNone(stt.transcribe(audio, folder, None, max_chunks=1))
                self.assertEqual(api.call_count, 1)
                result = stt.read_json(stt.transcribe(audio, folder, None))
                self.assertEqual(api.call_count, 2)
                self.assertEqual(result["words"][1]["startMs"], 300100)
                self.assertEqual(result["segments"][1]["endMs"], 300500)
                stt.transcribe(audio, folder, None, max_chunks=0)
                self.assertEqual(api.call_count, 2)

    def test_source_wins_and_missing_script_comes_from_timed_speech(self):
        rows = align.review(package(), timeline())["rows"]
        self.assertEqual(rows[0]["timelineCandidate"]["startMs"], 0)
        self.assertIsNone(rows[1]["timelineCandidate"])
        self.assertIn("お店に行きます", rows[1]["scriptJaCandidate"])
        self.assertNotIn("明日", rows[1]["scriptJaCandidate"])
        self.assertEqual(rows[2]["timelineCandidate"]["startMs"], 6000)
        self.assertIn("verify-stt-script", rows[2]["needs"])

    def test_shared_cue_and_script_do_not_become_question_bounds(self):
        fixture = package()
        fixture["annotations"]["audioSegments"] = [
            dict(role="shared", mondaiId="m1", questionIds=["q1", "q2"], startMs=1200, endMs=7000)]
        fixture["content"]["choukai"]["mondais"][0]["blocks"][0]["mediaItems"] = [
            {"id": "a", "kind": "audio", "audio": {"scriptJaMd": "明日は休みです。"}}]
        rows = align.review(fixture)["rows"]
        self.assertEqual([r["role"] for r in rows], ["mondai", "shared", "question", "question"])
        self.assertTrue(rows[2]["hasScript"])
        self.assertEqual(rows[2]["scriptOwnerId"], "a")
        self.assertEqual(rows[2]["needs"], ["locate-cue"])
        self.assertEqual(rows[3]["needs"], ["locate-cue"])

    def test_duplicate_announcements_and_word_anchors_are_unresolved(self):
        data = timeline()
        data["segments"][3]["text"] = "一番。"
        self.assertIsNone(align.review(package(), data)["rows"][2]["timelineCandidate"])
        script = "レストランで店員さんにお昼のおすすめについて聞いています"
        words = [dict(text=c, startMs=i * 10, endMs=i * 10 + 10) for i, c in enumerate(script * 2)]
        index = align.WordIndex(words)
        self.assertIsNone(index.script_range(script, 0, 10000))
        self.assertEqual(index.script_range(script, 0, len(script) * 10), (0, len(script) * 10))

    def test_wrong_master_and_bad_local_times_rejected(self):
        data = timeline()
        data["sourceSha256"] = "other"
        with self.assertRaises(ValueError):
            align.review(package(), data)
        with self.assertRaises(ValueError):
            stt.absolute_rows({"text": "話", "words": [dict(word="話", start=5, end=1)]}, "words", 0, 10000)


if __name__ == "__main__":
    unittest.main()
