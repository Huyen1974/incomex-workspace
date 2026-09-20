# COLLAB — vps-clean-20-9-26

Việc: đĩa VPS đầy lại nhanh sau đợt dọn 24/07 → tìm vòi rò, dọn phần không dùng, khoá vòi, chừa chỗ cho Graph.
Host: Claude Chat · Host_ID: CLAUDE-VPSC-260920-A · mở việc theo lệnh Owner 2026-09-20
HTML chính: `view.html`

## Dòng hiện hành
VPSC | Dọn đĩa VPS + khoá vòi rò | việc 1/5 | DRAFT | NEXT: GPT review PROMPT.md | BLOCK: —

- PROMPT hiện hành: `PROMPT.md` · RUN_ID `VPSC-R1-20260920-01` · khảo sát CHỈ ĐỌC · DRAFT.
- PROMPT_SHA: SAME_COMMIT (Host ghi hash thật ngay sau commit mở việc).

## Số đo gọi thật (Claude Chat, 2026-09-20)
- 24/07: 87% → 61%, trống 13 → 39GB (KB `vps-clean-minimum-2026-07-24.md`).
- 20/09 ~01Z: 83/96GB, trống 14GB · ~12Z: 84/96GB, trống 13GB (+~1GB trong ~11 giờ, trùng lượt build R03 final-close).
- Nhịp TB ~0,45GB/ngày → ~3 tuần chạm 95%.
- Nguồn: `vps_status` resources/containers · `fs_list` gốc code · `query_pg`. Nghi phạm: `view.html` §2.

## Quyết định Owner
- D01 · 2026-09-20 · Mở việc tại `work/vps-clean-20-9-26/`: đánh giá vì sao đĩa VPS đầy nhanh, đề xuất dọn phần không dùng để có chỗ cài Graph DB.

## Kế hoạch
- VPSC.1 | Mở việc + PROMPT khảo sát chỉ đọc | ▶ chờ GPT review
- VPSC.2 | Claude Code khảo sát chỉ đọc → báo cáo KB | □ sau REVIEWED + READY + RUN
- VPSC.3 | Host tự đo lại số của Agent → danh sách dọn vào `view.html` → Owner duyệt | □
- VPSC.4 | Dọn (cứu trước, xoá sau) + khoá vòi, MỘT PROMPT làm một lần (sửa chính `PROMPT.md`) | □ sau Owner duyệt và R03 CLOSED
- VPSC.5 | Theo dõi 2 tuần theo T1–T5 → đóng; mở việc Graph | □

## Câu hỏi hội đồng
- Q01 · Bằng chứng thô để đâu? Đề xuất Host: trên VPS `/opt/incomex/evidence/VPSC-R1-20260920/`, KHÔNG đưa lên repo — repo công khai, bằng chứng chứa đường dẫn/tên dịch vụ nội bộ. Repo chỉ giữ COLLAB/view/PROMPT.
- Q02 · Agent báo cáo ở đâu? Đề xuất Host: sửa vào KB có sẵn `knowledge/current-state/reports/vps-clean-minimum-2026-07-24.md`, chèn mục "ĐỢT 2" lên đầu — một tài liệu, không tạo tài liệu KB mới.
- Q03 · Khoá chéo R03? Đề xuất Host: R03 chưa CLOSED thì image đang chạy + tag rollback R03 = KEEP; VPSC.2 chỉ đọc nên chạy được ngay (không deploy, không phá băng backend); VPSC.4 xoá thật chờ R03 CLOSED.
- Q04 · OWNER · Đích sau dọn: trống ≥45GB (≤55%) và tăng ≤3GB/tháng ngoài dữ liệu nghiệp vụ. Đề xuất Host: gật (đủ ~1 năm không phải dọn tay).

## Ý kiến đang mở
- —

## Owner cần quyết
- Q04 · Đích sau dọn ≥45GB trống + ≤3GB/tháng. Đề xuất: gật.

## NEXT
- GPT đọc `AGENTS.md` → file này → `view.html` → `PROMPT.md`; tạo Pxx hoặc ghi `GPT REVIEWED@<full SHA> · ACCEPT`, kèm trả lời Q01–Q03.
- Hết P OPEN: Host ghi `READY@<full SHA>`; Owner (hoặc GPT trong phạm vi Owner giao) RUN.
