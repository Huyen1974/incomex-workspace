# Kiểm tra Agent Data/RAG và log VPS — 23/10/2026

**Loại hồ sơ:** báo cáo kiểm tra chỉ đọc theo yêu cầu trực tiếp của Owner. **Người kiểm:** Codex, có ba nhánh kiểm tra song song; cùng một ghế kỹ thuật, không tính là hội đồng hoặc nghiệm thu khác hãng. **Nơi chuẩn:** `work/vps-clean-20-10-26/`. Thời gian trong báo cáo dùng UTC (`Z`); cộng 7 giờ để ra giờ Việt Nam. Thu thập 22/10/2026 22:45–22:56Z, tức 23/10 05:45–05:56 +07; đối chiếu và hoàn thiện hồ sơ tới khoảng 06:00 +07. Cutoff riêng của từng phép đo ghi bên dưới.

## 1. Kết luận để Owner quyết định

**Agent Data/RAG đang hoạt động, nhưng chưa đủ bằng chứng để tin cậy vô điều kiện. Có sai lệch dữ liệu và khoảng trống kiểm soát thực tế cần xử lý.** Hiện chưa có bằng chứng toàn bộ kho hỏng hay cần dựng lại.

- **Có vector mồ côi:** 2 mã tài liệu có vector nhưng không có nguồn KB đang hoạt động. Ngoài ra có **9 điểm vector không có mã tài liệu**, bị công cụ audit theo ID bỏ sót.
- **Có thiếu vector và phân loại bỏ sót:** audit báo 1 tài liệu thiếu vector; trong 6 mục bị loại khỏi cảnh báo có thêm 1 comment có nội dung thật bị nhận nhầm là thư mục. Cần chốt chính sách nguồn trước khi reindex.
- **Có lỗi đồng bộ gần đây:** log Agent Data từ lần triển khai tối qua có 18 dòng `vector_sync_error`, trong đó xác định được 10 lỗi xóa vector timeout. Không suy rằng tất cả đã tự hồi phục.
- **Đèn xanh chưa bảo đảm dữ liệu đúng:** `/health` trả `healthy` đồng thời `data_integrity.sync_status=warning`; Docker healthcheck chỉ thăm `/info`. Audit hiện hữu còn bỏ qua vector không có ID và chưa kiểm nội dung cũ/sai nguồn.
- **Các lỗi VPS cần hiệu chỉnh:** Count Refresh định kỳ bị chặn khi ghi trực tiếp `meta_catalog`; một producer độc lập là `dot-context-pack-verify` không ghi được issue do vượt giới hạn trường; có lỗi HTTP 5xx, lỗi snapshot Git tạm thời và cảnh báo kiểm tra mirror cần phân chủ.
- **Không có bằng chứng phải chữa swap bằng restart/nâng RAM ngay:** swap gần đầy, nhưng mẫu ngắn còn RAM khả dụng và không ghi nhận swap-in/out. Áp lực bộ nhớ cục bộ và OOM lịch sử vẫn phải xem riêng.
- **Backup có tín hiệu tốt, khôi phục toàn bộ sau triển khai chưa được chứng minh trọn vẹn:** bộ offsite gần nhất có đủ hai collection Qdrant, có đối chiếu hash; không chạy restore mới trong lượt này.

**Cách sử dụng hiện tại:** RAG phù hợp để tìm đầu mối và trích đoạn. Với quyết định vận hành, phê duyệt hoặc kết luận trạng thái hôm nay, cần mở đúng tài liệu gốc, kiểm ngày/phiên và đối chiếu runtime hoặc Git workspace mới nhất. Điểm tìm kiếm không phải xác suất thông tin đúng. Các đề xuất dưới đây chưa được triển khai hoặc phê duyệt sửa.

## 2. Phạm vi và cách kiểm tra

Đã đọc `AGENTS.md`, `README.md` và `COLLAB.md` hiện hành của việc; giữ nguyên Host GPT Chat và PROMPT R3 DRAFT. Đây là lượt kiểm tra/báo cáo trực tiếp Owner yêu cầu, **không phải chạy R3, không phát READY/RUN sửa hệ thống, không đóng task VPSC2**.

Đã kiểm tra runtime Agent Data; cả hai collection Qdrant và aliases; audit nguồn KB ↔ vector theo hai chiều; cấu trúc chunk trên toàn bộ điểm; mã đồng bộ/xóa/tìm kiếm; gọi thử từ hai bề mặt MCP; log dịch vụ, kernel/systemd, backup; hash mã đang phục vụ và mẫu tài nguyên. Dùng SSH chỉ đọc và công cụ/DOT hiện hữu; không gọi heal/cleanup/reindex, không sửa hay xóa tài liệu/vector/DB/config, không restart, không tạo cron/monitor, không gửi Telegram. Chỉ các file báo cáo/trỏ báo cáo trong workspace được ghi. Truy vấn đọc bình thường có thể tạo log/history ứng dụng.

