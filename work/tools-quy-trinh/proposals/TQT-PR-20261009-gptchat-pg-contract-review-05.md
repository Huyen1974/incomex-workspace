# TQT-PR-20261009-gptchat-pg-contract-review-05
## Làm chuẩn ngoài PG: phải chốt cả dữ liệu, ràng buộc và thao tác nguyên tử

TQT-PROPOSAL: TQT-PR-20261009-gptchat-pg-contract-review-05
TARGET: view.html#tqt-process-model (TQT-MODEL-001), check-process-model.py, gói SQL nháp và TQT-ISS-007.
TESTED: Đọc mô hình 15 bảng, code kiểm/xuất SQL; chạy lại checker hiện hành 27/27 trong snapshot; thêm 17 phép thăm dò ca sai và kiểm hợp đồng đầu vào/đầu ra. SQL subset kiểm bằng SQLite đúng cách exporter hiện hành; KHÔNG PostgreSQL, concurrency, tải lớn hoặc Field thật.
OBSERVED: Đã có mã/quan hệ, ba trục kiểm và đường xuất SQL. Tuy nhiên một số luật mới nằm trong hàm Python, một số chưa được cả Python lẫn schema chặn; hợp đồng JSON và phép chiếu phiếu khai báo sang bảng còn cần làm rõ. Có thể nạp đủ cột mà vẫn nhận/đóng sai việc.
PROPOSED_CHANGE: Giữ mô hình/159 câu/sáu ô, sửa hợp đồng và ràng buộc ngay trong SSOT, ánh xạ từng luật sang DB hoặc DOT transaction; dùng cùng ca đúng/ca sai cho checker ngoài PG và đợt staging sau này. Không áp PG từ proposal này.

## 0. Vai trò, nguồn và giới hạn

Ghế: GPT Chat · Vai: Reviewer theo yêu cầu Owner; Host: Astra Codex, phiên Owner chỉ định.
Bước/vòng: góp ý thiết kế sẵn chuyển PG · 0/5; không tự mở/chốt vòng hội đồng hoặc phát READY/RUN.
Scope ghi: CHỈ proposal này. Không sửa README/COLLAB/PROMPT/view/checker, Master, sổ chuẩn, UI sản phẩm, PG/Directus. TQT-ISS-007 tiếp tục là đầu mối của Host; không tạo sổ mới.
Based_on: `8b3c1317b937705f6e6bad8897cefab6a8c36da5`. Trước ghi đối chiếu `f97a84483f578555b04b15c07b8ee3dd53f0c65c`: diff toàn work/tools-quy-trinh rỗng.

Nguồn/hash:
- view.html SHA256 `8eaf89dd4aae01723a4c20cbdc72968d15d8188c3346516271f7e3682fabc179`.
- JSON model canonical SHA256 do checker hiện hành sinh: `a3ce244dd473a71919ba07f723c1c005853fa9f3419007da98a07fba862e0b6d`.
- check-process-model.py SHA256 `f705cf00d538140376aa5ace6c5bfacaf6e17959f7236dc5b6ac28291e32ac85`.
- SQL nháp vừa sinh trong snapshot SHA256 `9950318a72676421175c9a1f63cf6a2e68a26066ac5976c8e6f1550829ac6765`.
- README phiên `8f4cca0da0d80433cc982b5488d61701c99fa7f7267cbe70eb9fdfd63a12ea52`; COLLAB phiên `17f0cb0089c3ec47b32fe8699c1565b5d010cdbd586a49e78579ab95c826694a`.

