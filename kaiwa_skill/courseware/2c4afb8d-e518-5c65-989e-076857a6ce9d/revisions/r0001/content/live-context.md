# Làm quen & trò chuyện với người mới

{
  "schema_version": "3.2-draft",
  "stage_uid": "2c4afb8d-e518-5c65-989e-076857a6ce9d",
  "display_code": "T-001",
  "title": "Làm quen & trò chuyện với người mới",
  "level": "Trung",
  "scope": "Làm quen trong lớp và sự kiện, đáp qua lại thay vì hỏi như phỏng vấn, nhận tín hiệu muốn dừng, nối lại cuộc nói ở lần gặp sau và khép lời với đường tiếp phù hợp. Trình độ Trung; chỉ luyện nghe và nói.",
  "events": [
    {
      "id": "e01",
      "title": "Gặp trong lớp hoặc nhóm mới",
      "situation_ids": [
        "s01",
        "s02",
        "s03",
        "s04",
        "s05"
      ]
    },
    {
      "id": "e02",
      "title": "Gặp ở sự kiện địa phương",
      "situation_ids": [
        "s06",
        "s07",
        "s08",
        "s09",
        "s10"
      ]
    },
    {
      "id": "e03",
      "title": "Cân bằng chủ đề riêng tư",
      "situation_ids": [
        "s11",
        "s12",
        "s13",
        "s14",
        "s15"
      ]
    },
    {
      "id": "e04",
      "title": "Nối lần gặp thứ hai",
      "situation_ids": [
        "s16",
        "s17",
        "s18",
        "s19",
        "s20"
      ]
    },
    {
      "id": "e05",
      "title": "Kết thúc có đường tiếp",
      "situation_ids": [
        "s21",
        "s22",
        "s23",
        "s24",
        "s25"
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


## Từ cho lớp và sự kiện [v_context]

{
  "id": "v_context",
  "source_refs": [],
  "items": [
    {
      "id": "v_context-w-d73150de71b7",
      "ja": "参加する",
      "source_refs": []
    },
    {
      "id": "v_context-w-d3c09df41fcc",
      "ja": "講座",
      "source_refs": []
    },
    {
      "id": "v_context-w-0634cc2853b8",
      "ja": "受付",
      "source_refs": []
    },
    {
      "id": "v_context-w-57d96c91dcb2",
      "ja": "案内",
      "source_refs": []
    },
    {
      "id": "v_context-w-c742537502dc",
      "ja": "展示",
      "source_refs": []
    },
    {
      "id": "v_context-w-2ea6cd27051c",
      "ja": "印象",
      "source_refs": []
    },
    {
      "id": "v_context-w-dcc23a41414b",
      "ja": "感想",
      "source_refs": []
    },
    {
      "id": "v_context-w-9683551a843c",
      "ja": "説明",
      "source_refs": []
    },
    {
      "id": "v_context-w-322870357d83",
      "ja": "興味",
      "source_refs": []
    },
    {
      "id": "v_context-w-54c74a0d3533",
      "ja": "会場",
      "source_refs": []
    }
  ]
}



## Mẫu để hỏi và kể qua lại [g_core]

{
  "id": "g_core",
  "source_refs": [
    "srcGrammar"
  ],
  "items": [
    {
      "id": "g_core-g-4f7d17723ebe",
      "name_ja": "〜んです／んですか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-7634048f223c",
      "name_ja": "普通形と思います（推量・意見）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-3a4690736128",
      "name_ja": "Vたことがあります",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-9d0dc4495cf6",
      "name_ja": "〜たら（仮定条件）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-a9a4f882243d",
      "name_ja": "〜でしょう",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-f1eefc720467",
      "name_ja": "〜かもしれません",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_core-g-5b8d10b4a720",
      "name_ja": "条件形（〜ば）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Mở chuyện từ điểm hai người đang chia sẻ [k_open]

# Mở một cuộc nói có chỗ bám

Ở mức Trung, đích không dừng ở nói tên. Hãy nhìn việc cả hai đang cùng làm: chờ lớp, xem tác phẩm, chuẩn bị dụng cụ. Một câu hỏi cụ thể dễ trả lời hơn câu hỏi về lý lịch. Người kia biết hoặc chưa biết đều có đường tiếp.

<a id="s01_u01"></a>
すみません、この材料は二人で使うんでしょうか。

Xin lỗi, nguyên liệu này hai người dùng chung phải không ạ?

<a id="s01_u02"></a>
そうみたいです。私も今日が初めてで、まだよく分からなくて。

Có vẻ vậy. Hôm nay tôi cũng lần đầu đến, vẫn chưa rõ lắm.

Nghe người kia cũng lần đầu đến, tự cho biết mình ở vị trí tương tự rồi hỏi nhẹ:

<a id="s01_u03"></a>
あ、そうなんですか。私も初めてなんです。料理はよくされるんですか。

À, vậy ạ. Tôi cũng lần đầu. Anh/chị có hay nấu ăn không?

Trong skit B27, câu mở là hỏi chỗ ngồi. Sau đó mới đến môn học, năm học và tên. Tên không nhất thiết là câu đầu tiên. Với người chưa thân, giữ です・ます tới khi hai bên tự chuyển giọng. Được ngồi cạnh không đồng nghĩa người kia có thời gian nói dài.


## Mạch làm quen ở lớp: từ chỗ ngồi đến lời rủ [kn27]

# Một cuộc làm quen thật có nhiều bước

Skit ① của bài 出会い đặt hai sinh viên mới gặp trong lớp. Người mở chuyện xin ngồi cạnh, hỏi ngay về môn họ cùng học, tự nói mình cũng học năm nhất kinh tế sau khi nghe câu trả lời, rồi hai bên trao tên. Lời rủ ăn trưa đến sau khi đã có điểm chung và chỉ là một đề nghị nhẹ. Một lời từ chối vẫn phải được tôn trọng; nguồn này là nhánh nhận lời.

Lời Nhật giữ nguyên trong bài shadowing kế tiếp. Chú ý 「名前聞いてもいい？」 (mình hỏi tên cậu được không?) thân mật lên sau khi hai người đã tìm được điểm chung; với người lớn tuổi hoặc người lạ chưa thân, nói lịch sự hơn. 「なんか」 (kiểu như), 「そーお」 (vậy à) là lời nói tự nhiên trong script, để nhận diện khi nghe, không bắt chước trong mọi quan hệ.

Trong chặng, hãy tự tạo nhánh khác khi người kia không muốn ăn cùng hoặc chưa muốn cho cách liên lạc. Đừng mặc định cuộc gặp nào cũng tiến nhanh như skit nguồn.


## Hội thoại gốc: gặp người mới ở lớp [sh27]

{
  "id": "sh27",
  "source_refs": [
    "srcB27"
  ],
  "knowledge_ids": [
    "kn27"
  ],
  "items": [
    {
      "id": "skit1",
      "kind": "dialogue",
      "example_id": "b27_01",
      "speakers": [
        {
          "id": "A",
          "role": "Sinh viên cùng lớp"
        },
        {
          "id": "B",
          "role": "Sinh viên cùng lớp"
        }
      ],
      "turns": [
        {
          "id": "sh27--skit1--t01",
          "speaker": "A",
          "ja": "となり、空いてますか。",
          "vi": "Chỗ bên cạnh có ai ngồi chưa?"
        },
        {
          "id": "sh27--skit1--t02",
          "speaker": "B",
          "ja": "あ、はい。",
          "vi": "À, chưa."
        },
        {
          "id": "sh27--skit1--t03",
          "speaker": "A",
          "ja": "ありがとう。あのー、この授業、難しいとか、何か知ってます？",
          "vi": "Cảm ơn. À, cậu biết môn học này có khó không hay biết gì về nó không?"
        },
        {
          "id": "sh27--skit1--t04",
          "speaker": "B",
          "ja": "あ、なんか先輩がおもしろいから取ったほうがいいよって言ってたんで、来てみたんですけど。",
          "vi": "À, anh chị khóa trên bảo môn này thú vị và nên học, nên mình đến thử xem."
        },
        {
          "id": "sh27--skit1--t05",
          "speaker": "A",
          "ja": "そうなんですか。よかった。あ、何年生ですか。",
          "vi": "Vậy à, tốt quá. À, cậu học năm mấy?"
        },
        {
          "id": "sh27--skit1--t06",
          "speaker": "B",
          "ja": "経済の１年です。",
          "vi": "Mình là sinh viên năm nhất khoa kinh tế."
        },
        {
          "id": "sh27--skit1--t07",
          "speaker": "A",
          "ja": "あ、いっしょいっしょ。私も経済の１年。",
          "vi": "À, giống nhau rồi. Mình cũng là năm nhất khoa kinh tế."
        },
        {
          "id": "sh27--skit1--t08",
          "speaker": "B",
          "ja": "ほんとですか。名前聞いてもいい？",
          "vi": "Thật à? Mình hỏi tên cậu được không?"
        },
        {
          "id": "sh27--skit1--t09",
          "speaker": "A",
          "ja": "山下恵子です。",
          "vi": "Mình là Yamashita Keiko."
        },
        {
          "id": "sh27--skit1--t10",
          "speaker": "B",
          "ja": "山下さん。あ、私、橋本みどりって言います。",
          "vi": "Yamashita nhỉ. À, mình tên là Hashimoto Midori."
        },
        {
          "id": "sh27--skit1--t11",
          "speaker": "A",
          "ja": "よろしく。あ、そうだ、この後、誰かとお昼食べる約束してる？",
          "vi": "Rất vui được biết cậu. À phải rồi, sau giờ này cậu có hẹn ăn trưa với ai không?"
        },
        {
          "id": "sh27--skit1--t12",
          "speaker": "B",
          "ja": "いや、特に。お弁当持ってきてるんで。",
          "vi": "Không, không hẹn ai cả. Mình có mang cơm hộp."
        },
        {
          "id": "sh27--skit1--t13",
          "speaker": "A",
          "ja": "あ、そーお？ じゃ、一緒に食べない？ 私もパン買ってきてるから。",
          "vi": "Vậy à? Thế ăn cùng mình nhé? Mình cũng mua bánh mì rồi."
        },
        {
          "id": "sh27--skit1--t14",
          "speaker": "B",
          "ja": "ああ、じゃ。",
          "vi": "Ừ, thế nhé."
        }
      ],
      "authorship": "source_quote"
    }
  ]
}



## Phản hồi điều vừa nghe: へー và ああ [k70]

# Phản hồi khi nghe một điều mới

Trong bài 70, lời người kia mở ra tin mới: sắp chuyển khỏi ký túc xá để ở riêng. Lời đáp 「へー」 cho thấy thông tin làm mình chú ý; 「ああ」 thường báo rằng giờ mình đã hiểu lý do. Chỉ đáp 「そうですか」 (ra vậy ạ) rồi chuyển câu hỏi có thể khô; phản hồi ngắn trước, sau đó mới hỏi vào điều họ vừa kể.

## Hội thoại mở đầu và cách lịch sự hơn

<a id="b70_01"></a>
来月、寮を出て、一人暮らしを始めることにしたんです。

Tháng tới tôi đã quyết định rời ký túc xá và bắt đầu sống một mình.

<a id="b70_02"></a>
へー、そうなんだ。

Ồ, ra vậy.

Sách đối chiếu cách nói lịch sự hơn:

<a id="b70_03"></a>
へー、そうなのですね

Ồ, ra là thế ạ.

Không đem 「へー、そうなんだ」 (ồ, ra vậy) vào mọi cuộc gặp mới: giọng thân mật có thể quá gần. Với người mới gặp, 「そうなんですか」 (vậy ạ), 「ああ、そうだったんですか」 (à, ra là thế ạ) an toàn hơn. 「へー」 kéo dài không đúng chỗ cũng dễ thành phản ứng thiếu nghiêm túc.

## Ba cặp tình huống của bài nguồn

**Điều làm mình ngạc nhiên vì chưa biết:**

<a id="b70_04"></a>
ここは昔、海だったんだよ。

Xưa kia chỗ này từng là biển đấy.

<a id="b70_05"></a>
へー、知らなかった。

Ồ, tớ không biết.

**Hiểu vì sao người kia đã về trước:**

<a id="b70_06"></a>
あの日は体調が悪くて、先に帰ったんです。

Hôm ấy tôi không khỏe nên về trước.

<a id="b70_07"></a>
ああ、そうだったんですか。

À, ra là vậy ạ.

**Nhận xét một thay đổi được mời góp ý:**

<a id="b70_08"></a>
ここの色を変えてみたんだけど、どう？

Tớ thử đổi màu chỗ này, cậu thấy sao?

<a id="b70_09"></a>
ああ、いいと思いますよ。

À, tôi thấy được đấy.

Bài nguồn đi từ tin mới → lời giải thích → lời xin ý kiến. Với người lạ, đáp một nhịp rồi hỏi một câu nối đúng chi tiết, đừng bắn liên tiếp câu hỏi riêng tư. Ví dụ ứng dụng mới của chặng nằm ở các hội thoại lớp học và sự kiện sau bài luyện gốc.


## Luyện nguyên bài nguồn — Phản hồi điều vừa nghe: へー và ああ [sh70]

{
  "id": "sh70",
  "source_refs": [
    "srcB11"
  ],
  "knowledge_ids": [
    "k70"
  ],
  "items": [
    {
      "id": "sh70_01",
      "kind": "sentence",
      "example_id": "b70_01",
      "ja": "来月、寮を出て、一人暮らしを始めることにしたんです。",
      "vi": "Tháng tới tôi đã quyết định rời ký túc xá và bắt đầu sống một mình.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_02",
      "kind": "sentence",
      "example_id": "b70_02",
      "ja": "へー、そうなんだ。",
      "vi": "Ồ, ra vậy.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_03",
      "kind": "sentence",
      "example_id": "b70_03",
      "ja": "へー、そうなのですね",
      "vi": "Ồ, ra là thế ạ.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_04",
      "kind": "sentence",
      "example_id": "b70_04",
      "ja": "ここは昔、海だったんだよ。",
      "vi": "Xưa kia chỗ này từng là biển đấy.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_05",
      "kind": "sentence",
      "example_id": "b70_05",
      "ja": "へー、知らなかった。",
      "vi": "Ồ, tớ không biết.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_06",
      "kind": "sentence",
      "example_id": "b70_06",
      "ja": "あの日は体調が悪くて、先に帰ったんです。",
      "vi": "Hôm ấy tôi không khỏe nên về trước.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_07",
      "kind": "sentence",
      "example_id": "b70_07",
      "ja": "ああ、そうだったんですか。",
      "vi": "À, ra là vậy ạ.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_08",
      "kind": "sentence",
      "example_id": "b70_08",
      "ja": "ここの色を変えてみたんだけど、どう？",
      "vi": "Tớ thử đổi màu chỗ này, cậu thấy sao?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh70_09",
      "kind": "sentence",
      "example_id": "b70_09",
      "ja": "ああ、いいと思いますよ。",
      "vi": "À, tôi thấy được đấy.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    }
  ]
}



## Từ phản hồi và nối chuyện [v_turn]

{
  "id": "v_turn",
  "source_refs": [],
  "items": [
    {
      "id": "v_turn-w-5332a6eb33fc",
      "ja": "きっかけ",
      "source_refs": []
    },
    {
      "id": "v_turn-w-f751bed20659",
      "ja": "続ける",
      "source_refs": []
    },
    {
      "id": "v_turn-w-2c01205b05f1",
      "ja": "選ぶ",
      "source_refs": []
    },
    {
      "id": "v_turn-w-4e7195698ce6",
      "ja": "気に入る",
      "source_refs": []
    },
    {
      "id": "v_turn-w-2f714a0fdaef",
      "ja": "気づく",
      "source_refs": []
    },
    {
      "id": "v_turn-w-cefca9281425",
      "ja": "覚える",
      "source_refs": []
    },
    {
      "id": "v_turn-w-7aab9166a665",
      "ja": "比べる",
      "source_refs": []
    },
    {
      "id": "v_turn-w-51313fc4dd42",
      "ja": "取り違える",
      "source_refs": []
    },
    {
      "id": "v_turn-w-55d50f53ea2d",
      "ja": "新鮮",
      "source_refs": []
    },
    {
      "id": "v_turn-w-3e5d2eea56a1",
      "ja": "詳しい",
      "source_refs": []
    }
  ]
}



## Phản hồi, hỏi tiếp và tự chia sẻ cân xứng [k_recip]

# Để lời nói đi hai chiều

Một vòng tự nhiên: nghe một chi tiết → phản hồi đúng cảm xúc → hỏi thêm một điểm → kể một mẩu tương xứng về mình. Hỏi liên tiếp mà không tự nói gì dễ thành một cuộc phỏng vấn.

<a id="s02_u02"></a>
春からです。最初は一回だけのつもりだったんですけど。

Từ mùa xuân. Ban đầu tôi chỉ định đến một lần thôi.

<a id="s02_u03"></a>
へえ、そうなんですか。それで、続けようと思ったきっかけは何ですか。

Ồ, vậy ạ. Rồi điều gì khiến anh/chị muốn tiếp tục?

<a id="s02_u05"></a>
それはいいですね。私も、いつも同じ作家ばかり読んでしまうので。

Hay thật. Tôi cũng hay chỉ đọc mãi một tác giả.

B11 bài 70 dùng 「へー」 báo ngạc nhiên và 「ああ」 báo đã hiểu. Bài 73 đưa 「で」 nối diễn biến. Khi mới gặp, câu hỏi đầy đủ lịch sự thường dễ nghe hơn một tiếng 「で？」 (rồi sao?). Với chuyện không vui, nhận cảm xúc trước khi hỏi; không phản hồi hào hứng khi người kia vừa kể bệnh hay thất bại.

Tự chia sẻ cho người kia có chỗ hỏi lại. Trong s03, người học nói muốn học vẽ rồi hỏi đối phương muốn vẽ gì. Nếu họ đáp ngắn, dừng đúng điểm ấy; câu trả lời ngắn có thể vì họ bận.


## Hỏi tiếp diễn biến: で và それで [k73]

# Hỏi tiếp để cuộc kể có đường đi

Bài 73 dùng 「で」 như dạng ngắn của 「それで」. Khi người kia đang kể một diễn biến còn dang dở, 「で、どうなったの？」 (rồi chuyện thế nào?) mời họ kể kết quả. Sách cũng cho thấy 「で、いつにします？」 (vậy chọn khi nào?) chuyển sang chuyện sắp xếp tiếp theo; đó là một chức năng khác với hỏi kết cục. Hãy nghe xem người kia còn muốn kể hay đã muốn đổi việc.

## Hội thoại mở đầu và câu đối chiếu

<a id="b73_01"></a>
で、結局、どうなったの？

Rồi cuối cùng thế nào?

<a id="b73_02"></a>
中止になったよ。

Bị hủy rồi.

Cách hỏi lịch sự được sách đối chiếu:

<a id="b73_03"></a>
それで、どうなりましたか

Rồi chuyện gì xảy ra ạ?

Với người mới gặp, dùng 「それで、どうなりましたか」 (rồi chuyện gì xảy ra ạ?) hoặc một câu hỏi gắn chi tiết vừa nghe, tránh một chữ 「で？」 (rồi sao?) nghe như thúc giục. Sau chuyện không vui, một câu thấu hiểu có thể cần trước câu hỏi.

## A. Hỏi tiếp câu chuyện

<a id="b73_04"></a>
で、どうしたんですか。

Rồi anh/chị đã làm sao ạ?

<a id="b73_05"></a>
しょうがないから、遅れて行きました。

Không còn cách nào nên tôi đến muộn.

<a id="b73_06"></a>
で、大丈夫だったんですか。

Rồi mọi chuyện có ổn không ạ?

<a id="b73_07"></a>
ええ。なんとか無事に着きました。

Vâng, cuối cùng cũng đến nơi an toàn.

## B. Chuyển sang bước kế

<a id="b73_08"></a>
で、いつにします？

Vậy chọn khi nào?

<a id="b73_09"></a>
早いほうがいいですね。

Càng sớm càng tốt nhỉ.

Hai cặp đầu hỏi chuyện sau sự cố và kết quả an toàn; cặp cuối chốt thời điểm. Trong cuộc làm quen của chặng này, dùng đúng chức năng: người kia kể đi buổi đầu rồi, có thể hỏi buổi ấy ra sao; nếu họ đã muốn rời đi thì chốt dịp gặp lại mà không ép.


## Luyện nguyên bài nguồn — Hỏi tiếp diễn biến: で và それで [sh73]

{
  "id": "sh73",
  "source_refs": [
    "srcB11"
  ],
  "knowledge_ids": [
    "k73"
  ],
  "items": [
    {
      "id": "sh73_01",
      "kind": "sentence",
      "example_id": "b73_01",
      "ja": "で、結局、どうなったの？",
      "vi": "Rồi cuối cùng thế nào?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_02",
      "kind": "sentence",
      "example_id": "b73_02",
      "ja": "中止になったよ。",
      "vi": "Bị hủy rồi.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_03",
      "kind": "sentence",
      "example_id": "b73_03",
      "ja": "それで、どうなりましたか",
      "vi": "Rồi chuyện gì xảy ra ạ?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_04",
      "kind": "sentence",
      "example_id": "b73_04",
      "ja": "で、どうしたんですか。",
      "vi": "Rồi anh/chị đã làm sao ạ?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_05",
      "kind": "sentence",
      "example_id": "b73_05",
      "ja": "しょうがないから、遅れて行きました。",
      "vi": "Không còn cách nào nên tôi đến muộn.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_06",
      "kind": "sentence",
      "example_id": "b73_06",
      "ja": "で、大丈夫だったんですか。",
      "vi": "Rồi mọi chuyện có ổn không ạ?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_07",
      "kind": "sentence",
      "example_id": "b73_07",
      "ja": "ええ。なんとか無事に着きました。",
      "vi": "Vâng, cuối cùng cũng đến nơi an toàn.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_08",
      "kind": "sentence",
      "example_id": "b73_08",
      "ja": "で、いつにします？",
      "vi": "Vậy chọn khi nào?",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    },
    {
      "id": "sh73_09",
      "kind": "sentence",
      "example_id": "b73_09",
      "ja": "早いほうがいいですね。",
      "vi": "Càng sớm càng tốt nhỉ.",
      "authorship": "source_quote",
      "source_refs": [
        "srcB11"
      ]
    }
  ]
}



## Bắt chuyện từ việc cùng đang làm [s01]

{
  "id": "s01",
  "source_refs": [],
  "title": "Bắt chuyện từ việc cùng đang làm",
  "event_id": "e01",
  "setting": "Trước buổi học nấu ăn, hai người đang đứng trước bàn nguyên liệu.",
  "communication_goal": "Mở lời bằng việc chung, nghe đáp và nói lý do mình đến.",
  "relationship": "Hai học viên lần đầu gặp, dùng です・ます.",
  "outcome": "conversation_opened",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s01--t01",
      "speaker": "A",
      "ja": "すみません、この材料は二人で使うんでしょうか。",
      "vi": "Xin lỗi, nguyên liệu này hai người dùng chung phải không ạ?"
    },
    {
      "id": "s01--t02",
      "speaker": "B",
      "ja": "そうみたいです。私も今日が初めてで、まだよく分からなくて。",
      "vi": "Có vẻ vậy. Hôm nay tôi cũng lần đầu đến, vẫn chưa rõ lắm."
    },
    {
      "id": "s01--t03",
      "speaker": "A",
      "ja": "あ、そうなんですか。私も初めてなんです。料理はよくされるんですか。",
      "vi": "À, vậy ạ. Tôi cũng lần đầu. Anh/chị có hay nấu ăn không?"
    },
    {
      "id": "s01--t04",
      "speaker": "B",
      "ja": "家では簡単なものだけです。ここで少し習ってみたくて。",
      "vi": "Ở nhà tôi chỉ làm món đơn giản. Tôi muốn đến đây học thử một chút."
    },
    {
      "id": "s01--t05",
      "speaker": "A",
      "ja": "私も同じです。今日は何を作るのか楽しみですね。",
      "vi": "Tôi cũng vậy. Mong xem hôm nay mình sẽ làm món gì nhỉ."
    },
    {
      "id": "s01--t06",
      "speaker": "B",
      "ja": "ええ。分からないところがあったら、一緒に聞きましょう。",
      "vi": "Vâng. Nếu có chỗ nào chưa rõ, ta cùng hỏi nhé."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi về thời điểm tham gia và hỏi tiếp một chi tiết [s02]

{
  "id": "s02",
  "source_refs": [],
  "title": "Hỏi về thời điểm tham gia và hỏi tiếp một chi tiết",
  "event_id": "e01",
  "setting": "Trong nhóm đọc sách, người học nói chuyện với thành viên đã tới trước.",
  "communication_goal": "Hỏi từ khi nào họ tham gia và vì sao họ tiếp tục đến.",
  "relationship": "Người mới và thành viên cùng nhóm, lịch sự vừa phải.",
  "outcome": "shared_motivation",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s02--t01",
      "speaker": "A",
      "ja": "この読書会には、いつごろから参加されているんですか。",
      "vi": "Anh/chị tham gia nhóm đọc sách này từ khoảng khi nào ạ?"
    },
    {
      "id": "s02--t02",
      "speaker": "B",
      "ja": "春からです。最初は一回だけのつもりだったんですけど。",
      "vi": "Từ mùa xuân. Ban đầu tôi chỉ định đến một lần thôi."
    },
    {
      "id": "s02--t03",
      "speaker": "A",
      "ja": "へえ、そうなんですか。それで、続けようと思ったきっかけは何ですか。",
      "vi": "Ồ, vậy ạ. Rồi điều gì khiến anh/chị muốn tiếp tục?"
    },
    {
      "id": "s02--t04",
      "speaker": "B",
      "ja": "自分では選ばない本を読めるのが面白くて。",
      "vi": "Tôi thấy thú vị vì được đọc những cuốn tự mình sẽ không chọn."
    },
    {
      "id": "s02--t05",
      "speaker": "A",
      "ja": "それはいいですね。私も、いつも同じ作家ばかり読んでしまうので。",
      "vi": "Hay thật. Tôi cũng hay chỉ đọc mãi một tác giả."
    },
    {
      "id": "s02--t06",
      "speaker": "B",
      "ja": "じゃ、今日の本について、後で感想を聞かせてください。",
      "vi": "Vậy lát nữa cho tôi nghe cảm nhận về cuốn hôm nay nhé."
    }
  ],
  "authorship": "original_extension"
}



## Kể lý do mình đến và nhường câu hỏi lại [s03]

{
  "id": "s03",
  "source_refs": [],
  "title": "Kể lý do mình đến và nhường câu hỏi lại",
  "event_id": "e01",
  "setting": "Trong buổi luyện vẽ, người kia hỏi tại sao người học đăng ký.",
  "communication_goal": "Kể vừa đủ về mình rồi hỏi lại, tránh độc thoại.",
  "relationship": "Hai học viên mới quen.",
  "outcome": "reciprocal_exchange",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s03--t01",
      "speaker": "B",
      "ja": "どうしてこの講座に来ようと思ったんですか。",
      "vi": "Vì sao anh/chị muốn đến khóa học này?"
    },
    {
      "id": "s03--t02",
      "speaker": "A",
      "ja": "最近、散歩中に見た景色を描いてみたくなったんです。でも、一人だと続かなくて。",
      "vi": "Gần đây tôi muốn thử vẽ cảnh nhìn thấy lúc đi dạo. Nhưng làm một mình thì khó duy trì."
    },
    {
      "id": "s03--t03",
      "speaker": "B",
      "ja": "ああ、分かります。私も道具だけ買って、そのままでした。",
      "vi": "À, tôi hiểu. Tôi cũng mua dụng cụ rồi để nguyên đó."
    },
    {
      "id": "s03--t04",
      "speaker": "A",
      "ja": "そうだったんですか。今日は何か描きたいものがあるんですか。",
      "vi": "Vậy ạ. Hôm nay anh/chị muốn vẽ thứ gì không?"
    },
    {
      "id": "s03--t05",
      "speaker": "B",
      "ja": "近所の川です。季節で色が変わるのが好きで。",
      "vi": "Con sông gần nhà. Tôi thích màu sắc thay đổi theo mùa."
    },
    {
      "id": "s03--t06",
      "speaker": "A",
      "ja": "いいですね。あとで絵を見せていただいてもいいですか。",
      "vi": "Hay quá. Lát nữa tôi có thể xem tranh của anh/chị không?"
    },
    {
      "id": "s03--t07",
      "speaker": "B",
      "ja": "もちろん。よかったら、描いた絵を見せてくださいね。",
      "vi": "Tất nhiên. Nếu tiện, anh/chị cũng cho tôi xem tranh đã vẽ nhé."
    }
  ],
  "authorship": "original_extension"
}



## Bị tưởng là người hướng dẫn rồi đính chính [s04]

{
  "id": "s04",
  "source_refs": [],
  "title": "Bị tưởng là người hướng dẫn rồi đính chính",
  "event_id": "e01",
  "setting": "Người mới bước vào lớp và hỏi người học như thể họ là người phụ trách.",
  "communication_goal": "Đính chính nhẹ, vẫn giúp họ tìm thông tin.",
  "relationship": "Hai học viên mới gặp.",
  "outcome": "role_clarified",
  "follows": [],
  "alternative_to": [
    "s01"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s04--t01",
      "speaker": "B",
      "ja": "すみません、今日の先生ですか。受付はどこでしょう。",
      "vi": "Xin lỗi, anh/chị là giáo viên hôm nay ạ? Quầy tiếp nhận ở đâu?"
    },
    {
      "id": "s04--t02",
      "speaker": "A",
      "ja": "いえ、私も参加者なんです。受付を探しているんです。",
      "vi": "Không, tôi cũng là người tham gia. Tôi cũng đang tìm quầy tiếp nhận."
    },
    {
      "id": "s04--t03",
      "speaker": "B",
      "ja": "あ、失礼しました。慣れているように見えたので。",
      "vi": "À, xin lỗi. Vì trông anh/chị có vẻ quen nơi này."
    },
    {
      "id": "s04--t04",
      "speaker": "A",
      "ja": "実は私も初めてです。受付なら、あの案内の隣かもしれません。",
      "vi": "Thật ra tôi cũng lần đầu đến. Quầy tiếp nhận có lẽ ở cạnh bảng hướng dẫn kia."
    },
    {
      "id": "s04--t05",
      "speaker": "B",
      "ja": "ありがとうございます。一緒に行ってみますか。",
      "vi": "Cảm ơn. Ta cùng đến xem nhé?"
    },
    {
      "id": "s04--t06",
      "speaker": "A",
      "ja": "そうしましょう。私も場所を確かめたかったんです。",
      "vi": "Vâng, cùng đi. Tôi cũng muốn xác nhận chỗ đó."
    }
  ],
  "authorship": "original_extension"
}



## Sau khi đính chính, trao tên và hẹn ở buổi nhóm sau [s05]

{
  "id": "s05",
  "source_refs": [],
  "title": "Sau khi đính chính, trao tên và hẹn ở buổi nhóm sau",
  "event_id": "e01",
  "setting": "Hai người đã tìm được quầy tiếp nhận và chuẩn bị vào lớp.",
  "communication_goal": "Trao tên và mở khả năng gặp lại không tạo cam kết nặng.",
  "relationship": "Hai học viên vừa gặp ở s04.",
  "outcome": "next_meeting_possible",
  "follows": [
    "s04"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s05--t01",
      "speaker": "A",
      "ja": "無事に受付が見つかってよかったですね。私はリンといいます。",
      "vi": "May quá tìm được quầy tiếp nhận. Tôi tên là Linh."
    },
    {
      "id": "s05--t02",
      "speaker": "B",
      "ja": "助かりました。私は佐藤です。さっきは勘違いしてすみません。",
      "vi": "Anh/chị giúp tôi nhiều quá. Tôi là Satō. Lúc nãy tôi hiểu nhầm, xin lỗi nhé."
    },
    {
      "id": "s05--t03",
      "speaker": "A",
      "ja": "気にしないでください。来週も参加されますか。",
      "vi": "Đừng bận tâm. Tuần sau anh/chị cũng tham gia chứ?"
    },
    {
      "id": "s05--t04",
      "speaker": "B",
      "ja": "仕事次第ですが、来られたらまたお話ししたいです。",
      "vi": "Còn tùy công việc, nhưng nếu đến được tôi muốn nói chuyện tiếp."
    },
    {
      "id": "s05--t05",
      "speaker": "A",
      "ja": "私もです。来週、会えたらよろしくお願いします。",
      "vi": "Tôi cũng vậy. Nếu gặp tuần sau, mong được trò chuyện tiếp."
    },
    {
      "id": "s05--t06",
      "speaker": "B",
      "ja": "はい、またそのときに。",
      "vi": "Vâng, hẹn khi ấy."
    }
  ],
  "authorship": "original_extension"
}



## Mở chuyện ở sự kiện bằng kinh nghiệm tham dự [s06]

{
  "id": "s06",
  "source_refs": [],
  "title": "Mở chuyện ở sự kiện bằng kinh nghiệm tham dự",
  "event_id": "e02",
  "setting": "Ở lễ hội khu phố, hai người đứng chờ xem tiết mục.",
  "communication_goal": "Hỏi họ đã từng dự chưa và chia sẻ trải nghiệm của mình.",
  "relationship": "Hai khách tham dự chưa biết nhau.",
  "outcome": "event_talk_started",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s06--t01",
      "speaker": "A",
      "ja": "このお祭りには、前にも来たことがありますか。",
      "vi": "Anh/chị đã từng đến lễ hội này chưa?"
    },
    {
      "id": "s06--t02",
      "speaker": "B",
      "ja": "去年、一度だけ来ました。あのときは雨で、途中で帰ったんです。",
      "vi": "Năm ngoái tôi đến một lần. Hôm đó trời mưa nên tôi về giữa chừng."
    },
    {
      "id": "s06--t03",
      "speaker": "A",
      "ja": "そうだったんですか。今年は晴れてよかったですね。私は今日が初めてです。",
      "vi": "Vậy à. Năm nay trời quang thật may. Tôi thì hôm nay lần đầu tới."
    },
    {
      "id": "s06--t04",
      "speaker": "B",
      "ja": "それなら、この後の太鼓もおすすめですよ。",
      "vi": "Nếu vậy, tiết mục trống lát nữa cũng đáng xem đấy."
    },
    {
      "id": "s06--t05",
      "speaker": "A",
      "ja": "へえ、そうなんですね。どの辺りから見ると見やすいですか。",
      "vi": "Ồ, vậy ạ. Đứng chỗ nào thì dễ xem?"
    },
    {
      "id": "s06--t06",
      "speaker": "B",
      "ja": "向こうの木の近くなら、全体が見えますよ。",
      "vi": "Gần cái cây phía kia thì nhìn được toàn cảnh."
    }
  ],
  "authorship": "original_extension"
}



## Từ nhận xét hiện tại đến cảm nhận của người kia [s07]

{
  "id": "s07",
  "source_refs": [],
  "title": "Từ nhận xét hiện tại đến cảm nhận của người kia",
  "event_id": "e02",
  "setting": "Hai người vừa xem phần giới thiệu của buổi triển lãm cộng đồng.",
  "communication_goal": "Nêu một nhận xét cụ thể rồi mời cảm nhận khác.",
  "relationship": "Khách xem triển lãm mới gặp.",
  "outcome": "views_exchanged",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s07--t01",
      "speaker": "A",
      "ja": "さっきの写真、同じ通りでも季節で雰囲気が違いましたね。",
      "vi": "Những bức ảnh vừa rồi cho thấy cùng một con phố mà không khí khác theo mùa nhỉ."
    },
    {
      "id": "s07--t02",
      "speaker": "B",
      "ja": "そうですね。私は冬の写真が印象に残りました。",
      "vi": "Đúng vậy. Với tôi, ảnh mùa đông gây ấn tượng nhất."
    },
    {
      "id": "s07--t03",
      "speaker": "A",
      "ja": "ああ、雪が少し積もっていた写真ですか。どんなところがよかったですか。",
      "vi": "À, bức có tuyết phủ mỏng phải không ạ? Anh/chị thích điểm nào?"
    },
    {
      "id": "s07--t04",
      "speaker": "B",
      "ja": "人が少なくて、静かな感じがしたんです。",
      "vi": "Ít người nên tôi thấy một cảm giác yên tĩnh."
    },
    {
      "id": "s07--t05",
      "speaker": "A",
      "ja": "なるほど。私は夏のにぎやかな写真が好きでした。見方が違うと面白いですね。",
      "vi": "Ra vậy. Tôi lại thích bức mùa hè đông vui. Góc nhìn khác nhau thật thú vị."
    },
    {
      "id": "s07--t06",
      "speaker": "B",
      "ja": "ええ。隣の部屋にも同じ通りの絵があるそうですよ。",
      "vi": "Vâng. Nghe nói phòng bên cạnh còn có tranh vẽ cùng con phố ấy."
    }
  ],
  "authorship": "original_extension"
}



