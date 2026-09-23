# PROMPT — HJW.2B1 · SEC-CLEAN + Scoped Capability Audit

RUN_ID: HJW-2B1-20260923-02
STATUS: DRAFT — KHÔNG RUN cho tới khi Host ghi READY@ đúng SHA cuối chạm file này

Executor_Surface: Claude Code CLI trên Mac
Runtime_Write_Path: SSH/root-operator tới VPS
Report_Write_Path: fs_* vào work/hermes-joint-workspace/
Work: work/hermes-joint-workspace/

## Mục tiêu

Sau KQ DỪNG G0.2 của HJW-2B:
1. Giảm rủi ro L1 ngay: gỡ AGENT_DATA_* khỏi môi trường Hermes nếu xác nhận không consumer hiện hành nào cần.
2. Giữ Hermes/Telegram/serve hoạt động bình thường sau cleanup.
3. Chỉ-read khảo sát phương án cấp capability hẹp bằng **thành phần hiện hữu**; chưa triển khai proxy/backend/capability route mới trong RUN này.
4. Trả lời dứt khoát: có thể tạo endpoint cho Hermes mà **không lộ master key** và endpoint tự enforce capability hẹp (tool + write scope HJW) hay không.

**Không tiếp tục automation Phase 1 trong RUN này.**

## Checkpoint

- Đọc AGENTS.md → COLLAB.md → PROMPT.md.
- Kiểm READY@ đúng commit cuối chạm PROMPT.
- Đọc KQ@HJW-2B-20260923-01 DỪNG + evidence G0.2.
- Không in/log/hash-compare giá trị secret mới; bằng chứng chỉ dùng tên biến, quyền, route, tool list, status code.
- Không chạm QDRANT key, OpenRouter key, Telegram token, GSM versions, JEV config.

## A. Read-gate trước cleanup

Xác nhận lại:
- Hermes config chưa có mcp_servers;
- hermes cron list và mọi job đang pause/disabled;
- tìm theo **tên biến** AGENT_DATA_API_KEY / AGENT_DATA_URL trong config/unit/script/runtime để xác định consumer thực tế, không in value;
- kiểm cả skills, notepad/config phụ, job paused/disabled và các process/socket đang hoặc từng nối 127.0.0.1:6533;
- xác định relay 6533 trước đây phục vụ luồng nào: workspace, Agent Data/knowledge-base hay chức năng khác;
- xác định chính xác file/script/root oneshot nào đưa AGENT_DATA_* vào /run/hermes/or.env và unit nào EnvironmentFile file đó.

Nếu có consumer hiện hành ngoài workspace MCP, có luồng knowledge-base đang dùng, hoặc bỏ biến sẽ làm hỏng chức năng đang chạy ⇒ **DỪNG trước mutation** và báo đúng consumer.

## B. SEC-CLEAN — mutation nhỏ, rollback rõ

Nếu A PASS:
1. Ghi trạng thái cron ban đầu (paused/running + số job) để khôi phục đúng sau restart.
2. Backup đúng file/script/unit sẽ sửa vào hồ sơ VPS HJW; không backup plaintext secret.
3. Sửa nguồn nạp để **không còn materialize AGENT_DATA_API_KEY** cho Hermes. Gỡ AGENT_DATA_URL khỏi Hermes env nếu không consumer nào cần; URL không phải secret nhưng không giữ cấu hình chết.
4. Không thay các secret khác trong /run/hermes/or.env.
5. Trước restart gateway/serve: gửi Owner một dòng Telegram báo Hermes sẽ gián đoạn vài phút. Gửi không thành công ⇒ DỪNG trước restart.
6. Pause cron nếu chưa pause; restart đúng service cần thiết; smoke:
   - Telegram Owner ↔ Hermes;
   - hermes-serve/local health;
   - process env chỉ kiểm **tên biến**: AGENT_DATA_API_KEY không còn;
   - OpenRouter/Telegram chức năng vẫn sống.
7. Khôi phục cron về **đúng trạng thái trước RUN**. Nếu ban đầu running thì resume; nếu ban đầu paused thì giữ paused. Xác nhận trạng thái cuối.
8. Rollback ngay nếu smoke hoặc restore-state fail; báo DỪNG.

