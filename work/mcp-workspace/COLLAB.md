# COLLAB — mcp-workspace

Founders: GPT Chat + Claude Chat
Host: GPT · Owner giao: 2026-09-20
Mục tiêu cuối: GPT/Claude edit tự nhiên và ổn định qua MCP trên Git workspace + vùng VPS được phép ghi; kết thúc kết nối để quay lại công việc nghiệp vụ.

## R03 — trạng thái hiện hành
R03 | NAME-TWIN-REPAIR + FINAL CLIENT ACCEPTANCE | PROMPT DRAFT sau tái cấu trúc | NEXT: Claude Chat REVIEW | BLOCK: —

- Repo đã tái cấu trúc: root chỉ còn `AGENTS.md`, `README.md`, `COLLAB.md`, `work/`.
- Toàn bộ việc này nằm tại `work/mcp-workspace/`; test/chứng tích không còn rải ở root.
- PROMPT hiện hành: `work/mcp-workspace/PROMPT.md`.
- **PROMPT_SHA = de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4**.
- READY cũ `8114352...` hết hiệu lực vì PROMPT đã đổi path/nội dung theo chỉ đạo Owner.
- Phạm vi repair vẫn khóa: chỉ lỗi #24 tên sinh đôi D1–D4; không thêm capability/tool/schema.

## Client cuối — đã chốt
- ChatGPT Pro hiện tại của Owner **không có Refresh app**.
- Chỉ sau `MACHINE_DONE`: tạo **một MCP app mới** từ đúng Full All server hiện hữu, giữ URL/auth/secret; Scan Tools đúng một lần và so tool/schema/metadata/build + 29 capability với `DANH-MUC-CONG-CU.md` trước khi Owner Connect tay.
- Không đạt cổng Scan thì dừng trước Connect; không tạo chuỗi app mới.
- Giữ app cũ rollback tới khi app mới PASS. Claude reconnect/open phiên mới sau backend cuối.

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

## Prompt / giấy phép
- Claude Founder REVIEWED@de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4: **CHỜ**
- GPT Host READY@de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4: **CHỜ**
- RUN: chỉ phát sau khi REVIEWED + READY đã có commit thật trong Git.

## Claude review
P15 | GPT | OPEN
Đọc `AGENTS.md` → file này → `PROMPT.md`. Chỉ kiểm: (a) cấu trúc repo dài hạn; (b) repair #24 không đổi phạm vi; (c) cơ chế GPT Pro = MCP app mới/Scan trước Connect; (d) bài 9 bước + VPS/CROSS đủ để đóng R03.
Nếu đồng ý, ghi ngay tại đây: `Claude REVIEWED@de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4 · ACCEPT`. Nếu cần chỉnh, ghi ADJUST tối đa 5 dòng, không mở capability mới.

## Bằng chứng gần nhất
- `957547d2518b83c9ef7b6bbbde2c996c92e887d4` · gom toàn bộ R03/test/archive vào `work/mcp-workspace/`.
- `16f23cc65c714e5471733f0b89778ab90359997a` · tạo COLLAB gốc tối giản.
- `de45f4ecbe2d19a1327bcd8dccb6e1eab74123a4` · cập nhật AGENTS/README/PROMPT theo cấu trúc mới + client Pro không Refresh.

Lịch sử chi tiết trước bản rút gọn này giữ trong Git; không chép lại vào COLLAB.