Số đếm PG và Qdrant được đọc tuần tự trong cửa sổ kiểm tra, không phải một snapshot giao dịch chung xuyên hai hệ. Phần log nêu rõ cửa sổ lưu được; không suy từ việc không thấy lỗi thành không từng có lỗi. Khi nguồn hoặc capability chưa đủ, ghi **CHƯA ĐO/CHƯA CHỨNG MINH**.

## 3. Vector và dữ liệu nguồn

### 3.1. Kiểm kê toàn bộ Qdrant

Phép kiểm kê/scroll lúc 22:50:49–22:51:51Z đọc toàn bộ payload cần thiết, không tải embedding để tái tính, không ghi dữ liệu.

| Phần kiểm | Kết quả | Ý nghĩa |
|---|---:|---|
| Số collection / alias | 2 / 0 | Không chỉ kiểm mỗi KB rồi suy ra toàn Qdrant |
| `production_documents` | 20.278 điểm | Kho truy xuất KB chính |
| Mã tài liệu khác rỗng trong collection này | 10.021 | Một tài liệu có thể có nhiều chunk |
| Nhóm có mã nguồn rỗng | 1 nhóm, 9 điểm | Không truy được nguồn theo khóa chuẩn |
| Mã tài liệu KB active duy nhất theo audit | 10.026, gồm ID rỗng | Kết quả set ID, không phải COUNT(*) tất cả hàng PG; đọc lại 22:54:01Z |
| Mã tài liệu có vector nhưng không có nguồn active | 2 mã / 2 điểm | Mồ côi theo ID, đã đọc gốc độc lập trả 404 |
| Tài liệu thiếu vector cần xử lý | 1 | Có nguồn/nội dung thật |
| Trường hợp thiếu vector bị classifier loại khỏi cảnh báo | 6 | Có ít nhất 1 false negative: comment có nội dung thật |
| `iu_core_iu_chunks` | 149 điểm / 141 mã nguồn | Nguồn dạng `information_unit/<UUID>` |

Không phát hiện trùng chỉ số chunk, thiếu chỉ số hoặc số chunk khai báo mâu thuẫn trong hai collection ở phép kiểm toàn bộ này. Đây là kiểm tra **cấu trúc**; chưa chứng minh nội dung mỗi chunk và embedding còn khớp bản nguồn mới nhất.

### 3.2. Những sai lệch đã xác nhận

**Hai nguồn mồ côi theo ID:**

1. `operations/tasks/comments/comment-1842`.
2. `registries/workflow_step_relations/wsr-87`.

Audit so nguồn active và Qdrant phát hiện cả hai; gọi độc lập `get_document_chunk` qua MCP đều trả `404 Document not found`. “Mồ côi” ở đây bao gồm nguồn đã soft-delete hoặc không còn active, không tự suy là mất vĩnh viễn trong PostgreSQL. Cần đối chiếu lịch sử xóa và chính sách lưu trước khi đề xuất dọn.

**Chín vector không có `document_id`:** payload có `document_id=''`, các chunk 0–8 của tài liệu roadmap draft ngày 14/06/2026. Hàm `list_document_ids()` bỏ qua ID rỗng nên `/kb/audit-sync` không tính chúng vào 2 mã mồ côi. Chúng vẫn chiếm điểm lưu trữ; bước search bỏ hit không có ID, có thể làm hao số ứng viên truy xuất. Chưa có bằng chứng cần xóa ngay; cần xác định nguồn, phục hồi gắn kết hoặc xử lý theo chính sách được duyệt.

**Một tài liệu thiếu vector:** `knowledge/current-state/reports/qdrant-vector-liveness-and-orphan-r1-2026-07-25.md`. Đọc độc lập qua MCP thành công: revision 1, body 44.708 ký tự. Chính báo cáo này nói về liveness/orphan; việc mở theo đường dẫn được không có nghĩa tìm kiếm vector cũng tìm được nó. Tài liệu dài như vậy không thuộc nhóm rỗng/placeholder được miễn vector.

**Classifier bỏ sót thêm một nguồn có body:** raw ghost là 7, nhưng audit loại 6 mục: một ID rỗng, `test_empty.md.tmpl`, ba đường `knowledge/dev`, `knowledge/dev/blueprints`, `knowledge/dev/laws`, và `operations/tasks/comments/comment-2430`. Comment-2430 đọc được body 105 ký tự, revision 1; bị coi `directory_like_path` chỉ vì tên không có đuôi file. Đây là false negative của cách phân loại. Nội dung là healthcheck; cần quyết có giữ loại này trong semantic corpus hay không, không tự động embed chỉ để số audit về 0.

