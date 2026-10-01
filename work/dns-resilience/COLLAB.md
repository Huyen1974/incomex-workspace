# COLLAB — dns-resilience
Tên việc: DNS-RES · Chống phụ thuộc sự cố DNS trước cutover VPS1

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Xác nhận User: **ĐÃ XÁC NHẬN — 2026-10-01 · Owner yêu cầu tiếp tục điều hành theo phương án Claude P78; kế hoạch DNS-RES đã được Host chốt trước tại VPSUP P56.**
### 1. Mục tiêu
Loại phụ thuộc một nhà cung cấp DNS trước cutover VPS1, không làm gián đoạn tên miền và không thêm proxy/CDN ngoài phạm vi.
### 2. Thế nào là hoàn thành
Zone đích DNS-only khớp zone nguồn từng bản ghi; đường đổi NS và rollback đã diễn tập/đo được; public resolvers xác nhận không lệch sau đúng thời gian TTL/NS thực đo; từ lúc cutover VPS1 tới hết 7 ngày monitor không đổi DNS.
### 3. Chi tiết cần đạt (AI ghi, Host kiểm)
- Vòng DNS0 đầu tiên **chỉ đọc**: inventory zone/NS/SOA/TTL/DNSSEC/CAA/MX/TXT/A/AAAA/CNAME/SRV và hostnames đang dùng; đo zone-cha NS TTL và resolver behavior; inventory registrar/provider từ bằng chứng công khai + config hiện hữu, không đoán.
- Candidate đích: Cloudflare **DNS-only**, không proxy. Không tạo zone/account/resource trong DNS0 nếu chưa chứng minh đường credentials/quyền hiện hữu.
- So từng record nguồn ↔ candidate manifest; chuẩn bị rollback NS cũ, TTL thực đo, checklist cert/TLS/email/e-learning/Kuma.
- Owner dự kiến chỉ 1 thao tác nếu bắt buộc: đổi nameserver ở registrar sau khi Host xác nhận zone đích đầy đủ. Không yêu cầu Owner copy secret.
- Không chờ cố định 72h: thời gian chờ chỉ bằng TTL/NS propagation thực đo + kiểm resolver độc lập; nếu bằng chứng đã đủ thì không kéo dài theo giờ vô ích.
- DNS-RES không chặn G5 lab; là hard gate trước production cutover G6/G7. Từ cutover tới hết 7 ngày monitor: freeze DNS.
### Vòng trước
- VPSUP P55/P56: DNS-RES tách RUN riêng; Cloudflare DNS-only candidate; zone đích phải khớp từng record; đổi NS là thao tác Owner; trước đây đề xuất 72h, P78 cập nhật sang cổng evidence/TTL đo được.

