# TQT-PR-20261009-gptchat-mow001-walkthrough-03 — Phiếu đi từng bước trước khi Codex làm lại

TQT-PROPOSAL: TQT-PR-20261009-gptchat-mow001-walkthrough-03
TARGET: MOW-NHC-001; ma trận 140 câu/53 nhóm; ba MOT 1.1–1.3, nghiệp vụ UI/Config/Test; tham chiếu Config và quy trình rà UI legacy.
TESTED: Đọc nguồn hiện hành; ghép 9 bộ câu hỏi; tự trả lời 44 Q_ID liên quan, 7 câu Config tham chiếu và đối chiếu 8 câu UI cũ cho ba MOT. Kiểm 3 trạng thái đầu UI sống; chạy 10 phép kiểm chẩn đoán bằng đúng module JS có SHA khớp nguồn, với hai bản ghi minh họa. Không chạy tìm kiếm/JEV production, không thực hiện click browser E2E và không sửa UI.
BLOCKER_TYPE: THIEU_HUONG_DAN / THIEU_SAN_PHAM / THIEU_QUYET_DINH — phân loại riêng tại mục 9.
OBSERVED: Bộ câu hỏi mới đã dẫn được tới đúng việc cần trả lời; điểm dừng hiện nằm ở đáp án/đặc tả áp dụng và mã UI cũ, không phải thiếu một Bước con. Đường live chưa tìm thật; phần minh họa lọc được nhưng không đánh giá JEV; 1.3 vẫn là ô người tự xác nhận, chưa phải kết luận máy tìm được/chưa tìm được theo phạm vi mới.
PROPOSED_CHANGE: Giữ 140 câu/53 nhóm và ba Bước con. Host chốt phiếu đáp án áp dụng + hợp đồng đầu vào/kết quả UI nhỏ ở mục 10, sửa đúng nguồn liên quan rồi làm UI001. Chưa cần triển khai backend để vẽ bản thử, nhưng không dùng bản thử để báo tìm kiếm thật đã chạy. MOW002 không làm.

## 0. Vai trò, phạm vi, kết luận

Ghế: GPT Chat — Reviewer theo yêu cầu Owner, đóng vai người thực hiện phép đọc/áp dụng; không phải Host.
Host: Astra Codex, phiên Owner đã chỉ định. Chỉ Host quyết tiếp nhận và sửa bốn file chính.
Bước/vòng: rà cuối trước lượt áp dụng MOW001; không tự mở/chốt vòng hội đồng, không phát READY/RUN.
Based_on: repo `69961997bd036c87960462b380f7e840dd7d45fd`.
Scope ghi: chỉ file đề xuất này trong proposals/. Không sửa sổ chuẩn, UI-REVIEW-MOW001.json, Công thức, Master, runtime, PG/Directus.

**Kết luận:** tôi đọc được, ghép được và viết được phiếu trả lời có căn cứ. Tuy nhiên, chưa thể tự hoàn thiện/kiểm đạt toàn UI001 mà không điền/chốt các đáp án thiết kế còn thiếu. Có thể giao Codex bắt đầu lượt áp dụng thực tế bằng việc hoàn tất phiếu đáp án, không cần thêm vòng tăng câu hỏi tổng quát. Không được nhảy thẳng từ “140 câu đã hiện” sang “vẽ xong/đã tìm được thật”.

- Việc đọc/ghép và xác định khoảng trống: đã làm trong phiếu này.
- Trọn quy trình rà UI bằng browser, mọi nhánh và kết quả thật: **PARTIAL**, chưa có bằng chứng đủ.
- Tự vẽ và nghiệm thu thiết kế mới: **chưa thực hiện**; một số đáp án còn là đề xuất cần Host nhận.
- Production tìm kiếm/Vector/JEV: **chưa chạy**, không suy từ minh họa.

## 1. Nguồn và cách kiểm

Các ký hiệu sau được dùng trong câu trả lời; version/hash phải được đo lại nếu Host áp dụng sau khi nguồn đổi.

| Mã | Nguồn đã đọc/đo | Phiên bản |
|---|---|---|
| S1 | tools-quy-trinh/view.html, JSON tqt-question-matrix và renderer | SHA256 `707390ffbdbd2398bba9ff9ead402496e74ef0d091b6493912b4b46c1e50ab10` |
| S2 | tools-quy-trinh/README.md, PROMPT phần hiện hành, COLLAB §0 | repo `69961997…`; README `26035bc892ad48b2e8d59e6a82dc24956b24e11d3b4ad0cce369075a537363cb` |
| S3 | ui/definition-master-data-v1.js: CT-001, NHCN-001/002/003, các Master; nguồn mô tả/Config của từng bước | `93eae888106544e7905751a15cc72b360971f3d8bda437887bfbf3f5c07b044c` |
| S4 | ui/field-flow-v1.js: renderer, jev(), search(), xác nhận | `f4010c721b2690d9909216d62f93fcf2fb031ca7e746ed9135236f112d08140f` |
| S5 | ui/field-flow-model-v1.js: create/change/go/filter/result/choose/confirm | `03197b1fa31c7dbe8b1c43043425f395359d0797c6b22fb88d7db6a54a50a430` |
| S6 | ui/search-demo-data.json: dữ liệu minh họa, KHÔNG canonical | `9e5f69e50bba9596825b3b493cf88ab0a81421a7c617826bc42f4d7262ff922c` |
| S7 | ui/config-master-data-v1.js: CONFIG_PRINCIPLES, đủ 7 câu nguồn | `8cdde9db9832bf15c88ae4fb2fa939760d5cca2bdb8f322201dec23e2e96474e` |
| S8 | UI-DESIGN-STANDARD.md → ban-duyet.html#standard-UI-029 / #parent-ui-common / #parent-ui-review-gate | ban-duyet `e02299dfdd8a15769ece7104a930f09451dd22a16d60a208b2a0bafe80e02069` |
| S9 | work/mow-mot-moit-mout/UI-REVIEW-MOW001.json, phiếu trước | `e5d2f0b26d6762b5fd64842e083ab8889e930ea3b09d18fcef5c854b8562302f`, vẫn PARTIAL |
| S10 | ui/definition-master-registry-v1.js: Master Field ML-DEF-008, T0 độc lập; field-master-v1.html là demo cũ | `e658ec26a41689341d1ee46b4fb62353b5adb81a304c59b1dc3cfa78ddcf3c8d` |

