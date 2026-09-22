# Proof A · Bằng chứng và tái chạy

Đo ngày 09/09/2026. Phạm vi là retrieval trên corpus nhỏ/mở rộng và sáu contract guards TEST ONLY. **Không phải T1 production, full admission, supervised authoring hoặc runtime proof.**

## Kết quả và mẫu số

| Corpus | Mode | Ứng viên eligible mỗi ca | Hit@5 known target | Query warm median ms | Warm p95 ms | EXPLAIN execution median ms | Shortlist mean / 16 |
|---|---|---:|---:|---:|---:|---:|---:|
| small | A0 | 14 | 8/12 | 3.000 | 71.818 | 1.203 | 0.625 |
| small | A1 | 14 | 12/12 | 5.421 | 54.579 | 5.630 | 2.625 |
| expanded | A0 | 1452 | 8/12 | 10.780 | 81.937 | 11.056 | 0.625 |
| expanded | A1 | 1452 | 12/12 | 79.927 | 109.365 | 78.883 | 3.500 |

12 positive queries có một known relevant target mỗi ca. Dùng hit@5, không trộn với Recall@5 nhiều relevant IDs. Giữ nguyên B11/B12/B13/B16 ngoài mẫu số theo artifact E06; B12 có retrieval reference nhưng bị loại khỏi positive score vì ambiguity như bản gốc. A0 tái hiện đúng 8/12 và bốn miss B05/B07/B08/B14. A1 tìm 12/12, cả 12 hạng 1, không đổi thứ hạng giữa hai corpus. Metadata xuất hiện trong top5 ở 9/16 ca mở rộng; toàn 1.452 ứng viên đủ điều kiện, không bị loại bằng type/domain suy từ đáp án.

Không chấm mọi metadata là irrelevant: chưa phân xử hết relevant IDs, nên precision/false-positive rate/exhaustive Recall@5 = NOT MEASURED. B11 là counterexample đã biết rõ về nghĩa: creation date khác modification date, dù có lexical match. B12 runtime trạng thái khác Definition; B13 đơn vị hours khác minutes. Không lấy “top1” làm reuse.

False-reuse, false-new, NEEDS_DECISION rate toàn T1 đều **NOT MEASURED**: 0 reuse decisions, 0 new decisions và 0 production admission resolutions đã chạy. Không có quyết định không là safety PASS. Sáu synthetic guard cases gồm khác nghĩa/subject, khác unit, thiếu contract, denied scope, MOIT thêm Field đã có, và compatible control; kết quả 6/6 trong [safety-raw.txt](./safety-raw.txt). `allowed` là fixture input, không authenticated request/Proof B. Các nhãn guard chỉ mô tả kết quả phép kiểm, không thêm lifecycle status vào sản phẩm.

## Dữ liệu và nguồn nhãn

- Tập nhỏ: đúng 14 provisional concepts từ `work/discovery4.jsonl` E05 ngày 08/09. Giữ source ID/key, kind, name, mô tả + boundary và aliases như snapshot. Contract_ref 0/14, promoted 0/14, không nâng thành canonical/published.
- Tập mở rộng: 14 trên + 1.438 legacy metadata trích read-only ngày 09/09; tổng nguồn 1.497, loại 59 không khớp information_schema. Đây là field metadata khớp cột/view nguồn, không đồng nhất tất cả với physical base-table columns hay canonical Field Definitions.
- Allowlist: ID/collection/field/datatype, note được lọc. 921 note không rỗng; loại nội dung một note theo bộ lọc, giữ 920; không bỏ cả candidate. Không lấy options/display-options/default/examples/translations/Flow payload, business rows, credentials, student files, vectors hoặc KB. Không thêm alias/metadata vào nguồn.
- Giữ collection provenance; subject mapping/business unit/structured contract không có thì NULL. Physical datatype có thật không đồng nghĩa semantic contract đầy đủ. Expanded status `active` chỉ là row eligible cho lab, không published lifecycle status.
- [queries-e06.json](./queries-e06.json) phục hồi từ script gốc và đối chiếu source result; [labels-e06.json](./labels-e06.json) giữ retrieval/admission riêng. Nhãn E06 là source-text regression labels đã có; sáu ca tổng hợp do Agent chuẩn bị trước chạy, chưa được PM/domain chuyên môn nghiệm thu. Không phải held-out evaluation.

