# TQT-PR-20261009-gptchat-closure-master-lifecycle-04
## Từ câu hỏi tới MOW gọi được và vòng xử lý khép kín

TQT-PROPOSAL: TQT-PR-20261009-gptchat-closure-master-lifecycle-04
TARGET: view.html#tqt-composite-processes / closure_review / tqt-question-matrix; TQT-TH-001; TQT-ISS-007.
TESTED: Đọc nguồn mới, 19 câu bổ sung, quy trình tổng hợp/rules/notes, README/COLLAB/AGENTS, CT-003/004/005/005.1 và D158. Kiểm tĩnh snapshot 8bc0adb15489ef8fe5c4b03a7dea91e6a5a5b900, mở phần khép kín bản d60306d HTTP200/console0. Không chạy tạo Field hoặc đổi nguồn.
BLOCKER_TYPE: THIEU_HUONG_DAN / THIEU_KHAI_BAO / THIEU_QUYET_DINH — nhãn phân tích trong proposal, không thêm trạng thái hệ thống.
OBSERVED: Mô tả đúng nhiều chỗ nối nhưng chưa có mã MOW Master; các việc con dẫn bằng link tài liệu, chưa là hợp đồng gọi có dữ liệu. Bộ ghép theo đối tượng Field không tự mang bộ khai báo MOW/MOT đang thực hiện. Mức đã kiểm, kết quả kiểm và hiệu lực còn cần tách nghĩa.
PROPOSED_CHANGE: Giữ hệ khái niệm hiện tại; chốt quan hệ/đăng ký MOW con, biến câu đã có thành khai báo bắt buộc có nguồn/giá trị; chứng minh một ca thiếu Field đi hết có nhận việc, trả kết quả và kiểm nơi phát hiện. Chưa thêm T2.5, Master thứ hai hoặc tăng câu theo chỉ tiêu.

## 0. Vai trò và bằng chứng

Ghế: GPT Chat · Vai: Reviewer theo yêu cầu Owner. Host: Astra Codex, phiên được Owner chỉ định.
Bước/vòng: rà khép kín tiếp theo · 0/5; không tự mở/chốt hội đồng của Host, không phát READY/RUN.
Based_on: 8bc0adb15489ef8fe5c4b03a7dea91e6a5a5b900. Trước khi ghi đã kiểm 88b1b59948314f50d94f4880839a3cc132a171f2: diff toàn work/tools-quy-trinh rỗng, source view giữ nguyên hash.
Scope ghi: CHỈ file đề xuất này. Không sửa bốn file chính, sổ chuẩn, Công thức, Master, runtime, UI, PG/Directus. Không tạo task mới.

**Kết luận:** hướng Codex đúng. Câu hỏi là căn cứ khai báo; công việc trả lời/kiểm câu hỏi phải được nhóm thành MOW/MOT theo mục đích và đầu ra, không thành một loại đối tượng mới. Chưa gọi được quy trình chỉ vì có tên/mã tài liệu/link/đủ câu hỏi. Bước tiếp nên hoàn thiện một mẫu khai báo và một ca có bằng chứng, không phải tăng câu chung theo cảm giác.

Đã xác minh:
- 159 câu/53 nhóm, đúng 19 câu mới so với d517a1e; ID duy nhất, cha/owner hợp lệ; 30 tham chiếu câu trong closure_review.question_sets đều tồn tại.
- Một mô tả quy trình TQT-TH-001, 3 giai đoạn/9 việc con. Mỗi việc có id/title/work/uses/output/next. Cả 9 next là văn bản; 21 uses chỉ có label/href.
- closure_review.registration.master_record_id=null. README và UI ghi đúng CHƯA ĐĂNG KÝ MOW. Chưa có bằng chứng thực thi vòng thiếu Field.
- Python tái hiện compose: CTCM+B1.3+FIELD+UI=36 câu, Config=34, Test=36; không có Q-MOW-* hoặc Q-MOT-* trong cả ba. Chọn Tầng=MOW có 9 câu MOW nhưng không có FIELD/MOT; chọn MOT có 9 câu MOT nhưng không có FIELD/MOW. Đúng đối với bộ chọn một đối tượng; chưa là phiếu khai báo toàn quy trình.
- tracking.levels ghi các mức từ Chưa khai báo tới Đã kiểm chạy thật; health trộn Còn hiệu lực/Cần kiểm lại với Không đạt/Bị chặn/Không áp dụng.

