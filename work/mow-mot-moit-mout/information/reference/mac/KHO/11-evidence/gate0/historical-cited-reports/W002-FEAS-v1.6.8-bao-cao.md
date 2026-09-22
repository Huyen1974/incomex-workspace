# W002-FEAS v1.6.8 — báo cáo convergence

08/09/2026 · Codex nộp PM · FEAS PM REVIEW / PARTIAL

Đã cập nhật trực tiếp file gốc lên v1.6.8 và kiểm đọc lại; backup nguyên v1.6.7 khớp byte. Đã thu thiết kế về một pilot nhỏ và ghi rõ executable còn thiếu. Đây là bản sửa tài liệu + trace read-only, chưa phải rehearsal thành công.

[Mở file thiết kế gốc](</Users/nmhuyen/Desktop/quy trình/cấu trúc hệ thống.html>) · [Backup nguyên v1.6.7](</Users/nmhuyen/Desktop/quy trình/backup/cau-truc-he-thong-v1.6.7-truoc-convergence-2026-09-08.html>) · [E07: evidence/Flow seed IDs](W002-FEAS-v1.6.8-E07-evidence.json)

**1. W002-FACTORY.** PM ACCEPT / DONE cho architecture baseline v1.6.4 theo chỉ đạo FEAS04. Không implementation/runtime PASS. FEAS vẫn ACCEPT WITH REQUIRED FEASIBILITY CONVERGENCE / PM REVIEW / PARTIAL.

**2. Sáu blocker cũ.** CAT-01 thu về lazy pilot bootstrap, vẫn BLOCKER. CAT-02 và COL-01 ANSWERED về nguyên tắc bounded/lazy, phần proof gộp CAT-01/TST-02; global ontology/cleanup defer. SEA-02 DEFER có điều kiện vì semantic optional. TST-02 giữ bounded benchmark BLOCKER; PERM-01 giữ HARD BLOCKER. RUN-01 và MIG-01 chuyển thành blocker thực thi/platform/operations. Sổ hiện: 20 câu = 10 ANSWERED / 5 DEFERRED / 5 BLOCKER; không dùng nhãn ANSWERED để giả proof đã chạy.

**3. Lazy catalog.** Yêu cầu vật liệu → tìm legacy/current → reuse mapping approved → canonicalize đúng legacy item khi cần → admission nếu chưa có → lưu mapping dùng lần sau. Không dọn toàn kho trước pilot. Đo requested/already-canonical/canonicalized/new/unresolved, human semantic decisions và active human effort. Global N vẫn UNKNOWN nhưng không chặn; chưa tìm hết phạm vi không được gán global identity hay tự publish.

**4. Semantic/vector.** Không còn là prerequisite riêng của Gate0. Primary path thử PG key/alias/normalized lexical + contract trước. Nếu bounded benchmark usable và Decision Queue chấp nhận được thì defer semantic; nếu chưa đủ, TST-02 vẫn blocker và thử reuse Qdrant trước alternative. Không cài extension hoặc đưa Qdrant vào Factory trong lượt này.

**5. Assembly T0–T5.** Một bảng tại #executable-assembly ghi actual primitive, executable/process, state owner và gap/fallback I-level cho đủ sáu năng lực. T1 có PG SQL/Directus API; T2 có Directus/Nuxt WCR candidate; T3 có validation/fixture verifier khác purpose; T4 có WCR transition chưa đầy APR contract. T0 advance và T5 claim→execute→ack: NO REUSABLE EXECUTOR PROVEN. Không dùng tên abstraction để điền process.

**6. Trace bổ sung.** E07: agent-api-executor chạy uvicorn main:app, flags execute=false/real_run=false/dry_run_only=true, /dispatch từ chối REAL_RUN và chỉ trả fixture result trong memory. Cowork MCP→systemd coworkd.py→configured runner agent.py là shell/session transport; adapter dùng filesystem jobs, runner Popen/poll/cancel. Không thấy job_queue/fn_job_/event_outbox reference trong hai source được rà. Docker runner metadata running nhưng top/exec không lấy được task: chưa healthy proof, không kết luận chết. Không gọi dispatch/job hay restart để thử.

**7. Thin-adapter rule.** Thay “thin config” bằng structural test: generic, chỉ chuyển contract, không rule/branching, runtime state, competing truth, approval/assignment/version decision. Generic worker mới vẫn không thin nếu giữ orchestration, kể cả ghi state trong PG. NOT THIN → STOP VS1 → finding. Không giới hạn LOC, không viết worker.

