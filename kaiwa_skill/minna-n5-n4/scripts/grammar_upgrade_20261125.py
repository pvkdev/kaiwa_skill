"""Build the reviewed lesson-39 Harumii grammar upload and audit its source."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materials/grammar"
OUT = ROOT / "authored/grammar-upload/2026-11-25"
REPORT = ROOT / "reports/grammar-upgrade-2026-11-25-audit.json"

SPECS = {
    "61594c26": {
        "description": "Nối các hành động, tính chất hoặc nêu nguyên nhân dẫn tới cảm xúc và kết quả",
        "conjugation": "Vて／Vなくて／Aい→Aくて／Aな・N＋で",
        "structures": ["Vて、〜", "Vなくて、〜", "Aい → Aくて、〜", "Aな・N ＋ で、〜"],
        "intro": [
            "Dạng nối **て／で** liên kết hai vế. Nghĩa cụ thể phụ thuộc vào quan hệ giữa hai vế; thì của câu thường nằm ở vế cuối.",
            "- **Trình tự:** hành động trước dẫn đến hành động sau (ví dụ 1–5, 8).",
            "- **Nguyên nhân:** sự việc trước gây ra cảm xúc, trạng thái hoặc kết quả ở vế sau (ví dụ 6–10). Ở cách dùng này, vế sau thường là cảm xúc hay kết quả tự nhiên; khi nêu lý do cho mệnh lệnh hoặc ý chí, cân nhắc から／ので.",
            "- **Liệt kê tính chất, thông tin:** nối tính từ, danh từ hoặc các mệnh đề miêu tả (ví dụ 11–18).",
            "Dạng **Vなくて** cũng có thể nêu nguyên nhân, chẳng hạn 会えなくて寂しいです. Với danh từ chỉ thiên tai hoặc biến cố, **Nで** có thể trực tiếp nêu nguyên nhân: 台風で建物が倒れました.",
        ],
        "sections": [("Ví dụ", list(range(1, 19)))],
        "fix": {
            3: (None, "Cuối tuần tôi đi mua sắm với bạn, cùng ăn cơm rồi xem phim."),
            7: ("お元気で、本当によかったです。", "Tôi rất vui vì anh vẫn khỏe."),
            11: (None, "Tàu Shinkansen vừa nhanh vừa an toàn."),
            16: ("木村さんは会社員で、田中さんは銀行員です。", None),
        },
        "notes_after": {7: "*Bối cảnh: gặp lại sau mười năm.*"},
    },
    "447866c5": {
        "description": "Chỉ nơi diễn ra hành động, phương tiện, nguyên nhân, phạm vi, nhóm người hoặc thời lượng",
        "conjugation": "N ＋ で ＋ V／A／です",
        "structures": ["N（địa điểm・phương tiện・nguyên nhân・phạm vi）＋ で ＋ V", "N（số người・thời gian・giá tiền）＋ で ＋ V／です"],
        "intro": [
            "Trợ từ **で** gắn với danh từ để chỉ bối cảnh hoặc cách thực hiện hành động. Nghĩa thay đổi theo danh từ đứng trước và vị ngữ đứng sau.",
            "**きれいで** và **ベトナム人で** là dạng nối của tính từ な hoặc danh từ; chúng không phải cùng cách dùng với trợ từ chỉ địa điểm. Các ví dụ này được giữ để phân biệt.",
        ],
        "sections": [
            ("Nơi diễn ra hành động", list(range(1, 8))),
            ("Phương tiện và ngôn ngữ", list(range(8, 13))),
            ("Dạng nối của tính từ な và danh từ", [13, 14]),
            ("Nhóm người cùng thực hiện", [15, 16, 17, 27, 28]),
            ("Nguyên nhân là biến cố", [18]),
            ("Giá tiền và thời gian cần để hoàn thành", [19, 20, 29, 30]),
            ("Phạm vi và điều kiện", [21, 22, 23, 24]),
            ("Phân biệt でも／では", [25, 26]),
        ],
        "notes": {
            "Nơi diễn ra hành động": "Địa điểm hành động dùng **で**; nơi tồn tại của người hoặc vật thường dùng **に**. Ví dụ 6–7 là hai lượt của một đoạn hỏi đáp.",
            "Nhóm người cùng thực hiện": "Với **ひとりで**, **二人で**, **家族で**, で cho biết người cùng tham gia hoặc cách thực hiện; không chỉ địa điểm.",
            "Phân biệt でも／では": "Trong **あしたでも** và **これでは**, で kết hợp với trợ từ も／は. Hai ví dụ được giữ để người học nhận ra tổ hợp này, không xem chúng là で đơn lẻ.",
        },
        "fix": {
            3: (None, "Tôi sẽ ăn tối ở nhà hàng."),
            7: ("日本語学校で勉強しました。", None),
            18: ("事故で、２人が亡くなりました。", "Hai người đã thiệt mạng vì tai nạn."),
            22: ("日本では、３月と４月と５月は春です。", None),
            25: ("あしたでもいいです。", None),
            26: ("これではだめです。", None),
            28: ("家族全員でドライブしました。", "Cả gia đình đã đi chơi bằng ô tô."),
        },
    },
    "d740c696": {
        "description": "Nêu lý do, nguyên nhân cho một sự việc hoặc lời đề nghị",
        "conjugation": "V・Aい thể thường＋ので／Aな・N＋なので; Vます＋ので trong lời nói lịch sự",
        "structures": ["V・Aい（thể thường）＋ ので", "Aな・N ＋ なので", "Vます ＋ ので（lịch sự）"],
        "intro": [
            "**ので** nêu lý do cho sự việc hoặc lời đề nghị ở vế sau. Cách nói này thường trình bày lý do mềm hơn **から**.",
            "Với tính từ な và danh từ ở hiện tại khẳng định, cần **な** trước ので: **好きなので**, **工事中なので**. Có thể dùng **ますので** khi nói lịch sự.",
        ],
        "sections": [("Ví dụ", list(range(1, 10)))],
        "fix": {
            1: ("明日、病院へ行きますので、学校を休みます。", "Vì ngày mai phải đến bệnh viện nên tôi sẽ nghỉ học."),
            2: ("歯医者の予約がありますので、２時ごろ会社へ行きます。", "Vì có hẹn với nha sĩ nên khoảng 2 giờ tôi mới đến công ty."),
            3: ("頭がとても痛いので、会社を休みました。", None),
            6: ("彼女はここのコーヒーが好きなので、よく来ます。", None),
            8: ("今、工事中なので、この道は車が通れません。", None),
            9: ("あした試験があるので、今夜は早く寝てください。", "Vì ngày mai có bài thi nên tối nay hãy đi ngủ sớm."),
        },
    },
    "3fd64d53": {
        "description": "Giữa chừng một việc đang diễn ra hoặc trên đường đi đến đâu đó",
        "conjugation": "Vる／Vている＋途中で; Nの＋途中で",
        "structures": ["Vる ＋ 途中で", "Vている ＋ 途中で", "N ＋ の途中で"],
        "intro": [
            "**途中で** đánh dấu một thời điểm ở giữa quá trình. Với động từ chuyển động, nó thường có nghĩa “trên đường”; với hoạt động khác, nó thường có nghĩa “giữa lúc đang làm”.",
            "Dùng **Vている途中で** để nhấn mạnh hành động đang diễn ra. **Nの途中で** dùng với danh từ chỉ hoạt động hoặc hành trình, như 会議の途中で, 散歩の途中で.",
        ],
        "sections": [("Ví dụ", list(range(1, 14)))],
        "fix": {
            1: ("学校に行く途中で、ノートを家に忘れたことに気づいたので帰りました。", "Trên đường đến trường, tôi nhận ra đã để quên vở ở nhà nên quay về."),
            2: ("考えている途中で、田中さんが私の名前を呼びました。", "Đang suy nghĩ thì anh Tanaka gọi tên tôi."),
            3: ("宿題をやっている途中で、教室に忘れ物をしたことに気づきました。", "Đang làm bài tập thì tôi nhận ra mình đã để quên đồ ở lớp."),
            4: ("帰る途中で、社長から会社に戻るように電話がかかってきました。", "Trên đường về, tôi nhận được điện thoại của giám đốc bảo quay lại công ty."),
            5: ("ご飯を食べている途中で、知り合いが家を訪ねてきました。", "Đang ăn cơm thì một người quen đến thăm nhà."),
        },
    },
    "02683e06": {
        "description": "Phân biệt ý định của người nói với kế hoạch hoặc lịch trình đã xác định",
        "conjugation": "V thể ý chí＋と思います／V thể từ điển＋つもりです／V thể từ điển・Nの＋予定です",
        "structures": ["V thể ý chí ＋ と思います／と思っています", "V thể từ điển ＋ つもりです", "V thể từ điển・Nの ＋ 予定です"],
        "intro": [
            "Cả ba mẫu đều có thể dịch là **định làm**, nhưng sắc thái khác nhau:",
            "- **予定です**: một kế hoạch hoặc lịch trình đã được sắp xếp; mức độ cụ thể thường cao hơn ý định đơn thuần.",
            "- **つもりです**: ý định của người nói, thường đã có trước lúc nói; không nhất thiết đã xếp lịch.",
            "- **ようと思います**: suy nghĩ hoặc quyết định của người nói. Có thể là ý định mới nảy ra, cũng có thể là ý định đã có; **ようと思っています** thường nhấn mạnh ý định đã duy trì một thời gian.",
            "Ba câu đầu dùng cùng đích đến Osaka để so sắc thái. Với một việc thường ngày như ngủ sớm, **早く寝ようと思います** là tự nhiên; **早く寝るつもりです** cũng đúng khi người nói đã có ý định rõ, còn **早く寝る予定です** phù hợp khi việc đó gắn với lịch hoặc kế hoạch cụ thể. Không nên coi hai mẫu sau là sai tuyệt đối.",
        ],
        "sections": [("Ví dụ", [1, 2, 3, 4])],
        "fix": {
            1: (None, "Tôi có kế hoạch đi Osaka."),
            2: (None, "Tôi định đi Osaka."),
            3: (None, "Tôi đang nghĩ sẽ đi Osaka."),
            4: (None, "Tôi định đi ngủ sớm."),
        },
    },
    "345b2e7c": {
        "name": "[Địa điểm] へ／に Vます(bỏ ます) に行きます／来ます",
        "description": "Đi hoặc đến một nơi để thực hiện mục đích",
        "conjugation": "[Địa điểm] へ／に ＋ Vます(bỏ ます)／N chỉ hoạt động ＋ に行きます／来ます",
        "structures": ["[Địa điểm] へ／に ＋ Vます(bỏ ます) ＋ に行きます／来ます", "[Địa điểm] へ／に ＋ N chỉ hoạt động ＋ に行きます／来ます"],
        "intro": [
            "**へ／に** sau địa điểm chỉ đích đến. **に** sau động từ ở dạng bỏ ます hoặc sau danh từ chỉ hoạt động đánh dấu mục đích đến đó.",
            "Nếu hành động có tân ngữ, **を** gắn với tân ngữ: 昼ごはんを食べに行きます. **を** không thay cho へ／に sau địa điểm trong cấu trúc này.",
        ],
        "sections": [("Ví dụ", [1, 2, 3, 4, 5, 6])],
        "fix": {
            1: ("スーパーへ買い物に行きます。", None),
            2: ("昼ごはんを食べに行きます。", "Tôi đi ăn trưa."),
            3: ("先生、資料をもらいに来ました。", None),
            4: (None, "Tôi đã đến Nhật để học tiếng Nhật."),
            5: ("サイゴンへ遊びに行きます。", "Tôi sẽ đến Sài Gòn chơi."),
            6: ("ハノイへお祭りを見に行きます。", None),
        },
    },
}


def parse(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    end = lines.index("---", 1)
    header = {}
    for line in lines[1:end]:
        key, _, value = line.partition(":")
        header[key] = json.loads(value) if value.strip().startswith('"') else value.strip()
    return header, lines[end + 1:]


def examples(body):
    pairs = []
    for i, line in enumerate(body):
        if line.startswith("##### "):
            j = i + 1
            while j < len(body) and not body[j].strip():
                j += 1
            assert j < len(body) and body[j].startswith("###### "), line
            ja = re.sub(r"^(?:\d+\.|ー)\s*", "", line[6:].strip()).strip()
            vi = re.sub(r"^→\s*", "", body[j][7:].strip()).strip()
            pairs.append((ja, vi))
    return pairs


def build_one(path, spec):
    h, body = parse(path)
    pairs = examples(body)
    requested = [i for _, ids in spec["sections"] for i in ids]
    assert Counter(requested) == Counter(range(1, len(pairs) + 1)), path
    h["name"] = spec.get("name", h["name"])
    h["description"] = spec["description"]
    h["conjugation"] = spec["conjugation"]
    lines = ["---"]
    for key in ("id", "jlpt", "name", "description", "conjugation"):
        lines.append(f"{key}: {json.dumps(h[key], ensure_ascii=False)}")
    lines += ["---", "", f"# {h['name']}", "", f"> {h['description']}", "", "---", "", "## Cấu trúc ngữ pháp", ""]
    for i, structure in enumerate(spec["structures"]):
        lines.append(f"> **{structure}**" + ("<br>" if i + 1 < len(spec["structures"]) else ""))
    lines += ["", "## Cách dùng", ""]
    for paragraph in spec["intro"]:
        lines += [paragraph, ""]
    for title, indices in spec["sections"]:
        lines += [f"## {title}", ""]
        note = spec.get("notes", {}).get(title)
        if note:
            lines += [note, ""]
        for n, old_index in enumerate(indices, 1):
            ja, vi = pairs[old_index - 1]
            fixed_ja, fixed_vi = spec.get("fix", {}).get(old_index, (None, None))
            ja, vi = fixed_ja or ja, fixed_vi or vi
            lines += [f"##### {n}. {ja}", f"###### → {vi}", ""]
            post = spec.get("notes_after", {}).get(old_index)
            if post:
                lines += [post, ""]
    target = OUT / path.parent.name / path.name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    actual = examples(parse(target)[1])
    expected = []
    for _, indices in spec["sections"]:
        for old_index in indices:
            ja, vi = pairs[old_index - 1]
            fixed_ja, fixed_vi = spec.get("fix", {}).get(old_index, (None, None))
            expected.append((fixed_ja or ja, fixed_vi or vi))
    assert actual == expected, f"Example preservation failed: {path}"
    assert sum("![" in s for s in body) == sum("![" in s for s in parse(target)[1]), f"Image preservation failed: {path}"
    return {"file": str(path.relative_to(BASE)).replace("\\", "/"), "id": h["id"], "examples_before": len(pairs), "examples_after": len(requested), "edited_example_indices": sorted(spec.get("fix", {})), "images_before": body.count("!["), "images_after": 0}


def main():
    files = sorted(BASE.glob("N[45]/*.md"))
    assert len(files) == 180
    audit = []
    selected = []
    for path in files:
        h, body = parse(path)
        ex = sum(s.startswith("##### ") for s in body)
        tr = sum(s.startswith("###### ") for s in body)
        audit.append({"file": str(path.relative_to(BASE)).replace("\\", "/"), "id": h["id"], "examples": ex, "translations": tr, "images": sum("![" in s for s in body), "h1": sum(s.startswith("# ") for s in body), "h4": sum(s.startswith("#### ") for s in body), "legacy_meaning": not any(s.startswith("> ") for s in body[:10])})
        key = h["id"][:8]
        if key in SPECS:
            selected.append(build_one(path, SPECS[key]))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({"baseline_count": len(files), "levels": dict(Counter(p.parent.name for p in files)), "selected": selected, "inventory": audit}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Audited {len(files)} baselines; authored {len(selected)} upgrades; {sum(x['examples_after'] for x in selected)} examples preserved.")


if __name__ == "__main__":
    main()
