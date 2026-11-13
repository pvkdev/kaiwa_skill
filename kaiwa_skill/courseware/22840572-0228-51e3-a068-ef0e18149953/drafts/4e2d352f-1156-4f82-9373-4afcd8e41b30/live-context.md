# Nhờ việc khó, từ chối và thương lượng giới hạn

{
  "schema_version": "3.2-draft",
  "stage_uid": "22840572-0228-51e3-a068-ef0e18149953",
  "display_code": "H-050",
  "title": "Nhờ việc khó, từ chối và thương lượng giới hạn",
  "level": "Thượng",
  "scope": "Xử lý lời nhờ khó trong quan hệ bạn bè, người quen và cộng tác: hỏi rõ trách nhiệm, nói lời từ chối, thương lượng phần có thể giúp, báo thay đổi sau khi nhận, bàn giao và giữ quan hệ. Luyện nghe và nói qua các diễn biến có hậu quả.",
  "events": [
    {
      "id": "e01",
      "title": "Lời nhờ còn mơ hồ",
      "situation_ids": [
        "s01",
        "s02",
        "s03"
      ]
    },
    {
      "id": "e02",
      "title": "Cân nhắc nhận, từ chối hoặc giới thiệu người khác",
      "situation_ids": [
        "s04",
        "s05",
        "s06",
        "s07"
      ]
    },
    {
      "id": "e03",
      "title": "Khi người nhờ thúc ép hoặc hiểu nhầm",
      "situation_ids": [
        "s08",
        "s09",
        "s10",
        "s11"
      ]
    },
    {
      "id": "e04",
      "title": "Việc đổi sau khi đã nhận",
      "situation_ids": [
        "s12",
        "s13",
        "s14",
        "s15"
      ]
    },
    {
      "id": "e05",
      "title": "Bàn giao khi phải dừng",
      "situation_ids": [
        "s16",
        "s17",
        "s18"
      ]
    },
    {
      "id": "e06",
      "title": "Gặp lại sau lời từ chối",
      "situation_ids": [
        "s19",
        "s20"
      ]
    }
  ],
  "retired_ids": [],
  "source_refs": [],
  "curriculum": {
    "version": "5.0",
    "registry": "kaiwa_skill/planning/v5/chang_registry.json",
    "roadmap": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5.jsonl",
    "policy": "kaiwa_skill/planning/v5/KAIWA_CHANG_V5_META.json"
  },
  "harumii_export": "harumii-stage.json",
  "authoring_mode": "canonical"
}


## Từ để hỏi rõ việc và hạn [v_scope]

{
  "id": "v_scope",
  "source_refs": [],
  "items": [
    {
      "id": "v_scope-w-0d603e6d0a7e",
      "ja": "範囲",
      "source_refs": []
    },
    {
      "id": "v_scope-w-e4e63c53a66d",
      "ja": "締め切り",
      "source_refs": []
    },
    {
      "id": "v_scope-w-1d6ce8ec2c34",
      "ja": "見積もる",
      "source_refs": []
    },
    {
      "id": "v_scope-w-c2d344b1bdc3",
      "ja": "確認する",
      "source_refs": []
    },
    {
      "id": "v_scope-w-f43e344a8341",
      "ja": "担当",
      "source_refs": []
    },
    {
      "id": "v_scope-w-0494a572721c",
      "ja": "判断する",
      "source_refs": []
    },
    {
      "id": "v_scope-w-a1b71818fed2",
      "ja": "引き受ける",
      "source_refs": []
    }
  ]
}



## Mẫu hỏi rõ và để ngỏ câu trả lời [g_scope]

{
  "id": "g_scope",
  "source_refs": [],
  "items": [
    {
      "id": "g_scope-g-15064748f421",
      "name_ja": "〜かどうか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_scope-g-d0bf74383824",
      "name_ja": "〜までに",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_scope-g-9707e09abe4c",
      "name_ja": "Vてもらいます／Vてもらえますか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_scope-g-14be8d0d6400",
      "name_ja": "Vてほしい",
      "jlpt_level": "N4",
      "reference": {
        "kind": "bunpou"
      }
    }
  ]
}



## Hỏi rõ trước khi nhận việc [k_scope]

# Hỏi rõ trước khi nhận việc

Một lời nhờ như “xem giúp một chút” có thể chỉ là góp ý, cũng có thể bị hiểu thành nhận trách nhiệm toàn bộ. Hỏi kết quả cần có, hạn và phần ai quyết định. Sau đó nói rõ bạn đang kiểm khả năng, chưa nhận lời. 「確認してからお返事します」 hẹn một câu trả lời, không hứa sẽ làm việc ấy. Nếu cần người có chuyên môn hoặc quyền quyết, hỏi ai là người phụ trách thay vì tự phán đoán. Với người quen, có thể nói mềm hơn; ranh giới vẫn phải rõ.

<a id="k_scope_ex01"></a>
どこまで私が担当する想定ですか。

Anh/chị đang tính để tôi phụ trách đến phần nào?

<a id="k_scope_ex02"></a>
内容を確認してから、今日中にお返事します。

Để tôi xem rõ nội dung rồi trả lời trong hôm nay.

<a id="k_scope_ex03"></a>
最終的な判断は、どなたがなさいますか。

Ai sẽ là người quyết định cuối cùng ạ?


## Khi lời từ chối để ngỏ chưa đủ [k_indirect]

# Khi lời từ chối để ngỏ chưa đủ

「ちょっと…」 thường báo rằng việc đó khó nhận, nhưng người nghe có thể hiểu là chỉ vướng thời điểm. Trong ba cuộc nói dưới đây, một lời mời được khép lại ngay; một người nhờ tiếp tục gây sức ép; còn lời phàn nàn quá vòng vo khiến người nghe phải hỏi thẳng. Hãy nghe trọn lượt đáp rồi để ý khi nào cần chuyển từ tín hiệu mềm sang giới hạn cụ thể. Với việc khó, nói “phần này tôi không thể nhận” giúp tránh cam kết nhầm. Lời giải thích nên đủ rõ, không cần kể chuyện riêng tư dài.

<a id="k_indirect_ex01"></a>
その件は引き受けられません。別の方法を考えましょう。

Việc ấy tôi không thể nhận. Ta cùng nghĩ cách khác nhé.

<a id="k_indirect_ex02"></a>
先ほどの話は提案で、私が担当するという意味ではありません。

Điều tôi vừa nói là một gợi ý, không có nghĩa tôi sẽ phụ trách.


## Nghe lời từ chối, sức ép và lời nói rõ [sh_indirect]

