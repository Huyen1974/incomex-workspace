# R1 · MOW — bằng chứng rà UI cho PM, 10/09/2026

**R1 CANONICAL CANDIDATE: NO CURRENT CANDIDATE FIT — Gate2 cần ghép đường review chung vào canonical data và checkpoint có quyền.** Đây là kết luận trong 7 URL thuộc U02/U03 và vùng U04 đã rà; không kết luận toàn hệ không có chức năng đó. **W003 SUBMITTED; D03 OPEN, PM quyết.** Gate1 DOING, Gate2 chưa mở. Báo cáo này là evidence của SSOT, không phải tài liệu kiến trúc thay thế.

## 1. Quyết định PM và phạm vi

PM đã ACCEPT/DONE Gate0; W002-FEAS ACCEPT WITH FOLLOW-UP cho bounded feasibility implementation path. Proof A/B/C được nhận đúng phạm vi trong [lệnh PM](pm-command.md). Gói trước đã kiểm lại 199/199 hash. Điều đó chứng minh có đường triển khai tối thiểu, không chứng minh các UI MOW đang phục vụ đã nối vào đường ấy.

R1 chỉ đọc 7 URL, mở Help/detail/mode/filter; thêm 2 deep-link xuất phát từ drawer để kiểm giữ context. U04 là vùng graph/dependency/I/O của U03, không URL thứ tám. 7/7 có kết luận; không candidate chưa kiểm trong danh sách này. Đọc 7 HTML và 47 script URL trực tiếp của chúng, lưu URL/status/TLS/SHA trong [source-capture](source-capture.json), [asset-capture](asset-capture.json). Không quét toàn repo; không chạy save/approve/activate/đúc/test trên production. Không thử Agent write vào các UI này. Không network interception: API nhận định từ deployed source và hành vi đọc; giới hạn này không được gọi là chứng minh network vắng mặt tuyệt đối.

## 2. Bảng candidate

