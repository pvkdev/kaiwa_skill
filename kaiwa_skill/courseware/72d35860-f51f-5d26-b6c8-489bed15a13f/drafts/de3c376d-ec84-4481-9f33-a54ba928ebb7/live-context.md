# Nhà hàng và quán ăn

{
  "schema_version": "3.2-draft",
  "stage_uid": "72d35860-f51f-5d26-b6c8-489bed15a13f",
  "display_code": "S-031",
  "title": "Nhà hàng và quán ăn",
  "level": "Sơ",
  "scope": "Vào quán, hỏi bàn và món, gọi đúng số suất, xử lý thay đổi nhỏ trong bữa, kiểm hóa đơn và liên hệ lại khi để quên đồ. Chỉ luyện nghe và nói.",
  "events": [
    {
      "id": "e01",
      "title": "Vào quán và nhận chỗ",
      "situation_ids": [
        "s01",
        "s22",
        "s02",
        "s03",
        "s04",
        "s05"
      ]
    },
    {
      "id": "e02",
      "title": "Xem và gọi món",
      "situation_ids": [
        "s06",
        "s07",
        "s08",
        "s09",
        "s10",
        "s11",
        "s12"
      ]
    },
    {
      "id": "e03",
      "title": "Trong bữa ăn",
      "situation_ids": [
        "s13",
        "s14",
        "s15",
        "s16"
      ]
    },
    {
      "id": "e04",
      "title": "Thanh toán và liên hệ lại",
      "situation_ids": [
        "s17",
        "s18",
        "s19",
        "s20",
        "s21"
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


## Từ để vào quán và chọn món [v01]

{
  "id": "v01",
  "source_refs": [],
  "items": [
    {
      "id": "v01-w-81c69df6eb94",
      "ja": "席",
      "source_refs": []
    },
    {
      "id": "v01-w-2e349895e8bc",
      "ja": "空く",
      "source_refs": []
    },
    {
      "id": "v01-w-8981f8b72b35",
      "ja": "二人",
      "source_refs": []
    },
    {
      "id": "v01-w-6f3443ca32a1",
      "ja": "メニュー",
      "source_refs": []
    },
    {
      "id": "v01-w-ef9afc92783f",
      "ja": "静か",
      "source_refs": []
    },
    {
      "id": "v01-w-9c3250ff63e1",
      "ja": "写真",
      "source_refs": []
    },
    {
      "id": "v01-w-b3cd0ed8a602",
      "ja": "おすすめ",
      "source_refs": []
    },
    {
      "id": "v01-w-84de258837d4",
      "ja": "注文する",
      "source_refs": []
    },
    {
      "id": "v01-w-79bdb367f49b",
      "ja": "一人前",
      "source_refs": []
    }
  ]
}



## Mẫu hỏi và nhờ khi vào quán [g01]

{
  "id": "g01",
  "source_refs": [
    "grammar_m"
  ],
  "items": [
    {
      "id": "g01-g-f011cf9db004",
      "name_ja": "場所にNがあります／います",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-e8fb271526f3",
      "name_ja": "Vてください",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-e3085d375ad7",
      "name_ja": "Vます形＋たいです",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-785102d73d16",
      "name_ja": "Vてもいいですか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-bcb2597d78fc",
      "name_ja": "Nなら",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-29eeee4d83d1",
      "name_ja": "Vてもらいます",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Vào quán: nói số người và hỏi chỗ [k01]

# Từ cửa quán đến chỗ ngồi

Nói số người ngay khi nhân viên đón khách. Nếu đã đặt bàn, nêu giờ và tên dùng khi đặt; nhân viên có thể nhắc lại cả hai để xác nhận. Nếu chưa đặt, hỏi còn bàn rồi chờ họ dẫn đi. Câu hỏi về bàn đi trước câu hỏi về món.

Khi muốn bàn yên hơn, hỏi xem còn chỗ phù hợp không. Đừng tự chuyển bàn vì nhân viên có thể đã dành bàn ấy cho khách khác. Nếu quán báo kín bàn, hỏi một mốc giờ có thể quay lại; câu trả lời thường là dự kiến, chưa có nghĩa quán giữ bàn cho mình.

Có quán chỉ còn bàn dùng được đến một giờ nhất định. Hãy nghe lại giờ phải rời bàn và tự quyết định có đủ thời gian ăn không. Nếu đồng ý, xác nhận rõ; nếu không, hỏi giờ khác hoặc chọn quán khác. Đừng nhận bàn rồi mới phát hiện hai bên hiểu khác nhau.

Nói số người, đặt bàn và hỏi giờ quay lại bằng ba câu sau:

<a id="s01_u01"></a>
すみません、二人です。席はありますか。

Xin lỗi, chúng tôi có hai người. Còn bàn không ạ?

<a id="s22_u01"></a>
七時に二人で予約したいです。席はありますか。

Tôi muốn đặt bàn cho hai người lúc bảy giờ. Quán còn bàn không ạ?

<a id="s04_u03"></a>
何時ごろなら空きますか。

Khoảng mấy giờ thì có bàn ạ?


## Nhận diện cách nói trang trọng của nhân viên [g_ref]

{
  "id": "g_ref",
  "source_refs": [
    "grammar_m"
  ],
  "items": [
    {
      "id": "g_ref-g-d7b0b8312fda",
      "name_ja": "尊敬語",
      "jlpt_level": "N3",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g_ref-g-a7a307e9ecd2",
      "name_ja": "特別な尊敬語",
      "jlpt_level": "N3",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Luyện đủ câu khi gọi món và dùng bữa [sh01]

{
  "id": "sh01",
  "source_refs": [
    "b08_05",
    "b08_06"
  ],
  "knowledge_ids": [],
  "items": [
    {
      "id": "i01",
      "kind": "sentence",
      "example_id": "q01",
      "ja": "メニューを見せてもらえますか。",
      "vi": "Cho tôi xem thực đơn được không?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i02",
      "kind": "sentence",
      "example_id": "q02",
      "ja": "すみません、注文をお願いします。",
      "vi": "Xin lỗi, tôi muốn gọi món.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i03",
      "kind": "sentence",
      "example_id": "q03",
      "ja": "コーヒーをお願いします。",
      "vi": "Cho tôi cà phê.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i04",
      "kind": "sentence",
      "example_id": "q04",
      "ja": "ホットとアイス、どちらになさいますか。",
      "vi": "Quý khách dùng loại nóng hay lạnh?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i05",
      "kind": "sentence",
      "example_id": "q05",
      "ja": "ホットでお願いします。",
      "vi": "Cho tôi loại nóng.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i06",
      "kind": "sentence",
      "example_id": "q06",
      "ja": "お飲み物はお食事の後でよろしいですか。",
      "vi": "Quý khách dùng đồ uống sau bữa ăn được chứ ạ?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i07",
      "kind": "sentence",
      "example_id": "q07",
      "ja": "後でお願いします。",
      "vi": "Xin mang sau bữa ăn.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i08",
      "kind": "sentence",
      "example_id": "q08",
      "ja": "一緒でお願いします。",
      "vi": "Xin mang cùng với bữa ăn.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_05"
      ]
    },
    {
      "id": "i09",
      "kind": "sentence",
      "example_id": "q09",
      "ja": "私はこれにします。さくらさんは何にしますか。",
      "vi": "Tôi chọn món này. Sakura, bạn chọn món gì?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i10",
      "kind": "sentence",
      "example_id": "q10",
      "ja": "おすすめは何ですか。",
      "vi": "Món nào được quán gợi ý?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i11",
      "kind": "sentence",
      "example_id": "q11",
      "ja": "これは豚肉が入っていますか。",
      "vi": "Món này có thịt lợn không?",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i12",
      "kind": "sentence",
      "example_id": "q12",
      "ja": "生の魚は苦手なんです。",
      "vi": "Tôi không hợp món cá sống.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i13",
      "kind": "sentence",
      "example_id": "q13",
      "ja": "お酒は飲めないんです。",
      "vi": "Tôi không uống được rượu.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i14",
      "kind": "sentence",
      "example_id": "q14",
      "ja": "注文したものが来ないんですが。",
      "vi": "Món tôi gọi vẫn chưa được mang ra.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i15",
      "kind": "sentence",
      "example_id": "q15",
      "ja": "これは注文していません。",
      "vi": "Tôi không gọi món này.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    },
    {
      "id": "i16",
      "kind": "sentence",
      "example_id": "q16",
      "ja": "お会計お願いします。",
      "vi": "Cho tôi thanh toán.",
      "authorship": "source_quote",
      "source_refs": [
        "b08_06"
      ]
    }
  ]
}



## Nói số người và nhận bàn [s01]

{
  "id": "s01",
  "source_refs": [],
  "title": "Nói số người và nhận bàn",
  "event_id": "e01",
  "setting": "Hai người tới quán lúc trưa, chưa đặt bàn.",
  "communication_goal": "Hỏi còn bàn và theo nhân viên đến chỗ ngồi.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s01--t01",
      "speaker": "A",
      "ja": "すみません、二人です。席はありますか。",
      "vi": "Xin lỗi, chúng tôi có hai người. Còn bàn không ạ?"
    },
    {
      "id": "s01--t02",
      "speaker": "B",
      "ja": "はい、あります。こちらへどうぞ。",
      "vi": "Vâng, còn ạ. Mời đi lối này."
    },
    {
      "id": "s01--t03",
      "speaker": "A",
      "ja": "ありがとうございます。ここでいいです。",
      "vi": "Cảm ơn. Chỗ này được ạ."
    },
    {
      "id": "s01--t04",
      "speaker": "B",
      "ja": "では、メニューをお持ちします。",
      "vi": "Vậy tôi sẽ mang thực đơn đến."
    }
  ],
  "authorship": "original_extension"
}



## Gọi điện đặt bàn hai người [s22]

{
  "id": "s22",
  "source_refs": [],
  "title": "Gọi điện đặt bàn hai người",
  "event_id": "e01",
  "setting": "Khách gọi cho quán vào buổi chiều để xin bàn lúc bảy giờ tối cùng một người bạn.",
  "communication_goal": "Hỏi bàn còn không, nói số người và xác nhận giờ đặt.",
  "relationship": "Khách và nhân viên quán qua điện thoại; lịch sự, ngắn gọn.",
  "outcome": "reserved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người gọi đặt bàn"
    },
    {
      "id": "B",
      "role": "Người nhận cuộc gọi"
    }
  ],
  "turns": [
    {
      "id": "s22--t01",
      "speaker": "A",
      "ja": "七時に二人で予約したいです。席はありますか。",
      "vi": "Tôi muốn đặt bàn cho hai người lúc bảy giờ. Quán còn bàn không ạ?"
    },
    {
      "id": "s22--t02",
      "speaker": "B",
      "ja": "はい、あります。お名前をお願いします。",
      "vi": "Vâng, còn ạ. Xin cho biết tên quý khách."
    },
    {
      "id": "s22--t03",
      "speaker": "A",
      "ja": "グエンです。七時に二人です。",
      "vi": "Tôi là Nguyen. Hai người lúc bảy giờ ạ."
    },
    {
      "id": "s22--t04",
      "speaker": "B",
      "ja": "グエン様、七時に二名様ですね。",
      "vi": "Anh/chị Nguyen, hai người lúc bảy giờ nhỉ."
    },
    {
      "id": "s22--t05",
      "speaker": "A",
      "ja": "はい、お願いします。",
      "vi": "Vâng, nhờ anh/chị đặt giúp."
    },
    {
      "id": "s22--t06",
      "speaker": "B",
      "ja": "ありがとうございます。お待ちしています。",
      "vi": "Cảm ơn quý khách. Chúng tôi sẽ chờ."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi bàn yên hơn [s02]

{
  "id": "s02",
  "source_refs": [],
  "title": "Hỏi bàn yên hơn",
  "event_id": "e01",
  "setting": "Hai người được dẫn đến bàn gần cửa ra vào; phía trong có bàn còn trống.",
  "communication_goal": "Hỏi có thể ngồi bàn phía trong không.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s02--t01",
      "speaker": "A",
      "ja": "すみません、静かな席はありますか。",
      "vi": "Xin lỗi, có bàn nào yên tĩnh hơn không ạ?"
    },
    {
      "id": "s02--t02",
      "speaker": "B",
      "ja": "はい、あちらの席が静かです。",
      "vi": "Vâng, bàn bên kia yên tĩnh hơn ạ."
    },
    {
      "id": "s02--t03",
      "speaker": "A",
      "ja": "ありがとうございます。あちらにします。",
      "vi": "Cảm ơn. Chúng tôi chọn bàn đó."
    },
    {
      "id": "s02--t04",
      "speaker": "B",
      "ja": "かしこまりました。こちらへどうぞ。",
      "vi": "Vâng. Mời đi lối này."
    }
  ],
  "authorship": "original_extension"
}



## Nhận bàn có giới hạn giờ [s03]

{
  "id": "s03",
  "source_refs": [],
  "title": "Nhận bàn có giới hạn giờ",
  "event_id": "e01",
  "setting": "Quán còn một bàn nhưng cần lấy lại lúc bảy giờ. Hiện là sáu giờ.",
  "communication_goal": "Xác nhận thời gian dùng bàn trước khi nhận.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "conditional",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s03--t01",
      "speaker": "B",
      "ja": "七時までですが、席があります。",
      "vi": "Còn bàn, nhưng chỉ dùng đến bảy giờ ạ."
    },
    {
      "id": "s03--t02",
      "speaker": "A",
      "ja": "今、六時ですね。一時間ですか。",
      "vi": "Bây giờ sáu giờ rồi nhỉ. Vậy là một tiếng ạ?"
    },
    {
      "id": "s03--t03",
      "speaker": "B",
      "ja": "はい、七時までです。よろしいですか。",
      "vi": "Vâng, đến bảy giờ. Quý khách dùng được chứ ạ?"
    },
    {
      "id": "s03--t04",
      "speaker": "A",
      "ja": "はい、大丈夫です。お願いします。",
      "vi": "Vâng, được ạ. Nhờ anh/chị sắp xếp giúp."
    }
  ],
  "authorship": "original_extension"
}



## Hết bàn và hỏi giờ quay lại [s04]

{
  "id": "s04",
  "source_refs": [],
  "title": "Hết bàn và hỏi giờ quay lại",
  "event_id": "e01",
  "setting": "Quán đang kín bàn; khách có thể quay lại sau.",
  "communication_goal": "Hỏi giờ có thể quay lại thay vì chờ vô định.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "pending",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s04--t01",
      "speaker": "A",
      "ja": "二人ですが、席はありますか。",
      "vi": "Chúng tôi có hai người. Còn bàn không ạ?"
    },
    {
      "id": "s04--t02",
      "speaker": "B",
      "ja": "申し訳ありません。今は満席です。",
      "vi": "Rất xin lỗi. Hiện quán đã kín bàn."
    },
    {
      "id": "s04--t03",
      "speaker": "A",
      "ja": "何時ごろなら空きますか。",
      "vi": "Khoảng mấy giờ thì có bàn ạ?"
    },
    {
      "id": "s04--t04",
      "speaker": "B",
      "ja": "七時ごろです。",
      "vi": "Khoảng bảy giờ ạ."
    },
    {
      "id": "s04--t05",
      "speaker": "A",
      "ja": "分かりました。七時ごろ、また来ます。",
      "vi": "Tôi hiểu rồi. Khoảng bảy giờ chúng tôi sẽ quay lại."
    }
  ],
  "authorship": "original_extension"
}



## Xác nhận bàn sau khi quay lại [s05]

{
  "id": "s05",
  "source_refs": [],
  "title": "Xác nhận bàn sau khi quay lại",
  "event_id": "e01",
  "setting": "Hai khách quay lại vào bảy giờ sau khi quán báo hết chỗ.",
  "communication_goal": "Nhắc việc đã hỏi trước và xác nhận bàn còn trống.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [
    "s04"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s05--t01",
      "speaker": "A",
      "ja": "七時ごろに来ました。二人です。席はありますか。",
      "vi": "Chúng tôi quay lại lúc bảy giờ. Có hai người. Còn bàn không ạ?"
    },
    {
      "id": "s05--t02",
      "speaker": "B",
      "ja": "はい、今、席が空いています。こちらへどうぞ。",
      "vi": "Vâng, hiện có bàn trống. Mời đi lối này."
    },
    {
      "id": "s05--t03",
      "speaker": "A",
      "ja": "ありがとうございます。ここでいいです。",
      "vi": "Cảm ơn. Bàn này được ạ."
    }
  ],
  "authorship": "original_extension"
}



## Từ để chọn và gọi món [v02]

{
  "id": "v02",
  "source_refs": [],
  "items": [
    {
      "id": "v02-w-979d721bde05",
      "ja": "カレー",
      "source_refs": []
    },
    {
      "id": "v02-w-04c2cf5dd7c4",
      "ja": "サラダ",
      "source_refs": []
    },
    {
      "id": "v02-w-9ef3f345dbc4",
      "ja": "少ない",
      "source_refs": []
    },
    {
      "id": "v02-w-d9a111f6526e",
      "ja": "辛い",
      "source_refs": []
    },
    {
      "id": "v02-w-29304473e83f",
      "ja": "入る",
      "source_refs": []
    },
    {
      "id": "v02-w-bc4b199bb4d0",
      "ja": "足りる",
      "source_refs": []
    },
    {
      "id": "v02-w-522bf697a5f8",
      "ja": "待つ",
      "source_refs": []
    },
    {
      "id": "v02-w-327b54d04f71",
      "ja": "水",
      "source_refs": []
    },
    {
      "id": "v02-w-22592e3d0e1c",
      "ja": "箸",
      "source_refs": []
    }
  ]
}



## Mẫu chọn món và hỏi thành phần [g02]

{
  "id": "g02",
  "source_refs": [
    "grammar_m"
  ],
  "items": [
    {
      "id": "g02-g-87a82d22f4e7",
      "name_ja": "Nにします",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g02-g-96dd40503007",
      "name_ja": "Vています（結果の状態）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g02-g-4f7d17723ebe",
      "name_ja": "〜んです／んですか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g02-g-2a6692689c28",
      "name_ja": "可能動詞",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Chọn món: hỏi một điều mỗi lượt [k02]

# Xem món, hỏi rõ rồi mới chốt số suất

Khi thực đơn có ảnh, chỉ vào ảnh và hỏi tên món. Sau đó hỏi riêng điều bạn cần biết: món cay không, một suất dành cho mấy người, hoặc có thành phần bạn không ăn được không. Hỏi từng điều giúp nhân viên trả lời chính xác và giúp bạn quyết định nhanh hơn.

Nếu nhân viên chưa chắc thành phần, để họ kiểm tra rồi nghe câu trả lời cuối. Một lời “để tôi hỏi lại” chưa phải xác nhận món không chứa thành phần ấy. Nếu món đã hết, hỏi món thay thế và gọi lại tên cùng số suất của món mới.

Khi gọi món, nói tên món rồi số suất. Nhân viên thường nhắc lại; hãy nghe số trước khi xác nhận. Nếu họ nói một suất nhưng bạn cần hai, sửa ngay bằng một câu ngắn. Có thể nhắc cả đơn sau khi sửa để chắc rằng món, số suất và đồ uống đều đúng.

Bốn câu dưới đây lần lượt dùng để xin thực đơn, chọn món, hỏi món gợi ý và kiểm thành phần:

<a id="q01"></a>
メニューを見せてもらえますか。

Cho tôi xem thực đơn được không?

<a id="q09"></a>
私はこれにします。さくらさんは何にしますか。

Tôi chọn món này. Sakura, bạn chọn món gì?

<a id="q10"></a>
おすすめは何ですか。

Món nào được quán gợi ý?

<a id="q11"></a>
これは豚肉が入っていますか。

Món này có thịt lợn không?


## Hỏi tên món trong ảnh [s06]

{
  "id": "s06",
  "source_refs": [],
  "title": "Hỏi tên món trong ảnh",
  "event_id": "e02",
  "setting": "Khách xem thực đơn có ảnh nhưng không đọc được tên món.",
  "communication_goal": "Hỏi tên và quyết định gọi món.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s06--t01",
      "speaker": "A",
      "ja": "すみません、この写真の料理は何ですか。",
      "vi": "Xin lỗi, món trong ảnh này là món gì ạ?"
    },
    {
      "id": "s06--t02",
      "speaker": "B",
      "ja": "チキンカレーです。",
      "vi": "Đó là cà ri gà ạ."
    },
    {
      "id": "s06--t03",
      "speaker": "A",
      "ja": "辛いですか。",
      "vi": "Món đó cay không ạ?"
    },
    {
      "id": "s06--t04",
      "speaker": "B",
      "ja": "少し辛いです。",
      "vi": "Hơi cay ạ."
    },
    {
      "id": "s06--t05",
      "speaker": "A",
      "ja": "では、これを一つお願いします。",
      "vi": "Vậy cho tôi một phần món này ạ."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi một suất có đủ cho hai người [s07]

{
  "id": "s07",
  "source_refs": [],
  "title": "Hỏi một suất có đủ cho hai người",
  "event_id": "e02",
  "setting": "Hai người định gọi chung một món trước khi gọi thêm.",
  "communication_goal": "Hỏi một suất có đủ cho hai người không, rồi quyết định số suất.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s07--t01",
      "speaker": "A",
      "ja": "二人で食べたいです。一つで足りますか。",
      "vi": "Hai người chúng tôi muốn ăn chung. Một suất có đủ không ạ?"
    },
    {
      "id": "s07--t02",
      "speaker": "B",
      "ja": "一人前は少ないです。二つがいいですよ。",
      "vi": "Một suất thì hơi ít. Hai suất sẽ vừa hơn ạ."
    },
    {
      "id": "s07--t03",
      "speaker": "A",
      "ja": "そうですか。では、二つお願いします。",
      "vi": "Vậy ạ. Cho chúng tôi hai suất."
    },
    {
      "id": "s07--t04",
      "speaker": "B",
      "ja": "かしこまりました。二つですね。",
      "vi": "Vâng, hai suất nhỉ."
    }
  ],
  "authorship": "original_extension"
}



## Gọi món và số suất [s08]

{
  "id": "s08",
  "source_refs": [],
  "title": "Gọi món và số suất",
  "event_id": "e02",
  "setting": "Hai khách đã chọn xong món tại bàn.",
  "communication_goal": "Gọi món, nước và nghe nhân viên xác nhận.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s08--t01",
      "speaker": "A",
      "ja": "すみません、注文をお願いします。カレーを二つと、サラダを一つください。",
      "vi": "Xin lỗi, cho chúng tôi gọi món. Hai phần cà ri và một phần sa lát ạ."
    },
    {
      "id": "s08--t02",
      "speaker": "B",
      "ja": "カレーが二つ、サラダが一つですね。お飲み物は？",
      "vi": "Hai cà ri và một sa lát nhỉ. Còn đồ uống ạ?"
    },
    {
      "id": "s08--t03",
      "speaker": "A",
      "ja": "水を二つお願いします。",
      "vi": "Cho hai cốc nước ạ."
    },
    {
      "id": "s08--t04",
      "speaker": "B",
      "ja": "かしこまりました。",
      "vi": "Vâng ạ."
    }
  ],
  "authorship": "original_extension"
}



## Sửa khi nhân viên nghe nhầm số suất [s09]

{
  "id": "s09",
  "source_refs": [],
  "title": "Sửa khi nhân viên nghe nhầm số suất",
  "event_id": "e02",
  "setting": "Khách gọi hai phần cà ri; nhân viên nghe thành một phần.",
  "communication_goal": "Sửa số suất và nghe lại xác nhận.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "corrected",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s09--t01",
      "speaker": "B",
      "ja": "カレーを一つですね。",
      "vi": "Một phần cà ri ạ."
    },
    {
      "id": "s09--t02",
      "speaker": "A",
      "ja": "すみません、一つではなく、二つです。",
      "vi": "Xin lỗi, không phải một mà là hai phần ạ."
    },
    {
      "id": "s09--t03",
      "speaker": "B",
      "ja": "失礼しました。カレーを二つですね。",
      "vi": "Xin lỗi quý khách. Hai phần cà ri ạ."
    },
    {
      "id": "s09--t04",
      "speaker": "A",
      "ja": "はい、二つです。",
      "vi": "Vâng, hai phần ạ."
    }
  ],
  "authorship": "original_extension"
}