**Kiểm ma trận thực sự:** job `53cf836bee694646a16911fca2590f61`, Python trong snapshot repo, exit 0. CTCM + FIELD + mỗi B1.1/B1.2/B1.3 + UI = 32 câu; đổi UI thành CONFIG = 31, thành TEST = 31. Hợp chín bộ được **44 Q_ID khác nhau**. CONFIG.required_reference có đủ 7 source_index và chỉ rõ ứng viên dùng lại, không tự đánh đủ. Đây là đọc JSON/tái hiện thuật toán kế thừa, không phải browser thao tác bộ chọn.

**Màn hình sống đã mở qua ui_inspect:** `tim-kiem-chung-v1.html?scope=FIELD&flow=field&embed=mow&step=1` (1280px), step=2 (390px), step=3 (1280px); cả ba HTTP 200, console_errors=0 ở lần mở tương ứng. Step1 có ô tên/mã, mô tả, Tìm kiếm, Nâng cao, Xóa; step2 có trạng thái/nhánh/kiểu; step3 mở trực tiếp thì chưa chọn Field và nút xác nhận bị khóa. Không suy các quan sát tải trang này thành kiểm responsive/toàn tương tác đạt.

**Phép đi bằng mã thực:** chép đúng S5 vào môi trường kiểm cục bộ, kiểm SHA256 khớp từng byte, chạy Node v22.16.0 với các cột liên quan của hai bản ghi S6: MOIT.phone_number và MOUT.phone_number. 10 phép kiểm chẩn đoán đều chạy xong; chi tiết mục 8. Đây là module thật với dữ liệu minh họa đã có, không phải tự viết lại thuật toán hay JEV giả.

**Giới hạn:** một script trích xuất ban đầu lỗi cú pháp đã sửa và chạy lại; không tính lượt lỗi là kiểm đạt. Thử browser tương tác trong môi trường cục bộ không đi tiếp do DNS EAI_AGAIN; không vượt chặn. Các kiểm browser ở phiếu này chỉ là ui_inspect nêu trên, không bấm/gửi/lưu production. Không nghiệm thu lại toàn bộ 140 câu, chỉ tập áp dụng cho MOW001.

## 2. Đi bộ: dừng ở mỗi bước và kết luận rõ

**Ca cụ thể dùng để thử cách làm:** cần tìm định nghĩa Field số điện thoại dùng làm đầu vào. Vòng đầu gõ `SĐT`; vòng sau bổ sung ngữ cảnh đầu vào MOIT. Đây là dữ liệu thử của Reviewer, không biến thành mặc định nghiệp vụ hay chỉ đạo mới của Owner. Chỉ hỏi Field nào phù hợp với nhu cầu tìm; không nhập số điện thoại người thật, không áp dụng Field vào form và không thực hiện B2 Dùng.

| Chặng | Tôi làm gì, trả lời gì | Đi tiếp hay dừng? |
|---|---|---|
| 0. Đọc và xác định việc | Đọc AGENTS → mục tiêu/Host → README → JSON câu hỏi → nguồn MOW/UI. Chọn CTCM, FIELD, ba Bước con và UI/Config/Test; không chọn T3–T7 hay Chuỗi khác. Các câu cha trả lời ở phạm vi cha rồi dẫn lại. | Đi được. Không cần đoán Host, file nguồn hoặc số bước. |
| 1.1 Tìm thường | Trạng thái đầu trống; người gõ SĐT. Tôi biết ô nào, nút nào và đối tượng cần tìm. Nhưng S4 search() ở mode live trả ngay unavailable, chưa gọi nguồn Field/Vector. | Đường tìm thật dừng ở đây. Không biến lỗi/chưa kết nối thành “không tồn tại Field”. |
| 1.1 tiếp bằng minh họa tách biệt | Dùng đúng hai bản ghi S6 trong module S5: query SĐT cho 2 kết quả MOIT.phone_number/MOUT.phone_number. Có ID/tên/kiểu/ngữ cảnh để xem. | Đi được phần minh họa. Không có điểm/màu/đánh giá JEV để kết luận phù hợp. Cần đáp án hợp đồng kết quả; không coi hai kết quả này là dữ liệu canonical. |
| 1.2 Tìm nâng cao | Chuyển sang 1.2 giữ query; thêm branch=Nhận đơn › MOIT, mô tả nhu cầu đầu vào; lọc từ 2 còn 1 trong module. | Lọc minh họa làm được. Chỉ sửa description không làm kết quả lọc thay đổi; renderer cũng báo chưa có dịch vụ tìm theo mô tả. Vòng 2 đánh giá theo ngữ cảnh thật chưa thực hiện. |
| 1.3 Đánh giá/kết luận tìm kiếm | Theo phạm vi mới, máy phải đánh giá mức phù hợp; màu và lý do gắn kết quả. S4 lại hiển thị “Chưa có đánh giá JEV”, rồi ô người dùng tích “Field này phù hợp…”. S5 chỉ cho demo confirm sau accepted=true. | Dừng tại khoảng trống quan trọng: ô người tích không thay cho máy kiểm, một kết quả còn lại không tự là Xanh. Chưa được tự công nhận TÌM ĐƯỢC bằng logic này. |
| Kết thúc B1 | Đầu ra chỉ là kết luận tìm được/chưa tìm được cùng kết quả/phạm vi/căn cứ. B1 không thực hiện Dùng/Tạo/Sửa. S5 receipt hiện chỉ có demo fieldId/query/filters/destination/persisted=false, chưa có kết luận máy. | Có thể đặc tả đầu ra ngay, nhưng phải ghi rõ đây là đề xuất chờ Host chốt. Không bắt buộc mở B2 hoặc ghi DB để kết thúc việc thiết kế B1. |
| Bàn giao lần rà | Tôi trả phiếu này, chỉ rõ Q nào có căn cứ/Q nào thiếu và nguồn phải bổ sung. Sổ/phiếu MOW chính để Host tiếp nhận, không sửa trái quyền. | Hoàn thành phép đi câu hỏi; rà/vẽ/kiểm đầu–cuối thực tế còn PARTIAL. |

## 3. Trả lời đủ câu chung/chuyên môn gốc — 21 Q_ID

