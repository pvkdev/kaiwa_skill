"""Build reviewable Harumii curriculum POST bodies from native storage. No network calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlsplit
from uuid import UUID


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export_dir", type=Path)
    ap.add_argument("--scope", choices=["grammar", "vocab"], default="grammar")
    ap.add_argument("--unit-id", default="<UNIT_ID>")
    ap.add_argument("--template-ids", type=Path, help="JSON format -> ExerciseTemplate UUID")
    ap.add_argument("--session-ids", type=Path, help="JSON group_key -> ExerciseSession UUID")
    ap.add_argument("--audio-urls", type=Path, help="JSON pending media ID -> verified Harumii playback HTTPS URL")
    ap.add_argument("--grouped", action="store_true", help="require each exercise to have grammar group and session mapping")
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    idx = json.loads((args.export_dir / "index.json").read_text(encoding="utf-8"))
    templates = json.loads(args.template_ids.read_text(encoding="utf-8")) if args.template_ids else {}
    sessions = json.loads(args.session_ids.read_text(encoding="utf-8")) if args.session_ids else {}
    audio_urls = json.loads(args.audio_urls.read_bytes()) if args.audio_urls else {}
    for value in [*templates.values(), *sessions.values(), *([args.unit_id] if args.unit_id != "<UNIT_ID>" else [])]:
        if UUID(value).int == 0:
            raise ValueError("Empty UUID binding")
    requests = []
    orders = {}
    unresolved = []
    for row in idx["sections"]:
        storage = json.loads((args.export_dir / row["storage_file"]).read_text(encoding="utf-8"))
        fmt = storage["format"]
        for mid in row.get("pending_audio_media_ids", []):
            media = next(m for m in storage["content"]["jlpt_block"]["mediaItems"] if m["id"] == mid)
            bound = audio_urls.get(mid)
            if not bound:
                unresolved.append(f"audio:{mid}")
            elif urlsplit(bound).scheme != "https" or not urlsplit(bound).hostname:
                raise ValueError(f"Invalid playback URL for {mid}")
            else:
                media["audio"]["url"] = bound
        key = row.get("group_key")
        if args.grouped and not key:
            raise ValueError(f"{row['id']}: missing grammar group")
        session_id = sessions.get(key) if key else None
        if args.grouped and not session_id:
            unresolved.append(f"session:{key}")
        template_id = templates.get(fmt)
        if not template_id:
            unresolved.append(f"template:{fmt}")
        order_key = key if args.grouped else "all"
        orders[order_key] = orders.get(order_key, 0) + 1
        body = {
            "exerciseTemplateId": template_id or f"<TEMPLATE_ID_{fmt}>",
            "content": json.dumps(storage["content"], ensure_ascii=False, separators=(",", ":")),
            "orderInSession": orders[order_key],
        }
        if session_id or args.grouped:
            body["sessionId"] = session_id or f"<SESSION_ID_{key}>"
        if storage.get("audioPath"):
            body["audioPath"] = storage["audioPath"]
        requests.append({
            "source_section_id": row["id"],
            "placement_after_grammar_refs": row.get("placement_after_grammar_refs", []),
            "method": "POST",
            "path": f"/api/learning/admin/{args.scope}-curriculum-units/{args.unit_id}/exercises",
            "body": body,
        })
    if args.unit_id == "<UNIT_ID>":
        unresolved.append("unitId")
    output = {"lesson": idx.get("lesson"), "ready_to_send": not unresolved, "unresolved": sorted(set(unresolved)), "requests": requests}
    path = args.out or args.export_dir / "api-requests.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"prepared {len(requests)} POST bodies; ready_to_send={output['ready_to_send']}; {path}")


if __name__ == "__main__":
    main()
