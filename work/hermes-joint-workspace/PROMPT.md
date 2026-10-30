# HJW — RUN18: Claude Code CLI KST review PR #358 × PR #357; KHÔNG merge/deploy
RUN_ID: HJW-G8-KST-PR358-PR357-REVIEW-20261030-18
STATUS: FINAL_PROMPT · chỉ hiệu lực nếu GPT Host đã ký READY@full last-touch PROMPT SHA trong HJW COLLAB và Owner chuyển tay. AUTO0 · NO_AUTO_RUN.
Executor_Surface: Claude Code CLI trên MacBook, vai KST đọc và phản biện mã (không Host, không tự phát RUN/READY, không lấy phiếu Claude Chat thay). Host GPT Chat; cross-brand council feedback P470 đã có, REVIEW_REUSED=P470.
Write_Path: HJW STARTED/KQ+Bảng qua Workspace Gateway (Claude `fs_*` hoặc `workspace_*` đang được bind hợp lệ) theo README D12, không ghi GitHub native vào incomex-workspace. GitHub `Huyen1974/agent-data-test`/PR #358, #357 **chỉ đọc** qua GitHub/Git/gh; có thể tạo worktree/branch tạm trên Mac, tuyệt đối không push/merge/đổi PR.
Read_First: root AGENTS.md A0/A2/A5/A6 (DROOT30/31/56/58/60) → root COLLAB.md hiện hành → HJW COLLAB §0/§1–3/Bảng/P458/P468–P475 → PROMPT này → work/github-management/COLLAB.md/GHM_CODE_CHANNEL → agent-data-test AGENTS.md → PR #358, PR #357, evidence RUN16/17.
Source evidence: P474 commit `0e050d44aa3350574f57fbfa34645bc0b7e08124`; PR #358 OPEN/DRAFT, head `4851f6cde86bade6ce70433958cddc76a307f9f1`, base main `b4c9ea19cf2e57594a231c2819e098fe0002c99a`, 6 files, 89 main-based + 90 live-overlay tests, gate SUCCESS run `40990592102`. PR #357 OPEN/DRAFT head `36c682914c9f412078113b6d85319f11356d1130` and changes `workspace_tasks.py` overlapping. VPS Agent Data code `1cc706dc0f1ba7ef05f4631c04f604d2cacd9982`, image `sha256:4635e417e5400a9f85d1ed569f1c2f977845405bf7b8d834ab7002006f7d1045`, 4 worker. FS/helper G8 candidate PASS P468/P469, still no production deployment.

## 1. Mục tiêu và hàng rào
**Một việc trong RUN18:** KST **review độc lập PR #358 và cách hợp nhất an toàn với PR #357**, kiểm tính đúng đắn của 4 facts trên nền queue mới, trả quyết định có bằng chứng và đường sửa nhỏ nhất nếu có. Không tính review là merge-ready hoặc G8_SYSTEM; còn Linux image rebuild/rollback AD, real client C1/C2, advertise/enforce. Không kiểm lại 89/90 fixtures chỉ để điền PASS; kiểm trọng điểm có rủi ro.

**CẤM TUYỆT ĐỐI:** không push/merge/rebase remote, không đổi PR #357/#358, không đánh dấu ready-for-review, không ký `KST_ACCEPT@SHA` với nghĩa cho merge, không chạy `deploy-vps.yml`/CI rerun, không GitHub→VPS, không đổi live image/worker/queue/secret/Guard/baseline/code ledger/Hermes/Gemini, không thao tác PG/Directus, không mở task mới. `.github/workflows/deploy-vps.yml` ở main có trigger `push main` cho `agent_data/**` và script rsync xuống VPS; chưa chứng minh workflow bị vô hiệu hoàn toàn ⇒ **cấm merge dù PR gate xanh**. Không cần VPS-GHI vì 0 VPS write.

## 2. INPUT READY (Host đã đo) / DROOT60
- H1 repo/read path: GitHub repo private active, PR358/PR357 tồn tại OPEN/DRAFT, HEAD/base pin như trên, 6 file PR358, 4 file PR357; GH KST code lane trước đó có thật (PR357 do Claude Code CLI viết). Đường HJW Gateway đã dùng P468/P474. Tại S0 KST chỉ recheck freshness của GH read/Workspace.
- H2 ranh giới: PR #358 chỉ sửa 2 module contract mới + `workspace_idempotency.py`, `workspace_tasks.py`, `workspace_tools.py`, `workspace_transfer.py`; PR #357 sửa `workspace_execution.py`, `workspace_runtime.py`, `workspace_tasks.py`, test queue. Giữ `AGENT_INFRA_TOOLS`/Hermes trong canonical main, không bật nó từ runtime image.
- H3 CI: gate của PR358 trên đúng SHA SUCCESS đã thấy ở GitHub Actions; **chỉ kiểm lại HEAD freshness**, không giả G8 full hoặc độc lập review đã xong.
- H4 năng lực/chi phí: Mac review Git/diff + targeted Python/SQLite fixture offline; không Docker daemon Mac, VPS RAM có lúc ~4.2GiB nhưng swap gần đầy ⇒ không build image nặng trên VPS; CI/bare Git/pytest nếu thiếu tool tại thời điểm RUN = EXECUTOR_FRESHNESS, không tự mở kiến trúc khác.
- H5 Owner P458: 4 logical facts (AI product, AI source environment, task, command_ref) với raw/canonical/provenance, missing guidance, alias mềm, auth/A2 unchanged, upload/queue/replay; `operation_id` là idempotency, không phải RUN authorization. PR #357 live queue must preserve durable idempotent/supervisor/restart behavior. Source/review refs đủ; 0 HOST_UNVERIFIED; test/merge-tree outcome mới đo khi thi hành.