## Người kia đang chờ bạn, nhường họ đi [s08]

{
  "id": "s08",
  "source_refs": [],
  "title": "Người kia đang chờ bạn, nhường họ đi",
  "event_id": "e02",
  "setting": "Người đối thoại nhìn về lối vào và nói đang đợi bạn.",
  "communication_goal": "Nhận tín hiệu bận, kết thúc ngắn mà vẫn thân thiện.",
  "relationship": "Hai người vừa nói vài câu ở sự kiện.",
  "outcome": "respectful_pause",
  "follows": [
    "s07"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s08--t01",
      "speaker": "B",
      "ja": "すみません、友人がもうすぐ来るので、入口を見ていないと。",
      "vi": "Xin lỗi, bạn tôi sắp đến nên tôi phải để mắt tới lối vào."
    },
    {
      "id": "s08--t02",
      "speaker": "A",
      "ja": "あ、そうでしたか。引き止めてしまってすみません。",
      "vi": "À, ra vậy. Xin lỗi vì tôi đã giữ anh/chị lại."
    },
    {
      "id": "s08--t03",
      "speaker": "B",
      "ja": "いえいえ。お話できて楽しかったです。",
      "vi": "Không đâu. Rất vui được nói chuyện."
    },
    {
      "id": "s08--t04",
      "speaker": "A",
      "ja": "私もです。どうぞお友達を迎えに行ってください。",
      "vi": "Tôi cũng vậy. Anh/chị cứ đi đón bạn nhé."
    },
    {
      "id": "s08--t05",
      "speaker": "B",
      "ja": "ありがとうございます。展示も楽しんでください。",
      "vi": "Cảm ơn. Anh/chị tiếp tục xem triển lãm vui nhé."
    },
    {
      "id": "s08--t06",
      "speaker": "A",
      "ja": "はい。では、またどこかで。",
      "vi": "Vâng. Vậy hẹn gặp dịp khác."
    }
  ],
  "authorship": "original_extension"
}



