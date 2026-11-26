"""Second editorial pass: directly solve text-sufficient B drills across 50 lessons.

Keys were chosen by reading each source cue and option bank, then checked against
the lesson's B instruction. No key is represented as a source reveal.
"""

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

from renshuu_dom import parse, reviewed_snapshots
from renshuu_examples import text_only_instruction

ROOT = Path(__file__).resolve().parents[1]

# Values are the exact grammatical fragment(s) from each source option bank.
ANSWERS = {
 1: {'b3':['じゃ ありません。']*4},
 2: {'b4':['本ですか、','「い」ですか、','「1」ですか、','「シ」ですか、']},
 3: {
  'b3':['…1階です。','…教室です。','…地下です。','…事務所です。'],
  'b4':['…そちらです。','…こちらです。','…3階です。','…大阪です。'],
 },
 4: {
  'b2':['ペキンは 今 何時ですか。','バンコクは 今 何時ですか。','ロンドンは 今 何時ですか。','ロサンゼルスは 今 何時ですか。'],
  'b3':['あしたは 何曜日ですか。','会議は 何曜日ですか。','試験は 何曜日ですか。','休みは 何曜日ですか。'],
  'b4':['…9時から','…10時から','…9時から','…9時15分から'],
  'b6':['働きます。','休みます。','働きます。','勉強します。'],
  'b8':['働きません。','勉強します。','勉強しました。','働きませんでした。'],
  'b9':['寝ますか。','起きましたか。','働きますか。','勉強しましたか。'],
 },
 5: {
  'b4':['…彼女と','…会社の 人と','…家族と','…一人で'],
  'b5':['…9月14日に','…来年の 3月に','…来月','…今週の 水曜日に'],
  'b6':['…一人で','…アメリカへ','…船で','…来年の 12月に'],
  'b7':['…バスと 電車で','…7時に','…木村さんと','…どこも'],
 },
 6: {
  'b2':['飲みません。','勉強します。','読みました。','見ませんでした。'],
  'b3':['何を']*4,
  'b5':['…駅で','…会社の 食堂で','…スーパーで','…大学で'],
 },
 7: {
  'b6':['もらいました。','…アメリカの 大学で','…あした','…友達に'],
  'b7':['まだです。','行きました。','まだです。','寝ました。'],
 },
 8: {
  'b2':['じゃ ありません。','じゃ ありません。','じゃ ありません。','じゃ ありません。'],
  'b3':['くないです。','くないです。','くないです。','よくないです。'],
  'b4':['じゃ ありません。','安いです。','よくないです。','便利です。'],
  'b6':['新しい','な','いい','な'],
  'b7':['どんな']*4,
  'b8':['冷たい','な','な','新しい'],
 },
 9: {
  'b1':['好きです。','好きじゃ ありません。','好きです。','好きじゃ ありません。'],
  'b4':['わかります。','わかりません。','わかります。','わかりません。'],
  'b5':['あります。','ありません。','ありません。','あります。'],
  'b6':['が']*4,
  'b8':['下手ですから。','嫌いですから。','行きますから。','たくさん ありましたから。'],
 },
 10: {'b3':['何が','だれが','何が','だれが'],
      'b5':['あります。','います。','あります。','あります。']},
 11: {
  'b5':['1日に','1週間に','1か月に','1年に'],
  'b6':['4年','2週間','5時間','10分だけ'],
  'b7':['2週間','1年ぐらい','45分','8時間'],
 },
 12: {
  'b1':['でした。']*4,
  'b2':['忙しかった','楽しかった','暖かかった','人が 多かった'],
  'b3':['とても にぎやかでした。','簡単じゃ ありませんでした。','おもしろかったです。','あまり よくなかったです。'],
  'b4':['曇りでした。','辛かったです。','あまり 寒くなかったです。','とても すてきでした。'],
  'b6':['かたかなの ほうが','小さい みかんの ほうが','父の ほうが','どちらも'],
 },
 13: {
  'b2':['車が','靴が','時計が','うちが'],
  'b4':['2月に','生け花を','両親に','食べたくないです。','旅行の 本を'],
  'b6':['買い物に','食事に','釣りに','旅行に'],
  'b7':['ホテルの プールへ 泳ぎに','デパートへ 買いに','奈良の 美術館へ 見に','インド料理の レストランへ 食事に'],
  'b8':['靴を 買いに','カリナさんに 会いに','2時ごろ 迎えに','来月 旅行に'],
 },
 14: {
  'b2':['つけて','閉めて','撮って','話して'],
  'b4':['かきましょうか。','持ちましょうか。','つけましょうか。','行きましょうか。'],
  'b5':['コピーして','送って','呼んで','来て'],
 },
 15: {
  'b1':['帰って','消して','借って','開けて'],
  'b4':['いません。','住んで','持って','知りません。'],
  'b5':['作って','売って','使って','造って'],
  'b6':['経済を','アップル銀行で','美術を','さくら大学で'],
 },
 16: {
  'b1':['休んで、','乗って、','行って、','買って、'],
  'b3':['下ろしてから、','終わってから、','来てから、','入れてから、'],
  'b4':['終わってから、','送ってから、','見せてから、','終わってから、'],
  'b5':['人が','冬が','食べ物が','雪祭りが'],
  'b6':['狭くて、','青くて、','にぎやかで、','45歳で、'],
  'b7':['よくて、','元気で、','広くて、','静かで、'],
  'b8':['あの 若くて、','あの ダンスが 上手で、','あの 黒くて、','あの 赤くて、'],
 },
 17: {
  'b2': ['押さないで','なくさないで','書かないで','心配しないで'],
  'b3': ['行かなければ','見せなければ','起きなければ','返さなければ'],
  'b4': ['返さなければ','書かなければ','飲まなければ','覚えなければ'],
  'b5': ['急がなくても','作らなくても','来なくても','行かなくても'],
  'b6': ['行かなければ','起きなくても','話さなければ','つけなくても'],
  'b7': ['行かなければ なりません。','書かなくても','払わなければ','来なくても'],
  'b8': ['答えは 鉛筆で','たばこは 外で','お金は 受付で','保険証は 来月'],
 },
 18: {
  'b1': ['運転が','料理が','サッカーが','ダンスが'],
  'b3': ['泳ぐ','作る','書く','歌う'],
  'b4': ['寮の 部屋で 料理が','インターネットで ホテルの 予約が','借りる','行く'],
  'b5': ['乗る','見る','借りる','使う'],
  'b8': ['会社へ 行く','日本へ 来る','会議の','クリスマスの','5年','3日'],
 },
 19: {
  'b2': ['習った','上った','泊まった','食べた'],
  'b4': ['ゴルフの 練習を したり、','食べたり','スキーに 行ったり、','資料を 作ったり、'],
  'b5': ['暗く','強く','眠く','きれいに','上手に','部長に'],
 },
 20: {
  'b1': ['また 来る。','買わない。','疲れた。','書かなかった。'],
  'b2': ['おもしろい。','よくない。','痛かった。','楽しくなかった。'],
  'b3': ['上手だ。','休みじゃない。','雨だった。','暇じゃなかった。'],
  'b4': ['見たい。','ならない。','した。','いい。','いる。','できない。','出さなくても','ない。'],
  'b5':['要る？','読んだ？','行かなかった。','今月の 終わりごろに'],
  'b6':['多い。','よくない。','おもしろくなかった。','楽しかった。'],
  'b7':['何時？','休み？','猫の ほうが','きれいだった。'],
  'b8':['降って いる？','知らない。','ない。','できる。','来なくても','食べに 行った？','京都に','返さなければ ならない？'],
 },
 21: {
  'b1':['9時に 来る','運転しない','人が 多い','あした 休みだ'],
  'b2':['もう 帰った','売って いない','勝つ','あの 箱の 中だ'],
  'b3':['ほんとうに よく 働く','デザインが いい','時間の 使い方が 上手だ','いい 病院だ'],
  'b4':['おもしろくない','いい 先生だ','役に 立つ','いちばん きれいだ'],
  'b5':['どう 思いますか。','休みが 多い','とても きれいだ','交通が 便利だ'],
  'b7':['海が きれい','おもしろい','イーさんを 知らない','あった'],
  'b8':['すごいです。','大変じゃ ありません。','寒くなかったです。','かわきました。'],
 },
 22: {
  'b1': ['母に もらった','京都で 撮った','作った','かいた'],
  'b2':['コピーして いる','新聞を 読んで いる','女の 人と 話して いる','コーヒーを 飲んで いる'],
  'b3': ['はいて いる','して いる','かけて いる','かぶって いる'],
  'b4': ['初めて 主人に 会った','先週 見学した','働いて いる','毎朝 お弁当を 買う'],
  'b5': ['いつも 買い物する','よく 寝る','きのう 見た','行った'],
  'b6': ['奈良で 撮った','要らない','病院で もらった','座って いる'],
  'b7': ['ユーモアが ある','料理を 作る','話す','パーティーで 着る'],
  'b8': ['市役所へ 行く','部長と 食事する','テレビを 見る','本を 読む'],
 },
 23: {
  'b1': ['病院へ 行く','出かける','漢字が わからない','時間が ない'],
  'b3': ['頭が 痛い','暇な','妻が 病気の','晩ご飯の'],
  'b4': ['かぜを ひいた','道が わからない','眠い','あしたの 天気を 知りたい'],
  'b5': ['これを 引く','触る','これを 左へ 回す','これを 右へ 回す'],
 },
 24: {
  'b1':['くれました。']*4,
  'b7':['あげました。']*4,
 },
 25: {
  'b1': ['歩いたら、','飲んだら、','来なかったら、','なかったら、'],
  'b2': ['近かったら、','暑かったら、','簡単だったら、','航空便だったら、'],
  'b3': ['よかったら、','あったら、','眠く なったら、','足りなかったら、'],
  'b4': ['着いたら、','終わったら、','出たら、','なったら、'],
  'b5': ['覚えても、','押しても、','結婚しても、','調べても、'],
  'b6': ['眠くても、','行きたくても、','下手でも、','病気でも、'],
  'b7': ['あっても、','暇でも、','取ったら、','悪かったら、'],
 },
 26: {
  'b2':['撮ったんですか。','かいたんですか。','やって いるんですか。','勉強したんですか。'],
  'b4':['引っ越しするんですか。','ケーキを 食べないんですか。','会議に 間に 合わなかったんですか。','早く 帰るんですか。'],
  'b5':['遠いんです。','来なかったんです。','なんです。','あるんです。'],
  'b6':['かいて','手伝って','教えて','ちょっと 見て'],
  'b7':['買ったら','調べたら','持って 行ったら','したら'],
 },
 27: {
  'b1':['読めます。','修理できます。','一人で 着物が','行けます。'],
  'b2':['買えません。','走れません。','来られません。','寝られません。'],
  'b3':['もらえますか。','借りられますか。','乗れますか。','登れますか。'],
  'b5':['駐車場が','公園の 隣に','早く できます。','水曜日に'],
  'b6':['作れませんから、','飲みませんでしたから、','休めませんから、','降りませんでしたから、','寝ませんでしたから、','ありませんから、'],
  'b7':['ビールは 飲みますが、','料理は しますが、','アニメは 好きですが、','英語は 話せますが、','てんぷらや すき焼きは 食べられますが、','日曜日は 休めますが、'],
 },
 28: {
  'b2':['聞きながら','運転しながら','飲みながら','弾きながら','ボランティアを しながら','絵を 教えながら'],
  'b3':['見て います。','子どもと 遊んだり、','自転車で','本を 読んで います。'],
  'b4':['北海道は 涼しいし、','あの 美容院は 上手だし、','新しい 台所は きれいだし、','この 車は 形も いいし、'],
  'b5':['品物も 多いし、','用事も ないし、','デザインも すてきだし、サイズも ちょうど いいし、','ペットも 飼えるし、'],
  'b6':['緑も 多いし、','子どもも 好きだし、','ボーナスも ないし、','値段も 安いし、デザインも いいし、'],
 },
 29: {
  'b2':['テーブルが','時計が','洗濯機が','スーパーが'],
  'b4':['しまったんですか。']*4,
  'b5':['書いて','作って','やって','して'],
  'b6':['行って','遅れて','なくして','まちがえて'],
 },
 30: {
  'b2':['あります。']*4,
  'b3':['友達が 来る','料理を 始める','試験の','旅行の'],
  'b4':['7時までに','月曜日までに','次の 会議までに','引っ越しの 日までに'],
  'b5':['ええ、使ったら、']*4,
  'b6':['閉めて','つけて','置いて','そのままに して'],
 },
 31: {
  'b1':['しよう。','座ろう。','寝よう。','行こう。'],
  'b2':['行こうと','休もうと','登ろうと','書こうと'],
  'b3':['まだ 読んで','まだ 行って','まだ 開けて','まだ 食べて'],
  'b4':['書こうと 思って います。','返そうと 思って います。','見に 行こうと 思って います。','決めようと 思って います。'],
  'b6':['いいえ、行かない','いいえ、受けない','いいえ、取らない','いいえ、会わない'],
  'b7':['着く','食べる','行く','乗る'],
  'b8':['の']*4,
 },
 32: {
  'b1':['寝た','予約した','読まない','歩かない'],
  'b2':['冷やした','休んだ','出かけない','しない'],
  'b4':['あした 晴れる','彼女は 道が わかる','高橋さんは きょう うちに いる','彼は 試合に 出る'],
  'b5':['暑い','置けない','うるさい','ある'],
  'b6':['…ええ、山は 寒い','…ええ、雨が 降る','…ええ、込む','…ええ、バスの 中で 気分が 悪く なる'],
 },
 33: {
  'b1':['れ。','け。','れ。','ろ。'],
  'b7':['来週の 火曜日だ','出席できない','行く','着いた'],
  'b8':['行けないと','待って いると','悪いと','予約したと'],
 },
 34: {
  'b1': ['さっき 書いた','わたしが やった','先生が 言った','今 聞いた','料理番組で 見た','歯医者に 教えて もらった'],
  'b3': ['説明が 終わった','新しいのを 買った','コンサートの','ジョギングの'],
  'b4': ['土曜日 仕事が 終わった','いいえ、おふろに 入った','講義の','いいえ、昼ごはんの'],
 },
 35: {
  'b1': ['聞けば、','急げば、','秋に なれば、','橋が できれば、','わかれば、','機会が あれば、'],
  'b3': ['かけなければ、','閉めなければ、','飲まなければ、','できなければ、','足りなければ、','いすが なければ、'],
  'b4': ['正しければ、','よければ、','だめなら、','なら、'],
  'b5': ['なれば、','申し込めば、','よければ、','なら、'],
  'b6': ['すれば いいですか。','行けば いいですか。','行けば いいですか。','あげれば いいですか。'],
  'b7': ['炊飯器なら、','花見なら、','パソコン教室なら、','日本料理の 本なら、'],
 },
 36: {
  'b1':['おいしい 料理が 作れる','試合に 出られる','よく 見える','かぜが 治る'],
  'b2':['道を 間違えない','年を 取ってから 困らない','家族が 心配しない','食べ物が 腐らない'],
  'b3':['はい、ほとんど 書ける','はい、少し わかる','はい、300ぐらい 読める','はい、このごろ やっと かけられる'],
  'b4':['早く わかる','早く 乗れる','早く 泳げる','早く 弾ける'],
  'b6':['寝る','運動する','食べない','しない'],
  'b7':['連絡する','戻す','なくさない','洗濯しない'],
 },
 37: {
  'b2':['紹介されました。','頼まれました。','質問されました。','言われました。'],
  'b3':['取られました。','汚されました。','踏まれました。','持って 行かれました。'],
  'b6':['開かれますか。','書かれましたか。','輸出されますか。','つくられましたか。'],
  'b7':['使われて います。','つくられて います。','翻訳されて います。','輸入されて います。'],
 },
 38: {
  'b1':['育てるのは','知るのは','変えるのは','運転するのは'],
  'b2':['散歩するのは','知るのは','通うのは','続けるのは'],
  'b3':['散歩するのが','負けるのが','ほめるのが','つくのが','走るのが','食べるのが'],
  'b4':['嫌いなんです。','上手なんです。','速いんです。','遅いんです。'],
  'b5':['きょう 持って 来るのを','送るのを','彼女に 連絡するのを','時間を 言うのを'],
  'b6':['やめるのを','入院して いるのを','つくられたのを','登れないのを'],
  'b7':['のは 何ですか。','のは どこですか。','のは 何ですか。','のは どこですか。'],
  'b8':['いいえ、日本へ 来たのは','いいえ、勉強して いるのは','いいえ、なりたいのは','いいえ、心配なのは'],
 },
 39: {
  'b1': ['見て、','取られて、','合格して、','死んで、'],
  'b2': ['会えなくて、','できなくて、','なくて、','来なくて、'],
  'b3': ['歯が 痛くて、','質問が 難しくて、','自転車が 邪魔で、','試験の ことが 心配で、'],
  'b5': ['来るので、','込んで いないので、','最近 太ったので、','守らなかったので、'],
  'b6': ['高いので、','汚いので、','簡単なので、','日曜日だったので、'],
  'b7': ['ビザを 取りに 行かなければ ならないので、','漢字を 調べたいので、','この 荷物は 邪魔なので、','日本語が あまり 上手じゃ ないので、'],
  'b8': [
   ['いいえ、台風で','木が 倒れたので、'],
   ['いいえ、インフルエンザで','1週間 勉強しなかったので、'],
   ['いいえ、きのうの 雨と 雷で','会場が 使えないので、'],
   ['いいえ、事故で','けがを したので、'],
  ],
 },
 40: {
  'b1':['置いたか、','何キロ あるか、','いちばん いいか、','どちらが 表か、'],
  'b2':['残って いるか、','何が いいか、','作れるか、','到着するか、'],
  'b3':['うまく いくか どうか、','ないか どうか、','いいか どうか、','必要か どうか、'],
  'b4':['あるか どうか、','足りるか どうか、','20キロ以下か どうか、','ないか どうか、'],
  'b6':['…サイズが 合うか どうか、','…もう うちを 出たか どうか、','…おいしいか どうか、','…元気か どうか、'],
  'b7':['入って','乗って','着て','して'],
 },
 41: {
  'b1':['もらったんです。','いただいたんです。','いただいたんです。','もらったんです。'],
  'b2':['くれたんです。','くださったんです。','くださったんです。','くれたんです。'],
  'b4':['いただきました。','いただきました。','いただきます。','いただきます。'],
  'b5':['くださいました。']*4,
  'b6':['やりました。','やりました。','わたしは 犬を','やりました。'],
  'b7':['くださいました。','いただきました。','くださいました。','いただきました。','やります。','やります。'],
  'b8':['よく 聞こえないんですが、','セーターの サイズを まちがえたんですが、','日本料理に 興味が あるんですが、','ちょっと 寒いんですが、'],
 },
 42: {
  'b1': ['持つ ために、','出る ために、','なる ために、','住む ために、'],
  'b2': ['仕事の ために、','アニメの 研究の ために、','日本語の 勉強の ために、','子どもの 教育の ために、'],
  'b3': ['子どもたちの ために、','国の ために、','結婚する 二人の ために、','外国人の ために、'],
  'b4': ['育てる ために、','作る ために、','…世界の 平和の ために、','…オリンピックの ために、日本の 音楽家が'],
  'b5': ['入れるのに','測るのに','包むのに','計算するのに'],
  'b6': ['育てるのに','勉強するのに','…ええ。お土産に','…はい。旅行に'],
  'b7': ['修理するのに','生活するのに','育てるのに','書くのに'],
 },
 43: {
  'b2': ['降りそうですよ。','消えそうですよ。','やみそうですよ。','変わりそうですよ。'],
  'b3': ['続きそうです。','咲きそうです。','上がりそうです。','増えそうです。'],
  'b4': ['なりそうですから、','なくなりそうですから、','なりそうですから、','来そうですから、'],
  'b5': ['寂し','うれし','暇','便利'],
  'b6': ['暖かそうですね。','重そうですね。','元気','幸せそうですね。'],
  'b7': ['見て きますから、','聞いて きますから、','買って きますから、','止めて きますから、'],
  'b8': ['ちょっと 見て きます。','散歩して','ちょっと コピーして','行って きます。'],
 },
 44: {
  'b3':['飲みすぎて、','疲れすぎて、','重すぎて、','濃すぎて、'],
  'b4':['飲みすぎたんです。','見すぎたんです。','高すぎるんです。','複雑すぎるんです。'],
  'b5':['使いやすいです。','住みやすいです。','わかりにくいです。','飲みにくいです。'],
  'b6':['滑りやすいです。','腐りやすいです。','割れにくいです。','乾きにくいです。'],
  'b8':['11時の 便に','「ホテルひろしま」に','シングルに','和食に'],
 },
 45: {
  'b1':['交通事故に あった','友達を 連れて 来る','何か 問題が あった','受付に だれも いない'],
  'b2':['風が 強い','薬が 必要な','エアコンの 調子が 悪い','食堂が 休みの'],
  'b3':['時間に 間に 合わない','20キロ以上の','予約を キャンセルしたい','領収書が ない'],
  'b4':['2時間 並んだのに、','楽しみに して いたのに、','彼は 日本へ 来た ことが ないのに、','毎日 8時間 寝て いるのに、'],
  'b5':['仕事は 忙しいのに、','お正月なのに、','保険証が 必要だったのに、','この アパートは 汚くて、狭いのに、'],
  'b6':['ボタンを 押したのに、','気を つけて いたのに、','もう 遅いのに、','約束は 10時なのに、'],
  'b7':['町の 真ん中に あるのに。','有名なのに。','そんなに 安くないのに。','一度も 遅れた ことが ないのに。'],
 },
 46: {
  'b1':['始まる','頼む','探す ところです。','電話する'],
  'b2':['調べて いる','片づけて いる','書いて いる','相談して いる'],
  'b3':['出た','寝た','終わった','着いた'],
  'b4':['来た ところなんです。','乗った ところなんです。','始まる ところなんです。','食事して いる'],
  'b5':['始めた ばかりです。','買った','会った','行った'],
  'b6':['ばかりなので、','ばかりなので、','できた','洗濯した'],
  'b7':['聞いた ばかりなのに、','磨いた ばかりなのに、','買った ばかりなのに、','結婚した ばかりなのに、'],
  'b8':['来る はずです。','おいしい','上手な','留守の'],
 },
 47: {
  'b1':['なるそうです。','発見されたそうです。','とても 寒いそうです。','弁護士だそうです。'],
  'b3':['興味が あるそうですよ。','別れたそうですよ。','おいしいそうですよ。','好きだそうですよ。'],
  'b6':['いるようですから、','寒いようですから、','好きなようですから、','忘れ物のようですから、'],
 },
 48: {
  'b3':['帰らせて います。','行かせて います。','娘に 朝ごはんの 準備を','息子に 犬の 世話を'],
  'b5':['止めさせて','帰らせて','使わせて','撮らせて','聞かせて','やらせて'],
 },
 49: {
  'b1':['読まれました。','出かけられました。','出張されます。','来られます。'],
  'b2':['行かれましたか。','帰られますか。','取られますか。','引っ越しされますか。'],
  'b3':['おやめに なります。','お乗りに なりません。','お書きに なりました。','お作りに なりました。'],
  'b4':['おわかりに なりますか。','お疲れに','お泊まりに なりましたか。','お買いに なりましたか。'],
  'b5':['なさいますか。','いらっしゃいますか。','いらっしゃいましたか。','おっしゃいましたか。','召し上がりますか。','ご覧に なりますか。'],
  'b6':['いらっしゃいましたか。','いらっしゃいますか。','召し上がりますか。','いらっしゃいますか。','ご覧に なりましたか。','ご存じですか。'],
  'b7':['お取りください。','お過ごしください。','ご連絡ください。','ご利用ください。'],
 },
 50: {
  'b2':['ご紹介します。','ご用意します。','ご説明します。','ご連絡します。'],
  'b4':['お目に かかりました。','いただきました。','拝見しました。','伺いました。'],
  'b5':['伺います。','存じません。','伺いました。','お目に かかりました。'],
  'b6':['参りました。','おります。','勉強して おります。','留学いたします。'],
  'b7':['参りました。','住んで おります。','勉強いたしました。','教えて おります。'],
 },
}

