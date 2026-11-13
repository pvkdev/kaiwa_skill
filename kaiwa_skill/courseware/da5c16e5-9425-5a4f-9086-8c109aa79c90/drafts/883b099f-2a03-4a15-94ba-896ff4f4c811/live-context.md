# Tàu điện & xe buýt

{
  "schema_version": "3.2-draft",
  "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
  "display_code": "S-011",
  "title": "Tàu điện & xe buýt",
  "level": "Sơ",
  "scope": "Tự hỏi và xác nhận tuyến, điểm đổi tàu, cửa lên xe buýt và lối cần hỗ trợ. Ga あおば・さくら・みどり, tuyến, sân ga, xe buýt và thời gian trong ví dụ là giả định để luyện nói; không dùng làm hướng dẫn hành trình thật.",
  "events": [
    {
      "id": "E01",
      "title": "Chọn tàu và chuyển tuyến",
      "situation_ids": [
        "S001",
        "S002",
        "S003",
        "S004",
        "S005"
      ]
    },
    {
      "id": "E02",
      "title": "Đi xe buýt",
      "situation_ids": [
        "S006",
        "S007",
        "S008",
        "S009",
        "S010"
      ]
    },
    {
      "id": "E03",
      "title": "Nhờ hỗ trợ ở ga",
      "situation_ids": [
        "S011",
        "S012",
        "S013",
        "S014",
        "S015"
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


## Tuyến, sân ga và hướng đi [v01]

{
  "id": "v01",
  "source_refs": [],
  "items": [
    {
      "id": "v01-w-53e5e276999d",
      "ja": "駅",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-92e4d1d0c7a5",
      "ja": "電車",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-eb5f20728ecc",
      "ja": "地下鉄",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-3591416633b9",
      "ja": "路線",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-8bc0d9d711df",
      "ja": "路線図",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-49339890223b",
      "ja": "ホーム",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-40df685932a3",
      "ja": "番線",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-2f0ba088d763",
      "ja": "改札",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-1a7930272017",
      "ja": "入口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-7016090059bd",
      "ja": "出口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-524cf02384b2",
      "ja": "東口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-b87fc48997f4",
      "ja": "西口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-5f8118b538fc",
      "ja": "北口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-c9e911b9d487",
      "ja": "南口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-f1d021640a1a",
      "ja": "行き",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-3fc5b79e6d29",
      "ja": "方面",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-6e724a72699e",
      "ja": "乗り換え",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-daeff88261e6",
      "ja": "各駅停車",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-db945cfe9f9f",
      "ja": "快速",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-0fba29b6556a",
      "ja": "急行",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-172fb7e67b9b",
      "ja": "次",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-1520c48351f9",
      "ja": "反対側",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-bdc75bec19b8",
      "ja": "乗ります",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-2842fb8c1ac4",
      "ja": "降ります",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-e97c65421fd1",
      "ja": "止まります",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-800c65527500",
      "ja": "出発",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-d8ffe3744ac8",
      "ja": "到着",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v01-w-7d1aab6a161f",
      "ja": "終点",
      "exposure": "new",
      "source_refs": []
    }
  ]
}



## Hỏi vị trí, điểm đến và nơi thực hiện hành động [g01]

{
  "id": "g01",
  "source_refs": [
    "src-minna"
  ],
  "items": [
    {
      "id": "g01-g-dfee7a69fe14",
      "name_ja": "どこ／どちら",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-75f60a3a2f7c",
      "name_ja": "場所へ行きます／来ます／帰ります",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    },
    {
      "id": "g01-g-7073bac4406f",
      "name_ja": "場所でVます",
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
    }
  ]
}



## Hỏi từng thông tin để tự chọn được tàu [k01]

# Nói rõ điểm đến, rồi hỏi từng phần

Đứng trước nhiều bảng và tuyến, hãy bắt đầu bằng điểm đến mình cần. Sau lời mở đầu ngắn, hỏi tàu đang chỉ có đi tới đó không. Một câu trả lời “không” vẫn hữu ích: mình còn có thể hỏi cách đi khác, thay vì kết thúc cuộc nói ngay.

<a id="k01-ex01"></a>
この電車はみどり駅に行きますか。

Tàu này có đến ga Midori không?

Nếu phải chuyển tuyến, hỏi nơi đổi trước. Khi đã biết tên ga đổi, mới hỏi sân ga hoặc tên tuyến tiếp theo. Cách tách này giúp người nghe trả lời ngắn và giúp mình giữ được từng thông tin.

<a id="k01-ex02"></a>
どこで乗り換えますか。

Tôi đổi tàu ở đâu?

<a id="k01-ex03"></a>
みどり駅行きは何番線ですか。

Tàu đi ga Midori ở sân ga số mấy?

Phân biệt điểm đến, tên tuyến và sân ga: tên một ga xuất hiện trên bảng chưa đủ cho biết tàu có dừng ở ga đó. Cần nghe cả câu trả lời, nhất là phần phủ định hoặc chỉ dẫn đi sang phía khác. Khi có nhiều loại tàu, có thể hỏi nhân viên loại nào dừng ở nơi mình cần; không đoán mọi tàu nhanh có cùng danh sách điểm dừng.

Nếu chưa nghe kịp, hỏi lại ngay. Đừng chỉ đáp “vâng” để cuộc nói kết thúc trong khi mình chưa biết phải đi đâu. Có thể chỉ xin nhắc lại tên ga hoặc số sân ga, không phải xin đọc lại toàn bộ chỉ dẫn.

<a id="k01-ex04"></a>
もう一度、お願いします。

Xin vui lòng nói lại một lần nữa.

Ở các bài sau, tên ga và số sân ga đều là dữ kiện giả định. Mục tiêu là tự hỏi được và hiểu cách tiếp nối, không ghi nhớ một lộ trình đi lại thật.


## Nhóm câu mở lời, hỏi tuyến và hỏi lại [sh01]

{
  "id": "sh01",
  "source_refs": [
    "src-b08"
  ],
  "knowledge_ids": [
    "k01"
  ],
  "items": [
    {
      "id": "sh01-i1",
      "kind": "sentence",
      "example_id": "k01-ex01",
      "ja": "この電車はみどり駅に行きますか。",
      "vi": "Tàu này có đến ga Midori không?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh01-i2",
      "kind": "sentence",
      "example_id": "k01-ex02",
      "ja": "どこで乗り換えますか。",
      "vi": "Tôi đổi tàu ở đâu?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh01-i3",
      "kind": "sentence",
      "example_id": "k01-ex03",
      "ja": "みどり駅行きは何番線ですか。",
      "vi": "Tàu đi ga Midori ở sân ga số mấy?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh01-i4",
      "kind": "sentence",
      "example_id": "k01-ex04",
      "ja": "もう一度、お願いします。",
      "vi": "Xin vui lòng nói lại một lần nữa.",
      "authorship": "source_adaptation"
    }
  ]
}



## Xác nhận và báo ý định nhẹ nhàng với ね [k02]

# Nghe rồi nhắc lại để người kia có thể xác nhận

Đuôi ね có thể giúp chia sẻ cảm nhận hoặc tìm sự đồng tình, xác nhận lại thông tin, và nhắc nhở hoặc dặn dò. Trong các cuộc nói khi đi lại, ta tập trung vào xác nhận và báo ý định; không dùng một cách nói để thay mọi loại câu hỏi.

Khi nhân viên vừa nói tên ga hoặc sân ga, nhắc lại đúng phần cần kiểm. Với quan hệ khách–nhân viên, giữ dạng lịch sự. Đuôi ね cho người kia cơ hội đáp lại, nhưng bản thân đuôi câu không biến điều mình đoán thành thông tin đúng.

<a id="k02-ex01"></a>
乗り換えは、さくら駅ですね。

Tôi đổi tàu ở ga Sakura, đúng không ạ?

<a id="k02-ex02"></a>
二番線ですね。

Sân ga số 2, đúng không ạ?

Dừng một nhịp để nghe câu xác nhận hoặc lời sửa. Nếu đối tác nói “không, là sân ga khác”, hãy sửa lại thông tin và xác nhận tiếp; không nhắc mãi câu sai vì muốn luyện đúng mẫu. Nếu chưa hề có dữ kiện, hỏi một câu thực sự trước, rồi mới nhắc lại điều vừa nghe.

Một chức năng khác trong bài nguồn là báo việc mình sắp làm để người nghe biết và có thể phản hồi. Câu sau có thể dùng khi nhân viên đã chỉ nơi chờ; nó không thay thế việc xin phép nếu mình chưa được chỉ dẫn hoặc không rõ có thể đứng đó hay không.

<a id="k02-ex03"></a>
では、こちらで待ちますね。

Vậy tôi sẽ đợi ở đây nhé.

Phần shadowing ngay sau dùng ba ví dụ vừa học. Hãy nghe cả câu người kia đáp và luyện nhường lượt, không chỉ kéo dài âm cuối ね.


## Sau video: nhắc lại thông tin và báo nơi chờ [sh02]

{
  "id": "sh02",
  "source_refs": [
    "src-b11"
  ],
  "knowledge_ids": [
    "k02"
  ],
  "items": [
    {
      "id": "sh02-i1",
      "kind": "sentence",
      "example_id": "k02-ex01",
      "ja": "乗り換えは、さくら駅ですね。",
      "vi": "Tôi đổi tàu ở ga Sakura, đúng không ạ?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh02-i2",
      "kind": "sentence",
      "example_id": "k02-ex02",
      "ja": "二番線ですね。",
      "vi": "Sân ga số 2, đúng không ạ?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh02-i3",
      "kind": "sentence",
      "example_id": "k02-ex03",
      "ja": "では、こちらで待ちますね。",
      "vi": "Vậy tôi sẽ đợi ở đây nhé.",
      "authorship": "source_adaptation"
    }
  ]
}



## Hỏi tàu này có tới ga cần không [S001]

{
  "id": "S001",
  "source_refs": [],
  "title": "Hỏi tàu này có tới ga cần không",
  "event_id": "E01",
  "setting": "Tại ga Sakura giả định, khách hỏi nhân viên về tàu đang chờ ở sân ga.",
  "communication_goal": "Xác nhận đúng tàu và điểm xuống.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S001--t01",
      "speaker": "A",
      "ja": "すみません。この電車はみどり駅に行きますか。",
      "vi": "Xin lỗi, tàu này có đến ga Midori không?"
    },
    {
      "id": "S001--t02",
      "speaker": "B",
      "ja": "はい、行きます。みどり駅は二つ目です。",
      "vi": "Vâng, có. Midori là ga thứ hai."
    },
    {
      "id": "S001--t03",
      "speaker": "A",
      "ja": "二つ目ですね。乗り換えはありますか。",
      "vi": "Ga thứ hai, đúng không ạ? Tôi có phải đổi tàu không?"
    },
    {
      "id": "S001--t04",
      "speaker": "B",
      "ja": "いいえ、このままで大丈夫です。",
      "vi": "Không, bạn cứ đi tàu này là được."
    },
    {
      "id": "S001--t05",
      "speaker": "A",
      "ja": "分かりました。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Cảm ơn anh/chị."
    },
    {
      "id": "S001--t06",
      "speaker": "B",
      "ja": "お気をつけて。",
      "vi": "Chúc bạn đi đường cẩn thận."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi phải đổi ở ga nào [S002]

{
  "id": "S002",
  "source_refs": [],
  "title": "Hỏi phải đổi ở ga nào",
  "event_id": "E01",
  "setting": "Tại ga Aoba giả định, khách muốn tới Midori và chưa biết cần đổi tàu.",
  "communication_goal": "Hỏi ga đổi, tuyến tiếp theo và nhắc lại đúng.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S002--t01",
      "speaker": "A",
      "ja": "すみません。みどり駅に行きたいです。",
      "vi": "Xin lỗi, tôi muốn đến ga Midori."
    },
    {
      "id": "S002--t02",
      "speaker": "B",
      "ja": "A線でさくら駅まで行ってください。",
      "vi": "Bạn hãy đi tuyến A đến ga Sakura."
    },
    {
      "id": "S002--t03",
      "speaker": "A",
      "ja": "さくら駅で乗り換えますか。",
      "vi": "Tôi đổi tàu ở ga Sakura phải không ạ?"
    },
    {
      "id": "S002--t04",
      "speaker": "B",
      "ja": "はい。そこでB線に乗り換えてください。",
      "vi": "Vâng. Bạn đổi sang tuyến B ở đó."
    },
    {
      "id": "S002--t05",
      "speaker": "A",
      "ja": "A線でさくら駅、そこでB線ですね。",
      "vi": "Đi tuyến A đến Sakura, rồi đổi sang tuyến B ở đó, đúng không ạ?"
    },
    {
      "id": "S002--t06",
      "speaker": "B",
      "ja": "はい、そのとおりです。",
      "vi": "Vâng, đúng như vậy."
    },
    {
      "id": "S002--t07",
      "speaker": "A",
      "ja": "ありがとうございます。",
      "vi": "Cảm ơn anh/chị."
    },
    {
      "id": "S002--t08",
      "speaker": "B",
      "ja": "どういたしまして。",
      "vi": "Không có gì."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi sân ga của tuyến tiếp theo [S003]

{
  "id": "S003",
  "source_refs": [],
  "title": "Hỏi sân ga của tuyến tiếp theo",
  "event_id": "E01",
  "setting": "Sau khi xuống tuyến A ở ga Sakura giả định, khách cần tìm tuyến B đi Midori.",
  "communication_goal": "Tìm sân ga và kiểm tra lại chiều đi.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S003--t01",
      "speaker": "A",
      "ja": "すみません。B線のみどり駅行きは何番線ですか。",
      "vi": "Xin lỗi, tuyến B đi ga Midori ở sân ga số mấy?"
    },
    {
      "id": "S003--t02",
      "speaker": "B",
      "ja": "二番線です。階段を下りて、左です。",
      "vi": "Sân ga số 2. Bạn xuống cầu thang rồi rẽ trái."
    },
    {
      "id": "S003--t03",
      "speaker": "A",
      "ja": "二番線ですね。次の電車でいいですか。",
      "vi": "Sân ga số 2, đúng không ạ? Tôi đi chuyến tiếp theo được chứ?"
    },
    {
      "id": "S003--t04",
      "speaker": "B",
      "ja": "はい。みどり行きの各駅停車に乗ってください。",
      "vi": "Vâng. Bạn hãy lên tàu dừng mọi ga hướng Midori."
    },
    {
      "id": "S003--t05",
      "speaker": "A",
      "ja": "みどり行きですね。ありがとうございます。",
      "vi": "Hướng Midori, đúng không ạ. Cảm ơn anh/chị."
    },
    {
      "id": "S003--t06",
      "speaker": "B",
      "ja": "はい。お気をつけて。",
      "vi": "Vâng. Bạn đi đường cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Khi phát hiện đi nhầm: hỏi lại đúng chỗ rồi chốt lại [k03]

# Đi nhầm vẫn có thể tiếp tục cuộc nói

Nhận ra mình đứng sai sân ga không có nghĩa phải nghe lại từ đầu một chỉ dẫn dài. Nói ngắn mình muốn đến đâu và điều đang không khớp. Khi nhân viên sửa, hỏi lại đúng từ hoặc con số chưa rõ, rồi kiểm tra phương án mới.

<a id="k03-ex01"></a>
反対側ですか。

Ở phía đối diện phải không ạ?

Hỏi lại một từ vừa nghe là một cách giữ cuộc nói. Đừng chỉ lặp lại vì muốn bắt chước âm: cần chờ phần giải thích hoặc xác nhận. Nếu bối rối giữa hai con số, nêu cả hai lựa chọn để đối tác biết mình đang cần làm rõ điều gì.

<a id="k03-ex02"></a>
二番線ですか、三番線ですか。

Sân ga số 2 hay số 3 ạ?

Không phải lời chỉ dẫn nào cũng chắc chắn: có người chỉ nói theo trí nhớ hoặc đang đoán. Hãy phân biệt điều đã được xác nhận với điều còn chưa rõ. Nếu người đang hỏi cũng không chắc, có thể nhờ họ chỉ tới nhân viên phù hợp, thay vì tiếp tục đoán theo.

<a id="k03-ex03"></a>
すみません、よく分かりません。もう一度、お願いします。

Xin lỗi, tôi chưa hiểu rõ. Xin hãy nói lại một lần nữa.

Sau khi đã được sửa, dùng cách nhắc lại của bài trước: ga nào, sân ga nào, hướng nào. Cuộc thoại tiếp nối bên dưới cho thấy việc nhắc lại giúp nhân viên phát hiện hoặc xác nhận phần hiểu của mình. Giữ tên ga/số sân ga đủ rõ; không cần lặp toàn bộ lời giải thích.


## Luyện giữ lượt khi nghe chưa chắc [sh03]

{
  "id": "sh03",
  "source_refs": [
    "src-b27",
    "src-b14"
  ],
  "knowledge_ids": [
    "k03"
  ],
  "items": [
    {
      "id": "sh03-i1",
      "kind": "sentence",
      "example_id": "k03-ex01",
      "ja": "反対側ですか。",
      "vi": "Ở phía đối diện phải không ạ?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh03-i2",
      "kind": "sentence",
      "example_id": "k03-ex02",
      "ja": "二番線ですか、三番線ですか。",
      "vi": "Sân ga số 2 hay số 3 ạ?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh03-i3",
      "kind": "sentence",
      "example_id": "k03-ex03",
      "ja": "すみません、よく分かりません。もう一度、お願いします。",
      "vi": "Xin lỗi, tôi chưa hiểu rõ. Xin hãy nói lại một lần nữa.",
      "authorship": "source_adaptation"
    }
  ]
}



## Đứng sai chiều, nhờ chỉ sang đúng bên [S004]

{
  "id": "S004",
  "source_refs": [],
  "title": "Đứng sai chiều, nhờ chỉ sang đúng bên",
  "event_id": "E01",
  "setting": "Ở ga Sakura giả định, khách đứng tại sân ga 3 hướng Kita thay vì hướng Midori.",
  "communication_goal": "Nhận ra sai chiều, hỏi rõ sân ga đúng.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "misunderstanding_then_corrected",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S004--t01",
      "speaker": "A",
      "ja": "すみません。この電車でみどり駅に行けますか。",
      "vi": "Xin lỗi, tôi đi tàu này đến ga Midori được không?"
    },
    {
      "id": "S004--t02",
      "speaker": "B",
      "ja": "いいえ、これは反対方向です。みどり行きは二番線です。",
      "vi": "Không, đây là hướng ngược lại. Tàu đi Midori ở sân ga số 2."
    },
    {
      "id": "S004--t03",
      "speaker": "A",
      "ja": "すみません。二番線ですか、三番線ですか。",
      "vi": "Xin lỗi, sân ga số 2 hay số 3 ạ?"
    },
    {
      "id": "S004--t04",
      "speaker": "B",
      "ja": "二番線です。向こうのホームです。",
      "vi": "Số 2. Ở sân ga phía bên kia."
    },
    {
      "id": "S004--t05",
      "speaker": "A",
      "ja": "あちらですね。階段はどこですか。",
      "vi": "Ở phía kia, đúng không ạ? Cầu thang ở đâu?"
    },
    {
      "id": "S004--t06",
      "speaker": "B",
      "ja": "少し戻ると、右にあります。",
      "vi": "Bạn quay lại một chút, cầu thang ở bên phải."
    },
    {
      "id": "S004--t07",
      "speaker": "A",
      "ja": "分かりました。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Cảm ơn anh/chị."
    },
    {
      "id": "S004--t08",
      "speaker": "B",
      "ja": "お気をつけて。",
      "vi": "Bạn đi đường cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Sau khi được sửa: nhắc lại tuyến và sân ga [S005]

{
  "id": "S005",
  "source_refs": [],
  "title": "Sau khi được sửa: nhắc lại tuyến và sân ga",
  "event_id": "E01",
  "setting": "Tiếp ngay S004, khách muốn kiểm lại thông tin trước khi rời chỗ nhân viên.",
  "communication_goal": "Xác nhận cả chiều đi và ga xuống, không chỉ một con số.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [
    "S004"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S005--t01",
      "speaker": "A",
      "ja": "すみません。もう一つ、いいですか。",
      "vi": "Xin lỗi, tôi hỏi thêm một điều được không?"
    },
    {
      "id": "S005--t02",
      "speaker": "B",
      "ja": "はい、どうぞ。",
      "vi": "Vâng, bạn cứ hỏi."
    },
    {
      "id": "S005--t03",
      "speaker": "A",
      "ja": "二番線のみどり行きですね。",
      "vi": "Tàu hướng Midori ở sân ga số 2, đúng không ạ?"
    },
    {
      "id": "S005--t04",
      "speaker": "B",
      "ja": "はい。各駅停車に乗ってください。",
      "vi": "Vâng. Bạn hãy lên tàu dừng mọi ga."
    },
    {
      "id": "S005--t05",
      "speaker": "A",
      "ja": "みどり駅は二つ目ですね。",
      "vi": "Midori là ga thứ hai, đúng không ạ?"
    },
    {
      "id": "S005--t06",
      "speaker": "B",
      "ja": "そうです。次がはな駅、その次がみどり駅です。",
      "vi": "Đúng vậy. Ga tiếp theo là Hana, sau đó là Midori."
    },
    {
      "id": "S005--t07",
      "speaker": "A",
      "ja": "分かりました。助かりました。",
      "vi": "Tôi hiểu rồi. Anh/chị giúp tôi nhiều quá."
    },
    {
      "id": "S005--t08",
      "speaker": "B",
      "ja": "どういたしまして。",
      "vi": "Không có gì."
    }
  ],
  "authorship": "original_extension"
}



## Bến xe, cách lên xuống và khi lỡ bến [v02]

{
  "id": "v02",
  "source_refs": [],
  "items": [
    {
      "id": "v02-w-2cc0af026c11",
      "ja": "バス",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-8bc293bce38f",
      "ja": "バス停",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-4086cc58eaf5",
      "ja": "停留所",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-39a820586735",
      "ja": "乗り場",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-e5150d0a0c03",
      "ja": "運転手",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-6044e9f095e0",
      "ja": "前",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-e9fa45a75ea1",
      "ja": "後ろ",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-1a7930272017",
      "ja": "入口",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v02-w-7016090059bd",
      "ja": "出口",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v02-w-9aa38cd3f56d",
      "ja": "運賃",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-90d5e37ab1e7",
      "ja": "お金",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-abfcd7a55281",
      "ja": "現金",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-fd5e29a803f1",
      "ja": "ICカード",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-49603387cada",
      "ja": "整理券",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-6e724a72699e",
      "ja": "乗り換え",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v02-w-d4791fb11477",
      "ja": "公園",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-c589f1086ffe",
      "ja": "市役所",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-c43fe4333999",
      "ja": "図書館",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-616b0d572eed",
      "ja": "病院",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-172fb7e67b9b",
      "ja": "次",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v02-w-b378e984210c",
      "ja": "戻ります",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-b018b96704a5",
      "ja": "払います",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-2debee25dba9",
      "ja": "乗り過ごします",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-8f5ab70b827c",
      "ja": "横断歩道",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-367e6951e58c",
      "ja": "遅れます",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v02-w-45720855fc5e",
      "ja": "待ちます",
      "exposure": "new",
      "source_refs": []
    }
  ]
}



## Nghe chỉ dẫn, trình bày điều đang gặp [g02]

{
  "id": "g02",
  "source_refs": [
    "src-minna"
  ],
  "items": [
    {
      "id": "g02-g-e8fb271526f3",
      "name_ja": "Vてください",
      "jlpt_level": "N5",
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
    }
  ]
}



## Đi xe buýt: hỏi đúng tuyến, cách lên và bước tiếp theo [k04]

# Hỏi xe đang đứng trước mình, không áp một cách đi cho mọi tuyến

Tên điểm đến trên bảng, số tuyến và bến xuống là những thông tin khác nhau. Bắt đầu bằng nơi mình muốn tới; nếu xe không đi thẳng, hỏi bến đổi và số xe tiếp theo, rồi xác nhận. Các cuộc thoại ở đây diễn ra khi xe đang dừng để việc trao đổi có bối cảnh rõ.

<a id="k04-ex01"></a>
このバスは中央公園に行きますか。

Xe buýt này có đến công viên Chūō không?

Không học thuộc “xe buýt Nhật luôn lên cửa sau” hoặc “luôn trả tiền lúc xuống”. [Hướng dẫn chính thức của Kyoto](https://www2.city.kyoto.lg.jp/kotsu/webguide/en/bus/howtoride_bus.html) mô tả hai cách khác nhau theo tuyến ngay trong cùng hệ thống. Vì vậy bài học cần giúp mình hỏi được cách dùng chính chiếc xe này; ví dụ dưới là câu hỏi, không phải quy tắc vận hành chung.

<a id="k04-ex02"></a>
前から乗りますか、後ろから乗りますか。

Tôi lên cửa trước hay cửa sau?

<a id="k04-ex03"></a>
お金はいつ払いますか。

Tôi trả tiền lúc nào?

Có thể hỏi thêm về thẻ IC hoặc vé đánh số khi cần. Không mặc định tiền mặt/thẻ nào cũng dùng được hoặc số tiền của một ví dụ áp dụng cả nước. Trong các mẫu luyện, giá và số tuyến được giả định để mình tập hỏi và nghe câu trả lời.

Nếu đã đi quá bến, nói rõ sự việc rồi hỏi phương án tiếp theo. Không cần một lời giải thích dài hoặc xin lỗi liên tục. Chỉ dẫn sửa đường có thể gồm bến xuống, hướng quay lại và tuyến khác; hãy chia nhỏ để hỏi và dùng cách xác nhận với ね đã học.

<a id="k04-ex04"></a>
すみません。乗り過ごしました。

Xin lỗi, tôi đã đi quá bến rồi.

<a id="k04-ex05"></a>
次で降りればいいですか。

Tôi xuống ở bến tiếp theo thì được phải không ạ?

Mẫu cuối là một cụm hỗ trợ để hỏi “làm như vậy thì được chứ?”. Người mới có thể dùng cách đơn giản hơn: nói tên bến muốn kiểm tra rồi hỏi lại. Các ví dụ không bắt người học phải tự chia thành thạo mọi dạng điều kiện. Khi đã biết mình sẽ đến muộn, cuộc gọi cho người đang đợi là một tình huống riêng: nói đang ở đâu, ước lượng khi nào đến và thống nhất có tiếp tục đợi hay đổi điểm gặp.


## Nhóm shadowing xe buýt: hỏi, nghe rồi hỏi tiếp [sh04]

{
  "id": "sh04",
  "source_refs": [
    "src-b01",
    "src-b08"
  ],
  "knowledge_ids": [
    "k04"
  ],
  "items": [
    {
      "id": "sh04-i1",
      "kind": "sentence",
      "example_id": "k04-ex01",
      "ja": "このバスは中央公園に行きますか。",
      "vi": "Xe buýt này có đến công viên Chūō không?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh04-i2",
      "kind": "sentence",
      "example_id": "k04-ex02",
      "ja": "前から乗りますか、後ろから乗りますか。",
      "vi": "Tôi lên cửa trước hay cửa sau?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh04-i3",
      "kind": "sentence",
      "example_id": "k04-ex03",
      "ja": "お金はいつ払いますか。",
      "vi": "Tôi trả tiền lúc nào?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh04-i4",
      "kind": "sentence",
      "example_id": "k04-ex04",
      "ja": "すみません。乗り過ごしました。",
      "vi": "Xin lỗi, tôi đã đi quá bến rồi.",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh04-i5",
      "kind": "sentence",
      "example_id": "k04-ex05",
      "ja": "次で降りればいいですか。",
      "vi": "Tôi xuống ở bến tiếp theo thì được phải không ạ?",
      "authorship": "source_adaptation"
    }
  ]
}



## Hỏi xe có dừng gần nơi cần đến [S006]

{
  "id": "S006",
  "source_refs": [],
  "title": "Hỏi xe có dừng gần nơi cần đến",
  "event_id": "E02",
  "setting": "Tại bến giả định, xe số 5 đang dừng và khách muốn đến công viên Chūō.",
  "communication_goal": "Biết xe phù hợp và tên bến xuống.",
  "relationship": "Khách và Tài xế, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Tài xế"
    }
  ],
  "turns": [
    {
      "id": "S006--t01",
      "speaker": "A",
      "ja": "すみません。このバスは中央公園に行きますか。",
      "vi": "Xin lỗi, xe này có đến công viên Chūō không?"
    },
    {
      "id": "S006--t02",
      "speaker": "B",
      "ja": "はい。中央公園前で降りてください。",
      "vi": "Có. Bạn xuống ở bến Chūō Kōen-mae."
    },
    {
      "id": "S006--t03",
      "speaker": "A",
      "ja": "いくつ目ですか。",
      "vi": "Là bến thứ mấy ạ?"
    },
    {
      "id": "S006--t04",
      "speaker": "B",
      "ja": "ここから三つ目です。",
      "vi": "Từ đây là bến thứ ba."
    },
    {
      "id": "S006--t05",
      "speaker": "A",
      "ja": "三つ目の中央公園前ですね。ありがとうございます。",
      "vi": "Bến thứ ba, Chūō Kōen-mae, đúng không ạ. Cảm ơn anh/chị."
    },
    {
      "id": "S006--t06",
      "speaker": "B",
      "ja": "はい。どうぞ。",
      "vi": "Vâng. Mời bạn lên xe."
    }
  ],
  "authorship": "original_extension"
}



## Hỏi cửa lên xe và lúc trả tiền [S007]

{
  "id": "S007",
  "source_refs": [],
  "title": "Hỏi cửa lên xe và lúc trả tiền",
  "event_id": "E02",
  "setting": "Khách chưa lên chiếc xe giả định đang dừng tại bến.",
  "communication_goal": "Hỏi hai thông tin khác nhau: cửa lên và lúc trả tiền.",
  "relationship": "Khách và Tài xế, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Tài xế"
    }
  ],
  "turns": [
    {
      "id": "S007--t01",
      "speaker": "A",
      "ja": "すみません。前から乗りますか、後ろから乗りますか。",
      "vi": "Xin lỗi, tôi lên cửa trước hay cửa sau?"
    },
    {
      "id": "S007--t02",
      "speaker": "B",
      "ja": "後ろから乗ってください。降りるときは前です。",
      "vi": "Bạn lên cửa sau. Khi xuống thì xuống cửa trước."
    },
    {
      "id": "S007--t03",
      "speaker": "A",
      "ja": "お金はいつ払いますか。",
      "vi": "Tôi trả tiền lúc nào?"
    },
    {
      "id": "S007--t04",
      "speaker": "B",
      "ja": "降りるときに払ってください。二百円です。",
      "vi": "Bạn trả lúc xuống. Giá vé là 200 yên."
    },
    {
      "id": "S007--t05",
      "speaker": "A",
      "ja": "ICカードも使えますか。",
      "vi": "Tôi dùng thẻ IC cũng được chứ?"
    },
    {
      "id": "S007--t06",
      "speaker": "B",
      "ja": "はい、使えます。降りるときにタッチしてください。",
      "vi": "Vâng, dùng được. Bạn chạm thẻ lúc xuống."
    },
    {
      "id": "S007--t07",
      "speaker": "A",
      "ja": "後ろから乗って、降りるときに払いますね。",
      "vi": "Tôi lên cửa sau và trả tiền lúc xuống, đúng không ạ?"
    },
    {
      "id": "S007--t08",
      "speaker": "B",
      "ja": "はい、そうです。",
      "vi": "Vâng, đúng vậy."
    }
  ],
  "authorship": "original_extension"
}



## Không đi thẳng: hỏi bến chuyển xe [S008]

{
  "id": "S008",
  "source_refs": [],
  "title": "Không đi thẳng: hỏi bến chuyển xe",
  "event_id": "E02",
  "setting": "Khách muốn tới tòa thị chính, nhưng xe đang hỏi không đến thẳng.",
  "communication_goal": "Nghe việc cần chuyển xe, hỏi rõ bến và số tuyến sau.",
  "relationship": "Khách và Tài xế, lịch sự.",
  "outcome": "transfer_required",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Tài xế"
    }
  ],
  "turns": [
    {
      "id": "S008--t01",
      "speaker": "A",
      "ja": "すみません。市役所に行きたいんですが、このバスでいいですか。",
      "vi": "Xin lỗi, tôi muốn đến tòa thị chính. Tôi đi xe này được chứ?"
    },
    {
      "id": "S008--t02",
      "speaker": "B",
      "ja": "市役所には行きません。中央公園前で乗り換えてください。",
      "vi": "Xe này không đến tòa thị chính. Bạn đổi xe ở Chūō Kōen-mae."
    },
    {
      "id": "S008--t03",
      "speaker": "A",
      "ja": "そこで何番のバスに乗りますか。",
      "vi": "Ở đó tôi lên xe số mấy ạ?"
    },
    {
      "id": "S008--t04",
      "speaker": "B",
      "ja": "八番です。市役所前で降りてください。",
      "vi": "Số 8. Bạn xuống ở Shiyakusho-mae."
    },
    {
      "id": "S008--t05",
      "speaker": "A",
      "ja": "中央公園前で八番ですね。乗り場は同じですか。",
      "vi": "Đổi sang xe số 8 ở Chūō Kōen-mae, đúng không ạ? Bến lên có cùng chỗ không?"
    },
    {
      "id": "S008--t06",
      "speaker": "B",
      "ja": "はい、同じ乗り場です。",
      "vi": "Vâng, cùng một bến."
    },
    {
      "id": "S008--t07",
      "speaker": "A",
      "ja": "分かりました。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Cảm ơn anh/chị."
    },
    {
      "id": "S008--t08",
      "speaker": "B",
      "ja": "どういたしまして。",
      "vi": "Không có gì."
    }
  ],
  "authorship": "original_extension"
}



## Lỡ bến: hỏi cách quay lại [S009]

{
  "id": "S009",
  "source_refs": [],
  "title": "Lỡ bến: hỏi cách quay lại",
  "event_id": "E02",
  "setting": "Xe đã đi qua bến Chūō Kōen-mae; khách hỏi khi xe dừng ở một bến tiếp theo trong mạng giả định.",
  "communication_goal": "Biết nơi xuống an toàn theo lộ trình được chỉ và tuyến quay lại.",
  "relationship": "Khách và Tài xế, lịch sự.",
  "outcome": "missed_stop_then_return",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Tài xế"
    }
  ],
  "turns": [
    {
      "id": "S009--t01",
      "speaker": "A",
      "ja": "すみません。中央公園前で降りたかったんですが、乗り過ごしました。",
      "vi": "Xin lỗi, tôi định xuống ở Chūō Kōen-mae nhưng đã đi quá bến."
    },
    {
      "id": "S009--t02",
      "speaker": "B",
      "ja": "次の図書館前で降りてください。",
      "vi": "Bạn xuống ở bến Toshokan-mae tiếp theo nhé."
    },
    {
      "id": "S009--t03",
      "speaker": "A",
      "ja": "そこから戻れますか。",
      "vi": "Từ đó tôi quay lại được chứ?"
    },
    {
      "id": "S009--t04",
      "speaker": "B",
      "ja": "はい。反対側のバス停から五番に乗って、一つ目です。",
      "vi": "Được. Bạn lên xe số 5 từ bến phía đối diện; Chūō Kōen-mae là bến đầu tiên."
    },
    {
      "id": "S009--t05",
      "speaker": "A",
      "ja": "反対側の五番で、一つ目ですね。",
      "vi": "Xe số 5 phía đối diện, xuống ở bến đầu tiên, đúng không ạ?"
    },
    {
      "id": "S009--t06",
      "speaker": "B",
      "ja": "そうです。横断歩道は図書館の前にあります。",
      "vi": "Đúng vậy. Vạch qua đường ở trước thư viện."
    },
    {
      "id": "S009--t07",
      "speaker": "A",
      "ja": "分かりました。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Cảm ơn anh/chị."
    },
    {
      "id": "S009--t08",
      "speaker": "B",
      "ja": "お気をつけて。",
      "vi": "Bạn đi đường cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Báo người đợi rằng mình sẽ đến muộn [S010]

{
  "id": "S010",
  "source_refs": [],
  "title": "Báo người đợi rằng mình sẽ đến muộn",
  "event_id": "E02",
  "setting": "Sau S009, khách gọi bạn đang đợi ở cổng công viên; thời gian chỉ là ước lượng trong cảnh giả định.",
  "communication_goal": "Nói sự việc, báo mốc dự kiến và thống nhất tiếp tục gặp.",
  "relationship": "Người đến muộn và Bạn đang đợi, lịch sự.",
  "outcome": "resolved",
  "follows": [
    "S009"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Người đến muộn"
    },
    {
      "id": "B",
      "role": "Bạn đang đợi"
    }
  ],
  "turns": [
    {
      "id": "S010--t01",
      "speaker": "A",
      "ja": "もしもし、リンさん。すみません。バスを乗り過ごしました。",
      "vi": "A lô, Linh à. Xin lỗi, tôi đi xe buýt quá bến mất rồi."
    },
    {
      "id": "S010--t02",
      "speaker": "B",
      "ja": "そうなんですか。今、どこですか。",
      "vi": "Vậy à? Giờ bạn đang ở đâu?"
    },
    {
      "id": "S010--t03",
      "speaker": "A",
      "ja": "図書館前です。今からバスで戻ります。",
      "vi": "Tôi đang ở Toshokan-mae. Bây giờ tôi sẽ đi xe buýt quay lại."
    },
    {
      "id": "S010--t04",
      "speaker": "B",
      "ja": "分かりました。あとどのぐらいですか。",
      "vi": "Tôi hiểu rồi. Khoảng bao lâu nữa bạn tới?"
    },
    {
      "id": "S010--t05",
      "speaker": "A",
      "ja": "あと十分ぐらいです。入口で待ってください。",
      "vi": "Khoảng 10 phút nữa tôi tới. Bạn đợi ở lối vào giúp tôi nhé."
    },
    {
      "id": "S010--t06",
      "speaker": "B",
      "ja": "はい。公園の入口で待っています。気をつけて。",
      "vi": "Được. Tôi sẽ đợi ở lối vào công viên. Bạn đi cẩn thận nhé."
    },
    {
      "id": "S010--t07",
      "speaker": "A",
      "ja": "ありがとうございます。また電話します。",
      "vi": "Cảm ơn bạn. Tôi sẽ gọi lại nhé."
    },
    {
      "id": "S010--t08",
      "speaker": "B",
      "ja": "はい、では、また。",
      "vi": "Ừ, vậy lát gặp nhé."
    }
  ],
  "authorship": "original_extension"
}



## Lối đi, hành lý và quầy hỗ trợ [v03]

{
  "id": "v03",
  "source_refs": [],
  "items": [
    {
      "id": "v03-w-ba2a88af355e",
      "ja": "荷物",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-a8386a4cf650",
      "ja": "スーツケース",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-b47390ac87c3",
      "ja": "エレベーター",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-241046c62bb5",
      "ja": "エスカレーター",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-44ec5ddfce33",
      "ja": "階段",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-a35b413643e9",
      "ja": "通路",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-94c617250b91",
      "ja": "係員",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-57d96c91dcb2",
      "ja": "案内",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-f9673884e94b",
      "ja": "手伝い",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-2f0ba088d763",
      "ja": "改札",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v03-w-34d06e878426",
      "ja": "有人改札",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-d2b6a3926211",
      "ja": "窓口",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-4acdff7ee037",
      "ja": "切符",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-b4292723cbc2",
      "ja": "ベンチ",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-6044e9f095e0",
      "ja": "前",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v03-w-f8c6e3e86baa",
      "ja": "横",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-fb70218c7353",
      "ja": "近く",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-92c38c0d985a",
      "ja": "一緒",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-1a3205c3a91e",
      "ja": "母",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-7ec26292414b",
      "ja": "名前",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-dce52f3e1119",
      "ja": "確認",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-45720855fc5e",
      "ja": "待ちます",
      "exposure": "review",
      "source_refs": []
    },
    {
      "id": "v03-w-98fc560da459",
      "ja": "使います",
      "exposure": "new",
      "source_refs": []
    },
    {
      "id": "v03-w-8fc80163d735",
      "ja": "困ります",
      "exposure": "new",
      "source_refs": []
    }
  ]
}



## Hỏi có thể chờ ở đâu [g03]

{
  "id": "g03",
  "source_refs": [
    "src-minna"
  ],
  "items": [
    {
      "id": "g03-g-785102d73d16",
      "name_ja": "Vてもいいですか",
      "jlpt_level": "N5",
      "reference": {
        "kind": "minna"
      }
    }
  ]
}



## Nhờ chỉ lối phù hợp và giữ rõ điểm chờ/điểm gặp [k05]

# Nói nhu cầu cụ thể, rồi hỏi bước tiếp theo

Khi mang nhiều hành lý, đi cùng người khó dùng cầu thang hoặc cần người chỉ lối, điều quan trọng là cho nhân viên biết mình cần gì và đang muốn đến đâu. Không cần một câu chuyện dài. Có thể nói riêng hai câu ngắn: tình trạng hiện tại và điều muốn hỏi.

<a id="k05-ex01"></a>
荷物が多いです。エレベーターはどこですか。

Tôi có nhiều hành lý. Thang máy ở đâu?

<a id="k05-ex02"></a>
母と一緒です。階段はちょっと…。

Tôi đi cùng mẹ. Đi cầu thang thì hơi khó…

Mẫu thứ hai cố ý để phần cuối ngắn lại theo ngữ cảnh: “cầu thang thì hơi khó…”. Có thể nói rõ hơn nếu người nghe chưa hiểu; không dùng sự ngập ngừng thay cho thông tin thiết yếu. Chỉ chia sẻ điều cần cho việc hướng dẫn, không cần tự thêm tên bệnh hay giải thích chuyên môn.

Không mặc định mọi ga đều có cùng lối đi hoặc việc hỗ trợ sẽ diễn ra ngay. [Hướng dẫn JR East](https://www.jreast.co.jp/en/equipment/equipment_1/wheelchair/) cho biết việc hướng dẫn có thể cần phối hợp và có trường hợp phải chờ. Bài luyện này chỉ giúp mình hỏi, nghe điều kiện và xác nhận bước tiếp theo; không hứa trước một dịch vụ hay thời gian chờ thật.

<a id="k05-ex03"></a>
ここで待ってもいいですか。

Tôi đợi ở đây được không?

Nếu được yêu cầu đợi, cần biết chờ ở đâu. Nếu nhân viên ở ga sau sẽ gặp mình, cần hỏi rõ sân ga, vị trí gần vật mốc nào và điều cần nói với người đó. Dùng cách nhắc lại của các bài trước để chốt thông tin, thay vì chỉ gật đầu.

<a id="k05-ex04"></a>
改札の横のベンチですね。

Ghế băng bên cạnh cổng soát vé, đúng không ạ?

Vé không qua cổng là một việc khác với tìm thang máy. Khi người đang hỏi không phải người xử lý vé, nhiệm vụ vừa sức là tìm đúng quầy có nhân viên, mang vé đến và giải thích hiện tượng. Không cần tự suy đoán nguyên nhân, mức phí hay quy định vé.

<a id="k05-ex05"></a>
切符のことは、どこで聞けばいいですか。

Về việc vé tàu, tôi nên hỏi ở đâu?

Ở các cuộc thoại tiếp theo, chỗ chờ và điểm gặp đều được đặt cho cảnh giả định. Hãy luyện nhận thông tin mới, hỏi thêm phần còn thiếu và nhắc lại bằng cách của mình. Cụm hỏi vị trí và cách nêu điểm đến từ bài đầu tiếp tục được dùng ở đây.


## Luyện nói nhu cầu, xin chờ và xác nhận địa điểm [sh05]

{
  "id": "sh05",
  "source_refs": [
    "src-b08"
  ],
  "knowledge_ids": [
    "k05"
  ],
  "items": [
    {
      "id": "sh05-i1",
      "kind": "sentence",
      "example_id": "k05-ex01",
      "ja": "荷物が多いです。エレベーターはどこですか。",
      "vi": "Tôi có nhiều hành lý. Thang máy ở đâu?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh05-i2",
      "kind": "sentence",
      "example_id": "k05-ex02",
      "ja": "母と一緒です。階段はちょっと…。",
      "vi": "Tôi đi cùng mẹ. Đi cầu thang thì hơi khó…",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh05-i3",
      "kind": "sentence",
      "example_id": "k05-ex03",
      "ja": "ここで待ってもいいですか。",
      "vi": "Tôi đợi ở đây được không?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh05-i4",
      "kind": "sentence",
      "example_id": "k05-ex04",
      "ja": "改札の横のベンチですね。",
      "vi": "Ghế băng bên cạnh cổng soát vé, đúng không ạ?",
      "authorship": "source_adaptation"
    },
    {
      "id": "sh05-i5",
      "kind": "sentence",
      "example_id": "k05-ex05",
      "ja": "切符のことは、どこで聞けばいいですか。",
      "vi": "Về việc vé tàu, tôi nên hỏi ở đâu?",
      "authorship": "source_adaptation"
    }
  ]
}



## Mang nhiều hành lý: hỏi thang máy [S011]

{
  "id": "S011",
  "source_refs": [],
  "title": "Mang nhiều hành lý: hỏi thang máy",
  "event_id": "E03",
  "setting": "Khách ở sảnh ga Aoba giả định, cần tới sân ga số 2.",
  "communication_goal": "Hỏi lối phù hợp và xác nhận vị trí thang máy.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S011--t01",
      "speaker": "A",
      "ja": "すみません。荷物が多いです。エレベーターはどこですか。",
      "vi": "Xin lỗi, tôi có nhiều hành lý. Thang máy ở đâu?"
    },
    {
      "id": "S011--t02",
      "speaker": "B",
      "ja": "あちらの窓口の後ろです。",
      "vi": "Ở phía sau quầy bên kia."
    },
    {
      "id": "S011--t03",
      "speaker": "A",
      "ja": "窓口の後ろですね。二番線に行けますか。",
      "vi": "Phía sau quầy, đúng không ạ? Tôi dùng thang đó lên sân ga số 2 được chứ?"
    },
    {
      "id": "S011--t04",
      "speaker": "B",
      "ja": "はい。二階で降りて、左に進んでください。",
      "vi": "Được. Bạn ra ở tầng 2 rồi đi sang trái."
    },
    {
      "id": "S011--t05",
      "speaker": "A",
      "ja": "二階で降りて、左ですね。ありがとうございます。",
      "vi": "Ra ở tầng 2 rồi sang trái, đúng không ạ. Cảm ơn anh/chị."
    },
    {
      "id": "S011--t06",
      "speaker": "B",
      "ja": "はい。お気をつけて。",
      "vi": "Vâng. Bạn đi cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Đi cùng người khó dùng cầu thang: nhờ chỉ lối [S012]

{
  "id": "S012",
  "source_refs": [],
  "title": "Đi cùng người khó dùng cầu thang: nhờ chỉ lối",
  "event_id": "E03",
  "setting": "Khách đi cùng mẹ, ở ga Aoba giả định; cần lối đến tuyến A không phải đi cầu thang.",
  "communication_goal": "Nêu nhu cầu vừa đủ và hỏi đường phù hợp.",
  "relationship": "Khách đi cùng mẹ và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách đi cùng mẹ"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S012--t01",
      "speaker": "A",
      "ja": "すみません。母と一緒です。階段はちょっと…。エレベーターはありますか。",
      "vi": "Xin lỗi, tôi đi cùng mẹ. Đi cầu thang thì hơi khó… Ở đây có thang máy không?"
    },
    {
      "id": "S012--t02",
      "speaker": "B",
      "ja": "はい、あります。どちらまで行かれますか。",
      "vi": "Có. Anh/chị định đi đến đâu ạ?"
    },
    {
      "id": "S012--t03",
      "speaker": "A",
      "ja": "みどり駅です。まずA線に乗ります。",
      "vi": "Đến ga Midori. Trước hết chúng tôi lên tuyến A."
    },
    {
      "id": "S012--t04",
      "speaker": "B",
      "ja": "では、こちらの通路を進んでください。エレベーターがあります。",
      "vi": "Vậy anh/chị đi theo lối này. Có thang máy ở đó."
    },
    {
      "id": "S012--t05",
      "speaker": "A",
      "ja": "この通路ですね。母と一緒に行きます。",
      "vi": "Lối này, đúng không ạ? Tôi sẽ đi cùng mẹ."
    },
    {
      "id": "S012--t06",
      "speaker": "B",
      "ja": "はい。分からないことがあれば、係員に聞いてください。",
      "vi": "Vâng. Nếu có điều gì chưa rõ, anh/chị cứ hỏi nhân viên."
    },
    {
      "id": "S012--t07",
      "speaker": "A",
      "ja": "ありがとうございます。助かります。",
      "vi": "Cảm ơn anh/chị. Như vậy giúp chúng tôi nhiều lắm."
    },
    {
      "id": "S012--t08",
      "speaker": "B",
      "ja": "お気をつけて。",
      "vi": "Anh/chị đi cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Cần kiểm tra hỗ trợ ở ga đổi: hỏi nơi chờ [S013]

{
  "id": "S013",
  "source_refs": [],
  "title": "Cần kiểm tra hỗ trợ ở ga đổi: hỏi nơi chờ",
  "event_id": "E03",
  "setting": "Khách cần chỉ lối không qua cầu thang ở Sakura, nhân viên Aoba chưa xác nhận được việc tiếp nối.",
  "communication_goal": "Hiểu cần chờ xác nhận và xác định đúng nơi chờ.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "pending_then_waiting_place_agreed",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S013--t01",
      "speaker": "A",
      "ja": "すみません。さくら駅で乗り換えます。母は階段が使えません。",
      "vi": "Xin lỗi, chúng tôi đổi tàu ở ga Sakura. Mẹ tôi không dùng cầu thang được."
    },
    {
      "id": "S013--t02",
      "speaker": "B",
      "ja": "さくら駅に確認します。少しお待ちください。",
      "vi": "Tôi sẽ kiểm tra với ga Sakura. Anh/chị vui lòng chờ một chút."
    },
    {
      "id": "S013--t03",
      "speaker": "A",
      "ja": "ここで待ってもいいですか。",
      "vi": "Tôi đợi ở đây được không?"
    },
    {
      "id": "S013--t04",
      "speaker": "B",
      "ja": "はい。改札の横にベンチがあります。そちらでお待ちください。",
      "vi": "Được. Có ghế băng bên cạnh cổng soát vé. Anh/chị đợi ở đó nhé."
    },
    {
      "id": "S013--t05",
      "speaker": "A",
      "ja": "改札の横のベンチですね。",
      "vi": "Ghế băng bên cạnh cổng soát vé, đúng không ạ?"
    },
    {
      "id": "S013--t06",
      "speaker": "B",
      "ja": "はい、そうです。",
      "vi": "Vâng, đúng vậy."
    },
    {
      "id": "S013--t07",
      "speaker": "A",
      "ja": "分かりました。ここで待ちます。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Chúng tôi sẽ đợi ở đây. Cảm ơn anh/chị."
    },
    {
      "id": "S013--t08",
      "speaker": "B",
      "ja": "はい。確認します。",
      "vi": "Vâng. Tôi sẽ kiểm tra."
    }
  ],
  "authorship": "original_extension"
}



## Sau khi xác nhận được: hỏi rõ điểm gặp ở ga đổi [S014]

{
  "id": "S014",
  "source_refs": [],
  "title": "Sau khi xác nhận được: hỏi rõ điểm gặp ở ga đổi",
  "event_id": "E03",
  "setting": "Tiếp S013: nhân viên đã xác nhận được với ga Sakura trong cảnh giả định.",
  "communication_goal": "Chốt nơi nhân viên ga sau sẽ gặp và tên cần báo.",
  "relationship": "Khách và Nhân viên ga, lịch sự.",
  "outcome": "resolved",
  "follows": [
    "S013"
  ],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên ga"
    }
  ],
  "turns": [
    {
      "id": "S014--t01",
      "speaker": "A",
      "ja": "すみません。さくら駅では、どこで待ちますか。",
      "vi": "Xin lỗi, ở ga Sakura chúng tôi đợi ở đâu?"
    },
    {
      "id": "S014--t02",
      "speaker": "B",
      "ja": "二番線に係員がいます。そこでお待ちください。",
      "vi": "Có nhân viên ở sân ga số 2. Anh/chị đợi ở đó nhé."
    },
    {
      "id": "S014--t03",
      "speaker": "A",
      "ja": "二番線のどこですか。",
      "vi": "Chỗ nào ở sân ga số 2 ạ?"
    },
    {
      "id": "S014--t04",
      "speaker": "B",
      "ja": "エレベーターの前です。",
      "vi": "Ở trước thang máy."
    },
    {
      "id": "S014--t05",
      "speaker": "A",
      "ja": "二番線のエレベーターの前ですね。",
      "vi": "Trước thang máy ở sân ga số 2, đúng không ạ?"
    },
    {
      "id": "S014--t06",
      "speaker": "B",
      "ja": "はい。お名前を教えてください。",
      "vi": "Vâng. Anh/chị cho tôi biết tên nhé."
    },
    {
      "id": "S014--t07",
      "speaker": "A",
      "ja": "リンです。",
      "vi": "Tôi là Linh."
    },
    {
      "id": "S014--t08",
      "speaker": "B",
      "ja": "リンさんですね。さくら駅に伝えます。",
      "vi": "Linh, đúng không ạ? Tôi sẽ báo cho ga Sakura."
    },
    {
      "id": "S014--t09",
      "speaker": "A",
      "ja": "ありがとうございます。よろしくお願いします。",
      "vi": "Cảm ơn anh/chị. Nhờ anh/chị giúp."
    },
    {
      "id": "S014--t10",
      "speaker": "B",
      "ja": "はい。お気をつけて。",
      "vi": "Vâng. Anh/chị đi cẩn thận nhé."
    }
  ],
  "authorship": "original_extension"
}