## Trạng thái
DNS-RES | **DNS0 PASS · DNS1 READY/RUN** | PROMPT last-touch `a8e2dace65bada8ae8346bad134e3507fc91499b`; `READY@a8e2dace65bada8ae8346bad134e3507fc91499b`; RUN_ID `DNSRES-DNS1-STAGED-CUTOVER-20261001-01` | Owner dùng một browser session: export full zone + tạo/import Cloudflare trước, agent kiểm 0 lệch, rồi mới đổi NS; không chờ cố định 72h.
- STARTED@DNSRES-DNS0-INVENTORY-20261001-01 2026-10-01T04:47:32Z · executor=Claude Code CLI · read-gate PASS: `workspace_stat` root workspace HEAD `f15f66f` (fresh); PROMPT last-touch `3b46b4650b4981d2c4b59b92ee1e26b5699222d8` = READY D4; đã đọc AGENTS → §0 → D4/D5 → PROMPT → VPSUP P55/P56/P78/P79; 0 STOP_REQUESTED/HOLD. Write_Path báo cáo: `workspace_*` agent-data (khoá `claude-code`). Runtime_Write_Path NONE (read-only); hồ sơ theo D5 tại VPS1 `/opt/incomex/work/dns-resilience/DNS0-20261001/`.
- KQ@DNSRES-DNS0-INVENTORY-20261001-01 XONG · MACHINE_DONE · INVENTORY_PASS · OWNER_CLOUDFLARE_SETUP_REQUIRED · COMPLETENESS=PUBLIC_ONLY · 2026-10-01 04:47Z–05:17Z · Claude Code CLI · **Gate:** STARTED `5bc176c`; trước KQ (05:16Z) PROMPT vẫn last-touch `3b46b46`, `work/dns-resilience/` chỉ có thêm commit STARTED, 0 STOP_REQUESTED/HOLD. **Zone (đo thật từ VPS1 + Mac, chỉ đọc):** authoritative = Mắt Bão — zone cha `.vn` 8/8 máy trỏ `ns1/ns2.matbao.vn`, zone con tự khai `ns1/ns2.matbao.com` (cùng 3 IP, không lệch chức năng; glue ns2 thiếu 1 IP; các máy này cũng tự host zone matbao.vn); SOA serial 2026080801; **10 RRset / 11 bản ghi**: apex + www → hosting cPanel bên thứ ba (website), 4 tên → VPS1 (vps/directus/ops/giaoduc), elearning → VPS2 (TTL 300), ai → CNAME Firebase; 3 IP authoritative nhất quán; 6 resolver từ VPS1 + Mac 0 lệch (OpenDNS từ chối IP Contabo → thay AdGuard/DNS.SB). **COMPLETENESS=PUBLIC_ONLY:** AXFR/IXFR bị từ chối 7/7 đích; dò có giới hạn 135 tên (8 từ nginx/cert/Kuma/CT log + 127 nhãn phổ biến gồm 56 selector DKIM, `_dmarc`, `_domainkey`, `_tcp`, `_tls`) → 127 NXDOMAIN, không wildcard, `_domainkey`/`_dmarc` NXDOMAIN; cấu hình hiện hữu không có đường gửi thư ký theo tên miền (VPS1 0 SMTP/MTA; e-learning dùng hộp thử mailtrap) ⇒ **DNS1 phải xuất toàn bộ zone từ panel nhà cung cấp hiện tại trong cùng nhóm thao tác Owner, đối chiếu 0 lệch rồi mới đổi NS** (đạt thì nâng `EXPORT`). **Parent NS TTL 43200 s (12 h)**; NS zone con + bản ghi 3600 s; negative TTL 3600 s; **DNSSEC không ký** (0 DS ở 8/8 máy `.vn`, 0 DNSKEY/RRSIG) ⇒ Cloudflare để DNSSEC tắt. **Mail:** không MX/SPF/DKIM/DMARC/CAA; implicit MX ⇒ thư gửi @tên-miền đi về hosting của apex (Exim mở) — giữ nguyên A apex. **Hostname map 8/8** (dịch vụ · cert hạn + cách cấp · Kuma · mail; 4 tên không có Kuma: apex/www, giaoduc, elearning, ai). **Cloudflare:** 0 credential/API hiện hữu (GSM 46 secret, VPS1, Mac) ⇒ `OWNER_CLOUDFLARE_SETUP_REQUIRED`, một lượt Owner = xuất zone hiện tại + tạo zone Cloudflare 8 bản ghi DNS-only theo manifest + đổi NS sau khi máy xác nhận khớp; `.vn` nhận NS thuần Cloudflare (thực nghiệm 6/13 tên miền mẫu). Registrar chưa xác minh công khai (`.vn` không whois cổng 43/RDAP; NS ở Mắt Bão không chứng minh registrar). **Rollback** NS = `ns1.matbao.vn`, `ns2.matbao.vn` + giữ zone Mắt Bão nguyên vẹn tới hết freeze. **Cổng đo:** 8/8 máy `.vn` đổi xong + 43200 s + 3600 s biên, không 72 h. JEV `gen-dec-1790831784-IBmYOThAftINFJZqeRxP` INVENTORY_PASS 0,70 (lượt đầu `gen-dec-1790831403-ODXWELNL0EMhf9kCb1l5` STOP 0,79 vì điều 4 thiếu ô “không có” → đã bổ sung map, điều 4 0,96). **Sự cố:** `nginx -T` đổ cả tệp secrets của nginx vào hồ sơ ~1 phút (quyền 0664) → `shred -u`; audit claude-mcp 0 lượt đọc; không in ra transcript; thay bằng bản lọc server_name. Hồ sơ VPS1 `/opt/incomex/work/dns-resilience/DNS0-20261001/` (`INDEX.md` `a5e57168…`, `SHA256SUMS` `4b625e24…` 33 tệp; đọc được qua MCP root `code`). 0 mutation DNS/NS/registrar/Cloudflare/runtime; không sang DNS1. Áp: SAME_COMMIT.

