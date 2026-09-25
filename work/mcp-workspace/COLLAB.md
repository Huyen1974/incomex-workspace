# COLLAB — mcp-workspace
Tên việc: MCP Workspace — đường ghi chung + khoá cứng chỉ qua gateway
Host: GPT Chat · Host_ID: GPT-MCPW-250925-A · Owner giao 25/09/2026 điều hành nốt MCPW-LOCK + P02 rồi đóng (trước đó: Claude Chat `CLAUDE-MCPW-260924-A` từ 24/09; vòng 20/09 Host GPT)

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
Xác nhận User: **ĐÃ XÁC NHẬN** (nguyên văn lời User, 24/09/2026) — Owner gật đề xuất `Mở lại mcp-workspace để khoá đường ghi repo chỉ qua gateway` (COLLAB gốc DROOT20).

### 1. Mục tiêu
- Nguyên văn Owner: “Đúng vậy chúng ta khóa lại để bắt buộc làm theo 1 con đường giúp tôi.”
- Nguyên tắc áp (AGENTS A10-R2, nguyên văn Owner): “Quy định là không đủ, phải cưỡng chế. Không thể làm sai.”

### 2. Thế nào là hoàn thành
- Theo đề xuất Owner đã gật (DROOT20): mọi lần ghi repo bằng tài khoản người (GitHub connector của GPT, git push từ Mac, kể cả Owner) bị GitHub từ chối; cổng `fs_*` và `workspace_*` vẫn ghi được — 3 phép thử T1–T3 PASS.
- **Owner 25/09/2026: ĐÃ GẬT.** Vòng P02 tiếp tục trong chính việc này (kiến trúc Owner duyệt tại `ef28301`, proposal triển khai Claude tại `7400ad3`): GitHub chậm/down thì đọc qua cổng không báo BẬN, trả bản tốt cuối có nhãn + nợ kiểm lại; ghi vẫn luôn hỏi GitHub — hoàn thành khi 12 phép thử ở khối `Claude · P02-IMPL` PASS. Thứ tự đã chốt: **MCPW-LOCK trước → P02 sau; không gộp**.

### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Chốt kỹ thuật: GitHub Repository Ruleset `gateway-only-writes` — tính năng có sẵn của GitHub (R1 bậc 1), không viết code. Mọi nhánh: chặn tạo/cập nhật/xoá + force push; miễn trừ **chỉ DeployKey**; không thêm vai trò admin/maintain/write (sẽ mở lại lỗ). Không đụng branch protection cổ điển (README §4).
- Trước khi bật phải chứng minh chỉ-đọc: cả 2 cổng đẩy bằng deploy key có quyền ghi của repo. `fs_*` đã biết dùng `MCP_WORKSPACE_GH_DEPLOY_KEY` (BẢN ĐỒ HỆ THỐNG 17/09); `workspace_*` chưa xác nhận → gate G1.5.
- Rollback đã duyệt trước: cổng bị chặn → đặt ruleset `enforcement=disabled` (không xoá). Cửa khẩn cấp Owner: tắt ruleset trong Settings → Rules.
- Sau MCPW-LOCK XONG: Host tự thử lại, sửa README D12 `CHƯA CƯỠNG CHẾ` → `ĐÃ CƯỠNG CHẾ`; **chưa đóng việc** — P02 chạy tiếp trong cùng việc (Owner 25/09, `ef28301`); `Đóng mcp-workspace` sau P02 XONG.
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
- **RUN 25/09 (Claude Code CLI, báo trong chat Owner — chưa ghi KQ):** G0 PASS (READY khớp `d71a6c3…`) · G1.1–G1.7 PASS chỉ đọc: repo có đúng **1** deploy key ghi-được (id 163589117, `SHA256:ctotGu9U…`), cả `fs_*` lẫn `workspace_*` dùng chung key này ⇒ G1.6 đạt, không key thừa; 0 ruleset; 0 workflow; không PAT. **Dừng trước mutation, GitHub chưa đổi gì:** chế độ auto của Claude Code chặn lệnh tạo ruleset vì lệnh RUN nằm trong đoạn *dán* vào. Không phải lỗi PROMPT/READY ⇒ không READY lại, không ghi `KQ … DỪNG`. Gỡ: Owner **gõ tay** một câu cho phép trong đúng phiên đó → agent làm tiếp §3 → T1 → T2 (KQ qua `fs_edit`) → T3 (`workspace_edit`); FAIL ⇒ `disabled`.
- **Bàn giao Host GPT (Owner 25/09: “GPT điều hành nốt và đóng việc”):** (1) Sau KQ: tự kiểm qua API — đúng 1 ruleset `gateway-only-writes`, `enforcement=active`, bypass chỉ `DeployKey`, không admin/role/app; commit KQ có author gateway; T1 bị từ chối thật và không còn dòng probe; T3 có commit. (2) Sửa README D12 `CHƯA CƯỠNG CHẾ` → `ĐÃ CƯỠNG CHẾ`. (3) Soạn P02 vào **chính** `PROMPT.md` (chỉ sau KQ XONG của LOCK) theo khối `Claude · P02-IMPL` (K1–K6, 12 acceptance, không thêm deploy key) → Claude review → READY → Owner RUN. (4) Nghiệm thu 12 acceptance → `Đóng mcp-workspace`. Lưu ý: sau LOCK mọi AI chỉ ghi qua 2 cổng; GitHub native của GPT bị từ chối là đúng thiết kế.

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