## Vé không qua cổng: tìm đúng chỗ hỏi [S015]

{
  "id": "S015",
  "source_refs": [],
  "title": "Vé không qua cổng: tìm đúng chỗ hỏi",
  "event_id": "E03",
  "setting": "Khách hỏi một nhân viên hướng dẫn ở gần cổng; việc kiểm vé do quầy có nhân viên xử lý.",
  "communication_goal": "Mô tả hiện tượng và tìm quầy phù hợp.",
  "relationship": "Khách và Nhân viên hướng dẫn, lịch sự.",
  "outcome": "directed_to_correct_staff",
  "follows": [],
  "alternative_to": [],
  "speakers": [
    {
      "id": "A",
      "role": "Khách"
    },
    {
      "id": "B",
      "role": "Nhân viên hướng dẫn"
    }
  ],
  "turns": [
    {
      "id": "S015--t01",
      "speaker": "A",
      "ja": "すみません。切符を入れましたが、改札が開きません。",
      "vi": "Xin lỗi, tôi cho vé vào nhưng cổng soát vé không mở."
    },
    {
      "id": "S015--t02",
      "speaker": "B",
      "ja": "あちらの有人改札で係員に聞いてください。",
      "vi": "Anh/chị hỏi nhân viên ở cổng soát vé có người trực bên kia nhé."
    },
    {
      "id": "S015--t03",
      "speaker": "A",
      "ja": "右の窓口ですか。",
      "vi": "Quầy bên phải phải không ạ?"
    },
    {
      "id": "S015--t04",
      "speaker": "B",
      "ja": "はい、右です。切符を持って行ってください。",
      "vi": "Vâng, bên phải. Anh/chị mang vé đến đó nhé."
    },
    {
      "id": "S015--t05",
      "speaker": "A",
      "ja": "分かりました。ありがとうございます。",
      "vi": "Tôi hiểu rồi. Cảm ơn anh/chị."
    },
    {
      "id": "S015--t06",
      "speaker": "B",
      "ja": "どういたしまして。",
      "vi": "Không có gì."
    }
  ],
  "authorship": "original_extension"
}



