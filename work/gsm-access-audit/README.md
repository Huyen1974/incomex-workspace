# GSM Access Audit — đề bài kỹ thuật

## 1. Vì sao mở việc này

Owner muốn loại mọi cơ chế gọi Google Secret Manager (GSM) vô lý, dù chi phí tuyệt đối nhỏ. Mục tiêu là giảm phụ thuộc Google, quota/latency/rủi ro và chi phí nếu access calls thực sự vượt free tier.

**Không được nhầm:** báo cáo Billing gần nhất cho project `github-chatgpt-ggcloud` đang quy chi phí nhìn thấy vào SKU **Secret version replica storage**. Vì vậy audit call frequency là một bài toán kiến trúc/vận hành trước; nó chỉ giảm trực tiếp hóa đơn khi access operations thực sự vượt free tier hoặc kéo theo SKU khác.

## 2. Câu hỏi audit

Tạo ma trận:

| Caller | Secret | API/cách gọi | Trigger | Tần suất | Burst | Version ref | Có thể cache? | Lý do |
|---|---|---|---|---:|---:|---|---|---|

Phải phủ:
- app/service trên VPS;
- systemd;
- cron;
- Docker/container entrypoint;
- gateway/MCP/agent;
- health check;
- backup/deploy/update scripts;
- tool chạy tay nhưng lặp thường xuyên;
- mọi wrapper gọi `gcloud secrets versions access`, GSM REST/gRPC hoặc client library.

## 3. Cách đo — ưu tiên không mutation

1. **Static search:** tìm GSM API/client/wrapper và secret resource names trong code/config.
2. **Runtime mapping:** map process/container/unit/cron → script/binary → secret call.
3. **Existing evidence:** dùng log/metric/Billing/Audit log đã có; không bật logging mới có thể phát sinh chi phí nếu chưa được duyệt.
4. **Call-rate reconstruction:** từ cron cadence, request path, loop/retry và process restart frequency.
5. Nếu chưa đủ để định lượng, đề xuất một instrumentation nhỏ ở lượt sau; không tự cài trong GSM.1.

## 4. Kiến trúc mục tiêu — chưa phải quyết định triển khai

Ưu tiên từ đơn giản đến phức tạp:

### A. Startup fetch + in-memory cache
Phù hợp khi secret chỉ cần lúc service khởi động. Pin version cụ thể. Rotation qua deploy/restart có kiểm soát.

### B. In-memory TTL refresh
Cho process sống dài cần nhận rotation mà không restart. TTL chỉ đặt sau khi biết yêu cầu rotation. 1h/6h/24h là các phương án cần đánh giá, không phải mặc định.

### C. Event/reload có kiểm soát
Khi rotate secret, gửi reload/restart cho đúng service; tránh polling GSM liên tục.

### D. Local broker/cache
Chỉ khi nhiều process cùng đọc cùng secret và tổng call thực sự đáng kể. Tránh dựng thêm service nếu A/B đủ.

**Không mặc định env/file cache.** Google cảnh báo file system và environment variables có thể làm tăng nguy cơ lộ secret; nếu dùng phải nêu threat model và biện pháp che log/debug.

## 5. Tiêu chí thiết kế

Với từng caller phải chốt:
- max calls/day;
- max stale time của secret;
- behavior khi GSM unavailable;
- startup failure policy;
- rotation procedure;
- rollback;
- cách tránh thundering herd khi nhiều process restart;
- cách đo trước/sau.

## 6. Baseline giá và best practice

Nguồn chính thức:
- Pricing: https://cloud.google.com/secret-manager/pricing
  - 10.000 access operations/tháng đầu miễn phí;
  - active secret versions tính riêng;
  - destroyed versions không tính storage.
- Best practices: https://docs.cloud.google.com/secret-manager/docs/best-practices
  - ưu tiên pin version cụ thể;
  - workload thường đọc secret lúc startup;
  - không mặc định đưa secret vào file/env nếu không cần.

## 7. Deliverable vòng audit

Không cần tài liệu dài. Kết quả GSM.1–GSM.3 nên gom vào **một mục mới trong file này** hoặc `view.html`:
- top callers;
- calls/month hiện tại;
- root cause của call thừa;
- target call budget;
- phương án ít thay đổi nhất;
- tác động chi phí;
- rủi ro/rollback.

Không tạo thêm file progress/archive nếu không cần.
