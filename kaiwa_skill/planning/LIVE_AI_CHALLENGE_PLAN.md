# Kế hoạch bổ sung Live AI Challenge vào skill biên soạn chặng

Ngày: 2026-11-13. Trạng thái: **thiết kế challenge để duyệt; phần free talk đã bổ sung vào skill/hợp đồng V3.2. Chưa sửa Harumi**.

Người dùng chốt bổ sung: free talk cuối chặng phải có sẵn tình huống/context tổng hợp kiến thức trong chặng. **Giới hạn 1.000 ký tự chỉ dành cho tình huống user tự nhập trong app, không áp cho challenge hoặc free talk của lộ trình do tác giả biên soạn.** Harumi sẽ tích hợp luồng nội dung lộ trình phù hợp; không thiết kế nội dung quanh giới hạn nhập tay.

Giữ lộ trình V5 hiện hành: **289 chặng, Sơ 80 / Trung 145 / Thượng 64**. Không thêm chặng cho đủ 300. Challenge là nội dung bên trong chặng, không phải chặng mới hoặc bài kiểm tra.

## 1. Kết luận thiết kế

Skill cần bổ sung loại node `live_challenge`, xuất **hai phần nội dung riêng từ cùng một bản dữ liệu gốc**:

1. **Phần người học:** bối cảnh, vai, việc cần trao đổi, gợi ý các bước và kiến thức/cách nói có thể dùng.
2. **Phần AI:** tình huống nhập vai, thông tin của nhân vật, cách phản ứng và nhánh diễn biến để người học thực sự phải hỏi, giải thích, xác nhận, thương lượng…

Một chặng có một hoặc vài challenge phù hợp, xen sau những cụm kiến thức và tình huống liên quan. Không ấn định số lượng giống nhau cho mọi chặng. Giữ node **free talk cuối chặng** như một lựa chọn riêng. Skill phải soạn cả tình huống free talk và context học đầy đủ, không chỉ tên topic hoặc danh sách con trỏ.

Mạch học gợi ý:

> Từ vựng/ngữ pháp cần dùng → kiến thức → shadowing ví dụ → tình huống mẫu → challenge vận dụng → kiến thức/tình huống tiếp theo → challenge tổng hợp nếu có ích → free talk.

Đây là mạch đề xuất; người học được mở bất kỳ node nào. Với Speak Japanese, vẫn giữ **kiến thức dành cho video → shadowing ví dụ ngay sau video**, rồi mới đặt challenge. Challenge yêu cầu chuyển kiến thức sang một cuộc trao đổi mới, không yêu cầu đọc lại hội thoại đã thuộc.

## 2. Những gì đã kiểm trong Harumi

Các đường dẫn Harumi dưới đây tính từ `D:/CODE/git/harumi`. Đã đọc thiết kế/config mẫu và đối chiếu các phần code liên quan; **chưa truy cập config DB đang active, chưa gọi Live, chưa chạy thử giọng nói**. Những nhận xét về runtime là từ code; hành vi hội thoại vẫn cần pilot thật.

### Đã có đường truyền tình huống vào prompt

- `frontend/src/lib/kaiwa/scenarioLaunchAnswers.ts:36`: `buildScenarioLaunchAnswers()` tạo `scenarioMode=customize`, kèm node text `customizeDescription`.
- `frontend/src/components/kaiwa/KaiwaScenarioSetupPanel.tsx:71`: luồng tùy chỉnh gọi start với `quickStart: false`, `characterId`, `answers`.
- `backend/src/Harumi.ChatPractice/Shared/KaiwaCallPromptCompileService.cs:56`: quick start lấy câu trả lời mặc định; nội dung challenge cần đi bằng luồng customize.
- Cùng file, `ResolveScenarioSituationRaw()` lấy text của `customizeDescription`; chế độ resume/reuse có thể lấy tình huống và config snapshot cũ.
- `frontend/src/lib/kaiwa/liveSessionClient.ts:265`: client nhận token/setup từ backend. Không cần skill tạo token, websocket hay cấu hình giọng nói.

Vì vậy skill có thể xuất text để gắn đúng chỗ tình huống hiện có. **Không cần thiết kế lại engine Live để biên soạn challenge.**

### Config mẫu chưa phải config đang chạy

