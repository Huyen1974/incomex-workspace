# PROMPT — Hardening cuối cho hai đầu nối của workspace chung (GPT + Claude)

Trạng thái: DRAFT · Bản gộp GPT Chat + Claude Chat · 2026-09-19 · thay bản DRAFT 229f612
Chỉ chạy khi `COLLAB.md` ở gốc repo ghi `READY@<commit>` khớp commit cuối chạm file này VÀ Owner ra lệnh RUN.

## 0. Trước khi làm (bắt buộc)
1. Kiểm READY trên bản sao riêng (repo công khai, không cần khoá): `git clone --depth 50 https://github.com/Huyen1974/incomex-workspace /tmp/iw-ready`; so **đúng toàn bộ SHA 40 ký tự** từ `git log -1 --format=%H -- PROMPT.md` với dòng `READY@<full-sha>` trong `COLLAB.md`. Chỉ khớp tuyệt đối mới làm; lệch, SHA rút gọn hoặc chưa có READY → DỪNG, báo.
2. Đọc từ chính bản sao đó: `AGENTS.md`, `README.md` (§0–§11; §11: mã trên VPS là nguồn gốc duy nhất), `COLLAB.md` mục P03, P05, P06.
3. Không fetch/pull/sửa bằng tay hai clone làm việc (`/opt/incomex/mcp-roots/gh`, `/opt/incomex/data/workspace-tools/github-workspace`): chúng do dịch vụ khác quản lý; chạy git bằng user khác có thể hỏng quyền file. Chỉ tác động lên chúng qua mã của đầu nối.
4. Mỗi lỗi H01–H14: TÁI HIỆN bằng test đỏ trước khi sửa. Không tái hiện được → ghi "không tái hiện" kèm bằng chứng, không sửa mù.

## 1. Mục tiêu
Hai đầu nối tự viết, cùng một repo `Huyen1974/incomex-workspace`:
- GPT/AgentData: `/opt/incomex/docker/agent-data-repo/agent_data/` (`workspace_tools.py`, `workspace_operations.py`, `workspace_idempotency.py`, `workspace_execution.py`, `workspace_tasks.py`, `workspace_transfer.py`, `server.py`), `scripts/workspace-exec-worker.py`, tests tương ứng; container `incomex-agent-data`.
- Claude: `/opt/incomex/claude-mcp/app/` (`fsroots.py`, `server.py`) và trợ lý host `incomex-mcp-helper.service`; container `incomex-claude-mcp`.
Đích: làm việc nhiều tuần mà KHÔNG có bốn loại lỗi "im lặng": đọc bản cũ mà không biết; từ chối mà không nói lý do; báo thành công giả; ghi đôi. Sửa gốc, không vá triệu chứng, không bắt người dùng né lỗi của công cụ.

