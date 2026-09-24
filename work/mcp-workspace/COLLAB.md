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
MCPW-LOCK | PROMPT `MCPW-LOCK-20260924-01` soạn xong · Host READY ở commit kế tiếp | Executor_Surface: Claude Code CLI trên Mac · Write_Path báo cáo `fs_*` | T3 (`workspace_*`) Host tự thử nếu agent không bind.

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
