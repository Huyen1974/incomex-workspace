# COLLAB — MMIM Lane C · Human Step / UI

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** — Owner 28/09/2026 yêu cầu Lane C trả lời dần hai câu: có bao nhiêu Step con người cần làm và bao nhiêu UI unique cần tương tác.

### 1. Mục tiêu
Suy Human Step và UI từ Process/Model đã có, không liệt kê tùy ý; đối chiếu UI xanh/thực tế đã làm.

### 2. Thế nào là hoàn thành
C01 chỉ làm **MOW**: từ MOW.* + CHUNG.* được gọi, suy ra Human Step candidate và UI candidate; phân biệt instance với canonical; chưa sửa CAT-004/UI catalog.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- SSOT Process: `../ban-duyet.html#ml5-cho-ai`.
- Step canonical hiện tại: CAT-004; UI canonical + 16 UI xanh là evidence.
- 470 requirements của MOM04 = evidence inventory, **không phải Step/UI count**.
- Kết quả C01 là working evidence; Host/Owner mới hợp nhất canonical.
- KQ mới nhất: **C01 DỪNG chốt unique** · 6/6 process · 25 instance/candidate chưa gộp · U_MOW/UI_MISSING UNKNOWN · chi tiết KQ C01 dưới đây.
- HOST GATE · PASS · PROCESS=`VEUI.MOW` · catalog=`ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7` · prompt=`34b8873f02cf60603487f06cc0be43fe084b7b572eda91df348cfff56549520a`.
- READY@8794c1fa9c868db731a6e1b9d4b99dad56e56c53 · RUN_ID `MMIM-LANE-C01-20260928-01`.
- RUN ISSUED · chỉ lane-c/COLLAB được ghi; canonical parent + VPS UI READ-ONLY; XONG/DỪNG rồi dừng.
- C02 HOST GATE · PASS · PROCESS=`VEUI.MOW` · prompt=`261aa3164e345c3658c287713671f8ce4a52dd7c9276b674726d19e8f2c0652d`.
- READY@f95b2211777c56bc9a288ae1e302ac76a35fdb49 · RUN_ID `MMIM-LANE-C02-20260928-01`.
- RUN ISSUED · song song A05/B03; chỉ lane-c/COLLAB, canonical parent + VPS UI READ-ONLY.
- C02 D74 RE-GATE · PASS · prompt=`f7d12de568042f39f4806bc60adc3a94e6640b792b97abd4dcba9d44486f636b`.
- READY@1bd42c508d18fb747a0aeeb16f16886d18edec9a · RUN_ID `MMIM-LANE-C02-20260928-01` · **SUPERSEDES READY f95b...**.

### Vòng trước
A01 đã PASS P0/process gate. Lane C mở sau D59, bắt đầu từ MOW vì phức tạp nhất.

## Codex · KQ C01 · MMIM-LANE-C01-20260928-01 · 28/09/2026

**DỪNG chốt số unique — đã lập evidence C01; cần B/A bổ sung contract trước khi gộp.**

- MOW process đã đi: **6/6**; 7 CHUNG được gọi; chỉ đọc thêm MOT.CHAY vì MOW.CHAY gọi thật.
- Human Step instances: **25** = 8 + 2 + 3 + 6 + 2 + 4; gồm 1 duyệt có điều kiện và 3 bước runtime thừa kế.
- H_MOW: **25 hồ sơ candidate chưa gộp**; số loại Human Step canonical đã chứng minh = **UNKNOWN**.
- UI routes đã mở: **9**; U_MOW (UI unique theo chữ ký) = **UNKNOWN**.
- UI_MISSING (UI thật sự thiếu, khác gap label/config/đấu nối) = **UNKNOWN**.
- OPEN: chữ ký quyền/state/return · duyệt ý/bản/config/ngừng · picker/chỗ gắn · config/bật/phạm vi · lượt chạy thật.
- NEXT: **B/A chốt contract MOW về quyền, trạng thái và điểm quay về cho các nhóm đang OPEN.**

<details>
<summary>Chi tiết C01 · nguồn, 25 instance/candidate, Step → UI, JEV và phần cần trả B/A</summary>

### Phạm vi và bằng chứng đầu vào

