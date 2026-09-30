# PROMPT — MCPW PHA B1 · SURFACE IDENTITY / AUTH PROFILE

RUN_ID: MCPW-B1-IDENTITY-20260930-01
Host: GPT Chat · GPT-MCPW-250925-A
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: `work/mcp-workspace/COLLAB.md`.
Runtime: VPS1 production.
STATUS: DRAFT — CHƯA READY/RUN.

## 0. Mục tiêu duy nhất

Pha B được tách thành hai RUN để giảm blast radius:
- **B1 (RUN này):** mỗi surface có danh tính server-side đáng tin, không dựa vào `clientInfo`/User-Agent/tên commit tự khai.
- **B2 (RUN sau):** execution ledger + START/FINISH/NEXT trên identity đã nghiệm thu.

B1 phải giữ nguyên contract MCP hiện hành: không thêm server/DB/port/tool, không đổi tools/list/schema, không đổi write authority GitHub. Reuse-first/code-last theo DROOT22.

Các surface cần phân biệt bằng bằng chứng runtime, không đoán:
1. GPT web/desktop/Work đang dùng cùng connector hiện hành → một profile `gpt-web` nếu transport thực tế không phân biệt thêm.
2. Codex → `codex`.
3. Claude Code CLI → `claude-code`.
4. Claude Chat/Cowork → `claude-chat`.
5. Hermes giữ profile server-auth hiện hữu, **không sửa** trong B1.

Nếu inventory cho thấy tên/transport khác thực tế, dùng đúng surface thật; không tự tạo identity giả để đủ danh sách.

## 1. Read gate / collision gate

Đọc:
AGENTS.md → root COLLAB DROOT09/19/22/25/28/29/30/31 → MCPW COLLAB §0 + N1–N9 + P35–P43 + P52–P55 → PROMPT này.

Đọc live trạng thái VPSUP:
- `VPSUP-G3-TARGET-20260930-01` có thể đang STARTED nhưng G3 là **read-only**.
- G3 read-only không chặn B1.
- Nếu VPSUP/G3 hoặc RUN khác đã mở mutation trên nginx/agent-data/claude-mcp/GSM/credential/MCP/Hermes ⇒ DỪNG trước mutation.
- Không sửa `work/vps1-up-grade/`; moving-target consumer do G3 tự recheck trước final PASS.

Ngay sau read-gate PASS và **trước PRE**, ghi:
`STARTED@MCPW-B1-IDENTITY-20260930-01 <UTC> · executor=Claude Code CLI`
vào task COLLAB. Ghi không được ⇒ DỪNG.

## 2. PRE — inventory bằng chứng hiện hành, không dùng giả định P39

Trước mutation, xác minh và lưu sanitized evidence:
- auth path hiện hành của `workspace_*`, `fs_*`, master route, agent profiles, claude-mcp, nginx includes/routes, OAuth/path-secret/header nếu có;
- profile/credential nào đang được mỗi surface thật sử dụng;
- actor hiện được server quyết định từ đâu; điểm nào còn lấy từ `clientInfo`/UA;
- exact 37-tool contract: names + input schemas + serverInfo/version/hash;
- Agent Data / claude-mcp / nginx image+StartedAt+health+network;
- Config Guard registry hiện hành (sau §8A kỳ vọng 54 CLEAN) + Protection Guard;
- P02 identity/baseline hiện hành;
- Hermes profile/tool/write scope/AUTO/STOP chỉ đọc để chứng minh **không bị chạm**;
- GSM chỉ metadata/version/state/fingerprint; **không in secret**;
- Mac client configs của Codex/Claude Code nếu được phép đọc; không in credential;
- exact backup/hash/owner/mode của mọi file sẽ có thể thay.

**Quan trọng:** việc Owner vừa Authenticate `claude.ai Incomex VPS` không tự chứng minh surface identity; phải xem server-side auth evidence.

Nếu auth topology thực tế khác P39 theo cách đòi:
- server/port/public endpoint mới;
- tool/schema mới;
- OAuth provider mới;
- thay đổi kiến trúc lớn hơn một mapping/profile/routing delta mỏng;
⇒ ghi `IDENTITY_DESIGN_DELTA_REQUIRED` + evidence rồi DỪNG, không cố ép P39.

## 3. Lựa chọn implementation trong RUN — reuse-first

Ưu tiên theo thứ tự:

A. **Tốt nhất:** transport/auth hiện hành đã cung cấp identity server-side đáng tin (credential/profile/OAuth claim) ⇒ chỉ map/bind surface vào actor profile; không tạo secret mới nếu không cần.

B. Nếu cần credential riêng: reuse `agent_profiles` + GSM/project hiện hữu + nginx/secrets include hiện hữu; mỗi surface một credential/profile server-side. Không project/service/secret-store mới.

C. Chỉ nếu A/B không thể giữ full master capability: cho phép **delta code nhỏ nhất** để profile riêng có đúng capability master hiện hành mà **không đổi tool list/schema**. Code delta này phải vào DROOT29 ngay trong RUN. Nếu cần thay contract/tool schema ⇒ DỪNG.

A0 (đánh giá đầu tiên — mục tiêu 0 thao tác Owner): nếu Codex/Claude Code chuyển được sang credential/profile riêng bằng cấu hình Mac, thì mỗi route web hiện hữu (route path-secret của GPT; route claude-mcp của claude.ai) chỉ còn đúng một surface dùng ⇒ route chính là identity của surface web đó. Chống giả bằng bằng chứng server-side sẵn có (vd nguồn mạng của request: dải máy chủ nhà cung cấp connector so với máy Owner, nếu nginx/agent-data đã ghi được). Chỉ khi không tách được mới dùng checkpoint web ở §4.3.

Không dùng `clientInfo`, User-Agent hoặc commit prefix để cấp quyền/định actor; chúng chỉ là display metadata.

## 4. Rollout không làm gián đoạn

Triển khai theo 4 nấc, mỗi nấc có health gate:

1. **PREPARE:** tạo/bind profile/route mới song song; legacy shared route vẫn hoạt động như cũ.
2. **CLI CUTOVER:** tự cập nhật Codex + Claude Code config trên Mac bằng cơ chế hiện hữu nếu có; không hỏi Owner nếu Agent làm được.
3. **WEB CUTOVER:** chuẩn bị hoàn toàn phía server trước. Nếu ChatGPT/claude.ai bắt buộc Owner đổi URL/reconnect trong UI, dừng đúng một checkpoint `OWNER_WEB_CONNECTOR_SWITCH_REQUIRED` và đưa **một hướng dẫn gộp ngắn** cho tất cả thao tác tay còn lại. Không yêu cầu Owner làm từng bước kỹ thuật phía server.
4. **ENFORCE LEGACY:** chỉ khi đủ cả 3: (a) mọi surface từng ghi qua legacy đã có **một lần GHI thật** qua đường mới — riêng Host GPT và Reviewer Claude Chat mỗi bên ghi 1 dòng hợp lệ vào task COLLAB, actor đúng (đọc thôi là chưa đủ); (b) đối chiếu log ghi hiện hữu (access/audit, ≥7 ngày gần nhất) trên legacy: mọi người ghi phải map được vào surface đã cutover — còn người ghi không map được (script/cron/DOT/tool lạ) ⇒ **không ENFORCE**, ghi `ENFORCE_DEFERRED` + danh sách; (c) deny bằng một công tắc cấu hình (lật lại = rollback, không redeploy). Sau ENFORCE, legacy shared auth/route trở thành `unattributed`: đọc được theo quyền hiện hành, **ghi DENY**. Không xoá legacy trong RUN này để rollback dễ.

Restart/recreate:
- chỉ component có config/code đổi;
- từng component một, dùng DROOT10 health gate;
- không restart Hermes;
- không restart Directus/Nuxt/Qdrant/Postgres;
- nginx chỉ reload nếu đủ; recreate chỉ khi bằng chứng bắt buộc.

Ngay trước first runtime mutation và trước ENFORCE LEGACY: áp DROOT30 re-read task COLLAB + PROMPT + READY/HOLD/STOP và collision gate.

## 5. Server-auth identity contract

Sau cutover:
- actor/profile lấy từ server-authenticated source;
- cùng một credential/profile không được đổi actor bằng `clientInfo`;
- surface không xác thực hoặc legacy shared không được mutation;
- read-only/review paths không bị phá;
- Hermes giữ nguyên actor `agent-gw/hermes`;
- Host/Reviewer `kind=review` chưa triển khai ở B1; không được vô tình chặn luồng hội đồng hiện hành. B2 mới triển khai lifecycle gate.

Nếu current auth không thể phân biệt GPT web và Claude Chat mà không Owner reconnect, checkpoint web cutover là hợp lệ; không gán bừa actor.

## 6. Acceptance B1

Bắt buộc:

1. **Contract freeze:** tools/list + schema hash + serverInfo/version đúng baseline DROOT09; 0 tool mới/mất/đổi schema.
2. **Identity:** mỗi surface đã cutover trả actor/profile đúng từ server evidence.
3. **Spoof negative:** giả `clientInfo=openai-mcp` hoặc tên surface khác không đổi actor đã xác thực.
4. **Legacy:** read vẫn hoạt động; write bị DENY sau ENFORCE, có exact error/audit; không làm legacy biến thành quyền surface mới.
5. **Cross-profile:** credential/profile A không được nhận actor B.
6. **CLI:** Codex và Claude Code thực tế connect/read bằng profile riêng; mutation smoke dùng cách ít rác nhất (ưu tiên audit/no-op/controlled existing marker); nếu phải ghi thật thì dùng đúng task COLLAB và trả file về nội dung sạch trong RUN.
7. **Web:** ChatGPT và Claude Chat/Cowork phải có một read thật qua connector đã cutover, và trước ENFORCE có một write thật vào task COLLAB với actor đúng (Host GPT + Reviewer Claude); nếu UI reconnect là thao tác Owner bắt buộc thì KQ chưa XONG trước checkpoint đó.
8. **Hermes regression:** profile/tool/write scope/AUTO/STOP unchanged; Telegram/HJW control không bị sửa.
9. **P02:** read-serving/freshness regression = 0.
10. **Failure:** Agent Data down ⇒ claude-mcp/legacy không được fail-open thành write.
11. **Outside scope:** 0 Directus/PG/Qdrant/Nuxt/DNS mutation; 0 `work/vps1-up-grade/` write.
12. **Rollback:** một đường trả profile/routing/client config về known-good pre-B1; proof trên bản sao/controlled path trước KQ.

## 7. DROOT29 / Điều 30–31

Bất kỳ code/config production bền nào đổi trong B1:
- regression proof hành vi cũ bị chạm;
- đăng ký/refresh đúng Config Guard hiện hữu, không dựng guard mới;
- mutant/negative bắt được drift;
- watchdog checker sống;
- rollback exact old/new + reason + RUN_ID;
- controlled rebaseline **chỉ** delta B1.

Sau final restart/recreate Agent Data/claude-mcp (nếu có), thực hiện **controlled P02 identity rebaseline** theo P43: old/new + reason + RUN_ID + POST proof. Không silent rebaseline.

Guard PRE/POST theo cơ chế hiện hữu; ngoài-scope delta = 0.

## 8. No-AI-Wait / Owner interaction

Không soak >15 phút trên Mac.
- phép thử dài ⇒ VPS deterministic existing Guard/Kuma/timer;
- B1 dự kiến không cần soak dài.

Agent tự làm tối đa.
Chỉ dừng hỏi Owner khi:
- UI của ChatGPT/claude.ai thực sự bắt buộc người dùng reconnect/change URL;
- hoặc scope/contract phải mở rộng ngoài PROMPT.

Nếu cần Owner, gộp thành **một checkpoint duy nhất**.

## 9. KQ

PASS khi mọi acceptance §6 đạt và legacy write đã fail-closed, **hoặc** `ENFORCE_DEFERRED` kèm danh sách người ghi chưa map (identity các surface đã đạt; Host quyết bước enforce riêng sau khi xử lý danh sách).

Ghi:
`KQ@MCPW-B1-IDENTITY-20260930-01 XONG`

Nếu dừng vì topology khác:
`KQ@MCPW-B1-IDENTITY-20260930-01 DỪNG · IDENTITY_DESIGN_DELTA_REQUIRED`

Nếu dừng chờ thao tác web bắt buộc:
không ghi KQ terminal; ghi checkpoint
`OWNER_WEB_CONNECTOR_SWITCH_REQUIRED`
và chờ Owner làm một lần, sau đó re-read DROOT30 rồi tiếp tục.

KQ phải báo:
- actor/profile matrix before→after;
- tool/schema hash before→after;
- component StartedAt before→after;
- Guard/Config Guard/P02/Hermes regression;
- legacy deny evidence;
- rollback;
- mọi Owner action thực tế đã cần.

## 10. NEXT

Sau B1 XONG:
- Host + Claude review KQ;
- mở **B2 lifecycle ledger / auto-claim / START-FINISH / NEXT** theo P39/N1–N9;
- B2 xong mới Pha C scoped lease/fencing.

Không tự chạy B2/C trong RUN này.
