# PROMPT — HVU.B3-CLEANUP · Claude hoàn tất cleanup + audit đường tín hiệu

RUN_ID: HVU-B3-CLEANUP-20260921-03
Host: GPT Chat · `GPT-HVU-20260921-A`
Executor_Surface: Claude Code CLI/Cowork
Reviewer_Surface: Claude Chat

## 0. Trạng thái nền — KHÔNG mở lại core B3
B2/B2.1/B3 core đã chạy production và live Claude Chat PASS 5/5 (P19). Core được coi là FROZEN:
- `Vừa làm` = Git author gateway của commit cuối chạm riêng task, không TTL.
- `Đang làm` = **latest-only presence per task**, TTL 600s; activity mới hơn thay ngay activity cũ của cùng task. Mỗi task tối đa một `Đang làm`. Commit clear chỉ khi surface commit vẫn là latest; call sau sáng lại.
- tools/list/schema/serverInfo/version/auth/URL giữ nguyên.
- rollout theo STARTING/TỐT/HỎNG của DROOT10.

Lượt này chỉ cleanup/audit các lỗ còn lại. Không redesign, không đổi semantics core, không quay lại writers/provenance ledger.

## 1. Vá legacy actor — bắt buộc
Trong B2 `sync.py`, coi **chính xác** hai author name legacy sau là pre-B3/unknown dù email là gateway:
- `AI via Incomex Workspace`
- `Claude via MCP`

Kết quả:
- không tạo hàng actor cho hai tên trên;
- task có commit cuối legacy đó hiển thị xám/unknown cho tới commit gateway B3 thật tiếp theo;
- không suy actor từ subject/prefix để “bù”.

Không mở rộng blacklist bằng heuristic.

## 2. Tên hiển thị cho User — chỉ dùng bảng A9
Không tự viết regex/map thứ hai trong UI. `sync.py`/adapter đọc **Bảng phiên dịch người làm** tại AGENTS A9 và xuất mapping/display data cho UI.
- `Anthropic/ClaudeAI*` → `Claude Chat/Cowork` (chỉ tách khi metadata thật sự phân biệt được).
- `claude-code*` → `Claude Code CLI`.
- `codex*` → `Codex`.
- `openai-mcp*` → `GPT Chat/Work` (chỉ tách khi metadata thật sự phân biệt được).
- `Claude via MCP` / `AI via Incomex Workspace` → legacy trước B3: unknown/xám, không tạo hàng.
- nhãn lạ → `Chưa rõ`; tooltip/title phải cho xem raw label.

UI Tình trạng của **task đang chọn** chỉ render union của actor `Vừa làm` và actor `Đang làm`; tối đa 2 hàng, hoặc 1 hàng nếu cùng actor. Không render danh sách global mọi surface đã từng thấy. Dưới bảng chỉ dùng hai chú thích ngắn: `Vừa làm: lần ghi gần nhất` và `Đang làm: hoạt động mới nhất ≤10 phút`; raw label/chi tiết kỹ thuật chỉ ở tooltip.

## 3. Đổi `Đang làm` thành latest-only + audit stdio proxy
### 3A. Latest-only presence — bắt buộc theo chỉ đạo Owner
- Store/runtime hiệu lực phải là **latest-only thật** theo `work_id`: một record current `{surface_key,label,last_seen,generation}` hoặc state machine/tombstone tương đương. Record bị thay phải mất quyền trở lại, không được chỉ ẩn tạm.
- Tool activity scoped task với timestamp mới hơn → thay ngay record cũ của task, bất kể surface cũ còn trong TTL; tăng generation/event sequence.
- TTL 600s áp cho record current; quá TTL → task không có actor đang làm. Không chọn record cũ làm fallback.
- Commit của surface S trên task A: chỉ clear current nếu record current vẫn là S và không có event/generation mới hơn commit. Clear phải tạo trạng thái rỗng/tombstone cho generation đó; không `delete current rồi max(record cũ)`.
- Job bookkeeping nếu cần nhiều record phải tách khỏi **current task presence**; heartbeat cũ chỉ trở thành current khi nó phát sinh một activity/heartbeat **mới sau** event thay/clear.
- Regression bắt buộc: A→X → A active; B→X mới hơn → chỉ B active; B commit X → X **trống**, A không sống lại dù A timestamp cũ còn trong TTL; A read X sau đó → A active mới. A→Y không ảnh hưởng X; TTL chỉ xám current.

### 3B. Audit + hoàn tất stdio proxy cho Claude Code/Cowork/Hermes
P18/Codex cho biết canonical `mcp_server/stdio_server.py` đã được sửa để forward client identity, nhưng **các bản cài/process cũ có thể chưa nạp bản mới**.

Claude phải khảo sát thực địa, không đoán:
1. Xác định cho từng surface đang/có thể dùng: Claude Code CLI, Cowork, Codex, Hermes:
   - config/entrypoint thật;
   - path proxy thật đang được gọi;
   - hash/version của file;
   - backend route dùng (JSON-RPC hay REST);
   - có forward `clientInfo.name/version` / internal identity header hay không.
2. So với canonical B3 hiện hành. Nếu bản cài stale:
   - cập nhật **đúng bản cài/config**, không chỉ source repo;
   - restart/reload **chỉ process/proxy cần thiết** nếu có thể làm an toàn;
   - không restart ChatGPT/Claude Chat hay bắt Owner reconnect nếu không cần.