- STARTED@DNSRES-DNS1-STAGED-CUTOVER-20261001-01 2026-10-01T07:34Z · executor=Claude Code CLI · read-gate PASS: `workspace_stat` root workspace HEAD `83d322b` (task path sau đó chỉ có commit khác task `b694bbd` MMIM); PROMPT last-touch `a8e2dace65bada8ae8346bad134e3507fc91499b` = READY D7 (giữ ở D9/D10); đã đọc AGENTS → root DROOT25/28/30/31/32 → §0 → DNS0 KQ → D5–D10 → PROMPT; 0 STOP_REQUESTED/HOLD. Write_Path: `workspace_*` agent-data (khoá `claude-code`). Runtime_Write_Path: chỉ Owner thao tác panel DNS/registrar ở substep A/B; VPS runtime READ-ONLY. Chốt D8/D9/D10 áp trước bước B (không B trước 08:02:39Z; không STARTED-chưa-KQ mutation VPS1).

## Quyết định
- D1 · 2026-10-01 · Không bật Cloudflare proxy trong DNS-RES; DNS-only để không đổi nginx/TLS/real-IP.
- D2 · 2026-10-01 · Không dùng ngưỡng chờ 72h cố định; chỉ chờ phần thời gian tạo thêm bằng chứng dựa TTL/NS thực đo.
- D3 · 2026-10-01 · DNS0 là read-only, được chạy song song G4C soak/G5 draft/MCP review; cấm NS/zone mutation.

### D4 · Host GPT · 2026-10-01 · DNS0 READY/RUN
- PROMPT last-touch = `3b46b4650b4981d2c4b59b92ee1e26b5699222d8`; chưa có STARTED/KQ DNS0 tại thời điểm phát lệnh.
- **READY@3b46b4650b4981d2c4b59b92ee1e26b5699222d8**.
- **RUN@DNSRES-DNS0-INVENTORY-20261001-01 · ISSUED.**
- DNS0 read-only, được chạy song song G4C soak và MCP review; cấm tạo zone/đổi NS/registrar/VPS runtime.
- Owner cần quyết: —.

### D5 · Claude Chat (Reviewer) · 2026-10-01 · ACCEPT DNS0 — READY giữ nguyên, không sửa PROMPT
- Đúng ý VPSUP P78: read-only, cổng đo được, không 72h cố định, DNS-only. Lúc 04:37Z chưa có STARTED DNS0.
- **2 làm rõ cho executor (không đổi phạm vi):**
  1. Evidence đặt ở VPS1 `/opt/incomex/work/dns-resilience/DNS0-20261001/` (Host/Reviewer đọc được qua MCP), không chỉ nằm trên Mac. Đây là ghi hồ sơ, không phải mutation runtime.
  2. **Giới hạn đầy đủ của manifest:** truy vấn DNS công khai không liệt kê được toàn zone (AXFR thường tắt) ⇒ bản ghi tên lạ (DKIM selector, TXT xác minh dịch vụ, subdomain ít dùng) có thể sót — sót DKIM/SPF là hỏng email công ty sau khi đổi NS. DNS0 phải ghi cờ `COMPLETENESS=PUBLIC_ONLY|AXFR|EXPORT` trong KQ: thử AXFR (chỉ đọc), dò DKIM theo selector biết từ cấu hình mail/nhà cung cấp; nếu chỉ có `PUBLIC_ONLY` thì DNS1 phải gộp **xuất zone từ nhà cung cấp hiện tại** vào đúng nhóm thao tác Owner duy nhất (cùng lúc tạo Cloudflare/đổi NS), không phát sinh thêm lượt Owner.
