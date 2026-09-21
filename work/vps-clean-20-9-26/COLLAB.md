# COLLAB — vps-clean-20-9-26

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: dọn VPS an toàn, không làm hỏng cơ chế hiện tại; tìm nguyên nhân ổ đĩa phình nhanh và đề xuất/xử lý cách chặn tăng trưởng để có chỗ cho công việc tiếp theo (Owner nêu: cài thêm Graph DB).
- Nhiệm vụ/phạm vi: khảo sát trước, không mutation production ở vòng R1; Claude đề xuất, GPT/Codex kiểm chéo kỹ trước khi Owner duyệt bất kỳ dọn/xoá thật nào.
- Tiêu chí xong: xác định được nguồn tăng dung lượng với bằng chứng, có phương án dọn + khoá vòi được kiểm chéo; mọi mutation chỉ diễn ra sau đúng cổng duyệt và có đường rollback/cứu trước xoá.
- Xác nhận User: **ĐÃ XÁC NHẬN** — Owner giao trực tiếp 2026-09-20; D01 và yêu cầu an toàn/kiểm chéo của việc này.

Host: Claude Chat · Host_ID: CLAUDE-VPSC-260920-A · mở việc theo lệnh Owner 2026-09-20
HTML chính: `view.html`

## Dòng hiện hành
VPSC | Dọn đĩa VPS + khoá vòi rò | việc 1/6 mở lại | DRAFT · OWNER STORAGE POLICY mới | NEXT: Host cập nhật A0 + PROMPT/view theo P10, rồi review/READY lại | BLOCK: RUN cũ không còn hiệu lực

- PROMPT hiện hành: `PROMPT.md` · RUN_ID `VPSC-R1-20260920-01` · AUDIT / NO PRODUCTION MUTATION · DRAFT lại do Owner bổ sung chính sách storage 2026-09-21.
- **PROMPT_SHA hiện vẫn = 88ec65875ab3c8f7d5ee98fdb0ae3374cc47ad22**, nhưng chưa phản ánh P10 nên KHÔNG RUN.
- **GPT REVIEW_INVALID@88ec65875ab3c8f7d5ee98fdb0ae3374cc47ad22** — review cũ đúng với scope cũ nhưng mất hiệu lực theo A0 sau khi Owner bổ sung storage policy.
- **Host READY_INVALID@88ec65875ab3c8f7d5ee98fdb0ae3374cc47ad22** — READY cũ mất hiệu lực theo A0; Host phải sửa scope rồi phát SHA/REVIEW/READY mới.

## Số đo gọi thật (Claude Chat, 2026-09-20)
- 24/07: 87% → 61%, trống 13 → 39GB (KB `vps-clean-minimum-2026-07-24.md`).
- 20/09 ~01Z: 83/96GB, trống 14GB · ~12Z: 84/96GB, trống 13GB (+~1GB trong ~11 giờ, trùng lượt build R03 final-close).
- Nhịp TB ~0,45GB/ngày → ~3 tuần chạm 95%.
- Nguồn: `vps_status` resources/containers · `fs_list` gốc code · `query_pg`. Nghi phạm: `view.html` §2.

## Quyết định Owner
- D01 · 2026-09-20 · Mở việc tại `work/vps-clean-20-9-26/`: đánh giá vì sao đĩa VPS đầy nhanh, đề xuất dọn phần không dùng để có chỗ cài Graph DB.
- D02 · 2026-09-21 · Owner chốt nguyên tắc storage: VPS ưu tiên dữ liệu business + working set runtime thực sự cần để chạy. Dữ liệu vận hành không phải business không được tăng vô hạn: cần giữ dài hạn thì offload Google Drive/off-VPS; tái tạo được thì giới hạn TTL/retention rồi purge. `3GB/tháng ngoài business` chỉ là ngưỡng báo động/điều tra, không phải mức tăng được coi là PASS. Owner giao nhóm kỹ thuật tự quyết chi tiết.

## Kế hoạch
- VPSC.1 | Mở việc + PROMPT R1 | ▶ mở lại theo D02/P10; READY `88ec658` đã vô hiệu, chờ Host cập nhật + review/READY mới
- VPSC.2 | Claude Code chạy R1 (kiểm toán, không đụng production) → KB mục ĐỢT 2 nhãn `UNVERIFIED_R1` | □ chưa RUN
- VPSC.3 | Kiểm chéo: Host tự đo lại + lập đề xuất dọn theo nhóm trên `view.html` → GPT (hoặc Codex/Astra do GPT giao) thẩm tra độc lập, PASS/REVISE/BLOCK từng nhóm | □
- VPSC.4 | Owner duyệt các nhóm đã PASS | □
- VPSC.5 | Dọn (cứu trước, xoá sau) + khoá vòi — MỘT PROMPT làm một lần (sửa chính `PROMPT.md`) | □ sau VPSC.4 và R03 CLOSED
- VPSC.6 | Theo dõi 2 tuần theo T1–T5 → đóng; mở việc Graph | □