Bằng chứng thực hiện:
1. Job `cdedf91fc3bb494eb441ae3acc65d50d`, exit 0: chạy lại `python3 check-process-model.py view.html --emit-pg /tmp/tqt-review-draft.sql --report /tmp/tqt-review-report.json`, kết quả `SIMULATION_ONLY`, 27 phép PASS, production_ready=false; đọc toàn schema/rows và SQL sinh. Files /tmp chỉ trong snapshot tạm, không phải file đã lưu lên repo.
2. Job `e1de9d6626984ce9a62568c83c7d2a64`, exit 0: 17 probe reviewer, gọi đúng hàm Python và SQLite constraints; báo ACCEPTED/REJECTED, không gọi đó là PASS production.
3. Job `f25cf40246fc456a8c7d27cd5b8bffef`, exit 0: đối chiếu contract/mapping, payload rỗng và đường lưu phiếu khai báo.
4. Thử ui_inspect URL revision 79fa9e35cc8bf13f77e65b7d951dfa00d74a4179 do Owner cung cấp trả SCREENSHOT_HTTP_FAILED ở môi trường này. Không kết luận website lỗi toàn hệ; lần rà này kết luận từ nguồn repo, mô hình và code, không tái chứng nhận giao diện.

**Kết luận mức độ:** đủ để tiếp tục hoàn thiện bản chuẩn bên ngoài PG, CHƯA đủ để đóng băng thành gói chỉ cần nạp PG rồi vận hành. Đây là nhận xét về thiết kế còn phải bổ sung, không phủ nhận báo cáo 27 phép kiểm trong phạm vi mô phỏng mà Host đã ghi đúng.

## 1. Những gì nên giữ

Giữ 15 bảng quản lý/định nghĩa hiện có làm nền, mã tách định nghĩa→phiên→run→round→step_run→call→event, tách issue và từng impact, level/result/validity, phiếu bốn phạm vi và sáu ô cho Owner. Các bảng quản lý là bản ghi phục vụ MOW/MOT, không tạo thêm tầng nghiệp vụ.

Giữ việc sinh SQL từ cùng SSOT, PK/FK/UNIQUE/CHECK, có index FK và schema draft riêng; giữ DRAFT/SIM chưa phải Master thật. Không tăng câu theo số lượng hoặc chuyển sang T2.5 để giải quyết lỗi cưỡng chế dữ liệu.

Điểm cần nâng cấp: **một luật phải chỉ được dữ liệu nó dùng, nơi cưỡng chế nó và ca sai chứng minh nó thật sự bị chặn.** Có câu mô tả/ID hoặc Python chạy đúng ca mẫu chưa bằng PG/DOT giữ đúng trong mọi đường ghi.

## 2. Các tình huống sai đã thử — không phải danh sách lỗi phỏng đoán

### 2.1. Gọi đúng hàm hiện hành

| Probe | Kết quả thực tế | Đánh giá / cần sửa |
|---|---|---|
| close_issue([], 'RESOLVED', True) | True | Không có nơi/ca được kiểm cũng cho đóng. `all([])` không phải bằng chứng khép kín. Nếu thực sự không áp dụng phải là quyết định khác, không RESOLVED. |
| close_issue(['MET','MET'], 'RESOLVED', False) | True | Nhánh RESOLVED bỏ qua authorized. Phải kiểm thẩm quyền trong thao tác đóng thực; không chỉ ở nhánh NOT_PURSUED. |
| receive_reply với ACK ID không tồn tại và deadline năm 2000, cha STARTED | APPLY_TO_RETURN_STEP | Hàm chỉ kiểm có chuỗi ACK, correlation/version/state; chưa kiểm event thật hoặc thời hạn. SQL FK có thể bắt ACK không tồn tại khi ghi, nhưng helper không chứng minh đã làm điều đó. |
| should_recheck với NA, dependency_complete=True, deps=[] | False | Có thể giữ NA không có căn cứ/duyệt/danh mục phạm vi trong tình huống thử. Phải kiểm NA có lý do, thẩm quyền và điều kiện xét lại. Không yêu cầu chạy lại liên tục khi blocker vẫn còn. |
| production_ready với cả ba danh sách rỗng | True | Cổng all() trên tập rỗng không được công nhận một quy trình sẵn chạy. Cần xác định root cụ thể và closure bắt buộc của nó. |
| production_ready sau gán toàn REGISTERED/APPROVED/verified=True, nhưng Master ref trỏ ACTOR | True | Gán cờ không chứng minh đăng ký Master. Cần kiểm loại/quan hệ Master thật và quyền dùng phiên trong phạm vi gọi. |