## Người kia chỉ muốn xem yên tĩnh, khép lời [s09]

{
  "id": "s09",
  "source_refs": [],
  "title": "Người kia chỉ muốn xem yên tĩnh, khép lời",
  "event_id": "e02",
  "setting": "Người học thử hỏi cảm nhận ở một gian triển lãm yên tĩnh.",
  "communication_goal": "Chấp nhận lời từ chối trò chuyện không dò lý do.",
  "relationship": "Hai khách lạ.",
  "outcome": "declined_respected",
  "follows": [],
  "alternative_to": [
    "s07"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s09--t01",
      "speaker": "A",
      "ja": "この作品、面白いですね。よくこちらにいらっしゃるんですか。",
      "vi": "Tác phẩm này thú vị nhỉ. Anh/chị hay đến đây không?"
    },
    {
      "id": "s09--t02",
      "speaker": "B",
      "ja": "すみません。今日は一人で静かに見たいので。",
      "vi": "Xin lỗi. Hôm nay tôi muốn xem một mình trong yên tĩnh."
    },
    {
      "id": "s09--t03",
      "speaker": "A",
      "ja": "あ、失礼しました。お邪魔しました。",
      "vi": "À, xin lỗi. Tôi đã làm phiền rồi."
    },
    {
      "id": "s09--t04",
      "speaker": "B",
      "ja": "いえ。",
      "vi": "Không sao."
    },
    {
      "id": "s09--t05",
      "speaker": "A",
      "ja": "どうぞ、ごゆっくり。",
      "vi": "Mời anh/chị cứ xem thong thả."
    }
  ],
  "authorship": "original_extension"
}