**Trùng nội dung cần xem có chọn lọc:** có 185 nhóm hash chunk giống nhau giữa các nguồn khác nhau; có bản draft/report hợp lệ. Đếm được **77 tài liệu/77 điểm** chứa cùng mẫu `Health check: OPS write OK at undefined`, thuộc comment-2393…2470 trừ comment-2430 đang thiếu vector. Đây là tín hiệu nhiễu chất lượng kho, **không phải 185 vector mồ côi hay 185 lỗi cần xóa**. Nên thống nhất nguồn nào cần đưa vào RAG trước khi dọn bản sao hoặc dữ liệu thử. Chưa đo tác động tới recall/precision.

### 3.3. Kho IU và giới hạn tính đầy đủ

149 điểm IU có cấu trúc chunk hợp lệ, không phát hiện `point_key` trùng trong phép kiểm. **Chưa đối chiếu được toàn bộ 141 mã nguồn với bản ghi IU thật qua capability/DOT đọc nguồn đã được xác minh.** Vì vậy không kết luận “IU sạch mồ côi” và không mở rộng kết luận KB sang IU.

**CHƯA ĐO:** đối chiếu toàn bộ body/hash/phiên nguồn PG với từng payload chunk; tái tính embedding; semantic recall/precision trên bộ câu hỏi chuẩn; tỷ lệ nguồn mới nhất theo ngày; khả năng bỏ sót sự kiện trong những lần ngắt kết nối trước cửa sổ log. Không gộp việc chưa đo này thành PASS.

## 4. Đồng bộ và độ tin cậy của RAG

### 4.1. Lỗi đồng bộ có thật, cơ chế vẫn có khoảng hở

Trong log Agent Data giữ được sau lần triển khai 22/10 15:06Z đến khoảng 22:48Z có **18 dòng `vector_sync_error`**. Có **10 dòng xóa vector timeout** xác định được nguồn, tập trung 18:00:12–18:00:36Z, liên quan các CAT-008/013/009/018/020/021/024/045/078/026. Chưa chứng minh chúng là nguyên nhân của hai nguồn mồ côi hiện tại; không gán quan hệ nhân quả chỉ vì cùng hệ vector.

Đối chiếu nội dung độc lập lúc **22:55:46Z** cho chín CAT đầu trong danh sách trên: **9/9 body nguồn PG qua MCP và payload Qdrant có SHA-256 khớp**, mỗi nguồn một điểm. Mẫu này chưa thấy stale payload còn lại sau timeout; CAT-026 chưa có phép so hash trong mẫu, và không suy từ chín nguồn ra toàn kho hoặc tính đúng của embedding.

`vector_store.py` ghi chi tiết action/document/error bằng `extra`, nhưng plain-text log giữ lại chỉ hiện token `vector_sync_error`; 8 dòng còn lại chưa phân đủ hành động và nguồn. Đây là nợ khả năng truy lỗi, khiến việc điều tra phải dựa vào dòng phụ hoặc audit dữ liệu.

Đọc mã cho thấy:

- API cập nhật lưu nguồn PG trước rồi xử lý vector theo best-effort; lỗi xóa chỉ được log. API xóa vẫn đánh dấu nguồn deleted sau lần thử xóa vector dù thao tác vector có lỗi. Không có giao dịch nguyên tử PG–Qdrant.
- Listener dùng PG NOTIFY và có khóa leader, giúp tránh mỗi worker xử lý cùng một sự kiện. Trong nhánh đã đọc, kết quả đồng bộ `error` không được ghi thành một hàng đợi retry bền hoặc dead-letter để khôi phục theo sự kiện. Kết nối lại không tự chứng minh các sự kiện đã lỡ được phát lại.
- `upsert_document` tạo ID chunk xác định, ghi các chunk mới nhưng không tự xóa đuôi chunk cũ khi nội dung ngắn đi. API update có bước xóa trước; đường listener upsert không có bước đó. Đây là rủi ro thấy trong mã; phép kiểm cấu trúc hiện tại **không phát hiện đuôi chunk sai**, chưa kết luận đang có hỏng nội dung từ cơ chế này.

Do đó, sửa nguồn hoặc upsert thành công chưa đủ để đánh dấu đồng bộ hoàn tất; điều kiện nghiệm thu cần gồm đối chiếu nguồn–vector và phục hồi khi lỗi.

### 4.2. Health và công cụ audit đang phản ánh thiếu

Mẫu `/health` trong container trả:

```json
{"status":"healthy","data_integrity":{"document_count":10026,"vector_point_count":20278,"ratio":2.02,"sync_status":"warning"}}
```

