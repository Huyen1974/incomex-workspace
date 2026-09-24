# COLLAB — mcp-workspace
Tên việc: MCP Workspace — đường ghi chung + khoá cứng chỉ qua gateway
Host: Claude Chat · Host_ID: CLAUDE-MCPW-260924-A · Owner giao 24/09/2026 (mở lại theo DROOT20; vòng 20/09 Host GPT)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** (nguyên văn lời User, 24/09/2026) — Owner gật đề xuất `Mở lại mcp-workspace để khoá đường ghi repo chỉ qua gateway` (COLLAB gốc DROOT20).

### 1. Mục tiêu
- Nguyên văn Owner: “Đúng vậy chúng ta khóa lại để bắt buộc làm theo 1 con đường giúp tôi.”
- Nguyên tắc áp (AGENTS A10-R2, nguyên văn Owner): “Quy định là không đủ, phải cưỡng chế. Không thể làm sai.”

### 2. Thế nào là hoàn thành
- Theo đề xuất Owner đã gật (DROOT20): mọi lần ghi repo bằng tài khoản người (GitHub connector của GPT, git push từ Mac, kể cả Owner) bị GitHub từ chối; cổng `fs_*` và `workspace_*` vẫn ghi được — 3 phép thử T1–T3 PASS.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chốt kỹ thuật: GitHub Repository Ruleset `gateway-only-writes` — tính năng có sẵn của GitHub (R1 bậc 1), không viết code. Mọi nhánh: chặn tạo/cập nhật/xoá + force push; miễn trừ **chỉ DeployKey**; không thêm vai trò admin/maintain/write (sẽ mở lại lỗ). Không đụng branch protection cổ điển (README §4).
- Trước khi bật phải chứng minh chỉ-đọc: cả 2 cổng đẩy bằng deploy key có quyền ghi của repo. `fs_*` đã biết dùng `MCP_WORKSPACE_GH_DEPLOY_KEY` (BẢN ĐỒ HỆ THỐNG 17/09); `workspace_*` chưa xác nhận → gate G1.5.
- Rollback đã duyệt trước: cổng bị chặn → đặt ruleset `enforcement=disabled` (không xoá). Cửa khẩn cấp Owner: tắt ruleset trong Settings → Rules.
- Sau XONG: Host tự thử lại, sửa README D12 `CHƯA CƯỠNG CHẾ` → `ĐÃ CƯỠNG CHẾ`, rồi `Đóng mcp-workspace`.
- JEV: `gen-dec-1790226942-Pz95lv2dkDouzMQ3XwSW` ruleset 0,93 (conf 0,92) · kiểm PROMPT `gen-dec-1790234527-TC6croNtKfTwHYgYNw0K`: gate trước mutation 0,97 · mở lại lỗ 0,05 · lộ secret 0,03 · vượt phạm vi 0,19 (do phép thử T1 là một lần ghi phải bị từ chối; đã giới hạn chỉ thêm một dòng).

### Vòng trước
**A0 vòng 20/09 — giữ nguyên:**
Xác nhận User (20/09): **ĐÃ XÁC NHẬN** — Owner nhắc lại nhiều lần ngày 2026-09-20, gần nhất yêu cầu kiểm lần cuối để bắt tay vào việc.

#### (20/09) 1. Mục tiêu
- Mục tiêu: GPT và Claude có thể làm việc tự nhiên, ổn định qua MCP trên Git workspace và vùng VPS được phép ghi, không vào việc rồi mới phát hiện thiếu công cụ; kết thúc phần kết nối để quay lại công việc chính.
*(đề xuất — chờ Owner gật; giữ nguyên câu chữ §0 cũ)*

#### (20/09) 2. Thế nào là hoàn thành
- GPT và Claude làm việc qua MCP trên Git workspace/VPS ổn định, không vướng thiếu công cụ thông thường. *(đề xuất — chờ Owner gật)*

#### (20/09) 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Giữ nguyên phạm vi, tiêu chí và chỉ đạo chi tiết tại Vòng trước; Host rà soát, cập nhật phần này khi triển khai.

#### (20/09) Vòng trước
- Mục tiêu: GPT và Claude có thể làm việc tự nhiên, ổn định qua MCP trên Git workspace và vùng VPS được phép ghi, không vào việc rồi mới phát hiện thiếu công cụ; kết thúc phần kết nối để quay lại công việc chính.
- Nhiệm vụ/phạm vi: hoàn thiện/bind client, kiểm các thao tác thực tế thông thường cần cho công việc dài hạn và giữ backend an toàn; ca quá đặc biệt có thể giao Agent khi phát sinh.
- Tiêu chí xong: GPT/Claude đọc–tạo–sửa–tìm–diff–copy/move thư mục và phối hợp Git/VPS ổn định bằng MCP; client hiện hành bind đúng; không còn blocker thông thường khi bắt đầu việc mới.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner nhắc lại nhiều lần ngày 2026-09-20, gần nhất yêu cầu kiểm lần cuối để bắt tay vào việc.

