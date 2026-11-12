# Independent sample QA — H heads 155–162

- Source: PDF170–177, SHA-256 `2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05`.
- Output: `chapters/10-h-155-171.md`, SHA-256 at review `cfadd0954949013f927a03fc6f1c23666e4b095cbb7b671dd0ca04de96d5113f`.
- Recheck output SHA-256: `5ae1047055524dc784a7f4f9131c94ea2a42e243101b11bcf996ec44a32dca71`.
- Opened all eight source images and compared the complete head blocks 155–162. This review does not cover heads 163–171 or other chapters.

## Findings

1. **PDF172, head157, situation ④ Illegal parking omitted.** Source: A「自転車、持っていかれたの？」 B「お恥ずかしい話です。停めたらいけない場所だったんです。」 Output stops after situation 3 at line 35. Add both Japanese turns and their Vietnamese translations.
2. **PDF175, head160, situation ⑥ Promising to meet omitted.** Source: A「ごめん、やっぱり金曜日行けなくなった。」 B「えー、話が違うじゃない！金曜日なら大丈夫って言うから変えたのに。」 Output stops after situation 5 at line 70. Add both Japanese turns and their Vietnamese translations.
3. **PDF175, head160, situation ① dropped Japanese conjunction.** Source has 「月・水・金と土曜日でいいですか。」; output line 66 has 「月・水・金・土曜日でいいですか。」 Restore 「と」. Vietnamese meaning is adequate.

The remaining six heads (155, 156, 158, 159, 161, 162) had no findings in this scope. These are source-to-output discrepancies; no stylistic or source-normalization changes are proposed.

## Targeted recheck

All three findings are **resolved** in the chapter hash above. Situation ④ now appears at line 36, situation ⑥ at line 72, and the source conjunction 「と」 at line 67. Both added situations retain the printed Japanese turns and direct Vietnamese translations. The recheck covered these three locations only.
