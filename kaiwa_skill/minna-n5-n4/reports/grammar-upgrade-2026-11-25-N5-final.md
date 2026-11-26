# N5 editorial upload batch — 2026-11-25

All 53 N5 entries deferred by the structure audit now have candidate Markdown in two separate batches:

- `authored/grammar-upload/2026-11-25-N5-editorial/N5/`: 43 files, packaged as `exports/grammar-upload/2026-11-25-N5-editorial-43.zip`.
- `authored/grammar-upload/2026-11-25-N5-final/N5/`: 10 files, packaged as `exports/grammar-upload/2026-11-25-N5-final-v2.zip`.

Both ZIPs passed `grammar_upload.py`, which validates existing UUID, level, filename, H1, meaning, structure, and H5/H6 shape. An additional audit found 53 distinct UUIDs, 938 H5/H6 pairs, five retained images, and no Vietnamese text, conjugation arrows, intonation arrows, or A/B labels inside H5. The 10-file final batch explicitly reconciles each source H5 as a retained Japanese sentence or a reclassified form, rule, variant, or note. JSON audits: `reports/grammar-upgrade-2026-11-25-N5-editorial.json` and `reports/grammar-upgrade-2026-11-25-N5-final.json`.

Editorial corrections include Japanese sentence typos, mistranslations, dialogue speaker placement, misleading statements about は／が, validity of `あなただけに`, and the distinction that だけ can appear with a negative predicate while しか requires one. Conjugation lists remain as rules instead of being mislabelled sentence examples. For the long sentence-ending-particle page, three previously untranslated telephone dialogue turns received Vietnamese translations; intonation marks moved below the translations. These candidates still require human content review before applying in Harumii; the long vĩ tố article in particular contains broad usage and gender statements retained from the source.

Earlier ZIPs named `2026-11-25-N5-editorial.zip` and `2026-11-25-N5-final.zip` are stale. Automatic approval review blocked deletion of the former, so use the `-43.zip` and `-v2.zip` files above, or package directly from the current authored folders.
