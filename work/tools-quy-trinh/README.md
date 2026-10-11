# tools-quy-trinh · Cửa vào

**Điểm vào: [Danh sách 39 Master đã đưa vào thiết kế](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-design-review-v1.html).** Đây là danh sách các Master, giữ nguyên bức tranh toàn cảnh. DEF 00.1 · MASTER TIẾN TRÌNH CÔNG VIỆC là dòng đầu, vị trí 0.1; bấm dòng này mới mở trang tiến trình riêng. Không nhúng bảng công việc lên thay danh sách Master. Danh mục toàn hệ thống gồm cả Master chưa thiết kế được quản lý riêng; làm UI đến đâu thì đưa vào danh sách thiết kế đến đó.

DEF 00.1 dùng lại Master có khóa cũ CAT-227*, không tạo Master thứ hai. Hồ sơ chi tiết, việc con, kết quả kiểm và bàn giao nối về mã việc; vòng nâng cấp giữ lịch sử và gắn hồ sơ mới. Tầng của việc, chuyên môn T3, mốc và vòng đời là các trường riêng. Ngày thực tế tách ngày kế hoạch; chưa có phải hiện Chưa ghi. Nguồn tổng hợp duy nhất: `catalog.work_schedule` trong `view.html`; UI đọc nguồn này, không nhập tiến độ hai nơi. Hiện chỉ có 2 việc ghi danh, chưa chứng minh bao phủ toàn hệ thống. Phép chiếu/khóa/quy tắc PG được thiết kế trong `work_schedule.pg_design`, chưa triển khai PG.

**Hồ sơ ngay trong từng việc:** trang Master có thanh riêng “MASTER TIẾN TRÌNH CÔNG VIỆC” dưới “Master Duyệt thiết kế”. Mở tên việc hoặc Chi tiết để xem cùng khung 7 mốc và 11 mục phải ghi. Mốc hiện tại khác mốc đã kiểm đạt. Mỗi nhóm RG01–RG11 tổng hợp những nghĩa vụ thuộc đúng application_id + quy trình/phiên + đối tượng/phiên; số đã ghi, đã đối chiếu và ô Xong lấy từ `tqt-record-control`, cùng quy tắc với Overview. Không chép trạng thái vào hướng dẫn, không dùng hồ sơ MOW001 cho việc khác. Chưa gắn hồ sơ hiện rõ; ghi một phần không được tính là đủ; nhánh chưa phát sinh không tính là lỗi. Ô Xong chỉ đọc, tự tích khi đủ căn cứ, không ghi giả vào trình duyệt. PG chưa nối.

## Over view · đúng hai câu hỏi

**[1. Việc phải qua mốc nào, đang ở đâu?](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=tqt-checkpoint-list)**
**Kiểm đầu vào (1–3) → làm theo quy trình (4) → kiểm đầu ra, duyệt và bàn giao (5–7).** Bảy mốc thuộc quy trình ⑤, chiếu từ 6 MOT; chưa thêm quy trình/tầng. Mốc đang chuẩn bị khác mốc đã kiểm đạt. Bộ 7 mốc đang áp thử, còn chờ hội đồng thống nhất.

**[2. Phải ghi gì, vào Master nào, từng việc đã ghi và đối chiếu chưa?](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=tqt-recording-guide)**

Tách hai bảng, cùng dùng quy trình ⑤:

- **Hướng dẫn chung:** phải ghi gì → tên/mã Master → còn thiếu nơi lưu/UI gì → cách ghi. Dấu **?** giải thích từng cột. Không ghi tiến độ của một việc vào đây.
- **Hồ sơ tiến độ từng việc:** một mã hồ sơ cho mỗi lần làm; từng dòng nối về Master đích và bản ghi cụ thể. **Đã ghi chưa:** Chưa ghi / Đã ghi. **Đối chiếu:** Chưa đối chiếu (xám) / Đã đối chiếu (xanh) / Cần sửa lại (đỏ). Hai cột độc lập; đã ghi vẫn có thể cần sửa.

**Mọi sổ đều là Master List có mã.** Chưa có Master → ghi “Chưa có”, bổ sung Master of Master và thiết kế UI theo UI.MASTER. Có mã nhưng thiếu nơi lưu hoặc UI → hiện đúng phần thiếu. Tài liệu chuẩn bị, phiếu JSON hay liên kết mở được không tự chứng minh đã có bản ghi trong Master.

**Ca MOW001/G1:** đang chuẩn bị mốc 2, **0/7 mốc đã kiểm đạt**. Có 34 nghĩa vụ, chưa gắn bằng chứng bản ghi Master nên hiển thị Chưa ghi / Chưa đối chiếu; không kết luận dữ liệu ngoài hồ sơ không tồn tại. Dữ liệu chuẩn bị vẫn giữ nguyên. Số dòng theo phạm vi từng việc, không cố định 34. Chưa đến mốc/nhánh được chú thích riêng, không coi là lỗi. P01 chuẩn bị được làm ngay; chưa sửa sản phẩm trước xác nhận mốc 3.

