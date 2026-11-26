"""Inspect the archived lesson 39 assessment DOM without network access."""
from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = next((ROOT / "sources/lesson-39/assessment").glob("*.json"))
OUTPUT = ROOT / "authored/lesson-39/assessment.json"

# Choice IDs are the archived DOM's data-option strings, not display letters.
KEY = {
    1: ("0", "'Ngạc nhiên, giật mình' là びっくりします; phải có び đầu từ, っ nhỏ và âm くり."),
    2: ("1", "'Thất vọng' là がっかりします; viết っ nhỏ sau が và giữ âm か không có dấu đục."),
    3: ("3", "Xà phòng là せっけん; âm ngắt viết bằng っ nhỏ, cuối từ là ん."),
    4: ("3", "Quầy lễ tân khách sạn là フロント; các lựa chọn khác nhầm dấu đục hoặc nhầm ソ với ン."),
    5: ("3", "Xe tải là トラック; ッ là chữ nhỏ và âm đầu là ト, không có dấu đục."),
    6: ("1", "答えます dùng với câu hỏi theo mẫu 質問に答えます, nghĩa là trả lời câu hỏi của thầy."),
    7: ("1", "通ります đi với địa điểm を để chỉ tuyến xe đi qua: 公園の前を通ります."),
    8: ("0", "Gọi nhầm tên trước mọi người khiến người nói xấu hổ, nên dùng 恥ずかしいです."),
    9: ("1", "Đỗ đại học là tin vui; 合格して、とてもうれしいです nghĩa là đỗ nên rất vui."),
    10: ("0", "Xe đâm vào tường là 車が壁にぶつかりました; trợ từ に chỉ vật bị va vào."),
    11: ("1", "複雑, 'phức tạp', đọc là ふくざつ; cả ざ và つ đều cần đúng âm."),
    12: ("0", "安心, 'an tâm', đọc là あんしん; あんぜん là 安全, nghĩa là an toàn."),
    13: ("1", "首相, 'thủ tướng', đọc là しゅしょう; không kéo dài âm しゅ đầu."),
    14: ("0", "地震, 'động đất', đọc là じしん; 地 đọc じ trong từ này."),
    15: ("3", "邪魔, 'vướng víu, cản trở', đọc là じゃま; ゃ là chữ nhỏ."),
    16: ("0", "りこん, 'ly hôn', viết là 離婚; 婚 là chữ 'hôn' trong hôn nhân."),
    17: ("0", "おおぜい, 'rất đông người', viết là 大勢, thường đi với 人 như 人が大勢."),
    18: ("2", "ふとりました nghĩa là 'đã béo lên', viết 太りました từ động từ 太ります."),
    19: ("2", "きたない nghĩa là 'bẩn', viết 汚い; vì đĩa bẩn nên cần rửa."),
    20: ("1", "かいじょう là địa điểm tổ chức buổi tiệc, viết 会場; 場 nghĩa là nơi chốn."),
    21: ("3", "事故で chỉ nguyên nhân khách quan 'do tai nạn'; vì vậy 事故でバスが遅れたんです."),
    22: ("2", "不便 là tính từ đuôi な; khi nối với 困ります để nêu nguyên nhân, dùng 不便で."),
    23: ("3", "会えない là phủ định thể khả năng; khi nêu cảm xúc buồn vì không gặp gia đình, đổi ない thành なくて."),
    24: ("3", "Trước ので, tính từ đuôi な cần な: 暇なので nghĩa là vì hôm nay rảnh."),
    25: ("3", "用事があるので nêu lý do từ chối lời rủ đi uống: vì có việc nên tôi xin về trước."),
    26: ("2", "Người B ngập ngừng vì bận việc; A hỏi lại 行けませんか, nên câu 忙しくて…… diễn tả lý do không đi được."),
    27: ("1", "Câu hỏi hỏi có ngủ được không, B đáp いいえ; phòng bên ồn khiến B 寝られませんでした, không ngủ được."),
    28: ("2", "Người nói không hiểu tiếng Nhật và xin được nói tiếng Anh; わからないので nêu lý do lịch sự trước lời nhờ vả."),
    29: ("3", "Hỏi buổi tiệc thế nào thì trả lời rằng đã nói chuyện với nhiều người nên vui: 話せて、楽しかったです."),
}