## C. CAP-PATH-AUDIT — CHỈ ĐỌC, KHÔNG triển khai

Khảo sát các thành phần đang có: systemd socket/proxyd, nginx hiện hữu, Agent Data routes /mcp*, route/tool filters, OS ACL/socket permission, MCP client config của Hermes.

**Thứ tự audit nhanh:** đọc/đo trước các route sẵn có `/mcp`, `/mcp-readonly`, `/mcp-gpt`, `/mcp-gpt-full` và code/config filter phía server:
- route nào thực sự giới hạn tool list;
- route nào có write;
- có cơ chế hiện hữu nào giới hạn write theo path không;
- các route có dùng cùng master key hay có boundary riêng.

Phải trả lời riêng 3 lớp:

### C1. Secret isolation
Có thể để master Agent Data key ở root/server side và không cho user/process Hermes đọc được không?

### C2. Caller boundary
Có thể giới hạn endpoint cho đúng caller dự kiến bằng mechanism sẵn có (UNIX socket ACL, systemd socket permission, client ticket sẵn có...) không?

**Lưu ý:** chỉ C2 PASS vẫn chưa đủ, vì threat model L1 chính là user/process Hermes bị chiếm.

### C3. Capability boundary — BẮT BUỘC
Endpoint phải **tự enforce ở phía server/relay**, không dựa vào config/toolset của Hermes:
- chỉ expose đúng tool cần cho Phase 1;
- write chỉ được vào `work/hermes-joint-workspace/**`;
- cấm delete/destructive/exec/root khác;
- caller không thể dùng raw HTTP/MCP để vượt scope.

Được phép tận dụng route/filter/config/code **đã tồn tại**. Không viết backend mới, không thêm proxy service mới, không sửa R03 contract trong RUN này.

Kết luận:
- **FEASIBLE_EXISTING** nếu C1+C2+C3 đều làm được bằng thành phần/config hiện hữu, nêu chính xác cách và rollback.
- **NOT_FEASIBLE** nếu thiếu C3 hoặc phải sửa backend/viết proxy mới.
- Không được gọi một proxy chỉ “giấu master key” là đạt D08 nếu capability phía sau vẫn là master/full-write.

## D. Báo cáo

Cập nhật COLLAB.md + view.html:
- KQ cleanup: PASS/ROLLBACK/DỪNG;
- AGENT_DATA_* còn/không còn trong env Hermes (chỉ tên biến);
- trạng thái cron trước/sau;
- CAP-PATH-AUDIT = FEASIBLE_EXISTING hoặc NOT_FEASIBLE;
- nếu feasible: mô tả tối thiểu kiến trúc, **không triển khai**;
- nếu not feasible: nêu chính xác thiếu lớp nào C1/C2/C3.

Evidence runtime vào hồ sơ VPS của HJW theo AGENTS A8.

## CẤM

- Không tiếp tục automation Phase 1 trong RUN này.
- Không khai mcp_servers/workspace_* cho Hermes trong RUN này.
- Không dựng route/proxy/service mới.
- Không sửa backend Agent Data hoặc contract R03.
- Không mở webhook/port mới.
- Không chạm/rotate/xoá QDRANT, OpenRouter, Telegram, GSM version hoặc JEV config.
- Không đưa master Agent Data key trở lại môi trường Hermes sau cleanup.
- Không log/copy plaintext secret vào repo, evidence hoặc chat.

## BÁO CÁO / AP-CLOSE

- Chỉ dùng đúng RUN_ID `HJW-2B1-20260923-02`; không ghi lại KQ của RUN HJW-2B cũ.
- KQ@HJW-2B1-20260923-02 XONG nếu cleanup PASS và audit có kết luận rõ FEASIBLE_EXISTING/NOT_FEASIBLE.
- KQ@HJW-2B1-20260923-02 DỪNG nếu cleanup không an toàn, rollback xảy ra, restore-state fail hoặc không đủ evidence để kết luận.
- Không tự chạy nhánh tiếp theo sau KQ. Host sẽ quyết.
