"""Editorial pass over N5 legacy grammar entries deferred by the structure audit.

Only emits an entry after the strict Harumii validator and a source-content audit.
Ambiguous dialogue pairings stay deferred for human review.
"""
from __future__ import annotations

import json
import re
import tempfile
from collections import Counter
from pathlib import Path

from grammar_upload import parse, validate_body
from grammar_upgrade_structure import convert, extract_pairs

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar"
OUT = ROOT / "authored/grammar-upload/2026-11-25-N5-editorial/N5"
AUDIT = ROOT / "reports/grammar-upgrade-2026-11-25-structure-audit.json"
REPORT = ROOT / "reports/grammar-upgrade-2026-11-25-N5-editorial.json"

# Explicit Japanese corrections established from the surrounding sentence and Vietnamese.
JAPANESE_FIX = {
    "3dc1b515": {"学校へ行いきます。": "学校へ行きます。"},
    "04ebe2be": {"（先生は）あそこにあります。": "（先生は）あそこにいます。"},
    "d3f4d38a": {"いいえ、 一度 も（ 食 べたことがありません。": "いいえ、一度も食べたことがありません。", "はい、２ 回来 たことがあります。": "はい、２回来たことがあります。"},
    "bd5c6fb1": {"私は先生に日本をいただきました。": "私は先生に本をいただきました。"},
    "acd79fea": {"彼女 は 昨日 と 同 じシャツを 着 ている。": "彼女は昨日と同じシャツを着ている。"},
    "2d042174": {"ごめん。もう食べました": "ごめん。もう食べました。", "はい、もう来ました": "はい、もう来ました。"},
    "d9c76709": {"紅茶で飲みに行きましょうか。": "紅茶を飲みに行きましょうか。"},
    "d1f4282f": {"すみません、電話が故障しているらしいんんですけど。": "すみません、電話が故障しているらしいんですけど。"},
}
VIETNAMESE_FIX = {
    "d1f4282f": {"Ngày mai tô phải đến công ty. Tuy là chủ nhật nhưng vì có việc…": "Ngày mai tôi phải đến công ty. Tuy là chủ nhật nhưng vì có việc…"},
    "f0cb6e5c": {"Chiều chủ nhật, chúng ta hãy cùng đá bóng nhé?": "Chiều thứ bảy, chúng ta hãy cùng đá bóng nhé?"},
    "7279d6c1": {"Chúng ta hãy đi vào kỳ nghĩ hè nhé.": "Chúng ta hãy đi vào kỳ nghỉ hè nhé."},
    "4574819e": {"Tớ được cho hẳn 10 man cơ đấy nhé.": "Tớ được cho hẳn 1 man cơ đấy nhé."},
}

# Short meanings replace source labels that omit a documented use or contain a wrong assertion.
MEANINGS = {
    "c8685c69": "Đánh dấu chủ thể hoặc đối tượng của trạng thái; nối mệnh đề với nghĩa nhưng",
    "3dc1b515": "Chỉ hướng hoặc đích đến của sự di chuyển và người nhận trong một số cách nói",
    "04ebe2be": "Diễn tả sự hiện diện của người hoặc động vật",
    "50198d60": "Diễn tả mong muốn thực hiện một hành động",
    "57bcd8c3": "Phân biệt nơi diễn ra hành động với nơi tồn tại hoặc đích đến",
    "6185d59d": "Diễn tả hành động ở quá khứ bằng dạng khẳng định hoặc phủ định lịch sự",
    "7279d6c1": "Đề nghị giúp người nghe hoặc cùng chọn cách thực hiện một việc",
    "fdb89b70": "Đánh dấu đối tượng của hành động, điểm rời đi hoặc đường đi qua",
}
STRUCTURE_RESTORE = {
    "b9aec5a1": ("Cách chia động từ sang thể た để kể việc đã xảy ra hoặc hoàn tất", ["Vて → Vた", "Vで → Vだ"]),
    "169197ef": ("Cách chia động từ sang thể て／で để nối với các mẫu ngữ pháp khác", ["Vます → Vて／Vで（theo nhóm động từ）"]),
    "3195653a": ("Dạng thông thường của động từ và tính từ dùng trong lời nói thân mật và mệnh đề phụ", ["Vます／Vません／Vました／Vませんでした → Vる／Vない／Vた／Vなかった"]),
    "bcefb395": ("Chia tính từ い và tính từ な sang dạng phủ định hiện tại hoặc quá khứ", ["Aい（bỏ い）＋くない／くなかった", "Aな＋じゃない／じゃなかった"]),
    "3dac0571": ("Phân biệt từ chỉ gần người nói, gần người nghe, xa cả hai và từ để hỏi", ["こ／そ／あ／ど＋chỉ thị từ（これ・それ・あれ・どれ）"]),
}