Không coi các helper là security boundary hiện hữu. Đây là ca phải có trong bộ chuẩn trước khi chúng được chuyển thành DOT/guard PG.

### 2.2. Nạp ca sai vào SQLite schema do chính mô hình sinh, rồi gọi structural()

| Probe | SQL subset | structural() | Ý nghĩa |
|---|---|---|---|
| issue CLOSED/RESOLVED trong khi hai impact vẫn UNMET | Nhận | Nhận | Điều kiện đóng hiện chưa được nối tới dữ liệu tác động thực. |
| step_def.mot_version_id trỏ phiên MOW | Nhận | Từ chối | Python biết loại; FK hiện chỉ biết phiên có tồn tại. |
| edge.process_version_id khác phiên của from/to step | Nhận | Từ chối | Quan hệ tồn tại chưa đủ; phải cùng phiên quy trình. |
| run.owner_ref trỏ CHAIN thay vì ACTOR | Nhận | Nhận | Reference chung chưa ràng buộc vai nghĩa của từng cột. |
| call trả sang step_run thuộc run khác | Nhận | Từ chối | SQL chưa cưỡng chế cùng run. |
| call trả sang step_run DUNG ở vòng khác trong cùng run | Nhận | Nhận | Cùng run chưa đủ: phải đúng việc/attempt đích còn được nhận hoặc có chính sách nhận muộn. Không mặc định cấm mọi trả khác vòng hợp lệ; cần đích và chính sách cụ thể. |
| một event loại UNRELATED dùng đồng thời làm ACK và RETURN, cùng call/run | Nhận | Nhận | Event tồn tại và cùng call chưa chứng minh đúng loại/đúng actor/trật tự. |
| hai answer cùng question/subject/scope/run/revision, đổi answer_key tự do | Nhận | Nhận | Chưa có khóa nghiệp vụ được kiểm đủ hoặc thuật toán key canonical, nên có thể tạo hai đáp án cạnh tranh. |
| REGISTERED với master_id/master_record_id trỏ REF-HOST | Nhận | Nhận | Cần typed reference + mapping Master, không chỉ FK có row. |
| PASS/CURRENT bị xóa hết dependency | Nhận | Từ chối | Luật phụ thuộc hiện còn ở Python; DB chưa tự giữ. |
| assessment FAIL/CURRENT supersedes PASS/CURRENT nhưng bản cũ vẫn CURRENT | Nhận | Nhận | Chưa có cách chọn kết quả hiện hành theo scope/supersession. Không cấm nhiều bằng chứng độc lập; phải định nghĩa rõ bản nào dùng để quyết định. |

Những dòng SQL subset nhận KHÔNG phải thử PostgreSQL. Tuy nhiên exporter PG dùng cùng danh sách CHECK/UNIQUE và các FK đơn; đọc DDL chưa thấy cơ chế cưỡng chế thay thế cho các luật trên. Vì vậy không thể lấy 27 mô phỏng để kết luận gói PG đã mang đủ invariant.

## 3. Ưu tiên 1 — đưa luật quan hệ vào hợp đồng cưỡng chế, không để trong lời giải thích

Đề nghị thêm vào SSOT một **bảng đối chiếu ràng buộc** (có thể là metadata trong model, không bắt buộc thêm bảng nghiệp vụ PG):

`mã luật | ý nghĩa | bảng/cột/phạm vi | FK/UNIQUE/CHECK hay DOT/trigger/transaction | lỗi trả về | ca hợp lệ | ca phải từ chối`.

