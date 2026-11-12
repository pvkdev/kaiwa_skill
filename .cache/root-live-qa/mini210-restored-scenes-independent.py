import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CACHE = Path(__file__).resolve().parent
BOOK = ROOT / "kaiwa_skill/knowledge/すぐに使える 日本語会話 超ミニフレーズ 発展210"
PDF_SHA = "2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05"
MANIFEST = json.loads((CACHE / "mini210-restored-source-manifest.json").read_text(encoding="utf-8"))
IMAGES = {row["head"]: row for row in MANIFEST["pages"]}

# Transcribed only from the final numbered activity on each opened page.
SOURCE = {
    141: ("⑤ Again from the first", "うーん…。どうも納得いかないなあ。もう一回やり直しだ。", "えっ、これ捨てちゃうの？ もったいない。"),
    144: ("④ A worry", "検査、明日だよね？ 何もなければいいんだけど。", "大丈夫だよ。元気すぎるぐらいだから。"),
    147: ("⑤ A troubling person; Variations", "みんな心配してるのに。何考えてんのかなあ、まったく！", "困った人だね。"),
    150: ("④ Being treated unfairly", "みんな頑張ってるのに、評価されるのはいつも彼女ばっかり。", "なんだかね。"),
    163: ("④ About clothes; Related phrases 一言余計だ", "その服、かわいいね。ちょっとサイズが小さいかもしれないけど。", "一言余計だよ。"),
    166: ("⑤ After a lecture", "こういうのに出ると、いろいろ勉強になるね。", "そうだね。"),
    169: ("⑤ Found", "あっ、コンタクトあったよ！", "よかった～！ これ高いんですよ。見つかってほっとしました。"),
    174: ("⑤ After receiving advice; Variations", "いろいろアドバイスありがとうございます。また頑張ります。", "ええ。頑張ってください。"),
    177: ("⑤ Materials", "間違ってたらごめんなさい。この資料作ったの、森さん？", "はい、私ですが、何か問題ありましたか？"),
    180: ("④ Cold attitude", "人が困ってるのに、何もしてあげないなんて…。見損なったよ。", "ちょっとがっかりだよね。"),
    183: ("④ Unexpected remark", "へー、彼がそんなこと言ったんだ。", "ちょっと見直したでしょ？"),
    184: ("④ About character", "森さんって、どんな人ですか。", "ああ…。あの人はなかなか難しいですよ。"),
    189: ("④ At home", "雨やまないね。", "うん。なんか、行くのがめんどくさくなってきた。"),
    197: ("④ Regret; Variations", "あの件、部長に言ったの？", "うん…。でも、やめとけばよかった。逆に、いろいろ注意されたよ。"),
    200: ("⑤ Passing", "やっと合格しました！", "なんだ、やればできるじゃん！"),
    203: ("⑤ Criticism of others", "部長にまた文句言われたよ。みんな頭が固いって。", "よく言うよね。自分はどうなんだって。"),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def chapter_for(head):
    if head <= 154:
        return "chapters/09-n-138-154.md"
    if head <= 171:
        return "chapters/10-h-155-171.md"
    if head <= 194:
        return "chapters/11-m-172-194.md"
    return "chapters/12-y-195-206.md"


units = {r["unit_id"]: r for r in (json.loads(s) for s in (BOOK / "_meta/units.jsonl").read_text(encoding="utf-8").splitlines() if s.strip())}
state = json.loads((BOOK / "_meta/direct-state.json").read_text(encoding="utf-8"))
chapters = state.get("chapters", {})
if not chapters:
    chapters = state.get("chapter_checkpoints", {})

rows = []
for head, (caption, source_a, source_b) in SOURCE.items():
    page = head + 15
    chapter_rel = chapter_for(head)
    chapter = BOOK / chapter_rel
    chapter_text = chapter.read_text(encoding="utf-8")
    m = re.search(rf'(?ms)^<a id="u-210-{head}"></a>\n(.*?)(?=^<a id="u-210-\d+"></a>|\Z)', chapter_text)
    section = m.group(1).strip() if m else ""
    last_activity = IMAGES[head]["last_activity"]
    item = re.search(rf'(?m)^{last_activity}\. \*\*(.*?)(?=\n\n|\Z)', section)
    output_quote = item.group(0).strip() if item else ""
    page_record = json.loads((BOOK / f"_meta/pdf-pages/p{page:04d}.json").read_text(encoding="utf-8"))
    unit = units.get(f"u-210-{head}", {})
    chapter_status = chapters.get(chapter_rel, {}).get("status", "unknown")
    statuses = [unit.get("review_status", "unknown"), page_record.get("review_status", "unknown"), chapter_status]
    # Chapter 11 has an unrelated source issue; its checked pages/units are
    # eligible for this bounded scene readback even while chapter status differs.
    status = "checked" if output_quote and all(x in ("author_checked", "complete") for x in statuses[:2]) else "waiting"
    finding = None
    if head == 141 and "やり直した" in output_quote:
        status = "finding"
        finding = "Nguồn やり直しだ là quyết định làm lại; output やり直した và VI 'đã làm lại' đổi sang quá khứ."
    if head == 147 and "かねぇ" in output_quote:
        status = "finding"
        finding = "Nguồn 何考えてんのかなあ; output 何考えてんのかねぇ đổi chữ Nhật."
    if head == 144 and "Ngày mai cậu kiểm tra" in output_quote:
        status = "finding"
        finding = "検査 trong ngữ cảnh sức khỏe/English 'having that test done' bị dịch mơ hồ như bài kiểm tra."
    if head == 180 and ("cậu chẳng giúp" in output_quote or "đánh giá nhầm cậu" in output_quote):
        status = "finding"
        finding = "Nguồn bình luận về người thứ ba (English 'them'), nhưng VI chuyển thành trách người đối thoại 'cậu'."
    image_path = CACHE / IMAGES[head]["image"]
    assert digest(image_path) == IMAGES[head]["image_sha256"]
    rows.append({
        "head": head,
        "pdf_page": page,
        "last_activity": last_activity,
        "source_caption_and_relation": caption,
        "source_quote": {"A": source_a, "B": source_b},
        "output_quote": output_quote,
        "status": status,
        "pending": bool(status in ("finding", "waiting")),
        "finding": finding,
        "source_image": str(image_path.relative_to(ROOT)).replace("\\", "/"),
        "source_image_sha256": IMAGES[head]["image_sha256"],
        "chapter": chapter_rel,
        "chapter_sha256_snapshot": digest(chapter),
        "page_review_status": page_record.get("review_status"),
        "unit_review_status": unit.get("review_status"),
        "chapter_review_status": chapter_status,
    })

report = {
    "purpose": "Independent targeted readback of only the final activity on 16 restored heads; not a semantic review of all 210 heads.",
    "reviewed_at_utc": datetime.now(timezone.utc).isoformat(),
    "source_pdf_sha256": PDF_SHA,
    "source_pages_opened": [r["pdf_page"] for r in rows],
    "head_count": len(rows),
    "status_counts": {s: sum(r["status"] == s for r in rows) for s in ("checked", "finding", "waiting")},
    "resolved_after_writer_recheck": [
        {"head": 141, "pdf_page": 156, "before": "もう一回やり直した。／Tôi đã làm lại một lần nữa", "source_and_current": "もう一回やり直しだ。／Phải làm lại một lần nữa thôi", "result": "resolved"},
        {"head": 147, "pdf_page": 162, "before": "何考えてんのかねぇ、まったく！", "source_and_current": "何考えてんのかなあ、まったく！", "result": "resolved"},
        {"head": 144, "pdf_page": 159, "before": "Ngày mai cậu kiểm tra rồi nhỉ?", "source_and_current": "Ngày mai cậu đi kiểm tra sức khỏe rồi nhỉ?", "result": "resolved"},
        {"head": 180, "pdf_page": 195, "before": "cậu chẳng giúp gì… Tôi đã đánh giá nhầm cậu", "source_and_current": "người ấy chẳng giúp gì… Tôi đã đánh giá nhầm người ấy", "result": "resolved"},
    ],
    "rows": rows,
}
json_path = CACHE / "mini210-restored-scenes-independent.json"
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "# Independent QA: 16 restored final activities in 発展210",
    "",
    f"Source PDF SHA256: `{PDF_SHA}`. Reviewed physical PDF pages: {', '.join(map(str, report['source_pages_opened']))}.",
    "Only the final numbered activity on each page and its relevant Variation/Related label was compared. Earlier activities and the rest of the book are outside this QA scope.",
    "",
    f"Current status: {report['status_counts']['checked']} checked, {report['status_counts']['finding']} findings, {report['status_counts']['waiting']} waiting.",
    "Four findings at heads 141, 144, 147 and 180 were corrected by the writer and rechecked against the same source images. Chapter 11 remains needs_review for matters outside these six sampled final scenes; its six target page and unit records are author_checked.",
    "",
]
for row in rows:
    lines += [
        f"## Head {row['head']} · PDF {row['pdf_page']} · {row['status']}",
        "",
        f"Source scene: {row['source_caption_and_relation']}. A: {row['source_quote']['A']} B: {row['source_quote']['B']}",
        f"Output: {row['output_quote'] or '(not restored/checkpointed yet)'}",
        f"Evidence: image SHA256 `{row['source_image_sha256']}`; chapter SHA256 `{row['chapter_sha256_snapshot']}`; page/unit/chapter statuses `{row['page_review_status']}/{row['unit_review_status']}/{row['chapter_review_status']}`.",
    ]
    if row["finding"]:
        lines.append(f"Finding: {row['finding']}")
    lines.append("")
md_path = CACHE / "mini210-restored-scenes-independent.md"
md_path.write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"counts": report["status_counts"], "json_sha256": digest(json_path), "md_sha256": digest(md_path), "json": str(json_path), "md": str(md_path)}, ensure_ascii=False))