RULE = {
 1:'Phủ định vị ngữ danh từ ở hiện tại là Nじゃ ありません; không thêm です sau ありません.',
 2:'Hỏi lần lượt hai phương án trong gợi ý bằng Nですか、Nですか; phần đầu cần có か.',
 3:'Hỏi vị trí dùng どこ／どちら và trả lời bằng đúng địa điểm được cho trong ngoặc.',
 4:'Khoảng thời gian bắt đầu với から và kết thúc bằng まで; động từ hiện tại hoặc quá khứ theo từ chỉ thời gian.',
 5:'Người đi cùng dùng と; đi một mình dùng 一人で. Ngày cụ thể dùng に, còn 来月 không cần に.',
 6:'Trợ từ で đánh dấu nơi diễn ra hành động; câu trả lời giữ đúng thì và khẳng định/phủ định của gợi ý.',
 7:'Người nhận dùng に, địa điểm xảy ra hành động dùng で; もう hỏi việc đã xong và まだです báo chưa xong.',
 8:'Phủ định tính từ な dùng じゃ ありません, tính từ い dùng ～くないです; trước danh từ, tính từ な cần な.',
 9:'Câu giải thích nguyên nhân dùng mệnh đề thể lịch sự + から; giữ nội dung và thời của gợi ý.',
 10:'Hỏi sự tồn tại của vật hoặc người chưa xác định dùng 何が hoặc だれが; は không thay が trong câu hỏi này.',
 11:'Tần suất dùng khoảng thời gian + に + số lần; thời lượng dùng đơn vị thời gian trực tiếp, không thêm に.',
 12:'Danh từ và tính từ な ở quá khứ dùng でした; tính từ い đổi ～い thành ～かった, riêng いい thành よかった.',
 13:'Mong muốn dùng Vます bỏ ます + たい; mục đích di chuyển dùng thân ます hoặc danh từ hoạt động + に.',
 14:'Lời yêu cầu dùng thể て + ください; lời đề nghị giúp dùng thân ます + ましょうか.',
 15:'Xin phép dùng thể て + もいいですか; trạng thái hoặc hoạt động tiếp diễn dùng thể て + います.',
 16:'Nối hành động dùng thể て; trước から dùng thể て, tính từ い nối bằng ～くて, tính từ な/danh từ nối bằng で.',
 17: 'Vないでください diễn đạt lời yêu cầu không làm; Vなければなりません là phải làm, còn Vなくてもいいです là không cần làm.',
 18: 'Nができます dùng cho khả năng với danh từ; trước ことができます hoặc まえに, động từ cần thể từ điển.',
 19: 'Kinh nghiệm dùng thể た + ことがある; liệt kê hoạt động dùng thể た + り; thay đổi trạng thái dùng ～く／～に なります.',
 20: 'Lối thân mật đổi vị ngữ lịch sự sang thể thường nhưng giữ nguyên thời và ý phủ định của gợi ý.',
 21:'Trước と 思います dùng thể thường; danh từ và tính từ な hiện tại khẳng định cần だ. Trước でしょう không giữ だ.',
 22: 'Mệnh đề bổ nghĩa cho danh từ dùng thể thông thường ngay trước danh từ; không giữ ます／ました trong mệnh đề.',
 23: 'Trước とき dùng thể thường của động từ hoặc tính từ; Vると biểu thị kết quả thường xảy ra sau thao tác.',
 24:'Khi người khác làm điều tốt cho mình dùng ～てくれました; khi mình giúp người khác dùng ～てあげました.',
 25: 'Điều kiện たら dùng thể た + ら; nhượng bộ ても dùng thể て + も và giữ kết quả trái kỳ vọng.',
 26:'～んです đi sau thể thường để nêu hoàn cảnh; lời nhờ lịch sự dùng thể て + いただけませんか, lời hỏi cách làm dùng たらいいですか.',
 27:'Thể khả năng nhóm I đổi âm cuối sang hàng え; しか đi với phủ định để nói “chỉ có”.',
 28:'Hai hành động đồng thời nối bằng thân ます + ながら; nhiều lý do nối bằng thể thường + し.',
 29:'Trạng thái kết quả dùng Vています; làm xong hoặc lỡ làm dùng Vてしまう, trước んです phải chia thể thường.',
 30:'Trạng thái vật đã được ai đó sắp đặt dùng Vてあります; chuẩn bị trước dùng Vておく, hạn hoàn thành dùng までに.',
 31:'Ý định dùng thể ý chí + と思っています hoặc thể từ điển + 予定です; kế hoạch bằng danh từ dùng Nの予定です.',
 32:'Lời khuyên dùng Vた／Vない ほうがいい; phỏng đoán dùng thể thường + でしょう／かもしれません.',
 33:'Mệnh lệnh nhóm I đổi âm cuối sang hàng え; trước と 言う／伝える dùng thể thường, người nhận lời nhắn dùng に.',
 34: 'とおりに và あとで lấy thể た của động từ; nếu đứng sau danh từ thì dùng Nの.',
 35: 'Điều kiện động từ dùng ～ば, phủ định dùng ～なければ; tính từ い dùng ～ければ, danh từ hoặc tính từ な dùng ～なら.',
 36:'Để nói mục tiêu hoặc điều muốn tránh dùng thể từ điển/thể ない + ように; thay đổi khả năng dùng ように なりました.',
 37:'Câu bị động chuyển người/vật chịu tác động lên chủ đề; người gây hành động đi với に, đồ vật của mình vẫn đi với を.',
 38:'Danh từ hóa động từ bằng thể từ điển + の; dùng のは cho chủ đề, のが với cảm nhận/năng lực, のを với 忘れる hoặc 知る.',
 39: 'Nối nguyên nhân bằng thể て／なくて hoặc ので đúng loại từ; Nで nêu nguyên nhân sự kiện.',
 40:'Câu hỏi gián tiếp dùng thể thường + か; câu hỏi có/không dùng かどうか, danh từ và tính từ な bỏ だ.',
 41:'Người nhận いただく làm chủ ngữ khiêm nhường; người tặng くださる làm chủ ngữ kính ngữ; やる dùng cho người dưới hoặc động vật.',
 42: 'Vる ために nêu mục đích của hành động, Nの ために nêu mục đích với danh từ; công dụng dùng Vるのに hoặc Nに.',
 43: 'Dấu hiệu sắp xảy ra và vẻ ngoài dùng thân ます hoặc thân tính từ + そう; đi làm rồi quay lại dùng Vて きます.',
 44:'Quá mức dùng thân ます/tính từ bỏ い + すぎる; dễ/khó làm dùng thân ます + やすい／にくい.',
 45:'場合は đứng sau thể thường hoặc Nの／Aな; のに nối kết quả trái kỳ vọng với dạng chia đúng của vế trước.',
 46:'ところ phân biệt sắp làm Vる, đang làm Vている, vừa xong Vた; ばかり diễn đạt việc mới xảy ra.',
 47:'そうだ thuật lại thông tin dùng thể thường; ようだ suy đoán dựa trên dấu hiệu, danh từ đi với の.',
 48:'Sai khiến động từ nhóm I chuyển âm cuối sang hàng あ + せる; sau động từ có tân ngữ を, người làm dùng に.',
 49:'Kính ngữ nâng người được nói đến: ～れる／られる, お＋thân ます＋になる hoặc động từ kính ngữ đặc biệt.',
 50:'Khiêm nhường ngữ hạ hành động của bản thân: ごNします hoặc các động từ đặc biệt như 伺う, 参る, おる.',
}