**Rà Master ngày 11/10:** dùng lại 11 mã trong **[Master of Master — 86 mục](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-of-master-v1.html)**. Trong phạm vi này: 3 Master chưa khai nơi lưu, 4 nguồn khác chưa xác minh. UI thiếu đã có bản thiết kế list + mẫu khai báo, chưa nghiệm thu. Các nhóm có thể trùng nhau. Đã ghi thiếu và yêu cầu thiết kế vào từng Master cùng `TQT-ISS-007`; ánh xạ đang ở mức thiết kế, chưa chứng minh các Master vận hành được. Danh mục 30 Master định nghĩa là một phạm vi khác, không dùng để đếm toàn hệ thống.

**Cách làm:** đọc mục tiêu → khai đúng việc/phạm vi → lấy quy trình/câu hỏi → liệt kê mọi nơi phải ghi từ đầu vào, đầu ra, kế hoạch và nhánh → kiểm Master và quyền → xác nhận đủ → làm → kiểm → duyệt/bàn giao. Rà từ danh sách phải ghi, không chỉ từ những bản ghi đang có. Thiếu nơi ghi thì giữ người xử lý, quay S5 của ⑤, dùng ②/③; không mở sổ không mã.

**Nguồn:** luật/mốc và hướng dẫn chung ở `view.html → catalog.work_form.record_control`; nghĩa vụ và tiến độ từng việc ở `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24` (`record_requirements`, `record_checks`). Đây là dữ liệu chuẩn bị cho hồ sơ CAT-227*, chưa ghi vào Master vận hành. Overview đọc bản chiếu có kiểm hash; tên/mã Master là snapshot từ Master of Master, phải sinh lại khi nguồn đổi. Không sửa hai nơi hay đổi trạng thái giả trên trình duyệt.

**Hướng PG:** tách quy định theo phiên quy trình; hồ sơ theo lần làm; dòng ghi/đối chiếu theo mã nghĩa vụ; đích bằng mã Master + mã bản ghi + phiên. Đối chiếu đạt cần căn cứ/người/thời điểm; đổi nguồn thì kiểm lại, giữ lịch sử. Các option hiện chỉ đọc từ nguồn, **chưa có API lưu PG**. Bảng/khóa, ánh xạ toàn phiếu, quyền và kiểm đồng thời còn mở tại `TQT-ISS-007`.

**Kiểm Host:** `node check-record-control.js view.html` kiểm 26 ca về tách hướng dẫn/hồ sơ, sai lần/phiên/Master, thiếu dòng, bằng chứng và trạng thái; `python3 check-overview-consistency.py view.html` đối chiếu phiếu nguồn. Các kiểm thiết kế không thay kiểm PG thực tế hay nghiệm thu sản phẩm. PR11 giữ các điểm chưa đủ ở `TQT-ISS-007`.

## MASTER TIẾN TRÌNH CÔNG VIỆC · DEF 00.1

**[Mở tiến trình các việc theo QTTH 05](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/process-work-master-v1.html?master=DEF00.1)**: mỗi dòng là một việc dự kiến, có thứ tự, việc phải xong trước, hồ sơ, mốc hiện tại, chỗ mắc và người tiếp. Dùng lại CAT-227*, không mở Master trùng với sổ hồ sơ. CAT-228* giữ các việc con; CAT-230* là hàng đợi kỹ thuật, không thay lịch trình người dùng.

- MOW001: đã gắn hồ sơ chuẩn bị; mốc/tình trạng lấy từ hồ sơ hiện hữu, không nhập lại.
- MOW002: đứng sau MOW001; chưa triển khai, chưa gắn hồ sơ. Chỉ mở khi MOW001 đạt nghiệm thu thiết kế và có bàn giao, Host xác nhận tiếp tục. Đóng bằng hủy/từ chối không tự mở việc sau.
- Ngày chưa chốt hiện Chưa khai. Làm lại giữ lịch sử hồ sơ; không lấy mã MOW làm thứ tự, không tạo dòng trùng cho mỗi lần thử kỹ thuật.

Nguồn thiết kế: `catalog.work_schedule` (CAT-227*); luật/mẫu UI: `catalog.work_master_designs`. Khóa và phụ thuộc theo mã, không theo tên; kiểm thiếu hồ sơ, sai phiên, trùng mã/thứ tự và vòng phụ thuộc. Dữ liệu này chưa ghi vào PG; ánh xạ bảng/khóa/quyền vẫn thuộc TQT-ISS-007.

**[Khu Master đang rà](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-design-review-v1.html)** bổ sung 9 Master đã có mã, thành 39 mục chọn thiết kế (30 cũ + 9). Master of Master vẫn 86 mục. Mỗi UI mới dùng nguyên UI.MASTER cha, có list và nút Xem mẫu khai báo; mẫu không phải bản ghi đã thực hiện. Không nhập các UI nháp vào danh mục UI con đã duyệt. Kiểm cấu trúc: `node check-work-masters.js view.html` (mã/phiên/hồ sơ/phụ thuộc; 10 ca sai bị chặn). Khi rà UI, chạy thêm với đường dẫn nguồn `process-work-master-v1.js` để kiểm cả 9 cấu hình list/mẫu khai báo.

## Hiện hành · D24/P23 · Host đọc tại COLLAB §0
**5 quy trình tổng hợp + 12 quy trình thành phần.** Host đã chốt **MOW-TH-005 · Từ mục tiêu đến kết quả được nghiệm thu**, phiên `1.1-design`, Chuỗi CTCM `CH-001`, để áp thử thiết kế. Owner giao Host tự quyết; không còn chờ phê duyệt riêng ⑤. Chưa nghiệm thu PG hay tự động hóa.