Docker kiểm `/info` mỗi 15 giây; đây là dấu hiệu tiến trình trả lời được. `_compute_data_integrity()` trong `server.py` dùng tỷ lệ số vector/tài liệu với ngưỡng cứng. Chunking hợp lệ cũng làm tỷ lệ tăng; tỷ lệ này không cho biết chính xác mồ côi, mất vector hoặc nội dung cũ. Trạng thái overall không hạ theo trường warning này. Không nên diễn giải “healthy” thành “dữ liệu nhất quán”.

DOT `dot-vector-audit` còn có cấu hình mặc định/credential fallback cũ: một lần gọi không xác thực thành công vẫn in dấu `?`, Orphans/Ghosts=0 và exit 0. Lần kiểm được dùng cho số liệu trong báo cáo đã ràng buộc đúng runtime, xác thực thành công, `auto_heal=false`. **Không sử dụng số 0 của lần gọi thất bại làm chứng cứ sạch.** Không đưa credential vào hồ sơ này.

### 4.3. Kiểm thử truy xuất từ client thật

| Probe chỉ đọc | Quan sát | Kết luận được phép |
|---|---|---|
| Tìm `vps-clean-20-10-26`, direct MCP, limit 5 | 5 kết quả; 1.802 ms; top tài liệu kiến trúc 26/03/2026 | Tìm được tư liệu liên quan; chưa chứng minh trạng thái việc tháng 10 |
| Tìm chủ đề Agent Data/Qdrant/orphan | 5 kết quả; 1.879 ms; top báo cáo 02/05/2026 | Đường embedding–retrieval đang hoạt động ở mẫu này |
| Chuỗi chưa có `AUDIT_READONLY_20261023_ZZQ9_NO_SUCH_DOCUMENT` | Vẫn trả tư liệu cũ không trả lời chuỗi này; tagged plugin trả 3 kết quả trong 370 ms | Không có cổng bảo đảm “không tìm thấy nguồn đúng” ở lớp retrieval |
| Tagged Incomex plugin limit 1 | Trả đúng 1 kết quả, 239 ms | Giới hạn đúng ở profile này |
| Direct MCP limit 3 | Trả 5 kết quả | Khác biệt contract ở đường legacy, không quy lỗi cho mọi client |
| Đọc trực tiếp hai mã mồ côi / một nguồn thiếu vector | 404 / 200 tương ứng | Xác nhận độc lập audit theo ID |

Chế độ hiện hành trả các snippet nguồn, không phải một câu trả lời vận hành đã xác minh. Điểm `score` cộng thêm boost đường dẫn/tiêu đề/tag và có thể có ưu tiên độ mới; không phải confidence 0–1 về sự thật. Mỗi snippet chỉ lấy tối đa 500 ký tự của chunk được chọn, nên dễ mất điều kiện/ngoại lệ ở phần khác.

`vector_store.search()` bắt lỗi rồi trả danh sách rỗng; `/chat` có thể chuyển sang keyword scan PG. Nếu cả hai không trả context, raw mode có thể trả HTTP 200 với nội dung rỗng. **Đây là rủi ro từ mã đã đọc, không phải một outage được cố ý gây ra trong audit.** Consumer chưa có trường rõ ràng phân biệt “không có kết quả”, “đang fallback” và “nguồn truy xuất lỗi”.

Git workspace và KB là hai nguồn có hợp đồng riêng. Không tìm được task mới bằng vector không tự chứng minh Git sync hỏng. Tra việc hiện tại phải dùng `workspace_read/search` và kiểm `freshness/source_head`.

## 5. Log VPS gần đây và điều cần hiệu chỉnh

Cutoff cố định cho số HTTP/PG là **22/10 22:48:55Z**; cửa 24 giờ bắt đầu 21/10 22:48:55Z. Log Agent Data chỉ còn từ 22/10 15:06:22Z sau recreate (~7 giờ 42 phút), nên không đủ 24 giờ/7 ngày. Directus chỉ còn từ 18/10 10:55Z, không đủ 7 ngày. Qdrant, nginx và PostgreSQL còn đủ cửa 7 ngày yêu cầu. Không cộng lỗi nhiều tầng thành số sự cố độc lập.

| Dịch vụ | Request nhận dạng trong 24 giờ/phần còn lưu | 5xx | 7 ngày/phần còn lưu |
|---|---:|---:|---|
| Agent Data | 7.574 trong ~7h42 | 0 | Thiếu log trước recreate; lỗi đồng bộ async vẫn có |
| Qdrant | 11.233 | 0 | 78.808 request, 0×5xx |
| Directus | 37.355 | 16 | Từ 18/10: 180.241 request, 63×500; không gọi là đủ 7 ngày |
| nginx | 42.203 | 7 | 286.053 request, 472×5xx: 238×502, 200×503, 19×500, 15×504 |

472 lỗi trong 7 ngày và 7 lỗi trong 24 giờ phản ánh hai cửa sổ khác nhau, chưa chứng minh một triển khai cụ thể đã giải quyết nguyên nhân. Traffic có healthcheck/probe/scan; bảng này không phải SLO nghiệp vụ.

