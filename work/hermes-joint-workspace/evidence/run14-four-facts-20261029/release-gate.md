# RUN14 release gate — DỪNG trước advertise

## Một blocker chính
G8: RUNTIME_CANONICAL_RELEASE_DIVERGENCE. Candidate từ đúng runtime P452 đã kiểm, nhưng thay nguyên byte vào source canonical sẽ bỏ những phần ngoài phạm vi RUN14. Không tự promote/deploy một bản vừa thay policy khai danh vừa đổi consumer/quyền của hệ thống khác.

Bằng chứng trực tiếp từ `git diff --no-index` (read-only VPS):
- Canonical Agent Data `agent_data/workspace_tools.py` có `AGENT_INFRA_TOOLS = frozenset({'infra_graph', 'infra_logs', 'infra_ops_plan'})` và union đó trong `agent_profiles`; runtime baseline/candidate không có. Candidate có thêm declaration adapter. Ghi đè canonical sẽ bỏ phần Hermes đã có; build từ canonical kèm phần đó có thể đưa thay đổi profile ngoài RUN14 vào runtime. Chưa chạy phép thử/được chốt release delta đó trong PROMPT này.
- Canonical `claude-mcp/app/server.py` có `SURFACE_LABEL = os.environ.get("MCP_SURFACE_LABEL", "Anthropic/ClaudeAI [auth:claude-chat]")`; runtime Claude/candidate dùng nhãn Claude cố định. Sổ `code-ledger.tsv` ghi source này phục vụ cả incomex-claude-mcp và incomex-gemini-mcp. Không được ghi đè làm mất khả năng phân biệt Gemini sau upgrade.
- Hash canonical: workspace_tools.py `84ed31d64c7d517205de0de641633bbf6252a727b54084b7eccdb032ac5a907b`; Claude server.py `d14c6a1278f6a587f62359577acb75dbdebbf09317a4b3204c05f7c959381992`. Baseline runtime tương ứng `d3f22b9285f5e7a2b14cb737c7cb1cb6d3f16640a3c412bfcc53c7016c6ec55b` và `422dd29578daac04d626509c556a6f981d90665d0ae598d4499eb5703faa28d9`.
- Helper canonical/runtime cùng hash `e5790c74edbb24575c5015982953d98aa8165657574b4782df18a49382710f11`.
- Công cụ apply-v0 hiện hữu có target compose AD/FS, helper và registry/sổ mã. Chưa gọi apply; không sửa registry/compose/source/permission. Đây không phải thiếu công cụ hay thiếu nút Refresh.

Giữ hai image candidate đã build và local source snapshot; Git hồ sơ chứa diff/build/manifest/test để truy nguồn nhưng **chưa phải source release canonical đã promote**. Không dùng commit Mac-local hay hồ sơ patch để tự tuyên G8 PASS.

## G1–G9
| Nhóm | Bằng chứng lab | Trạng thái production |
|---|---|---|
| G1 | PASS schema optional, mô tả 4 facts, thiếu field trả guidance + isError qua real Linux HTTP hai Gateway | UNKNOWN client active chưa Refresh |
| G2 | PASS 38 ca delta: NFKC/casefold/alias, unknown product, missing/type/length/control, env typo, task mismatch/multiple target, ad-hoc vs RUN, provenance | PARTIAL; chưa đo tất cả task/assignment thực |
| G3 | PASS fixture credential swap, không lấy env từ shared auth, metadata giả bị từ chối; quyền nghiệp vụ cũ giữ nguyên | PARTIAL; chưa cold-client âm thật |
| G4 | PASS fixture write/edit/copy/move/transaction/restore dispatch/upload/import/queue/helper carry; HTTP file-write thật cả hai image | PARTIAL; helper đặc quyền/Git production không chạy |
| G5 | PASS retry, đổi facts/auth, immutable receipt và alias-upgrade hash; reverse patch hồi phục byte baseline | PARTIAL; chưa race/lost-response production |
| G6 | Native tools phiên Codex hiện tại vẫn schema cũ; chưa advertise nên không Refresh giả | UNKNOWN; C2 active NOT_TESTED |
| G7 | Không lấy tác giả/unit/HTTP simulator làm AI độc lập | C1_COLD/C1_FINAL NOT_TESTED |
| G8 | Hai image build/hash pin + HTTP lab; Guard PRE PASS; source/runtime divergence đã đo | BLOCKED trước source promotion/advertise/enforce; production rollback/rebuild guard chưa nghiệm thu |
| G9 | Không network/service/key/permission mới; không đụng production/Hermes/Gemini; lab network none | Giữ phạm vi; không tuyên full parity |

## Giới hạn và đường tiếp
AD HTTP probe tắt lifespan để không nối external services, không phải full startup nghiệm thu. Các fixture FS helper/Git giữ giới hạn P452; unit/HTTP không thay C1 thật. Chưa có chuẩn chuyển schema active hay canary enforcement production an toàn. Không đề nghị Owner Refresh khi schema chưa được deploy.

NEXT_TRIGGER: GPT Host chốt release boundary/canonical source đối với hai delta Hermes/Gemini có sẵn; tiếp tục đúng candidate và image pin, hoàn tất G8 + kiểm Linux/rebuild tương ứng, rồi advertise-only → Refresh/C2 active → AI C1_COLD/FINAL → enforce. Không mở task/hệ thống/vòng thiết kế mới; Owner không phải kiểm từng thao tác hoặc duyệt lại quyền.