def normalize_h5(body, uid8):
    """Number unnumbered Japanese turns when each already has an adjacent translation."""
    out = []
    changed = []
    pending_role = None
    for i, line in enumerate(body):
        if not line.startswith("##### "):
            if line.startswith("###### "):
                role_in_translation = re.match(r"^(######\s*→\s*)(A|B)\s*[:：]\s*", line)
                if role_in_translation:
                    pending_role = pending_role or role_in_translation.group(2)
                    line = role_in_translation.group(1) + line[role_in_translation.end():]
                for old, new in VIETNAMESE_FIX.get(uid8, {}).items():
                    if old in line:
                        changed.append({"kind": "correct_Vietnamese", "before": old, "after": new})
                        line = line.replace(old, new)
            out.append(line)
            if pending_role and re.match(r"^######\s*→\s*", line):
                out.append(f"*Lượt thoại: {pending_role}.*")
                pending_role = None
            continue
        raw = line[6:].strip()
        numbered = re.fullmatch(r"\d+\.\s*(.+)", raw)
        ja = numbered.group(1).strip() if numbered else raw
        role_match = re.match(r"^(?:(A|B)\s*[:：]?\s*(?=[「『])|(A|B)\s*[:：]\s*|(ー)\s*|(店員)：)", ja)
        if role_match:
            role = next((x for x in role_match.groups() if x), None)
            pending_role = "đáp" if role == "ー" else role
            ja = ja[role_match.end():].strip()
            changed.append({"kind": "move_dialogue_role_below_translation", "role": pending_role})
        if not numbered:
            next_nonblank = next((s for s in body[i + 1:] if s.strip()), "")
            if not re.match(r"^######\s*→\s*", next_nonblank):
                raise ValueError(f"unnumbered_H5_not_adjacent_to_translation: {raw!r} -> {next_nonblank!r}")
            if not ja or not re.search(r"[ぁ-んァ-ヶ一-龯]", ja):
                raise ValueError("unnumbered_H5_not_Japanese_sentence")
            changed.append({"kind": "number_dialogue_turn", "before": raw, "after": ja})
        fixed = JAPANESE_FIX.get(uid8, {}).get(ja)
        if fixed:
            changed.append({"kind": "correct_Japanese", "before": ja, "after": fixed})
            ja = fixed
        out.append(f"##### 999. {ja}")
    return out, changed


def reorder_dialogue_pairs(body):
    """Pair consecutive Japanese and Vietnamese dialogue turns in their source order."""
    result, edits = [], []
    i = 0
    while i < len(body):
        if not body[i].startswith("##### "):
            result.append(body[i])
            i += 1
            continue
        j = i
        while j < len(body) and (not body[j].strip() or body[j].startswith(("##### ", "###### "))):
            j += 1
        segment = body[i:j]
        ja = [x for x in segment if x.startswith("##### ")]
        vi = [x for x in segment if x.startswith("###### ")]
        if len(ja) > 1 and len(ja) == len(vi):
            result.extend(x for pair in zip(ja, vi) for x in (pair[0], pair[1], ""))
            edits.append({"kind": "pair_dialogue_turns", "count": len(ja)})
        else:
            result.extend(segment)
        i = j
    return result, edits