## Tự trò chuyện: chuyến đi và những điều cần hỏi [ft01]

{
  "id": "ft01",
  "source_refs": [],
  "context_node_ids": [
    "v01",
    "g01",
    "k01",
    "sh01",
    "k02",
    "sh02",
    "S001",
    "S002",
    "S003",
    "k03",
    "sh03",
    "S004",
    "S005",
    "v02",
    "g02",
    "k04",
    "sh04",
    "S006",
    "S007",
    "S008",
    "S009",
    "S010",
    "v03",
    "g03",
    "k05",
    "sh05",
    "S011",
    "S012",
    "S013",
    "S014",
    "S015"
  ],
  "overview_vi": "Tự hỏi và xác nhận tuyến, điểm đổi tàu, cửa lên xe buýt và lối cần hỗ trợ. Ga あおば・さくら・みどり, tuyến, sân ga, xe buýt và thời gian trong ví dụ là giả định để luyện nói; không dùng làm hướng dẫn hành trình thật.",
  "optional_extensions": [],
  "context_export": "live-context.md",
  "free_talk": {
    "learner_intro_vi": "Bạn có thể kể một chuyến đi, hỏi cách đi trong mạng giả định hoặc nhờ giải thích cách nói vừa học. Không cần hoàn thành checklist; được đổi chủ đề và hỏi lại bất kỳ lúc nào.",
    "ai_situation_vi": "Trò chuyện tự do với người học Sơ về tàu điện, xe buýt và nhờ hỗ trợ. Tài liệu dưới đây là chất liệu tham khảo, không chứng minh người học đã thuộc. Gợi một chuyện cụ thể về điểm đến hoặc trải nghiệm đi lại, rồi theo điều user muốn nói. Ôn tự nhiên câu hỏi điểm đến, nơi đổi tàu, sân ga, cách nhắc lại với ね, hỏi lại khi nghe chưa rõ, cửa lên xe và lúc trả tiền; nếu user muốn thì mở rộng sang cần thang máy, chờ hỗ trợ hoặc vé không qua cổng. Đừng lần lượt hỏi hết các bài, diễn mọi vai trong ví dụ hay đọc nguyên câu thoại thay user. Chỉ giữ một vai đối tác phù hợp; dùng tiếng Nhật ngắn, dễ hiểu, giải thích bằng tiếng Việt khi user yêu cầu theo config app. Khi bí, gợi ý nhỏ, cho nói theo cách khác. Cho phép mở rộng, đổi đề tài hoặc dừng, không có điểm hoặc kết quả đạt/trượt. Các ga/tuyến/thời gian giả định là bài luyện; không khẳng định là lịch tàu hoặc thủ tục áp dụng mọi nơi. Nếu user hỏi chuyến đi thật hiện tại, không biến dữ kiện giả định thành thông tin thật; cần xác thực bằng thông tin hiện hành hoặc hỏi nhân viên phù hợp.",
    "conversation_starters_vi": [
      "Bạn hay đi tàu hay xe buýt? Có điều gì bạn muốn hỏi nhân viên mà chưa biết nói?",
      "Bạn từng đi nhầm chiều hoặc xuống quá bến chưa?",
      "Nếu mang hành lý lớn, bạn muốn hỏi nhân viên ga điều gì?"
    ],
    "mode": "free_talk",
    "content_origin": "curriculum_authored",
    "situation_export": "free-talk-situation.md"
  }
}



