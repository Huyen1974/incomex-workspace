# PROMPT — HJW · N2 OPENAI DOTS INTEGRATION

RUN_ID: HJW-N2-OPENAI-DOTS-20261006-01
STATUS: DRAFT · Host P168 soạn · Claude P170 đã rà một vòng và sửa thẳng bảy chỗ C1–C7 (bảng ở P170 mục 2) · chờ Host rà delta rồi READY; chưa RUN
Host: GPT Chat · GPT-HJW-260922-A
Reviewer: Claude Chat
Primary_Executor: Claude Code CLI cho server/config/protection và cho thao tác giao diện OpenAI qua Chrome đã đăng nhập của Owner (§2 mục 6); dot của Owner là target surface phải tự tạo live evidence bằng identity của chính nó
Write_Path: repo qua workspace_*; runtime/config chỉ qua DOT/wrapper/apply path hiện hữu; không ad-hoc
Node: N2 / 6 · Roadmap SSOT HJW 0.9 + 0.17
Owner_steps: Pha A = 0. Có mutation ⇒ dự kiến đúng một lần bấm “Cho phép áp” khi Claude Code hỏi (auto-mode chặn ghi máy chủ). Ngoài ra chỉ gọi Owner cho một thao tác human-only thật sự (OAuth/account approval) hoặc đúng một quyết định R5. **Không giữ RUN/task/terminal/browser sống để chờ Owner.**

## 0. Mục tiêu duy nhất
Cắm **dot của Owner (OpenAI “dots”) như một agent thay được** vào HJW bằng đường **chính thức tốt nhất, ít thay đổi nhất, kiểm chứng được** (Owner 05/10: “kết nối tối ưu GPT DOT”); chưa giao Dot điều hành production.

**Đích là dot.** ChatGPT Work (tác vụ theo lịch/sự kiện) là đường chính thức của cùng tài khoản: được dùng làm “chuông cửa” nếu dot không có trigger riêng, và ghi thành dòng riêng trong bảng Pha A. Không trộn hai sản phẩm thành một.

Đo và nếu khả thi triển khai đủ bốn năng lực:
1. **Repo access** — target OpenAI đọc/ghi đúng workspace/repo được phép.
2. **Identity** — ghi bằng identity server-side riêng, không mượn `gpt-web/openai-mcp` hay courier; **cách ly hai chiều**: dot không dùng được danh tính `gpt-web` (danh tính máy đang dùng để kiểm quyền Host, DROOT41) và phiên GPT Chat không dùng được danh tính của dot.
3. **Scope** — read/write do server/gateway cưỡng chế; ngoài phạm vi bị từ chối.
4. **External wake** — event/task hợp lệ đánh thức dot mà Owner không copy-paste. **Thanh đo (Host + Reviewer làm rõ, không nới):** tín hiệu do máy phát, không người bấm ⇒ dot tự chạy đúng một lượt và ghi nhận trong **≤ 10 phút**; lúc không có việc thì không tốn lượt mô hình (D05).

N2 kết thúc bằng đúng một phân loại:
- `DIRECT_PASS`: access + identity + scope + live external wake đều PASS bằng đường hãng hỗ trợ.
- `COURIER_REQUIRED`: access + identity + scope PASS nhưng hãng không có wake phù hợp sau khi đã đo đủ; residual sang N3 theo R5. Chỉ có lịch cố định mà lần nào cũng chạy mô hình, hoặc trễ hơn thanh đo ⇒ ghi kèm `SCHEDULE_ONLY:<chu kỳ>`, **không** tính WAKE_PASS; Owner quyết ở R5.
- `VENDOR_LIMIT`: gói/vùng/tính năng chặn một năng lực bắt buộc khác. Gồm cả trường hợp hãng không cho cách ly danh tính: `VENDOR_LIMIT:identity_isolation`.

Không code lách UI để giả PASS.

