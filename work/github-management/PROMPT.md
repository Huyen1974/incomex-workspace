# PROMPT — GHM C1B CLOSE · CÒN THIẾU SAU P61 (DRAFT)

RUN_ID: GHM-C1B-CLOSE-20261026-02
STATUS: DRAFT_FOR_CLAUDE_REVIEW_P62 · NOT_READY · NO_RUN
PREVIOUS_RUN: GHM-C1B-CODEX-BASELINE-MANUAL-CD-20261026-01 = P61 XONG CÓ GIỚI HẠN; mọi READY cũ là lịch sử, không phê duyệt RUN này.
EXECUTOR_DE_XUAT: Codex CLI/Desktop trên Mac. Claude Chat là Reviewer; GPT Host chốt chữ ký mới; Owner chuyển lệnh. KST Claude Code CLI giữ vai trò Chief sau C1B.

## Mục tiêu / phạm vi
Khép đúng phần thiếu của C1B tại P61, không làm lại phần đã nghiệm thu: khôi phục đường deploy/rollback thật cho Agent Data và Web từ hai GitHub main đã có CI, và chuyển 3 nhóm audit sang phép kiểm VPS tương đương khi thực sự an toàn. Giữ runtime cũ healthy cho tới khi candidate đủ chứng cứ; kết thúc diễn tập vẫn trả về bản cũ khỏe. Không tự làm C3/C2/C4.
Repo mã chỉ PRIVATE Huyen1974/agent-data-test và Huyen1974/web-test; incomex-workspace chỉ ghi hồ sơ. Không archive thêm, không đổi public/private, mua gói, force-push, xóa main/tag, mở auto-CD, đổi DB/PG/Qdrant/Directus/compose/nginx/Guard ngoài phạm vi. Không đẩy token/config nhạy cảm vào repo công khai.
Codex/Claude Code CLI trên Mac được dùng gh phiên Owner, SSH/GSM và quyền đã cấp; không đòi PAT hay tài khoản mới để thay quyền Mac. CI chạy từ PR không đọc secret/GSM, không được root/Docker socket. VPS-GHI chỉ giữ lúc áp host; code/CI/đọc audit độc lập vẫn tiếp tục khi cờ host bận, cuối cùng KQ sạch/NEXT_TRIGGER.

## Kế thừa bắt buộc
Đọc AGENTS.md và task COLLAB §0/P58–P62, ROADMAP, C1B-REPORT; P61 hash/manifest private, cờ VPS-GHI/Guard PRE, repo main và runner hiện tại. Ghim và so live SHA lại trước mutation: AD main e6274592b9b8a291e4b9aeafcdf55370a10e09f4; Web main 747c3b12c893a4186c197f17d312e38da7ed654f4. Nếu main tiến bởi người khác, đối chiếu thật và xử lý riêng nhánh, không reset.
C1A CI 2/2, C1B S1/S2 baseline, 2 builds, script/known-good và S7 archive đã có. KHÔNG cài runner lại, không baseline từ đầu, không promote lịch sử cũ, không xem Web runtime Nuxt 4 = source Nuxt 3. Token Directus cũ HTTP 401 là nợ lịch sử, không tự xoay key/điều tra thêm.

## R1 · Khép Web candidate ở nguồn, không vá output
Trên nhánh sửa riêng từ Web main: tái hiện continuity.css + interaction.js 404 trong canary, sửa cơ chế tham chiếu asset khi Nitro bundle chuyển import.meta.url; ưu tiên thay đổi source nhỏ và test hồi quy 2 tài nguyên. Không nâng Nuxt/framework đồng loạt nếu không có bằng chứng cần thiết; báo rõ Nuxt source 3.20.2 với runtime 4.5.2 và ảnh hưởng contract.
Rebuild từ lockfile bằng resources bounded, tái dùng cache/known-good đã có. Canary: ít nhất 8 route cũ, 2 asset phải 200 + nội dung/type đúng, và các contract quan trọng theo P61. HTTP 200 HTML không thay kiểm CSS/JS. Không deploy nếu 2 asset hay contract chưa đạt. Đẩy nhánh → CI trên đúng commit mới rồi main fast-forward non-force khi đã đủ điều kiện/Owner RUN; không tự merge mã GitHub cũ.

## R2 · Gỡ khác biệt Agent Data Compose mà không đổi production config
So effective service config hiện dùng (docker inspect/container fingerprint + mounts/env đã ẩn giá trị) với compose rendered config và overrides; chỉ ghi diff đã khử bí mật. Xác định config-hash lệch do đâu, đường chạy candidate image và rollback old digest với đúng network/volumes/env/port/user/entrypoint.
Nếu không chứng minh được hoàn nguyên đúng trạng thái old, KHÔNG restart AD. Không đổi Compose/nginx hoặc nâng quyền runner để ép PASS. AD canary/contract thật phải đạt trước deploy. Nếu blocker AD chưa giải được, ghi riêng AD và tiếp tục Web/audit độc lập.