Các luật tối thiểu:
- Phiên thuộc đúng định nghĩa; tham chiếu master/actor/rule/question đúng loại, đúng scope.
- step_def thuộc một process version; cả from/to/return của edge thuộc phiên đó.
- step_run thuộc đúng run/round và đúng định nghĩa bước; trả kết quả đúng call và return_step_run đã khai, không tự áp vào bước bị hủy.
- ACK/RETURN thuộc đúng call/run, đúng loại event và chủ thể được phép; trạng thái ACKNOWLEDGED/RETURNED không được dựng từ một event bất kỳ.
- Kết quả kiểm gắn đúng answer revision, subject, run/step scope; dependency/evidence đúng phiên.

**Cách biểu diễn PG đề xuất:** dùng UNIQUE/FK ghép cho quan hệ cùng phạm vi (thí dụ id+process_version_id, id+run_id), typed reference hoặc trigger có kiểm loại; bổ sung cột neo run/phiên ở nơi cần nếu giúp DB kiểm bằng FK. Luật nhiều hàng như đóng issue dùng thao tác DOT nguyên tử/trigger có khóa phù hợp; không nhét truy vấn nhiều bảng vào CHECK rồi coi là an toàn.

PostgreSQL chỉ kiểm CHECK cho row được INSERT/UPDATE; không hỗ trợ dùng CHECK để duy trì ràng buộc đọc dữ liệu khác row. FK ghép là công cụ đúng cho quan hệ nhiều cột. Thiết kế MATCH/NULL rõ cho liên kết đang chờ ACK: chưa nhận có thể null, nhưng đến trạng thái đã nhận thì không được trống hoặc sai phạm vi. Chọn phương án cưỡng chế cụ thể ngay ở bản ngoài PG.

Quyền: nếu luật do DOT giữ thì quyền UPDATE trực tiếp của tài khoản tác nghiệp phải bị hạn chế tương ứng. Một worker có quyền sửa bảng tùy ý có thể đi vòng qua DOT; UI ẩn nút không phải constraint. Chưa sửa roles/PG ở lượt này.

## 4. Ưu tiên 2 — mỗi chỗ nối phải có dữ liệu đủ nghĩa để nạp, không phải JSON hợp lệ là xong

Đã kiểm:
- Sáu step dùng chung một input_contract và một output_contract; chỉ có danh sách `required`, chưa có kiểu/nullable/nguồn ngữ nghĩa cho từng trường.
- Input hiện yêu cầu issue_id, impact_ids, request_key, origin_version.
- Output hiện cam kết issue_id, impact_results, outcome, evidence_id.
- Chín edge không-terminal map issue_id, impact_ids, origin_version. Ví dụ DRAFT-EDGE-1: request_key đích chưa có mapping; impact_ids/origin_version nguồn chưa được output cam kết.
- Thay `call.input_data={}`: structural() và SQL subset đều nhận.

**Đề nghị:** xác định tường minh hai vùng, `envelope` (call ID/request key/phiên/thông tin liên hệ) và `payload` (dữ liệu nghiệp vụ). Một trường lấy từ envelope, input cha, constant đã duyệt hay output trước phải được khai ngay; không để agent tự đoán khi đấu.

Không khẳng định impact_ids/origin_version chắc chắn không có lúc chạy: chúng có thể được kế thừa. Vấn đề là **đường kế thừa chưa được khai để máy kiểm**. Bản chốt cần: tên trường, kiểu/cardinality, nullable, tham chiếu định nghĩa/phiên MOIT/MOUT/Field hoặc schema tương đương có quản lý, source path, target path, phép chuyển, điều kiện lỗi. JSONB chỉ giữ phần mềm dẻo; quan hệ cốt lõi cần dùng làm FK/kiểm quyền/đóng việc không nên chỉ nằm trong chuỗi JSON không kiểm.

Ca phải có: thiếu required; sai kiểu; null thay missing; mapping đọc key không có; schema version khác; output hợp lệ nhưng không đáp ứng input sau; envelope có request_key nhưng payload không cần nhập lại. Phân biệt lỗi hợp đồng với lỗi nguồn thật.