def duplicate_comparison_translations(body):
    """The に/で comparison has two written variants sharing one Vietnamese gloss."""
    result, edits = [], []
    i = 0
    while i < len(body):
        if not body[i].startswith("##### "):
            result.append(body[i])
            i += 1
            continue
        j = i
        while j < len(body) and (not body[j].strip() or body[j].startswith(("##### ", "###### "))):
            j += 1
        segment = body[i:j]
        ja = [x for x in segment if x.startswith("##### ")]
        vi = [x for x in segment if x.startswith("###### ")]
        if len(ja) == 2 and len(vi) == 1:
            result.extend([ja[0], vi[0], "", ja[1], vi[0], ""])
            edits.append({"kind": "share_comparison_translation", "Japanese": ja, "Vietnamese": vi[0]})
        else:
            result.extend(segment)
        i = j
    return result, edits


def reclassify_conjugation_forms(body):
    """The て-form page lists conjugations, not Japanese sentence examples."""
    result, edits = [], []
    i = 0
    while i < len(body):
        line = body[i]
        if not line.startswith("##### "):
            result.append(line)
            i += 1
            continue
        form = re.sub(r"^\d+\.\s*", "", line[6:].strip())
        match = re.fullmatch(r"(\S+?)\s*(?::\s*([^→]+?))?\s*→\s*(\S+)", form)
        j = i + 1
        while j < len(body) and not body[j].strip():
            j += 1
        if not match or j >= len(body) or not body[j].startswith("###### → "):
            raise ValueError("ambiguous_conjugation_form")
        source, embedded_gloss, target = match.groups()
        translation = body[j][len("###### → "):].strip()
        translated = re.fullmatch(r"\S+\s*:\s*(.+?)\s*→\s*\S+", translation)
        if not translated:
            raise ValueError("ambiguous_conjugation_gloss")
        gloss = translated.group(1).strip()
        if embedded_gloss and embedded_gloss.strip() != gloss:
            raise ValueError("conjugation_gloss_mismatch")
        gloss = {"Ân": "Ấn", "Làm, vẽ": "Làm", "Đi": "Đến" if source == "きます" else "Đi"}.get(gloss, gloss)
        result.append(f"- **{source} → {target}** — {gloss}")
        edits.append({"kind": "reclassify_conjugation_form", "source": source, "target": target, "gloss_vi": gloss})
        i = j + 1
    if len(edits) != 29:
        raise ValueError("conjugation_form_count_changed")
    return result, edits


