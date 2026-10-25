# ROADMAP — github-management V0.3 · 24/10/2026
**Trạng thái: Claude P5 + GPT Host P6 ĐỒNG THUẬN KỸ THUẬT CÓ CỔNG · CHỜ OWNER GO · KHÔNG RUN.**  
Đầu việc chi tiết cùng mã ở [KE-HOACH.md](KE-HOACH.md) §2; lý do từng sửa ở [COLLAB.md](COLLAB.md) P5 (C1–C10). V0.1 = P3 · V0.2 = P4 · V0.3 = V0.2 + C1–C10.
Ưu tiên 1: nhân không gian làm việc để 3–5 agent viết mã song song trên hai repo hiện hữu; Claude Code CLI làm kỹ sư trưởng (KST) — người duy nhất ghi `main`; sau đó tự động giao batch ban đêm. Không dựng thêm repo hay máy chủ chỉ để được code song song.

## 0. Giới hạn
- Hai kho `Huyen1974/agent-data-test`, `Huyen1974/web-test` giữ PRIVATE (lịch sử chưa quét bí mật). Khoá `main` trên kho private cần GitHub Pro (§V) ⇒ Owner mua Pro ở đầu R2, sau khi ngân sách Actions $0 «dừng khi chạm mức» đã có (R1).
- Codex phụ trách R0–R2 và điều phối R4/R6. **Ghi `main` chỉ KST** bằng chìa riêng (R3 trở đi); Codex không cầm chìa KST. GPT Host chốt PROMPT; Owner duyệt mutation production.
- Không đổi VPS runtime, remote Git, deploy, secrets, cron, Guard ngoài RUN hợp lệ. GitHub Actions: không bắt buộc tắt; bắt buộc không phát sinh chi phí mất kiểm soát — ngân sách $0 + «Stop usage», chỉ giữ workflow cần (Owner 25/10, thay câu 23/10).
- Kiểm thử unit trong sandbox riêng của từng ghế; pilot R4 chọn việc có unit test nên chưa cần staging; không dồn build/test lên VPS1 (swap đầy).

## I. Bảng mốc
| Mốc | Ai | Việc | Đạt khi / điểm DỪNG |
|---|---|---|---|
| **R0 — Đo** ✓ P12 · **R1 — Khoá chi phí** | 🤖 Codex | R0 (xong, P12) chỉ đọc: 2 thư mục mã VPS `docker/agent-data-repo`, `docker/nuxt-repo` (nhánh, HEAD, sạch/bẩn, HEAD có trên `vps-daily-*` chưa); dịch vụ → commit đang chạy; workflow + Dependabot; mọi thẻ/app/khoá ghi được 2 kho (tên + quyền, không in giá trị); có gì đang kéo `main` không; đường gọi cho R6 (Dot→Codex, Codex cloud, Claude Code web). R1 (Owner 25/10: chỉ cần kiểm soát chi phí, không cần tắt Actions — PROMPT GHM-R1-COST): đo billing; ngân sách Actions $0 + «Stop usage» + cảnh báo; tắt riêng từng workflow thừa (bật lại được), giữ 3 nhóm kiểm cần chạy trên phút miễn phí; Actions vẫn bật; không runner. Self-hosted chỉ xét khi phút miễn phí không đủ cho 3 nhóm. | R0: bảng nguồn / đang chạy / thẻ (P12). R1: ngân sách $0 + Stop có thật; active chỉ còn 3 nhóm; tiền phát sinh 0. |
| **R2 — Khoá + vai** | 🤖 Codex (GitHub) · Claude Code CLI trên VPS (chìa KST, PAT backup; cờ VPS-GHI + Đ30/31) | Ruleset chỉ `main` 2 kho: update · deletion · non_fast_forward, bypass duy nhất DeployKey. Chìa KST sinh trong bản clone riêng của KST trên VPS (remote riêng, không phải khoá mặc định của máy); 1 deploy key ghi/kho. Mỗi ghế dev 1 thẻ fine-grained (Contents + Pull requests, không Administration); hạ quyền mọi thẻ admin trong bảng R0. Codex soạn AGENTS.md ≤ 1 trang + mẫu PR 6 ô (chưa commit). | T-a, T-b, T-d, T-e PASS bằng danh tính thật (COLLAB P1 §4); 0 thẻ admin ngoài Owner trên web (passkey). |
| **R3 — Mã nền = VPS** | KST | Tag `archive/main-<ngày>` cho main cũ. Bản clone KST lấy HEAD thẳng từ thư mục mã VPS (cùng máy), merge main cũ với chiến lược giữ nguyên cây VPS ⇒ `main` tiến thẳng, không force-push (T-c). Commit luật R2 lên trên. **Cầu nối tới R5:** mỗi sáng KST merge commit VPS mới vào main. | `git diff <HEAD VPS> main` chỉ khác các tệp luật; main cũ là tổ tiên; tag khôi phục được. |
| **R4 — Thử 3 ghế** | Codex (cloud) · Claude Code (cloud) · Hermes (VPS) · KST | 3 việc thật, khác khu tệp, có unit test, ≤ 2 giờ; mỗi ghế sandbox riêng, nhánh `dev/<ghế>/<mã việc>`, phiếu 6 ô. KST duyệt trên main mới nhất: NHẬN / SỬA / TRẢ LẠI / BỎ. | 3 PR thật; ≥ 2 NHẬN; 0 lần dev ghi được main; Actions 0; ghi giờ chờ từng PR. |
| **R5 — Triển khai từ main** (∥ R6) | KST · 😊 Owner GO (nối lại GitHub→VPS — luật DROOT56) | Theo cờ từng khu: VPS lấy đúng SHA main bằng thẻ chỉ đọc → build/khởi động lại theo cách đang dùng → health; lùi = SHA trước. Rồi **khoá VPS chống sửa mã nhầm (P7):** root `agent-data` của cổng workspace → chỉ đọc; 2 thư mục mã gắn chỉ đọc, chỉ bước deploy của KST mở rồi khoá lại; `origin` giữ URL chết DROOT56, deploy dùng URL riêng + thẻ chỉ đọc; Guard: thư mục sạch, HEAD = SHA đã deploy, đang chỉ đọc; biển `00-NHAN-THU-MUC.md` chỉ đường GitHub. Dừng backup ngược khi đã khớp. | SHA đang chạy = SHA main; diễn tập lùi PASS; sửa tay ⇒ «Read-only file system»; sửa qua MCP ⇒ `READ_ONLY_ROOT`; mở khoá ngoài deploy ⇒ Guard đỏ. |
| **R6 — Ca đêm** (∥ R5) | 🤖 bộ giao việc đã chứng minh ở R0 · KST | Giao 3–5 việc buổi tối; mỗi việc biên nhận, hạn, dừng sạch; lỗi một việc không chặn việc khác; sáng KST duyệt, bảng 1 dòng/việc; không deploy. | ≥ 2/3 NHẬN, không ai canh đêm. Không có đường gọi thật ⇒ NO-GO, không chạy nền giả. |

