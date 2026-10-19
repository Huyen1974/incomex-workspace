# BÁO CÁO · NÂNG HERMES v0.22.2 + APP MAC · NGÀY 18/10/2026

RUN `HJW-UPGRADE-BUTTON-20261017-01` · người làm: Claude Code CLI (executor) · lệnh trực tiếp của Owner · ghi chi tiết trong `COLLAB.md` mục P323–P330 · kiểm cuối 19/10/2026 01:35Z (08:35 +07).

## 1. Tóm tắt cho Owner

- **Hermes trên VPS và app Hermes trên Mac đã cùng bản chính thức mới nhất v0.22.2** (commit `d923a5eb`), Owner đã mở app gửi câu và dùng bình thường. Hermes nghỉ 13,5 phút lúc nâng (13:07:43–13:21:15Z).
- **Từ nay nâng Hermes:** Owner nói «nâng Hermes» với Claude Code (P325.7). Timer đêm chỉ báo khi hãng có bản ổn định mới, đúng một tin mỗi bản: «Có Hermes X. Muốn nâng: nói với Claude Code "nâng Hermes"». Không còn câu «bấm Update trên app Mac».
- **Mọi thứ đã đổi đều vào bảo vệ Điều 30/31** (khoá Config Guard, phép kiểm hồi quy, canh 5 phút/lần, đường lùi) — bảng ở mục 4; Guard POST đạt, biên nhận Telegram mid 224 và 225.
- **Bản chụp cũ (0.21.4) đã lên Google Drive, kiểm đọc lại được rồi mới xoá trên VPS**; lần nâng sau bản chụp cũ tự lên Drive rồi mới xoá, không chồng trên máy. Bản chụp để lùi của 18/10 giữ trên VPS.
- **Còn mở một việc:** đèn #11 (đĩa) đỏ từ 14:00Z 18/10 do phần tăng dung lượng hợp lệ của lượt nâng; hiện chỉ còn lý do SLOPE24, dự kiến xanh ở mẫu **19/10 14:00Z (21:00 +07)** — chưa báo xanh khi chưa xanh.
- **Sự cố ngoài việc này:** 15:04:40Z VPS bị bấm nút nguồn từ phía nhà cung cấp (log «Power key pressed short»), lên lại 15:27Z với kernel mới; mọi dịch vụ đã lên, ai bấm chưa rõ.

## 2. Diễn biến (giờ UTC; +07 = cộng 7 giờ)

| Giờ | Việc | Kết quả |
|---|---|---|
| 07:58 | Lượt 1 theo đề bài P316/P322 (nút nâng cấp Telegram, launchd Mac) | STARTED P323 |
| 09:43 | Owner: «Dừng lại… 1 việc đơn giản lại làm nó phức tạp» | KQ DỪNG P325; 0 cài lên Hermes; đồ thử đã dọn |
| 10:35 | Lượt 2 theo P325 (Host): một việc VPS + app Mac, bỏ nút/launchd, không `HERMES_MANAGED` | STARTED P326 |
| ~10:48 | Owner duyệt trước: «đạt thì nâng luôn» | ghi HUMAN_DIRECTIVE |
| 11:04–11:45 | Diễn tập trên bản sao (container `ubuntu:24.04` có sẵn) + app Mac v0.22.2 dựng chỗ tạm nối vào backend bản sao | **PASS 24/24**: chat + công cụ qua app, thử âm (update lén bị chặn), fixture HJW 42/42 + 27/27 |
| 12:00 | Guard PRE | PASS 22/22 đèn |
| 13:05–13:22 | Nâng VPS bằng `hermes-safe-update apply --reviewed --target-sha d923a5eb…` | **THÀNH CÔNG**; health sau nâng 21/21 |
| 13:23–13:26 | Ghi nhận Config Guard, Guard INV14 nhận cách chạy mới của v0.22, đèn #21 đặt mốc mới | CLEAN 490/490 · #21 drift=none · trả VPS-GHI |
| 13:27–13:31 | App Mac: cây nguồn kéo từ gương VPS lên `d923a5eb`, dựng bằng lệnh của hãng (app tắt ~1 phút) | chat thật + công cụ `hostname` đạt; Telegram qua gateway mid 223; MCP đạt |
| 13:40–13:48 | Owner: mọi thứ vào Điều 30/31 ngay | Guard POST PASS, biên nhận mid 224 (P327) |
| ~14:05 | Owner xác nhận app Mac dùng được + giao 2 việc nhỏ | — |
| 14:12–14:30 | (a) timer đêm chỉ báo bản ổn định; (b) chứng minh plugin hjw-control nạp trong serve + gateway | Guard POST PASS mid 225 · **KQ XONG P328** |
| ~14:40 | Owner: đưa bản chụp cũ lên Drive rồi mới xoá, ghi sổ, lần sau tự lên Drive, capability_check | — |
| 14:50–14:56 | `.previous` lên Drive + kiểm đọc lại | md5 + sha256 khớp |
| 15:00–15:04 | Lượt 3: cài updater mới, xoá `.previous`, ghi sổ dung lượng | apply-v0 APPLIED · +2,46 GB trống |
| 15:04:40–15:27 | VPS bị bấm nút nguồn (ngoài VPS), tắt rồi bật lại | mọi dịch vụ lên lại |
| 15:31–15:52 | Chạy lại kiểm hồi quy, khôi phục mốc chạy timer (C15), Guard POST | **KQ XONG P330**, trả VPS-GHI |
| 21:19 | Timer đêm chạy mã mới lần đầu | «đã mới nhất stable v0.22.2», không gửi tin |

