# HJW — RUN13 DRAFT: triển khai candidate xưng danh an toàn, C1/C2 thật

RUN_ID: HJW-DECLARATION-GATE-COMPAT-20261029-13
STATUS: DRAFT_FOR_CLAUDE_B2 · NOT_READY · NO_RUN
Executor_Surface: Codex Desktop/Work (Owner chuyển tay chỉ SAU Host READY đúng last-touch SHA)
Task: Huyen1974/incomex-workspace · work/hermes-joint-workspace
Write_Path: Git/KQ theo `workspace_*` D12; source code theo đường repo/operator đã duyệt; production duy nhất qua VPS-GHI CAS + apply/Config Guard/rollback.
Read_First: AGENTS.md A2/A5/A6/D12 → HJW COLLAB §0, Bảng, P442–P454 → PROMPT này → `work/hermes-joint-workspace/evidence/run12-declaration-20261029/{README.md,candidate.patch.md,manifest.json,tests.md}`.
Supersedes: RUN12 P452 KQ DỪNG CÓ KẾT QUẢ; **KHÔNG chạy lại RUN12, không sửa lại candidate vô cớ**.

## Kết quả bắt buộc và phạm vi
1. `declared_actor` tự khai ngay lời gọi ghi. AI quên khai gặp lỗi `DECLARATION_REQUIRED` chỉ cách tự sửa, 0 mutation, retry 1 write/receipt chứa declared + authenticated actor. Không có token/vé bên ngoài, không thay quorum A2.
2. Một contract tại hai Gateway AD/workspace + Claude/fs, bao gồm import/upload/task/helper/write_file; không đụng GitHub ruleset, GSM/root, PG/Directus/Lark hay kết nối hãng ngoài phạm vi.
3. **C1:** ít nhất một client AI thật (không phải unit test) gọi thiếu → nhận hướng dẫn → tự gọi lại → SHA/receipt. **C2:** đánh giá phiên đang ghi/schema cache, phân loại `CLIENT_SCHEMA_STALE`, không khóa hoạt động của chúng. **Chưa C1 thì chưa feature XONG**.

## S0 · Tiếp nhận candidate đã có, không yêu cầu Owner UI trước
- Recheck HEAD/READY/STOP, shared mutation/VPS-GHI và Guard theo mức bước. Đọc P452 evidence patch SHA256 `53f9c88836763a0ae613d0ecc0a4f7b17d8723b57f7ab8f2f540a0444374162c`, manifest/pins hai image live và helper. Patch lấy byte runtime, không lấy GitHub checkout khác hash để ghi đè.
- Kiểm source canonical, baseline, ảnh rollback và khả năng build từ patch; nếu vướng SSOT canonical, ghi chính xác nguồn commit/branch/diff theo đường đã duyệt, không `git push` trực tiếp vào protected main. Không lấy commit Mac-local `0ca9577f` làm source remote đã phát hành.
- **Không dừng chỉ vì chưa Refresh tools:** nút custom MCP đã được xác nhận trong Chrome. Chỉ dùng sau server quảng bá metadata mới. Không bấm cho bản schema đang cũ, không qua GUI Codex bị hãng chặn.

## S1 · Build/test Linux biệt lập từ patch, không làm lại nghiên cứu
- Dựng candidate image/runner trong môi trường biệt lập đã có từ đúng baseline/runtime và patch đã lưu, test Linux HTTP MCP tools/list, schema/dispatcher/receipt và các đường writer liên quan; tận dụng 98 fixture, chỉ bổ sung những ca khác biệt môi trường thật. Không chỉnh quyền/container production ở bước này; không xây gateway/proxy/service thường trú.
- Đối chiếu file/image hash, phân loại warning hay lỗi thật, chứng minh rollback image/helper/Config Guard và liệt kê footprint trước apply. Nếu build/rollback thiếu bằng chứng thì KQ DỪNG có source candidate, không mutation production.

## S2 · Quảng bá schema tương thích rồi nhận metadata trên client
- Nếu S1 PASS, không có production conflicts và đã có lease/Guard PRE/rollback, apply bản **advertise-only** theo Config Guard hiện hữu. `declared_actor` xuất hiện trong tools/list nhưng **chưa bắt buộc**; thử lại một lệnh ghi cũ vô hại qua cả AD và FS để chứng minh các client schema cũ không mất đường ghi.
- Sau server quảng bá schema mới, dùng **Refresh tools** của hosted Incomex MCP custom (Chrome đã đăng nhập) và native Codex local Restart/new session; kiểm Claude/fs theo connector hỗ trợ, không tự đoán tất cả cùng cách. C2 gồm client/route, thấy schema, ghi được field, trạng thái stale, kế hoạch/điều kiện chuyển; không đòi Owner tự đăng nhập khi agent làm được. Nếu một bước thật human-only thì nêu đúng thao tác đó SAU khi candidate đã quảng bá, không giữ job chờ.
- **Không bật enforce** khi một client ghi active bắt buộc chưa có cách gửi field mới. Nếu chưa hoàn tất C2, giữ/rollback advertise-safe theo kế hoạch, báo KQ DỪNG có kết quả — không biến thành RUN vô hạn.

## S3 · Kiểm C1 rồi bật cưỡng chế, không làm rơi phiên khác
- Ưu tiên **client AI thật thử gate trong lab MCP biệt lập** nếu client kết nối được theo native mà không cần endpoint thường trú mới; nếu thành công ghi client/tool/request/response và receipt, không gọi 98 fixture là C1. Nếu lab không thể nhận client thật, chỉ triển khai enforce chung khi đã chứng minh các writer active bắt buộc có schema mới, có cửa sổ kiểm soát ngắn, image/rollback sẵn và thực hiện C1 ngay. Không tự mở selector canary actor/task, parser `message` hay máy chủ mới; nếu cách này không an toàn, STOP với advertise-only/candidate.
- C1 phải là *thiếu declared_actor → DECLARATION_REQUIRED kèm ví dụ + hướng dẫn → AI tự gọi lại → 1 ghi thành công có SHA*; đối chiếu 0 side effect cho call thiếu, retry/idempotency, actor khai vs actor credential. Guard POST và client write regression PASS sau enforce. Nếu fail, rollback đúng footprint, giữ bằng chứng và KQ DỪNG sạch.

## KQ
- Đưa một `P455 · Codex Worker · KQ RUN13` trong HJW COLLAB; update Bảng/NEXT_TRIGGER, commit/diff Linux build và results/receipt tại các nguồn sẵn có. **KQ XONG** chỉ khi hai Gateway enforce thật an toàn, C1 real-client PASS, C2 active không làm hỏng việc đang ghi, Guard POST + rollback evidence đúng. Trường hợp chỉ có candidate+advertise-safe vẫn báo **DỪNG CÓ KẾT QUẢ**, không giả feature PASS.
- Không hỏi Owner kiểm login/Refresh trước khi có bước human-only thật; không tự lập tác vụ mới, kéo dài bảo trì/đèn đỏ ngoài scope hoặc cấp quyền/chìa mới.
STEP_WALK_V1: S0 read-gate/pin + canonical source → S1 Linux candidate/fixture → S2 apply advertise-safe + Refresh client + C2 → S3 C1 real client/enforce guarded → P455/KQ. STOP đúng điểm có rủi ro thực, không tự hứa background.
