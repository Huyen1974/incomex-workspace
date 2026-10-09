# TQT-PR-20261009-gptchat-v2-technical-ux-06
## Giữ sáu bước; chưa đóng băng v2 vì còn khoảng trống trong cổng thực thi

TQT-PROPOSAL: TQT-PR-20261009-gptchat-v2-technical-ux-06
TARGET: TQT-MODEL-001 v2; check-process-model.py; view.html#tqt-process-model-view; README; TQT-ISS-007.
TESTED: Chạy lại checker hiện hành 83/83 trong snapshot; thêm 13 phép thăm dò; đọc SQL sinh, giao thức transaction, phiếu khai báo và trang sáu ô được render. Không thực thi PostgreSQL, không ghi UI/PG/Directus/runtime.
OBSERVED: v2 tiến bộ và khả thi làm nền. Tuy nhiên vẫn có đường đóng sớm, thiếu bằng chứng nhận cuối, retry không phân biệt nội dung đổi, đáp án lệch đối tượng, chưa có cổng đủ câu hỏi, và thu hồi quyền bị lịch sử chặn. Gói PG còn rủi ro search_path cần xử lý trước staging.
PROPOSED_CHANGE: Giữ sáu ô/159 câu/53 nhóm và các mã nguồn. Hoàn thiện cổng trên chính mô hình, bổ sung ca sai và ca hợp lệ sau thay đổi quyền, rồi dùng cùng bộ ca trên PostgreSQL qua DOT được duyệt. Mặt người chỉ hiện dòng công việc và kết quả; chi tiết máy để phía sau.

## 1. Kết luận cho Host

**Đồng ý giữ NOT_FROZEN và TQT-ISS-007 mở. Không đề nghị làm lại kiến trúc hoặc tăng thêm tầng nghiệp vụ.**

83 ca hiện hành thật sự chạy đạt khi reviewer chạy lại; nhưng đó chưa phải bằng chứng mọi cách sửa trạng thái sai đều bị từ chối. Ngoài các việc Host đã biết là Master/DOT/concurrency/restore, reviewer tái hiện được khoảng trống ngay trên mô hình hiện tại.

Mục tiêu không phải tăng số ca tùy ý. Mỗi luật cần một ca đúng được nhận, một ca sai bị từ chối và một đầu ra người dùng đọc được. Luật nghiệp vụ nhiều hàng phải được giữ ở lớp có quyền thực thi thực sự, không chỉ phụ thuộc runner gọi đúng thứ tự.

### Những điểm ưu tiên

| Mã góp ý | Hiện tượng đã kiểm | Việc cần bổ sung trước khi công nhận chuẩn |
|---|---|---|
| R06-01 | Sau một call trả kết quả và hai phép retest, mô hình nhận run=XONG/issue=CLOSED dù còn 1 step STARTED, 5 step READY. | Kiểm trạng thái cuối theo đường thực thi hợp lệ; không bỏ qua bước bắt buộc hoặc đóng trong khi bước thuộc đường đó còn chạy. |
| R06-02 | Trace sáu bước kết thúc với outbox bàn giao cuối PENDING, attempts=0; không có event nhận sau CLOSE. | Tách đã giải quyết khỏi đã bàn giao có nhận. Việc yêu cầu VHCM/người nhận xác nhận chưa được XONG trước bằng chứng nhận. |
| R06-03 | Một đáp án TARGET đổi sang một Field version hợp lệ khác vẫn được nhận trong cùng target_context_id. Giảm 70 đáp án mẫu còn 5 vẫn nạp được với run STARTED. | Khóa đúng đối tượng/phiên được khai; cổng đủ câu hỏi lấy từ bộ ghép đúng phạm vi, không chỉ đủ bốn nhãn phạm vi hoặc đủ số dòng tự khai. |
| R06-04 | reply('verified') rồi retry reply('rejected') trả cùng event cũ; đổi receiver/return destination trong candidate của idempotent_lookup vẫn nhận call cũ. | Cùng yêu cầu và cùng nội dung thì dùng lại; thay nội dung hoặc đích nghiệp vụ bất biến thì báo conflict, không im lặng coi là retry giống nhau. |
| R06-05 | Thu hồi grant ACK sau một ACK hợp lệ bị từ chối TQT-R-ACK vì toàn lịch sử bị đối chiếu quyền hiện tại. | Quyền tại lúc hành động phải có phiên/bằng chứng; thu hồi quyền cho hành động tương lai không làm sai bản ghi đã hợp lệ trong quá khứ. |
| R06-06 | RETURN có outcome='NOT_A_DEFINED_ROUTE' vẫn được ghi. | Kiểm outcome thuộc hợp đồng/các đường trả hợp lệ của đúng step/callee version trước khi ghi RETURN/apply. |
| R06-07 | 8 hàm PG được sinh không có SET search_path gắn với hàm; có lời gọi và tên bảng không ghi schema. Export chỉ SET LOCAL khi cài gói. | Schema-qualify hoặc pin search_path tin cậy; kiểm bằng phiên DB mới/default search_path. Đây là phân tích mã, chưa phải lỗi đã chạy lại trên PG. |

