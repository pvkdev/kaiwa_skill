"""Build the two optional JLPT reading sections reviewed against the lesson 39 snapshots."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEWED = {
    "short_reading":"2ac6e0fd797cf3e979015665bf184929f483cb220e81fd008085d52dc113a736",
    "long_reading":"94093ba0c02e101f6613109e1b1bfe7e9bab91c3f3cf13fbddf9a238af1fe283",
}


def question(sid, prompt, choices, key, why, evidence):
    return {"id":"minna.l39.read."+sid, "source_item_id":sid if sid.startswith("p7-") else None,
            "prompt_ja":prompt, "choices":[{"id":str(i+1),"text":s} for i,s in enumerate(choices)],
            "correct_choice_id":str(key), "explanation_vi":why, "evidence_paragraph_id":evidence,
            "answer_provenance":"ai_editorial"}


def main():
    short = ["着物","洋服"]
    questions = {
        "short_reading":[
            question("p7-1","本文によると、今、普段の生活で着る人が多いのはどちらですか。",short,2,
                     "Đoạn 2 giải thích Âu phục dễ mặc và hợp với sinh hoạt hiện nay. Kimono được nhắc ở đoạn cuối với các dịp đặc biệt.","p7-pa-2"),
            question("p7-2","着るのに時間がかかるのはどちらですか。",short,1,
                     "Đoạn 1 nói 着物を着るのは難しいし、時間もかかって. Cụm 時間もかかって nói về việc mặc kimono.","p7-pa-1"),
            question("p7-3","本文によると、仕事をするときに便利なのはどちらですか。",short,2,
                     "Đoạn 1 kể rằng kimono bất tiện khi làm việc nên người ta chuyển sang mặc Âu phục.","p7-pa-1"),
            question("p7-4","今では、特別な機会にだけ着ることが多いのはどちらですか。",short,1,
                     "Đoạn cuối nêu đám cưới, lễ trưởng thành và Tết làm ví dụ cho 特別な機会にだけ着る. Chủ ngữ ở đây là 着物.","p7-pa-3")],
        "long_reading":[
            question("rescue","鳥島にいた五人は、どうやって島を出ましたか。",["自分たちで新しい船を作りました。","アメリカの船に助けられました。","日本から家族が迎えに来ました。"],2,
                     "Đoạn 3 kể rằng sau 143 ngày, năm người được một tàu săn cá voi của Mỹ cứu. Việc Manjiro học đóng tàu xảy ra sau đó.","p3"),
            question("return","日本へ帰った万次郎たちがすぐに捕まったのは、どうしてですか。",["当時、外国に出た日本人が帰ることは許されていなかったから。","村の船をアメリカで売ってしまったから。","英語を教えることが禁止されていたから。"],1,
                     "Đoạn 6 giải thích lệnh cấm trở về của Mạc phủ. Đoạn 7 kể việc họ bị bắt ngay khi về Nhật, rồi mới được thả.","p6"),
            question("work","1853年から、万次郎はどんな仕事をしましたか。",["アメリカの船長として魚を取りました。","高知で数学だけを教えました。","通訳や翻訳をしたり、英語を教えたりしました。"],3,
                     "Đoạn 9 liệt kê phiên dịch, biên dịch, dạy tiếng Anh và đóng tàu. Việc học toán thuộc quãng đời ở Mỹ.","p9")]
    }
    sections = []
    for family, qs in questions.items():
        doc = json.loads((ROOT/f"normalized/lesson-39/{family}.json").read_bytes())
        if Path(doc["source_snapshot"]).stem != REVIEWED[family]:
            raise ValueError(f"Recheck lesson 39 answers against the updated {family} passage")
        ps = doc["paragraphs"]
        ids = {p["source_id"] for p in ps}
        if not all(q["evidence_paragraph_id"] in ids for q in qs):
            raise ValueError(f"Reading evidence changed: {family}")
        sections.append({"id":f"minna.l39.{family}","kind":"jlptReading","source_snapshot":doc["source_snapshot"],
                         "source_url":doc["source_url"],"optional":True,
                         "question_provenance":"adapted_from_source_items" if family=="short_reading" else "ai_authored_from_passage",
                         "cluster_prompt_ja":"本文を読んで、質問に答えてください。",
                         "media":{"kind":"passage","ja":"\n\n".join(p["ja"] for p in ps),
                                  "vi":"\n\n".join(p["vi"] for p in ps)},"questions":qs})
    path = ROOT/"authored/lesson-39/reading.json"
    path.write_text(json.dumps({"lesson":39,"sections":sections},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


if __name__ == "__main__":
    main()
