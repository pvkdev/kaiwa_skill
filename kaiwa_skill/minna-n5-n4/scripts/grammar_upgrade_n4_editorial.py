"""Editorial N4 repairs for selected legacy lessons with paired examples."""
import json
import re
from collections import Counter
from pathlib import Path

from grammar_upload import parse, validate_body

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar/N4"
OUT = ROOT / "authored/grammar-upload/2026-11-25-N4-editorial/N4"
AUDIT = ROOT / "reports/grammar-upgrade-2026-11-25-N4-editorial-audit.json"
DEFERRED = ROOT / "reports/grammar-upgrade-2026-11-25-structure-audit.json"

# Structures are reviewed against each original lesson, including its distinct uses.
PLANS = {
    "f01b1078": ("Cách chia thể khả năng để nói có thể làm việc gì", ["V nhóm I: hàng い → hàng え ＋ ます", "V nhóm II: bỏ ます ＋ られます", "します → できます／来ます → 来られます"]),
    "2c967d25": ("Cách chia thể ý chí để rủ rê, quyết định hoặc đề xuất", ["V nhóm I: âm cuối hàng う → hàng お ＋ う", "V nhóm II: bỏ る ＋ よう", "する → しよう／来る → 来よう"]),
    "b87b9e73": ("Danh từ hóa tính từ bằng hậu tố さ để nói mức độ hoặc kích thước", ["Aい: bỏ い ＋ さ", "Aな: bỏ な ＋ さ"]),
    "9ba904e6": ("Phân biệt danh từ hóa động từ bằng の và こと", ["V thể thường ＋ の／こと", "V thể thường ＋ のは／のが／のを", "V thể thường ＋ ことは／ことが／ことを"]),
    "6c3c83d3": ("Phân biệt điều kiện ～たら và ～ば theo quan hệ và ý định ở vế sau", ["V・A・N thể た ＋ ら、〜", "V thể ば／Aい→ければ、〜", "Aな・N ＋ なら（ば）、〜"]),
    "ec90e1c9": ("Phân biệt もう và まだ: đã rồi, vẫn còn hoặc vẫn chưa", ["もう ＋ Vた／Vました", "まだ ＋ Vています", "まだ ＋ Vていません"]),
    "fdcde6df": ("Phân biệt vừa mới xảy ra theo thời điểm thực và cảm nhận", ["Vた ＋ ところです", "Vた ＋ ばかりです"]),
    "2e32444d": ("So sánh trạng thái hiện có và kết quả của hành động có chủ ý", ["Nが ＋ V tự động từている", "Nが／Nを ＋ V tha động từてある"]),
    "cd100f19": ("Cấm hoặc ngăn người khác thực hiện hành động", ["V thể từ điển ＋ な"]),
    "09f626a8": ("Cách chia và sử dụng thể mệnh lệnh trực tiếp", ["V nhóm I: âm cuối hàng う → hàng え", "V nhóm II: bỏ る ＋ ろ", "する → しろ／せよ; 来る → 来い"]),
    "a80986ab": ("Phân biệt tự động từ và tha động từ qua chủ thể và tân ngữ", ["Nが ＋ V tự động từ", "Nを ＋ V tha động từ"]),
    "52684d0f": ("Diễn tả vẻ ngoài hoặc dấu hiệu có thể nhận thấy", ["Vます bỏ ます ＋ そうです", "Aい bỏ い ＋ そうです", "Aな bỏ な ＋ そうです", "そうな ＋ N／そうに ＋ V"]),
    "8483e740": ("Làm theo đúng điều đã nói, chỉ dẫn hoặc kế hoạch", ["Vる／Vた ＋ とおりに", "N ＋ のとおりに", "N ＋ どおりに"]),
    "107c91e0": ("Càng làm hoặc càng có tính chất A thì mức độ B càng tăng", ["Vば ＋ Vるほど", "Aい→Aければ ＋ Aいほど", "Aな ＋ なら（ば）＋ Aなほど"]),
    "dbf050b2": ("Dùng thể khả năng để nói năng lực hoặc điều kiện cho phép", ["V nhóm I: hàng い → hàng え ＋ ます", "V nhóm II: bỏ ます ＋ られます", "します → できます／来ます → 来られます", "Nが ＋ V thể khả năng"]),
    "d92323f1": ("Nói một việc vẫn chưa xảy ra hoặc chưa hoàn tất", ["まだ ＋ Vていません"]),
    "7eb6d3c7": ("Xin phép thử làm một việc", ["Vて ＋ みてもいいですか"]),
    "55975be2": ("Nói một việc vừa mới xảy ra theo cảm nhận của người nói", ["Vた ＋ ばかりです", "Vた ＋ ばかりの ＋ N"]),
    "8232af37": ("Động từ tôn kính chỉ đi, đến hoặc ở", ["Nは／が ＋ いらっしゃいます", "V thể từ điển ＋ いらっしゃいます"]),
    "ed4427fc": ("Xin phép mình làm việc gì bằng thể sai khiến", ["V thể sai khiếnて ＋ ください", "V thể sai khiếnて ＋ もらえますか／もらえませんか"]),
    "e064551a": ("Trạng thái còn lại do ai đó làm sẵn có chủ ý", ["Nが ＋ V tha động từてあります", "Nは ＋ nơiに ＋ V tha động từてあります"]),
    "bb7dda53": ("Dẫn lời nói trực tiếp hoặc gián tiếp ở quá khứ", ["「Lời nói trực tiếp」＋ と言いました", "V・A・N thể thường ＋ と言いました／と言っていました"]),
    "ce3f4248": ("Thuật lại điều ai đó đang hoặc vẫn nói", ["V・A・N thể thường ＋ と言っています"]),
    "8ec25d8f": ("Cách chia thể điều kiện ～ば cho động từ, tính từ và danh từ", ["V nhóm I: âm cuối hàng う → hàng え ＋ ば", "V nhóm II: bỏ る ＋ れば", "する → すれば／来る → 来れば", "Vない → Vなければ", "Aい: bỏ い ＋ ければ／Aくない → Aくなければ", "Vたい → Vたければ／Vたくなければ", "Aな・N ＋ であれば／なら（ば）; phủ định ＋ でなければ／じゃなければ"]),
    "6b9cdf20": ("Điều kiện nếu A thì B hoặc sau khi A xảy ra thì B", ["Vた ＋ ら", "Aい: bỏ い ＋ かったら", "Aな・N ＋ だったら"]),
    "1e14f94a": ("Tổng hợp cách nói làm giúp và nhận sự giúp đỡ", ["N1は N2に Vてあげます", "N1は N2に Vてもらいます", "N1が N2に Vてくれます"]),
    "9a15b593": ("Nêu một khả năng chưa chắc chắn", ["V・Aい thể thường ＋ かもしれません", "Aな・N（hiện tại khẳng định bỏ だ）＋ かもしれません"]),
    "6bd63e67": ("Hỏi hoặc trình bày cách đọc và nội dung chữ viết", ["「文字」＋ と読みます", "場所に「文字」と書いてあります", "何と読みますか／何と書いてありますか"]),
}

