# PROMPT — GS-CLEAN-WRITE-20261020-01

## 0. CONTRACT · ONE RUN · OWNER AUTHORISED · GUARD-FAIL-CLOSED
RUN_ID: GS-CLEAN-WRITE-20261020-01
Task: `work/graph-server/` · mốc GS-CLEAN sau R10, trước R10B; **duy nhất dọn 7 trial folders DS1–DS7 + 2 restore-check log volumes DS8–DS9**.
Executor_Surface: Claude Code CLI **phiên mới trên Mac**, Owner tự dán RUN.
Repository Write_Path: Incomex MCP full all 2 `workspace_*` root=`workspace`; read status/root via same gateway; VPS mutations chỉ qua SSH/approved existing commands đúng phạm vi; Drive dùng **cổng rescue hiện hữu** và GPG/GSM hiện hữu, không thêm tài khoản/công cụ/timer/worker mới.
Review: Claude Chat P158 `ACCEPT` nội dung W1–W8, nguồn P156 `b4aef9a`, GPT Host B3 P159, Owner trực tiếp cho phép DS1–DS9. **READY@full last-touch commit of THIS PROMPT phải xuất hiện tại Graph COLLAB P159, rồi Owner dán RUN; READY không tự là RUN.**
STATUS: HOST DRAFT UNTIL P159 READY · no executor may treat this file alone as authorisation.

**Chỉ đạo Owner nguyên văn trong chat:** «Đồng ý xóa cái này: | Thư mục thử + 2 ổ log thử | 9 | Dọn sau khi anh gật». Owner cũng chuyển nguyên dòng quyền: «Tôi (Owner) gật xoá DS1–DS9 đúng danh sách P156/P158 theo SHA trên, sau khi lưu Drive mã hoá và giải mã thử PASS.» **Quyền này chỉ giới hạn tập DS đã khóa và điều kiện Drive encrypted + readback/restore**; không miễn Guard/không cho xóa ảnh đang chạy, 3 log volume production, R9/R10 evidence, backup hay bất kỳ đồ khác.

**Danh sách khóa:** DELETE_SET_SHA256=`f98de1e8e2f334593aec72a00f3d53fd35d967a1815b7e88f2e78a2e3f77b6be`, canonical UTF-8 **1727 byte**: 9 dòng xếp DS1→DS9, mỗi dòng `DS_ID<TAB>absolute-path-or-volume:<full-id><TAB>allocated-bytes-int<TAB>tree-sha256<TAB>meta-sha256<LF>`, không header, dòng cuối có LF. Host đã tái lập và tự kiểm SHA của đúng 9 dòng P156/P158; **executor phải tính lại SHA256 tại S0 bằng bytes, không tin report.** Không dùng tên rút gọn/wildcard. Nếu khác SHA ⇒ `DELETE_SET_IDENTITY_MISMATCH`, DỪNG **trước mọi mutation**.

```tsv
DS1	/opt/incomex/work/graph-server/runtime/run1	1168302080	82de36d03e10507c140c1b0d56ea5db32df22f7df5d2e6df51c138c678413a08	b69eb8e403bb316a9fc8bc98797dc9a39e48a1f4b693a2cf48939d344a5ec5e7
DS2	/opt/incomex/work/graph-server/runtime/r5	615952384	95f5d401a4faaa640d062bbc828a7012da13459a7ddf0fe946a956a27457242b	27d3b889abce3162bed8b6c0be72037a69927f7e23a1af4ebdca49416a03dd3e
DS3	/opt/incomex/work/graph-server/runtime/r6c	548192256	72181da3b2a20151ac28242efcc26f9a5276b463d916fb2acb351467ab3549cc	c3f9c8fc403d6d7e89fe201ba6e700f613c8fa47256ff5c3aeccefb0e93ad9f8
DS4	/opt/incomex/work/graph-server/runtime/r6d	542724096	8ba25f2ed6f209102bd0eba63b392b5412575f650cd2977908c628a265957b2d	b0e814d320fa9cdcdbfd566a288ae42b0509e14639b8da4a77bb93a4a40e8134
DS5	/opt/incomex/work/graph-server/runtime/r6e	3596288	ad290102f4718d2bd497f282aacbf8087042dc2f4a765919a00119b223684c98	ca972c056a13c5fe0bedc335ff471bd7e21aed6d6031483c1110139587463547
DS6	/opt/incomex/work/graph-server/runtime/r6b	40960	4ece9324e928b3fb4afa5a51fa9f943aaec6704749cdf90ea7692d7bbb56c371	df4c51ff31b71c3c77760108aa1813941871bd38f3ed140314c3e05474cc8e83
DS7	/opt/incomex/work/graph-server/runtime/r6b0	49152	1ab3ad5c2a09bec9956b1a3a6089e27e2f65be10314c26edd0fdee005cbf40e4	d357a1cbf4fe139f0254a1ee0157f9cf6c672c091713082b931a46e7f93bcd81
DS8	volume:953f6b499ec078e7fcc89785df72a125ff56b6e30968bac2cbfea860eef5d7f3	106496	6e78749efa3fb1a82c2c1c1ad4714c8ffacefd593123dfc56a3935611d9646c4	4d2605cb60e98b2d2fc66addb8c1e3c2b4a14e27114c064040e5551cbd2a14e6
DS9	volume:b11795c7c9616de6c568f160a361e706ccd25e80c648578ed989e98de2b2995a	106496	9a4ce5243325e43b75422ec176733639122113e810ae18ca1a1fbf4cdfbdab4a	41580799293bdb5e7f1e0ac46b00494835160efe188aaea6f26f0b6742f84ac8
```

