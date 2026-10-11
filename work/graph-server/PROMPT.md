# PROMPT — GS-VIEW0-MAC-LOCAL-20261011-17 · MÀN HÌNH ĐỒ THỊ TRÊN MAC CỦA OWNER
RUN_ID: `GS-VIEW0-MAC-LOCAL-20261011-17`
Task: `work/graph-server/` · theo GS-RM1 VIEW0 & Owner D24.
Executor_Surface: Claude Code CLI trên MacBook Owner (phiên thực thi do Owner tự dán sau Claude Reviewer exact SHA ACCEPT + GPT Host READY).
Repo_Write_Path: Incomex MCP `workspace_*` root=`workspace` chỉ ghi KQ/Board/root sau khi có kết quả; Mac artifacts ngoài repo/iCloud/Google Drive/cloud sync; Graph source **READ-ONLY** qua đường `graph-v1 export` sẵn có.
STATUS: **DRAFT P118 · CLAUDE P117 V1–V8 ĐƯỢC HOST CHỐT · CHỜ MỘT CLAUDE REVIEW EXACT SHA · NO READY/RUN**.
**R10 preservation:** bản R10 chính xác được giữ ở Git commit last-touch `ebf52956eb740037f9aaf4e217897235dd7cc671`; P108/P109 đã ký **nội dung** đó. Khi VIEW0 chiếm `PROMPT.md`, R10 KHÔNG còn là PROMPT active, READY cũ không còn dùng được. Sau VIEW0 KQ, Host khôi phục nguyên byte R10 từ commit trên, kiểm đối chiếu, Reviewer xác nhận SHA mới 1 lượt, Host mới READY khi VPSC #11 GREEN và Guard đạt. Cấm nói SHA R10 cũ là active READY.

## 0. MỤC TIÊU OWNER / SCOPE
Owner: “điều tôi cần nhất là làm sao để nhìn được các mối quan hệ đó biểu diễn trên màn hình.” Lượt này hoàn thành một **màn hình cục bộ, tương tác thật, bấm đúp mở trên Mac**, xem node/edge Graph đã nạp; tìm mã, zoom, click cạnh, xem evidence/trust. Không xây website, không dựng máy duyệt mới, không tạo source khách chưa được duyệt.
Nguồn có thật: Base88, PG/DOT và 3 cây Python/51 file; R7/R9 3.596 node/6.823 edge là mốc lịch sử, không dùng thay phép đo xuất thực.
Đèn #11 VPSC đang RED theo lần kiểm P117; **được phép chỉ đọc Graph**, tuyệt đối không mutation Neo4j, DB, graph-v1 scripts, nginx/Nuxt/Config Guard, cron, graph prod, hoặc tạo tệp mới trên VPS khi đèn đỏ. Không can thiệp VPSC N2a hay HJW/Mac Hermes configuration.

## 1. S0 · AUTH / MAC READ-GATE
- Đọc `AGENTS.md` → root `COLLAB.md` → Graph §0/Bảng/GS-RM1/P115–P118 → PROMPT này; verify cross-vendor Reviewer P119 ACCEPT **exact last-touch SHA**, Host READY cùng SHA và Owner RUN; `COUNCIL_ALERT`/STOP/concurrent conflict phải sạch. Re-read trước mutation theo DROOT30. Không có READY thì không chạy.
- Trên Mac xem đủ phiên bản, shell, dung lượng, path, công cụ Graph connector hiện hữu, khả năng nghe localhost; không viết vào repository, system Mac keychain/cấu hình SSH/MCP, cron/launchd, hoặc Mac Hermes tree/hook khi có phiên HJW Mac khác đang làm. Việc sửa UI Mac trong scope chỉ gồm thư mục VIEW0 riêng được phép.
- `graph-v1 export`: đọc HELP/định dạng/hash và xác định thực sự read-only. Ưu tiên **stream stdout từ lệnh có sẵn về tệp trên Mac** hoặc sao chép immutable export đã có kèm source hash/version, không sinh file trên VPS. Nếu command chỉ ghi VPS hoặc nguồn có thiếu lớp, **DỪNG với một blocker `NO_READONLY_EXPORT_TO_MAC`**; không tự chạy Cypher qua credential/admin, không vượt Guard, không đổi lệnh graph-v1. #11 đỏ không phải lý do ngừng Mac-only nếu không có ghi VPS.
- Chọn local path không thuộc đồng bộ cloud, Git checkout, repo, thư mục Downloads đồng bộ hoặc account khác; quyền 0700 với folder, 0600 với data; không gửi raw data lên Git/OpenRouter/Gephi online.