- `Shared/KaiwaConfigService.cs:22`: nguồn active là `KaiwaSystemConfig.ConfigJson` trong DB; seed là fallback.
- `design/kaiwa-ai/kaiwa_config.sample_v7.json` dùng schema `kaiwa-config-v4`; số v7 là phiên bản file mẫu.
- Trong mẫu v7 và seed, `customizeDescription.maxLength=1000`. Mẫu v7 có `learnerCompiledPromptMaxLength=12000`.
- `Shared/KaiwaModerationService.cs:91` kiểm độ dài theo runtime settings và có thể từ chối nội dung quá dài. `Shared/KaiwaPartTreeResolver.cs:518` dùng lại text đã được moderation xác nhận; đường fallback gọi `SanitizeFreeText`, có khả năng cắt theo giới hạn node. Không được giả định mọi đường đều cắt, hoặc mọi đường đều từ chối như nhau.
- `Shared/KaiwaPromptComposer.cs:35` kiểm độ dài prompt learner sau ghép. Độ dài ở đây là chuỗi .NET/UTF-16, **không phải số token**.

Đây là quan sát về **luồng user nhập tay hiện có**, không phải trần biên soạn lộ trình. Không cắt/rút kiến thức để vừa trường này. Khi tích hợp nội dung lộ trình, app cần cách nạp riêng và ngân sách context phù hợp; giữ bản đầy đủ, không cắt âm thầm. Chưa xác minh config DB production.

### Prompt gốc đặt một số ranh giới hữu ích

Master prompt mẫu v7:

- AI là một người nhập vai, giữ một giọng/nhân vật xuyên suốt.
- Ưu tiên người học nói nhiều; hỗ trợ khi bí, không đóng vai giáo viên chấm bài.
- Mặc định trò chuyện tự nhiên và có thể chuyển chủ đề; tình huống cụ thể cần nói rõ phạm vi hoạt động ban đầu.
- Tình huống tùy chỉnh được bọc `UNTRUSTED_USER_INPUT`: dùng làm bối cảnh, không phải quyền ghi đè chỉ dẫn gốc.
- Nhân vật đã có tên, quan hệ, mô tả; tình huống mới có thể xung đột nếu lấy nhân vật không phù hợp.

Challenge phải tương thích các nguyên tắc đó. Không viết “bỏ qua prompt trước”, không bắt AI đọc checklist cho người học, không biến cùng một nhân vật thành nhân viên ga rồi thành cảnh sát hoặc người bạn trong một cuộc gọi.

### Phần hiển thị nhiệm vụ chưa có hợp đồng riêng trong luồng đã kiểm

- `frontend/src/lib/kaiwa/types.ts:258`: request hiện có `characterId`, `quickStart`, `answers`… chưa có trường challenge với mục tiêu/gợi ý riêng.
- `components/kaiwa/KaiwaCallScreen.tsx` sử dụng `useKaiwaCall`; chưa thấy bộ dữ liệu nhiệm vụ/challenge trong các interface và màn hình đã kiểm.
- `components/learning/templates/AIKaiwa.tsx:30` vẫn ghi rõ integration placeholder. Không coi component này là cầu nối Learning → Live đã hoàn thiện.

Do đó **dữ liệu có thể soạn ngay**, nhưng việc hiển thị brief ở node/cuộc gọi và nối node học sang Live là phần tích hợp Harumi riêng. Plan này chỉ xác định dữ liệu app cần nhận, chưa sửa UI hoặc thêm API.

### Xem trước admin không thay được kiểm tra learner

`backend/src/Harumi.ChatPractice/Extensions/EndpointExtensions.cs:331`: `/calls/preview-prompt` chỉ cho admin và gửi `IsAdmin=true` vào compiler. Admin có chính sách bỏ qua giới hạn learner.

Sau này kiểm tương thích cần fixture/compiler chạy dưới chính sách learner và một lượt pilot tài khoản thường; không coi preview admin thành công là đủ. Không cần thêm endpoint public xem system prompt.

## 3. Cách chọn challenge cho từng chặng

Tác giả phải đọc lại mục tiêu chặng, kiến thức và các cụm tình huống đã biên soạn rồi mới chọn nhiệm vụ.

