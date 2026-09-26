# PROMPT — HJW CONTROL C · Approval trust boundary

RUN_ID: HJW-CONTROL-C-20260926-03
STATUS: Chỉ thực thi sau READY/RUN mới của Host.
Host: GPT Chat · GPT-HJW-260922-A
Executor_Surface: Claude Code CLI phiên mới trên Mac Owner.
Report_Write_Path: gateway `workspace_*`/`fs_*`; chỉ file HJW hiện hữu.
Runtime_Write_Path: SSH/operator VPS hiện hữu; mã/runtime VPS là SSOT.
Căn cứ: P45 KQ Pha A XONG; P43/P44 đường giả duyệt; DROOT22; Điều 30/31.
JEV Host: `gen-dec-1790396378-h4XGdkVnURY99UxKdvnV` — chọn audit+conditional-apply bằng cơ chế cách ly sẵn có = 1,00; Pha B tiếp tục chặn.

## 0. Đích

Đóng duy nhất blocker còn lại trước Pha B:

> Không một phiên Hermes/LLM nào — Telegram, Desktop, cron/job hay session khác — được có khả năng tự ghi/giả trạng thái Owner approval.

Ưu tiên tuyệt đối:
1. dùng toolset/profile/sandbox/cấu hình **sẵn có của Hermes**;
2. không dựng service/store/bot mới;
3. không vá core Hermes;
4. không giảm công cụ chat Owner nếu chưa chứng minh không còn cách giữ nguyên năng lực hiện tại.

Pha C KHÔNG bật plugin approval production, KHÔNG gửi thẻ thật, KHÔNG gọi model Hermes, KHÔNG mở one-shot, KHÔNG restart ngoài đúng thành phần cần thiết nếu có apply config an toàn.

Pha B chưa READY/RUN.

## 1. Reuse evidence

Không audit lại P41/P45 từ đầu. Đọc:
- `/opt/incomex/work/hermes-joint-workspace/HJW-CONTROL-20260926-01/G0.md`
- `.../phaseA/EVIDENCE-A.md`
- P43–P45 trong HJW COLLAB.

Revalidate:
- Hermes code/version hiện hành còn là baseline P45; nếu safe-update đã áp bản mới thì chỉ rerun fixture A2/A4/A5 liên quan trước kết luận;
- `ws-dispatch` vẫn `no_agent`, one-shot vẫn hard-disabled;
- 0 Hermes ASSIGN open/claimed;
- Guard/Kuma/P02 healthy.

## 2. Audit trust boundary thật

Kiểm trực tiếp source/config/runtime của Hermes, không suy từ docs:
- interactive Telegram Owner chat toolset/profile;
- Desktop/serve interactive profile;
- cron/job toolset `incomex-workspace`;
- plugin execution context;
- terminal/shell tool implementation: user, cwd, allowed paths, sandbox, mount/namespace/chroot/bwrap/container nếu có;
- ai có thể write `notepad.db`, `~/.hermes/plugins`, config/plugin state và lifecycle records.

Lập ma trận:
`surface/session → toolset → unix identity → can_write_approval_store? → can_write_plugin? → can_run_terminal? → expected_after`.

Không in secret/token/env values.

## 3. Preferred solution — isolate approval without reducing Owner chat capability

Tìm và ưu tiên cơ chế sẵn có có thể đồng thời:
- interactive Owner chat vẫn giữ các công cụ hợp lệ hiện tại;
- nhưng **mọi LLM-executed terminal/server-write path không thể chạm approval state/plugin control state**;
- callback Owner thật từ Telegram adapter/plugin vẫn có thể ghi decision thông qua đường không do LLM điều khiển;
- one-shot Hermes job chỉ có 7 tool workspace, không terminal;
- approval consume vẫn atomic theo P45.

Ứng viên hợp lệ nếu có sẵn: per-tool sandbox, path deny/allow, namespace/mount read-only, restricted execution profile, per-platform toolset override, dedicated non-LLM callback context, permission hook trước terminal dispatch.

Nếu tìm được:
- chứng minh bằng fixture trước;
- chỉ apply cấu hình/hook sẵn có;
- backup/rollback trước;
- restart tối thiểu đúng service bị ảnh hưởng nếu bắt buộc;
- không restart nginx/Agent Data/P02;
- sau apply chạy negative tests mục 5.

Nếu giải pháp làm giảm tool chat Owner hoặc thay semantics terminal Owner => DỪNG trước apply và sang §4.

## 4. Nếu không thể giữ nguyên năng lực Owner chat

KHÔNG tự cắt tool.

Ghi đúng:
`KQ@HJW-CONTROL-C-20260926-03 DỪNG · OWNER_CAPABILITY_DECISION_REQUIRED`

và đưa tối đa 2 phương án:
A. bỏ/giới hạn nhóm terminal/server-write khỏi Hermes Telegram/Desktop interactive sessions;
B. một cơ chế trust boundary khác chỉ khi dùng **thành phần hiện hữu** đã tìm thấy.

Mỗi phương án nêu:
- mất gì;
- giữ gì;
- rollback;
- phạm vi ảnh hưởng;
- vì sao cần.

Không dựng root-owned service/store mới trong RUN này.

## 5. Acceptance C1–C9

C1. Approval state/plugin control state không writable bởi bất kỳ LLM-capable interactive Hermes session nào.
C2. Owner callback path hợp lệ vẫn ghi được decision mà không thông qua LLM.
C3. One-shot job profile = đúng 7 workspace tools, không terminal/server-write.
C4. Telegram/Desktop Owner chat baseline capabilities không giảm nếu RUN ghi XONG.
C5. Fake approval attempts từ interactive session bị DENY ở filesystem/tool boundary; không chỉ app-level check.
C6. Approval ticket duplicate/replay/expired/generation cũ vẫn không chạy.
C7. `ws-dispatch` no_agent + one-shot hard-disabled giữ nguyên trong Pha C.
C8. Guard/STOP/Kuma/P02/Agent Gateway/Telegram hiện hữu không regression.
C9. Rollback phục hồi chính xác config/tool policy; rollback không mở lại one-shot/fail-open.

Test nhạy cảm/repro chỉ ở hồ sơ VPS root-only; repo public chỉ summary.

## 6. Output

PASS chỉ khi C1–C9 đạt:
`KQ@HJW-CONTROL-C-20260926-03 XONG`

Kèm trong HJW COLLAB:
- trust-boundary mechanism đã dùng;
- surfaces đã test;
- Owner chat capability giữ nguyên;
- diff runtime;
- rollback;
- Hermes version baseline.

DỪNG nếu:
- phải vá core;
- phải dựng service/store mới;
- phải giảm Owner chat capability;
- không chứng minh filesystem/tool-boundary deny;
- update Hermes làm invalid fixture mà chưa rerun.

Sau XONG, Host mới soạn Pha B: D4 checkpoint/Kuma + D5 enable plugin/restart gateway + một thẻ Telegram thật.

Không update Hermes trong RUN này. Không chạy `hermes-safe-update apply --reviewed`. Không phát assignment Hermes. Không gọi model Hermes.