**Một đường làm:** ⑤ khai việc và hai đầu nối → chuẩn bị/khai nơi ghi/lập kế hoạch → xác nhận đủ điều kiện → làm từng MOT → kiểm sản phẩm và kết nối → duyệt, bàn giao có xác nhận. QT-CTCM-012 lấy/kiểm bộ câu hỏi trong phần chuẩn bị. Sai/thiếu: Tool 008 ghi cùng hồ sơ → ② nhận xử lý → cần sửa hướng dẫn thì ③ → kiểm lại đúng nơi phát hiện. Chưa có người nhận thì người giao vẫn giữ.

[Mở Over view](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view) · [Master Quy trình tổng hợp](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/quy-trinh-tong-hop-master-v1.html) · [Master of Master (86 mục)](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-of-master-v1.html).

**Nguồn duy nhất:** `view.html#tqt-composite-processes.catalog`. 17 MOW có chú giải; 12 thành phần có 50 MOT trỏ về từng hướng dẫn gốc; ⑤ có 6 MOT. Các bước này dùng chung `catalog.trial_contract` (hiển thị tại `#tqt-trial-contract`), không nhân bản câu hỏi hay sổ. Mỗi MOT kế thừa đúng lần làm, đối tượng/phiên, người làm/kiểm/nhận, nơi đọc/ghi, tiêu chí và đích trả. Đây là mã thiết kế, chưa là đăng ký runtime.

⑤ chọn **một** quy trình phù hợp, không chạy tất cả; chỉ dùng tại cửa nhận việc, không gọi đệ quy trong quy trình con. Hướng dẫn từng phần có MOW sở hữu tại `instruction_owners`. Kho câu hỏi, tiêu chí và bằng chứng là nội dung dùng trong quy trình; không tạo loại đối tượng quản lý mới. Không thêm T2.5 hay đổi công thức.

**Nguồn Tool cũ:** hướng dẫn trên `tools-playbook-v1.html` chuyển thành tham chiếu lịch sử; đọc hướng dẫn hiện hành từ Master → Overview. Sổ vấn đề/kết quả sản phẩm vẫn ở nguồn gốc; chưa dời dữ liệu. TQT-ISS-004 theo dõi phần dữ liệu còn lại.

**Phiếu áp dụng:** `../mow-mot-moit-mout/UI-REVIEW-MOW001.json#/application_D24` đã khai 13 mục và kế hoạch cho MOW001/G1. Overview chỉ là bản xem sinh lại từ phiếu, kiểm hash và đối chiếu nội dung; không sửa hai nơi. Mẫu/luật chung thuộc `catalog.work_form` của ⑤. **Bước tiếp:** kiểm điều kiện và đáp án G1, ghi `start_confirmation` trước sửa UI. Chỉ G1 tới nghiệm thu thiết kế, không G2/G3. `issue_register_ref` là nơi ghi bắt buộc; `issue_ref` có thể null nếu không có lỗi mới. Ghi vướng đúng sổ, Host hiệu chỉnh đúng nguồn. Không đợi hoàn thành backend mới thử thiết kế; chưa làm MOW002.

**Giới hạn:** 5 chốt cưỡng chế TQT-ISS-007 và nghiệm thu PG/DOT/quyền/đồng thời/khôi phục vẫn mở. Kết quả kiểm danh mục và mô phỏng không thay nghiệm thu chạy thật.

Kiểm nguồn: `python3 check-overview-consistency.py view.html` → `python3 check-process-catalog.py view.html`; mô hình: `python3 check-process-model.py view.html`. Giữ phiếu/sổ hiện hữu; không mở sổ song song.

## Ý kiến hội đồng · Host kết luận
| Ý kiến | Kết luận hiện hành | Nguồn |
|---|---|---|
| PR-01/02 | Đã tiếp nhận phần câu hỏi/ghép, nguồn hiện có ở ma trận và rules | proposals/ · lịch sử ô3 |
| PR-03 | Đã áp phiếu thử MOW001, chưa nghiệm thu sản phẩm | UI-REVIEW-MOW001.json của task sản phẩm |
| PR-04/05 | Đã tiếp nhận mô hình/khép kín; các chốt còn thiếu giữ TQT-ISS-007 | closure_review / tqt-process-model |
| PR-06 | Sửa retry/schema, còn5 chốt mở | host_review_06 · commit3bc305d |
| PR-07 | C1/C2/C4 tiếp nhận; C3 giữ mức0–4 và thêm điều kiện từng mốc. Mục tiêu2–3 chưa áp | review_07 / checkpoint_policy · P16 |