Ký hiệu: **C** = có căn cứ để đặc tả/tiếp tục, KHÔNG đồng nghĩa đã chạy đạt; **R** = giá trị có lúc chạy, nguồn/cách dùng đã biết; **G** = thiếu căn cứ thiết kế, hoặc cần quyết định/hợp đồng; **N/A** = ngoài phạm vi, nêu lý do. Một câu có thể C ở phần nguyên tắc nhưng G ở phần binding thật.

Các câu ở bảng này áp ở đúng cấp B1/Chuỗi/Tầng; không bắt mỗi Bước con chứng minh toàn Chuỗi đã hoạt động.

| Q_ID | Câu trả lời khi áp dụng MOW001 | Căn cứ / tình trạng |
|---|---|---|
| Q-CHAIN-01 | CTCM hỗ trợ người/AI tìm thành phần Field đã có để giảm tạo trùng; ca hiện tại chỉ Tìm ở T0, không vận hành hay tạo quy trình nghiệp vụ phái cử. | S1,S2; C |
| Q-CHAIN-02 | Phạm vi CTCM là chế tạo năng lực, nhưng lượt B1 bắt đầu từ yêu cầu tìm và kết thúc bằng kết luận tìm. Không bắt chuyển Chuỗi để xong từng MOT. | S1; C theo phạm vi, không kết luận toàn Chuỗi xong |
| Q-CHAIN-03 | Host task chịu trách nhiệm tiếp nhận; người thực hiện ghi phiếu có nguồn và kiểm lại. Chưa có chứng cứ để nhận toàn máy CTCM vận hành đạt. | S2,S9; C/N-A nghiệm thu toàn Chuỗi |
| Q-CTCM-01 | Thành phần đang xét là định nghĩa Field cho nội dung số điện thoại đầu vào; không phải tạo Field mới trong bước này. | Q-B1-01 + ca thử; C/R |
| Q-CTCM-02 | Dùng lại Master Field, metadata, UI-029 và câu hỏi có ID; phần thiếu là binding tìm/JEV và đặc tả đầu ra, chỉ ghi đề xuất. | S3,S4,S8,S10; C/G |
| Q-CTCM-03 | Đầu ra cấp Chuỗi cần tài liệu/thiết kế và bằng chứng phù hợp. Riêng B1 trả kết quả cho người/yêu cầu đã gọi tìm, không bắt bước Dùng của Chuỗi khác chạy. | S1 R-INHERIT; C; đích integration cụ thể G |
| Q-LAYER-01 | T0 Field là đối tượng định nghĩa, không phải giá trị số điện thoại một cá nhân. | S3,S10; C |
| Q-LAYER-02 | Địa chỉ danh mục là ML-DEF-008, definition-master-v1.html?stt=8. API/chỉ mục được search theo quyền vẫn chưa xác minh; không lấy field-master demo/S6 làm nguồn production. | S3,S10; C địa chỉ, G nguồn chạy |
| Q-LAYER-03 | Field có thể được các MOIT/MOUT tham chiếu. Trong B1 chỉ đọc danh tính/metadata/ngữ cảnh để đối chiếu, không gắn nó vào form. | S3,S10; C |
| Q-LAYER-04 | Có ID/tên/kiểu dữ liệu/nguồn/validation và metadata liên quan. S10 nêu cột danh mục nhưng chưa đủ chứng minh mọi trường nào bắt buộc trong hợp đồng response của search. | S10; C một phần, G hợp đồng response |
| Q-LAYER-05 | Kiểm tính hợp lệ của định nghĩa để đối chiếu nhu cầu; việc được cấp phép dùng là B2. Không bắt B1 thực thi Dùng. Quyền đọc nguồn phải đúng phạm vi. | S1 R-INHERIT, S10; C; rule runtime G |
| Q-FIELD-01 | Với ứng viên demo MOIT.phone_number: tên SĐT, kiểu Văn bản, không đơn vị đo. Field thật và metadata cụ thể là R sau tìm. Không suy hai mã MOIT/MOUT demo là hai định nghĩa T0 canonical khác nhau. | S6,S10; R/G ánh xạ canonical |
| Q-FIELD-02 | Đọc định nghĩa từ danh mục được chỉ; ở ca này không nhập giá trị điện thoại. Nguồn giá trị của Field khi được dùng là metadata theo nơi dùng, chỉ đọc nếu là tiêu chí tìm. | S10; C; không khai giá trị cá nhân |
| Q-FIELD-03 | “Bắt buộc” theo nơi sử dụng không được gán mặc định vào Field T0. Validation/kiểu là dữ kiện để tìm phù hợp; quy tắc cụ thể đọc từ định nghĩa/config khi cần. Không giả N-A cho câu đang thực sự dùng làm tiêu chí. | S10 và R-ANSWER; C/R, G khi validation nguồn chưa có |
| Q-STEP-01 | B1 bàn giao danh sách/đối tượng tìm được hoặc kết luận chưa tìm được trong phạm vi đã tìm, kèm căn cứ, cho người hoặc nơi gọi tìm. Không bàn giao “đã áp dụng Field”. | S1 Q-B1-03; C; khuôn response/đích cụ thể G |
| Q-STEP-02 | Cần yêu cầu tìm, phạm vi loại FIELD và nguồn truy vấn; người nêu nhu cầu, máy tìm/đánh giá. Quyền/adapter cụ thể phải lấy từ Config, chưa có thì không tự chọn tài khoản. | S3,S4,S7; C nguyên tắc/G kết nối |
| Q-STEP-03 | Bằng chứng gồm phiên yêu cầu, nguồn/phạm vi đã truy, kết quả và đánh giá tương ứng. Chỉ tải trang hoặc có 1 dòng trả về không chứng minh tìm phù hợp. Khuôn kết luận cuối còn cần chốt. | S1 R-ANSWER/R-PROVE, S4,S5; G |
| Q-STEP-04 | Trống/chưa tìm; yêu cầu hợp lệ; đang tìm; có ứng viên; không ứng viên; thiếu căn cứ; lỗi/thiếu quyền; bổ sung ngữ cảnh/tìm lại; hủy/dừng. 1.2 là tùy nhu cầu; không phải ca nào cũng buộc thực hiện mọi MOT. | S1,S4,S5; C; màu/điều kiện dừng G |
| Q-B1-01 | Tìm Field số điện thoại ở ngữ cảnh đầu vào, vòng đầu chỉ gõ SĐT. Đây là input thử, không phải chuẩn toàn hệ thống. | S6 và ca thử; R |
| Q-B1-02 | Nguồn danh mục có địa chỉ S10; nơi thực thi tìm theo quyền/Vector chưa được nối S4. Phạm vi không phải “mọi bản ghi ở mọi nơi”. | S3,S4,S10; G nguồn tìm thật |
| Q-B1-03 | Tìm được khi có kết quả phù hợp với yêu cầu trong phiên tìm; chưa tìm được khi đã kết thúc việc tìm mà chưa xác định phù hợp, có phạm vi/căn cứ. Lỗi nguồn/chưa chạy không chứng minh không tồn tại. Không thực hiện B2. | S1; C nguyên tắc/G quy tắc quyết cuối và gói đầu ra |

