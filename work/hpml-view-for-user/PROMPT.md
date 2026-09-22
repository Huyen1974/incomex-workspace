# PROMPT — HVU.VPSARCHIVE01 · DRAFT VPS gọn như GitHub

STATUS: DRAFT · CHỈ REVIEW/ĐỒNG THUẬN · KHÔNG RUN PRODUCTION
RUN_ID: HVU-VPSARCHIVE01-DESIGN-20260922-01
Host: GPT Chat
Reviewer: Claude Chat
Executor_Surface dự kiến: Claude Code CLI

## 0. Mục tiêu Owner đã xác nhận
Hai mục tiêu phải đạt đồng thời:
1. **Hàng ngày nhìn gọn:** Task html view mặc định chỉ cho Owner thấy vài chục việc đang làm; việc cũ không được tràn danh sách.
2. **Lịch sử không mất:** việc đã xong vẫn có hồ sơ trên VPS để giữ, tìm, bàn lại, mở lại/nâng cấp; xoá chỉ khi Owner quyết riêng.

GitHub/workspace vẫn là SSOT của task/doc; runtime/service VPS vẫn giữ nguyên SSOT hiện hành. Pha này chỉ tổ chức **hồ sơ/evidence không phải runtime** trên VPS và UI hiển thị.

## 1. Host review P29 Claude — ACCEPT WITH REFINEMENTS
### A. Web gọn mặc định — ACCEPT
- Khi ô search rỗng: render danh sách **Now בלבד** + một control duy nhất `Đã xong (N)` đang gập.
- Bấm control mới mở danh sách Done; không cần page mới.
- Khi search có chữ: tìm xuyên Now + Done theo logic hiện có id/title/A0; Done match phải xuất hiện dù control đang gập.
- Clear search → trở lại chế độ mặc định Now + `Đã xong (N)`.
- N = đúng số task bucket Done trong tasks.json.

### B. Hai tủ hồ sơ VPS — ACCEPT
Dùng đúng cấu trúc:
- `/opt/incomex/work/<task-id>/` = hồ sơ task đang Now.
- `/opt/incomex/work/done-tasks/<task-id>/` = hồ sơ task Done.

Chỉ chứa **task evidence/history không phải runtime**: log chẩn đoán, báo cáo/bằng chứng, before/after, export/snapshot, artifact rollback đã archive-safe.
Không chứa/không move:
- runtime đang chạy;
- systemd/nginx/container/live build đang được tham chiếu;
- secret;
- gói rollback còn là đường cứu hộ đang hoạt động.

Không cần tạo folder rỗng cho mọi task; tạo lazily khi task thật sự có hồ sơ VPS.

### C. Tự đi hai chiều theo Git — ACCEPT
Tái dùng chính B2 sync sau khi publish thành công:
- Task Now: nếu chỉ có `.../done-tasks/<id>/` → atomic rename về `.../work/<id>/`.
- Task Done: nếu chỉ có `.../work/<id>/` → atomic rename vào `.../work/done-tasks/<id>/`.
- Không có cả hai → no-op.
- Có cả hai → warning + không overwrite/merge tự động.
- Chỉ được rename **bên trong /opt/incomex/work**; tuyệt đối không tự quét/move từ `/opt/incomex/deploys` hay vùng runtime khác.
- Không delete tự động. Xoá = hành động Owner riêng.

### D. KHÔNG thêm `VPS_Evidence:` vào từng PROMPT
P29 đề xuất mỗi PROMPT có line đường dẫn; Host đổi để giảm duplicate:
- evidence path suy ra 100% từ `task-id + bucket`, nên **không ghi lặp vào PROMPT**.
- Sau RUN PASS, AGENTS A8/A9 chỉ cần một rule chung về `/opt/incomex/work`.
- tasks.json có thể xuất `vpsEvidencePath` dạng derived data, hoặc UI tự derive từ id+bucket; chọn cách ít code nhất.
- Trang detail hiển thị `Hồ sơ VPS: <path>` nếu folder tồn tại; nếu chưa có thì `Hồ sơ VPS: chưa có`. Không biến path thành state source thứ hai.

### E. Cleanup lịch sử `/opt/incomex/deploys` — AUDIT TRƯỚC, KHÔNG MOVE THEO TÊN
Một lần cho HVU:
- inventory các `hvu-*`/file liên quan đã nêu ở P29;
- phân loại từng item:
  1. `LIVE_RUNTIME` → giữ nguyên;
  2. `ACTIVE_RECOVERY` (đường rollback còn được dùng/tham chiếu) → giữ nguyên cho tới khi safe;
  3. `ARCHIVE_SAFE` → có thể move vào `/opt/incomex/work/hpml-view-for-user/history/`.
- Chỉ move ARCHIVE_SAFE có bằng chứng nguồn/task rõ.
- Không đoán item mơ hồ; để nguyên + liệt kê.
- Sau move, mọi rollback script được chuyển phải vẫn callable ở path mới; test syntax + dependency/path, và cập nhật pointer/report nếu cần.
- Gói rollback của **chính RUN VPSARCHIVE01** ở vùng deploy hiện hành cho tới acceptance; chỉ archive sau khi không còn là active recovery.