3. Nếu process của chính Claude Code không thể tự hot-reload mà vẫn tiếp tục phiên:
   - cập nhật source/config để **process kế tiếp chắc chắn dùng bản mới**;
   - nếu có thể spawn một smoke client/process mới độc lập thì dùng nó để kiểm;
   - không gọi đây là lỗi core B3.
4. Không in/log secret. File nhạy cảm chỉ kiểm path/hash/field cần thiết.

Báo cáo bảng:
`surface | entrypoint/config | proxy path/hash | route | identity forwarding | live label | action`.

## 4. Claude Code phải tự kiểm nhãn thật của CHÍNH MÌNH
Đây là acceptance quan trọng nhất của lượt đổi tay.

Trình tự:
1. Claude Code gọi read scoped `work/hpml-view-for-user/` → kiểm presence xuất hiện bằng nhãn thật của Claude Code (không synthetic).
2. Claude Code ghi **chính báo cáo/audit thật của lượt này** vào COLLAB — commit này là công việc thật, không phải fixture.
3. Đọc Git metadata của commit: author phải là nhãn client thật, email gateway đúng.
4. Chờ webhook/B2 publish → `lastActors` của HVU phải đổi sang nhãn Claude Code thật.
5. Presence cùng surface phải clear sau commit.
6. Gọi read scoped lần nữa → presence sáng lại.

Nếu phiên hiện tại đi qua proxy stale và không thể đổi nhãn mà không restart chính phiên:
- sửa proxy/config trước;
- dùng fresh smoke process/client nếu khả thi;
- nếu tuyệt đối cần Owner mở phiên mới, ghi đúng **một** action tối thiểu và lý do kỹ thuật; không bắt Owner làm các bước khác.

## 5. Rà mọi đường ghi ngoài gateway — phân loại, không mở rộng bừa
Codex đã liệt kê: SSH/local Git, GitHub web/API/CLI, host scripts/automation, Cowork shell/patch_export, clone ngoài VPS.

Claude rà lại và phân loại từng đường:
- **NORMAL_AI_PATH**: đường AI dùng thường xuyên để sửa `incomex-workspace`. Mục tiêu là route qua một trong hai gateway để actor/presence tự bắt; nếu có thể cấu hình lại mỏng/an toàn thì làm trong lượt này.
- **ADMIN/EXCEPTION_PATH**: human/admin/SSH hoặc đường cứu hộ. Giữ nguyên; commit qua đây có actor unknown là đúng.
- **NOT_A_SOURCE_WRITE**: ví dụ `workspace_exec` snapshot không tự commit nguồn; ghi rõ để khỏi hiểu nhầm.

Không dựng gateway thứ ba, không hook toàn hệ thống, không thay auth/secrets.

## 6. Synthetic-test hygiene
- Hai commit synthetic đã vào main: **không rewrite/reset lịch sử**.
- Từ lượt này: client/identity giả chỉ test ở temp repo, snapshot, disposable branch không merge, hoặc unit fixture.
- Main chỉ nhận commit công việc thật của surface thật.
- Nếu trong script/test hiện có default đẩy synthetic identity lên main, sửa guard/test target để ngăn tái diễn.

## 7. Kiểm regression và 2 điểm vàng
Bắt buộc:
1. `tasks.json`: legacy names không còn trong `lastActors`; task legacy thành unknown.
2. UI không còn hàng `AI via Incomex Workspace` / `Claude via MCP`.
3. UI display theo A9: `openai-mcp/...` → `GPT Chat/Work`, `claude-code/...` → `Claude Code CLI`, `Anthropic/ClaudeAI...` → `Claude Chat/Cowork`, `codex...` → `Codex`; raw label chỉ ở tooltip/debug.
4. Claude Code live acceptance §4 PASS hoặc ghi chính xác giới hạn restart.
5. P19 Claude Chat vẫn không regression: `Anthropic/ClaudeAI` hợp lệ.
6. B2 webhook/backstop/3-revision retention/last-good vẫn PASS.
7. B3 presence không tạo commit; state bounded; **mỗi task tối đa một actor `Đang làm`**, tín hiệu mới thay tín hiệu cũ ngay và record cũ **không được sống lại** sau clear/TTL.
8. Public MCP contract/version không đổi.
9. Không synthetic commit mới vào main.
10. UI/nginx/services healthy.

## 8. Kết thúc
- Không tạo progress file mới.
- Cập nhật COLLAB với:
  - kết quả cleanup;
  - bảng surface/proxy;
  - đường ghi NORMAL/ADMIN/NOT_SOURCE;
  - nhãn live Claude Code quan sát được;
  - lỗ nào còn OPEN thật sự.
- Ghi `KQ@HVU-B3-CLEANUP-20260921-03 XONG` khi cleanup + audit đạt; surface chưa tồn tại/chưa chạy như Hermes không chặn XONG nếu config/proxy đã sẵn sàng và ghi `FIRST_USE_PENDING`.
- Nếu hỏng core đã PASS: rollback phần cleanup và ghi DỪNG.
- Trả một dòng: `XONG · HVU.B3-CLEANUP · <refs>` hoặc `DỪNG · HVU.B3-CLEANUP · <lý do>`.
