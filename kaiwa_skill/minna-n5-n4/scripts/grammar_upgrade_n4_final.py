"""Repair remaining N4 legacy lessons with explicit example/formula decisions."""
import html
import json
import re
from pathlib import Path

from grammar_upload import parse, validate_body

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar/N4"
OUT = ROOT / "authored/grammar-upload/2026-11-25-N4-final/N4"
AUDIT = ROOT / "reports/grammar-upgrade-2026-11-25-N4-final-audit.json"
QUEUE = ROOT / "reports/grammar-upgrade-2026-11-25-N4-editorial-audit.json"

# Each plan was checked against the relevant original article, including multi-use articles.
PLANS = {
    "9c126d59": ("Sai khiến: bắt, cho phép hoặc khiến ai làm việc gì", ["V nhóm I: hàng う → hàng あ ＋ せる", "V nhóm II: bỏ る ＋ させる", "する → させる／来る → 来させる", "Nを／に ＋ V sai khiến"]),
    "e1fee180": ("Cách chia động từ ở thể bị động", ["V nhóm I: hàng う → hàng あ ＋ れる", "V nhóm II: bỏ る ＋ られる", "する → される／来る → 来られる"]),
    "d4721bfe": ("Bị động trực tiếp, gián tiếp và bị động của sự việc", ["Nは Nに V bị động", "Nは Nに Nを V bị động", "Nが／は V bị động"]),
    "c1ee3692": ("Khiêm nhường ngữ để nói về hành động của mình hoặc người cùng phe", ["お ＋ Vます bỏ ます ＋ します", "ご ＋ N Hán Nhật ＋ します", "Động từ khiêm nhường đặc biệt: 参ります／申します／いただきます"]),
    "b6df952a": ("Tôn kính ngữ để nói về hành động hoặc trạng thái của người được kính trọng", ["V thể bị động tôn kính", "お ＋ Vます bỏ ます ＋ になります", "ご ＋ N Hán Nhật ＋ になります", "Động từ tôn kính đặc biệt: いらっしゃいます／おっしゃいます／なさいます"]),
    "dfe9e422": ("Làm giúp, được làm giúp và lựa chọn mức lịch sự", ["N1は N2に Vてあげます／さしあげます", "N1は N2に Vてもらいます／いただきます", "N1が N2に Vてくれます／くださいます"]),
    "a3390110": ("Phân biệt あげる, さしあげる và やる theo người nhận", ["N1は N2に N3を あげます", "N1は N2に N3を さしあげます", "N1は N2に N3を やります"]),
    "5d5c346a": ("So sánh sắc thái nêu lý do bằng から, ので và て", ["Lý do ＋ から、kết quả", "Lý do ＋ ので、kết quả", "Vて／Aくて／Aな・Nで、cảm xúc hoặc kết quả"]),
    "107771cc": ("Phân biệt hướng của hành động giúp đỡ", ["N1は N2に Vてあげます", "N1が người nói／người nhàに Vてくれます", "N1は N2に Vてもらいます"]),
    "83a24a8c": ("Ý định vừa nghĩ ra và ý định đang duy trì", ["V thể ý chí ＋ と思います", "V thể ý chí ＋ と思っています"]),
    "2c47ef34": ("Các cách dùng ～ように để nêu mục tiêu, yêu cầu, mong ước và nhận định", ["Vる／Vない ＋ ように ＋ V", "Vる／Vない ＋ ようにしてください", "Vる／Vない ＋ ように祈る／願う", "Thể thường ＋ ように感じる／思う"]),
    "0c06187e": ("Nêu mục đích bằng ～ために", ["V thể từ điển ＋ ために", "N ＋ のために"]),
    "32f91ce9": ("Suy đoán hoặc hỏi mềm bằng でしょう／だろう", ["V・Aい thể thường ＋ でしょう／だろう", "Aな・N（bỏ だ）＋ でしょう／だろう", "〜でしょうか"]),
    "83c830c2": ("Ba thời điểm sắp làm, đang làm và vừa làm", ["Vる ＋ ところです", "Vている ＋ ところです", "Vた ＋ ところです", "Vる ＋ ところでした（suýt nữa）"]),
    "d46cf19d": ("Quyết định chọn hoặc làm cho trở thành trạng thái nào đó", ["N ＋ にします", "Aい: bỏ い ＋ くします", "Aな ＋ にします"]),
    "84c447b3": ("Dự đoán có căn cứ rằng điều gì phải đúng", ["V・Aい thể thường ＋ はずです", "Aな ＋ なはずです", "N ＋ のはずです", "〜はずがありません／そんなはずはありません"]),
    "f62c3280": ("Các cách dùng やる／します và sắc thái trong khẩu ngữ", ["Nを ＋ やります／します", "Vて ＋ やります"]),
    "62fb39ee": ("Cố gắng tạo thói quen hoặc tránh một việc", ["Vる／Vない ＋ ようにします", "Vる／Vない ＋ ようにしています"]),
    "8a990587": ("Dần có khả năng hoặc thay đổi thói quen", ["Vる／Vない ＋ ようになります", "V khả năng ＋ ようになります"]),
    "92f918c3": ("Trong trường hợp một điều kiện xảy ra", ["V・Aい thể thường ＋ 場合は", "Aな ＋ な場合は", "N ＋ の場合は"]),
    "5e8c84a0": ("Liệt kê tính chất hoặc nhiều lý do bằng ～し", ["V・Aい thể thường ＋ し", "Aな・N ＋ だし", "〜し、〜し、〜"]),
    "846b121c": ("Nêu ý định làm hoặc không làm", ["V thể từ điển ＋ つもりです", "Vない ＋ つもりです", "Vた ＋ つもり（coi như đã làm）"]),
    "003e4a48": ("Làm trước để chuẩn bị hoặc giữ nguyên trạng thái", ["Vて ＋ おきます", "Vて ＋ おいてください", "Khẩu ngữ: Vとく／Vどく"]),
    "42f5dd0a": ("Hoàn tất một việc hoặc lỡ xảy ra kết quả đáng tiếc", ["Vて ＋ しまいます", "Vて ＋ しまいました", "Khẩu ngữ: Vちゃう／Vじゃう"]),
    "d33f33a3": ("Làm giúp người dưới hoặc người thân với sắc thái thân mật", ["Vて ＋ やります／やる"]),
    "a38f78db": ("Dễ làm, khó làm hoặc dễ xảy ra", ["Vます bỏ ます ＋ やすい", "Vます bỏ ます ＋ にくい"]),
    "521d31fd": ("Nêu bối cảnh, giải thích hoặc hỏi lý do bằng ～んです", ["V・Aい thể thường ＋ んです", "Aな・N ＋ なんです", "〜んですが、〜"]),
}