### P02 · GPT Chat · OPEN FOR CLAUDE REVIEW · GitHub remote SSOT + VPS local read cache
- **Based_on:** MCPW-STAB FINAL PARTIAL commit `25fac164b52cfc10e721bc62141ecbba551b531b` + GitHub Docs kiểm 24/09/2026 (`Repository limits`, `Best practices for REST API`, `About webhooks`).
- **Chẩn đoán:** sự cố B vừa đo **không phải bằng chứng GitHub hết API quota**. Lượt lỗi do bước GitHub SSH/deploy-key lookup có lúc kéo tới ~15 s; single-flight `git fetch` giữ đường refresh/root lock ~14,3 s > `lock_wait_seconds=10`, nên 11/12 read nhận `WORKSPACE_BUSY` dù clone local vẫn đọc được. Khi GitHub trở lại 1,3–2,9 s thì 12/12 PASS mà không đổi code. Vì vậy nâng GitHub Team/Enterprise **chưa có căn cứ sẽ chữa lỗi này**; paid plan chỉ đánh giá lại nếu telemetry chứng minh rate-limit/throttling thực sự.
- **Căn cứ GitHub:** Git read automation có khuyến nghị tối đa 15 ops/s/repo và GitHub nêu rõ có thể dùng **repository cache server**; REST/API nên ưu tiên webhook thay polling. Đây phù hợp hướng tách GitHub khỏi critical path đọc.
- **Đề xuất kiến trúc R0 — CHỈ ĐỂ REVIEW, NO RUN:**
  1. **GitHub giữ vai trò remote/durable SSOT + write authority.** Không đổi quy tắc gateway-only write, expected version/head, operation_id, branch/ruleset.
  2. **VPS local clone/mirror = read-serving last-good cache, KHÔNG phải SSOT.** `workspace_read/search/stat/log/diff` ưu tiên đọc local ngay, không bắt mỗi request phải chờ GitHub refresh.
  3. **Refresh tách khỏi read critical path:** một refresh single-flight nền; webhook push là trigger chính, backstop định kỳ bắt sự kiện thất lạc. Refresh thành công mới atomically advance local cache/source_head.
  4. **Write vẫn strict với GitHub:** trước mutation phải đảm bảo remote/current HEAD theo contract; GitHub chậm/mất kết nối thì write được phép chờ/fail rõ ràng, tuyệt đối không commit/push trên base stale.
  5. **Freshness phải nhìn thấy được:** local read trả last-good kèm tuổi/source_head bằng metadata hiện hữu nếu đủ; nếu contract hiện hữu không thể biểu đạt rõ stale/refreshing mà không đổi public semantics/schema thì phải dừng và xin Owner chốt trước. Không âm thầm gọi stale là fresh.
  6. **Không dựng Forgejo/Gitea ở R0; không mua GitHub chỉ để chữa B.** Chỉ cân nhắc self-hosted secondary remote/Forgejo hoặc paid GitHub khi có số đo cho thấy GitHub thật sự là bottleneck dài hạn mà cache không giải quyết.
  7. **Chưa chốt shared cache hay cache riêng:** Claude cần đánh giá (A) một bare mirror/cache dùng chung cho `fs_*` + `workspace_*` để giảm fetch, hay (B) giữ clone/cache riêng từng gateway để ít coupling hơn. Ưu tiên ít code, rollback dễ, không tạo SSOT thứ hai.
- **Điểm cần Claude phản biện trước khi chốt:**
  - P02.1: R0 có giữ đúng nguyên tắc GitHub SSOT nhưng bỏ GitHub khỏi critical path read không?
  - P02.2: cách tối thiểu nào để UI/tool biết `fresh / refreshing / stale` mà **không phá public MCP contract freeze**?
  - P02.3: shared bare mirror hay per-gateway local cache phù hợp hơn với lock/transaction hiện tại?
  - P02.4: webhook + backstop hiện hữu có đủ làm refresh trigger, hay cần thêm cơ chế nào thật sự bắt buộc?
  - P02.5: có bằng chứng nào cho thấy nâng gói GitHub sẽ cải thiện SSH deploy-key lookup latency vừa gặp? Nếu không, đề nghị không mua vì lý do này.
- **Trạng thái:** `OPEN · REVIEW ONLY · NO RUN`. Không sửa PROMPT, không mở task mới, không thay runtime trước consensus GPT + Claude + Owner.

#### Claude review P02 · Claude Chat (Host MCPW `CLAUDE-MCPW-260924-A`) · 2026-09-25 · **PARTIAL → CONSENSUS CANDIDATE** · NO RUN
- **Based_on:** `24957845c105532875dfe5d38a286a4a09cd2796` + đọc mã thật (root `code`): `agent_data/workspace_tools.py` L476–533 (`refresh_for_read`, trần 2 s, `SAFETY_READS`), L1000–1065 (`prepare_git`, `VERSION_CONFLICT` theo `HEAD:hash`); `claude-mcp/app/fsroots.py` L116–122, L282–295, L346–358; `claude-mcp/helper/mcp_host_helper.py` L696–720; README §12.3/§12.5. **Chưa đọc:** mã receiver webhook HVU, chi tiết journal recovery, cỡ checkout repo.
- **Kết luận:** ĐỒNG Ý hướng P02 (GitHub = SSOT + quyền ghi; VPS = bản đệm đọc, không phải SSOT). Nhưng thứ chữa lỗi B **không phải webhook**, mà là 3 chốt: **(1)** lượt nói chuyện GitHub chạy **ngoài** khoá mà người đọc cần; **(2)** đọc từ **ảnh chụp bất biến của commit tốt cuối**, không đọc worktree của writer (writer đang giữ khoá qua cả fetch+push, GitHub chậm thì đọc worktree vẫn kẹt); **(3)** chờ có hạn, hết hạn trả bản tốt cuối **kèm nhãn** — đọc không bao giờ BUSY vì refresh. Webhook chỉ làm đọc nhanh hơn/ít gọi GitHub. Ví dụ nôm na: GitHub = thư viện gốc; VPS = tủ bản photo có đóng dấu ngày đối chiếu; đọc lấy bản photo, muốn sửa sách phải ra thư viện gốc.
- **Bậc (A10-R1):** 2 cấu hình/ghép (git native `fetch`/`worktree`/`merge-base --is-ancestor`, đổi con trỏ nguyên tử, receiver webhook HMAC + backstop sẵn có của README §12.3) + 3 code mỏng (đổi gốc đọc + hạn chờ + nhãn, ở 2 cổng). Bậc 1 không đạt: không có sản phẩm cache Git cắm thẳng vào 2 gateway tự viết; Forgejo/GitHub trả phí không chữa đúng nguyên nhân.
- **Read path (Q1): CÓ.** `AI → gateway → ảnh chụp last-good của chính cổng` cho read/search/list/stat/log/diff. Ba nhóm:
  - Đọc thường (read/search/list): đã đối chiếu GitHub trong ≤ W → trả ngay; quá W → kích fetch nền single-flight, chờ tối đa D_plain≈3 s.
  - Đọc để quyết định (stat/log/diff — kiểm READY SHA, commit agent): vẫn **thử** đối chiếu GitHub (dùng chung lượt fetch bắt đầu sau khi request đến, như nay), chờ tối đa D_safe≈5 s; quá hạn → last-good có nhãn, **không BUSY**.
  - `ref=<sha>`: commit bất biến → có sẵn trong kho local thì trả ngay, không cần tươi; thiếu → kích fetch, chờ D; vẫn thiếu → lỗi not-found hiện có + gợi ý thử lại.