## Bài học và nội dung gối đầu

{
  "schema_version": "1.0",
  "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
  "lessons": [
    {
      "id": "l01",
      "summary": "Điểm đến → ga đổi → sân ga; hỏi lại khi cần.",
      "node_ids": [
        "v01",
        "g01",
        "k01",
        "sh01"
      ],
      "lookback": [],
      "reuse": [],
      "reason_no_reuse": "Bài đầu của pilot; các chặng trước chưa biên soạn, chưa có nguồn để tuyên bố đã ôn.",
      "pending_previous": [
        {
          "note": "S-011 là pilot độc lập; hai chặng gợi ý trước chưa có nội dung đã chốt. Sẽ đối chiếu khi chúng tồn tại."
        }
      ]
    },
    {
      "id": "l02",
      "summary": "ね để xác nhận; ba cuộc trao đổi tìm tàu, ga đổi và sân ga.",
      "node_ids": [
        "k02",
        "sh02",
        "S001",
        "S002",
        "S003"
      ],
      "lookback": [
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l01"
        }
      ],
      "reuse": [
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "k01"
          },
          "in": [
            {
              "node_id": "S001"
            },
            {
              "node_id": "S002"
            },
            {
              "node_id": "S003"
            }
          ],
          "purpose": "Dùng lại cách hỏi điểm đến/đổi tàu/sân ga trong các cuộc nói có lượt đáp."
        }
      ],
      "pending_previous": []
    },
    {
      "id": "l03",
      "summary": "Hỏi lại dữ kiện chưa rõ; xử lý nhầm chiều và kết lại bằng xác nhận.",
      "node_ids": [
        "k03",
        "sh03",
        "S004",
        "S005"
      ],
      "lookback": [
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l01"
        },
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l02"
        }
      ],
      "reuse": [
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "k01"
          },
          "in": [
            {
              "node_id": "S004"
            },
            {
              "node_id": "S005"
            }
          ],
          "purpose": "Nhắc lại điểm đến và xin nói lại."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l02",
            "node_id": "k02"
          },
          "in": [
            {
              "node_id": "S005"
            }
          ],
          "purpose": "Ứng dụng xác nhận với ね sau khi đã được sửa thông tin."
        }
      ],
      "pending_previous": []
    },
    {
      "id": "l04",
      "summary": "Tuyến buýt, cửa lên/trả tiền, chuyển xe, lỡ bến và báo muộn.",
      "node_ids": [
        "v02",
        "g02",
        "k04",
        "sh04",
        "S006",
        "S007",
        "S008",
        "S009",
        "S010"
      ],
      "lookback": [
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l02"
        },
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l03"
        },
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l01"
        }
      ],
      "reuse": [
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l02",
            "node_id": "k02"
          },
          "in": [
            {
              "node_id": "S006"
            },
            {
              "node_id": "S007"
            },
            {
              "node_id": "S008"
            },
            {
              "node_id": "S009"
            }
          ],
          "purpose": "Nhắc lại dữ kiện mới sau khi nghe câu trả lời."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l03",
            "node_id": "k03"
          },
          "in": [
            {
              "node_id": "S008"
            },
            {
              "node_id": "S009"
            }
          ],
          "purpose": "Duy trì cuộc trao đổi khi phải đổi phương án."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01"
          },
          "in": [
            {
              "node_id": "v02"
            },
            {
              "node_id": "S008"
            }
          ],
          "purpose": "Ôn có nghĩa các từ bến, lối vào/ra, đổi xe và tiếp theo."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01",
            "item_id": "v01-w-1a7930272017"
          },
          "in": [
            {
              "node_id": "v02",
              "item_id": "v02-w-1a7930272017"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 入口 trong nhóm xe buýt."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01",
            "item_id": "v01-w-7016090059bd"
          },
          "in": [
            {
              "node_id": "v02",
              "item_id": "v02-w-7016090059bd"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 出口 trong nhóm xe buýt."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01",
            "item_id": "v01-w-6e724a72699e"
          },
          "in": [
            {
              "node_id": "v02",
              "item_id": "v02-w-6e724a72699e"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 乗り換え trong nhóm xe buýt."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01",
            "item_id": "v01-w-172fb7e67b9b"
          },
          "in": [
            {
              "node_id": "v02",
              "item_id": "v02-w-172fb7e67b9b"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 次 trong nhóm xe buýt."
        }
      ],
      "pending_previous": []
    },
    {
      "id": "l05",
      "summary": "Nói nhu cầu, hỏi lối, chờ phối hợp và kiểm đúng điểm gặp/quầy.",
      "node_ids": [
        "v03",
        "g03",
        "k05",
        "sh05",
        "S011",
        "S012",
        "S013",
        "S014",
        "S015"
      ],
      "lookback": [
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l03"
        },
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l04"
        },
        {
          "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
          "revision": null,
          "lesson_id": "l01"
        }
      ],
      "reuse": [
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l03",
            "node_id": "k03"
          },
          "in": [
            {
              "node_id": "S013"
            },
            {
              "node_id": "S014"
            },
            {
              "node_id": "S015"
            }
          ],
          "purpose": "Hỏi lại đúng vị trí/dữ kiện còn thiếu rồi xác nhận."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l04",
            "node_id": "g02"
          },
          "in": [
            {
              "node_id": "S011"
            },
            {
              "node_id": "S012"
            },
            {
              "node_id": "S013"
            }
          ],
          "purpose": "Nghe Vてください và dùng cụm trình bày hoàn cảnh."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "g01"
          },
          "in": [
            {
              "node_id": "S011"
            },
            {
              "node_id": "S012"
            }
          ],
          "purpose": "Dùng lại điểm đến, vị trí và mong muốn."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l01",
            "node_id": "v01",
            "item_id": "v01-w-2f0ba088d763"
          },
          "in": [
            {
              "node_id": "v03",
              "item_id": "v03-w-2f0ba088d763"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 改札 khi hỏi hỗ trợ ở ga."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l04",
            "node_id": "v02",
            "item_id": "v02-w-6044e9f095e0"
          },
          "in": [
            {
              "node_id": "v03",
              "item_id": "v03-w-6044e9f095e0"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 前 khi hỏi hỗ trợ ở ga."
        },
        {
          "from": {
            "stage_uid": "da5c16e5-9425-5a4f-9086-8c109aa79c90",
            "revision": null,
            "lesson_id": "l04",
            "node_id": "v02",
            "item_id": "v02-w-45720855fc5e"
          },
          "in": [
            {
              "node_id": "v03",
              "item_id": "v03-w-45720855fc5e"
            }
          ],
          "purpose": "Ôn cùng nghĩa từ 待ちます khi hỏi hỗ trợ ở ga."
        }
      ],
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
      "note": "Đọc các phần đã ghi locator; không đọc toàn sách."
    },
    {
      "book_id": "B02",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B03",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B04",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B05",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B06",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B07",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B08",
      "status": "read",
      "note": "Đọc các phần đã ghi locator; không đọc toàn sách."
    },
    {
      "book_id": "B09",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B10",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B11",
      "status": "read",
      "note": "Đọc các phần đã ghi locator; không đọc toàn sách."
    },
    {
      "book_id": "B12",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B13",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B14",
      "status": "read",
      "note": "Đọc các phần đã ghi locator; không đọc toàn sách."
    },
    {
      "book_id": "B15",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B16",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B17",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B18",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B19",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B20",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B21",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B22",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B23",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B24",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B25",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B26",
      "status": "index_only",
      "note": "Đã quét mục lục/chỉ mục theo chủ đề/chức năng; không chọn để đọc sâu cho pilot này."
    },
    {
      "book_id": "B27",
      "status": "read",
      "note": "Đọc các phần đã ghi locator; không đọc toàn sách."
    }
  ],
  "entries": [
    {
      "id": "src-b08",
      "kind": "book",
      "book_id": "B08",
      "title": "どんどん話せる！日本語会話フレーズ大特訓 必須700",
      "path": "kaiwa_skill/knowledge/どんどん話せる！日本語会話フレーズ大特訓 必須700/chapters/04-part4-bamen.md",
      "sha256": "ba773e01d02ce1bb2e8ada8ccb568e9c870c4c045186011519865fe785a953cd",
      "read_status": "read",
      "locator": "u-part4-unit01, u-part4-unit02; lines 8–64",
      "note": "Mẫu hỏi điểm đến, đổi tàu, sân ga; hỏi lúc trả tiền; giản hóa khi cần.",
      "used_for": [
        "k01",
        "sh01",
        "k04",
        "sh04",
        "k05",
        "sh05"
      ]
    },
    {
      "id": "src-b11",
      "kind": "book",
      "book_id": "B11",
      "title": "わかる！話せる！日本語会話 基本文型88",
      "path": "kaiwa_skill/knowledge/わかる！話せる！日本語会話 基本文型88/chapters/01-ne.md",
      "sha256": "04abb8c4d2276904f5e524a40b965a4c3704fa494fbaaeba1733c23ae7a9ad27",
      "read_status": "read",
      "locator": "u-part1-01; toàn bài lines 1–116",
      "note": "Giữ ba chức năng của ね; chọn xác nhận/báo ý định cho video, ví dụ đi lại viết mới.",
      "used_for": [
        "k02",
        "sh02"
      ]
    },
    {
      "id": "src-b01",
      "kind": "book",
      "book_id": "B01",
      "title": "5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày",
      "path": "kaiwa_skill/knowledge/5500 câu giao tiếp tiếng Nhật trong sinh hoạt hằng ngày/chapters/07-phuong-tien-van-chuyen.md",
      "sha256": "c1e5c23ef8c4359b25fe3a794879a809514831ec79332e81ffbda167cc4038fb",
      "read_status": "read",
      "locator": "Xe buýt lines 6–127",
      "note": "Nhóm câu đổi xe, hỏi nơi xuống và đi quá bến; chỉnh cách nói cho tự nhiên, không bê các câu nguồn lạ.",
      "used_for": [
        "k04",
        "sh04"
      ]
    },
    {
      "id": "src-b14",
      "kind": "book",
      "book_id": "B14",
      "title": "シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版",
      "path": "kaiwa_skill/knowledge/シャドーイング 日本語を話そう！ 初～中級編 インドネシア語・タイ語・ベトナム語版/chapters/02-unit-1.md",
      "sha256": "7d751d79b9578ca8a73bf18fd652d9b9828138ddc43fa46f2dda181c2f19c686",
      "read_status": "read",
      "locator": "lines 302–321 và 619–628, các đoạn hội thoại hoàn chỉnh",
      "note": "Nhịp xác nhận, hỏi vị trí và lặp từ chưa rõ; chọn cách hỏi lại, không nhập cảnh hết tàu sang chặng này.",
      "used_for": [
        "k03",
        "sh03"
      ]
    },
    {
      "id": "src-b27",
      "kind": "book",
      "book_id": "B27",
      "title": "聞いて覚える話し方 日本語生中継 初中級編２",
      "path": "kaiwa_skill/knowledge/聞いて覚える話し方 日本語生中継 初中級編２/chapters/09-bai-08-eki-de.md",
      "sha256": "3f3179efa77c6ecef13d005a06bbf068633001a26244750767f4e5ccfb2cefd9",
      "read_status": "read",
      "locator": "u-sh2-l08-expression-check tới u-sh2-l08-expression-uncertain-practice, lines 119–182",
      "note": "Hỏi kiểm thông tin và phân biệt chưa chắc; không bắt dùng các mẫu trung cấp dài ở Sơ.",
      "used_for": [
        "k03",
        "sh03"
      ]
    },
    {
      "id": "src-minna",
      "kind": "reference",
      "path": "kaiwa_skill/reference/grammar/MINNA_01_50_GRAMMAR.json",
      "sha256": "77503e668fd152260f34a49c18986030209779df413b52822b78eeffd42b73d2",
      "locator": "Bài 3,5,6,13,14,15,26",
      "note": "Tên mẫu đối chiếu index; level N5/N4 là mapping biên tập để tìm kiếm, không danh mục JLPT chính thức.",
      "used_for": [
        "g01",
        "g02",
        "g03"
      ]
    },
    {
      "id": "src-kyoto",
      "kind": "web",
      "url": "https://www2.city.kyoto.lg.jp/kotsu/webguide/en/bus/howtoride_bus.html",
      "retrieved_on": "2026-11-13",
      "locator": "How to Get on & off the Bus, khác biệt EX100/101 và tuyến khác",
      "note": "Chỉ dùng xác nhận quy tắc lên/trả tiền có thể khác theo tuyến. Không nhập giá thật vào ví dụ giả định.",
      "used_for": [
        "k04"
      ]
    },
    {
      "id": "src-jr",
      "kind": "web",
      "url": "https://www.jreast.co.jp/en/equipment/equipment_1/wheelchair/",
      "retrieved_on": "2026-11-13",
      "locator": "駅の利用, 係員のご案内 và その他のお願い事項",
      "note": "Có thể cần liên hệ/phối hợp/chờ; các điểm gặp và phút chờ trong bài là giả định, không bảo đảm dịch vụ.",
      "used_for": [
        "k05"
      ]
    }
  ]
}

