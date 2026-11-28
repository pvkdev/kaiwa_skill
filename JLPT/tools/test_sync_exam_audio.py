import json
from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import wave

from sync_exam_audio import fetch_feed, index_episodes, reconcile

FEED = "https://example.test/jlpt/rss"
URL = "https://media.example.test/opaque/12345"
FIXTURE = Path(__file__).resolve().parents[1] / "contracts/v1/synthetic-draft.json"


def item(title, url=URL, guid="episode-12", duration="00:40"):
    return (f"<item><title>{title}</title><guid>{guid}</guid>"
            f'<itunes:duration>{duration}</itunes:duration><enclosure type="audio/mpeg" url="{url}" /></item>')


def episodes(*items):
    return index_episodes(('<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"><channel>' +
                           "".join(items) + "</channel></rss>").encode())


class RssBinding(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name).resolve()
        self.path = self.root / "packages/N5/2025-12/package.json"
        self.path.parent.mkdir(parents=True)
        self.audio = self.root / "N5/2512/JLPT-N5-2025-12.mp3"
        self.audio.parent.mkdir(parents=True)
        with wave.open(str(self.audio), "wb") as fixture_audio:
            fixture_audio.setparams((1, 1, 8000, 0, "NONE", ""))
            fixture_audio.writeframes(b"\x80" * 8000 * 40)
        self.data = json.loads(FIXTURE.read_bytes())
        self.data["exam"].update(year=2025, month=12)
        self.path.write_text(json.dumps(self.data), encoding="utf-8")

    def test_title_then_idempotent_reimport(self):
        index = episodes(item(self.audio.stem))
        rows, issues = reconcile(self.root, FEED, index)
        self.assertEqual((rows[0][3], issues), (URL, []))
        saved = self.path.read_bytes()
        bound = json.loads(saved)
        self.assertEqual(bound["masterAudio"]["rss"], {"feedUrl": FEED, "episodeGuid": "episode-12", "enclosureUrl": URL})
        self.assertEqual(bound["revision"], self.data["revision"] + 1)
        self.assertEqual(bound["content"], self.data["content"])
        reconcile(self.root, FEED, index)
        self.assertEqual(self.path.read_bytes(), saved)

    def test_archived_and_deferred_recordings_return_only_with_active_source(self):
        active = self.audio.parent
        archive = active.parent / "old" / active.name
        archive.parent.mkdir()
        active.rename(archive)
        index = episodes(item(self.audio.stem))
        before = self.path.read_bytes()
        self.assertEqual(reconcile(self.root, FEED, index), ([], []))
        active.mkdir()
        (active / ".defer-audio-rss").touch()
        self.assertEqual(reconcile(self.root, FEED, index), ([], []))
        self.assertEqual(self.path.read_bytes(), before)
        (archive / self.audio.name).rename(self.audio)
        rows, issues = reconcile(self.root, FEED, index)
        self.assertEqual((rows[0][3], issues), (URL, []))

    def test_opaque_title_and_exact_encoded_filename(self):
        self.audio = self.audio.rename(self.audio.with_name("Audio N5.mp3"))
        url = "https://files.example.test/audio/Audio%20N5.mp3?version=1"
        rows, _ = reconcile(self.root, FEED, episodes(item("Tên khác", url)))
        self.assertEqual(rows[0][3], url)

    def test_version_13_updates_coverage_only(self):
        self.data["schemaVersion"] = "1.3.0"
        self.data["exam"]["slug"] = "2025/12"
        self.data["annotations"].setdefault("sentencePairs", {})
        notes = list(self.data["review"]["issues"])
        self.data["review"]["issues"].append(dict(code="COVERAGE_rssUrl", severity="error", targetId=None, message="URL"))
        self.path.write_text(json.dumps(self.data), encoding="utf-8")
        _, issues = reconcile(self.root, FEED, episodes(item(self.audio.name)))
        self.assertEqual(issues, [])
        saved = json.loads(self.path.read_bytes())
        self.assertEqual(saved["exam"]["slug"], "2025/12")
        checklist = saved["review"]["issues"]
        self.assertEqual([i for i in checklist if not i["code"].startswith("COVERAGE_")], notes)
        self.assertNotIn("COVERAGE_rssUrl", [i["code"] for i in checklist])
        self.assertIn("COVERAGE_script", [i["code"] for i in checklist])

    def test_feed_pagination_finds_episode_on_second_page(self):
        def response(request, timeout):
            if request.full_url == FEED:
                xml = '<link rel="next" href="?page=2"/>'
            else:
                self.assertEqual(request.full_url, FEED + "?page=2")
                xml = item(self.audio.name)
            stream = BytesIO(('<rss xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"><channel>'
                              + xml + "</channel></rss>").encode())
            stream.url = request.full_url
            return stream
        with patch("sync_exam_audio.urlopen", side_effect=response):
            rows, _ = reconcile(self.root, FEED, index_episodes(fetch_feed(FEED, None)))
        self.assertEqual(rows[0][3], URL)

    def test_misfiled_recording_and_wrong_local_duration(self):
        wrong = self.audio.rename(self.audio.with_name("JLPT-N4-2025-12.mp3"))
        rows, _ = reconcile(self.root, FEED, episodes(item(wrong.name)))
        self.assertEqual(rows[0][2], "Tên file khác cấp/kỳ của đề")
        self.assertIsNone(rows[0][3])
        wrong.rename(self.audio)
        self.data["masterAudio"]["durationMs"] = 42000
        self.path.write_text(json.dumps(self.data), encoding="utf-8")
        before = self.path.read_bytes()
        _, issues = reconcile(self.root, FEED, episodes(item(self.audio.stem, duration="")))
        self.assertIn("File nguồn khác thời lượng", issues[0])
        self.assertEqual(before, self.path.read_bytes())

    def test_unmatched_ambiguous_missing_guid_duration_and_cross_exam(self):
        before = self.path.read_bytes()
        for index in (None, episodes(item("khác")), episodes(item(self.audio.name), item(self.audio.name)),
                      episodes(item(self.audio.name, guid="")), episodes(item(self.audio.name, url="http://bad.test/a.mp3"))):
            rows, _ = reconcile(self.root, FEED, index)
            self.assertIsNone(rows[0][3])
            self.assertEqual(self.path.read_bytes(), before)
        rows, issues = reconcile(self.root, FEED, episodes(item(self.audio.name, duration="42")))
        self.assertTrue(issues)
        self.assertEqual(self.path.read_bytes(), before)
        self.audio = self.audio.rename(self.audio.with_name("master.mp3"))
        second = self.root / "N4/2512" / self.audio.name
        second.parent.mkdir(parents=True)
        second.touch()
        rows, _ = reconcile(self.root, FEED, episodes(item(self.audio.name)))
        self.assertEqual([row[2] for row in rows], ["Một tập khớp nhiều kỳ"] * 2)
        self.assertEqual(self.path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
