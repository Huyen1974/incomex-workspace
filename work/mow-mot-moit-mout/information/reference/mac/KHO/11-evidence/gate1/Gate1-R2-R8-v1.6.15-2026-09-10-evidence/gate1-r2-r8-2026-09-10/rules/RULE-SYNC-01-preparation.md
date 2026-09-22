# RULE-SYNC-01 — exact targets / patch chưa áp dụng

**PREPARED / PM-HELD.** Chỉ chuẩn bị, không thay file luật local hay KB. Đây là bản patch đề nghị của work item SSOT, không luật có hiệu lực. Phải được PM giao xử lý trước build.

Hai nguyên tắc lấy nguyên nghĩa từ SSOT mục `#rule-sync` (tiêu đề RULE-SYNC-01):

1. PG-first ≠ PG-only. Trước custom SQL/function/trigger phải xét PG native → Directus built-in → internal component → ecosystem → composition; có evidence loại I0–I6, bao gồm built-in của TARGET version.
2. Code trong Flow exec, SQL function, Nuxt server hay extension đều là code; không đổi nhãn “config” để vượt reuse gate.

[Minimal proposed patch](RULE-SYNC-01-proposed.patch) chèn đúng hai mệnh đề vào ba điểm áp dụng; không đổi business rule/authority, không sinh subsystem. [Source hashes](patch-targets.json).

| Exact source | Current đã đọc | Vị trí patch | Source of authority / cách áp dụng sau này |
|---|---|---|---|
| `/Users/nmhuyen/Documents/Codex/2026-08-19/ng-d-n-th-c-t/web-test/.claude/skills/incomex-rules.md` | Snapshot local, summary9nguyên tắc; Q0–Q4 line131 | Sau dòng Q0–Q4 của #18 Assembly | Mirror hướng dẫn Agent local; cập nhật theo KB được ban hành, không tuyên bố mirror cao hơn luật |
| `knowledge/dev/laws/law-01-foundation-principles.md` | Native KB body v3.3, revision12; §13 lines102–111 | Cuối §13 trước nguyên tắc14 | Luật nền tảng NT13; publish qua quy trình quản trị KB khi được giao |
| `knowledge/dev/laws/constitution.md` | Native KB v4.6.3, revision44; 15NT | Table row NT13 line25 | Hiến pháp tóm tắt NT13; PM/authority luật phải chấp thuận, không tự enact |

Cả hai KB source được đọc bằng native MCP main agent. Search metadata Foundation còn v3.0/11NT, trong khi body là v3.3/rev12: dùng body/revision làm evidence, ghi metadata drift để sửa đúng nguồn cùng đợt được giao; không lấy search title làm current law.

Các xung đột phải giải cùng Gate2 trước build:

- **Nuxt cấm code/chỉ đọc tuyệt đối:** Foundation§6 lines24–35, incomex-rules #24 và summary line29, `AGENTS.md` lines28/37. SSOT hiện cho generic UI transport sau reuse proof, business truth vẫn PG. Đề nghị PM xác nhận phạm vi: cấm per-workflow business logic/bypass, không cấm generic render/transport đã được giao; không tự sửa luật để hợp thức hóa adapter.
- **Hard-lock Nuxt3/PG16 tại AGENTS:** current evidence khác stable TARGET; sau PLATFORM FREEZE, cập nhật source version policy theo quyết định, giữ CURRENT khác TARGET. Không tự đổi thành latest không pin.
- **Yêu cầu annotate/deploy/KB write của quy trình thường:** user giao PM prompt lần này chỉ read-review + một SSOT cuối; scope cụ thể đó được áp dụng. Không label/update production chỉ để tuân thủ một quy trình rộng hơn.
- **Approval không bị mở rộng:** I7/custom authorization theo quyền hiện hành; patch reuse không tự cho Agent approve/publish/create schema. D04/D05 và cấp quyền build vẫn phải giải riêng.

`AGENTS.md` exact path: `/Users/nmhuyen/Documents/Codex/2026-08-19/ng-d-n-th-c-t/web-test/AGENTS.md`; snapshot [AGENTS-before.md](AGENTS-before.md). File này là conflict/mirror follow-up, không nằm trong patch hai nguyên tắc do chưa có platform decision. Không thay đổi số nguyên tắc hoặc ban hành phiên luật mới trong lượt review.