WEAR = {
 'はいて いる':'靴 đi với はく → はいて いる trước 人.',
 'して いる':'ネクタイ đi với する → して いる trước 人.',
 'かけて いる':'眼鏡 đi với かける → かけて いる trước 人.',
 'かぶって いる':'帽子 đi với かぶる → かぶって いる trước 人.',
}

FILL_PROMPT = {
 (22,'b4-4'): '＜木村さんが 毎朝 お弁当を 買います＞ 木村さんが ＿＿ コンビニは 駅の 前に あります。',
 (22,'b5-1'): '＜わたしが いつも 買い物します＞ わたしが ＿＿ スーパーは 野菜が 安いです。',
 (40,'b7-1'): '＜温泉に 入った ことが ない＞ 温泉に 入った ことが ないので、温泉に ＿＿ みたいです。',
 (40,'b7-2'): '＜馬に 乗った ことが ない＞ 馬に 乗った ことが ないので、馬に ＿＿ みたいです。',
 (40,'b7-3'): '＜着物を 着た ことが ない＞ 着物を 着た ことが ないので、着物を ＿＿ みたいです。',
 (40,'b7-4'): '＜生け花を した ことが ない＞ 生け花を した ことが ないので、生け花を ＿＿ みたいです。',
}
FILL_EXPLANATION = {
 (22,'b4-4'):'Gợi ý gốc là 木村さんが 毎朝 お弁当を 買います. Trước コンビニ, động từ 買います đổi sang thể thường 買う; cả mệnh đề là 毎朝 お弁当を 買う.',
 (22,'b5-1'):'Gợi ý gốc là わたしが いつも 買い物します. Trước スーパー, 買い物します đổi sang thể thường 買い物する; vì thế điền いつも 買い物する.',
 (40,'b7-1'):'Chưa từng vào suối nước nóng nên muốn thử: 入ります đổi sang thể て là 入って, tạo 入ってみたいです.',
 (40,'b7-2'):'Chưa từng cưỡi ngựa nên muốn thử: 乗ります đổi sang thể て là 乗って, tạo 乗ってみたいです.',
 (40,'b7-3'):'Chưa từng mặc kimono nên muốn thử: 着ます đổi sang thể て là 着て, tạo 着てみたいです.',
 (40,'b7-4'):'Chưa từng cắm hoa nên muốn thử: します đổi sang thể て là して, tạo してみたいです.',
}
PROMPT_OVERRIDES = {
 (9,'b6-1'):'日曜日は 試験 ＿＿ あります。',
 (9,'b6-2'):'火曜日は 用事 ＿＿ あります。',
 (9,'b6-3'):'水曜日は アルバイト ＿＿ あります。',
 (9,'b6-4'):'金曜日は 時間 ＿＿ あります。',
 (44,'b8-1'):'飛行機は 何時の 便に しますか。（11時の 便） ⇒',
 (44,'b8-2'):'ホテルは どこに しますか。（「ホテルひろしま」） ⇒',
}
INSTRUCTION_OVERRIDES = {
 9:'Gợi ý chữ đã cho: chọn trợ từ đúng trong câu Nがあります.',
 44:'Theo địa điểm hoặc lựa chọn ghi trong ngoặc, chọn cụm đúng trước します.',
}

