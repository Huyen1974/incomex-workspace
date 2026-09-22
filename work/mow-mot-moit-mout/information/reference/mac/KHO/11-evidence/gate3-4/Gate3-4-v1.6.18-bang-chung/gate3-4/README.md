# Gate3–4 — Agent mới đọc từ đây · v1.6.18

**W005 Revision2 đã nộp: BLOCKED BY DATA-AUTHORITY.** Gate3/4 DOING/PARTIAL; Gate5–7 NOT STARTED; O1–O3 NOT VERIFIED. D08 DECIDED PM: “Ghi nhận thời lượng xử lý”. D04 WAITING OWNER. Phiếu B Platform ACCEPT WITH FOLLOW-UP. Đây là bằng chứng/bàn giao; [cấu trúc hệ thống](<../cấu trúc hệ thống.html>) là SSOT duy nhất.

## Đọc ít, đúng việc

1. Owner: [báo cáo12 ý để dán vào Chat](BAO-CAO-GUI-PM.md) + [một ZIP gửi kèm](../KHO/11-evidence/gate3-4/Gate3-4-v1.6.18-bang-chung.zip).
2. Agent/PM: [REVIEW](REVIEW.md) chỉ rõ6 gap, nguồn/counterexample và đề xuất nhỏ dùng native trước; [matrix177 fact](data/pilot-critical-matrix.json) chỉ đọc các dòng liên quan.171 mapping trong LAB không phải171 authority production;119 proposal logic chưa được nhận.
3. Supervisor: [đầu vào review](SUPERVISOR-REVIEW-INPUT.md),10 raw files,5 câu PASS/FAIL và lệnh replay. Không cần đọc toàn bộ transcript trừ khi kiểm một claim.

**Việc kế tiếp:** PM/supervisor xét gói và chọn phạm vi khép Task/Context/consumer. Chưa chạy Formal Gate5 hoặc dựng engine/UI mới. Một quyết định D04 không tự giải6 gap kỹ thuật. [Plan Gate5](GATE5-PLAN.md) đã chuẩn bị, chưa chạy. Nếu sau này đóng Gate3/4 theo Pilot, mở lại lazy cho mỗi family mới.

## Bằng chứng đã đóng theo thứ tự

| Bước | Kết quả / nơi mở |
|---|---|
| 01 · Archive |9 ZIP lịch sử/hash; SSOT external Codex href209→0. [Result](evidence/01-archive/result.json). |
| 02 · Freeze |172 fact trước mapping; thêm5 ở bước05,0 bị bỏ. [Frozen set](evidence/02-freeze/pilot-critical-set.json). |
| 03 · PG Intent→Draft |2 phiên mới reuse12 Version, Draft/WAIT; P01 đọc lại sau Làm mới. Prompt/transcript/PG/metrics/[runbook T0](evidence/03-intent-draft/T0-RUNBOOK-CANDIDATE.md). |
| 04 · Missing/resume |2 phiên mới gắn Condition đúng parent/slot/revision;4/4 negatives sau sửa native. [Result](evidence/04-missing-resume/result.json). |
| 05 · Readiness |7 mục ×2 bước, đúng MOT/MOUT ownership;14 dòng generic UI. HMITL synthetic, chưa readiness full runtime. [Result](evidence/05-readiness/result.json). |
| 06 · Machine |Compile/test16/16 tại Draftrev3; output thiếu rollback/noACK sau sửa guard. [Result](evidence/06-machine-test/result.json). |
| 07 · Lifecycle |32/32 quyền/runtime; frozen17/17; native Publish/Activate tách nhau. [Result](evidence/07-lifecycle/result.json). |
| 08 · Feedback/V2 |Integer feedback1→V2 ngưỡng90, V1 immutable;17/17 +6/6. [Result](evidence/08-feedback-v2/result.json). |
| 09 · Data |C04 Search/IO refs khai báo lại, V2rev2/test17/17; shape40 profiles116/116;177 facts/6 gap, không exit. [Result](evidence/09-data-lock/result.json). |
| 10 · Bàn giao |Export, cleanup, code/SSOT QA, one-write receipt, exact snapshot, manifest. [QA](QA.json). |
| Replay |[Lần chạy2 phiên ở lab mới](evidence/replays/proof-g34r2-replay-20260911094208-58c626/result.json); chỉ head/WAIT, không replay lifecycle/UI cuối. |