## 4. Dừng từng MOT để trả lời câu hành động riêng — 10 Q_ID, 18 lần áp dụng

| Q_ID | 1.1 Tìm thường | 1.2 Tìm nâng cao | 1.3 Xác nhận phù hợp |
|---|---|---|---|
| Q-CHILD-01 | Nhận query/mô tả/phạm vi; trả tập ứng viên và ngữ cảnh tìm. Nếu cần chuyển 1.2, giữ input; nếu đủ thì máy đánh giá. C/G response. | Nhận yêu cầu đang tìm; bổ sung filter/ngữ cảnh; trả tập đã thu hẹp cùng query mới. C/G nguồn filter. | Nhận yêu cầu + ứng viên + metadata/bằng chứng; trả đánh giá/kết luận của B1 hoặc yêu cầu làm rõ/tìm lại. Không chuyển nghĩa thành “đã Dùng”. G schema. |
| Q-CHILD-02 | Trống/sai thì hướng nhập lại; lỗi nguồn giữ input, báo chưa tìm được do lỗi kỹ thuật, không báo đối tượng không tồn tại. S4 có invalid/unavailable. C. | Filter chặt quá thì bỏ bớt/thay, không tạo 1.4. Lỗi dịch vụ khác kết quả rỗng. C/G việc tìm lại thật. | Thiếu căn cứ/Vàng thì nêu thông tin còn thiếu và tìm lại; lỗi đánh giá thì chưa đánh giá, không Đỏ giả; chưa có đủ rule ở nguồn. G. |
| Q-CHILD-03 | Người nhập; máy truy nguồn/xếp kết quả. S5 hiện chỉ filter demo, không Vector/JEV. C vai trò/G triển khai. | Người bổ sung điều kiện; máy lọc/tìm lại và đánh giá theo ngữ cảnh mới. C/G. | Máy đánh giá phù hợp; người có thể xem, bổ sung hoặc dừng. Checkbox hiện tại không phải bằng chứng máy đã kiểm. G/S4,S5. |
| Q-CHILD-04 | Bắt đầu khi input hợp lệ và nguồn khả dụng; xong tác vụ truy khi có phản hồi phân biệt kết quả/lỗi. S5 revision kiểm phản hồi còn đúng. C/G source. | Bắt đầu khi cần làm rõ/lọc sâu; xong khi phản hồi thuộc query/filter mới, không dùng stale result. W04/W07 kiểm được phần model. C/G. | Bắt đầu khi có dữ kiện cần kiểm; kết thúc bằng đánh giá/kết luận có căn cứ hoặc trạng thái chưa thể kết luận. Không cần chờ B2. Chưa có machine verdict. G. |
| Q-B1.1-01 | Người chưa biết mã nhập mô tả nhu cầu; UI đã có ô. Dịch vụ hiểu mô tả chưa có, là G kết nối/đặc tả, không phải thiếu giá trị người chưa nhập. | N/A: câu riêng của 1.1; dẫn ngữ cảnh đã nhập. | N/A: câu riêng của 1.1. |
| Q-B1.1-02 | Cần xếp theo phù hợp và giải thích từ dữ kiện nào. S5 hiện giữ thứ tự lọc, S3 mới nêu exact_match_rule/ranking_rule; chưa có giá trị áp dụng hay đánh giá thật. G. | N/A câu riêng. | N/A câu riêng. |
| Q-B1.2-01 | N/A câu riêng. | Vòng đầu SĐT cho hai demo đầu vào/đầu ra; thiếu ngữ cảnh “đầu vào MOIT”. Đáp án này là ví dụ thật từ fixture, không mặc định mọi lần tìm đều thiếu như vậy. C. | N/A câu riêng. |
| Q-B1.2-02 | N/A câu riêng. | S4 có filter trạng thái, nhánh, kiểu; S5 dùng so sánh bằng giữa các filter và kết hợp với query. W04 lọc branch còn một dòng, quay lại W06 giữ dữ liệu. Danh sách filter/toán tử nguồn thật còn G. | N/A câu riêng. |
| Q-B1.3-01 | N/A câu riêng. | N/A câu riêng. | Đối chiếu yêu cầu hiện tại và metadata ứng viên, không quyền Dùng. S3 có mandatory_checks nhưng chưa điền bộ kiểm áp cho MOW001. Không tự chế ngưỡng phần trăm. G. |
| Q-B1.3-02 | N/A câu riêng. | N/A câu riêng. | Màu thể hiện mức phù hợp với yêu cầu tìm. Vàng/thiếu căn cứ thì bổ sung ngữ cảnh/tìm lại; query mới phải làm đánh giá cũ hết hiệu lực. S4 chưa có JEV và badge kết quả thật. C ý nghĩa/G contract+UI. |

## 5. Nghiệp vụ UI/Config/Test — 13 Q_ID, 39 lần áp dụng