**Chưa coi việc nạp phiếu thiếu là lỗi tự thân:** phiếu nháp cần được phép thiếu. Khoảng trống R06-03 nằm ở cổng cho bắt đầu/nhận đạt: phải chứng minh đúng tập câu bắt buộc đã được xử lý, thay vì dùng khả năng lưu phiếu làm bằng chứng đủ để chạy.

## 2. Vai trò, phiên nguồn và bằng chứng

Reviewer: GPT Chat theo yêu cầu trực tiếp của Owner. Host hiện hành: Astra Codex, phiên được Owner chỉ định. Đây là đề xuất riêng; không phải phiếu khác hãng/quorum, không phát READY/RUN và không sửa năm file chính của task.

Nguồn được rà: commit v2 Owner dẫn `871115917f97810e84ebcf591eaa884bf581ec6e`; bản ghi kiểm sau đó `6b8ca99126f329c20319b6c54dbb68ad6d7be59d`; snapshot chạy kiểm tại HEAD `538793bc03e75e003168fe7d06198160d366a8c3`. Đã đọc README, §0, các làm rõ mục tiêu 09/10 và proposal05, không dùng giả định Host GPT của lịch sử cũ.

- check-process-model.py SHA256: `699c4497a36d7299049652209e09642a7247c08ef4b2882deaa4f18ef038d9dc`.
- Model canonical SHA256: `f2e5b358eedac180c4f17aa0594f27d687fe145ba4843e82fbba6ee8ec32f471`.
- view.html SHA256: `6a31638541850cb004e6803e0ff1f43bf1324d65ae0ab7378a8edd45b32b2fe1`.
- README SHA256: `8bfaa6a8d92b9b936216be86fccab2ec2aa2ec8400c9c4ea91f131476fee384e`.

Các job read-only snapshot, không thay nguồn:
1. `e3f90f365b9048859dd3ce491fb4a869`: chạy lại CLI --emit-pg/--report/--trace. Exit 0, SIMULATION_ONLY, passed=83, NOT_FROZEN, production_ready=false. SQL/report/trace tại /tmp trong snapshot, không phải artifacts đã nộp lên repo.
2. `2e813703f28c45b59505f978ea5e83a2`: đọc schema 18 bảng, contract/enforcement/protocol/stages/phiếu; exit 0.
3. `afff3956436e4a12a0ccc9f55b729d5a`: 11 phép thăm dò; exit 0. stdout SHA256 `2e6aa56ce317529ee7ed574b61bbde7fc84cbd94162515b96a711e51672035a2`.
4. `b9da2960b8f94e54b2f1cc5cc93eb582`: 2 probe bổ sung, đọc trạng thái bàn giao của trace sáu bước và kiểm source PG function; exit 0. stdout SHA256 `49f6a796268ea85c46af31b6e6c94aae36865b821d2f045a41d702214dc1181c`.
5. ui_inspect tại revision 538793bc, selector #tqt-process-model-view: HTTP 200, console_errors=0. Đọc được sáu ô, nhãn mô phỏng, mã DRAFT, người giữ và trạng thái call. Không lấy kiểm này làm phép thử người mới hiểu trong 30 giây.