## Nhắc lại toàn bộ món đã gọi [s10]

{
  "id": "s10",
  "source_refs": [],
  "title": "Nhắc lại toàn bộ món đã gọi",
  "event_id": "e02",
  "setting": "Sau khi sửa số suất cà ri, khách muốn kiểm cả đơn trước khi nhân viên đi.",
  "communication_goal": "Xác nhận toàn bộ món và nước.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [
    "s09"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s10--t01",
      "speaker": "A",
      "ja": "カレーを二つ、サラダを一つ、水を二つです。",
      "vi": "Hai cà ri, một sa lát và hai cốc nước ạ."
    },
    {
      "id": "s10--t02",
      "speaker": "B",
      "ja": "はい、そのとおりです。",
      "vi": "Vâng, đúng như vậy ạ."
    },
    {
      "id": "s10--t03",
      "speaker": "A",
      "ja": "お願いします。",
      "vi": "Nhờ anh/chị ạ."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi món có thịt lợn không [s11]

{
  "id": "s11",
  "source_refs": [],
  "title": "Hỏi món có thịt lợn không",
  "event_id": "e02",
  "setting": "Một khách muốn kiểm thành phần trước khi gọi món; thực đơn không ghi rõ.",
  "communication_goal": "Hỏi thành phần, nhận câu trả lời rồi chọn món.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s11--t01",
      "speaker": "A",
      "ja": "すみません、これは豚肉が入っていますか。",
      "vi": "Xin lỗi, món này có thịt lợn không ạ?"
    },
    {
      "id": "s11--t02",
      "speaker": "B",
      "ja": "確認します。少々お待ちください。",
      "vi": "Để tôi kiểm tra. Xin chờ một chút."
    },
    {
      "id": "s11--t03",
      "speaker": "B",
      "ja": "お待たせしました。豚肉は入っていません。",
      "vi": "Xin lỗi đã để quý khách chờ. Món này không có thịt lợn ạ."
    },
    {
      "id": "s11--t04",
      "speaker": "A",
      "ja": "分かりました。では、これをお願いします。",
      "vi": "Tôi hiểu rồi. Vậy cho tôi món này ạ."
    }
  ],
  "authorship": "original_extension"
}



