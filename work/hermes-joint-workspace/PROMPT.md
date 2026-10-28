# HJW — Triển khai tối thiểu có nghiệm thu: khai danh tại cửa ghi

RUN_ID: HJW-DECLARATION-GATE-ONE-PASS-20261028-11
STATUS: HOST_FINAL_AFTER_CLAUDE_P446 · CHƯA RUN · chỉ hiệu lực khi Host ký READY SHA và Owner giao
Executor_Surface: Codex Desktop/Work (Owner giao tay sau GPT Host READY đúng SHA)
Task: Huyen1974/incomex-workspace · work/hermes-joint-workspace
Write_Path: repo báo cáo qua `workspace_*` D12; mã Gateway chỉ qua đường repo + operator/apply đã được kiểm toán và VPS-GHI khi Host/Owner giao RUN.
Read_First: `AGENTS.md` A0/A2/A5/A6/A9/A10 → HJW COLLAB §0/§1–3 + P442–P447 → PROMPT này; hash runtime P444 và Claude P446 ACCEPT. Không dùng thông tin lịch sử thay kiểm live.
Phạm vi: HJW declaration gate CHỈ trong các Gateway đã có; không mở task/server/DB; không đổi quyền/quorum, Gmail, PG/Directus trực tiếp, GSM/root hay GitHub ruleset.

## Mục tiêu nghiệm thu duy nhất
**AI qua cửa đã được cấp quyền nhìn ngay cách khai danh khi muốn ghi; AI quên khai nhận `DECLARATION_REQUIRED` rõ cách tự sửa, không tạo side effect; gửi lại có `declared_actor` thì ghi thành công trong một lượt, receipt lưu cả tên khai và actor credential.**
Một hợp đồng chung áp cho `workspace_*`, `fs_*`, upload/import/async/helper/`write_file`. Không xin token/vé riêng; `operation_id` chỉ chống ghi trùng. Tên khai không cấp phiếu A2.

### C1/C2 — điều kiện chốt theo Claude P446
- **C1 — CLIENT_REAL_PASS (BẮT BUỘC):** ít nhất một **AI/client thật** sử dụng MCP đã cập nhật, cố tình gọi ghi thiếu `declared_actor`, thấy `DECLARATION_REQUIRED` và hướng dẫn tự sửa, tự gọi lại cùng công cụ với tên khai hợp lệ, nhận commit/receipt thật; không cần Owner điền hộ, không lấy unit-test server thay cho AI. Ghi rõ client/route, thời điểm, mã giao dịch, SHA và bằng chứng không ghi khi thiếu.
- **C2 — CLIENT_SCHEMA_STALE:** kiểm/ghi client nào giữ tools/list schema cũ, không truyền được `declared_actor`, cách refresh được hãng hỗ trợ, đã thử lại hay chưa. C2 được phép tồn tại như **giới hạn công khai**, không coi bề mặt stale đã PASS; nếu client đang dùng không thể ghi do enforcement, phải khắc phục hoặc DỪNG rollout phần liên quan, không khóa nhầm việc khác.
- **Phạm vi PASS node:** cả AD/workspace và Claude/fs cùng các nhánh upload/queue/helper có coverage + test fixture PASS; tối thiểu C1 một client thật; C2 được phân loại công khai. Không suy một client PASS = mọi sản phẩm PASS.

## S0 · Nguồn mã thật và điểm dừng trước ghi
- Đọc mới HEAD/STOP/READY, VPS-GHI/Guard và hiện trạng công việc khác. Không giữ lệnh chờ.
- Đối chiếu **đúng runtime** hai image và helper P444 với source/manifest. **Pin digest image đang chạy, hash file runtime, trạng thái helper và ảnh rollback trước mọi sửa**; pin lại ngay trước mutation để phát hiện concurrent change. Patch bắt đầu từ byte runtime, không checkout mới nhất đè production. Giữ bằng chứng/manifest và mã patch tại nguồn đã được duyệt, không đưa bí mật lên repo public. Không đòi tái dựng toàn bộ upstream nếu pin runtime, bản sửa và bản lùi đủ kiểm chứng. Không chứng minh baseline+rollback ⇒ `KQ DỪNG` trước mutation, nêu đúng một blocker.
- Kiểm những client **thật đang dùng** và cách native refresh/discover `tools/list` hợp lệ. Trước cưỡng chế phải có đường để một client thật gửi được field mới và không làm các client ghi đang hoạt động bị khóa. Không suy Codex/GPT/Claude/Live đều tự nhận schema mới; nếu stale thì phân loại C2, nêu một cách xử lý không cần Owner tự chỉnh mã.