def prepare(path):
    h, body = parse(path)
    uid8 = h["id"][:8]
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    end = lines.index("---", 1)
    edits = []
    if uid8 in STRUCTURE_RESTORE:
        meaning, structures = STRUCTURE_RESTORE[uid8]
        h["description"] = meaning
        first_h1 = next((i for i, line in enumerate(body) if line.startswith("# ")), None)
        if first_h1 is None:
            raise ValueError("missing_H1_for_structure_restore")
        old_tail = body[first_h1 + 1:]
        body = ["# " + h["name"], "", meaning, "", "---", "", "## Cấu trúc ngữ pháp", ""]
        body += ["> **" + s + "**" + ("<br>" if i + 1 < len(structures) else "") for i, s in enumerate(structures)]
        body += ["", "## Cách dùng", ""] + old_tail
        edits.append({"kind": "editorial_structure_restore", "meaning": meaning, "structures": structures})
    if uid8 == "89b98a33":
        point = body.index("## Cấu trúc 1")
        body = ["# " + h["name"], "", h["description"], "", "---", "", "## Cấu trúc ngữ pháp", ""] + body[point + 1:]
        edits.append({"kind": "restore_H1_and_main_structure", "before": "legacy unheaded prelude", "after": h["name"]})
        for i, line in enumerate(body):
            if line.startswith("###### ") and not re.match(r"^######\s*→", line):
                body[i] = "*" + line[7:].strip() + "*"
                edits.append({"kind": "move_context_note_below_translation", "before": line, "after": body[i]})
    if uid8 == "57bcd8c3":
        heading = body.index("## Cấu trúc ngữ pháp")
        body = ["# " + h["name"], "", h.get("description") or MEANINGS[uid8], "", "---", ""] + body[heading:]
        edits.append({"kind": "restore_meaning_prelude", "after": MEANINGS[uid8]})
        for i, line in enumerate(body):
            if "「Địa điểm + **に**」: Diễn tả **hành động**" in line:
                fixed = line.replace("「Địa điểm + **に**」: Diễn tả **hành động**", "「Địa điểm + **で**」: Diễn tả **hành động**")
                edits.append({"kind": "correct_Vietnamese_rule", "before": line, "after": fixed})
                body[i] = fixed
            if "👉" in body[i]:
                old = body[i]
                body[i] = body[i].replace("👉", "-")
                edits.append({"kind": "replace_emoji_marker", "before": old, "after": body[i]})
        body, pair_edits = duplicate_comparison_translations(body)
        edits += pair_edits
        use = body.index("## Ví dụ")
        body[use + 1:use + 1] = ["", "*Ví dụ 母に手紙を書きます dùng に cho người nhận, ngoài hai cách dùng chỉ địa điểm đang so sánh.*", ""]
        edits.append({"kind": "clarify_other_ni_use", "after": "Ví dụ 9 dùng に cho người nhận"})
    # A legacy H1 may use an abbreviated display name; use the baseline metadata name.
    first = next((i for i, s in enumerate(body) if s.strip()), None)
    if first is not None and body[first].startswith("# ") and body[first] != "# " + h["name"]:
        edits.append({"kind": "H1_match_name", "before": body[first], "after": "# " + h["name"]})
        body[first] = "# " + h["name"]
    if "## Cấu trúc ngữ pháp" not in body:
        aliases = [i for i, s in enumerate(body) if s in {"## Cấu trúc", "## Cấu Trúc ngữ pháp"}]
        if len(aliases) == 1:
            old = body[aliases[0]]
            body[aliases[0]] = "## Cấu trúc ngữ pháp"
            edits.append({"kind": "structure_heading", "before": old, "after": body[aliases[0]]})
    if uid8 == "719d2ed0" and "## Cấu trúc ngữ pháp" not in body:
        pos = next(i for i, s in enumerate(body) if s.startswith("> **"))
        body[pos:pos] = ["## Cấu trúc ngữ pháp", ""]
        edits.append({"kind": "restore_structure_heading", "after": "## Cấu trúc ngữ pháp"})
    if uid8 == "fdb89b70":
        old = "***N  +  を  +  V   です。***"
        if old in body:
            body[body.index(old)] = "> **N ＋ を ＋ V**"
            edits.append({"kind": "correct_structure", "before": old, "after": "> **N ＋ を ＋ V**"})
    if uid8 == "d5746c92":
        notes = []
        for i, line in enumerate(body):
            match = re.fullmatch(r"> \*\*(.+?)\*\* \((.+)\)\s*", line)
            if match:
                body[i] = f"> **{match.group(1)}**"
                notes.append(f"- **{match.group(1)}**: {match.group(2)}.")
                edits.append({"kind": "move_structure_note", "before": line.strip(), "after": body[i]})
        if notes:
            use = body.index("## Cách dùng / Ý nghĩa")
            body[use + 1:use + 1] = ["", *notes, ""]
    if uid8 == "04201d11":
        images = [line for line in body if line.startswith("![")]
        if len(images) != 1:
            raise ValueError("image_structure_count")
        image = images[0]
        body[body.index(image)] = "> **こちら／そちら／あちら／どちら**"
        use = body.index("## Cách dùng / Ý nghĩa")
        body[use + 1:use + 1] = ["", image, ""]
        edits.append({"kind": "preserve_image_after_structure", "image": image})
        for i, line in enumerate(body):
            if "「こちら」「そちら」「こちら」" in line:
                fixed = line.replace("「こちら」「そちら」「こちら」", "「こちら」「そちら」「あちら」")
                edits.append({"kind": "correct_Vietnamese_rule", "before": line, "after": fixed})
                body[i] = fixed
            if line == "##### ３. どこ Và どちら":
                body[i] = "### どこ と どちら"
                edits.append({"kind": "reclassify_subheading", "before": line, "after": body[i]})
    if uid8 == "169197ef":
        for i, line in enumerate(body):
            if "Bỏ ます, đổi き thành いで" in line:
                fixed = line.replace("Bỏ ます, đổi き thành いで", "Bỏ ます, đổi ぎ thành いで")
                edits.append({"kind": "correct_Vietnamese_rule", "before": line, "after": fixed})
                body[i] = fixed
        body, form_edits = reclassify_conjugation_forms(body)
        edits += form_edits
    if uid8 in {"50198d60", "7a4bd08a", "b8bb9cf8", "2c221ed9"}:
        for i, line in enumerate(body):
            if line.startswith("###### ") and not re.match(r"^######\s*→", line):
                text = line[7:].strip()
                if text.startswith("**"):
                    text = text.replace("**", "").strip()
                    body[i] = "### " + text
                else:
                    body[i] = text
                edits.append({"kind": "reclassify_commentary", "before": line, "after": body[i]})
        if uid8 == "50198d60":
            for i, line in enumerate(body):
                if line.startswith("##### ") and "Ta sẽ nói:" in line:
                    body[i] = line[6:].strip()
                    edits.append({"kind": "reclassify_editorial_cue", "before": line, "after": body[i]})
    body, pair_edits = reorder_dialogue_pairs(body)
    edits += pair_edits
    # The generic audit only deferred unnumbered H5. Keep other structures for hand review.
    body, turn_edits = normalize_h5(body, uid8)
    edits += turn_edits
    if uid8 in MEANINGS:
        old = h.get("description", "")
        h["description"] = MEANINGS[uid8]
        edits.append({"kind": "editorial_meaning", "before": old, "after": h["description"]})
        # Preserve the original introductory sentence in the body; the converter will
        # replace the top quote, so its wording is documented in the audit record.
        for i in range((first or 0) + 1, len(body)):
            if body[i].strip() and body[i].strip() != "---":
                if body[i].startswith(("## ", "##### ")):
                    break
                body[i] = h["description"]
                break
    header = ["---"]
    for key in ("id", "jlpt", "name", "description", "conjugation"):
        if key in h:
            header.append(f"{key}: {json.dumps(h[key], ensure_ascii=False)}")
    header += ["---"]
    return "\n".join(header + body) + "\n", edits


