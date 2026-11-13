# Worker contract — V5 roadmap, 2026-11-13

Root owns BUILD_MANIFEST, order, level, registry, merge, renderer, Git. Worker owns only its stage files and research/source ledger. Do not mutate V4.1 or knowledge/PDF/bunpou. User authorized comprehensive V5 now, not just another preview. No dialogues/lessons yet: detailed roadmap situations are the deliverable.

## Per-stage deliverable

Each assigned stage => `work/stages/<stage_key>.json`. `stage_key` is immutable build key (legacy S/T/H or V5P); display code comes from manifest, not worker. Read its scope_note and other related stage scopes to avoid duplicates. Every stage needs:

- objective: concrete speaking outcome appropriate to assigned level.
- knowledge_focus: useful knowledge/communication points to support future lessons, not full teaching text.
- events: multiple real event families; each has ID, name, roles.
- situations: substantive spoken tasks with event_id, branch, and optional continues_from local IDs. Title must explain the concrete scene/action, not just “bị từ chối” or generic noun lists.
- coverage_note: what breadth was considered and what belongs elsewhere; cross_stage_refs by immutable build keys.
- source_refs: external ledger IDs/known book evidence only when actually read. `lookup_books` in assignment is not verified attribution.

New situations are `ai_authored` by default even when informed by research. Never assign book support to all new scenarios merely because the stage has a source bank. Base/preview seeds stay in root metadata as traces, not claims the new text was copied from a book. External and AI-authored content are essential and explicitly allowed.

## Depth and diversity

Brainstorm each stage independently. Consider: distinct event families; social roles/relationships; initial request; granted/denied/conditional/pending outcomes where meaningful; what happens after; misunderstanding, constraints, repair, changed needs, handoff and follow-up. Do not force every outcome into every event. Do not produce the same matrix of generic cases for every topic.

Often 16–28 substantive situations makes sense; simple foundation may need fewer and big multi-event stages may need 30–40+. These are planning guides, not quotas. Quality and meaningful difference decide. Six preview seeds are not a limit. Save enough cases to cover the stage's actual scope.

For company party stages explicitly cover year-end, New Year, welcome, farewell, celebration/promotion/achievement and project completion. Respect role boundaries: attendee T-22, 幹事 V5P-118, MC H-46, company trip T-23. Not all seven become separate stages.

For permission/request stages include granted, denied, condition, waiting and later changes when natural, with linked continuation scenes. “Accepted” and “denied” are different scenes, but a whole stage cannot be one request relabeled 20 times.

Speak only. Documents may be objects discussed at a counter, never a writing/form/email exercise. No tests, learner scoring or access gates. Japanese app tools already exist. Safety/legal/medical: plan communication and requests to professionals; do not invent authoritative instructions. Basic help is available from Sơ. No demand to disclose actual trauma.

## Output helper (read-only for workers)

Import `stage_writer.py` from `kaiwa_skill/planning/v5/work` and call `write_stage(owner,key,objective,knowledge_focus,events,coverage_note,cross_stage_refs=[],source_refs=[],source_findings=[])`.

Each event is `{'name': '...', 'roles': ['người học ...','người đối diện ...'], 'cases': [ ... ]}`. Each case is a string (routine) or `{'title':'...', 'branch':'declined', 'from': 1}`. `from` is the 1-based earlier case index WITHIN THAT EVENT; helper resolves to local situation ID. It can also be a list of earlier case indices. Allowed branches: routine, accepted, declined, conditional, pending, alternative, misunderstanding, problem, resolved, unresolved, follow_up. Helpers generate IDs and atomic files; do not auto-generate the situation titles from templates.

Helper refuses overwriting a stage. To improve a finished file, read/edit it preserving existing IDs, then recheck. Save an owner progress JSON after meaningful batches (files completed, current stage, next action). Root can read complete files while you work; no shared-file writes. Keep working through all assigned stages, communicate real progress and call out scope/level concerns. Do not stop after research or 1 batch; finish assignment unless root reassigns.
