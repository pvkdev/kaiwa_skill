import html
import json
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
import unittest


CHECK = runpy.run_path(str(Path(__file__).resolve().parents[1] / "scripts" / "check.py"))
PAIR_KEY = html.escape(json.dumps(["Dịch script 1", "q-1", 0, "会話"], ensure_ascii=False), quote=True)
PAIR = f'<div data-key="{PAIR_KEY}" data-vi="Hội thoại">Nhật · 会話<br>Việt · Hội thoại<a href="#line">Gốc</a></div>'
SCRIPT = '<div data-key="script-0"><strong>Script</strong>会話<a href="#panel">Gốc</a></div>'
ANSWER = '<div data-key="answer-q-1"><strong>Giải thích</strong>Lời giải</div>'
FIXTURE = f"""<!doctype html>
<!-- Page saved with SingleFile
 url: https://www.vnjpclub.com/thi-thu/jlpt-n3/?vnjp_jlpt_level=n3&giaotrinh=2025-07&theloai=choukai
-->
<div class="vnjp-jlpt-root">
  <div class="q-item" id="q-1">
    <label class="choice-correct"><input type="radio" value="1"></label>
    <div class="result-line">Đáp án đúng: 1</div>
    <div class="complete-answer">Lời giải</div>
    <div class="vnjp-choukai-q-script">
      <button class="vnjp-choukai-q-script-toggle">Script</button>
      <div class="vnjp-choukai-q-script-panel" id="panel">
        <div class="vnjp-choukai-q-player" data-start="1" data-end="3"></div>
        <div class="vnjp-jlpt-tudich">
          <span class="vnjp-jlpt-candich" id="line">会話</span>
          <span class="vnjp-jlpt-kqdich">Hội thoại</span>
        </div>
      </div>
    </div>
  </div>
</div>
<section id="jlpt-singlefile-notes">
  <p role="status">Đã rà xong. Script 1/1. Bản dịch 1/1 dòng đã rà. Giải thích 1/1 câu.</p>
  <div>
    {PAIR}{SCRIPT}{ANSWER}
    <div data-key="audio|script 1|div[1]"><strong>Câu 1 · Audio script 1</strong>
data-start = 1
data-end = 3</div>
    <div data-key="audio|đề|audio[1]">
src = https://www.vnjpclub.com/thithu/mp3/n3/2025-07.mp3
Thời lượng = 5 s</div>
  </div>
</section>"""


class AuditTest(unittest.TestCase):
    def inspect(self, raw=FIXTURE):
        with TemporaryDirectory() as folder:
            file = Path(folder) / "sample.html"
            file.write_text(raw, encoding="utf-8")
            return CHECK["inspect_html"](file)

    def test_complete_snapshot_and_matching_audio(self):
        report = self.inspect()
        for key in ("structure_issues", "summary_issues", "answer_issues", "explanation_issues",
                    "missing_pairs", "pair_issues", "script_coverage", "script_issues", "clip_issues"):
            self.assertEqual(report[key], [], key)
        audio = [{"file": "JLPT-N3-2025-07.mp3", "probe": {"format": {"duration": "5"}}, "decode": "passed"}]
        self.assertEqual(CHECK["inspect_package"](Path("N3/2507"), [report], audio, ("choukai",)), [])

    def test_missing_appendix_entries_detected_despite_success_banner(self):
        mutations = (
            (PAIR, "missing_pairs"),
            (SCRIPT, "script_coverage"),
            (ANSWER, "explanation_issues"),
        )
        for fragment, key in mutations:
            with self.subTest(key=key):
                report = self.inspect(FIXTURE.replace(fragment, ""))
                self.assertTrue(report[key])
                self.assertTrue(report["summary_issues"])

    def test_duplicate_choices_ambiguous_links_and_impossible_milestones(self):
        raw = FIXTURE.replace('<label class="choice-correct">', '<label class="choice-correct"><input type="radio" value="2">')
        raw = raw.replace('id="line">会話</span>', 'id="line">会話</span><span id="line">別の文</span>')
        report = self.inspect(raw.replace('data-end="3"', 'data-end="6"'))
        self.assertTrue(report["answer_issues"])
        self.assertTrue(report["pair_issues"])
        self.assertTrue(report["clip_issues"])

    def test_wrong_period_missing_section_and_wrong_audio_duration(self):
        report = self.inspect()
        assess = CHECK["inspect_package"]
        issues = assess(Path("N3/2507"), [report], [], CHECK["PARTS"])
        self.assertTrue(any("missing HTML for moji_bunpo_dokkai" in issue for issue in issues))
        self.assertTrue(any("matching offline audio file not found" in issue for issue in issues))
        audio = [{"file": "JLPT-N3-2025-07.mp3", "probe": {"format": {"duration": "2"}}}]
        issues = assess(Path("N3/2507"), [report], audio, ("choukai",))
        self.assertTrue(any("duration does not match" in issue for issue in issues))
        issues = assess(Path("N3/2512"), [report], audio, ("choukai",))
        self.assertTrue(any("unexpected exam identity" in issue for issue in issues))

    def test_baseline_flags_content_missing_from_both_sides(self):
        previous = self.inspect()
        raw = FIXTURE.replace(PAIR, "").replace('class="vnjp-jlpt-candich"', 'class="removed"')
        raw = raw.replace("Bản dịch 1/1", "Bản dịch 0/0")
        current = self.inspect(raw)
        self.assertFalse(current["missing_pairs"])
        self.assertFalse(current["summary_issues"])
        issues = CHECK["inspect_package"](Path("N3/2507"), [current], [], ("choukai",), [previous])
        self.assertTrue(any("translation count fell compared with baseline" in issue for issue in issues))

    def test_saved_overlay_and_body_blur_are_reported_separately(self):
        overlay = '<div id="vnjp-devtools-overlay" style="position:fixed;inset:0">Developer Tools đang mở</div>'
        raw = '<body style="filter:blur(6px)">' + FIXTURE + overlay + '</body>'
        report = self.inspect(raw)
        self.assertEqual(len(report["display_issues"]), 2)
        self.assertEqual(report["missing_pairs"], [])
        hidden = self.inspect(raw.replace('id="vnjp-devtools-overlay"', 'id="vnjp-devtools-overlay" hidden'))
        self.assertEqual(len(hidden["display_issues"]), 1)


if __name__ == "__main__":
    unittest.main()
