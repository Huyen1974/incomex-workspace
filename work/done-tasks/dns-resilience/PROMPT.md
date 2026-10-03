# PROMPT — DNS1 STAGED CLOUDFLARE CUTOVER · full-zone proof before delegation

RUN_ID: DNSRES-DNS1-STAGED-CUTOVER-20261001-01
STATUS: **DRAFT — CHƯA READY/RUN.**
Host: GPT Chat
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: workspace_* → incomex-workspace/main.
Runtime_Write_Path: DNS provider/registrar only at explicit Owner substeps; VPS runtime READ-ONLY.

## 1. Mục tiêu
Trong **một browser session của Owner**, chuyển authoritative DNS từ Mắt Bão sang Cloudflare DNS-only mà không mất record: lấy full zone → tạo/import Cloudflare → agent query assigned Cloudflare NS và chứng minh 0 diff → Owner đổi NS → agent xác minh parent/public resolvers. Không chờ giờ cố định.

## 2. Read gate / PRE
Đọc AGENTS → root COLLAB DROOT25/28/32 → `work/dns-resilience/COLLAB.md` §0 + DNS0 KQ + D5/D6 → PROMPT này. READY phải = commit cuối chạm PROMPT. Ghi STARTED theo DROOT31.

PRE read-only:
- đọc DNS0 evidence `/opt/incomex/work/dns-resilience/DNS0-20261001/`;
- current authoritative/parent delegation vẫn Mắt Bão; current public RRsets không drift không giải thích so DNS0;
- DNSSEC vẫn OFF;
- không dùng raw `nginx -T`; cấm ghi secret-bearing output vào evidence;
- xác định registrar qua VNNIC Whois/public evidence nếu được; không mutation trước Owner substep.

## 3. OWNER_DNS_SESSION · substep A — full zone + Cloudflare pending zone
Agent chuẩn bị hướng dẫn cực ngắn rồi dừng đúng checkpoint:
`OWNER_DNS_SESSION_A_REQUIRED`

Owner làm trong một browser session:
1. Mắt Bão: mở domain → Bản ghi DNS; **xuất/download toàn bộ zone nếu có**. Nếu panel không có export, lưu full list record bằng file/CSV/HTML/PDF/screenshot đủ mọi dòng; không sửa record.
2. Cloudflare: tạo/đăng nhập account → Add/Onboard domain → apex `incomexsaigoncorp.vn` → Free plan/full setup; import/upload full zone nếu có file phù hợp hoặc nhập/copy toàn bộ record; **tất cả DNS-only / proxy OFF**; DNSSEC OFF; **chưa đổi registrar nameserver**.
3. Lưu full zone/list Mắt Bão trên Mac dưới `/Users/nmhuyen/Desktop/DNS_CURRENT_EXPORT.*` (format bất kỳ agent đọc được) và lưu hai Cloudflare assigned nameserver public vào `/Users/nmhuyen/Desktop/CLOUDFLARE_NS.txt` (mỗi dòng một NS). Không lưu password/token.
4. Quay lại Claude Code và báo `A_DONE`.

Nếu Cloudflare quick scan tự tạo record, không tin scan là đầy đủ; full export/list Mắt Bão mới là source để đối chiếu.

## 4. Verify Cloudflare trước delegation
Sau `A_DONE`:
- đọc export/list local + DNS0 manifest; normalize RRsets theo DNS semantics (FQDN/trailing dot/order; không làm mất TTL/type/value);
- set `COMPLETENESS=EXPORT` chỉ khi artifact thực sự chứa full list từ panel/provider, không phải ảnh một phần;
- query **trực tiếp cả hai assigned Cloudflare authoritative NS** khi zone còn pending; lấy toàn bộ record có thể kiểm theo export + từng hostname record, SOA/NS;
- so source Mắt Bão export ↔ Cloudflare authoritative: **0 missing, 0 unexpected materially different**, ngoại trừ SOA/NS provider-managed khác expected;
- đặc biệt giữ apex A, www, VPS1 hostnames, elearning, ai CNAME và mọi TXT/MX/DKIM/DMARC/CAA/SRV lộ ra trong EXPORT;
- tất cả A/AAAA/CNAME web records = DNS-only/proxy OFF; DNSSEC OFF;
- nếu mismatch: báo exact record, Owner sửa trong **cùng browser session**, rồi agent requery; không mở task/vòng mới.