Mỗi bước giữ manifest tại thời điểm đóng, cả lỗi đầu/lần sửa/rerun. Kết quả cũ trong từng bước là lịch sử đúng revision; current machine TEST **fda153af-8158-4558-bea5-c1f06486927d**, V2 **ca51f9b9-2cb2-4a89-b081-43927711709c revision2**, closure **70c6658c9f3de73ffe25de5fd97cd29583f955c9eece289db5dd56c32e031b70**. Approval probe cuối đã revoke; V2 chưa Published/Active.

## Danh mục thư mục

| Nơi | Nội dung / quy tắc đọc |
|---|---|
| `BAO-CAO-GUI-PM.md`, `REVIEW.md` | Báo cáo Owner và phân tích giới hạn hiện hành; không phải hai quyết định riêng. |
| `summary.json`, `QA.json` | Kết quả có cấu trúc và self-QA A–K; không independent acceptance. |
| `PLATFORM.md` | Phiếu B giữ findings v17, không research lại; adoption follow-up riêng. |
| `GATE5-PLAN.md`, `SUPERVISOR-REVIEW-INPUT.md` | Điều kiện thử chính thức và cách kiểm lại; chưa giao chạy Gate5. |
| `contracts/` | Contracts/native Joi descriptions/cases;40 portable profiles khác mẫu số32 PG profile rows. |
| `data/` | Matrix177/authority/relation current; `contract-data-matrix.json` chỉ trỏ matrix385 lịch sử, không đọc311 UNKNOWN ngoài Pilot. |
| `evidence/01-*`…`10-*`, `evidence/replays/` | Raw theo bước, prompt/tool/PG/source/config/counterexample; manifest giữ trace. |
| `proof/rev2/` | Guard cuối, compiler/harness/config declarations/replay; [PLAN](proof/rev2/PLAN.md) phân biệt source và thứ tự. `ui-reused/` chỉ3 source snapshot đã có. |
| `proof/` ngoài `rev2/` | Baseline v17 cần cho head replay, worker105 dòng và UI transport; không dùng script lịch sử để ghi đè matrix/current. `runtime/dependencies.tar.gz` cần replay. |
| [KHO/11-evidence](../KHO/11-evidence/INDEX.md) | ZIP niêm phong + file được dẫn đã giải nén. [v17](../KHO/11-evidence/gate3-4/Gate3-4-v1.6.17-bang-chung/gate3-4/README.md) giữ raw cũ đã được PM nhận bounded. |

Lab chính/replay và local UI/tunnel đã dọn sau export; không lab sống để tiếp tục lệnh cũ. Không production DML/DDL/deploy/restart, không Run Script Flow, per-workflow code hoặc page Pilot mới. Guard vẫn I6 code cần bảo trì, harness/config không được tính là “code mới0”. UI cần Làm mới; phiên resume khởi chạy thủ công; chưa T0 dispatcher, full HMITL→AUTO hay before/after kinh doanh.

Đã dọn cache, private files, node_modules/build và bản raw v17 trùng sau đối chiếu ZIP/hash; không xóa workspace nguồn hoặc bằng chứng duy nhất. Mỗi nhiệm vụ sau phải cập nhật SSOT/README/báo cáo cùng lượt; không tạo sổ trạng thái song song. ZIP là review bundle, không bản website tự chứa toàn bộ kho lịch sử; HTML snapshot giữ nguyên relative project links.