### F. Link theo task-id — ACCEPT + làm rõ
- Link tới “một việc” không dùng raw Git path `work/.../` vì archive/reopen làm đổi path.
- Owner View cần deep-link ổn định theo task-id. Nếu app đã support thì tái dùng; nếu chưa, thêm cách tối thiểu như `?task=<id>`.
- Sửa `jev-gw.service Documentation=` đang 404 sang deep-link task JEV ổn định; reload daemon nếu cần nhưng không restart service nếu Documentation-only.
- Các doc mới từ nay ưu tiên task-id/deep-link; không rewrite lịch sử cũ hàng loạt.

## 2. Đồng bộ source Git trên VPS
Source clone/read-only mirror đã đi theo GitHub `work/done-tasks/`; giữ nguyên cơ chế này.
**Không tạo sync thứ hai cho mã/tài liệu nguồn.**
`/opt/incomex/work` ở pha này chỉ là kho hồ sơ VPS/evidence, không thay GitHub SSOT.

## 3. Acceptance đề xuất
Bắt buộc chứng minh:
1. initial web/search rỗng: chỉ Now + một dòng `Đã xong (N)`; không render hàng trăm Done.
2. expand Done → thấy Done; search một từ thuộc Done khi đang gập → tìm ra đúng Done.
3. clear search → trở về gọn.
4. tạo fixture evidence A Now trong `/opt/incomex/work/A`; đổi bucket fixture → reconcile move hai chiều; conflict both-sides → warning/no overwrite; không delete.
5. live/runtime paths không bị move.
6. một item HVU `ARCHIVE_SAFE` được migrate thật + evidence rollback/path PASS; item active/mơ hồ giữ nguyên.
7. detail hiển thị đúng evidence path/“chưa có”.
8. stable deep-link `task-id` mở được JEV/HVU cả Now/Done; `Documentation=JEV` hết 404.
9. B2 webhook/backstop/last-good/retention/presence regression PASS.
10. disk/state bounded; không daemon/scheduler mới.

## 4. Claude cần review
Claude Chat ghi P31 vào COLLAB:
- ACCEPT/CHANGE A–F.
- Đặc biệt phản biện 3 refinement Host:
  1. bỏ `VPS_Evidence` khỏi từng PROMPT và derive path;
  2. sync chỉ rename trong `/opt/incomex/work`, cleanup `/deploys` phải audit-safe;
  3. stable deep-link theo task-id, không raw Git path.
- Kiểm có blocker kỹ thuật nào khiến evidence rename sau publish không an toàn.
- Nếu không blocker, đề nghị Host chuyển DRAFT thành RUN và pin READY cho Claude Code CLI.

Không mutation runtime ở lượt review này.
- Không tạo page/database/archive UI mới.
- Bấm task Done vẫn mở đúng detail/document URL theo task-id.
- Không thay actor naming/presence semantics.

## 5. Lifecycle hai chiều + A9 / README / root rules — chỉ cập nhật sau cutover thành công
### 5.1 Hai lệnh chuẩn cho người và AI
Ghi vào AGENTS/A9 khi cutover PASS:
- `Đóng <id>` = intent kết thúc + archive. Máy kiểm hai dấu hiệu trước move: (a) RUN_ID hiện hành đã có `KQ@<RUN_ID> XONG`; (b) `## Owner cần quyết` không còn dòng chờ. Nếu cả hai đạt → move ngay, không hỏi. Nếu thiếu một trong hai → hỏi đúng **một câu** nêu phần chưa hoàn tất và xin Owner xác nhận đóng. Nếu Owner xác nhận, hoặc ngay từ câu lệnh đã nói rõ `đóng luôn/bỏ việc này dù chưa xong` (ngữ nghĩa tương đương), ghi `CLOSED · <ngày> · theo lệnh Owner · chưa hoàn tất` và ghi ngắn phần còn thiếu (ví dụ `chưa có KQ XONG`/`còn Owner wait`) rồi move. Không hỏi lặp. Lịch sử phải trung thực; không tự tạo `KQ XONG` giả.
- `Mở lại <id>` = move `work/done-tasks/<id>/` → `work/<id>/` **và tạo một khối A0 vòng mới ở đầu §0**. Lịch sử A0 cũ giữ nguyên phía dưới.
  - Nếu User chỉ nói bare `Mở lại <id>`: A0 mới ghi `Xác nhận User: CHƯA XÁC NHẬN`, UI Mục tiêu phải về trạng thái điều chỉnh/vàng; Host hỏi ngắn mục tiêu sửa/nâng cấp trước khi plan/RUN.
  - Nếu cùng câu User đã nói rõ mục tiêu (`Mở lại <id> để ...` hoặc ngữ nghĩa tương đương): dùng nguyên ý User làm A0 mới và coi đó là xác nhận trực tiếp; không hỏi lại câu đã có đáp án.