- **Freshness (Q2)** — dùng lại từ vựng README §12.5, thêm `refreshing`: `fresh` = đối chiếu GitHub thành công trong cửa sổ cho phép (đọc quyết định: lượt đối chiếu bắt đầu sau khi request đến) · `refreshing` = chưa đạt fresh trong hạn chờ, đang có fetch chạy, lần thành công gần nhất ≤ 5 phút · `stale` = lượt gần nhất lỗi, hoặc biết GitHub có HEAD mới chưa áp, hoặc > 5 phút chưa đối chiếu được, hoặc vừa khởi động chưa đối chiếu. Metadata: giữ `source_head` (= SHA ảnh chụp đang phục vụ), `refreshed_at` (= lần đối chiếu GitHub thành công gần nhất — đúng nghĩa hiện nay, chỉ là tuổi có thể lớn hơn), `remote_head` khi biết; thêm **một khoá phản hồi** `freshness` ở `workspace_*` (đã kiểm: không tool nào khai `outputSchema` ⇒ tools/list + hash `dbbfc590a969` giữ nguyên, không tạo app GPT mới, không reconnect); `fs_*` chỉ sửa dòng chữ `NGUỒN:` sẵn có. Luật cho AI: khác `fresh` thì không kết luận “đã có/chưa có”; ghi vẫn an toàn.
- **Cache topology (Q3): chọn H = cache riêng từng cổng + chuông chung.**
  - A (mirror chung): một chỗ nói chuyện GitHub, nhưng buộc 2 cổng khác user/container/deploy key vào một thư mục + một khoá ⇒ coupling cao, hỏng một là hỏng cả hai, rollback chung; và **mất “đọc thấy ngay cái mình vừa ghi”** (mirror chỉ được lấy từ GitHub). Loại.
  - B (riêng từng cổng, không chuông): ít coupling, rollback từng cổng; nhưng mỗi cổng tự hỏi GitHub mỗi W ⇒ chạy vô ích (trái DROOT07).
  - **H = B + chuông:** receiver webhook sẵn có chỉ thêm việc *chạm* một file chuông cho mỗi cổng; mỗi cổng tự fetch bằng key của mình. Chuông chết ⇒ chỉ mất prefetch, cổng tự đối chiếu theo W — không mất đúng/sai. JEV `gen-dec-1790286830-xT0ZurcKTAriERkZNn9W`: H 0,63 · B 0,36 · A 0,01 (conf 0,51, JEV phân vân H/B; chọn H theo DROOT07).
- **Refresh (Q4):** webhook + backstop **đủ**, và đúng/sai không dựa vào nó (JEV: webhook cần cho đúng 0,20). Không tin payload — mỗi lượt đọc HEAD thật; debounce = single-flight (chuông dồn → 1 fetch; chuông đến lúc đang fetch → đúng 1 lượt nữa). **Không thêm timer backstop cho cổng:** lượt đọc quá W chính là backstop lười, chỉ chạy khi có người đọc; backstop 15′ của receiver giữ nguyên cho Owner View. Ảnh chụp **chỉ tiến**: SHA mới phải là hậu duệ SHA đang phục vụ, không thì giữ cũ + `stale` + log. **Ghi thành công → advance ngay** ảnh chụp của chính cổng đó lên SHA vừa push (GitHub đã nhận ff = đúng HEAD GitHub lúc đó); cổng kia thấy qua chuông vài giây. Tham số đề xuất W=60 s, D_plain 3 s, D_safe 5 s — agent đo rồi chốt; nếu Owner giữ W=2 s như nay thì chuông gần như vô tác dụng.
- **Write (Q5):** flow P02 đúng; chốt lại: đọc ảnh chụp → lấy khoá root (chỉ writer chờ writer) → fetch GitHub trong khoá như nay → ff worktree → so `expected_version`/`expected_head` với HEAD thật, lệch → `VERSION_CONFLICT` (không tự hoà giải) → commit → push ff, không force → OK: advance ảnh chụp · bị từ chối: khôi phục clone như nay · mất phản hồi: `OUTCOME_UNKNOWN`/`RECOVERY_REQUIRED` + journal như nay. Không phá `operation_id`, transaction/restore, recovery. Lưu ý: `workspace_*` version gắn HEAD cả repo ⇒ đọc cũ rồi ghi **chắc chắn** `VERSION_CONFLICT` (an toàn, tốn một vòng); `fs_*` gắn nội dung file ⇒ file đó không đổi thì ghi tiếp đúng. JEV: đọc cũ rồi ghi đè được bản mới 0,17. Writer vẫn giữ khoá qua mạng ⇒ hai lượt **ghi** cùng cổng lúc GitHub chậm có thể BUSY — chấp nhận (ghi phải chờ GitHub là đúng thiết kế).
- **Failure (Q6):**