## Hết món và chọn món khác [s12]

{
  "id": "s12",
  "source_refs": [],
  "title": "Hết món và chọn món khác",
  "event_id": "e02",
  "setting": "Khách gọi cà ri nhưng quán đã bán hết; vẫn có cơm gà.",
  "communication_goal": "Chọn món thay thế sau lời báo hết món.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "alternative",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s12--t01",
      "speaker": "A",
      "ja": "カレーを一つお願いします。",
      "vi": "Cho tôi một phần cà ri ạ."
    },
    {
      "id": "s12--t02",
      "speaker": "B",
      "ja": "申し訳ありません。カレーはもうありません。",
      "vi": "Rất xin lỗi. Cà ri đã hết rồi ạ."
    },
    {
      "id": "s12--t03",
      "speaker": "A",
      "ja": "そうですか。チキンライスはありますか。",
      "vi": "Vậy ạ. Cơm gà còn không ạ?"
    },
    {
      "id": "s12--t04",
      "speaker": "B",
      "ja": "はい、あります。",
      "vi": "Vâng, còn ạ."
    },
    {
      "id": "s12--t05",
      "speaker": "A",
      "ja": "では、チキンライスを一つお願いします。",
      "vi": "Vậy cho tôi một phần cơm gà ạ."
    }
  ],
  "authorship": "original_extension"
}



