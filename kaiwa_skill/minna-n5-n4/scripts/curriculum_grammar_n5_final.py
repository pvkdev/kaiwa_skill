"""Manually resolve N5 legacy grammar entries left by the editorial structure pass.

The batch is separate because these sources contain form tables, variant lists and
shared dialogue translations that cannot safely be treated as sentence examples.
"""
from __future__ import annotations

import html
import json
import re
from collections import Counter
from pathlib import Path

from grammar_upload import parse, validate_body

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar/N5"
OUT = ROOT / "authored/grammar-upload/2026-11-25-N5-final/N5"
AUDIT = ROOT / "reports/grammar-upgrade-2026-11-25-N5-editorial.json"
REPORT = ROOT / "reports/grammar-upgrade-2026-11-25-N5-final.json"

EDITORIAL = {
    "4fb29356": ("Cách chia động từ sang thể từ điển theo ba nhóm", ["Vます → Vる／Vう（theo nhóm động từ）"]),
    "d6225fc2": ("Cách chia động từ sang thể phủ định ない theo ba nhóm", ["Vます → Vない（theo nhóm động từ）"]),
    "e14aee6b": ("Cách đọc số và dùng trợ số từ để đếm người, vật, thời gian", ["Số đếm ＋ trợ số từ（人・本・枚・個…）"]),
    "b8bb9cf8": ("Diễn tả việc cần phải làm bằng ないといけない／だめだ", ["Vない ＋ といけない", "Vない ＋ とだめだ", "N／Aな ＋ でないといけない", "Aい（bỏ い）＋くないといけない"]),
    "ab5c0e07": ("Diễn tả sự bắt buộc bằng なくてはいけない／なくちゃいけない", ["Vなくてはいけない", "Vなくちゃいけない", "N／Aな ＋ でなくてはいけない", "Aい（bỏ い）＋くなくてはいけない"]),
    "f30c54cc": ("Diễn tả sự bắt buộc bằng なければなりません", ["Vない（bỏ ない）＋ なければなりません"]),
    "26c62437": ("Phân biệt だけ chỉ giới hạn và しか đi với vị ngữ phủ định", ["N／V ＋ だけ", "N ＋ しか ＋ Vない"]),
    "4f31090e": ("Dùng tiền tố お／ご để nói lịch sự về người khác hoặc sự việc liên quan", ["お ＋ từ thuần Nhật", "ご ＋ từ Hán Nhật（có ngoại lệ）"]),
    "25ca71cb": ("Diễn tả sắc thái và thái độ bằng các trợ từ đứng cuối câu", ["Câu ＋ trợ từ cuối câu（ね・よ・ぞ・かな…）"]),
    "46c8ddc5": ("Phân biệt は đánh dấu chủ đề và が đánh dấu chủ thể hoặc trọng tâm mới", ["N ＋ は ＋ nhận xét về chủ đề", "N ＋ が ＋ vị ngữ"]),
}
EXPECTED_RECLASSIFIED_H5 = {
    "4fb29356": 1, "d6225fc2": 27, "25ca71cb": 0, "4f31090e": 5,
    "26c62437": 8, "46c8ddc5": 9, "e14aee6b": 0,
    "b8bb9cf8": 10, "ab5c0e07": 12, "f30c54cc": 12,
}


def body_tail(body, uid):
    """Keep source teaching content after its old H1 and introduction."""
    h1 = next(i for i, line in enumerate(body) if line.startswith("# "))
    start = next(i for i in range(h1 + 1, len(body)) if body[i] == "---") + 1
    tail = body[start:]
    if uid == "4f31090e":
        # Its introduction is before the first divider and remains in the new meaning.
        pass
    return tail