# These are formulas, rejected counterexamples, or captions, not Japanese sentences
# with a Vietnamese translation. They remain visible as ordinary Markdown text.
DEMOTE_H5 = {
    "e1fee180": set(range(1, 12)),
    "d4721bfe": {19, 22},
    "c1ee3692": {27, 28, 29, 30, 31, 33, 34, 35, 36, 37},
    "b6df952a": set(range(11, 19)) | {31, 32, 33, 36, 37, 40} | set(range(53, 58)) | set(range(59, 64)),
    "a3390110": {1, 2},
    "107771cc": {4, 16, 35},
    "83a24a8c": {23},
    "0c06187e": {19, 21},
    "84c447b3": {22},
    "f62c3280": {10, 11, 13, 16},
    "62fb39ee": {32},
    "92f918c3": {17, 18},
    "846b121c": {23},
    "d33f33a3": {1},
    "a38f78db": set(range(1, 6)),
}
DEMOTE_H6 = {
    "a3390110": {1, 2, 3},
    "2c47ef34": {1, 15, 34, 53},
    "83c830c2": {45},
    "521d31fd": {1, 14},
    "f62c3280": {8, 9},
}
ADDED_TRANSLATIONS = {
    "5d5c346a": {26: "Vì gió mạnh thổi nên các biển hiệu khắp nơi đã đổ hoặc bị thổi bay."},
    "f62c3280": {8: "Hay làm bài tập về nhà nhỉ?", 9: "Hay làm bài tập về nhà nhỉ?"},
    "dfe9e422": {47: "Nếu lo cho sức khỏe thì đi khám đi!", 49: "Anh Ando là nhân viên mới nên hãy chỉ dẫn nhiều điều.", 50: "Vì tôi là người mới nên xin hãy chỉ dẫn nhiều điều."},
}
SKIP = {
    "a1bcb005": "Bài ～いい có năm nhóm cách dùng và nhiều câu Nhật hỏng; cần duyệt lại từng hội thoại trước khi upload.",
}