### 5.1. Lỗi nguồn dữ liệu lặp lại

PostgreSQL 24 giờ có **41 sự kiện ERROR/FATAL** theo severity header, gồm hai producer lỗi độc lập:

- **16 lần UPDATE số đếm `meta_catalog` bị S129-A chặn**, tương ứng **4 đợt × 4 PATCH** lúc 00:00, 06:00, 12:00, 18:00Z ngày22/10 vào các bản ghi19/42/122/27; Directus có 16 HTTP500 cùng dạng lỗi counting fields. Đây là16request, không phải16lần flow chạy. Rào bảo vệ đang làm việc; caller định kỳ vẫn dùng đường không hợp lệ. Phù hợp với R2-6 trước đó SKIP, không coi đã được sửa. Chủ TQT/DOT cần sửa caller theo công cụ được phép.
- **16 lỗi `fn_log_issue` vượt `varchar(50)`**, nguồn `dot-context-pack-verify`: 8 slot 01:30, 04:30, 07:30, 10:30, 13:30, 16:30, 19:30, 22:30Z, mỗi slot 2 lỗi. Statement cho thấy checker H11a báo basic-description-missing từ 7.007→7.014, H11b detail-description-missing 451; đây là số trong cảnh báo checker, chưa độc lập đếm lại dữ liệu nền. **Lỗi đã xác nhận là INSERT issue thất bại**, không phải truy vấn kiểm description bị crash. `entity_code` dài 69/70 ký tự là dấu hiệu lệch giới hạn; log không chỉ cột gây overflow, cần đối chiếu schema trước khi sửa. Không gắn lỗi này cho Count Refresh.

Chín lỗi còn lại gồm 3 FATAL do caller dùng role `postgres` không tồn tại và 6 lỗi query/schema/type không khớp. Chưa xác định caller; có thể là probe/audit, không suy PG crash. Trong 7 ngày có 261 ERROR/FATAL; 36 lỗi `btrim(integer)` chỉ thấy tới 20/10 10:00Z và không xuất hiện trong 24 giờ cuối, không liệt kê là lỗi đang tái diễn.

Không nới S129-A hoặc quyền ghi trực tiếp để làm tác vụ hết lỗi. Không tắt flow hay sửa schema trong lượt báo cáo này.

### 5.2. HTTP 5xx và cửa sổ triển khai

Nginx 24 giờ có **7 phản hồi 5xx** được nhận diện:

| UTC 22/10 | Đường gọi | Mã | Nhận định |
|---|---|---:|---|
| 04:00:12 | `/server/ping` | 503 | Ngoài cửa sổ recreate Agent Data; nguyên nhân chưa chứng minh |
| 09:37:02 | `/api/presence/event` | 502 | Cần đối chiếu upstream đúng thời điểm |
| 15:06:38 | `/api/mcp` | 502 | Trùng cửa sổ Agent Data recreate |
| 15:06:41–42, 3 lần | `/api/health` | 502 | Trùng cửa sổ recreate |
| 19:30:11 | `/items/tasks` | 503 | Ngoài cửa sổ recreate; cần chủ web/Directus đối chiếu |

Bốn lỗi 502 trùng thời điểm triển khai không đồng nghĩa service liên tục lỗi suốt ngày. Hai 503 ngoài cửa sổ vẫn cần điều tra; chưa đủ bằng chứng quy cho CPU/swap, R2 hoặc Graph. Không tính tỷ lệ uptime/SLA khi chưa có mẫu tổng request và quy tắc loại healthcheck phù hợp.

Có nhiễu quyền/route cần đối chiếu producer: Directus 24 giờ có 3.917×403 (trong đó `/items/pages` 2.620, `/server/health` 451, `/items/web_incomex_inbox` 300); Agent Data có 97 POST `/mcp-agent`401, 32 GET/HEAD405. Có thể là test deny, consumer sai credential hoặc monitor gọi đường không được phép; chưa chứng minh user hợp lệ bị chặn. Không cấp quyền rộng để hết log đỏ. Nginx có 98×499 là client đóng kết nối, không tự cộng thành server5xx; 881 warning response buffered-to-tempfile trong cửa log độc lập là I/O spill cần đo trước tuning.

### 5.3. Hệ điều hành và snapshot