**KEEP bất biến dù không nằm trong bảng xóa:** Neo4j production `incomex-graph-neo4j`/volume `incomex_graph_v1_data`/journal; `prod-v1`, `mcp-readonly-v1`, code ledger/compose/rollback/backups; images I1 Cognee `sha256:db0973f4...` (pinned builder) và I2 Neo4j `sha256:d9cfe829...` (running); volumes log V1–V3 production (P156 có 3 tên FULL); **16 evidence folders, đặc biệt R9 `EVIDENCE.sha256` 99/99 và R10 `EVIDENCE.sha256` 41/41 + private alias/receipts/brief**; nguồn R10B. Nguồn bí mật phải giữ riêng; không được gửi plaintext secret/PII lên Git/Drive hoặc in stdout.

## 1. W1 · S0 HARD GATE & AUTHORITY
1. Đọc `AGENTS.md` A4/A5/A6, DROOT30/31/45/54/55 → root `COLLAB.md` (VPS-GHI, STOP, shared lease, điều khiển đa RUN) → `work/graph-server/COLLAB.md` §0, GS-RM1, P145, P150–P159 → `PROMPT.md` hiện hành. Đo binding `workspace_*` root workspace, HEAD/version, **last-touch PROMPT SHA đúng Host READY P159**. P158 reviewer ACCEPT W1–W8; Owner GẬT DS1–DS9 và hash phải có **nguyên văn trong khối Owner dán**. Thiếu quyền bất kỳ ⇒ DỪNG, không giả đã gật.
2. READ-only S0: bang-den **22/22 xanh**, #11 GREEN, Config Guard CLEAN, INV20/22/23 PASS, Graph `graph-v1 status` + read-only baseline 3596 nodes/6823 edges và Base88 614/611/151/128, 5 protected pins; source R9 99/99 và R10 41/41, D23 Drive/GPG availability, disk MemAvailable và disk free đủ làm từng gói; 0 STOP_REQUESTED/COUNCIL_ALERT, 0 incompatible RUN/lease, root VPS-GHI trống. Đọc các DS chính xác và tính lại manifest 1727 bytes/SHA; chỉ nguồn P156/P158, không tự discover/delete khác. **Không gọi `watch --guard` ghi state khi chưa có khoá.**
3. **W2/lease:** Sau read gate, dùng `workspace_transaction` CAS/expected_head để ghi **VPS-GHI giữ RUN_ID + STARTED@${runId}** trong cùng commit (DROOT54), chỉ sau đó mới tạo staging encrypted receipts và chạy Guard PRE/stateful. Lease không lấy được ⇒ DỪNG an toàn, không polling/chờ. Không để các mutation cùng VPS chạy xen. Nếu DROOT30 freshness đổi/STOP, nhả khoá trong cùng KQ DỪNG. Từ lúc giữ khoá, log bước ở đúng Graph COLLAB, metadata ngắn, không tạo file báo cáo/progress ở Git.