## Câu hỏi hội đồng
- Q01 · Bằng chứng thô trên VPS, không lên repo. GPT: đồng ý có điều kiện (che secret + giới hạn dung lượng + index). Host: ACCEPT — PROMPT §2 (≤200MB, `INDEX.md`). CLOSED · Áp: c0ddf9e
- Q02 · Báo cáo sửa vào KB 24/07. GPT: đồng ý nếu R1 mang nhãn chưa thẩm tra. Host: ACCEPT — `UNVERIFIED_R1` ở đầu PROMPT + §9. CLOSED · Áp: c0ddf9e
- Q03 · Khoá chéo R03. GPT: đồng ý; mọi dọn/image/tag/rescue/restart có thể ảnh hưởng runtime hoặc rollback chờ R03 CLOSED. Host: ACCEPT — PROMPT §2. CLOSED · Áp: c0ddf9e
- Q04 · OWNER · Đích sau dọn: trống ≥45GB (≤55%) và tăng ≤3GB/tháng ngoài dữ liệu nghiệp vụ. Đề xuất Host: gật (đủ ~1 năm không phải dọn tay).

## Ý kiến
Ghi hộ: GPT gửi P01–P06 qua Owner 2026-09-20 vì đường `workspace_*` của GPT mất giữa phiên; GPT không ghi qua GitHub native (đúng D12). Người góp ý: GPT · Based_on `e50e95c` · đã đọc: AGENTS, README, COLLAB, view, PROMPT, trạng thái R03. GPT xác nhận hoặc sửa lời ghi hộ khi có lại đường ghi.
- P01 · Scope PROMPT đầu + §2 · Đổi "chỉ đọc" thành AUDIT / NO PRODUCTION MUTATION; R1 mang `UNVERIFIED_R1` tới khi kiểm chéo · ACCEPTED · Áp: c0ddf9e
- P02 · Scope Kế hoạch + view §5 · Thêm cổng thẩm tra độc lập Codex/Astra, PASS/REVISE/BLOCK từng nhóm, trước Owner duyệt · PARTIAL: nhận cổng + quyền PASS/REVISE/BLOCK (VPSC.3). Người thẩm tra ghi là Founder không soạn (GPT), GPT được giao Codex/Astra làm thay; không đặt Astra thành vai mới vì AGENTS A2 chưa có vai này — thêm vai là sửa luật nền (cần D ở COLLAB gốc + Owner) · Áp: c0ddf9e
- P03 · Scope PROMPT §5 · Kiểm backup đủ 7 mục; chưa chứng minh → UNKNOWN_HOLD · PARTIAL: nhận 6 mục + UNKNOWN_HOLD. Mục "restore dùng được": R1 KHÔNG diễn tập restore — đĩa 87%, restore tạm cần thêm GB, là việc DR riêng; R1 kiểm không tốn đĩa (sha256 khớp meta, đọc cấu trúc gói mã hoá không giải mã ra đĩa) + dẫn bằng chứng restore gần nhất; cũ hơn 30 ngày → ghi rủi ro, đề xuất diễn tập sau khi dọn · Áp: c0ddf9e
- P04 · Scope PROMPT §2 + §6 · Siết DELETE_PROVEN_SAFE; local-only phải rescue + checksum + cách restore; Nuxt không tag + rollback R03 hard-KEEP · ACCEPTED + bổ sung: R1 ước lượng GB cần cứu và nơi cất NGOÀI VPS — không `docker save` ra chính ổ đang đầy · Áp: c0ddf9e
- P05 · Scope PROMPT §0–§4 · Dừng scan nặng khi Used ≥90% hoặc Available <8GB; evidence ≤200MB; ctime chỉ khoanh vùng; giải thích du≠df · ACCEPTED (+ đối chứng bằng btime `stat -c %W` nếu filesystem hỗ trợ) · Áp: c0ddf9e
- P06 · Scope PROMPT §4 + §9 · Sổ nguồn sinh (Generator Registry) đủ cột, phủ đủ nhóm · ACCEPTED · Áp: c0ddf9e
- P07 · GPT · Based_on `c0ddf9e` · Scope PROMPT §0.1 + §0.4 · ACCEPTED · Không clone repo vào `/tmp`: bản hiện tại vẫn clone trước cả bước đo `df`, vừa tự sinh rác vừa có thể làm nặng thêm ổ đang gần đầy. Đề nghị bước đầu tiên là `df`; đọc repo bằng checkout/mount đã có hoặc đọc remote không tạo clone bền vững. Không có nguồn đọc an toàn thì DỪNG, không tự clone vào `/tmp`. · Host: ACCEPTED — §0 viết lại: đo df là bước 1; không clone; đọc repo bằng `workspace_*` hoặc GitHub đọc-only không lưu file; không đọc clone của đầu nối (có thể cũ); không có đường → DỪNG. Clone chỉ vài MB nhưng để lại là đúng bệnh việc này đang trị. · Áp: 88ec658
- P08 · GPT · Based_on `c0ddf9e` · Scope PROMPT §2 + §9 · ACCEPTED · Raw evidence tuyệt đối không commit/push lên repo public. §2 đã nói KHÔNG đưa lên repo nhưng §9 lại cho phép “evidence thuộc cây git thì commit” — mâu thuẫn. Sửa thành: raw evidence luôn ở ngoài cây Git; nếu phát hiện path evidence nằm trong tracked checkout thì DỪNG/đổi sang path ngoài Git; repo/KB chỉ ghi summary/index đã sanitize, không chứa raw output/secret. · Host: ACCEPTED — bằng chứng thô chuyển ra `/var/lib/incomex-audit/VPSC-R1-20260920/`, kiểm `rev-parse` trước khi ghi, trong cây Git → DỪNG; bỏ câu commit ở §9. Lý do thêm: `/opt/incomex` là cây Git (không remote) nên `evidence/` cũ không đạt. · Áp: 88ec658
- P09 · GPT · Based_on `c0ddf9e` · Scope PROMPT §1e + §6 · ACCEPTED · `DELETE_PROVEN_SAFE` cần gate riêng cho DB; gate hiện tại thiên về Docker/file và chưa đủ để xếp `directus_gov_test_20260602` hay DB/schema vào lớp xoá. Đề nghị thêm `DB_DELETE_GATE`: chứng minh đúng target + owner/size; không có active connection; không app/DSN/cron/job/script nào tham chiếu; không dependency cần giữ; có backup off-VPS phù hợp + checksum + bằng chứng/cách restore; và việc DROP thực tế chỉ ở lượt dọn sau Owner duyệt. Thiếu bất kỳ mục nào → `UNKNOWN_HOLD`, không `DELETE_PROVEN_SAFE`. · Host: ACCEPTED + thêm một phép đo: chỉ số `pg_stat_database` đọc 2 lần cách ≥30 phút (một lần thấy 0 kết nối chưa chứng minh không ai dùng); §1e dẫn thẳng tới gate. · Áp: 88ec658
- P10 · GPT · Based_on `88ec658` + yêu cầu Owner 2026-09-21 · Scope A0 + PROMPT §4/§7/§9 + `view.html` T2/T3 · OPEN · Phải phân biệt **BUSINESS_LIVE / RUNTIME_WORKING_SET / NONBUSINESS_KEEP / DISPOSABLE_REBUILDABLE** cho từng nguồn sinh. Mỗi nguồn phải có: GB hiện tại, tốc độ tăng, có cần local không, local budget/TTL, nơi offload nếu cần giữ, hoặc quy tắc purge nếu tái tạo được. Không đẩy cache/build/log rác sang Drive chỉ để đổi chỗ; Drive/off-VPS dành cho backup/archive/rescue/evidence cần lưu dài hạn, còn active DB/runtime giữ local. Tiêu chí PASS: non-business đạt working set hữu hạn/ổn định qua chu kỳ retention; nguồn nào còn tăng tuyến tính không giới hạn = FAIL dù tổng chưa tới 3GB/tháng. `3GB/tháng ngoài business` hạ thành ngưỡng đỏ bắt buộc điều tra, không phải allowance. Báo cáo phải tách footprint business vs operational và ước lượng steady-state local sau retention/offload. Host cập nhật khối A0, PROMPT và view trước READY mới. · Áp: SAME_COMMIT
GPT đã đọc `AGENTS.md`, `COLLAB.md` và toàn bộ `PROMPT.md@c0ddf9e` cho lượt review trước; lượt P10 đã đọc PROMPT hiện hành `88ec658` và `view.html` T1–T5.

## Owner cần quyết
- Q04 · CLOSED · Owner 2026-09-21 giao nhóm kỹ thuật quyết. Chốt kỹ thuật: giữ mục tiêu ≥45GB trống; bỏ `≤3GB/tháng` khỏi tiêu chí PASS và dùng nó như ngưỡng đỏ. PASS theo D02/P10: non-business phải bounded/steady-state, hoặc offload/purge có kiểm soát.

## NEXT
- **KHÔNG dùng câu RUN cũ.** Host cập nhật khối A0 theo D02, sửa chính `PROMPT.md` và `view.html` theo P10; mọi sửa PROMPT phải phát full SHA mới.
- Vì GPT là người mở P10, sau khi Host sửa: GPT review SHA mới; ACCEPT → Host READY SHA mới → mới phát RUN Claude Code.
- R1 vẫn chỉ AUDIT/NO PRODUCTION MUTATION; không offload/purge/xoá thật trong lượt khảo sát.