## 3. Kết quả từng việc

**Nâng Hermes VPS (P326–P327).** 0.21.5 `749220ef` → v0.22.2 `d923a5eb` qua `hermes-safe-update` (chụp bản lùi 2,5 phút → bộ nâng của hãng 10 phút → kiểm sức khoẻ). Cấu hình chỉ đổi khoá `_config_version` (46→50); định tuyến model + 5 alias giữ nguyên. Tệp managed scope `/etc/hermes/config.yaml` ghim `sessions.auto_prune: false` (bản 0.22 mặc định tự xoá phiên cũ) và `command_allowlist: []` — đã đo Hermes áp dụng thật. Không bật `HERMES_MANAGED`.

**App Mac (P327).** Giữ cây nguồn (origin = gương VPS), kéo tiến đúng commit VPS, dựng bằng lệnh của hãng (Node 26.7.0 hãng ghim, `npm ci` + `npm run build` + `npm run builder -- --dir`); thanh trạng thái `client v0.22.2 · backend v0.22.2`; lệnh `hermes` trên Mac cũng báo v0.22.2. App cũ lưu ở `~/.hermes/backups/hjw-p325-20261018/`.

**Timer đêm (P328 a).** `hermes-safe-update auto` dùng đúng phép kiểm `hermes update --check` của hãng (kênh stable), không so với `main`; mỗi bản mới báo một lần.

**Plugin hjw-control (P328 b).** Đo trực tiếp trong hai tiến trình đang chạy: nạp thành công ở cả serve và gateway. Dòng lỗi «dictionary changed size» thuộc tiến trình ngắn trong lúc kiểm sức khoẻ (10 plugin của hãng bị cùng lỗi) — lỗi lõi hãng, không vá. Guard thêm phép canh: gateway khởi động mà không nạp hjw-control ⇒ đèn đỏ.

**Bản chụp cũ lên Drive (P329–P330).** `snapshot-truoc-update.previous` (0.21.4, 24/09, 2,27 GB) → Drive `incomex-encrypted-v1/rescue/hermes-snapshot/` (mã hoá bằng khoá công khai của hệ backup, 1,31 GB; md5 Drive khớp; tải lại toàn bộ khớp sha256) rồi mới xoá. Giải mã cần khoá bí mật của Owner như mọi bản backup Drive khác. Sổ dung lượng ghi thêm `~/.hermes/tools` (1,6 GB công cụ hãng tải cùng lần nâng).

**capability_check `tools.override`.** Plugin không xin quyền này và không cần; dòng «deny» là phép dò kiểm toán của chính Hermes mỗi lần nạp plugin ngoài hãng. Không cấp, không sửa.

**Phần đã bỏ (nút Telegram, launchd, làm lại INV14).** 0 dòng trong Config Guard / sổ mã, 0 tệp/unit cài, đồ thử trên Mac và VPS đã gỡ (giữ trong hồ sơ).

