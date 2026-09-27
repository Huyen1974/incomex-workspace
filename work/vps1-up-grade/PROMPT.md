# PROMPT — VPSUP SEC1A-DOT · kiểm cơ chế DOT/Secret Manager + đóng Public write

RUN_ID: VPSUP-SEC1A-DOT-20260927-01
STATUS: Chỉ thực thi sau khi COLLAB có READY đúng SHA commit cuối chạm file này và Owner/GPT Host phát RUN.
Host: GPT Chat · GPT-VPSUP-20260926-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: **fs_* / Incomex VPS MCP · root gh → incomex-workspace/main**.
Runtime_Write_Path: chỉ gọi DOT/MCP đã duyệt cho Directus/PG; SSH chỉ audit/read và kiểm runtime. Runtime VPS là SSOT.
Không có Write_Path dự phòng. Không bind được fs_* hoặc không vào được runtime đúng đường đã audit ⇒ DỪNG.

**DIRECTUS/PG: DOT ONLY · Secrets: Secret Manager · No direct login/write.**
Người/AI/Agent không đăng nhập Studio/psql, không lấy/copy credential; DOT tự nạp secret và tự mutation. Thiếu capability ⇒ DỪNG hoặc chỉ bổ sung DOT hiện hữu theo phạm vi dưới đây; không fallback REST/SQL.

## 0. Read gate bắt buộc

1. `fs_stat work/vps1-up-grade/COLLAB.md`.
2. Đọc theo thứ tự: `AGENTS.md` A10-R3 → `work/vps1-up-grade/COLLAB.md` (§0, D19–D20, SEC1 KQ, P12) → `PROMPT.md` → `view.html` §9.
3. Xác minh `READY@<40hex>` đúng commit cuối chạm `PROMPT.md`. Sai/missing ⇒ DỪNG.
4. Xác minh không có RUN/mutation hạ tầng khác đang diễn ra trên VPS1/VPS2. Có ⇒ DỪNG.
5. Runtime live thắng mọi số lịch sử.

## 1. Mục tiêu duy nhất

A. Kiểm chứng cơ chế chuẩn Directus/PG đang chạy: DOT nào, Secret Manager/loader nào, credential được nạp theo cơ chế nào — chỉ ghi tên/cơ chế, tuyệt đối không secret value.
B. Xác định vì sao SEC1-A trước hiểu sai thành “cần machine admin account”.
C. Nếu DOT hiện hữu có capability quản trị Directus permissions: dùng **chính DOT** gỡ Public CREATE #620 + UPDATE #621 trên `approval_requests`, giữ Public READ và mọi quyền khác.
D. Kiểm biển chỉ dẫn tại nơi agent thường chạm Directus/PG, gồm `report-pg`; không viết manual dài.
E. VPS2 phần B chỉ read-check để chắc containment 3307/8080 vẫn PASS/TEMPORARY; không sửa lại.

## 2. Cấm

- Không dùng Owner password/account; không unsuspend break-glass admin; không tạo admin/token/user.
- Không đọc/copy secret value từ Secret Manager ra terminal/log/chat/file.
- Không direct Directus mutation REST/GraphQL/MCP nếu call không nằm bên trong DOT đã duyệt.
- Không SQL write/psql mutation; không thay PG schema/data.
- Không xóa Public READ/quyền khác; không thử anonymous write tạo dữ liệu.
- Không reboot/restart/recreate VPS2; không đụng firewall B ngoài read-only verify.
- Không backup/cleanup/upgrade/Flow/cron/Hermes trong RUN này.
- Không tạo tài liệu tổng hợp hay file mới chỉ để ghi chú.

## 3. Audit DOT/Secret Manager — chỉ đọc trước

1. Inventory entrypoint DOT hiện hữu liên quan Directus/PG: command/script/service/dispatcher/help/cron; ưu tiên thứ đang chạy thật.
2. Với mỗi DOT liên quan: mục đích, input, mutation target, secret loader/caller, **tên secret/reference nhưng không value**, audit/rollback.
3. Xác nhận credential Directus/PG nằm trong Secret Manager hoặc loader Owner đã duyệt; không thử login bằng credential người.
4. Xác định DOT nào có thể thay Directus permissions. Nếu generic DOT: chứng minh có giới hạn target/action và trace.
5. `report-pg`: xác nhận census/read-only, tìm source path/route và xem đã có biển DOT-only chưa.
6. Tìm đúng các operator/help hiện hữu mà agent thường chạm Directus/PG; không tạo manual tổng hợp.
7. Đọc lại #620/#621 + Public binding bằng DOT/read-only tool hiện hữu; xác nhận anonymous write kể từ G0/SEC1; chuẩn bị exact rollback bằng cùng DOT.
8. Verify B: 3307/8080 ngoài internet vẫn đóng, 80/443/e-learning vẫn PASS. Không mutation B.
## 4. Nhánh A — DOT phù hợp đã có