REASONS = {
    "9c126d59": "Bảng chia thể sai khiến xen giữa H5/H6; 41 H5 cần phân loại câu ví dụ với dòng công thức.",
    "e1fee180": "11 H5 là các dạng chia bị động, không có H6; cần chuyển thành bảng và rà lời giải từng nhóm.",
    "d4721bfe": "42 H5 nhưng 40 H6; ví dụ bị động trực tiếp/gián tiếp cần ghép thủ công.",
    "c1ee3692": "39 H5 nhưng 29 H6 trong bài tổng hợp khiêm nhường ngữ; có bảng động từ đặc biệt.",
    "b6df952a": "65 H5 nhưng 41 H6 trong bài tổng hợp tôn kính ngữ; có bảng động từ và nhiều cách dùng.",
    "9959d2a0": "10 cặp hiển thị nhưng nhiều H5 gộp câu hỏi gốc và câu gián tiếp; cần tách lượt và dịch tương ứng.",
    "47669f80": "25 cặp hiển thị nhưng nhiều H5 gộp hai câu bằng dấu /; cần tách câu và dịch trước khi đánh số.",
    "dfe9e422": "50 H5/47 H6, có định dạng trong dịch và nhiều mẫu cho/nhận lẫn mức lịch sự.",
    "a3390110": "18 H5/19 H6, có dòng dịch lẻ; cần xác định cặp của ba mức cho/tặng.",
    "5d5c346a": "45 H5/44 H6; bài so sánh から／ので／て có nhiều đoạn ví dụ không ghép liền.",
    "107771cc": "49 H5/46 H6; bài so sánh cho/nhận có nhiều cặp thiếu hoặc lồng nhau.",
    "83a24a8c": "23 H5/22 H6 ở hai cách dùng ý định; cần ghép và kiểm lời dẫn hội thoại.",
    "2c47ef34": "52 H5/56 H6, có dịch lẻ trong nhiều mục ように; chưa thể bảo toàn cặp bằng phép chuyển tự động.",
    "0c06187e": "22 H5/20 H6; ために bao gồm mục đích và lợi ích, cần ghép đủ ví dụ.",
    "32f91ce9": "18 H5/18 H6 nhưng hội thoại có hai H5 liên tiếp rồi hai H6; phải tách theo lượt.",
    "173cd56e": "9 cặp hiển thị nhưng có hội thoại gộp và nhiều câu trong một H5; cần tách từng lượt.",
    "83c830c2": "49 H5/50 H6; bài tổng hợp ba thời điểm ところ có bản dịch lẻ.",
    "d46cf19d": "12 H5/12 H6 nhưng một đoạn hội thoại có hai H5 rồi hai H6; cần tách theo lượt.",
    "84c447b3": "34 H5/33 H6; mục はず có lời dẫn không đi kèm dịch, cần đối chiếu thủ công.",
    "f62c3280": "17 H5/13 H6; ～やります gộp nhiều nghĩa và ví dụ chưa ghép đủ.",
    "62fb39ee": "32 H5/31 H6; có ví dụ sai/đúng minh họa ようにする phải phân loại trước khi upload.",
    "8a990587": "24 H5/24 H6 nhưng nhiều bản dịch không đứng cạnh câu Nhật.",
    "92f918c3": "18 H5/16 H6; hai câu đánh dấu (X) là phản ví dụ không có dịch, không nên ép thành cặp hợp lệ.",
    "5e8c84a0": "15 H5/15 H6 nhưng hội thoại và lời bình chen giữa câu và bản dịch.",
    "846b121c": "25 H5/24 H6; bài ý định có các ví dụ và chú thích không ghép đều.",
    "003e4a48": "26 H5/26 H6 nhưng hội thoại A/B có hai H5 liên tiếp rồi hai H6; cần tách theo lượt.",
    "42f5dd0a": "32 H5/32 H6 nhưng lời dẫn chen giữa cặp ở các cách dùng てしまう.",
    "d33f33a3": "16 H5/15 H6; ～てやる có một câu thiếu dịch và sắc thái xã hội cần biên tập.",
    "a38f78db": "18 H5/13 H6; năm H5 là bảng chuyển dạng ～やすい, không phải câu ví dụ.",
    "521d31fd": "16 H5/18 H6 và một ảnh; nhiều lời dịch lẻ trong bài んです cần ghép thủ công.",
    "a1bcb005": "Bài ～いい gộp nhiều chức năng, có H4 và câu Nhật hỏng như そちら hoのほう／わたしが無いのよ; cần duyệt ngữ nghĩa từng hội thoại.",
}