Kiểm read-only: job 1c6c010d941f43adb949f9817738e971 exit0; job 4c05d9bd3b7d4b2f8ffa87d6980455dd exit0. Đây là kiểm tài liệu/thuật toán kế thừa bằng Python, không browser E2E hay runtime. UI-inspect #tqt-closure-review trên bản Owner gửi d60306d: HTTP200, console0, có bốn điểm hở và trạng thái chưa chạy; không mở hết mọi details.
Nguồn/hash: view.html SHA256 142267aab8207b05a7e174ed7e554422a4d949db4cd5db4721b56aacbe7293c4; README 7a5bfb55c3c501a13b2e76c5d50ea9f056619b7365f998e7acecc6013350a738; COLLAB d748e48ce4863afc4e3e5053e52cccc12c3c301a2c5f5386fbcc92428b5d9c58. Nguồn CT-003/004/005/005.1: ui/definition-master-data-v1.js SHA256 93eae888106544e7905751a15cc72b360971f3d8bda437887bfbf3f5c07b044c; FORMULA-AI-README D158 SHA256 053066f72c283274dac3e0e0afcf601d295eb16e211aff25e4d7e7a3e9bfd357.

## 1. GIỮ những gì đã có

MOW tổng hợp vẫn MOW; chưa cần loại/tầng mới chỉ vì sơ đồ thu/xổ sâu hơn. Chuyên môn Bước/Tầng/Chuỗi và nghiệp vụ UI/Test/Config/NTGV giữ nguyên. Một câu không phải một Task. Q-LAYER-06/07/08, Q-MOW-04…09, Q-MOT-04…09, Q-TEST-05/06, Q-UI-06, Q-NTGV-05 đã có: không viết một bộ tương tự ở nơi khác.

Đường phát hiện→xác minh→dùng lại/sửa/tạo→đấu lại→kiểm nơi phát hiện đúng hướng. B1 chỉ tìm/kiểm trong phạm vi, không tự làm Dùng/Tạo/Sửa. closure_review.connection đã hỏi nguồn–đích, nhánh, dữ liệu, điều kiện/trigger, người nhận, hạn và bằng chứng; thiếu tiếp theo là khai giá trị và kiểm sử dụng, không phải chưa hề có câu hỏi.

Phân biệt định nghĩa/lần áp dụng, giữ lịch sử, không lấy số câu làm % nghiệm thu, không gọi demo là chạy thật — GIỮ. TQT-ISS-007 theo dõi cơ chế; vấn đề sản phẩm ở sổ nguồn tương ứng. Proposal này không mở sổ thứ hai.

## 2. Định danh và gọi con — chưa thể chỉ thêm mã cho tài liệu

### 2.1. Rà cả quy trình con, không chỉ TQT-TH-001
TQT-TH-001-PG và TQT-TH-001-OPS cũng là khung hướng dẫn chưa có bằng chứng đăng ký/gọi. Link tới Tool001/004/007 mở tài liệu không tự thành một lệnh gọi MOW/MOT.

Áp Q-LAYER-06 cho mọi phần được coi có thể gọi lại:
**mã tài liệu → mã Master MOW/MOT nếu có → phiên bản → khai báo đầu vào/ra → bên được phép làm → bằng chứng một lần áp dụng.**
Nếu chỉ là tài liệu hỗ trợ MOT thì giữ là tài liệu, không bắt cấp MOW cho mọi link. Nếu là quy trình độc lập thật thì đăng ký đúng Master/công thức. Bản chưa đăng ký vẫn được soạn/phản biện; trước gọi/thực thi phải có định danh hợp lệ. Không tạo vòng chết “chưa có thủ tục đăng ký thì không được soạn thủ tục đăng ký”.

### 2.2. Quan hệ gọi khác quan hệ cấu thành
CT-002 là chiều lắp ráp; CT-005/D158 hiện sinh MOW từ một Nhóm cha. Composite xuyên nhiều Bước chưa thể gán đại vào một NHC để lấy mã. Bản mới đã nhận diện hạn chế này đúng.

Phương án ưu tiên để Host xem xét: **MOW tổng hợp có các MOT điều phối; MOT được khai báo gọi phiên bản MOW con**, ánh xạ MOIT vào và nhận MOUT/kết quả về. Trên UI có thể thu gọn thành “quy trình → quy trình con”. Đây là đề xuất quan hệ, chưa là sửa Công thức.

