"""Place exercises after the last required grammar point in each lesson's source order."""
from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT / name).read_bytes())


def make_order():
    manifest = []
    group_counts = Counter()
    video_ids = read("catalog/grammar-video-ids.json")
    for lesson in read("catalog/grammar-points.json"):
        n = lesson["lesson"]
        relative = f"lesson-{n:02}"
        points = lesson["points"]
        order = {p["id"]:i for i,p in enumerate(points)}
        registered = video_ids[str(n)]
        if (len(order) != len(points) or not order.keys() <= registered.keys()
                or len(set(registered.values())) != len(registered)
                or any(not re.fullmatch(rf"minna\.l{n:02}\.g\d+\.video", s) for s in registered.values())):
            raise ValueError(f"Review permanent video IDs for lesson {n}")
        pairs = [{"grammar_ref":p["id"], "title":p["title"], "video_asset":registered[p["id"]],
                  "quick_checks":[], "renshuu_b":[]} for p in points]
        for unit, field in (("quick-checks","quick_checks"),("renshuu","renshuu_b"),("renshuu-drills","extra_drills")):
            if unit == "renshuu-drills" and not (ROOT/f"authored/{unit}/{relative}.json").exists():
                continue
            doc = read(f"authored/{unit}/{relative}.json")
            for item in doc["items"]:
                refs = item["grammar_refs"]
                if not refs or not set(refs) <= order.keys():
                    raise ValueError(f"{item['id']}: incomplete grammar mapping")
                after = max(refs, key=order.__getitem__)
                if item.get("placement_after_point_id", after) != after:
                    raise ValueError(f"{item['id']}: disagrees with reviewed placement")
                pairs[order[after]].setdefault(field, []).append(item["id"])
                group_counts[field] += 1
        if not all(p["quick_checks"] for p in pairs):
            raise ValueError(f"Lesson {n} has grammar points without any practice")
        row = {"lesson":n, "source":lesson["url"], "normalized":f"normalized/{relative}/grammar.json",
               "quick_check_bank":f"authored/quick-checks/{relative}.json",
               "renshuu_b_bank":f"authored/renshuu/{relative}.json","grammar_practice_pairs":pairs}
        if any(p.get("extra_drills") for p in pairs):
            row["extra_drill_bank"] = f"authored/renshuu-drills/{relative}.json"
        if n == 39:
            pilot = read("authored/lesson-39/grammar-practice.json")
            pilot_nodes = pilot["nodes"][::2]
            row["pilot_bank"] = "authored/lesson-39/grammar-practice.json"
            by_asset = {p["video_asset"]:p for p in pairs}
            for node, practice in zip(pilot_nodes,pilot["nodes"][1::2],strict=True):
                target = by_asset.get(node["video_asset_id"])
                if target is None:
                    raise ValueError("Review retired lesson-39 pilot video binding")
                target["pilot_groups"] = [g["id"] for g in practice["groups"]]
        manifest.append(row)
    return manifest, group_counts


if __name__ == "__main__":
    result, counts = make_order()
    path = ROOT / "catalog/grammar-practice-order.json"
    temp = path.with_suffix(".json.tmp")
    temp.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",encoding="utf-8",newline="\n")
    temp.replace(path)
    print(f"{len(result)} lessons, {sum(len(x['grammar_practice_pairs']) for x in result)} video/practice pairs, {dict(counts)}")