TEXT_SUFFICIENT_WITH_PICTURE = {(19,'b5'),(23,'b5'),(25,'b3'),(42,'b5'),(43,'b5'),(45,'b1'),(46,'b4')}
EXTERNAL_CONTEXT_WITHOUT_INLINE_PICTURE = {(3,'b1'),(14,'b7')}
WRONG_OVERRIDES = {
 (10,'b3-1'):'何は',
 (10,'b3-3'):'何は',
 (19,'b5-5'):'上手な',
 (25,'b3-4'):'足りたら、',
 (27,'b3-1'):'もらいますか。',
 (27,'b3-2'):'借れますか。',
 (27,'b3-3'):'乗りますか。',
 (27,'b3-4'):'登りますか。',
 (31,'b8-1'):'に',
 (31,'b8-2'):'に',
 (31,'b8-3'):'に',
 (31,'b8-4'):'に',
 (37,'b6-1'):'開きます。',
 (37,'b6-2'):'書きました。',
 (37,'b6-3'):'輸出します。',
 (37,'b6-4'):'つくりました。',
 (8,'b2-1'):'くないです。',
 (8,'b4-1'):'くないです。',
 (8,'b4-2'):'安くないです。',
 (8,'b4-4'):'便利なです。',
 (8,'b7-1'):'どう',
 (8,'b7-2'):'どう',
 (8,'b7-3'):'どう',
 (8,'b7-4'):'どう',
 (9,'b1-3'):'好きじゃ ありません。',
 (9,'b4-1'):'わかりません。',
 (9,'b4-3'):'わかりません。',
 (9,'b5-4'):'ありません。',
 (9,'b6-1'):'を',
 (9,'b6-2'):'を',
 (9,'b6-3'):'を',
 (9,'b6-4'):'を',
 (10,'b5-1'):'います。',
 (10,'b5-2'):'あります。',
 (10,'b5-3'):'います。',
 (10,'b5-4'):'います。',
 (8,'b6-2'):'の',
 (8,'b8-1'):'な',
 (8,'b8-3'):'の',
 (13,'b4-2'):'習いたくないです。',
 (13,'b4-5'):'読みたくないです。',
 (16,'b7-2'):'親切の',
 (16,'b7-4'):'いいでした。',
 (16,'b8-2'):'すてきの',
 (20,'b5-2'):'読む？',
 (20,'b6-1'):'多いだ。',
 (20,'b7-3'):'猫を',
 (40,'b7-4'):'する',
 (49,'b5-1'):'なさりますか。',
 (49,'b5-2'):'いらっしゃりますか。',
 (49,'b5-3'):'いらっしゃりましたか。',
 (49,'b5-4'):'おっしゃりましたか。',
 (49,'b5-5'):'ご覧に なりますか。',
 (49,'b5-6'):'お見に なりますか。',
}
SKIP_ITEMS = {(13,'b8-3'):'ごろ và ぐらいに đều diễn đạt giờ gần đúng',
              (5,'b6-1'):'người đi cùng phụ thuộc tranh; không thể suy chỉ từ câu hỏi',
              (5,'b6-2'):'đích đến phụ thuộc tranh; hai nơi đều hợp lệ',
              (5,'b6-3'):'phương tiện phụ thuộc tranh; tàu và máy bay đều hợp lệ',
              (5,'b7-2'):'giờ về phụ thuộc lịch ngoài cue',
              (5,'b7-3'):'người đi cùng phụ thuộc lịch ngoài cue',
              (5,'b7-4'):'có đi đâu vào thứ bảy hay không phụ thuộc lịch',
              (44,'b8-3'):'phòng đơn và phòng đôi đều hợp lệ nếu thiếu hình lựa chọn',
              (44,'b8-4'):'món Nhật và món Tây đều hợp lệ nếu thiếu hình lựa chọn',
              (8,'b5-1'):'そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập',
              (8,'b5-2'):'そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập',
              (8,'b5-3'):'そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập',
              (8,'b5-4'):'そして và が đều tạo được câu; mức tương phản là lựa chọn biên tập',
              (20,'b7-1'):'何時？ và 何時だ？ đều là lối hỏi thân mật',
              (20,'b7-2'):'休み？ và 休みだ？ đều là lối hỏi thân mật',
              (20,'b8-1'):'phương án còn lại là mảnh câu đáp cùng nguồn',
              (20,'b8-6'):'phương án còn lại là mảnh câu đáp cùng nguồn',
              (20,'b8-8'):'phương án còn lại là mảnh câu đáp cùng nguồn',
              (15,'b4-4'):'知りません và 知っていません đều có thể diễn đạt không biết',
              (40,'b6-1'):'phương án còn lại là thành phần khác của cùng một đáp án',
              (40,'b6-2'):'phương án còn lại là thành phần khác của cùng một đáp án',
              (40,'b6-3'):'phương án còn lại là thành phần khác của cùng một đáp án',
              (49,'b5-6'):'お見になる và ご覧になる đều là kính ngữ đúng',
              (49,'b6-5'):'お見になる và ご覧になる đều là kính ngữ đúng',
              (50,'b2-2'):'お用意します và ご用意します đều được dùng'}