## Từ dùng trong bữa và khi thanh toán [v03]

{
  "id": "v03",
  "source_refs": [],
  "items": [
    {
      "id": "v03-w-319df777c4a4",
      "ja": "まだ",
      "source_refs": []
    },
    {
      "id": "v03-w-792ec616b4c0",
      "ja": "来る",
      "source_refs": []
    },
    {
      "id": "v03-w-327b54d04f71",
      "ja": "水",
      "source_refs": []
    },
    {
      "id": "v03-w-22592e3d0e1c",
      "ja": "箸",
      "source_refs": []
    },
    {
      "id": "v03-w-c2d344b1bdc3",
      "ja": "確認する",
      "source_refs": []
    },
    {
      "id": "v03-w-1822aa2f0bf7",
      "ja": "会計",
      "source_refs": []
    },
    {
      "id": "v03-w-f7fedf35dec3",
      "ja": "別々",
      "source_refs": []
    },
    {
      "id": "v03-w-9e18b24236e4",
      "ja": "お釣り",
      "source_refs": []
    },
    {
      "id": "v03-w-2a438695d5f5",
      "ja": "忘れる",
      "source_refs": []
    }
  ]
}



## Mẫu để hỏi lại và giải quyết [g03]

{
  "id": "g03",
  "source_refs": [
    "grammar_m"
  ],
  "items": [
    {
      "id": "g03-g-e8fb271526f3",
      "name_ja": "Vてください",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g03-g-785102d73d16",
      "name_ja": "Vてもいいですか",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g03-g-96dd40503007",
      "name_ja": "Vています（結果の状態）",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g03-g-a482f09d9eb2",
      "name_ja": "Vた／Nの＋あとで",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g03-g-f1eefc720467",
      "name_ja": "〜かもしれません",
      "jlpt_level": "N4",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g03-g-c4ab9b349b4b",
      "name_ja": "Vます形／N＋に行きます",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Trong bữa: báo việc cụ thể, chờ bước xử lý [k03]

# Trong bữa: nói điều đang thiếu và đợi phản hồi

Gọi nhân viên bằng một lời mở ngắn, rồi nói rõ món nào chưa đến. Nếu các món khác đã được mang ra, nêu tên món còn thiếu để họ kiểm đơn nhanh. Khi nhân viên nói sẽ kiểm tra, chờ câu trả lời tiếp theo; đừng xem đó là lời hứa về số phút nếu họ chưa nêu thời gian.

Khi món được mang tới khác món bạn gọi, chỉ ra hai tên món: món bạn đã đặt và món đang ở trên bàn. Cách nói này giúp nhân viên xác nhận nhầm ở đâu. Đợi họ kiểm đơn, rồi xác nhận lại khi món đúng được mang tới.

Với yêu cầu nhỏ như thêm nước hoặc đũa, nói số lượng cùng đồ cần thêm. Nhân viên có thể mang tới ngay hoặc báo phải chờ. Nếu câu trả lời chưa rõ, bạn có thể hỏi lại một lần ngắn.

Phân biệt “món đã gọi chưa tới” với “món này tôi không gọi” qua hai câu sau:

<a id="q14"></a>
注文したものが来ないんですが。

Món tôi gọi vẫn chưa được mang ra.

<a id="q15"></a>
これは注文していません。

Tôi không gọi món này.


## Xin thêm nước và đũa [s13]

{
  "id": "s13",
  "source_refs": [],
  "title": "Xin thêm nước và đũa",
  "event_id": "e03",
  "setting": "Trong bữa ăn, hai khách cần thêm nước và một đôi đũa.",
  "communication_goal": "Nhờ nhân viên mang thêm đồ.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s13--t01",
      "speaker": "A",
      "ja": "すみません、水をもう一つと、箸を一膳ください。",
      "vi": "Xin lỗi, cho thêm một cốc nước và một đôi đũa ạ."
    },
    {
      "id": "s13--t02",
      "speaker": "B",
      "ja": "はい、すぐお持ちします。",
      "vi": "Vâng, tôi sẽ mang tới ngay."
    },
    {
      "id": "s13--t03",
      "speaker": "A",
      "ja": "ありがとうございます。",
      "vi": "Cảm ơn ạ."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi món còn đang chờ [s14]

{
  "id": "s14",
  "source_refs": [],
  "title": "Hỏi món còn đang chờ",
  "event_id": "e03",
  "setting": "Khách đã gọi một phần cà ri nhưng món chưa đến; các món khác đã lên bàn.",
  "communication_goal": "Nói rõ món còn thiếu và hỏi nhân viên kiểm tra.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "pending",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s14--t01",
      "speaker": "A",
      "ja": "すみません、カレーを注文しましたが、まだ来ていません。",
      "vi": "Xin lỗi, tôi đã gọi cà ri nhưng món vẫn chưa tới ạ."
    },
    {
      "id": "s14--t02",
      "speaker": "B",
      "ja": "申し訳ありません。すぐ確認します。",
      "vi": "Rất xin lỗi. Tôi sẽ kiểm tra ngay."
    },
    {
      "id": "s14--t03",
      "speaker": "A",
      "ja": "お願いします。",
      "vi": "Nhờ anh/chị ạ."
    },
    {
      "id": "s14--t04",
      "speaker": "B",
      "ja": "あと五分ぐらいです。",
      "vi": "Khoảng năm phút nữa ạ."
    },
    {
      "id": "s14--t05",
      "speaker": "A",
      "ja": "分かりました。待ちます。",
      "vi": "Tôi hiểu rồi. Tôi sẽ chờ."
    }
  ],
  "authorship": "original_extension"
}



## Nhận món khác với món đã gọi [s15]

{
  "id": "s15",
  "source_refs": [],
  "title": "Nhận món khác với món đã gọi",
  "event_id": "e03",
  "setting": "Nhân viên mang cơm gà tới, nhưng khách đã gọi cà ri.",
  "communication_goal": "Nêu chỗ khác nhau và nhờ kiểm tra.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "pending",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s15--t01",
      "speaker": "B",
      "ja": "お待たせしました。チキンライスです。",
      "vi": "Xin lỗi đã để quý khách chờ. Cơm gà đây ạ."
    },
    {
      "id": "s15--t02",
      "speaker": "A",
      "ja": "すみません、私はカレーを注文しました。これはチキンライスですね。",
      "vi": "Xin lỗi, tôi đã gọi cà ri. Món này là cơm gà nhỉ."
    },
    {
      "id": "s15--t03",
      "speaker": "B",
      "ja": "失礼しました。注文を確認します。",
      "vi": "Xin lỗi quý khách. Tôi sẽ kiểm tra đơn."
    },
    {
      "id": "s15--t04",
      "speaker": "A",
      "ja": "お願いします。",
      "vi": "Nhờ anh/chị ạ."
    }
  ],
  "authorship": "original_extension"
}



