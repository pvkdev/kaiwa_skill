# Mini210 index: independent read-only review

Baseline index SHA256: `27c754b96cac8098d63176d946078f9539e46efa23c16acc239e75d9a4a0964c`
Current index SHA256: `dfc846635d901cb1b46c2a13a59e02a81b1fb86e08e1fde0fc7a40fc100a20d0`
Source PDF SHA256: `2fdf1586c2e2673f6b27b93fcf3c04c8584567fdd3c2258bcdd0033743de2b05`

Opened source PDF226–231. Source rows per page: 56/57/58/51/50/48 = 320. All 320 printed refs lead to a corresponding main head and existing unit anchor. After writer fixes, all 320 current rows match the reviewed source transcript; 0 open findings.

## Findings

- **idx226-a-big-dea**, PDF226: source `A big dea たいしたもんだ 132`; output `A big deal たいしたもんだ 132`. Retain printed key A big dea; a note may identify main PDF132 as A big deal.
- **idx226-not-at-all**, PDF226: source `(Not) ~at all ぜんぜん 109`; output `(Not) at all ぜんぜん 109`. Restore printed ~ placeholder in the key.
- **idx226-dont-you-agree**, PDF226: source `Both aliases print そうおもわなない？ 111`; output `Both aliases show そうおもわない？ 111`. Retain printed index spelling and note that main PDF111 has そう思わない？.
- **idx229-p-order**, PDF229: source `Pissed off → Pitiful → Please do it as soon as possible`; output `Please do it as soon as possible → Pissed off → Pitiful`. Restore printed order of the three rows, retaining their key/JP/ref.
- **idx231-tthats**, PDF231: source `Tthat's what I said だからいったのに 134`; output `That's what I said だからいったのに 134`. Retain printed Tthat’s typo; a note may identify main PDF134 as That’s what I said.

Full row-by-row source/output transcript, bitmap hashes, target positions, and scope limits are in the JSON report.
