# PROMPT — HVU.VPSARCHIVE01 · RUN VPS gọn như GitHub

RUN_ID: HVU-VPSARCHIVE01-RUN-20260922-01
Host: GPT Chat
Reviewer: Claude Chat · P31 ACCEPT/CHANGE
Executor_Surface: Claude Code CLI
Write_Path: runtime VPS theo README §11 + workspace MCP cho Git docs

## 0. Gate trước mutation
1. Đọc AGENTS.md → root COLLAB.md → work/hpml-view-for-user/COLLAB.md → PROMPT này → README §11–§12.
2. Commit cuối chạm PROMPT phải khớp READY trong COLLAB; lệch → DỪNG.
3. Consensus binding: Owner A0 vòng HVU-VPSARCHIVE01 + P29/P30/P31 + Host P32.
4. Lấy baseline trước sửa: runtime refs; sync-status/tasks.json; số Now/Done; sidebar + master list 7 cột; systemd unit/drop-ins của sync; owner/group/mode/ACL các path liên quan; /opt/incomex/deploys inventory; JEV Documentation hiện tại; rollback point.
5. Không sửa/redeploy hai MCP gateway; không đổi MCP schema/version/auth; không xóa tự động bất cứ hồ sơ nào.

## 1. Mục tiêu phải đạt đồng thời
1. **Hàng ngày nhìn gọn:** khi không tìm kiếm, Owner chỉ thấy việc Now; việc Done nằm sau một control gập `Đã xong (N)`.
2. **Lịch sử không mất:** việc Done vẫn tìm/mở được; evidence/history VPS nằm trong kho theo task-id; mở lại thì hồ sơ đi ngược về Now; xoá chỉ Owner quyết riêng.
3. **Không làm gãy máy đang chạy:** runtime/service/live build/secret/active recovery không được move chỉ vì task Done.

GitHub/workspace vẫn là SSOT của task/doc. VPS runtime vẫn theo README §11. `/opt/incomex/work` chỉ là kho **evidence/history không phải runtime**.

## 2. Web gọn — áp cho CẢ sidebar và Master list 7 cột
Dùng cùng một state/filter cho hai bề mặt; không để một bên gọn, một bên vẫn tràn Done.

### 2.1 Khi search rỗng
- Sidebar: chỉ render task bucket=Now + đúng một control `Đã xong (N)` đang gập.
- Master list 7 cột: cũng chỉ render Now + đúng một row/control `Đã xong (N)` đang gập; không liệt kê từng Done.
- Bấm control → mở/đóng danh sách Done trên cả bề mặt liên quan theo thiết kế ít sửa nhất.
- N = số task bucket=Done trong tasks.json.

### 2.2 Khi search có chữ
- Search xuyên Now + Done theo logic hiện hành id + title + toàn bộ A0.
- Done match phải hiện ngay dù nhóm Done đang gập.
- Clear search → trở về chế độ mặc định chỉ Now + `Đã xong (N)`.
- Không full-text HTML; không page/archive UI mới.

### 2.3 Regression
- Detail/task selection, actor status, Last time, tiến độ, polling và nút Copy hiện hành không regression.

## 3. Kho evidence VPS hai chiều
### 3.1 Cấu trúc duy nhất
- Now evidence: `/opt/incomex/work/<task-id>/`
- Done evidence: `/opt/incomex/work/done-tasks/<task-id>/`

Không thêm `VPS_Evidence:` vào từng PROMPT. Path suy ra từ task-id + bucket theo một rule nền.

Không cần tạo folder rỗng cho mọi task. Tạo lazily khi có evidence thật.

### 3.2 Evidence được phép
Ví dụ:
- log chẩn đoán;
- report/bằng chứng;
- before/after;
- export/snapshot;
- artifact rollback đã được xác định archive-safe.

Không move vào kho này:
- executable/runtime/service đang chạy;
- systemd/nginx/compose/container/live build đang được tham chiếu;
- secret;
- active recovery còn là đường cứu hộ hiện hành;
- item chưa chứng minh được thuộc task nào.

### 3.3 Reconcile tự động bằng sync hiện có
Sau khi publish task snapshot thành công, reconcile evidence folder:
- task Now + chỉ có Done path → atomic rename về Now path;
- task Done + chỉ có Now path → atomic rename sang Done path;
- không có cả hai → no-op;
- có cả hai → warning + không overwrite/merge;
- chỉ rename bên trong `/opt/incomex/work`;
- không quét/move từ `/opt/incomex/deploys` hay vùng khác;
- không delete.

Rename hai chiều phải ở cùng filesystem; nếu không cùng filesystem → DỪNG thay vì copy/delete.

