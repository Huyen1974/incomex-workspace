# COLLAB — vps-clean-20-9-26

Việc: đĩa VPS đầy lại nhanh sau đợt dọn 24/07 → tìm vòi rò, dọn phần không dùng, khoá vòi, chừa chỗ cho Graph.
Host: Claude Chat · Host_ID: CLAUDE-VPSC-260920-A · mở việc theo lệnh Owner 2026-09-20
HTML chính: `view.html`

## Dòng hiện hành
VPSC | Dọn đĩa VPS + khoá vòi rò | việc 1/6 | DRAFT (đã sửa theo P01–P06) | NEXT: GPT review lại PROMPT_SHA mới | BLOCK: GPT mất đường ghi `workspace_*` (phía client; container agent-data vẫn healthy, không restart) → GPT trả lời qua Owner

- PROMPT hiện hành: `PROMPT.md` · RUN_ID `VPSC-R1-20260920-01` · AUDIT / NO PRODUCTION MUTATION · DRAFT.
- **PROMPT_SHA = c0ddf9e3a0e85952375bd0f986903e94c81a35fe** (commit cuối chạm `PROMPT.md`; REVIEWED/READY theo đúng mã này). Bản `e50e95c` hết hiệu lực.

## Số đo gọi thật (Claude Chat, 2026-09-20)
- 24/07: 87% → 61%, trống 13 → 39GB (KB `vps-clean-minimum-2026-07-24.md`).
- 20/09 ~01Z: 83/96GB, trống 14GB · ~12Z: 84/96GB, trống 13GB (+~1GB trong ~11 giờ, trùng lượt build R03 final-close).
- Nhịp TB ~0,45GB/ngày → ~3 tuần chạm 95%.
- Nguồn: `vps_status` resources/containers · `fs_list` gốc code · `query_pg`. Nghi phạm: `view.html` §2.

## Quyết định Owner
- D01 · 2026-09-20 · Mở việc tại `work/vps-clean-20-9-26/`: đánh giá vì sao đĩa VPS đầy nhanh, đề xuất dọn phần không dùng để có chỗ cài Graph DB.

## Kế hoạch
- VPSC.1 | Mở việc + PROMPT R1 | ▶ đã sửa theo P01–P06, chờ GPT review lại
- VPSC.2 | Claude Code chạy R1 (kiểm toán, không đụng production) → KB mục ĐỢT 2 nhãn `UNVERIFIED_R1` | □ sau REVIEWED + READY + RUN
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
GPT còn một vòng phản biện (A5) cho P02, P03.

## Owner cần quyết
- Q04 · Đích sau dọn ≥45GB trống + ≤3GB/tháng. Đề xuất: gật.

## NEXT
- GPT đọc lại `PROMPT.md` ở SHA mới (diff từ `e50e95c`): ghi `GPT REVIEWED@<full SHA> · ACCEPT` hoặc phản biện P02/P03. Chưa có lại đường ghi → trả lời qua Owner; Host ghi `GPT REVIEWED@<SHA> · qua Owner` (nguyên văn), rồi `READY@<SHA>`.
- Sau READY: Owner (hoặc GPT trong phạm vi Owner giao) RUN.
