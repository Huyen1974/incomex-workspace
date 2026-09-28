# PROMPT — LANE E01 · Audit năng lực kiểm “đã có / dùng lại / tạo mới”

RUN_ID: MMIM-LANE-E01-20260928-01
PROCESS: CHUNG.TIM
STATUS: Chỉ chạy sau PROCESS_GATE PASS + READY của Host.

Host: GPT Chat · Host_ID `GPT-MMIM-260920-A`
Executor_Surface: Codex
Write_Path: chỉ `work/mow-mot-moit-mout/lane-e/COLLAB.md`.
Canonical/UI/tools: READ-ONLY.

## 0. Registry
Đọc `../council/REGISTRY.md` READ-ONLY.
Entry CODEX-MMIM-E phải đúng E01 + Reserved_Targets.
Không sửa Registry.

METHODOLOGY_TOPIC thuộc Chat.2. E01 không tạo confidence threshold, gray-zone policy, layer model hay quyết định reuse/create.

## 1. Câu hỏi duy nhất
Hiện tại hệ thống **thực sự có những khả năng kiểm nào** để hỗ trợ câu hỏi:
`đã có? giống bao nhiêu? dùng lại được không? cần tạo mới không?`

Chỉ inventory capability/evidence, không quyết policy.

## 2. Kiểm các nhóm hiện có
- exact code/name duplicate checks
- `CHUNG.TIM` search contract + coverage outcomes
- K11 semantic overlap status
- JEV integration: dùng ở đâu, output gì, giới hạn gì
- DOT/checkers/scripts trong `cong-cu/`
- Tool catalog CAT-006 / K01–K18
- process gate / walk check
- UI/search surfaces nếu chúng cung cấp evidence
- Graph/PGVector chỉ ghi nếu repo task này có evidence thật liên quan; không kéo kiến thức ngoài.

## 3. Mỗi capability ghi
- name/code
- what it can prove
- what it **cannot** prove
- input required
- output/evidence
- deterministic / probabilistic / human-dependent
- latest tested status
- source/file/tool
- missing evidence
- suitable for: exact existence / candidate retrieval / semantic overlap / reuse suitability / final yes-no
- confidence number nếu source thật có; không tự đặt threshold

## 4. Vùng xám
Chỉ liệt kê:
- hiện source có threshold/policy nào;
- nếu không có → `POLICY_ABSENT`.
Không đề xuất 50/75 hay policy mới.

## 5. Output
Mặt đầu ≤10 dòng:
`Có thể chứng minh chắc: ...`
`Chỉ tạo candidate/probability: ...`
`Chưa chứng minh được: ...`

Chi tiết matrix bên dưới.

## 6. KQ
`KQ@MMIM-LANE-E01-20260928-01 XONG|DỪNG`
`KQ@LANE-E E01 · PROCESS=CHUNG.TIM · PROCESS_GATE=PASS|BLOCK · capabilities=<n> · deterministic=<n> · probabilistic=<n> · policy_absent=<n> · NEXT=CHAT2_REVIEW`
`COORD · NOW=XONG|DỪNG · NEXT=CHAT2_REVIEW · BLOCKED_BY=<...> · RESERVED_TARGETS=lane-e/COLLAB.md · LAST_SYNC=D79/E01`

Dừng.
