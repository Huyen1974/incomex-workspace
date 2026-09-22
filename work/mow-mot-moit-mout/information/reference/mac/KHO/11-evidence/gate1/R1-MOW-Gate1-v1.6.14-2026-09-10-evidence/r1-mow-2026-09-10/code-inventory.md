# Công thực hiện R1 · 10/09/2026

**Product code mới = 0.** Không đổi source/component UI, backend, database schema/data, guard, worker, KB, platform version hoặc production deployment. Các HTML/JavaScript trong `source/` là bản đọc từ URL đang phục vụ; không phải code mới do R1 viết. Ảnh, text, JSON inventory, diff và snapshot là evidence.

| Phần local | Mục đích | Ghi vào đâu |
|---|---|---|
| `harness/capture-source.py` | GET 7 URL, giữ TLS verification, ghi status/SHA/source | Thư mục evidence local |
| `harness/capture-assets.py` | Resolve script trực tiếp đúng `<base>`, bỏ comment, GET và hash | Thư mục evidence local |
| `harness/update-ssot.py` | Soạn bản tạm, kiểm ID/anchor/cột bảng/style/script, đối chiếu hash trước ghi, backup, chặn ghi lần hai | Chỉ SSOT được PM giao và evidence local |
| `harness/package-evidence.py` | Kiểm source/snapshot/backup/link, lập inventory/hash/ZIP và kiểm ZIP đọc lại | Thư mục evidence local |

Số dòng vật lý và SHA từng harness có tại [inventory](harness-inventory.json). Đây là code hỗ trợ thu/kiểm tài liệu, không đưa vào runtime sản phẩm. Không cài framework hay dependency mới. Viewer local dùng HTTP server có sẵn của Python, chỉ bind loopback; kết thúc sau kiểm. Các đoạn kiểm tài liệu/thu screenshot trong phiên cũng chỉ chạy local, không được quảng bá thành module sản phẩm.

Các candidate từ Gate0 giữ nguyên phân loại feasibility: guard 163 dòng core + 2 dòng entry và 50 dòng SQL support; generic UI transport 87 dòng + UForm 9 thêm/1 bỏ; generic worker 92 dòng + 33 dòng DDL/5 TEST tables, pg-boss 12.30.0 + pg 8.23.0 / 21 locked packages và 1 worker riêng. Đây là chi phí của proof trước đã được PM nhận, không phải code phát sinh trong R1; xem [gói Gate0](../Proof-Gate0-UI-Runtime-2026-09-10-evidence.zip).

Trước canonical build/deploy vẫn phải xét CURRENT và TARGET-VERSION BUILT-IN, PLATFORM FREEZE, RULE-SYNC-01, target rehearsal theo dependency, maintenance owner và exit path. Gate0 DONE không cho phép đưa business branch/NTGV/approval/per-workflow/latest-version/business validation vào worker, hoặc business truth vào UI adapter.