## Gặp lại ở gian khác và nhắc một điểm chung [s10]

{
  "id": "s10",
  "source_refs": [],
  "title": "Gặp lại ở gian khác và nhắc một điểm chung",
  "event_id": "e02",
  "setting": "Sau cuộc nói ở s07, hai người tình cờ gặp lại trước tranh về cùng con phố.",
  "communication_goal": "Nối lại bằng chi tiết người kia đã nói, không giới thiệu lại từ đầu.",
  "relationship": "Hai khách vừa trò chuyện ở triển lãm.",
  "outcome": "conversation_resumed",
  "follows": [
    "s07"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s10--t01",
      "speaker": "A",
      "ja": "あ、さっき冬の写真がお好きだとおっしゃっていましたよね。こちらの絵も冬ですね。",
      "vi": "À, lúc nãy anh/chị nói thích ảnh mùa đông nhỉ. Bức tranh này cũng là mùa đông."
    },
    {
      "id": "s10--t02",
      "speaker": "B",
      "ja": "覚えていてくださったんですね。これも静かな雰囲気で好きです。",
      "vi": "Anh/chị còn nhớ à. Tôi cũng thích vẻ yên tĩnh của bức này."
    },
    {
      "id": "s10--t03",
      "speaker": "A",
      "ja": "写真と比べると、色は少し暖かく感じます。どう思われますか。",
      "vi": "So với ảnh, tôi thấy màu sắc ấm hơn một chút. Anh/chị nghĩ sao?"
    },
    {
      "id": "s10--t04",
      "speaker": "B",
      "ja": "確かに。雪だけでなく、家の明かりも描いてあるからかもしれません。",
      "vi": "Đúng vậy. Có lẽ vì họa sĩ vẽ cả ánh đèn trong nhà bên cạnh tuyết."
    },
    {
      "id": "s10--t05",
      "speaker": "A",
      "ja": "ああ、そこは気づきませんでした。教えてくださってありがとうございます。",
      "vi": "À, tôi không để ý chỗ ấy. Cảm ơn anh/chị đã chỉ cho tôi."
    },
    {
      "id": "s10--t06",
      "speaker": "B",
      "ja": "こちらこそ。また違う見方ができました。",
      "vi": "Tôi cũng cảm ơn. Nhờ vậy tôi có thêm cách nhìn khác."
    }
  ],
  "authorship": "original_extension"
}



## Từ cho giới hạn và khép lời [v_boundary]

{
  "id": "v_boundary",
  "source_refs": [],
  "items": [
    {
      "id": "v_boundary-w-781c454504b1",
      "ja": "立ち入る",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-2879cbfd3a3d",
      "ja": "個人的",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-30ef46370393",
      "ja": "引き止める",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-fd30cff313eb",
      "ja": "連絡先",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-cc2f84a3cf89",
      "ja": "交換する",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-1b1b5806b28b",
      "ja": "予定",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-880022c6c6e6",
      "ja": "確かめる",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-f673b3e9727f",
      "ja": "親しい",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-8149a2153a58",
      "ja": "無理",
      "source_refs": []
    },
    {
      "id": "v_boundary-w-ce0472659a8b",
      "ja": "決まる",
      "source_refs": []
    }
  ]
}



## Mẫu để gợi ý và giữ khoảng cách [g_follow]