1. **Chọn một việc ngoài đời có điểm kết thúc tự nhiên:** tìm được cách đi, thống nhất lịch, làm rõ điều kiện xin phép, chốt phương án đặt bàn…
2. **Ghép các hành động giao tiếp cùng một sự kiện:** mở lời → nêu nhu cầu → hỏi thêm → xử lý thông tin mới → xác nhận → kết thúc.
3. **Chọn kiến thức/từ/ngữ pháp hỗ trợ**, gồm nội dung hai bài trước và bài cũ có liên quan. Ghi rõ phần nào mới, phần nào ôn; không coi bài chưa viết là đã dạy.
4. **Tạo khoảng trống thông tin:** người học biết nhu cầu của mình; AI biết thông tin cần hỏi. AI không tự đọc hết mọi đáp án ngay lượt đầu.
5. **Thêm diễn biến có ích:** nghe nhầm, cần xác nhận, không được đáp ứng ngay, phương án thay thế, thay đổi điều kiện… Chọn biến thể phù hợp, không dồn mọi rắc rối vào một lượt luyện.
6. **Ghi lý do đặt node tại đây:** người học vừa có đủ chất liệu để thử nói tự lập, hoặc đây là lúc kết hợp các cụm đã học.

Một challenge có thể bao phủ vài tình huống mẫu. Không cần một challenge cho mỗi tình huống; cũng không bắt một challenge phải gánh toàn chặng. Các nhánh đồng ý/từ chối/có điều kiện nên thành biến thể rõ, để luyện lại có giá trị.

Nếu sự kiện cần nhiều người, chia thành các challenge liên tiếp, mỗi challenge một đối tác. Thông tin nối tiếp phải được khai báo trong bối cảnh; không giả định app đã tự chuyển kết quả cuộc gọi trước sang cuộc gọi sau.

### Độ khó là chất lượng trao đổi

- **Sơ:** nhiệm vụ cụ thể, ít thông tin cùng lúc, gợi ý rõ; vẫn có hỏi lại và xác nhận. Không chỉ trả lời có/không.
- **Trung:** kết hợp lý do, điều kiện, câu hỏi tiếp nối, phương án khác, điều chỉnh sau phản hồi.
- **Thượng:** xử lý ý chưa nói thẳng, ưu tiên xung đột, thuyết phục, sắc thái quan hệ, thông tin thiếu và giải pháp thỏa đáng.

Không tự đồng nhất ba cấp của lộ trình với một JLPT cố định. Ghi yêu cầu ngôn ngữ thực tế của challenge; profile learner của app vẫn do app quản lý.

## 4. Hai phần dữ liệu cho một challenge

### A. Phần hiện cho người học

- Tên nhiệm vụ và bối cảnh ngắn bằng tiếng Việt.
- Bạn là ai, đang nói với ai; thông tin bạn đã biết và nhu cầu riêng của bạn.
- Những việc cần trao đổi để giải quyết tình huống, diễn đạt như mục tiêu giao tiếp, không phải rubric chấm điểm.
- Gợi ý các bước, chỉ mở khi cần nếu app hỗ trợ.
- Từ/cụm, tên ngữ pháp và liên kết kiến thức có thể dùng; thêm ít mẫu câu mở đầu hoặc câu cứu nguy. Không đưa cả bài trả lời chuẩn.
- Lời nhắc được hỏi lại, nói theo cách khác, yêu cầu giúp hoặc dừng bất kỳ lúc nào.

Không hiện sẵn toàn bộ thông tin AI đang nắm hoặc bí mật của biến thể. Nhưng phải cung cấp đủ dữ kiện để người học biết mình muốn gì, không bắt họ đoán đề.

### B. Phần gắn vào tình huống gửi AI

- Vai đối tác duy nhất, quan hệ và nơi đang trao đổi.
- Nhu cầu của người học để AI phối hợp đúng cảnh; không coi đây là lời user đã nói trong hội thoại.
- Dữ kiện AI biết, điều kiện có thể đáp ứng, phương án thay thế, điều chưa biết/không có thẩm quyền quyết.
- Cách phản ứng khi người học hỏi, hiểu nhầm, đề nghị khác hoặc cần hỗ trợ.
- Biến thể đã chọn cho lần luyện này; không tự đổi dữ kiện ngẫu nhiên giữa cuộc nói.
- Phạm vi kiến thức/ngôn ngữ vừa sức. Hỗ trợ bằng cách đơn giản hóa hoặc gợi ý nhỏ, không nói hết phần của user.
- Khi việc đã giải quyết, xác nhận trong vai và để user kết thúc hoặc nói tiếp. Không phát thông báo “đạt/trượt”, không tự đóng cuộc gọi.

