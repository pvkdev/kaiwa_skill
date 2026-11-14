import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
WORK = Path(__file__).parent
V61 = ROOT / "kaiwa_skill/planning/v6_1"
INDEX = {x["unit_id"]: x for x in json.loads((WORK / "unit_index.json").read_text(encoding="utf8"))}
STAGES = {x["display_code"]: x for x in map(json.loads, (ROOT / "kaiwa_skill/planning/v5/KAIWA_CHANG_V5.jsonl").read_text(encoding="utf8").splitlines())}

def select(stage, item):
    uid = item["uid"]
    if uid == "u-180-f-023":
        x = INDEX[uid]
        y = INDEX["u-180-f-024"]
        return {"kind": item["kind"], "book_id": x["book_id"], "book_title": x["book_title"],
                "unit_id": uid, "title_ja": "23. 手とり足とり", "source_number_prefix": "23. ",
                "path": x["path"], "sha256": x["sha256"], "start_line": x["start_line"],
                "end_line": y["end_line"], "pack_id": "B20/CD-12-23-24",
                "boundary": f"Trọn CD 12 gồm bài 23 手とり足とり và bài 24 一から十まで, lời giải thích và bốn Listen & Speak, dòng {x['start_line']}–{y['end_line']}; dừng trước anchor bài 25.",
                "audio": [{"disc": None, "track": "CD 12", "locator": f"B20 Section F, bài 23–24; icon CD 12 ở bài 23 và _meta/audio.json; {x['path']} dòng {x['start_line']}–{y['end_line']}"}],
                "audio_note": "Icon CD 12 ở bài 23; bài 24 tiếp cùng nhóm trước CD 13. Đối chiếu _meta/audio.json, chưa nghe file audio.",
                "situation_ids": item["situations"], "fit_vi": item["fit"],
                "difficulty_vi": item["difficulty"], "read_status": "whole_unit_read"}
    if uid == "u-shadow-mid-u8-presentation-p0164":
        x = INDEX[uid]
        return {"kind": item["kind"], "book_id": x["book_id"], "book_title": x["book_title"],
                "unit_id": uid, "title_ja": "プレゼンテーション", "path": x["path"], "sha256": x["sha256"],
                "start_line": x["start_line"], "end_line": x["end_line"],
                "pack_id": f"B13/{uid}", "boundary": f"Trọn bài プレゼンテーション từ lời giới thiệu đến bốn đoạn về biểu đồ, doanh số, so sánh đối thủ và kết luận tạm, dòng {x['start_line']}–{x['end_line']}; dừng trước anchor bài tiếp theo.",
                "audio": [{"disc": "DISK 2", "track": "31", "locator": f"{uid}; {x['path']} dòng {x['start_line']}–{x['end_line']}"}],
                "audio_note": "Nhãn DISK 2 / 31 in ở tiêu đề bài; chưa nghe file audio.",
                "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
                "read_status": "whole_unit_read"}
    if uid == "u-m-p0124-intro":
        path = next((ROOT / "kaiwa_skill/knowledge").glob("シャドーイング 日本語を話そう 就職*")) / "chapters/15-unit3-4.md"
        data = path.read_bytes()
        lines = data.decode("utf-8-sig").splitlines()
        labels = [(i, m.group(1), m.group(2)) for i, line in enumerate(lines, 1)
                  if (m := re.search(r"^#+[^\n]*DISC\s+(\d+)\s*/\s*(\d+)", line, flags=re.I))]
        return {"kind": item["kind"], "book_id": "INTERVIEW", "book_title": path.parents[1].name,
                "unit_id": uid, "title_ja": "3-4　個人面接③：通し練習（入室から退室まで）", "source_number_prefix": "3-4　",
                "path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(data).hexdigest(),
                "start_line": 1, "end_line": len(lines), "pack_id": "INTERVIEW/u3-4-full-interviews",
                "boundary": f"Trọn chương 3-4 個人面接③：通し練習（入室から退室まで）, lời dẫn, ba cuộc phỏng vấn mô phỏng và POINT, đủ DISC 2 / 22–24 theo thứ tự, dòng 1–{len(lines)} đến hết chương.",
                "audio": [{"disc": "DISC " + disc, "track": track,
                            "locator": f"3-4 個人面接③, tiêu đề track dòng {line}; {path.relative_to(ROOT).as_posix()}"}
                           for line, disc, track in labels],
                "audio_note": "Đối chiếu đủ ba nhãn DISC 2 / 22–24 trong chương clean; chưa nghe file audio.",
                "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
                "read_status": "whole_unit_read"}
    if uid == "u-m-p0106-intro":
        path = next((ROOT / "kaiwa_skill/knowledge").glob("シャドーイング 日本語を話そう 就職*")) / "chapters/14-unit3-3.md"
        data = path.read_bytes()
        lines = data.decode("utf-8-sig").splitlines()
        labels = [(i, m.group(1), m.group(2)) for i, line in enumerate(lines, 1)
                  if (m := re.search(r"^#+[^\n]*DISC\s+(\d+)\s*/\s*(\d+)", line, flags=re.I))]
        return {"kind": item["kind"], "book_id": "INTERVIEW", "book_title": path.parents[1].name,
                "unit_id": uid, "title_ja": "3-3　個人面接②：志望動機", "source_number_prefix": "3-3　",
                "path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(data).hexdigest(),
                "start_line": 1, "end_line": len(lines), "pack_id": "INTERVIEW/u3-3-motivation",
                "boundary": "Trọn chương 3-3 個人面接②：志望動機, hướng dẫn mở đầu, 19 cuộc hỏi đáp và POINT, đủ DISC 2 / 14–21 theo thứ tự, dòng 1–384 đến hết chương.",
                "audio": [{"disc": "DISC " + disc, "track": track,
                            "locator": f"3-3 個人面接②：志望動機, tiêu đề track dòng {line}; {path.relative_to(ROOT).as_posix()}"}
                           for line, disc, track in labels],
                "audio_note": "Đối chiếu đủ tám nhãn DISC 2 / 14–21 trong chương clean; chưa nghe file audio.",
                "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
                "read_status": "whole_unit_read"}
    if uid == "u-m-p0153-men-set-su":
        path = next((ROOT / "kaiwa_skill/knowledge").glob("シャドーイング 日本語を話そう 就職*")) / "chapters/18-komatta-toki.md"
        data = path.read_bytes()
        return {"kind": item["kind"], "book_id": "INTERVIEW", "book_title": path.parents[1].name,
                "unit_id": uid, "title_ja": "困ったときの答え方・フレーズ集",
                "path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(data).hexdigest(),
                "start_line": 1, "end_line": len(data.decode("utf-8-sig").splitlines()),
                "pack_id": "INTERVIEW/komatta-toki", "boundary": "Trọn chương 困ったときの答え方・フレーズ集: ba phần 面接で, 電話で, 面接の前に; mọi mẫu khi chưa đáp ngay, không nghe rõ, gọi lại và đến muộn, dòng 1–94 đến hết chương.",
                "audio": [], "audio_note": "Chương clean không ghi DISC/track riêng cho bảng mẫu; chưa xác minh file nghe.",
                "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
                "read_status": "whole_unit_read"}
    if uid == "u-shadow-mid-u8-interview-p0158":
        x = INDEX[uid]
        return {"kind": item["kind"], "book_id": x["book_id"], "book_title": x["book_title"],
                "unit_id": uid, "title_ja": "就職面接", "path": x["path"], "sha256": x["sha256"],
                "start_line": x["start_line"], "end_line": x["end_line"],
                "pack_id": f"B13/{uid}", "boundary": f"Trọn bài 就職面接, một cuộc phỏng vấn từ câu hỏi muốn làm gì tại công ty đến lý do muốn làm ở Nhật, dòng {x['start_line']}–{x['end_line']}; dừng trước anchor bài tiếp theo.",
                "audio": [{"disc": "DISK 2", "track": "28", "locator": f"{uid}; {x['path']} dòng {x['start_line']}–{x['end_line']}"}],
                "audio_note": "Nhãn DISK 2 / 28 in ở tiêu đề bài; chưa nghe file audio.",
                "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
                "read_status": "whole_unit_read"}
    if uid in {"u-p3-head-057", "u-p3-head-061"}:
        pilot = "S-049.json" if uid == "u-p3-head-057" else "S-040.json"
        canonical = json.loads((V61 / "decisions" / pilot).read_text(encoding="utf8"))
        template = next(s for s in canonical["selections"] if s["book_id"] == "B19" and s["unit_id"] == uid)
        return {**template, "kind": item["kind"], "situation_ids": item["situations"],
                "fit_vi": item["fit"], "difficulty_vi": item["difficulty"]}
    if uid == "u-i-75":
        canonical = json.loads((V61 / "decisions/S-072.json").read_text(encoding="utf8"))
        template = next(s for s in canonical["selections"] if s["book_id"] == "B24" and s["unit_id"] == uid)
        return {**template, "kind": item["kind"], "situation_ids": item["situations"],
                "fit_vi": item["fit"], "difficulty_vi": item["difficulty"]}
    x = INDEX[uid]
    h = x["heading"]
    title = h.split(" — ")[0]
    if x["book_id"] in {"B11", "B12", "B18"}:
        title = h
    prefix = re.match(r"^(Unit [0-9]+ |\([0-9]+\) |[0-9]+\. |[0-9]+　\([0-9]+\) |[0-9]+　|[0-9]+ )", title)
    marker = re.search(r"CD-(\d+)\s*/?\s*(\d+)", x["text"])
    if marker:
        audio = [{"disc": "CD-" + marker.group(1), "track": marker.group(2), "locator": f"{uid}; {x['path']} dòng {x['start_line']}–{x['end_line']}"}]
        audio_note = "Nhãn CD/track và phần chữ xác minh trong chapter clean; chưa nghe file audio thực tế."
    else:
        marker = re.search(r"CD[:：]?\s+(\d+)", x["text"])
        voice = re.search(r"音声\s*(\d+)", x["text"])
        label = "CD " + marker.group(1) if marker else "音声 " + voice.group(1) if voice else None
        audio = [{"disc": None, "track": label, "locator": f"{uid}; {x['path']} dòng {x['start_line']}–{x['end_line']}"}] if label else []
        audio_note = "Nhãn audio trong chapter clean; số đĩa và file nghe chưa xác minh." if label else "Chapter clean không gắn track riêng cho đơn vị; chưa xác minh audio thực tế."
    return {"kind": item["kind"], "book_id": x["book_id"], "book_title": x["book_title"],
            "unit_id": uid, "title_ja": title, "path": x["path"], "sha256": x["sha256"],
            "start_line": x["start_line"], "end_line": x["end_line"],
            "pack_id": f"{x['book_id']}/{uid}",
            "boundary": f"Trọn đơn vị {uid} từ anchor dòng {x['start_line']} qua toàn bộ lời giải thích, ví dụ/câu luyện đến dòng {x['end_line']}; kết thúc trước anchor đơn vị kế tiếp.",
            "audio": audio, "audio_note": audio_note,
            "situation_ids": item["situations"], "fit_vi": item["fit"], "difficulty_vi": item["difficulty"],
            "read_status": "whole_unit_read", **({"source_number_prefix": prefix.group()} if prefix else {})}

def main(path):
    spec = json.loads(Path(path).read_text(encoding="utf8"))
    stage = STAGES[spec["code"]]
    decision = {"stage_uid": stage["uid"], "display_code": spec["code"],
                "vocabulary_topics": spec["topics"], "search_notes": spec["notes"],
                "selections": [select(stage, item) for item in spec["selections"]],
                "considerations": spec.get("considerations", [])}
    target = V61 / "decisions" / f"{spec['code']}.json"
    text = json.dumps(decision, ensure_ascii=False, indent=2) + "\n"
    with target.open("x", encoding="utf8") as f:
        f.write(text)
    print(target)

if __name__ == "__main__":
    main(sys.argv[1])