- `systemd-networkd-wait-online.service` hiện failed; timeout ngày 22/10 04:38:49Z sau khi bắt đầu 04:36:48Z. Dịch vụ mạng/VPS vẫn phục vụ trong mẫu kiểm tra. Cần chủ hạ tầng kiểm quan hệ wait-online với interface thật; không coi failed unit này là bằng chứng đang mất mạng và không chỉ reset-failed để che dấu.
- Có 3 lỗi snapshot trong 24 giờ do `index.lock exists` ở Git notebook UI. Lượt gần nhất 22:50:55Z đã `success`, exit 0. Cần xem tương tranh/khóa và cơ chế phát hiện snapshot bị bỏ lỡ; **không tự xóa lock** khi chưa biết tiến trình đang giữ.
- Receipt retention 22:30:46Z ghi `FSCK_SAU_LOI` cho hai mirror Git. Kiểm connectivity sau đó exit 0; full fsck bị timeout 30 giây, chưa chứng minh corruption hoặc full integrity. Cơ chế hiện tại nuốt stderr và vẫn return 0 nên receipt chưa đủ giúp phân biệt lỗi Git, timeout và tình trạng tạm thời.
- Có lỗi apt-daily liên quan network timeout; không tự kết luận bản vá an toàn đã được áp đủ.
- Config drift-check đã success 22:40Z, **510/510 MATCH**, 0 fail trong 24 giờ; 636 failed events của 7 ngày đều trước 19/10 04:10Z. JEV health cũng 0 fail/24h, lần cuối success. Không báo lỗi lịch sử này như lỗi hiện hành.
- Hàng nghìn dòng UFW block là hoạt động chặn lưu lượng ngoài vào; không cộng chúng thành hàng nghìn lỗi ứng dụng hoặc bằng chứng bị xâm nhập.

### 5.4. OOM lịch sử

Kernel còn lưu 4 lần OOM kill trong 7 ngày: 18/10 15:06:20Z, 21/10 14:05:51Z và 22/10 02:48:38Z, 02:51:49Z. Lần 18/10 xác định thuộc `incomex-claude-kb`. Ba lần Python còn lại thuộc cgroup container khác đã không còn trong inventory hiện tại; giới hạn khoảng 1 GiB phù hợp môi trường thử nhưng **chưa có mapping bằng receipt để gọi là rehearsal hợp lệ**. Không gán ba lần này cho Agent Data hoặc cho rằng không quan trọng. Chủ Graph/executor cần đối chiếu container ID với hồ sơ lần chạy.

Container Agent Data hiện hành có RestartCount=0/OOM=0 là số của vòng đời container này; không phủ nhận OOM lịch sử của VPS.

## 6. Runtime, tài nguyên và tác động các triển khai

### 6.1. Agent Data sau lần triển khai 22/10

Runtime dùng image `agent-data-hvu:hjw-cap-20261022`, release source `b6ebaf945308638ce3af61d44b5efaa54a67d680`, bắt đầu 15:06:20Z. Mã phục vụ nằm trong `/app`, có mount source riêng vào `/workspace/agent-data`; không suy mount source là code đang thực thi. **31 file Python/JSON ứng dụng đối chiếu SHA-256 khớp byte, 0 file thay đổi hoặc chỉ có trong app**; source có thêm 7 macOS sidecar `._*.py` không đóng vào image. Không kiểm toàn bộ dependency packages/config; không tuyên bố mọi file trên VPS đều không drift. Image chưa có OCI source-revision label; nhận diện release được hỗ trợ bởi phép so hash hiện tại.

14 container đang chạy trong inventory. Agent Data, PostgreSQL, Qdrant và Directus có health xanh ở thời điểm đọc. Các thay đổi Graph, Nuxt, Hermes và Agent Data gần nhau về thời gian làm nhu cầu truy release/footprint tăng; log và receipt cần ghi được phiên đang chạy để phân biệt lỗi triển khai với nợ cũ.

### 6.2. Mẫu tài nguyên

Mẫu khoảng 22:48Z có swap dùng khoảng 2.044/2.047 MiB, RAM available khoảng 6,2 GiB; `vmstat` 10 giây ghi si=0, so=0 và CPU idle khoảng 80–90%, iowait 0. **Không chứng minh host đang thrashing hoặc thiếu RAM toàn cục trong mẫu này.** Mẫu ngắn không bảo đảm các giờ cao điểm cũng tương tự. PSI memory avg10 some/full là 0,36%/0,21%, IO 0,73%/0,57%; là mẫu ngắn, không phải độ trễ p95 ứng dụng.

Agent Data có khoảng 1,30 GB cgroup RAM và 776,6 MB swap với giới hạn RAM 6 GiB. Claude MCP dùng khoảng 1,447/1,61 GB theo cgroup, `memory.events.max=5643`, không có OOM trong snapshot cgroup hiện tại. Counter `max` là lịch sử chạm giới hạn, không phải 5.643 vụ OOM, không đủ để gọi là heap leak; cgroup gồm cả page cache, khác process RSS.

Không đề xuất tăng RAM, swapoff, drop_caches hoặc restart để làm đẹp số. Nếu cần quyết định tiết kiệm tài nguyên, tiếp tục đo theo từng cgroup/đúng giờ chậm bằng cơ chế sẵn có; không thêm lớp monitor mặc định.

