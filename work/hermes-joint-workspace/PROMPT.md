# HJW — DRAFT thực thi nhỏ nhất: khai danh ngay tại cửa ghi

RUN_ID: HJW-DECLARATION-GATE-ONE-PASS-20261028-11
STATUS: DRAFT_FOR_CLAUDE_B2 · NOT_READY · NO_RUN
Executor_Surface: Codex Desktop/Work (Owner giao tay sau GPT Host READY đúng SHA)
Task: Huyen1974/incomex-workspace · work/hermes-joint-workspace
Write_Path: repo báo cáo qua `workspace_*` D12; mã Gateway chỉ qua đường repo + operator/apply đã được kiểm toán và VPS-GHI khi Host/Owner giao RUN.
Read_First: `AGENTS.md` A0/A2/A5/A6/A9/A10 → HJW COLLAB §0/§1–3 + P442–P445 → PROMPT này; nguồn code AgentData/Claude Gateway theo hash P444.
Phạm vi: HJW declaration gate CHỈ trong các Gateway đã có; không mở task/server/DB; không đổi quyền/quorum, Gmail, PG/Directus trực tiếp, GSM/root hay GitHub ruleset.

## Mục tiêu nghiệm thu duy nhất
**AI qua cửa đã được cấp quyền nhìn ngay cách khai danh khi muốn ghi; AI quên khai nhận `DECLARATION_REQUIRED` rõ cách tự sửa, không tạo side effect; gửi lại có `declared_actor` thì ghi thành công trong một lượt, receipt lưu cả tên khai và actor credential.**
Một hợp đồng chung áp cho `workspace_*`, `fs_*`, upload/import/async/helper/`write_file`. Không xin token/vé riêng; `operation_id` chỉ chống ghi trùng. Tên khai không cấp phiếu A2.

## S0 · Nguồn mã thật và điểm dừng trước ghi
- Đọc mới HEAD/STOP/READY, VPS-GHI/Guard và hiện trạng công việc khác. Không giữ lệnh chờ.
- Đối chiếu **đúng runtime** hai image và helper P444 với Git source/commit/manifest; chốt một bản build có thể tái tạo và đường lùi byte/hash đúng. Nếu đang chạy ≠ checkout: không sửa mù/khôi phục tùy tiện; dùng lại quy trình image/source đã có để pin baseline tối thiểu tại SSOT. Không chứng minh được baseline/rollback ⇒ `KQ DỪNG` trước source/runtime mutation, nêu đúng một blocker.
- Kiểm client current tools/list: liệu `declared_actor` mới có hiện trong schema của GPT/Claude/Live hiện tại, đường refresh hợp lệ nếu stale. **Không cưỡng chế khi client chưa thể gửi trường**; nhưng không coi release không enforce là hoàn tất.

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
- Nghiệm thu **thực**: một GPT/OpenAI Cloud và một Claude/FS hiện hữu thực hiện vòng `missing → instruction → retry → receipt`; owner không gõ tên thay AI. Nếu Live chưa có tool hợp lệ, ghi `LIVE_NOT_TESTED` không chặn nghiệm thu Gateway, nhưng không nói Live PASS.
- Giữ các nhóm connector ngoài scope và Hermes-Mac P438 không đổi.

## S3 · Kết quả & dừng sạch
- Ghi P/KQ vào duy nhất HJW COLLAB qua đường D12 (hợp đồng giao dịch hiện hành); cung cấp image/source commit, SHA, diff, test/ca âm, tool discovery, actor proof, rollback/Guard, trạng thái từng adapter và các client.
- KQ=XONG chỉ khi cả hai gateway writer và đường internal đã có gate, các client tiêu biểu tự khắc phục lỗi; thiếu một điều kiện → DỪNG có giới hạn, không báo FULL_PASS. 0 job/lease tạm khi kết thúc.
- Không tự chạy phần việc khác, không tự đổi roadmap/roster/Host; Host B3 sẽ nghiệm thu và ra bước tiếp theo.

STEP_WALK_V1: S0 Codex preflight + pin baseline → S1 Codex patch/test trên nguồn được pin → S2 deploy có Guard + client acceptance → S3 ghi P/KQ/commit và trả Owner; bất kỳ guard fail: rollback/stop và báo DỪNG. **DRAFT — không có authority thi hành trước READY + Owner RUN.**