| Q_ID | 1.1 | 1.2 | 1.3 |
|---|---|---|---|
| Q-UI-01 | Tiêu đề Tìm Field, ô input và nút rõ; biết đang Tìm. C theo màn đã mở, chưa khẳng định usability toàn bộ. | Tiêu đề Nâng cao và câu hướng dẫn giữ nhu cầu rõ. C. | Hiện yêu cầu người xác nhận thay vì hiển thị kết luận máy; chưa đáp ứng ý nghĩa mới. G. |
| Q-UI-02 | Dùng UI-029, theo S8; không tạo renderer riêng cho mỗi MOW. Parity chưa đo lại. C/NOT_TESTED. | Dùng cùng UI-029, vùng filter cấu hình riêng. C/NOT_TESTED parity. | Có thể dùng cùng nguồn/biến thể hiển thị đánh giá; nếu cần mẫu khác phải tra/duyệt theo S8, không cấp ID mới tự động. G quyết phần riêng; không kết luận chưa có mẫu là phải dựng lại toàn bộ. |
| Q-UI-03 | Máy biết MOW/Field/phạm vi; người gõ query/description. Nhãn và nơi nhập đã có. C/R. | Máy giữ input/filter trước; người thêm ngữ cảnh/filter cần thiết. C/R. | Máy điền ứng viên, đánh giá và lý do; người chỉ xem/chỉnh nhu cầu. Không yêu cầu người tick hộ máy. G phần hiện thực. |
| Q-UI-04 | Đã có idle/loading/results/empty/invalid/unavailable ở S4; thiếu hiển thị đánh giá từng ứng viên theo nguồn mới. C/G. | Tương tự; cần giữ rõ “không kết quả sau lọc” khác lỗi/thiếu ngữ cảnh. C/G. | Cần pending/đã đánh giá/thiếu căn cứ/lỗi đánh giá và kết luận tìm. S4 mới có chưa chọn/checkbox/receipt demo. G. |
| Q-UI-05 | Nút search/nâng cao/xóa có code; browser mới kiểm tồn tại, chưa bấm E2E. Live search chưa nối. PARTIAL. | Filter/back/bỏ lọc có code; W04/W06 kiểm model, không thay browser. PARTIAL. | Nút confirm demo chỉ tạo receipt cục bộ; không chứng minh machine verdict. Không chấp nhận đổi nhãn đơn thuần để báo đúng. G. |
| Q-CONFIG-01 | Áp cho phiên tìm Field CH-001/B1/1.1; phân biệt dữ liệu query và rule tìm. Chưa xác định record Config runtime chính xác. C/G. | Áp cho bộ lọc 1.2 cùng query; không làm rộng scope khi back. C/G binding. | Áp cho đánh giá phù hợp B1/1.3, không quyền Dùng; thiếu nguồn config áp dụng cụ thể. G. |
| Q-CONFIG-02 | S3 nêu search_fields, exact_match_rule, ranking_rule, aliases; chưa có giá trị/binding cho nguồn thật. Input trống ban đầu có S5, không tự gán rule mặc định. C/G. | S3 nêu filter_fields/operators/default_sort/saved_filter_scope; S5 có demo equals. Chưa dùng equals demo thay mọi nghiệp vụ. G. | S3 nêu mandatory_checks/green/yellow/red/evidence_fields; một số nghĩa cũ là “được dùng” phải đối chiếu ranh giới mới, không nhận nguyên xi. G. |
| Q-CONFIG-03 | Chưa có quy tắc ưu tiên chung đã chốt ở S7. Không tự chọn rule đầu; UI có thể biểu diễn “chưa cấu hình/xung đột”. G, không bắt giải toàn engine để vẽ. | Tương tự; chưa biết operator hoặc nhiều rule khớp thì ghi thiếu. G. | Tương tự; không để điểm tương tự tự vượt rule bắt buộc; không tự đặt ngưỡng mới. G. |
| Q-CONFIG-04 | Người sửa nguồn thiết kế theo Host/guard task, khác người gõ query. Bản Config thực/phiên hiệu lực/rollback chưa xác minh. C/G. | Cùng nguyên tắc; chỉ reset filter UI không phải rollback Config hệ thống. C/G. | Cùng nguyên tắc; đổi cách hiểu màu phải cập nhật nguồn/phiên và kiểm consumer, không chỉ sửa badge. C/G. |
| Q-TEST-01 | Ca trống; tên/mã; mô tả; một/nhiều/không ứng viên; lỗi nguồn, mỗi ca có expected lấy từ Q/nguồn. Một phần expected về verdict còn G. | Ca thêm/bỏ filter, sửa ngữ cảnh, quay lại, response cũ. S5 có thể thử phần trạng thái. C/G. | Ca chưa chọn, có dữ kiện, xanh/vàng/đỏ, thiếu đánh giá, kết thúc tìm. Expected nguyên tắc có, rule cụ thể G. |
| Q-TEST-02 | Đã thử module W01/W02/W08, tải trang; chưa browser submit/focus/nhãn trong mọi nhánh. PARTIAL. | Module W04–W07; viewport tải trang 390px; chưa đo parity/bàn phím đầy đủ. PARTIAL. | Module W03/W09/W10; tải direct step3; chưa có máy đánh giá, không thử giả JEV rồi nhận E2E. BLOCKED/PARTIAL. |
| Q-TEST-03 | Người biết nơi gõ nhưng không tìm thật được hiện nay. Reviewer đọc đúng nguồn để lập phiếu, không coi đọc README là lỗi. PARTIAL. | Người nhìn được filter nhưng chưa chứng minh tìm lại theo ngữ cảnh thật. PARTIAL. | Không thể xác nhận người mới làm trọn đích tìm bằng máy hiện nay. PARTIAL. |
| Q-TEST-04 | Hash nguồn và dữ liệu thử đã ghim; module có thể tái hiện. Browser E2E chưa có ở lượt này. C/PARTIAL. | Cùng snapshot/test, không dùng kiểm cũ cho bản tương lai. C/PARTIAL. | Cùng snapshot; phép kiểm receipt demo không đổi thành bằng chứng kết luận thật. C/PARTIAL. |

**Đối chiếu số lượng:** 21 Q_ID chung + 4 CHILD + 6 câu riêng ba Bước con + 13 nghiệp vụ = **44 Q_ID**. Theo ba MOT là 120 lần áp dụng câu trong hợp UI/Config/Test; câu chung dẫn cùng đáp án đúng phạm vi, không chép về ma trận. Bảy câu tham chiếu Config dưới đây bổ sung 21 lần đối chiếu, không đổi số 140 câu gốc.

## 6. Bảy câu Config gốc — đã trả lời riêng từng MOT

Đường chuẩn: S7 CONFIG_PRINCIPLES; tham chiếu tại S1 groups.CONFIG.required_reference. Các mã C1…C7 bên dưới chỉ là số dòng tham chiếu, KHÔNG cấp Q_ID mới.