Watcher đĩa 22:00Z đang green, root còn khoảng **45,6 GB**; dung lượng dùng tăng khoảng **549 MB/24h**, giảm khoảng 2,53 GB/72h. Có 4 debt theo dõi, 0 overdue; không coi green là nguồn tăng trưởng đã được quy đủ. Hai job config-drift và presence-import trong 24 giờ có tổng **973,7 CPU-giây**, khoảng **0,188% năng lực 6 vCPU/ngày**. Đây chỉ là chi phí hai job có accounting, không phải tổng mọi cơ chế canh và không phải số tiết kiệm before/after. Nhịp config20 phút/presence-import10 phút còn đúng cấu hình R2.

## 7. Backup, retention và khả năng khôi phục

- Log local PG và Qdrant 16–22/10 ghi 7/7 lượt thành công cho từng job; bản PG local mới nhất kết thúc 22/10 00:28:37Z, Qdrant 01:00:26Z. Daily Qdrant local chỉ lấy `production_documents`.
- Bộ offsite mã hóa `20261022T183701Z` có đủ 8 file data+sidecar trên Drive. Hash SHA-256 ciphertext đối chiếu khớp cho bốn phần DB/cấu hình/metadata/data. Log/source của bộ offsite cho thấy **cả `production_documents` và `iu_core_iu_chunks` được snapshot**, nên không kết luận IU thiếu backup chỉ vì job local có một collection.
- Log Drive 16–22/10 có 7 lượt PASS, không thấy FAIL hoặc QDRANT_DEGRADED trong cửa sổ đã kiểm. Backup code có các lượt DONE; điều này hỗ trợ tính liên tục của lưu bản sao, chưa thay bằng chứng restore.
- Tar dữ liệu sống có cảnh báo `file changed as we read it` trong 21–22/10. Với SQLite hoặc dữ liệu đang ghi, một tar thành công không tự bảo đảm ảnh nhất quán ứng dụng. Cần xác định nguồn cụ thể/biên nhận snapshot; không suy toàn bộ backup hỏng.
- Đã tìm thấy bằng chứng **restore PG18 thật ngày 03/10, G7-05**: Directus391 bảng và metadata10 bảng, `ISOLATED_RESTORE=PASS`, comparison mismatch0, negative control fail-closed, rc0, residue0. Hồ sơ tại `work/done-tasks/vps1-up-grade/G7/VPSUP-G7-PROD-CUTOVER-20261003-05/results/restore-verify-{directus,metadata}.txt` dưới kho VPS. Không chạy restore mới từ bộ offsite22/10; restore cũ không chứng nhận dữ liệu hôm nay. Restore Qdrant gần nhất chưa được kiểm lại đầy đủ trong audit này.
- **Khoảng trống config/docs hiện hành:** các job offsite đã đọc không bao gồm toàn cây `/opt/incomex/config` hoặc `/opt/incomex/docs`. Repo `/opt/incomex` có `config/workspace-exec.json` và `config/workspace-tools.json` khác Git, last commit chạm hai file là18/09; workspace-tools hiện mtime22/10 15:12Z. Backup code/metadata không tự khôi phục được cấu hình quyền/capability đúng phiên. `backup-agent-configs.sh` đã đọc chỉ xử lý cấu hình Mac; snapshot mcp-writes là Git local. Chưa chứng minh đường offsite/restore cho hai cây này trong những job được kiểm; không khẳng định tuyệt đối không có bản sao nơi khác.
- Có lệch giữa nhãn lịch, filename và giờ log thực tế: Qdrant ghi dự kiến03:00UTC nhưng log chạy01:00Z; code backup filename01:00ICT ứng với18:00Z hôm trước. Cần chủ backup xác nhận timezone hiệu lực/RPO mong muốn trước khi đổi lịch; không báo backup mất chỉ vì tên hoặc giờ khác dự kiến.

## 8. Việc nên làm tiếp — đề xuất, chưa triển khai