## Nhận đúng món sau khi quán kiểm tra [s16]

{
  "id": "s16",
  "source_refs": [],
  "title": "Nhận đúng món sau khi quán kiểm tra",
  "event_id": "e03",
  "setting": "Nhân viên đã mang nhầm cơm gà và nay quay lại với cà ri.",
  "communication_goal": "Xác nhận đúng món và tiếp tục bữa ăn.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [
    "s15"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s16--t01",
      "speaker": "B",
      "ja": "お待たせしました。ご注文のカレーです。",
      "vi": "Xin lỗi đã để quý khách chờ. Đây là cà ri quý khách đã gọi."
    },
    {
      "id": "s16--t02",
      "speaker": "A",
      "ja": "はい、これです。ありがとうございます。",
      "vi": "Vâng, đúng món này rồi. Cảm ơn ạ."
    },
    {
      "id": "s16--t03",
      "speaker": "B",
      "ja": "どうぞ、ごゆっくり。",
      "vi": "Mời quý khách dùng bữa thong thả."
    }
  ],
  "authorship": "original_extension"
}



## Thanh toán: nghe lại số tiền và kiểm món [k04]

# Tính tiền và khép lại việc còn dang dở

Trước khi trả, hỏi quán tính ở bàn hay tại quầy nếu bạn chưa rõ. Nếu hai người muốn trả riêng, hỏi ngay trước lúc thu ngân lập hóa đơn. Quán có thể đồng ý hoặc chỉ nhận một lần thanh toán; khi đó hãy chọn ai trả ở quầy rồi hai người tự chia sau.

