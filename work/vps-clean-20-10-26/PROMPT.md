# PROMPT — VPSC2-RAG-A-TRUST-GATE-20261023-01

DRAFT — KHÔNG RUN. Chỉ chạy khi trong task COLLAB có Claude Chat `ACCEPT@<full SHA last-touch PROMPT.md>` + GPT Host `READY@<cùng SHA>`; Owner dán cho Claude Code CLI.
RUN_ID: VPSC2-RAG-A-TRUST-GATE-20261023-01
Executor_Surface: Claude Code CLI trên Mac Owner.
Write_Path: Incomex workspace_* root=workspace cho STARTED/KQ/COLLAB; VPS1 qua đường mutation đã duyệt (`incomex-config-apply-v0`/Config Guard, DOT hợp lệ); không bypass gateway/Guard.
Đọc: AGENTS.md → root COLLAB → `work/vps-clean-20-10-26/COLLAB.md` §0/Bảng/P13–P15 → PROMPT.md → `BAO-CAO-Agent-Data-RAG-2026-10-23.md` (commit 3ff49530). R3 cũ SUPERSEDED_UNRUN, không chạy.

MỤC TIÊU RAG-A (sửa bởi Claude P15): làm cho phép đo RAG nói thật và lập danh sách sai lệch đầy đủ làm đầu vào RAG-B — CHỈ PHÍA HOST. KHÔNG build/restart/thay container Agent Data; KHÔNG sửa/xoá/reindex vector, KB PG, Qdrant. Mọi sửa mã Agent Data (health, log, classifier gốc, sync bền, payload revision) dồn vào MỘT bản phát hành RAG-B để chỉ thay container một lần. Không tuyên bố RAG_DATA_CLEAN hay GO_PRODUCTION.

S0 READ GATE (≤10′): đúng ACCEPT + READY cùng SHA; không STOP/STARTED trùng; root VPS-GHI CAS (bận ⇒ KQ DỪNG sạch, không ngồi chờ). PRE: container/image/RestartCount Agent Data, số điểm 2 collection Qdrant, COUNT KB active, Guard 22 đèn theo ID, Config Guard baseline các đích sẽ chạm, đường lùi. Ghi STARTED + Bảng cùng commit.

A1 · DOT audit nói thật (≤25′) — `dot-vector-audit` và wrapper đang chạy (đọc bản runtime, không dùng bản Git thay):
1.1 Ba trạng thái: exit 0 = đo được, in rõ `STATUS=CLEAN` hoặc `STATUS=DRIFT` kèm số từng loại · exit 2 = `STATUS=ERROR` (sai xác thực, timeout, HTTP ≠ 200, JSON thiếu trường). Không còn «Orphans=0, Ghosts=0» khi gọi lỗi; bỏ đường fallback credential cũ. DRIFT đã biết (nằm trong manifest A2) không làm đỏ đèn; ERROR mới đỏ. Trước khi đổi, liệt kê mọi consumer của mã thoát/đầu ra (cron 04:30, Guard, bản tin); consumer nào đổi nghĩa thì ghi rõ hoặc SKIP A1.
1.2 Đếm điểm `document_id` rỗng ở CẢ HAI collection bằng scroll Qdrant chỉ đọc (`with_vectors=false`), in vào kết quả audit.
1.3 Mục bị classifier loại (`directory_like_path`…): wrapper đọc lại từng mục qua đường đọc hiện có; có body ⇒ báo GHOST thật. Sửa gốc classifier trong Agent Data để RAG-B.
1.4 Phép thử âm trên BẢN SAO: sai khoá ⇒ exit 2; URL Qdrant/Agent Data hỏng ⇒ exit 2; chạy thật `auto_heal=false` ⇒ exit 0 + `STATUS=DRIFT` có đủ 2 orphan, 9 blank-ID, 1 missing, comment-2430. Thiếu một ca ⇒ không áp A1.
1.5 Áp qua apply-v0/Config Guard; cập nhật sổ DOT (`dot_tools`) nếu đổi phiên bản; đủ 4 ô Điều 30/31.

A2 · Manifest đầy đủ, CHỈ ĐỌC (≤20′) — ghi thành mục «Phụ lục M · manifest 23/10» cuối `BAO-CAO-Agent-Data-RAG-2026-10-23.md` (không tạo tệp mới; chỉ ID/đường dẫn/hash/số đếm, không chép nội dung tài liệu):
2.1 Mỗi sai lệch một dòng: loại (orphan · blank-ID · missing · misclassified · noise · stale) · collection · ID/điểm · trạng thái nguồn PG (active/soft-deleted/không có) · luật áp dự kiến (L1–L4, P15) · rủi ro.
2.2 IU: đối chiếu 2 chiều 141 mã nguồn với bảng nguồn IU qua đọc PG chỉ đọc; không đọc được ⇒ UNKNOWN kèm lý do, không PASS.
2.3 Nhiễu: đếm tài liệu thử/sức khoẻ trong kho — đã biết `task_comments` 2393–2471 (79 bình luận «Health check: OPS write OK at undefined», flow «OPS Write Health Check» 6h tạo từ 03/10); liệt kê thêm mẫu thử khác nếu thấy.
2.4 Độ cũ: payload hiện không có revision/hash ⇒ chỉ so được tài liệu 1 chunk; ghi số tài liệu so được/không so được (căn cứ cho RAG-B thêm revision vào payload).

