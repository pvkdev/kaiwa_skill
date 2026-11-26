"""Verify authored supplemental listening, local audio, and pending native exports."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/listening-supplemental-01-39.json"


def run():
    result = []
    for lesson in (1, 39):
        lesson_name = f"lesson-{lesson:02d}"
        authored = json.loads((ROOT / "authored" / lesson_name / "listening.json").read_text(encoding="utf-8"))
        assert len(authored["sections"]) == 1
        section = authored["sections"][0]
        assert section["kind"] == "jlptListening" and len(section["questions"]) == 2
        media = section["media"]
        assert media["url"].startswith("pending://") and media["harumii_audio_bound"] is False
        source = json.loads((ROOT / authored["source_snapshot"]).read_text(encoding="utf-8"))
        assert source["url"] == authored["source_url"]
        html = source["sections"][0]["html"]
        assert f'data-ml-sec="{section["source_group_id"].removeprefix("ml-")}"' in html
        item_count = html.count("data-ml-item=")
        empty_scripts = html.count('<div class="ml-script-body"></div>')
        assert item_count == empty_scripts and item_count > 0
        assert "data-answer=" not in html
        for q in section["questions"]:
            assert q["evidence_ja"] in media["script_ja"]
            assert q["evidence_ja"] in q["explanation_vi"]
            assert q["correct_choice_id"] in {c["id"] for c in q["choices"]}
            assert q["source_item_id"] is None
        asset = ROOT / media["local_asset"]
        assert asset.is_file()
        sha = hashlib.sha256(asset.read_bytes()).hexdigest()
        assert sha in media["verification"]
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(asset)], capture_output=True, text=True, check=True)
        duration = float(probe.stdout.strip())
        assert duration > 2
        subprocess.run(["ffmpeg", "-v", "error", "-i", str(asset), "-f", "null", "NUL"], capture_output=True, text=True, check=True)
        export = ROOT / "exports/curriculum-exercises/listening" / lesson_name
        index = json.loads((export / "index.json").read_text(encoding="utf-8"))
        row = index["sections"][0]
        assert row["paste_file"] is None and row["question_count"] == 2
        assert row["pending_audio_media_ids"] == [section["id"] + ".media"]
        storage = json.loads((export / row["storage_file"]).read_text(encoding="utf-8"))
        assert storage["format"] == "Listening" and storage["audioPath"] is None
        native = storage["content"]["jlpt_block"]
        assert native["mediaItems"][0]["audio"]["url"] == media["url"]
        assert native["mediaItems"][0]["audio"]["scriptJaMd"] == media["script_ja"]
        assert len(native["questions"]) == 2
        result.append({"lesson": lesson, "source_group_id": section["source_group_id"], "source_snapshot_items": item_count, "source_snapshot_empty_scripts": empty_scripts, "source_answers_verified": 0, "scope": "AI-authored supplemental", "script_ja": media["script_ja"], "audio_asset": media["local_asset"], "duration_seconds": duration, "bytes": asset.stat().st_size, "sha256": sha, "ffmpeg_full_decode": "pass", "native_export": str(export.relative_to(ROOT)).replace("\\", "/"), "questions": 2, "harumii_audio_bound": False})
    REPORT.write_text(json.dumps({"lessons": result}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"lessons": len(result), "questions": sum(x["questions"] for x in result), "full_decode": "pass", "binding": "pending"}, ensure_ascii=False))


if __name__ == "__main__":
    run()