| Câu nguồn | 1.1 | 1.2 | 1.3 |
|---|---|---|---|
| C1 Bắt đầu từ đâu? | Tại yêu cầu tìm Field hợp lệ của người/nơi gọi. Nguồn/adapter chưa nối. | Từ yêu cầu đang có cần lọc/bổ sung; cũng có thể mở trực tiếp với input trống rồi nhập. | Từ ứng viên và yêu cầu cùng phiên cần đánh giá; không đòi bấm Dùng. |
| C2 Kết thúc ở đâu? | Có phản hồi truy phù hợp phiên yêu cầu, hoặc trạng thái lỗi; 1.1 xong chưa đồng nghĩa toàn B1 đã kết luận. | Có phản hồi cho input/filter mới; còn Vàng thì có thể tìm tiếp. | Kết luận tìm hoặc báo thiếu căn cứ để tìm lại/dừng; schema cụ thể cần Host chốt. |
| C3 Điều kiện là gì? | Input hợp lệ, nguồn được phép truy và phạm vi FIELD; thiếu source báo unavailable, không kết luận vắng. | Filter/ngữ cảnh có nghĩa trong phạm vi đã chọn; operator do config quyết. | Có dữ kiện đối chiếu và rule/phiên; thiếu rule không được tự tô xanh/đỏ. |
| C4 Trigger là gì? | Người submit Tìm; S4 có handler. | Submit sau thêm/bỏ điều kiện; không nhất thiết mọi lần gõ đều gọi máy. | Theo đề xuất hiện tại: dữ liệu tìm mới về kích hoạt đánh giá tự động, đồng bộ query revision; handler thực chưa có. |
| C5 Ai làm? | Người mô tả; adapter/Vector truy; evaluator/JEV đánh giá theo contract. Binding máy thật G. | Người làm rõ; máy lọc/tìm lại/đánh giá lại. | Máy đánh giá; người không tick thay kết luận máy. Người quản lý config khác người thực hiện. |
| C6 Báo cáo cho ai? | Người/yêu cầu gọi tìm xem kết quả và lý do ngay UI. Lỗi kỹ thuật cần đầu mối theo sổ cũ; chưa giao verifier thật thì giữ thiếu. | Cùng người/yêu cầu tìm; không tự gửi sang task khác. | Người/yêu cầu tìm nhận kết luận; không gửi “đã Dùng” hay tự giao người duyệt mới. |
| C7 Chuyển tiếp cho ai? | Cho bước lọc/đánh giá trong cùng B1 hoặc trả kết quả; giữ query/metadata. | Cho đánh giá cùng phiên hoặc lặp tìm. | B1 kết thúc/trả kết quả. Chuyện bước khác tiêu thụ kết quả là ngoài phạm vi thực thi B1; không bắt nó chạy để đạt phiếu này. |

**NTGV:** không thiết kế cơ chế giao việc mới ở lượt tìm này. Tham chiếu C5/C6 và Q-CHILD-03 trả vai trò có sẵn. Không thể reuse mặc nhiên người phụ trách Config làm người đánh giá; khi thực sự dựng phân công mới thì mới ghép đủ bốn câu NTGV. Không bỏ qua quyền/scope chỉ vì không ghép NTGV.

## 7. Tám câu rà UI legacy — đối chiếu đủ 24 ô, không làm nguồn câu hỏi mới

| Câu | 1.1 | 1.2 | 1.3 |
|---|---|---|---|
| Q1 Làm gì/xong khi? | UI nói Tìm Field; thiếu kết quả tìm thật. | UI nói thu hẹp; có filter demo, chưa semantic. | UI nói xác nhận, chưa đúng máy kiểm và kết luận tìm. |
| Q2 Bắt đầu/nhận gì? | Trống, không prefill kết quả. | Query/description từ trước; direct load trống hợp lệ. | Chưa chọn thì khóa; code nhận selected và query. Contract machine evaluation còn thiếu. |
| Q3 Nhập/chọn gì? | Tên/mã/mô tả nhìn thấy; mô tả chưa chạy được. | Thêm trạng thái/nhánh/kiểu; cần sources/operators rõ cho bản thật. | Đáng ra xem đánh giá hoặc bổ sung ngữ cảnh; code hiện bắt checkbox. |
| Q4 Bấm gì? | Search/nâng cao/xóa hiện rõ. | Search/quay về/xóa và filter hiện rõ. | Chọn lại/confirm hiện rõ nhưng ý nghĩa confirm cần sửa. |
| Q5 Phân biệt trạng thái? | Code có idle/results/empty/unavailable; chưa có badge JEV. | Cùng trạng thái + filter; thiếu semantic đánh giá lại. | Chưa chọn/đã xác nhận demo không thay xanh/vàng/đỏ có căn cứ. |
| Q6 Đạt rồi đi đâu? | Kết quả thuộc B1; có thể xem đánh giá hoặc lọc sâu. | Kết quả tìm mới, không sang Dùng tự động. | Kết thúc/trả kết luận tìm; không buộc chuyển B2. |
| Q7 Không đạt/lỗi/hủy/back? | Giữ input, thử lại/đổi; lỗi nguồn không phải không tồn tại. | Bỏ filter, giữ ngữ cảnh, loại response cũ. | Vàng tìm lại, lỗi đánh giá báo thiếu, không checkbox chữa thành xanh. |
| Q8 Thay đổi gì/ai nhận/bằng chứng? | Chỉ truy vấn/trạng thái tìm; không sửa Field. | Chỉ query/filter/trạng thái tìm; không sửa definition. | Trả kết quả tìm cho nơi gọi/người dùng; receipt hiện chỉ minh họa, chưa phải contract kết luận. |

Bảng này là câu trả lời của lượt áp dụng, không sửa bộ 8 câu nguồn và không suy là 24 ô đã có PASS browser.

## 8. Ca kiểm cụ thể và kiểm hai chiều

### 8.1. Kết quả module thực S5 (10 ca, không phải E2E)

