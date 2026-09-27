# PROMPT — VPSUP SEC1 · khẩn đóng 2 lỗ lộ G0

RUN_ID: VPSUP-SEC1-20260927-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: SSH/operator hiện hữu tới VPS1 + VPS2; runtime VPS là SSOT.
Không có Write_Path dự phòng. Không bind được fs_* hoặc không vào được đúng hai máy bằng đường đã audit ⇒ DỪNG trước mutation.

## 0. Read gate bắt buộc

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc theo thứ tự: `AGENTS.md` → `work/vps1-up-grade/COLLAB.md` (§0, D14–D18, P07–P11, G0 KQ) → `PROMPT.md` → `view.html` §9.
3. Xác minh `READY@<40hex>` đúng commit cuối chạm `PROMPT.md`. Sai/missing ⇒ DỪNG.
4. Xác minh không có RUN/mutation hạ tầng khác đang diễn ra trên VPS1/VPS2. Có ⇒ DỪNG.
5. Runtime live thắng mọi số lịch sử.

## 1. Mục tiêu duy nhất

Đóng **đúng hai exposure G0 đã chứng minh**, không làm việc khác:

A. VPS1 Directus: gỡ **Public anonymous CREATE + UPDATE** trên collection `approval_requests`; không thay business data, cron, Flow, public READ hoặc permission collection khác.

B. VPS2: chặn **internet ingress** vào host port `3307` (MySQL) và `8080` (`cms_nginx`) bằng containment firewall runtime không restart container; giữ e-learning 80/443 và kết nối nội bộ hoạt động.

Đây là **SEC1 containment**, không phải backup, cleanup, upgrade hay hardening hoàn chỉnh.

## 2. Ngoài phạm vi — cấm

- Không nâng Directus/MySQL/Docker/Nuxt/Qdrant.
- Không sửa schema, business data, user data, password, MySQL grants, `root@'%'`.
- Không sửa/disable cron `dot-apr-execute`, Flow, Hermes, queue.
- Không xóa Public READ permissions hoặc bất kỳ permission collection khác.
- Không enable UFW, không cài package/firewall tool.
- Không sửa compose/port binding, không restart/recreate container ở VPS2.
- Không dọn log/cache/image.
- Không sửa backup trong RUN này.
- Không thay DNS/nginx/Caddy config.
- Không tạo file/evidence mới trên VPS1/VPS2 ngoài thay đổi runtime firewall rule cần thiết.
- Không in secret/token/password/private key/cookie.
- Không thử anonymous write vào `approval_requests` vì sẽ tạo dữ liệu.

## 3. Preflight — chỉ đọc, phải PASS trước từng mutation

### A · VPS1 Directus
1. Đo lại Public permission của `approval_requests`:
   - exact permission IDs cho CREATE và UPDATE;
   - fields/filter/validation/presets;
   - Public policy/role binding.
2. Xác nhận activity từ G0 đến hiện tại: có anonymous CREATE/UPDATE không.
3. Tìm runtime/source caller của `approval_requests`; xác nhận không có luồng công khai ẩn danh hợp lệ đang cần CREATE/UPDATE.
4. Liệt kê **mọi Public CREATE/UPDATE/DELETE khác** để Host biết, nhưng **không sửa** chúng trong SEC1.
5. Xác định credential API-only hiện hữu có quyền quản trị system permissions; không dùng password Owner, không in token.

Nếu permission đã đổi, có anonymous usage thật, có dependency công khai hợp lệ, hoặc chỉ có thể sửa bằng direct SQL ⇒ **DỪNG phần A, không đoán**.

### B · VPS2 network
1. Xác nhận live:
   - 80/443 e-learning healthy;
   - `3307` và `8080` vẫn published/public;
   - container/port mappings;
   - external interface;
   - Docker firewall backend/chains.
2. Từ Mac Owner, kiểm external reachability 3307/8080 trước thay đổi bằng TCP probe an toàn, không đăng nhập DB.
3. Xác nhận container nội bộ không cần internet-origin access vào hai host port này.
4. Chuẩn bị **exact rollback command(s)** trước khi thêm rule.
5. Không dùng UFW để giả chặn Docker nếu chain thực tế không đi qua UFW.

Nếu không xác định được chain/match an toàn chỉ nhắm ingress internet 3307/8080, hoặc rule có nguy cơ ảnh hưởng 22/80/443/internal Docker ⇒ **DỪNG phần B**.

## 4. Mutation A — Directus native API only

Chỉ khi Preflight A PASS:

1. Dùng Directus system API/native permission endpoint với credential máy quản trị hiện hữu.
2. Lưu trong memory của phiên trước-state tối thiểu để rollback: permission ID, action, collection, fields, filter, validation, presets, policy/role binding. Không ghi secret.
3. Xóa/disable **chính xác hai permission CREATE + UPDATE của Public trên `approval_requests`**.
4. Không chạm READ/DELETE hay collection khác.
5. Postcheck bằng GET metadata/system API:
   - Public CREATE = không còn;
   - Public UPDATE = không còn;
   - Public READ trạng thái như trước;
   - permission unrelated unchanged.
6. Không anonymous POST/PATCH để test.

Nếu postcheck sai hoặc API/system health regression:
- rollback ngay bằng native API từ before-state;
- verify rollback;
- phần A = DỪNG.

Không fallback sang direct SQL nếu native API fail.

## 5. Mutation B — VPS2 runtime firewall containment

Chỉ khi Preflight B PASS.

Mục tiêu: chặn **external ingress only** tới published host ports 3307/8080 mà không restart/recreate container.

1. Dùng firewall backend hiện hữu của Docker:
   - nếu iptables: ưu tiên `DOCKER-USER`, match external ingress và **original destination port** bằng conntrack khi DNAT làm đổi port;
   - nếu nftables backend: dùng chain/hook hiện hữu tương đương, không dựng framework firewall mới.
2. Rule phải:
   - chỉ nhắm external interface/public ingress;
   - chỉ 3307 + 8080;
   - không chặn loopback/internal Docker/established traffic;
   - không chạm 22/80/443.
3. Không enable UFW, không install persistence package.
4. Ghi exact rollback command trong memory/report trước khi apply.
5. Apply runtime rule(s).

### Verify ngay
- Từ Mac ngoài VPS2: 3307 + 8080 không còn reachable.
- 80 + 443 vẫn reachable.
- E-learning page/health vẫn PASS.
- Từ VPS2: MySQL container healthy + internal connection/app health PASS; `cms_nginx` nội bộ PASS.
- Không restart container; StartedAt không đổi.

Nếu bất kỳ regression:
- rollback rule ngay;
- verify service trở lại;
- phần B = DỪNG.

**Lưu ý:** runtime firewall containment có thể mất sau reboot. SEC1 phải ghi `TEMPORARY_UNTIL_PERSISTENT_BINDING`. Cấm reboot VPS2 trước RUN hardening kế tiếp. Persistent bind `127.0.0.1`/compose + MySQL upgrade/grant hardening chỉ làm sau khi e-learning có offsite backup.

## 6. Nghiệm thu SEC1

### PASS A
- Public `approval_requests`: CREATE=0, UPDATE=0.
- READ không bị thay ngoài chủ đích.
- không business data change.
- Directus/Nuxt/agent health không regression.
- cron vẫn nguyên trạng.

### PASS B
- external 3307=closed;
- external 8080=closed;
- 80/443 PASS;
- MySQL/cms_nginx internal PASS;
- 0 container restart/recreate;
- rollback command đã xác định;
- trạng thái TEMPORARY được ghi rõ.

### Không mở rộng
Nếu phát hiện Public write permission khác hoặc exposure khác:
- ghi 🔴/🟡 vào report;
- không tự sửa ngoài hai mục A/B.

## 7. Report — chỉ SSOT hiện hữu

Không tạo file mới.

### view.html §9
Chỉ trong §9:
- thêm/cập nhật một khối ngắn `SEC1` ngay sau kết quả G0;
- A: trước → sau, PASS/DỪNG;
- B: trước → sau, PASS/DỪNG + TEMPORARY/PERSISTENT;
- regression check;
- next: `BK1 backup` trước mọi cleanup/recreate VPS2.

### COLLAB.md
- cập nhật Dòng hiện hành;
- ghi `KQ@VPSUP-SEC1-20260927-01 XONG` chỉ khi A+B đều PASS;
- nếu một phần fail: `KQ@VPSUP-SEC1-20260927-01 DỪNG` + nêu phần nào đã đóng an toàn/phần nào chưa;
- xử lý OQ-G0-1 theo kết quả, không tạo quyết định Owner giả.

### Commit
Dùng `fs_transaction` sửa `view.html` + `COLLAB.md` một commit:
`[Claude Code] VPSUP-SEC1 · đóng public write và public DB ports`

Kết thúc Owner đúng một dòng:
`XONG` hoặc `DỪNG — <lý do ngắn>`.

## 8. Bước sau SEC1 — không làm trong RUN này

Host sẽ phát RUN riêng **BK1**:
1. backup encrypted `incomex_metadata` + `/opt/incomex/data` lên Drive;
2. upload/verify e-learning backup 09/08 lên Drive;
3. restore/read-back proof;
4. sau đó mới persistent-bind 3307/8080, sửa `cms_queue`, dọn ≈26GB, swap/RAM lab.

Không tự nhảy sang BK1.