{
  "id": "g_follow",
  "source_refs": [
    "srcGrammar"
  ],
  "items": [
    {
      "id": "g_follow-g-4c35d11f4495",
      "name_ja": "V辞書形／Vない形＋つもりです",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-775b98f5e29e",
      "name_ja": "普通形ので",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-bcb2597d78fc",
      "name_ja": "Nなら",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-4cb34096f58c",
      "name_ja": "Vた／Vない＋ほうがいいです",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-9bef619f7064",
      "name_ja": "普通形＋そうです（伝聞）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-e43c8ceb1aff",
      "name_ja": "V辞書形／Vない形＋ようにしています",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-d7b0b8312fda",
      "name_ja": "尊敬語",
      "jlpt_level": "N3",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-1d7887721d40",
      "name_ja": "形容詞＋そうです（様態）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_follow-g-b48020003f86",
      "name_ja": "Vます形＋やすい／にくい",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Chủ đề riêng tư và cách sửa lời [k_boundary]

# Ranh giới không cần giải thích dài

Quê quán, việc làm và lý do chuyển nhà có thể dễ nói với người này nhưng riêng tư với người khác. Có thể đáp ở mức rộng, nói rõ chưa muốn kể chi tiết rồi chuyển về điều chung. Câu hỏi của người khác không tạo nghĩa vụ khai hết.

<a id="s11_u04"></a>
町の名前は、もう少し仲良くなってからでもいいですか。

Tên thành phố cụ thể, để khi thân hơn tôi kể được không?

<a id="s14_u02"></a>
きっかけは個人的なことなので、今は詳しく話さなくてもいいですか。

Lý do bắt đầu hơi riêng tư, lúc này tôi không kể chi tiết được không?

Nếu mình lỡ hỏi sâu, xin lỗi ngắn và nói người kia không cần trả lời:

<a id="s13_u03"></a>
すみません。立ち入ったことを聞いてしまいました。答えなくて大丈夫です。

Xin lỗi, tôi đã hỏi chuyện quá riêng tư. Anh/chị không cần trả lời đâu.

Sau đó đưa ra chủ đề an toàn đã có trong cuộc gặp và chờ đối phương chọn. Không khẳng định mọi người Nhật đều tránh một chủ đề; phản ứng tùy người và quan hệ. Từ chối trao đổi liên lạc cũng là ranh giới, không phải vấn đề cần thuyết phục.


## Chọn mức kể về nơi mình đến [s11]

{
  "id": "s11",
  "source_refs": [],
  "title": "Chọn mức kể về nơi mình đến",
  "event_id": "e03",
  "setting": "Người mới quen hỏi người học đến từ đâu trong giờ nghỉ.",
  "communication_goal": "Trả lời mức thông tin thoải mái rồi chuyển sang bối cảnh chung.",
  "relationship": "Hai người cùng lớp, chưa thân.",
  "outcome": "boundary_kept",
  "follows": [
    "s05"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s11--t01",
      "speaker": "B",
      "ja": "リンさんは、どちらのご出身なんですか。",
      "vi": "Linh đến từ đâu vậy?"
    },
    {
      "id": "s11--t02",
      "speaker": "A",
      "ja": "ベトナムです。北のほうで育ちました。",
      "vi": "Tôi đến từ Việt Nam, lớn lên ở miền Bắc."
    },
    {
      "id": "s11--t03",
      "speaker": "B",
      "ja": "そうなんですね。どちらの町ですか。",
      "vi": "Vậy à. Thành phố nào vậy?"
    },
    {
      "id": "s11--t04",
      "speaker": "A",
      "ja": "町の名前は、もう少し仲良くなってからでもいいですか。",
      "vi": "Tên thành phố cụ thể, để khi thân hơn tôi kể được không?"
    },
    {
      "id": "s11--t05",
      "speaker": "B",
      "ja": "もちろんです。聞きすぎましたね。",
      "vi": "Tất nhiên. Tôi đã hỏi hơi sâu rồi."
    },
    {
      "id": "s11--t06",
      "speaker": "A",
      "ja": "いえ、大丈夫です。佐藤さんは、この講座をどうやって知ったんですか。",
      "vi": "Không sao đâu. Satō biết đến khóa này bằng cách nào?"
    },
    {
      "id": "s11--t07",
      "speaker": "B",
      "ja": "図書館の掲示板で見つけました。",
      "vi": "Tôi thấy trên bảng thông báo ở thư viện."
    },
    {
      "id": "s11--t08",
      "speaker": "A",
      "ja": "そうなんですね。私も図書館によく行きます。",
      "vi": "Vậy à. Tôi cũng hay đến thư viện."
    }
  ],
  "authorship": "original_extension"
}



## Từ câu hỏi công việc chuyển sang sở thích chung [s12]

{
  "id": "s12",
  "source_refs": [],
  "title": "Từ câu hỏi công việc chuyển sang sở thích chung",
  "event_id": "e03",
  "setting": "Ở giờ giải lao, người kia hỏi người học làm nghề gì.",
  "communication_goal": "Đáp vừa đủ rồi nối sang điều cả hai muốn trao đổi.",
  "relationship": "Hai người mới quen ở nhóm ảnh.",
  "outcome": "topic_shifted",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s12--t01",
      "speaker": "B",
      "ja": "普段は、どんなお仕事をされているんですか。",
      "vi": "Bình thường anh/chị làm công việc gì?"
    },
    {
      "id": "s12--t02",
      "speaker": "A",
      "ja": "人と話すことの多い仕事です。今日は仕事を忘れて写真を楽しみたくて。",
      "vi": "Công việc của tôi là thường xuyên nói chuyện với mọi người. Hôm nay tôi muốn tạm quên việc và thưởng thức ảnh."
    },
    {
      "id": "s12--t03",
      "speaker": "B",
      "ja": "あ、分かります。私も休みの日は別のことをしたいです。",
      "vi": "À, tôi hiểu. Ngày nghỉ tôi cũng muốn làm chuyện khác."
    },
    {
      "id": "s12--t04",
      "speaker": "A",
      "ja": "そうですよね。さっきの川の写真、どこが気に入りましたか。",
      "vi": "Đúng thế nhỉ. Bức ảnh con sông lúc nãy, anh/chị thích điểm nào?"
    },
    {
      "id": "s12--t05",
      "speaker": "B",
      "ja": "光が水に映っているところです。",
      "vi": "Đoạn ánh sáng phản chiếu trên nước."
    },
    {
      "id": "s12--t06",
      "speaker": "A",
      "ja": "私もそこが好きでした。時間帯は朝でしょうか。",
      "vi": "Tôi cũng thích chỗ ấy. Có lẽ được chụp buổi sáng nhỉ."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi sâu quá làm người kia im lặng rồi sửa lời [s13]

{
  "id": "s13",
  "source_refs": [],
  "title": "Hỏi sâu quá làm người kia im lặng rồi sửa lời",
  "event_id": "e03",
  "setting": "Người học hỏi vì sao người kia chuyển thành phố, người kia ngập ngừng.",
  "communication_goal": "Nhận tín hiệu và tự rút câu hỏi, không đòi giải thích.",
  "relationship": "Hai người mới quen trong nhóm.",
  "outcome": "repair_accepted",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s13--t01",
      "speaker": "A",
      "ja": "こちらへ引っ越されたのは、何か理由があったんですか。",
      "vi": "Anh/chị chuyển đến đây vì có lý do gì vậy?"
    },
    {
      "id": "s13--t02",
      "speaker": "B",
      "ja": "えっと……それは、ちょっと。",
      "vi": "Ừm... chuyện đó thì hơi..."
    },
    {
      "id": "s13--t03",
      "speaker": "A",
      "ja": "すみません。立ち入ったことを聞いてしまいました。答えなくて大丈夫です。",
      "vi": "Xin lỗi, tôi đã hỏi chuyện quá riêng tư. Anh/chị không cần trả lời đâu."
    },
    {
      "id": "s13--t04",
      "speaker": "B",
      "ja": "いえ、ありがとうございます。まだ話すほど親しくなくて。",
      "vi": "Không sao, cảm ơn. Chúng ta chưa thân đến mức để nói chuyện đó."
    },
    {
      "id": "s13--t05",
      "speaker": "A",
      "ja": "そうですよね。さっきの講座の話に戻ってもいいですか。",
      "vi": "Đúng vậy. Ta quay lại chuyện khóa học lúc nãy được không?"
    },
    {
      "id": "s13--t06",
      "speaker": "B",
      "ja": "はい。今日の先生の説明、分かりやすかったですね。",
      "vi": "Được chứ. Cách giải thích của giáo viên hôm nay dễ hiểu nhỉ."
    }
  ],
  "authorship": "original_extension"
}



## Người kia hỏi thêm, chọn phần mình muốn kể [s14]

{
  "id": "s14",
  "source_refs": [],
  "title": "Người kia hỏi thêm, chọn phần mình muốn kể",
  "event_id": "e03",
  "setting": "Người mới quen muốn biết vì sao người học bắt đầu tham gia hoạt động cộng đồng.",
  "communication_goal": "Giữ giới hạn của mình mà vẫn nuôi trao đổi hai chiều.",
  "relationship": "Hai thành viên mới cùng hoạt động.",
  "outcome": "partial_disclosure",
  "follows": [],
  "alternative_to": [
    "s13"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s14--t01",
      "speaker": "B",
      "ja": "どうして急にこの活動を始めたんですか。何かあったんですか。",
      "vi": "Sao anh/chị đột nhiên bắt đầu hoạt động này? Có chuyện gì à?"
    },
    {
      "id": "s14--t02",
      "speaker": "A",
      "ja": "きっかけは個人的なことなので、今は詳しく話さなくてもいいですか。",
      "vi": "Lý do bắt đầu hơi riêng tư, lúc này tôi không kể chi tiết được không?"
    },
    {
      "id": "s14--t03",
      "speaker": "B",
      "ja": "もちろんです。つい聞きすぎてしまいました。",
      "vi": "Tất nhiên. Tôi lỡ hỏi nhiều quá."
    },
    {
      "id": "s14--t04",
      "speaker": "A",
      "ja": "でも、近所の人と一緒に何かしたいと思ったのは本当です。",
      "vi": "Nhưng tôi thật sự muốn làm điều gì đó với người trong khu phố."
    },
    {
      "id": "s14--t05",
      "speaker": "B",
      "ja": "それなら、今日の準備はどうでしたか。",
      "vi": "Vậy việc chuẩn bị hôm nay thế nào?"
    },
    {
      "id": "s14--t06",
      "speaker": "A",
      "ja": "初めてで緊張しましたが、皆さんが声をかけてくれて安心しました。",
      "vi": "Lần đầu tôi hơi căng thẳng, nhưng mọi người bắt chuyện nên tôi yên tâm hơn."
    }
  ],
  "authorship": "original_extension"
}



## Tìm điểm quan tâm chung rồi hỏi sâu vừa đủ [s15]

{
  "id": "s15",
  "source_refs": [],
  "title": "Tìm điểm quan tâm chung rồi hỏi sâu vừa đủ",
  "event_id": "e03",
  "setting": "Sau khi đổi từ chuyện công việc sang ảnh chụp, hai người cùng quan tâm phong cảnh.",
  "communication_goal": "Nối một chi tiết rồi chia sẻ điều mình thích.",
  "relationship": "Hai người đã trao đổi ở s12.",
  "outcome": "common_interest_found",
  "follows": [
    "s12"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s15--t01",
      "speaker": "A",
      "ja": "先ほど、川の光がお好きだとおっしゃいましたね。水辺をよく撮られるんですか。",
      "vi": "Lúc nãy anh/chị nói thích ánh sáng trên sông. Anh/chị có hay chụp ven nước không?"
    },
    {
      "id": "s15--t02",
      "speaker": "B",
      "ja": "ええ。仕事の帰りに、川沿いを歩くことが多いんです。",
      "vi": "Có. Trên đường đi làm về tôi thường đi dọc sông."
    },
    {
      "id": "s15--t03",
      "speaker": "A",
      "ja": "いい習慣ですね。私は歩くのは好きですが、つい写真を撮り忘れます。",
      "vi": "Thói quen hay quá. Tôi thích đi bộ nhưng cứ quên chụp ảnh."
    },
    {
      "id": "s15--t04",
      "speaker": "B",
      "ja": "景色が変わったところだけ撮れば、あとで見返すのも楽しいですよ。",
      "vi": "Chỉ cần chụp chỗ phong cảnh thay đổi, sau này xem lại cũng vui."
    },
    {
      "id": "s15--t05",
      "speaker": "A",
      "ja": "なるほど。次の散歩で試してみます。それで、最初に撮ったのはどんな景色でしたか。",
      "vi": "Ra vậy. Lần đi dạo sau tôi sẽ thử. Vậy lúc mới chụp, anh/chị chụp cảnh gì?"
    },
    {
      "id": "s15--t06",
      "speaker": "B",
      "ja": "雨上がりの橋でした。光がきれいだったんです。",
      "vi": "Một cây cầu sau mưa. Ánh sáng lúc ấy rất đẹp."
    }
  ],
  "authorship": "original_extension"
}



## Lần gặp thứ hai: nhớ một chi tiết và cập nhật [k_revisit]

# Ký ức nhỏ nối lời