**8. Authority contract.** Tách authenticated_actor, executing_service, on_behalf_of_actor, approver. Server không tin approved_by/actor body; xác thực scope/delegation/current policy tại write/release; audit actor+executor+delegation+approver evidence+correlation. PERM-01 cần allow/deny, chống spoof/escalation, delegation thiếu/hết hiệu lực và audit proof trên môi trường an toàn; chưa claim security vulnerability.

**9. CURRENT baseline.** MIG1 C-S / CP1-S nằm sau CP1 current parity và trước D–E bất kỳ upgrade. L chạy lại cùng VS1/VS1-R fixture/expected trên TARGET. So behavior/human path/native reuse/adapters/permission/save-readback/runtime. Nếu CURRENT dừng vì thiếu executor, ghi đúng điểm dừng; chỉ thử target có giả thuyết built-in cụ thể, không bịa CURRENT PASS.

**10. Clone contradiction.** Hai profiles cùng SSOT: PARITY CLONE theo manifest DB/files/config/source cần migration; SLICE FIXTURE chỉ metadata cần thiết + synthetic records. Lab occupancy/isolation/data handling/secret/egress phải kiểm trước boot. Fixture nhỏ không được dùng để claim full parity; Agent không tự chọn full production clone. Backup/restore trước mỗi upgrade, không chờ M.

**11. First-pilot platform.** PG16 supported current minor + Directus stable target sau rehearsal + Nuxt4 + Node supported, exact pins kiểm trước chạy. Các patch numbers cũ chỉ là candidate từ v1.6.6, không được trình là latest mới xác minh. PG18 N–P là optional post-core; core decision tại M, Q là hồ sơ/addendum, không chờ PG18 để bắt đầu.

**12. Change materiality.** NON-MATERIAL → đường nhẹ/automated checks; COMPATIBLE → impact/test scoped; MATERIAL → version/full material tests/approval; HIGH-RISK → stronger evidence/approval. Alias đổi matching/meaning không tự được xếp nhẹ. Published pins/history bảo toàn. CREATE không né governance; D05 chi tiết đúng Gate3–4.

**13. Relation evidence.** AUTHORITATIVE: canonical typed/hard integrity hoặc accepted equivalent có proof. DISCOVERED: metadata/code/inference chưa hard-proof, chỉ cảnh báo/impact candidate. Không một mình auto-delete/retire/migrate hay kết luận không có nơi dùng. Promotion cần endpoint/type/version/authority/enforcement evidence; query rỗng vẫn giới hạn coverage/quyền.

**14. Flow blast radius.** E07 seed 18 active direct Flows trên workflows/workflow_steps/WCR: 9 DOT-REG và 9 WATCHDOG. Đây là superset theo collection, chưa final slice set. Cần freeze theo action rồi truy downstream/requests/hooks/auth/release/audit và smoke tập đó ở CURRENT/TARGET. Không audit/test cả 128 Flow. Tên Review Gate Enforcement/User Supreme Authority Override thực tế gắn feedbacks/ai_discussion_comments, không đủ kết luận là WCR authority.

**15. License precondition.** PRECONDITION DATA=PENDING trước H; PM kiểm source Directus của exact target cùng dữ kiện doanh nghiệp có thẩm quyền. PM tự kiểm được thì tự giải; chỉ Owner biết thì hỏi trước H và khi đó WAITING OWNER tăng. WAITING OWNER=0 chỉ là chưa có yêu cầu đang gửi, không biểu thị đã đủ điều kiện.

**16. Năm câu hội tụ.** Catalog bounded; authority; exact execution chain; same-slice CURRENT/TARGET; operations clone/backup/rollback. Diễn giải bằng FZ1–FZ7, không FZ8/T6/framework mới. Production-strength/global catalog/PG18/full128/long-wait/scale route Gate5–7.

**17. Gate và phạm vi.** Gate0 DOING; O1–O3 NOT VERIFIED. D1/D2 PM REVIEW/PARTIAL; MIG1, VS1/VS1-R, RULE-SYNC-01 và W003/R1 BACKLOG. Không chạy MIG1/VS1, không DDL/DML/upgrade/deploy production; không mở Agent build.

**18. File/version/backup.** v1.6.8 · 08/09/2026. 477.857 → 487.224 byte (+1.96%); 1.505 → 1.508 dòng. Backup nguyên v1.6.7 đã kiểm khớp byte trước sửa; giữ tất cả 314 ID cũ, 324 ID hiện tại; fragment links hợp lệ, HTML lồng hợp lệ, JavaScript tương tác không đổi. Không tạo file architecture thứ hai; báo cáo/evidence chỉ hỗ trợ file gốc.

## E07 — executable và giới hạn