AI phản ứng theo **ý nghĩa** lời nói, không so khớp chuỗi câu hoặc bắt đủ mẫu ngữ pháp. Người học đổi chủ đề/yêu cầu trợ giúp thì tôn trọng ưu tiên hiện có của app; mục tiêu là trợ giúp luyện nói.

## 5. Một ví dụ preview

Ví dụ minh họa cho chặng **S-011 — Tàu điện & xe buýt**, key cũ `S-14`, UID `da5c16e5-9425-5a4f-9086-8c109aa79c90`.

Các tình huống V5 có thể kết hợp: `S001` hỏi tàu có tới ga cần không, `S002` hỏi ga đổi, `S003` hỏi sân ga tiếp theo, `S005` nhắc lại để xác nhận. Phần hỏi mua vé dưới đây là mở rộng mới theo yêu cầu người dùng, **chưa gán nguồn sách hoặc node đã tồn tại**.

### Người học nhìn thấy

**Hỏi đường và cách mua vé ở ga**

Bạn đang ở ga あおば, muốn đến ga みどり. Hãy trao đổi với nhân viên để biết cách đi và cách mua vé. Đây là mạng tàu giả định dùng để luyện nói.

Việc cần trao đổi:

- Tàu có đi thẳng không; nếu phải đổi thì đổi ở đâu và sang sân ga nào.
- Giá vé, cách mua và nơi có thể mua vé.
- Nhắc lại thông tin quan trọng để chắc rằng mình đã hiểu, rồi cảm ơn.

Gợi ý khi cần:

1. Mở lời: `すみません。ちょっといいですか。`
2. Nêu điểm đến và hỏi cách đi: `みどり駅に行きたいんですが…。`
3. Hỏi tiếp điều chưa rõ: `どこで乗り換えますか。` / `何番線ですか。`
4. Hỏi vé: `切符はどこで買えますか。` / `いくらですか。`
5. Xác nhận lại theo thông tin vừa nghe. Có thể nhờ nói lại: `もう一度、お願いします。`

Đây là gợi ý nói, không phải các câu bắt buộc. Chỉ chính thức gắn tên ngữ pháp/node ôn khi đã đối chiếu bài học thực tế.

### AI nhận được trong trường tình huống

```text
Mô phỏng tại ga あおば giả định. Bạn chỉ đóng vai nhân viên ga; người học là hành khách muốn đến ga みどり và hỏi cách mua vé. Dữ kiện cố định: đi tuyến A đến さくら, đổi sang tuyến B tại sân ga 2; vé 320 yên, mua ở máy cạnh quầy, chọn màn hình tiếng Việt được. Đây là dữ kiện luyện tập, không phải thông tin tàu thật. Trả lời tiếng Nhật ngắn, dễ hiểu ở mức Sơ. Hãy chào như nhân viên ga rồi nhường lượt; đợi khách hỏi, cung cấp phần liên quan, không đọc hết đường đi và cách mua vé ngay đầu. Nếu khách nhắc sai ga đổi/sân ga thì đính chính nhẹ. Nếu khách chưa biết mua vé thì hướng dẫn từng bước khi họ hỏi. Giữ nguyên dữ kiện, không nói thay khách hoặc bắt họ đọc câu chuẩn. Khi khách bí, đơn giản hóa hoặc gợi ý nhỏ trong vai. Khi khách xác nhận xong, đáp tự nhiên và để họ cảm ơn/kết thúc hoặc hỏi thêm; không chấm điểm. Tôn trọng yêu cầu dừng, trợ giúp hoặc đổi chủ đề.
```

Một biến thể khác có thể đổi thành máy bán vé đang không dùng được và quầy có bán vé. Biên soạn thành variant riêng, chọn trước khi xuất prompt; không gắn cả hai bộ dữ kiện mâu thuẫn vào cùng một tình huống. Brief phải được cập nhật nếu mục tiêu thay đổi.

## 6. Hợp đồng biên soạn đề xuất

Đây là **schema mới đề xuất cho kho nội dung**, không phải API Harumi đã có.

