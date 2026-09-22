# Gate3–4 v1.6.17 — đọc từ đây

**Bàn giao ngày 11/09/2026: BLOCKED BY DATA-AUTHORITY + LIFECYCLE-AUTHORITY.** Có kết quả một phần, chưa đủ đóng Gate3/4. Gate0–2 giữ phạm vi PM đã nhận; D04 WAITING OWNER; Gate5–7 NOT STARTED và O1–O3 NOT VERIFIED.

Nguồn chuẩn duy nhất của dự án là [cấu trúc hệ thống](<../cấu trúc hệ thống.html>). Thư mục này giữ bằng chứng của lượt v1.6.17, không thay thế trạng thái hiện hành trong file chính. Bản v17 được ghi một lần sau backup và QA; receipt lưu hash bản trước/bản sau. Khác biệt giữa v16 PM đã xem và v16 đầu lượt là thay đổi tổ chức workshop/README do Owner chỉ đạo sau đó, được ghi rõ trong receipt.

## Chuyển cho GPT Chat / PM

1. Mở [báo cáo 12 ý](BAO-CAO-GUI-PM.md), sao chép toàn bộ và dán vào Chat.
2. Đính kèm [một ZIP bằng chứng](../Gate3-4-v1.6.17-bang-chung.zip). Không cần gửi từng file hoặc yêu cầu Chat truy cập đường dẫn trên máy.

ZIP có README là bản báo cáo, summary, snapshot HTML đúng byte, khai báo, dữ liệu, raw results, nguồn và manifest SHA256. Chat đọc báo cáo → QA → summary, rồi chỉ mở bằng chứng cần phản biện. Một số liên kết **lịch sử** trong HTML vẫn cần workspace cũ; toàn bộ bằng chứng mới của lượt này có trong ZIP. Thư mục workshop đi kèm ZIP vẫn chỉ là mô phỏng thiết kế.

## Agent mới hoặc quay lại sau này

Đọc file cấu trúc hệ thống hiện hành → [QA.json](QA.json) → [REVIEW.md](REVIEW.md). Việc tiếp theo là chứng minh đúng nguồn semantic Definition/Version/owner cho representative pilot và nối lifecycle policy thật. Codex chịu trách nhiệm truy nguồn/đề xuất; PM nhận mapping/policy; Owner chỉ quyết D04 hoặc thay đổi trách nhiệm thực sự thuộc Owner. Không đưa việc chọn bảng/cột cho Owner.

Đừng chạy lại mọi thử nghiệm đã đạt hoặc đọc toàn bộ lịch sử. Không chuẩn hóa toàn catalog, thêm auth/queue framework hoặc tạo schema theo số vị trí trong matrix. 44 NEW_REQUIRED hiện chỉ là đề xuất chưa đủ bằng chứng loại reuse, **chưa được nhận và không cho phép production DDL**. 311 UNKNOWN là phần thiếu có đầu mối, không phải số cột cần tạo.

## Bằng chứng nào là kết quả cuối?

| Nội dung | File cần đọc | Phạm vi |
|---|---|---|
| Kiểm cấu trúc **112/112**, 28 profile/11 family | `evidence/contract-shape-final.json`, receipt và `contracts/` | C01 sửa lần cuối sau cleanup lab; chạy local Joi17.13.3 cùng phiên bản Directus. Chỉ kiểm cấu trúc. |
| P1/P2/P3/P4 và immutability **17/17** | `evidence/final-closure/runtime-proof-results.json`, `release-v1/v2.json`, `closure-check-v1/v2.json` | Fresh lab cuối: V1 16 node, V2 17; refs/digest/reachability đúng, không main/latest. Một MOT/AUTO ghi nội bộ. |
| P5/P6 **29/29** | `evidence/boundary-proof-results.json` | Binding/Definition, kết quả muộn và synthetic review/resume. |
| Reference/type/unit/FK/UNIQUE **30/30** | `evidence/extra-contract-results.json` | Cổng ghi và hard constraints trong lab. |
| Action/evidence stale **10/10** | `evidence/lifecycle-proof-results.json` | Không phải actual approval/expiry/SoD hay full lifecycle. |
| Nuxt bridge, platform/PG | `PLATFORM.md`, `evidence/nuxt-*`, `evidence/pg-minor-*` | Có build/SSR/session/Form/readback/Table; module còn audit risk. Directus12 chờ license. Production PG chỉ đọc. |
| Cleanup/an toàn | `evidence/cleanup.json`, `evidence/final-closure/cleanup.json`, `evidence/local-cleanup.json`, `evidence/safety-scan.json` | Hai lab dọn hết. Năm demo process state + hai safe GET không đổi, không phải full regression. |