## 2. Danh mục lỗi (đã đối chiếu mã nguồn; P0 làm trước)
| Mã | Phía | Lỗi | Sửa | Mức |
|---|---|---|---|---|
| H01 | Claude | `fs_log`, `fs_diff` (fsroots.py ~1338, ~1361) không gọi `_freshen` như `fs_list/read/stat/search` | `fs_log`/`fs_diff` phải **force-refresh remote ngay trước khi đọc**, không chỉ đi qua TTL cache; nối freshness/HEAD vào kết quả như các read tool | P0 |
| H02 | Cả hai | độ tươi khác nhau: Claude đọc trễ tối đa 20 s (`FS_PULL_TTL_S`), GPT 2 s (`git_read_refresh_seconds`) | read thông thường có thể dùng cache cấu hình được ≤2 s; **mọi read quyết định an toàn/phiên bản** (`stat`, `log`, `diff`, kiểm READY và source trước `exec`) phải force-refresh. Kết quả Git read trả `source_head`/`refreshed_at` hoặc metadata tương đương | P0 |
| H03 | GPT | dispatcher (workspace_tools.py ~639–648) loại riêng `workspace_stat` khỏi bước kéo | `workspace_stat` phải force-refresh remote trước khi trả version/HEAD; worktree bẩn → không merge, trả `dirty:true` + HEAD local/remote, không giả dữ liệu là fresh | P0 |
| H04 | GPT | `git()` (~136–158) gom mọi lỗi thành `GIT_OPERATION_FAILED`, bỏ stderr, không ghi log | lỗi theo phase: fetch · fast-forward · add · diff-check · commit · push · rollback; detail an toàn (lệnh mạng che output, không URL/credential); ghi log vận hành có event id | P0 |
| H05 | GPT | `git diff --cached --check` đang gom cả whitespace và conflict marker vào một chốt chặn cứng | Tách loại: trailing whitespace / blank-at-EOF → `warnings`, không chặn và không tự sửa bytes; **leftover conflict marker (`<<<<<<<`, `=======`, `>>>>>>>`) vẫn là hard error** với path:line:lý do rõ ràng | P0 |
| H06 | GPT | transaction trả `changed=bool(after)` → no-op vẫn báo đổi | no-op → `changed:false`, `commit:null`, không push; hỗn hợp → chỉ tính file thật sự đổi | P0 |
| H07 | Cả hai | operation_id không gắn tên tool: GPT `workspace_idempotency.py`; Claude `_args_hash` (fsroots.py ~407) và phép so ở ~435 | khoá = tool + hash tham số; cùng id khác tool → `OPERATION_ID_REUSED`, không replay | P0 |
| H08 | Cả hai | hoàn tác không sạch bị coi như thất bại sạch rồi cho chạy lại: GPT `ROLLBACK_CONFLICT`; Claude `fs_transaction` ghi journal `failed` dù `undo_problems` khác rỗng (~1638) | trạng thái `recovery_required`/`unknown`, không tái thực thi, nói rõ file nào cần kiểm | P0 |
| H09 | GPT | `workspace_exec`: worker chụp snapshot không kéo bản mới, không giữ shared lock | kéo trước, chụp dưới shared lock, trả `source_head`; snapshot vẫn cô lập | P1 |
| H10 | GPT | `workspace_diff(from_version)` không đọc backup của transaction; log có cấu trúc không phản ánh transaction | đọc được sau edit đơn, transaction, copy/move | P1 |
| H11 | GPT | `locked()` thử flock một lần rồi BUSY (README nói có chờ); telemetry có nhiều lỗi read/search chưa phân loại | chờ có hạn + backoff, cấu hình được; ghi chỉ chờ trước phase quan trọng; BUSY kèm `retry_after_seconds`; phân loại lỗi hiện có, không giả định đều là BUSY. Claude đã có vòng chờ (~314–326): kiểm, giữ | P1 |
| H12 | Cả hai | client giữ danh sách tool cũ: ChatGPT TEST20 vẫn chặn `operation_id` khi gọi thẳng `workspace_edit`/`workspace_transaction`; Claude Chat chưa thấy `fs_transaction/fs_stat/fs_copy`; `serverInfo.version` cố định `1.0.0` | tăng version chuẩn mỗi lần đổi schema, kiểm `tools/list`, dùng `listChanged` nếu client hỗ trợ; viết quy trình phát hành bắt buộc làm mới client vào báo cáo; không dùng `workspace_task_start` làm đường vòng lâu dài | P1 |
| H13 | GPT | metrics chỉ đếm tổng lỗi | đếm theo tool + mã lỗi + phase, đã làm sạch | P2 |
| H14 | Cả hai | mất phản hồi ở điểm tạo việc: `workspace_task_start`, `workspace_exec`, `workspace_import_file`, `workspace_upload_begin` và điểm tương đương phía Claude | retry không tạo việc trùng hoặc mồ côi; chỗ nào đã an toàn thì ghi bằng chứng, không sửa | P2 |

## 3. Thứ tự, tiến độ và điểm dừng an toàn
- `RUN_ID: HARDEN-20260919-01`. Không tạo file progress/handoff/archive mới trong repo. `PROMPT.md` là work order duy nhất và **bất biến sau READY**; lịch sử prompt nằm trong Git.
- Tiến độ chi tiết có đúng hai nguồn: (a) commit mã `[Claude Code] Hxx · <tóm tắt>`; (b) mục §13 trong báo cáo KB đã chỉ định ở §7. `COLLAB.md` chỉ giữ trạng thái tổng quát do Host cập nhật sau nghiệm thu, không dùng làm nhật ký từng bước của Agent.
- Làm P0 → P1 → P2. Xong mỗi mục: test xanh + commit mã vào git sẵn có của thư mục mã, message `[Claude Code] Hxx · <tóm tắt>` và cập nhật một dòng trạng thái Hxx trong báo cáo hiện hữu.
- Xong toàn bộ P0: deploy (mỗi service một lần), nghiệm thu backend phần P0, ghi báo cáo. Rồi mới sang P1, P2 và deploy lần hai nếu cần.
- Ngữ cảnh chạm 60–70%: dừng ở ranh giới một mục đã xong, cập nhật §13 (xong gì · dở gì · commit cuối · làm tiếp từ Hxx nào). Phiên Agent sau tiếp tục bằng `PROMPT.md` + §13 + Git log; không cần chép lại lịch sử chat. Không để mã nửa chừng chưa commit hoặc chưa deploy.

## 4. Triển khai và quyền (Owner cấp qua lệnh RUN)
- Sửa trên VPS, dựng tại chỗ (README §11); không kéo mã từ GitHub; không force-push. Trước khi dựng, xác định container chạy mã bằng mount hay image rồi làm đúng cách đó; đọc `claude-mcp/00-NHAN-THU-MUC.md`.
- Được phép: restart `incomex-claude-mcp`, `incomex-mcp-helper.service`; restart `incomex-agent-data` chỉ khi không có tác vụ/giao dịch đang chạy (hàng đợi job rỗng, không manifest `prepared`/`push_unknown`/`rollback_conflict`); bận thì chờ tối đa 10 phút, vẫn bận → DỪNG, báo.
- Service không healthy trong 2 phút sau restart → hoàn nguyên đúng commit mã của mình, dựng lại, báo. Đây là hoàn nguyên duy nhất được phép.
- Không đổi auth/URL/secret, tên tool, service hay cấu hình nào khác. Phát hiện bug buộc phải đổi những thứ đó → DỪNG, báo trước.
- Ngoài phạm vi: đĩa VPS 86% là nợ đã biết, không dọn trong đợt này.