def form_bullets(tail, uid, changes):
    result = []
    for line in tail:
        if not line.startswith("##### "):
            result.append(line)
            continue
        raw = re.sub(r"^\*?\d+\.\s*", "", line[6:].strip()).strip("*")
        if uid == "4fb29356" and "→" not in raw and "、" in raw:
            result.append("- **Đuôi nhóm 1:** " + raw)
            changes.append("moved_group1_endings_to_rule")
            continue
        if uid == "4fb29356" and "→" not in raw:
            result.append(line)
            continue
        match = re.fullmatch(r"([^→]+?)\s*→\s*(.+)", raw)
        if not match:
            raise ValueError("form_table_not_parseable")
        source, target = (part.strip() for part in match.groups())
        if uid == "d6225fc2" and source == "きます" and target == "きない":
            source, target = "着ます", "着ない"
        elif uid == "d6225fc2" and source == "きます" and target == "こない":
            source, target = "来ます", "来ない"
        result.append(f"- **{source} → {target}**")
        changes.append("reclassified_conjugation_form")
    return result


def obligation_variants(tail, uid, changes):
    result = []
    i = 0
    while i < len(tail):
        line = tail[i]
        if line.startswith("###### ") and not re.match(r"^######\s*→", line):
            result.append("### " + line[7:].replace("**", "").strip())
            changes.append("reclassified_commentary")
            i += 1
            continue
        if line.startswith("##### ") and ("『" in line or line.startswith("##### →")):
            label = line[6:].strip()
            if label.startswith("→"):
                # Already consumed with its preceding variant label.
                raise ValueError("orphan_variant_example")
            j = i + 1
            while j < len(tail) and not tail[j].strip():
                j += 1
            if j >= len(tail) or not tail[j].startswith("##### →"):
                raise ValueError("variant_example_missing")
            example = tail[j][len("##### →"):].strip().replace("勉強しきゃならない", "勉強しなきゃならない")
            label = re.sub(r"^\d+\.\s*", "", label).strip()
            result.append(f"- **{label}**: {example}")
            changes.append("reclassified_variant_as_rule")
            i = j + 1
            continue
        if uid == "b8bb9cf8" and "行かないといけなった" in line:
            line = line.replace("行かないといけなった", "行かないといけなかった")
            changes.append("corrected_Japanese_past_obligation")
        if uid == "b8bb9cf8" and "Tôi đã không đến đó thì không được." in line:
            line = line.replace("Tôi đã không đến đó thì không được.", "Tôi đã phải đến đó.")
            changes.append("corrected_Vietnamese_past_obligation")
        if uid == "b8bb9cf8" and "Không tới giờ học là không được đâu. (Phải tới lớp học đấy)" in line:
            line = line.replace("Không tới giờ học là không được đâu. (Phải tới lớp học đấy)", "Bạn phải tham dự buổi học đấy.")
            changes.append("corrected_Vietnamese_obligation")
        if uid == "f30c54cc" and "受けなればならない" in line:
            line = line.replace("受けなればならない", "受けなければならない")
            changes.append("corrected_Japanese_obligation")
        result.append(line)
        i += 1
    return result