{
  "id": "sh_indirect",
  "source_refs": [
    "srcB09"
  ],
  "knowledge_ids": [
    "k_indirect"
  ],
  "items": [
    {
      "id": "d01",
      "kind": "dialogue",
      "example_id": "b09_21_01",
      "speakers": [
        {
          "id": "A",
          "role": "Người mời"
        },
        {
          "id": "B",
          "role": "Người được mời"
        }
      ],
      "turns": [
        {
          "id": "sh_indirect--d01--t01",
          "speaker": "A",
          "ja": "今週の土曜日あたり、ゴルフなんかいかがですか。",
          "vi": "Khoảng thứ Bảy tuần này, anh chơi golf nhé?"
        },
        {
          "id": "sh_indirect--d01--t02",
          "speaker": "B",
          "ja": "土曜日ですか。土曜日はちょっと…。",
          "vi": "Thứ Bảy à? Hôm ấy tôi hơi khó…"
        },
        {
          "id": "sh_indirect--d01--t03",
          "speaker": "A",
          "ja": "そうですか。じゃまた別の機会にでも…。",
          "vi": "Vậy à. Thế để dịp khác nhé…"
        }
      ],
      "authorship": "source_quote"
    },
    {
      "id": "d02",
      "kind": "dialogue",
      "example_id": "b09_21_04",
      "speakers": [
        {
          "id": "A",
          "role": "Người nhờ"
        },
        {
          "id": "B",
          "role": "Người được nhờ"
        }
      ],
      "turns": [
        {
          "id": "sh_indirect--d02--t01",
          "speaker": "A",
          "ja": "明日、練習が終わってから、部室の大掃除をやってくれないか。",
          "vi": "Ngày mai sau buổi tập, em dọn tổng vệ sinh phòng câu lạc bộ được không?"
        },
        {
          "id": "sh_indirect--d02--t02",
          "speaker": "B",
          "ja": "明日は試験前なので、ちょっと…。",
          "vi": "Ngày mai sát ngày thi nên em hơi khó…"
        },
        {
          "id": "sh_indirect--d02--t03",
          "speaker": "A",
          "ja": "そんなこと言ってたらちっともきれいにならないじゃないか。",
          "vi": "Nếu cứ nói thế thì phòng chẳng bao giờ sạch được."
        },
        {
          "id": "sh_indirect--d02--t04",
          "speaker": "B",
          "ja": "でも、練習の後は疲れますし…。",
          "vi": "Nhưng sau buổi tập em cũng mệt nữa…"
        }
      ],
      "authorship": "source_quote"
    },
    {
      "id": "d03",
      "kind": "dialogue",
      "example_id": "b09_21_08",
      "speakers": [
        {
          "id": "A",
          "role": "Người góp ý"
        },
        {
          "id": "B",
          "role": "Người hàng xóm"
        }
      ],
      "turns": [
        {
          "id": "sh_indirect--d03--t01",
          "speaker": "A",
          "ja": "あのう、ちょっと…。",
          "vi": "À, cho tôi nói một chút…"
        },
        {
          "id": "sh_indirect--d03--t02",
          "speaker": "B",
          "ja": "はい、何でしょうか。",
          "vi": "Vâng, có chuyện gì vậy?"
        },
        {
          "id": "sh_indirect--d03--t03",
          "speaker": "A",
          "ja": "お宅の犬が少し…。",
          "vi": "Con chó nhà anh/chị hơi…"
        },
        {
          "id": "sh_indirect--d03--t04",
          "speaker": "B",
          "ja": "うちの犬が何か？",
          "vi": "Chó nhà tôi làm sao?"
        },
        {
          "id": "sh_indirect--d03--t05",
          "speaker": "A",
          "ja": "夜になりますとあたりが静かになりますので、犬の声がどうも…。",
          "vi": "Đêm xuống xung quanh yên tĩnh, nên tiếng chó thì thật hơi…"
        },
        {
          "id": "sh_indirect--d03--t06",
          "speaker": "B",
          "ja": "うるさいとおっしゃるんですか。",
          "vi": "Ý chị là nó ồn à?"
        },
        {
          "id": "sh_indirect--d03--t07",
          "speaker": "A",
          "ja": "ええ、そういうわけですから…。",
          "vi": "Vâng, chính vì thế nên…"
        }
      ],
      "authorship": "source_quote"
    }
  ]
}



## Hỏi kết quả thật cần [s01]

{
  "id": "s01",
  "source_refs": [],
  "title": "Hỏi kết quả thật cần",
  "event_id": "e01",
  "setting": "Một đồng nghiệp quen nhờ bạn “xem giúp” phần chuẩn bị buổi sinh hoạt cộng đồng, nhưng chưa nói rõ muốn bạn làm gì.",
  "communication_goal": "Phân biệt góp ý với nhận tổ chức.",
  "relationship": "Đồng nghiệp quen, nói thân mật với nhau.",
  "outcome": "scope_clarified",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s01--t01",
      "speaker": "B",
      "ja": "今度の交流会の準備、ちょっと見てもらえない？",
      "vi": "Buổi giao lưu sắp tới, cậu xem giúp phần chuẩn bị được không?"
    },
    {
      "id": "s01--t02",
      "speaker": "A",
      "ja": "もちろん話は聞けるよ。「見る」って、何をしてほしいの？",
      "vi": "Tớ nghe chuyện thì được. “Xem” là cậu muốn tớ làm gì?"
    },
    {
      "id": "s01--t03",
      "speaker": "B",
      "ja": "会場と参加人数を見て、当日の流れを決めてほしいんだ。",
      "vi": "Tớ muốn cậu xem địa điểm, số người tham gia rồi quyết định chương trình hôm ấy."
    },
    {
      "id": "s01--t04",
      "speaker": "A",
      "ja": "それなら運営を任せる話だね。助言だけだと思っていたから、まず範囲を確認させて。",
      "vi": "Vậy là giao tớ điều hành rồi. Tớ tưởng chỉ góp ý; cho tớ xác nhận phạm vi trước nhé."
    },
    {
      "id": "s01--t05",
      "speaker": "B",
      "ja": "そうだね。お願いしたいことを整理してから、もう一度話すよ。",
      "vi": "Ừ. Để tớ sắp lại những việc muốn nhờ rồi nói tiếp."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi hạn và người quyết [s02]

{
  "id": "s02",
  "source_refs": [],
  "title": "Hỏi hạn và người quyết",
  "event_id": "e01",
  "setting": "Một người quen muốn bạn giúp liên hệ các nhóm cho buổi giao lưu. Bạn cần biết hạn và ai phê duyệt thay đổi.",
  "communication_goal": "Làm rõ trách nhiệm trước khi đáp.",
  "relationship": "Người quen cùng nhóm tình nguyện.",
  "outcome": "decision_owner_named",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s02--t01",
      "speaker": "B",
      "ja": "参加する団体への連絡をお願いできる？",
      "vi": "Cậu liên hệ với các nhóm tham gia giúp được không?"
    },
    {
      "id": "s02--t02",
      "speaker": "A",
      "ja": "いつまでに、何団体へ連絡する予定？内容を変える必要が出たら、誰が判断する？",
      "vi": "Hạn khi nào, liên hệ bao nhiêu nhóm? Nếu cần đổi nội dung, ai quyết định?"
    },
    {
      "id": "s02--t03",
      "speaker": "B",
      "ja": "金曜までに三団体。内容の変更は私が決めるよ。",
      "vi": "Đến thứ Sáu, ba nhóm. Việc đổi nội dung tớ sẽ quyết."
    },
    {
      "id": "s02--t04",
      "speaker": "A",
      "ja": "わかった。連絡だけなら時間を見積もれる。返事は今夜でもいい？",
      "vi": "Hiểu rồi. Nếu chỉ liên hệ thì tớ ước lượng được thời gian. Tối nay tớ trả lời nhé?"
    },
    {
      "id": "s02--t05",
      "speaker": "B",
      "ja": "うん、待ってる。まだ引き受けたわけじゃないんだよね。",
      "vi": "Ừ, tớ đợi. Cậu vẫn chưa nhận lời đúng không?"
    },
    {
      "id": "s02--t06",
      "speaker": "A",
      "ja": "そう。確認してから返事をするね。",
      "vi": "Đúng. Tớ sẽ xem lại rồi trả lời."
    }
  ],
  "authorship": "original_extension"
}



## Chờ thông tin rồi mới trả lời [s03]

{
  "id": "s03",
  "source_refs": [],
  "title": "Chờ thông tin rồi mới trả lời",
  "event_id": "e01",
  "setting": "Người quen muốn bạn chăm sóc gian hàng cả ngày nhưng chưa có lịch chia ca.",
  "communication_goal": "Đặt mốc hỏi lại mà không nhận lời trước.",
  "relationship": "Hai thành viên cùng nhóm.",
  "outcome": "pending_details",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s03--t01",
      "speaker": "B",
      "ja": "土曜日、受付を一日お願いしてもいい？",
      "vi": "Thứ Bảy cậu phụ trách quầy tiếp đón cả ngày được không?"
    },
    {
      "id": "s03--t02",
      "speaker": "A",
      "ja": "交代する人と休憩の時間は決まってる？",
      "vi": "Đã có người đổi ca và giờ nghỉ chưa?"
    },
    {
      "id": "s03--t03",
      "speaker": "B",
      "ja": "まだ。月曜までに決めるつもり。",
      "vi": "Chưa. Tớ định chốt trước thứ Hai."
    },
    {
      "id": "s03--t04",
      "speaker": "A",
      "ja": "その情報がないと一日引き受けられるか判断できない。決まったら教えて。水曜に返事をするよ。",
      "vi": "Chưa có thông tin đó thì tớ không biết có nhận cả ngày được không. Khi chốt thì báo tớ nhé. Thứ Tư tớ trả lời."
    },
    {
      "id": "s03--t05",
      "speaker": "B",
      "ja": "わかった。今は保留ということだね。",
      "vi": "Hiểu rồi. Hiện tại là đang để ngỏ đúng không?"
    },
    {
      "id": "s03--t06",
      "speaker": "A",
      "ja": "うん、まだ約束はしていないよ。",
      "vi": "Ừ, tớ chưa hứa nhận."
    }
  ],
  "authorship": "original_extension"
}



## Từ nói ranh giới và phương án khác [v_boundary]