- Executor_Surface: **Codex desktop**. Write_Path: **workspace_* root=workspace**. Chỉ ghi `work/mow-mot-moit-mout/lane-c/COLLAB.md`; canonical parent và VPS `ui` READ-ONLY.
- Đọc AGENTS → COLLAB cha (§0, D36/D46/D56–D59, D60, Live Contract, MOM04 KQ) → COLLAB lane → PROMPT; README technical contract cho đường ghi. A0 ĐÃ XÁC NHẬN; RUN của Owner khớp.
- READY `8794c1fa9c868db731a6e1b9d4b99dad56e56c53` đúng commit cuối chạm lane-c/PROMPT, kiểm bằng workspace_log trước phân tích và trước ghi. Prompt SHA256 `34b8873f02cf60603487f06cc0be43fe084b7b572eda91df348cfff56549520a`.
- Process gate đã chạy đúng lệnh PROMPT trong snapshot cô lập: job `5585f909cc524e19a39e5c66dc0aac60`, source_head `a64e26fef286b44242677b86e5982151aeb9ce05`, exit=0, stderr rỗng, **PASS / VEUI.MOW / reason=OK / process_count=39 / step_count=8**. stdout SHA256 `c99d20f2adf51485a38990c1b57b02c45da07f14c3394309bee4d5d7bac72cb5`; step_count=8 là số khối của VEUI.MOW, không phải H_MOW.
- Snapshot chốt trước ghi: HEAD `c54b35f953e722502bd1cfd535b74a5bd7d5a7c4`, fresh/recheck_required=false. Ban-duyet SHA256 `ba8096abf853e721f460c990667a59db379ccc9aca8347aa16dade4f1601a4a7`; COLLAB cha `4f68f65b5a260d25718e3c3f0b58fc441bcb8e6fca49b22419e7bba6ad04f80f`; hai nguồn không đổi trong lượt dù HEAD chuyển do công việc khác.
- Nguồn process: [ml5-cho-ai](../ban-duyet.html#ml5-cho-ai), L365–368; 6 MOW + CHUNG.TIM/NEU/DUYET/CAPMA/KIEM/BAT/NGUNG. MOT.CHAY đọc vì MOW.CHAY gọi thật; không phân tích thêm authoring MOT/FORM/FIELD. VEUI.MOW là process áp dụng cho C01; không cộng các bước Nhà máy VEUI vào H sử dụng MOW.
- Canonical đối chiếu: [CAT-004](../ban-duyet.html#ml3-11) L171 (workflow_steps 105, không phải 105 loại Human Step); [chuẩn cha](../ban-duyet.html#parent-ui-standards) L98; child directory L103; [MOW references](../ban-duyet.html#mom-step-group-MOW) L105; MOM UI references L122. Bảy MOW reference cũ đều OPEN, chưa là canonical Step đã nghiệm thu.
- MOM04 KQ cha L1054–1134 + D58: **16 UI xanh / 470 requirements / 5 pilot**, MOW 212 requirements, loop 8 Step/10 UI/20 CF **tham chiếu**. Không dùng các số này hoặc “MOW 6 UI có nguồn” ở catalog cũ làm Step/UI unique count. MOW xanh được giữ = **UI-005/001/004**.

### Quy tắc đếm

“Instance” ở đây là **một vị trí thao tác người trong call graph**, mở rộng call CHUNG và dependency MOT.CHAY một lần cho mỗi caller; không phải số lần một người thực hiện trong sản xuất. Nhánh duyệt KHAI có điều kiện vẫn được giữ để không mất khả năng; khi nhánh đó không chạy có 24 vị trí. Tệp/bình luận là một khối người theo nguồn, không bắt người bình luận mỗi lượt. Lặp MOT theo số bước MOW, retry, số chữ ký, số bản ghi và số nơi dùng không được nhân vào C01.

Không tách một khối chỉ vì có nhiều fields; không tự thêm thao tác nhập form ngoài khối Lưu/gửi của MOT.CHAY. Machine blocks ghi ở bảng riêng và không cộng H. Số 1–25 dưới đây **chỉ là số dòng tham chiếu nội bộ của evidence C01**, không cấp mã Step/UI mới.

### Human Step instance table

| Process / một lần đi call graph | Human instances theo thứ tự | n |
|---|---|---:|
| MOW.TAO | 1 Tìm → 2 Nêu nhu cầu → 3 Duyệt ý → 4 Khai MOW → 5 Xếp bước → 6 Nối bước → 7 Duyệt bản → 8 Bật | 8 |
| MOW.LAP | 9 Tìm → 10 Gắn vào cha | 2 |
| MOW.KHAI | 11 Cấu hình nơi chạy → 12 Duyệt cấu hình **nếu nguyên tắc yêu cầu** → 13 Bật | 3 |
| MOW.SUA | 14 Nêu nhu cầu → 15 Duyệt ý sửa → 16 Khai clone MOW → 17 Duyệt bản sửa → 18 Áp tất cả/chỉ nơi này → 19 Bật | 6 |
| MOW.XOA | 20 Nêu nhu cầu ngừng → 21 Duyệt ngừng; phần ngừng/lưu trữ sau đó là máy | 2 |
| MOW.CHAY | 22 Nhận/mở form → 23 Lưu/gửi → 24 Tệp/bình luận (ba bước từ **MOT.CHAY**) → 25 Theo dõi lượt (MOW) | 4 |
| **Tổng** | 8 trực tiếp MOW + 14 tại CHUNG được gọi + 3 runtime thừa kế | **25** |

### Machine Step instance blocks — loại khỏi H

| Caller | Machine blocks / call được loại khỏi H |
|---|---|
| MOW.TAO | NEU cấp mã nhu cầu; DUYET tạo phiếu/chọn người (hai lần); AI phác thảo; khóa gói; CAPMA; KIEM/nhánh lỗi; BAT tự sinh dùng ở đâu. |
| MOW.LAP | Kiểm bản/quyền; tự sinh dùng ở đâu. |
| MOW.KHAI | DUYET tạo phiếu/chọn người nếu cần; BAT tự sinh dùng ở đâu. |
| MOW.SUA | NEU cấp mã; xem ảnh hưởng; DUYET tạo phiếu hai lần; clone bản mới; KIEM/nhánh lỗi; BAT cập nhật dùng ở đâu. |
| MOW.XOA | NEU cấp mã; DUYET tạo phiếu; NGUNG kiểm nơi dùng/lượt, ngừng/lưu trữ. Không có H xác nhận xóa thật trong nguồn. |
| MOW.CHAY → MOT.CHAY | Trigger, mở lượt; giao/báo việc; ghi nghiệp vụ/đọc lại/event; bàn giao/retry/sự cố; rẽ nhánh/nhắc/leo thang/kết thúc-hỏng. |

### Canonical Human Step candidate table

Giữ **25 hồ sơ chưa gộp** để trace đủ instance. **Đây không phải khẳng định có 25 loại Human Step unique.** Chưa có cặp nào đủ bằng chứng bằng nhau cả `intent + input người + output + state transition + quyền + điểm quay về`. Thiếu quyền/return không được coi là giá trị bằng nhau. Trạng thái mô tả bên dưới chỉ là cách đọc intent/thứ tự nguồn; tên trạng thái, commit và quyền thật vẫn OPEN.

| # | Instance / intent | Input người | Output / nơi ghi | State theo nguồn hoặc suy từ thứ tự | Quyền | Điểm tiếp tục thành công* |
|---:|---|---|---|---|---|---|
| 1 | TAO / TIM · Tìm phần đã có | Tên/nghĩa/nhãn | Kết quả tìm; chỉ đọc 01/61/20/64/48 | Chưa tìm → đã có kết quả; không ghi | OPEN · NT05 chưa bind vai cụ thể | NEU |
| 2 | TAO / NEU · Nêu nhu cầu tạo | Một dòng nhu cầu; thảo luận AI nếu có | Nhu cầu 39/72; máy cấp mã 02 | Nhu cầu tạo được nêu | OPEN · NT05 chưa bind vai cụ thể | DUYET ý |
| 3 | TAO / DUYET ý · Cho phép tạo/phác thảo | Duyệt hoặc trả + lý do; phiếu từ máy | Quyết định 42/73; đọc 41 | Phiếu ý → duyệt/trả; trạng thái MOW OPEN | OPEN · NT03 chọn người duyệt | AI phác thảo |
| 4 | TAO / Khai · Khai MOW mới | Tên/loại/neo T2 | 09/46/49/64; đọc 21/22 | Nháp mới → có khai báo | OPEN · NT05 chưa bind vai cụ thể | Xếp bước |
| 5 | TAO / Xếp · Chọn/xếp MOT hoặc quy trình con | Thành phần và vị trí bước | 11; đọc 08/09 | Nháp → có danh sách bước | OPEN · NT05 chưa bind vai cụ thể | Nối bước |
| 6 | TAO / Nối · Nối các bước | Trước/sau, song song, hội tụ, điều kiện | 12; đọc 31 | Bước → có quan hệ phụ thuộc | OPEN · NT05 chưa bind vai cụ thể | Máy khóa gói |
| 7 | TAO / DUYET bản · Cho phép phát hành bản tạo | Duyệt/trả + lý do trên bản đã kiểm | 42/73; đọc 41 | Phiếu bản → duyệt/trả; không tự bật | OPEN · NT03 chọn người duyệt | BAT |
| 8 | TAO / BAT · Bật bản tạo đã duyệt | Nơi/lúc/tham số | 47/71/49; máy sinh 48 | Chỗ dùng → bật; điều kiện cụ thể OPEN | OPEN · NT05 chưa bind vai cụ thể | Kết thúc TAO |
| 9 | LAP / TIM · Tìm bản dùng lại | Tên/nghĩa/nhãn | Kết quả tìm; chỉ đọc 01/61/20/64/48 | Chưa tìm → đã có kết quả; không ghi | OPEN · NT05 chưa bind vai cụ thể | Máy kiểm bản/quyền |
| 10 | LAP / Gắn · Gắn bản có rồi vào cha | Cha/chỗ gắn/bản chọn; schema OPEN | 11/15/49 | Bản có rồi → có chỗ gắn | OPEN · NT05 chưa bind vai cụ thể | Máy sinh dùng ở đâu |
| 11 | KHAI / Config · Cấu hình chỗ dùng | Trigger, khuôn↔đơn vị, kho, kích hoạt, nhánh, quyền | 47/15/16/30/75; đọc 17/18/22/31/32/33 | Chỗ dùng → cấu hình; rule duyệt OPEN | OPEN · NT05 chưa bind vai cụ thể | DUYET nếu cần, nếu không BAT |
| 12 | KHAI / DUYET config · Duyệt cấu hình có điều kiện | Duyệt/trả + lý do | 42/73; đọc 41 | Phiếu config → duyệt/trả | OPEN · NT03 chọn người duyệt | BAT |
| 13 | KHAI / BAT · Bật chỗ dùng đã cấu hình | Nơi/lúc/tham số | 47/71/49; máy sinh 48 | Cấu hình → bật; điều kiện cụ thể OPEN | OPEN · NT05 chưa bind vai cụ thể | Kết thúc KHAI |
| 14 | SUA / NEU · Nêu nhu cầu sửa | Một dòng nhu cầu | 39/72; máy cấp mã 02 | Nhu cầu sửa được nêu | OPEN · NT05 chưa bind vai cụ thể | Máy xem ảnh hưởng |
| 15 | SUA / DUYET ý · Cho phép sửa/clone | Duyệt/trả + lý do; có ảnh hưởng | 42/73; đọc 41 | Phiếu ý sửa → duyệt/trả | OPEN · NT03 chọn người duyệt | Máy clone bản mới |
| 16 | SUA / Khai · Khai clone MOW | Tên/loại/neo T2 | 09/46/49/64; đọc 21/22 | Clone mới → khai bản sửa | OPEN · NT05 chưa bind vai cụ thể | KIEM |
| 17 | SUA / DUYET bản · Duyệt bản sửa đã kiểm | Duyệt/trả + lý do | 42/73; đọc 41 | Phiếu bản sửa → duyệt/trả; chưa áp nơi dùng | OPEN · NT03 chọn người duyệt | Chọn phạm vi NT19 |
| 18 | SUA / Phạm vi · Chọn nơi nhận bản mới | Tất cả/chỉ nơi này | 30; context nơi dùng OPEN | Bản sửa → lựa chọn phạm vi áp | OPEN · NT05 chưa bind vai cụ thể | BAT |
| 19 | SUA / BAT · Bật bản sửa theo phạm vi | Nơi/lúc/tham số | 47/71/49; máy sinh 48 | Phạm vi đã chọn → bật; OPEN | OPEN · NT05 chưa bind vai cụ thể | Kết thúc SUA |
| 20 | XOA / NEU · Nêu nhu cầu ngừng | Một dòng nhu cầu | 39/72; máy cấp mã 02 | Nhu cầu ngừng được nêu | OPEN · NT05 chưa bind vai cụ thể | DUYET ngừng |
| 21 | XOA / DUYET · Cho phép ngừng/lưu trữ | Duyệt/trả + lý do | 42/73; đọc 41 | Phiếu ngừng → duyệt/trả; chưa ngừng | OPEN · NT03 chọn người duyệt | NGUNG kiểm nơi dùng/lượt rồi ngừng |
| 22 | CHAY → MOT.CHAY / Mở · Nhận và mở đúng việc | Chọn/nhận việc, đúng bản ghi/form | Không ghi; đọc 06/14/10/54 | Việc được giao → mở để làm; state thật OPEN | OPEN · NT05 chưa bind vai cụ thể | Lưu/gửi trong bước MOT |
| 23 | CHAY → MOT.CHAY / Gửi · Gửi kết quả việc | Kết quả/form; schema tùy MOT | 63/52/54; máy mới ghi nghiệp vụ 18→ | Thao tác gửi → máy ghi/đọc lại rồi chuyển; state thật OPEN | OPEN · NT05 chưa bind vai cụ thể | Máy ghi nghiệp vụ/đọc lại |
| 24 | CHAY → MOT.CHAY / Tệp · Bổ sung tệp/bình luận | Tệp hoặc bình luận theo context việc | 74/73 | Có bổ sung bằng chứng; trạng thái bước OPEN | OPEN · NT05 chưa bind vai cụ thể | Máy bàn giao sản phẩm |
| 25 | CHAY / Theo dõi · Theo dõi lượt MOW | Chọn lượt/ngữ cảnh; dữ liệu có sẵn không nhập lại | Không ghi; đọc 57/69/70 | Chỉ quan sát; không tự đổi run | OPEN · NT05 chưa bind vai cụ thể | Caller lượt hiện tại; máy kết thúc/hỏng |

\* Cột cuối là **bước kế tiếp thành công suy từ mũi tên nguồn**, chưa phải contract picker/duyệt/hủy/lỗi “quay về đúng chỗ gọi”. NT03 chọn người duyệt và NT05 phân quyền là luật chung, chưa bind vai của từng instance. Mọi bước có ghi còn phải đọc sổ Tool 35/37 theo ml5; C01 không thực hiện các ghi này.

Những khác biệt đủ để không gộp trực tiếp: duyệt ý ≠ duyệt bản ≠ duyệt cấu hình ≠ duyệt ngừng về đối tượng/ủy quyền/state; khai nháp mới ở TAO tiếp Xếp bước, khai clone ở SUA tiếp KIEM. Không mở rộng bước SUA để tự thêm Xếp/Nối vốn chưa được process SUA khai rõ; trả B/A nếu cần bổ sung.

### Step → UI mapping

**Chọn cha trước; route, child/config và UI unique là ba thứ khác nhau.** UI-005 Thường/Đề xuất là mode variant; UI-009 là drawer cùng Master; UI-011/012 là trang evidence phụ trợ. 9 routes đã mở dùng 8 mã child catalog hiện hữu; UI-005 có hai mode trong tập này. Các mã child và mode vẫn không phải số UI unique. “Chỉ hai view Kanban/Master” không có nghĩa người chỉ có hai interaction phải học: Config/Review/Workspace còn cần chữ ký riêng. Cùng cha chưa đủ gộp; khác query/nhãn cũng chưa đủ tách.

| Candidate # | Chữ ký UI cần kiểm (cha · dữ liệu người · hành động · state) | UI/route thừa kế | Kết luận C01 |
|---|---|---|---|
| 1, 9 | UI.MASTER · truy vấn · tìm/chọn · kết quả hiện/chọn trả caller | UI-029 và bộ lọc UI-001 | Có khung tìm/đường Quay lại. Chưa có picker commit-result/permission. **Hai Human Step chưa gộp; không đếm hai query thành hai UI unique.** |
| 2, 14, 20 | UI.MASTER/UI.CANVAS · một dòng nhu cầu · gửi · nhu cầu chờ xử lý | UI-004 Sổ góp ý + UI-005 Đề xuất | Xanh có neo/vòng đời góp ý; nguồn MOM ghi UI-004 chưa đủ nhu cầu chung. Không suy góp ý = nhu cầu tạo/sửa/ngừng. Config/label hay thiếu UI thật: **OPEN**. |
| 3, 7, 12, 15, 17, 21 | UI.REVIEW · quyết định/lý do + đối tượng duyệt · duyệt/trả · state riêng từng ý/bản/config/ngừng | UI-009 detail của UI-001; UI-011 checkpoint phụ trợ | Có vùng 3 câu hỏi và evidence; UI thật đang “Bản xem chỉ đọc”, chưa chứng minh phiếu + thao tác duyệt/trả đúng quyền. Không gọi UI-003 NTGV là phiếu duyệt MOW. |
| 4, 16 | UI.CANVAS · tên/loại/neo · lưu khai báo · nháp mới/clone → khai báo | UI-005 Đề xuất; UI-001 bút sửa/detail | Candidate hiện hữu, chưa kiểm commit/ngữ cảnh phiên bản. Cùng fields chưa đủ gộp state; không tạo UI mới. |
| 5 | UI.CANVAS · MOT/quy trình con/thứ tự · xếp/gắn · bước trong nháp | UI-005; UI-009 bảng bước | Có cấu trúc để kế thừa; edit/chọn bản/đường trả chưa chứng minh. |
| 6 | UI.CANVAS · cạnh/điều kiện · nối · relation trong bản nháp | UI-005; UI-009 bảng bước + UI-011 R04 | R04 chờ step_dependency thật; không suy bảng xem = editor nối đã đủ. |
| 10 | UI.MASTER picker hoặc UI.CANVAS config · bản/cha/chỗ gắn · chọn-gắn · quan hệ được lưu | UI-029 tìm + UI-001/UI-005 caller | **OPEN** picker trả mã/bản/quyền/chỗ gắn. Chưa kết luận cần UI unique mới. |
| 11 | UI.CONFIG · trigger/kho/quyền/nhánh · lưu config · chỗ dùng có cấu hình | UI-005 đề xuất/UI-009 candidate; chuẩn UI.CONFIG tham khảo | Chuẩn Config đã có; không suy New MODT đã thực hiện MOW.KHAI. Trường/state riêng và rule duyệt cần B/A bind. |
| 8, 13, 19 | UI.CONFIG · nơi/lúc/tham số · bật · chỗ dùng được bật | Candidate cùng cha UI.CONFIG trong MOW; UI-001 status chỉ là hiển thị | Có nguyên tắc thừa kế, chưa chứng minh bật đúng nơi/bản/rights. Không thêm màn “Bật” riêng chỉ từ tên bước. |
| 18 | UI.CONFIG · tất cả/chỉ nơi này + ảnh hưởng · áp bản · các chỗ dùng đổi bản | UI-005/UI-009 candidate, NT19 | Chưa có evidence chọn phạm vi và kết quả áp. Thiếu config hay thiếu UI thật: **OPEN**. |
| 22 | UI.WORKSPACE · chọn việc · mở đúng form · assigned → mở | UI-010 MOT dashboard được MOW.CHAY gọi | Đã mở mock MOT-2599; form và ngữ cảnh hiện rõ. Chưa có test binding bản ghi/quyền thật. |
| 23 | UI.WORKSPACE · kết quả form · lưu/gửi · submitted → máy ghi/đọc lại | Cùng UI-010, form nhúng | Có required 0/2 và nút Hoàn thành disabled. Không nhập/lưu; chưa nghiệm thu chống trùng/lưu/đọc lại. Không mở thêm scope authoring FORM. |
| 24 | UI.WORKSPACE · tệp/bình luận · bổ sung · evidence được gắn đúng step_run | UI-010 candidate; UI-004 chỉ thừa kế cơ chế neo góp ý | Nguồn process có thao tác; route đang mở chưa chứng minh attachment/comment gắn đúng lượt. Không đánh đồng bình luận với góp ý cải tiến. |
| 25 | UI.CANVAS/UI.MASTER · chọn lượt · xem · chỉ đọc run/step_run | UI-005 Vận hành / UI-012 Dữ liệu & sự kiện | UI-012 tự nói là cấu trúc/danh mục sự kiện mẫu, **chưa phải nhật ký thực tế**. UI theo dõi lượt đúng data/quyền vẫn OPEN. |

Bảng này là các **vùng cần kiểm chữ ký**, không phải 14 UI unique hay 14 UI phải làm mới. Chưa phân định chắc “cùng cha + label/config” với “thật sự thiếu UI”; vì vậy **U_MOW=UNKNOWN, UI_MISSING=UNKNOWN**, không gán 0, 9 routes, 3 UI xanh, 10 references hoặc 25 Human instances để lấp số.

### UI thật đã đọc — 9 routes

| Entry | Route đã mở bằng CUA | Evidence chỉ đọc |
|---|---|---|
| UI-005 | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=thuong) | Thẻ T2, T7→T0, Thường/Đề xuất/Vận hành; mock; chỉ xem. |
| UI-001 | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html) | 7 quy trình mẫu; filters, 3 vai, edit/detail/help; không thao tác ghi. |
| UI-004 | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-gopy-list-v1.html) | 8 góp ý mẫu/4 mới; neo bước-lượt; vòng đời; chưa nối bảng. |
| UI-009 (detail UI-001) | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html?chi-tiet=WF-0001) | 3 câu hỏi; bản xem chỉ đọc; CHƯA PHÁT HÀNH 1/14. |
| UI-005 (mode variant) | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=de-xuat) | Đề xuất/+ chèn/đề xuất cải tiến; không nhập hay gửi. |
| UI-010 (dependency runtime) | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-dashboard-v1.html?cong-viec=MOT-2599) | Đúng ngữ cảnh task; form nhúng/required 0/2; Hoàn thành disabled. |
| UI-029 | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/tim-kiem-chung-v1.html?scope=MOW&return=%2Fui-preview%2Fmcp-writes%2Fmow-unified-canvas-v2.html%3Ftang%3DT2%26che-do%3Dthuong) | Khung search + link Quay lại đúng caller; chưa nối dữ liệu/quyền. |
| UI-012 (attachment) | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-nhap2-data-events.html?quy-trinh=WF-0001) | Dữ liệu/event schema mẫu; link về chi tiết; không phải event log thật. |
| UI-011 (attachment) | [Mở nguồn](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-nhap2-checkpoints.html?quy-trinh=WF-0001) | 1/14 bằng chứng mẫu; R04/R11/R12/R14 chờ nguồn; link về chi tiết. |