Các `release-v*.json`, `runtime-proof-results.json` và `contract-shape-results.json` ngay dưới `evidence/` là **lượt đầu đã được thay thế ở phần pin/shape**. Giữ để truy lỗi và kiểm receipt xuất bằng chứng; không dùng chúng làm trạng thái cuối. `final-closure/contract-shape-results.json` giữ nguyên 110/110 tại thời điểm lab; kết quả hiện hành là 112/112 ở file nêu trên. Guard/worker giữ nguyên hash giữa hai lab và bước sửa C01 cuối. `release-v3.json` là fixture cố ý invalid để kiểm permanent failure, không phải một release được duyệt.

## Phạm vi từng khu

| Khu | Có gì / lúc nào cần đọc |
|---|---|
| `BAO-CAO-GUI-PM.md` | Báo cáo được chọn lọc để dán trực tiếp cho Chat; một kết luận thống nhất. |
| `summary.json`, `QA.json` | Số liệu, quyết định, QA A–H và 16 nhóm ca PM. A/D/E/F/G/H PASS theo phạm vi ghi rõ; B/C FAIL. Checklist hoàn tất không đồng nghĩa exit đạt. |
| `REVIEW.md`, `PLATFORM.md` | Giới hạn, blocker/đầu mối và quyết định platform của lượt này; không là sổ kiến trúc thứ hai. |
| `contracts/` | C01–C10, 11 family, native Joi descriptions và positive/negative cases. Chưa là toàn bộ semantic lock. |
| `data/` | Contract→data matrix, 18 quan hệ phân biệt hard FK với metadata/inferred/missing, và 9 nhóm authority. Candidate không tự thành nguồn chuẩn. |
| `proof/extension/`, `proof/runtime/` | Hai adapter I6 sửa từ Gate0/2 và runtime dependencies exact. Fault proxy chỉ gây lỗi TEST; pg-boss giữ queue/retry/ACK. |
| `proof/ui/` | FormCustom/Form/UForm/DirectusTable cùng transport/session được tái dùng. Mã này là lab UI bridge, không deploy production. |
| Các file trực tiếp trong `proof/` | Kế hoạch trước code; khởi tạo/dọn lab; khai báo/fixture/SQL; các phép thử; đọc metadata production; dựng matrix và thu nguồn. Danh mục chi tiết ở dưới. |
| `evidence/source/` | Raw primary sources theo receipt; tên hash tránh trùng URL. Receipt HTTP404 là lần tìm nguồn thất bại, không dùng làm căn cứ; nguồn thành công ở official-followup.json. Chỉ mở khi cần xác minh fact. |
| `evidence/final-closure/` | Kết quả runtime/closure cuối, snapshot và receipt xuất/cleanup của lab thứ hai. |
| Các file khác trong `evidence/` | Raw API/PG/log; Nuxt screenshot/transport; code inventory/diffs; chỉ đạo PM/luật đã đọc; SSOT diff/snapshot/QA/write receipt. |
| `evidence/package-verification.json` | Biên nhận kiểm ZIP và SHA256 của gói. Nằm ngoài ZIP để tránh checksum tự tham chiếu; manifest payload nằm trong ZIP. |

## Chạy lại khi có lý do kỹ thuật

Các harness được viết cho **lab synthetic riêng**, chạy qua SSH `vps2`; không chạy trên production. `provision-lab.py`/`bootstrap-lab.py` tạo tài nguyên có label sở hữu, private network, không public port; phải chọn tên mới và kiểm hạn mức/phạm vi trước khi chạy. File private chứa credentials được tạo riêng và đã xóa, không nằm trong gói. Không copy credentials của hệ thống đang hoạt động.