{
  "id": "v_boundary",
  "source_refs": [],
  "items": [
    {
      "id": "v_boundary-w-edfd15ad8ea7",
      "ja": "難しい",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-0d603e6d0a7e",
      "ja": "範囲",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-eb3626663bcc",
      "ja": "相談する",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-b145fe4af8af",
      "ja": "提案する",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-14896683954a",
      "ja": "責任",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-8149a2153a58",
      "ja": "無理",
      "source_refs": []
    }
  ]
}



## Mẫu nói điều kiện và giới hạn [g_boundary]

{
  "id": "g_boundary",
  "source_refs": [],
  "items": [
    {
      "id": "g_boundary-g-5897ef3ec140",
      "name_ja": "〜なら（条件）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_boundary-g-f1cb680ec7ef",
      "name_ja": "〜ても／〜でも",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_boundary-g-1cd8275e1692",
      "name_ja": "〜わけではない",
      "jlpt_level": "N3",
      "reference": {
        "kind": "bunpou"
      }
    },
    {
      "id": "g_boundary-g-217be0136ae1",
      "name_ja": "〜んです／んですが",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_boundary-g-c68aaf5daf3c",
      "name_ja": "V辞書形／Vている／Vた＋ところです",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Từ chối mà không mở lời hứa mới [k_boundary]

# Từ chối mà không mở lời hứa mới

Đầu tiên ghi nhận nhu cầu của người kia. Tiếp theo nói phần không thể nhận bằng một câu dứt khoát, rồi chỉ đề nghị điều thật sự làm được. Nếu họ giảm phạm vi nhưng phần cốt lõi vẫn là trách nhiệm bạn không thể mang, có quyền giữ lời từ chối. Tránh dùng 「また今度」 nếu bạn không muốn tạo kỳ vọng lần sau. Trong quan hệ công việc, lý do có thể là trách nhiệm đang có hoặc thiếu quyền quyết, không cần bịa lịch bận. Với bạn thân, giữ giọng gần gũi nhưng không biến lời “thử xem” thành đồng ý.

<a id="k_boundary_ex01"></a>
気持ちは分かるけれど、全体の責任は引き受けられない。

Tớ hiểu cậu cần giúp, nhưng tớ không thể nhận trách nhiệm toàn bộ.

<a id="k_boundary_ex02"></a>
この部分なら手伝える。ただし、最終確認はお願いしたい。

Phần này thì tớ giúp được. Nhưng khâu xác nhận cuối nhờ cậu làm.

<a id="k_boundary_ex03"></a>
回数を減らしても、今回は引き受けられません。

Dù giảm số lần, lần này tôi vẫn không thể nhận.


## Nhận phần nhỏ, chốt ranh giới [s04]

{
  "id": "s04",
  "source_refs": [],
  "title": "Nhận phần nhỏ, chốt ranh giới",
  "event_id": "e02",
  "setting": "Một người quen cần người chuẩn bị buổi họp cộng đồng. Bạn chỉ có thể xem sơ đồ chỗ ngồi, không điều phối cả buổi.",
  "communication_goal": "Thương lượng phần làm được và người quyết.",
  "relationship": "Hai thành viên cùng nhóm.",
  "outcome": "partial_acceptance",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s04--t01",
      "speaker": "B",
      "ja": "当日の進行も含めて、準備を全部お願いできないかな。",
      "vi": "Cậu có thể lo hết phần chuẩn bị, kể cả điều phối trong ngày không?"
    },
    {
      "id": "s04--t02",
      "speaker": "A",
      "ja": "全部は難しいけど、座席の配置案なら木曜までに見られるよ。",
      "vi": "Toàn bộ thì khó, nhưng bản bố trí chỗ ngồi tớ xem được trước thứ Năm."
    },
    {
      "id": "s04--t03",
      "speaker": "B",
      "ja": "進行はやっぱり無理？",
      "vi": "Phần điều phối vẫn không được à?"
    },
    {
      "id": "s04--t04",
      "speaker": "A",
      "ja": "うん、その日は参加できない。進行は別の人に頼んでほしい。",
      "vi": "Ừ, hôm ấy tớ không tham gia được. Phần điều phối cậu nhờ người khác nhé."
    },
    {
      "id": "s04--t05",
      "speaker": "B",
      "ja": "じゃ、配置案だけお願いするね。",
      "vi": "Vậy nhờ cậu xem riêng bản bố trí."
    },
    {
      "id": "s04--t06",
      "speaker": "A",
      "ja": "了解。変更を決めるのはそちらでお願い。",
      "vi": "Được. Việc quyết thay đổi nhờ bên cậu nhé."
    }
  ],
  "authorship": "original_extension"
}



## Nhận việc đã rõ và hẹn cập nhật [s05]

{
  "id": "s05",
  "source_refs": [],
  "title": "Nhận việc đã rõ và hẹn cập nhật",
  "event_id": "e02",
  "setting": "Người quen nhờ bạn gọi xác nhận giờ đến của hai nhóm tham gia, không cần bạn hứa giải quyết mọi thay đổi.",
  "communication_goal": "Nhận phạm vi rõ và mốc báo lại.",
  "relationship": "Thành viên cùng ban tổ chức.",
  "outcome": "accepted_with_update",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s05--t01",
      "speaker": "B",
      "ja": "二つの団体に到着時間を確認してもらえる？変更があれば私が調整する。",
      "vi": "Cậu xác nhận giờ đến của hai nhóm giúp được không? Nếu có thay đổi tớ sẽ điều chỉnh."
    },
    {
      "id": "s05--t02",
      "speaker": "A",
      "ja": "それなら引き受けられる。明日の夕方までに確認して、結果を伝えるよ。",
      "vi": "Nếu vậy tớ nhận được. Tớ sẽ xác nhận rồi báo kết quả trước chiều mai."
    },
    {
      "id": "s05--t03",
      "speaker": "B",
      "ja": "ありがとう。返事がない団体があったら？",
      "vi": "Cảm ơn. Nếu có nhóm không trả lời thì sao?"
    },
    {
      "id": "s05--t04",
      "speaker": "A",
      "ja": "返事がないこともその時点で伝える。私の判断で時間は変えないよ。",
      "vi": "Đến lúc ấy tớ cũng sẽ báo là chưa có hồi âm. Tớ không tự đổi giờ."
    },
    {
      "id": "s05--t05",
      "speaker": "B",
      "ja": "わかった。それでお願い。",
      "vi": "Hiểu rồi. Nhờ cậu như vậy nhé."
    }
  ],
  "authorship": "original_extension"
}



## Từ chối việc vượt khả năng [s06]

{
  "id": "s06",
  "source_refs": [],
  "title": "Từ chối việc vượt khả năng",
  "event_id": "e02",
  "setting": "Một người quen nhờ bạn đứng ra giải quyết tranh chấp tiền giữa hai thành viên nhóm. Bạn không có thông tin hoặc thẩm quyền.",
  "communication_goal": "Từ chối vai phân xử và đề nghị người phù hợp.",
  "relationship": "Người quen trong nhóm cộng đồng.",
  "outcome": "declined_and_redirected",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s06--t01",
      "speaker": "B",
      "ja": "二人のお金の問題、間に入って決めてくれない？",
      "vi": "Chuyện tiền giữa hai người ấy, cậu đứng giữa quyết giúp được không?"
    },
    {
      "id": "s06--t02",
      "speaker": "A",
      "ja": "話を聞くことはできるけど、私が結論を出す立場ではないよ。",
      "vi": "Tớ có thể nghe chuyện, nhưng tớ không ở vị trí đưa ra kết luận."
    },
    {
      "id": "s06--t03",
      "speaker": "B",
      "ja": "でも、君なら公平に見てくれると思って。",
      "vi": "Nhưng tớ nghĩ cậu sẽ nhìn công bằng."
    },
    {
      "id": "s06--t04",
      "speaker": "A",
      "ja": "信頼してくれてありがとう。ただ、事実も全部知らないし、判断役は引き受けられない。責任者に相談しよう。",
      "vi": "Cảm ơn cậu tin tớ. Nhưng tớ không biết đầy đủ sự việc và không thể nhận vai phán xử. Ta hỏi người phụ trách nhé."
    },
    {
      "id": "s06--t05",
      "speaker": "B",
      "ja": "そうだね。まず本人たちにも確認する。",
      "vi": "Ừ nhỉ. Trước tiên tớ sẽ hỏi lại chính hai người đó."
    }
  ],
  "authorship": "original_extension"
}