MANUAL = {
    "9959d2a0": ("Lồng câu hỏi có từ để hỏi vào mệnh đề lớn", ["Từ để hỏi ＋ V・Aい thể thường ＋ か、〜", "Từ để hỏi ＋ Aな・N（bỏ だ）＋ か、〜"], [
        ("電車が何時に大阪に着きますか。", "Tàu đến Osaka lúc mấy giờ?"),
        ("知っていますか。", "Anh có biết không?"),
        ("電車が何時に大阪に着くか知っていますか。", "Anh có biết tàu đến Osaka lúc mấy giờ không?"),
        ("プレゼントは何がいいですか。", "Quà gì thì phù hợp?"),
        ("彼に聞きましょう。", "Hãy hỏi anh ấy."),
        ("プレゼントは何がいいか彼に聞きましょう。", "Hãy hỏi anh ấy xem quà gì thì phù hợp."),
        ("彼に初めて会ったのはいつですか。", "Lần đầu cậu gặp anh ấy là khi nào?"),
        ("忘れてしまいました。", "Tôi đã quên mất."),
        ("彼に初めて会ったのはいつか忘れてしまいました。", "Tôi đã quên lần đầu gặp anh ấy là khi nào."),
        ("東京駅までは何番線ですか。", "Đến ga Tokyo thì đi đường tàu số mấy?"),
        ("教えてください。", "Xin hãy chỉ cho tôi."),
        ("東京駅までは何番線か教えてください。", "Xin hãy cho tôi biết đến ga Tokyo thì đi đường tàu số mấy."),
        ("どうしてうるさい音楽が好きですか。", "Vì sao anh ấy thích nhạc ồn ào?"),
        ("彼に聞きました。", "Tôi đã hỏi anh ấy."),
        ("どうしてうるさい音楽が好きか彼に聞きました。", "Tôi đã hỏi anh ấy vì sao lại thích nhạc ồn ào."),
    ]),
    "47669f80": ("Lồng câu hỏi có hay không vào mệnh đề lớn", ["V・Aい thể thường ＋ かどうか、〜", "Aな・N（bỏ だ）＋ かどうか、〜"], [
        ("山田さんがパーティーに来ますか。", "Anh Yamada có đến dự tiệc không?"),
        ("わかりません。", "Tôi không biết."),
        ("山田さんがパーティーに来るかどうかわかりません。", "Tôi không biết anh Yamada có đến dự tiệc hay không."),
        ("このケーキはおいしいですか。", "Bánh này có ngon không?"),
        ("食べてみてください。", "Hãy ăn thử xem."),
        ("このケーキはおいしいかどうか食べてみてください。", "Hãy ăn thử xem bánh này có ngon hay không."),
        ("彼は元気ですか。", "Anh ấy có khỏe không?"),
        ("何年も会っていないので、わかりません。", "Vì nhiều năm không gặp nên tôi không biết."),
        ("何年も彼に会っていないので、彼は元気かどうかわかりません。", "Vì nhiều năm không gặp nên tôi không biết anh ấy có khỏe hay không."),
        ("その話は本当ですか。", "Câu chuyện đó có thật không?"),
        ("教えてください。", "Xin hãy cho tôi biết."),
        ("その話は本当かどうか教えてください。", "Xin hãy cho tôi biết câu chuyện đó có thật hay không."),
        ("リンさんは先生と話しましたか。", "Chị Linh đã nói chuyện với thầy cô chưa?"),
        ("知っていますか。", "Anh có biết không?"),
        ("リンさんは先生と話したかどうか知っていますか。", "Anh có biết chị Linh đã nói chuyện với thầy cô hay chưa không?"),
    ]),
    "173cd56e": ("Giải thích nghĩa của từ, ký hiệu hoặc phát ngôn", ["「Từ・ký hiệu」＋ は ＋ …という意味です", "V・A・N thể thường ＋ という意味です", "どういう意味ですか"], [
        ("「禁煙」はタバコを吸うのを禁止するという意味です。", "「禁煙」nghĩa là cấm hút thuốc."),
        ("「ともだち」は英語で「Friend」という意味です。", "「ともだち」trong tiếng Anh nghĩa là “friend”."),
        ("このマークは何という意味ですか。", "Ký hiệu này có nghĩa là gì?"),
        ("このマークはどういう意味ですか。", "Ký hiệu này có nghĩa là gì?"),
        ("洗濯機で洗えるという意味です。", "Nghĩa là có thể giặt bằng máy giặt."),
        ("この漢字はどういう意味ですか。", "Chữ Hán này có nghĩa là gì?"),
        ("使うなという意味です。", "Nghĩa là cấm sử dụng."),
        ("それは飽きやすいという意味です。", "Nó có nghĩa là rất dễ chán."),
        ("「立入禁止」は入るなという意味です。", "「立入禁止」nghĩa là cấm vào."),
        ("それは僕が彼女を好きだという意味です。", "Điều đó có nghĩa là tôi thích cô ấy."),
        ("「Cảm ơn」は日本語で「ありがとう」という意味です。", "“Cảm ơn” trong tiếng Nhật là 「ありがとう」."),
    ]),
}