Không nhập/gửi/lưu, đổi tình trạng góp ý, bật, duyệt hay mutation bất kỳ UI. CUA chỉ mở trang/đọc mode, menu, detail; một click mở vùng đề xuất không xác nhận editor đã đủ. “Xanh” ở MOM04 là baseline thiết kế cần kế thừa, không phải chứng cứ operation/PG runtime đạt.

Hash HTML VPS kiểm mới C01: UI-005 `e73db99920aff75895682845ca11ea482eeb750a5b9789634b556e29b263a022`; UI-001 `8dcf620905672af8812b4671899a7286d892b60dc01e839b8d71175fe8cacda4`; UI-004 `1a94f9447787025ba64fd05cad806e511d6f796fa2dc91219d8fa08fed4a78e1`; UI-010 `9afc417c98b71a5db5bd2f626e875210cba5b1eb0d838993e0e5a7c0bcabd129`; UI-029 `dad49ca6caf2cf6778857b990eb87df48f1e15c7c807e9b74ecd8dc6a975e63c`; UI-011 `5ba439827ca71b41ed0cb1585ac0f40ba80faa20d6ce137356e364924601377b`; UI-012 `0f8e91c622b018fb61893eb2155199d1c33602237fd79042b0649645b4fc0cfe`. Hash file shell không đại diện toàn bộ JS/data renderer; browser evidence ghi riêng ở bảng.