## Chuyển đầu mối có sự đồng ý [s07]

{
  "id": "s07",
  "source_refs": [],
  "title": "Chuyển đầu mối có sự đồng ý",
  "event_id": "e02",
  "setting": "Một người quen cần người dẫn chương trình. Bạn không rảnh nhưng biết người từng làm, chưa chắc người ấy nhận.",
  "communication_goal": "Xin phép trước khi kết nối, không hứa hộ người thứ ba.",
  "relationship": "Hai người quen cùng nhóm.",
  "outcome": "referral_with_consent",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s07--t01",
      "speaker": "B",
      "ja": "来月の会の司会をお願いできる？",
      "vi": "Cậu dẫn chương trình buổi tháng sau được không?"
    },
    {
      "id": "s07--t02",
      "speaker": "A",
      "ja": "その日は難しい。経験のある佐藤さんに聞いてみることはできるけど、あなたの連絡先を伝えてもいい？",
      "vi": "Hôm ấy tớ không được. Tớ có thể hỏi chị Sato, người từng dẫn chương trình, nhưng tớ đưa thông tin liên lạc của cậu cho chị ấy được không?"
    },
    {
      "id": "s07--t03",
      "speaker": "B",
      "ja": "うん、私の連絡先は伝えていいよ。",
      "vi": "Ừ, cậu đưa thông tin liên lạc của tớ cũng được."
    },
    {
      "id": "s07--t04",
      "speaker": "A",
      "ja": "ありがとう。佐藤さんが受けるかどうかは、本人に確認してから知らせるね。",
      "vi": "Cảm ơn. Chị Sato có nhận hay không, tớ sẽ hỏi chị ấy rồi báo lại."
    },
    {
      "id": "s07--t05",
      "speaker": "B",
      "ja": "助かる。もし無理でも、こちらで別の人を探すよ。",
      "vi": "Tốt quá. Nếu chị ấy không được, bên tớ sẽ tìm người khác."
    }
  ],
  "authorship": "original_extension"
}



## Khi người kia tiếp tục thúc ép [k_pressure]

# Khi người kia tiếp tục thúc ép

Một lời từ chối mềm có thể bị hiểu là còn thương lượng được. Khi người kia nhắc lại, đừng thêm lý do mới liên tục: nhắc lại giới hạn, nói đâu là phần có thể bàn và đâu là phần đã chốt. Nếu bạn từng gợi ý tên người khác, đính chính ngay rằng gợi ý ấy không phải lời nhận làm thay. Cuộc nói có thể khép lại mà chưa có phương án: hẹn người nhờ tìm lựa chọn khác, không để trạng thái mơ hồ. Một người được nhờ dọn phòng đã nói 「ちょっと…」, nhưng người đàn anh vẫn thúc giục; lúc đó cần nói rõ phần mình không thể làm.

<a id="k_pressure_ex01"></a>
先ほどお伝えしたとおり、私には引き受けられません。

Như tôi đã nói lúc nãy, tôi không thể nhận việc ấy.

<a id="k_pressure_ex02"></a>
別の人を探すことは提案しましたが、私が代わるとは言っていません。

Tôi có gợi ý tìm người khác, chứ không nói tôi sẽ làm thay.

<a id="k_pressure_ex03"></a>
今日は結論が出ませんね。そちらで別の方法を考えてください。

Hôm nay ta chưa có kết luận. Anh/chị hãy tìm cách khác nhé.


## Nhắc lại giới hạn khi bị nài [s08]

{
  "id": "s08",
  "source_refs": [],
  "title": "Nhắc lại giới hạn khi bị nài",
  "event_id": "e03",
  "setting": "Sau khi bạn từ chối làm người dẫn chương trình, người quen bảo “chỉ một tiếng thôi”.",
  "communication_goal": "Giữ lời từ chối mà không tranh cãi số phút.",
  "relationship": "Hai người quen cùng nhóm.",
  "outcome": "boundary_repeated",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s08--t01",
      "speaker": "B",
      "ja": "全部じゃなくて、一時間だけでいいからお願いできない？",
      "vi": "Không cần cả buổi, chỉ một tiếng thôi, cậu làm được chứ?"
    },
    {
      "id": "s08--t02",
      "speaker": "A",
      "ja": "時間の長さではなく、その日に私が司会をできないんだ。",
      "vi": "Vấn đề không phải dài ngắn; hôm ấy tớ không thể dẫn chương trình."
    },
    {
      "id": "s08--t03",
      "speaker": "B",
      "ja": "準備はこっちでやるから。",
      "vi": "Bên tớ sẽ lo phần chuẩn bị mà."
    },
    {
      "id": "s08--t04",
      "speaker": "A",
      "ja": "そうしてくれるのはありがたい。でも返事は変わらないよ。司会は別の人を探してほしい。",
      "vi": "Tớ biết cậu sẵn lòng chuẩn bị. Nhưng câu trả lời của tớ vẫn vậy. Cậu tìm người khác dẫn nhé."
    },
    {
      "id": "s08--t05",
      "speaker": "B",
      "ja": "わかった。もう頼まないよ。",
      "vi": "Hiểu rồi. Tớ không nhờ nữa."
    }
  ],
  "authorship": "original_extension"
}



## Đính chính lời gợi ý bị hiểu nhầm [s09]

{
  "id": "s09",
  "source_refs": [],
  "title": "Đính chính lời gợi ý bị hiểu nhầm",
  "event_id": "e03",
  "setting": "Bạn từng gợi ý có thể chia ca, nhưng người quen báo với nhóm rằng bạn sẽ xếp lịch.",
  "communication_goal": "Sửa hiểu nhầm và nêu đúng phần mình chưa nhận.",
  "relationship": "Hai thành viên quen trong ban tổ chức.",
  "outcome": "misunderstanding_repaired",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s09--t01",
      "speaker": "B",
      "ja": "みんなには、シフトを君が決めると伝えたよ。",
      "vi": "Tớ đã báo mọi người là cậu sẽ xếp ca."
    },
    {
      "id": "s09--t02",
      "speaker": "A",
      "ja": "待って。分担を提案したけど、私がシフトを決めるとは言っていないよ。",
      "vi": "Khoan đã. Tớ gợi ý chia việc, chứ chưa nói tớ sẽ xếp ca."
    },
    {
      "id": "s09--t03",
      "speaker": "B",
      "ja": "あ、ごめん。「分けたらどう？」を引き受ける意味だと思った。",
      "vi": "À xin lỗi. Tớ tưởng câu “hay chia ra?” nghĩa là cậu nhận làm."
    },
    {
      "id": "s09--t04",
      "speaker": "A",
      "ja": "誤解させてごめん。私からも確認するけど、担当者はまだ決まっていないと伝えてくれる？",
      "vi": "Xin lỗi vì tớ nói chưa rõ. Tớ cũng sẽ xác nhận lại, nhưng cậu báo rằng người phụ trách vẫn chưa được chốt nhé?"
    },
    {
      "id": "s09--t05",
      "speaker": "B",
      "ja": "うん、すぐ訂正する。",
      "vi": "Ừ, tớ sẽ đính chính ngay."
    }
  ],
  "authorship": "original_extension"
}



## Chỉ bàn lại khi phạm vi thật sự giảm [s10]

{
  "id": "s10",
  "source_refs": [],
  "title": "Chỉ bàn lại khi phạm vi thật sự giảm",
  "event_id": "e03",
  "setting": "Người quen rút việc điều phối cả buổi xuống còn rà một danh sách trước ngày tổ chức.",
  "communication_goal": "Kiểm phần mới rồi quyết định, không mặc định mọi thay đổi đều đủ.",
  "relationship": "Hai người cùng nhóm.",
  "outcome": "reduced_scope_considered",
  "follows": [
    "s08"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s10--t01",
      "speaker": "B",
      "ja": "司会は別の人に頼んだ。参加者の名前だけ、前日に確認してもらえる？",
      "vi": "Tớ đã nhờ người khác dẫn. Cậu chỉ xem tên người tham gia vào hôm trước được không?"
    },
    {
      "id": "s10--t02",
      "speaker": "A",
      "ja": "名前の確認だけなら検討できる。人数は何人で、誰の一覧を使うの？",
      "vi": "Nếu chỉ xem tên thì tớ có thể cân nhắc. Bao nhiêu người và dùng danh sách của ai?"
    },
    {
      "id": "s10--t03",
      "speaker": "B",
      "ja": "二十人くらい。私が確定した一覧を渡す。",
      "vi": "Khoảng hai mươi người. Tớ sẽ đưa danh sách đã chốt."
    },
    {
      "id": "s10--t04",
      "speaker": "A",
      "ja": "それなら金曜の夜に確認できる。変更の連絡はそちらでお願い。",
      "vi": "Vậy tối thứ Sáu tớ xem được. Việc báo thay đổi nhờ bên cậu nhé."
    },
    {
      "id": "s10--t05",
      "speaker": "B",
      "ja": "わかった。そこは私がするよ。",
      "vi": "Hiểu rồi. Phần đó tớ làm."
    }
  ],
  "authorship": "original_extension"
}



