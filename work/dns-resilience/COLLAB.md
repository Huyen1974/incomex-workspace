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
DNS-RES | **DNS0 READY/RUN · READ-ONLY INVENTORY** | PROMPT last-touch `3b46b4650b4981d2c4b59b92ee1e26b5699222d8`; `READY@3b46b4650b4981d2c4b59b92ee1e26b5699222d8`; RUN_ID `DNSRES-DNS0-INVENTORY-20261001-01` | NEXT: Agent inventory/measure → Host review manifest + xác định bước tự động/Owner duy nhất.

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

## Owner cần quyết
- —

## Con trỏ
- Luật: ../../AGENTS.md · ../../README.md · ../README.md
- Nguồn quyết định gốc: ../vps1-up-grade/COLLAB.md · P55/P56/P78