## 3. KST thực hiện gọn, một lượt ≤15 phút/checkpoint
**S0 · one read-gate (chỉ đọc):** gh/GitHub đúng repo & refs, HJW READY SHA/STOP/STARTED, HEAD #358/#357/main chưa thay; nếu có HEAD đổi, diff nhanh và xét scope mới, không tiếp tục bằng SHA cũ. Không làm precheck RUN khác; ghi STARTED theo DROOT31 trước công việc chạy.

**S1 · kiểm độc lập mã:**
1. Rà chính xác 6-file diff PR358, schema/tool descriptions, `declaration_contract.resolve`, `workspace_declaration.call/target`, trusted server context, alias/command_ref/operation_id, auth before declaration, scope/target_task, upload begin/append/commit, queued writer và helper receipt; kiềm chế quyền. Đặc biệt kiểm tool bị phân loại NON_SOURCE có làm mutation logic nào lọt gate hay không, sai/task path mơ hồ có 0 mutation thực không, và default advertise/legacy write.
2. So với PR357: `workspace_tasks.py` P358 dùng `find_by_operation/q.enqueue` cũ, P357 dùng `enqueue_once` atomic và supervisor recovery. Không để rebase/merge xoá P357 queue logic, idempotency cross-process/replay after finished hoặc `_declaration` carrier. Kiểm PR358 SHA vẫn exactly 6 paths, không đổi Hermes/ACL/tool catalog.
3. Tạo một **bản tích hợp tạm chỉ trên Mac** (local `main+PR357+delta PR358` hoặc git merge-tree+scoped patch, no push) và chạy tối thiểu tests HJW RUN17 + queue PR357 liên quan: 10 accepted/4 running/6 waiting/10 replay/0 dup, conflict same operation_id different facts, restart/supervisor liveness nếu fixture cho phép. Thử read/write/legacy, upload/queue, auth negativity. Nếu chạy test không thể vì thiếu Python deps ⇒ review static có chỉ rõ UNTESTED, không đánh PASS giả; không giữ Codex/Owner chờ.
4. Nêu rõ **thứ tự tích hợp đề xuất** và diff kiểm trước merge sau này. Hiện PR357 DRAFT DO NOT MERGE, PR358 cũng DRAFT; code review PASS không phải permission merge. Cần kế hoạch tích hợp khi Host+Owner chốt đường deploy/cắt nguồn riêng.

**S2 · KQ và đóng, không thêm code task:** Trong `work/hermes-joint-workspace/COLLAB.md` ghi P476/KQ + update Bảng, evidence hẹp `evidence/run18-kst-pr-review-20261030/` nếu cần; đính kèm pinned PR SHA+base, từng hunk rủi ro, kết quả test thực, 1–3 sửa tối thiểu hoặc PASS, tình trạng Gate, đề xuất node G8_AD_LINUX_REBUILD/ROLLBACK sau khi source tích hợp. Có thể ghi một bình luận review **COMMENT (không APPROVE)** vào PR #358 với same pinned SHA nếu chính Claude CLI có đường GitHub phù hợp, nhưng không bắt buộc và không thay COLLAB. Nếu blocker thì `KST_REVIEW_NEEDS_FIX` và mô tả cụ thể; nếu đủ thì `KST_CODE_REVIEW_PASS_SCOPED_BUT_NO_MERGE`; không báo full system PASS. Ghi KQ/đóng RUN; dọn worktree Mac (không đụng branch HJW/GitHub remote), không background process.

## STEP_WALK_V1
| Bước | Actor/trigger | Evidence | Hỏng/tiếp |
|---|---|---|---|
| S0 | Claude Code CLI, Owner dispatch sau READY | exact PR SHA, HJW gate, git/gh read | HEAD drift → diff+KQ hẹp, không chờ Owner hay mutate |
| S1 | KST một lượt đọc/test Mac | 6-file review, integration PR357+358 local, queue/negative+receipt tests hoặc UNTESTED nêu lý do | phát hiện bug → exact hunk+fix tối thiểu, không push/merge |
| S2 | KST đóng trước hết lượt | P476 KQ, Bảng, evidence+decision, no live change | Host xem xét bước Linux rebuild/roadmap, không auto RUN |

**Không biến thiếu Docker/review khác hãng/CI pending thành S0 blocker; chỉ báo phạm vi thật đã chứng minh.** No app/server restart.