Không có phép chạy PostgreSQL, test tải, restart/restore thật, role/DOT binding hoặc ca B3–B7/Field thật trong lần phản biện này. Những mục đó vẫn là điều kiện staging, không báo đã đạt.

## 3. Chi tiết kỹ thuật và tiêu chí kiểm lại

### R06-01 — Có thể kết thúc run khi chưa kết thúc đường thực thi

Thực hiện đúng API mô phỏng hiện có:

```python
s = Simulation(model)
s.ack(); s.reply()
s.retest('SIM-IMPACT-A'); s.retest('SIM-IMPACT-B')
s.close()
```

Kết quả: issue CLOSED, run XONG; chỉ có 1 call. step1 vẫn STARTED, step2…6 vẫn READY. Tình huống này cũng xuất hiện như phép thử closure mức thấp trong bộ hiện hành; chưa có luật phân biệt “đóng một issue hợp lệ” với “run tổng hợp đã hoàn thành đường được chọn”.

Nguyên nhân: Simulation.close() và TQT-R-CLOSE kiểm impacts, quyền, event, run/outcome, active calls/outbox; không kiểm terminal step hoặc đường đi hợp lệ của các step_run. Có thể chuyển run XONG mặc dù bước của chính run vẫn STARTED.

Đề xuất: giữ riêng thao tác đánh dấu issue đã giải quyết và thao tác hoàn tất run. Chỉ hoàn tất run khi các bước bắt buộc của đường thực thi đã kết thúc/được bỏ qua hợp lệ theo edge, không còn việc con cần chờ. Không yêu cầu cả sáu bước phải chạy trong mọi nhánh nếu công thức đã có nhánh bỏ qua; phải có bằng chứng nhánh đó, không đơn giản đếm sáu.

Ca kiểm thêm: đóng ngay bước1 phải bị chặn; đóng khi một step STARTED phải bị chặn; đường reuse hoặc từ chối được phép bỏ qua bước phải kết thúc đúng outcome; không để đóng trước rồi mới “vá” step cuối ở transaction sau.

### R06-02 — Outbox bền vững chưa phải người nhận đã nhận

Trace persisted_workflow hiện cho run XONG, issue CLOSED, close event SIM-EVENT-21. Dòng bàn giao cuối: destination_ref=REF-HOST, state=PENDING, attempts=0; không có event nào sau CLOSE chứng minh đã nhận.

README mục tiêu đã ghi một lần chế tạo phải bàn giao có nhận cho VHCM để kết thúc. Việc có outbox giúp không mất yêu cầu gửi, nhưng không chứng minh đã có ACK của đích. Sáu ACK của các call con cũng không tự thay ACK bàn giao cuối.

Đề xuất: khai receiver/handoff requirement theo từng quy trình; nếu yêu cầu có nhận thì ràng buộc ACK cuối đúng run, phiên kết quả, recipient, correlation và bằng chứng. Có thể lưu “đã giải quyết” trước, nhưng chưa ghi toàn việc XONG/đã bàn giao. Trường hợp tài liệu không cần bàn giao phải N/A có căn cứ. Không tạo trạng thái execution chờ vô hạn mới trái luật chung; giữ trạng thái nghiệp vụ và cơ chế KQ/NEXT_TRIGGER hiện hành.

Ca kiểm: outbox PENDING không đủ; ACK sai người/sai kết quả/sai phiên không đủ; gửi lặp không nhân tác động; chỉ nhận đúng ACK mới đủ hoàn thành. Không ép mọi bản ghi outbox của run đều phải ACK nếu chúng không thuộc bàn giao bắt buộc.

### R06-03 — Phiếu giữ được dữ liệu nhưng chưa khóa đủ nghĩa đối tượng/câu hỏi

Phép thử A: clone một object_def/object_version FIELD hợp lệ, đổi đúng một answer.scope_role=TARGET sang version mới, giữ nguyên declaration.target_context_id, tính lại answer_key. structural/open_db nhận. Trong cùng context SIM-FIELD-SEARCH-PHONE có hai target subject versions: DRAFT-FIELD-PHONE-V1 và SIM-OTHER-FIELD-V1.

