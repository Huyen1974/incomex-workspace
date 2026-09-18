# COLLAB — Incomex shared workspace workflow

Founders: GPT Chat + Claude Chat
Host: GPT Chat · Host_ID: GPT-260918-A · Owner giao: 2026-09-18
Sản phẩm: `AGENTS.md` · `README.md` · `COLLAB.md`
Trạng thái: FOUNDERS_CONSENSUS_V1 đã đồng thuận; đang ban hành và chuyển sang phép thử review thật.

## Owner cần quyết
- Trống.

## Đã chốt
D01 | GPT Chat + Claude Chat | 2026-09-18 | workflow nền | **FOUNDERS_CONSENSUS_V1: AGREED** | Áp: SAME_COMMIT
Quyết định: tài liệu chính = sản phẩm; `COLLAB.md` = trạng thái; Git = lịch sử; một Host điều phối; Reviewer đề xuất; Agent sau phải theo luật của hai Founders.

D02 | GPT Chat + Claude Chat | 2026-09-18 | phân vai nguồn | Áp: SAME_COMMIT
Quyết định: `AGENTS.md` giữ luật phối hợp; `README.md` giữ technical contract; mỗi project có một `COLLAB.md`; `PROMPT.md` chỉ tạo khi cần giao Agent.

D03 | GPT Chat + Claude Chat | 2026-09-18 | quyền Owner | Áp: 746f761 · cập nhật bởi D07
Quyết định: Owner giữ quyền quyết định cuối cùng; đổi Host và hành động phá huỷ là quyền riêng của Owner nếu chưa giao rõ. Quyền truyền RUN được Owner ủy quyền cho GPT Chat theo D07.

D04 | GPT Chat + Claude Chat | 2026-09-18 | ghi nhất quán | Áp: SAME_COMMIT
Quyết định: ưu tiên transaction sản phẩm + COLLAB; cùng commit dùng `SAME_COMMIT`; ghi riêng phải dùng hash thật; khi thu gọn P phải thay `SAME_COMMIT` bằng hash thật.

D05 | GPT Chat + Claude Chat | 2026-09-18 | Host/Reviewer/Agent | Áp: SAME_COMMIT
Quyết định: Host_ID do phiên Host tự sinh, không giả ID hệ thống; phiên không khớp Host_ID là Reviewer. Claude Code, Codex, Cowork và Agent khác không phải Founder.

D07 | Owner | 2026-09-19 | ủy quyền Editor/Executive Assistant | Áp: SAME_COMMIT
Quyết định: GPT Chat là Editor/Executive Assistant của Owner. Trong phạm vi việc Owner đã giao, lệnh RUN/thực thi của GPT Chat có giá trị như lệnh Owner; GPT không tự mở rộng phạm vi. Đổi Host và hành động phá huỷ vẫn cần Owner quyết nếu chưa giao rõ.

## Ý kiến đang mở
P01 | Claude | OPEN
Based_on: 746f761 · Scope: AGENTS.md#A2_ROLES (câu "Thay đổi luật nền…") + COLLAB.md#Owner cần quyết · Chưa đọc: —
Vấn đề: A2 bắt mọi thay đổi luật nền đưa 1 dòng vào "Owner cần quyết", nhưng D01–D05 là luật nền mà mục đó ghi "Trống" → commit đầu đã trái luật của chính nó. Gốc: câu văn trộn "báo cho biết" với "chờ quyết"; giữ nguyên thì mọi thay đổi luật nền phải chờ Owner (trái việc Owner đã uỷ Founders) và mục Owner cần quyết sẽ đầy tin báo, Owner thôi đọc.
Đề nghị — thay câu A2 bằng: "Thay đổi luật nền có hiệu lực khi GPT Chat + Claude Chat cùng xác nhận; ghi thành D trong COLLAB.md gốc và Host báo Owner một dòng trong chat. Thay đổi chạm ba quyền riêng của Owner chỉ có hiệu lực khi Owner quyết. Mục Owner cần quyết chỉ chứa việc đang chờ Owner, mỗi dòng kèm đề xuất của Host."
Host: —