Phương án chứa trực tiếp MOW con cũng cần làm rõ loại quan hệ, cách đếm, trạng thái và đường trả về. Cả hai vẫn cần chốt quy tắc Nhóm cha/đăng ký tổng hợp; phương án MOT gọi MOW không tự giải quyết hết CT-005. Rà khả năng Gộp/Tách hiện hữu trước, chỉ đổi gốc khi đúng thẩm quyền Owner/Host MOW.

Tách ba ý nghĩa: **loại đối tượng quy trình**, **đối tượng mà quy trình xử lý**, **độ sâu gọi**. MOW tìm Field là quy trình T2 xử lý đối tượng T0; gọi thêm một MOW chưa tự thành T3 chuyên môn hay T2.5. T2.5/Master riêng giữ là đề xuất, chưa cần để hoàn thành ca đầu.

## 3. Chỗ hở đã đo: câu MOW/MOT chưa đi cùng phiếu đối tượng Field

36 câu CTCM+B1.3+FIELD+UI không có bộ Q-MOW/Q-MOT. Các câu ấy có tại mặt khép kín và nhóm riêng; chưa có đường bắt buộc trong một phiếu áp dụng toàn việc.

**Không sửa bằng cách đổi Field thành MOW hoặc đổ mọi câu vào mọi bộ chọn.** Tách hai phạm vi trả lời:
1. Quy trình/công việc đang thiết kế/chạy: khai MOW/MOT — tên/mã, việc con, thứ tự, MOIT/MOUT, đọc/ghi, người nhận, báo cáo, kết thúc.
2. Đối tượng chuyên môn được xử lý: Field — nghĩa/thuộc tính/nguồn/điều kiện đối chiếu B1. Nghiệp vụ UI/Config/Test ghép tiếp.

Đề nghị trong quy trình tổng hợp thêm hướng dẫn bắt buộc: **mở phiếu khai báo MOW/MOT trước, dẫn bộ câu hỏi thành phần vào cùng phiếu**. Đáp án kèm mã đối tượng mà nó mô tả; cùng Q_ID không mặc định cùng đáp án. Bộ chọn cho người vẫn gọn.

Một khuôn chung áp dụng cho khai một MOT, một MOW, một MOW tổng hợp; khác nhau ở con được gọi và cách ghép. Không cần nhân ba bộ câu hỏi hoặc tự nhận cả ba đã là MOW đăng ký. Phần kế thừa khai một lần, phần riêng/lần áp dụng điền theo nguồn đúng.

## 4. Biến các mũi tên thành khai báo kiểm/gọi được

Chín next bằng văn xuôi và 21 label/href là cách trình bày hợp lý cho bản hiểu; không phải dữ liệu đủ để DOT biết một bàn giao đã nhận. Dùng chính các trường closure_review.connection, khai một lần và render ra cả sơ đồ người lẫn bảng máy.

Mỗi nối phải có: **mã/phiên nguồn → kết quả/nhánh → dữ liệu gửi → mã/phiên đích → điều kiện/trigger → người nhận → bằng chứng nhận → kết quả trả về → lỗi/hạn đi đâu**.

Làm rõ hướng dẫn trả lời Q-MOW-08/Q-MOT-07/09:
- Mã định nghĩa khác **mã lần gọi**: kết quả con mang mã việc cha/nơi phát hiện/vấn đề, trả đúng lần đang chờ, không chỉ đúng tên quy trình.
- **Gửi chưa phải nhận.** Người gửi/điều phối giữ trách nhiệm đến khi có bên nhận hoặc nhánh từ chối hợp lệ; quá hạn phải có đầu mối, không để cả hai bên nghĩ bên kia giữ.
- Gửi lại không tạo hai đề xuất/Field; cùng tác động có khóa nhận diện lần xử lý và phép thử chống trùng. Q-MOT-09 đã có, cần đáp án/ca chứ không thêm khẩu hiệu.
- Cha bị hủy/đổi phiên thì kết quả con về muộn không được ghi nhầm lên phiên mới. Ghi nguồn kết quả và quyết định xử lý muộn.
- Nhánh song song có danh sách phải hội đủ, nhánh N-A có căn cứ và xử lý nhánh lỗi. Vòng lặp cần điều kiện thoát/giới hạn/đầu mối khi không thoát; không cấm mọi vòng lặp.