| Ưu tiên | Việc cụ thể | Chủ tiếp nhận | Điều kiện nghiệm thu |
|---|---|---|---|
| Sớm | Xác minh 2 nguồn mồ côi, 9 điểm thiếu ID, nguồn thiếu vector và comment bị phân loại sai; sửa theo chính sách từng nguồn | Chủ Agent Data/RAG + dữ liệu nguồn | Manifest trước/sau; nguồn hợp lệ; audit 2 chiều; không mất dữ liệu hợp lệ; có rollback và readback |
| Sớm | Sửa khả năng báo thất bại của DOT audit, classifier tên không có đuôi và kiểm ID rỗng/nguồn IU | Chủ DOT/RAG | Auth/upstream lỗi phải exit khác 0; audit không giả sạch; có đối chiếu cả hai collection và giới hạn nội dung/hash công khai |
| Sớm | Khép lỗi đồng bộ khi timeout/mất kết nối và khôi phục log action/doc/error | Chủ Agent Data | Lỗi không bị “thành công” che; retry/outbox/reconcile có receipt; thử lỗi và content thu ngắn trên môi trường an toàn |
| Sớm | Sửa Count Refresh và lỗi ghi issue độc lập của context-pack-verify | Chủ TQT/DOT | Caller qua đường được phép; ghi sổ lỗi thành công; kiểm riêng hai producer ít nhất một chu kỳ thật; không nới rào S129-A |
| Kế tiếp | Phân biệt health sống, integrity và retrieval degraded trong consumer đang có | Chủ Agent Data/giám sát | Hiển thị lỗi/thiếu nguồn đúng; thử âm; không mở rộng số monitor nếu cập nhật cơ chế hiện hữu đáp ứng được |
| Kế tiếp | Xử lý 503 ngoài triển khai và lỗi snapshot/retention Git | Chủ CWEB/TQT và hạ tầng | Có correlation request/upstream; phân rõ lock/timeout/corruption; receipt lỗi không bị exit 0 che |
| Kế tiếp | Khép restore set sau triển khai và kiểm tính nhất quán dữ liệu sống | Chủ backup/hạ tầng | Liệt kê nguồn → bản sao → hash → cách restore; thử khôi phục cách ly theo phép riêng, gồm hai Qdrant và config/ACL đúng phiên |
| Theo dõi | Phân OOM/cgroup pressure, wait-online, nhiễu healthcheck trong KB | Chủ từng dịch vụ | Mapping evidence rõ; đo đúng giờ tải; không dọn/xóa hàng loạt theo tên hoặc counter tích lũy |

Ưu tiên dùng tính năng, cấu hình và cơ chế đang chạy; chỉ thêm mã mỏng khi không có khả năng hiện hữu đáp ứng. Không có lý do từ số liệu này để bulk reindex, xóa toàn Qdrant, tắt Guard hoặc restart cả VPS. Mỗi hành động sửa có tác động cần phạm vi/phép thực thi riêng theo quy tắc workspace.

JEV được dùng làm ý kiến phụ về ba lựa chọn: tin cậy có điều kiện; đề xuất sửa có giới hạn; chưa chứng minh thrashing từ mẫu swap. Receipt `gen-dec-1792709594-PuKtgdDFuxPK2Fuf2sJT`. JEV không kiểm VPS và không thay bằng chứng hoặc nghiệm thu của Owner/Host.

## 9. Bằng chứng và cách tiếp tục

| Nguồn bằng chứng | Nội dung/cách kiểm | Giới hạn |
|---|---|---|
| Runtime/source Agent Data | `docker inspect`, hash các file `/app` so `/opt/incomex/docker/agent-data-repo` | Chỉ footprint đã đo; không in env/credential |
| Audit nguồn–KB | Existing DOT `dot-vector-audit`, `auto_heal=false`, ràng buộc đúng local runtime | Chỉ ID; nhánh lỗi wrapper không phải bằng chứng sạch |
| Qdrant inventory | List collections/aliases và scroll toàn bộ payload 22:50:49–22:51:51Z, `with_vectors=false` | Không tái tính embedding; IU nguồn chưa đối chiếu |
| Readback gốc từ Codex | `get_document_chunk` hai orphan404, nguồn thiếu vector200 | Không viết/sửa tài liệu |
| Client retrieval | Direct MCP Agent Data và Incomex MCP full all 2, các probe tại §4.3 | Mẫu chức năng, không phải bộ eval recall |
| Mã đồng bộ | `agent_data/server.py` `_sync_vector_entry`, `_delete_vector_entry`, `_run_audit`, `_retrieve_query_context`; `vector_store.py`; `pg_vector_listener.py` | Rủi ro mã ghi riêng với lỗi thực đo |
| Logs | Docker retained logs; nginx; kernel/systemd journal; PG/Directus qua log và DOT | Theo cửa sổ lưu thực tế; Agent Data chỉ từ lần recreate |
| Backup/retention | Log job, sidecar/hash và Drive listing bộ 22/10; receipt retention; fsck chỉ đọc | Không tạo snapshot/backup/restore mới |
| Quyền/phạm vi | Yêu cầu Owner tại chat23/10; AGENTS/README/COLLAB việc | Chỉ kiểm tra và báo cáo |

Không chép nguyên khối log hoặc dữ liệu nghiệp vụ vào repo công khai. Muốn xử lý tiếp, bắt đầu từ các lỗi đã xác nhận và điều kiện nghiệm thu ở §8; không dùng báo cáo này làm lệnh sửa production, không thay dấu READY của R3 DRAFT.