def convert_manual(path, spec):
    h, body = parse(path)
    desc, structures, examples = spec
    h["description"] = desc
    h["conjugation"] = "／".join(structures)
    lines = ["---"]
    for field in ("id", "jlpt", "name", "description", "conjugation"):
        lines.append(f"{field}: {json.dumps(h[field], ensure_ascii=False)}")
    lines += ["---", "", "# " + h["name"], "", "> " + desc, "", "---", "", "## Cấu trúc ngữ pháp", ""]
    for i, structure in enumerate(structures):
        lines.append("> **" + structure + "**" + ("<br>" if i + 1 < len(structures) else ""))
    lines += ["", "## Cách dùng", "", "Dùng để đưa một câu hỏi vào trong câu lớn. Câu được lồng dùng thể thường và kết thúc bằng か hoặc かどうか theo loại câu hỏi.", "", "## Ví dụ", ""]
    for i, (ja, vi) in enumerate(examples, 1):
        lines += [f"##### {i}. {ja}", "###### → " + vi, ""]
    if h["id"].startswith("47669f80"):
        source_pairs = [(s[6:].strip(), body[j][7:].strip()) for j, s in enumerate(body) if s.startswith("##### ") and j + 2 < len(body) and body[j + 2].startswith("###### ")]
        assert len(source_pairs) == 25
        lines += ["## Ví dụ bổ sung từ bản gốc", ""]
        for n, (ja, vi) in enumerate(source_pairs[10:], 1):
            ja, _ = normal_ja(ja)
            vi = normal_vi(vi).replace("nổ lực", "nỗ lực")
            lines += [f"##### {n}. {ja}", "###### → " + vi, ""]
        count = 30
    else:
        count = len(examples)
    while lines and not lines[-1].strip():
        lines.pop()
    new_body = lines[lines.index("---", 1) + 1:]
    validate_body(new_body, h["name"], path)
    target = OUT / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"pairs": count, "images": 0, "manual_split": True}


