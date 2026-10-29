# Guard and closure

VPS-GHI acquired by CAS with STARTED commit `03ef7cff2053ee02a6b9ccfb4a15d13a65f3dd3f`, 10:28Z; returned with P468/KQ at 10:47Z. Production untouched.

PRE: `/tmp/hjw-run16-guard/guard-pre-HJW-RUN16-20261029T102821Z.json` PASS.

POST1 retained: `/tmp/hjw-run16-guard/guard-post-HJW-RUN16-20261029T104013Z.json` FAIL because transient existing scheduled container `dot-directus-license-1618062` appeared in snapshot footprint without coverage. Subsequent read-only inspect found it already gone. Existing root COLLAB records this scheduled Directus checker; no changes made to it. No invented coverage, allow flag or new baseline.

Final POST: `/tmp/hjw-run16-guard/guard-post-HJW-RUN16-FINAL-20261029T104645Z.json` PASS against the SAME original PRE; footprint zero, same-or-better PASS with PREEXISTING_SAME #24. Hermes/Gemini/ACL/code-ledger checks pass.

Worktree `/tmp/hjw-g8-fs-helper-20261029-16` clean before removal; lab `/tmp/hjw-run16-lab` removed, no RUN16 containers remain. No background jobs/terminal awaiting Owner. Git release ref, final candidate image and original pinned images retained; Guard JSON retained for traceability.

## Exact final Guard output

```text
00452246b1ac499d2e62cba8ea12be2aee919f2b
7e3c04967d054e7a40877d00c264aaee623546d1
  INV1.ruleset                        PASS  PASS (cached 17:06 29/10, age 39m <= 120m) · id/enforcement/target/~ALL/4 rules/updated_at match
  INV2.gpt_full_all_2                 PASS  tools=37 hash=dbbfc590a969 caps=ok · e2e ref workspace_read=ok
  INV3.claude_surface                 PASS  tools=23 fp=4f1000e9aad3 caps=ok · e2e ref fs_read=ok
  INV7.hermes                         PASS  tools=7 e2e=ok badkey=401 AGENT_DATA_env=0
  INV24.gemini                        PASS  vps tools=23 e2e=ok badkey=401 · google-main tools=37 e2e=ok
  INV10.pending_records               PASS  pending=0 stuck=[]
  INV10.clone_remote_drift            PASS  clones hold nothing unconfirmed; snapshots on the remote line
  INV5_6.health_routes                PASS  gateways healthy, helper alive + write path ok, config-guard CLEAN, routes 200
  INV11.mcpw_switches                 PASS  lifecycle.mode=audit · legacy_master=enforce
  INV12.lifecycle_snapshot            PASS  age 109 s · 10 tasks/45 rows · red=0 · ssh_unknown=88
  INV13.owner_view_labels             PASS  6/6 marks (423496 B)
  INV14.hermes_client_backend_compat  PASS  serve+gateway @ bf0203a794 · Mac @ bf0203a794 (09:49 24/10)
  INV15.kuma_telegram_coverage        PASS  đường giám sát khoẻ · fleet 32/32 · up=31 · đều gắn Telegram #2 · lịch Disk/Guard đúng · bảng đèn 320 s · đèn dịch vụ đỏ (không tính vào #22): #24
  CTR-WATCHDOG-01                     PASS  the mutant pending record is caught
  INV18.web_incomex                   PASS  {"watch": "PASS", "namespace": "web_incomex", "published": 27, "routes": 6, "runtime_files": 1876, "source_files": 233, "watchdog": "mutant rejected", "errors": []}
  INV19.hjw_contract                  PASS  chỉ Host giao · quét việc mở · write trong việc · vé gắn file · đối chiếu phạm vi · AUTO rỗng · handoff nghỉ · máy ghi hộ kết quả (chặn dấu máy/thiếu STATUS) · một bộ điều phối · NEXT (23 phép nghĩa) · gate root:hermes 640 · khoá Hermes ≤ 7 tool · ghi work/*/COLLAB.md · guard hậu ảnh 11 phép · đọc đúng ""+TQT · hai cổng: 0 sudo · 13 đường credential đóng · gcloud rỗng · 0 biến Google · 0 docker
  INV20.connector_twin_sync           PASS  PASS agent-data cloud=release 2b14c2a (nguồn đi trước 1 commit chưa phát hành) · lark lark-n1-1 24 tool · web 37/24 · Mac khớp (thấy lần cuối 29/10 10:26Z)
  INV21.owner_view_goal_flow          PASS  10 việc đang làm đọc được mục tiêu · đồng bộ 90 s trước
  INV22.graph_v1                      PASS  graph-v1 PASS · running/healthy rc=0 · loopback 17474/17687 · auth+invariants 2438s trước
  INV23.code_ledger                   PASS  bề mặt 603 tệp đều trong sổ · UNKNOWN 3 vùng không quét: bind-ro:incomex-claude-mcp:/var/lib/incomex-mcp-helper/queue; bind-ro:incomex-gemini-mcp:/var/lib/incomex-mcp-helper/queue
  INV25.github_ci_runners             PASS  agent-data-test: connected/limits PASS; web-test: connected/limits PASS
  INV16.tin_bao_diem_danh             PASS  TIN BÁO 2026-10-29T10:40:02Z: 86 loại · 84 chạy · 0 hỏng · 2 chưa xác định
  C3 baseline: PRE v2 · FOOTPRINT 0 mục: 
  C3.footprint_coverage               PASS  0 mục · đủ 4 ô
  C3.same_or_better                   PASS  PREEXISTING_SAME #24
  C3.change_event                     PASS  nhóm EVENT so PRE: 4 nhóm
  saved /tmp/hjw-run16-guard/guard-post-HJW-RUN16-FINAL-20261029T104645Z.json
GUARD POST HJW-RUN16-FINAL: PASS
```