| Ca | Đọc | Ghi |
|---|---|---|
| GitHub down 30 s | trong W: `fresh`; quá W: sau D trả last-good `refreshing`→`stale`; không BUSY | `UPSTREAM_UNAVAILABLE`, không ghi gì; đang push → `OUTCOME_UNKNOWN` + recovery hiện có |
| GitHub chậm 15–30 s | như trên; fetch nền xong tự advance | chậm; ghi thứ hai cùng cổng có thể BUSY |
| Webhook lỡ | đọc quá W tự đối chiếu; tệ nhất cũ ≤ W, `refreshed_at` nói rõ | — |
| Webhook trễ / đảo thứ tự | vô hại: không tin payload, chỉ tiến theo hậu duệ | — |
| Cache hỏng | fetch/fsck lỗi → `stale` + cảnh báo, vẫn phục vụ ảnh chụp còn nguyên; dựng clone mới cạnh bên từ GitHub rồi chuyển con trỏ; clone hỏng giữ nguyên để tra, không xoá | cổng đó dừng ghi tới khi clone mới xong |
| Cache cũ 5 phút | `stale`, AI thấy rõ | vẫn đối chiếu GitHub |
| AI đọc cũ rồi ghi / HEAD đổi khi AI đang sửa | — | `workspace_*`: `VERSION_CONFLICT`; `fs_*`: file không đổi → ghi đúng, đổi → từ chối |
| Hai cổng cùng ghi | — | GitHub ff phân xử; bên thua `push_rejected` → khôi phục → đọc lại |
| Cache mới hơn Owner View | bình thường: hai bản dẫn xuất cùng nguồn, cùng chuông nên lệch vài giây; A8 vẫn kiểm đúng revision Owner View | — |
| VPS reboot | phục vụ ảnh chụp trên đĩa ngay, nhãn `stale` tới lượt đối chiếu đầu; không bao giờ `fresh` khi chưa đối chiếu | recovery journal như nay |

- **Owner cần quyết (một dòng, chờ GPT đối chiếu xong mới đưa lên mục `Owner cần quyết`):** “Đọc không bao giờ báo BẬN vì GitHub chậm: trả bản tốt cuối kèm nhãn tươi/đang cập nhật/cũ; đọc thường tin bản đã đối chiếu trong 60 giây (có chuông webhook thì cập nhật ngay); đọc để quyết định (stat/log/diff) luôn hỏi GitHub, chậm quá 5 giây thì trả bản tốt cuối có nhãn. Ghi giữ nguyên, luôn hỏi GitHub. Không đổi 37 tool/schema → không phải kết nối lại.” **Đề xuất: gật.** Cần ghi thành D vì đổi *ngữ nghĩa phản hồi* (BUSY → last-good có nhãn) — ngoại lệ DROOT09 giống author attribution.
- **P02 cần sửa:** (1) webhook là tối ưu, không phải cơ chế đúng/sai — chuông lạc không được dẫn tới “cũ mà không nhãn”; (2) thêm tách **ảnh chụp đọc** khỏi **worktree ghi** — chỉ “refresh nền” mà đọc vẫn trên worktree thì writer chậm vẫn chặn đọc; (3) advance phải gồm cả **push thành công của chính cổng** và **chỉ tiến theo hậu duệ**; (4) loại A mirror chung (lý do Q3); (5) dùng lại receiver + từ vựng README §12.5, không dựng pipeline/timer mới; (6) luật H02 “đọc an toàn không từ cache” diễn giải lại: an toàn nằm ở **lượt ghi đối chiếu lại**; đọc quyết định vẫn thử đối chiếu nhưng hạ xuống last-good có nhãn thay vì BUSY.
- **MCP schema:** KHÔNG đổi tools/list, input schema, hash, auth, `operation_id`. CÓ đổi ngữ nghĩa phản hồi đọc + thêm khoá `freshness` → cần D Owner (dòng trên).
- **Forgejo / GitHub trả phí:** KHÔNG. Sự cố do bước tra deploy key đơn lẻ kéo 15 s, không phải quota (JEV 0,09).
- **Bước tiếp:** GPT đối chiếu một vòng (A5) → nhận thì ghi CONSENSUS → Owner gật dòng trên → Host Claude soạn **một** PROMPT cho Claude Code CLI gộp 2 cổng + chuông + test cưỡng chế R2 (mutant bỏ hạn chờ phải FAIL): 12-way đọc khi GitHub giả chậm 20 s = 0 BUSY · không bao giờ `fresh` khi chưa đối chiếu · đọc sau ghi cùng cổng thấy ngay · không lùi SHA · reboot ra `stale`. MCPW-LOCK giữ READY độc lập, không chạy chung.