Một chi tiết người kia tự kể là điểm bắt đầu tốt: cuốn sách, bức tranh định vẽ, tiết mục đã xem. Hỏi về kết quả như lời mời kể, không như kiểm tra lời dự định.

<a id="s17_u01"></a>
先週、近所の川を描きたいとおっしゃっていましたよね。描けましたか。

Tuần trước anh/chị nói muốn vẽ con sông gần nhà. Anh/chị vẽ được chưa?

<a id="s17_u02"></a>
覚えていてくださったんですね。実は雨が続いて、まだ行けていないんです。

Anh/chị còn nhớ à. Thật ra trời mưa liên tục nên tôi chưa đi được.

Nếu họ chưa làm, đừng ép giải thích. Chuyển sang hiện tại:

<a id="s17_u03"></a>
そうでしたか。無理に行くことはないですよね。今日は何を描く予定ですか。

Vậy à. Không cần cố đi bằng được nhỉ. Hôm nay anh/chị định vẽ gì?

Nếu nhớ nhầm, tự sửa và hỏi lại đúng sự kiện. Trong s18, người học nhầm triển lãm thư pháp với gốm; việc cần làm là nhận lời đính chính. Lời mời hoạt động chung đến sau khi có hứng thú thật. Người kia vẫn có thể muốn giữ cuộc gặp trong nhóm.


## Lần gặp thứ hai nhớ điều người kia kể [s16]

{
  "id": "s16",
  "source_refs": [],
  "title": "Lần gặp thứ hai nhớ điều người kia kể",
  "event_id": "e04",
  "setting": "Một tuần sau, hai người gặp lại ở nhóm đọc sách.",
  "communication_goal": "Nối từ kế hoạch trước, không hỏi chung chung rồi hết chuyện.",
  "relationship": "Hai thành viên đã nói ở s02.",
  "outcome": "prior_thread_revisited",
  "follows": [
    "s02"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s16--t01",
      "speaker": "A",
      "ja": "こんにちは。先週、普段は選ばない本を読むのが楽しいとおっしゃっていましたよね。",
      "vi": "Chào anh/chị. Tuần trước anh/chị nói thích đọc những cuốn bình thường sẽ không tự chọn nhỉ."
    },
    {
      "id": "s16--t02",
      "speaker": "B",
      "ja": "覚えていてくださったんですね。実は、そのあと別の作家も読んでみました。",
      "vi": "Anh/chị còn nhớ à. Thật ra sau đó tôi đã thử đọc thêm một tác giả khác."
    },
    {
      "id": "s16--t03",
      "speaker": "A",
      "ja": "そうなんですか。どんなところが新鮮でしたか。",
      "vi": "Vậy à. Điểm nào khiến anh/chị thấy mới mẻ?"
    },
    {
      "id": "s16--t04",
      "speaker": "B",
      "ja": "話の進み方がゆっくりで、最初は驚きました。でも、だんだん好きになって。",
      "vi": "Mạch truyện chậm, ban đầu tôi ngạc nhiên. Nhưng dần dần lại thích."
    },
    {
      "id": "s16--t05",
      "speaker": "A",
      "ja": "ああ、後からよさが分かる本ってありますよね。私も一冊試してみたいです。",
      "vi": "À, có những cuốn càng đọc mới càng thấy hay nhỉ. Tôi cũng muốn thử một cuốn."
    },
    {
      "id": "s16--t06",
      "speaker": "B",
      "ja": "では、あとで題名をお伝えしますね。",
      "vi": "Vậy lát nữa tôi sẽ nói tên sách nhé."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi việc họ dự định làm đã diễn ra chưa [s17]

{
  "id": "s17",
  "source_refs": [],
  "title": "Hỏi việc họ dự định làm đã diễn ra chưa",
  "event_id": "e04",
  "setting": "Gặp lại một người ở lớp vẽ, người ấy từng định vẽ dòng sông gần nhà.",
  "communication_goal": "Nhớ kế hoạch cũ và đón nhận cả kết quả chưa làm được.",
  "relationship": "Hai học viên gặp lại sau s03.",
  "outcome": "followed_up_without_pressure",
  "follows": [
    "s03"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s17--t01",
      "speaker": "A",
      "ja": "先週、近所の川を描きたいとおっしゃっていましたよね。描けましたか。",
      "vi": "Tuần trước anh/chị nói muốn vẽ con sông gần nhà. Anh/chị vẽ được chưa?"
    },
    {
      "id": "s17--t02",
      "speaker": "B",
      "ja": "覚えていてくださったんですね。実は雨が続いて、まだ行けていないんです。",
      "vi": "Anh/chị còn nhớ à. Thật ra trời mưa liên tục nên tôi chưa đi được."
    },
    {
      "id": "s17--t03",
      "speaker": "A",
      "ja": "そうでしたか。無理に行くことはないですよね。今日は何を描く予定ですか。",
      "vi": "Vậy à. Không cần cố đi bằng được nhỉ. Hôm nay anh/chị định vẽ gì?"
    },
    {
      "id": "s17--t04",
      "speaker": "B",
      "ja": "窓から見える木を描こうと思っています。",
      "vi": "Tôi định vẽ cái cây nhìn từ cửa sổ."
    },
    {
      "id": "s17--t05",
      "speaker": "A",
      "ja": "いいですね。雨の日は、いつもと違う色がありそうです。",
      "vi": "Hay đó. Ngày mưa có lẽ sẽ có màu sắc khác mọi ngày."
    },
    {
      "id": "s17--t06",
      "speaker": "B",
      "ja": "そう言っていただけると、描くのが楽しみになります。",
      "vi": "Anh/chị nói vậy làm tôi háo hức muốn vẽ hơn."
    }
  ],
  "authorship": "original_extension"
}



## Nhớ nhầm tên hoạt động và để người kia sửa [s18]

{
  "id": "s18",
  "source_refs": [],
  "title": "Nhớ nhầm tên hoạt động và để người kia sửa",
  "event_id": "e04",
  "setting": "Người học gặp lại người quen ở sự kiện sau hai tuần.",
  "communication_goal": "Đính chính trí nhớ sai, rồi hỏi tiếp đúng sự kiện.",
  "relationship": "Hai người đã từng nói ngắn.",
  "outcome": "misremembering_repaired",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s18--t01",
      "speaker": "A",
      "ja": "この前の書道展、いかがでしたか。",
      "vi": "Triển lãm thư pháp lần trước thế nào ạ?"
    },
    {
      "id": "s18--t02",
      "speaker": "B",
      "ja": "あ、書道展ではなくて、陶芸展です。",
      "vi": "À, không phải triển lãm thư pháp, mà là triển lãm gốm."
    },
    {
      "id": "s18--t03",
      "speaker": "A",
      "ja": "あ、そうでした。取り違えてすみません。陶芸展には行かれたんですか。",
      "vi": "À, đúng rồi. Xin lỗi, tôi nhớ nhầm. Anh/chị có đến triển lãm gốm không?"
    },
    {
      "id": "s18--t04",
      "speaker": "B",
      "ja": "ええ。小さな作品が多くて、見ていて楽しかったです。",
      "vi": "Có. Nhiều tác phẩm nhỏ nên xem rất thú vị."
    },
    {
      "id": "s18--t05",
      "speaker": "A",
      "ja": "そうなんですね。特に印象に残ったものはありますか。",
      "vi": "Vậy à. Có tác phẩm nào gây ấn tượng đặc biệt không?"
    },
    {
      "id": "s18--t06",
      "speaker": "B",
      "ja": "青いお皿です。色がとてもきれいでした。",
      "vi": "Một chiếc đĩa màu xanh. Màu rất đẹp."
    }
  ],
  "authorship": "original_extension"
}



## Rủ xem hoạt động chung sau khi thấy có hứng thú [s19]

{
  "id": "s19",
  "source_refs": [],
  "title": "Rủ xem hoạt động chung sau khi thấy có hứng thú",
  "event_id": "e04",
  "setting": "Hai người đã trò chuyện về ảnh, khu bên cạnh sắp có phần giới thiệu tranh.",
  "communication_goal": "Đề nghị nhẹ và cho người kia lựa chọn.",
  "relationship": "Hai người đã gặp lại ở s10.",
  "outcome": "invitation_accepted",
  "follows": [
    "s10"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s19--t01",
      "speaker": "A",
      "ja": "このあと、隣の部屋で作品の説明があるそうです。興味があれば、一緒に聞きませんか。",
      "vi": "Lát nữa phòng bên có phần giới thiệu tác phẩm. Nếu anh/chị thích, ta cùng nghe không?"
    },
    {
      "id": "s19--t02",
      "speaker": "B",
      "ja": "いいですね。私も気になっていました。何時からですか。",
      "vi": "Hay đấy. Tôi cũng đang quan tâm. Mấy giờ bắt đầu?"
    },
    {
      "id": "s19--t03",
      "speaker": "A",
      "ja": "三時からです。まだ少し時間がありますね。",
      "vi": "Từ ba giờ. Vẫn còn một chút thời gian."
    },
    {
      "id": "s19--t04",
      "speaker": "B",
      "ja": "それなら、先にこの部屋を見終わってから行きましょう。",
      "vi": "Vậy mình xem hết phòng này rồi hãy sang nhé."
    },
    {
      "id": "s19--t05",
      "speaker": "A",
      "ja": "そうしましょう。急がずに見られますね。",
      "vi": "Vâng. Mình có thể xem thong thả."
    },
    {
      "id": "s19--t06",
      "speaker": "B",
      "ja": "ええ、楽しみです。",
      "vi": "Vâng, tôi háo hức đấy."
    }
  ],
  "authorship": "original_extension"
}



## Người kia chưa muốn hẹn riêng, để cuộc gặp tự nhiên [s20]

{
  "id": "s20",
  "source_refs": [],
  "title": "Người kia chưa muốn hẹn riêng, để cuộc gặp tự nhiên",
  "event_id": "e04",
  "setting": "Người học mời người vừa gặp lại cùng đi xem triển lãm tuần sau.",
  "communication_goal": "Tôn trọng khoảng cách quan hệ và đề nghị gặp trong nhóm nếu tự nhiên.",
  "relationship": "Người mới quen, chưa hẹn riêng.",
  "outcome": "private_invitation_declined",
  "follows": [],
  "alternative_to": [
    "s19"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s20--t01",
      "speaker": "A",
      "ja": "来週の展示も、よかったら二人で見に行きませんか。",
      "vi": "Triển lãm tuần sau, nếu anh/chị muốn, hai người mình cùng đi xem không?"
    },
    {
      "id": "s20--t02",
      "speaker": "B",
      "ja": "誘ってくださってありがとうございます。でも、まだ二人だけで出かけるのは少し早いかなと思って。",
      "vi": "Cảm ơn anh/chị đã mời. Nhưng tôi nghĩ đi riêng hai người lúc này hơi sớm."
    },
    {
      "id": "s20--t03",
      "speaker": "A",
      "ja": "そうですよね。急に誘ってしまってすみません。気にしないでください。",
      "vi": "Đúng nhỉ. Xin lỗi vì tôi mời hơi đột ngột. Anh/chị đừng bận tâm."
    },
    {
      "id": "s20--t04",
      "speaker": "B",
      "ja": "いえ、今日ここでお話しするのは楽しいですよ。",
      "vi": "Không đâu. Hôm nay nói chuyện ở đây thì rất vui."
    },
    {
      "id": "s20--t05",
      "speaker": "A",
      "ja": "私もです。では、残りの展示を一緒に見ましょうか。",
      "vi": "Tôi cũng vậy. Vậy ta cùng xem phần triển lãm còn lại nhé?"
    },
    {
      "id": "s20--t06",
      "speaker": "B",
      "ja": "はい、それならぜひ。",
      "vi": "Vâng, thế thì được."
    }
  ],
  "authorship": "original_extension"
}



