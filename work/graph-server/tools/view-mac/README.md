# view-mac — dựng và mở màn hình Graph riêng trên Mac (Gephi Lite, chỉ 127.0.0.1)

- **Vì sao có thư mục này:** đến 28/10/2026 repo chỉ ghi mã băm các công cụ này (P280, `tools/ramgate/README.md`), bản chạy chỉ nằm trên máy Owner `~/Incomex-Graph-View/` ⇒ mất Mac là mất đường dựng. DOC-SYNC 28/10 (Claude Chat B2, chỉ đọc) chép **byte-exact** lên đây; đã soát 0 secret/token, 0 mã đơn/record id thật, chỉ có đường dẫn VPS đã công khai trong COLLAB.
- **Bản Mac là bản chạy.** Sửa trên Mac thì cùng lượt phải chép lại đây và cập nhật mã băm bên dưới; không chạy từ repo sang VPS (DROOT56).

## Đang dùng (GEXF hiện hành `2cdd641220e6991ec689aaa5c5fbefa5df66e4a4e974d06ea2b22c9375013826` = D23, 8.968 nút/20.984 cạnh)

| tệp repo | trên Mac | sha256 | vai trò |
|---|---|---|---|
| `OPEN-GRAPH.command` | `OPEN-GRAPH.command` | `7fb3f892ed0ef6c7bdf13f3340e0d2c8001e9c6f3f8741b9cd1a411fa5e3fc2b` | bấm đúp để mở: tìm python3, chạy `python3 -I tools/serve.py --open` |
| `serve.py` | `tools/serve.py` | `6aa7560b1d13f24d2514b53ac2831878c8978c1673a7e95e866e0ef61dd272e7` | máy chủ tạm: chỉ 127.0.0.1, cổng 47390–47399, kiểm Host (chống DNS rebinding), chỉ phục vụ `app/gephi-lite/v1.0.2/` + 5 tệp `data/`, CSP `connect-src 'self'` trên mọi phản hồi, `no-store`; tắt = đóng Terminal/Ctrl+C, không dịch vụ nền |
| `build/build_view_c1e.py` | `tools/build/build_view_c1e.py` | `eac5c80eb530661246d6f0cc9380e01332d6dbe8b477d4b2cff0ca27957a5201` | dựng GEXF từ bản xuất D23 (RUN GS-RAM-GATE-C1E-20261027-15, E3): `prep` / `write` / `verify` |
| `build/layout_c1e.mjs` | `tools/build/layout_c1e.mjs` | `e32e2feea943cf890f177c229748faffaafaafb2ab46543a235a8b9a00db3614` | toạ độ ForceAtlas2 theo 4 khối lớp, seed cố định |
| `../ux16/` | `ux16/` | xem `../ux16/README.md` | bảng «Hướng dẫn & Quan hệ» vá vào bundle Gephi Lite |

**Dựng lại GEXF (trên Mac):** cần thư mục nguồn D23 đã qua ACL view (`meta.json` khớp RECMAN `6e7ec6e7…`, `SHA256SUMS`, `nodes.jsonl`, `rels.jsonl`, `cert-cells.json`, `cert-summary.json`, `graph-invariants.json`) và vendor `graphology@0.25.4` + `graphology-layout-forceatlas2@0.10.1`.
1. `python3 -I build/build_view_c1e.py prep <src> <work>` — kiểm sha nguồn, ghi `layout-input.json`.
2. `node build/layout_c1e.mjs <vendor> <work>` — ghi `positions.json` (chạy lại ra cùng toạ độ).
3. `python3 -I build/build_view_c1e.py write <src> <work> <out>` — ghi `graph-merged.gexf` + `manifest.json` (quyền 600).
4. `python3 -I build/build_view_c1e.py verify <src> <out>` — `gexf-verify.json` phải `PASS` (khớp `gs_keys_sha256`/`edges_sha256` với `graph-invariants.json`).
5. Chép `out/graph-merged.gexf` sang `data/` là bước riêng, có người duyệt (bản đang chạy: `c1e/out/` và `data/` cùng `2cdd6412…`).

## Lịch sử (giữ để tra, dựng lại bản cũ)

| tệp repo | sha256 | lượt |
|---|---|---|
| `build/build_view.py` | `cc80da6f724821cffee6e276831090f3594c455965be31ff7b883b8b6967bd8e` | VIEW0 · GS-VIEW0-MAC-LOCAL-20261011-17 (nguồn R9, 3 lớp, 4 tệp GEXF) |
| `build/layout.mjs` | `efc3bc5ed61938d3d55317f7e9d8239dc5cf204dcaf61f47ad9bd3e756a028d7` | VIEW0 + R11 (3 khối xếp tam giác) |
| `build/verify_gexf.py` | `f22c742841639e211b7bd2fbb4caea1cb4aa6b70ecd6a3e96f4777ade90d007b` | VIEW0 |
| `build/check_source.py` | `8ec585033a197c84a2bae8b2ad701a1ce1c8f709676b7cc84d35730d43d72efc` | VIEW0 (đếm/băm bản xuất R9) |
| `build/build_view_r11.py` | `d42620e7f3775f6efaf26e03857651846a9fc6d5a637d0d02bac2786490af0d9` | R11 · GS-R11-R10C-INTEGRATED-20261021-03 (pin sha qua biến môi trường) |
| `build/verify_gexf_r11.py` | `97231744d368d53cae149566595f4e1395789cfa9efd5dc137321bc3123bfc05` | R11 |

## Ở lại Mac, KHÔNG đưa lên repo

- Dữ liệu `data*/`, `c1e/out/`, `evidence*/` — dữ liệu nghiệp vụ thật, PRIVATE.
- `README.txt` hướng dẫn Owner (sha256 `024de3d94074c69fb2cd536bf6e17570bd219c5464207e160713f230cf560b53`) — có mã đơn thật làm ví dụ.
- `app/gephi-lite/v1.0.2/` — bản phát hành Gephi Lite; bundle đã vá dựng lại bằng `../ux16/build.py`.
- `ux16/tests/` — có mã đơn/record id thật.

## Nợ

- Chưa đăng ký vào sổ công cụ Master Tool/DOT (cần lượt có quyền ghi).
