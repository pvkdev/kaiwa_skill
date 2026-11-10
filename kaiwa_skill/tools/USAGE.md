# Resumable PDF ingest

Requires Python 3.10+, pypdfium2 and Pillow. Install with `python -m pip install -r kaiwa_skill/requirements.txt`. ReportLab is only used by tests. Source PDFs are read only. Commands below run from the repository root; add global `--root PATH` before the command to use a different skill directory.

```powershell
python kaiwa_skill/tools/ingest.py inventory
python kaiwa_skill/tools/ingest.py status-all
python kaiwa_skill/tools/ingest.py init --source "book/Kaiwa/example.pdf"
python kaiwa_skill/tools/ingest.py claim BOOK_ID --owner worker-name --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py render BOOK_ID --pages 1-3 --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py record BOOK_ID --page 1 --markdown draft.md --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py evidence-template BOOK_ID --page 1
python kaiwa_skill/tools/ingest.py verify BOOK_ID --page 1 --evidence review.json --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py needs_review BOOK_ID --page 2 --issue "Unreadable annotation; request closer crop" --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py reconcile BOOK_ID --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py build BOOK_ID --token UNIQUE_TOKEN
python kaiwa_skill/tools/ingest.py status BOOK_ID
python kaiwa_skill/tools/ingest.py release BOOK_ID --token UNIQUE_TOKEN
python -m unittest discover -s kaiwa_skill/tests -v
```

`BOOK_ID` is returned by `init` and inventory: sanitized ASCII filename plus the first 12 characters of the source SHA-256. A custom `init --id` is supported, but catalog/status-all use the default id. Do not use custom ids in the standard corpus workflow.

Claim each PDF before a worker starts, pass the token on mutations, and release at the end. Claims do not expire automatically. A command always uses an exclusive `.write.lock`; different books can progress independently. `status` is read only and may observe an in-progress write; repeat after the writer finishes if needed. `status-all` reads the catalog and current page states, including uninitialized books. Refresh inventory when sources are added.

Files live under `corpus/BOOK_ID/`: `manifest.json`, `pages/p0001.md`, `pages/p0001.json`, and `renders/p0001.png`. Paths in data are portable and relative. Each page checkpoint is authoritative; the manifest is a reconstructible summary. `reconcile` refreshes it after interruption and invalidates changed content. A missing/corrupt page checkpoint is never inferred to be verified. Re-render the affected page, record a fresh draft, and review it again. A changed source hash fails closed; restore the original PDF or initialize the changed PDF under its new id.

`record` inserts missing page and initial block anchors:

```html
<a id="p0001"></a>
<a id="p0001-b001"></a>
```

Add a new block anchor for each useful searchable unit, keeping dialogues together. `search.jsonl` contains one row per block, with the Markdown prefix preceding the first block in each row's `context` field so unit/title/printed-page context is preserved. Inline local Markdown/HTML links are checked relative to `pages/`; use paths such as `../assets/crop.png`. The combined book rebases them. Reference-style links are rejected. This is a basic link validator, not a complete Markdown parser; avoid nested parentheses in filenames.

`evidence-template` outputs JSON with `page`, `source_sha256`, `render_sha256`, `markdown_sha256`, `reviewer`, `reviewed_at`, `checks`, and `notes`. Save it using UTF-8. After actually viewing the rendered source and comparing the draft, fill the actual reviewer identity, timezone-bearing ISO timestamp and concrete notes. Set `visual_review`, `text_complete`, `reading_order`, and `japanese_accuracy` to true only when satisfied. The template defaults to false. Tooling checks the attestation and matching hashes; it cannot prove that a person or agent visually inspected a page. Never auto-fill review claims.

Local linked assets are also bound by an `asset_sha256` map (book-relative paths to SHA-256) in the page checkpoint, review evidence, and search rows, plus `page_asset_hashes` in the build marker. Changing or deleting an asset invalidates its page review and `build_current`, even if the Markdown is unchanged. Re-render to reset the draft checkpoint, record any corrections, and perform a fresh review using newly generated evidence. Older plain-text pages with no local assets remain valid with an omitted map interpreted as `{}`; older asset-bearing pages must be reviewed with hash-bound evidence.

`needs_review` persists issues and excludes the page from output. After resolving them, `record` a corrected draft and review again. `book.md` and `search.jsonl` include only verified, intact pages. Partial books say `INCOMPLETE`. Full page coverage says `TRANSCRIPTION_COMPLETE_REVIEW_REQUIRED`: `complete` / `transcription_complete` mean machine coverage only, and coordinator acceptance remains separate. `build.json` is the final publication marker with output and page hashes; `status.build_current` checks it. The two output files are individually atomic, not a multi-file transaction, so consumers must check that marker after a crash.

For stale claims/locks, the coordinator must first confirm the previous writer has stopped. Inspect the current token, then run:

```powershell
python kaiwa_skill/tools/ingest.py recover BOOK_ID --kind write --expected-token TOKEN --reason "Confirmed worker stopped" --confirm-writer-stopped
```

Use `--kind claim` for abandoned claims. A torn/invalid JSON lock can be recovered with `--expected-sha256 DIGEST` instead of a token, using the SHA-256 of the exact current file (`Get-FileHash -Algorithm SHA256`). Recovery checks the token/digest, archives an audit record (including raw bytes for digest recovery), and removes the lock. It does not detect process death for you; recovering an active writer is unsafe. Inventory is atomic but not a worker coordination mechanism; run it through the coordinator.