### OPEN / ambiguous và JEV

JEV skill dùng cho **năm nhóm merge mơ hồ**; không dùng JEV để đếm, để viết bảng hay để vượt missing evidence. State gửi source text + call sites + rule sáu phần, không gài kết luận mong muốn. Result `gen-dec-1790542602-duWBqzoO9HfKYaheST79`, model trả về `typesafe/jev-1.13-20260917`:

| Nhóm | Dòng | Choice JEV / xác suất / confidence | Quyết định evidence C01 |
|---|---|---|---|
| TIM tạo/lắp | 1, 9 | SEPARATE 0.50; OPEN 0.49; MERGE 0.01; confidence 0.26 | OPEN, giữ riêng; search route có Quay lại nhưng chưa có chosen-result/rights/return contract. |
| NEU tạo/sửa/ngừng | 2, 14, 20 | SEPARATE 0.59; OPEN 0.41; MERGE 0; confidence 0.39 | Giữ riêng theo caller/state; output nhu cầu+mã giống chưa đủ. |
| Duyệt ý tạo/sửa | 3, 15 | OPEN 0.67; SEPARATE 0.33; MERGE 0; confidence 0.51 | OPEN, giữ riêng; quyền và return chưa bind. |
| Duyệt bản tạo/sửa | 7, 17 | SEPARATE 0.60; OPEN 0.40; MERGE 0; confidence 0.39 | Giữ riêng: sau duyệt TAO bật, SUA còn chọn phạm vi. |
| BAT tạo/khai/sửa | 8, 13, 19 | OPEN 0.61; SEPARATE 0.39; MERGE 0; confidence 0.41 | OPEN, giữ riêng; cần effective rights/state/return của chỗ dùng. |

JEV confidence thấp/vừa, không chứng minh canonical và không tự cấp quyền. Khai MOW 4/16 và các loại duyệt khác nhau có khác state/điểm tiếp tục ngay trong nguồn, không gọi JEV cho việc exact rule đã trả lời.

**Năm OPEN cần trả đúng nơi:**

1. **Contract gộp — B/A:** bind state trước/sau, vai/quyền và return thành công/trả/hủy/lỗi cho năm nhóm trên; giữ mã process. H_MOW chưa được chốt unique trước khi có các trường này.
2. **Duyệt/bật/phạm vi — B/A:** DUYET ý/bản/config/ngừng và điều kiện KHAI cần rule cụ thể; NT19 cần bản/nơi dùng/ảnh hưởng; UI review chỉ đọc không thay operation. Không tự sửa CAT-003/CAT-004/UI.
3. **Chọn/gắn/xếp/nối — B/A trước, C sau:** picker trả mã+bản đúng cha/chỗ gắn; R04 cần relation thực. CHUNG.TIM tìm chưa tự có nghĩa “chọn và commit vào caller”.
4. **Thừa kế UI — Host/C:** baseline xanh có khuôn, nhưng input/action/state phải được đối chiếu khi contract đã rõ; phân biệt thiếu label/config/đấu nối với thiếu UI unique. Chưa có căn cứ số UI_MISSING.
5. **Runtime — B/A:** MOW.CHAY theo run thật, dependency MOT.CHAY đúng form/bản ghi/quyền, gửi/lưu/đọc lại, tệp/bình luận; UI-012 là schema/event mẫu, R11/R12/R14 chờ nguồn. Không nghiệm thu operation bằng màu xanh thiết kế.

### Kết quả và NEXT