A3 · Sao lưu cấu hình hiện hành (≤15′): đưa `/opt/incomex/config` (và thư mục baseline Config Guard nếu dung lượng nhỏ) vào job sao lưu offsite mã hoá đang chạy phù hợp nhất — KHÔNG tạo job/cron mới. Qua apply-v0; `bash -n`; dry-run liệt kê thấy đường dẫn mới. Nếu một lượt thật < 10′ và không trùng lịch thì chạy 1 lần và kiểm Drive có tệp + hash; không thì ghi lượt lịch kế tiếp để S0 của RAG-B kiểm (không ngồi chờ).

A4 · Tắt 2 flow sinh lỗi/rác — CHỈ khi task COLLAB có dòng `OWNER_GAT_A4` (thiếu ⇒ SKIP cả A4):
4.1 Thêm lệnh `set-status <flow-id> active|inactive` cho DOT `dot-directus-flow` (hiện chỉ list/show/trigger — lý do R2-6 phải SKIP): có kiểm trước/sau, nhật ký, đăng ký sổ DOT; thử trên flow giả trước khi dùng thật.
4.2 Đổi INACTIVE đúng 2 flow: «OPS Write Health Check» (6h; mỗi lượt tạo một bình luận thử lọt vào RAG) và «[DOT-REG] Count Refresh (6h)» (16 PATCH/ngày bị S129-A chặn). Không xoá flow; không xoá bình luận đã có (RAG-B xử theo luật L3). Cổng: không flow/route/monitor nào dùng kết quả của chúng — có ⇒ SKIP đúng flow đó.
4.3 Ghi mốc lượt 6h kế tiếp để S0 RAG-B kiểm «không còn bình luận mới/PATCH lỗi» (không chờ).

S3 POST (≤10′): Guard 22 đèn theo ID so PRE; Config Guard MATCH; Agent Data container/image/RestartCount KHÔNG đổi; số điểm 2 collection và COUNT KB không đổi do RUN; audit thật exit 0 + DRIFT đúng danh sách; lỗi mới ⇒ lùi đúng mục, ghi PARTIAL.

S4 KQ (≤10′): ghi KQ + Bảng duy nhất trong task: A1–A4 APPLIED/SKIP + lý do + sha/đường lùi; manifest ở Phụ lục M; trả VPS-GHI; 0 tiến trình nền/tệp tạm. Lỗi thuộc chủ khác (503, snapshot lock, fsck exit 0, wait-online, OOM mapping, context-pack-verify) không sửa chéo.

STEP_WALK_V1:
| Bước | Ai | Trigger | SLA | Evidence | Hỏng thì ai biết, bao lâu | Bước kế |
|---|---|---|---|---|---|---|
| S0 | Claude Code | Owner dán sau READY | ≤10′ | ACCEPT/READY SHA, VPS-GHI, PRE | KQ DỪNG ngay trên task | A1 |
| A1 | Claude Code | S0 PASS | ≤25′ | 4 ca thử âm, apply-v0, 4 ô Đ30/31 | Guard 5′ → Kuma → Telegram ≤10′ | A2 |
| A2 | Claude Code | A1 xong/SKIP | ≤20′ | Phụ lục M đủ loại, IU 2 chiều/UNKNOWN | GPT + Claude đọc KQ | A3 |
| A3 | Claude Code | A2 xong | ≤15′ | dry-run có đường dẫn mới, sha | Kuma backup sẵn có | A4 |
| A4 | Claude Code | `OWNER_GAT_A4` có | ≤15′ | DOT set-status thử giả + 2 flow INACTIVE | RAG-B S0 kiểm lượt 6h kế | S3 |
| S3→S4 | Claude Code | mục cuối xong | ≤20′ | POST 22 đèn, số dữ liệu không đổi, KQ, trả VPS-GHI | Host nhận KQ | GPT soạn RAG-B |

Tổng ≤ 115′. Một dòng Owner: XONG|DỪNG · VPSC2-RAG-A · A1/A2/A3/A4=APPLIED|SKIP · prod_data_changes=0 · AgentData restart=0 · Guard/Kuma · VPS-GHI trả · commit.