def only_comparison(tail, changes):
    # This legacy article marks an accepted だけに ordering with X. Preserve all
    # eight variants as an explained comparison, then retain its six sentence pairs.
    anchor = next(i for i, line in enumerate(tail) if line.startswith("**3. Ngoài ra"))
    last = tail[anchor:]
    result = [
        "## Cách dùng 1: Giới hạn với だけ và しか", "",
        "だけ thường đi với khẳng định nhưng cũng có thể xuất hiện trong câu phủ định; しか cần vị ngữ phủ định.", "",
        "##### 1. 洋子だけが出席した。", "###### → Chỉ có Yoko tham dự.", "",
        "##### 2. 洋子しか出席しなかった。", "###### → Chỉ có Yoko tham dự.", "",
        "##### 3. 一万ドンだけあります。", "###### → Chỉ có mười nghìn đồng.", "",
        "##### 4. 一万ドンしかありません。", "###### → Chỉ có mười nghìn đồng.", "",
        "## Cách dùng 2: Vị trí cạnh trợ từ", "",
        "に／で có thể xuất hiện trước hoặc sau だけ, với sắc thái khác nhau. Với しか, trợ từ đứng trước しか.", "",
        "- **あなたにだけお知らせします。** — Chỉ báo cho riêng bạn. (Đúng)",
        "- **あなただけにお知らせします。** — Chỉ báo cho bạn, không báo cho người khác. (Đúng; nguồn đánh dấu X sai)",
        "- **あなたにしか知らせなかった。** — Chỉ báo cho bạn. (Đúng)",
        "- **あなたしかに知らせなかった。** — Sai vị trí trợ từ.",
        "- **公園でだけ遊んだ。** — Chỉ chơi ở công viên. (Đúng)",
        "- **公園だけで遊んだ。** — Chỉ chơi ở công viên. (Đúng, nhấn vào địa điểm)",
        "- **公園でしか遊ばなかった。** — Chỉ chơi ở công viên. (Đúng)",
        "- **公園しかで遊ばなかった。** — Sai vị trí trợ từ.", "",
        "## Cách dùng 3: だけ đi sau các loại từ khác", "",
    ]
    result += [line.replace("**", "") if line.startswith(("##### ", "###### ")) else line for line in last]
    changes += ["split_shared_translation_for_four_examples", "reclassified_eight_validity_variants", "corrected_dake_ni_validity"]
    return result


def honorific_prefixes(tail, changes):
    # Source first two comparisons put two H5 sentences before one combined
    # Vietnamese translation; split these without changing either utterance.
    joined = "\n".join(tail)
    for ja1, ja2, vi1, vi2 in [
        ("私の仕事は日本語の先生です。", "田村さんの**お**仕事は銀行員ですね。", "Công việc của tôi là giáo viên tiếng Nhật.", "Công việc của anh chị Tamura là nhân viên ngân hàng nhỉ."),
        ("私の趣味は読書です。", "田村さんの**ご**趣味は水泳ですね。", "Sở thích của tôi là đọc sách.", "Sở thích của chị Tamura là bơi lội nhỉ."),
    ]:
        pattern = re.compile(r"##### " + re.escape(ja1) + r"\n\s*##### " + re.escape(ja2) + r"\n\s*###### →[^\n]*\n→[^\n]*")
        replacement = f"##### {ja1}\n###### → {vi1}\n\n##### {ja2.replace('**', '')}\n###### → {vi2}"
        joined, count = pattern.subn(lambda _: replacement, joined, count=1)
        if count != 1:
            raise ValueError("honorific_shared_translation_not_found")
        changes.append("split_shared_honorific_translation")
    result = joined.splitlines()
    for i, line in enumerate(result):
        if line.startswith("##### "):
            line = line.replace("**", "").strip()
            sentence = re.sub(r"^\d+\.\s*", "", line[6:].strip()).strip("「」")
            if sentence in {"お粗末な～。", "ご盛大な～。", "先生からのご連絡", "ご連絡をする", "お野菜を使ったお料理"}:
                result[i] = "- **" + sentence + "**"
                # Its H6 gloss is converted to ordinary text in a later pass.
                changes.append("reclassified_honorific_fragment")
            else:
                result[i] = ("##### " + sentence).replace("ご参加して頂き", "ご参加いただき").replace("ありがとうございます。。", "ありがとうございます。").replace("ご自由にしてお使いください", "ご自由にお使いください")
                if "ご自由にしてお使いください" in line:
                    changes.append("corrected_Japanese_honorific_sentence")
    # A fragment's immediately following H6 is a gloss, not a sentence translation.
    for i in range(len(result) - 1):
        if result[i].startswith("- **"):
            j = i + 1
            while j < len(result) and not result[j].strip():
                j += 1
            if j < len(result) and result[j].startswith("###### →"):
                result[j] = "  " + result[j][len("###### →"):].strip()
    return result