**DỪNG ở việc chốt H/UI unique**, vì thiếu các phần bắt buộc của chữ ký process và chưa phân định thiếu UI hay thiếu cấu hình. Phân tích 6/6, 25 hồ sơ, mapping và JEV đã ghi để B/A/Host tiếp tục từ bằng chứng này; không làm C02 và không hợp nhất canonical. Không tạo file/phần mềm/UI mới. Áp: SAME_COMMIT.

NEXT duy nhất: **B/A chốt contract MOW về quyền, trạng thái và điểm quay về cho các nhóm đang OPEN.**

</details>

KQ@MMIM-LANE-C01-20260928-01 DỪNG
KQ@LANE-C C01 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · HEAD=c54b35f953e722502bd1cfd535b74a5bd7d5a7c4 · H_MOW=25 · U_MOW=UNKNOWN · UI_MISSING=UNKNOWN · NEXT=B/A chốt contract MOW về quyền, trạng thái và điểm quay về cho các nhóm đang OPEN.

H_MOW=25 ở tín hiệu trên = pool candidate chưa gộp; **H unique đã chứng minh UNKNOWN**. Hai UNKNOWN thay số vì thiếu evidence; không tạo số giả để khớp khuôn `<n>`. HEAD là snapshot nguồn trước commit KQ; commit áp KQ lấy từ Git history.

## C02 · chốt Human Step theo contract-v1; rà UI duy nhất

RUN MMIM-LANE-C02-20260928-01 · PROCESS VEUI.MOW. Gate PASS bằng dot-process-gate (39 process, 8 step; prompt SHA f7d12de5; catalog SHA 78b4a687). Registry CODEX-MMIM-C đúng RUN/target. B02R1 ánh xạ 25/25 instance của C01 vào 15 direct step-key; 12 process contract-v1 trong ban-duyet.html#ml5-cho-ai còn nguyên SHA 78b4a6879e8881bb26d67dcf3af6ec29e49abbc6c2032ec3b097105b1ae7e868 tại lần đối chiếu. Không suy bước người từ metadata List của A04.

### H_MOW = 15

Mỗi dòng là chữ ký sáu phần theo thứ tự: intent; input người; output; chuyển trạng thái; lớp quyền; điểm quay về. “Cao · CV1” là độ tin cho contract-v1 ở ban-duyet.html#ml5-cho-ai, đối chiếu map B02R1 trong lane-b/COLLAB; không phải xác nhận đã vận hành hay bind người cụ thể theo NT03/NT05. Số trong ngoặc là instance C01; cùng step-key ở nhiều caller nhận tham số caller_context/subject/place nhưng giữ cùng kiểu chữ ký.

| Human Step chuẩn / instance | Chữ ký sáu phần | Nguồn/tin cậy |
|---|---|---|
| CHUNG.TIM.S01 (1, 9) | SEARCH; catalog/object/query/scope; FOUND_EXACT/CANDIDATES/NOT_FOUND/SEARCH_INCOMPLETE + coverage; SEARCH_REQUESTED→SEARCH_RESULT; REQUESTER; CALLER | CV1 · cao |
| CHUNG.NEU.S01 (2, 14, 20) | REQUEST; need_text/target/caller_context; NEED_RECORDED (máy cấp need_code tiếp); NEED_UNSTATED→NEED_RECORDED; REQUESTER; CHUNG.NEU.S02→CALLER | CV1 · cao |
| CHUNG.DUYET.S02 (3, 7, 12, 15, 17, 21) | REVIEW; subject/version/decision_context + quyết định/lý do; APPROVED hoặc RETURNED + record; REVIEW_PENDING→APPROVED/RETURNED; APPROVER; CALLER cả hai nhánh | CV1 · cao |
| CHUNG.BAT.S01 (8, 13, 19) | ACTIVATE; approved_version/place/time/params/rights; yêu cầu bật (máy trả ACTIVE/BLOCKED + usage ref); APPROVED_READY→ACTIVATION_REQUESTED; ACTIVATOR; CHUNG.BAT.S02→CALLER | CV1 · cao |
| MOW.TAO.S05 (4) | EDIT; tên/loại/neo T2 trên AI draft; khai nháp; AI_DRAFT_READY→DRAFT_DEFINED; EDITOR; MOW.TAO.S06 | CV1 · cao |
| MOW.TAO.S06 (5) | EDIT; MOT/quy trình con + thứ tự; danh sách bước; DRAFT_DEFINED→STEPS_SELECTED; EDITOR; MOW.TAO.S07 | CV1 · cao |
| MOW.TAO.S07 (6) | EDIT; trước/sau/song song/hội tụ/điều kiện; quan hệ bước; STEPS_SELECTED→FLOW_CONNECTED; EDITOR; MOW.TAO.S08 | CV1 · cao |
| MOW.LAP.S03 (10) | EDIT; bản đã kiểm/cha/chỗ gắn; ATTACHED_TO_PARENT + usage ref; EXISTING_VERSION_VERIFIED→ATTACHED_TO_PARENT; EDITOR; MOW.LAP.S04 | CV1 · cao |
| MOW.KHAI.S01 (11) | CONFIGURE; nơi/trigger/khuôn↔đơn vị/kho/nhánh/quyền; cấu hình chỗ dùng; CONFIGURATION_PENDING→CONFIGURED; CONFIGURATOR; MOW.KHAI.S02 | CV1 · cao |
| MOW.SUA.S05 (16) | EDIT; tên/loại/neo T2 trên clone; khai bản sửa; CLONED_DRAFT→REVISED_DRAFT_DEFINED; EDITOR; MOW.SUA.S06 | CV1 · cao |
| MOW.SUA.S08 (18) | CONFIGURE; tất cả/chỉ nơi này; phạm vi áp bản; REVISED_VERSION_APPROVED→ROLLOUT_SCOPE_SELECTED; CONFIGURATOR; MOW.SUA.S09 | CV1 · cao |
| MOT.CHAY.S03 (22) | EXECUTE; assignment/form/bản ghi; mở đúng form; ASSIGNED→OPENED; ASSIGNEE; MOT.CHAY.S04 | CV1 · cao |
| MOT.CHAY.S04 (23) | EXECUTE; form/kết quả; SUBMITTED rồi máy ghi/đọc lại; OPENED→SUBMITTED; ASSIGNEE; MOT.CHAY.S05 | CV1 · cao |
| MOT.CHAY.S08 (24) | ATTACH; tệp/bình luận; annotation; RESULT_COMMITTED→RESULT_ANNOTATED; CONTRIBUTOR; MOT.CHAY.S09 | CV1 · cao |
| MOW.CHAY.S07 (25) | VIEW; ngữ cảnh lượt; không ghi; RUNNING→RUNNING; VIEWER; CALLER | CV1 · cao |

Không có cặp khác step-key nào đồng nhất cả sáu phần. Đặc biệt TAO.S05 và SUA.S05 có input gần giống nhưng trạng thái và return khác. CHUNG.NGUNG và MOW.XOA không có direct Human Step. C01 giữ 25 hồ sơ vì chưa có contract; C02 thay kết luận **unique H** bằng 15, không thay số instance 25. Quyền ở đây là lớp contract, còn binding vai thực tế theo NT03/NT05 vẫn OPEN.

### H → UI · kiểm màn hiện có

Dùng chữ ký UI parent + human data shape + primary action + state transition. Bảng phân loại mức **bằng chứng hiện có**, không nghiệm thu thao tác chạy thật. EXISTING_GREEN/BASELINE nghĩa là có khung tham chiếu; OPEN_EVIDENCE nghĩa là chưa phân biệt được dùng lại qua cấu hình/đấu nối với UI thiếu. Không có kết luận chắc thuộc VARIANT_CONFIG_LABEL hoặc MISSING_UI.

