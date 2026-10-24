# PROMPT — GS-C1D-FIX-RECOVERY-20261024-11
RUN_ID: GS-C1D-FIX-RECOVERY-20261024-11
TASK: work/graph-server · C1-D-FIX đúng một lỗi D23, KHÔNG chạy lại C1-D.
STATUS: DRAFT_NOT_READY; chỉ READY khi GPT Host ký đúng full SHA commit cuối chạm PROMPT.md và SHA256, Owner tự dán một RUN cho Claude Code CLI. KHÔNG tự RUN/C1-E.
READ: AGENTS.md A0/A4/A5/A6; COLLAB.md §0.0, §1–3, D19/D20/D25, P231–P234; tools/c1d/graph-refresh.c1d.diff, c1d_apply.py; runtime VPS là nguồn kiểm cuối. Claude P233 commit 822672c827b9b692e5469fe9dbf499e76729f805.

GOAL D25 OWNER 24/10: Graph phải không âm thầm bỏ sót những biến đổi liên quan đối tượng/cạnh để chương trình khác dùng quyết định. C1-D-FIX chỉ khép lỗ recovery gây kẹt cập nhật đêm sau; KHÔNG chứng nhận all-change coverage. 49/100 ô ĐỦ là scoped; 0/9 source families FULL. Nguồn không có lịch sử biến động liên tục vẫn MỘT PHẦN/UNKNOWN, query NOT_ACTION_SAFE khi cần ô đó. Không lấy nâng ngưỡng cảnh báo làm cấp giấy xanh.

SCOPE: Chỉ sửa atomicity/rollback local recovery point D23; gia cố c1d_apply; đọc báo cáo lượt 2026-10-23T22:40Z; Guard, thử lỗi; conditional floor 29→45. Không lane/timer/service/monitor mới, không Neo4j tạm, không xóa Graph; không sửa PG/Directus/Lark/Qdrant hay WAL/CDC/Kafka/Debezium, không triển khai code Git→VPS ngoài apply-v0 có thẩm quyền, không dừng timer, không C1-E. D20 giữ nguyên, không làm hộ VPSC/HJW/JEV.

S0 READ-ONLY + FAIL-CLOSED:
1. Kiểm exact Host READY PROMPT last-touch SHA40/SHA256, Owner manual consent đúng RUN_ID, no STOP/COUNCIL_ALERT, identity, cờ VPS-GHI, prior KQ; kiểm code runtime và patch diff, nguồn và điểm D23 live, INV/PINS/SOURCES/RECMAN/cross-edges. Không giả định repo = VPS.
2. Đọc original systemd journal/report lượt tự nhiên 23/10 22:40Z (= 24/10 05:40 +07): PASS/SKIP/FAIL, các lane DELTA/NO_CHANGE, cross-edges 70 kỳ vọng và thực tế, L2 tuổi, canary, trạng thái #24, nghĩa mã b74b06c34a và 6dc111a427. Không có quyền đọc: đánh dấu UNVERIFIED, không giả PASS, không nâng floor nhờ nhật ký đó.
3. Fresh Guard PRE 22/22, Config Guard CLEAN, disk #11/memory/swap, VPS-GHI free và held_by_run kiểm lại, D23 restore khả dụng, active local point == recovery-manifest identity/epoch/hash. Nếu lệch => RED/DỪNG sạch, ZERO protected writes; không tự ghi point để che mismatch. Gate đỏ/unknown => KQ DỪNG, nhả lease, không WAIT.

A. SỬA NHỎ "STAGE → COMMIT" D23:
4. Giữ byte old active point = PRE. Tạo new recovery point trong tên staging, không thay active; dùng chuẩn ghi tệp bền/kiểm hash sẵn có. Apply Graph F, invariants/pins, sources, recovery-manifest và cross-edges qua cơ chế hiện tại; verify chúng cùng thế hệ; CHỈ SAU tất cả thành công mới atomic rename/commit local active point. Nếu bất kỳ bước nào thất bại, gồm việc chốt active point, rollback Graph/INV/PINS/SOURCES/RECMAN/cross-edges về PRE + xóa staging, active point vẫn byte PRE. Không để reader gắn nhãn ĐỦ trên nửa trạng thái.
5. Dùng CÙNG core function với đường production trên Graph GIẢ/fixture có trạng thái: lỗi giả F1 sau tạo staged point; F2 sau apply recovery-manifest trước commit active; F3 mismatch active point/manifest từ PRE. F1/F2: Graph/INV/PINS/SOURCES/RECMAN/cross-edges/active point phải byte-exact PRE; không staging/lease sót; lượt kế tiếp tự chạy được không cần người. F3: RED + 0 mutation. Không Neo4j tạm, không PASS nếu mock bỏ qua core.
6. Gia cố c1d_apply: clone timeout <=5 phút; ngay trước protected write xác minh held_by_run == RUN_ID; thiếu/quá hạn => DỪNG và nhả cờ. apply-v0 theo Điều 30/31 + Config Guard/sổ mã, dry-run/rehearsal rollback, 1 cửa sổ ghi ngắn. Tránh 22:30–23:00Z, không pause/ép timer.

B. POST + FLOOR:
7. Chỉ nếu A PASS, journal S0 có receipt đủ, 16 ô L1 PG có source-native↔Graph ID+edge oracle độc lập và Guard POST PASS thì đổi `certified_floor` 29→45 cho mốc chuông. KHÔNG đổi giấy N4/claim source; 4 ô hạ tầng chờ thêm một natural tick ĐỦ. Thiếu bằng chứng => giữ 29, PARTIAL có lý do, không xem là FAIL của A khi A đạt.
8. Kiểm fresh Guard POST, Config Guard CLEAN, #11/#24 thực đo, original timer ON, Graph/checkpoint/manifest cùng version, reader N4 fail-closed, 0 volume/Neo4j/fixture sót, VPS-GHI RELEASED; no background.
9. KQ: PRE/POST version/commit + nhật ký S0 PASS/SKIP/UNVERIFIED, receipt lỗi giả F1/F2/F3, bảy nhóm byte PRE, apply-v0 và lùi, sàn 29/45 với điều kiện, active point/manifest, natural timer, Guard #11/#24, lease, 49/100 scoped hoặc số thật, 0/9 families FULL, owner backlog. Không tuyên PASS ở tầng chưa đo.

GIAO CHỦ, KHÔNG LÀM TẠI GRAPH RUN: VPSC bổ sung mẫu `incomex_graph_v1_rc_*` vào sổ dung lượng nhưng không bỏ qua disk thật; chủ JEV kiểm đèn #19 DOWN 00:18Z; HJW kiểm 2 units; Graph ghi G9 `work/*` ở backlog. Sau FIX chỉ thiết kế/đo C1-D-CONTINUITY: source contract và durable event cursor vs snapshot/counter, create/update/delete/đổi cạnh, độ trễ/gap, native oracle, downstream NOT_ACTION_SAFE. Đề xuất PG CDC/đổi schema riêng Owner/D20 nếu thật cần, không tự bật.

OWNER MANUAL DISPATCH — sau Host READY exact SHA: "Tôi đồng ý chạy duy nhất GS-C1D-FIX-RECOVERY-20261024-11 theo PROMPT READY do GPT Host ký; S0 không đủ thì DỪNG, không chạy C1-E."