**Ngay ô Phát hiện:** input đang yêu cầu issue_id trong khi phần việc là ghi hồ sơ. Cần chốt caller cấp ID/ghi issue+impact trước khi gọi hay chính step1 tạo; chọn một cách và khai thứ tự transaction. Không tự kết luận deadlock, nhưng không để hai bên đều chờ bên kia tạo mã.

## 5. Ưu tiên 3 — phiếu khai báo bốn phạm vi phải chuyển sang bảng không mất dữ liệu

Mặt người đã có MOW/MOT/target/business; đây là tiến bộ. Nhưng `declaration.required_fields` gồm declaration_id, process_version_id, task_version_id, target_type, target_context_id, chain_id, step_id, business_ids, answer_ids, owner_ref, source_versions, open_issue_ids. Model chưa có quan hệ persisted riêng cho phiếu này; answer chỉ có question_ref/subject_version_id/scope_role/run_id/answer_key/revision/value/source_ref.

Không bắt buộc tạo bảng tên declaration. Yêu cầu là **mọi field của phiếu phải có đích bảng/cột hoặc quan hệ tham chiếu xác định và phép đọc lại tái dựng được phiếu ban đầu**. Không dựa vào agent phân tích chuỗi answer_key để tìm ngữ cảnh.

Đề nghị chốt khóa đáp án theo đúng lần áp dụng: phiên câu hỏi + subject version + vai phạm vi + context nghiệp vụ/đối tượng + run/step hoặc ngữ cảnh khai báo + revision. Cùng mã câu khác phạm vi giữ riêng; cùng phạm vi không có hai đáp án hiện hành tự sinh chỉ vì đổi key. Nếu answer_key dùng làm khóa rút gọn, quy tắc sinh/canonicalization phải được cố định, kiểm collision và gắn các thành phần tường minh.

Lưu ý PostgreSQL UNIQUE mặc định coi NULL khác NULL; nếu có đáp án ở cấp định nghĩa với run_id null, phải chốt uniqueness cho trường hợp đó bằng constraint/index phù hợp phiên PG đã chọn. Đừng giả cùng UNIQUE như có run là đủ.

Cần một phép round-trip: khai phiếu bốn phạm vi → xuất dữ liệu SQL → đọc lại theo các khóa → dựng đúng các scope/đáp án/bằng chứng, không mất context, không tăng bản trùng. Hiện mô hình có một answer minh họa; chưa chứng minh phiếu 70 lượt áp dụng được lưu/khôi phục đầy đủ.

## 6. Ưu tiên 4 — đóng việc bằng bằng chứng và quyền; chạy lại không nhân tác động

### Đóng issue
- RESOLVED cần tập impact được xác định, có ít nhất một impact cần xử lý hoặc một kết luận không áp dụng được duyệt rõ; không lấy all(empty) làm đạt.
- Mọi impact bắt buộc phải có kết quả kiểm MET còn hiệu lực trên đúng nguồn/phiên, đúng ca, bằng chứng và người xác nhận. `goal_result='MET'` tự ghi chưa đủ.
- Người có thẩm quyền đóng và close_rule đúng phiên phải được kiểm cho RESOLVED lẫn NOT_PURSUED. Lưu quyết định/actor/thời điểm/evidence, không chỉ resolution là một chuỗi bất kỳ.
- Đóng issue + kiểm tập impact + ghi event + cập nhật run phải nguyên tử. Khi có impact mới đồng thời: phải bị xét trong transaction hoặc mở lại theo quy tắc; không để một worker đóng trên danh sách cũ rồi rơi mất nơi bị ảnh hưởng.
- Nếu bị từ chối thì kết thúc NOT_PURSUED, mục tiêu của nơi phát hiện không tự đổi MET.