| Human Step | UI parent / route tham chiếu · dữ liệu → thao tác → state cần chứng minh | Phân loại |
|---|---|---|
| CHUNG.TIM.S01 | UI.MASTER / UI-029 · query → chọn kết quả trả caller → SEARCH_RESULT; picker/permission chưa có bằng chứng | EXISTING_GREEN/BASELINE |
| CHUNG.NEU.S01 | UI.MASTER/CANVAS / UI-004,005 · need_text → ghi nhu cầu → NEED_RECORDED; góp ý mẫu chưa chứng minh need_code | OPEN_EVIDENCE |
| CHUNG.DUYET.S02 | UI.REVIEW / UI-009,011 · subject/lý do → duyệt/trả → APPROVED/RETURNED; hiện là review chỉ đọc | OPEN_EVIDENCE |
| CHUNG.BAT.S01 | UI.CONFIG / UI-001,005 · nơi/lúc/tham số → bật → ACTIVATION_REQUESTED; trạng thái hiển thị chưa chứng minh thao tác | OPEN_EVIDENCE |
| MOW.TAO.S05 | UI.CANVAS / UI-005 Đề xuất · tên/loại/neo → lưu → DRAFT_DEFINED; save chưa chứng minh | OPEN_EVIDENCE |
| MOW.TAO.S06 | UI.CANVAS / UI-005,009 · MOT/con/thứ tự → xếp → STEPS_SELECTED; editor chưa chứng minh | OPEN_EVIDENCE |
| MOW.TAO.S07 | UI.CANVAS / UI-005,011 · cạnh/điều kiện → nối → FLOW_CONNECTED; R04 chờ nguồn | OPEN_EVIDENCE |
| MOW.LAP.S03 | UI.MASTER/CANVAS / UI-029,005 · bản/cha/chỗ gắn → gắn → ATTACHED_TO_PARENT; picker/commit chưa chứng minh | OPEN_EVIDENCE |
| MOW.KHAI.S01 | UI.CONFIG / UI-005,009 + mẫu Config · trigger/kho/nhánh/quyền → lưu → CONFIGURED; chưa có form MOW tương ứng | OPEN_EVIDENCE |
| MOW.SUA.S05 | UI.CANVAS / UI-005 · tên/loại/neo trên clone → lưu → REVISED_DRAFT_DEFINED; quan hệ với TAO.S05 chưa chốt | OPEN_EVIDENCE |
| MOW.SUA.S08 | UI.CONFIG / UI-005,009 · tất cả/chỉ nơi này → áp → ROLLOUT_SCOPE_SELECTED; NT19 chưa có thao tác mẫu | OPEN_EVIDENCE |
| MOT.CHAY.S03 | UI.WORKSPACE / UI-010 · assignment/form/bản ghi → mở → OPENED; khung task/form có, binding thật OPEN | EXISTING_GREEN/BASELINE |
| MOT.CHAY.S04 | UI.WORKSPACE / UI-010 · form/kết quả → gửi → SUBMITTED; khung form/nút có, lưu/đọc lại OPEN | EXISTING_GREEN/BASELINE |
| MOT.CHAY.S08 | UI.WORKSPACE / UI-010 · tệp/bình luận → gắn step_run → RESULT_ANNOTATED; chưa thấy binding | OPEN_EVIDENCE |
| MOW.CHAY.S07 | UI.CANVAS / UI-005 Vận hành + UI-012 · chọn lượt → xem run thật → RUNNING; UI-012 chỉ là schema/event mẫu | OPEN_EVIDENCE |

Đã mở read-only bằng ui_inspect (HTTP 200) một route đại diện cho cả 14 vùng UI ứng viên C01: UI-001/009 Master/chi tiết, UI-004 góp ý, UI-005 Thường/Đề xuất/Vận hành, UI-010 MOT dashboard, UI-029 tìm kiếm, UI-011 checkpoint, UI-012 data/events; thêm mẫu cha Config /admin-new-modt. Chuẩn parent ở ban-duyet.html#parent-ui-standards cho phép tái dùng khuôn và thay label/config, không tự biến một route/mode thành một UI duy nhất. UI-010 hiện có nút “Hoàn thành ✓” **được bật** lúc “Bắt buộc 0/2”, khác ghi nhận C01 là disabled; không bấm/gửi nên chưa chứng minh SUBMITTED. UI-011 là checkpoint mẫu 1/14 và UI-012 là schema/event, không phải log lượt thật. Các hash file UI-001/004/005/010/029/011/012 ở VPS khớp catalog; không sửa UI.

Merge UI duy nhất còn mơ hồ rõ ràng là TAO.S05 ↔ SUA.S05: cùng parent/field/action ứng viên nhưng state nháp mới và clone khác; chưa biết là một cấu hình hay hai interaction. JEV tham khảo ba lựa chọn SAME/DIFFERENT/OPEN: result gen-dec-1790569053-JCuyiSJEeenPJ6kM7LNe, OPEN 0,41, DIFFERENT 0,31, SAME 0,28, confidence 0,12. JEV không thay bằng chứng. Những nhóm UI.CONFIG và UI.WORKSPACE cũng không gộp chỉ vì chung parent/route: data/action/state khác. Do chưa có binding thao tác và chuyển trạng thái đủ cho mọi H, **U_MOW=UNKNOWN**. Do chưa chứng minh một hành động không thể nằm trong khuôn hiện có hoặc chỉ thiếu cấu hình/đấu nối, **UI_MISSING=UNKNOWN**, không suy bằng 0 hoặc bằng số route.

NEXT duy nhất: **Host giao B/A chốt bảng binding 15 H→UI theo parent, dữ liệu người, thao tác chính và chuyển trạng thái.**

KQ@MMIM-LANE-C02-20260928-01 DỪNG
KQ@LANE-C C02 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · instances=25 · H_MOW=15 · U_MOW=UNKNOWN · UI_MISSING=UNKNOWN · NEXT=Host giao B/A chốt bảng binding 15 H→UI theo parent, dữ liệu người, thao tác chính và chuyển trạng thái.
COORD · NOW=DỪNG · NEXT=Host giao B/A chốt bảng binding 15 H→UI theo parent, dữ liệu người, thao tác chính và chuyển trạng thái. · BLOCKED_BY=UI live mới chứng minh khung, chưa đủ action/state và binding để phân biệt variant với missing · RESERVED_TARGETS=lane-c/COLLAB.md · LAST_SYNC=D72-D73/C02
- C03 HOST GATE · PASS · PROCESS=`CHUNG.APQUYTRINH` · prompt=`3a1219ecdb4b9e3c060dd8b5a9c0c37a5590337cac3c1ea9088357fa88fee3e0`.
- READY@903b34c4dc7103a7dc88a84d3f59d4ac5d6b3aee · RUN_ID `MMIM-LANE-C03-20260928-01`.
- C03 D79 RE-GATE · PASS · prompt=`e9f3d8231c89fa9ccea0888a3c4f12e149f93bc094a0c56220a2cacb5b6565a0`.
- READY@c48c877992fea2ec0acd26f7f02a20c6c9ca9ab6 · RUN_ID `MMIM-LANE-C03-20260928-01` · supersedes READY 903b...

STARTED@MMIM-LANE-C04-20260930-01 2026-09-30T07:10:53Z · executor=Codex

## Codex · KQ C04 · 30/09/2026

MOW — List UI-001 có; Kanban UI-005 có; baseline với dữ liệu mẫu.  
MOT — List UI-002 có; Kanban UI-028 có; baseline, chưa nối dữ liệu thật.  
MOIT — List UI-013 có; Kanban UI-019 có; mock dùng lại cha.  
MOUT — List UI-014 có; Kanban UI-020 có; mock dùng lại cha.  
Field — List UI-022 có; Kanban UI-021 có; mock dùng lại cha.  
**Công thức 2 view = PARTIAL:** có khuôn dùng chung; chưa chứng minh đủ thao tác/vòng đời 3→7.  
**Loại từ “Thứ” khỏi mặt Owner = YES**, theo D91; dùng “Đối tượng”.  
**6 khuôn cha = REPLACE_WITH_2_VIEW_PARENTS** ở công thức; giữ 4 chuẩn khu làm việc trong chi tiết.  
**18 ứng viên cũ = 18 NOT_PROVEN; 0 QUALIFIES và 0 NOT_OBJECT đã chứng minh.**

<details>
<summary>Evidence C04 · 5 đối tượng, 18 ứng viên, nghĩa của 6 chuẩn và giới hạn</summary>

### Phạm vi, gate và concurrency

