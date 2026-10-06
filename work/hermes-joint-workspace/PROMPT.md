# PROMPT — HJW · N2 OPENAI DOTS INTEGRATION

RUN_ID: HJW-N2-OPENAI-DOTS-20261006-01
STATUS: DRAFT · Host P168 soạn · chờ Claude Reviewer đúng 1 vòng; chưa READY, chưa RUN
Host: GPT Chat · GPT-HJW-260922-A
Reviewer: Claude Chat
Primary_Executor: Claude Code CLI cho server/config/protection; OpenAI Work/Dot là target surface phải tự tạo live evidence bằng identity của chính nó
Write_Path: repo qua workspace_*; runtime/config chỉ qua DOT/wrapper/apply path hiện hữu; không ad-hoc
Node: N2 / 6 · Roadmap SSOT HJW 0.9 + 0.17
Owner_steps: mặc định 0; chỉ gọi Owner cho một thao tác human-only thật sự (OAuth/account approval) hoặc đúng một quyết định R5. **Không giữ RUN/task/terminal/browser sống để chờ Owner.**

## 0. Mục tiêu duy nhất
Cắm **OpenAI Dot/Work như một agent thay được** vào HJW bằng đường **chính thức, nhỏ nhất, kiểm chứng được**; chưa giao Dot điều hành production.

Đo và nếu khả thi triển khai đủ bốn năng lực:
1. **Repo access** — target OpenAI đọc/ghi đúng workspace/repo được phép.
2. **Identity** — ghi bằng identity server-side riêng, không mượn `gpt-web/openai-mcp` hay courier.
3. **Scope** — read/write do server/gateway cưỡng chế; ngoài phạm vi bị từ chối.
4. **External wake** — event/task hợp lệ đánh thức Work/Dot mà Owner không copy-paste.

N2 kết thúc bằng đúng một phân loại:
- `DIRECT_PASS`: access + identity + scope + live external wake đều PASS bằng đường hãng hỗ trợ.
- `COURIER_REQUIRED`: access + identity + scope PASS nhưng hãng không có wake phù hợp sau khi đã đo đủ; residual sang N3 theo R5.
- `VENDOR_LIMIT`: gói/vùng/tính năng chặn một năng lực bắt buộc khác.

Không code lách UI để giả PASS.

## 1. Luật khóa
- Đọc `AGENTS.md` → root `COLLAB.md` → HJW Bảng → §0.3 → §0.9 → §0.17 → P167 → P168 → file này.
- Áp A6, DROOT30/31/34/37/42/43 và R1/R3/R5 tại §0.17.
- **DROOT43:** cần Owner auth/approval/R5 ⇒ checkpoint + `KQ DỪNG` sạch rồi tắt executor; resume **cùng RUN_ID**, không mở waiter/RUN/node mới.
- Không mở task/project/file tiến độ mới; không dựng gateway/service/DB/UI mới nếu đường hiện hữu đủ.
- Không build/release `agent-data` trong N2 trừ khi evidence chứng minh blocker duy nhất và Host+Reviewer sửa prompt/READY trước.
- `AUTO_ALLOWLIST` giữ rỗng; N2 không bật AUTO.
- Không ghi secret/token/private IP/chat id vào repo.
- Mutation N2 phải vào D30/31 + Config/Protection Guard + rollback/receipt trong chính N2.
- Không sửa CWEB/#22 trong N2. Green gate là điều kiện RUN/mutation, không phải lý do agent ngồi chờ.

## 2. Cổng vào — không chờ
1. Re-read Bảng + prompt; READY phải trỏ đúng last-touch; không HOLD/STOP.
2. Fresh-check shared mutation/concurrency.
3. Fresh protection/registry:
   - Pha A read-only được làm dù #22 CWEB đang đỏ.
   - Trước mutation đầu tiên và live acceptance cuối: protection phải PASS/green bởi surface check được thật.
   - Đỏ ngoài N2 ⇒ `KQ DỪNG · EXTERNAL_GREEN_GATE`; **không sleep/poll**.
4. Dùng tài khoản/surface OpenAI thật + tài liệu OpenAI chính thức hiện hành; không dùng blog/community làm nguồn năng lực.
5. Sign-in/OAuth/consent nếu thật sự cần thì gom thành **một lượt human-only**, không hỏi lắt nhắt.

## 3. PHA A — INVENTORY CHÍNH THỨC + LIVE ACCOUNT · READ-ONLY
Lập một bảng:
`Năng lực | đường chính thức | live account thấy gì | identity | scope | wake/trigger | evidence | kết luận`.

Bắt buộc giải U3/U4 trước mutation:
- GPT hiện thấy `Incomex_MCP_full_all_2` primary 37-tool, identity `gpt-web/openai-mcp`.
- GPT còn thấy `Incomex_AgentData_MCP___GPT_Full_TEST20` 37-tool, cùng roots — **duplicate-registration candidate**, chưa xoá chỉ vì tên “test”.
- Map opaque app/connector IDs bằng manifest/tool/route evidence thành `PRIMARY / DUPLICATE_REGISTRATION / DISTINCT_RUNTIME / UNKNOWN_WITH_REASON`.
- Liệt kê registration/plugin/app mà target thực sự thấy; không suy từ memory.