### Call/ACK/RETURN/retry
Giữ UNIQUE(step_run_id,request_key) và correlation riêng. Nhưng cần phân biệt **retry vận chuyển của cùng tác vụ** với **lần xử lý mới sau hiệu chỉnh**. Thay attempt/step_run không được vô tình né khóa chống trùng và tạo Field hai lần. Cần logical operation key có scope/callee/input fingerprint; cùng key khác payload phải bị báo conflict, không trả thành công cũ. Chuẩn key và quyền có thể gắn bằng DOT, không giao agent nhớ.

Nhận RETURN phải kiểm event thật đúng loại, actor, call/run/đích/phiên, trạng thái đích còn nhận, deadline hoặc chính sách nhận muộn, payload hợp đồng. Hai worker cùng nhận/chốt một RETURN chỉ tạo một tác động; kết quả muộn lưu lịch sử nhưng không tự hồi sinh bước bị hủy.

Thiết kế transaction ràng buộc cập nhật trạng thái + event + mục cần gửi ra. Khoảng crash “đã ghi nhưng chưa gửi” và “đã gửi nhưng chưa ghi xác nhận” cần được xử lý bằng outbox/inbox hoặc cơ chế tương đương có bằng chứng; PG transaction riêng không làm thao tác hệ ngoài PG tự động nguyên tử. Đây là cơ chế thực thi, không thêm một tầng nghiệp vụ. Chọn lock/version check/transaction isolation và quy tắc retry cụ thể; không coi việc không trùng UNIQUE trong test đơn luồng là đã kiểm concurrency.

## 7. Ưu tiên 5 — bất biến lịch sử và kết quả hiện hành phải có quy tắc máy đọc được

`object_version` và `assessment` được mô tả bất biến; schema sinh hiện chưa có guard UPDATE/DELETE cho nội dung. Hash chỉ được script tính/so trước khi xuất, không tự ngăn sửa row sau nhập. Không yêu cầu hash SQL phải giống serialization Python một cách tình cờ: ghi rõ thuật toán/canonical body/Unicode/number/ordering, dữ liệu được hash và quy tắc version.

Giữ kết quả kiểm bất biến; lưu invalidation/supersession bằng event hoặc projection hiện hành có ràng buộc. Bằng chứng quá khứ không nên bị ghi đè để đổi FAIL thành PASS; view hiện hành phải chọn đúng assessment theo subject/question/scope/phiên. Nhiều bằng chứng khác loại/người kiểm có thể cùng tồn tại; chỉ tránh hai kết luận cạnh tranh được coi đồng thời là đáp án duy nhất.

Dependency phải trỏ nguồn và phiên thật, biết cả yêu cầu mức kiểm. Thiếu inventory không được giữ xanh. N/A cần lý do/người duyệt/phạm vi, cũng phải xét lại nếu phạm vi đổi. BLOCKED cùng nguyên nhân không cần chạy lại phép thử tốn kém, nhưng việc đánh dấu phụ thuộc/điều kiện đã đổi vẫn phải được xử lý; đừng trộn “không chạy retry” với “bỏ qua invalidation”.

Định nghĩa một lần run dùng phiên bất biến nào, còn “bản mới nhất ngoài hệ” được theo dõi thế nào. Thay định nghĩa tạo phiên mới; run cũ không tự trỏ sang mới. Nếu cho migrate run đang chạy phải có thủ tục mapping/duyệt riêng, không coi đổi FK là xong.

## 8. Gói PG thực sự chuẩn cần nhiều hơn CREATE TABLE + INSERT demo

Gói hiện sinh SQL vào schema riêng, gồm định nghĩa **và** các row SIM ở một file; đúng cho demo. Chưa nên gọi nó là migration production. Đề nghị chốt ngay ngoài PG:

1. **Manifest:** model/schema version, phiên PostgreSQL mục tiêu được xác minh, hash nguồn/xuất, bộ test, expected counts, người duyệt và mapping sang Master/cột hiện hữu. Không tạo kho định nghĩa song song với Master thật.
2. **Phân gói:** schema/ràng buộc/index; definition/config được duyệt; fixture SIM tách riêng; DOT/guard thao tác; kiểm sau nạp. Mã nháp không thành Master chỉ bằng đổi nhãn, có mapping một-một giữ lịch sử.
3. **Ràng buộc và quyền:** bảng rule-to-enforcement mục3; role/privilege/search_path đúng scope; chỉ đường được cấp mới thay phiên/đóng/call. Không mặc định mọi ref có verified=True là đủ.
4. **Dữ liệu chuẩn:** timestamps có offset/time semantics; kiểu số/chuỗi/null, JSON payload schema, ID/uniqueness/namespaces, immutable content và audit/retention. Không ép UUID hoặc identity mới nếu mã chuẩn hiện có đã đáp ứng; quan trọng là không cấp lại và không nhập lẫn SIM.
5. **Cách áp phiên:** precondition/schema fingerprint, migration ID/checksum, một transaction theo gói có ranh giới rõ, cách chạy lại khi mất phản hồi, kiểm trước/sau, rollback/forward-fix đúng loại. Không dùng CREATE IF NOT EXISTS để che schema drift. Không thực thi SQL tay vào PG/Directus; staging/production sau duyệt phải qua DOT.
6. **Phép thử cuối bắt buộc trên PG staging:** cả ca đúng lẫn ca sai và interleaving đồng thời; xuất/nạp/đọc lại round-trip giữ ID/phiên/quan hệ; kiểm driver/JSONB/timestamptz/FK deferred/constraint thực. Tải/lưu lượng/retention đặt theo workload thực và đo; chưa cần đưa toàn hệ production vào chỉ để thử schema.

Không cần chuẩn bị thêm hàng trăm câu hỏi UI. Chốt 6 mục trên trong mô hình/rule/test chính là giảm số lần phải ngồi sửa PG về sau. Phần schema chắc chắn làm được ở ngoài; hành vi riêng PostgreSQL vẫn cần một lượt kiểm staging để xác nhận, không thể chứng minh bằng SQLite.

## 9. Đề nghị trình tự Host xử lý

**A. Sửa ngay ngoài PG:** giữ schema nền/sáu ô, nhận hoặc bác từng gap có lý do; bổ sung rule-to-enforcement, mapping contract/phiếu, close/call guards, effective history và negative tests. Chỉ sửa SSOT, SQL luôn sinh lại.

**B. Áp đúng một mô hình sai/thiếu:** có đủ event SENT→ACK→RETURN→kiểm nơi phát hiện→đóng; ít nhất một nhánh từ chối, một nhánh hủy/quá hạn, retry, hai nơi cùng thiếu; có dữ liệu persisted để đọc lại. Không chỉ cho sẵn danh sách outcome vào walk() rồi kết luận hệ xử lý thật. B3–B7 đang còn tài liệu/danh mục thì ghi đúng dependency, không đóng TQT-ISS-007.

**C. Đóng băng gói thử PG:** toàn bộ ca sai phải bị chặn ở đúng lớp đã khai, không phải fail vì một lỗi FK khác không liên quan. Phép kiểm giữ 27 ca hiện có nhưng bổ sung ca biên này; không đánh đổi một ca đúng để chặn mọi dữ liệu.

**D. Sau đó mới đề nghị staging qua DOT:** đọc lại bằng chứng, test concurrent và restore; chưa đăng ký/triển khai thật nếu còn Master/rule/quyền OPEN. MOW002 không mở trong lượt này.

Mặt Owner giữ nguyên **Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm lại → Kết thúc**. Mỗi ô cho thấy đã chuẩn khai báo/chưa chuẩn, đã kiểm đâu và lỗi nào; không đẩy PK/FK/transaction lên bảng nhìn nhanh. Thêm chi tiết cho AI ở dữ liệu, không thêm bậc nhìn cho Owner.