## S1 · Patch tối thiểu, không nhân chính sách
- Ưu tiên đúng 2 adapter entrypoint của AD (`workspace_*`) và Claude (`fs_*`), dùng cùng contract validator/mô tả/lỗi. Tool thuộc nhóm source-write/stage/queue phải được phân loại đầy đủ; unknown tool không tự bypass. Chỉ sửa file cần thiết trong danh sách P444, không lấy «11 file» làm chỉ tiêu.
- Tên công khai: `declared_actor` (một chuỗi hợp lệ), yêu cầu tại lời gọi ghi; gate sau auth/scope, trước staging/queue/idempotency/commit. Invalid/missing trả:
  `error=DECLARATION_REQUIRED; field=declared_actor; example=gpt-live; instruction="Gọi lại chính tool này với tên AI của bạn; giữ nội dung và operation_id nếu phù hợp"; mutation=none`.
- tools/list/description báo trước cách khai, client/schema mới/cũ có đường tiếp cận thực; nếu client không chuyển được argument vì stale schema, bảo toàn khả năng khôi phục bằng hỗ trợ native/discovery, không giả kết quả.
- Kết quả thành công: `declared_actor` và `authenticated_actor` (credential server), tool/task/path, hash/transaction ID, Git SHA, `replayed`; giữ Git author hiện hữu, giữ D12 và A2. Upload/import giữ actor từ begin; task/helper mang context server qua queue, không buộc AI khai lại ở mỗi bước nội bộ.
- Giữ retry/legacy journal: missing actor không "đốt" operation_id; same id + same signed/declared payload không ghi đôi; actor khác không mượn receipt; job cũ không được nâng phiếu/sửa dấu vết. Không cần service lưu vé.

## S2 · Test và triển khai có kiểm soát, chỉ sau READY/Owner RUN
- Test fixture cho từng lớp: tool description; thiếu/null/rỗng/sai kiểu nhận hướng dẫn; deny trước mọi side effect; tên đúng ghi 1 lần; retry/replay đúng; upload/import/async/helper/`write_file` phủ đủ; stale client; read-only không đổi, profile/key/quorum giữ. Có test cho tool mới không phân loại; test âm và đường lùi.
- Đề xuất triển khai tương thích: advertize schema + canary client trước, sau đó enforce khi đường refresh hoạt động; không giữ hai cơ chế lâu dài, không thêm lịch/monitor/service mới. Chốt Guard PRE, image/source pin, rollback; deploy qua apply hiện hữu, kiểm POST, dừng/rollback khi regression; không thử bằng production data.
- Nghiệm thu **thực C1:** ít nhất **một client AI đang sử dụng thật** (ưu tiên Codex Desktop có kết nối `workspace_*` đã ghi P444) chạy vòng `missing → instruction → retry với declared_actor → commit/receipt`, không Owner điền hộ. Nếu sẵn có Claude/FS và GPT/Cloud thực, thử thêm từng bên để nâng độ tin cậy; không tự dựng CUA/relay hay giữ RUN chờ người chỉ để chứng minh một bề mặt chưa khả dụng. Bộ test fixture/cổng phải đạt đủ **hai Gateway**, upload/import/queue/helper/`write_file`. **C2:** mỗi client stale phải ghi riêng nguyên nhân, refresh đã thử và mức chưa đạt; không đếm stale là PASS. GPT Live không có tool thực tế thì `LIVE_NOT_TESTED`, không đánh đồng với Gateway FAIL hoặc LIVE PASS.
- Giữ các nhóm connector ngoài scope và Hermes-Mac P438 không đổi.

## S3 · Kết quả & dừng sạch
- Ghi P/KQ vào duy nhất HJW COLLAB qua đường D12 (hợp đồng giao dịch hiện hành); cung cấp image/source commit, SHA, diff, test/ca âm, tool discovery, actor proof, rollback/Guard, trạng thái từng adapter và các client.
- KQ=XONG chỉ khi hai Gateway và mọi internal writer trong scope có gate+test PASS, runtime/rollback hash đúng, **C1 ít nhất một AI/client thật tự sửa lỗi và commit thành công**, không phá khả năng ghi của client đang dùng; C2 phải báo riêng stale client và mức đã/không thử, không nhận là PASS toàn bộ bề mặt. Không có C1 hoặc có client active bắt buộc bị khóa ⇒ DỪNG có giới hạn, không báo FULL_PASS. 0 job/lease tạm khi kết thúc.
- Không tự chạy phần việc khác, không tự đổi roadmap/roster/Host; Host B3 sẽ nghiệm thu và ra bước tiếp theo.

STEP_WALK_V1: S0 Codex preflight + pin exact runtime/rollback và đường refresh schema → S1 vá tối thiểu hai adapter + fixture tests → S2 Guard/apply + nghiệm thu **C1 client thật và C2 stale report** không khóa client active → S3 P/KQ+SHA/receipt, trả Owner; Guard/rollback/client gate bắt buộc FAIL thì DỪNG sạch. **Chỉ thi hành khi Host READY đúng last-touch PROMPT SHA và Owner RUN trực tiếp.**