## 2. W3 · IDENTITY + SECRET COMPLETENESS, BEFORE ANY ARCHIVE
Với mỗi DS *riêng biệt* theo thứ tự:
- Kiểm canonical absolute path/64-hex volume name, không symlink ngoài scope, không mount production, không special file/device, không bind/container-use. Ghi lại `tree` (SHA256 danh sách `relpath<TAB>sha256(file)<LF>` sort byte) + `meta` (`relpath<TAB>size<TAB>mtime_ns<LF>` sort byte), total size/count; so **đúng SHA P156 của chính DS**. SHA sai hoặc object content thay ⇒ `HOLD_IDENTITY_MISMATCH`, không đóng gói/xóa DS đó.
- Bốn `secrets/` nhỏ trong trial: **KHÔNG in plaintext, không copy nội dung ra Git/chat/file tạm bền**; hash in-memory (metadata digest), đối chiếu **số dòng tree = toàn bộ regular files thực tế gồm hidden/secrets**. Kiểm tệp duy nhất còn đang cần bởi prod/GSM/key idempotency/rollback bằng **metadata/ownership/reference** an toàn, không đọc xuất nội dung. Nếu script tree excludes secrets, sole recovery hoặc file chưa chứng minh, `HOLD_SECRET_INCOMPLETE` đúng DS. Có thể chạy các DS còn lại.
- Gói `tree/meta` trong P156 là checksum trạng thái khảo sát, không là giấy chứng nhận dữ liệu tuyệt đối an toàn. **Không được tự sửa SHA approved để cho PASS**. Mỗi lệnh nặng có `timeout`; không dùng lệnh kẹt kiểu `sort > /dev/stdin`.

## 3. W4 · FINAL REFERENCE GATE BEFORE ARCHIVE AND BEFORE DELETE
Đo lại references của DS chính xác (Docker running **và stopped**; `docker inspect`, volume mounts, bind mounts, symlinks, open handles; systemd/cron/compose/Code Ledger, protected `prod-v1`/scripts/rollback, Snapshots, restore-check). Mọi target vẫn còn dùng/sole copy/không chứng minh được refs ⇒ `HOLD_REFERENCED_OR_UNKNOWN`, **KEEP**, không bẻ hard guard. Ngay trước local DELETE đo lại lần nữa, không dựa tình trạng trước upload. Production I1/I2, V1–V3 và evidence là **cấm xóa tuyệt đối**.

## 4. W5 · WHOLE-ITEM ENCRYPTED DRIVE ARCHIVE & TEST RESTORE
Chỉ DS vượt W3/W4 mới được backup. **Mỗi thư mục DS1–DS7 = một gói nguyên vẹn**, gồm cả hidden files, secrets (nếu có), symlink metadata/owner/ACL khi phù hợp; mỗi DS8/DS9 là một gói từ đúng Docker volume `_data`. KHÔNG xóa riêng bất kỳ `neostore.transaction.db.*` nào. Tránh `tar` dereference/follow symlink ra ngoài.
- Dùng GPG người nhận D23 đúng key ở GSM, chỉ nạp key tạm vào tmpfs, không in key/secret; **stream tar→GPG**, không tạo archive plaintext/secret trên disk bền. Dùng **Drive rescue existing infrastructure** với nhánh xác thực, tên gói deterministic RUN_ID/DS, không mở dịch vụ hoặc backup stack mới. Không upload chưa mã hóa. Chứng minh remote upload có ID/sha/md5 provider, đọc ngược bản remote/tải về và so SHA256 ciphertext với local source. Bản Drive phải độc lập, có quyền và không sắp hết hạn trong phạm vi recovery.
- **Trước DELETE**, giải mã thử bản *tải từ Drive*, giải nén trong tmpfs sandbox riêng giới hạn tài nguyên, đếm đủ files, tính lại tree SHA256 bằng bytes và đối chiếu với tree P156 gồm đầy đủ tệp secrets (không in file); kiểm đường restore về đúng absolute path hoặc recipe tái tạo Docker volume. Không tạo volume prod hay viết Graph để thử. tmpfs không đủ/không đảm bảo isolation ⇒ **HOLD DS**, không fallback plaintext lên disk bền. Dọn decrypted tmpfs/temporary encrypted staging theo quy trình an toàn; giữ bản trên Drive. **Chỉ coi `ARCHIVE_RESTORE_PASS` khi đã có remote readback + decrypt/test restore + hash + filecount + identity proof**; checksum upload một mình KHÔNG đủ.
- Nếu một DS bị HOLD, tiếp tục DS khác **chỉ khi** tài nguyên/Guard/shared lease vẫn an toàn; không chạy nền, không để lại staging không rõ. Không mở rộng scope sang các data của Graph production.

## 5. W6 · EXACT DELETE AFTER ALL PER-DS PROOFS
- Ngay trước khi xóa mỗi DS: fresh read task PROMPT/READY/STOP, Guard/current shared state, lock chính mình, canonical exact ID, re-evaluate refs/mount/open handles, tree/meta. Bất kỳ lệch ⇒ HOLD. Yêu cầu kết quả archive `ARCHIVE_RESTORE_PASS` **cho chính DS ấy** (không dùng proof của DS khác).
- DS1–DS7: chỉ xóa **đúng thư mục tuyệt đối được duyệt**, sau validation canonical path, no mounted/symlink target; không follow symlinks, không glob/wildcard/prefix path. DS8–DS9: `docker volume rm <full exact 64-hex volume-id>` thường, Docker từ chối ⇒ KEEP, **không `-f`/prune**.
- Không chạm `prod-v1`, KEEP evidence R9/R10, volume data/3 log volumes production, image I1/I2, journal Neo4j prod hoặc dữ liệu HJW/TQT/VPSC/PG. Không `docker system prune`, `git prune`, bulk `rm -rf` trên parent, không DEL ngoài 9 rows.