| Candidate | Vai trò phù hợp | Actual connected? | Điểm mạnh | Gap chính | Đề nghị | Evidence |
|---|---|---|---|---|---|---|
| U02 · MOW Master v1 | Library/master | MOCK; 7 dòng MASTER_CONFIG inline. Không canonical read/write | Bộ lọc chữ/trạng thái/cây, drawer | Không admission/near/impact/version thật; nút tạo đi thẳng Canvas | Ghép thư viện, loại khỏi default authoring path | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-v1.html), [ảnh](browser/master.png), [tìm](browser/master-search.png), source/mow-master-v1.html:18–33 |
| U02 · process-draft v1 / Nháp 1 | Expert review/reference | MOCK; scope/relations/versions hiển thị chưa nối | Bước, biên MOW, Help tại chỗ, chỗ thiếu | Drawer nhiều mục, Help nhiều kết luận cũ xung đột; không revision/API | Giữ reference/Help có chọn lọc; fallback, không primary | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-process-draft-v1.html), [drawer](browser/draft-detail.png), [Help đầy đủ](browser/draft-help.txt), source/mow-drawer-scope.js_v-11 |
| U02 · MOW Master Nháp 2 | Hình thức review chính tốt nhất để tái sử dụng | MOCK; 10/10 kiểm JS trên contract mẫu, 1/14 checkpoint khai sẵn | Drawer 3 câu; phân lớp detail/Mặt bàn; công khai chưa phát hành | Mặt bàn là tài liệu; thiếu intent→Agent/reuse/real diff/checkpoint. Contract S1–S4 khác bảng 8 việc, badge 7 khác readiness17 Nháp1 | **Ghép khung review vào đường chính đề xuất**, chưa chọn cả ứng dụng làm canonical | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-master-nhap2-v1.html), [drawer](browser/nhap2-detail.png), [checkpoint](browser/nhap2-checkpoints.png), source/nhap2-core.js_v-6:11–25,145–166,178–218 |
| U02 · Master list quy trình | Library variant | MOCK; WF-0001 là Xuất khẩu, khác WF-0001 Nhập kho bên Master | Bộ lọc cây chung, có mô tả chi tiết | Identity không đồng nhất giữa preview; không nguồn/version thật | Retire-candidate cho bản trùng, bảo toàn nội dung trước khi PM quyết; chưa xóa | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/master-list-quy-trinh-v1.html), [ảnh](browser/process-list.png), [text](browser/process-list-dom.txt), source/master-list-quy-trinh-v1.html |
| U03 · Unified Canvas v2 | Graph visualizer/context + expert proposal | DRAFT/mock; const D, st, proposals trong bộ nhớ; runtime là mẫu | 7 tầng, drill-down, proposal có vị trí, biểu diễn Human/AI | Chưa chứng minh executable graph/branch/join/edge ID; sửa từng dòng; không canonical target/revision | Ghép view đồ thị theo yêu cầu, expert edit; runtime monitor chỉ mock | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/mow-unified-canvas-v2.html?tang=T2&che-do=de-xuat), [đề xuất](browser/canvas-edit-preview.png), [runtime](browser/canvas-runtime.png), source/mow-unified-canvas-v2.html |
| U03 · MODW builder v1 | Expert assembly demo | MOCK; TREE/PEOPLE/STORES và JSON local; cast chỉ alert demo | Chọn cha, người, kho, thời gian; preview tức thời | Sáu nhóm khai thủ công, dữ liệu riêng; gộp T1–T7/people/store vượt biên MOW nếu dùng làm editor thật | Fallback/expert; không default và không production executable | [Trang](https://vps.incomexsaigoncorp.vn/ui-preview/mcp-writes/modw-builder-v1.html), [ảnh](browser/modw.png), source/modw-builder-v1.html:143–168,238–251 |
| U03 · New MODT /admin-new-modt?tang=T2 | Expert task/data mapping view; T2 canvas variant | DRAFT/mock, HTML tĩnh dù URL trông như app; Field tương tự là mẫu; test chỉ đổi DOM; approval preview dùng sessionStorage | I/O/reference liền chỗ, Help cột, cho thấy nguồn thiếu | Mở URL T2 ban đầu ra T1/Nhận đơn; click T2 mới đúng tầng. Không canonical read/write/ownership enforcement | Fallback/owner-editor handoff; không primary MOW; không mở R2/R6 | [Trang](https://vps.incomexsaigoncorp.vn/admin-new-modt?tang=T2), [ban đầu](browser/new-modt.png), [sau chọn T2](browser/new-modt-t2.png), [Field tương tự](browser/new-modt-similar.png), source/admin-new-modt.html:2290–2317,2640–2690 |
| U04 · vùng graph/dependency/branch/join/I/O | Một view bên trong U03 | MOCK / NOT CONNECTED | Node/order và I/O có thể đọc bằng mắt | Cây tổ chức không là dependency graph; Nháp2 có fan-in S2+S3→S4 ở JSON mẫu nhưng không same-data edge view; chưa thấy readiness cho nhánh/join thật | Ghép subgraph review theo context; gap về liên kết/hiển thị, không tạo engine mới | Ảnh Canvas T2 + New MODT phía trên; source/nhap2-core.js_v-6:145–155 |

Không dùng chữ “Bản thật”, “Đang chạy”, “10/10”, “SSOT” trên preview làm chứng cứ production. Source tồn tại và được HTTP phục vụ khác với dữ liệu nghiệp vụ được kết nối.

## 3. Đề xuất đường mặc định — PM chưa quyết

Tái sử dụng **cách review ba câu hỏi của drawer Nháp2** làm phần người nhìn; giữ library Master và Canvas như view cùng context có thể mở khi cần. Không chọn nguyên Mặt bàn Nháp2 làm workspace chạy thật: nội dung đó hiện là tài liệu mô tả hệ thống. Không yêu cầu tám màn mới.

Đường đề xuất: người nêu ý tưởng/bối cảnh → Agent tìm/reuse và dựng nháp qua cổng chung → hệ kiểm và trả thiếu/khác biệt/bằng chứng → người xem ý nghĩa, quyền và ngoại lệ ở một review context → hệ ghi quyết định theo quyền, test, ban hành theo dependency. Đường này là yêu cầu đã có trong SSOT, chưa được chứng minh trên các candidate R1. PM có thể chọn hình thức tái sử dụng dù chưa đủ chọn UI nối thật.

### G1–G8: cùng context, không tám màn

| Stage | UI hiện có phục vụ được gì | Agent/system phải làm | Human touch đúng phạm vi | Gap cần đưa Gate2 thiết kế; Contract/Data ở Gate3–4 |
|---|---|---|---|---|
| G1 Intent | Canvas proposal mở đúng node; Nháp2 mô tả góp ý một dòng | Tự gắn actor/scope/đối tượng/revision, hiểu intent | Nêu mục tiêu/điều chưa rõ | Chưa có intent intake→Agent/checkpoint trên canonical data; không bắt sửa từng step |
| G2 Reuse | Master có lọc chữ/trạng thái/cây trên mẫu | Tra exact/near/meaning/scope, where-used, admission trước tạo | Chốt ambiguity/khác nghĩa nếu cần | Không near MOW/impact/version diff/admission receipt; tìm Field tương tự của New MODT không thay G2 |
| G3 Draft | Drawer bảng bước/Canvas preview | Khai MOW và refs tới MOT/version theo đúng owner; bulk/dry-run qua cổng | Review thay đổi; expert override có quyền | Chưa canonical ID/version/revision hoặc đọc nháp do Agent tạo; deep-link không giữ target |
| G4 Resolve/readiness | Nháp1 badge17, Nháp2 14checkpoint + 10 luật mẫu | Một kết quả kiểm có source/revision, mở yêu cầu bù đúng owner, nhớ checkpoint và resume | Chỉ quyết gap máy không tự giải | Badge/graph/contract mẫu khác nguồn; chưa stale detection/refetch/resume; không viết validator thứ hai trong UI |
| G5 Decision | Drawer 3 câu; Mặt bàn giải thích mục tiêu | Sinh diff/impact/recommendation có provenance | Chốt nghĩa, scope, ngoại lệ/rủi ro | Chưa material diff hoặc receipt quyết định; không biến admin thành người tìm/lắp mọi thứ |
| G6 Test | Nháp1 có danh mục; Nháp2 10/10 local; New MODT nút dấu ✓ | Runner/test registry hiện có trả result đúng version/suite | Review fail cần nghĩa nghiệp vụ | Không có automated test receipt cho MOW thật; click dấu ✓ không phải test. UI chỉ hiển thị kết quả hệ thống |
| G7 Approval | Help mô tả ba dấu; Nháp2 mẫu approvals[] | Kiểm authority/delegation/separation, persist approval đúng artifact/hash | Người có quyền duyệt | Chưa auth/audit/approval enforcement trên candidate; không mang approvals mẫu vào truth |
| G8 Publish/Activate | Nháp1 khóa Mở quy trình; Nháp2 có liên kết lỗi404 | Gate release đã test, atomic activate, immutable pin theo contract | Quyết định cho phép phát hành | Chưa release-aware API/read-back hoặc state thật; dùng candidate Gate0 theo Reuse Ladder, không tự production-final |

G9/G10 chỉ nhận diện link/runtime monitor mẫu và cải tiến trong Help; không mở R8/R9 hay nghiệm thu runtime ở lượt này.

## 4. Những chỗ có thể làm thiết kế quay về thao tác tay

- Canvas edit NV01 mở **5 dòng công việc** để sửa tên/thứ tự/Human-AI; không có Agent dựng/reuse trong đường này. MODW có **6 nhóm khai** (node/tầng, cha, người làm, người nhận, kho, thời gian). Đây là expert/fallback.
- Không quan sát ô buộc người tự gõ raw ID ở Canvas/MODW; việc chọn label không chứng minh resolved ID đúng. Các mã ở JSON Nháp2 là tự ghép từ code mẫu. Không kết luận tất cả UI bắt gõ ID.
- Người có thể tìm Master, mở drawer, theo liên kết sửa, quay lại xem Help; lần thử thực tế link sửa mất target. Không có end-to-end task hoàn tất để đo số hop/thời gian tạo quy trình. Các số trên là control/step quan sát, **không phải đo usability hay tỷ lệ 98%**.
- Chưa có chứng cứ Agent đọc/ghi cùng canonical MOW/version/revision rồi UI refresh. Reload chỉ đọc lại JavaScript mẫu. Gate0 đã chứng minh cơ chế ở fixture riêng; chưa tích hợp vào candidate R1. Không yêu cầu Agent click UI để khai báo.

## 5. Ownership, reuse và các gap chính xác

**R1-GAP-01 — Context và data chung.** WF-0001 Nhập kho ở Master/Nháp1/Nháp2 nhưng Xuất khẩu ở Master list. Drawer link `?edit=WF-0001` thực tế mở Canvas T4 mặc định, không MOW đó ([ảnh](browser/canvas-edit-link.png)); `/w/wf-0001` 404 ([ảnh](browser/run-link-404.png)). Cần canonical object_id/version_id/revision, same-context views và read-back/refetch sau Agent write. Chưa chứng minh namespace/different-dataset mapping giải được khác biệt này.

**R1-GAP-02 — Intent/reuse/admission.** Tìm “Nhập kho” trên Master trả mẫu phù hợp, source dùng lọc local. Không có exact-vs-near decision, where-used/impact thật, revision diff hay admission trước CREATE. Trước build: xét PG catalog/query + Directus read/filter/permission + assets resolver/guard Gate0 đã đo + target built-in; chỉ transport/view gap còn lại mới cân nhắc custom. Không đặt mới schema/engine hoặc làm full catalog trong R1.

**R1-GAP-03 — Readiness/test/diff một nguồn.** Nháp1 17 thiếu, Nháp2 badge cũ7, 1/14 checkpoint và 10/10 luật cùng hiện trên WF-0001; bảng trái8 ACTION +1 dự phòng khác contract mẫu4 ACTION +1 WAIT_ONLY. Source `itemContract()` khai approvals/hash/proof=true và `validateBusiness()` kiểm chúng trong JS. Không thể dùng con số này để cho phép chạy. New MODT `testMark.onclick` chỉ đổi dấu ✓ và gọi fillT1ProposalPeople; data-test-source ghi future:test-status-table. **Không bấm nút test**. Cần render machine result có artifact/version/suite/provenance; không copy detector/business logic vào UI.

**R1-GAP-04 — Biên owner và graph.** MOW sửa graph/order/dependency/branch/join và binding/routing/handoff/timing/error cấp MOW. Definition MOT/MOIT/MOUT/Field/shared TriggerCondition/NTGV/People đi editor chủ quản, trả reference. Help Nháp1 có biên này, nhưng MODW gộp T1–T7/người/kho; New MODT đưa field/JSON/test/NTGV lên cùng mặt bàn, chưa có owner-aware action/API. Việc mở chung một màn không tự vi phạm; **nếu ghi các definition đó bằng quyền MOW thì mới sai**. R1 chưa ghi thử nên authority enforcement = NOT PROVEN. Fan-in ở JSON Nháp2 không chứng minh graph thực tế render và runtime dùng cùng cạnh.

**R1-GAP-05 — Authority, publish và Help drift.** Không quan sát login/actor ID/scope/audit receipt canonical trên 7 preview. Source không có canonical MOW API write; sessionStorage New MODT chỉ preview approval. Help Nháp1 có “chỉ ghi B làm sai thay vì chặn”, list cha trong một ô, latest child lúc gọi, định mức9bảng; Nháp2 thay một phần nhưng có “Code trước” cho UI/orchestration và công thức1MOIT cho mọi MOT. Đây là historical design text, không được ghi đè current SSOT/PM baseline. Route Help consistency vào Gate1/Gate2 và RULE-SYNC-01 trước build; security/release contract vào Gate3–6, runtime failure matrix Gate5–7. Không tự sửa Help/luật/catalog trong R1.

## 6. Cheap change / hai mode / tiêu chí nghiệm thu lại

| Tiêu chí giữ đúng SSOT | Kết quả R1 trên candidate MOW |
|---|---|
| CR1 · One source | Chưa đạt: các bộ mẫu khác nhau; chưa cùng canonical ID/version/revision hoặc một nguồn sửa logic |
| CR2 · Reuse | Chưa chứng minh: có tìm/lọc và reference mẫu; không có danh sách nơi dùng/cơ chế tham chiếu thật |
| CR3 · Impact | Chưa chứng minh where-used/impact của đúng phiên bản trước thay đổi |
| CR4 · Human effort | Quan sát 5 dòng sửa Canvas, 6 nhóm khai MODW; chưa có task hoàn tất để đo thao tác/thời gian hay sửa lặp |
| CR5 · Auto test | Chưa có test receipt cho MOW thật; dấu ✓/10 luật local không chứng minh regression theo impact |
| CR6 · Version safety | Chưa chứng minh candidate đọc đúng pin của lượt cũ/mới; Gate0 có TEST fixture riêng đã được nhận |
| CR7 · Rollback | Chưa có ca hoàn nguyên tương thích hoặc xử lý tác động dữ liệu trên các candidate |
| CR8 · Measure | Chưa có baseline/kỳ trước–sau/nguồn số đo tác động của thay đổi; NOT MEASURED |

HMITL/AUTO hiện bằng icon/contract/runtime mẫu; chưa evidence mode switch/MOT output→MOW next step trên candidate này. Full automated test **NOT RUN** theo scope read-only; Gate0 accepted proof giữ riêng.

Chỉ đủ đánh giá lại candidate nối thật khi PM giao phạm vi tiếp và có: (a) cùng MOW ID/version/revision ở library/drawer/graph; (b) Agent tạo/sửa qua cổng được phép, UI refetch đọc đúng, stale/conflict không ghi đè; (c) intent→reuse→draft/thiếu→resume có checkpoint; (d) readiness/diff/test/approval cùng artifact; (e) owner handoff giữ context/quyền; (f) negative path và publish/activate theo gate được mở. Đây là tiêu chí/đầu chờ cho PM, không đề nghị chạy production write ngay.

## 7. Công thực hiện, bảo toàn và giới hạn

**Product code mới = 0.** Không sửa UI, backend, schema, worker/guard, version platform, dữ liệu demo hay KB. Harness local chỉ tải source, kiểm hash, biên tập/kiểm SSOT và đóng gói evidence; kê ở [code-inventory](code-inventory.md). Các thao tác UI chỉ đọc/mở/đóng/chọn view/tìm/checkbox hiển thị mẫu; không gửi đề xuất hoặc đánh dấu test. Không cần cài framework/dependency mới.

Đã đọc AGENTS/incomex-rules hiện hữu và retrieval KB trước khi kết luận. [KB source](governance-documents.json): VPS rules rev2; Constitution4.6.3 rev44; Canvas spec rev1. Canvas spec tự ghi API/DOT spec-only, 6 tầng, khác current preview7 tầng; không dùng nó thay actual. Không làm production PR/deploy/KB label write vì PM chỉ giao read-only và một lần cập nhật local SSOT. [Corrections](corrections.md) giữ lỗi công cụ/harness, không biến false404 thành lỗi ứng dụng.

**Next action duy nhất đề nghị:** GPT Chat/PM xét D03 trên bộ R1 này: nhận hoặc trả sửa đề xuất phân vai “review Nháp2 + library Master + Canvas theo context”, và disposition năm gap; chưa tự mở Gate2/R2–R9. SSOT một lần cuối phản ánh Gate0 DONE / Gate1 DOING / W003 SUBMITTED / O1–O3 NOT VERIFIED.