**Thứ tự:** R0+R1 → R2 → R3 → R4 → (R5 ∥ R6). R6 được viết code/PR song song, nhưng **cấm merge vào main khi R5 đang chốt release/deploy/rollback**. Đọc cổng P6 COLLAB và KE-HOACH §5. Mỗi mốc một RUN.

## II. Ba điều chỉnh với lời Owner
1. «Tắt Actions» → Owner 25/10 đổi thành «kiểm soát chi phí»: Actions vẫn bật; ngân sách $0 + «Stop usage» phải có trước khi gắn thẻ mua Pro.
2. «Xoá mã main hiện tại»: không xoá. Main cũ thành tag + cha của commit merge; cây main mới đúng bằng cây VPS. Đổi main không chạm production vì GitHub→VPS đang cắt (R0 xác nhận).
3. «Repo mở»: giữ private vì lịch sử chưa quét bí mật; khoá bằng Pro thay vì public.

## III. Ranh giới repo (Codex đo ở R0, KST ghi ở R3)
| Repo / vùng | Dự kiến sở hữu | Ngoài phạm vi |
|---|---|---|
| agent-data-test | Ứng dụng Agent Data/RAG, code truy vấn/ingest, adapter vector/PG, MCP/backend thuộc Agent Data, test liên quan | Dữ liệu PG/Qdrant, env, secret, backup, cấu hình hệ điều hành |
| web-test | UI/Nuxt, frontend, web integration/Directus interface, frontend tests | Data Directus/PG, secrets, RAG core, cấu hình runtime chưa phân nhà |
| OUT-OF-SCOPE | DOT runtime, Graph, nginx, systemd, Guard, scripts/compose chung chưa rõ chủ | Không tự ép vào 2 kho, không tự mở repo ops mới (ghi nợ «kho ops») |

## IV. Nhận việc / review / ca đêm (dùng lại hội đồng hiện có)
- Host chuẩn bị batch phiếu 6 ô; Owner duyệt batch. Ghế đọc AGENTS.md của kho + phiếu; mỗi ghế sandbox + nhánh riêng; viết mã không cần cờ VPS-GHI.
- KST xử lý PR theo hàng đợi trên main mới nhất: NHẬN / SỬA / TRẢ LẠI / BỎ; xung đột trả cụ thể, không tự chọn ours/theirs; main đổi sau khi test thì test lại; tác giả không tự duyệt; PR do KST tự viết cần ghế khác hãng duyệt.
- Giao việc đêm chỉ qua đường đã chứng minh có biên nhận (R0); chưa có thì Owner giao tay. Sáng: bảng mỗi việc một dòng (KE-HOACH §4); mặc định không deploy.

## V. Bằng chứng (chỉ đọc, không mutation)
- GPT 24/10: agent-data VPS nhánh `claude/gpt-operation-id-20260918` HEAD 75ed0e80; GitHub main 0a26280b (agent-data-test), 07caed3b (web-test), cả hai private, chưa protected; 17 + 11 workflow, Actions web còn chạy 24/10; ruleset kho private không khả dụng trên plan hiện tại (API yêu cầu Pro/public).
- Claude 24/10: `vps-daily-20261023` của agent-data-test = 75ed0e80 = HEAD VPS ⇒ lịch sử VPS đã nằm trong Git. agent-data đang chạy image dựng từ b6ebaf94, HEAD 75ed0e80 đã build chưa tạo lại (đo 23/10, HJW P359) ⇒ «đang chạy» ≠ HEAD. «UI master af8d1404» là kho ui-preview, không phải web-test; nguồn web-test trên VPS là `docker/nuxt-repo`, chưa đo.
- Ruleset `gateway-only-writes` của `incomex-workspace` (kho tài khoản cá nhân, 25/09): bypass chỉ DeployKey đã chặn cả tài khoản Owner (HTTP 409) ⇒ mô hình một chìa chạy được trên tài khoản cá nhân.
- Trước mỗi RUN lấy lại HEAD tại thời điểm đó. DRAFT không cấp quyền thay đổi gì.