Nguyên nhân: validate_contracts và PG guard chỉ so TARGET.kind với declaration.target_type; declaration chưa có khóa đúng target version/set đã khai. Đúng loại FIELD chưa đủ để chứng minh đúng Field đang làm.

Sửa: phiếu phải tham chiếu đúng target version hoặc tập target được công bố; đáp án thuộc chính tập đó. Không áp đặt một đối tượng duy nhất nếu sau này bài toán thật khai nhiều đối tượng, nhưng không cho tự đổi đối tượng mà giữ nguyên context.

Phép thử B: chỉ giữ một answer mỗi scope và các answer được assessment tham chiếu (tổng 5 thay vì 70), đồng bộ declaration.answer_ids. structural/open_db vẫn nhận, run hiện là STARTED. Điều này không phủ nhận roundtrip 70; nó chứng minh roundtrip không phải gate đầy đủ câu hỏi.

Sửa: từ ma trận 159 câu/53 nhóm, chọn đúng tập Q theo Chuỗi/Tầng/Bước/nghiệp vụ và phiên nguồn; lập manifest câu bắt buộc cho lần áp dụng. Trước READY/STARTED hoặc công nhận đủ, đối chiếu theo khóa câu+đối tượng+phạm vi, đáp án có căn cứ/validity/level phù hợp, hoặc N/A đã được duyệt. Không hardcode 70 hay 159 thành số bắt buộc. Cho phép lưu DRAFT thiếu, nhưng thiếu không được tự chuyển bước.

Ca kiểm: thiếu một câu bắt buộc; cùng số lượng nhưng thay câu khác; đáp án đúng Q nhưng sai Field version; N/A không có lý do/quyền; tái dùng đáp án sai source version. Phải có ca đủ thật được chấp nhận.

### R06-04 — Retry phải so nội dung, không chỉ thấy có bản cũ

Simulation.reply('verified') rồi reply('rejected') trả cùng SIM-EVENT-3; output được lưu vẫn là verified, không báo khác payload. Hàm trả sớm khi delivery_state=RETURNED nên không đối chiếu outcome mới.

idempotent_lookup(model, candidate) cũng trả SIM-CALL-001 khi candidate giữ run/callee/request_key/fingerprint nhưng đổi return_step_run_id và receiver_ref. Phép thử này ở helper lookup, không khẳng định đã ghi candidate sai vào DB; hiện helper chưa phân biệt thay đường nhận/trả với retry thuần túy.

Sửa: khóa operation và fingerprint cho request/response cùng envelope nghiệp vụ bất biến. Cùng key + cùng payload và đích nghiệp vụ -> dùng lại; cùng key + thay nội dung/receiver/đường trả -> conflict. Không đưa attempt ID ngẫu nhiên vào khóa theo cách phá retry qua lần thử lại; nếu cho alias attempt mới phải giữ đường trả nghiệp vụ nguyên gốc một cách tường minh.

Ca kiểm: reply cùng nội dung trả cùng event; đổi outcome/evidence/impact_results phải bị từ chối; request đổi receiver hoặc logical return target phải bị từ chối; retry sau commit trước gửi vẫn không nhân call/event/tác động.

### R06-05 — Quyền hiện tại đang làm vô hiệu lịch sử hợp lệ

Sau s.ack() hợp lệ, s.transact(...) đặt enabled=False cho grant ACK bị từ chối với TQT-R-ACK. Đây là thao tác thu hồi cho tương lai, không phải tạo ACK mới không quyền. Model hiện không phân biệt hai tình huống.

TQT-R-ACK/TQT-R-DEPS/TQT-R-CLOSE quét bản ghi lịch sử và đòi grant đang enabled. Vì evidence/event append-only, đổi quyền có thể làm cả mô hình không còn ghi được nếu quyền cũ từng được sử dụng.

Sửa: lưu authorization decision/grant version áp dụng tại event, thời hạn/phạm vi/căn cứ từ actor tin cậy. Kiểm quyền hiện tại cho hành động mới; không yêu cầu quyền cũ phải tồn tại enabled mãi chỉ để lịch sử vẫn hợp lệ. Thu hồi không được xoá lịch sử. Không nhận actor_ref tự khai của worker thay xác thực server.