def loose_pairs(body):
    pairs = []
    for i, line in enumerate(body):
        if line.startswith("##### "):
            j = i + 1
            while j < len(body) and not body[j].strip():
                j += 1
            if j >= len(body) or not body[j].startswith("###### "):
                raise ValueError("unpaired_H5")
            ja = re.sub(r"^\d+\.\s*", "", line[6:].strip()).strip()
            vi = re.sub(r"^→\s*", "", body[j][7:].strip()).strip()
            if not ja or not vi or re.search(r"[*_`]", ja + vi):
                raise ValueError("formatted_or_empty_example")
            role = ""
            m = re.match(r"^(A|B|C|客|店員|学生|先生)\s*[:：]\s*(.+)", ja)
            if m:
                role, ja = m.group(1), m.group(2)
            elif ja.startswith("ー"):
                role, ja = "lượt đáp", ja[1:].strip()
            pairs.append((ja, vi, role))
        elif line.startswith("###### "):
            k = i - 1
            while k >= 0 and not body[k].strip():
                k -= 1
            if k < 0 or not body[k].startswith("##### "):
                raise ValueError("orphan_H6")
    return pairs


def build(path, description, structures):
    h, body = parse(path)
    assert h["jlpt"] == "N4" and h["id"][:8] in PLANS
    if h["id"].startswith("6bd63e67"):
        body = [s.replace("「ちゅうしゃきんし」**と読みます**。", "「ちゅうしゃきんし」と読みます。")
                  .replace("\\[立ち入り禁止\\] と書いてあります。", "「立ち入り禁止」と書いてあります。")
                  .replace("Có viết là “Không dẫm lên (vạch, cỏ)”.", "Có ghi là “Cấm vào”.") for s in body]
    if h["id"].startswith("8ec25d8f"):
        body = [s.replace("来れれれば", "来られれば") for s in body]
    source_pairs = loose_pairs(body)
    images = [line for line in body if "![" in line]
    h["description"] = description
    h["conjugation"] = "／".join(structures)
    assert len(h["conjugation"]) <= 1024
    result = ["---"]
    for key in ("id", "jlpt", "name", "description", "conjugation"):
        result.append(f"{key}: {json.dumps(h[key], ensure_ascii=False)}")
    result += ["---", "", "# " + h["name"], "", "> " + description, "", "---", "", "## Cấu trúc ngữ pháp", ""]
    for i, structure in enumerate(structures):
        result.append("> **" + structure + "**" + ("<br>" if i + 1 < len(structures) else ""))
    result += ["", "## Nội dung và ví dụ", ""]
    first = next(i for i, line in enumerate(body) if line.strip())
    assert body[first].startswith("# "), path
    tail = body[first + 1:]
    n = 1
    pair_index = 0
    i = 0
    while i < len(tail):
        line = tail[i]
        if h["id"].startswith("9a15b593") and "Người nói chỉ chắc chắn" in line:
            line = line.replace("Người nói chỉ chắc chắn **khoảng 50%.**", "Mẫu này không gắn với một tỷ lệ chắc chắn cố định.")
        if line == "## Cấu trúc ngữ pháp":
            line = "## Chi tiết cấu trúc từ bản gốc"
        if line.startswith("#### "):
            line = "### " + line[5:]
        if re.match(r"^#{2,3} ", line):
            n = 1
        if line.startswith("##### "):
            j = i + 1
            while j < len(tail) and not tail[j].strip():
                j += 1
            ja, vi, role = source_pairs[pair_index]
            if role:
                result += [f"*Vai trong bản gốc: {role}.*", ""]
            result += [f"##### {n}. {ja}", "###### → " + vi, ""]
            pair_index += 1
            n += 1
            i = j + 1
            continue
        result.append(line)
        i += 1
    while result and not result[-1].strip():
        result.pop()
    new_body = result[result.index("---", 1) + 1:]
    validate_body(new_body, h["name"], path)
    assert [(ja, vi) for ja, vi, _ in loose_pairs(new_body)] == [(ja, vi) for ja, vi, _ in source_pairs]
    assert pair_index == len(source_pairs)
    assert [s for s in new_body if "![" in s] == images
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / path.name).write_text("\n".join(result) + "\n", encoding="utf-8")
    return len(source_pairs), len(images)