## 10. Mã tái hiện ngắn cho Host (chỉ snapshot, không PG)

Bên dưới chỉ import checker và dùng SQLite in-memory. Chạy từ work/tools-quy-trinh; kết quả True/ACCEPTED chỉ ra model guard còn thiếu, không phải nghiệm thu.

```python
import copy, importlib.util
spec = importlib.util.spec_from_file_location('checker', 'check-process-model.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
base = m.read_model('view.html')

print('empty impacts:', m.close_issue([], 'RESOLVED', True))
print('no authority:', m.close_issue(['MET', 'MET'], 'RESOLVED', False))

d = copy.deepcopy(base)
d['rows']['issue'][0].update(state='CLOSED', resolution='RESOLVED')
db = m.open_db(d)  # currently succeeds despite UNMET impact rows
m.structural(d)    # currently succeeds too
db.close()

call = dict(base['rows']['call'][0])
call.update(delivery_state='ACKNOWLEDGED', ack_event_id='NO-SUCH-EVENT',
            deadline_at='2000-01-01T00:00:00Z')
print('invalid reply:', m.receive_reply(call, call['correlation_id'],
                                      'STARTED', call['callee_version_id']))

d = copy.deepcopy(base)
d['rows']['call'][0]['input_data'] = {}
db = m.open_db(d)
m.structural(d)  # currently succeeds; input contract not enforced here
db.close()
```

Bộ 17 probe đầy đủ có kết quả tại job e1de9d6626984ce9a62568c83c7d2a64; bảng mục2 là bản lưu trường hợp và expected/observed. Host nên đưa ca đã tiếp nhận vào checker chính, không lấy proposal làm SSOT test song song.

## 11. Căn cứ kỹ thuật chính thức đã đối chiếu

- PostgreSQL Constraints: https://www.postgresql.org/docs/current/ddl-constraints.html — CHECK/NULL, FK nhiều cột, UNIQUE và NULLS NOT DISTINCT, giới hạn CHECK đọc bảng khác. Ưu tiên invariant declarative nơi biểu diễn được; phần còn lại cần guard transactional phù hợp.
- PostgreSQL Transaction Isolation: https://www.postgresql.org/docs/current/transaction-iso.html — đọc/ghi đồng thời phải có isolation/locking và xử lý retry thích hợp; ca tuần tự không chứng minh không race.
- PostgreSQL JSON Types: https://www.postgresql.org/docs/current/datatype-json.html — JSON/JSONB là kiểu lưu trữ dữ liệu JSON; yêu cầu nghiệp vụ/schema bên trong phải khai/kiểm riêng.
- PostgreSQL Privileges: https://www.postgresql.org/docs/current/ddl-priv.html — quyền ghi/gọi phải phù hợp đường cưỡng chế; tài khoản đọc/worker/owner không mặc nhiên giống nhau.

Chỉ dùng những đặc tính nền nêu trên; chưa xác nhận major version PG đích của môi trường hiện hành. Mọi ví dụ giải pháp/schema là đề xuất để Host chốt, không là lệnh SQL chạy trên hệ thống.

## Phản hồi Host

Chưa có. Astra Codex quyết tiếp nhận/sửa/không nhận từng mục, nối vào TQT-ISS-007 và sửa nguồn chính khi được phép. Reviewer không tự cấp mã Master, không đổi thẩm quyền, không phát RUN và không tuyên bố có cổng PG đã chạy.

DOER_CONFIRM của Reviewer: đã đọc, chạy lại bộ 27 và tái hiện các ca sai trong snapshot; chưa chạy PostgreSQL hoặc hoàn tất ca Field thật. Kết luận **DESIGN_REVIEW_PARTIAL / CHƯA SẴN NẠP VẬN HÀNH**, không cần làm lại toàn bộ mô hình.

Áp: SAME_COMMIT — chỉ áp việc lưu góp ý riêng này, chưa áp các thay đổi được đề nghị.