Nếu thấy món không gọi trên hóa đơn, nêu đúng tên món và để nhân viên kiểm lại. Chỉ xác nhận số tiền sau khi đã nghe tổng mới. Khi trả tiền mặt, nhắc lại tổng và số tiền đưa nếu cần để tránh nghe nhầm.

Sau khi rời quán, nếu nghi để quên đồ, gọi lại và nói ngắn thời điểm dùng bữa, màu hoặc đặc điểm của món đồ. Hỏi quán đã thấy chưa; chỉ hẹn đến lấy sau khi nhân viên xác nhận đang giữ đồ.

Câu xin thanh toán và câu báo món lạ trên hóa đơn:

<a id="q16"></a>
お会計お願いします。

Cho tôi thanh toán.

<a id="s19_u01"></a>
すみません、このサラダは注文していません。

Xin lỗi, chúng tôi không gọi phần sa lát này ạ.


## Hỏi thanh toán riêng [s17]

{
  "id": "s17",
  "source_refs": [],
  "title": "Hỏi thanh toán riêng",
  "event_id": "e04",
  "setting": "Hai khách muốn mỗi người trả phần mình đã gọi.",
  "communication_goal": "Hỏi quán có thể tính riêng và chấp nhận cách quán thực hiện.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s17--t01",
      "speaker": "A",
      "ja": "すみません、別々に払ってもいいですか。",
      "vi": "Xin lỗi, chúng tôi trả riêng được không ạ?"
    },
    {
      "id": "s17--t02",
      "speaker": "B",
      "ja": "はい、できます。何を注文しましたか。",
      "vi": "Vâng, được ạ. Quý khách đã gọi món nào?"
    },
    {
      "id": "s17--t03",
      "speaker": "A",
      "ja": "私はカレーと水です。",
      "vi": "Tôi gọi cà ri và nước ạ."
    },
    {
      "id": "s17--t04",
      "speaker": "B",
      "ja": "かしこまりました。こちらの分からお会計します。",
      "vi": "Vâng. Tôi sẽ tính phần này trước."
    }
  ],
  "authorship": "original_extension"
}



## Quán không thể tính riêng [s18]