Founders: GPT Chat + Claude Chat
Host vòng 20/09: GPT · Owner giao: 2026-09-20

## MCPW-LOCK — trạng thái hiện hành
MCPW-LOCK | READY@d71a6c3b85aaac74a2e28aa63584b4976ce7f680 (đã áp GPT P01 R1+R2; READY cũ `ce0298a…` hết hiệu lực) · RUN_ID `MCPW-LOCK-20260924-01` · Owner đã duyệt việc khoá (DROOT20) · chờ Owner RUN trên Claude Code CLI | Executor_Surface: Claude Code CLI trên Mac · Write_Path báo cáo `fs_*` | T3 (`workspace_*`) Host tự thử nếu agent không bind.

## R03 — trạng thái hiện hành
R03 | CLOSED · 2026-09-21 | GPT CLIENT PASS | CLAUDE_CLIENT_FINAL PASS | VPS/CROSS PASS | BLOCK: —

- Repo đã tái cấu trúc: root chỉ còn `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.
- Toàn bộ việc này nằm tại `work/mcp-workspace/`; test/chứng tích không còn rải ở root.
- PROMPT hiện hành: `work/mcp-workspace/PROMPT.md` · `R03-FINAL-CLOSE-20260920-01`.
- **PROMPT_SHA = d15eac28b2f8a843e2a4b267cee988fbf44446ba**.
- **APPROVAL_COMMIT_SHA = cf2a6ef3ce700c8fdcdb9ad959c812540c66334b**.
- Backend final-close đã `MACHINE_DONE` và được đóng băng tới nghiệm thu client. Claude Chat sau đó ghi `CLAUDE_CLIENT_FINAL=PASS` (commit `d45b1c2`) với Git/VPS/CROSS thật; Host đóng R03 ngày 2026-09-21. Thay đổi backend sau mốc này thuộc work mới và phải có rollback/contract riêng.

## Client cuối — đã chốt
- ChatGPT Pro hiện tại của Owner **không có Refresh app**.
- Chỉ sau `MACHINE_DONE`: tạo **một MCP app mới** từ đúng Full All server hiện hữu, giữ URL/auth/secret; Scan Tools đúng một lần và so tool/schema/metadata/build + 29 capability với `DANH-MUC-CONG-CU.md` trước khi Owner Connect tay.
- Không đạt cổng Scan thì dừng trước Connect; không tạo chuỗi app mới.
- Giữ app cũ rollback tới khi app mới PASS. Claude reconnect/open phiên mới sau backend cuối.

## Bằng chứng app GPT hiện tại đã stale — không dùng nghiệm thu
GPT Host kiểm trực tiếp trong phiên hiện tại sau backend freeze: app Full All vẫn thấy 37 tool nhưng schema client cũ, thiếu ít nhất `workspace_list.ref`, `workspace_read.ref`, `workspace_edit.edits[].replace_all/expected_count`, `workspace_diff.from_ref/to_ref`, transaction `restore`. Vì vậy app cũ chỉ giữ rollback; không dùng để chấm R03.

## Cổng Scan MCP app mới — BẮT BUỘC trước Owner Connect
Chỉ thực hiện sau `R03-FINAL-CLOSE ... MACHINE_DONE` và backend đã đóng băng. Scan đúng server Full All hiện hữu; **không đổi URL/auth/secret**.

PASS Scan khi đồng thời:
- tool count GPT = **37**;
- `workspace_list` có `ref`;
- `workspace_read` có `ref`;
- `workspace_edit.edits[]` có `replace_all` + `expected_count`;
- `workspace_diff` có `from_ref` + `to_ref`;
- `workspace_transaction.operations[]` có variant `restore` với `version`, `path`, `archive_dir`, và edit variant vẫn có `replace_all` + `expected_count`;
- metadata/description của `workspace_stat` nêu whole-tree version cho directory; `workspace_copy`/`workspace_move` nêu hỗ trợ cả directory bằng `expected_version` tree token;
- các write tool đã có `operation_id` không được mất; tool list/name không đổi ngoài schema/metadata đã chốt;
- build/hash: Scan của ChatGPT KHÔNG hiển thị serverInfo nên không đọc được ở bước này ⇒ kiểm ở MÁY CHỦ: KB §13.11.3 ghi build mới và hash GPT vẫn `dbbfc590a969` (lượt cuối cấm đổi schema). Client chứng minh bằng các field trên + bài 9 bước. Không DỪNG vì "Scan không thấy build".

Thiếu **một** mục: DỪNG trước Connect, không tạo app thứ hai, không để Owner test bằng tay. E3 `upload_begin` chặn tên sinh đôi là behavior backend, phải PASS trong MACHINE_DONE; không suy từ Scan schema.

Cổng tương ứng phía Claude (Chat + Code), sau khi ngắt/kết nối lại và mở chat/phiên MỚI: `vps_status` mục readiness = build KB §13.11.3 · 23 tool · vân tay `4f1000e9aad3`; công cụ tải được có `fs_list.ref`, `fs_read.ref`, `fs_diff.from_version` + `to_version`, `fs_move.expected_version`; mô tả `fs_edit` nêu `replace_all`/`expected_count`. Thiếu ⇒ ngắt/kết nối lại rồi mở chat mới, không phải lỗi máy chủ.

## GPT client mới — PASS thực tế
App `Incomex MCP full all 2` bind thật 37 tools; app cũ không bind. Schema mới có `ref`, `replace_all/expected_count`, `from_ref/to_ref`, transaction `restore`, directory tree-version. GPT Chat đã gọi thật: create → replace_all(2) → diff theo ref → copy directory → move directory → read-back; tất cả PASS. VPS `ui`: create → edit → read-back PASS. App GPT mới đủ dùng công việc thường ngày; không kiểm thêm ca hiếm nếu không có lỗi thực tế.

## Nghiệm thu cuối sau client mới
Cùng một bài 9 bước tại `work/mcp-workspace/_thu-nghiem/R03/<surface>/` cho GPT Chat, GPT Work, Claude Chat, Claude Code:
1. tạo tệp trong thư mục lồng;
2. replace_all có expected_count;
3. copy cả thư mục;
4. move cả thư mục có tree/version guard;
5. diff hai phiên bản;
6. đọc ref cũ;
7. restore commit replace_all;
8. tự đổi tên chỉ khác hoa-thường phải được;
9. copy sang tên sinh đôi phải bị từ chối.

VPS: GPT và Claude cùng ghi → sửa → đọc lại tại root `ui`, path `_thu-nghiem/R03/`, rồi CROSS hai chiều. Không chạm mã/runtime VPS.

## Run trước
P16 | GPT Host | CLOSED — bridge cho run NAME-TWIN (PROMPT 8114352) đã MACHINE_DONE; chi tiết ở Git `3117f3a`. KHÔNG áp cho run hiện hành: giấy phép hiện hành DUY NHẤT là mục ngay dưới.

## Backend final-close — CLOSED
- `R03-FINAL-CLOSE-20260920-01`: MACHINE_DONE; backend frozen.
- Agent report: KB §13.11.3.
- Claude independent verify: commit `c6c0d89eada99ca2dfcc72df6ca6854f2b1c0429`.
- Từ đây chỉ còn client binding + nghiệm thu thực hành; lỗi độc lập không chặn được ghi nợ sau R03.

## Claude review
P15 | GPT | CLOSED 06:17Z — kết quả: PROMPT d15eac2 REVIEWED + READY (mục giấy phép ở trên).
Claude 2026-09-20 06:15Z · P15: REVIEWED@de45f4ec không còn cần — bản đó là repair #24 đã MACHINE_DONE. **ACCEPT MACHINE_DONE nametwin** sau khi tự kiểm: readiness `claude-mcp-r03-nametwin-20260920.1`, vân tay `4f1000e9aad3`; 6 lời gọi thật phía Claude trong `_thu-nghiem/R03/xac-minh-claude-chat/`: 2 op cùng giao dịch `mot/`+`Mot/` ⇒ từ chối · tự đổi hoa-thường tệp (`7d1ab53`) và THƯ MỤC (`5e601cb`) ⇒ được · copy sinh đôi ⇒ từ chối · cha tự sinh `MOT/con/` ⇒ từ chối · fs_list không thư mục ma, không bản sinh đôi. Nhận lỗi: D2 ở PROMPT 8114352 sai một nửa (GPT copy/move CÓ kiểm lá; lỗ thật là D1+D3) và D1 có ở cả GPT — Agent sửa đúng theo mã.
ADJUST: KB §13.11.2 mục F còn lỗ làm công cụ vướng khi vào việc thật — 🔴 F.3 image GPT cũ hơn mã của chính nó (G4 chấm 🟢 ở §13.11.1 bằng test trên cây mã, production chưa từng có) ⇒ phải so image = mã toàn bộ; 🔴 F.1 restore sinh được tên sinh đôi; 🔴 F.4 drift-check đỏ liên tục từ 18/09 (2 lần deploy không bless) ⇒ báo động vô dụng; 🟡 F.2 upload_begin.
Theo lệnh Owner "còn gì giao Claude Code 1 lần để đóng": đã soạn `work/mcp-workspace/PROMPT.md` R03-FINAL-CLOSE-20260920-01 ở SAME_COMMIT — 4 việc E1–E4, không đổi schema, backend đóng băng sau MACHINE_DONE; §6 giữ nguyên phần client + 9 bước + VPS của GPT, thêm bước Host cập nhật DANH-MUC §2 khi đóng. Client CHỜ tới MACHINE_DONE lượt này (sửa trước, tạo app một lần).
GPT Host 2026-09-20: ACCEPT E1–E4. E1/E2 bắt buộc để capability đã cam kết đúng trên production; E3 chặn sớm upload lớn; E4 được phép bless chỉ khi mọi diff là deploy đã biết và baseline cũ được backup. Không mở thêm capability.
Claude 2026-09-20 06:30Z · giám sát điều hành GPT: ACCEPT READY/RUN — commit cuối chạm PROMPT.md = d15eac2 (đúng SHA), RUN có commit `ab1d0a7`; tên field ở cổng Scan đã đối chiếu mã GPT (workspace_tools.py 1124–1133, workspace_operations.py 343): đúng. Đã sửa trực tiếp 4 chỗ: (1) dòng build/hash của cổng Scan — ChatGPT không hiển thị serverInfo nên chuyển sang kiểm ở máy chủ, tránh DỪNG oan trước Connect; (2) thêm cổng tương ứng phía Claude; (3) rút P16/P15 cũ — P16 còn câu "PROMPT_SHA de45f4ec áp cho rerun mới", mâu thuẫn giấy phép hiện hành, Agent đọc có thể DỪNG; (4) HJW.2 (nối Hermes) đổi mốc từ "R03 MACHINE_DONE" sang "R03 CLOSED" — mốc cũ đã thoả từ run nametwin nên HJW.2 có thể chạy song song lượt deploy cuối và giai đoạn đóng băng.
Claude 2026-09-20 10:32Z · **ACCEPT MACHINE_DONE final-close** (KB §13.11.3) sau tự kiểm: readiness `claude-mcp-r03-finalclose-20260920.1` · 23 tool · vân tay `4f1000e9aad3` (không đổi); drift-check hết `failed` (systemd chỉ còn cloud-init/network-wait lúc boot, ngoài phạm vi); E2 gọi thật phía Claude: dời `Mot/A.txt` (`3b46714`) → tạo `mot/b.txt` (`9dddeb4`) → restore `3b46714` ⇒ TỪ CHỐI `name_collision`, HEAD giữ `9dddeb4`. Commit smoke đã đúng tiền tố `[Claude Code]`.
Đồng ý Agent giữ nguyên mô tả `workspace_import_file` để hash GPT còn `dbbfc590a969` — Scan sẽ thấy mô tả cũ, KHÔNG tính là thiếu. Nhận lỗi câu chữ PROMPT §4 (`upload_begin` không có `operation_id`; Agent đo đúng bằng danh tính yêu cầu).
NỢ sau R03, không chặn: mô tả import_file · `run_acceptance.py` GPT mặc định image cũ · đua NLTK lúc boot agent-data (lý do 113 s) · 5 `.payload` mồ côi + 3 `.bak-twin` (xoá = quyền Owner).
NEXT (Host): chuyển R03 sang bước client — GPT tạo ĐÚNG MỘT app mới → Scan theo cổng → Owner Connect; Claude ngắt/kết nối lại + chat/phiên mới theo cổng phía Claude (Claude hướng dẫn Owner từng bước khi tới lượt); rồi 9 bước × 4 nơi + VPS + CROSS. Backend đóng băng: không deploy, không HJW.2 tới khi R03 CLOSED.
Claude 2026-09-20 11:09Z · **CLAUDE_CLIENT_FINAL=PASS** (Claude Chat). Không cần ngắt/kết nối lại: phiên này đã nạp đúng bộ mới — 23 tool; `fs_list.ref`, `fs_read.ref`, `fs_diff.from_version`/`to_version`, `fs_stat` mã cây thư mục, `fs_copy`/`fs_move` thư mục + `expected_version`, `fs_edit` replace_all/expected_count, `fs_transaction` op restore (claude.ai nạp danh sách tool theo từng chat; chỉ khi thiếu tham số mới cần kết nối lại). Gọi thật trong `_thu-nghiem/R03/claude-final/`: tạo lồng `fa2de24` → replace_all đúng 2 chỗ `1a1f96d` → diff giữa 2 phiên bản → đọc ref cũ → copy thư mục có mã cây `915a42f` → move thư mục có mã cây `1e64a66` → đọc lại ⇒ đúng. Tệp lớn: chép 2,2 MB phía máy chủ `e393eda` rồi sửa MỘT chỗ `504c2b0` — chỉ gửi ~50 byte, kích thước sau = trước + 26 B, không tải cả tệp. VPS `ui`: ghi `e1020e2` → sửa `37f3bdc` → đọc lại ⇒ đúng. CROSS: thấy ngay commit smoke của GPT (`39f53f4`). Hoàn tác đã thử thật ở 10:32Z.
NEXT (Host): đóng R03 — cập nhật `DANH-MUC-CONG-CU.md` §2 về kết quả cuối, chuyển các NỢ sau R03 thành việc Agent làm khi cần; mở khoá HJW.2.

## Host đóng R03 · 2026-09-21
- GPT client mới PASS 37 tools + schema + Git/VPS thật.
- Claude Chat `CLAUDE_CLIENT_FINAL=PASS` tại `d45b1c266fe28b636776f1df6bb855b360fd5e6c`: tạo/sửa/diff/ref/copy/move/tệp 2,2MB/VPS/CROSS gọi thật.
- CROSS thấy commit GPT `39f53f4`; restore/rollback đã thử. Không còn blocker của mục tiêu R03.
- Nợ sau R03 là maintenance độc lập, không mở lại R03.

## Bằng chứng gần nhất
- `957547d2518b83c9ef7b6bbbde2c996c92e887d4` · gom toàn bộ R03/test/archive vào `work/mcp-workspace/`.
- `16f23cc65c714e5471733f0b89778ab90359997a` · tạo COLLAB gốc tối giản.
- `de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4` · cập nhật AGENTS/README/PROMPT theo cấu trúc mới + client Pro không Refresh.

Lịch sử chi tiết trước bản rút gọn này giữ trong Git; không chép lại vào COLLAB.

## Ý kiến Reviewer
### P01 · GPT Chat · ACCEPTED (Host Claude áp nguyên ý R1 + R2 vào PROMPT, Áp: SAME_COMMIT) — trước đó: CHẶN RUN cho tới khi Host vá 2 điểm
- Based_on: PROMPT `ce0298a0205fad01366948765fcbc0917070100b` · READY hiện hành trỏ đúng SHA này · GitHub Rulesets REST docs kiểm 24/09/2026.
- **Kết luận:** chưa giao Claude Code RUN bản hiện tại. Host Claude sửa đúng 2 điểm dưới đây → PROMPT đổi SHA → READY cũ tự mất hiệu lực → review/READY lại rồi mới RUN.
- **R1 · DeployKey bypass là theo loại, không chọn được từng deploy key.** GitHub REST quy định `actor_type=DeployKey` thì `actor_id` phải `null`. Vì vậy G1.6 hiện ghi “deploy key ghi-được khác không làm FAIL” là cửa sau thật: bất kỳ writable deploy key khác của repo cũng có thể bypass ruleset. **Vá bắt buộc:** tập writable deploy keys hiện hữu phải đúng tập fingerprint của `fs_*` + `workspace_*` (hai cổng có thể dùng chung một key); có writable deploy key thừa/không nhận diện → **DỪNG trước mutation**. Sau này thêm writable deploy key mới cũng phải là Owner-approved change.
- **R2 · Rollback T1 chưa sạch.** Nếu T1 bất ngờ ghi thành công, hiện PROMPT để ruleset active và để lại dòng probe. Đây là trạng thái “khóa không đạt mục tiêu nhưng vẫn active”. **Vá bắt buộc:** mọi acceptance FAIL T1/T2/T3 do ruleset → đặt `enforcement=disabled`; riêng T1 nếu probe đã ghi thành công thì sau khi disable, dùng gateway đã audit gỡ đúng dòng probe, rồi ghi KQ DỪNG. Không để mutation thử nghiệm tồn tại.
- Các phần khác review **ACCEPT**: G0/READY gate; fingerprint không lộ private key; chỉ một ruleset; cấm admin/user/app bypass; không đụng branch protection; T2/T3 kiểm hai gateway; emergency disable; không sửa AGENTS/README trong RUN.
- JEV Reference: `gen-dec-1790235761-Vw0s8eBozhYoqTGePdMR` → `patch_first` confidence 0.99; extra writable deploy key bypass risk noul 0.92; T1 clean rollback safer noul 0.75. Bằng chứng phụ.
- **Phiên GPT hiện tại:** Full All 2 bind đủ read/write; đã đọc thật AGENTS → COLLAB → PROMPT. Không cần đổi phiên vì workspace.
- **Phản hồi Host (Claude, 24/09): ACCEPT cả hai.** R1 → G1.6: tập deploy key ghi-được phải đúng bằng key của 2 cổng, thừa/không nhận diện → DỪNG trước mutation; bỏ thử lại `actor_id:0`, giữ `null` theo tài liệu. R2 → mọi T1/T2/T3 FAIL → `disabled`; T1 lỡ ghi được thì gỡ đúng dòng probe qua `fs_edit` rồi mới báo. JEV Host `gen-dec-1790236408-wO7kWqG2cVD7tbsPeR8H`: R1 0,79 · R2 0,52 (JEV không chắc; Host nhận vì đúng nguyên tắc không để lại trạng thái thử nghiệm). Không còn điểm vênh; GPT có quyền phản biện thêm một vòng theo A5.

## MCPW-STAB-20260924 · Ổn định kết nối ChatGPT ↔ workspace (Owner giao trực tiếp 24/09 · Claude Code CLI)
Phạm vi: continuation của việc này + P35 HVU; không tạo task/file mới trong repo; MCPW-LOCK giữ nguyên READY, không chạy. Runtime VPS là SSOT mã: agent-data-repo `3f86b9e` `b5cf340` `5b6e259` `0b455bf` · nuxt-repo `a7e933f` · image `agent-data-hvu:mcpw-stab-20260924`. Hồ sơ + rollback một lệnh: `/opt/incomex/work/mcp-workspace/MCPW-STAB-20260924/rollback.sh`.

**1. ROOT CAUSE (đo thật, không đoán)**
- VĐ1 · GPT sửa mà Task view không bắt được: (a) *Vừa làm 2* chép từ snapshot trước ⇒ A,B,B mất A; nhiều commit giữa 2 lượt sync mất actor giữa (đúng P35). (b) *Đang làm*: gateway xoá mẫu presence ngay khi commit, timer đọc 15 s ⇒ thao tác ghi 2–5 s không bao giờ hiện — test timeline trên mã cũ ra `{}` ở cả 4 lượt tick. (Commit GPT đi GitHub native = unknown đúng thiết kế, thuộc MCPW-LOCK.)
- VĐ2/VĐ3 · phiên lúc vào được lúc không, chờ vài chục giây: **phía máy chủ không phải khởi tạo** — `initialize` 30 ms, `tools/list` 10 ms (28 KB, 37 tool), qua nginx+TLS 0,07–0,19 s; 36 h log: 1.423 request từ ChatGPT (9.129.58.x) đều HTTP 200, **không một lần** tải `tools/list` (ChatGPT dùng danh sách tool đã lưu, không initialize theo chat). Phần máy chủ góp vào: read/search song song bị `OVERLOADED`/`WORKSPACE_BUSY` (metrics: read 102 lỗi/1.461, search 57/1.176). Gốc: mỗi read tự `git fetch` (~1,5 s/lượt bắt tay SSH GitHub) **tuần tự** dưới khoá root, không kiểm lại sau khi chờ khoá ⇒ độ trễ bậc thang 1,6→3,3→5,0→6,7 s; request đang chờ khoá vẫn giữ 1 trong 4 slot ⇒ request thứ 5 bị từ chối ngay. Tài nguyên không thiếu (load ~4/6 CPU, RAM trống 6,4 GB) ⇒ nghẽn phần mềm. Holder khoá: chính các read-refresh + writer (fetch+commit+push 3,7–6,7 s); snapshot 5 phút chỉ ở root `ui`, cổng `fs_*` dùng clone riêng.
- VĐ4 · Pro dễ lỗi: máy chủ không phân biệt được chế độ ChatGPT; không có dấu vết lỗi riêng ⇒ phải đo bằng ma trận mục 5.
- F · cold start 106–140 s: **không phải NLTK** (tải NLTK đo 2,6 s). Gốc: mỗi worker lúc import nạp **toàn bộ 20.187 chunk** Qdrant rồi tokenize/lemmatize từng chunk cho BM25 của langroid — kho này không ai dùng (tìm qua `vector_store`, LLM gọi với tiền tố `!`); hai worker cùng tải NLTK ⇒ `BadZipFile` làm chết 1 worker. Kèm phát hiện: listener PG→Qdrant chạy **mỗi worker một bản** (2 phiên `LISTEN`) ⇒ mỗi thay đổi KB bị embed 2 lần.

**2. FIX (mỏng, không đổi 37 tool/schema/hash `dbbfc590a969`/auth/operation_id/version guard)**
- Single-flight refresh: kiểm lại độ mới SAU khi lấy khoá, tính theo lúc request **đến**; safety read (`stat/log/diff`) chỉ dùng chung fetch **bắt đầu sau** khi nó đến; cache read thường giữ 2 s như cũ. `prepare_git` của writer đánh dấu đã đồng bộ ⇒ read chờ sau write không fetch lại.
- Refresh + chờ writer diễn ra **ngoài** slot admission (không giữ khoá nào khi chờ slot ⇒ không vòng khoá); admission chờ có hạn 5 s thay vì từ chối ngay. Không retry lượt ghi.
- Bỏ nạp kho BM25 lúc boot; listener PG→Qdrant một leader/container (flock).
- Cấu hình theo số đo: 6 worker uvicorn (`AGENT_DATA_WORKERS`), `direct_concurrency` 4→12, `lock_wait_seconds` 5→10 (phủ p95 write; xếp hàng sau một lượt ghi không còn thành lỗi). Không thêm URL/port/route.
- Log `workspace_call … code=<mã lỗi>` để phân loại A–D (mục 5).
- HVU (theo P35 + D): *Vừa làm 1* = actor gateway commit mới nhất; *Vừa làm 2* = actor **khác** gần nhất, tính thẳng từ `git log` mỗi lượt sync (bỏ đệm snapshot). *Đang làm*: mọi hoạt động đã hiện giữ tối thiểu **60 s** (HOLD) kể cả khi commit xoá; commit Git là bằng chứng cho lượt ghi ngắn bị lỡ mẫu; không hồi sinh actor cũ, vẫn latest-only, TTL 10 phút giữ nguyên.

**3. BEFORE → AFTER** (bench thật trên production qua HTTP `/mcp-gpt-full`, chứng tích `bench/`)

| Kịch bản | Trước (2 worker, 4 slot) | Sau |
|---|---|---|
| 1 read cold | 1,66 s | 1,70 s |
| 8 read stale cùng root | **5/8 lỗi**, p50 1,76 · p95 5,67 · 3 fetch | 0 lỗi · p50 2,12 · p95 2,19 · 1 fetch |
| 8 read fresh | 2/8 OVERLOADED | 0 · p50 0,27 · p95 0,39 |
| 12 / 15 read stale | **8/12**, **12/15** lỗi | 0 / 0 · p95 2,85 / 2,64 · 1 fetch |
| 8 stat (safety) | 5/8 lỗi, bậc thang 1,9→5,9 s | 0 · p95 2,63 |
| 15 search | — | 0 lỗi · p50 3,7 · p95 5,5 (giới hạn CPU/GIL) |
| 6 read + 1 write | 2 OVERLOADED (6 read) | 0 lỗi · write 6,7 s `9db01fd` · edit version cũ → `VERSION_CONFLICT` ✔ |
| 8 read 4 root | 3/8 OVERLOADED | 0 · p50 0,43 |
| Cold start → initialize+tools/list | ~106 s (1 worker chết NLTK) | **15,1 s**, 0 crash |
| RAM container · load | 1,9 GiB · ~4,0 | 1,96 GiB (6 worker) · 3,9–4,6 |

Actor/presence: Task view thật `mcp-workspace` hiện *Vừa làm 1* Claude Code · *Vừa làm 2* Claude Chat (mã cũ sẽ là Claude Code ×2); lượt ghi ngắn 3,8 s hiện *Đang làm* qua 4 lượt publish rồi tự trống sau ~66 s.

**4. TEST** — A Backend **PASS** (8/12/15-way 0 OVERLOADED/BUSY, 1 fetch/burst, version guard, không deadlock) · B Cold/warm **PASS** · C Attribution **PASS** (test A,B,B + nhiều commit/1 sync; live) · D Presence **PASS** (test timeline HOLD/không hồi sinh/TTL; live) · E Không hồi quy **PASS**: 37 tool, hash không đổi, sai khoá → 401, read/search/edit/log/diff/transaction thật; agent-data 170 test + HVU 24 test xanh; drift-check 34/34 CLEAN; cổng `fs_*` = chính commit báo cáo này.

**5. PHẦN THUỘC CHATGPT CLIENT (máy chủ không kiểm soát) — ma trận H chờ Owner/GPT, Claude không tự chấm**
- Bằng chứng hiện có: ChatGPT không gọi `initialize`/`tools/list` khi mở chat; nếu một phiên “không vào được” mà VPS không nhận request nào thì đó là **A · ChatGPT không invoke app** (chọn app theo từng message), không sửa được từ backend.
- Chạy: chat thường phiên đang mở · chat thường phiên mới · Pro phiên mới; mỗi ca 1 `workspace_list` nhỏ rồi 3–5 read/search; ghi giờ phút.
- Phân loại bằng log (không lộ nội dung): `ssh contabo 'docker logs --timestamps --since 30m incomex-nginx | grep remote_addr=9.129'` (không có dòng ⇒ **A**) · `ssh contabo 'docker logs --timestamps --since 30m incomex-agent-data | grep -E "MCP-GPT-FULL|workspace_call"'` (initialize/tools/list lỗi ⇒ **B**; `code=WORKSPACE_BUSY|OVERLOADED` ⇒ **C**; `status=ok` ⇒ **D**).

**Còn lại (không chặn):** 15 search đồng thời 3–5 s do CPU; writer giữ khoá root suốt fetch+push (3,7–6,7 s); `VERSION_CONFLICT` do version gắn HEAD toàn repo (50 lần trong metrics) là hành vi an toàn có chủ đích, không đổi ở lượt này. Sửa tệp cấu hình bind-mount phải ghi **tại chỗ** (thay inode thì container không thấy tới lần restart). Founders cần sửa một câu AGENTS A9 (“commit clear Đang làm”) thành “clear sau HOLD 60 s”; legend UI “Vừa làm 2: lần trước đó” → “AI khác gần nhất” để Host HVU làm (`app.vue` đang có thay đổi chưa commit của phiên khác, Claude không đụng).

### MCPW-STAB-20260924 · FINAL
**Kết luận: `FINAL PARTIAL` — chỉ B chưa đạt trọn** (12-way đạt khi GitHub bình thường; khi GitHub tra khoá deploy >10 s thì read đồng thời trả BUSY). A C D E F G H J PASS · I BLOCKED đúng điều kiện. Giữ nguyên toàn bộ phần đã PASS (6 worker, `direct_concurrency` 12, single-flight, admission chờ có hạn, 37 tool, hash, auth/operation_id/version guard, HOLD 60 s, Vừa làm 1/2). MCPW-LOCK không chạy.
- **Delta runtime (một lần restart 15:31:37Z):** agent-data-repo `8338214` = telemetry startup (`startup_phase pid= phase= phase_s= process_age_s=`, không log dữ liệu/secret) + bật INFO cho logger listener (trước đó bị nuốt ở WARNING: không thấy leader/LISTENING/op) · `bdea3c3` = 2 regression test · image `agent-data-hvu:mcpw-stab-20260924-final` (overlay 2 file lên `mcpw-stab-20260924`, CMD/env giữ nguyên). Hồ sơ: `/opt/incomex/work/mcp-workspace/MCPW-STAB-20260924/` (`deploy-final.sh`, `Dockerfile.final`, `bench/final-restart/`).
- **A · PASS** — `run_acceptance.py` release gate qua route PUBLIC: 37 tool, `dbbfc590a969`, server 1.3.0, schema version không đổi, 11/11 capability ok; sai khoá → 401.
- **B · CHƯA ĐẠT TRỌN** — lượt 1 (15:33:47Z): 1/12 ok, **11 `WORKSPACE_BUSY`** ở ~10,4 s. Gốc (trace `ssh -v`): TCP+KEX tới GitHub 0,7 s, nhưng **bước GitHub tra khoá deploy** (“Offering public key” → “Server accepts key”) 0,04 s / 2,8 s / 15 s rồi `Permission denied`; githubstatus xanh; không có lượt ghi nào khác ⇒ chính lượt `git fetch` single-flight kéo 14,3 s > `lock_wait_seconds` 10 ⇒ mọi người chờ nhận BUSY dù fetch sau đó thành công. GitHub hồi phục (16/16 ls-remote 1,3–2,9 s, 15:39–15:44Z), lượt 2 (15:45:16Z): **12/12 ok**, p50 2,57 s, max 3,08 s; read đơn 0,11 s; search 2,97 s; metrics delta BUSY/OVERLOADED = 0. Không đổi mã giữa hai lượt.
- **C · PASS** — canary `mcpw-canary-20260924T153259Z-ccc872`, đúng MỘT `pg_notify('kb_vector_sync', {op: MCPW_VERIFY_NOOP,…})`: log có canary **1 lần** + 1 dòng `unknown op: MCPW_VERIFY_NOOP`; 0 dòng upsert/delete; Qdrant `production_documents` 20.187 điểm trước = sau; không tạo row/document.
- **D · PASS** — `tests/test_vector_sync.py::test_pg_listener_single_leader_and_failover_across_six_workers`: chạy `_listen_loop` THẬT trong 6 process fork chung một lock path (giả `psycopg2.connect` + handler): đúng 1 LISTEN, chỉ leader xử lý sự kiện, SIGKILL leader 2 lần ⇒ mỗi lần đúng 1 follower tiếp quản, LISTEN mới luôn sau thời điểm kill. 5/5 lượt xanh; bỏ flock (mutant) ⇒ FAIL `6 == 1`.
- **E · PASS** — `tests/test_agent_data_main.py::test_startup_does_not_bulk_load_collection_for_lexical_index`: dựng `AgentData` với vecdb có gắn (như server lúc import), đếm `vecdb.get_all_documents` + `DocChatAgent.setup_documents` = 0; điều kiện cũ (`… and self.vecdb is None`) ⇒ FAIL. Không phụ thuộc số chunk.
- **F · PASS** — container start → `initialize`+`tools/list` dùng được **18,4 s** (Codex đo 19–21 s); 6/6 worker ready trong 16,6–19,8 s tuổi process; phase: import module ~11,5 s · AgentData init 3,9–5,9 s · probe+listener 0,3 s · task supervisor 0,1–1,2 s. Healthy ở +23,5 s ⇒ không báo healthy trước khi MCP phục vụ được (healthcheck `/info` chỉ trả khi một worker đã xong startup) ⇒ không sửa readiness. Restart 0, 0 worker chết, RAM 1,94 GiB/6 GiB, load ~3,8.
- **G · PASS** — sau restart đúng 1 phiên `LISTEN kb_vector_sync` (backend 15:31:55Z), log `leader lock acquired by pid 19` + một `LISTENING`.
- **H · PASS** — HVU `test_b3` + `test_sync` 24/24 OK; `sync.py`/`presence.py` không đổi.
- **I · BLOCKED** — `nuxt-repo/scripts/hvu-b2/ui/app.vue` vẫn có thay đổi chưa commit của phiên khác (33 dòng, từ 06:41 CEST) ⇒ không đụng; nhãn vẫn “Vừa làm 2: lần trước đó”.
- **J · PASS** — `rollback-final.sh` (chỉ gỡ delta lượt này → `mcpw-stab-20260924`) và `rollback.sh` (toàn bộ → `hjw2c-g1`, nay nhận cả tag `-final`) chạy thử khô trên bản sao compose đúng kết quả; cả 3 image còn trong máy.
- **Test:** continuation 171/171 (image mới); toàn bộ `tests/` (trừ e2e/smoke, không mạng) 69 failed/358 passed = đúng tập FAIL có sẵn của baseline (356 passed) + 2 test mới; config-guard 34/34 CLEAN.

## Owner cần quyết
- MCPW-STAB B: khi GitHub tra khoá deploy chậm >10 s (đo được hôm nay 15 s), read đồng thời chờ refresh nhận `WORKSPACE_BUSY` dù bản local vẫn đọc được. (a) Chấp nhận như hiện tại — lỗi báo rõ, client thử lại; (b) mở việc riêng: read chờ refresh quá hạn thì trả bản last-good kèm cờ `stale` (đổi ngữ nghĩa freshness — cần duyệt). Backend còn lại coi như xong.
