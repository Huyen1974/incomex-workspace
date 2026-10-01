# PROMPT — DNS0 READ-ONLY INVENTORY · DNS resilience preflight

RUN_ID: DNSRES-DNS0-INVENTORY-20261001-01
STATUS: **DRAFT — CHƯA READY/RUN.**
Host: GPT Chat
Executor_Surface: Claude Code CLI trên Mac Owner.
Report_Write_Path: workspace_* → incomex-workspace/main.
Runtime_Write_Path: **NONE. READ-ONLY.** Cấm DNS/registrar/Cloudflare/VPS config mutation.

## 1. Mục tiêu
Tạo bằng chứng đủ để Host dựng DNS-RES cutover với tối đa 1 thao tác Owner, không suy đoán và không chờ giờ cố định.

## 2. Read gate
Đọc AGENTS → `work/dns-resilience/COLLAB.md` §0 → PROMPT này → `work/vps1-up-grade/COLLAB.md` P55/P56/P78. READY phải = commit cuối chạm PROMPT. Ghi STARTED theo DROOT31 trước PRE; RUN này read-only.

## 3. Inventory public DNS
Xác định canonical apex từ config/public service hiện hành, kỳ vọng `incomexsaigoncorp.vn` nhưng **phải đo, không mặc định**.

Từ ít nhất 3 resolver độc lập + authoritative query, thu:
- registrar/registry evidence công khai nếu query được;
- parent-zone delegation NS + TTL;
- authoritative NS/SOA serial/refresh/retry/expire/minimum;
- DNSSEC: DS/DNSKEY trạng thái;
- A, AAAA, CNAME, MX, TXT (SPF/DKIM/DMARC/verification), CAA, SRV, NS subdomain nếu có;
- mọi hostname tìm được từ nginx cert/config/compose/Kuma/app config **read-only**; không brute-force vô hạn;
- wildcard behavior;
- TTL từng RRset.

Không in secret/token. Không query private DNS credentials.

## 4. Inventory hệ thống liên quan
Read-only trên VPS1/Mac config hiện hữu:
- nginx server_name/cert SANs;
- TLS cert expiry/issuer + ACME mode nếu thấy trong config;
- Kuma monitors dùng hostname nào;
- email/MX hostnames;
- `elearning.*` và mọi public app hostname;
- registrar/provider hiện hành nếu có bằng chứng trong config/docs; không đoán từ NS nếu reseller mơ hồ.

## 5. Manifest
Tạo evidence trên máy thực thi, không tạo repo file mới ngoài COLLAB/view hiện hữu:
- `CURRENT-RRSETS.tsv`;
- `HOSTNAME-CONSUMERS.tsv`;
- `PARENT-NS.txt`;
- `DNSSEC.txt`;
- `CUTOVER-CANDIDATE.md`: exact record manifest Cloudflare DNS-only, không proxy, **không tạo zone**;
- `ROLLBACK.md`: exact old NS + điều kiện rollback;
- `MEASURED-GATE.md`: TTL/NS propagation evidence cần kiểm sau đổi, không dùng 72h cố định.

## 6. Acceptance DNS0
PASS khi:
1. authoritative source xác định rõ;
2. manifest record đủ và resolver/authoritative không còn mismatch chưa giải thích;
3. parent NS TTL + DNSSEC state rõ;
4. hostname public map được tới service/cert/monitor/mail;
5. có exact candidate manifest + rollback NS;
6. kết luận:
   - `AUTO_ZONE_POSSIBLE` nếu credential/API Cloudflare hiện hữu được chứng minh bằng metadata/config an toàn, không cần Owner secret; hoặc
   - `OWNER_CLOUDFLARE_SETUP_REQUIRED` nếu không có đường tự động; chỉ nêu đúng một nhóm thao tác tối thiểu.

KQ:
`KQ@DNSRES-DNS0-INVENTORY-20261001-01 MACHINE_DONE · INVENTORY_PASS · <AUTO_ZONE_POSSIBLE|OWNER_CLOUDFLARE_SETUP_REQUIRED>`
hoặc `DỪNG · <exact blocker>`.

Không tự đổi DNS, không tạo Cloudflare zone, không đổi registrar NS, không chạm VPS runtime.