## Khép cuộc nói khi chưa thống nhất [s11]

{
  "id": "s11",
  "source_refs": [],
  "title": "Khép cuộc nói khi chưa thống nhất",
  "event_id": "e03",
  "setting": "Người quen vẫn muốn bạn nhận toàn bộ ca trực dù bạn đã giải thích không thể làm.",
  "communication_goal": "Kết thúc rõ ràng, không tạo lời hứa thay thế.",
  "relationship": "Hai người quen trong nhóm.",
  "outcome": "unresolved_but_closed",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s11--t01",
      "speaker": "B",
      "ja": "やっぱり君に全部お願いしたいんだ。ほかに人がいなくて。",
      "vi": "Tớ vẫn muốn cậu nhận hết. Không còn ai khác."
    },
    {
      "id": "s11--t02",
      "speaker": "A",
      "ja": "困っているのは分かる。でも、私が全部担当することはできない。",
      "vi": "Tớ hiểu cậu đang bí. Nhưng tớ không thể phụ trách toàn bộ."
    },
    {
      "id": "s11--t03",
      "speaker": "B",
      "ja": "じゃあ、今は答えが出ないね。",
      "vi": "Vậy giờ vẫn chưa có cách rồi."
    },
    {
      "id": "s11--t04",
      "speaker": "A",
      "ja": "そうだね。私の返事は「引き受けない」で確定している。別の体制を考えてほしい。",
      "vi": "Đúng. Phần trả lời của tớ đã rõ là không nhận. Cậu hãy tính cách tổ chức khác nhé."
    },
    {
      "id": "s11--t05",
      "speaker": "B",
      "ja": "分かった。こちらで相談する。",
      "vi": "Hiểu rồi. Bên tớ sẽ bàn tiếp."
    }
  ],
  "authorship": "original_extension"
}



## Từ báo thay đổi và bàn giao [v_change]

{
  "id": "v_change",
  "source_refs": [],
  "items": [
    {
      "id": "v_change-w-785f06f6d1f4",
      "ja": "追加する",
      "source_refs": []
    },
    {
      "id": "v_change-w-dadf94109e38",
      "ja": "優先する",
      "source_refs": []
    },
    {
      "id": "v_change-w-736446211b85",
      "ja": "延ばす",
      "source_refs": []
    },
    {
      "id": "v_change-w-d750d0c075e6",
      "ja": "進捗",
      "source_refs": []
    },
    {
      "id": "v_change-w-bcd69e5aeb73",
      "ja": "引き継ぐ",
      "source_refs": []
    },
    {
      "id": "v_change-w-3f987b7dbd75",
      "ja": "未決定",
      "source_refs": []
    },
    {
      "id": "v_change-w-cf83d7094bfd",
      "ja": "確定する",
      "source_refs": []
    }
  ]
}



## Mẫu báo điều kiện và trạng thái [g_change]

{
  "id": "g_change",
  "source_refs": [],
  "items": [
    {
      "id": "g_change-g-054513c3b455",
      "name_ja": "〜場合は",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_change-g-53c17fc96cd3",
      "name_ja": "〜ておく",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_change-g-09e406da0836",
      "name_ja": "〜た上で",
      "jlpt_level": "N2",
      "reference": {
        "kind": "bunpou"
      }
    }
  ]
}



## Khi đã nhận nhưng việc tăng lên [k_change]

# Khi đã nhận nhưng việc tăng lên

Đã nhận một phần không có nghĩa là tự động nhận mọi phần phát sinh. Báo ngay khi phạm vi đổi, nhắc lại điều đã thống nhất và đưa lựa chọn có điều kiện: giữ phạm vi cũ, thêm việc nhưng dời hạn, hoặc chuyển phần mới cho người phụ trách. Nếu người kia đồng ý, nhắc lại phân công và mốc tiếp theo bằng lời. Nếu chưa thống nhất, chỉ làm phần cũ mà bạn vẫn có thể làm; đừng để sự im lặng bị hiểu là nhận phần mới.

<a id="k_change_ex01"></a>
最初にお受けしたのは、参加者への連絡までです。

Ban đầu tôi chỉ nhận liên hệ người tham gia.

<a id="k_change_ex02"></a>
この作業も追加するなら、締め切りを二日延ばしていただけますか。

Nếu thêm cả việc này, anh/chị có thể dời hạn thêm hai ngày không?

<a id="k_change_ex03"></a>
新しい部分は担当者に相談した上で決めましょう。

Ta hãy hỏi người phụ trách rồi quyết phần mới nhé.


## Báo phần mới trước khi làm [s12]

{
  "id": "s12",
  "source_refs": [],
  "title": "Báo phần mới trước khi làm",
  "event_id": "e04",
  "setting": "Bạn đã nhận gọi xác nhận giờ đến. Người quen thêm việc phân công chỗ ngồi.",
  "communication_goal": "Nêu phần mới nằm ngoài cam kết và hỏi ưu tiên.",
  "relationship": "Hai thành viên cùng ban tổ chức.",
  "outcome": "new_scope_flagged",
  "follows": [
    "s05"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s12--t01",
      "speaker": "B",
      "ja": "到着時間の確認に加えて、席も決めてもらえる？",
      "vi": "Ngoài xác nhận giờ đến, cậu xếp chỗ ngồi luôn được không?"
    },
    {
      "id": "s12--t02",
      "speaker": "A",
      "ja": "席決めは最初の話にはなかったね。今は連絡を優先しているから、追加するなら分担を相談したい。",
      "vi": "Xếp chỗ không nằm trong phần đã bàn. Giờ tớ đang ưu tiên liên hệ; nếu thêm thì mình cần bàn chia việc."
    },
    {
      "id": "s12--t03",
      "speaker": "B",
      "ja": "そうか。急に増やしてごめん。席は私が考えるよ。",
      "vi": "Ra vậy. Xin lỗi vì thêm đột ngột. Chỗ ngồi để tớ tính."
    },
    {
      "id": "s12--t04",
      "speaker": "A",
      "ja": "ありがとう。到着時間は明日の夕方に伝えるね。",
      "vi": "Cảm ơn. Giờ đến tớ sẽ báo vào chiều mai."
    }
  ],
  "authorship": "original_extension"
}



## Thêm việc nếu dời hạn [s13]

{
  "id": "s13",
  "source_refs": [],
  "title": "Thêm việc nếu dời hạn",
  "event_id": "e04",
  "setting": "Bạn đã nhận rà danh sách người tham gia. Người quen muốn thêm kiểm tra nhu cầu ăn uống; bạn chỉ có thể làm nếu dời hạn.",
  "communication_goal": "Đưa điều kiện thời gian và chốt lại.",
  "relationship": "Hai người cùng tổ chức buổi giao lưu.",
  "outcome": "deadline_renegotiated",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s13--t01",
      "speaker": "B",
      "ja": "食事の希望も一緒に確認してもらえる？",
      "vi": "Cậu hỏi thêm nhu cầu ăn uống giúp được không?"
    },
    {
      "id": "s13--t02",
      "speaker": "A",
      "ja": "追加で確認するなら、返事を集める時間が要る。締め切りを日曜まで延ばせる？",
      "vi": "Nếu hỏi thêm, cần thời gian gom hồi âm. Dời hạn đến Chủ nhật được không?"
    },
    {
      "id": "s13--t03",
      "speaker": "B",
      "ja": "日曜なら大丈夫。土曜には途中経過だけ教えて。",
      "vi": "Chủ nhật được. Thứ Bảy báo tớ tiến độ giữa chừng nhé."
    },
    {
      "id": "s13--t04",
      "speaker": "A",
      "ja": "了解。土曜に進捗、日曜に確認できた分の結果を伝える。返事のない人は別に知らせるよ。",
      "vi": "Được. Thứ Bảy tớ báo tiến độ, Chủ nhật báo kết quả đã xác nhận. Ai chưa hồi âm tớ sẽ báo riêng."
    },
    {
      "id": "s13--t05",
      "speaker": "B",
      "ja": "それでお願い。",
      "vi": "Nhờ cậu như vậy nhé."
    }
  ],
  "authorship": "original_extension"
}