Một JSON gốc cho mỗi challenge, dùng để dẫn xuất learner Markdown và AI situation text:

```text
id, revision, stage_uid, type=live_challenge, title_vi
placement: after_node_ids, rationale_vi
covers: event_ids, situation_uids, communicative_functions
learning_refs: knowledge_node_ids, vocabulary_node_ids, grammar_refs
reuse_refs: các node/bài trước + revision đã đọc
learner_brief:
  scene_vi, learner_role_vi, counterpart_role_vi, known_facts
  goals[], optional_steps[], hints[], suggested_expressions[]
ai_scenario:
  counterpart_role, world_facts, information_reveal_policy
  response_branches, help_policy, natural_closure, language_scope
variants[]: id, facts_override, branch, learner_brief_adjustments
exports: learner_brief_md, ai_situation_txt
provenance, fact_check, change_log
```

Quy tắc:

- Dùng UID chặng và UID tình huống V5; local `S001` chỉ có nghĩa bên trong chặng. Node kiến thức chưa viết phải ghi unresolved trong bản kế hoạch, không bịa liên kết đã tồn tại. Bản nội dung chốt không được còn tham chiếu treo.
- Mục tiêu trong brief và phản ứng trong AI phải khớp. Mỗi mục tiêu phải có cơ hội thực hiện trong cảnh; AI phải có đủ thông tin hoặc cách xử lý khi không biết.
- `placement` là chỉ dẫn biên tập/thứ tự, không phải điều kiện mở khóa.
- Mỗi bản xuất chọn một variant và ghi ID/revision/variant/hash trong manifest. Không để exporter tự sửa nội dung để vừa giới hạn.
- Kiến thức và hội thoại tự viết mang nhãn trung thực. Dữ kiện giả định ghi rõ; thông tin ngoài đời có rủi ro sai cần nguồn và thời điểm kiểm thích hợp.
- Không đưa rubric, điểm phát âm, điểm hoàn thành, test hoặc trạng thái learner vào schema này.

Đầu ra dự kiến trong revision chặng:

```text
challenges/ch01.json              # bản gốc biên soạn
challenges/ch01.learner.md        # dẫn xuất để preview/hiển thị
challenges/ch01.ai-situation.txt  # dẫn xuất cho một variant đã chọn
```

Brief và AI prompt phục vụ hai đối tượng; không dán toàn bộ brief có gợi ý đáp án vào phần AI một cách máy móc. Giữ bản đầy đủ để biên tập, bản xuất runtime phải ngắn và đủ đúng nhiệm vụ.

## 7. Cách dùng với Harumi hiện có

Nội dung lộ trình dùng **luồng do tác giả chuẩn bị**, tách với tình huống user nhập tay. Skill xuất đầy đủ tình huống challenge, brief cho người học và tình huống/context free talk. Không áp trần 1.000 ký tự hoặc bắt rút gọn để chạy qua form hiện tại.

Helper hiện có minh họa vị trí tình huống đi vào prompt; đây **không phải hợp đồng import cuối cùng cho lộ trình**:

```text
answers = buildScenarioLaunchAnswers(activeLearnerConfig, "customize", {
  languageKey: một lựa chọn hợp lệ trong config,
  customSituationText: nội dung ai-situation.txt
})
startCall({ characterId: nhân vật phù hợp, quickStart: false, answers, ... })
```

Đây là mô tả nối dữ liệu, không phải đoạn code hoàn chỉnh đã triển khai.

- Không truyền prompt tự do trực tiếp thành `systemInstruction`, không bịa part `challengePrompt` mà config chưa khai báo.
- Lượt mới không dùng `resume_last`, `reuse_recent_setup` hoặc `continueFromSummaryId` của bài khác. Nếu tiếp tục đúng một challenge thì cần giữ định danh/revision/variant; cơ chế ràng buộc này là đề xuất tích hợp sau, chưa có trường dedicated trong request hiện đã kiểm.
- Chọn nhân vật có vai phù hợp. Chưa thể khẳng định thêm text “bạn là nhân viên ga” sẽ luôn thắng quan hệ/mô tả của một nhân vật người yêu hoặc sếp.
- App sẽ phân biệt nội dung lộ trình đã biên soạn và text user tự nhập; không lấy quyền admin làm cách phát nội dung cho learner. Điều chỉnh giới hạn/adapter ở Harumi là phần tích hợp riêng.
- Challenge dùng ngữ cảnh phù hợp nhiệm vụ; free talk có phần tổng hợp và tài liệu toàn chặng. Giữ hai mục đích này, không rút cả hai thành một prompt ngắn chung.
- Kiểm ngân sách context thực tế khi tích hợp model/vận chuyển; nếu cần chọn lọc hoặc chia gói, giữ bản đầy đủ và ghi rõ lựa chọn. Không coi 1.000 ký tự là quy tắc tác giả hoặc tiêu chí nghiệm thu nội dung.