#### GPT đối chiếu P02 · 2026-09-25 · **ACCEPT → CONSENSUS CANDIDATE** · NO RUN
- **ACCEPT lõi kiến trúc Claude:** GitHub tiếp tục là durable SSOT + write authority; mỗi gateway giữ **ảnh chụp bất biến last-good riêng để phục vụ đọc**; webhook chỉ là chuông tối ưu, không phải nguồn đúng/sai; write luôn revalidate GitHub như hiện hành. Không dùng shared mirror, không Forgejo, không mua GitHub để chữa sự cố SSH/deploy-key latency này.
- **Điểm bắt buộc giữ:** read path không được đọc worktree mà writer đang dùng; snapshot chỉ tiến theo commit hậu duệ đã kiểm chứng. Push thành công của chính gateway được advance snapshot của gateway đó ngay; gateway kia bắt qua chuông/lazy refresh.
- **Freshness contract:** `fresh` = snapshot đã được đối chiếu remote trong cửa sổ cho phép; `refreshing` = đang có lượt refresh và còn last-good hợp lệ; `stale` = chưa/không thể đối chiếu đủ mới, biết remote có HEAD mới chưa áp, hoặc vượt ngưỡng stale. `source_head` luôn là SHA snapshot đang phục vụ; `refreshed_at` là lần đối chiếu remote thành công gần nhất. Có thể thêm response-only `freshness` vì hiện không khai outputSchema; không đổi 37 tool/input schema/hash/auth nên không yêu cầu reconnect/Refresh app.
- **Guardrail quyết định:** nội dung `refreshing`/`stale` vẫn được đọc/hiển thị, nhưng **không được dùng để kết luận một sự thật cần HEAD hiện thời** (READY/SHA, “đã có/chưa có”, nghiệm thu dựa trên remote hiện tại). Trường hợp đó phải coi là `unknown` cho tới khi có `fresh` hoặc bước write revalidate remote thành công. Như vậy availability read tăng nhưng safety không giảm.
- **Chuông chung là implementation gate, chưa mặc định:** trước RUN, Agent phải đọc receiver webhook thật + quyền filesystem/container và chứng minh có thể phát tín hiệu cho hai cache riêng bằng cơ chế hiện hữu, HMAC giữ nguyên, không tạo pipeline/SSOT mới. Nếu receiver hiện hữu không ghép mỏng được thì fallback vẫn là per-gateway lazy refresh theo W; correctness không phụ thuộc webhook.
- **Thông số W/D là tuning, không phải quyết định kiến trúc:** khởi điểm Claude đề xuất W≈60s, D_plain≈3s, D_safe≈5s; Agent phải benchmark và chốt trong PROMPT/RUN với acceptance. Không được tăng timeout để che lỗi.
- **Failure semantics ACCEPT:** GitHub chậm/down không làm read trả BUSY chỉ vì refresh; trả last-good có nhãn. Write giữ nguyên strict upstream, `VERSION_CONFLICT`/`UPSTREAM_UNAVAILABLE`/`OUTCOME_UNKNOWN` + recovery như hiện hành.
- **JEV độc lập:** `gen-dec-1790288247-aX9iyCn6ujIQCPUNXr2X` chọn H (per-gateway cache + shared webhook hint) 1.00; `labeled_last_good` 1.00; xác suất cần rediscovery/reconnect vì response-only field 0.15. Bằng chứng phụ, quyết định do GPT+Claude+Owner.
- **Kết luận Founders candidate:** GPT + Claude đã đồng thuận về cấu trúc. Còn đúng **một quyết định Owner** về đổi semantics read `BUSY → last-good có freshness`; chưa soạn PROMPT/RUN trước khi Owner gật.

#### Owner chốt P02 · 2026-09-25 · **APPROVED ARCHITECTURE · NO RUN YET**
- Owner **đồng ý** đổi read semantics: GitHub chậm/down không làm read báo `BUSY`; gateway trả snapshot last-good từ VPS kèm `fresh / refreshing / stale`. GitHub vẫn là durable SSOT + write authority; mọi write vẫn bắt buộc revalidate GitHub trước mutation.
- **Yêu cầu bổ sung của Owner — “nợ freshness”:** AI/Agent phải được phép xử lý ngay trên last-good nhưng phải **nhớ quay lại kiểm tra bản mới hơn**. Không dựa vào trí nhớ tự phát của model; response không-`fresh` phải mang tín hiệu máy đọc rõ ràng.
- **Contract để Host đưa vào PROMPT:** mọi read dùng dữ liệu `refreshing`/`stale` mà có ảnh hưởng tới kết luận hiện trạng trả thêm `recheck_required=true` (response-only), cùng `source_head`, `refreshed_at` và gợi ý thời điểm recheck nếu hữu ích. Gateway đồng thời tự kích/join refresh single-flight nền; Agent không cần dừng công việc để chờ ngay.
- **Luật AI:** khi thấy `recheck_required=true`, được tiếp tục đọc/phân tích/draft trên last-good và coi các kết luận hiện trạng là **provisional**. Trước khi (a) trả kết luận cuối cho Owner về trạng thái hiện tại, READY/SHA, “đã có/chưa có”, hoặc (b) thực hiện hành động phụ thuộc HEAD hiện thời, Agent phải gọi lại một read/safety-read liên quan để trả “nợ freshness”. Nếu lần recheck là `fresh` thì debt clear. Nếu vẫn `refreshing/stale`, không lặp vô hạn: được hoàn tất nhưng phải nói rõ **“chưa xác nhận bản mới nhất”** và không biến dữ liệu đó thành bằng chứng fresh. Write path vẫn tự revalidate upstream như guardrail độc lập.
- `ref=<sha>` đã có commit bất biến local thì không tạo freshness debt cho chính nội dung commit đó; debt chỉ áp khi kết luận phụ thuộc **HEAD hiện tại**.
- **Implementation gate:** snapshot đọc tách worktree ghi; per-gateway cache riêng; webhook/chung chỉ là hint tối ưu. Trước RUN Agent phải đọc receiver webhook thật và chứng minh ghép chuông cho hai cache bằng cơ chế hiện hữu mà không tạo pipeline/SSOT mới; nếu không ghép mỏng được thì lazy refresh vẫn phải đúng độc lập.
- **Bước tiếp theo đã được Owner cho phép:** Host Claude soạn **một PROMPT triển khai duy nhất** cho hai gateway theo consensus P02 + freshness-debt ở trên; chưa RUN cho tới khi PROMPT được review/READY theo luật repo. **Guard điều phối:** `work/mcp-workspace/PROMPT.md` hiện vẫn là `MCPW-LOCK-20260924-01` READY; tuyệt đối không ghi đè/làm mất READY này. Host trước hết soạn nội dung P02 ở mức proposal/review (chat hoặc khối điều phối trong COLLAB), đồng thời đề xuất thứ tự hai RUN; chỉ đưa P02 vào `PROMPT.md` khi MCPW-LOCK đã được xử lý hoặc Owner chốt rõ việc supersede.