Đo đường chính thức theo thứ tự:
1. Plugin/App/connected app hiện hữu.
2. GitHub integration và event-triggered Work task **chỉ cho event hãng thật sự hỗ trợ**.
3. Work Cloud Browser/browser chính thức khi cần signed-in action.
4. Sau đó mới kết luận thiếu external wake.

**Không suy diễn:** cloud browser hay event task không tự chứng minh arbitrary external wake vào một chat/agent bất kỳ.

Pha A chưa có bảng ⇒ **cấm cài/config**. Nếu đã đủ bằng chứng `VENDOR_LIMIT`, đi thẳng §8.

## 4. PHA B — DELTA TỐI THIỂU / CHECKPOINT
Nếu access + identity + scope làm được bằng gateway hiện hữu:
- Chốt exact profile/credential/route cần thêm/sửa.
- Identity target riêng (logical profile `openai-dot/work` hoặc tên canonical tìm được); server suy từ credential, `clientInfo` không quyết identity.
- Read/write scope tách riêng và enforce ở choke point chung.
- Thu hồi profile không làm surface GPT/Claude khác hỏng.
- Thêm mapping attribution A9 trước first write nếu thiếu.
- **Không cổng mới, duplicate proxy, build agent-data** nếu config hiện hữu đủ.

Nếu cần server config/secret hoặc Owner OAuth:
- ghi exact change + rollback + negative tests;
- Owner human-only thật sự ⇒ `CHECKPOINT_N2_OWNER_ACTION` + đúng một thao tác + `KQ DỪNG · CONTINUE_SAME_NODE`; tắt executor, không chờ.

## 5. PHA C — ACCESS / IDENTITY / SCOPE LIVE
Chỉ khi gate sạch:
- Reuse gateway/profile/config hiện hữu.
- Target OpenAI tự làm ít nhất một read và, nếu scope cho phép, một write vô hại vào **fixture/đường đã có và được phép**; không tạo fixture/file mới để test.
- Write/commit mang identity target riêng phía server.

Negative bắt buộc:
1. credential/profile lạ ⇒ 401/deny;
2. read/write ngoài scope qua fixture deny/path hiện hữu ⇒ bị chặn; không tạo fixture mới;
3. client metadata không thể mượn identity khác;
4. thu hồi target profile không làm GPT/Claude mất đường.

Không PASS vì Host/Claude làm thay target.

## 6. PHA D — EXTERNAL WAKE
1. Tìm trigger/capability chính thức trên live account.
2. Có trigger phù hợp + fixture/event an toàn **đã tồn tại** ⇒ live-test: event → Work/Dot nhận → target tự đọc ref → ghi acknowledgement/evidence bằng identity riêng.
3. Không tạo PR/repo/task/fixture mới nếu chưa được duyệt.
4. Capability chỉ hỗ trợ event hẹp nhưng không đáp ứng HJW ⇒ ghi giới hạn, không DIRECT_PASS.
5. **Không browser/desktop automation để giả wake trong N2**; phần đó thuộc N3.
6. Cần Owner/action để tạo live proof ⇒ checkpoint + KQ DỪNG, không waiter; không hạ acceptance thành docs-only.

## 7. PHA E — PROTECTION R3
Mutation N2 phải có:
- Điều 30/31;
- Config/Protection Guard + negative/mutant tương ứng;
- rollback dry-run/known-good;
- receipt/trace;
- fresh protection PASS trước KQ.

Không rebaseline để che drift; đỏ ngoài N2 thì dừng sạch, không sửa hộ.

## 8. DISPOSITION / R5
### DIRECT_PASS
Chỉ khi access live + identity riêng live + scope/negative live + external wake live + R3 protection đều PASS.
`KQ@HJW-N2-OPENAI-DOTS-20261006-01 XONG · DIRECT_PASS · ACCESS_PASS · IDENTITY_PASS · SCOPE_PASS · WAKE_PASS · PROTECTION_CLEAN`

### COURIER_REQUIRED
Access + identity + scope PASS, nhưng chính thức không có wake phù hợp.
`KQ@HJW-N2-OPENAI-DOTS-20261006-01 DỪNG · COURIER_REQUIRED · R5_OWNER_DECISION_REQUIRED · CONTINUE_SAME_NODE`
Dừng sạch ngay. Host hỏi Owner đúng một câu: chấp nhận residual wake chuyển N3 hay giữ N2.

### VENDOR_LIMIT
Capability/gói/vùng chặn một năng lực bắt buộc:
`KQ@HJW-N2-OPENAI-DOTS-20261006-01 DỪNG · VENDOR_LIMIT:<năng_lực> · R5_OWNER_DECISION_REQUIRED · CONTINUE_SAME_NODE`
Kèm official + live evidence và một phương án đề nghị; không code lách.

## 9. Đầu ra bắt buộc
Trong HJW COLLAB:
1. bảng Pha A;
2. exact delta + rollback nếu có;
3. kết quả access / identity / scope / wake;
4. negative tests;
5. protection/receipt;
6. đúng một disposition `DIRECT_PASS | COURIER_REQUIRED | VENDOR_LIMIT`;
7. Bảng cập nhật; nếu DỪNG ghi rõ **0 agent/task/terminal đang chờ**.

Không mở N3 trước Host + Reviewer disposition R5.