Thiết kế adapter nội dung khóa học phía Harumi ở bước riêng, hỗ trợ context lộ trình và đồng bộ brief–prompt. Chưa đề xuất tên bảng/endpoint mới hoặc sửa engine trong lượt cập nhật skill này.

## 8. Những phần skill cần sửa sau khi duyệt

Trong `.agents/skills/kaiwa-stage-content/`:

1. **`SKILL.md`:** thêm bước thiết kế challenge sau cụm bài phù hợp; sửa bước 10 từ “một Live AI” thành “các challenge theo nhu cầu + một free talk cuối chặng”. Giữ toàn bộ quy tắc Speak Japanese, shadowing, gối đầu, nguồn và học tự do.
2. **`references/content-contract.md`:** thêm `live_challenge`, hợp đồng hai phần, variant, placement, provenance; phân biệt với `live_context` hiện có. Phần free talk đã nâng V3.2: `free_talk` do tác giả soạn + `free-talk-situation.md` kèm tài liệu toàn chặng.
3. **Thêm `references/live-challenges.md`:** cách xây nhiệm vụ tổng hợp, khoảng trống thông tin, độ khó, phản ứng, hướng dẫn tương thích Harumi và ví dụ.
4. **`references/progression.md`:** challenge sử dụng kiến thức hai bài trước nhưng không tự tính thành một bài kiến thức mới làm trượt cửa sổ ôn. Kết quả ôn phải chỉ tới nội dung thực tế và revision đã đọc.
5. **`references/editorial-workflow.md` và `situation-coverage.md`:** đưa việc chọn/tổng hợp nhiệm vụ vào sau bản đồ tình huống; ghi phần được luyện qua challenge và phần có chủ ý chỉ giữ bài mẫu. Không ép phủ 100%.
6. **`references/checkpoint.md`:** checkpoint tới từng challenge/variant; sửa một bài đánh dấu các challenge phụ thuộc cần đọc lại, không sinh lại toàn chặng.
7. **`scripts/stage_work.py`:** nhận type challenge mới; kiểm liên kết/ID/placement; xuất hai phần; phân loại node trong learning-map. Phần free talk V3.2 đã có kiểm trường/thứ tự cuối chặng và exporter; vẫn đọc V3.0/V3.1. Không có trần 1.000 ký tự cho dữ liệu lộ trình.

**Điểm phải sửa đặc biệt:** hợp đồng hiện bắt `live-context.md` ghép mọi node khác. Khi có nhiều challenge, không được ghép mọi AI instruction vào cùng prompt free talk, gây xung đột vai và nhiệm vụ. Kho context đầy đủ có thể chứa kiến thức, từ, ngữ pháp, mẫu luyện và mô tả challenge dưới dạng tài liệu; các chỉ dẫn nhập vai executable phải tách riêng. Prompt một challenge chỉ chọn một cảnh/variant, không nạp lệnh của challenge khác.

Các kiểm tra phần mềm ở đây chỉ bảo đảm dữ liệu và exporter hoạt động đúng; không tạo bài test cho người học. Kiểm ngữ nghĩa, tính tự nhiên và khả năng khiến user chủ động nói vẫn do biên tập/pilot.

## 9. Áp dụng vào V5 và thử nghiệm

### Bước 1 — sửa hợp đồng và helper

Sau khi duyệt plan, sửa đúng các phần trên. Không thay UID, cụm, số lượng và thứ tự 289 chặng. Blueprint challenge ở lớp biên soạn nội dung; registry V5 tiếp tục là khung điều hướng.

### Bước 2 — pilot ba kiểu chặng

