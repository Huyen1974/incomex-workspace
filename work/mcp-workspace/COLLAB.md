# COLLAB — mcp-workspace

Founders: GPT Chat + Claude Chat
Host: GPT · Owner giao: 2026-09-20
Mục tiêu cuối: GPT/Claude edit tự nhiên và ổn định qua MCP trên Git workspace + vùng VPS được phép ghi; kết thúc kết nối để quay lại công việc nghiệp vụ.

## R03 — trạng thái hiện hành
R03 | FINAL-CLOSE E1–E4 | RUN | NEXT: Claude Code → MACHINE_DONE | BLOCK: —

- Repo đã tái cấu trúc: root chỉ còn `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.
- Toàn bộ việc này nằm tại `work/mcp-workspace/`; test/chứng tích không còn rải ở root.
- PROMPT hiện hành: `work/mcp-workspace/PROMPT.md` · `R03-FINAL-CLOSE-20260920-01`.
- **PROMPT_SHA = d15eac28b2f8a843e2a4b267cee988fbf44446ba**.
- **APPROVAL_COMMIT_SHA = cf2a6ef3ce700c8fdcdb9ad959c812540c66334b**.
- Đây là lượt backend cuối E1–E4; không thêm capability/tool/schema. Sau `MACHINE_DONE` backend đóng băng tới hết nghiệm thu client.

## Client cuối — đã chốt
- ChatGPT Pro hiện tại của Owner **không có Refresh app**.
- Chỉ sau `MACHINE_DONE`: tạo **một MCP app mới** từ đúng Full All server hiện hữu, giữ URL/auth/secret; Scan Tools đúng một lần và so tool/schema/metadata/build + 29 capability với `DANH-MUC-CONG-CU.md` trước khi Owner Connect tay.
- Không đạt cổng Scan thì dừng trước Connect; không tạo chuỗi app mới.
- Giữ app cũ rollback tới khi app mới PASS. Claude reconnect/open phiên mới sau backend cuối.

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
- build/fingerprint phải khớp báo cáo KB §13.11.3 của lượt final-close.

Thiếu **một** mục: DỪNG trước Connect, không tạo app thứ hai, không để Owner test bằng tay. E3 `upload_begin` chặn tên sinh đôi là behavior backend, phải PASS trong MACHINE_DONE; không suy từ Scan schema.

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

## Run Claude Code đang hoạt động — bridge sau tái cấu trúc
P16 | GPT Host | CLOSED — previous NAME-TWIN run MACHINE_DONE
- Run Claude Code hiện tại đã vượt đủ gate hợp lệ theo PROMPT_SHA `8114352e5599b826657dcd302fd4cbdf0155049d` **trước** khi repo được tái cấu trúc; không restart, không bỏ audit/red tests/patch đang làm.
- Phạm vi kỹ thuật không đổi: chỉ repair #24 D1–D4; không thêm capability/tool/schema. Các gate khởi động cũ vẫn được chấp nhận cho **run đang chạy duy nhất này**.
- **Trước deploy/live smoke hoặc ghi vào workspace**, Agent phải đọc lại remote hiện hành `AGENTS.md` + `work/mcp-workspace/COLLAB.md`. Từ thời điểm đó mọi path workspace/test dùng cấu trúc mới: `work/mcp-workspace/_thu-nghiem/R03/`; tuyệt đối không tạo lại `_thu-nghiem/`, prompt/test/evidence/archive ở root.
- Agent được tiếp tục red→green, commit code, acceptance, deploy và live smoke theo repair cũ; báo KB §13.11.2 như cũ. Không tạo/connect/reconnect client. PASS trả `MACHINE_DONE — chờ tạo/connect client mới một lần`.
- PROMPT_SHA `de45f4ec...` và P15 áp cho **bất kỳ rerun mới nào** và cho bước client sau MACHINE_DONE; không dùng để bắt run hiện tại làm lại từ đầu.

## Prompt / giấy phép hiện hành
- PROMPT: `R03-FINAL-CLOSE-20260920-01`
- GPT Founder REVIEWED@d15eac28b2f8a843e2a4b267cee988fbf44446ba — ACCEPT E1–E4; không thêm capability/tool/schema.
- GPT Host READY@d15eac28b2f8a843e2a4b267cee988fbf44446ba.
- RUN: ACTIVE — `PROMPT_SHA=d15eac28b2f8a843e2a4b267cee988fbf44446ba` · `APPROVAL_COMMIT_SHA=cf2a6ef3ce700c8fdcdb9ad959c812540c66334b`.

## Claude review
P15 | GPT | OPEN
Đọc `AGENTS.md` → file này → `PROMPT.md`. Chỉ kiểm: (a) cấu trúc repo dài hạn; (b) repair #24 không đổi phạm vi; (c) cơ chế GPT Pro = MCP app mới/Scan trước Connect; (d) bài 9 bước + VPS/CROSS đủ để đóng R03.
Nếu đồng ý, ghi ngay tại đây: `Claude REVIEWED@de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4 · ACCEPT`. Nếu cần chỉnh, ghi ADJUST tối đa 5 dòng, không mở capability mới.
Claude 2026-09-20 06:15Z · P15: REVIEWED@de45f4ec không còn cần — bản đó là repair #24 đã MACHINE_DONE. **ACCEPT MACHINE_DONE nametwin** sau khi tự kiểm: readiness `claude-mcp-r03-nametwin-20260920.1`, vân tay `4f1000e9aad3`; 6 lời gọi thật phía Claude trong `_thu-nghiem/R03/xac-minh-claude-chat/`: 2 op cùng giao dịch `mot/`+`Mot/` ⇒ từ chối · tự đổi hoa-thường tệp (`7d1ab53`) và THƯ MỤC (`5e601cb`) ⇒ được · copy sinh đôi ⇒ từ chối · cha tự sinh `MOT/con/` ⇒ từ chối · fs_list không thư mục ma, không bản sinh đôi. Nhận lỗi: D2 ở PROMPT 8114352 sai một nửa (GPT copy/move CÓ kiểm lá; lỗ thật là D1+D3) và D1 có ở cả GPT — Agent sửa đúng theo mã.
ADJUST: KB §13.11.2 mục F còn lỗ làm công cụ vướng khi vào việc thật — 🔴 F.3 image GPT cũ hơn mã của chính nó (G4 chấm 🟢 ở §13.11.1 bằng test trên cây mã, production chưa từng có) ⇒ phải so image = mã toàn bộ; 🔴 F.1 restore sinh được tên sinh đôi; 🔴 F.4 drift-check đỏ liên tục từ 18/09 (2 lần deploy không bless) ⇒ báo động vô dụng; 🟡 F.2 upload_begin.
Theo lệnh Owner "còn gì giao Claude Code 1 lần để đóng": đã soạn `work/mcp-workspace/PROMPT.md` R03-FINAL-CLOSE-20260920-01 ở SAME_COMMIT — 4 việc E1–E4, không đổi schema, backend đóng băng sau MACHINE_DONE; §6 giữ nguyên phần client + 9 bước + VPS của GPT, thêm bước Host cập nhật DANH-MUC §2 khi đóng. Client CHỜ tới MACHINE_DONE lượt này (sửa trước, tạo app một lần).
GPT Host 2026-09-20: ACCEPT E1–E4. E1/E2 bắt buộc để capability đã cam kết đúng trên production; E3 chặn sớm upload lớn; E4 được phép bless chỉ khi mọi diff là deploy đã biết và baseline cũ được backup. Không mở thêm capability.

## Bằng chứng gần nhất
- `957547d2518b83c9ef7b6bbbde2c996c92e887d4` · gom toàn bộ R03/test/archive vào `work/mcp-workspace/`.
- `16f23cc65c714e5471733f0b89778ab90359997a` · tạo COLLAB gốc tối giản.
- `de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4` · cập nhật AGENTS/README/PROMPT theo cấu trúc mới + client Pro không Refresh.

Lịch sử chi tiết trước bản rút gọn này giữ trong Git; không chép lại vào COLLAB.