## Giữ phần cũ, từ chối phần mới [s14]

{
  "id": "s14",
  "source_refs": [],
  "title": "Giữ phần cũ, từ chối phần mới",
  "event_id": "e04",
  "setting": "Sau khi bạn nhận kiểm giờ đến, người quen muốn bạn trực điện thoại cả ngày diễn ra sự kiện.",
  "communication_goal": "Tách cam kết cũ và lời từ chối mới.",
  "relationship": "Hai người quen cùng nhóm.",
  "outcome": "old_scope_kept_new_declined",
  "follows": [
    "s05"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s14--t01",
      "speaker": "B",
      "ja": "当日の電話対応もお願いできないかな。",
      "vi": "Hôm diễn ra buổi đó cậu trực điện thoại luôn được không?"
    },
    {
      "id": "s14--t02",
      "speaker": "A",
      "ja": "当日は別の予定があるから、それは引き受けられない。到着時間の確認は予定どおり進めるよ。",
      "vi": "Hôm ấy tớ có việc khác nên không nhận phần đó. Việc xác nhận giờ đến tớ vẫn làm như đã hẹn."
    },
    {
      "id": "s14--t03",
      "speaker": "B",
      "ja": "分かった。電話は別の人に頼む。",
      "vi": "Hiểu rồi. Phần điện thoại tớ nhờ người khác."
    },
    {
      "id": "s14--t04",
      "speaker": "A",
      "ja": "助かる。確認結果は明日まとめて伝えるね。",
      "vi": "Cảm ơn. Kết quả xác nhận tớ sẽ báo gộp vào ngày mai."
    }
  ],
  "authorship": "original_extension"
}



## Chuyển phần cần quyền quyết [s15]

{
  "id": "s15",
  "source_refs": [],
  "title": "Chuyển phần cần quyền quyết",
  "event_id": "e04",
  "setting": "Trong lúc liên hệ các nhóm, một nhóm đề nghị đổi giờ và đổi địa điểm. Bạn chỉ được giao xác nhận thông tin.",
  "communication_goal": "Chuyển quyết định về đúng người và hẹn phản hồi.",
  "relationship": "Hai thành viên ban tổ chức.",
  "outcome": "decision_escalated",
  "follows": [
    "s05"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s15--t01",
      "speaker": "A",
      "ja": "一団体から時間と会場を変えたいと連絡があった。私だけでは決められないから、相談したい。",
      "vi": "Một nhóm báo muốn đổi giờ và địa điểm. Tớ không thể tự quyết nên muốn bàn với cậu."
    },
    {
      "id": "s15--t02",
      "speaker": "B",
      "ja": "連絡ありがとう。それぞれ、変更したい理由は聞いた？",
      "vi": "Cảm ơn đã báo. Cậu đã hỏi lý do họ muốn đổi từng phần chưa?"
    },
    {
      "id": "s15--t03",
      "speaker": "A",
      "ja": "時間は移動の都合、会場は人数が増えたからだそう。返事はいつまでに必要？",
      "vi": "Họ nói giờ là vì đi lại, địa điểm vì số người tăng. Khi nào cần trả lời?"
    },
    {
      "id": "s15--t04",
      "speaker": "B",
      "ja": "明日の昼までに私が確認して決める。今は返事を保留にして。",
      "vi": "Trước trưa mai tớ sẽ kiểm rồi quyết. Giờ cứ để câu trả lời chờ đã."
    },
    {
      "id": "s15--t05",
      "speaker": "A",
      "ja": "分かった。先方には明日の午後に返答すると伝える。",
      "vi": "Hiểu rồi. Tớ sẽ báo họ rằng chiều mai sẽ có câu trả lời."
    }
  ],
  "authorship": "original_extension"
}



## Bàn giao khi phải dừng [k_handoff]

# Bàn giao khi phải dừng

Khi không thể tiếp tục, báo trước khi người khác tưởng việc đã xong. Nói ba điều theo thứ tự: phần đã hoàn thành, phần chưa quyết hoặc chưa nhận được hồi âm, và người có quyền quyết định tiếp. Hỏi người tiếp quản cần biết thông tin nào; nếu chỉ có thể giải thích một lần sau bàn giao, nói rõ mốc. Sau đó xác nhận người mới đã hiểu, thay vì tự tuyên bố “đã bàn giao” khi họ chưa nhận.

<a id="k_handoff_ex01"></a>
三団体には連絡済みですが、一団体からはまだ返事がありません。

Tôi đã liên hệ ba nhóm, nhưng còn một nhóm chưa trả lời.

<a id="k_handoff_ex02"></a>
残っている判断は、会場を変えるかどうかです。

Quyết định còn lại là có đổi địa điểm hay không.

<a id="k_handoff_ex03"></a>
明日一度だけ、経緯を説明できます。

Ngày mai tôi có thể giải thích diễn biến một lần.


## Báo phần xong và phần còn mở [s16]

{
  "id": "s16",
  "source_refs": [],
  "title": "Báo phần xong và phần còn mở",
  "event_id": "e05",
  "setting": "Bạn phải rời nhóm tổ chức sớm. Người quen tiếp quản liên hệ các nhóm.",
  "communication_goal": "Báo trạng thái cụ thể thay vì “gần xong”.",
  "relationship": "Bạn và người tiếp quản cùng nhóm.",
  "outcome": "handoff_status_clear",
  "follows": [
    "s15"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s16--t01",
      "speaker": "A",
      "ja": "三団体のうち二団体は時間が確定した。一団体はまだ返事待ち。",
      "vi": "Trong ba nhóm, hai nhóm đã chốt giờ. Một nhóm vẫn chưa hồi âm."
    },
    {
      "id": "s16--t02",
      "speaker": "B",
      "ja": "会場については決まっている？",
      "vi": "Địa điểm đã quyết chưa?"
    },
    {
      "id": "s16--t03",
      "speaker": "A",
      "ja": "そこも未決定。人数が増える可能性を伝えたけど、判断は責任者にお願いしている。",
      "vi": "Cũng chưa. Tớ đã báo khả năng tăng người, còn quyết định là của người phụ trách."
    },
    {
      "id": "s16--t04",
      "speaker": "B",
      "ja": "分かった。私が返事を追って、責任者にも確認する。",
      "vi": "Hiểu rồi. Tớ sẽ liên hệ hỏi xem nhóm còn lại trả lời chưa, rồi hỏi cả người phụ trách."
    },
    {
      "id": "s16--t05",
      "speaker": "A",
      "ja": "ありがとう。必要な経緯は今ここで説明するよ。",
      "vi": "Cảm ơn. Diễn biến cần biết tớ giải thích ngay đây."
    }
  ],
  "authorship": "original_extension"
}



## Sửa hiểu nhầm “đã hoàn thành” [s17]

{
  "id": "s17",
  "source_refs": [],
  "title": "Sửa hiểu nhầm “đã hoàn thành”",
  "event_id": "e05",
  "setting": "Người nhờ tưởng bạn đã chốt cả địa điểm, nhưng bạn chỉ xác nhận giờ đến.",
  "communication_goal": "Chỉnh trạng thái và thống nhất ai xử lý phần còn lại.",
  "relationship": "Hai thành viên cùng ban tổ chức.",
  "outcome": "completion_misunderstanding_fixed",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s17--t01",
      "speaker": "B",
      "ja": "会場も含めて全部終わったと聞いたけど、これで大丈夫？",
      "vi": "Tớ nghe nói cả địa điểm đã xong hết, vậy ổn rồi chứ?"
    },
    {
      "id": "s17--t02",
      "speaker": "A",
      "ja": "ううん、終わったのは到着時間の確認だけ。会場の変更はまだ決まっていない。",
      "vi": "Chưa đâu. Chỉ việc xác nhận giờ đến là xong. Đổi địa điểm vẫn chưa được quyết."
    },
    {
      "id": "s17--t03",
      "speaker": "B",
      "ja": "私が勘違いした。会場は誰に聞けばいい？",
      "vi": "Tớ hiểu nhầm. Địa điểm thì hỏi ai?"
    },
    {
      "id": "s17--t04",
      "speaker": "A",
      "ja": "責任者の田中さん。私から状況を伝えておくので、最終判断は直接確認して。",
      "vi": "Chị Tanaka phụ trách. Tớ sẽ báo tình hình, còn quyết định cuối cùng cậu hỏi trực tiếp chị ấy nhé."
    },
    {
      "id": "s17--t05",
      "speaker": "B",
      "ja": "分かった。今日中に確認する。",
      "vi": "Hiểu rồi. Hôm nay tớ sẽ hỏi."
    }
  ],
  "authorship": "original_extension"
}



