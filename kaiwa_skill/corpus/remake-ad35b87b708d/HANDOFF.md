# HANDOFF — remake-ad35b87b708d

- Source: `book/BJT/ロールプレイで学ぶ ビジネス日本語 - 中級レベル ―就活から入社まで― [Remake].pdf` (140 physical pages).
- Source SHA-256: `ad35b87b708de387488152e8fd1aca16e63e37d28502d7901ef8e8d7d0891089`.
- Latest worker: `production_book_12_root_cont2` (`gpt-6-sol/high`); claim released at handoff.
- Status at handoff: **88 verified, 52 pending, 0 rendered, 0 draft, 0 needs_review, 0 invalid**; `build_current=true`, `complete=false`, coordinator acceptance pending.
- Verified physical pages: **p0001–p0088**. Resume at **p0089** after status/reconcile and a new unique claim.
- Text-only outputs: `book.md`, `search.jsonl`, `build.json`; authoritative checkpoints are `pages/pXXXX.md` and `pages/pXXXX.json`.
- Latest build (2026-11-11T02:45:39.015832+00:00): `book_sha256=5541187c6d86d489c3eb9e769579bbdd8718e777289b21d93402739f7abb8f97`; `search_sha256=f814bdc374365a6d17d24cc434ba833adac04d18a9f27993d0d0e0c0d3d8e0c0`.

## Review and source fidelity

Every completed PDF page was visually opened (full page and enlarged crops where needed) and compared against its Markdown in both directions. Source pages are image scans and have no usable selectable text. Reviews include all visible languages; ruby spans and occurrences; bold, underline, blanks, and glossary stars; tables, role cards, diagrams, icons and footers; printed page numbers and watermark overlays independently. Inferred continuation headings or speaker labels are explicitly marked `(biên tập)`. No open readability issue is recorded.

Root separately QA sampled p10, p16, p20, p28, p32, p50, p60, and p68; no source-word correction was required. The p28 inferred-heading label was corrected and reverified. Source p16 prints `Dongseo` in Vietnamese while p10 prints `Tozai` in English; both are preserved.

Root also opened the full source and Markdown for prefix pages p17, p26, p27, p28, p30, p31, p33, p34, p35, p36, p38, and p40, confirming their single ASCII `*` marks are literal glossary footnotes. These 12 pages and 20 more p41–75 pages received a markup-only escape (`\*`) and were reverified with exact plain-text equality after removing the backslash and unchanged source/render hashes. A complete p1–88 Markdown audit found no unescaped single `*`; genuine `**` emphasis remains. p76–88 already used escaped glossary markers on first verification.

The source PDF and `bunpou_skill/` remained read only. No Git operation was performed.

## Verified page Markdown SHA-256