| Ca | Điều kiện/thao tác | Quan sát đã kiểm bằng assert | Ý nghĩa nghiệm thu |
|---|---|---|---|
| W01 | create(example) | idle, rows rỗng, valid=false | Trạng thái đầu đúng; không phải tìm thành công |
| W02 | query=SĐT, filter hai record S6 | 2 ID MOIT.phone_number/MOUT.phone_number | Chỉ chứng minh tìm từ khóa trên fixture |
| W03 | chọn MOIT.phone_number; trước/sau accepted=true; confirm | step=3; checkbox cho phép confirm; receipt demo=true,persisted=false | Chứng minh UI cũ dùng xác nhận người; KHÔNG đạt máy đánh giá |
| W04 | từ 1.1 sang 1.2; branch=Nhận đơn › MOIT | Giữ query; còn 1 ứng viên | Lọc được, không tự kết luận xanh |
| W05 | đổi description, bỏ branch | Vẫn 2 ứng viên | Mô tả không được model này dùng để đánh giá lại |
| W06 | chọn từ 1.2 rồi go(2) | query/filter/1 dòng giữ nguyên | Back giữ ngữ cảnh ở lớp model |
| W07 | sửa description sau chọn, đưa response revision cũ | selected/rows bị xóa; response cũ bị bỏ | Không dùng đánh giá/kết quả cũ cho yêu cầu mới |
| W08 | query không khớp fixture | phase=empty | Không match trong fixture, không kết luận toàn hệ thống không tồn tại |
| W09 | mở step3 trực tiếp chưa chọn | canConfirm=false | Guard chọn ở UI cũ; không chứng minh machine verdict |
| W10 | mode live, cấp candidate vào hàm để kiểm guard, accepted=true | canConfirm=false | Không lách demo confirm sang live; không gọi nguồn thật |

Node v22.16.0 local, nguồn S5 chép đúng hash; dữ liệu chỉ là projection của hai record S6. 10/10 assertion PASS = tái hiện chẩn đoán đúng mã đang có, không có nghĩa 10/10 yêu cầu nghiệp vụ mới PASS. S4 còn trả unavailable ngay ở search live và jev() chỉ dựng placeholder — đã đọc trực tiếp, không suy từ giao diện trống.

### 8.2. Hai chiều yêu cầu ↔ UI/Config ↔ ca

| Yêu cầu/căn cứ | Phần thực hiện dự kiến/hiện có | Ca và kết luận |
|---|---|---|
| Nhập nhu cầu không biết mã — Q-B1.1-01 | Ô query + description hiện có | W01; browser tải step1 thấy đủ; xử lý semantic còn thiếu |
| Dùng đúng danh mục/phạm vi — Q-B1-02/Q-LAYER-02 | search adapter + config source | LIVE-SOURCE: BLOCKED vì S4 chưa nối; không thay bằng S6 |
| Đánh giá từng ứng viên — Q-B1.1-02/Q-B1.3-01/02 | Badge trạng thái/lý do trên dòng + panel chi tiết | COLOR-1/2: chưa có contract và evaluator; không thể dùng W02 làm PASS |
| Tìm lại với ngữ cảnh mới — Q-B1.2-01/02 | query/filter + request revision + evaluator lại | W04–W07 chỉ model phần lọc/invalidate; semantic còn thiếu |
| Không thấy khác lỗi — Q-B1-03/Q-UI-04 | empty khác unavailable/error, scope kết luận | W08 + đọc S4; cần đặc tả kết luận cuối, không giả nonexistence |
| Máy kết luận không phải người tick — Q-CHILD-03/Q-B1.3-02 | Đánh giá/kết luận từ máy; không checkbox thay thế | W03 xác nhận code hiện tại chưa đúng yêu cầu mới |
| Không thực hiện Dùng — Q-B1-03/R-INHERIT | B1 chỉ result report, không gọi apply/create | Kiểm source S4/S5 không ghi production; nghĩa UI confirm cũ phải chỉnh, không thêm B2 |
| Kế thừa UI cha — Q-UI-02 | UI-029 + chuẩn S8 | NOT_TESTED parity đầy đủ, không sửa mã UI mới ở lượt này |
| Ghi và truy bằng chứng — Q-TEST-04/R-ANSWER | Phiếu chính S9 và sổ OPEN khi Host nhận | Phiếu Reviewer riêng đã có; chưa ghi/đóng sổ chuẩn |

Các ca yêu cầu mới có expected nguyên tắc, nhưng màu/ngưỡng/cấu trúc cuối cần Host chốt trước khi test PASS. Không lấy code đang thiếu để tự viết expected hợp thức hóa nó.

## 9. Điểm còn thiếu — giữ sổ cũ, không cấp thêm issue chính

Các mã W-GAP bên dưới chỉ là mục trong đề xuất này để Host xử lý; KHÔNG là sổ thứ hai.

| Mục | Câu bị dừng | Thiếu gì cụ thể | Nguồn và đầu mối xử lý đề nghị |
|---|---|---|---|
| W-GAP-A | Q-B1-02, Q-LAYER-02, Q-CONFIG-01/02 | Có địa chỉ Master Field nhưng chưa có binding truy vấn/metadata theo quyền; bản code live không gọi tìm. | Gắn OPEN-08; Codex xác minh nguồn thật/hợp đồng, Host có quyền task MOW chốt. Backend chưa nối là thiếu sản phẩm, không chặn vẽ phần UI nếu contract được khai rõ. |
| W-GAP-B | Q-B1.1-02, Q-B1.3-01/02, Q-UI-03/04, Q-CONFIG-02/03 | Chưa có đáp án áp dụng cho máy trả dữ kiện nào, màu từ rule nào, lý do/thiếu ngữ cảnh ở đâu; S3 green_rule vẫn mang nghĩa cũ “được dùng”. | Gắn OPEN-04/OPEN-03 và câu gốc liên quan; Host hòa giải theo ranh giới Tìm mới, không tự đổi nghĩa Công thức hay lấy score làm phép Dùng. |
| W-GAP-C | Q-STEP-01/03, Q-B1-03, Q-CHILD-01/04, Config C2/C6/C7 | Thiếu gói kết luận B1; chưa rõ “đã có tập ứng viên phù hợp” hay bắt chọn một mới kết thúc; UI cũ dùng checkbox/receipt demo. | Gắn OPEN-03. Host xác nhận kết quả tìm cần trả trên UI/cho nơi gọi. Không bắt giải B2, không tạo/sửa Field, không tự yêu cầu PG persistence. |
| W-GAP-D | Q-UI-02, Q-TEST-02/04 | Chưa kiểm parity, toàn bộ browser/nhánh sau khi sửa; cổng kiểm toàn UI vẫn PARTIAL. | Gắn OPEN-05/09; Codex kiểm đúng bản sửa. Đây là thực thi/test, không thêm câu gốc hay 1.4. |
| W-GAP-E | R-ANSWER, Q-CONFIG-02, Q-FIELD-03 | Có thể lẫn biến lúc chạy với thiếu định nghĩa; có thể dùng schema/fixture cũ để giả lấp đáp án. | Dùng quy tắc R-ANSWER hiện có và phiếu áp dụng; ghi rõ đã có schema/nguồn, biến lúc chạy, hay thật sự chưa có source/criteria. Không cần thêm câu chung. |