## Một đường vào cho người/AI mới
Đọc AGENTS.md → COLLAB.md mục tiêu và kiểm soát → [chọn quy trình hiện có](view.html#tqt-process-inventory) → khai MOW/MOT đang làm, đúng đối tượng/phiên và nghiệp vụ → lấy bộ câu hỏi/ghi chú tương ứng → làm từng bước → nộp kết quả, bằng chứng hoặc chỗ thiếu.
Host ghi vào phiếu/sổ hiện hữu của công việc; AI góp ý chỉ tạo proposal theo hướng dẫn bên dưới. Chưa đủ câu/căn cứ hoặc chưa có nơi nhận thì ghi rõ điểm dừng; không tự xác nhận đủ.

## Rà vòng 6 · lịch sử trước khi lập Master riêng
Nguồn quyết định: `tqt-process-model.host_review_06`; theo dõi cùng TQT-ISS-007. **87 ca hiện có đạt nhưng còn 5 chốt chưa kín**: kết thúc đúng đường thực thi; nhận bàn giao cuối; đúng đối tượng và tập câu bắt buộc; quyền tại thời điểm hành động; đường nhận kết quả hợp lệ. Đã sửa retry khác nội dung/đích trong mô phỏng và cố định search_path cho 8 hàm SQL sinh ra; chưa nghiệm thu PG.
Kiểm kê tại `tqt-composite-processes.inventory`: hai bản phác thảo tổng hợp, hai hướng dẫn điều phối cần chốt cách xếp, 9 Tool và 2 khung con. Mã tài liệu/nháp/Tool chưa thay mã Master. Đây là danh mục nguồn, không phải đăng ký mới.
**Ý mục 3 của Owner vẫn là đề xuất:** quy trình/bước tham chiếu câu hỏi dùng chung và chịu trách nhiệm trả lời/kiểm/ghi/đi tiếp; chưa áp quy tắc mỗi nhóm câu phải thành MOW riêng. Sáu vùng chưa nối và ba vùng giao nhau đã ghi tại danh mục; không mở sổ khác.

## Đọc đích trước khi làm
Mục tiêu chuẩn và tiêu chí hoàn thành ở [COLLAB.md §0, ô 1–2](COLLAB.md); trạng thái hiện tại ở Bảng điều khiển cùng file. Đọc mục tiêu Owner hiện hành D25 ngày 10/10 tại đó (thay bản 15 ý cũ): phải có quy trình khép kín, đủ câu hỏi/đáp án và bằng chứng làm theo ra đúng sản phẩm. Ma trận, UI và mô hình dữ liệu là các phần phục vụ mục tiêu này. Chi tiết dưới đây là cách thực hiện và lịch sử; không thay tiêu chí nghiệm thu.

## Mô hình hướng PG · v2 · đang kiểm ngoài PG
[Mặt người vẫn sáu ô](view.html#tqt-mo-hinh-pg). SSOT: JSON `view.html#tqt-process-model` (`TQT-MODEL-001`). Giữ 159 câu/53 nhóm; không thêm tầng nghiệp vụ.

- **Tiếp nhận proposal05:** sửa hợp đồng đầu vào/ra và nguồn cấp từng trường; khóa ghép/đúng loại tham chiếu; kiểm sự kiện nhận/trả, quyền đóng, bằng chứng từng nơi; giữ lịch sử. Luật ở `enforcement` / `contract_enforcement`, cách ghi nguyên tử ở `transaction_protocol`.
- **Lưu và đọc lại:** thêm ba bảng hỗ trợ `declaration`, `grant_scope`, `outbox` vào nền 15 bảng. Phiếu đủ bốn phạm vi, 70 lượt đáp án mẫu; TARGET trỏ Field, PROCESS/TASK trỏ MOW/MOT. Khóa đáp án theo phiếu/câu/đối tượng/phạm vi/phiên trả lời; không dùng mã tự đặt để né trùng. UI xuất phiếu vẫn là nháp, chưa nối thao tác lưu thật.
- **Bằng chứng v2 trước rà vòng 6:** 83 ca nền đạt, gồm lưu–đọc lại 70 đáp án và trace sáu ô. Vòng này thêm 4 ca chặn retry/schema, tổng 87. Những ca này không kiểm đủ 5 chốt đang mở; 70 chỉ là dữ liệu thử lưu, không phải số câu bắt buộc hay đáp án nghiệp vụ đã duyệt.
- **Xuất gói:** `python3 check-process-model.py view.html --emit-pg /tmp/tqt-schema.sql --report /tmp/tqt-report.json --trace /tmp/tqt-trace.json`. Mặc định SQL chỉ có schema, FK/CHECK/UNIQUE, hàm/trigger và view; thêm `--include-simulation` mới có DRAFT/SIM. Report chứa mã ca/hash mô hình/hash SQL; trace chứa các bản ghi vòng thử. SQL sinh ra không là SSOT thứ hai.
- **Cơ chế cưỡng chế dự kiến:** FK ghép cho cùng phiên/lần/vòng và đúng loại; deferred trigger cho luật nhiều hàng; immutable trigger giữ bằng chứng; transaction SERIALIZABLE + state/event/outbox; retry cùng khóa và fingerprint. SQL/8 hàm PL/pgSQL đã kiểm cú pháp bằng pglast 8.5. Chưa chạy SQL này trên PostgreSQL.
- **Gói vẫn NOT_FROZEN:** chưa chốt mã Master/nhóm, phiên PG, vai DOT và ánh xạ actor tin cậy; chưa có adapter DOT/dispatcher/inbox được kiểm. Không cấp quyền worker ghi bảng trực tiếp. DRAFT/SIM không phải mã Master, không được gọi production.
- **Điều kiện kiểm PG:** cùng ca đúng/sai, hai phiên nhận việc đồng thời, đóng so với thêm nơi ảnh hưởng, retry sau mất kết nối, cha hủy/con trả muộn, hash Python–PG và restore nguyên gói. Guard quét toàn mô hình và khóa thô hiện chỉ cho staging nhỏ; trước production phải giới hạn truy vấn/khóa theo issue/run, đo tải/index/retention. Không lấy SQLite hoặc kiểm cú pháp làm bằng chứng PG/concurrency/scale.
- **Việc còn mở:** `package.freeze_requires`, `pg.open` và [TQT-ISS-007](view.html#TQT-ISS-007); chưa đóng ca B3–B7/Field thật. Một lần chế tạo phải bàn giao có nhận cho VHCM để kết thúc; việc thuần tài liệu không cần PG thì khai N/A có căn cứ.

## Khép kín MOW/MOT · bản thiết kế 09/10/2026
- Đọc [bốn chỗ hở và đường thiếu Field](view.html#tqt-khep-kin). Nguồn: `tqt-composite-processes.closure_review`; renderer đọc câu hỏi từ `tqt-question-matrix`, không chép bộ thứ hai.
- **Lịch sử trước Master tổng hợp:** TQT-TH-001 là mã tài liệu. Hiện dùng MOW-TH-001 trong ML-MOW-TH-001; không dùng đoạn lịch sử này để phủ nhận mã thiết kế. Quyền runtime/PG vẫn chưa nghiệm thu; chưa thêm T2.5.
- Ma trận có 159 câu/53 nhóm; thêm 19 câu tại đúng Tầng/MOW/MOT/UI/Test/NTGV. Đây là câu hỏi đang hiệu chỉnh, không phải 159 câu đều áp dụng cho mọi việc hay đã được trả lời.
- Khai báo theo thứ tự, xem quan hệ ra→vào, nguồn đọc/nơi ghi, người nhận và điều kiện đóng. Ghép câu hỏi thành việc con theo đầu vào/ra/trách nhiệm; không sinh một Task cho mỗi câu.
- Phân biệt mức bằng chứng với hiệu lực kết quả, vòng đời định nghĩa với lần áp dụng. Cơ chế chọn phần cần kiểm lại/PG/DOT/JEV mới là thiết kế; chưa có lưu tự động hay chạy nền.
- Hồ sơ theo dõi duy nhất: [TQT-ISS-007](view.html#TQT-ISS-007). Nội dung hồ sơ đọc từ cùng JSON; không đóng chỉ vì hoàn thiện tài liệu. OPEN-10 vẫn thuộc sổ sản phẩm hiện hành.

## List quy trình tổng hợp · xem chi tiết
- [Mở trên hệ thống](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=list-quy-trinh-tong-hop). Thu/xổ theo quy trình → giai đoạn → bước.
- Quy trình đầu: **TQT-TH-001 · Thiết kế - xây dựng một chi tiết/chức năng trong chế tạo cỗ máy**. Nguồn duy nhất là JSON `tqt-composite-processes` trong `view.html`; giao diện và vùng AI đọc cùng dữ liệu.
- Bắt đầu ở quy trình tổng hợp để biết thứ tự, checkpoint và đường quay lại; sau đó mở quy trình con/câu hỏi/ghi chú theo liên kết. Không nhầm 9 bước phối hợp ở đây với B1–B9 của Công thức.
- Mỗi lượt áp dụng lưu bằng chứng/checkpoint trong phiếu sản phẩm hiện có; vấn đề ở sổ của nguồn cần sửa. Phần tổng hợp chỉ dẫn nguồn, không mở sổ mới. Hướng dẫn con mới còn trạng thái cần áp thử.
- Host sửa nguồn sau khi tiếp nhận; người góp ý chỉ nộp riêng. Thêm quy trình tổng hợp sau này vào cùng danh sách, không tạo các bản chuẩn rải rác.

## Ma trận câu hỏi · hiệu lực 08/10/2026
- Host/roster hiện hành chỉ xác định tại [COLLAB.md §0](COLLAB.md); thành viên ngoài Host nộp đề xuất riêng. Không suy ra quyền hiện hành từ quyết định lịch sử.
- Mở trực tiếp [Câu hỏi cơ bản trên hệ thống](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=cau-hoi-co-ban). URL ghi nhớ tab/mục; bước 1.2 dùng section=q-B1-2, mã câu vẫn Q-B1.2-01. Renderer chỉ nhận từ đúng iframe; xem bằng chứng ở COLLAB §0 ô 3.
- Đọc [Câu hỏi cơ bản](view.html#cau-hoi-co-ban) → [Câu hỏi nghiệp vụ](view.html#cau-hoi-nghiep-vu); đọc hàng loạt tại [Ma trận câu hỏi](view.html#ma-tran-cau-hoi).
- **SSOT của bộ câu hỏi mới:** JSON trong `view.html`, script `id="tqt-question-matrix"`. `groups` chứa mã/loại/cha/nguồn; `questions` chứa mã câu, nhóm sở hữu, câu hỏi, trạng thái; `groups[].required_reference` nối câu nguồn bắt buộc ngoài ma trận (Config); ứng viên dùng lại đáp án phải kiểm đúng phạm vi, không tự đánh dấu đủ. `inheritance` quy định câu chung; `rules` giữ quy tắc dùng, tách, kế thừa, ghép và kiểm chứng (hiển thị tại “Cách dùng”/“Cách kiểm sau khi ghép”). AI đọc trực tiếp JSON này; bảng, sơ đồ, bộ ghép và vùng JSON để sao chép đều đọc cùng dữ liệu.
- Host sửa câu hỏi trong JSON, giữ nguyên mã; không sửa chữ tại bản render, không nhân câu hỏi vào từng MOW/MOT. Bước con kế thừa bước lớn và câu chung; thêm câu riêng khi có khác biệt cần kiểm. Thêm nhóm/câu phải kiểm mã duy nhất, cha tồn tại, có câu hỏi, mọi cách xem cùng kết quả.
- Thuật ngữ theo chỉ đạo mới: **chuyên môn = Bước/Tầng/Chuỗi**; **nghiệp vụ = UI/Test/Config…**. Các cách gọi khác ở hồ sơ cũ được giữ để truy nguồn.
- Các nhóm nghiệp vụ khởi đầu: UI, Test/rà UI, Config, Nguyên tắc giao việc (đã được nêu trong mục tiêu Owner); thêm nhóm trong ma trận thì thẻ và bộ ghép tự nhận. Câu hỏi của các nhóm này vẫn là bản khởi tạo.
- Bộ câu hỏi mới là **bản đầu đang hiệu chỉnh**, không phải kết luận đã đủ hoặc đã qua hội đồng. Thành phần Công thức được đối chiếu nguồn; không đồng nghĩa các câu hỏi mới đã được Owner duyệt. Tầng bối cảnh T3–T7 thu gọn; B8/B9 chưa có bước con.
- Nội dung cũ giữ nguyên trong [Quy trình hiện có](view.html#tqt-legacy), liên kết cũ vẫn mở đúng mục. Hướng dẫn hiện hành ở tools-quy-trinh; hồ sơ sản phẩm vẫn giữ tại nguồn gốc. TQT-ISS-004 còn phần kiểm/cắt chuyển dữ liệu sản phẩm.
- Góp ý: file riêng theo mẫu bên dưới, trỏ mã Q/nhóm, nêu chỗ vướng khi làm và câu đề nghị sửa. Chỉ Host quyết định tiếp nhận rồi cập nhật nguồn; không sửa thẳng bốn file chính. Chưa gọi hội đồng trong lượt dựng bản đầu này.


## Ghi chú riêng · đọc trước khi ghép
- Cùng JSON `view.html#tqt-question-matrix` có `note_policy` và `notes`; đây là nguồn duy nhất của quy tắc đặt/ghép ghi chú. Mỗi ghi chú có mã, nơi sở hữu, phạm vi áp dụng, nội dung, nguồn và trạng thái. Host tiếp nhận trước khi dùng như quy định.
- Bấm Bước/Tầng để xem “Ghi chú riêng”; bộ ghép tự lấy mục khớp đúng lựa chọn. Xem toàn bộ dưới Ma trận câu hỏi. MOIT/MOUT cùng T0.5 nhưng không tự dùng chung ghi chú.
- Nội dung chỉ đúng với một MOW/MOT ghi ở phiếu sản phẩm, không biến thành luật chung. Lượt áp dụng hiện hành: [MOW001 · phiếu đáp án, hợp đồng A/B/C và bằng chứng](../mow-mot-moit-mout/UI-REVIEW-MOW001.json), mục hiện hành `application_D24`; `process_trial_20261009` là căn cứ lượt cũ, cần kiểm hiệu lực trước dùng lại. Thứ tự thực hành UI/Config nằm ở notes của nhóm nghiệp vụ.
- Khi thêm ghi chú: kiểm mã/owner/phạm vi tồn tại; kiểm cả ca khớp và ca không khớp; không có ghi chú không đồng nghĩa đã rà đủ. Thay nguồn vẫn phải cập nhật bằng chứng tại phiếu áp dụng.

## 0. ĐỌC NGAY — DÀNH CHO MỌI AI (kể cả khi vừa bị từ chối ghi)

**Host duy nhất của task hiện hành:** đọc `Host/Host_ID/Host_Surface` tại [COLLAB.md §0](COLLAB.md). README chỉ dẫn nguồn quyền, không duy trì danh tính Host thứ hai. Mục tiêu và tiêu chí xong chỉ ở [COLLAB.md §0](COLLAB.md); phải đọc `../../AGENTS.md` và §0 trước khi thực thi.

**Chọn đúng tình huống:**

1. **Muốn dùng quy trình để làm thật:** đọc [Quy trình hiệu chỉnh hướng dẫn và quy trình](view.html#quy-trinh-hieu-chinh) nếu đang xây/sửa quy trình; nếu đang rà UI, đọc [Rà một UI · 6 bước](view.html#ra-ui). Thực hiện theo bước, lưu **sản phẩm/bằng chứng thực tế** tại task sản phẩm được phép ghi. Không đạt → ghi đúng chỗ thiếu, không tự tô PASS.
2. **Thành viên ngoài Host muốn sửa quy trình hoặc sổ TQT:** **KHÔNG** sửa trực tiếp `view.html`, `COLLAB.md`, `README.md` hay hồ sơ trên trang. Tạo **một file đề xuất riêng** `work/tools-quy-trinh/proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md`, tên không trùng; Host đọc → duyệt → chỉ Host nhập vào nguồn chính rồi kiểm lại.
3. **Bị từ chối ghi, VERSION_CONFLICT hoặc không rõ quyền:** **DỪNG sửa nguồn đích**; đọc lại file README **`work/tools-quy-trinh/README.md`**, đối chiếu quyền và mẫu bên dưới; chuyển sang nộp đề xuất riêng, không retry cùng lệnh/bypass/ép push. Nếu ngay cả đường tạo đề xuất bị chặn, báo Host mã lỗi + đường dẫn + thời điểm; không tự mở đường khác.

### Xác nhận của người thực hiện — bắt buộc trước khi Host công nhận quy trình đạt

Bộ 8 câu/MOT và 7 câu Config **đã nằm ở** [“Rà một UI”](view.html#ra-ui); không viết lại bộ câu ở đây. Mỗi lần rà một UI, Codex/agent phải có câu trả lời + bằng chứng hoặc ghi rõ BLOCKED/NOT_TESTED/N-A kèm lý do cho **mọi câu áp dụng**, mọi nhánh bắt buộc và việc bàn giao.

Cuối lượt, **chính AI đã làm** ghi xác nhận tại phiếu được giao; thành viên ngoài Host nộp góp ý quy trình qua proposal, không sửa nguồn chuẩn. Host theo quyền tại COLLAB §0.

```text
DOER_CONFIRM: YES | NO | PARTIAL     # Tôi đọc từ đầu, không được giải thích thêm, có hoàn tất quy trình RÀ SOÁT trong phạm vi giao không?
READ_VERSION: <commit/phiên bản README + #ra-ui + URL/phiên bản UI>
SCOPE: <MOT/màn nào, phần nào N-A hoặc chưa được phép thử>
QUESTION_COVERAGE: <Q1-Q8/MOT và 7 Config: đủ câu trả lời + chứng cứ hoặc lý do còn thiếu>
BRANCH_COVERAGE: <nhánh và ca: PASS/FAIL/BLOCKED/NOT_TESTED/N-A + lý do>
DELIVERED_OUTPUT: <đường dẫn phiếu kiểm, số ca, mã sổ, bằng chứng đọc lại; thiếu thì ghi CHƯA CÓ>
MISSING_FROM_PROCEDURE: <đúng câu/bước/đường dẫn/định nghĩa xong cần thêm, hoặc KHÔNG>
UI_PRODUCT_STATUS: <PASS|FAIL|BLOCKED|PARTIAL>  # Kết quả sản phẩm UI, TÁCH với việc làm được quy trình rà
```

**Quy tắc đọc kết luận:** `DOER_CONFIRM=YES` chỉ khi agent tự đi hết hướng dẫn và **bàn giao được phiếu rà soát đầy đủ phạm vi** mà không phải hỏi cách làm; UI đang lỗi vẫn có thể được kết luận `BLOCKED/FAIL` **nếu đã phát hiện, đối chiếu nguồn, ghi bằng chứng và hồ sơ đúng**. Nếu mới thử vài ca, chưa phủ hết câu hỏi/nhánh hoặc không tìm được nơi lưu thì `PARTIAL/NO`, **không** dùng 5 ca đạt để kết luận cả quy trình. Host chỉ công nhận bản hướng dẫn sau xác nhận của người làm **và** kiểm được kết quả thật; khi thiếu câu/bước, ghi vào hồ sơ TQT-ISS-003, sửa theo vòng TQT-QT-001 và cho phiên mới thử lại.

**Khuôn đề xuất 6 dòng (không cần viết báo cáo dài):**

```text
TQT-PROPOSAL: <mã duy nhất / tên file>
TARGET: <TQT-QT-001 hoặc TOOL-CTCM-xxx / mã sổ + bước>
TESTED: <ai đã đọc và làm / phiên nguồn / đầu ra thật / link evidence>
BLOCKER_TYPE: <THIEU_HUONG_DAN | THIEU_SAN_PHAM | THIEU_QUYET_DINH | THIEU_QUYEN | LOI_QUY_TRINH>
OBSERVED: <đọc hướng dẫn nào, làm đến bước nào, kết quả thực tế và đúng ra phải là gì>
PROPOSED_CHANGE: <thêm/sửa đúng câu, bước, nhánh, kiểm chứng lại thế nào>
```

Nếu **thiếu chức năng sản phẩm** (ví dụ chưa có nguồn Field thật/JEV) thì nêu `THIEU_SAN_PHAM` và mã issue sản phẩm, **không** viết hướng dẫn giả rằng đã có. Host phân loại trước khi sửa.

### Quyền ghi & phản hồi khi bị chặn (TQT_GATE_V1)

| Vai trò | Được ghi | Không được ghi |
|---|---|---|
| Host đúng phiên/bề mặt được ghi tại COLLAB §0 | Nội dung chuẩn/sổ/README trong task sau khi duyệt và kiểm bằng version | Không tự sửa runtime MOW/VPS ngoài phạm vi |
| Mọi AI ngoài phiên Host đã chỉ định | File đề xuất **riêng** trong `proposals/`; bằng chứng sản phẩm ở task được giao | 3 file chuẩn và sổ TQT trên trang |
| Owner | Góp ý/đề xuất trực tiếp bằng chat; Host ghi lên repo | Không bị yêu cầu thao tác Git/Markdown |

**Hiệu lực:** quy định vai trò và đường nộp đề xuất **đã áp dụng**; cổng từ chối ghi theo danh tính kỹ thuật **CHƯA ĐƯỢC XÁC MINH** (TQT-ISS-006). Github đang khóa push thường theo ruleset `gateway-only-writes`, nhưng gateway có DeployKey chung: **không có nghĩa** mọi AI khác đã bị chặn path.

**Yêu cầu kỹ thuật để hoàn thiện TQT-ISS-006, chưa giả là máy đã làm:** gateway phải xác thực **đúng phiên/bề mặt được Owner giao làm Host** bằng identity server-side, không tin chuỗi tự khai trong commit và không chỉ so chuỗi Host_ID tự khai (có thể dùng chung nhiều bề mặt). Khi AI khác cố ghi các file chuẩn, trả `HOST_APPROVAL_REQUIRED`, kèm `readme_path=work/tools-quy-trinh/README.md` và `allowed_proposal_path=work/tools-quy-trinh/proposals/TQT-PR-...`; thử được ca từ chối main, cho phép proposal và Host duyệt nhập/kiểm. Nếu lỗi do nguồn bận/xung đột thì trả lỗi thật, không ngụy thành đã bị chặn quyền.

**Không thay luật toàn repo.** Quy ước này chỉ dành cho `work/tools-quy-trinh`. Sổ `OPEN-01…10` ở MOW vẫn sửa tại nguồn MOW tới khi hoàn tất chuyển nguồn TQT-ISS-004.

---
Đọc `../../AGENTS.md` → [§0/Bảng điều khiển](COLLAB.md) trước; lấy mục tiêu, tiêu chí, Host/roster và việc kế tiếp từ đó.

## Mở đúng nội dung

| Cần làm gì | Nguồn phải đọc |
|---|---|
| Owner xem task | [Over view — bức tranh chung](https://vps.incomexsaigoncorp.vn/knowledge/modules?task=tools-quy-trinh&view=content&section=over-view) |
| Nhìn nhanh có gì, thiếu gì, tắc ở đâu | [Phiếu đủ/thiếu trên Overview](view.html#tqt-work-board) |
| Nhận diện phạm vi, lớp và nhóm chuyên môn | [Cách phân loại](view.html#phan-loai) |
| Tổ chức câu hỏi từ gốc, ghép với nghiệp vụ | [Ma trận câu hỏi](view.html#ma-tran-cau-hoi) · [Phạm vi Host hiện hành](PROMPT.md); ý kiến ngoài Host gửi riêng |
| Owner cùng xây dựng quy trình hiệu chỉnh | [Quy trình hiệu chỉnh hướng dẫn và quy trình · TQT-QT-001](view.html#quy-trinh-hieu-chinh) — MOW-TH-003, có bước duyệt/công bố/kiểm nơi dùng/ngừng bản cũ |
| Rà UI đang có, viết ca và lưu kết quả | [Hướng dẫn thực hành](view.html#ra-ui) → 8 câu/MOT, 7 câu Config, khuôn ca, nơi ghi và kiểm lại |
| Đọc đủ 9 Tools, từng bước/câu hỏi | [9 Tool · một khuôn](view.html#tool-9) — hướng dẫn hiện hành; bản cũ tại VPS giữ lịch sử |
| Luật dùng chung: công thức, xong khi, đi tới đích, sửa hay ghi sổ, Tool→DOT | [Dùng chung](view.html#dung-chung) |
| Xem áp thử MOW-NHC-001 và các lượt chạy | [Áp thử](view.html#ap-thu) · [Sổ lượt chạy](view.html#so-luot-chay) |
| Nguồn cũ đã chép, nơi đang gọi, cách cắt chuyển | [Chuyển nguồn](view.html#chuyen-nguon) → mở bản cũ tại VPS |
| Ghi/kiểm vấn đề của tools-quy-trinh | [Sổ vấn đề](view.html#so-van-de) — TQT sửa ở đây; OPEN là bản chép, trạng thái hiện hành ở sổ MOW tới khi cắt chuyển |
| Đọc vấn đề và kết quả MOW đã có | [Sổ MOW / Tools](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#issue-register) · [Kết quả từng lượt](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tools-playbook-v1.html#tools-run-register) |
| AI ngoài Host gửi đề xuất sửa quy trình/sổ | Tạo file **riêng** `proposals/TQT-PR-YYYYMMDD-<seat>-<so>.md` gồm mã Tool/vấn đề, ca làm thật, câu/bước cần sửa, đề xuất và bằng chứng; **không sửa** `view.html`/`COLLAB.md`/`README.md` |
| Host duyệt và nhập chuẩn | [TQT-HOST-GATE](COLLAB.md) · Host đối chiếu, chấp thuận/từ chối và cập nhật một nguồn, kiểm kết quả; chưa có chốt chặn quyền máy riêng, theo TQT-ISS-006 |
| Đọc cách góp ý / việc bị tắc | [Cách góp ý](view.html#gop-y) · gửi theo file đề xuất nêu trên, không viết trực tiếp vào sổ chuẩn |
| Tiếp nhận thêm nguồn | Đọc TQT-SOURCES và TQT-REQ trong COLLAB; giữ mã/nguồn/hợp đồng hiện hành |

`view.html` là HTML chính duy nhất. Mục tiêu/tiêu chí/trạng thái điều hành nằm trong COLLAB; sổ vấn đề của task nằm trong `view.html#so-van-de`. Mỗi nội dung có đúng một nơi cập nhật.

Artifact/quy trình được bổ sung về sau phải đăng ký tại đây hoặc danh mục chuẩn được công bố trong task, để phiên tiếp theo biết lúc nào đọc và dùng.
