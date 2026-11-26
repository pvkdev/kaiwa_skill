"""Build the portable Minna viewer from the two reviewed release ZIPs (pip install mistune>=3,<4)."""
import base64
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZipFile

import mistune

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "exports/harumii/minna-50-exercises-preview.zip"
GRAMMAR = ROOT / "exports/grammar-upload/minna-n5-n4-grammar-r2.zip"
TEMPLATE = Path(__file__).with_name("roadmap_viewer.template.html")
OUTPUT = ROOT / "lo-trinh-minna.html"


def load(z, name):
    return json.loads(z.read(name))


def questions(content, prefix):
    if "jlpt_block" in content:
        result = []
        for q in content["jlpt_block"]["questions"]:
            options = q["choices"]
            answer = next(i for i, c in enumerate(options) if c["id"] == q["correctChoiceId"])
            result.append({"id":q["id"], "prompt":q["prompt"]["text"], "vi":q["prompt"].get("textVi"),
                           "choices":[c["text"] for c in options], "key":[answer], "why":q["explanation"]})
        return result
    result = []
    for i, q in enumerate(content["questions"]):
        item = {"id":f"{prefix}.{i+1}", "prompt":q["question_ja"], "vi":q.get("question"),
                "instruction":content.get("cluster_prompt_ja"), "why":q["explanation"]}
        if "blank_answers" in q:
            item["blanks"] = q["blank_answers"]
        else:
            item["choices"] = q["choices"]
            item["multi"] = "correct_indices" in q
            item["key"] = q.get("correct_indices", [q["correct_index"]])
        result.append(item)
    return result


def extra_section(section, audio_file=None):
    c = section["storage"]["content"]
    result = {"id":section["id"],"kind":section["kind"],"questions":questions(c,section["id"])}
    for item in c.get("jlpt_block",{}).get("mediaItems",[]):
        if item["kind"] == "audio":
            a = item["audio"]
            result.update(audio=audio_file, transcript=[a["scriptJaMd"],a["scriptViMd"]])
        elif item["kind"] == "passage":
            p = item["passage"]
            result["passage"] = [p["jaMd"],p["viMd"]]
    return result


def lesson(z,n):
    d = load(z,f"lessons/{n:02}.json")
    text = z.read(d["vocabulary"]["path"]).decode("utf-8-sig")
    words = [list(map(str.strip, line.strip().strip("|").split("|",4))) for line in text.splitlines()
             if re.match(r"^\|\s*\d+\s*\|",line)]
    if len(words) != d["vocabulary"]["word_count"] or [int(w[0]) for w in words] != list(range(1,len(words)+1)):
        raise ValueError(f"Vocabulary rows differ in lesson {n}")
    data = {"n":n,"words":words,"nodes":d["nodes"],"groups":[],"source":d["grammar_source"],
            "tracks":json.loads(d["media_context"].get("data-mg-tracks","{}")), "extra":{}}
    for g in d["groups"]:
        group = {k:g[k] for k in ("grammar_ref","title","meaning","formula","usage","examples","video_asset")}
        items = []
        for row in g["practice"]:
            [item] = questions(row["storage"]["content"],row["id"])
            items.append({**item,"id":row["id"],"bank":row["bank"],"source_id":row["source_id"]})
        data["groups"].append({**group,"items":items})
    for k, path in d.get("supplements",{}).items():
        doc = load(z,path)
        if k=="reading_exercises":
            data["extra"][k] = {s["id"].split(".")[-1]: questions(s["storage"]["content"],s["id"]) for s in doc}
        elif k in ("assessment_exercises","listening_exercises"):
            data["extra"][k] = [extra_section(s,s.get("audio_file")) for s in doc["sections"]]
        else:
            data["extra"][k] = doc.get("sections",doc.get("paragraphs"))
    return data


def build():
    with ZipFile(RELEASE) as z:
        manifest = load(z,"manifest.json")
        for name, digest in manifest["sha256"].items():
            if sha256(z.read(name)).hexdigest() != digest:
                raise ValueError(f"Checksum mismatch for {name}")
        lessons = [lesson(z,n) for n in range(1,manifest["lesson_count"]+1)]
        audio = {s:"data:audio/mpeg;base64,"+base64.b64encode(z.read(s)).decode()
                 for s in z.namelist() if s.endswith(".mp3")}
        pilot = load(z,manifest["supplements"]["lesson_39_pilot"])
        lessons[38]["extra"]["pilot"] = pilot["nodes"]
        lessons[38]["extra"]["templates"] = [
            extra_section(s, manifest["supplements"]["pending_listening_asset"] if s["kind"]=="jlptListening" else None)
            for s in load(z,manifest["supplements"]["lesson_39_five_templates"])]
    markdown = mistune.create_markdown(escape=True,plugins=["table"])
    library = []
    with ZipFile(GRAMMAR) as z:
        for name in sorted(z.namelist()):
            text = z.read(name).decode("utf-8-sig").replace("\r\n","\n")
            _,head,body = text.split("---\n",2)
            fields = {}
            for line in head.splitlines():
                key,value = line.split(":",1)
                value = value.strip()
                fields[key] = json.loads(value) if value.startswith('"') else value
            # Preserve a link to remote illustrations. No external resource loads on file open.
            body = re.sub(r'!\[([^\]]*)\]\((https?://[^ )]+)\)',
                          lambda match:f"[{match[1] or 'Xem ảnh minh họa'} (cần mạng)]({match[2]})",body)
            body = re.sub(r"(?m)^# [^\n]*\n","",body,count=1)
            body = re.sub(r"<br\s*/?>","  \n",body,flags=re.I)
            library.append({"id":fields["id"],"name":fields["name"],"level":fields["jlpt"],
                            "meaning":fields.get("description",""),"html":markdown(body)})
    bank = Counter(q["bank"] for le in lessons for g in le["groups"] for q in g["items"])
    if any(bank[k]!=manifest["counts"][k] for k in bank):
        raise ValueError("Question count mismatch")
    data = json.dumps({"lessons":lessons,"library":library,"audio":audio},ensure_ascii=False,separators=(",",":"))
    data = data.replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count("__COURSE_JSON__") != 1:
        raise ValueError("Missing template data slot")
    OUTPUT.write_text(template.replace("__COURSE_JSON__",data),encoding="utf-8",newline="\n")
    print(f"{OUTPUT} | {len(lessons)} lessons, {len(library)} articles, {bank.total()} grammar exercises")


if __name__ == "__main__":
    build()