## 5. Nghiệm thu backend (Claude Code tự làm; không phải PASS ở client)
- Commit thử thật chỉ nằm trong `_thu-nghiem/hardening-20260919/` của repo, file nhỏ, message `[Claude Code] TEST Hxx`; không xoá sau khi thử, liệt kê trong báo cáo. Không đụng `AGENTS.md`, `README.md`, `COLLAB.md`, `PROMPT.md`.
- Gọi qua đúng đường mã của từng đầu nối (endpoint MCP nội bộ hoặc handler), không dùng git tay thay đầu nối.
- A. Độ tươi chéo: GPT đang ở commit A; Claude đẩy B; **ngay lập tức, kể cả trong cửa sổ TTL**, không gọi đọc trung gian → GPT `stat`, `log`, `diff` thấy B; `exec` chạy trên `source_head=B`. Chiều ngược: GPT đẩy → Claude cold `fs_log`, `fs_diff` thấy B ngay. Test phải chứng minh safety-critical read không phụ thuộc cache TTL.
- B. Snapshot: giữ khoá ghi nhiều file trong lúc `exec` bắt đầu chụp → chờ, hoặc trọn bản trước, hoặc trọn bản sau; không trạng thái lai.
- C. Lỗi minh bạch: trailing whitespace và blank-at-EOF → ghi THÀNH CÔNG kèm `warnings`, bytes giữ nguyên; fixture có leftover conflict marker (`<<<<<<<` / `=======` / `>>>>>>>`) → bị CHẶN với mã/phase/path:line rõ; `expected_version` cũ; remote đã chạy trước; lỗi git giả lập → đúng phase, không còn `GIT_OPERATION_FAILED` chung khi đã biết nguyên nhân.
- D. Transaction: no-op → `changed:false`, không commit; 2 file → đúng 1 commit; lỗi ở op thứ N → không file nào đổi; push bị từ chối → hoàn tác đủ; `diff(from_version)` sau transaction đọc được trước/sau.
- E. Idempotency, mọi tool ghi, cả hai phía: cùng id + cùng tool + cùng payload → replay, 1 commit; khác payload → từ chối; khác tool → từ chối; mất phản hồi → replay/recover; sau restart → replay; hoàn tác không sạch/không rõ kết quả → không tái thực thi.
- F. Khoá: giữ ngắn hơn hạn chờ → lệnh đọc tự chờ rồi PASS; giữ quá hạn → BUSY + retry_after, không treo.
- G. Schema: version/hash mới hiện trong `tools/list` của cả hai server.
- Toàn bộ test cũ vẫn xanh; thêm test cho H01–H14.

## 6. Cấm
Không sửa `AGENTS.md`, `README.md`, `COLLAB.md`, `PROMPT.md` (Agent không sửa luật nền — AGENTS A2; Host cập nhật sau nghiệm thu client). Không xoá file, dữ liệu, nhánh, fixture. Không ghi PASS client dựa trên backend. Không mở rộng phạm vi. Gặp gì ngoài dự kiến → DỪNG, báo.

## 7. Báo cáo (cũng là chỗ bàn giao)
- Ghi vào KB, tài liệu có sẵn `knowledge/current-state/reports/mcp-incomex-vps-nang-cap-fs-roots-2026-09-17.md`, thêm mục §13 "Hardening 2026-09-19"; cập nhật dần tại đó, không tạo tài liệu mới.
- Mở đầu bằng bảng H01–H14 và A–G × 🟢🟡🔴 + bằng chứng một dòng. Sau đó: nguyên nhân gốc từng lỗi, file/dòng đã sửa, test mới, commit mã, service đã deploy và lúc nào, version/hash schema, danh sách việc chờ nghiệm thu client.
- Không ghi "production ready" khi client chưa PASS.

## 8. Sau khi Agent xong (không phải việc của Agent)
1. Owner làm mới hai client theo quy trình phát hành (H12).
2. Claude Chat nghiệm thu client: `fs_log/fs_diff` lạnh thấy commit mới của GPT; `fs_transaction`; `operation_id`.
3. GPT Chat nghiệm thu client: gọi thẳng `workspace_edit` và `workspace_transaction` có `operation_id`; `workspace_stat` lạnh; cảnh báo khoảng trắng.
4. GPT (Host) dùng transaction đã sửa cập nhật `AGENTS.md` + `README.md` + `COLLAB.md` trong một commit: P01–P06, D06, README mô tả đúng hành vi mới, bỏ đường vòng P03, không đưa luật khoảng trắng vào luật làm việc. Đây cũng là phép thử transaction ở client thật.