## Xác nhận người tiếp quản đã nhận [s18]

{
  "id": "s18",
  "source_refs": [],
  "title": "Xác nhận người tiếp quản đã nhận",
  "event_id": "e05",
  "setting": "Bạn đã báo tình hình cho người tiếp quản; hôm sau hai người nói lại phần chờ hồi âm.",
  "communication_goal": "Xác nhận chủ mới của việc và giới hạn hỗ trợ.",
  "relationship": "Bạn và người tiếp quản cùng nhóm.",
  "outcome": "handoff_accepted",
  "follows": [
    "s16"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s18--t01",
      "speaker": "A",
      "ja": "昨日の件、残っていた一団体への連絡は引き継げそう？",
      "vi": "Việc hôm qua, cậu tiếp nhận liên hệ với nhóm còn lại được chứ?"
    },
    {
      "id": "s18--t02",
      "speaker": "B",
      "ja": "うん、担当を引き受けた。連絡先も確認したよ。",
      "vi": "Ừ, tớ đã nhận phụ trách và kiểm thông tin liên lạc rồi."
    },
    {
      "id": "s18--t03",
      "speaker": "A",
      "ja": "ありがとう。経緯で分からないところがあれば、今日中なら一度説明できる。",
      "vi": "Cảm ơn. Nếu có chỗ chưa rõ về diễn biến, trong hôm nay tớ có thể giải thích một lần."
    },
    {
      "id": "s18--t04",
      "speaker": "B",
      "ja": "今は大丈夫。新しい返事は私から責任者に伝える。",
      "vi": "Hiện giờ ổn. Hồi âm mới tớ sẽ báo cho người phụ trách."
    },
    {
      "id": "s18--t05",
      "speaker": "A",
      "ja": "了解。これで私の担当は終わりにするね。",
      "vi": "Hiểu rồi. Vậy phần tớ phụ trách kết thúc ở đây nhé."
    }
  ],
  "authorship": "original_extension"
}



## Sau lời từ chối, giữ quan hệ bằng việc thật [k_relation]

# Sau lời từ chối, giữ quan hệ bằng việc thật

Từ chối một việc không đồng nghĩa từ chối con người. Khi gặp lại, có thể hỏi ngắn xem họ đã tìm được cách giải quyết chưa, nhưng đừng hỏi như để nhận lại phần việc. Nếu họ tưởng bạn giận, nói rõ ranh giới là về việc và thời gian của bạn. Cảm ơn họ đã tôn trọng câu trả lời; đừng hứa “lần sau việc gì cũng được”. Câu chuyện có thể chuyển sang chuyện chung khác khi cả hai đều sẵn sàng.

<a id="k_relation_ex01"></a>
先日は引き受けられなかったけど、その後どうなった？

Hôm trước tớ không nhận được; sau đó việc ấy thế nào rồi?

<a id="k_relation_ex02"></a>
あなたに怒っているわけじゃないよ。今回はその役割を担えなかっただけ。

Tớ không giận cậu đâu. Chỉ là lần này tớ không thể đảm nhận vai đó.

<a id="k_relation_ex03"></a>
分かってくれてありがとう。別の話だけど、来週の集まりには行く？

Cảm ơn cậu đã hiểu. Chuyện khác nhé, tuần sau cậu có đến buổi gặp không?


## Gặp lại sau khi từ chối [s19]

{
  "id": "s19",
  "source_refs": [],
  "title": "Gặp lại sau khi từ chối",
  "event_id": "e06",
  "setting": "Một tuần sau lời từ chối dẫn chương trình, bạn gặp người đã nhờ tại buổi họp nhóm.",
  "communication_goal": "Hỏi tình hình không ngỏ ý nhận lại.",
  "relationship": "Hai người quen trong nhóm.",
  "outcome": "relationship_resumed",
  "follows": [
    "s07"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s19--t01",
      "speaker": "A",
      "ja": "先日は引き受けられなくてごめん。その後、司会は決まった？",
      "vi": "Hôm trước tớ không nhận được, xin lỗi nhé. Sau đó đã có người dẫn chưa?"
    },
    {
      "id": "s19--t02",
      "speaker": "B",
      "ja": "うん、佐藤さんが引き受けてくれた。心配してくれてありがとう。",
      "vi": "Ừ, chị Sato nhận rồi. Cảm ơn cậu đã hỏi."
    },
    {
      "id": "s19--t03",
      "speaker": "A",
      "ja": "決まってよかった。準備は順調？",
      "vi": "Chốt được thì tốt rồi. Chuẩn bị ổn chứ?"
    },
    {
      "id": "s19--t04",
      "speaker": "B",
      "ja": "今のところね。今日は会場の下見に来たんだ。",
      "vi": "Tạm thời ổn. Hôm nay tớ đến xem địa điểm."
    },
    {
      "id": "s19--t05",
      "speaker": "A",
      "ja": "そうなんだ。じゃ、会議が始まる前に少し見て回ろうか。",
      "vi": "Ra vậy. Thế trước khi họp mình đi xem một vòng nhé?"
    }
  ],
  "authorship": "original_extension"
}



## Làm rõ ranh giới không phải giận [s20]

{
  "id": "s20",
  "source_refs": [],
  "title": "Làm rõ ranh giới không phải giận",
  "event_id": "e06",
  "setting": "Sau khi bạn từ chối nhận toàn bộ ca trực, người bạn ít thấy bạn nói chuyện và tưởng bạn giận.",
  "communication_goal": "Sửa hiểu nhầm, giữ ranh giới đã nói.",
  "relationship": "Hai bạn quen trong nhóm.",
  "outcome": "relationship_reassured",
  "follows": [
    "s11"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người xử lý lời nhờ"
    },
    {
      "id": "B",
      "role": "Người nhờ hoặc người tiếp quản"
    }
  ],
  "turns": [
    {
      "id": "s20--t01",
      "speaker": "B",
      "ja": "この前のことで、私に怒ってる？",
      "vi": "Chuyện hôm trước làm cậu giận tớ à?"
    },
    {
      "id": "s20--t02",
      "speaker": "A",
      "ja": "怒ってないよ。ただ、あの役割は私には重すぎたんだ。",
      "vi": "Tớ không giận. Chỉ là trách nhiệm đó vượt quá sức tớ."
    },
    {
      "id": "s20--t03",
      "speaker": "B",
      "ja": "急に頼んで、何度も押してしまってごめん。",
      "vi": "Xin lỗi vì nhờ gấp rồi còn nài nhiều lần."
    },
    {
      "id": "s20--t04",
      "speaker": "A",
      "ja": "話してくれてありがとう。次はお互い、できる範囲を先に確認しよう。",
      "vi": "Cảm ơn cậu đã nói. Lần sau hai bên hỏi rõ phạm vi có thể làm trước nhé."
    },
    {
      "id": "s20--t05",
      "speaker": "B",
      "ja": "うん。今日は普通に話せてよかった。",
      "vi": "Ừ. Hôm nay lại nói chuyện thoải mái được, tớ mừng lắm."
    }
  ],
  "authorship": "original_extension"
}



## Trò chuyện tự do: lời nhờ khó và giới hạn [ft01]