{
  "id": "s18",
  "source_refs": [],
  "title": "Quán không thể tính riêng",
  "event_id": "e04",
  "setting": "Hai khách hỏi trả riêng nhưng quán chỉ tính một hóa đơn cho bàn.",
  "communication_goal": "Nghe điều kiện và chọn một người trả ở quầy.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "alternative",
  "follows": [],
  "alternative_to": [
    "s17"
  ],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s18--t01",
      "speaker": "A",
      "ja": "別々に払えますか。",
      "vi": "Chúng tôi trả riêng được không ạ?"
    },
    {
      "id": "s18--t02",
      "speaker": "B",
      "ja": "申し訳ありません。お会計は一緒でお願いします。",
      "vi": "Xin lỗi, xin quý khách thanh toán chung ạ."
    },
    {
      "id": "s18--t03",
      "speaker": "A",
      "ja": "分かりました。私がまとめて払います。",
      "vi": "Tôi hiểu rồi. Tôi sẽ trả chung ạ."
    },
    {
      "id": "s18--t04",
      "speaker": "B",
      "ja": "ありがとうございます。こちらでお願いします。",
      "vi": "Cảm ơn quý khách. Xin thanh toán ở đây ạ."
    }
  ],
  "authorship": "original_extension"
}



## Chỉ ra món không gọi trên hóa đơn [s19]

{
  "id": "s19",
  "source_refs": [],
  "title": "Chỉ ra món không gọi trên hóa đơn",
  "event_id": "e04",
  "setting": "Khách thấy hóa đơn có thêm một phần sa lát mà bàn mình không gọi.",
  "communication_goal": "Báo đúng món có vấn đề và yêu cầu kiểm tra.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "pending",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s19--t01",
      "speaker": "A",
      "ja": "すみません、このサラダは注文していません。",
      "vi": "Xin lỗi, chúng tôi không gọi phần sa lát này ạ."
    },
    {
      "id": "s19--t02",
      "speaker": "B",
      "ja": "失礼しました。確認します。",
      "vi": "Xin lỗi quý khách. Tôi sẽ kiểm tra."
    },
    {
      "id": "s19--t03",
      "speaker": "A",
      "ja": "お願いします。",
      "vi": "Nhờ anh/chị ạ."
    }
  ],
  "authorship": "original_extension"
}



## Thanh toán sau khi sửa hóa đơn [s20]

{
  "id": "s20",
  "source_refs": [],
  "title": "Thanh toán sau khi sửa hóa đơn",
  "event_id": "e04",
  "setting": "Nhân viên đã kiểm tra và bỏ phần sa lát ghi nhầm khỏi hóa đơn.",
  "communication_goal": "Nghe tổng tiền mới và thanh toán.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "resolved",
  "follows": [
    "s19"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s20--t01",
      "speaker": "B",
      "ja": "お待たせしました。サラダを外しました。全部で千八百円です。",
      "vi": "Xin lỗi đã để quý khách chờ. Tôi đã bỏ phần sa lát khỏi hóa đơn. Tổng cộng là 1.800 yên ạ."
    },
    {
      "id": "s20--t02",
      "speaker": "A",
      "ja": "千八百円ですね。二千円でお願いします。",
      "vi": "1.800 yên nhỉ. Tôi gửi 2.000 yên ạ."
    },
    {
      "id": "s20--t03",
      "speaker": "B",
      "ja": "二百円のお釣りです。",
      "vi": "Tiền thừa 200 yên ạ."
    },
    {
      "id": "s20--t04",
      "speaker": "A",
      "ja": "ありがとうございます。",
      "vi": "Cảm ơn ạ."
    }
  ],
  "authorship": "original_extension"
}



## Gọi quán hỏi đồ để quên [s21]

{
  "id": "s21",
  "source_refs": [],
  "title": "Gọi quán hỏi đồ để quên",
  "event_id": "e04",
  "setting": "Sau bữa tối, khách gọi lại quán vì có thể để quên một chiếc ô đen.",
  "communication_goal": "Nói lúc đã dùng bữa và hỏi quán đã thấy ô chưa.",
  "relationship": "Khách và nhân viên quán; nói lịch sự, ngắn gọn.",
  "outcome": "follow_up",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người dùng bữa"
    },
    {
      "id": "B",
      "role": "Nhân viên quán"
    }
  ],
  "turns": [
    {
      "id": "s21--t01",
      "speaker": "A",
      "ja": "もしもし。今日の七時ごろ、そちらで食事をしました。黒い傘を忘れたかもしれません。",
      "vi": "A lô. Khoảng bảy giờ hôm nay tôi đã ăn ở quán. Có thể tôi để quên một chiếc ô đen."
    },
    {
      "id": "s21--t02",
      "speaker": "B",
      "ja": "黒い傘ですね。少々お待ちください。確認します。",
      "vi": "Ô đen nhỉ. Xin chờ một chút, tôi sẽ kiểm tra."
    },
    {
      "id": "s21--t03",
      "speaker": "B",
      "ja": "ありました。お店で預かっています。",
      "vi": "Có rồi ạ. Quán đang giữ giúp."
    },
    {
      "id": "s21--t04",
      "speaker": "A",
      "ja": "ありがとうございます。明日、取りに行きます。",
      "vi": "Cảm ơn ạ. Mai tôi sẽ đến lấy."
    }
  ],
  "authorship": "original_extension"
}



## Trò chuyện tự do về một bữa ăn ngoài [ft01]

{
  "id": "ft01",
  "source_refs": [],
  "context_node_ids": [
    "v01",
    "g01",
    "k01",
    "g_ref",
    "sh01",
    "s01",
    "s22",
    "s02",
    "s03",
    "s04",
    "s05",
    "v02",
    "g02",
    "k02",
    "s06",
    "s07",
    "s08",
    "s09",
    "s10",
    "s11",
    "s12",
    "v03",
    "g03",
    "k03",
    "s13",
    "s14",
    "s15",
    "s16",
    "k04",
    "s17",
    "s18",
    "s19",
    "s20",
    "s21"
  ],
  "overview_vi": "Vào quán, hỏi bàn và món, gọi đúng số suất, xử lý thay đổi nhỏ trong bữa, kiểm hóa đơn và liên hệ lại khi để quên đồ. Chỉ luyện nghe và nói.",
  "optional_extensions": [],
  "context_export": "live-context.md",
  "free_talk": {
    "learner_intro_vi": "Hãy trò chuyện về một bữa ăn ngoài mà bạn muốn thử hoặc từng gặp. Có thể bắt đầu từ tìm chỗ, chọn món, chuyện trong bữa hay lúc thanh toán; bạn được đổi hướng theo điều mình muốn kể.",
    "ai_situation_vi": "Trò chuyện bằng tiếng Nhật ngắn và tự nhiên với người học về một bữa ăn tại quán. Trước tiên hỏi người học thích đi quán kiểu nào hoặc đã từng gặp chuyện gì khi gọi món. Theo câu trả lời để nói sâu một mạch: đến quán và hỏi bàn; xem ảnh và hỏi món; nói số suất, thành phần; đợi món, báo món khác; thanh toán riêng hoặc kiểm hóa đơn; gọi lại vì để quên đồ. Dùng vốn câu ở tài liệu như gợi ý, không ép người học đi đủ các cảnh, không kiểm tra hay chấm điểm. Khi người học bí, gợi một câu hỏi đơn giản và chờ họ tự nói. Giữ nhất quán vai trò; nếu đang là bạn đồng hành, đừng đột ngột đóng vai nhân viên trừ khi người học muốn nhập vai. Các món, giờ và giá trong hội thoại là giả định, không khẳng định quy định chung của mọi quán.",
    "conversation_starters_vi": [
      "Bạn thường hỏi điều gì trước khi gọi một món lạ?",
      "Nếu quán hết món bạn định gọi, bạn sẽ hỏi gì tiếp?",
      "Bạn đã từng cần nhờ nhân viên kiểm lại món hoặc hóa đơn chưa?"
    ],
    "mode": "free_talk",
    "content_origin": "curriculum_authored",
    "situation_export": "free-talk-situation.md"
  }
}