def sentence_endings(tail, changes):
    out = []
    pending_pitch = None
    extra = {
        "A: すみません、田中さんの電話番号は何番ですか。": "Xin lỗi, số điện thoại của anh Tanaka là số mấy ạ?",
        "B: ０９３－１２３－４５６７です。": "Là 093-123-4567 ạ.",
        "A: ０９３－１２３－４５６７ですね↑。どうも": "093-123-4567 phải không ạ. Cảm ơn.",
    }
    for line in tail:
        if line.startswith("##### "):
            raw = line[6:].strip().replace("++", "").replace("****", "")
            if raw in extra:
                speaker, sentence = raw.split(":", 1)
                sentence = sentence.strip().replace("↑", "").replace("。どうも", "。どうも。")
                out += ["##### " + sentence, "###### → " + extra[raw], f"*Lượt thoại: {speaker}.*"]
                if "↑" in raw:
                    out.append("*Ngữ điệu lên ở ですね.*")
                changes.append("translated_unpaired_phone_dialogue_turn")
                continue
            if "↑" in raw or "↓" in raw:
                pending_pitch = "Ngữ điệu lên." if "↑" in raw else "Ngữ điệu xuống."
                raw = raw.replace("↑", "").replace("↓", "")
                changes.append("moved_intonation_mark_below_translation")
            if raw != line[6:].strip():
                changes.append("removed_inline_example_formatting")
            line = "##### " + raw
        elif line.startswith("###### "):
            line = re.sub(r"^######\s*→\s*", "###### → ", line)
            for note in ("Nam giới hay dùng dạng này.", "Nữ giới hay dùng dạng này."):
                if note in line:
                    line = line.replace(" . " + note, "").replace(" " + note, "").strip()
                    line = line.replace("(Cái", "Cái").replace("(Anh", "Anh").replace("?)", "?")
                    out.append(line)
                    out.append("*" + note + "*")
                    changes.append("moved_usage_note_below_translation")
                    break
            else:
                out.append(line)
            if pending_pitch:
                out.append("*" + pending_pitch + "*")
                pending_pitch = None
            continue
        out.append(line)
    return out