Ca kiểm: grant không có/đã hết hiệu lực thì ACK mới bị từ chối; thu hồi sau ACK cũ thành công và giữ ACK cũ; RETURN sau thu hồi theo chính sách đã chốt (dừng, đổi người hoặc nhận muộn), không để toàn hệ bị khóa.

### R06-06 — Outcome đúng kiểu string nhưng không có đường nhận

Sau ACK, reply('NOT_A_DEFINED_ROUTE') vẫn được ghi RETURN và output_data. Hợp đồng hiện chỉ yêu cầu outcome là chuỗi không rỗng. Đường chạy sau đó phụ thuộc runner tìm đúng edge; không có cổng bảo đảm mọi RETURN hợp lệ đều có cách xử lý.

Sửa: ràng buộc outcome theo output contract của đúng callee/step/version và đường trả, có nhánh lỗi/không hỗ trợ tường minh. Thực hiện kiểm trong cùng transaction nhận/apply. Nếu chưa biết route thì lưu thông điệp bị từ chối/ghi lỗi đúng chỗ, không coi là kết quả RETURN đã áp thành công.

Ca kiểm: outcome lạ; outcome hợp lệ ở step khác nhưng sai step hiện tại; route nhiều nghĩa; route đúng; mapping thiếu trường hoặc sai kiểu. Không dùng một danh sách outcome chung quá rộng để mọi step đều nhận được mọi kết quả.

### R06-07 — PG search_path và parity chưa được bảo đảm

Nguồn pg_guards sinh 8 CREATE FUNCTION, không có SET search_path ở hàm; body gọi tqt_assert_graph/tqt_canon và các bảng không ghi schema. main chỉ SET LOCAL search_path trong transaction cài gói. Sau commit/ở kết nối mới, SET LOCAL không còn; hàm không mặc nhiên tìm bảng/hàm theo schema nơi nó được tạo.

Đây là phân tích SQL tĩnh có căn cứ PostgreSQL, chưa chạy lại trên PostgreSQL. Không lấy pglast parse thành công làm bằng chứng resolve tên/privilege/trigger chạy đúng.

Sửa: schema-qualify mọi đối tượng sinh và/hoặc pin search_path tin cậy ở từng hàm; không tự bật SECURITY DEFINER để giải quyết quyền. Kịch bản staging phải dùng role DOT thật và connection mới có search_path mặc định/khác, không chỉ gọi trong transaction vừa cài schema.

Điểm parity cần đưa vào cùng đợt kiểm (chưa gọi là lỗi đã tái hiện PG): kiểm edge.mapping ở Python hiện khác phạm vi kiểm SQL; JSON integer trong Python và jsonb_typeof(number) cần mapping rõ khi contract có số nguyên; thứ tự step/edge khi hash, Unicode và canonical JSON phải tương đương; identity/role và quyền schema phải đúng trước khi cấp cho DOT.

Nguồn chính thức đã đối chiếu ngày 09/10/2026:
- PostgreSQL Schemas / search_path: https://www.postgresql.org/docs/17/ddl-schemas.html
- SET / SET LOCAL chỉ tới hết transaction: https://www.postgresql.org/docs/current/sql-set.html
- CREATE FUNCTION / SET và search_path an toàn: https://www.postgresql.org/docs/current/sql-createfunction.html
- Serialization Failure Handling / retry nguyên transaction: https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html

## 4. Những chốt v2 đã tốt — không sửa lùi

Reviewer thử ACK có target_step_run_id NULL, callee_version_id NULL, actor_ref NULL, at NULL hoặc call_id NULL: đều bị từ chối bởi CHECK/NOT NULL/structural. Thử xóa event evidence qua Simulation.transact cũng bị immutable guard chặn. Không đưa giả thuyết NULL-bypass vào danh sách lỗi vì lần này các ca đó đã bị chặn đúng.

Giữ typed/composite FK, tách định nghĩa/phiên/lần/vòng/call/event, fingerprint, khóa đáp án, immutable evidence, rollback candidate và report/trace. Giữ tách schema-only với --include-simulation và trạng thái NOT_FROZEN. Không nhận 70 lượt đáp án mẫu là đáp án nghiệp vụ được duyệt.