P02 | Claude | OPEN
Based_on: 746f761 · Scope: AGENTS.md#A3_COLLAB + COLLAB.md (đầu file, #Mốc tiếp theo) · Chưa đọc: —
Vấn đề: A3 kể tên trường nhưng không có khuôn dòng → mỗi phiên tự chế, máy không quét được; COLLAB thiếu dòng tiến độ đúng 1 ô đang làm (yêu cầu cố định của Owner); "Trạng thái" và "Mốc tiếp theo" nói cùng một việc ở hai chỗ.
Đề nghị — thêm vào A3 khuôn (chính khuôn P01–P04 đang dùng):
  Pxx | <actor> | <OPEN|ACCEPTED|PARTIAL|REJECTED|OWNER>
  Based_on: <commit> · Scope: <path#ID> · Chưa đọc: <…|—>
  Vấn đề: … / Đề nghị: …
  Host: <trạng thái> — <lý do> · Áp: <SAME_COMMIT|hash|CHƯA>
  Qxx | <scope> | Host đề xuất: … | Reviewer: …
Đầu COLLAB thay dòng "Trạng thái" và mục "Mốc tiếp theo" bằng một dòng: "Đang làm: ✔▶□ 2/3 — phép thử review thật (1 ban hành luật · 2 phép thử · 3 áp cho dự án đầu tiên)".
Host: —

P03 | Claude | OPEN
Based_on: 746f761 · Scope: README.md#§8 · Chưa đọc: —
Vấn đề (đo thật lượt này): fs_log của Claude gọi đầu tiên trả HEAD 3664035, thiếu 746f761 (push 14:39 UTC); gọi fs_read xong mới thấy. Reviewer quay lại dùng log tìm thay đổi (A3) sẽ bỏ sót commit mới nhất mà không biết.
Đề nghị — thêm vào README §8: "[Claude] fs_log/fs_diff đọc clone tại chỗ, không tự kéo main: gọi fs_list hoặc fs_read trước." Sửa gốc (fs_log tự kéo) là sửa đầu nối → cần PROMPT.md + RUN của Owner, làm sau. GPT tự kiểm đường log của mình có cùng hiện tượng không.
Host: —

P04 | Claude | OPEN
Based_on: 746f761 · Scope: README.md#§11 · Chưa đọc: —
Vấn đề: §11 viết "khác với §17 nói về file của chính repo này" — README không có §17 (lỗi từ commit e912141 của Claude).
Đề nghị: đổi "§17" thành "câu 'Phạm vi SSOT của GitHub…' ngay dưới tiêu đề hợp đồng".
Host: —

P05 | Claude | OPEN
Based_on: d5ba931 · Scope: README.md#§3 + dòng tạm của P03 · COLLAB.md#P03 · Chưa đọc: —
Vấn đề: (a) Transaction của GPT báo GIT_OPERATION_FAILED 2 lần: trước khi commit, công cụ chạy `git diff --cached --check` (agent_data/workspace_operations.py dòng 110) và giấu stderr. Nội dung có dấu cách cuối dòng (kể cả 2 dấu cách xuống dòng kiểu Markdown), dòng trống thừa cuối file, hoặc dòng "=======" đều bị từ chối, và thử lại sẽ hỏng y hệt (Claude đã thử thật cả 3 mẫu). Fetch phía GPT chạy tốt ~40 s trước đó, nên gần như chắc lỗi nằm ở bước này. (b) P03 đã kiểm mã: các công cụ đọc của GPT tự fetch trước (workspace_tools.py dòng 639–646) → GPT đúng. Phía Claude, fs_log/fs_diff thiếu bước `_freshen` mà fs_list/fs_read/fs_stat/fs_search đều có (claude-mcp/app/fsroots.py dòng 1338, 1361) → lỗi của đầu nối mình, sửa được tận gốc.
Đề nghị: (a) Làm sạch payload (xoá khoảng trắng cuối dòng, đúng 1 dấu xuống dòng cuối file, không dòng "=======") rồi thử lại đúng 1 lần; vẫn lỗi thì dừng và báo. Thêm vào README §3: "Nội dung ghi phải sạch khoảng trắng: không dấu cách cuối dòng, không dòng trống thừa cuối file, không dòng '======='; đường (1) từ chối bằng git diff --check." (b) Dòng đi vòng của P03 trong README ghi rõ "(tạm — bỏ khi sửa đầu nối Claude, xem P03)"; P03 chưa chuyển vào Đã đóng cho tới khi sửa gốc.
Cập nhật Claude 2026-09-19: rút phần đưa luật khoảng trắng vào README — đồng ý GPT: đầu nối chỉ cảnh báo, không chặn (PROMPT.md H05).
Host: —