## 2. V1–V4: DATA FULL + MAC VIEWER
**V1**: Mac local-only, 0 server/config/code mutation; chỉ dùng đọc source read-only. Chưa có nguồn khách/KB/policy thì không bịa node.
**V2**: từ bản xuất graph-v1 tạo 3 tệp **đủ nguyên lớp** (Base88, PG/DOT, Code) và 1 tệp gộp với source hash/timestamps; phân loại theo source/provenance thật, giữ node/edge đúng lớp, phân biệt unknown/candidate/trust; đối chiếu tổng bằng unique node/edge IDs, không mất cạnh nối giữa lớp (tệp gộp giữ). **Không cắt dữ liệu còn 50–100 node**; có thể chọn một vùng nhỏ làm góc nhìn ban đầu để dễ đọc nhưng vẫn search được toàn bộ. Dữ liệu không đủ khả năng cho phép hiển thị ⇒ ghi exclusions có đếm, không tự chế nhãn người/tổ chức từ ID.
**V3**: Một thư mục trên Mac như `~/Incomex-Graph-View/` **chỉ nếu** nằm ngoài mọi đồng bộ; gồm các tệp Graph riêng tư, manifest sha256/count, layout đã lưu và **`OPEN-GRAPH.command`** mà Owner bấm đúp từ Finder. Không bản nào vào public `ui-preview`/Git/GDrive; README tiếng Việt chỉ hướng dẫn “bấm mở, tìm, đóng”.
**V4**: ưu tiên Gephi Lite **nguyên bản** (GPL-3.0), ghim commit/bản phát hành/checksum; tận dụng bản build tĩnh hoặc local build khi vừa sức, không chỉnh source Gephi. Kiểm định dạng GEXF 1.2/1.3, GraphML hoặc Graphology JSON **bằng code chạy thật**, không giả định JSON tùy ý được hỗ trợ. Server tạm chỉ nghe `127.0.0.1`, không cài background daemon/launchd/cron, không public IP; tắt cửa sổ lệnh thì thoát và dọn process. Không bật map tiles/GitHub Gist/remote updates/external uploads từ dữ liệu. Mở tệp bằng click phải ra **đồ thị đã có bố cục, màu/nhãn, có tìm kiếm**; không bắt Owner chạy layout/cấu hình bằng tay. Nếu Gephi không qua test "một bấm + full data + privacy", dùng thư viện OSS hiện có (Sigma.js/Graphology) làm một trang HTML cục bộ mỏng, không tự viết engine/server sản phẩm mới, ghi bằng chứng nguyên nhân fallback.

## 3. V5–V8: PROOF/OWNER UAT/HYGIENE
**V5 machine-pass**: (a) hash và số node/edge của 3 lớp/tệp gộp đối soát export; (b) trình duyệt trên Mac mở đúng `OPEN-GRAPH.command`, thấy graph thật/search/click/zoom, ảnh/chứng cứ lưu **Mac local evidence**, không ghi VPS vì #11 RED; (c) localhost only + thử ngoài LAN bị chặn + 0 external data call; (d) 0 Graph writes, invariants/provenance before/after đọc được; (e) đọc health #11 đầu/cuối nếu read-only cho phép, ghi đúng Owner VPSC.
**V6**: MACHINE `KQ XONG` với trạng thái VIEW0 `TECH_READY · OWNER_UAT_OPEN` khi đủ V5, đóng phiên executor/nhả busy ngay. Owner sẽ bấm mở sau đó và chốt UAT riêng; **không giữ session AI/terminal chờ Owner**, không đánh dấu mục tiêu VIEW0 ✅ trước khi Owner nhìn thấy và xác nhận.
**V7**: tránh sa đà cài đặt/đóng gói quá khoảng 15 phút khi chưa chứng minh đường viewer dễ dùng; nếu cần sửa sản phẩm/nhiều đường vòng => `KQ DỪNG` với đúng 1 blocker/giải pháp nhỏ nhất, dọn local temp/process, không đợi.
**V8 optional**: cuối lượt, nếu máy đọc được sổ/receipt đã có **mà không quét toàn VPS hay viết VPS**, kiểm kê sơ bộ GRAPH group ~8,59 GB (P117) theo live image/volume/recovery/trial/evidence và danh sách path/byte/refs. Không xóa/nén/chuyển Drive/repack; ghi `INVENTORY_DEFERRED` nếu không đủ chứng cứ hoặc tốn công. Không gate VIEW0. GS-CLEAN vẫn là node riêng, Owner duyệt exact hash/Drive-first trước xóa thật.

## 4. KQ & ROADMAP
Báo `KQ@GS-VIEW0-MAC-LOCAL-20261011-17 XONG|DỪNG` trong chính Graph COLLAB/root (cùng commit nhả busy), chứng cứ private ở Mac, Git chỉ ghi count/hash/đường sử dụng không tiết lộ user path/PII. Nếu machine XONG thì Bảng phải ghi `TECH_READY OWNER_UAT_OPEN`, không đánh dấu hoàn tất mục tiêu đến khi Owner tự xem.
Sau KQ, Host khôi phục **nguyên byte** R10 từ Git `ebf52956eb740037f9aaf4e217897235dd7cc671`, yêu cầu Claude xác nhận **SHA mới do Git last-touch** theo A6 (không rà lại kiến trúc), Host READY sau VPSC #11 GREEN/Guard 22/22/shared free và câu Owner consent JEV. R10→R10B Owner catalog/APR/real DELTA→GS-CLEAN safe Drive-first→R10C nightly Owner-approved & web link có đăng nhập đã đo→R11 code coverage. Mọi bước khác giữ nguyên, không VPSC/HJW mutation.

## 5. STEP WALK · KHÔNG GIỮ TERMINAL CHỜ
| Bước | Ai | Khi nào | Evidence | Nếu không đạt |
|---|---|---|---|---|
| S0 | Claude Code Mac | Review exact SHA + Host READY + Owner RUN | đúng Mac/source/không conflict | DỪNG trước mutation |
| Export | Claude Code Mac | S0 PASS | 3 lớp đủ + bản gộp/hash/checksum | không có read-only path thì DỪNG |
| Viewer | Claude Code Mac | data PASS | one-click+layout/search/click/full class | Gephi fail → thin OSS fallback hoặc DỪNG |
| V5 | Claude Code Mac | viewer built | local browser/count/privacy/no Graph write | DỪNG chính xác |
| V8 | Claude Code Mac | V5 pass | inventory optional chỉ-read | SKIP, không gate |
| KQ | Claude Code Mac | terminal | XONG machine, OWNER_UAT_OPEN, release busy | NEXT Owner mở màn hình |

**KHÔNG:** SSH ghi VPS tại #11 RED; Neo4j write; APR schema/decision; code ledger/hook Mac Hermes; public graph export/Gephi online; CREATE NEW TASK; giả green; chờ giờ.