class Node:
    def __init__(self, tag="", attrs=(), parent=None, data=""):
        self.tag, self.attrs, self.parent, self.data = tag, dict(attrs), parent, data
        self.children = []

    def matches(self, tag=None, cls=None):
        return (tag is None or self.tag == tag) and (cls is None or cls in self.attrs.get("class", "").split())

    def findall(self, tag=None, cls=None):
        out = []
        for c in self.children:
            if c.matches(tag, cls):
                out.append(c)
            out.extend(c.findall(tag, cls))
        return out

    def one(self, tag=None, cls=None):
        return next(iter(self.findall(tag, cls)), None)

    def text(self):
        if self.tag in {"rt", "button", "svg"} or "screen-reader-text" in self.attrs.get("class", "").split():
            return ""
        if self.tag == "#text":
            return self.data
        return "".join(c.text() for c in self.children).strip()


class DOM(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.current = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in {"img", "br", "hr", "input", "source", "meta"}:
            self.current = node

    def handle_endtag(self, tag):
        current = self.current
        while current is not self.root and current.tag != tag:
            current = current.parent
        if current is not self.root:
            self.current = current.parent

    def handle_data(self, data):
        self.current.children.append(Node("#text", parent=self.current, data=data))


def read_items():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    for number, section in enumerate(source["sections"], 1):
        dom = DOM()
        dom.feed(section["html"])
        section_id = dom.root.one(cls="mt-sec").attrs["data-section"]
        for li in dom.root.findall("li", "mt-item"):
            qbody = li.one(cls="mt-q-body")
            question = qbody.one(cls="mt-ask")
            lines = qbody.findall(cls="mt-line")
            if lines:
                prompt = "\n".join(f"{line.one(cls='mt-who').text()}: {line.one(cls='mt-line-ja').text()}" for line in lines)
            else:
                prompt = question.text()
            hint = qbody.one(cls="mt-hint")
            target = qbody.one("u", "mt-u")
            choices = [
                {"id": x.attrs["data-option"], "text": x.one(cls="mt-opt-t").text()}
                for x in li.findall("button", "mt-opt")
            ]
            imgs = [x.attrs for x in qbody.findall("img")]
            yield {"section": number, "section_id": section_id, "source_id": li.attrs["id"],
                   "prompt": prompt, "hint_vi": hint.text() if hint else "",
                   "target": target.text() if target else "",
                   "choices": choices, "images": imgs, "source_class": li.attrs.get("class")}


def make_source():
    sections = []
    for item in read_items():
        number = int(item["source_id"].split("-")[-1])
        if not sections or sections[-1]["id"] != item["section_id"]:
            sections.append({"id": item["section_id"], "kind": "manualQnA", "questions": []})
        if item["section"] == 1:
            prompt_ja = f"「{item['prompt']}」に当たる日本語を選びなさい。"
            prompt_vi = f"Chọn cách viết đúng cho: {item['prompt']}."
        elif item["section"] in (3, 4):
            task = "読み方" if item["section"] == 3 else "漢字"
            prompt_ja = f"【{item['target']}】の{task}を選びなさい。\n{item['prompt']}"
            prompt_vi = f"Chọn {'cách đọc' if item['section'] == 3 else 'chữ Hán'} đúng cho {item['target']}."
        else:
            prompt_ja = item["prompt"].replace("（　）", "(...)")
            prompt_vi = item["hint_vi"]
        choices = item["choices"]
        if number == 28:
            # The archived わからなくて can also introduce a reason in this sentence.
            # Make that distractor ungrammatical so the edited exercise has one key.
            choices = [dict(x) for x in choices]
            choices[3]["text"] = "日本語が わからないくて"
        correct, explanation = KEY[number]
        sections[-1]["questions"].append({
            "id": item["source_id"], "source_id": item["source_id"],
            "prompt_ja": prompt_ja, "prompt_vi": prompt_vi,
            "choices": choices, "correct_choice_id": correct,
            "explanation_vi": explanation,
            **({"adaptation_note": "Phương án 3 của bản lưu (わからなくて) có thể diễn đạt lý do; đổi thành わからないくて để chỉ còn một đáp án."} if number == 28 else {}),
        })
    return {"lesson": 39, "source_snapshot": SOURCE.relative_to(ROOT).as_posix(),
            "source_url": json.loads(SOURCE.read_text(encoding="utf-8"))["url"],
            "sections": sections}


if __name__ == "__main__":
    source = make_source()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(source, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(source['sections'])} sections / {sum(len(s['questions']) for s in source['sections'])} questions -> {OUTPUT}")