EXTERNAL_SKIP_ITEMS = {(5,'b6-1'),(5,'b6-2'),(5,'b6-3'),
                       (5,'b7-2'),(5,'b7-3'),(5,'b7-4'),
                       (44,'b8-3'),(44,'b8-4')}

# Each row is a new, self-contained AI exercise. The original source cue remains
# documented as ambiguous; these answers are not presented as source keys.
REWRITES = {
 (8,'b5-1'):{'prompt_ja':'会社の 寮（新しい・きれい） ⇒','instruction_vi':'Chọn câu giữ nguyên hai nhận xét tích cực và nối chúng thành hai câu lịch sự.',
  'answer':'会社の 寮は 新しいです。そして、きれいです。',
  'distractors':['会社の 寮は 新しいだです。そして、きれいです。','会社の 寮は 新しいです。そして、きれいくです。','会社の 寮は 新しいです。そして、きれいなです。'],
  'explanation_vi':'新しい là tính từ い nên nói 新しいです; きれい là tính từ な nên vị ngữ là きれいです. そして nối thêm nhận xét thứ hai. Các phương án còn lại chia sai tính từ.'},
 (8,'b5-2'):{'prompt_ja':'先生（親切・おもしろい） ⇒','instruction_vi':'Chọn câu giữ nguyên hai nhận xét tích cực và nối chúng thành hai câu lịch sự.',
  'answer':'先生は 親切です。そして、おもしろいです。',
  'distractors':['先生は 親切なです。そして、おもしろいです。','先生は 親切です。そして、おもしろいだです。','先生は 親切です。そして、おもしろいなです。'],
  'explanation_vi':'親切 là tính từ な nhưng trước です không thêm な; おもしろい là tính từ い. そして bổ sung nhận xét cùng chiều. Ba câu nhiễu dùng đuôi tính từ sai.'},
 (8,'b5-3'):{'prompt_ja':'日本の 食べ物（おいしい・高い） ⇒','instruction_vi':'Chọn câu lịch sự giữ đúng cả hai ý: ngon nhưng đắt.',
  'answer':'日本の 食べ物は おいしいですが、高いです。',
  'distractors':['日本の 食べ物は おいしいだが、高いです。','日本の 食べ物は おいしくが、高いです。','日本の 食べ物は おいしいですが、安いです。'],
  'explanation_vi':'おいしいですが nối hai nhận xét đối lập; 高い giữ đúng ý “đắt”. おいしいだが và おいしくが sai dạng, còn 安い đổi nghĩa thành “rẻ”.'},
 (8,'b5-4'):{'prompt_ja':'日本の 生活（忙しい・おもしろい） ⇒','instruction_vi':'Chọn câu lịch sự giữ đúng cả hai ý: bận nhưng thú vị.',
  'answer':'日本の 生活は 忙しいですが、おもしろいです。',
  'distractors':['日本の 生活は 忙しいだが、おもしろいです。','日本の 生活は 忙しくが、おもしろいです。','日本の 生活は 忙しいですが、つまらないです。'],
  'explanation_vi':'忙しいですが diễn đạt sự tương phản với おもしろい. Hai dạng 忙しいだが／忙しくが sai, còn つまらない trái với gợi ý “thú vị”.'},
 (13,'b8-3'):{'prompt_ja':'何時に 子どもを 迎えに 行きますか。（2時ごろ） ⇒','instruction_vi':'Trả lời bằng mốc giờ gần đúng trong ngoặc và đúng trợ từ của 迎えに行きます.',
  'answer':'2時ごろ 子どもを 迎えに 行きます。',
  'distractors':['2時ごろ 子どもが 迎えに 行きます。','2時ごろ 子どもに 迎えに 行きます。','2時ごろ 子どもで 迎えに 行きます。'],
  'explanation_vi':'子ども là người được đón nên đi với を; mục đích của 行きます là 迎えに. 2時ごろ cho biết giờ gần đúng. Các câu nhiễu đổi を thành trợ từ không hợp vai trò của 子ども.'},
 (15,'b4-4'):{'prompt_ja':'木村さんの 住所を 知って いますか。（いいえ） ⇒','instruction_vi':'Chọn câu đáp phủ định tự nhiên theo mẫu khi hỏi có biết địa chỉ hay không.',
  'answer':'いいえ、知りません。',
  'distractors':['いいえ、知りないです。','いいえ、知って います。','いいえ、知られません。'],
  'explanation_vi':'Trả lời “tôi không biết” dùng 知りません. 知りないです chia sai, 知って います là “biết”, còn 知られません là dạng phủ định của 知られる, không phải câu đáp này.'},
 (20,'b7-1'):{'prompt_ja':'今 何時ですか。 ⇒','instruction_vi':'Chọn câu hỏi thân mật cùng nghĩa, ở hiện tại.',
  'answer':'今、何時？','distractors':['今、何歳？','今、何時ですか？','今、何時だった？'],
  'explanation_vi':'今、何時？ hỏi giờ hiện tại theo lối thân mật. 何歳 hỏi tuổi, 何時ですか là lối lịch sự, 何時だった hỏi quá khứ.'},
 (20,'b7-2'):{'prompt_ja':'今日 デパートは 休みですか。 ⇒','instruction_vi':'Chọn câu hỏi thân mật cùng nghĩa, ở hiện tại.',
  'answer':'今日 デパートは 休み？','distractors':['今日 デパートは 休んだ？','今日 デパートは 休みですか？','今日 デパートは 休みだった？'],
  'explanation_vi':'休み？ hỏi cửa hàng hôm nay có nghỉ hay không theo lối thân mật. 休んだ là động từ quá khứ, khác với danh từ 休み; ですか là lối lịch sự, だった hỏi trạng thái trong quá khứ.'},
 (20,'b8-1'):{'prompt_ja':'今、雨が 降って います。相手に 現在の 様子を 確認します。 ⇒','instruction_vi':'Chọn câu hỏi thân mật hỏi xem mưa có đang rơi lúc này không.',
  'answer':'今、雨が 降って いる？','distractors':['今、雨が 降った？','今、雨が 降る？','今、雨が 降って いた？'],
  'explanation_vi':'降っている diễn đạt hành động đang diễn ra; thêm giọng hỏi thành 降っている？. 降った là đã rơi, 降る là hiện tại chung/tương lai, 降っていた là đang rơi trong quá khứ.'},
 (20,'b8-6'):{'prompt_ja':'きのう タイ料理を 食べに 行きました。 ⇒','instruction_vi':'Chọn câu hỏi thân mật “đã đi ăn món gì?” dựa trên câu đã cho.',
  'answer':'何を 食べに 行った？','distractors':['何を 食べに 行く？','何を 食べて 行った？','どこへ 食べに 行った？'],
  'explanation_vi':'食べに行った là “đã đi để ăn”; 何を hỏi món ăn. 行く đổi sang chưa quá khứ, 食べて行った là ăn rồi đi, どこへ hỏi nơi đến.'},
 (20,'b8-8'):{'prompt_ja':'来週の 木曜日までに 本を 返さなければ なりません。 ⇒','instruction_vi':'Chọn câu hỏi thân mật “phải trả sách chậm nhất khi nào?”',
  'answer':'いつまでに 本を 返さなければ ならない？',
  'distractors':['いつまでに 本を 返さなくても いい？','いつまで 本を 返した？','いつから 本を 返さなければ ならない？'],
  'explanation_vi':'いつまでに hỏi hạn chót; なければならない giữ nghĩa “phải trả”. なくてもいい là không cần, 返した hỏi đã trả, いつから hỏi mốc bắt đầu.'},
 (40,'b6-1'):{'prompt_ja':'この 服は サイズが 合いますか。（着て 確かめます） ⇒','instruction_vi':'Trả lời bằng câu gián tiếp かどうか và hành động thử Vてみます.',
  'answer':'サイズが 合うか どうか、着て みます。',
  'distractors':['サイズが 合いますか どうか、着て みます。','サイズが 合うか どうか、着る みます。','サイズが 合うか どうか、着て います。'],
  'explanation_vi':'Trước かどうか dùng thể thường 合う; hành động thử mặc dùng 着てみます. Ba câu nhiễu giữ ますか trước どうか, dùng thể từ điển trước みます, hoặc đổi thử làm sang đang mặc.'},
 (40,'b6-2'):{'prompt_ja':'ミラーさんは もう うちを 出ましたか。（電話を かけて 確かめます） ⇒','instruction_vi':'Trả lời bằng câu gián tiếp かどうか và hành động thử Vてみます.',
  'answer':'もう うちを 出たか どうか、電話を かけて みます。',
  'distractors':['もう うちを 出ましたか どうか、電話を かけて みます。','もう うちを 出たか どうか、電話を かける みます。','もう うちを 出るか どうか、電話を かけて みます。'],
  'explanation_vi':'Hỏi người ấy “đã rời nhà chưa” nên dùng thể quá khứ thường 出たかどうか. Thử gọi điện là 電話をかけてみます; 出ましたか và かけるみます sai cấu trúc.'},
 (40,'b6-3'):{'prompt_ja':'新しい レストランは おいしいですか。（行って 確かめます） ⇒','instruction_vi':'Trả lời bằng câu gián tiếp かどうか và hành động thử Vてみます.',
  'answer':'おいしいか どうか、行って みます。',
  'distractors':['おいしいだか どうか、行って みます。','おいしいか どうか、行く みます。','おいしくか どうか、行って みます。'],
  'explanation_vi':'Tính từ い おいしい đứng trực tiếp trước かどうか; thử đi xem dùng 行ってみます. Không thêm だ, không biến thành おいしくか, và みます cần thể て.'},
 (49,'b5-6'):{'prompt_ja':'中村課長は 歌舞伎を 見ますか。 ⇒','instruction_vi':'Chọn câu hỏi kính ngữ ở hiện tại về trưởng phòng Nakamura.',
  'answer':'中村課長は 歌舞伎を ご覧に なりますか。',
  'distractors':['中村課長は 歌舞伎を ご覧しますか。','中村課長は 歌舞伎を 拝見しますか。','中村課長は 歌舞伎を ご覧に なりましたか。'],
  'explanation_vi':'ご覧になる là kính ngữ của 見る dành cho hành động của trưởng phòng, hiện tại hỏi bằng なりますか. 拝見する là khiêm nhường cho mình; なりましたか đổi sang quá khứ.'},
 (49,'b6-5'):{'prompt_ja':'「七人の侍」は もう 見ましたか。 ⇒','instruction_vi':'Chọn câu hỏi kính ngữ ở quá khứ về việc người nghe đã xem phim hay chưa.',
  'answer':'「七人の侍」は もう ご覧に なりましたか。',
  'distractors':['「七人の侍」は もう 拝見しましたか。','「七人の侍」は もう ご覧に なりますか。','「七人の侍」は もう ご覧に なりませんか。'],
  'explanation_vi':'ご覧になりましたか kính trọng người nghe và giữ quá khứ của 見ましたか. 拝見 là khiêm nhường về mình; なりますか hỏi chưa quá khứ; なりませんか là lời mời.'},
 (50,'b2-2'):{'prompt_ja':'お弁当は こちらで 用意します。（わたしの 行動） ⇒','instruction_vi':'Chọn câu tự nói khiêm nhường về việc mình sẽ chuẩn bị cơm hộp tại đây.',
  'answer':'お弁当は こちらで ご用意します。',
  'distractors':['お弁当は こちらで ご用意なさいます。','お弁当は こちらで ご用意されます。','お弁当は こちらで ご用意して ください。'],
  'explanation_vi':'ご用意します nói khiêm nhường về hành động của mình. なさいます／されます nâng người khác; してください là nhờ người nghe, trái với “mình chuẩn bị”.'},
}
assert set(REWRITES)=={k for k in SKIP_ITEMS if k not in EXTERNAL_SKIP_ITEMS}
EXPLANATION_OVERRIDES = {
 (10,'b3-1'):'Gợi ý 何 yêu cầu câu hỏi “ベッドの 下に 何が ありますか”. 何が hỏi vật chưa xác định; 何は không dùng để hỏi chủ ngữ tồn tại ở đây.',
 (10,'b3-3'):'Gợi ý 何 yêu cầu câu hỏi “窓の 右に 何が ありますか”. Vật chưa xác định được hỏi bằng 何が; 何は sai chức năng trợ từ.',
 (41,'b6-3'):'Với 連れて 行く, con chó là đối tượng được dẫn đi nên dùng 犬を. 犬に không đánh dấu đối tượng trực tiếp của hành động này.',
 (17,'b7-3'):'Câu hỏi có （はい） nên người nói xác nhận phải trả tiền ngay: 払わなければ なりません. 払わなくても là không cần trả, trái với はい.',
 (23,'b5-3'):'Gợi ý nói xoay sang trái, nên dùng これを 左へ 回す trước と; 右へ là hướng ngược lại.',
 (23,'b5-4'):'Gợi ý nói xoay sang phải, nên dùng これを 右へ 回す trước と; 左へ là hướng ngược lại.',
 (25,'b7-1'):'Câu hỏi dùng あったら; câu trả lời phủ định “dù có cơ hội cũng không muốn sống ở nước ngoài” phải chuyển sang あっても.',
}