## 1. Luật khóa
- Đọc `AGENTS.md` → root `COLLAB.md` → HJW Bảng → §0.3 → §0.9 → §0.17 → P167 → P168 → file này.
- Áp A6, DROOT30/31/34/37/42/43 và R1/R3/R5 tại §0.17.
- **DROOT43:** cần Owner auth/approval/R5 ⇒ checkpoint + `KQ DỪNG` sạch rồi tắt executor; resume **cùng RUN_ID**, không mở waiter/RUN/node mới.
- Không mở task/project/file tiến độ mới; không dựng gateway/service/DB/UI mới nếu đường hiện hữu đủ.
- **Cổng và quyền khởi đầu của dot do Host + Reviewer chốt, executor không tự chọn:** dot vào bằng **cổng agent chung D13** (`/api/mcp-agent`, cùng loại với Hermes), hồ sơ riêng `openai-dot` **sao khuôn hồ sơ `hermes`** (cùng bộ tool, cùng kiểu phạm vi đọc/ghi), nhãn máy `agent-gw/openai-dot`. **Không** cấp route 37 tool của `gpt-web`/`claude-chat-web`. Lý do: T4 đòi đổi agent bằng một dòng chính sách nên các agent phải cùng khuôn; mở rộng quyền là việc của chính sách ở N5, do Owner. Dòng nhãn A9 cho `agent-gw/openai-dot` đã có trong AGENTS (P170); executor không sửa AGENTS.
- Không build/release `agent-data` trong N2 trừ khi evidence chứng minh blocker duy nhất và Host+Reviewer sửa prompt/READY trước.
- `AUTO_ALLOWLIST` giữ rỗng; N2 không bật AUTO.
- Không ghi secret/token/private IP/chat id vào repo.
- Mutation N2 phải vào D30/31 + Config/Protection Guard + rollback/receipt trong chính N2.
- Không sửa CWEB/#22 trong N2. Green gate là điều kiện RUN/mutation, không phải lý do agent ngồi chờ.