## 4. Quyền Linux — phải chạy thật bằng User=hvu-view
P31 đã xác nhận sync chạy với `User=hvu-view`, `ProtectSystem=strict`.

Agent phải khảo sát unit/drop-in thật rồi triển khai least-privilege:
1. cho sync ghi đúng `/opt/incomex/work` qua `ReadWritePaths=/opt/incomex/work` (drop-in hoặc cơ chế hiện hành tương đương);
2. root folder và `done-tasks` dùng group phù hợp với process `hvu-view`, setgid và default ACL/mode đủ để thư mục/file tạo mới bên dưới vẫn rename được bởi sync;
3. không mở quyền ngoài `/opt/incomex/work`;
4. kiểm chính xác owner/group/mode/ACL sau deploy;
5. acceptance bắt buộc: một task evidence folder **do root tạo** dưới kho Now phải được process/sync chạy bằng hvu-view rename Now→Done→Now thành công; không dùng root để giả PASS.

Không chmod 777.

## 5. Hồ sơ của CHÍNH RUN này
Từ lượt này, evidence/backup/rollback của VPSARCHIVE01 ghi ngay dưới:
`/opt/incomex/work/hpml-view-for-user/`

Không tạo deploy folder mới trong `/opt/incomex/deploys` cho RUN này, trừ khi một runtime tool hiện hành bắt buộc và Host prompt không thể thay; nếu gặp thì DỪNG/ghi lý do thay vì phá luật mới.

Rollback script phải:
- dùng path tương đối hoặc tự resolve directory của chính nó;
- vẫn chạy được sau khi evidence folder HVU bị rename sang `done-tasks/hpml-view-for-user`;
- được test syntax + dry/contract phù hợp trước acceptance.

Luật A8 mới sau PASS phải thắng mọi path evidence cũ ghi trong PROMPT lịch sử; không sửa hàng loạt PROMPT cũ.

## 6. Audit /opt/incomex/deploys — chỉ cleanup ARCHIVE_SAFE
Inventory các candidate HVU và candidate khác nếu thấy rõ, nhưng **không move theo tên**.

Phân loại máy kiểm:
- `LIVE_RUNTIME`: path xuất hiện trong unit systemd, drop-in, compose, nginx, crontab/timer hoặc live mount/config đang dùng → giữ nguyên.
- `ACTIVE_RECOVERY`: rollback/recovery mới nhất của một task đang Now, hoặc recovery được current run/report/pointer ghi là đường cứu hộ hiện hành → giữ nguyên.
  - Riêng HVU: `hvu-archive01-20260922` giữ ACTIVE_RECOVERY cho tới khi VPSARCHIVE01 PASS và rollback mới đã được nghiệm thu.
- `ARCHIVE_SAFE`: chứng minh được thuộc một task, không thuộc LIVE_RUNTIME, không thuộc ACTIVE_RECOVERY, không chứa secret; mới được move vào evidence history của task.
- Không phân loại chắc → `UNKNOWN`, giữ nguyên + báo cáo.

Khi move một item ARCHIVE_SAFE:
- cập nhật pointer/doc hiện hành nào vẫn trỏ path cũ;
- với rollback script: test `bash -n` + kiểm relative/dependency path;
- không làm mất khả năng rollback thật.

Không cần dọn hết deploys trong RUN này. Acceptance chỉ cần migrate an toàn **ít nhất một** item HVU ARCHIVE_SAFE và chứng minh các item còn lại được phân loại đúng.

## 7. Evidence path trên tasks/detail
Không biến evidence path thành state source thứ hai.

Chọn cách ít code nhất:
- tasks.json có derived `vpsEvidencePath`/existence, hoặc UI derive từ id+bucket + một tín hiệu existence hẹp;
- trang detail hiển thị:
  - `Hồ sơ VPS: /opt/incomex/work/<id>/` hoặc Done path nếu folder tồn tại;
  - `Hồ sơ VPS: chưa có` nếu chưa có evidence.
- Không directory-list public evidence; chỉ hiển thị path/status cho Owner/AI.

## 8. Deep-link task-id + sửa JEV 404
Thêm deep-link tối thiểu, không rebuild lại kiến trúc Nuxt:
- URL trang cha hỗ trợ `?task=<id>`.
- Khi mở URL có task id hợp lệ → UI chọn đúng task.
- Khi User chọn task → cập nhật URL cha giữ `task=<id>` mà không reload phá state, nếu cơ chế iframe/same-origin hiện hành cho phép như P31.
- invalid/missing id → fallback an toàn về mặc định, không lỗi.