## R3 · 3 audit: giữ tính năng, chuyển khi đáng tin
Đối chiếu P17/P61 và đúng 3 workflow: AD Data Lifecycle, Web Health Check, Web ops-smoke. Bảo toàn schedule, tần suất, kết quả và test semantics. GH-hosted jobs cũ vẫn ACTIVE đến khi đường thay PASS thật.
AD Data Lifecycle cần API key; Health Check có nhiều check cần API key. Phân biệt secret thật với biến vô dụng: VPS_SSH_KEY của Web Health Check được khai trong CHECK 12 nhưng không thấy dùng trong script; đọc xác minh rồi loại dependency giả ở candidate, không hủy kiểm tra PG.
Với audit cần credential, ưu tiên đường trusted sẵn trên VPS (nếu có và chứng minh cùng contract) để thực thi phép kiểm nhạy cảm, CI PR chỉ nhận kết quả không bí mật; không cấp GSM/secret/SSH/root cho persistent PR runner. Nếu chưa có đường hợp lệ thì GIỮ HOSTED và ghi điều kiện cần, không triển khai gateway mới.
Ops-smoke: kiểm nguồn 403 của Directus /server/health (public ACL/WAF/endpoint contract) so với health thật từ đường đáng tin; 403 KHÔNG là PASS. Không retry mù 10 phút; nếu có contract tương đương hợp lệ thì chạy thử trên runner VPS, verify Page+Asset+Health; ngược lại giữ workflow cũ. Không thay quyền Directus chỉ để lên đèn xanh.
Với từng nhóm: chạy candidate có log, SHA, runner label, lịch/triggers, test coverage chứng minh; chỉ promote workflow thay thế khi PASS tương đương. Không dùng việc thiếu secret làm lý do lược bỏ test. Tính phút hosted giảm thực đo, ngân sách Actions $0+Stop vẫn giữ.

## R4 · Diễn tập release/rollback thực tế theo app
Chỉ khi R1/R2 của app riêng đã PASS. Dùng script deploy P61/Điều 30–31 và known-good pin; không viết đường deploy thứ hai. PRE: app old healthy, exact runtime digest/config/output, rollback snapshot verified, Guard/VPS-GHI. Deploy lần lượt một app qua script, kiểm contract, rollback về old rồi check hash/health/StartedAt; sang app khác nếu an toàn.
Tổng tối đa 4 restart app cho hai diễn tập, cộng một recovery khẩn cấp known-good nếu rollback chưa khỏe như P50. Nếu không bảo đảm rollback thì dừng CHỈ app đó trước restart. Không restart DB, nginx config, toàn VPS; chỉ nginx reload đúng điều kiện đã được nghiệm thu trong P50.

## R5 · Kết quả, khả năng phát triển song song
Đề xuất Claude xét thêm: chuẩn bị CI trigger push/PR trên dev/* cho C3 (hiện probe C1B chỉ c1b-baseline), thử nhánh làm việc song song KHÔNG merge/deploy. Không tự nhận C3 RUN/PASS trong lượt này nếu Host/Owner chưa ký phần mở rộng.
KQ bảng riêng: AD deploy/rollback, Web deploy/rollback, 3 audit, CI triggers, Guard scoped, GLOBAL_GUARD nợ kế thừa, SHA GitHub/source/runtime, phút hosted, trạng thái VPS-GHI. Chỉ XONG khi 2/2 app thực tế rollback và 3/3 audit tương đương chuyển VPS; thiếu mục phải XONG CÓ GIỚI HẠN kèm bằng chứng/NEXT_TRIGGER. Hoàn nguyên và giữ app cũ healthy khi có lỗi. Ghi COLLAB, ROADMAP, README cùng commit và bàn giao Claude/GPT, không tự tiếp C2/C3/C4.

## Chặn scope
Không tạo key mới để khắc phục lỗi 403; không dùng token Directus lịch sử 401; không tự sửa PG/schema/migration; không cấp secret cho CI PR; không bỏ phép kiểm để được PASS; không chữa đèn Guard cũ #11; không archive/xóa thêm repo; không reset GitHub main; không thay repo public/private; không mua Pro. Khi blocker thật, hoàn thành mọi nhánh độc lập có thể chứng minh an toàn rồi báo chính xác mục còn thiếu.