def specific_explanation(lesson, group, cue, good, wrong):
    if (lesson,group)==(4,'b2'):
        return f'Bài này hỏi giờ hiện tại ở thành phố, nên dùng 何時 trong “{good}”; 何曜日 hỏi thứ trong tuần. Bản đồ chỉ dùng để xác định câu trả lời về giờ.'
    if (lesson,group)==(4,'b3'):
        return f'Cần hỏi sự kiện/ngày đã nêu rơi vào thứ mấy: “{good}” dùng 何曜日. 何時 hỏi giờ, không đúng mục tiêu gợi ý.'
    if (lesson,group)==(5,'b6'):
        return 'Câu hỏi hỏi いつ国へ帰りますか; mốc tháng 12 năm sau dùng 来年の12月に. Trợ từ で không đánh dấu thời điểm đi về.'
    if (lesson,group)==(5,'b7'):
        return 'Câu hỏi 毎朝何で会社へ行きますか hỏi phương tiện. バスと電車 là phương tiện nên theo sau bằng で; に không dùng ở đây.'
    if (lesson,group)==(9,'b6'):
        return f'Gợi ý “{cue}” được viết lại thành câu Nがあります. Danh từ chỉ việc hoặc thời gian đang có đi với が; を không đánh dấu chủ ngữ của あります.'
    if (lesson,group)==(10,'b5'):
        living = '象' in cue
        return ('象 là động vật, nên hỏi sự tồn tại bằng います; あります dùng cho vật vô tri.' if living else
                'Danh từ được hỏi là địa điểm hoặc vật vô tri, nên dùng あります; います dùng cho người hoặc động vật.')
    if (lesson,group)==(44,'b8'):
        return f'Khi chọn “{good}” trong mẫu Nにします, phương án được chọn dùng に. “{wrong}” dùng を nên không hợp cấu trúc chọn lựa này.'
    return None