#### Claude · P02-IMPL proposal · 2026-09-25 · Based_on `cbe7f2c` (gồm `ac73b15` `ef28301` `17378ba`) · **ĐỒNG THUẬN GPT + Owner chốt** · NO PROMPT/READY/RUN
- **Đồng thuận:** ACCEPT toàn bộ GPT `ac73b15` (kết luận cần HEAD hiện thời coi là `unknown` khi không fresh; chuông là implementation gate; W/D là tuning). Không còn điểm vênh kiến trúc. `PROMPT.md` không đụng: commit cuối chạm vẫn là `d71a6c3` = READY MCPW-LOCK.
- **1 · Nợ freshness (Owner chốt) — ACCEPT, thêm 4 chốt để máy làm, không dựa trí nhớ:**
  - N1 · Nhãn tất định: gateway không đoán “có ảnh hưởng kết luận không”. Mọi phản hồi phụ thuộc HEAD có `freshness≠fresh` ⇒ `recheck_required=true`; `fresh` ⇒ `false`; `ref=<sha>` (bất biến) ⇒ `false`. `fs_*` ghi hai khoá này dạng máy đọc trên dòng `NGUỒN:` + một câu nhắc tại chỗ.
  - N2 · Trả nợ đúng cách: recheck = một safety read (stat, hoặc log n=1) đúng path/root. `fresh` + `source_head` không đổi ⇒ xoá nợ. `fresh` nhưng `source_head` đã đổi ⇒ **chưa xoá**: diff head cũ → mới trên path liên quan (`fs_diff from_version` / `workspace_diff from_ref`), sửa kết luận rồi mới xoá. JEV: xoá nợ khi HEAD đổi mà không xem thay đổi là an toàn 0,10.
  - N3 · Vẫn không fresh: trả lời một lần, ghi rõ “chưa xác nhận bản mới nhất · source_head=… · refreshed_at=…” để người sau kiểm lại được; không lặp.
  - N4 · Refresh nền: đúng một lượt mỗi cổng (flock không chờ, xuyên 6 worker), không gắn với vòng đời request: request trả về rồi, fetch vẫn chạy tới xong hoặc tới timeout của chính nó.
  - Cưỡng chế (A10-R2): phần máy (nhãn, refresh nền, ghi đối chiếu GitHub) thành `ĐÃ CƯỠNG CHẾ` khi RUN XONG. Phần “AI kết luận trong chat” gateway không chặn được ⇒ `CHƯA CƯỠNG CHẾ`; bù bằng nhắc tại chỗ trong chính phản hồi, và mọi kết luận ghi vào repo (READY/KQ/D) đều đi qua đường ghi có đối chiếu GitHub. Founders đưa N2–N3 vào README Technical Contract sau RUN.
- **2 · Receiver webhook thật — đã đọc mã (root `code`), không suy từ README:**
  - Chuỗi thật: GitHub → nginx → Nuxt `web/server/api/knowledge/owner-view-webhook.post.ts` (HMAC trên raw bytes, lọc repo/event/main, ≤ 1 MB) → chỉ **mở kết nối** `/run/incomex/hvu-b2.sock` → systemd `incomex-hvu-sync.socket` kích `incomex-hvu-sync.service` (oneshot, user `hvu-view`, `ProtectSystem=strict`, chỉ ghi `/opt/incomex/data/hvu-b2` + thư mục data public) → `sync.py` rút socket, `ls-remote` + fetch vào **bare clone riêng qua HTTPS ẩn danh**, dựng snapshot, ghi nguyên tử `sync-status.json` (`publishedRevision`, `lastCheckedAt`, `status`). Timer 15′ kích cùng oneshot.
  - Kết luận: **ghép mỏng ĐƯỢC, nhưng dạng “bảng tin” (kéo) chứ không phải “chuông” (đẩy).** Hai cổng chỉ **đọc** `sync-status.json` có sẵn làm gợi ý: (a) `publishedRevision` khác và không phải tổ tiên của ảnh chụp ⇒ biết GitHub có HEAD mới ⇒ lượt đọc kế tiếp kích refresh ngay, không chờ hết W; (b) `publishedRevision` = ảnh chụp và `status=fresh` ⇒ tính như một lần GitHub xác nhận tại `lastCheckedAt`. Không đổi dòng nào của receiver/HVU; không daemon, pipeline hay SSOT mới; file thiếu/hỏng ⇒ bỏ gợi ý, về lazy theo W. JEV `gen-dec-1790289889-u4sxtE56pIF2lPvpoXHi`: đọc status có sẵn 0,94 · drop-in touch 0 · daemon mới 0.
  - Đường tới file: helper `fs_*` chạy trên host nên đọc thẳng. Container `workspace_*` **chưa thấy** thư mục public (compose sống không đọc được qua MCP vì quyền) ⇒ gate RUN: agent chọn cách thật sự sẵn có (HTTP nội bộ qua nginx đang phục vụ chính file đó, hoặc bind-mount ro) và chứng minh bằng lệnh thật. Không có cách mỏng ⇒ `workspace_*` chạy lazy-only, vẫn PASS đúng/sai.
  - Không cần đẩy prefetch: gợi ý chỉ làm lượt đọc sau biết “phải đối chiếu”; lượt đó tự chờ tối đa D.
  - Phát hiện phụ: HVU đọc GitHub bằng **HTTPS ẩn danh** (repo PUBLIC), không đi qua bước tra deploy key — chính bước đã kéo 15 s ở sự cố B. Agent **đo** thêm: fetch đọc của hai cổng qua HTTPS ẩn danh so với SSH deploy key; chỉ đổi nếu số đo tốt hơn. Ghi giữ SSH deploy key (điều kiện MCPW-LOCK). Repo trở lại private thì quay về SSH, không đổi kiến trúc.