Đọc đúng AGENTS → COLLAB cha → council/REGISTRY → lane-c/COLLAB → PROMPT. A0 đã xác nhận; Registry CODEX-MMIM-C khớp C04 và chỉ dành lane-c/COLLAB. READY 626769a87a786abfeb410ea3e85b8a48d9ff8846 đúng commit cuối chạm PROMPT; SHA PROMPT c0fae2b41af054534af335d9802272e1e3c899f962d9791f50f385a71bc1cc38. STARTED đã ghi tại commit cfd3764272e42421690a0788c1d9f4a0d632f23e.

Process gate đã chạy bằng dot-process-gate trong snapshot cô lập: job 8162dbf54f7445c0b0f3389cd6c2e247, source_head c51fe1b31585ebbe5d4761c9797055d6f978d890; exit 0, stderr rỗng; PASS / VEUI.MOW / reason OK / 39 process / 8 step. Catalog tại gate có SHA e0e533ab98b80ec80bc51cd616cce07aaa2d53f343099e1aedf664c441ff3bd5; stdout SHA bd560be5af69a7dbcaff3204b59d12d9964765878d71b53d3301230dbf43d876.

B05 đổi canonical sang ccf4e77b83b48d6691078dfc72f88de8a999a914bff836e3f84a4575abee8d4f tại HEAD 4e8cf8d4dacef4752a78538de07aaf85858f6379. Đã đọc hết diff từ snapshot audit: chỉ cập nhật mặt Công thức theo D91 và bọc lịch sử; các anchor parent, catalog và 18 nhãn dùng trong C04 không đổi. PROMPT/Registry/lane target vẫn hiện hành khi re-read trước KQ. C04 không ghi canonical/UI; kết quả là audit, không thiết kế thêm UI hay quyết methodology của Council.

### 5 đối tượng · List và Kanban thật

Đã inspect read-only 10/10 route dưới đây, HTTP 200; thêm MOW Đề xuất HTTP 200. UI code lấy từ child directory/registry, source được đọc trực tiếp ở VPS root ui. “Có” là có baseline/source và route chạy được; chưa chứng minh production. Mỗi query là ngữ cảnh của cùng nguồn, không là bản UI/renderer mới.

| Đối tượng | Master List · UI/route/source | Kanban · UI/route/source | Parent thực tế và reuse | Readiness / renderer mới |
|---|---|---|---|---|
| MOW | UI-001 · [mow-master-nhap2-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html) | UI-005 · [canvas T2](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=thuong) | UI.MASTER → master-list.js v16; UI.CANVAS → chính canvas cha | Baseline đã chọn; 7 quy trình mẫu. Dùng lại renderer; gap data/lifecycle. |
| MOT | UI-002 · [mot-master-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mot-master-v1.html) | UI-028 · [canvas T1](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T1&che-do=thuong) | UI.MASTER → master-list.js v16; cùng UI.CANVAS với nhánh chuẩn T1 mow-t1-work-standard-v1.js v2 | Baseline; 7 task hardcode, Kanban “Chưa kết nối”. Nhánh T1 đã có, không chứng minh cần renderer mới. |
| MOIT | UI-013 · [moit-master-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/moit-master-v1.html) | UI-019 · [canvas T0.5 MOIT](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T0.5&che-do=thuong&form=MOIT&cong-viec=T01) | UI.MASTER: wrapper → ui-child-from-parent-v1.js → MOT Master; UI.CANVAS dùng buildCard chung | Mock/baseline; 6 form minh họa, chưa nối nguồn thật. Dùng lại renderer. |
| MOUT | UI-014 · [mout-master-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mout-master-v1.html) | UI-020 · [canvas T0.5 MOUT](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T0.5&che-do=thuong&form=MOUT&cong-viec=T01) | Cùng loader Master và buildCard canvas của MOIT; đổi dữ liệu/nhãn | Mock/baseline; 6 thông tin đầu ra minh họa. Dùng lại renderer. |
| Field | UI-022 · [field-master-v1.html](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/field-master-v1.html) | UI-021 · [canvas T0 Field](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T0&che-do=thuong&form=MOIT&cong-viec=T01) | Cùng loader Master; buildCard chung + adapter kanban-field-v1.js hiện hữu | Mock/baseline; 3 trường minh họa, chưa nối PG. Dùng lại renderer. |

**Reuse có bằng chứng source:** ba wrapper MOIT/MOUT/Field nạp ui-child-from-parent-v1.js; loader fetch nguyên MOT Master và configureChildMaster thay nhãn/dữ liệu, giữ CSS/functions/thứ tự cột. Cả năm Kanban cùng mow-unified-canvas-v2.html: render gọi buildCard chung cho T2/T0.5/T0; T1 dùng T1_WORK_STANDARD.applyLayout và nhánh chung đã có. Vì vậy không có bằng chứng buộc tạo renderer mới cho hai loại view; phần còn thiếu là cấu hình/binding/vòng đời trên nguồn hiện hữu, cần kiểm tiếp khi được giao.

**Vì sao PARTIAL:** D91 gắn Master với Tìm+Dùng và Kanban với 3→7. Canvas hiện chủ yếu là thẻ hierarchy NV01…NV06 và công việc con; chưa có bằng chứng đủ các trạng thái/thao tác Đề xuất tạo → Duyệt đề xuất → Khai báo → Test → Duyệt cho dùng cho năm đối tượng. Source GN02 ghi Đề xuất chỉ intake + positioning, xử lý ở bảng chờ chuyên biệt bên ngoài canvas. submitAddModal (L1583) chỉ chèn newNode vào D[tier].nodes trong bộ nhớ rồi render; T1 TEST_STATUS_SOURCE.mode=future_table. Không thử tạo/lưu/duyệt/test/bật vì RUN read-only. Dấu xanh baseline trong eco-nav.js cũng ghi rõ không đồng nghĩa PG/config đã hoàn chỉnh.

Hash VPS hiện tại đã stat lại trước KQ, khớp lần inspect; dùng hash live, không lấy hash catalog lịch sử làm phiên bản đang chạy:

| Source | SHA256 |
|---|---|
| mow-master-nhap2-v1.html | a8635779d4b64344543988ca63041a41132705325f383a728b7358862c0d632b |
| mot-master-v1.html | 85da2f858f1f5e3f9e01110c110886c5c15cde043b47642068956324948c421e |
| moit-master-v1.html | 1e7702062f0bdcb005ff89c699ddbb057695039db01aa4b9df2edf61d41712fb |
| mout-master-v1.html | e1b4cbf0ff053f9126965ad5b218406e7daf4daaabd5b2aa7d3395b04524ec57 |
| field-master-v1.html | d090fa2603827cc22fa9f3c3ae02e9dc631f091991fcbfd6425e2a4d97a38845 |
| mow-unified-canvas-v2.html · chung năm route | 64c21429c5867948a4636f7c521c1f6ba1ecc3b18e62e5ab0f90638e0a08b869 |
| master-list.js | a92524f509b514e2a04677e3bd7d7dfd17efc8c206282840a6bf6b3f876baa57 |
| ui-child-from-parent-v1.js | c2c577bd0de00964b6da9b6a7dec49476f64fc85342d6a4a8ea4758ffd624363 |

### 18 ứng viên cũ · kiểm từng mục

Nguồn exact nhãn: ban-duyet.html L363, hàng D nhóm quy trình ở snapshot audit; đối chiếu các anchor dưới. Metadata/table evidence của catalog ghi từ 26/09, không phải lần C04 query PG. Mã CAT là identity của **danh sách**, chưa tự chứng minh identity/vòng đời từng đối tượng trong đó; dấu * là mã giữ chỗ. “?” = chưa có bằng chứng đúng scope. Có liên kết cha hoặc process đọc một catalog cũng chưa đủ chứng minh reuse/tìm/tạo/sửa/ngừng độc lập. Cần chứng minh nhu cầu quản trị bằng List/Kanban riêng; thiếu route hiện tại không tự làm ứng viên thành NOT_OBJECT.