| Physical page | SHA-256 |
| --- | --- |
| p0001 | `0a14ccedd03496505bd5020b22e43394425cc244d89725fce8f566e57f24b667` |
| p0002 | `c0412c916e022e48ed93ee95df00ebf00c0577710c140045e1643cc4f3d50d3b` |
| p0003 | `b56153da52d5e2e5fbf06aac6550368f1fccd176221eaf9e988c42353b4bda21` |
| p0004 | `4c88530df6ec3d814b8575032e483704c8088fa1cb0637f330c2f98cfeb46eb0` |
| p0005 | `6f9955850e88428570f1d226b46483e318f01e971dd2af2e3820ccb88abd928a` |
| p0006 | `8c717d3697c595c64cafee159f614bc5ed45adbe9858f6b44332520458b71c6c` |
| p0007 | `741e102f81e14ea0295360d67184c37fa5399e7be231a8a6b67a713be64886ce` |
| p0008 | `92378997097a50f7517fb10e6c8d7e8c7e8493b9cd21d04ac422acd5d086b524` |
| p0009 | `81b9e62dfae96baf737fe42d0a4f8fc50fe4431be8aa7f0a19fbbc58bbbdd12c` |
| p0010 | `50a90abfd80b8be4f28bff19f99b0c14cb6b1aa4cfee8f759d8ed53610ffa62c` |
| p0011 | `49d5047d73953482e31e9ee6fc1ccbbf5024d1053bbdd282dac8f23bc667867d` |
| p0012 | `79c8aa42914f50f0ad0ecdd49429e9f4ab4bf2bfc3937573112302c0e0a39071` |
| p0013 | `155b048b213f1a1fc8808314b5f1e93ee11e9c7f994d7c7d78e99e6a11219d67` |
| p0014 | `48453d4b9ad987614582225f655ce5e06ead1b99ce67c364bfe51ab8f6318659` |
| p0015 | `8ee8a2fa86815c2da56a2957134b82e0011374fb4c29d47e8a57c6455bec0c07` |
| p0016 | `ea40067968756dde1385734a622265c7e4661f7eca445a667d059b1d93e6df89` |
| p0017 | `c2215518d3473c9e84c94fed1bf394ad1fab53d79ab139dfefc5bb49cacd70d4` |
| p0018 | `aa9dfde52e4d47952e9ee0412f7c690dfac25412d1173b7f647b3a0ddd7f7e7e` |
| p0019 | `6f49136735867c52e06f365781198af4311b56459eddca0fbf67ecbd20e92436` |
| p0020 | `216003e83b8a8dc402ed7c80feb62493aa052385c90e0bdf55a2800f40768312` |
| p0021 | `b3343d7b2851009854ff59c2285dbe08125e663f426e0d2df76eb583a51925c8` |
| p0022 | `a77efc06fc23866cf009f905dd78ffe5e04e26f69b6f6fd092aaabbcdd1e1054` |
| p0023 | `32a37afcbb6143b77a73981971005f05708535a388a1520c0c9215a794753685` |
| p0024 | `7ac7675e1cda312e5946484e3e70fc59634d9a9fa7eab809f4ed318a3e4e237e` |
| p0025 | `bc0fa5e3411365c744fa80099916af8bb08d03fc4075af495c644af62a8b3974` |
| p0026 | `f311094517d94d19258373ac9caa286adedf25091a0eec551bfc35daf21c2af2` |
| p0027 | `cadfa75d1ffd37f50244f96d22879654f343acddc2715165e6d49671cea6ac30` |
| p0028 | `c2291af19550666e3e7ed16e20cecd47cba729a1487d216fc9f470caf5342674` |
| p0029 | `83848edec024c5e956e147eb29b53cc3496e018904d52aeb0fa2bde8302418a2` |
| p0030 | `01351937091eda589d881e718c3ba445e6dcc6353aef9dfdba15204e3a2629eb` |
| p0031 | `d3bd9f49e46f5c3218050c78cd4ba576c92f34986650ceeffcd6a3ea508d2be3` |
| p0032 | `ae009776c5e0f853ebdd9002dc929ddcdb33e2611f55a550f221a67525911c00` |
| p0033 | `c39662240f4edd781eab6a061d8b0478771546ce8667def92238dfa36d980238` |
| p0034 | `1c9a5660fd7eb4bbae1e94e69e26f7d14b48c3a90a9d48664f61764cefd5ab78` |
| p0035 | `decd843b1711ccf517cde6b1d76b3897d7af5595afaf4de8e0996995ff3fbd33` |
| p0036 | `15f3b7898d524b7affb1e2e2c146304fc1e8c11eaa462a603dd3cafcc65dd53d` |
| p0037 | `089a769e0d86cc76c1a2aacf6ef93093eaf0980c80a0a31e85ce20554d68070d` |
| p0038 | `5b68f329f4bc306310b7b6da87b4406ddcaff3af6922ddc70fd67b5ba44f415b` |
| p0039 | `b013e521c4e89e9fbbadfc532381a3e63af192f54412be7cfcd22d0d183b35fc` |
| p0040 | `1685f87db5a9ab3f614388450e01ca24a7ee2776e8b057e72996af03d7fd49c7` |
| p0041 | `cf0772b3039820ad1ddb2864544b8005199bc9ca400947c91347d937b9105c92` |
| p0042 | `90b1829a1b920026f431a3fe8b314e868f8610e61c7d80874df005789b34d475` |
| p0043 | `73ce45fdf590fe48e5c61dd02107d870dc404387ad4f62550f074d5ed2c02f6b` |
| p0044 | `72aa41fd23812d7b4675c1fb63404b1156ae42be2b733217ce499c02f2536b56` |
| p0045 | `b1e8aa02d32cfd2b5d590044e267f8031733b7c25c53a616d5557763659244cb` |
| p0046 | `c168faf736a2cc4b47d59edf485f4f134da455940cc6ec4b839c874fc2642e1d` |
| p0047 | `3f64412ecabacc28e8932e20d6914e21d86ddb450240301e515e0f108d707c72` |
| p0048 | `1850440b9e93f3b4e24a76098c3d50862c0672aef721b878247b510eed65a1d1` |
| p0049 | `32a4d31d3b8bb00477fd5cce843412054bc38e52689e644cdca00dc7b601d2ee` |
| p0050 | `ae4e3d5368b7630ed6b235517b7fc0c2d2a02be78e3b655dee32fe553d48ee73` |
| p0051 | `bf476f6f09396fffb32e987f4f0142a508b4a23de577312792d4551b800ec98b` |
| p0052 | `afed9f8d2ed90e344b31a8d6c361a8330167ba8f70bae9377972bbe807d128f8` |
| p0053 | `6e0181d3877e9aded501c22fc071f2b0ba5de7e1900930a80ccfd4de5f7fe985` |
| p0054 | `8ca11073bcfaa363f83d88251cc4599380ff391bebfdfa1b77f2da6da09dd7ba` |
| p0055 | `6e49937c1e83f016647b04aa17cf971de9ff4e8df17078067d385c6c57732447` |
| p0056 | `a2c30372b28629ab85d7f23da436f8a48d2815455ec9415c39522ecd22b4a55d` |
| p0057 | `a9a8a67d05fcd2db35eac5549112b47f4f15cd9ac40434403cabcbfb42f33465` |
| p0058 | `77181622b092e8d237cd3338d4901b6ec5d5da348b2667bfcd92195a130bb8f6` |
| p0059 | `07630f5b9cea2ba7fd5c8763ff5145ce0cdc8a481f5bb5cfe2789339892e9659` |
| p0060 | `2eab021a93128a2d30d9a626fc4e82a29c056e98cac58db0c32b9d7342f9b760` |
| p0061 | `1b7d509b7d229ec6c2ef3e71b5dac437cb2a5139e0b515e2d52316237f4ece6e` |
| p0062 | `1c45f1dbf1583f85d18c12bfb9b08ee5c75936086aa0cc15ded64c40f3b15d6e` |
| p0063 | `376a6600bd20445360b0486c4f17ac5ed3540a011344e2668f733d252f9899bf` |
| p0064 | `73c24752464eb7656860198dfbeeab972b1f8b3834abb2ec87420cd235a7ab64` |
| p0065 | `51114986b905e8399a27c99d4a55a4e55bca5f48a872862e9036a90a62ae3e32` |
| p0066 | `3dc6230311187295982cbac6044806efc54cf7b5a8027c6d16eee5adc870411b` |
| p0067 | `38503740940471aaa7456be45cbd1a8c0c6da20b7e57f6dda92c43725f24fda8` |
| p0068 | `3e3b0a04e5f20125aa8fd67f27960387ff04e8b65d668fc49b2f2f37ce7701ae` |
| p0069 | `e2d8f4fc01e315bee89882d4265c56e140614ed8f138db76d50113bf31417435` |
| p0070 | `3c3c084dd10632b0a20749f903792e20eefa27108fe0242a4a547f48c3922b5b` |
| p0071 | `b4193e822a579af4a2c4117b09e26920e71363d532aaad6f3d3f4d8a025b8eaf` |
| p0072 | `85442590f7e6636814f3a873be81dc76b279ead3cde83bd03d34e0d4a9758e9a` |
| p0073 | `c846cff113e3d7a51cedefdf49397cd3bde5c4800f9c640aa1bdd212a724d725` |
| p0074 | `09de10d567be246a057a244904572ca86c753e1923507c5dc1fdac0740cbc023` |
| p0075 | `ea65234d05cb191a8fb2975e87680f57f6e1c9f19e7ca82ad0b6879253352ee8` |
| p0076 | `6c5c96093dcba8134e6767fc63c967204f3e2a9d3df9d11fe3fb328c7a57f08b` |
| p0077 | `172238a6db857d573a9bbc3bffb68e6f188f5b193781b31580c6a48cff75a140` |
| p0078 | `439d7c388119f423118ecd31da6c083b4a56e010eb10307178192fe989fa27df` |
| p0079 | `46772d8f3037afebfa4cdb5233411c3dfcf2560f9fbca2896bdd0205627121a4` |
| p0080 | `70114b62ed1006e9c9c691e6d950dcb651c64dd36bb825e6a13addacd516257d` |
| p0081 | `175a929e2514fa5ae509e444516268eece96e685eab4cd6924388cf3c466a255` |
| p0082 | `4179ce3b6145ecc2dd49de908a31a2da15e0b227d0c16d54bc9fd83ad7b488e8` |
| p0083 | `b63f8d9b1db9ac9559c789edb5473bc7bf7a905df74bb79147d7cb8e148f78b9` |
| p0084 | `329e131e1f0d7bd8bad7d4b2b76dced56c87f546984fa7389e64693c2b49c226` |
| p0085 | `a90ea13a6f28127ff7dcd455d804428adce55113efa4cacae15b3ee39b00cd26` |
| p0086 | `12483523bb001128aceb3316cc283189a78b44cadcb8d26cc8bf8444aef966ad` |
| p0087 | `31ac54752c1cfdc145f99ef015c5157c6f6bd0adf482a68b9366275c4cc36c5f` |
| p0088 | `90130aafd8f2af241da42ab03f7150f045baf7645b22a7cdb42e0515008e8f1f` |