Đây là khai báo quan hệ và bản ghi của MOW/MOT/MOIT/MOUT, không thêm nguyên liệu gốc. Định nghĩa quy trình, lần chạy, đáp án và bằng chứng là những dữ liệu khác nhau; không cần ép mỗi ghi chú thành Field canonical riêng.

## 5. Đi trên thiết kế ca thiếu Field

Bảng này là phân tích thiết kế, **chưa thực thi B3–B7/PG hay tạo Field**.

| Điểm | Phần đã có | Giá trị còn phải khai để đi được | Phân biệt bắt buộc |
|---|---|---|---|
| Rà UI thấy thiếu | Nhu cầu và vị trí phát hiện | Mã hồ sơ, mã UI/MOW/MOT, phạm vi, người giữ; đã có cùng nhu cầu thì nối hồ sơ | Thấy thiếu có thể chỉ là thiếu binding/quyền; chưa là Field mới được duyệt |
| Giao xác minh | Gọi B1/NTGV | Mã MOW/MOT, đầu vào, người nhận, nhận việc ở đâu, nguồn/quyền/phiên tìm | Lỗi nguồn hoặc không có quyền xem không là chứng minh đối tượng không tồn tại |
| Chọn hướng | Dùng lại/sửa/tạo/chưa rõ | Tiêu chí không có phù hợp trong phạm vi đã kiểm, nhu cầu còn cần, quyền quyết | Không bắt mọi việc vào B3; không dựng một chức năng tìm mới trùng B1 |
| B3→B7 | Danh mục và tên Bước | Mã MOW/MOT thật, MOIT/MOUT, bên nhận/duyệt, nhánh làm rõ/từ chối/test fail | Đi qua năm nhãn không phải đã chạy năm quy trình |
| B2/đấu lại | Ý nối vào nơi cần | Mã nơi gốc, phiên Field được nhận, mapping, quyền sửa, bằng chứng bàn giao | B7 duyệt không tự nối Field vào UI; B1 không thực hiện B2 |
| Kiểm và đóng | Kiểm tại nơi phát hiện | Ca từng mắc, kết quả/đọc lại, người có quyền đóng, trạng thái từng nơi ảnh hưởng | Field xong nhưng UI còn lỗi thì mục tiêu chưa đạt; một nơi xanh không đóng mọi nơi |

### Kết thúc có loại kết quả, không buộc mọi hồ sơ đều “đã sửa thành công”
- Đã giải quyết: nhu cầu nơi phát hiện đạt, có bằng chứng.
- Trùng/đã có: liên kết hồ sơ/đối tượng gốc; việc đang bị chặn phải nối được vào kết quả dùng lại.
- Không thực hiện/không còn cần/bị từ chối: có quyết định đúng thẩm quyền, báo về nơi gọi. Mục tiêu cha còn chưa đạt hoặc có quyết định điều chỉnh; không tự tô thành đã giải quyết.
- Chưa rõ/chờ phụ thuộc: vẫn mở, có người giữ, sự kiện/mốc xét lại và đường quá hạn.

Đây là đề xuất phân loại, chưa thêm trạng thái canonical. Đối chiếu hệ trạng thái hiện hữu trước khi áp. Có thể hiển thị “thấy thiếu” ngay trên Master như **mặt xem hồ sơ liên kết**, không coi bản phát hiện là một định nghĩa Field sẵn dùng. Nếu chọn lưu ứng viên trong Master thì phải có ràng buộc không cho dùng trước duyệt và quy tắc chống trùng; không duy trì hai sổ cùng quyền sửa.

## 6. Hai cột dễ nhìn nhưng ba ý nghĩa phải rõ

Tách mức bằng chứng/hiệu lực đúng hướng. Tuy nhiên health hiện có Còn hiệu lực/Cần kiểm lại cùng Không đạt/Bị chặn/N-A; chúng không loại trừ nhau. Ca đã chạy FAIL vẫn có thể là kết quả mới nhất còn hiệu lực. Ca từng PASS có thể đã mất hiệu lực.

Giữ UI hai cột:

| Bằng chứng / kết quả | Hiệu lực |
|---|---|
| Đã kiểm thiết kế — ĐẠT | Còn hiệu lực |
| Đã chạy thật — KHÔNG ĐẠT | Còn hiệu lực |
| Đã chạy thật — ĐẠT | Cần kiểm lại do nguồn X đổi |
| Chưa chạy — BỊ CHẶN | Chờ nguồn Y / sự kiện xét lại |

Bên dữ liệu tách mức bằng chứng, kết quả kiểm, hiệu lực. N-A có phạm vi/lý do/người chấp nhận, không là mức cao hơn PASS. Giữ lịch sử kiểm; chỉ dùng lại kết quả ĐẠT còn hiệu lực và đủ mức yêu cầu. Điều này sửa tracking/Q-TEST-05/Q-LAYER-08, không đòi thêm nhiều câu/trạng thái hiển thị.

Bản đã nói source/rule/quyền/môi trường đổi thì kiểm lại — GIỮ. Cần khai dữ kiện: kết quả phụ thuộc mã/phiên nào, tiêu chí/mức bằng chứng yêu cầu, thời hạn/sự kiện hết hiệu lực, ca nào phải chạy lại. Khi phụ thuộc chưa khai đủ, không mặc định kết quả còn xanh.

Phần cần kiểm lại = chưa có, chưa đủ mức, không đạt, hết hiệu lực hoặc bị ảnh hưởng theo phụ thuộc. BLOCKED không tự chạy lại vô hạn khi điều kiện mở chặn chưa đổi; vẫn theo dõi hạn và đầu mối bằng cơ chế rẻ. Chỉ miễn kiểm lại phần đã đạt khi phạm vi/phiên/phụ thuộc còn đúng.

PG lưu trạng thái/quan hệ/bằng chứng; DOT kiểm luật đã khai; JEV hỗ trợ khớp nghĩa/chồng lấn chưa chắc, không thay quyền duyệt hay bằng chứng chạy; Agent/người xử lý trường hợp thiếu luật. Hướng này đã có trong nguồn, cần biến thành từng ca kiểm cụ thể. Không dùng một graph có mũi tên làm chứng minh nghiệp vụ hoàn toàn đủ.

## 7. Ranh giới kết thúc composite và trường hợp không cần PG

TQT-TH-001 hướng tới chức năng chạy được; G3 lại duy trì theo dõi và tái diễn thì sửa tiếp. Cần ghi rõ khi nào **một lần chế tạo/bàn giao** kết thúc để không mở mãi hoặc đóng giả.

Đề nghị một lần chế tạo xong khi phạm vi nghiệm thu đạt và quy trình vận hành **đã nhận**. Theo dõi dài hạn thuộc lần áp dụng/quy trình VHCM phù hợp, liên kết phiên bàn giao; G3 có thể kiểm chứng ban đầu hữu hạn bằng số ca/sự kiện theo rủi ro, không yêu cầu Owner giữ terminal chờ thời gian cố định. Nếu chủ ý MOW tồn tại suốt vòng đời, gọi là đang duy trì, không đồng thời báo XONG kiểu công việc hữu hạn. Giao tiếp giữa Chuỗi cũng phải khai, không trộn quan hệ Nhóm cha/con khác Chuỗi.

G2 hiện mang PG trong tên và bước 2.2. Với mục tiêu tổng quát “một chi tiết/chức năng”, cần nhánh áp dụng/N-A có căn cứ cho trường hợp chỉ tài liệu/thiết kế/Config không ghi PG. Chạm PG/Directus vẫn phải DOT. Không dùng phần backend chưa cần của một ca để chặn giả toàn thiết kế.

## 8. Chồng lấn và cách nhìn đơn giản

Hai quy trình dùng chung một MOW con là tái sử dụng, không mặc định lỗi. Phải bắt trường hợp hai bên cùng nhận một việc/cùng ghi một trạng thái mà chưa phân quyền hoặc chưa có bên chịu trách nhiệm chính. Chồng lấn có chủ ý phải khai điểm phối hợp/hợp nhất. So mục đích+đối tượng+phạm vi+trigger+nơi ghi như nguồn đã đề xuất; không chỉ so tên.

Mặt Owner chỉ cần một đường:
**Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm nơi phát hiện → Kết thúc.**

