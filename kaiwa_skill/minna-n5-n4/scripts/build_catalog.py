"""Generate the 50-lesson candidate index offline. Preserve previously edited records."""
import json
from pathlib import Path

CATALOG = Path(__file__).resolve().parents[1] / "catalog" / "sources.json"
SUFFIXES = {
    "lesson": "", "grammar": "-ngu-phap", "shadowing": "-luyen-doc",
    "conversation": "-hoi-thoai", "listening": "-luyen-nghe",
    "short_reading": "-bai-tap", "long_reading": "-25-bai-doc-hieu",
    "assessment": "-kiem-tra",
}


def build_catalog():
    data = (json.loads(CATALOG.read_text(encoding="utf-8")) if CATALOG.exists()
            else {"schema_version": 1, "course_id": "minna-n5-n4", "lessons": {}})
    if data["schema_version"] != 1 or data["course_id"] != "minna-n5-n4":
        raise ValueError("Unexpected catalog version or course")
    for number in range(1, 51):
        lesson = data["lessons"].setdefault(f"{number:02}", {
            "lesson_number": number, "target_level": "N5" if number <= 25 else "N4",
            "pages": {},
        })
        for family, suffix in SUFFIXES.items():
            url = f"https://www.vnjpclub.com/minna-no-nihongo/bai-{number}{suffix}.html"
            lesson["pages"].setdefault(family, {"candidate_url": url, "status": "candidate"})
    CATALOG.parent.mkdir(exist_ok=True)
    output = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if not CATALOG.exists() or CATALOG.read_text(encoding="utf-8") != output:
        tmp = CATALOG.with_suffix(".json.tmp")
        tmp.write_text(output, encoding="utf-8")
        tmp.replace(CATALOG)
    print(CATALOG)


if __name__ == "__main__":
    build_catalog()