def topic_vs_subject(tail, changes):
    joined = "\n".join(tail)
    repairs = {
        'Thứ làm bạn thấy khó hiểu nhất có lẽ là **"は"** và **"が"**. Thực ra tôi đã học ở trong trường ngoại ngữ nhưng không thấy giáo viên nào giải thích được rõ ràng sự khác nhau.': 'は và が đều có thể đứng sau danh từ, nhưng chúng thường hướng sự chú ý tới những phần khác nhau của thông tin.',
        'Họ thường chỉ giải thích là **"は"** là nhấn mạnh chủ ngữ, còn **"が"** là nhấn mạnh vị ngữ. Tôi thấy **không hẳn như vậy**, mà **"は"** và **"が"** có chức năng ngữ pháp **khác nhau**.': 'は thường nêu chủ đề đã biết hoặc đặt phạm vi đối chiếu. が thường giới thiệu hay làm nổi bật chủ thể, và cũng xuất hiện trong mệnh đề bổ nghĩa.',
        'Dưới đây, tôi sẽ giải thích thật đơn giản, rõ ràng cho các bạn về **"は"** và **"が"**.': 'Cần xét ngữ cảnh để chọn trợ từ; cả hai câu cùng một động từ vẫn có thể đúng.',
        '- Câu (1) là câu **ĐÚNG**, nó là một **CÂU KỂ**.': '- Câu dùng は lấy tôi làm chủ đề rồi kể việc ăn táo.',
        '- Còn câu (2) nếu đứng đơn độc thì là một câu **SAI**, câu (2) **CHỈ CÓ THỂ LÀ CÂU TRẢ LỜI** cho một câu hỏi về chủ thể.': '- Câu dùng が nhấn vào người ăn táo; câu này có thể đứng độc lập trong ngữ cảnh phù hợp.',
        '- Quả thật là người nghe sẽ hiểu, bởi vì thực ra nếu bạn **lược bỏ** bớt trợ từ thì dựa vào nội dung người nghe vẫn **phán đoán** được nội dung nhưng bạn sẽ **SAI**.': '- Trong hội thoại, đôi khi trợ từ được lược nếu ngữ cảnh đủ rõ; trong các ví dụ dưới đây, は và が đều đúng nhưng sắc thái khác nhau.',
        '## ① 「は」 dùng cho CÂU KỂ': '## ① は nêu chủ đề của câu',
        '## ② 「が」 dùng cho CÂU TRẢ LỜI của câu hỏi về chủ thể': '## ② が làm nổi bật chủ thể trong thông tin mới',
        'Thực ra câu (1) là **câu kể** lại sự kiện, còn (2) không phải là câu đứng một mình.  ': 'Câu (1) nêu chủ đề là tôi; câu (2) nhấn rằng chính tôi là người ăn.  ',
        'Nó là **Câu trả lời** cho câu hỏi:': 'Câu dùng が rất tự nhiên khi trả lời câu hỏi:',
        '## ③ 「は」 dùng cho CÂU, 「が」 dùng cho VẾ CÂU': '## ③ が trong mệnh đề bổ nghĩa và cách mô tả',
        '→ **「は」** dùng cho câu hoàn chỉnh có dạng sau:': 'は có thể nêu chủ đề của cả câu:',
        '→ **「が」** tạo nên vế câu dạng:': 'が cũng có thể đánh dấu chủ thể bên trong mệnh đề bổ nghĩa:',
        'Câu này là một câu đúng, và là một câu **KỂ SỰ KIỆN**, nhưng lại dùng **“が”**??': 'Trong câu này, 彼がしたこと là cụm chỉ “việc anh ấy đã làm”.',
        'Thực ra, nếu bạn dịch là:  **Anh ấy biết việc đã làm.**': 'Chủ thể của 知っています không được nêu rõ trong câu này.',
        'Thì bạn đã không hiểu ý nghĩa câu trên.': 'Theo ngữ cảnh, chủ thể ấy có thể là tôi hoặc một người khác.',
        'Câu này thực ra phải dịch là: **Tôi biết việc anh ta đã làm.**': 'Một cách dịch theo ngữ cảnh là: **Tôi biết việc anh ấy đã làm.**',
        'Bởi vì, trong câu tiếng Nhật, chủ ngữ ("tôi") đã được **ẩn** đi.': 'Tiếng Nhật thường lược chủ đề khi người nghe đã biết đang nói về ai.',
        'Câu đầy đủ của câu trên là:': 'Nếu chủ thể là tôi, có thể nói đầy đủ:',
        '→ **「が」** dùng cho vế câu': 'が còn đánh dấu thành phần được mô tả trong câu có chủ đề は:',
        '## ④ 「は」 có thể BỊ ẨN theo chủ ngữ (“tôi”)': '## ④ Lược chủ đề khi ngữ cảnh đã rõ',
        '食たべました': '食べました',
        'ベトナム人じん': 'ベトナム人',
        '料 金': '料金',
        '彼かれ**が**したこと **chỉ là một vế câu**, nó tạo nên một cụm có tính chất danh từ, làm đối tượng cho hành động “biết” của chủ thể “tôi” (mà đã được ẩn đi).': '彼がしたこと là mệnh đề bổ nghĩa cho こと; cả cụm là đối tượng của 知っています. Chủ thể của 知っています được hiểu theo ngữ cảnh.',
        '###### → Anh ta biết việc đã làm.': '###### → Tôi biết việc anh ấy đã làm.',
        '##### *(＝私は頭が痛い*': '##### *(＝私は頭が痛い。)*',
        '###### → Anh thái độ thật vô lễ.': '###### → Thái độ của anh thật vô lễ.',
    }
    for old, new in repairs.items():
        if old in joined:
            joined = joined.replace(old, new)
            changes.append("corrected_topic_subject_explanation")
    lines = joined.splitlines()
    out = []
    pending_speaker = None
    for line in lines:
        if line.startswith("##### ") and line[6:].strip().startswith("*(＝"):
            out.append("*" + line[6:].strip().strip("*") + "*")
            changes.append("reclassified_parenthetical_example_note")
            continue
        example_text = re.sub(r"^\d+\.\s*", "", line[6:].strip()) if line.startswith("##### ") else ""
        if example_text in {"彼がしたこと", "すいかちゃんが書いた手紙", "踊り子が踊った踊り", "彼女がくれたもの", "顔立ちがきれいな女性"}:
            out.append("- **" + example_text + "**")
            changes.append("reclassified_noun_phrase")
            continue
        previous = next((s for s in reversed(out) if s.strip()), "")
        if line.startswith("###### → ") and previous.startswith("- **"):
            out.append("  " + line[len("###### → "):])
            continue
        if line.startswith("##### ") and example_text.startswith(("ナガズキ：", "すいかちゃん：")):
            speaker, sentence = example_text.split("：", 1)
            pending_speaker = speaker
            out.append("##### " + sentence)
            changes.append("moved_dialogue_role")
            continue
        if line.startswith("###### → ") and out:
            line = re.sub(r"^(###### → )(Nagazuki|Suika-chan):\s*", r"\1", line)
            line = line.replace(" *(Không ẩn chủ ngữ)*", "")
            out.append(line)
            if pending_speaker:
                out.append("*Lượt thoại: " + pending_speaker + ".*")
                pending_speaker = None
            continue
        if line.startswith("> ##### "):
            line = "*" + line[len("> ##### "):].strip() + "*"
            changes.append("reclassified_quoted_example_note")
        out.append(line)
    # Supply four source Japanese utterances with missing Vietnamese translations.
    result = []
    for index, line in enumerate(out):
        result.append(line)
        if line.startswith("##### "):
            following = next((s for s in out[index + 1:] if s.strip()), "")
            if following.startswith("###### →"):
                continue
            ja = re.sub(r"^\d+\.\s*", "", line[6:].strip())
            vi = {
                "私はりんごを食べました。": "Tôi đã ăn táo.",
                "私がりんごを食べました。": "Chính tôi đã ăn táo.",
                "私は彼がしたことを知っています。": "Tôi biết việc anh ấy đã làm.",
            }.get(ja)
            if vi:
                result.append("###### → " + vi)
                changes.append("translated_unpaired_Japanese_sentence")
    return result