def main():
    deferred = json.loads(DEFERRED.read_text(encoding="utf-8"))["entries"]
    queue = [e for e in deferred if e["status"] == "deferred" and e["file"].startswith("N4/")]
    assert len(queue) == 59
    rows = []
    for e in queue:
        path = BASE / Path(e["file"]).name
        key = e["id"][:8]
        row = dict(e)
        if key in PLANS:
            try:
                pairs, images = build(path, *PLANS[key])
            except (ValueError, AssertionError, IndexError) as exc:
                row.update(status="deferred", editorial_reason=f"conversion_check_failed: {exc}")
            else:
                row.update(status="converted", pairs=pairs, images=images)
                if key == "6bd63e67":
                    row["editorial_changes"] = ["Bỏ bold khỏi một H5", "Chuẩn hóa cách ghi 立ち入り禁止", "Sửa nghĩa 立ち入り禁止 từ Không dẫm lên thành Cấm vào"]
                elif key == "8ec25d8f":
                    row["editorial_changes"] = ["Sửa dạng điều kiện khả năng 来られる → 来られれば (bản cũ ghi 来れれれば)"]
                elif key == "9a15b593":
                    row["editorial_changes"] = ["Bỏ khẳng định かもしれません luôn tương ứng 50% chắc chắn"]
        else:
            row["editorial_reason"] = REASONS[key]
        rows.append(row)
    summary = {"N4_deferred_input": len(queue), "converted": sum(r["status"] == "converted" for r in rows), "remaining": sum(r["status"] == "deferred" for r in rows), "pairs_retained": sum(r.get("pairs", 0) for r in rows), "images_preserved": sum(r.get("images", 0) for r in rows), "corrected_translation_pairs": 1}
    AUDIT.write_text(json.dumps({"summary": summary, "entries": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