Chỉ khi `COMPLETENESS=EXPORT` + 0 diff mới phát trong terminal:
`CLOUDFLARE_ZONE_VERIFIED · SAFE_TO_CHANGE_NS`

## 5. OWNER_DNS_SESSION · substep B — đổi nameserver
Sau câu SAFE_TO_CHANGE_NS, Owner trong cùng browser session:
- mở panel registrar thật (VNNIC Whois/panel evidence đã xác định; nếu domain nằm trong Mắt Bão ID thì vào quản lý tên miền → Name Server);
- thay đúng cặp NS hiện tại bằng **hai NS Cloudflare assigned** từ file;
- không bật DNSSEC, không xóa zone/bản ghi Mắt Bão;
- hoàn tất OTP nếu registrar yêu cầu;
- quay lại Claude Code báo `B_DONE`.

## 6. Post-delegation measured gate — không chờ 12h/72h máy móc
Sau `B_DONE` agent tự đo:
1. query toàn bộ parent `.vn` authoritative đã dùng ở DNS0; xác nhận delegation mới xuất hiện nhất quán hoặc ghi chính xác máy nào chưa cập nhật;
2. query old Mắt Bão authoritative và new Cloudflare authoritative: cả hai phải vẫn phục vụ cùng business RRsets trong cửa sổ cache;
3. query ≥6 public resolver + Mac/VPS1 cho apex/www/vps/directus/ops/giaoduc/elearning/ai và mọi record bổ sung từ EXPORT; 0 SERVFAIL/NXDOMAIN/mismatch ngoài cache delegation expected;
4. HTTPS/TLS/Kuma/mail-target checks read-only.

**Không bắt chờ hết parent NS TTL 43200s** nếu:
- parent authority đã nhận delegation mới; và
- old+new authoritative cùng business RRsets; và
- public resolver trả dữ liệu đúng dù còn NS cache cũ/mới.
TTL chỉ là thời gian cache có thể còn tồn tại; nó không tự tạo thêm bằng chứng nếu hai phía đã giống nhau.

Nếu parent chưa nhận NS mới, dùng machine timer nhẹ để recheck theo nhịp hợp lý (không Owner/AI ngồi chờ); kết thúc ngay khi evidence đủ, không chờ mốc giờ danh nghĩa.

## 7. Rollback / acceptance DNS1
Rollback trigger trước ổn định:
- Cloudflare authoritative thiếu/sai record không sửa được nhanh;
- parent delegation sai/partial kéo dài kèm resolver failure;
- SERVFAIL/NXDOMAIN/TLS/mail failure do delegation.
Rollback = Owner đổi NS về `ns1.matbao.vn` + `ns2.matbao.vn`; Mắt Bão zone phải vẫn nguyên. Sau rollback agent xác minh parent + resolver về known-good. Không xóa Cloudflare zone trong RUN.

PASS khi:
- `COMPLETENESS=EXPORT`;
- Cloudflare authoritative pre-delegation 0 diff business RRsets;
- parent delegation mới được xác nhận bằng authoritative evidence;
- old/new authoritative cùng dữ liệu trong cache window;
- public resolvers + HTTPS/Kuma/mail checks không lỗi;
- Mắt Bão rollback zone còn nguyên.

KQ:
`KQ@DNSRES-DNS1-STAGED-CUTOVER-20261001-01 XONG · CUTOVER_PASS · COMPLETENESS=EXPORT · DNS_ONLY`
hoặc `DỪNG · <exact blocker>`.

Không chạm VPS runtime, không bật Cloudflare proxy, không bật DNSSEC trong RUN này.