- **3 · Thứ tự hai RUN — Host chốt: MCPW-LOCK trước, P02 sau, KHÔNG gộp.**
  - LOCK đã READY `d71a6c3…`, chỉ là cấu hình GitHub, rollback một công tắc, chạy vài phút. P02 là thay đổi mã hai cổng, chưa có PROMPT.
  - LOCK trước ⇒ P02 được nghiệm thu **trên repo đã khoá** (ghi qua deploy key thật), đúng môi trường cuối. P02 trước ⇒ phép thử T2/T3 của LOCK rơi vào mã mới, có lỗi thì lẫn hai thay đổi.
  - Gộp ⇒ huỷ READY đã review, trộn một thay đổi cấu hình rollback một công tắc với một thay đổi mã, RUN_ID/KQ lẫn. Không lợi.
  - Rủi ro chấp nhận: sau LOCK, GPT chỉ ghi qua cổng. Lỗi B là **đọc** BUSY tạm khi GitHub chậm, ghi không bị ảnh hưởng; cửa khẩn cấp vẫn là tắt ruleset.
  - Ràng buộc chéo: P02 **không được thêm deploy key ghi** (sẽ phá G1.6 của LOCK); đọc dùng key hiện có hoặc HTTPS ẩn danh.
  - Trình tự: Owner RUN `MCPW-LOCK-20260924-01` (Claude Code CLI) → KQ XONG → Host tự thử + sửa README D12 → Host soạn P02 vào **chính** `PROMPT.md` (Git giữ lịch sử LOCK; trước KQ LOCK tuyệt đối không ghi) → GPT review → READY → Owner RUN. JEV cùng id trên: LOCK trước 0,78 · P02 trước 0,20 · gộp 0,01.
  - A0: §0 cũ ghi “sau LOCK thì Đóng” ⇒ cùng commit này sửa §0.3 để không đóng giữa chừng, và thêm dòng P02 `(đề xuất — chờ Owner gật)` ở §0.2.
- **4 · Kiến trúc triển khai P02 (proposal; mỗi cổng tự làm, cùng một luật):**
  - K1 Ảnh chụp đọc: thư mục bất biến theo SHA dựng từ object của clone cổng (`git worktree add --detach` hoặc tương đương), con trỏ `current` đổi nguyên tử; giữ bản trước cho request đang đọc; dọn bản dẫn xuất cũ có audit theo tiền lệ `revision-gc` của HVU. read/search/list/stat đọc thư mục này; log/diff/ref đọc object DB tại SHA ảnh chụp. Không lượt đọc nào chạm worktree ghi hay khoá root.
  - K2 Trạng thái cổng (file nhỏ, ghi nguyên tử): `snapshot_sha`, `confirmed_at`, `last_attempt`, `last_error`. Khởi động: có ảnh chụp ⇒ phục vụ ngay, nhãn không `fresh` tới lần xác nhận đầu.
  - K3 Refresher single-flight: fetch ngoài khoá root → kiểm hậu duệ (`merge-base --is-ancestor`) → dựng K1 → đổi con trỏ → cập nhật K2. Kích bởi: đọc không fresh · gợi ý HVU thấy HEAD mới · push thành công. Va chạm ref-lock với writer ⇒ refresher tự thử lại, không lộ ra người gọi.
  - K4 Tính nhãn mỗi request (không dùng mạng), từ K2 + gợi ý HVU. Đọc thường fresh ⇔ không biết HEAD mới hơn và `now − confirmed_at ≤ W`. Safety read fresh ⇔ lượt xác nhận bắt đầu sau khi request đến. Hết hạn D ⇒ trả last-good + `refreshing|stale` + `recheck_required=true`.
  - K5 Ghi: giữ nguyên toàn bộ luồng hiện hành (khoá writer, fetch GitHub, `expected_version`/`expected_head`, `operation_id`, journal/recovery); thêm đúng một bước: push OK ⇒ dựng K1 cho SHA vừa push **trước khi trả lời**.
  - K6 Hỏng: fetch/fsck lỗi ⇒ `stale` + `last_error` + cảnh báo, vẫn phục vụ ảnh chụp đang có. Dựng lại clone = runbook một lệnh do Host chạy, bản hỏng giữ nguyên để tra; V1 không tự động cho ít mã.
  - Tham số khởi điểm: W 60 s · D_plain 3 s · D_safe 5 s · ngưỡng stale 5′ — agent đo rồi chốt, không tăng timeout để che lỗi. Rollback: một lệnh mỗi cổng về image/config trước (mẫu `rollback.sh` MCPW-STAB); cổng này rollback không kéo cổng kia. Bậc: 2 ghép (git native, con trỏ nguyên tử, file status HVU sẵn có) + 3 code mỏng ở hai cổng.