{
  "id": "ft01",
  "source_refs": [],
  "context_node_ids": [
    "v_scope",
    "g_scope",
    "k_scope",
    "k_indirect",
    "sh_indirect",
    "s01",
    "s02",
    "s03",
    "v_boundary",
    "g_boundary",
    "k_boundary",
    "s04",
    "s05",
    "s06",
    "s07",
    "k_pressure",
    "s08",
    "s09",
    "s10",
    "s11",
    "v_change",
    "g_change",
    "k_change",
    "s12",
    "s13",
    "s14",
    "s15",
    "k_handoff",
    "s16",
    "s17",
    "s18",
    "k_relation",
    "s19",
    "s20"
  ],
  "overview_vi": "Xử lý lời nhờ khó trong quan hệ bạn bè, người quen và cộng tác: hỏi rõ trách nhiệm, nói lời từ chối, thương lượng phần có thể giúp, báo thay đổi sau khi nhận, bàn giao và giữ quan hệ. Luyện nghe và nói qua các diễn biến có hậu quả.",
  "optional_extensions": [],
  "context_export": "live-context.md",
  "free_talk": {
    "learner_intro_vi": "Hãy chọn một việc khó trong nhóm bạn, tổ chức cộng đồng hoặc nơi làm việc. Bạn có thể là người được nhờ hoặc người đang nhờ. Bắt đầu từ nhu cầu thật, hỏi phạm vi, nhận một phần, từ chối, đổi điều kiện hay quay lại chuyện sau đó. Cuộc nói có thể đi theo hướng bạn chọn; không cần dùng hết các câu mẫu.",
    "ai_situation_vi": "Trò chuyện tự do với người học về một lời nhờ có trách nhiệm rõ và khả năng thay đổi. AI chọn một quan hệ phù hợp rồi giữ nhất quán xưng hô và mức lịch sự. Có thể là bạn quen nhờ tổ chức một buổi gặp, đồng nghiệp cần hỗ trợ liên hệ các nhóm, hoặc người tiếp quản một việc còn dở. Cho thông tin theo câu hỏi; không mặc định lời gợi ý là lời nhận. Có thể đồng ý giới hạn, xin thêm thời gian, không thể đổi hạn, hoặc hiểu nhầm một phát biểu rồi để người học sửa. Nếu người học từ chối, tôn trọng và cùng tìm bước kế; không nài vô hạn. Nếu việc đã nhận phát sinh, giúp phân biệt cam kết cũ/phần mới; khi bàn giao, xác nhận việc xong/chưa xong và đầu mối. Sau lời từ chối, có thể cho hai người gặp lại và nói về chuyện chung. Các ví dụ, từ và mẫu trong context là tài liệu tham khảo, không phải lời người học đã nói. Để người học chủ động đổi hướng, kể cả ngoài các cảnh gợi ý. Không chấm điểm, khóa bài hoặc yêu cầu kể trải nghiệm riêng nhạy cảm.",
    "conversation_starters_vi": [
      "Một người quen nói “cậu lo giúp buổi gặp nhé” nhưng chưa nói cần lo đến đâu. Bạn muốn hỏi gì?",
      "Bạn đã nhận gọi xác nhận giờ đến; nay họ thêm việc xếp chỗ. Bạn sẽ nói thế nào?",
      "Bạn đã từ chối một vai khó. Tuần sau gặp lại người ấy, bạn muốn mở chuyện ra sao?"
    ],
    "mode": "free_talk",
    "content_origin": "curriculum_authored",
    "situation_export": "free-talk-situation.md"
  }
}



## Bài học và nội dung gối đầu

{
  "schema_version": "1.0",
  "stage_uid": "22840572-0228-51e3-a068-ef0e18149953",
  "lessons": [
    {
      "id": "l01",
      "summary": "Hỏi rõ trước khi nhận",
      "node_ids": [
        "v_scope",
        "g_scope",
        "k_scope",
        "k_indirect",
        "sh_indirect",
        "s01",
        "s02",
        "s03"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l02",
      "summary": "Từ chối và thương lượng phần có thể giúp",
      "node_ids": [
        "v_boundary",
        "g_boundary",
        "k_boundary",
        "s04",
        "s05",
        "s06",
        "s07",
        "k_pressure",
        "s08",
        "s09",
        "s10",
        "s11"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l03",
      "summary": "Khi phần việc đổi",
      "node_ids": [
        "v_change",
        "g_change",
        "k_change",
        "s12",
        "s13",
        "s14",
        "s15"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l04",
      "summary": "Bàn giao và tiếp tục quan hệ",
      "node_ids": [
        "k_handoff",
        "s16",
        "s17",
        "s18",
        "k_relation",
        "s19",
        "s20"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    }
  ]
}



## Nguồn và phạm vi chứng cứ

{
  "scan": [
    {
      "book_id": "B01",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B02",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B03",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B04",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B05",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B06",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B07",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B08",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B09",
      "status": "read",
      "note": "§21 用例/giải thích, ba hội thoại và audio.md; chọn toàn pack ví dụ dù track không in"
    },
    {
      "book_id": "B10",
      "status": "read",
      "note": "Bài 5, giải thích cách nhờ/từ chối, CD31–36, hai hội thoại chính; dùng kiến thức, không khai báo pack audio chưa kiểm"
    },
    {
      "book_id": "B11",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B12",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B13",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B14",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B15",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B16",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B17",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B18",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B19",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B20",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B21",
      "status": "read",
      "note": "Bài 4 本文会話, người được nhờ dạy tiếng Anh từ chối dù người kia giảm tần suất; dùng mạch/kiến thức, chưa pack"
    },
    {
      "book_id": "B22",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B23",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B24",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B25",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B26",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    },
    {
      "book_id": "B27",
      "status": "index_only",
      "note": "Đã quét tên, mục đích, thế mạnh và heading trong BOOK_GUIDE; chưa đọc nội dung liên quan hoặc không chọn."
    }
  ],
  "entries": [
    {
      "id": "srcB09",
      "kind": "book",
      "book_id": "B09",
      "path": "kaiwa_skill/knowledge/なめらか日本語会話/chapters/22-21-文句を言う・断る.md",
      "locator": {
        "heading": "§21 用例, PDF131–132; lời từ chối sau bị ép và lời nêu vấn đề còn để ngỏ"
      },
      "sha256": "6b9a3d706e5bc837e79451805d86d80bc192932e654f2bcc81fd12d68ef5c163",
      "read_status": "read",
      "used_for": [
        "k_indirect",
        "sh_indirect",
        "k_boundary",
        "k_pressure"
      ],
      "contribution": "Nguyên văn pack ví dụ; phân tích sắc thái ちょっと…"
    },
    {
      "id": "srcB10",
      "kind": "book",
      "book_id": "B10",
      "path": "kaiwa_skill/knowledge/にほんごで働く！ビジネス日本語30時間/chapters/05-頼む・断る.md",
      "locator": {
        "heading": "Bài 5, trang in 70–77; 表現 và 会話1–2"
      },
      "sha256": "c7e5bbd22c420c3d5d59ea2ecab511168451706d228e819e790ad7c034dee3f0",
      "read_status": "read",
      "used_for": [
        "k_scope",
        "k_boundary",
        "k_change"
      ],
      "contribution": "Mẫu từ chối, chuyển người khác và thương lượng hạn"
    },
    {
      "id": "srcB21",
      "kind": "book",
      "book_id": "B21",
      "path": "kaiwa_skill/knowledge/日本語でビジネス会話 中級編 本文冊/chapters/04-kotowari.md",
      "locator": {
        "heading": "Bài 4 断り, 本文会話 và 類話"
      },
      "sha256": "0b281055c67fffde7d8c037d25ab6a6990196a927761820dbc4e82c634477fd1",
      "read_status": "read",
      "used_for": [
        "k_scope",
        "k_boundary",
        "k_pressure",
        "k_change"
      ],
      "contribution": "Mạch người nhờ tiếp tục giảm phạm vi nhưng người được nhờ vẫn từ chối"
    },
    {
      "id": "srcJF",
      "kind": "web",
      "url": "https://www.jfstandard.jpf.go.jp/cando/about/summary/ja/render.do",
      "title": "みんなのCan-doサイト — Can-doとは",
      "accessed": "2026-11-13",
      "read_status": "read",
      "used_for": [
        "k_scope"
      ],
      "contribution": "Khung mục tiêu hành động giao tiếp; không phải nguồn nguyên văn hội thoại."
    },
    {
      "id": "srcOriginal",
      "kind": "original",
      "read_status": "read",
      "used_for": [],
      "contribution": "Biên soạn các cảnh hư cấu về lời nhờ khó, ranh giới, bàn giao và giữ quan hệ; không khẳng định quy trình pháp lý hay nhân sự."
    }
  ],
  "audio_evidence": [
    {
      "book_id": "B09",
      "edition": "なめらか日本語会話; 富阪容子, アルク; bản scan in lần 6 (2002-08-05), phát hành đầu 1997-01-15",
      "disc": "unknown",
      "track": "unknown",
      "locator": "§21 用例 PDF131–132 không in nhãn CD/track; băng bán riêng chỉ ghi rõ cho 聞きとり練習 tại PDF134",
      "availability": "unknown"
    }
  ]
}

