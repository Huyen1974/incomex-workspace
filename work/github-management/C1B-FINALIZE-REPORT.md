# C1B-FINALIZE — KQ XONG CÓ GIỚI HẠN

RUN_ID: `GHM-C1B-FINALIZE-20261027-03` · Executor: Codex · 27/10/2026.
Căn cứ: Owner RUN; GPT Host P69 READY PROMPT last-touch `88fbbda8c3da2043539d8e41701f21649b3ea64a`; SHA256 `b6a9c6d10ba6ee890cfd3a264c9ad385fa495935a011f59a7ae8495a6c85824b`. P70 STARTED, P71 KQ. Không dùng chữ ký cũ, không đổi PROMPT.

## 1. Kết luận cho Host

| Phần | Kết quả thực tế |
|---|---|
| S0 | PASS: quyền/READY/STOP/main/runner đối chiếu; P66 manifest 96/96; Guard PRE 22/22; VPS-GHI nhận CAS |
| S1 Agent Data | PASS mã + 14 tests + CI VPS + canary PG read-only; main fast-forward `5bc8a3f8cb0ba86654fe4c0e683abbc6e6f9469f` |
| S2 Web Health | CHƯA NGHIỆM THU: candidate chạy đủ 13 CHECK, 7 PASS, 1 FAIL dữ liệu, 5 lỗi kỹ thuật/chưa đo; không promote main |
| S3 AD deploy–rollback | DỪNG trước restart: script nguyên P61 chặn hash Compose; exact old image rollback còn gửi CREATE, trái điều kiện 0 DDL |
| S4 | KQ có giới hạn; phần P66 giữ nguyên; POST/receipt/cờ xem §5 |

`C1B_SCOPED=FAIL/CHƯA ĐẠT` · `AUDIT_EXECUTION_VERIFIED=PARTIAL` · `BUSINESS_HEALTH=FAIL` theo CHECK2, các nhánh bị HTTP401 vẫn UNKNOWN. Không coi job RED này chỉ gồm lỗi nghiệp vụ đã xác minh. Chưa đóng C1B, không chạy C3.0/C3/C2/C4.

## 2. Agent Data: phần đã hoàn thành và cổng dừng

Sửa nhỏ `ensure_tables()`: SELECT `to_regclass` cho 3 bảng + 3 index, qualify bằng `current_schema()`; đủ 6 thì return trước DDL. Thiếu tên giữ nhánh CREATE legacy, nhưng RUN không dùng nhánh đó trên production. Không so định nghĩa cột hay tự mở thêm điều kiện.