Trình tự tham khảo: PLAN → provision/bootstrap → seed/configure/install guard → runtime schema/prepare/control → run-runtime-proofs → boundary/extra/lifecycle → xuất và kiểm hash evidence → cleanup đúng label. Đọc từng script cần dùng để xác nhận đường dẫn `/tmp`, tên lab và đầu vào; đây là bộ nguồn có provenance, không cam kết một lệnh dựng production. Dependency đã khóa trong `proof/runtime/package-lock.json`, `proof/ui/package-lock.json`; môi trường internal cần chuẩn bị dependency trước khi tắt đường ra mạng.

Kiểm Joi có thể dùng `check-contracts.cjs` với native Directus hoặc biến TEST `G34_JOI_PATH`, `G34_CONTRACTS`, `G34_CASES`. Local test đã dùng Joi17.13.3; lock kiểm thử giữ tại `evidence/validator-test-package-lock.json`. Không thêm validator engine sản phẩm. Runtime/authority tests phải chạy riêng; shape PASS không thay thế chúng.

## Giữ bộ nhớ gọn và đúng

- Mỗi lần thêm/sửa/xóa nội dung, cập nhật README, summary/QA/báo cáo liên quan và hợp nhất trạng thái vào file cấu trúc hệ thống trong cùng lượt. Phân biệt đề xuất, PM quyết định, đã thử và đã triển khai.
- Lượt này đã xóa `.work` cùng build/cache/private config, các helper tạm/trùng và log rỗng; dừng preview/tunnel/lab. Khoảng 16 MB file tạm trong thư mục nhiệm vụ được dọn. Giữ nguồn tái hiện và bằng chứng còn cần kiểm, dù ca đã PASS.
- Không sửa kết quả cũ để giả một lần chạy mới. Khi có thử lại, ghi rõ kết quả nào thay thế phần nào; cập nhật chỉ mục. ZIP đã bàn giao là snapshot bất biến, không dùng nó làm bản làm việc.
- Không sinh thêm báo cáo/kiến trúc rải rác. `workshop/README.md` quản lý bảy file workshop; quyết định/vấn đề của dự án ở SSOT.

## Danh mục file đầy đủ

Danh mục bên dưới chỉ để tra cứu/kiểm kê; không phải thứ tự đọc. `manifest-sha256.json` trong ZIP là danh mục payload có hash. Biên nhận kiểm ZIP ngoài gói được kể trong danh mục này.

<details>
<summary>168 file — mở khi cần tra tên chính xác</summary>