## 5. PostgreSQL staging tối thiểu — chưa triển khai trong đề xuất này

Sau khi các khoảng trống mô hình được sửa, Host chốt một phiên PG mục tiêu, một mapping Master hợp lệ và role/actor DOT; chưa cần giải hết toàn bộ Master List.

Chạy trong staging được duyệt qua DOT: cài schema sạch; connection mới/default search_path; nạp phiếu có đúng target/câu hỏi và kiểm schema; chạy bộ đúng/sai tương đương Python; hai phiên tranh nhận một call; đóng so với thêm impact; thu hồi quyền so với reply; cancel so với return; retry toàn transaction khi 40001/40P01; mô phỏng chết sau commit trước dispatch; xác nhận nhận cuối; restore gói vào schema sạch và đối chiếu logic/hash.

Guard toàn đồ thị + advisory lock thô chỉ là nguyên mẫu nhỏ. Không yêu cầu tối ưu ngay để làm phức tạp bản người; trước production phải chuyển sang vùng ảnh hưởng issue/run và đo chi phí theo dữ liệu thật, nhất là deferred trigger gọi toàn graph sau từng row. Không kết luận scalability từ 83 ca nhỏ.

## 6. Phần trình bày: sáu ô là đúng, nội dung ở mặt ngoài vẫn quá kỹ thuật

Đã đọc trực tiếp vùng #tqt-process-model-view trên trang revision 538793bc: sáu tên Phát hiện/Xác minh/Xử lý/Đấu lại/Kiểm nơi phát hiện/Kết thúc đã rõ. Nhưng mỗi ô lặp DRAFT-MOT-GAP-x, OpenAI-main, mô phỏng/chưa đăng ký/chưa chạy; mũi tên hiện Chờ nhận SIM-CALL-001 rồi Chưa khai lần gọi. Bên dưới lại có sáu mục khai báo, mã, mức kiểm và PG. Người đọc phải tự phân biệt bản định nghĩa với một lần chạy mẫu và với bằng chứng 83 ca.

README hiện đưa mô hình PG, contract, 83 ca, 18 bảng, lệnh xuất và gói NOT_FROZEN lên rất sớm; phần chọn tình huống đọc/làm mới ở phía sau. Có nhiều cửa vào cùng lúc: quy trình tổng hợp, ma trận, hướng dẫn cũ và meta-process. Đây là trở ngại cho AI mới xác định phải làm bước nào trước, dù dữ liệu đã có.

### Mặt người đề nghị — giữ nguyên sáu bước và một SSOT

**Phát hiện → Xác minh → Xử lý → Đấu lại → Kiểm tại nơi phát hiện → Đóng**

**Chưa đạt → quay lại đúng chỗ cần sửa.**

Dưới tiêu đề chỉ cần: Việc đang làm / Bước hiện tại / Kết quả cần ra / Vướng gì / Ai làm tiếp. Mỗi ô mặt ngoài: tên hành động và đầu ra một dòng. Ví dụ Phát hiện → phiếu thiếu; Xác minh → dùng lại hay cần sửa/tạo; Đóng → mọi nơi đạt và người nhận đã xác nhận.

Mở ô mới hiện: câu phải trả lời theo đúng ca, đầu vào, người nhận/quyền, thao tác, nguồn đọc/nơi ghi, tiêu chí xong và bằng chứng. ID, table/FK/hash/event/debug dành cho “Chi tiết kỹ thuật”. Không bỏ thông tin kiểm soát; chỉ đưa về đúng tầng đọc.

Phân biệt rõ **Bản quy trình** với **Lần áp dụng**. Đang xem thiết kế thì không nhét các trạng thái của một SIM-CALL như tiến trình thật. Xem mẫu đã chạy thì chọn đúng trace/phiên, có nhãn MÔ PHỎNG rõ một lần ở đầu; không tô xanh production.

### Cửa AI mới đề nghị

README đầu trang cần trả lời ngay bốn câu: tôi phải làm gì; đọc đúng nguồn nào; ghi đầu ra ở đâu; mắc thì gửi cho ai. Một đường duy nhất:

`Mục tiêu/Host hiện hành → khai đúng MOW/MOT/đối tượng/nghiệp vụ → lấy bộ câu áp dụng → làm từng bước → nộp kết quả hoặc chỗ thiếu → Host kiểm/hiệu chỉnh.`

Lệnh chạy checker và mô hình PG để phần kỹ thuật phía sau. Không chép 159 câu sang README hay tạo sổ phụ. Cho AI một ví dụ khai hoàn chỉnh và liên kết tới dữ liệu thật của ví dụ, không chỉ tên schema và lệnh tổng quát.

## 7. Nghiệm thu theo đúng mục tiêu Owner

Chọn một ca nhỏ: một Field thiếu ảnh hưởng hai nơi trong MOW001. Một AI mới không có chat cũ chỉ đọc cửa vào, khai đúng phạm vi, lấy đúng bộ câu, làm đến sản phẩm/bằng chứng thật hoặc xác định chính xác điều kiện đang thiếu; nộp proposal theo quyền. Host sửa nguồn; một phiên mới làm lại.

Tách hai kết luận: (1) đã làm được một lượt rà/hiệu chỉnh và bàn giao báo cáo đúng; (2) mục tiêu sản phẩm Field/UI đã thực sự đạt. Báo BLOCKED đúng là đầu ra hợp lệ của bước rà, không được biến thành sản phẩm hoàn thành. Quy trình chế tạo chưa đủ B3–B7 và nơi nhận thật thì không công nhận end-to-end.

Chính người làm phải xác nhận DOER_CONFIRM kèm phiên nguồn và link sản phẩm, không chỉ Host hoặc checker xác nhận. Mô hình đạt ca đúng/sai nhưng AI không biết bắt đầu/ghi/trả đâu vẫn chưa đạt “đọc là làm được”.

Đề nghị Host xử lý theo thứ tự: R06-01/02/03 trước; R06-04/05/06 cùng bộ negative tests; R06-07 và staging trước đóng băng; rút mặt người/README từ cùng nguồn, sau đó cold-reader test. Không mở task mới hoặc yêu cầu Owner đọc sổ kỹ thuật.

## 8. Mã tái hiện gọn trong snapshot — không dùng PG

```python
import copy, runpy
n = runpy.run_path('check-process-model.py', run_name='review')
m = n['read_model']('view.html')
S = n['Simulation']

# R06-01: hiện còn nhận đóng sớm.
s = S(m); s.ack(); s.reply()
s.retest('SIM-IMPACT-A'); s.retest('SIM-IMPACT-B'); s.close()
print(s.model['rows']['run'][0]['state'])
print([(x['step_id'], x['state']) for x in s.model['rows']['step_run']])

# R06-02: trace đủ sáu bước vẫn chưa có nhận bàn giao cuối.
f = n['persisted_workflow'](m)
close_id = f.model['rows']['issue'][0]['close_event_id']
print([o for o in f.model['rows']['outbox'] if o['event_id'] == close_id])

# R06-04: response retry khác nội dung đang trả im lặng event cũ.
s = S(m); s.ack()
print(s.reply('verified'), s.reply('rejected'))
print(s.model['rows']['call'][0]['output_data'])

# R06-05: thu hồi quyền hiện tại bị event hợp lệ cũ chặn.
s = S(m); s.ack()
def revoke(z):
    for g in z['rows']['grant_scope']:
        if g['permission'] == 'ACK': g['enabled'] = False
try: s.transact(revoke)
except Exception as e: print(type(e).__name__, str(e))

# R06-06: outcome không có nhánh vẫn được ghi.
s = S(m); s.ack(); s.reply('NOT_A_DEFINED_ROUTE')
print(s.model['rows']['call'][0]['output_data'])
```

Mã trên chỉ để tái hiện những gì reviewer đã chạy. File nguồn, SQL trên PG, quyền và sổ chuẩn không được sửa từ proposal. Host quyết tiếp nhận/chỉnh/sắp xếp công việc và cập nhật TQT-ISS-007; proposal này không tự chuyển trạng thái bất kỳ việc nào.