def choose_wrong(correct, chips):
    others = [x for x in chips if x != correct]
    others.sort(key=lambda x: SequenceMatcher(None, correct, x).ratio(), reverse=True)
    return others[0]


def make_rewrite(lesson, group, sid, refs, point_order):
    spec=REWRITES[(lesson,sid)]
    texts=[spec['answer'],*spec['distractors']]
    assert len(texts)==4 and len(set(texts))==4,(lesson,sid)
    shift=(lesson+int(sid.split('-')[-1]))%4
    texts=texts[shift:]+texts[:shift]
    return {
        'id':f'rb2-rewrite-{lesson:02}-{sid}',
        'kind':'manualQnA','source_id':sid,'source_group_id':group,
        'prompt_ja':spec['prompt_ja'],'instruction_vi':spec['instruction_vi'],
        'choices':[{'id':f'c{i+1}','text':value} for i,value in enumerate(texts)],
        'correct':f'c{texts.index(spec["answer"])+1}',
        'explanation_vi':spec['explanation_vi'],
        'grammar_refs':refs,'grammar_mapping_status':'checked_group_map',
        'placement_after_point_id':max(refs,key=lambda x:point_order[x]),
        'original_source_issue':SKIP_ITEMS[(lesson,sid)],
        'provenance':{'source_prompt':'ai_rewritten_from_official_cue',
                      'source_option_bank':'not_used_as_answer_key',
                      'answer':'ai_rewritten','explanation':'ai_authored',
                      'human_review':'pending'},
    }