| Thành phần | Process/entrypoint đã thấy | Điều đã chứng minh / chưa chứng minh |
|---|---|---|
| Directus | node + pm2-runtime /directus | Process sống; không tự chứng minh Factory runtime. |
| Nuxt | node .output/server/index.mjs | Process sống, WCR routes là candidate; PERM-01 vẫn mở. |
| Agent API executor | uvicorn main:app:8090 | Source và config fail-closed dry-run; không claim/ACK PG workflow. |
| Cowork MCP | uvicorn app.server:app:8000 | Frontend shell tools → Unix socket RPC. |
| Cowork adapter | systemd /usr/bin/python3 -u /opt/incomex-cowork/adapter/coworkd.py | Active; JobManager/session files, không Factory checkpoint. |
| Cowork runner | configured python3 -u /opt/cowork/agent.py | Host source shell Popen/poll/cancel; docker top/exec không lấy được task. Runtime health/PG workflow fit chưa chứng minh. |

Source fingerprints và selected line numbers nằm trong E07 JSON. Bounded source scan không chứng minh không còn dynamic caller ở nơi khác. Không đọc business payload/secret, không gọi API dispatch hay Flow; SQL chỉ đọc directus_flows/operations bằng BEGIN READ ONLY + timeout8s + ROLLBACK. Counts là snapshot, không dashboard live.

## E07 — Flow seed, chưa phải final blast radius

Root collections: workflows, workflow_steps, workflow_change_requests, task_checkpoints. Selection: active direct event triggers; task_checkpoints không có direct seed trong query. Trim/expand theo actual slice actions, transitive operations/requests/PG hooks trước MIG1; không kích hoạt lại inactive Flow.

| Flow | ID | Event scope |
|---|---|---|
| [DOT-REG] WCR Delete -> AD | 3a178245-7171-403b-8255-5f0a48e536ce | items.delete |
| [DOT-REG] WCR Update -> AD | 3ca323af-9c65-443c-8ba4-c9b5026bda5a | items.update |
| [DOT-REG] Workflows Create -> AD | 4a3184be-8041-49d9-85c0-36ec3287d027 | items.create |
| [DOT-REG] Workflow Steps Create -> AD | 5644edf7-4ed5-4491-925f-6f90d5fae898 | items.create |
| [WATCHDOG] workflow_steps Update → Changelog | 5b6ccab7-76c2-4111-ab7b-ff46f8c89832 | items.update |
| [DOT-REG] Workflows Update -> AD | 5e99e732-cd8c-4c1f-b146-5361e0a7a689 | items.update |
| [DOT-REG] Workflow Steps Delete -> AD | 68139a34-dcb6-49ea-a072-8e29a9a666cd | items.delete |
| [WATCHDOG] workflow_change_requests Delete → Changelog | 6987e8f7-8f35-4b2c-bd73-18c1b47172cb | items.delete |
| [WATCHDOG] workflow_steps Create → Changelog | 751261f4-135e-45bc-ab0b-dec048716048 | items.create |
| [DOT-REG] WCR Create -> AD | 783986c6-9456-410a-8922-6571e487a585 | items.create |
| [WATCHDOG] workflow_change_requests Update → Changelog | 89dc2e7f-7a6e-4828-987c-1dd62ca7d63f | items.update |
| [WATCHDOG] workflow_change_requests Create → Changelog | 97350a72-64c5-46e2-a1ee-80d245a0465d | items.create |
| [WATCHDOG] workflows Create → Changelog | 9f41e946-4391-4785-aab5-1699b10d5cb9 | items.create |
| [WATCHDOG] workflows Update → Changelog | b9354955-1243-46ba-811d-f7ee2190da86 | items.update |
| [DOT-REG] Workflow Steps Update -> AD | bf831260-78d8-4495-8a5c-052806a74360 | items.update |
| [WATCHDOG] workflows Delete → Changelog | c1d7a9ce-ed5a-4867-8f8d-27065ab60460 | items.delete |
| [DOT-REG] Workflows Delete -> AD | de8d4d70-7578-4635-81c7-dfec12f9238c | items.delete |
| [WATCHDOG] workflow_steps Delete → Changelog | ff9d0a51-ac25-48ef-8be6-a3328b397983 | items.delete |

Các trường hợp tên dễ gây hiểu nhầm: Review Gate Enforcement→feedbacks; User Supreme Authority Override→ai_discussion_comments; Auto-Checkpoint Layer0→tasks. Đây là điều kiện đưa vào blast radius theo actual dependency, không dựa tên.

Nguồn PM: phản biện v1.6.7 do Owner đính kèm lượt này, được lưu tham chiếu FEAS04 trong SSOT. E01–E06 giữ lịch sử ở v1.6.7; E06 8/12 positive Recall@5 vẫn chỉ exact retrieval trên kho nháp, chưa phải kết quả full T1 hoặc lazy pilot.
