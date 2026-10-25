# HJW · KẾT THÚC PHẦN NÚT HERMES — KHÔNG LÀM LẠI
RUN_ID: HJW-HERMES-FINALIZE-20261025-02
STATUS: HOST_DRAFT · Chỉ RUN sau READY@last-touch-PROMPT tại task COLLAB, Owner chuyển tay Claude Code CLI.
Host: GPT Chat P394 · Reviewer nền: Claude Chat P392 (63f55924), GPT Host P393 đóng RUN cũ.
Executor_Surface: Claude Code CLI MỚI (KHÔNG resume phiên cũ).
Write_Path: Incomex MCP workspace_* cho hồ sơ, VPS qua đường quản trị/apply-v0 đã duyệt và VPS-GHI CAS. Chưa có quyền thực thi cho đến khi Owner giao.

**Mục tiêu duy nhất:** đóng phần C nút nâng Hermes đã áp dở; giải phóng VPS cho việc khác. P386 A/B XONG, P390 đã áp 3 file+mốc, P393 hành chính STOP/KQ DỪNG phiên cũ và VPS-GHI trống. **Tuyệt đối không làm lại token/Kuma, sudo/GSM, 69/69+32/32, A/B, không copy backup nhiều GB, không nâng stable khi chưa có phiên bản mới, không tạo dịch vụ/plugin/timer mới.**

**S0 (read-only, một lần):** Đọc AGENTS, root+HJW COLLAB P386/P390/P391/P392/P393 và PROMPT; kiểm latest READY, 0 RUN xung đột, STOP cũ, VPS-GHI trống. Kiểm có **bất kỳ tiến trình/job nào còn chạy từ RUN cũ** hay lượt cập nhật đang hoạt động không bằng đường VPS quản trị; mơ hồ ⇒ DỪNG/không restart. Kiểm config Guard 518/518 (đo tươi) và bản lùi byte-đúng của đúng các tệp P390. Sau S0 PASS ghi STARTED, dùng CAS nhận VPS-GHI cho thao tác ghi.

**S1 (kiểm đã áp, không triển khai lại):** Kiểm root `offer-tick` đã chạy qua nhịp thực, log từ lúc P390 áp có lỗi lặp không. Nếu trạng thái đúng và Hermes rỗi, **restart chỉ `hermes-gateway` một lần** để nạp plugin, smoke gateway/serve/Telegram và nút. Nếu chưa rỗi, dừng sạch, không cắt lượt model và không giữ lease chờ. Không nới khóa `.git`, không cho app Mac nâng VPS.

**S2 (kiểm nhanh, không kéo dài):** `hermes-safe-update check` chạy với khóa `.git` chỉ-đọc hiện hành, đo thời gian và tránh root-owned files trong `.git`. Không chạy fetch nâng thật. Đối chiếu S2 P388: `DUONG_GON_CHUA_CHUNG_MINH` — **giữ nguyên đường lùi đầy đủ**, không tiếp tục xây snapshot gọn. Chạy Guard POST/Điều 30–31 **chỉ với các thay đổi P390**. Lỗi thì lùi delta lỗi qua bản byte-đúng đã có và KQ DỪNG, không sửa Guard để che. Kiểm công việc đang chạy khác không bị ảnh hưởng.

**S3 (thoát khóa trước khi hỏi người):** Xác minh không job RUN tồn tại ngoài Hermes service thường trực; **nhả VPS-GHI bằng CAS ngay khi hoàn tất thao tác máy**, không giữ cờ chờ Owner. Gửi thẻ Telegram **DIỄN TẬP** đúng bot/Owner bằng đường hiện hữu, **không áp bản nâng thật**. Chạy lại đúng các negative chưa có chứng cứ runtime; không làm lại 35/35 và 15/15 unit test P390. Nếu Owner không bấm, ghi `OWNER_TAP_NOT_YET_OBSERVED` và đóng KQ, không giữ lượt chờ.

**S4 (một KQ, đóng):** KQ XONG chỉ khi gateway và root tick có bằng chứng, Guard POST đúng, thẻ đã được gửi và đường điều khiển có test dry-run/safe negative; nếu chưa đủ thì KQ DỪNG nêu một blocker duy nhất, **không mở vòng sửa vô hạn**. Ghi nhận live update khi có stable mới vẫn `NEXT_REAL_PATCH_UNTESTED`; đường gọn `DUONG_GON_CHUA_CHUNG_MINH`, giữ đường lùi cũ. Cập nhật Bảng/roadmap/Owner View và một biên nhận; 0 tiến trình tạm/cờ còn giữ. Không dọn báo cáo rời, không sửa N2 Dot/Graph/PG/Directus.

STEP_WALK_V1 (giới hạn một lượt máy, dừng sạch khi bị cổng từ chối, không hẹn nền):
| Bước | Ai/kích hoạt | Gate & bằng chứng | Nếu lỗi |
|---|---|---|---|
| S0 | Claude Code mới + Owner RUN | STOP cũ/KQ P393, không process cũ, rollback/Guard/VPS-GHI | KQ DỪNG, không mutation |
| S1 | Claude Code sau S0 | root tick, gateway idle, một restart, health | lùi đúng delta nếu cần, báo Host |
| S2 | Claude Code sau S1 | check .git RO, Guard POST footprint đúng | KQ DỪNG, không nới khóa |
| S3 | Claude Code sau S2 | xác minh no jobs; trả VPS-GHI; gửi thẻ demo | báo giới hạn, không chờ Owner |
| S4 | Claude Code cuối lượt | một KQ; task/Owner View đúng; 0 lease | Host rà, đóng |