## 4. Bảo vệ Điều 30/31 (mục — bảo vệ — thử)

Khoá = Config Guard lưu bản chuẩn + băm; canh = Config Guard + Guard chạy 5 phút/lần, đổi ngoài quy trình ⇒ đèn đỏ + Telegram; lùi = bản trước trong `/root/incomex-config-changes/HJW-UPGRADE-BUTTON-20261017-01/rollback/` áp qua `incomex-config-apply-v0`.

| Mục | Khoá toàn vẹn | Kiểm hồi quy | Canh liên tục | Đường lùi | Thử |
|---|---|---|---|---|---|
| Mã Hermes VPS v0.22.2 | đèn #21 mốc `d923a5eb`; INV14 (mã = bản đã duyệt) | health 21/21, diễn tập 24/24, chat + công cụ thật | INV14 + #21 | `hermes-safe-update rollback --restore-state` (bản chụp 18/10) | ĐẠT |
| Launcher + `~/.hermes/config.yaml` | Config Guard ce778750 / a1ca29c5 | health, định tuyến model | Config Guard + #21 | bản trước c076bf0c / 85302542 | ĐẠT |
| Managed scope `/etc/hermes/config.yaml` | Config Guard 4de88b45 + sổ mã | Hermes áp `auto_prune=False`, allowlist rỗng | Config Guard + INV23 | gỡ tệp + lùi sổ | ĐẠT |
| 2 unit + 4 drop-in, plugin hjw-control | Config Guard (không đổi) | fixture 42/42 + 27/27; đo nạp trong tiến trình | Config Guard + #21 + INV16 | Config Guard + bản chụp | ĐẠT |
| `hermes-safe-update` (timer chỉ báo; bản chụp cũ lên Drive) | Config Guard c5a9c94c | nâng thật + giả lập timer + Drive thật thuận/nghịch | Config Guard + INV16 C15 | bản trước 37b852c1 / baf95cd8 | ĐẠT |
| Guard (INV14 v0.22, canh plugin nạp) | Config Guard 9d0a8c43 | selftest PASS, 0 mutant lọt | Config Guard + selftest | bản trước 93b9e9ba / 98d3b4e3 | ĐẠT |
| Sổ Config Guard, sổ mã, sổ dung lượng | Config Guard 59f9efdf / 098a0d99 / 17500a3e | CLEAN 490/490, INV23 0 tệp ngoài sổ, bộ đọc sổ + event-post PASS | Config Guard + INV23 + #11 | bản trước trong `rollback/` | ĐẠT |
| Cây nguồn + app Mac `d923a5eb` | INV14 (Mac = VPS cùng commit) | app thật chat + công cụ | INV14 5 phút/lần | app cũ + HEAD `749220ef` trong `~/.hermes/backups/hjw-p325-20261018/` | ĐẠT |
| Bản chụp 0.21.4 trên Drive | md5 + sha256 trong hồ sơ | tải lại toàn bộ khớp | Drive (không tỉa thư mục này) | tải về + giải mã bằng khoá Owner | ĐẠT |

Guard POST: P327 PASS (7 mục dấu chân, mid 224) · P328 PASS (2 mục, mid 225) · P329 đủ 4 ô + INV16 xanh, FAIL duy nhất vì lý do đèn #11 đổi chữ (luật Guard coi mọi đổi chữ là FAIL) — sẽ chạy lại kèm biên nhận khi #11 xanh.

## 5. Sự cố và bài học