| # · Nhãn chính xác | Source / identity evidence | Lifecycle riêng | Reuse độc lập | Cần Master riêng | Cần Kanban riêng | Verdict |
|---|---|---|---|---|---|---|
| 1 · giá trị | #ml3-03 CAT-201*; nguồn nói bộ giá trị cố định, chưa phải scalar value | ? | FIELD.TAO gọi bộ giá trị khi thiếu; còn thiết kế | Catalog đề xuất, chưa bind nhu cầu riêng | ? | NOT_PROVEN |
| 2 · mẫu ô nhập | #ml3-05 CAT-203*; F/L/E/C, nguồn ←06 MOIT | ? | FIELD đọc05; chưa có sửa/ngừng độc lập | Studio reference, chưa chứng minh List riêng | ? | NOT_PROVEN |
| 3 · hợp đồng vào/ra | #ml3-10 CAT-206*; record type/source/create-update/cardinality, ←08 MOT | ? | Contract được gọi; registry độc lập chưa chứng minh | Catalog đề xuất | ? | NOT_PROVEN |
| 4 · bảng | #ml3-17 CAT-008 collection_registry; #ml3-65 CAT-001 table_registry; hai scope | ? đúng scope | FIELD đọc17, UI con dùng65; nhãn còn mơ hồ | Có catalog, chưa chốt đối tượng nào | ? | NOT_PROVEN |
| 5 · đối tượng nghiệp vụ | #ml3-18 CAT-211*; một dòng=1 danh sách bản ghi, ←17 | ? | Thiết kế đọc18; chưa bind record/contract | Catalog đề xuất | ? | NOT_PROVEN |
| 6 · nhãn | #ml3-20 CAT-018 taxonomy; #ml3-64 CAT-068 là liên kết entity_labels | ? | Tìm dùng nhãn; chưa bind reuse/lifecycle riêng | Có catalog reference | ? | NOT_PROVEN |
| 7 · cây tổ chức | #ml3-22 CAT-212*; iu_tree khác scope; UI023–027 xem cùng một cây | ? đúng object | Reference cây, chưa chứng minh object riêng | Có cách xem cây, List đúng object chưa chứng minh | Kanban lifecycle chưa bind | NOT_PROVEN |
| 8 · người | #ml3-23 CAT-213*; directus_users là user hệ thống, scope người nghiệp vụ chưa bind | ? đúng object | Caller/assignee theo thiết kế | Catalog đề xuất | ? | NOT_PROVEN |
| 9 · vai | #ml3-24 CAT-214*; directus_roles khác scope vai/chức vụ | ? đúng object | Process/quyền đọc vai theo thiết kế | Catalog đề xuất | ? | NOT_PROVEN |
| 10 · ủy quyền | #ml3-25 CAT-215*; process_axis_delegation reference | ? | Độc lập còn thiếu evidence | Catalog đề xuất | ? | NOT_PROVEN |
| 11 · agent | #ml3-26 CAT-010 agents; có registry reference | ? object-specific | MOT gọi agent; vòng đời/tìm-dùng độc lập chưa bind | Catalog có, nhu cầu riêng chưa chứng minh đủ | ? | NOT_PROVEN |
| 12 · nguyên tắc | #ml3-30 CAT-219*; NẾU…THÌ; #ml4-nt01…22 là loại, không là record lifecycle | ? | Nhiều process gọi NT; chưa bind object độc lập | UI003/bảng 12 cột là prototype | ? | NOT_PROVEN |
| 13 · điều kiện | #ml3-31 CAT-220*; vế NẾU, ←30 nguyên tắc | ? | Có thể là thành phần; chưa chứng minh độc lập | Catalog đề xuất | ? | NOT_PROVEN |
| 14 · trigger | #ml3-32 CAT-221*; CAT-019 trigger_registry là trigger CSDL, scope quy trình chưa bind | ? đúng object | MOW đọc32 theo thiết kế | Catalog đề xuất | ? | NOT_PROVEN |
| 15 · loại sự kiện | #ml3-33 CAT-222*; event_type_registry reference, ←32 | ? | Event design có; lifecycle/reuse riêng chưa bind | Catalog đề xuất | ? | NOT_PROVEN |
| 16 · bộ kiểm | #ml3-44 CAT-012 checkpoint_sets; khác kết quả kiểm #ml3-45 | ? bộ kiểm | CHUNG.KIEM đọc44; có reference, chưa chứng minh vòng đời độc lập | Catalog có, view/nhu cầu riêng chưa chứng minh | ? | NOT_PROVEN |
| 17 · UI cha | #ml3-58 CAT-234*; renderer/standards có; record ID/version/ngừng riêng chưa bind | ? | Tái dùng source có; quản trị object riêng chưa chứng minh | Catalog đề xuất | ? | NOT_PROVEN |
| 18 · hướng dẫn | #ml3-62 CAT-074 help_articles, ←59 UI con | ? article-specific | Help reference có, độc lập chưa bind | Catalog có, view/nhu cầu riêng chưa chứng minh | ? | NOT_PROVEN |

Tổng: QUALIFIES=0 đã chứng minh; NOT_PROVEN=18; NOT_OBJECT=0 đã chứng minh. Không suy ra 18 Kanban mới hay giữ số “23 Đối tượng” từ phép cộng cũ. P13 lịch sử nói một số thứ có đời sống riêng nhưng tự ghi chưa kiểm PG/runtime; sổ lifecycle_log chung #ml3-71 chưa bind vòng đời cho từng ứng viên. C04 giữ các mục để truy nguồn, không tự gộp/xóa/cấp UI code.

### “6 khuôn cha” và thuật ngữ

Nguồn #ia-parent-table L101 đặt tên sáu “Mẫu cha hướng tới”; #parent-ui-standards L98 ghi rõ chỉ hai view: Kanban và Master list, bốn mục còn lại là khu làm việc. D91 chốt cùng nghĩa. Verdict **REPLACE_WITH_2_VIEW_PARENTS** áp cho con số tổng hợp trên Công thức, đồng thời giữ sáu chuẩn hiện hữu ở tầng kỹ thuật:

| Chuẩn hiện hữu | Vai trò trong kiến trúc 2-view | Source |
|---|---|---|
| UI.MASTER | View parent Master List | mow-master-nhap2-v1.html / master-list.js |
| UI.CANVAS | View parent Kanban | mow-unified-canvas-v2.html |
| UI.CONFIG | Khu cấu hình, không thêm loại view | new-modt-v1.html / đường admin-new-modt |
| UI.STUDIO | Khu chọn thành phần/xem thử | mot-studio-v1.html / mot-studio-v1.js |
| UI.REVIEW | Khu xem/duyệt/kiểm | Chi tiết WF-0001 / nhap2-render.js |
| UI.WORKSPACE | Bàn làm việc | mot-dashboard-v1.html / mot-render-v1.js, mot-app-v1.js |

Hai loại view không đồng nghĩa chỉ có hai file renderer vật lý; nguồn có module/adapter theo phạm vi. Từ “Thứ” nên loại khỏi **mặt Owner = YES** vì D91 đã chốt “Đối tượng” với định nghĩa rõ; tên lịch sử/nhãn ứng viên vẫn giữ trong details để truy nguồn. C04 chỉ ghi kết luận, không tự sửa mặt canonical.

JEV tham khảo bounded classification bằng evidence nguồn/live trung tính: result gen-dec-1790752973-e5zRRYBTTEySQ6hQINXn, model do gateway trả typesafe/jev-1.13-20260917. Formula PARTIAL confidence 0,99; parent6 REPLACE_WITH_2_VIEW_PARENTS confidence 1,00; cả 18 chọn NOT_PROVEN, confidence 0,55–0,99 (thấp nhất ở giá trị/mẫu ô/điều kiện). Kết luận dựa trên source và giới hạn evidence; JEV không xác nhận runtime.

</details>

KQ@MMIM-LANE-C04-20260930-01 XONG
KQ@LANE-C C04 · PROCESS=VEUI.MOW · PROCESS_GATE=PASS · core_objects=5 · two_view_formula=PARTIAL · small18=NOT_PROVEN:18/QUALIFIES:0/NOT_OBJECT:0 · parent6=REPLACE_WITH_2_VIEW_PARENTS · NEXT=Host nghiệm thu C04.
COORD · NOW=XONG · NEXT=Host nghiệm thu C04. · BLOCKED_BY=none · RESERVED_TARGETS=lane-c/COLLAB.md · LAST_SYNC=FORMULA-01/C04