## Khép lời và giữ một đường gặp lại [k_close]

# Kết thúc mà vẫn còn đường tiếp

Nêu mình phải đi, nhắc một điều người kia đã chia sẻ và cảm ơn. Cách này cụ thể hơn lời chào chung, nhưng không ép họ nói tiếp.

<a id="s21_u01"></a>
そろそろ行かなくては。今日はお話できて楽しかったです。

Tôi phải đi rồi. Hôm nay được trò chuyện thật vui.

<a id="s21_u03"></a>
川沿いを歩く話が特に印象に残りました。教えてくださってありがとうございます。

Chuyện đi dọc bờ sông đặc biệt khiến tôi nhớ. Cảm ơn anh/chị đã kể.

Khi hai bên đều muốn nói tiếp, hỏi cách liên lạc vì một mục đích rõ và đưa lựa chọn gặp ở nhóm. Nếu họ không muốn, chấp nhận ngay:

<a id="s23_u02"></a>
すみません。初めて会った方とは、まだ交換しないようにしているんです。

Xin lỗi. Tôi chưa trao đổi cách liên lạc với người mới gặp lần đầu.

<a id="s23_u03"></a>
そうですよね。聞いてしまってすみません。無理にとは思っていません。

Đúng nhỉ. Xin lỗi vì đã hỏi. Tôi không muốn ép đâu.

「行けたら」 (nếu đi được) là khả năng, không phải lời hứa. Khi gặp lại, nối chủ đề đã nói thay vì chất vấn vì sao họ vắng hay chưa nhắn. Đường tiếp có thể chỉ là “nếu cùng đến buổi sau”, không bắt buộc số điện thoại hay hẹn riêng.


## Đang phải đi, cảm ơn cuộc trò chuyện [s21]

{
  "id": "s21",
  "source_refs": [],
  "title": "Đang phải đi, cảm ơn cuộc trò chuyện",
  "event_id": "e05",
  "setting": "Buổi nhóm sắp kết thúc và người học có việc khác.",
  "communication_goal": "Thông báo rời đi và ghi nhận điều người kia đã chia sẻ.",
  "relationship": "Hai người mới quen sau cuộc trò chuyện.",
  "outcome": "clean_exit",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s21--t01",
      "speaker": "A",
      "ja": "そろそろ行かなくては。今日はお話できて楽しかったです。",
      "vi": "Tôi phải đi rồi. Hôm nay được trò chuyện thật vui."
    },
    {
      "id": "s21--t02",
      "speaker": "B",
      "ja": "こちらこそ。写真のお話、面白かったです。",
      "vi": "Tôi cũng vậy. Chuyện ảnh chụp thú vị lắm."
    },
    {
      "id": "s21--t03",
      "speaker": "A",
      "ja": "川沿いを歩く話が特に印象に残りました。教えてくださってありがとうございます。",
      "vi": "Chuyện đi dọc bờ sông đặc biệt khiến tôi nhớ. Cảm ơn anh/chị đã kể."
    },
    {
      "id": "s21--t04",
      "speaker": "B",
      "ja": "またこの会でお会いできるといいですね。",
      "vi": "Mong lại gặp anh/chị ở nhóm này."
    },
    {
      "id": "s21--t05",
      "speaker": "A",
      "ja": "ええ。では、お先に失礼します。",
      "vi": "Vâng. Vậy tôi xin phép về trước."
    },
    {
      "id": "s21--t06",
      "speaker": "B",
      "ja": "お気をつけて。",
      "vi": "Anh/chị đi cẩn thận."
    }
  ],
  "authorship": "original_extension"
}



## Xin cách liên lạc khi cả hai cùng muốn trao đổi tiếp [s22]

{
  "id": "s22",
  "source_refs": [],
  "title": "Xin cách liên lạc khi cả hai cùng muốn trao đổi tiếp",
  "event_id": "e05",
  "setting": "Sau buổi nhóm, hai người đang bàn một cuốn sách muốn mượn chung.",
  "communication_goal": "Đề nghị trao đổi liên lạc có lý do và cho quyền từ chối.",
  "relationship": "Hai thành viên mới nói chuyện, chưa thân.",
  "outcome": "contact_exchanged",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s22--t01",
      "speaker": "A",
      "ja": "さっきの本、私も読んでみたいです。もしよければ、読み終わったころに感想を聞いてもいいですか。",
      "vi": "Tôi cũng muốn thử đọc cuốn lúc nãy. Nếu tiện, khi anh/chị đọc xong tôi có thể hỏi cảm nhận không?"
    },
    {
      "id": "s22--t02",
      "speaker": "B",
      "ja": "もちろんです。私も話したいと思っていました。",
      "vi": "Tất nhiên. Tôi cũng muốn nói về cuốn đó."
    },
    {
      "id": "s22--t03",
      "speaker": "A",
      "ja": "では、連絡先を交換してもいいですか。もちろん、この会で会ったときでも大丈夫です。",
      "vi": "Vậy mình trao đổi cách liên lạc được không? Tất nhiên, nói ở buổi nhóm sau cũng được."
    },
    {
      "id": "s22--t04",
      "speaker": "B",
      "ja": "大丈夫ですよ。メッセージでお願いします。",
      "vi": "Được. Nhắn tin cho tôi nhé."
    },
    {
      "id": "s22--t05",
      "speaker": "A",
      "ja": "ありがとうございます。本の話だけでなく、次回の会の予定も共有できますね。",
      "vi": "Cảm ơn. Ngoài chuyện sách, ta còn có thể chia sẻ lịch nhóm lần tới."
    },
    {
      "id": "s22--t06",
      "speaker": "B",
      "ja": "ええ。では、帰りに交換しましょう。",
      "vi": "Vâng. Vậy trên đường về mình trao đổi nhé."
    }
  ],
  "authorship": "original_extension"
}



## Không trao đổi liên lạc, tôn trọng lời đáp [s23]

{
  "id": "s23",
  "source_refs": [],
  "title": "Không trao đổi liên lạc, tôn trọng lời đáp",
  "event_id": "e05",
  "setting": "Người học ngỏ ý trao đổi liên lạc sau sự kiện nhưng người kia chưa muốn.",
  "communication_goal": "Khép lời không nài hoặc đòi lý do.",
  "relationship": "Hai người mới gặp ở sự kiện.",
  "outcome": "contact_declined",
  "follows": [],
  "alternative_to": [
    "s22"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s23--t01",
      "speaker": "A",
      "ja": "もしよかったら、連絡先を交換しませんか。",
      "vi": "Nếu tiện, ta trao đổi cách liên lạc không?"
    },
    {
      "id": "s23--t02",
      "speaker": "B",
      "ja": "すみません。初めて会った方とは、まだ交換しないようにしているんです。",
      "vi": "Xin lỗi. Tôi chưa trao đổi cách liên lạc với người mới gặp lần đầu."
    },
    {
      "id": "s23--t03",
      "speaker": "A",
      "ja": "そうですよね。聞いてしまってすみません。無理にとは思っていません。",
      "vi": "Đúng nhỉ. Xin lỗi vì đã hỏi. Tôi không muốn ép đâu."
    },
    {
      "id": "s23--t04",
      "speaker": "B",
      "ja": "分かってくださってありがとうございます。",
      "vi": "Cảm ơn anh/chị đã hiểu."
    },
    {
      "id": "s23--t05",
      "speaker": "A",
      "ja": "今日はお話できてよかったです。また会場でお会いしたら、よろしくお願いします。",
      "vi": "Hôm nay nói chuyện với anh/chị thật vui. Nếu gặp lại ở địa điểm này, mong được chào nhau tiếp."
    },
    {
      "id": "s23--t06",
      "speaker": "B",
      "ja": "はい。では、また。",
      "vi": "Vâng. Hẹn dịp khác."
    }
  ],
  "authorship": "original_extension"
}



## Buổi sau chưa chắc đi, để một lời hẹn mở [s24]

{
  "id": "s24",
  "source_refs": [],
  "title": "Buổi sau chưa chắc đi, để một lời hẹn mở",
  "event_id": "e05",
  "setting": "Sau khi bàn về một cuốn sách ở buổi nhóm, người học hỏi người kia có đến buổi tuần sau không.",
  "communication_goal": "Không biến câu trả lời chưa chắc thành lời hứa.",
  "relationship": "Hai người mới quen cùng nhóm.",
  "outcome": "no_fixed_plan",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s24--t01",
      "speaker": "A",
      "ja": "来週の会にも参加されますか。",
      "vi": "Tuần sau anh/chị cũng tham gia buổi nhóm chứ?"
    },
    {
      "id": "s24--t02",
      "speaker": "B",
      "ja": "まだ予定が分からないんです。行けたら、という感じです。",
      "vi": "Tôi vẫn chưa biết lịch. Kiểu nếu đi được thì sẽ đi."
    },
    {
      "id": "s24--t03",
      "speaker": "A",
      "ja": "分かりました。予定が決まってからで大丈夫ですよ。",
      "vi": "Tôi hiểu. Khi nào rõ lịch cũng được."
    },
    {
      "id": "s24--t04",
      "speaker": "B",
      "ja": "ありがとうございます。リンさんは行く予定ですか。",
      "vi": "Cảm ơn. Linh định đi chứ?"
    },
    {
      "id": "s24--t05",
      "speaker": "A",
      "ja": "私は今のところ行くつもりです。もし会えたら、今日の本の話の続きをしましょう。",
      "vi": "Hiện tôi định đi. Nếu gặp nhau, ta nói tiếp chuyện cuốn sách hôm nay nhé."
    },
    {
      "id": "s24--t06",
      "speaker": "B",
      "ja": "はい。会えたらうれしいです。",
      "vi": "Vâng. Nếu gặp được thì vui lắm."
    }
  ],
  "authorship": "original_extension"
}



## Gặp lại rồi nối chuyện từ lần trước [s25]

{
  "id": "s25",
  "source_refs": [],
  "title": "Gặp lại rồi nối chuyện từ lần trước",
  "event_id": "e05",
  "setting": "Sau một tuần, người kia thực sự tới buổi nhóm và nhận ra người học.",
  "communication_goal": "Nối lại một chủ đề cũ và mở chủ đề mới theo đáp của họ.",
  "relationship": "Hai người đã khép cuộc nói ở s24.",
  "outcome": "relationship_continues",
  "follows": [
    "s24"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người mở hoặc tiếp chuyện"
    },
    {
      "id": "B",
      "role": "Người mới gặp hoặc mới quen"
    }
  ],
  "turns": [
    {
      "id": "s25--t01",
      "speaker": "B",
      "ja": "あ、リンさん。先週はどうも。結局、来られました。",
      "vi": "À, Linh. Tuần trước cảm ơn nhé. Cuối cùng tôi đến được."
    },
    {
      "id": "s25--t02",
      "speaker": "A",
      "ja": "よかったです。またお会いできましたね。先週お話しした本、読み始めましたか。",
      "vi": "Thật vui. Ta gặp lại rồi. Cuốn sách nói tuần trước, anh/chị bắt đầu đọc chưa?"
    },
    {
      "id": "s25--t03",
      "speaker": "B",
      "ja": "ええ、少しだけ。思ったより読みやすかったです。",
      "vi": "Rồi, một chút thôi. Dễ đọc hơn tôi tưởng."
    },
    {
      "id": "s25--t04",
      "speaker": "A",
      "ja": "そうなんですか。どんなところからそう感じましたか。",
      "vi": "Vậy à. Điều gì khiến anh/chị thấy vậy?"
    },
    {
      "id": "s25--t05",
      "speaker": "B",
      "ja": "会話が多くて、人物が分かりやすいんです。",
      "vi": "Có nhiều hội thoại nên dễ hiểu các nhân vật."
    },
    {
      "id": "s25--t06",
      "speaker": "A",
      "ja": "なるほど。今日の会が終わったら、その続きも聞かせてください。",
      "vi": "Ra vậy. Khi buổi nhóm hôm nay xong, kể tiếp cho tôi nghe nhé."
    },
    {
      "id": "s25--t07",
      "speaker": "B",
      "ja": "ぜひ。リンさんの感想も聞きたいです。",
      "vi": "Rất vui. Tôi cũng muốn nghe cảm nhận của Linh."
    }
  ],
  "authorship": "original_extension"
}