Chỉ khi Audit PASS và DOT tự nạp secret mà Agent không nhìn thấy value:
1. Gọi DOT đúng operation revoke/delete/disable #620 + #621.
2. Không `curl` Directus trực tiếp, không SQL write, không sửa Public READ/quyền khác/business data/cron/Flow.
3. Postcheck qua DOT/read-only tool:
   - Public CREATE `approval_requests` = 0;
   - Public UPDATE = 0;
   - Public READ unchanged;
   - unrelated permissions unchanged;
   - Directus/Nuxt/agent health PASS;
   - audit trace chứng minh mutation đi qua DOT.
4. Regression ⇒ rollback bằng DOT ngay và DỪNG.
## 5. Nhánh B — DOT thiếu đúng capability + biển tại chỗ

Ưu tiên reuse:
1. Nếu DOT hiện hữu chỉ thiếu **một operation nhỏ** và có thể sửa chính file/dispatcher hiện hữu, không tạo file/service/DB/token/secret mới: được bổ sung operation tối thiểu `directus permission revoke` theo pattern sẵn; DOT tự nạp secret từ Secret Manager; allowlist `approval_requests` + `create|update` hoặc #620/#621; có dry-run/readback + rollback.
2. Nếu phải tạo file/tool/service/secret mới, thay schema, hoặc không có pattern DOT đủ tin cậy ⇒ **DỪNG** và ghi exact gap. Không fallback REST/SQL.
3. Sau extension nhỏ PASS, quay lại Nhánh A.

Biển chỉ dẫn:
- AGENTS A10-R3: chỉ kiểm, Agent không sửa luật nền.
- `view.html` SEC1: chỉ kiểm.
- `report-pg`/DOT operator-help: nếu thiếu biển, ghi exact source path + đúng câu `DIRECTUS/PG: DOT ONLY · Secrets: Secret Manager · No direct login/write`.
- Trong RUN này không rebuild/restart Nuxt chỉ để thêm chữ. Chỉ được thêm câu đó vào **file help/text hiện hữu** nếu không cần build/restart/reload và không tạo file mới; còn lại để lần bảo trì UI kế tiếp.
## 6. Nghiệm thu SEC1A-DOT

XONG khi:
- cơ chế DOT + Secret Manager được xác minh mà không lộ secret;
- A đóng qua DOT: CREATE=0, UPDATE=0; READ/quyền khác unchanged; audit trace/health PASS;
- B vẫn PASS/TEMPORARY;
- biển AGENTS + task rõ; report-pg/operator gap được chỉ đúng chỗ.

DỪNG khi thiếu capability cần file/service/secret mới, DOT không có rollback/allowlist, phải dùng login/direct API/SQL, B mất containment, hoặc có regression.
## 7. Report — chỉ SSOT hiện hữu

Không tạo report/file mới.

`view.html` §9: cập nhật khối SEC1 với B status, cơ chế DOT/Secret Manager, A XONG qua DOT hoặc DỪNG vì exact capability gap, và biển nào đã có/chỗ nào đề xuất thêm đúng một câu.

`COLLAB.md`: cập nhật Dòng hiện hành; ghi `KQ@VPSUP-SEC1A-DOT-20260927-01 XONG|DỪNG`; P12 phần “native API” đánh dấu superseded bởi DROOT26/D19, không xóa lịch sử. Nếu DỪNG, không đưa lựa chọn “login Owner/direct API/SQL” lên Owner.

Commit qua `fs_transaction`: `[Claude Code] VPSUP-SEC1A-DOT · kiểm DOT gate và đóng Public write`.
Kết thúc đúng một dòng XONG hoặc DỪNG.
## 8. Sau SEC1A — không làm

Nếu XONG: Host đi BK1 backup → persistent hardening VPS2. Không tự nhảy bước.
