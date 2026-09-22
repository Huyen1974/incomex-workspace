# Gate1 R2–R8 — evidence cho PM exit review

**READY FOR PM GATE1 EXIT REVIEW.** W003/R2–R8 SUBMITTED; Gate1 vẫn DOING. R1 đã PM ACCEPT, D03 DECIDED theo prompt 10/09. Không hiện thực hóa Gate2 hay tự nâng O1–O3.

SSOT duy nhất là file `cấu trúc hệ thống.html` trên Desktop. Tài liệu này là phụ lục evidence của SSOT, không kiến trúc có hiệu lực thứ hai. Quyết định role ngoài MOW/D03 và mọi G01–G08 là đề nghị PM. [Prompt nguồn](pm-command.md).

## Owner chỉ cần chuyển báo cáo này

[Báo cáo 12 ý cho PM](bao-cao-pm.md). Không cần đọc toàn bộ source/screenshots. PM có thể xét 5 pattern và 8 nhóm gap ngay, riêng PLATFORM FREEZE còn block cho Gate2.

## Kết luận R2–R8

| Review | Kết luận khả thi / gì được giữ | Input Gate2 |
|---|---|---|
| R2 MOT | Library C02; P02 review; C03 task contract expert; C04 merge capability; C05 HMITL workspace. C02 edit giữ code trên URL nhưng Studio không tải task; forms/reports trong drawer là schema mẫu. | Một context/revision; owner handoff; renderer/assignment/readiness chung, không chuỗi builder manual. |
| R3 MOIT/MOUT | Library C06/C09; C07 layout và C10 MOUT editor expert; C08/C11 gom binding. C21/C22 thực chất redirect v3. S01 Form/UForm/FormCustom và SharedDirectusTable ưu tiên tái dùng. C34 đang đọc report data, khác MOUT canonical-connected. | Declaration chung → render/refetch; physical mapping/query/policy rõ; không viết renderer mới chỉ vì mock chưa nối. |
| R4 Field/Table | Catalog C29/C30 có dữ liệu, nhưng 3 drilldown thiếu table render. C13 là noun review localStorage, không schema manager. F01–F10 widget type không business Field ID. | G02 reuse/search coverage/request-resume trước tạo nguyên liệu; Field meaning khác layout; Table physical name không business identity. |
| R5 Trigger/Condition | Picker C04/C08/C11 có nhưng mock; Trigger catalog count 107 không đồng nghĩa tìm được Definition. Không generic Condition library hiện hữu được chứng minh trong freeze. | Phân biệt reusable Definition, MOW/step Binding, runtime occurrence, Directus Flow config; không tạo registry mới từ kết luận thiếu UI. |
| R6 NTGV/People | Tái dùng rule-table C12/C39 vào expert/review; approval chỉ sessionStorage. Màn users hiện route Directus login404; chưa xác minh đủ People/Role/Delegation authoritative mapping. | **Một D04 proposal** vì forwarder/delegate/next-step recipient nhập nhằng; Owner quyết nghĩa, không Agent quyết. |
| R7 Governance | Shared P05 Test/Diff/Approval/Publish/Version/Help/Feedback; Guidance P01/P05. C14 QA tự chạy nên chỉ đọc source. C33 source approve→published và fallback document 1 không thể chọn làm generic approval. | D05 OPEN: giữ vai kiểm, policy quyết ai/khi nào ký; D06 OPEN: đề nghị góp ý 1 ô + authorized draft có reason/version; D07 OPEN: stop-new khác cancel-old. Không tự quyết quyền. |
| R8 Runtime | C05 workbench HMITL và C40 graph phù hợp pattern; C31 là category/Definition, C32 technical tasks. Done tại C05 chỉ đổi memory; chưa có monitor/ACK/attempt UI thật. | P04 phân biệt Workflow Instance, Task Instance, Attempt; HMITL input/result vs AUTO monitor/error/result; old run giữ pinned version. |

**Cross-owner A–F:** PASS ở role map đề nghị, runtime enforcement NOT PROVEN; D04 giữ cổng trước triển khai trách nhiệm. **AI-first:** existing default vẫn bắt người điều phối; không candidate nào fit toàn vòng nguyên trạng. Không đặt số 98% hoặc test PASS giả.

## Hồ sơ để PM kiểm

| Nội dung | File |
|---|---|
| Structured summary / trạng thái và số lượng | [Tóm tắt JSON](structured-summary.json) |
| Freeze 41 và provenance | [Frozen set](frozen-candidates.json), [hash](frozen-candidates.sha256), [scope/limitations](scope-and-limitations.md) |
| 13 câu hỏi mỗi candidate | [Structured JSON](structured-candidates.json), [bảng đọc](structured-candidates.md) |
| U01–U28 không bỏ sót | [Coverage](u01-u28-coverage.json) |
| Ít pattern và cross-owner A–F | [5 pattern role map](canonical-role-map.md) |
| Manual lặp / human boundary | [AI-first assessment](ai-first-assessment.md) |
| Duplicate / consumer / retire condition | [Disposition register](duplicate-disposition.md) |
| D04 đúng một đề xuất | [PM/Owner proposal](d04-owner-proposal.md) |
| Scope Gate2 đã nén | [8 capability groups](gap-compression.md) |
| CURRENT/TARGET + license/compatibility | [Platform freeze](platform-freeze.md), [official captures](platform-official-capture.json), [current evidence](platform-current-evidence.json) |
| Luật nguồn và patch chưa áp dụng | [RULE-SYNC preparation](rules/RULE-SYNC-01-preparation.md), [proposed patch](rules/RULE-SYNC-01-proposed.patch) |
| QA / giới hạn / chi phí | [Completeness QA](completeness-qa.json), [inventory](code-inventory.md), [limitations](scope-and-limitations.md) |
| SSOT một lần | [v1.6.15 snapshot](ssot-v1.6.15-readonly.html), [diff](ssot.diff), [write receipt](ssot-write-receipt.json), [HTML QA](ssot-stage-check.json), [visual QA](ssot-visual-qa.json) |
| R1/Gate0 acceptance evidence | [139/139 + 199/199 recheck](accepted-package-verification.json), `accepted/R1/`, `accepted/Gate0/` bản sao bất biến |

## Cách đọc implementation truth

- Mock/static/local: source data/config/DOM/sessionStorage; không được nâng từ nhãn “đang chạy”, “thật”, “SSOT”, “đã duyệt”.
- Partial: đã thấy deployed data read nhưng chưa canonical target lifecycle; không đoán authority/write từ source.
- Source-only/unproven: S01 là reusable component group; C14 không chạy do auto-test; C36/C37 live truy cập lỗi, source Nuxt cùng tên không phải UI đang phục vụ.
- Gate0 proof là PM-accepted bounded feasibility. Lát cắt renderer/adapter/worker được reuse làm evidence, không chứng minh mọi UI đã nối hay production-ready.

Các nguồn official có capture hash/UTC; current HTTP và browser states có file/URL. Source read là căn cứ logic control, screenshot/AX là căn cứ behavior nhìn thấy. Không chạy test product, không submit/approve/Done. Không tác động third-party hay nhắn PM thay Owner.

**Next actor:** GPT Chat / PM nhận/trả sửa toàn gói W003/Gate1, xét canonical roles R2–R8, D04 proposal, PLATFORM FREEZE và RULE-SYNC trước giao Gate2. Không mở R9/formal pilots hoặc build từ trạng thái READY này.