```text
BAO-CAO-GUI-PM.md
PLATFORM.md
QA.json
README.md
REVIEW.md
contracts/cases.json
contracts/contracts.json
data/authority-map.json
data/contract-data-matrix.json
data/relation-map.json
evidence/before.json
evidence/bootstrap.log
evidence/boundary-initial-failure.log
evidence/boundary-proof-results.json
evidence/boundary-run.log
evidence/cleanup.json
evidence/code-inventory.json
evidence/contract-check.log
evidence/contract-shape-final-receipt.json
evidence/contract-shape-final.json
evidence/contract-shape-results.json
evidence/demo-smoke-before.json
evidence/development-notes.md
evidence/export-receipt.json
evidence/extension-change.diff
evidence/extra-contract-results.json
evidence/extra-contract-run.log
evidence/final-closure/before.json
evidence/final-closure/cleanup.json
evidence/final-closure/closure-check-v1.json
evidence/final-closure/closure-check-v2.json
evidence/final-closure/closure-check-v3.json
evidence/final-closure/contract-shape-results.json
evidence/final-closure/demo-smoke-before.json
evidence/final-closure/export-receipt.json
evidence/final-closure/guard-installed.json
evidence/final-closure/lab.json
evidence/final-closure/release-v1.json
evidence/final-closure/release-v2.json
evidence/final-closure/release-v3.json
evidence/final-closure/runtime-proof-results.json
evidence/final-closure/runtime-worker.log
evidence/guard-installed.json
evidence/lab-final-metadata.json
evidence/lab.json
evidence/lifecycle-proof-results.json
evidence/lifecycle-run.log
evidence/local-cleanup.json
evidence/nuxt-audit.json
evidence/nuxt-browser.jpg
evidence/nuxt-browser.txt
evidence/nuxt-build.log
evidence/nuxt-session-ssr.json
evidence/nuxt-transport.jsonl
evidence/official-followup.json
evidence/official-sources.json
evidence/package-verification.json
evidence/pg-minor-metadata.jsonl
evidence/pg-minor-restore-results.json
evidence/pm-instructions.md
evidence/production-discovery.jsonl
evidence/production-mapping.jsonl
evidence/provision.log
evidence/release-v1.json
evidence/release-v2.json
evidence/release-v3.json
evidence/reproof-provision.log
evidence/reproof-run.log
evidence/restore-run.log
evidence/rule-sources.json
evidence/runtime-change.diff
evidence/runtime-initial-failure.log
evidence/runtime-proof-results.json
evidence/runtime-proxy.log
evidence/runtime-resume.log
evidence/runtime-run.log
evidence/runtime-worker.log
evidence/safety-scan.json
evidence/source/03550279fb-workers.md
evidence/source/190e456600-latest
evidence/source/19c5decfdd-license
evidence/source/1ff5d9c9a7-5.migration.md
evidence/source/3d16d1693e-index.json
evidence/source/4083209e26-faq
evidence/source/5f621f191b-forms.md
evidence/source/7262bfb546-open-innovation-grant
evidence/source/9939490d7a-faq
evidence/source/9ad5486411-latest
evidence/source/9c9326da87-oig
evidence/source/bbf31c0fb6-index
evidence/source/c8c5356323-Table.vue
evidence/source/ca35a5e8ac-latest
evidence/source/e17506afa1-latest
evidence/source/e203efdff7-12.30.0
evidence/ssot-browser-qa.json
evidence/ssot-change.diff
evidence/ssot-contract-data.jpg
evidence/ssot-owner.jpg
evidence/ssot-static-qa.json
evidence/ssot-v1.6.17.html
evidence/ssot-write-receipt.json
evidence/start.json
evidence/validator-test-package-lock.json
proof/PLAN.md
proof/bootstrap-lab.py
proof/build-contracts.py
proof/build-data-map.py
proof/check-contracts.cjs
proof/cleanup-lab.py
proof/collect-sources.py
proof/configure-guard.py
proof/contracts-fixture.json
proof/declaration-action.py
proof/declaration-agent-v1.json
proof/declaration-agent-v2.json
proof/extension/app.js
proof/extension/index.js
proof/extension/package.json
proof/extra-contract-proofs.py
proof/ids.json
proof/inspect-mapping.py
proof/inspect-pg-minor.py
proof/inspect-production.py
proof/install-guard.py
proof/lab-client.py
proof/lifecycle-proof.py
proof/pg-smoke-backup.py
proof/provision-lab.py
proof/relations.sql
proof/run-boundary-proofs.py
proof/run-runtime-proofs.py
proof/runtime-control.py
proof/runtime-prepare.py
proof/runtime-schema.sql
proof/runtime/fault-proxy.mjs
proof/runtime/kernel.mjs
proof/runtime/package-lock.json
proof/runtime/package.json
proof/runtime/setup.mjs
proof/seed-draft.py
proof/seed-lab.py
proof/ui/app.vue
proof/ui/components/BlockContainer.vue
proof/ui/components/base/FormCustom.ts
proof/ui/components/base/UForm.vue
proof/ui/components/base/VAlert.vue
proof/ui/components/base/VSignature.vue
proof/ui/components/base/VUpload.vue
proof/ui/components/blocks/Form.vue
proof/ui/components/shared/DirectusTable.vue
proof/ui/components/typography/Headline.vue
proof/ui/components/typography/Title.vue
proof/ui/composables/useDirectus.ts
proof/ui/composables/useDirectusTable.ts
proof/ui/composables/useGuardedSubmission.ts
proof/ui/nuxt.config.ts
proof/ui/package-lock.json
proof/ui/package.json
proof/ui/plugins/directus.ts
proof/ui/plugins/form-request.ts
proof/ui/plugins/presentation.client.ts
proof/ui/plugins/presentation.server.ts
proof/ui/server/api/lab/[...path].ts
proof/ui/server/api/session.post.ts
proof/ui/server/api/test-config.get.ts
proof/ui/tailwind.config.ts
proof/ui/types/table-proposals.ts
summary.json
```
</details>
