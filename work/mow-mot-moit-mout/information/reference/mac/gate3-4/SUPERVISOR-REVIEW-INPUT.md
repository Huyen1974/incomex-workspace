> **Phạm vi lịch sử v1.6.18; điều hành mới ·12/09/2026:** [Bản đồ bước](../BAN-DO-BUOC-UI-AGENT.html) đã nộp PhaB theo chỉ đạo tiếp tục của Owner; còn blocker9hàng nguồn lịch sử. PM v2 đã nhận D04 Owner ACCEPT (nghĩa vai), mở lại Gate1 completeness; Gate2 PARTIAL, Gate3/4 tạm dừng khóa cuối. Các chỉ đạo/nhãn pending phía dưới phản ánh lúc nộp Rev2, không là next action hiện hành. Giữ nguyên kết quả proof; lab đã dọn. Xem README thư mục và SSOT v1.6.20.

# Supervisor review — W005 Revision2 · v1.6.18

Codex kết luận **BLOCKED BY DATA-AUTHORITY**. Đây là self-review; supervisor chỉ kiểm PASS/FAIL theo PM, không phải thiết kế hoặc giao việc. Gate3/4 chưa được nhận; Gate5–7 chưa chạy; O1–O3 NOT VERIFIED. D08 PM quyết family thời lượng; D04 chưa Owner chốt.

PM yêu cầu fresh PG Intent→Draft/WAIT, resume đúng parent/revision, UI generic đọc lại,7 mục đúng owner, machine tests, lifecycle current grants/expiry/revoke/SoD/exact release,177 Pilot facts có nguồn/đường đọc-ghi/version/integrity/provenance và UNKNOWN0, không unqualified NEW_REQUIRED; archive bền và SSOT one-write. Hiện điều kiện DATA FAIL:171 mapping trong LAB,6 UNKNOWN,119 proposal logic chưa production admitted. Không coi đóng theo Pilot là khóa toàn hệ.

## Mười raw files ưu tiên

| File trong ZIP | Dùng kiểm |
|---|---|
| `gate3-4/evidence/03-intent-draft/agent-a-prompt.txt` | Prompt nguyên văn A, không mớm object IDs |
| `gate3-4/evidence/03-intent-draft/agent-b-prompt.txt` | Prompt nguyên văn B |
| `gate3-4/evidence/03-intent-draft/agent-a-transcript.jsonl` | Full tool calls + output A |
| `gate3-4/evidence/03-intent-draft/agent-b-transcript.jsonl` | Full tool calls + output B |
| `gate3-4/evidence/03-intent-draft/pg-before-agents.json` | Catalog và Intent trước fresh run |
| `gate3-4/evidence/03-intent-draft/pg-after-agents.json` | Hai Draft/missing và catalog sau run |
| `gate3-4/evidence/09-data-lock/pilot-data-gap.json` | Counterexample static input403 và thiếu Task/handoff |
| `gate3-4/evidence/07-lifecycle/lifecycle-authority.json` | Requests/receipts authority negatives; ca SoD thực grant bổ sung ở lifecycle-final-checks.json cùng thư mục |
| `gate3-4/evidence/10-handoff/gateway-transcript.jsonl` | Toàn bộ1347 HTTP request/response đã bỏ secrets của lab chính |
| `gate3-4/evidence/09-data-lock/pg-final.json` | Snapshot cuối: current Versions/profiles/evidence/feedback/registry và6 source gaps |

Các file trên là ưu tiên, không thay full evidence theo bước: phase04 giữ prompt/full transcript của hai fresh resume; phase06/07/08/09 giữ từng machine/lifecycle/feedback case, cả lỗi đầu và lần sửa. `03-intent-draft/T0-RUNBOOK-CANDIDATE.md` ghi chuỗi xác định được. Không đọc stderr debug thay cho JSONL tool transcript.

## Chạy lại đầu chuỗi — đã thử trên một lab mới

Từ máy có SSH alias `vps2`, Docker và image cache đúng baseline, Python3, Codex CLI trong PATH đã đăng nhập (dùng model mặc định hiện hành):

```sh
python3 '/Users/nmhuyen/Desktop/quy trình/gate3-4/proof/rev2/replay-head.py'
```

Nếu kiểm từ ZIP đã giải nén, đổi duy nhất đường dẫn gốc tới `gate3-4/proof/rev2/replay-head.py`; giữ cấu trúc `proof/` và `proof/runtime/dependencies.tar.gz`. Lệnh tạo lab có label mới, ghi Intent PG, chạy hai phiên `--ephemeral --ignore-user-config`, lưu prompt/full transcript/snapshots/HTTP và cleanup; không production mutation. Có thể tiêu thụ usage Codex và vài phút lab. Không cần nhập ID nguyên liệu hay chọn tool tiếp theo.

**Lần chạy đã kiểm:** `evidence/replays/proof-g34r2-replay-20260911094208-58c626/`, hai Draft, same refs, hai WAIT, catalog unchanged; cleanup thành công. Đối chiếu nghĩa topology/missing ở `evidence/replays/replay-review.json`. Replay chỉ tái lập đầu chuỗi trên catalog/guard seed ban đầu: không replay bộ readiness/lifecycle/UI mới cuối lượt, không hứa output byte-identical hoặc PASS với mọi model. Join/slot có biến thể biểu diễn; phần canonical C04/profile sửa về sau do harness không được giả nhận là fresh Agent đã tự sửa.

Hash từng file trong `manifest-sha256.json` ở gốc ZIP; mỗi phase giữ manifest tại thời điểm niêm phong. Hash ZIP ở KHO/11-evidence/INDEX và `.zip.sha256`; SSOT byte identity/backup/one-write ở `10-handoff/ssot-write-receipt.json`.

## Năm câu supervisor cần trả lời PASS/FAIL

1. **Fresh head là Agent/tool thật?** Đối chiếu prompt, work entry chỉ actor/PG Intent, tool sequence, catalog/PG before-after và rerun. PASS chỉ cho proof Agent thật trong lab; không suy có production T0 dispatcher hay full autonomous pipeline.
2. **Pilot data đã UNKNOWN0 và mọi proposal đủ authority?** Kỳ vọng từ dữ liệu hiện tại: **FAIL** —177/171LAB/6UNKNOWN;119 logical proposals chưa production acceptance. Kiểm executor≠writer, Task≠Workflow Instance và consumer description≠bound ref.
3. **Lifecycle enforcement thực sự chạy?** Kiểm native requests/denials/PG/no-duplicate, SoD có real grant, expiry/revoke/profile drift và exact release. Chỉ PASS bounded synthetic one-AUTO; không gán nhân sự/thẩm quyền production. Publish không tự activate được kiểm write-target source + receipts riêng, không giả có snapshot giữa hai action.
4. **Evidence/SSOT links bền và có thể mở?** Kiểm9 ZIP lịch sử/hash, current link tới thư mục giải nén trong dự án, external Codex href209→0, backup/342IDs/anchors/one-write/snapshot. ZIP review không chứa lại toàn bộ kho lịch sử; HTML snapshot giữ relative project links, không phải website tự chứa mọi lịch sử.
5. **Có claim nào vượt evidence?** Kiểm báo cáo/SSOT giữ PARTIAL/NOT STARTED, chưa D04 ACCEPT/O1–O3 VERIFIED; UI cần Làm mới; resume phiên thủ công; readiness synthetic; feedback/V2 qua harness; chưa đo lợi ích. Bất kỳ claim vượt các giới hạn này là FAIL, kể cả khi test count đúng.