- JEV `gen-dec-1790829444-msGIA7g7C8LYiwWRwPwQ`: ghi chú + 1 dòng đoạn dán 0,96 · cần zone export trước đổi NS 0,91.
- **Kết luận:** giao DNS0 được ngay với READY hiện hành; Owner thêm 1 dòng đầu đoạn dán: “Đọc thêm D5 trong work/dns-resilience/COLLAB.md và làm theo 2 làm rõ đó.”
- Owner cần quyết: —.

### D6 · Host GPT · 2026-10-01 · ACCEPT DNS0 · DRAFT DNS1 STAGED CUTOVER
- ACCEPT DNS0 KQ `2c9e20a…`: authoritative Mắt Bão, 10 RRset/11 record công khai, 6 resolver + Mac 0 lệch, parent NS TTL 43200s, DNSSEC OFF, `COMPLETENESS=PUBLIC_ONLY`, không Cloudflare credential hiện hữu.
- **Không coi PUBLIC_ONLY là đủ để đổi NS.** Cloudflare quick scan không đảm bảo đủ record; DNS1 phải lấy full export/list từ panel Mắt Bão, nâng completeness lên `EXPORT`, rồi mới cho đổi delegation.
- **Owner interaction tối thiểu = một browser session, hai substep:** A) export/full-list + tạo Cloudflare zone/import DNS-only, chưa đổi NS; B) sau agent query trực tiếp assigned Cloudflare NS và chứng minh 0 diff, Owner đổi NS ở registrar. Không có checkpoint thừa giữa hai substep.
- Không chờ 12h/72h cố định. Sau đổi NS: nếu parent `.vn` authoritative đã nhận NS mới và old Mắt Bão + new Cloudflare đều phục vụ cùng RRsets, cache resolver còn NS cũ vẫn an toàn; public resolver chuyển dần theo TTL. PASS dựa evidence, không dựa đồng hồ.
- Mắt Bão giữ zone cũ nguyên vẹn suốt DNS freeze làm rollback/fallback; không xoá record cũ sau cutover.
- Registrar: DNS0 chưa xác định. DNS1 thử VNNIC Whois/public panel evidence; nếu vẫn không xác định thì Owner chỉ ra đúng panel đang giữ domain trong browser session, không mở lượt hỏi riêng trước.
- **Trap từ DNS0:** cấm ghi raw `nginx -T` vào evidence vì include secrets. Từ nay chỉ đọc file/grep đã lọc, không dump secret-bearing config. Sự cố DNS0 chưa có bằng chứng secret bị đọc/exfiltrate ⇒ không rotate production secret chỉ vì nghi ngờ; có evidence truy cập mới mở rotation.
- Owner cần quyết: — (chưa thao tác cho tới DNS1 READY).

### D7 · Host GPT · 2026-10-01 · DNS1 READY/RUN
- PROMPT last-touch = `a8e2dace65bada8ae8346bad134e3507fc91499b`; chưa có STARTED/KQ DNS1 tại thời điểm phát lệnh.
- **READY@a8e2dace65bada8ae8346bad134e3507fc91499b**.
- **RUN@DNSRES-DNS1-STAGED-CUTOVER-20261001-01 · ISSUED.**
- DROOT32: không chờ TTL 12h/72h nếu old/new authoritative cùng dữ liệu và parent delegation đã cập nhật; chỉ giữ machine recheck nếu evidence chưa đủ.
- Owner interaction = một browser session hai substep A/B trong cùng RUN; không thêm vòng hỏi giữa nếu agent đã có đủ evidence.
- Owner cần quyết: —.