SQL nguồn [extract-metadata-readonly.sql](./extract-metadata-readonly.sql) có READ ONLY, timeout 8 giây, allowlist, giới hạn 2.000. Không nâng quyền hoặc ghi production; đường SSH/read-only giữ quyền đã có. SQL introspection đầu tiên thiếu `docker exec -i` nên không nhận stdin/không thực hiện query; đã chạy lại đúng chế độ đọc.

## Cấu hình cố định

Image `postgres:16.13-bookworm` được resolve về Linux amd64 digest `sha256:57c55aefb81a937d21171b7c2266264b5552cb1a4f90459bbdfc417a36883a4d`, sau đó chỉ chạy digest. Actual PG16.13; unaccent1.1, pg_trgm1.6; UTF8, C.UTF-8. Chọn 16.13 để tương ứng PG đã đo E06, không coi đây là quyết định pin nền production mới.

A0 giữ key/name/alias equality và sort rank của E06. A1 giữ raw exact trước, thêm NFC/lower/unaccent/whitespace, full-text AND và trigram threshold 0.30; xếp bucket → weighted FTS rank → lexical score → stable numeric source ID. [search-config.json](./search-config.json) và SQL là hợp đồng thực thi của phép đo. Original text/ký hiệu/units còn nguyên; phép trgm/FTS chỉ tạo ứng viên, không so meaning. [PG string functions](https://www.postgresql.org/docs/16/functions-string.html), [pg_trgm](https://www.postgresql.org/docs/16/pgtrgm.html), [unaccent](https://www.postgresql.org/docs/16/unaccent.html).

Default DB tsearch vẫn `english`, nhưng **mọi lời gọi tsvector/tsquery đều chỉ định `pg_catalog.simple`**. Test actual `Đ/đ PHÚT h/kg °C` → `d/d phut h/kg °c`, NFD/NFC bằng nhau. Không thêm alias sau kết quả; không branch theo case ID/target ID. Labels không được chuyển vào PostgreSQL; chỉ offline scorer đọc đáp án. Không LLM trong lookup/candidate ranking.

Không search index. Hai logical corpora cùng một bảng 1.466 row và có corpus filter; vì vậy thời gian của tập nhỏ cũng gồm quét bảng chung. A1 precompute normalized text/tsvector trước đo; setup/precompute time = NOT MEASURED sau sửa instrumentation, không được xem là miễn phí. Mỗi ô một psql session, 16 ca × 6 lượt = 96 timings; tổng 384 timings + 64 EXPLAIN ANALYZE. Lượt đầu không gọi cold, năm lượt sau gọi warm; không flush OS cache. 0.5 CPU quota, VPS2 có workload nền, sáu guard SELECT chạy trong session phụ; p95 phản ánh cả contention/throttling. Không suy throughput production từ số này. Query psql time, server EXPLAIN time và harness wall/residual tách trong [summary.json](./summary.json); SSH time không trộn vào query latency.

## Môi trường và cleanup

Local Docker daemon không kết nối được; không cài/start/thay Docker local. VPS2 kiểm được 4 CPU, khoảng 6,22 GB RAM và 71,66 GB disk available trước tạo. Dùng 0.5 CPU, RAM/swap 512MiB, pids96; volume tmpfs riêng cap256MiB; DB/user/random credential, tên/nhãn và internal network riêng; không public port và tắt TCP listener. Chỉ Docker exec qua Unix socket. Không dùng volume/database/credentials e-learning; không bật external egress hoặc viết production.

Check tài nguyên sau từng ô, ngừng nếu RAM available dưới2GiB hoặc OOM; không chạm ngưỡng. [before.json](./before.json), [after.json](./after.json), [lab.json](./lab.json), [resources-expanded-a1.json](./resources-expanded-a1.json), [cleanup.json](./cleanup.json) lưu actual evidence. Năm demo containers giữ cùng ID/image/StartedAt/restart count/running; không thực hiện ứng dụng regression test hoặc tuyên bố full demo health.

Đã cleanup đúng labeled container/network/volume và exact temporary directory (bao gồm credential). Không Docker prune hoặc sửa shared config. Image digest đã pull còn trong cache vì không có work ownership label; không tự xóa image chung.

Lỗi khởi tạo logging max-file=1, launch trước transfer xong, `current_setting(lc_collate)` và precedence JSON operator được giữ trong freeze revision history. Chúng xảy ra **trước kết quả tương ứng**, không thay retrieval algorithm/corpus/query/labels. r2 chỉ sửa harness/env instrumentation và cú pháp guard; không tune theo score. [freeze-manifest.json](./freeze-manifest.json), [freeze-manifest-r1.json](./freeze-manifest-r1.json).

## Công người/LLM và phần chưa đo

Lookup: 0 LLM calls và 0 tokens. Chuẩn bị intent/harness/synthetic labels do Codex trong phiên; không có telemetry đủ để đo riêng tổng calls/tokens/active effort. Không yêu cầu Owner labeling mới (0 phiên mới được yêu cầu); không có adjudication chuyên môn cho metadata bổ sung. Human effort minutes **NOT MEASURED**, không ghi 0. Nhãn và sửa SQL do Agent tạo là công chuẩn bị, không evidence hệ sản phẩm tự làm. Không sửa source metadata, không thêm canonical object.

Intent→published MOW = NOT COMPLETED; tỉ trọng 98% AI khai báo, gateway authority, declaration được validator đọc, PG checkpoint/read-back/resume, UI cùng ID/version và runtime đều chưa đo. PG16 lab này không cần Directus12/license/MIG1/VPS2 về mặt kiến trúc; VPS2 chỉ là nơi có tài nguyên phù hợp lần này. Authoring tiếp theo vẫn phụ thuộc gateway/contract riêng. B/C chờ PM giao theo dependency thực tế, không cần chờ A vô hạn.

## Tái chạy có kiểm soát

Các file `.sql`/`.py` là **test harness**, không resolver service hoặc product patch. [E06-original-benchmark.py.txt](./E06-original-benchmark.py.txt) chỉ là source lịch sử, **không chạy vào production**.

1. Trên host lab được giao, kiểm lại tài nguyên/demo và Docker có sẵn; dùng [provision-lab.py](./provision-lab.py). Script từ chối work directory tồn tại, tạo chỉ đúng tài nguyên riêng; không dùng tag latest.
2. Copy corpus-small/expanded, queries-e06, search-config, hai search SQL, lab-schema và run-harness vào thư mục lab do script tạo; **không copy labels**. Đợi transfer hoàn thành. Chạy `python3 run-harness.py /var/tmp/proof-a-20260909-01a07f1f`. Chỉ dùng `--resume-setup` để phục hồi trước khi có raw results; nó kiểm read-back corpus bằng file nguồn. Khi có raw results thì từ chối ghi đè.
3. Chạy `safety-run.sql` chỉ trong DB `proof_a` của labeled container; expected ở safety-fixture dùng offline. Đây là fixture identity, không actual auth.
4. Copy raw/plans/environment/timing/resource artifacts về nơi bằng chứng; chạy `python3 analyze-results.py` tại đây. Scorer xác minh frozen hashes, 96 record mỗi ô và thứ hạng lặp lại ổn định. Revision mới nếu đổi input/config; không sửa expected để hợp thức score.
5. Sau khi artifacts đã lưu/kiểm, [cleanup-lab.py](./cleanup-lab.py) kiểm exact ownership labels rồi chỉ dọn work này. Manifest cuối có hash mọi artifact để phát hiện chỉnh sửa.

**Disposition đề nghị:** lexical đủ triển vọng cho bounded candidate retrieval trên hai tập đã kiểm; tiếp tục phần authoring/admission bằng contract thực. B11 chứng minh chưa thể auto-admit từ top1. Không cài vector hoặc mở full catalog cleanup dựa trên kết quả này. PM mới nghiệm thu phần đã làm.

## Cập nhật SSOT và tính toàn vẹn

SSOT trên máy Owner đã ghi một lần lên v1.6.10 sau actual evidence; backup nguyên bản v1.6.9, hash trước/sau và read-back trong [ssot-update.json](./ssot-update.json). Không tạo bản HTML kiến trúc thứ hai trong bộ bằng chứng. Kiểm cấu trúc và giữ nguyên 332 ID/scripts/styles: [html-qa.json](./html-qa.json). [manifest.json](./manifest.json) bao gồm hash toàn bộ artifact cuối, trừ chính manifest. Hash chứng minh tính toàn vẹn của file đã ghi nhận, không thay nghiệm thu độc lập.
