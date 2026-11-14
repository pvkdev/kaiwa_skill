import json
import subprocess
from pathlib import Path

WORK = Path(__file__).parent

def s(kind, book, unit, situations, fit, difficulty):
    return dict(kind=kind, book_id=book, unit_id=unit, situations=situations,
                fit=fit, difficulty=difficulty)

def c(book, locator, reason, status='deferred'):
    return dict(book_id=book, locator=locator, reason=reason, status=status)

SPEAK = 'speak_japanese'
PACK = 'shadowing_pack'
DATA = [
 dict(code='S-004', topics=['Tên và đặc điểm đồ vật, số lượng, đơn vị đếm', 'Ngày, giờ và thời hạn', 'Giá tiền, cách trả và kiểm lại số'],
      notes=['Đọc đủ 15 tình huống V5 S-004; quét heading và nội dung catalog27 cho số, giờ, いくら, món hàng, xác nhận. Đọc trọn B08 Part 4 Unit 07 và Unit 08, B07 mục 84. Chọn Unit 07 vì tám câu cùng giao dịch hỏi giá và chỉ món; các bài khác thiên điều kiện yêu cầu hoặc cách trả.',
             'B08 Unit 07 có CD-2 / 10; các nội dung ngày/giờ, tiền thừa chưa thấy pack toàn đơn vị đúng cảnh ở nguồn được phép, dành cho biên soạn mới. Phạm vi quét thêm B01/B05/B06/B07/B11/B12/B14/B18/B19/B20/B24 qua chỉ mục, không nhận đã đọc trọn từng mục.'],
      selections=[s(PACK,'B08','u-part4-unit07',['S001','S002','S011','S012'],'Luyện hỏi giá, xác định món theo màu/cỡ và hỏi lựa chọn gần giống trong một lượt mua ngắn.','Có 試着 và cỡ giày ngoài phần số cốt lõi; giữ nguyên tám câu và giảng theo nhu cầu mua sắm cụ thể.')],
      considerations=[c('B08','B08 Part 4 Unit 08 u-part4-unit08:209–237','Đã đọc trọn tám câu; chủ yếu đặt hàng, đổi cỡ, gói quà và hình thức thanh toán, dành chặng mua sắm sau.'),
                      c('B07','B07 mục 84 u-200-084:3–16','Đã đọc trọn năm cặp; yêu cầu theo điều kiện trong bưu điện, nhà đất, làm tóc, quán ăn và công ty quá rộng cho bài số/giờ cơ bản.')]),
 dict(code='S-005', topics=['Khu vực, tiền thuê và kiểu phòng', 'Điều kiện sống, khoảng cách đến ga', 'Hẹn xem phòng và xác nhận khoản phí'],
      notes=['Đọc đủ 15 tình huống V5 S-005; tra 不動産・家賃・部屋 trong catalog27/source_index và annotations. Đọc trọn B08 Part 4 Unit 21 và B07 mục 84. Hai bài bổ sung: Unit 21 nêu phòng mong muốn, mục 84 nêu mức tiền thuê có hạn.',
             'B08 CD-2 / 24, B07 CD-1 84 in trong clean. Chưa thấy pack toàn đơn vị về bảng phí và buổi xem phòng trong nhóm audio được phép; phần đó cần nội dung do tác giả viết, không gán cho sách. B01/B14/B13 quét tiêu đề, không xác nhận đọc trọn.'],
      selections=[s(SPEAK,'B07','u-200-084',['S001','S004','S011'],'Ví dụ bất động sản nêu mức thuê tối đa; bốn ví dụ còn lại luyện cấu trúc chọn điều kiện ở dịch vụ khác, cùng mục đích nói.','Mẫu ～でお願いします ngắn, hợp Sơ; giải thích 以内 trong ví dụ nhà đất như giới hạn ngân sách.'),
                  s(PACK,'B08','u-part4-unit21',['S001','S002','S003','S004','S005','S006','S012'],'Tám câu đi theo việc nói mình tìm phòng, hỏi mong muốn, chọn sáng/rộng/yên tĩnh/gần ga và xin xem phòng.','Có ～のほうがいい và 徒歩10分以内 nhưng ngữ cảnh rõ, giảng như mẫu có thể thay từ.')],
      considerations=[c('B08','B08 Part 4 Unit 22 近所の人と話す','Đơn vị nói với hàng xóm sau chuyển nhà, thiên rác và thiết bị; để S-007.'),c('B14','B14 Unit 1–5, heading Section','Không thấy một section ghi ranh giới rõ cho thương lượng thuê nhà ở chỉ mục; chưa đọc trọn.')]),
 dict(code='S-006', topics=['Thành viên gia đình và cách gọi', 'Giờ ăn, quy tắc sinh hoạt cùng chủ nhà', 'Xin phép, báo về muộn và cảm ơn'],
      notes=['Đọc đủ 16 tình huống V5 S-006; tra ホストファミリー・家族・訪ねる trong catalog27. Đọc trọn B08 Part 4 Unit 20, Part 4 Unit 19 và Part 5 Unit 03. Unit 20 bám sát nhà chủ, Unit 03 nói gia đình, Unit 19 bổ sung lời khách/chủ ở bữa đầu và lúc ra về.',
             'Ba pack CD-2 / 23, 22, 39 in trong clean; giữ nguyên các câu khó như kỷ niệm gia đình và cảm ơn trang trọng trong mỗi unit. Quét B01/B07/B14/B18 theo chỉ mục để xét thêm, không có đơn vị đã đọc trọn khác được chọn.'],
      selections=[s(PACK,'B08','u-part4-unit20',['S001','S003','S005','S007','S009','S012','S015','S016'],'Mạch ở nhà chủ gồm chào, hỏi giờ, hỏi quy tắc, xem ảnh gia đình, báo về muộn và cảm ơn.','Tám câu cùng tình huống; câu cảm ơn cuối dài, luyện nhận biết và shadowing nguyên câu.'),
                  s(PACK,'B08','u-part5-unit03',['S002','S003','S004'],'Bổ sung tên quan hệ gia đình và cách hỏi người thân, giúp người học chọn lượng thông tin muốn kể.','Một số câu về đại học và kỷ niệm 50 năm khó hơn nền, vẫn giữ đủ bảy câu và giải nghĩa trước khi nghe.'),
                  s(PACK,'B08','u-part4-unit19',['S005','S006','S008','S016'],'Lời vào nhà, mời đồ uống, nhận lời và xin phép về hỗ trợ ngày đầu ở nhà chủ.','Có お招きいただき trang trọng, dùng như lời mẫu; không buộc tự tạo kính ngữ.')],
      considerations=[c('B07','B07 mục 157 お邪魔します','Chỉ mục cho thấy một bài lời vào nhà, nhưng B08 Unit 19 đã cung cấp cả lời khách và chủ; giữ để xét nếu chặng thăm bạn cần riêng.')]),
 dict(code='S-007', topics=['Chào khi mới chuyển đến và hỏi quy tắc khu nhà', 'Rác, đồ chung, thiết bị và chỗ để', 'Nhắc nhở, xin lỗi và chốt cách xử lý'],
      notes=['Đọc đủ 15 tình huống V5 S-007; tra 近所・引っ越し・ごみ・ルール trong catalog27. Đọc trọn B08 Part 4 Unit 22, B07 mục 183 và B08 Part 4 Unit 20. Unit 22 nói đúng quan hệ hàng xóm và cả lỗi thiết bị; mục 183 cho lời mở/xin lỗi ngắn.',
             'B08 CD-2 / 25 và B07 CD-2 83 đã kiểm trên clean. Unit 22 thiên xử lý rác, không chứa lời đối đáp tranh chấp tiếng ồn; phần đó cần tác giả viết mới. B01/B14/B13 quét chỉ mục thêm, chưa khẳng định đọc đủ.'],
      selections=[s(SPEAK,'B07','u-200-183',['S001','S004','S005','S011','S012'],'Tái dùng trọn bài すみません để mở lời với hàng xóm, xin lỗi sau gây phiền và cảm ơn khi họ giúp.','Năm cặp lời ngắn; giải thích sự khác nhau giữa xin lỗi và cảm ơn theo hành động.'),
                  s(PACK,'B08','u-part4-unit22',['S001','S002','S003','S009','S010'],'Bảy câu về tự giới thiệu phòng, hỏi quy tắc rác và báo bồn cầu tắc tạo nền cho việc nói đúng người khi mới chuyển đến.','Từ rác tái chế và đồ điện mới, học theo topic; không biến lời sách thành quy định chung mọi khu phố.')],
      considerations=[c('B08','B08 Part 4 Unit 20 u-part4-unit20:553–581','Đã đọc trọn; hỏi quy tắc nhà nhưng vai sống với gia đình chủ nhà, đã chọn ở S-006, không đại diện quan hệ hàng xóm.')]),
 dict(code='S-008', topics=['Phòng, chìa khóa và giờ ra vào ký túc xá', 'Dùng bếp, đồ chung và liên hệ người quản lý', 'Báo sự cố, xin ngoại lệ và bàn giao'],
      notes=['Đọc đủ 15 tình huống V5 S-008; tìm 寮・社宅・ルール・管理・鍵 trên catalog27/source_index, annotations B01/B05/B07/B08/B14/B18 và mục lục nhóm shadowing. Không thấy pack toàn đơn vị chuyên ký túc xá có ranh giới rõ. Đọc trọn B07 mục 16 và B08 Part 4 Unit 20 để so; mục 16 là lời hỏi chức năng chung phù hợp khi tiếp cận người quản lý, còn Unit 20 đặt trong gia đình chủ nhà.',
             'Chọn B07 mục 16 như bài mở lời hỏi điều kiện; các cảnh ký túc xá, nhà công ty và hậu quả cần tác giả viết mới. CD-1 16 đã kiểm trên clean, chưa nghe audio.'],
      selections=[s(SPEAK,'B07','u-200-016',['S001','S002','S003','S004','S012','S013'],'Luyện mở lời hỏi người phụ trách về giờ, quy tắc và ngoại lệ; bài có cảnh hỏi phí, hỏi đường và giáo viên nhưng chung một cách xin hỏi lịch sự.','お伺い là dạng lịch sự theo cụm; không xem toàn ví dụ là bối cảnh ký túc xá.')],
      considerations=[c('B08','B08 Part 4 Unit 20 u-part4-unit20:553–581','Đã đọc trọn; vai gia đình chủ nhà, gồm ảnh gia đình và cảm ơn khi được coi như người nhà; không áp nguyên pack vào nhà công ty.', 'unsuitable'),c('B08','B08 Part 4 Unit 22 u-part4-unit22:611–637','Đã đọc trọn; trọng tâm hàng xóm và rác, không bao trùm quầy quản lý/ký túc xá.','unsuitable')]),
 dict(code='S-009', topics=['Địa điểm công cộng trong khu phố', 'Thẻ thư viện, mượn và đặt sách', 'Giờ mở cửa, phòng sinh hoạt và hỏi tiếp'],
      notes=['Đọc đủ 21 tình huống V5 S-009; tra 図書館・本・予約・施設 trong catalog27 và B18 PART2. Đọc trọn B18 mục (2) 図書館で, ba cảnh làm thẻ, mượn sách và đặt trước; đây là bài gần nhất về chức năng sử dụng cơ sở công cộng.',
             'B18 音声 88 in trong clean; disc chưa rõ và chưa nghe audio. B08 Part 5 Unit 09 本 chỉ nói sở thích đọc, không phải dùng thư viện; B13/B14 quét heading chưa tìm pack trọn về thuê phòng sinh hoạt.'],
      selections=[s(SPEAK,'B18','u-keigo-situation-library-02',['S006','S007','S008','S009','S010'],'Ba cảnh đúng vai người dùng thư viện: làm thẻ, hỏi số sách và hỏi đặt trước khi sách đang được mượn.','Câu nhân viên có kính ngữ, thông tin thẻ/đặt trước dài; luyện nghe lời đáp, người học nói câu hỏi ngắn.')],
      considerations=[c('B08','B08 Part 5 Unit 09 本','Heading là chủ đề sách nhưng nội dung không được xác minh là pack về dùng thư viện; để chuyện sở thích đọc.'),c('B14','B14 Unit 1–5, heading Section','Không thấy section có tên thư viện hay cơ sở cộng đồng trong chỉ mục; chưa đọc trọn.')]),
 dict(code='S-010', topics=['Tên địa điểm, mốc đường và hướng rẽ', 'Xác nhận cổng ga, lối vòng và điểm đang đứng', 'Hỏi lại, sửa hiểu nhầm và cảm ơn'],
      notes=['Đọc đủ 15 tình huống V5 S-010; tra 道案内・道をたずねる・駅・交差点 trong catalog27. Đọc trọn B18 PART2 (11) năm cảnh, B08 Part 4 Unit 03 tám câu và B07 mục 16. B18 có lời cả người hỏi lẫn người chỉ, B08 luyện nhiều kiểu nêu đích.',
             'B18 音声 97 và B08 CD-2 / 6 đã kiểm trên clean; B18 disc chưa rõ. Chưa nghe file audio. B07 mục 16 có một ví dụ hỏi đường nhưng cả bài dạy mở lời đa bối cảnh, hai bài chọn đã đủ chức năng.'],
      selections=[s(SPEAK,'B18','u-keigo-situation-directions-11',['S001','S002','S003','S005','S006','S011','S012','S014','S015'],'Năm cảnh hỏi bảo tàng, quán cà phê, ga và bus; lời người qua đường có mốc, người học nhắc lại rồi cảm ơn.','Hỏi lịch sự ないでしょうか/ご存じないでしょうか cao hơn Sơ; giảng như mẫu cố định, đối chiếu cách hỏi đơn giản ở B08.'),
                  s(PACK,'B08','u-part4-unit03',['S001','S002','S003','S004','S006','S007','S008'],'Tám câu hỏi ga, địa chỉ, taxi, chùa và ga gần nhất; luyện diễn đạt đích và khoảng cách đi bộ.','Một vài tên riêng và 最寄り駅 mới, vẫn là câu ngắn; giữ cả unit thay vì chỉ một câu hỏi ga.')],
      considerations=[c('B07','B07 mục 16 u-200-016:30–45','Đã đọc trọn; có ví dụ hỏi đường nhưng toàn bài xoay lời mở ちょっとお伺いしたいんですが ở nhiều bối cảnh, không thêm mạch chỉ đường so với B18.'),c('B08','B08 Part 4 Unit 02 バス・タクシーを使う','Để chặng phương tiện vận tải; heading chưa đủ chứng minh toàn pack hợp chỉ đường.')])
]

for spec in DATA:
    path = WORK / (spec['code'] + '.spec.json')
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('checking', spec['code'], flush=True)
    subprocess.run(['py','-X','utf8',str(WORK/'save_one.py'),str(path)], check=True)
