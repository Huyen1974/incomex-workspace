# Canonical UI role map — đề nghị PM xét Gate1

R1/D03 đã được PM quyết ngày 10/09. Vai trò R2–R8 dưới đây là đề nghị, không tự nhận canonical implementation. Hợp nhất vào **5 pattern** đã có hình thức hoặc component tham chiếu; không tạo framework UI mới. Một logical Workspace có thể có nhiều URL, nhưng cùng object/context và một nơi giữ business truth.

| Pattern | Vai trò / family | Tái dùng trước | Default và giới hạn |
|---|---|---|---|
| P01 Library/Master | MOW, MOT, MOIT, MOUT, Field/Table, Trigger, Condition, NTGV, Guidance | R1 MOW Master; C01/C02/C06/C09 cùng `master-list.js`; C29/C30 catalog; C34 và S01 SharedDirectusTable; C35 Help | Tìm/lọc/inspect/reuse; Agent dùng cùng nguồn được phép. Không clone Master cho từng object. Đếm có dữ liệu chưa bằng tìm được đúng nguyên liệu. |
| P02 Review Workspace | Mọi Definition và đề xuất | **D03 đã chọn Nháp2 drawer ba câu hỏi**; schema preview C02/C06/C09; NTGV rule table C12/C39 | Người xem có được phát hành, đã nối đủ, đánh giá kết quả ra sao; mở sâu P03/P05 khi cần. Ngoài MOW, việc áp dụng shell này là đề nghị PM. Không lấy số readiness mẫu. |
| P03 Expert Editor | Graph MOW; MOT contract; MOIT layout; MOUT read/query; Field meaning; Table schema; Trigger/Condition Definition; NTGV rule | D03 Canvas/MODW/New MODT; C03/C04, C07/C08, C10/C11; S01 và native Directus metadata UI khi đủ quyền | Mở editor đúng owner và giữ context. C04/C08/C11 chỉ gom capability vào editor chủ quản; không tạo các nơi lưu bản khai riêng. Field/Trigger library còn thiếu mapping UI, không suy chưa có data. |
| P04 Runtime Workbench | HMITL inbox; AUTO monitor; Workflow/Task Instance, Attempt | C05 bố cục HMITL + MOIT/MOUT/Guidance; C40 graph; C32 table presentation; Gate0 worker/adapter là bằng chứng khả thi riêng | HMITL nhập/kết quả, AUTO chỉ monitor/error/result/attempt. Không hiện AUTO thành card bắt bấm Done. C31 là category/Definition list; C32 là technical tasks, chưa phải runtime target. |
| P05 Shared lifecycle/context panels | Diff/impact, readiness/missing, test, approval, publish/activate, version/history, Help, feedback/findings | Nháp2; C12 rule review presentation; C15 feedback; C26 matrix 4 nấc; C27 preview; C28 concept queue; C35 content library; Directus revisions/policies có sẵn | Một cách trình bày và một nguồn trạng thái theo contract. Nội dung/validator vẫn theo object/profile. Không tái dùng `approve → published` hoặc sessionStorage như authority engine. |

Đường mặc định: ý tưởng → Agent giải bối cảnh, tìm/reuse nguyên liệu qua P01 → đề nghị khai báo/thiếu + quay lại → người quyết H1–H5 ở P02/P05 → máy thực thi theo quyền → read-back/refetch đúng revision → P04 vận hành đúng bộ phiên bản. P03 chỉ dùng khi cần chuyên gia. Đây là đường target cần hoàn thiện, **chưa DEFAULT AI-FIRST FIT end-to-end**.

## Ownership review A–F

| Case | Quy tắc role map | Actual evidence / khoảng trống | Kết luận |
|---|---|---|---|
| A MOW → MOT | MOW inspect reference; sửa task mở MOT editor cùng source/return context | R1 link từng về T4 sai context; C03 là nhiều module mẫu | **PASS role map đề nghị**; enforcement/read-back NOT PROVEN |
| B MOT → MOIT/MOUT | Task chỉ liên kết input/reference/result; sửa Definition đúng MOIT/MOUT owner | C02 drawer có MOIT/MOUT code nhưng fallback sample; edit=TSK-0001 vào Studio không tải task | PASS map; current context loading chưa đạt |
| C MOIT → Field | Required/order/layout là form-level; meaning/unit/global constraints thuộc Field owner | C07 widget KIT; C20 ghi owner=GOV-MOIT; C08 mapping tên thành column | PASS map; schema không được sinh từ nhãn; enforcement chưa chứng minh |
| D MOW → Trigger/Condition | Binding tại workflow/step khác reusable Definition, khác runtime occurrence, khác Flow technical config | C04/C08/C11 picker mẫu; C29 có count Trigger nhưng detail thiếu bảng hiển thị | PASS map; chưa có UI chung đọc binding + Definition + occurrence đúng ref |
| E MOT → NTGV/People | NTGV rule dùng People/Role/Delegation; không sở hữu danh tính/quyền; next-step assignee do target MOT resolution | C02 vai 3 forwarder vs drawer delegate; C39 làm thay theo ủy quyền; C36 auth route lỗi | PASS map có ranh giới; **D04 OWNER DECISION REQUIRED** trước thực thi trách nhiệm; source authority chưa xác minh đủ |
| F Runtime | Instance không sửa Definition; attempt/error/retry/handoff theo pinned set và permission | C05 done/revise chỉ memory; C40 mã NV/T mẫu; C31 Definition categories | PASS map; runtime UI enforcement NOT PROVEN |

PASS ở đây chỉ xác nhận đề nghị không tạo competing truth/quyền sửa chéo. Không phải test quyền hay integration PASS. Bằng chứng chi tiết: [structured candidates](structured-candidates.md), [D04](d04-owner-proposal.md).