### D8 · Claude Chat (Reviewer) · 2026-10-01 · ACCEPT DNS1 — READY giữ nguyên, không sửa PROMPT
- DNS0 đạt và đã làm đúng D5 (hồ sơ VPS1 + `COMPLETENESS=PUBLIC_ONLY`, AXFR từ chối 7/7). Manifest 8 bản ghi có TTL đúng, cảnh báo proxy, xác nhận không có ACME DNS-01 (đổi NS không làm gãy gia hạn cert); NS trong zone TTL 3600 nên resolver bám Mắt Bão thêm tối đa ~1h — đã được giữ zone Mắt Bão che. DNS1 đúng hướng D5: có EXPORT mới đổi NS, kiểm trực tiếp NS Cloudflare trước, cổng đo theo DROOT32.
- **1 chốt cho executor (không đổi phạm vi):** ngay trước khi hướng dẫn Owner bước B (đổi NS), kiểm root/task COLLAB **không có `STARTED@` chưa KQ nào đang mutation production VPS1** (vd MCPW B2B restart agent-data, VPSUP S1). Có ⇒ dừng ở checkpoint, báo Host, chưa đổi NS. Lý do: từ B_DONE tới KQ DNS1 chỉ được có một thay đổi production đang diễn ra, để có sự cố thì biết ngay do đâu.
- **2 ghi chú cho Host:**
  1. Host giữ MCPW B2B/S1 không chạy từ B_DONE tới KQ DNS1 (đối chiều của chốt trên). Sau DNS1, sửa bản ghi nào (vd bước 11 chuyển `elearning`) thì sửa ở Cloudflare; nếu trong ~1 ngày đầu thì sửa cả Mắt Bão.
  2. **Khuôn KQ:** PROMPT ghi `KQ@… MACHINE_DONE · …` khiến Owner View hiện “unknown”, nên executor DNS0 phải tự thêm `XONG` (lệch PROMPT). Sửa một lần ở gốc: chuẩn `KQ@<RUN> XONG|DỪNG · <trạng thái phụ>` cho mọi PROMPT (VPSUP G5 cũng đang dùng `MACHINE_DONE`), hoặc cho parser hiểu `MACHINE_DONE`.
- Sự cố `nginx -T`: đồng ý không xoay secret production — cửa sổ ~1 phút, log 0 lượt đọc, chỉ root còn đọc được phần dư trên đĩa (root vốn đã có secret).
- Quy trình: DNS1 là thay đổi production nên cần 1 dòng Reviewer trước READY (VPSUP P75); D8 này bù trước khi STARTED.
- JEV `gen-dec-1790838925-14t2eptvC49DgGVmmfDS`: giữ các thay đổi production khác trong cửa sổ đổi NS 0,82 · sửa khuôn KQ 0,67.
- **Kết luận:** giao DNS1 được ngay với READY hiện hành; Owner thêm 1 dòng đầu đoạn dán: “Đọc thêm D8 trong work/dns-resilience/COLLAB.md và làm theo chốt trước bước B.”
- Owner cần quyết: —.

### D9 · Host GPT · 2026-10-01 · ACCEPT D8 · GIỮ COLLISION GATE HẸP
- ACCEPT D8; PROMPT DNS1 không đổi, **READY@a8e2dace65bada8ae8346bad134e3507fc91499b** giữ nguyên.
- Gate va chạm chỉ áp **ngay trước bước B và từ B_DONE tới KQ DNS1**: không launch MCPW B2B hoặc VPSUP S1 nếu chúng mutation VPS1 production. Trước B agent tự check STARTED/KQ; có active production mutation ⇒ dừng checkpoint, chưa đổi NS.
- **G5 lab trên VPS2 không bị gate này chặn.** Nếu G4C soak FINAL PASS trong lúc DNS1 đang chạy, Host vẫn có thể phát G5 và cho chạy song song vì không mutation VPS1/DNS.
- Sau KQ DNS1 XONG/DỪNG, production mutation khác mới được mở lại theo task riêng. Nếu cần sửa DNS record trong cửa sổ cache đầu, sửa Cloudflare và Mắt Bão cùng giá trị; nếu không có nhu cầu thì không đụng gì.
- Khuôn KQ mới từ đây ưu tiên `KQ@<RUN> XONG|DỪNG · <trạng thái phụ>`. Không sửa PROMPT đã review chỉ vì format; parser/root convention xử lý riêng, không thành gate cho DNS1/G5.
- Sự cố `nginx -T`: không có bằng chứng exfiltration ⇒ không rotate production secrets; giữ trap cấm raw dump secret-bearing config.
- Owner cần quyết: —.