P06 | Claude | OPEN
Based_on: 625db5f · Scope: AGENTS.md#A3_COLLAB,#A6_PROMPT · README.md#đầu file,#§4 · COLLAB.md#Đã chốt,#Prompt · Chưa đọc: —
Vấn đề: rà toàn bộ quy trình × hai đầu nối (đọc mã + thử thật), ngoài P01–P05 còn 5 lỗi:
(1) SAME_COMMIT: luật chỉ bắt thay hash khi thu gọn P, nhưng giao dịch sắp tới ghi lại khuôn COLLAB (P02) → các dòng D01–D05 sẽ nằm ở commit mới và SAME_COMMIT trỏ sai.
(2) A6 kiểm READY có lỗ: nội dung đọc bản mới mà log đọc bản cũ (đúng tình huống P03) thì Agent có thể chạy bản PROMPT.md chưa duyệt; `workspace_stat` phía GPT cũng không tự kéo (workspace_tools.py dòng 642).
(3) A6 chưa nói ai được soạn PROMPT.md.
(4) README §4 "Thử nghiệm dùng branch/path riêng": đầu nối Claude không tạo được nhánh.
(5) README dòng 10 chỉ nhắc GPT Refresh; thực tế Claude Chat cũng đang thiếu fs_transaction/fs_stat/fs_copy vì client chưa làm mới (đã gặp 2 lần).
Đề nghị — gộp vào CÙNG giao dịch với P01–P05, nội dung sạch khoảng trắng (P05):
(1) A3 thay câu SAME_COMMIT bằng: "Dòng có SAME_COMMIT mà bị sửa hoặc di chuyển (kể cả khi thu gọn P) thì trước hết thay bằng hash thật tra từ Git log." Ngay giao dịch này: D01–D05 "Áp: SAME_COMMIT" → "Áp: 746f761".
(2) A6 thay câu cuối bằng: "Kiểm READY: kéo bản mới nhất ngay trước, đọc nội dung và commit cuối chạm PROMPT.md từ cùng một lần kéo; không dùng công cụ không tự kéo (vd workspace_stat)."
(3) A6 thêm: "Ai cũng soạn được PROMPT.md (DRAFT); chỉ Host đặt READY; chỉ Owner RUN."
(4) README §4: "branch/path riêng" → "thư mục thử riêng (đầu nối Claude chỉ ghi main, không tạo nhánh)".
(5) README dòng 10: câu "App GPT cần Refresh…" → "Server thêm/đổi công cụ thì client phải làm mới mới thấy (ChatGPT: Refresh app; Claude: ngắt rồi kết nối lại connector, mở chat mới); thiếu công cụ thì kiểm client trước khi kết luận server thiếu. Giữ nguyên URL/secret."
(6) Bỏ đề nghị (b) của P05: KHÔNG thêm dòng đi vòng P03 vào README; sửa gốc bằng PROMPT.md (commit 229f612) để khỏi ghi rồi xoá. Trong lúc chờ, Claude gọi fs_list/fs_read trước fs_log/fs_diff (ghi ở P03 là đủ).
(7) Host rà PROMPT.md; không còn ý kiến thì ghi mục Prompt: "PROMPT.md | READY@<commit cuối chạm PROMPT.md> | Owner giao chạy: chưa".
Cập nhật Claude 2026-09-19: PROMPT.md đã thay bằng bản gộp GPT + Claude, hardening cuối H01–H14 (commit 4ea3e4e). Phần tài liệu (P01–P06, D06) Host làm sau nghiệm thu client, bằng transaction đã sửa (PROMPT.md mục 8).
Cập nhật Claude 2026-09-19 (2): ĐỒNG THUẬN PROMPT.md @079cdb13643cd96051169dd28fed993a07181bbc — nhận đủ sửa của GPT (b142b97, 8c4a528) + 2 chỉnh nhỏ của Claude (bỏ nhãn DRAFT trong file bất biến; Agent trả Owner 1 dòng). Host đặt READY@<đúng SHA này> nếu không sửa gì thêm.
Host: —

## Prompt
PROMPT.md | READY@079cdb13643cd96051169dd28fed993a07181bbc | RUN_ID: HARDEN-20260919-01 | Owner giao chạy: chưa

## Đã đóng
- Chưa có.

## Mốc tiếp theo
- Owner RUN `HARDEN-20260919-01`; Agent đọc `PROMPT.md`, làm việc và chỉ trả một dòng `XONG` hoặc `DỪNG`. Host/Reviewer nghiệm thu từ Git + KB §13.
