# PROMPT — VPSC2-RAG-A-TRUST-GATE-20261023-01

DRAFT — KHÔNG RUN. Claude Chat Reviewer kiểm và ACCEPT đúng full SHA last-touch của PROMPT.md, GPT Host ký READY cùng SHA, Owner dán cho Claude Code CLI mới thực thi.
RUN_ID: VPSC2-RAG-A-TRUST-GATE-20261023-01
Executor_Surface: Claude Code CLI trên Mac Owner.
Write_Path: Incomex workspace_* root=workspace cho STARTED/KQ/COLLAB; VPS1 mã nguồn SSOT qua đường mutation đã duyệt, incomex-config-apply-v0/Config Guard, DOT wrapper hợp lệ; không bypass gateway/Guard.
Đọc AGENTS.md → root COLLAB → work/vps-clean-20-10-26/COLLAB.md §0/Bảng/P13/P14 → PROMPT.md → BAO-CAO-Agent-Data-RAG-2026-10-23.md commit 3ff49530. R3 load audit trước là DRAFT SUPERSEDED_UNRUN, không chạy.

MỤC TIÊU NODE RAG-A: sửa sự thật/độ tin của báo cáo audit và trạng thái integrity, đồng thời làm rõ lỗi đồng bộ qua logs có định danh; chuẩn bị manifest để RAG-B làm retry/reconcile. KHÔNG sửa, xóa, tự reindex, tự heal dữ liệu/vector/PG/Qdrant production trong node này. Không tuyên bố RAG_DATA_CLEAN hoặc GO_PRODUCTION.

S0 READ GATE (≤10 phút): đúng roster/quorum, Claude ACCEPT+GPT READY cùng SHA, không STOP/STARTED trùng, root VPS-GHI CAS nếu có mutation; có owner/target chưa rõ hoặc cờ bận ⇒ KQ DỪNG, không chờ. Đọc PRE container release/image digest, source 31-file hash, Guard fleet IDs/count thực tế, ConfigGuard target baseline, backup/rollback known-good. Ghi STARTED/Bảng ở task khi gate PASS; giữ lease chỉ trong mutation. Không làm hỏng dịch vụ đang dùng.

S1 REPRO STAGING ISOLATED (≤25 phút, không sửa production data): xác nhận trực tiếp mã đang chạy của dot-vector-audit, server.py data integrity, vector_store.py và pg_vector_listener.py; không dùng Git mirror thay runtime. Test âm ở bản sao và công cụ hiện hữu:
(a) Qdrant/PG sai auth/timeout => audit ERROR/PARTIAL + exit nonzero, không "Orphans=0,Ghosts=0" giả.
(b) Duyệt cả production_documents và iu_core_iu_chunks; blank document_id hiển thị điểm còn thiếu; IU không đọc được nguồn => UNKNOWN, không PASS.
(c) 2 orphan IDs + 1 source thiếu vector + comment2430 phải được liệt kê/classifier rõ, không auto-embed theo extension.
(d) Qdrant delete timeout và vector_store.search backend failure phải log action/document/error_class/time/release an toàn, phân biệt NO_RESULTS với BACKEND_ERROR.
(e) /health process liveness giữ nguyên contract với Docker/Kuma; integrity warning và retrieval degradation hiển thị riêng, không tự 503 toàn bộ health làm restart/đèn đỏ giả.
Nếu staging negative FAIL hoặc không có capability/backup rollback => DỪNG trước mutation, không tự nới cổng.

S2 PATCH HẸP, INDEPENDENT (≤35 phút):
A. Audit/DOT: fail-closed khi auth/upstream lỗi; báo số ID rỗng, orphan/ghost đúng các nguồn hợp lệ; IU source chưa đọc được phải PARTIAL; classifier không suy path thiếu extension là directory; auto_heal=false giữ nguyên. Không đổi PG/Qdrant vector, chỉ đọc để kiểm. Sửa code theo đường DOT approved/ConfigGuard; không có đường an toàn => SKIP A.
B. Agent Data diagnostics/health: giữ process liveness, công bố integrity warning và lỗi vector sync đúng trạng thái; structured log action, doc identifier an toàn, exception type, mã phiên; không coi backend failure là empty normal. Backward-compatible client contract và negative tests. Không thêm queue/schema/cron/monitor, không sửa sync/delete/upsert semantics trong node A; phần retry/outbox/chunk tail để RAG-B sau review riêng. Nếu code path cần build/deploy, chỉ source đã xác nhận, image known-good, stage smoke, single service replace/restore theo official path, full Guard/rollback; nếu cần phá hợp đồng, SKIP B không cố triển khai.
Áp dụng từng nhóm đúng target protected với beforeimage, hash, rollback và bằng chứng; 4 ô Điều 30/31; tuyệt đối không biến patch kiểm toán thành bulk RAG mutation.

S3 POST (≤15 phút): kiểm thật audit read-only auto_heal=false trên hai collections, EXPECTED_FINDINGS vẫn còn (2 orphan IDs, 9 blank points, source thiếu vector/comment) và phải DRIFT/PARTIAL chứ không ép clean; IU cần source match thực hoặc UNKNOWN. Audit lỗi auth ở bản sao phải exit nonzero. Health liveness OK nhưng integrity phải báo cảnh báo, sync errors có trace. Source/runtime/image hash khớp, Guard PRE/POST và ConfigGuard CLEAN, Kuma theo monitor ID, backup cũ nguyên; COUNT/CHECKSUM Qdrant/PG không thay do RUN. Lỗi mới do RUN => rollback đúng nhóm, ghi PARTIAL/DỪNG. Không giả chứng minh live-negative khi chỉ test staging.

S4 KQ (≤10 phút): ghi COLLAB/Bảng duy nhất trong task với A/B APPLIED/SKIP, sha/rollback, guard, integrity/health evidence, no_data_mutation. Ghi RAG-B next với kế hoạch retry/outbox durable (cấm thêm schema khi chưa duyệt), idempotent delete+upsert+shortening, manifest chính xác 2 orphan, 9 blank, 1 ghost, comment2430, IU141, sample diff; RAG-C phục hồi backup PG/Qdrant 2 collections/config ACL và client retrieval eval. Từng thay đổi dữ liệu phải được Owner duyệt đúng đích sau review. Trả VPS-GHI, không để container/temp/process nền. Các lỗi CountRefresh, context-pack-verify, 503, snapshot thuộc chủ khác, không sửa chéo.

STEP_WALK_V1:
| Bước | Ai | Trigger | SLA | Evidence | Fail/Next |
|---|---|---|---|---|---|
| S0 | Claude Code | Owner RUN sau READY | ≤10′ | accept/ready SHA, VPS-GHI, PRE & rollback | Gate fail => KQ DỪNG |
| S1 | Claude Code | S0 PASS | ≤25′ | negative staging 5 ca, 0 prod data change | Fail => DỪNG trước mutation |
| S2 A/B | Claude Code | S1 PASS | ≤35′ | protected patch/tests, rollback per group | SKIP/rollback từng nhóm |
| S3 | Claude Code | sau S2 | ≤15′ | audit DRIFT đúng, health, Guard/Kuma, data unchanged | red mới => rollback |
| S4 | Claude Code | sau S3 | ≤10′ | KQ/Bảng, clean process/tmp, release VPS-GHI | Host nhận KQ |

Một dòng Owner: XONG|DỪNG · VPSC2-RAG-A · Audit=A/SKIP · Health=B/SKIP · prod_data_changes=0 · Guard/Kuma · VPS-GHI release · commit.