## Bài học và nội dung gối đầu

{
  "schema_version": "1.0",
  "stage_uid": "72d35860-f51f-5d26-b6c8-489bed15a13f",
  "lessons": [
    {
      "id": "l01",
      "summary": "Vào quán và nghe câu phục vụ",
      "node_ids": [
        "v01",
        "g01",
        "k01",
        "g_ref",
        "sh01"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l02",
      "summary": "Chọn chỗ và xử lý khi hết bàn",
      "node_ids": [
        "s01",
        "s22",
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
      "id": "l03",
      "summary": "Hỏi món và xác nhận đơn",
      "node_ids": [
        "v02",
        "g02",
        "k02",
        "s06",
        "s07",
        "s08",
        "s09",
        "s10",
        "s11",
        "s12"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l04",
      "summary": "Trong bữa ăn và xử lý món sai",
      "node_ids": [
        "v03",
        "g03",
        "k03",
        "s13",
        "s14",
        "s15",
        "s16"
      ],
      "lookback": [],
      "reuse": [],
      "pending_previous": []
    },
    {
      "id": "l05",
      "summary": "Thanh toán và liên hệ sau bữa",
      "node_ids": [
        "k04",
        "s17",
        "s18",
        "s19",
        "s20",
        "s21"
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
      "status": "read",
      "note": "Đọc phần nhà hàng đã chọn."
    },
    {
      "book_id": "B02",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B03",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B04",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B05",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B06",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B07",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B08",
      "status": "read",
      "note": "Đọc phần nhà hàng đã chọn."
    },
    {
      "book_id": "B09",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B10",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B11",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B12",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B13",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B14",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B15",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B16",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B17",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B18",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B19",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B20",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B21",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B22",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B23",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B24",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B25",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B26",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    },
    {
      "book_id": "B27",
      "status": "index_only",
      "note": "Quét danh mục 27 sách theo topic; không nhận là đã đọc nội dung."
    }
  ],
  "entries": [
    {
      "id": "b08_05",
      "kind": "book",
      "book_id": "B08",
      "path": "kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md",
      "locator": {
        "heading": "05 レストラン・喫茶店で①, trang 126–127"
      },
      "sha256": "ba773e01d02ce1bb2e8ada8ccb568e9c870c4c045186011519865fe785a953cd",
      "read_status": "read",
      "used_for": [
        "k02",
        "sh01"
      ],
      "contribution": "Câu mẫu trọn đơn vị về xem thực đơn và gọi món."
    },
    {
      "id": "b08_06",
      "kind": "book",
      "book_id": "B08",
      "path": "kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md",
      "locator": {
        "heading": "06 レストラン・喫茶店で②, trang 128–129"
      },
      "sha256": "ba773e01d02ce1bb2e8ada8ccb568e9c870c4c045186011519865fe785a953cd",
      "read_status": "read",
      "used_for": [
        "k02",
        "k03",
        "k04",
        "sh01"
      ],
      "contribution": "Câu mẫu trọn đơn vị về chọn món, thành phần, món chưa tới và thanh toán."
    },
    {
      "id": "b01_seat",
      "kind": "book",
      "book_id": "B01",
      "path": "kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/05-am-thuc.md",
      "locator": {
        "heading": "Ẩm thực, mục 4 Đặt chỗ, trang 117–118"
      },
      "sha256": "1f71b5c9c65ec81df97233506ed031f0b58b98bc611008651526b6b2d6a88830",
      "read_status": "read",
      "used_for": [
        "k01"
      ],
      "contribution": "Tham khảo các cách hỏi chỗ và phản hồi."
    },
    {
      "id": "b01_pay",
      "kind": "book",
      "book_id": "B01",
      "path": "kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/05-am-thuc.md",
      "locator": {
        "heading": "Ẩm thực, mục 7 Thanh toán, trang 120–121"
      },
      "sha256": "1f71b5c9c65ec81df97233506ed031f0b58b98bc611008651526b6b2d6a88830",
      "read_status": "read",
      "used_for": [
        "k04"
      ],
      "contribution": "Tham khảo cách hỏi tính tiền và chia thanh toán; bỏ câu Nhật bất thường."
    },
    {
      "id": "original",
      "kind": "original",
      "locator": {
        "stage": "S-031",
        "scope": "22 hội thoại tình huống, kiến thức hướng dẫn và context Live do AI soạn"
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
        "s22"
      ],
      "contribution": "Hội thoại mới theo seed và mở rộng có diễn biến; không gán sách hoặc CD."
    },
    {
      "id": "grammar_m",
      "kind": "reference",
      "path": "kaiwa_skill/reference/grammar/MINNA_01_50_GRAMMAR.json",
      "locator": {
        "lessons": [
          9,
          10,
          14,
          15,
          24,
          26,
          27,
          32,
          34,
          35,
          49
        ]
      },
      "sha256": "77503e668fd152260f34a49c18986030209779df413b52822b78eeffd42b73d2",
      "read_status": "read",
      "used_for": [
        "g01",
        "g02",
        "g03",
        "g_ref"
      ],
      "contribution": "Đối chiếu tên mẫu. JLPT là phân loại biên tập theo cách dùng thực, không phải bảng JLPT chính thức."
    }
  ]
}