1. **Owner dừng lượt 1 vì quá phức tạp** (nút Telegram, mã một lần, launchd). Bài học: đề xuất cách tối giản trước, hỏi trước khi dựng máy móc lớn cho việc hiếm.
2. **Nâng lâu hơn mong đợi:** bản nhảy lớn (~45.000 commit, hãng đổi cách cài sang bộ quản lý gói). Lần sau bản vá nhỏ không cần diễn tập; đổi số giữa mới diễn tập (P325.7).
3. **v0.22 chạy Hermes bằng python riêng của hãng** ⇒ INV14 cũ sẽ đỏ giả; đã sửa tối thiểu, giữ nguyên nghĩa. Chuỗi mẫu trong selftest từng ghi đường dẫn thật làm sổ mã báo «tệp mới» ⇒ đổi sang đường dẫn giả.
4. **Đèn #11 đỏ sau nâng:** +6 GB đúng vào lúc sổ dung lượng vừa đổi dòng (sáng 18/10) nên máy chưa có mốc để giải thích. Lần sau: khai dung lượng trước, không đổi dòng sổ sát ngày nâng, bản chụp cũ tự lên Drive (đã làm).
5. **VPS bị bấm nút nguồn giữa lượt 3** ⇒ systemd mất mốc lần chạy timer ⇒ đèn C15 đỏ; đã cho unit chạy một lượt. Ai bấm nút nguồn chưa rõ — Owner/nhà cung cấp nên kiểm.
6. **Xoá dữ liệu lớn đúng lúc máy đo đĩa (phút :00–:10)** sinh lý do «UNEXPLAINED» giả một mẫu; tránh khung đó.
7. **Guard chạy trùng lượt định kỳ** ⇒ INV20 báo lỗi giả; chạy PRE/POST ngay sau một lượt định kỳ UP.

## 6. Còn mở / việc tiếp

- **#11 xanh thật:** kiểm mẫu 19/10 14:00Z, chạy lại Guard POST P329 kèm biên nhận, ghi kết quả vào `COLLAB.md` (NEXT_TRIGGER=VERIFY_DEN11_XANH_19_10_14Z).
- **Drive `rescue/hermes-snapshot/` chưa có luật tỉa:** mỗi lần nâng thêm 1–3 GB mã hoá — Owner quyết khi cần.
- **Bản chụp lần nâng sau sẽ lớn hơn** (gồm cả môi trường + công cụ của hãng, ước ~6 GB) — vẫn dưới trần sổ 7 GB; cần khai `event-preflight` trước khi nâng.
- **Nâng lần sau:** Owner nói «nâng Hermes» → Claude Code làm P325.4–P325.6 (đổi số giữa thì diễn tập + thử cặp trước).
- Việc «VPS chạy vô nghĩa / swap» chuyển sang PROOT11 (việc riêng, không thuộc báo cáo này).

## 7. Kiểm cuối 19/10/2026 01:35Z

- Hermes VPS `d923a5eb` v0.22.2 `overall=ok`, gateway running, Telegram connected, config 50.
- App Mac dựng từ `d923a5eb` đang chạy; đường hầm Mac→VPS trả v0.22.2 ok; lệnh `hermes` trên Mac v0.22.2.
- Guard định kỳ 01:35Z UP, mọi bất biến đạt (INV14, INV16, INV23 PASS) · Config Guard CLEAN 490/490 · đèn #21 `drift=none`.
- Đèn #11 đỏ (mẫu 01:00Z): chỉ còn SLOPE24 −3,44 GiB; đĩa dùng 62 %, trống 37 GiB.
- Timer đêm 21:19Z: «đã mới nhất stable v0.22.2», không gửi tin; lần kế 19/10 21:21Z.
- VPS: `/var/backups/hermes` chỉ còn bản chụp 18/10; 0 container/thư mục/unit thử; trên Drive chỉ có bản 0.21.4.

## 8. Chi phí

Model trả tiền: vài lượt DeepSeek V4.1 Flash qua OpenRouter (kiểm sức khoẻ trước/sau nâng + một phiên thử trong app); diễn tập dùng model giả (0 đồng); JEV vài lượt (< 0,001 USD). Drive: +1,31 GB.

## 9. Hồ sơ / bằng chứng

- `COLLAB.md` mục P323–P330 (HUMAN_DIRECTIVE nguyên văn, STARTED/KQ, bảng bảo vệ).
- VPS `/root/incomex-config-changes/HJW-UPGRADE-BUTTON-20261017-01/` (`rollback/`, `evidence/`: Guard PRE/POST, coverage, Đ30 proofs, log thử, hồ sơ Drive) và các thư mục mutation `…-P325*`, `…-P326*`, `…-P328*`, `…-P329*`.
- Diễn tập: `/opt/incomex/work/hermes-joint-workspace/HJW-UPGRADE-20261017/results/rehearsals/v0.22.2-20261018T110416Z/`.
- Mac: `~/.hermes/backups/hjw-p325-20261018/` (app cũ, HEAD cũ, log dựng, đồ thử đã gỡ).