OPEN-10 về yêu cầu tạo bổ sung cũ không được đưa thành điều kiện B1 phải thực hiện Tạo mới mới xong. Nếu giữ hồ sơ đó, ghi rõ phạm vi/đầu ra của bước khác; B1 chỉ kết thúc kết quả tìm. Reviewer không sửa/đóng hồ sơ này.

## 10. Đề xuất đáp án tối thiểu để Codex làm tiếp — CHƯA DUYỆT

Không đề nghị thêm câu/bước. Đề nghị Host hoàn tất **một phiếu đáp án áp dụng MOW001**, dùng ba quyết định nhỏ sau làm bản đề xuất để chốt trong phạm vi thiết kế:

1. **Hợp đồng input/output của UI:** input = yêu cầu/mô tả + filter/phạm vi + phiên yêu cầu. Mỗi candidate trả ID, tên, kiểu/metadata nguồn, mức phù hợp, lý do và phần còn thiếu. Phản hồi có phiên query và phiên rule/nguồn. Các giá trị cụ thể do người nhập/máy cung cấp lúc chạy, UI không tự tính bằng phỏng đoán. Endpoint production chưa có thì dùng adapter/fixture có nhãn minh họa, không báo đã nối.
2. **Đánh giá và hiển thị:** máy kiểm khi có kết quả truy; màu + chữ/lý do hiển thị ngay ở từng kết quả, chi tiết mở khi cần. Màn 1.3 thể hiện đánh giá/kết luận, không ô người tích thay kết luận máy. Pending/chưa đánh giá/lỗi không giả thành Đỏ. Vòng 2 sửa ngữ cảnh/tìm lại, tăng phiên query, vô hiệu hóa đánh giá cũ. Không thêm 1.4, không buộc mọi lần tìm phải qua màn Advanced.
3. **Kết thúc B1:** trả tìm được/chưa tìm được cùng phạm vi, ứng viên và căn cứ của phiên hiện tại; lỗi/chưa đánh giá được hiển thị đúng trạng thái xử lý, không khẳng định không tồn tại. Không tự chuyển sang Dùng/Tạo/Sửa, không buộc backend của bước khác chạy. Đề xuất: xem/chọn candidate chỉ mở chi tiết; không biến thao tác chọn thành bằng chứng phù hợp. Host chốt cụ thể thời điểm/gói kết luận trước khi nghiệm thu thiết kế.

Đây là **đáp án đề xuất** để Host xem, không phải lời Owner hay tiêu chí đã phê duyệt. Không bắt chọn ngưỡng 80/90/100% tùy tiện. Quy trình Config phải tìm/đặt đúng rule theo quyết định hợp lệ; UI nhận kết quả máy và thể hiện chưa cấu hình khi thiếu, không lén dùng default.

**Trình tự ngắn đề nghị cho Codex:** lấy phiếu này đối chiếu nguồn → chốt các đáp án đề xuất còn G vào phiếu áp dụng chính → dựng/sửa UI001 theo đáp án đã chốt → thử các ca hai vòng và kết luận B1 → ghi DOER_CONFIRM + phiếu/bằng chứng thật. Nếu còn thiếu phải giữ G/issue, không tăng 140 câu cho đẹp. MOW002 chỉ xét sau khi 001 và cách làm được nghiệm thu; không triển khai ở lượt này.

## 11. Tự xác nhận và bàn giao

DOER_CONFIRM: PARTIAL
READ_VERSION: repo 69961997bd036c87960462b380f7e840dd7d45fd; S1–S10 tại mục 1.
SCOPE: đi bộ bằng câu hỏi cho ba MOT MOW001; phân biệt đọc/đặc tả, chẩn đoán module và UI sống. Không thực thi Dùng, không tạo Field, không có JEV production.
QUESTION_COVERAGE: trả lời 44 Q_ID áp dụng, 7 tham chiếu Config cho 3 MOT và 24 ô đối chiếu UI legacy; C/R/G/N-A có phạm vi và căn cứ. Không tính đủ câu là đủ kết quả.
BRANCH_COVERAGE: 10 ca chẩn đoán module đã chạy; 3 lần mở trạng thái đầu UI sống. Browser thao tác đầy đủ/parity/JEV thật/đích kết luận mới = chưa kiểm hoặc bị thiếu.
DELIVERED_OUTPUT: file đề xuất này; không cập nhật phiếu S9 hay sổ chuẩn trái quyền. Host có thể nhập các câu trả lời vào đúng phiếu sản phẩm, giữ Q_ID và nguồn; không chép chúng vào danh mục câu hỏi dùng chung.
MISSING_FROM_PROCEDURE: không thấy cần thêm câu gốc hay Bước con để biểu đạt các điểm dừng. Thiếu chính là đáp án áp dụng, hợp đồng search/evaluation/result và kiểm bằng UI thực tế. Chỗ READMEs/legacy chưa đồng nhất cần dùng phạm vi và nguồn mới, không khôi phục Host cũ.
UI_PRODUCT_STATUS: PARTIAL; live search/JEV/đánh giá và kết luận mới chưa có; mô hình xác nhận demo không phải nghiệm thu mục tiêu mới.

**Đề nghị Host:** tiếp nhận hoặc sửa ba đáp án thiết kế ở mục 10, rồi cho Codex làm lượt MOW001 với điểm kiểm “trả lời được trước khi vẽ”. Không cần một vòng mở rộng câu hỏi chung nữa chỉ để trì hoãn ca thực tế; cũng không phê duyệt vẽ hoàn chỉnh khi còn phải đoán dữ kiện gốc.

Phản hồi Host: CHƯA CÓ. Astra Codex quyết định; GPT Chat chỉ gửi phiếu thực hành/đề xuất. Không phát RUN, không tự nghiệm thu thay Host.

Áp: SAME_COMMIT — chỉ việc lưu phiếu đề xuất này, không áp các thay đổi được đề nghị.