## 6. W7 · POST GUARD / DATA INTEGRITY
Kiểm PRE vs POST:
- Neo4j read-only 3596 nodes/6823 edges + types 614/611/151/128, `graph-v1 watch --guard` PASS (sau giữ khóa), 5 pins, 16 evidence folders nguyên; R9 SHA check 99/99 và R10 41/41; backup/rollback/compose/Neo4j production volume/journals, image I1/I2, volumes V1–V3 nguyên quyền/tình trạng/refs; PG/Directus/Hermes/TQT không bị đổi.
- Protection Guard PRE+POST PASS `22/22`, Config Guard CLEAN, #11 thực GREEN, zero unapproved footprint, storage event declared/reconciled for GRAPH. Bất kỳ RED mới/identity loss ⇒ `POST_FAIL` và báo thật, không tự điều chỉnh baseline/threshold hoặc chạy tool chữa VPS của dự án khác.

## 7. W8 · DF BYTES / CLEAN SESSION / SINGLE KQ
- Ghi `df -B1 /` và disk usage graph pre/post, **actual freed bytes** không coi 2,879,070,208 B snapshot là chắc; số DS archive/restored/deleted/held, SHA manifests và Drive IDs+readback/restore receipts, từng bước W1–W8.
- Bằng chứng trên VPS chỉ metadata tối thiểu cho audit; archive encrypted ở Drive, 0 plaintext secrets outside intended tmpfs, 0 keys leaked; xóa staging/tmpfs sau proof, kể cả KQ DỪNG; không tạo timer/cron/background/agent con, không để lại 1 PID đọc treo (timeout, xác minh tiến trình do RUN tạo).
- Ghi `KQ@GS-CLEAN-WRITE-20261020-01 XONG|DỪNG` và trả `VPS-GHI: trống` **cùng commit/transaction**; nếu có DS HOLD hoặc Guard/POST chưa đạt, ghi `DỪNG · PARTIAL x/9` đầy đủ từng DS, không khai XONG giả; release trong mọi nhánh, kể cả lỗi. Không giữ máy chờ Owner/24h. Repo KQ chỉ metadata/receipts/paths approved không secrets, không tạo file mới Git. Báo Owner ≤5 dòng: x/9 deleted, bytes actual df freed, Drive restore PASS, KEEP unchanged, commit + remaining conditions. `NEXT_TRIGGER=GPT_HOST_REVIEW_GS_CLEAN_KQ_THEN_R10B`.

## 8. STEP_WALK_V1 (DROOT48) · EVERY STEP HAS OWNER, EVIDENCE AND FAIL ROUTE
| Bước | Ai | Trigger | Deadline/SLA | Evidence phải đo | Hỏng ai biết/lúc nào | Bước kế |
|---|---|---|---|---|---|---|
| W1 S0 + Owner gate | Claude Code | Owner pasted exact RUN | read-gate đầu phiên | Full 1727-byte SHA, 22/22, source + READY match | Executor báo Owner KQ DỪNG ngay nếu lệch | W2 |
| W2 CAS lease + STARTED/Guard PRE | Claude Code | W1 PASS | trước mọi write | root VPS-GHI/STARTED same commit, Guard PRE | Executor/KQ ngay khi fail | W3 |
| W3 tree/meta + secrets | Claude Code | W2 PASS | bounded timeout per DS | expected per-DS hash, secrets counted | HOLD exact DS, report same RUN | W4 |
| W4 references | Claude Code | W3 PASS | before archive & delete | all refs/container/mount proof | HOLD exact DS | W5 |
| W5 encrypted Drive + restore | Claude Code | W4 PASS | bounded; never sleep on wait | encrypted Drive readback, decrypt/restore tree PASS | HOLD exact DS | W6 |
| W6 exact delete | Claude Code | all gates for this DS PASS | immediately after proof | exact path/ID, delete receipt | HOLD/POST_FAIL, no scope expansion | W7 |
| W7 Guard/invariant POST | Claude Code | each DS and after all DS | before KQ | 22/22, Neo4j, KEEP, hashes match | KQ DỪNG and Host notified | W8 |
| W8 size and terminal KQ/release | Claude Code | W7 measured | same terminal run, no background | df bytes, 9 statuses, root KQ/release same commit | Owner knows in KQ immediately | Host review/R10B |
