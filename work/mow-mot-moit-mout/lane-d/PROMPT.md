# PROMPT — LANE D01 · Evidence map cho case Tạo mới MOW

RUN_ID: MMIM-LANE-D01-20260928-01
PROCESS: CHUNG.TIM
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path: chỉ `work/mow-mot-moit-mout/lane-d/COLLAB.md`.
Mọi canonical/UI/process/tool khác: READ-ONLY.

## 0. Registry
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-D phải đúng D01 + Reserved_Targets.
Không sửa Registry.

METHODOLOGY_TOPIC thuộc Chat.2:
- mô hình phân tầng;
- câu hỏi bắt buộc theo tầng;
- reuse/create/gray-zone/confidence/evidence method;
- cách chứng minh reliability.
D01 **không thiết kế** các nội dung trên.

## 1. Câu hỏi duy nhất
Với case hiện có **Tạo mới một MOW**, repo hiện đã có những bằng chứng gì ở từng độ sâu?

Không invent layer model mới. Chỉ dùng các tầng/đối tượng đã tồn tại trong source:
`MOW → MOT / process con → MOIT / MOUT → Field`
và các Shared process thật sự được gọi.

## 2. Với mỗi tầng/đối tượng, chỉ trích xuất facts
Tối đa các cột:
- Object / phạm vi
- Existing source/process code
- Input đã có
- Decision/question **đã thực sự ghi trong source**
- Search/check process đang có
- Tool/DOT/JEV/checker đang có
- Data/catalog được đọc
- Output/record được ghi
- Evidence hiện có
- Status: PROVEN / PARTIAL / ABSENT
- Gap: một câu

Nếu source không có câu hỏi/process/tool → ghi ABSENT. Không tự bổ sung câu hỏi “nên có”.

## 3. Nguồn bắt buộc
- MOW.TAO + CHUNG.* được gọi trong `ban-duyet.html#ml5-cho-ai`
- 23 contract-v1 hiện có
- B01 overlap/gap evidence
- B02R1/B03 KQ
- 4 Mother baseline liên quan
- CAT-003/CAT-004/CAT-006/CAT-235* khi liên quan
- `cong-cu/` và tool catalog
- Council Registry chỉ để tránh overlap

## 4. Output nhìn cái hiểu ngay
Mặt đầu ≤12 dòng:
`Tạo MOW → MOW → MOT → MOIT/MOUT → Field`
mỗi tầng ghi:
`evidence có / thiếu / source chính`.

Chi tiết dưới bằng bảng facts. Không kết luận phương pháp nào “đúng nhất”.

## 5. Acceptance
- Không sửa canonical/UI.
- Mỗi fact có source path/anchor/hash/version nếu đọc được.
- Phân biệt rõ `repo đã có` với `chưa có`.
- Không chuyển gap thành recommendation methodology.
- KQ dùng được như input cho Chat.2.

## 6. KQ
`KQ@MMIM-LANE-D01-20260928-01 XONG|DỪNG`
`KQ@LANE-D D01 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS|BLOCK · levels=<n> · proven=<n> · partial=<n> · absent=<n> · NEXT=CHAT2_REVIEW`
`COORD · NOW=XONG|DỪNG · NEXT=CHAT2_REVIEW · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-d/COLLAB.md · LAST_SYNC=D79/D01`

Dừng.