def normalize_examples(tail, changes):
    """Number genuine sentence pairs and leave rules outside H5/H6."""
    out = []
    number = 1
    i = 0
    while i < len(tail):
        line = html.unescape(tail[i]).replace("\u00a0", " ").replace("\u200b", "")
        if re.match(r"^#{2,3} ", line):
            number = 1
        if line.startswith("##### "):
            ja = re.sub(r"^\d+\.\s*", "", line[6:].strip()).replace("**", "")
            j = i + 1
            while j < len(tail) and not tail[j].strip():
                j += 1
            if j >= len(tail) or not tail[j].startswith("###### "):
                raise ValueError("unpaired_sentence_example")
            vi = re.sub(r"^######\s*→\s*", "", tail[j]).strip()
            if not vi or vi == tail[j]:
                raise ValueError("invalid_sentence_translation")
            out.extend([f"##### {number}. {ja}", "###### → " + vi, ""])
            number += 1
            i = j + 1
            continue
        if line.startswith("###### "):
            raise ValueError("orphan_translation")
        if re.match(r"^####\s", line):
            line = "### " + line[5:]
            changes.append("reclassified_H4")
        out.append(line)
        i += 1
    return out


def make(path):
    header, body = parse(path)
    uid = header["id"][:8]
    meaning, structures = EDITORIAL[uid]
    changes = []
    tail = body_tail(body, uid)
    if uid == "4fb29356":
        tail = form_bullets(tail, uid, changes)
    elif uid == "d6225fc2":
        tail = form_bullets(tail, uid, changes)
    elif uid == "e14aee6b":
        changes.append("restored_counting_structure")
    elif uid in {"b8bb9cf8", "ab5c0e07", "f30c54cc"}:
        tail = obligation_variants(tail, uid, changes)
        # The original structure block is now replaced by a clean short formula.
        if "## Cấu trúc ngữ pháp" in tail:
            s = tail.index("## Cấu trúc ngữ pháp")
            e = next(i for i in range(s + 1, len(tail)) if tail[i].startswith("## "))
            tail = tail[:s] + tail[e:]
    elif uid == "26c62437":
        tail = only_comparison(tail, changes)
    elif uid == "4f31090e":
        tail = honorific_prefixes(tail, changes)
    elif uid == "25ca71cb":
        tail = sentence_endings(tail, changes)
    elif uid == "46c8ddc5":
        tail = topic_vs_subject(tail, changes)
    tail = normalize_examples(tail, changes)
    header["description"] = meaning
    header["conjugation"] = " / ".join(structures)
    intro = ["# " + header["name"], "", "> " + meaning, "", "---", "", "## Cấu trúc ngữ pháp", ""]
    intro += ["> **" + s + "**" + ("<br>" if i + 1 < len(structures) else "") for i, s in enumerate(structures)]
    content = intro + ([""] if uid == "26c62437" else ["", "## Cách dùng", ""]) + tail
    front = ["---"] + [f"{k}: {json.dumps(header[k], ensure_ascii=False)}" for k in ("id", "jlpt", "name", "description", "conjugation")] + ["---", ""]
    return "\n".join(front + content).rstrip() + "\n", changes