def run():
    entries = json.loads(AUDIT.read_text(encoding="utf-8"))["entries"]
    deferred = [x for x in entries if x["status"] == "deferred" and x["file"].startswith("N5/")]
    results = []
    OUT.mkdir(parents=True, exist_ok=True)
    for entry in deferred:
        source = BASE / entry["file"]
        row = {"file": entry["file"], "id": entry["id"], "prior_reason": entry["reason"]}
        try:
            original_header, original_body = parse(source)
            original_h5 = sum(line.startswith("##### ") for line in original_body)
            original_h6 = sum(line.startswith("###### ") for line in original_body)
            original_images = [line for line in original_body if "![" in line]
            prepared, edits = prepare(source)
            with tempfile.TemporaryDirectory() as tmp:
                work = Path(tmp) / source.name
                work.write_text(prepared, encoding="utf-8")
                converted, pairs, images = convert(work)
            expected_pairs = 0 if source.name.endswith("__169197ef.md") else original_h5 - (1 if source.name.endswith(("__50198d60.md", "__04201d11.md")) else 0)
            if pairs != expected_pairs or images != len(original_images):
                raise ValueError("source_example_or_image_count_mismatch")
            target = OUT / source.name
            target.write_text(converted, encoding="utf-8")
            h, body = parse(target)
            validate_body(body, h["name"], target)
            row.update(status="candidate", pairs=pairs, images=images, edits=edits, target=str(target.relative_to(ROOT)).replace("\\", "/"), content_review="editorial_rules_applied; human_review_pending")
        except (ValueError, AssertionError, KeyError, TypeError, IndexError) as exc:
            row.update(status="deferred", reason=str(exc).split(":", 1)[0])
        results.append(row)
    REPORT.write_text(json.dumps({"summary": {"N5_deferred_baseline": len(deferred), "candidate": sum(x["status"] == "candidate" for x in results), "still_deferred": sum(x["status"] == "deferred" for x in results), "reasons": dict(Counter(x.get("reason") for x in results if x["status"] == "deferred"))}, "entries": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(json.loads(REPORT.read_text(encoding="utf-8"))["summary"], ensure_ascii=False))


if __name__ == "__main__":
    run()