Sửa:
`Documentation=https://vps.incomexsaigoncorp.vn/knowledge/modules?task=jev-integration`
cho `jev-gw.service`.
Chỉ `daemon-reload` nếu Documentation-only; không restart JEV service nếu không cần.

Link mới tới task dùng deep-link task-id, không raw Git folder path.

## 9. Luật nền sau khi runtime PASS
Chỉ sau khi các test/runtime acceptance chính PASS:
- AGENTS A8/A9: thêm một rule chung về evidence VPS:
  - evidence không-runtime mặc định ở `/opt/incomex/work/<id>/`;
  - Done ở `/opt/incomex/work/done-tasks/<id>/`;
  - sync tự rename hai chiều; không delete;
  - runtime/secret/active recovery không thuộc kho evidence.
- Không thêm `VPS_Evidence` vào từng PROMPT.
- README/runtime docs cập nhật path/permission/reconcile/deep-link.
- Root decision thêm DROOT cho VPS evidence archive nếu cần; không tạo state source mới.

## 10. Trình tự RUN
### Phase A — read-only baseline + test candidate
- Audit P31 đủ 6 điểm.
- Viết test/fixture trước mutation production.
- Test tối thiểu:
  1. sidebar empty search chỉ Now + Done(N);
  2. master list 7 cột empty search cũng chỉ Now + Done(N);
  3. expand/collapse Done;
  4. search Done khi group đang gập;
  5. clear search;
  6. evidence reconcile Now↔Done/conflict/no-folder;
  7. root-created folder rename bằng hvu-view;
  8. evidence path detail;
  9. deep-link valid/invalid + chọn task cập nhật URL;
  10. B2 webhook/backstop/last-good/retention/presence regressions.

### Phase B — tạo kho + quyền + deploy candidate
- Tạo `/opt/incomex/work` và `done-tasks` với owner/group/setgid/default ACL đúng.
- Tạo evidence folder của RUN này dưới Now path HVU; lưu before/rollback ở đó.
- Deploy sync/UI/systemd drop-in tối thiểu.
- Không touch/move deploys legacy ở phase này.
- Health + regression PASS; fail → rollback + DỪNG.

### Phase C — live reconcile + UI
- Dùng fixture/evidence thật an toàn để chứng minh hvu-view rename hai chiều.
- Kiểm web mặc định gọn ở cả sidebar và master list.
- Search Done + deep-link.
- Kiểm no-delete/no-overwrite conflict.

### Phase D — audit/migrate legacy an toàn + JEV link
- Inventory `/opt/incomex/deploys`.
- Migrate ít nhất một HVU ARCHIVE_SAFE; LIVE_RUNTIME/ACTIVE_RECOVERY/UNKNOWN giữ nguyên.
- Sửa pointer/doc cần thiết.
- Sửa JEV Documentation deep-link + daemon-reload.
- Xác minh HTTP/deep-link 200 và JEV service vẫn healthy.

### Phase E — luật nền + final acceptance
- Cập nhật AGENTS/README/root decision sau PASS.
- Không đóng/move HVU trong RUN này. HVU vẫn Now để Host nghiệm thu; việc đóng HVU là lệnh riêng sau nghiệm thu.
- Không move/mutate `mcp-workspace` hay task Git Done khác trong RUN này.

## 11. Acceptance bắt buộc
- Web initial view: chỉ Now + một `Đã xong (N)`; Done không tràn sidebar **và** master list.
- Search/expand/clear đúng.
- `/opt/incomex/work` permission least-privilege; hvu-view rename root-created folder hai chiều PASS.
- Reconcile chỉ trong evidence root; conflict safe; không delete.
- Runtime/live paths không move.
- Evidence RUN này + rollback nằm trong task evidence root và vẫn usable sau rename path.
- Ít nhất một legacy HVU ARCHIVE_SAFE migrate PASS; active/unknown giữ nguyên.
- Detail evidence path đúng.
- Deep-link JEV/HVU theo task-id PASS; JEV Documentation không 404; JEV không restart nếu không cần.
- B2/webhook/backstop/last-good/retention=3/presence/actor regressions PASS.
- MCP gateways untouched; contract/version/auth unchanged.
- Không daemon/scheduler mới.
- Disk/state bounded.

## 12. Báo cáo
- Cập nhật chính COLLAB; không tạo progress file.
- Ghi runtime refs, permission/unit diff, test results, evidence inventory table, item đã migrate, deep-link, JEV Documentation, rollback path.
- Ghi:
  `KQ@HVU-VPSARCHIVE01-RUN-20260922-01 XONG|DỪNG`
- Trả đúng một dòng:
  `XONG · HVU.VPSARCHIVE01 · <refs>`
  hoặc
  `DỪNG · HVU.VPSARCHIVE01 · <lý do>`.