## Guard và kết thúc lab
Guard PRE `guard-pre-HJW-RUN14-20261029T073218Z.json` PASS; Guard POST `guard-post-HJW-RUN14-20261029T074552Z.json` PASS, footprint 0, same_or_better PASS, PREEXISTING_SAME #24. Không có production mutation nên không có production rollback. Lab tmp source/tokenizer đã dọn, không còn container RUN14; giữ hai image candidate đã pin.

```text
/incomex-agent-data sha256:46e0ba15f18f2c4241a6a704eaa7c3f209432453a78e04dff626187ec1f50c8c
/incomex-claude-mcp sha256:bacd21605a06825d0a725bcaefecdf55abbe85e075ab7be8fe93da3e04b5f961
e5790c74edbb24575c5015982953d98aa8165657574b4782df18a49382710f11  /opt/incomex/claude-mcp/helper/mcp_host_helper.py
  INV1.ruleset                        PASS  PASS (cached 14:05 29/10, age 39m <= 120m) · id/enforcement/target/~ALL/4 rules/updated_at match
  INV2.gpt_full_all_2                 PASS  tools=37 hash=dbbfc590a969 caps=ok · e2e ref workspace_read=ok
  INV3.claude_surface                 PASS  tools=23 fp=4f1000e9aad3 caps=ok · e2e ref fs_read=ok
  INV7.hermes                         PASS  tools=7 e2e=ok badkey=401 AGENT_DATA_env=0
  INV24.gemini                        PASS  vps tools=23 e2e=ok badkey=401 · google-main tools=37 e2e=ok
  INV10.pending_records               PASS  pending=0 stuck=[]
  INV10.clone_remote_drift            PASS  clones hold nothing unconfirmed; snapshots on the remote line
  INV5_6.health_routes                PASS  gateways healthy, helper alive + write path ok, config-guard CLEAN, routes 200
  INV11.mcpw_switches                 PASS  lifecycle.mode=audit · legacy_master=enforce
  INV12.lifecycle_snapshot            PASS  age 92 s · 10 tasks/41 rows · red=0 · ssh_unknown=91
  INV13.owner_view_labels             PASS  6/6 marks (423496 B)
  INV14.hermes_client_backend_compat  PASS  serve+gateway @ bf0203a794 · Mac @ bf0203a794 (09:49 24/10)
  INV15.kuma_telegram_coverage        PASS  đường giám sát khoẻ · fleet 32/32 · up=31 · đều gắn Telegram #2 · lịch Disk/Guard đúng · bảng đèn 279 s · đèn dịch vụ đỏ (không tính vào #22): #24
  CTR-WATCHDOG-01                     PASS  the mutant pending record is caught
  INV18.web_incomex                   PASS  {"watch": "PASS", "namespace": "web_incomex", "published": 27, "routes": 6, "runtime_files": 1876, "source_files": 233, "watchdog": "mutant rejected", "errors": []}
  INV19.hjw_contract                  PASS  chỉ Host giao · quét việc mở · write trong việc · vé gắn file · đối chiếu phạm vi · AUTO rỗng · handoff nghỉ · máy ghi hộ kết quả (chặn dấu máy/thiếu STATUS) · một bộ điều phối · NEXT (23 phép nghĩa) · gate root:hermes 640 · khoá Hermes ≤ 7 tool · ghi work/*/COLLAB.md · guard hậu ảnh 11 phép · đọc đúng ""+TQT · hai cổng: 0 sudo · 13 đường credential đóng · gcloud rỗng · 0 biến Google · 0 docker
  INV20.connector_twin_sync           PASS  PASS agent-data cloud=release 2b14c2a (nguồn đi trước 1 commit chưa phát hành) · lark lark-n1-1 24 tool · web 37/24 · Mac khớp (thấy lần cuối 29/10 07:26Z)
  INV21.owner_view_goal_flow          PASS  10 việc đang làm đọc được mục tiêu · đồng bộ 89 s trước
  INV22.graph_v1                      PASS  graph-v1 PASS · running/healthy rc=0 · loopback 17474/17687 · auth+invariants 2400s trước
  INV23.code_ledger                   PASS  bề mặt 603 tệp đều trong sổ · UNKNOWN 3 vùng không quét: bind-ro:incomex-claude-mcp:/var/lib/incomex-mcp-helper/queue; bind-ro:incomex-gemini-mcp:/var/lib/incomex-mcp-helper/queue
  INV25.github_ci_runners             PASS  agent-data-test: connected/limits PASS; web-test: connected/limits PASS
  INV16.tin_bao_diem_danh             PASS  TIN BÁO 2026-10-29T07:40:02Z: 86 loại · 84 chạy · 0 hỏng · 2 chưa xác định
  C3 baseline: PRE v2 · FOOTPRINT 0 mục: 
  C3.footprint_coverage               PASS  0 mục · đủ 4 ô
  C3.same_or_better                   PASS  PREEXISTING_SAME #24
  C3.change_event                     PASS  nhóm EVENT so PRE: 4 nhóm
  saved /tmp/hjw-run14-guard/guard-post-HJW-RUN14-20261029T074552Z.json
GUARD POST HJW-RUN14: PASS
```