- User gọi mơ hồ bằng tên/nội dung: AI tìm theo **id + title + A0 goal** ở cả Now/Done. Đúng 1 kết quả → nhắc lại `title (id)` rồi thực hiện. Nhiều kết quả → hỏi xác nhận đúng một lựa chọn/mã; không tự đoán.
- Move giữ nguyên id/Git history. READY/RUN cũ không tự tái sử dụng sau reopen; parser đối chiếu PROMPT path/commit hiện tại như §2.5.

### 5.2 Luật nguồn trạng thái

Sau khi runtime hỗ trợ archive và pilot PASS:
- A9/README: discovery = hai glob tường minh; `done-tasks` reserved; Done = folder location.
- Root DROOT07/luật liên quan: bỏ “root Đã xong đánh dấu Done”; thêm quyết định archive folder-state.
- Root `## Đã xong`: không duy trì danh sách task; để đúng một dòng hướng dẫn kiểu:
  `- Archive: work/done-tasks/ · vị trí folder là trạng thái Done.`
- Không dùng root Done list làm fallback lâu dài.

## 6. Thứ tự triển khai bắt buộc — không để trạng thái sai tạm thời
### Phase A · Test candidate trước production
- Unit/regression với fixture đủ:
  1. active task bình thường;
  2. done task có PROMPT + HTML + asset;
  3. duplicate id Now+Done → Now thắng + warning;
  4. HVU active/done không copy app thành document;
  5. READY current-path;
  6. presence done-tasks/id-lạ bị lọc; Now latest-only vẫn đúng;
  7. public URL task-id ổn định qua move;
  8. retention/last-good/webhook regressions.
- Synthetic move chỉ trong temp clone/fixture, không main.

### Phase B · Deploy runtime support TRƯỚC move
- Deploy sync/presence/UI patch với rollback.
- Vì workspace Git HEAD chưa đổi, **không ép rebuild/publish dữ liệu theo logic mới**; backstop HEAD-unchanged phải no-op như thiết kế.
- Health/nginx/unit/regression PASS. Nếu runtime lỗi → rollback, DỪNG; chưa move task nào.

### Phase C · Pilot migration thật
Trong **một Git commit/mutation logic thống nhất**:
- move `work/mcp-workspace/` → `work/done-tasks/mcp-workspace/`;
- cập nhật root `## Đã xong` sang pointer archive và cập nhật A9/README/root decisions cần thiết.
Webhook bằng runtime mới phải publish:
- mcp-workspace bucket Done;
- task-id giữ `mcp-workspace`;
- document/history nếu có không mất;
- không có active presence;
- search tìm được và detail mở được;
- các task còn lại giữ bucket/trạng thái đúng.
Nếu pilot fail → rollback **cả runtime và Git move theo forward restore**, DỪNG.

### Phase D · Đóng chính HVU làm acceptance thật
Chỉ sau pilot PASS:
1. ghi báo cáo + `KQ@HVU-ARCHIVE01-RUN-20260922-01 XONG` vào COLLAB khi HVU còn ở active folder;
2. commit/push báo cáo;
3. final Git move nguyên `work/hpml-view-for-user/` → `work/done-tasks/hpml-view-for-user/`.
Webhook phải cho thấy:
- HVU bucket Done;
- URL/detail vẫn mở;
- app runtime vẫn phục vụ;
- HVU Done có `Đang làm=null`;
- `Vừa làm` là actor của move/close theo Git author;
- root không còn task-list Done song song.

Sau final move không sửa thêm nội dung HVU trừ khi rollback.

## 7. Reopen acceptance
Không cần reopen HVU production chỉ để test.
Dùng fixture/temp clone để chứng minh:
- move Done A → Now A giữ task-id/history;
- READY cũ mismatch path-current commit → không tự cấp phép RUN;
- activity sau reopen được publisher cho hiện lại.
Nếu có một task thật cần reopen trong quá trình làm thì dùng làm bằng chứng thay fixture.

## 8. Acceptance bắt buộc
- B2/B2.1 regression + webhook/backstop/last-good/retention=3 PASS.
- Không mất HTML/assets của task Done.
- Search/master list thấy cả Now/Done.
- Link public key task-id ổn định qua move.
- No duplicate state source: folder là state; root Done list không còn.
- B3 gateway untouched; MCP contract/version/auth unchanged.
- Presence không xuất `done-tasks`; Done activeActors null.
- Current Now signals không regression.
- Git history preserved; không reset/rewrite.
- VPS source clone có đúng `work/done-tasks/<id>` sau fetch; không manual VPS move.
- Rollback script/evidence rõ.

## 9. Báo cáo
- Cập nhật chính COLLAB; không tạo progress file mới.
- Ghi runtime refs, Git move refs, tests, rollback.
- KQ:
  `KQ@HVU-ARCHIVE01-RUN-20260922-01 XONG|DỪNG`
- Trả đúng một dòng:
  `XONG · HVU.ARCHIVE01 · <refs>`
  hoặc
  `DỪNG · HVU.ARCHIVE01 · <lý do>`.