## Trò chuyện tự do: từ cuộc gặp đầu đến lần gặp lại [ft01]

{
  "id": "ft01",
  "source_refs": [],
  "context_node_ids": [
    "v_context",
    "g_core",
    "k_open",
    "kn27",
    "sh27",
    "k70",
    "sh70",
    "v_turn",
    "k_recip",
    "k73",
    "sh73",
    "s01",
    "s02",
    "s03",
    "s04",
    "s05",
    "s06",
    "s07",
    "s08",
    "s09",
    "s10",
    "v_boundary",
    "g_follow",
    "k_boundary",
    "s11",
    "s12",
    "s13",
    "s14",
    "s15",
    "k_revisit",
    "s16",
    "s17",
    "s18",
    "s19",
    "s20",
    "k_close",
    "s21",
    "s22",
    "s23",
    "s24",
    "s25"
  ],
  "overview_vi": "Làm quen trong lớp và sự kiện, đáp qua lại thay vì hỏi như phỏng vấn, nhận tín hiệu muốn dừng, nối lại cuộc nói ở lần gặp sau và khép lời với đường tiếp phù hợp. Trình độ Trung; chỉ luyện nghe và nói.",
  "optional_extensions": [],
  "context_export": "live-context.md",
  "free_talk": {
    "learner_intro_vi": "Hãy chọn một người bạn chưa quen gặp trong lớp, nhóm đọc sách, lễ hội hoặc triển lãm. Bạn có thể bắt đầu từ điều đang diễn ra, kể điều mình muốn, hỏi tiếp và đổi hướng tự do. Người kia có thể muốn nói lâu, đang bận, giữ chuyện riêng tư hoặc tình cờ gặp lại bạn lần sau. Không có câu trả lời chuẩn.",
    "ai_situation_vi": "Đây là trò chuyện tự do cuối chặng, không phải lần lượt diễn năm challenge. AI chỉ đóng một người có quan hệ nhất quán với người học; khi người học đổi bối cảnh hợp lý có thể chuyển sang lần gặp sau, nhớ điều đã nói trong chính phiên này. Bắt đầu từ một hoạt động cụ thể như cùng xem tranh hoặc chuẩn bị lớp, không mở bằng hỏi lý lịch liên tiếp. Để người học chọn đề tài, nhịp độ, mức tự tiết lộ và thời điểm kết thúc. Hỏi tiếp từ chi tiết họ vừa nói, tự kể một điều cân xứng, phản hồi tin vui/tin khó bằng sắc thái phù hợp. Có thể cho thấy đang chờ bạn, không muốn nói riêng tư, chưa muốn trao đổi liên lạc, hoặc sẵn lòng gặp lại; phản ứng phải đúng quan hệ và không ép bất kỳ nhánh nào. Khi người học hỏi quá sâu, đặt giới hạn lịch sự; khi họ sửa lời, chấp nhận. Khi họ từ chối, dừng đề nghị. Vận dụng các mẫu của B11 bài 70/73 theo mức thân: phản hồi へー/ああ và hỏi tiếp で/それで; ở lần đầu ưu tiên câu lịch sự đầy đủ. B27 skit ① cho mạch chỗ ngồi → môn học → điểm chung → tên → lời rủ, nhưng không mặc định lời rủ được nhận. Các hội thoại s01–s25 là chất liệu lựa chọn, không phải lời phải đọc thuộc. Từ vựng nhóm v_context/v_turn/v_boundary và mẫu g_core/g_follow chỉ là hỗ trợ. Cho phép chủ đề mới nếu cuộc nói tự nhiên; không chấm điểm, không kiểm tra, không khóa, không nói thay người học.",
    "conversation_starters_vi": [
      "Hai bạn cùng đứng trước bàn nguyên liệu của buổi học đầu tiên. Bạn muốn mở lời thế nào?",
      "Ở triển lãm, người kia vừa nói thích ảnh mùa đông. Bạn muốn hỏi tiếp điều gì và kể cảm nhận nào của mình?",
      "Bạn gặp lại người từng định vẽ con sông nhưng chưa biết họ đã làm chưa. Bắt đầu ra sao để không tạo áp lực?",
      "Cuộc nói chuyện vui nhưng bạn phải đi. Bạn muốn khép lời và để ngỏ dịp gặp sau thế nào?"
    ],
    "mode": "free_talk",
    "content_origin": "curriculum_authored",
    "situation_export": "free-talk-situation.md"
  }
}



## Bài học và nội dung gối đầu

{
  "schema_version": "1.0",
  "stage_uid": "2c4afb8d-e518-5c65-989e-076857a6ce9d",
  "lessons": [
    {
      "id": "l01",
      "summary": "Mở chuyện ở lớp, phản hồi và hỏi tiếp",
      "node_ids": [
        "v_context",
        "g_core",
        "k_open",
        "kn27",
        "sh27",
        "k70",
        "sh70",
        "v_turn",
        "k_recip",
        "k73",
        "sh73",
        "s01",
        "s02",
        "s03",
        "s04",
        "s05"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l02",
      "summary": "Trò chuyện tại sự kiện và nhận tín hiệu dừng",
      "node_ids": [
        "s06",
        "s07",
        "s08",
        "s09",
        "s10"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l03",
      "summary": "Ranh giới riêng tư và tìm chủ đề chung",
      "node_ids": [
        "v_boundary",
        "g_follow",
        "k_boundary",
        "s11",
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
      "summary": "Nối lần gặp sau và lời mời có lựa chọn",
      "node_ids": [
        "k_revisit",
        "s16",
        "s17",
        "s18",
        "s19",
        "s20"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l05",
      "summary": "Khép cuộc nói và để đường tiếp",
      "node_ids": [
        "k_close",
        "s21",
        "s22",
        "s23",
        "s24",
        "s25"
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
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B02",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B03",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B04",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B05",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B06",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B07",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B08",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B09",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B10",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B11",
      "status": "read",
      "note": "Đã đọc phần được chọn và dùng trong chặng."
    },
    {
      "book_id": "B12",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B13",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B14",
      "status": "read",
      "note": "Đã đọc Section 6 để cân nhắc; không chọn vì toàn pack quá cơ bản cho mục tiêu Trung."
    },
    {
      "book_id": "B15",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B16",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B17",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B18",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B19",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B20",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B21",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B22",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B23",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B24",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B25",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B26",
      "status": "index_only",
      "note": "Quét heading và guide để tìm chất liệu, không gọi là đọc nội dung."
    },
    {
      "book_id": "B27",
      "status": "read",
      "note": "Đã đọc phần được chọn và dùng trong chặng."
    }
  ],
  "entries": [
    {
      "id": "srcB11",
      "kind": "book",
      "path": "kaiwa_skill/knowledge/わかる！話せる！日本語会話 基本文型88/chapters/11-part2-noi-thoai.md",
      "locator": {
        "heading": "Bài 70 CD 70, bài 73 CD 73",
        "lines": [
          50,
          139
        ]
      },
      "sha256": "3f4a0eea54e0a5819285150338a1223d747fa628dfd9838aba4ce61f6fa58ddd",
      "read_status": "read",
      "used_for": [
        "k70",
        "sh70",
        "k73",
        "sh73"
      ],
      "contribution": "Giữ lời gốc, mạch phân biệt phản hồi và hỏi tiếp; cặp video planned và shadowing.",
      "book_id": "B11"
    },
    {
      "id": "srcB27",
      "kind": "book",
      "path": "kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/14-script-bai-01.md",
      "locator": {
        "heading": "Bài 1 出会い, 聞き取り練習 skit ① 1-2",
        "lines": [
          4,
          23
        ]
      },
      "sha256": "6bd23dfe010a98301f24fcf7104b7bc516b15dca5ae32c91c7a23c267086d5e5",
      "read_status": "read",
      "used_for": [
        "kn27",
        "sh27"
      ],
      "contribution": "Giữ toàn 14 lượt skit gặp ở lớp; phân tích mạch làm quen.",
      "book_id": "B27"
    },
    {
      "id": "srcGrammar",
      "kind": "reference",
      "path": "kaiwa_skill/reference/grammar/MINNA_01_50_GRAMMAR.json",
      "locator": {
        "heading": "Tên mẫu Minna bài 19, 21, 25, 26, 31, 32, 35, 36, 39, 43, 44, 47, 49"
      },
      "sha256": "77503e668fd152260f34a49c18986030209779df413b52822b78eeffd42b73d2",
      "read_status": "read",
      "used_for": [
        "g_core",
        "g_follow"
      ],
      "contribution": "Đối chiếu tên mẫu; JLPT là mapping biên tập."
    },
    {
      "id": "jfB1",
      "kind": "web",
      "url": "https://www.jfstandard.jpf.go.jp/pdf/202305_JF_Cando_Category_list.pdf",
      "locator": {
        "item": "JFまるごと Can-do 196, B1, 社交的なやりとりをする",
        "web_lines": [
          3073,
          3082
        ]
      },
      "read_status": "read",
      "accessed_on": "2026-11-13",
      "used_for": [
        "k_open",
        "k_recip"
      ],
      "contribution": "Mục tiêu hội thoại hai chiều ở tiệc/nhóm mới; không cung cấp lời thoại cho chặng."
    },
    {
      "id": "irodoriL8",
      "kind": "web",
      "url": "https://www.irodori.jpf.go.jp/assets/data/pre-intermediate/pdf/ZZ_L08.pdf",
      "locator": {
        "lesson": "初中級 第8課 隣、いいですか？",
        "web_lines": [
          0,
          32
        ]
      },
      "read_status": "read",
      "accessed_on": "2026-11-13",
      "used_for": [
        "k_open"
      ],
      "contribution": "Tham khảo cách bắt chuyện từ bối cảnh cụ thể; không trích câu vào pack."
    },
    {
      "id": "original",
      "kind": "original",
      "locator": {
        "stage": "T-001",
        "scope": "25 tình huống, kiến thức, Live context do AI soạn và tác giả rà"
      },
      "read_status": "read",
      "used_for": [
        "s01",
        "s02",
        "s03",
        "s04",
        "s05",
        "s06",
        "s07",
        "s08",
        "s09",
        "s10",
        "s11",
        "s12",
        "s13",
        "s14",
        "s15",
        "s16",
        "s17",
        "s18",
        "s19",
        "s20",
        "s21",
        "s22",
        "s23",
        "s24",
        "s25"
      ],
      "contribution": "Hội thoại và nhánh mới, không gán cho sách hoặc audio."
    }
  ]
}