Ô: tên, mã thật hoặc chưa đăng ký, người giữ, kết quả/hiệu lực. Mũi tên: chưa gửi/chờ nhận/đã nhận/đã trả; chỗ hở ghi thẳng “chưa có nơi nhận”. Bấm mới mở nguồn–đích, dữ liệu, điều kiện, phiên, bằng chứng. Dùng cùng khai báo để render và kiểm; link tài liệu không tô như kết nối đã chạy. Màu phù hợp tìm kiếm khác trạng thái vận hành, cần nhãn rõ.

## 9. Một lượt tiếp theo nên chứng minh gì?

1. Chốt quan hệ gọi và cách đăng ký composite theo đúng nguồn; rà Gộp/Tách trước. Thay nghĩa Công thức thì đưa Owner lựa chọn thật sự cần quyết.
2. Hoàn thiện khai báo **một quy trình xử lý sai/thiếu dùng chung**: mã Master, đầu vào/ra, con gọi, chỗ nối, nơi ghi, NTGV, kết thúc, phụ thuộc. TQT-TH-001 gọi quy trình ấy, không chép nội dung vào từng công đoạn.
3. Một ca thiếu Field thật trong phạm vi được phép đi qua hồ sơ → nhận việc → xác minh → quyết hướng → xử lý → trả về nơi gốc → kiểm/đóng. Nhánh tạo mới chỉ chạy khi quyền/B3–B7 đủ; chưa đủ thì chỉ rõ mắt nối thiếu, không dùng giả lập để chứng nhận runtime.
4. Có thể làm bằng người/agent theo cùng quy trình và bằng chứng trước; sau đó tự động hóa từng đoạn đã ổn định. Không cần dựng toàn PG/DOT hoặc thêm hàng trăm câu mới để bắt đầu chứng minh.

### Ca đối chứng tối thiểu, chưa thực hiện trong proposal này

| Ca | Mong đợi |
|---|---|
| Đã có Field phù hợp | Dùng lại, không tạo mới; kết quả về đúng phạm vi |
| Cùng nhu cầu/sự kiện gửi hai lần | Một hồ sơ chủ/một tác động; các nơi phát hiện cùng được theo dõi |
| Gửi mà chưa ai nhận/quá hạn | Vẫn có người giữ, có đường báo/leo thang |
| B4/B7 từ chối hoặc hủy | Quyết định về đúng nơi gọi; mục tiêu chưa đạt không đóng như đã sửa |
| B7 duyệt nhưng UI còn thiếu binding | Hồ sơ gốc còn mở đến khi đấu/kiểm đúng |
| Nguồn/MOW con đổi sau lần đạt | Chỉ các kết quả phụ thuộc cần kiểm lại; lịch sử cũ giữ nguyên |

Kiểm cấu trúc trước: ID/phiên không tồn tại, đầu vào không có nguồn, kết quả không có nơi nhận/terminal, chu kỳ chưa khai thoát, tự gọi vô hạn, cùng nơi ghi chưa phân quyền. Cần kiểm thêm các lỗi thiết kế nghiệp vụ bằng ca thật; không hứa DOT có thể suy ra mọi điều người chưa khai.

## 10. Đề nghị Host tiếp nhận

Ưu tiên: (1) đăng ký và gọi con; (2) phiếu MOW/MOT cạnh phiếu đối tượng Field; (3) một nối thực có mã lần gọi/nhận/trả; (4) tách kết quả khỏi hiệu lực. Chỉnh thêm ranh giới kết thúc/chuyển vận hành và trường hợp không cần PG. Giữ TQT-ISS-007, gắn tiêu chí và bằng chứng phù hợp; không mở sổ mới.

T2.5 và số câu tăng 3–5 lần là giả thuyết để bàn, không tiêu chí nghiệm thu. Chỉ thêm khi ca thật lộ quyết định chưa được hỏi. Đo tiến bộ bằng đoạn đã có mã/đầu vào-ra/người nhận/bằng chứng, không số câu/tên quy trình.

DOER_CONFIRM: PARTIAL — đọc/đối chiếu và kiểm cấu trúc được; chưa gọi MOW tổng hợp đăng ký hoặc chạy ca thiếu Field qua B3–B7 vì các mã/quyền/binding chưa đủ. Không tạo Field/PG trong lượt này.
Phản hồi Host: CHƯA CÓ. Astra Codex quyết tiếp nhận/sửa/bỏ, Reviewer không tự cập nhật nguồn chính.
Áp: SAME_COMMIT — chỉ lưu góp ý, chưa áp các đề xuất kiến trúc/trạng thái.