## 2. Cổng vào — không chờ
1. Re-read Bảng + prompt; READY phải trỏ đúng last-touch; không HOLD/STOP.
2. Fresh-check shared mutation/concurrency. RUN khác đang `STARTED` chưa KQ trên máy chủ dùng chung ⇒ Pha A vẫn làm; tới mutation mà còn vậy ⇒ `KQ DỪNG · CONCURRENCY_GATE`, không chờ.
3. Fresh protection/registry:
   - Pha A read-only được làm kể cả khi có đèn ngoài N2 đang đỏ.
   - Trước mutation đầu tiên và live acceptance cuối: protection phải PASS/green bởi surface check được thật.
   - Đỏ ngoài N2 ⇒ gọi **đúng một lần** cơ chế one-shot/check hiện hữu của chính đèn đó (tiền lệ P160; không sửa config/code) rồi đọc lại ngay; còn đỏ ⇒ `KQ DỪNG · EXTERNAL_GREEN_GATE` kèm tên đèn. **Không sleep/poll.** (06/10 đèn #23 tự đỏ 4 phút rồi xanh; một lần chớp không được làm hỏng cả lượt.)
4. Dùng tài khoản/surface OpenAI thật + tài liệu OpenAI chính thức hiện hành; không dùng blog/community làm nguồn năng lực.
5. Sign-in/OAuth/consent nếu thật sự cần thì gom thành **một lượt human-only**, không hỏi lắt nhắt.
6. **Thao tác giao diện OpenAI:** executor làm qua Chrome đã đăng nhập của Owner theo cách N1 P152 — địa chỉ/khoá bí mật chỉ đi qua clipboard; kiểm đúng ô và độ dài trước khi bấm; không chụp màn hình khi bí mật đang hiện; trả lại nguyên trạng tab và bản nháp của Owner. Phiên không có công cụ trình duyệt ⇒ gom thành đúng một lượt việc tay ở checkpoint, không tự tìm đường khác. Chỉ dùng để cài đặt, quan sát và gõ câu khởi động cho phép thử Pha C; **không** dùng để giả wake (§6 mục 5).

## 3. PHA A — INVENTORY CHÍNH THỨC + LIVE ACCOUNT · READ-ONLY
Lập một bảng:
`Năng lực | đường chính thức | live account thấy gì | identity | scope | wake/trigger | evidence | kết luận`.

Bắt buộc giải U3/U4 trước mutation:
- GPT hiện thấy `Incomex_MCP_full_all_2` primary 37-tool, identity `gpt-web/openai-mcp`.
- GPT còn thấy `Incomex_AgentData_MCP___GPT_Full_TEST20` 37-tool, cùng roots — **duplicate-registration candidate**, chưa xoá chỉ vì tên “test”.
- Map opaque app/connector IDs bằng manifest/tool/route evidence thành `PRIMARY / DUPLICATE_REGISTRATION / DISTINCT_RUNTIME / UNKNOWN_WITH_REASON`.
- Liệt kê registration/plugin/app mà target thực sự thấy; không suy từ memory.

Đo đường chính thức theo thứ tự (mỗi dòng: tài liệu chính thức + tài khoản thật):
1. Plugin/App/connected app hiện hữu, gồm connector MCP tuỳ biến. Trả lời rõ ba câu **trước mọi mutation**: (a) dot có gọi được connector MCP tuỳ biến không; (b) hãng có cho gắn/giới hạn connector theo từng dot không; (c) **hiện tại** dot có thấy hoặc gọi được connector mang danh tính Host (`Incomex_MCP_full_all_2`, bản TEST20) không — thử bằng một lệnh **đọc**, không ghi. (c) = có ⇒ ghi ngay phát hiện `HOST_IDENTITY_SHARED` lên COLLAB cho Host + Reviewer; không tự xử.
2. Máy cloud riêng của dot: có gọi ra một địa chỉ HTTPS bằng khoá riêng được không. Nếu plugin là cài đặt dùng chung của tài khoản thì đây có thể là đường duy nhất tách được danh tính.
3. **Liệt kê đủ mọi loại trigger chính thức**, không chỉ GitHub: lịch/kiểm định kỳ của dot · tác vụ Work theo lịch · tác vụ Work theo sự kiện, **chỉ cho event hãng thật sự hỗ trợ** · dot trong Slack/Teams nếu tài khoản có. Chấm từng loại theo thanh đo ở §0 mục 4. Máy chủ Incomex phát đúng một sự kiện mà hãng hỗ trợ để gọi dot (“chuông cửa”) là đường chính thức, không phải lách.
4. Work Cloud Browser/browser chính thức khi cần signed-in action.
5. Sau đó mới kết luận thiếu external wake.

Ứng viên Reviewer đọc ở trang trợ giúp OpenAI ngày 06/10 qua công cụ tóm tắt — **phải kiểm lại trên tài khoản thật, không coi là sự thật**: plugin của dot dùng chung cài đặt ChatGPT của tài khoản · dot tự làm việc theo lịch/kiểm định kỳ và rà nền, có máy cloud riêng · Work có tác vụ theo sự kiện cho thư Gmail mới, tin Slack mới, hoạt động PR GitHub (tối đa 30 lần/giờ) và lịch tối đa một lần/giờ ở gói trả phí · trang về dot không nhắc webhook/API.

**Không suy diễn:** cloud browser hay event task không tự chứng minh arbitrary external wake vào một chat/agent bất kỳ.

Pha A chưa có bảng ⇒ **cấm cài/config**. Nếu đã đủ bằng chứng `VENDOR_LIMIT`, đi thẳng §8.

## 4. PHA B — DELTA TỐI THIỂU / CHECKPOINT
Nếu access + identity + scope làm được bằng gateway hiện hữu:
- **Executor chỉ được tự áp các thay đổi trong danh sách này** (cùng khuôn N1 R4-8a, hội đồng đã soát): (1) một khoá mới trong GSM cho hồ sơ dot; (2) một hồ sơ `openai-dot` trên cổng agent bằng config hiện hữu; (3) một route bí mật tới cổng agent sinh bằng `dot-connector-sync` (nâng DOT thêm đúng loại route này nếu chưa có); (4) dòng sổ `connectors.json` + INV20 + Config Guard + sổ tin báo cho đúng những thứ vừa thêm; (5) nạp lại agent-data **tối đa một lần**, không build. Mọi thứ đi qua `incomex-config-apply-v0`.
- **Cần gì ngoài danh sách** (đặt khoá lên máy cloud của dot, thêm đường phát thư/Slack/PR để rung chuông, nối app mới của Owner, đổi quyền hồ sơ khác…) ⇒ ghi exact change + rollback + negative tests rồi `KQ DỪNG · DELTA_REVIEW_REQUIRED · CONTINUE_SAME_NODE`; Host + Reviewer soát một lượt, resume cùng RUN.
- Pha A trả lời (b) = không (plugin không gắn riêng được cho dot) ⇒ đường plugin không tách được danh tính: **không áp danh sách trên cho đường plugin**; xét đường máy cloud riêng của dot (ngoài danh sách ⇒ `DELTA_REVIEW_REQUIRED`) hoặc kết luận `VENDOR_LIMIT:identity_isolation`.
- Identity target riêng: hồ sơ `openai-dot`, nhãn `agent-gw/openai-dot` (§1); server suy từ credential, `clientInfo` không quyết identity.
- Read/write scope tách riêng và enforce ở choke point chung.
- Thu hồi profile không làm surface GPT/Claude khác hỏng.
- Mapping attribution A9 cho `agent-gw/openai-dot` đã có (P170); executor kiểm có dòng đó trước first write.
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
4. thu hồi target profile không làm GPT/Claude mất đường;
5. cách ly hai chiều, thử bằng lệnh **đọc**: dot gọi qua connector/route mang danh tính `gpt-web` ⇒ không gọi được; phiên GPT Chat gọi route của dot ⇒ không gọi được. Một trong hai chiều gọi được ⇒ **không ghi IDENTITY_PASS**; phân loại `VENDOR_LIMIT:identity_isolation` (§8).

Phép thử ghi ngoài phạm vi chỉ dùng fixture deny sẵn có của cổng agent, loại mà lỡ thành công cũng không đổi nội dung thật; lỡ thành công ⇒ dừng ngay, coi là sự cố.

Không PASS vì Host/Claude làm thay target.

## 6. PHA D — EXTERNAL WAKE
1. Tìm trigger/capability chính thức trên live account.
2. Có trigger phù hợp + fixture/event an toàn **đã tồn tại** ⇒ live-test: event → Work/Dot nhận → target tự đọc ref → ghi acknowledgement/evidence bằng identity riêng. Mỗi lần kích quan sát **tối đa 10 phút**, **tối đa hai lần kích**; không đạt ⇒ ghi kết quả và kết luận, không ngồi chờ thêm.
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
Kèm official + live evidence và một phương án đề nghị; không code lách. Trước KQ `VENDOR_LIMIT`: mọi khoá/route/hồ sơ N2 đã tạo phải ở trạng thái **tắt** (bật lại được bằng một lệnh nếu Owner chấp nhận ở R5); không để đường sống mà không ai dùng; Guard sạch.

### Sau khi Owner trả lời R5
Chấp nhận ⇒ Host ghi dòng đóng `N2 PASS_WITH_RESIDUAL · DEFERRED_BY_VENDOR:<phần> · MOVE_TO:N3` vào Bảng, không cần RUN thêm. Không chấp nhận ⇒ ở lại N2, Host sửa PROMPT cho lượt kế.

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