- Native gate: PG? **Có**, catalog `to_regclass/current_schema`; Directus? Không cần cho bootstrap kết nối PG; native khác? Giữ psycopg2/cursor và CI có sẵn; vì sao code? Hàm startup đang gửi CREATE vô điều kiện, cần một fast-path tại đúng hàm. [PostgreSQL functions-info](https://www.postgresql.org/docs/current/functions-info.html), [schema/search_path](https://www.postgresql.org/docs/current/ddl-schemas.html).
- Live PostgreSQL `180006`, effective schema `public`, search_path `"$user", public`; 6/6 đối tượng hiện hữu. Actual diagnostic `statement_verbs=["SELECT"]`, `ddl_statements=0`, `transaction_read_only=on`.
- 8 unit mới (đủ 6, từng đối tượng thiếu, SELECT lỗi) + 6 test kế thừa = **14 PASS**; quét delta gitleaks sạch.
- [CI 40445758771](https://github.com/Huyen1974/agent-data-test/actions/runs/40445758771): GREEN, runner `ghm-ci-agent-data-test`, đúng SHA `5bc8a3f…`, 03:43:35–03:44:04Z (29 giây). Main cập nhật non-force từ `2517394…`; chưa thay runtime.
- Candidate digest `sha256:eb7cd9a8724d1db92f2d06660d75ebccde930d63263970111d3c8d30b4448b74`, image Config bằng old. Canary read-only root/mounts/PG, listener bị khóa, workspace supervisor tắt; 0 Qdrant mutation attempts. `/info`, `/health`, `/kb/list?limit=1` đều HTTP200; list có mảng items và 1 phần tử. Canary đã xóa; giữ candidate/known-good.

**S3 không thể chạy đúng toàn bộ điều kiện đang ký:**

1. Script P61 SHA256 `7b1d917c18090d26b8700c2b0d0f37655228f89ade2668fe92605d0b2ef10ea6` còn nguyên. Gate so Compose rendered `d55d47897eb0596f2299aa1902694b7a383fdd2f5216c5c7ea43ec1a8d6fc9cb` với live label `b0a7eb7f556a1c259197e66f5e5f449de8b9db43ff66e9ac4e297dfb61b86346`: không bằng. P66 effective config 17/17 không tự thay thế gate này. Không sửa script/label/Compose để vượt.
2. Old image `sha256:46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c` chưa có fast-path; bootstrap chứa 3 CREATE TABLE + 3 CREATE INDEX IF NOT EXISTS. Hash hàm `453f3e0179c92e2d5ab45d491f2f19349c2499ad8676486f9abbb4288ffe91f7`. Restart về exact old sẽ gửi DDL; không được coi IF NOT EXISTS là 0 DDL, không âm thầm thay old bằng image đã vá.

Đây là blocker điều kiện thực thi, không phải thiếu quyền Mac và không phải auto-review mới của canary. **0 restart AD/Web, 0 production DDL**. NEXT_TRIGGER AD: Host chốt đường kiểm Compose hợp lệ và rollback đáp ứng no-DDL; không cấp DDL chung để lách.

## 3. Web Health: bằng chứng từng CHECK

[Candidate 40445988505](https://github.com/Huyen1974/web-test/actions/runs/40445988505), SHA `191ff455298c53d165d5b09e6298024f59c35ad0`, runner `ghm-ci-web-test`, 03:46:03–03:46:42Z (39 giây), **RED**. Cả 13 step đã chạy, không continue-on-error. Lịch cũ trên main vẫn ACTIVE, không disable cùng tên.

| CHECK | Kết quả candidate | Ý nghĩa/chứng cứ |
|---|---|---|
| 1 Services | PASS | HTTP200, Qdrant ok |
| 2 Integrity | FAIL nghiệp vụ theo luật cũ | 10.041 docs/20.295 vectors, ratio 2,02, sync_status warning; HTTP200/JSON hợp lệ. SQL read-only độc lập xác nhận 10.041 alive docs |
| 3 Content | PASS | 3 bản ghi và đường dẫn có thật, trang tải được |
| 4 Cache | PASS với WARN theo luật cũ | Không nâng WARN thành PASS toàn diện CDN |
| 5 Search | CHƯA XÁC MINH | HTTP401 text/html trước /chat; không kết luận zero-context/RAG hỏng |
| 6 Directus | Lỗi bài kiểm | ping/collection đạt; thêm curl --fail làm 401/403 dự kiến của /flows dừng step. Đã sửa trên nhánh, chưa chạy lại |
| 7 Structure | CHƯA XÁC MINH | /kb/list HTTP401; không coi danh sách rỗng là sạch |
| 8 Sync gap | CHƯA XÁC MINH | Không có cache đủ trang từ CHECK7; FAIL CANNOT_COUNT, không dùng 0 |
| 9 Registry | PASS | Đủ collections theo ngưỡng cũ |
| 10 Quality | CHƯA XÁC MINH | CAT-ALL=SUM atoms=2.144.349, Qdrant ok; audit-sync dùng key không qua auth, không có số orphan mới |
| 11 Rules | PASS | Kết quả theo luật blocking hiện có, không sửa dữ liệu |
| 12 PG/page | PASS tại lượt đo | 169/169 catalog/counts, 2.459 edges, 851 lifecycle, 10 rules; registry GET HTTP200 trong 2,590821s |
| 13 Reconciliation INFO | PASS INFO | 2.459 edges; giữ đúng ý nghĩa INFO |

**Đối chứng giới hạn 15 giây:** đúng một GET cùng URL/phương thức từ GitHub-hosted tại cùng candidate: HTTP200, 191 CAT-code occurrences, **11,334452s**; job hosted 16 giây thực (03:46:04–03:46:20Z). VPS 2,59s. Không tái hiện timeout ở lượt này; không đủ cơ sở tuyên bố hiệu năng luôn ổn định. Không tăng timeout, không polling hosted. Không đổi billing/budget; thời lượng trên là job elapsed, không phải hóa đơn đã xác minh.

**Phân trang:** helper đi `prefix=knowledge/`, limit500, next_offset tới null, trần128 trang/300s, kiểm HTTP/schema/duplicate/offset; CHECK8 dùng cùng danh sách hoàn chỉnh. Fixture 10.040 docs =21 trang; 11 test local PASS, gồm auth/schema/EOF/cap/duplicate/UNKNOWN và ngưỡng gap. SELECT độc lập production read-only thu **9.604** ID knowledge, SHA256 `e8215d52af884bc998554367c25789fe690dcdaa7031d77a48b2bd33e85b4f49`; đây chỉ là số phía AD, **không chứng minh gap** hay CHECK7/8 đạt. Thử đọc bảng Directus trong DB AD trả UndefinedTable (DB khác), chỉ đọc và không mutation; không dùng kết quả đó làm số 0.

**Auth blocker:** secret `AGENT_DATA_API_KEY` của Web có metadata cập nhật 15/03, repo AD 29/09. Cùng tên/header không chứng minh cùng giá trị. Không hiển thị/đổi key, không suy tuổi secret là bằng chứng chắc chắn sai key. Bằng chứng chắc chắn là Web candidate trả HTTP401 tại /chat và /kb/list. Token Directus cũ không dùng lại.

Bản sửa cuối lưu nhánh `c1b-audit-finalize-health` tại **`d3b1ec811eb79733a4b63fe30c2adaf3b4f935b1`**: giữ HTTP401/403 dự kiến của /flows, log lỗi audit-sync ra stderr, chuẩn hóa whitespace key như audit AD; bỏ job hosted đối chứng sau lượt duy nhất. Unit11 và gitleaks PASS, nhưng **SHA này chưa được chạy trên GitHub**. Web main giữ `728fa1deaee45b36c07714ede1da4c0633683e89`.

Bộ xét duyệt tự động từ chối yêu cầu push+dispatch candidate thứ hai, lý do coi P69 chỉ cấp một lượt candidate có secret. Không thử lại dispatch qua đường khác. Chỉ push riêng bản sửa (không có trigger push) được phép và đã xong. **NEXT_TRIGGER Web:** Host/Owner xác nhận cách xử lý auth bằng credential hiện có và cấp rõ lượt kiểm candidate bổ sung; đủ 13 kết quả đáng tin mới promote và chạy main. Không giữ RUN chờ trả lời.

## 4. Nợ dữ liệu và phần kế thừa

- CHECK2 vẫn RED với sync_status warning; không đổi ngưỡng. Server dùng khoảng ratio 2–3 trong khi audit in 2,5–4,5 khỏe: Host giao chủ Agent Data thống nhất tiêu chí, không sửa trong RUN.
- 2 orphan/1 ghost là kết quả Lifecycle **P66**, không phải phép đo mới của RUN này; audit-sync Web bị chặn auth nên không cập nhật số đó, không cleanup dữ liệu.
- Web Nuxt4 source/parity166/CI16/deploy–rollback P66 giữ nguyên; Lifecycle/ops-smoke vẫn ACTIVE trên VPS, schedules không sửa/không chạy lại. Web Health main còn hosted ⇒ chuyển audit mới đạt **2/3**.
- Runners cùng ID/StartedAt, online/idle, mỗi runner 1CPU/1,5GiB và MemorySwap=Memory. Không socket/root/key mới. Lịch sử mới chỉ job trusted main, cleanup có sẵn được chạy trước audit. C3.0 tách lane PR/audit vẫn là việc sau.

## 5. Guard, bằng chứng và đóng RUN

- Guard POST **25/25 PASS** lúc 03:53:24Z; footprint production **0 mục**, coverage0/0 đủ, `PREEXISTING_SAME #24`. Telegram receipt **message_id=309**, đã giao qua sender sẵn có. Receipt ghi rõ deploy/audit còn chặn, không chứng nhận rollback AD.
- `POST_SCOPED=PASS` cho phần đã thực hiện, **không thay thế C1B_SCOPED còn FAIL**. `GLOBAL_GUARD=PARTIAL`: Graph #24 đỏ có sẵn và 3 vùng UNKNOWN INV23; giao đúng Host, không sửa hộ. Snapshot storage còn UNKNOWN_CLASS/SLOPE kế thừa, không mở cleanup ngoài RUN.
- Production giữ image/start time cũ, hai ứng dụng healthy; deploy script/config hashes không đổi. 0 restart, 0 DDL, 0 canary/container/build tạm; giữ candidate và known-good. Lease deploy cũ vẫn đóng; RUN này không mở lease deploy. Cờ VPS-GHI trả trong cùng commit KQ; 0 RUN active Codex.
- RAM available lúc đóng khoảng4,59GB; đĩa65%; swap hệ thống gần đầy như nền. Runner không có thêm swap, không thay giới hạn; không kết luận toàn VPS hết rủi ro chỉ từ Guard scoped.

Bằng chứng chi tiết/log build/canary/SQL/CI/audit/Guard và source helper lưu private theo RUN_ID; repo public chỉ chứa kết luận đã lược thông tin. Manifest private gồm **28 tệp**, SHA256 **`405421593757c28a99517a7cfdb1d69e2f788a4f611a716edd62947d0b9418ca`**. Không đưa credentials, nội dung tài liệu hoặc đường triển khai nhạy cảm lên repo public.

Đã đọc luật root/current PROMPT/P61–P69, rules hai repo và skill incomex-rules; KB constitution trả tài liệu v4.6.3. Quy trình cũ cấm main/manual deploy được thay trong đúng phạm vi Owner/P69. Không cập nhật KB/OR vì P69 chỉ dùng workspace làm sổ điều hành; không thêm nguồn chuẩn.

Ba câu kiểm thiết kế: (1) sửa nguyên nhân CREATE vô điều kiện/phân trang, không sửa số liệu cho xanh; (2) readonly PG, HTTP/schema/EOF gates và source SHA ngăn nhầm; (3) audit giữ schedule/dispatch có sẵn, phần chưa promote ghi rõ còn mở. Hai mũ code/review: unit, gitleaks, canary/source CI; không đánh đồng merge với nghiệm thu deploy.