def main():
    entries = json.loads(AUDIT.read_text(encoding="utf-8"))["entries"]
    deferred = [e for e in entries if e["status"] == "deferred"]
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for entry in deferred:
        path = BASE / Path(entry["file"]).name
        uid = entry["id"][:8]
        row = {"file": entry["file"], "id": entry["id"]}
        if uid not in EDITORIAL:
            row.update(status="deferred", reason="complex_content_requires_editorial_review")
            rows.append(row)
            continue
        try:
            original_header, original_body = parse(path)
            text, changes = make(path)
            target = OUT / path.name
            target.write_text(text, encoding="utf-8")
            h, body = parse(target)
            validate_body(body, h["name"], target)
            if h["id"] != original_header["id"] or h["jlpt"] != original_header["jlpt"]:
                raise ValueError("identity_changed")
            source_h5 = sum(s.startswith("##### ") for s in original_body)
            source_h6 = sum(s.startswith("###### ") for s in original_body)
            rendered_h5 = sum(s.startswith("##### ") for s in body)
            rendered_h6 = sum(s.startswith("###### ") for s in body)
            if rendered_h5 != rendered_h6 or source_h5 != rendered_h5 + EXPECTED_RECLASSIFIED_H5[uid]:
                raise ValueError("source_example_or_rule_coverage_mismatch")
            if sum("![" in s for s in original_body) != sum("![" in s for s in body):
                raise ValueError("source_image_count_mismatch")
            row.update(status="candidate", target=str(target.relative_to(ROOT)).replace("\\", "/"), source_h5=source_h5, source_h6=source_h6, rendered_h5=rendered_h5, reclassified_h5=EXPECTED_RECLASSIFIED_H5[uid], edits=dict(Counter(changes)), content_review="editorial_rules_applied; human_review_pending")
        except (ValueError, AssertionError, KeyError, TypeError, StopIteration, IndexError) as exc:
            row.update(status="deferred", reason=str(exc).split(":", 1)[0])
        rows.append(row)
    summary = {"baseline": len(rows), "candidate": sum(r["status"] == "candidate" for r in rows), "still_deferred": sum(r["status"] == "deferred" for r in rows), "reasons": dict(Counter(r.get("reason") for r in rows if r["status"] == "deferred"))}
    REPORT.write_text(json.dumps({"summary": summary, "entries": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