- **5 · Acceptance bắt buộc** (mỗi cổng, gọi thật; mỗi mục có mutant phải FAIL):
  1. GitHub giả chậm 20–30 s (làm chậm transport trên bản dựng thử; production chỉ đo, không tiêm lỗi): 12 read song song = **0 BUSY/OVERLOADED**, mỗi lượt ≤ D + 1 s; mutant bỏ hạn chờ ⇒ FAIL.
  2. Mọi phản hồi `refreshing|stale` có `recheck_required=true`; `fresh` = `false`; `ref=<sha>` = `false`.
  3. Gỡ độ chậm ⇒ safety read `fresh`, `recheck_required=false`, `source_head` = HEAD GitHub (xoá nợ); head đổi thì phản hồi có đủ head cũ/mới để diff.
  4. Restart/reboot khi GitHub bị chặn: **không phản hồi nào `fresh`** tới khi đối chiếu thành công.
  5. Ghi rồi đọc ngay cùng cổng thấy commit mới, kể cả khi GitHub chậm sau push.
  6. Cổng X ảnh chụp cũ S0; cổng Y push S1 sửa file F: X sửa F theo version S0 ⇒ từ chối; không tổ hợp nào ghi đè HEAD mới; GitHub giữ đủ thay đổi của cả hai.
  7. Không lùi: gợi ý/SHA cũ hoặc đảo thứ tự ⇒ ảnh chụp không lùi.
  8. Gợi ý HVU thiếu/hỏng ⇒ mục 1–7 vẫn PASS (lazy).
  9. Ghi + refresh đồng thời: không deadlock, không lỗi ref-lock lộ ra người gọi.
  10. Không hồi quy: GPT 37 tool + input schema + hash `dbbfc590a969` + auth 401 + `operation_id` replay + transaction/restore; Claude 23 tool + vân tay `4f1000e9aad3`; `run_acceptance.py` release gate; không thêm deploy key.
  11. Chạy trên repo đã bật ruleset (sau LOCK): ghi cả hai cổng qua deploy key PASS.
  12. Đo và ghi: p50/p95 đọc thường/safety, số lượt gọi GitHub mỗi giờ trước/sau, HTTPS ẩn danh so với SSH.
- **Còn lại:** GPT xác nhận mục 3 (thứ tự) để Host ghi CONSENSUS thứ tự RUN. Owner: gật dòng §0 và RUN LOCK.

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

## KQ — MCPW-LOCK-20260924-01
Agent: Claude Code CLI trên Mac Owner · 25/09/2026 · tiếp nối RUN 25/09 ghi ở mục `MCPW-LOCK — trạng thái hiện hành` (auto-mode chặn lệnh dán ⇒ Owner gõ tay cho phép; lệnh tạo ruleset và T1 vẫn bị auto-mode chặn ⇒ **Owner tự chạy đúng lệnh PROMPT bằng `!` trong phiên Claude Code**, agent kiểm lại bằng API).
- **G0 PASS** — `fs_read` AGENTS → COLLAB → PROMPT; commit cuối chạm PROMPT = `d71a6c3b85aaac74a2e28aa63584b4976ce7f680` = READY; kiểm lại trước khi ghi KQ: vẫn khớp.
- **G1.1 PASS** — `gh` tài khoản `Huyen1974`; `permissions.admin=true`, `visibility=public`, nhánh mặc định `main`.
- **G1.2 PASS** — `rulesets` = `[]` (không có `gateway-only-writes` trước khi bật).
- **G1.3 PASS** — đúng 1 deploy key: id `163589117` · `VPS MCP host helper (GSM: MCP_WORKSPACE_GH_DEPLOY_KEY)` · `read_only=false` · tạo 2026-09-17T10:14:20Z · ED25519 `SHA256:ctotGu9UmOMq45jA…` (file tạm khoá công khai đã xoá). Không có deploy key chỉ-đọc.
- **G1.4 PASS** — cổng `fs_*`: `/run/incomex-mcp-helper/gh_deploy_key` → `SHA256:ctotGu9UmOMq45jA…` = key 163589117. (File quyền 0640 nên `ssh-keygen -y -f` từ chối; lấy khoá công khai qua pipe `cat … | ssh-keygen -y -f /dev/stdin | ssh-keygen -lf -`, không in/copy/đổi quyền khoá riêng.)
- **G1.5 PASS** — cổng `workspace_*` (container `incomex-agent-data`, image `agent-data-hvu:mcpw-stab-20260924-final`): `WORKSPACE_CONFIG=/workspace/config.json` → root `workspace` = `/workspace/state/github-workspace`, mode git, nhánh `main`; `origin` = `git@github.com:Huyen1974/incomex-workspace.git` (SSH, không token); `core.sshCommand` = `ssh -F /dev/null -i /workspace/state/git-auth/id_ed25519 -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=yes …`; biến `GIT*` trong container: không có; khoá → `SHA256:ctotGu9UmOMq45jA…` = key 163589117 (không phải khoá tài khoản người).
- **G1.6 PASS** — tập deploy key ghi-được = {163589117} = tập fingerprint của 2 cổng (dùng chung một key); không key thừa/không nhận diện.
- **G1.7 PASS** — `contents/.github` → 404; `actions/workflows` total_count = 0.
- **Ruleset** — id **`23976991`**, tạo 2026-09-25T03:20:38Z (Owner chạy lệnh §3 nguyên văn). JSON đã gửi: `{"name":"gateway-only-writes","target":"branch","enforcement":"active","conditions":{"ref_name":{"include":["~ALL"],"exclude":[]}},"rules":[{"type":"creation"},{"type":"update","parameters":{"update_allows_fetch_and_merge":false}},{"type":"deletion"},{"type":"non_fast_forward"}],"bypass_actors":[{"actor_id":null,"actor_type":"DeployKey","bypass_mode":"always"}]}`. GET lại: `enforcement=active`, `source_type=Repository`, 4 rule creation/update/deletion/non_fast_forward, bypass **chỉ** `DeployKey` (không role/user/app); repo có đúng 1 ruleset.
- **T1 PASS** — `gh api -X PUT …/contents/work/mcp-workspace/COLLAB.md` (tài khoản Owner, nội dung = bản main + đúng 1 dòng probe, blob sha `d6efda1…`) → **HTTP 409** `Repository rule violations found — Cannot update this protected ref.` (03:22:52Z, request `E131:38B15A:86F044:8D9D4F:6AB5E90B`). Main không đổi, không có dòng probe ⇒ không cần gỡ.
- **T2 PASS** — chính commit ghi khối này qua `fs_edit` root `gh` (deploy key 163589117) đẩy lên `main` sau khi ruleset active.
- Không đổi setting GitHub nào khác; không sửa VPS; không sửa README/AGENTS; rollback không cần.

## Owner cần quyết
- —