### D10 · Claude Chat (Reviewer) · 2026-10-01 · ACCEPT D9 — READY giữ nguyên, không sửa PROMPT · 3 làm rõ cho chốt trước bước B
- Đã kiểm 07:28Z: PROMPT last-touch vẫn `a8e2dac` (HEAD `0aeda19`; commit sau D9 thuộc task khác, không chạm `work/dns-resilience/`); chưa có STARTED DNS1. Cloudflare có trả lời truy vấn cho zone còn pending trên NS được gán (docs Cloudflare “Zone status”) ⇒ bước kiểm 0 lệch trước khi đổi NS làm được.
- **3 làm rõ cho executor (không đổi phạm vi, không đổi READY):**
  1. **Không làm bước B trước khi soak G4C hết giờ — 08:02:39Z (15:02:39 giờ VN).** Soak do máy giữ trên VPS2 và đã có KQ (`SOAK_ARMED`) nên chốt “STARTED chưa KQ” không thấy; VPSUP đã ghi “không đổi NS/DNS trong lúc soak”. Tới `SAFE_TO_CHANGE_NS` mà chưa qua mốc ⇒ báo Owner đổi NS sau 15:03. Lý do: phán quyết soak 6h không bị nghi do DNS. Thực tế bước B gần như luôn sau mốc này ⇒ hầu như không tốn thêm thời gian.
  2. **“Mutation production VPS1” trong chốt D8/D9 = đổi service/container/config/nginx/compose/DB/khoá của VPS1** (vd MCPW B2B, VPSUP S1). Sửa file UI preview/tài liệu (vd MMIM A09 chỉ ghi HPML) **không tính** ⇒ không dừng checkpoint vì nó.
  3. **Sau B_DONE, một tên lỗi HTTPS/TLS/Kuma ⇒ thử lại thẳng IP gốc (bỏ qua DNS, `curl --resolve`).** Thẳng IP cũng lỗi ⇒ lỗi máy chủ (vd VPS2 đang chạy G5), không phải DNS ⇒ không phải lý do rollback NS; ghi lại, báo Host. Chỉ lỗi xuất hiện khi đi qua DNS mới tính là lỗi delegation.
- **Phía Owner (cho đơn giản):** không dán MCPW B2B / VPSUP S1 cho tới KQ DNS1; G5 lab VPS2 dán được. Lý do: B2B READY mở đúng lúc soak FINAL (~15:02) — trùng lúc Owner đang làm A/B; B2B chạy dở lúc tới bước B thì DNS1 phải chờ, tốn thời gian Owner hơn là để B2B sau.
- Ghi chú hệ thống cho Host: việc do máy giữ sau KQ (soak, timer) không hiện trong STARTED/KQ ⇒ chốt va chạm sau này nên đọc thêm “cửa sổ máy đang giữ”. Cách sửa gốc tuỳ Host; không thành gate cho DNS1/G5.
- JEV `gen-dec-1790839641-7L4VkUweO6G0bTwZtfuQ`: B sau mốc soak 0,79 · thử thẳng IP 0,64 · Owner không dán B2B/S1 tới KQ DNS1 0,81 · chạy kèm ghi chú nhỏ 0,71 (giữ lại 0,25).
- **Kết luận:** giao DNS1 ngay với READY hiện hành; dòng đầu đoạn dán đổi thành “Đọc thêm D8, D9, D10 …”, mục đọc COLLAB thành “D5–D10”.
- Owner cần quyết: —.

## Owner cần quyết
- —

## Con trỏ
- Luật: ../../AGENTS.md · ../../README.md · ../README.md
- Nguồn quyết định gốc: ../vps1-up-grade/COLLAB.md · P55/P56/P78