- **S-011 — Tàu điện & xe buýt**, key `S-14`: hỏi tuyến/chuyển tàu/xác nhận; thử phần mở rộng mua vé. Kiểm AI nhường lượt, không tự cung cấp hết đáp án.
- **T-073 — Xin phép & xác nhận lại**, key `T-35`: cùng một đối tác quyết định cho phép/từ chối/có điều kiện. Ví dụ cụm `S001–S004` đã có trong V5; tạo variant và xử lý bước tiếp theo, không nhồi cả ba kết quả vào một lượt.
- **T-117 — Làm 幹事 cho nomikai và tiệc đón tiễn**, key `V5P-118`: gom nhu cầu đặt chỗ, điều kiện quán, thay đổi số người và xác nhận trong các cảnh hợp vai. Cuộc nói với leader và cuộc nói với quán phải tách. Đọc lại toàn cụm rồi mới chọn UID tình huống cụ thể.

Ba chặng dùng để kiểm ba dạng nhiệm vụ, không phải cam kết mỗi chặng chỉ có một challenge. Nếu pilot chưa có bài kiến thức thực tế, chỉ chốt blueprint và ví dụ preview; chưa gọi đó là node hoàn chỉnh để xuất app.

Kiểm pilot:

- Brief đủ rõ nhưng không lộ hết đáp án; user có việc để tự động não và hỏi tiếp.
- AI nhận đủ thông tin, phản ứng được với cách nói khác và nhánh đã chọn; không giả làm nhiều người.
- Câu gợi ý và yêu cầu ngôn ngữ đúng chất liệu đã học; nhiệm vụ giải được mà không bắt thuộc mẫu.
- Hai bản xuất đồng nhất và không bị cắt; luồng tích hợp lộ trình đáp ứng ngân sách context thực tế, không áp giới hạn nhập tay 1.000 ký tự. Không lỗi khi tiếp tục cùng bài hoặc bắt đầu bài khác.
- Thử người học hỏi lại, bí từ, hiểu nhầm, đề xuất khác và xin dừng. Không có đạt/trượt hoặc khóa bài.
- Offline có thể kiểm nội dung/hợp đồng trước; khả năng nói thực tế chỉ kết luận sau khi thử Live với cấu hình active phù hợp.

### Bước 3 — mở rộng theo từng chặng

Khi biên soạn sâu mỗi chặng V5, tạo challenge sau khi đã chọn kiến thức và mẫu luyện. Ghi covers/reuse/placement và checkpoint. Không sinh hàng loạt prompt sơ sài cho 289 chặng trước khi biết nội dung học.

Theo dõi ngắn gọn: chặng đã có blueprint/challenge đã duyệt, sự kiện/chức năng được luyện, phần chưa chọn và lý do. Đây là thông tin biên tập để nâng cấp, không phải KPI phải tận dụng 100% nguồn.

## 10. Pause, phục hồi và chỉnh sửa

- Mỗi challenge có ID ổn định, revision và variant rõ. Sửa wording giữ ID; đổi bản chất nhiệm vụ thì tạo ID mới và ghi thay thế.
- Checkpoint ghi việc đã đọc, dữ liệu đã viết, variant còn thiếu, tham chiếu chưa giải quyết và next action.
- Chỉnh từ vựng/kiến thức/tình huống nguồn chỉ đánh dấu các challenge liên quan cần rà lại; không viết đè revision đã chốt hoặc thay prompt của phiên đang dùng snapshot.
- Ví dụ yêu cầu nâng cấp: “Trong T-117, thêm biến thể quán không nhận giảm số người sát giờ; giữ các challenge khác.” Tác giả tra UID và phụ thuộc, sửa đúng phạm vi, xuất lại hai phần và ghi revision mới.

## Phạm vi hoàn thành của lượt lập plan này

Đã điều tra code/config liên quan và viết đề xuất kèm ví dụ hai đầu ra. Sau góp ý của người dùng, đã bổ sung free talk biên soạn sẵn vào skill, hợp đồng V3.2 và helper xuất dữ liệu; bỏ giới hạn nhập tay khỏi thiết kế nội dung lộ trình. Hợp đồng/helper challenge vẫn là bước tiếp theo, chưa triển khai. **Chưa tạo nội dung courseware, chưa đổi V5, chưa sửa Harumi hoặc gọi API Live.**
