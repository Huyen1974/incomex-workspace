# COLLAB — gsm-access-audit

## 0. MỤC TIÊU/NHIỆM VỤ USER — BẮT BUỘC ĐỌC TRƯỚC
- Mục tiêu: xác định chính xác **ai/cơ chế nào đang gọi Google Secret Manager (GSM), gọi bao nhiêu, vì sao phải gọi**, rồi loại các lượt gọi vô lý để giảm phụ thuộc Google, quota/latency/rủi ro và chi phí nếu có.
- Nhiệm vụ/phạm vi: vòng đầu **AUDIT / NO PRODUCTION MUTATION**. Rà mã/runtime/cron/systemd/container/script hiện có trên VPS + dữ liệu Google/Billing/log đã có; lập ma trận caller → secret → trigger → tần suất → lý do. Sau đó mới đề xuất mô hình cache/refresh an toàn. Không mặc định “1 lần/ngày” trước khi đo.
- Tiêu chí xong: (1) có danh sách đầy đủ caller GSM; (2) có số đo/ước lượng đủ tin cậy về calls theo caller + secret + trigger; (3) phân loại call bắt buộc / dư thừa; (4) có target architecture và trần call cụ thể; (5) nêu tác động chi phí hiện tại và sau tối ưu; (6) mọi thay đổi production chỉ ở lượt sau khi Owner duyệt.
- Xác nhận User: **ĐÃ XÁC NHẬN — Owner 2026-09-22**: việc nhỏ nhưng cần làm để tránh “rỉ máu”; lập riêng trên GitHub/workspace để chuyển phiên khác.

Host: **Claude Chat** · Host_ID `CC-GSM-0922` · Owner giao 2026-09-22 ("rà soát và soạn điều hành trên repo để Claude vào bắt đầu audit").
HTML chính: `view.html`

## Dòng hiện hành
GSM | Audit/tối ưu lượt gọi Secret Manager | việc 1–2/5 | PROMPT GSM-A1 (chỉ đọc) READY · chờ RUN | NEXT: Owner hoặc GPT Chat phát RUN cho Claude Code CLI (dòng RUN ở mục Cửa vào) | BLOCK: —

## Quyết định Owner
- D01 · 2026-09-22 · Không bỏ GSM vội. Trước tiên phải tìm caller/tần suất/nguyên nhân và tối ưu cơ chế truy cập.
- D02 · 2026-09-22 · Không được tối ưu nhầm hóa đơn: báo cáo Billing hiện hành cho thấy chi phí đang thấy chủ yếu/tất cả ở SKU **Secret version replica storage**, chưa phải bằng chứng access calls đang gây khoản ~2 USD/tháng.
- D03 · 2026-09-22 · Google Cloud không phải runtime/SSOT: VPS vẫn là SSOT mã/runtime; Google chỉ còn project `github-chatgpt-ggcloud` cho Secret Manager và các tác vụ backup/offsite đã được Owner giữ lại. Không tạo thêm project/service Google trong việc này.

## Kế hoạch
- GSM.1 | **Inventory caller — read-only:** tìm mọi đường gọi `AccessSecretVersion`/REST/gcloud/client library/wrapper trong mã, systemd, cron, Docker/container, agent scripts, gateway, health/check job. | ▶ giao RUN `GSM-A1-20260922-01`
- GSM.2 | **Đo pattern:** caller nào gọi secret nào, trigger gì (startup/request/job/health loop/cron/retry), calls/ngày/tháng, burst/concurrency; đối chiếu Billing và log/metric hiện có. **+ tồn kho version đang tính tiền (P01).** | ▶ cùng RUN `GSM-A1-20260922-01`
- GSM.3 | **Thiết kế giảm call:** ưu tiên fetch lúc process start + cache memory + pinned version; với process sống lâu dùng TTL/refresh hợp lý hoặc refresh khi rotate/restart. “1 lần/ngày” chỉ dùng nếu threat model/rotation cho phép. | □
- GSM.4 | **Review:** GPT/Claude/Codex kiểm thiết kế + rollback + secret-rotation behavior; Owner duyệt. | □
- GSM.5 | **Triển khai + đo lại:** chỉ sau duyệt; so calls trước/sau, latency/quota, health; đóng khi đạt trần. | □