def main():
    snapshots = reviewed_snapshots(ROOT)
    maps = {}
    for path in (ROOT/'authored'/'renshuu').glob('group-map-*.json'):
        maps.update(json.loads(path.read_text(encoding='utf-8')))
    out = ROOT/'authored'/'renshuu-drills'
    out.mkdir(parents=True, exist_ok=True)
    stats = {'lessons':50,'lessons_with_round2_items':0,'source_drills_total':0,
             'eligible_confirmed_deterministic':0,'eligible_markup_text_review_candidates':0,
             'completed_existing_adaptations':0,'completed_round2_adaptations':0,
             'rewritten_ambiguous_items':0,'original_ambiguous_source_cues':[],
             'pending_by_reason':{},'authored_items':0,'manualQnA':0,'manualFillInBlank':0,'manualMultiSelect':0,
             'source_drill_answer_text_official':0,'skipped_picture_drills':0,
             'skipped_already_authored':0,'skipped_other_unreviewed':0,'per_lesson':[]}
    for lesson in range(1,51):
        group_specs = ANSWERS.get(lesson,{})
        snap_path = snapshots[lesson]
        snap = json.loads(snap_path.read_text(encoding='utf-8'))
        existing_path = ROOT/'authored'/'renshuu'/f'lesson-{lesson:02}.json'
        existing = json.loads(existing_path.read_text(encoding='utf-8'))
        already = {x['source_id'] for x in existing['items'] if x['source_id'] in snap['drill_ids']}
        stats['source_drills_total']+=len(snap['drill_ids'])
        stats['completed_existing_adaptations']+=len(already)
        point_order = {x['id']:i for i,x in enumerate(snap['points'])}
        items=[];skip=[];original_ambiguous=[]
        for section in snap['sections']:
            match = re.fullmatch(r'mg-(b\d+)',section['id'])
            if not match:continue
            group = match.group(1)
            root = parse(section['html'])
            drills = root.all('mg-drill')
            stats['eligible_markup_text_review_candidates']+=sum(
                not drill.all('mg-pic') or (lesson,group) in TEXT_SUFFICIENT_WITH_PICTURE
                for drill in drills)
            if group not in group_specs:
                for drill in drills:
                    sid=drill.attrs['data-mg-drill']
                    if sid in already:continue
                    if (lesson,sid) in REWRITES:
                        items.append(make_rewrite(lesson,group,sid,maps[str(lesson)][group],point_order))
                        original_ambiguous.append({'source_id':sid,'reason':SKIP_ITEMS[(lesson,sid)]})
                        stats['manualQnA']+=1
                        continue
                    if (lesson,sid) in SKIP_ITEMS:
                        reason='picture_or_external_context_unreviewed' if (lesson,sid) in EXTERNAL_SKIP_ITEMS else 'ambiguous_options'
                        skip.append({'source_id':sid,'reason':reason,'detail':SKIP_ITEMS[(lesson,sid)]})
                        stats['skipped_picture_drills' if reason=='picture_or_external_context_unreviewed' else 'skipped_other_unreviewed']+=1
                        continue
                    reason = ('picture_or_external_context_unreviewed' if drill.all('mg-pic') or
                              (lesson,group) in EXTERNAL_CONTEXT_WITHOUT_INLINE_PICTURE else
                              'text_not_yet_editorially_solved')
                    skip.append({'source_id':sid,'reason':reason})
                    stats['skipped_picture_drills' if reason=='picture_or_external_context_unreviewed' else 'skipped_other_unreviewed']+=1
                continue
            expected=group_specs[group]
            assert len(drills)==len(expected),(lesson,group,len(drills),len(expected))
            source_instruction = root.all('mg-part-ins')[0].text()
            instruction = text_only_instruction(source_instruction)
            refs = maps[str(lesson)][group]
            for drill,good in zip(drills,expected):
                sid=drill.attrs['data-mg-drill']
                if sid in already:
                    stats['skipped_already_authored']+=1
                    continue
                if (lesson,sid) in REWRITES:
                    items.append(make_rewrite(lesson,group,sid,refs,point_order))
                    original_ambiguous.append({'source_id':sid,'reason':SKIP_ITEMS[(lesson,sid)]})
                    stats['manualQnA']+=1
                    continue
                if (lesson,sid) in SKIP_ITEMS:
                    reason='picture_or_external_context_unreviewed' if (lesson,sid) in EXTERNAL_SKIP_ITEMS else 'ambiguous_options'
                    skip.append({'source_id':sid,'reason':reason,'detail':SKIP_ITEMS[(lesson,sid)]})
                    stats['skipped_picture_drills' if reason=='picture_or_external_context_unreviewed' else 'skipped_other_unreviewed']+=1
                    continue
                if drill.all('mg-pic') and (lesson,group) not in TEXT_SUFFICIENT_WITH_PICTURE:
                    skip.append({'source_id':sid,'reason':'picture_or_external_context_unreviewed'})
                    stats['skipped_picture_drills']+=1
                    continue
                cue=drill.all('mg-drill-q')[0].text().removeprefix(sid.split('-')[-1]+') ').strip()
                chips=[x.text() for x in drill.all('mg-chip')]
                goals=good if isinstance(good,list) else [good]
                assert all(x in chips for x in goals),(lesson,sid,goals,chips)
                if len(goals)==1:
                    if (lesson,sid) in FILL_PROMPT:
                        choices=[];correct=good;kind='manualFillInBlank'
                        explanation=FILL_EXPLANATION[(lesson,sid)]
                    else:
                        wrong=WRONG_OVERRIDES.get((lesson,sid),choose_wrong(good,chips))
                        assert wrong in chips and wrong!=good,(lesson,sid,good,wrong,chips)
                        choices=[good,wrong]
                        if (lesson+int(sid.split('-')[-1]))%2:choices.reverse()
                        correct=f'c{choices.index(good)+1}'
                        kind='manualQnA'
                        explanation=(WEAR.get(good) or f'Gợi ý “{cue}” cần biến đổi thành “{good}”. {RULE[lesson]}')
                        explanation+=f' “{wrong}” không diễn đạt đúng dạng hoặc nội dung cần luyện trong câu này.'
                        explanation=specific_explanation(lesson,group,cue,good,wrong) or explanation
                        explanation=EXPLANATION_OVERRIDES.get((lesson,sid),explanation)
                else:
                    choices=chips
                    correct=[f'c{choices.index(x)+1}' for x in goals]
                    kind='manualMultiSelect'
                    explanation=(f'Gợi ý “{cue}” cần cả “{goals[0]}” để nêu nguyên nhân ban đầu '
                                 f'và “{goals[1]}” để nối sự việc đó với kết quả. Chọn đủ hai mảnh; '
                                 'に không đánh dấu nguyên nhân sự kiện, còn なので không nối trực tiếp sau động từ thể thường.')
                item={
                    'id':f'rb2-{lesson:02}-{sid}', 'kind':kind,'source_id':sid,
                    'source_group_id':group,'prompt_ja':FILL_PROMPT.get((lesson,sid),PROMPT_OVERRIDES.get((lesson,sid),cue)),
                    'instruction_vi':(f'{INSTRUCTION_OVERRIDES.get(lesson,instruction) if (lesson,sid) in PROMPT_OVERRIDES else instruction} ' + ('Điền dạng đúng vào chỗ trống.' if kind=='manualFillInBlank' else
                                      f'Chọn {"cả hai mảnh nối nguyên nhân" if len(goals)>1 else "dạng đúng của phần cần biến đổi"} từ các lựa chọn.')),
                    'correct':correct,'explanation_vi':explanation,'grammar_refs':refs,
                    'grammar_mapping_status':'checked_group_map',
                    'placement_after_point_id':max(refs,key=lambda x:point_order[x]),
                    'provenance':{'source_prompt':'ai_adapted_from_official_prompt' if (lesson,sid) in PROMPT_OVERRIDES or (lesson,sid) in FILL_PROMPT else 'official_snapshot','source_option_bank':'official_snapshot',
                                  'answer':'ai_editorial_inference','explanation':'ai_authored','human_review':'pending'},
                }
                if choices:item['choices']=[{'id':f'c{i+1}','text':x} for i,x in enumerate(choices)]
                items.append(item)
                stats[kind]+=1
        out_doc={'lesson':lesson,'source_snapshot':snap_path.relative_to(ROOT).as_posix(),
                 'source_url':snap['url'],'items':items,'pending':skip,
                 'original_ambiguous_source_cues':original_ambiguous,
                 'review_status':'ai_editorial_draft','render_instruction_vi_with_prompt_ja':True}
        assert len(items)+len(skip)+len(already)==len(snap['drill_ids']),(lesson,len(items),len(skip),len(already),len(snap['drill_ids']))
        (out/f'lesson-{lesson:02}.json').write_text(json.dumps(out_doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        stats['authored_items']+=len(items)
        stats['rewritten_ambiguous_items']+=len(original_ambiguous)
        stats['original_ambiguous_source_cues'] += [dict(lesson=lesson,**row) for row in original_ambiguous]
        stats['lessons_with_round2_items']+=bool(items)
        stats['per_lesson'].append({'lesson':lesson,'source_drills':len(snap['drill_ids']),
                                    'completed_existing':len(already),'completed_round2':len(items),
                                    'rewritten_ambiguous':len(original_ambiguous),'pending':len(skip)})
        for row in skip:
            reason=row['reason']
            stats['pending_by_reason'][reason]=stats['pending_by_reason'].get(reason,0)+1
    stats['completed_round2_adaptations']=stats['authored_items']
    stats['eligible_confirmed_deterministic']=stats['completed_existing_adaptations']+stats['authored_items']
    stats['eligible_ai_keyed']=stats['eligible_confirmed_deterministic']
    assert stats['source_drills_total']==stats['eligible_confirmed_deterministic']+sum(stats['pending_by_reason'].values())
    assert stats['rewritten_ambiguous_items']==len(REWRITES)==17
    (ROOT/'reports'/'renshuu-drill-round2.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    original_lines=''.join(
        f'- Bài {x["lesson"]:02}, {x["source_id"]}: {x["reason"]}.\n'
        for x in stats['original_ambiguous_source_cues'])
    report = f'''# Renshuu B: biến thể trực tiếp từ drill nguồn, 50 bài

## Phạm vi

- Drill nguồn: **{stats['source_drills_total']}** trên 50 bài.
- Đã có trong bộ B chính: **{stats['completed_existing_adaptations']}** biến thể trực tiếp (2/bài).
- Vòng bổ sung này: **{stats['completed_round2_adaptations']}** biến thể ở **{stats['lessons_with_round2_items']}** bài; gồm {stats['manualQnA']} chọn một, {stats['manualFillInBlank']} điền chỗ trống, {stats['manualMultiSelect']} chọn nhiều.
- Trong đó có **{stats['rewritten_ambiguous_items']}** bài AI viết lại từ cue nguồn mơ hồ; mỗi bài có ngữ cảnh chữ, ba nhiễu và giải thích riêng. Đáp án của bài viết lại không phải khóa nguồn.
- **{stats['eligible_confirmed_deterministic']}** drill đã có biến thể với đáp án AI biên tập xác định. Đây là số *eligible ở mức bản nháp AI*, không tính ví dụ nhận diện trong bộ B chính.
- **{stats['eligible_markup_text_review_candidates']}** drill không mang ảnh trong markup hoặc thuộc nhóm có dữ kiện chữ đã kiểm. Đây là bộ lọc ứng viên theo markup, không phải tập bao trùm các câu đã biên tập: một số câu nguồn có ảnh đã được viết lại thành ngữ cảnh chữ.

## Còn chờ theo lý do

- **{stats['pending_by_reason'].get('picture_or_external_context_unreviewed',0)}** drill có ảnh/ngữ cảnh bên ngoài cue chưa được biên tập chắc.
- **{stats['pending_by_reason'].get('text_not_yet_editorially_solved',0)}** drill chữ chưa được giải và kiểm riêng.
- **{stats['pending_by_reason'].get('ambiguous_options',0)}** cue mơ hồ còn thiếu biến thể. Danh sách gốc 17 cue đã viết lại nằm ở mục dưới và trường `original_ambiguous_source_cues` trong JSON bài.

Tổng pending: **{sum(stats['pending_by_reason'].values())}**. Tất cả **{stats['source_drills_total']}** đáp án nguồn vẫn chưa được site trả trong snapshot. Trường `correct` của biến thể là đáp án suy luận/biên tập AI, `human_review` vẫn là `pending`; không gắn nhãn đáp án chính thức. Không dùng vị trí chip hoặc `data-p` làm đáp án.

## Cue nguồn mơ hồ đã viết lại

{original_lines}

## Tái tạo

Chạy `py -X utf8 scripts/renshuu_drill_round2.py` từ thư mục `minna-n5-n4`. Script tạo đủ 50 file `authored/renshuu-drills/lesson-NN.json` và báo cáo `reports/renshuu-drill-round2.json`. Bộ B chính `authored/renshuu/lesson-NN.json` được đọc để tránh trùng `source_id`; script này không sửa bộ chính.

## Giới hạn QA

Cặp đáp án được so với prompt, chỉ dẫn nhóm và bank lựa chọn đã lưu; mục mơ hồ bị giữ pending. Bản này là nháp biên tập AI cho root kiểm độc lập trước xuất native. `eligible_markup_text_review_candidates` không phải số câu có khóa chắc.
'''
    (ROOT/'reports'/'renshuu-drill-round2.md').write_text(report,encoding='utf-8')
    print(stats)


if __name__=='__main__':main()