def normal_ja(raw):
    s = re.sub(r"^\s*(?:\d+\.|\(\d+\))\s*", "", raw).strip()
    s = s.replace("*", "").replace("_", "")
    role = ""
    m = re.match(r"^([A-ZＡ-Ｚ]|客|店員|学生|先生|母|愛海)\s*[:：]?\s*(「.+)", s)
    if not m:
        m = re.match(r"^([A-ZＡ-Ｚ]|客|店員|学生|先生|母|愛海)\s*[:：]\s*(.+)", s)
    if m:
        role, s = m.group(1), m.group(2)
    elif s.startswith(("ー", "－")):
        role, s = "lượt đáp", s[1:].strip()
    return s, role


def normal_vi(raw):
    s = raw.replace("*", "").replace("_", "").replace("\\[", "[").replace("\\]", "]")
    return re.sub(r"^\s*(?:→|ー|－|※)\s*", "", s).strip()


def convert(path, plan):
    h, body = parse(path)
    key = h["id"][:8]
    h5, h6 = [], []
    n5 = n6 = 0
    for i, line in enumerate(body):
        if line.startswith("##### "):
            n5 += 1
            h5.append((n5, i, line[6:].strip()))
        elif line.startswith("###### "):
            n6 += 1
            h6.append((n6, i, line[7:].strip()))
    dem5, dem6 = DEMOTE_H5.get(key, set()), DEMOTE_H6.get(key, set())
    kept5 = [(n, i, text) for n, i, text in h5 if n not in dem5]
    kept6 = [(n, i, text) for n, i, text in h6 if n not in dem6]
    added = ADDED_TRANSLATIONS.get(key, {})
    if len(kept5) != len(kept6) + len(added):
        raise ValueError(f"unpaired_after_editorial: {len(kept5)} H5, {len(kept6)} H6, {len(added)} new translations")
    # Match within each uninterrupted H5/H6 block first. A dialogue often has
    # H5(A), H5(B), H6(A), H6(B), so adjacency alone is insufficient.
    mapping = {}
    used6 = set()
    h5byline = {i: (n, ja) for n, i, ja in kept5}
    h6byline = {i: (n, vi) for n, i, vi in kept6}
    block = []
    blocks = []
    for i, line in enumerate(body + ["END BLOCK"]):
        if i in h5byline or i in h6byline:
            block.append(i)
        elif line.strip():
            if block:
                blocks.append(block)
                block = []
    for block in blocks:
        bs5 = [i for i in block if i in h5byline]
        bs6 = [i for i in block if i in h6byline]
        to_add = [i for i in bs5 if h5byline[i][0] in added]
        if len(bs5) != len(bs6) + len(to_add):
            continue
        for i in to_add:
            n, ja = h5byline[i]
            mapping[i] = (ja, added[n])
        for i, j in zip([i for i in bs5 if i not in to_add], bs6):
            mapping[i] = (h5byline[i][1], h6byline[j][1])
            used6.add(j)
    missing5 = [(n, i, ja) for n, i, ja in kept5 if i not in mapping]
    missing6 = [(n, i, vi) for n, i, vi in kept6 if i not in used6]
    if len([x for x in missing5 if x[0] not in added]) != len(missing6):
        raise ValueError("unpaired_after_block_matching")
    k = 0
    for n, i, ja in missing5:
        if n in added:
            mapping[i] = (ja, added[n])
        else:
            mapping[i] = (ja, missing6[k][2])
            k += 1
    direct_checked = 0
    for n, i, ja in kept5:
        if n in added:
            continue
        j = i + 1
        while j < len(body) and not body[j].strip():
            j += 1
        prev = i - 1
        while prev >= 0 and not body[prev].strip():
            prev -= 1
        if j < len(body) and body[j].startswith("###### ") and (prev < 0 or not body[prev].startswith("##### ")):
            tnum = next(tn for tn, ti, _ in h6 if ti == j)
            if tnum not in dem6:
                expected = normal_vi(body[j][7:].strip())
                actual = normal_vi(mapping[i][1])
                if expected != actual:
                    raise ValueError(f"source_adjacent_pair_changed: H5#{n}")
                direct_checked += 1
    desc, structures = plan
    h["description"] = desc
    h["conjugation"] = "／".join(structures)
    lines = ["---"]
    for field in ("id", "jlpt", "name", "description", "conjugation"):
        lines.append(f"{field}: {json.dumps(h[field], ensure_ascii=False)}")
    lines += ["---", "", "# " + h["name"], "", "> " + desc, "", "---", "", "## Cấu trúc ngữ pháp", ""]
    for j, s in enumerate(structures):
        lines.append("> **" + s + "**" + ("<br>" if j + 1 < len(structures) else ""))
    lines += ["", "## Giải thích và ví dụ từ bản gốc", ""]
    first = next(i for i, s in enumerate(body) if s.strip())
    assert body[first].startswith(("# ", "## "))
    number = 1
    text_lines = body[first + 1:]
    source_images = [s for s in body if "![" in s]
    emitted = 0
    for off, source in enumerate(text_lines):
        idx = first + 1 + off
        if source.startswith("##### "):
            old_n = next(n for n, i, _ in h5 if i == idx)
            if old_n in dem5:
                lines.append("- " + html.unescape(source[6:].strip()))
                continue
            ja, vi = mapping[idx]
            ja, role = normal_ja(ja)
            vi = normal_vi(vi)
            if not ja or not vi:
                raise ValueError("empty_paired_example")
            if role:
                lines += ["*Vai trong bản gốc: " + role + ".*", ""]
            lines += [f"##### {number}. {ja}", "###### → " + vi, ""]
            emitted += 1
            number += 1
            continue
        if source.startswith("###### "):
            old_n = next(n for n, i, _ in h6 if i == idx)
            if old_n in dem6:
                lines.append("- " + html.unescape(source[7:].strip()))
            continue
        if source.startswith("## Cấu trúc ngữ pháp"):
            source = source.replace("## Cấu trúc ngữ pháp", "## Chi tiết cấu trúc từ bản gốc", 1)
        if source.startswith("#### "):
            source = "### " + source[5:]
        if re.match(r"^#{2,3} ", source):
            number = 1
        lines.append(source)
    if emitted != len(kept5):
        raise ValueError("lost_example")
    # Content repairs where the source itself contains an unmistakable typo.
    if key == "b6df952a":
        lines = [s.replace("いらしゃって", "いらっしゃって").replace("おしゃって", "おっしゃって") for s in lines]
    while lines and not lines[-1].strip():
        lines.pop()
    new_body = lines[lines.index("---", 1) + 1:]
    validate_body(new_body, h["name"], path)
    if [s for s in new_body if "![" in s] != source_images:
        raise ValueError("image_loss")
    if sum(s.startswith("##### ") for s in new_body) != len(kept5):
        raise ValueError("pair_loss")
    target = OUT / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"pairs": len(kept5), "demoted_h5": len(dem5), "demoted_h6": len(dem6), "new_translations": len(added), "images": len(source_images), "direct_pairs_verified": direct_checked}


def main():
    queue = [x for x in json.loads(QUEUE.read_text(encoding="utf-8"))["entries"] if x["status"] == "deferred"]
    assert len(queue) == 31
    result = []
    for item in queue:
        row = dict(item)
        key = row["id"][:8]
        if key in SKIP:
            row["final_reason"] = SKIP[key]
        else:
            try:
                path = BASE / Path(row["file"]).name
                row.update(convert_manual(path, MANUAL[key]) if key in MANUAL else convert(path, PLANS[key]))
            except (ValueError, AssertionError, IndexError, KeyError) as exc:
                row["final_reason"] = str(exc)
            else:
                row["status"] = "converted"
        result.append(row)
    summary = {"N4_queue_input": len(queue), "converted": sum(x["status"] == "converted" for x in result), "remaining": sum(x["status"] != "converted" for x in result), "pairs": sum(x.get("pairs", 0) for x in result), "images": sum(x.get("images", 0) for x in result), "added_translations": sum(x.get("new_translations", 0) for x in result)}
    AUDIT.write_text(json.dumps({"summary": summary, "entries": result}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(summary)
    print("remaining:", [(x["id"][:8], x.get("final_reason")) for x in result if x["status"] != "converted"])


if __name__ == "__main__":
    main()