## Giao Agent
- `PROMPT.md` · RUN_ID `GSM-A1-20260922-01` · Executor_Surface = Claude Code CLI trên Mac (SSH chỉ đọc VPS + `gcloud`/REST chỉ đọc) · Write_Path = `workspace_*` (dự phòng `fs_*`) · CHỈ ĐỌC · báo cáo vào `README.md` §8 + `view.html`.
- P01 · Claude (Host `CC-GSM-0922`) · Based_on `e112211` · Scope: Kế hoạch GSM.1–GSM.3 + README §7–§8 + `view.html` · đã đọc hết 3 file của việc + AGENTS.md. Đề nghị: (1) gộp GSM.1 + GSM.2 vào một RUN chỉ đọc; (2) đo từ hai phía — metric Google theo tài khoản gọi (trên xuống) đối chiếu với dựng từ mã/cron/systemd (dưới lên), lệch > 20% là còn caller chưa tìm ra; (3) thêm tồn kho version vào GSM.2 vì D02 cho thấy tiền nằm ở lưu trữ, tiêu chí xong (5) cần số này — chỉ đếm, không huỷ; (4) một file báo cáo duy nhất = README §8; `view.html` chuyển sang màn hình Owner (quyết gì · tiến độ · ma trận màu). Không chờ review GPT vì RUN không mutation; GPT góp P song song, P đúng áp ở GSM.3. · Host: ACCEPTED · Áp: `e1b4b36`
- READY@e1b4b36d1ed8b38215ac4dae9900ddfb53d03edd · Host `CC-GSM-0922` · 2026-09-22 · RUN chỉ đọc; Host đã tự rà 2 vòng (luật AGENTS A0/A6/A9 + bảo mật repo công khai; đủ 8 câu bắt buộc + nguồn đo độc lập).

## Guardrails
- Không in/log payload secret, token, service-account material hay nội dung secret.
- Không tạo Google Cloud project/API/service mới; không bật Data Access Logging hoặc telemetry có thể phát sinh chi phí nếu chưa được Owner duyệt.
- Không chuyển secret sang file/env chỉ để giảm call nếu làm tăng nguy cơ lộ. **In-memory cache trong process** là ứng viên mặc định; env/file chỉ được đề xuất khi đã nêu threat model và lý do.
- Không dùng alias `latest` làm mặc định nếu caller có thể pin version; cần giữ khả năng rollback/rotation rõ.
- Nếu nhiều process cùng dùng một secret, chỉ cân nhắc local secret broker/cache daemon khi số đo chứng minh có lợi; tránh dựng thêm hạ tầng cho việc nhỏ.
- Mọi kết luận “call nhiều” phải có số đo hoặc bằng chứng trigger; không suy từ chi phí storage.

## Câu hỏi bắt buộc phải trả lời
1. Caller GSM thực tế là những service/script/process nào?
2. Có caller nào gọi secret **mỗi request / mỗi health check / mỗi vòng cron ngắn** không?
3. Secret nào được đọc nhiều nhất? Tần suất và burst bao nhiêu?
4. Call nào chỉ cần ở startup? Call nào thật sự cần refresh giữa vòng đời process?
5. Rotation hiện diễn ra như thế nào; pin version hay dùng `latest`?
6. Nếu cache memory 1h / 6h / 24h hoặc startup-only thì failure mode là gì?
7. Access operations có thật sự vượt 10.000/tháng không? Nếu không, chi phí ~2 USD/tháng còn lại là storage active versions chứ không phải call.
8. Target call budget hợp lý theo từng caller là bao nhiêu?

## Baseline chính thức cần nhớ
- Google Secret Manager: 10.000 access operations/tháng đầu tiên miễn phí; vượt mức này giá hiện hành rất thấp theo từng 10.000 calls. Active secret versions là một dòng phí riêng.
- Google best practice: production thường pin secret version cụ thể và workload đọc khi startup; rotation/update đi theo release process.
- Nguồn tham khảo chính thức:
  - https://cloud.google.com/secret-manager/pricing
  - https://docs.cloud.google.com/secret-manager/docs/best-practices

## Cửa vào phiên sau
- Agent (Claude Code CLI): `RUN GSM-A1-20260922-01 · WS work/gsm-access-audit · Agent · đọc AGENTS.md → work/gsm-access-audit/COLLAB.md → PROMPT.md`
- Host/Review: `WS work/gsm-access-audit · <Host|Review> · GSM-A1 · đọc AGENTS.md → work/gsm-access-audit/COLLAB.md → README.md §8`

Phiên sau:
1. Host khớp `CC-GSM-0922` mới là Host; phiên khác mặc định Reviewer;
2. nhắc lại A0, không hỏi lại mục tiêu đã xác nhận;
3. sau KQ: Host nghiệm thu bằng Git + README §8 (tự gọi lại vài số đo, không tin báo cáo suông) rồi mới soạn GSM.3;
4. mọi thay đổi production + huỷ version chỉ ở GSM.5 sau Owner duyệt.

## Owner cần quyết
- —
