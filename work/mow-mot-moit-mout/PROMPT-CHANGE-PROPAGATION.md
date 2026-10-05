# PROMPT · CODEX · MMIM CHANGE PROPAGATION AUDIT

RUN_ID: MMIM-CHANGE-PROP-20261006-01
PROCESS: CHUNG.APQUYTRINH
EXECUTOR: Codex
MODE: audit + fix current/live only

## Đọc trước
1. `AGENTS.md`
2. `work/mow-mot-moit-mout/HANDOFF-20261001.md`
3. `work/mow-mot-moit-mout/FORMULA-AI-README.md`
4. `work/mow-mot-moit-mout/CHANGE-PROPAGATION.md`
5. `work/mow-mot-moit-mout/CHANGE-IMPACT-MAP.json`
6. tail `COLLAB.md` + `council/REGISTRY.md`
7. `ui/AGENTS.md`

## Mục tiêu
Áp quy trình lan truyền thay đổi cho case vừa xảy ra: **Master UI con chỉ chứa UI con đã OK; bản phác thảo Nhóm cha/Nhóm con chưa duyệt không được canonical hóa.**

### Change Event
```text
CE-20261006-001
TYPE: UI_CHILD_STATUS_CHANGE
ENTITY: Master Nhóm cha / Master Nhóm con
OLD: từng bị đưa thử vào canonical UI child registry/Master UI con
NEW: review-only until Owner approves
STATE: DRAFT
IMPACT_PROFILE: UI_CHILD_DRAFT + STATUS_OR_COUNT_CHANGE
```

## Việc phải làm
1. Quét current/live theo: `UI-030`, `UI-031`, `31/31`, `29/29`, `Đã có UI con`, `bản tạm`, `ML-DEF-018`, `child-ui-registry`.
2. Phân từng hit thành:
   - UPDATE current/live;
   - VERIFY derived;
   - HISTORY preserve;
   - N/A + lý do.
3. Xác nhận canonical hiện hành:
   - `child-ui-registry.json` chỉ có UI đã OK;
   - `ML-DEF-018` phản ánh đủ UI đã OK;
   - Nhóm cha/Nhóm con chỉ là review draft cho tới Owner duyệt.
4. Sửa mọi stale current/live còn sót; **không sửa lịch sử D142/D143 thành như chưa từng xảy ra**.
5. Kiểm live:
   - `danh-muc-ui-con-v1.html`;
   - `definition-master-v1.html?stt=18`;
   - `definition-master-index-v1.html`;
   - `master-design-review-v1.html`;
   - Master Nhóm cha/Nhóm con.
6. Rà luôn xem process này còn thiếu target nào; nếu có, cập nhật `CHANGE-IMPACT-MAP.json` / `CHANGE-PROPAGATION.md` trong cùng lượt.
7. Ghi COLLAB:
   `KQ@MMIM-CHANGE-PROP-20261006-01 XONG`
   hoặc `KQ@... DỪNG · <blocker>`.

## Cấm
- Không tạo UI con mới.
- Không duyệt thay Owner.
- Không cấp lại UI-030/UI-031.
- Không đổi concept/công thức.
- Không rewrite KQ lịch sử.
- Không tạo danh sách song song.

## PASS
- canonical UI child count và ML-DEF-018 khớp;
- zero stale current/live reference coi Nhóm cha/Nhóm con là UI con approved;
- review pages vẫn mở được;
- tất cả target impact map PASS/N-A có lý do;
- báo cáo ngắn: files changed + URLs + stale hits fixed + remaining OPEN.
