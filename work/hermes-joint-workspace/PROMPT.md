# PROMPT — HJW · LÀM XANH PHẦN ĐÈN CỦA HJW (#11 · #21 · #22-phần HJW) + SỬA STOP-HOOK BÁO SAI · MỘT LƯỢT
RUN_ID: HJW-GREEN-FIX-20261017-01
STATUS: DRAFT_HOST_P314 · Host tạm Claude Chat (lệnh Owner 17/10/2026) · chờ GPT Chat Reviewer ACCEPT đúng SHA cuối chạm tệp này · READY Host ký sẵn có điều kiện ở P314 · CHƯA CHẠY
Executor: Claude Code CLI trên MacBook, **cửa sổ mới** (SSH root VPS như các lượt PROOT05/06/09). Owner tự dán câu chuẩn DROOT38(c).
Write_Path: VPS qua `incomex-config-apply-v0` (Config Guard) + docker cho agent-data; Mac chỉ dọn đồ P313 để lại; repo: báo cáo trong `work/hermes-joint-workspace/COLLAB.md`, cờ VPS-GHI ở `COLLAB.md` gốc.
Nguồn bắt buộc đọc: Owner 17/10 07:15 (dòng 📥 đầu Bảng HJW) và 17/10 11:32 (§3); HJW P309 (gốc lệch config Hermes VPS), P313 + P314 (cờ bỏ quên, đo trước khi soạn); `work/tools-quy-trinh/COLLAB.md` KQ TQT-P41 mục 4 (INV20); COLLAB gốc PROOT05/06/09 (đường apply-v0, VPS-GHI, 4 ô, Guard pre/post).

## 0. ĐÍCH VÀ LUẬT CỨNG
- **Đích:** đèn #11 xanh · #21 xanh · #22 chỉ còn phần không thuộc HJW (GJW: INV24, `nginx-route-gemini-mcp`; phần khác nếu có thì ghi chủ) · stop-hook không còn nhắc «RUN … chưa có KQ» khi KQ đã ghi ở COLLAB gốc.
- **Ngoại lệ Owner 17/10 07:15:** luật ⛔ «không sửa Hermes VPS khi #11 đỏ/Guard FAIL» không chặn lượt này. Vẫn giữ: VPS-GHI (CAS, không chạy song song việc khác), Điều 30/31 (mọi thứ đổi vào Config Guard/sổ mã ngay trong lượt), `.pre` + lệnh lùi viết sẵn, **không rebaseline để che lỗi**, không đụng phần GJW, DROOT56 (không kéo/đẩy mã qua GitHub).
- **Owner 17/10 11:32: «Có thể chưa làm xong nhưng không được để lại tình trạng lỗi».** Mỗi pha A/B/C là một khối: đo PRE → đổi → kiểm → hỏng thì **lùi ngay về PRE** → điểm dừng an toàn. Hết thời gian/ngữ cảnh giữa pha: lùi pha đang dở, ghi KQ DỪNG, trả VPS-GHI. Không bỏ máy chủ nửa chừng; pha đã xong và kiểm đạt thì giữ.
- **Xoá dữ liệu** chỉ khi đã Drive-first (gói mã hoá + đọc ngược khớp) hoặc chứng minh là bản dư có nguồn gốc khác. **Không bao giờ** xoá/tỉa `/var/lib/hjw-control/ledger.jsonl`, `/var/lib/hjw-control/state.json` (sổ Guard INV17, bản tin 08:00).
- Không tạo daemon/timer/service/công cụ mới; dùng van của `vps-retention.sh`, apply-v0, Guard, `dot-connector-sync` sẵn có. 0 gọi model trả tiền (JEV được).
- **Báo từng bước (DROOT54a)** dưới mục KQ của RUN trong HJW COLLAB: `HJW-GREEN-FIX-20261017-01 · bước k/N · đã xong gì · UTC · dự kiến xong UTC`. Dự kiến: S0 30′ · A 30′ · B 30′ · C 45′ · POST 20′.

## 1. S0 — CHỈ ĐỌC (Mac + VPS)
1. **Read-gate:** AGENTS → HJW COLLAB (Bảng, §3, P313–P31x) → COLLAB gốc (VPS-GHI, DROOT54–56). Chỉ chạy khi: commit cuối chạm `PROMPT.md` = SHA trong dòng ACCEPT của GPT = SHA trong dòng READY của Host (P314 hoặc mục sau); 0 dòng STOP_REQUESTED; HJW không có STARTED chưa KQ. VPS-GHI trống ⇒ chiếm (CAS) + ghi dòng STARTED của RUN này cùng commit; bận (vd GJW đang giữ) ⇒ KQ DỪNG · VPS_BẬN, không chạy song song.
2. **Mac — đồ P313 để lại** (RUN Courier spike 13/10, Host đã đóng `CỜ_BỎ_QUÊN` ở P314): (a) còn phiên Claude Code nào của P313 sống không (chỉ xem; không đụng phiên của việc khác); (b) Hermes Local `hermes cron list`: job thử courier tạo 13/10 (tên/ID có `HJW-N3` hoặc `SPIKE`) — lịch, số lần chạy, lần cuối, có đánh thức agent/gọi model không (`~/.hermes/cron/executions.db` mode=ro), usage khoá Mac; (c) script thử trong `~/.hermes/scripts`; (d) Chrome hồ sơ `~/.hermes/chrome-hjw-n3-canary` có đang chạy với cổng debug không.
   **Dọn:** gỡ/tạm dừng đúng job thử (đúng ID); đóng tiến trình Chrome debug nếu còn. **Giữ** hồ sơ Chrome (đã đăng nhập, dùng lại cho Courier) và script thử — ghi «giữ có lý do». Ghi số đo lịch tự bắn làm đầu vào Courier. Không đổi khoá, `.env`, model mặc định, Hermes Desktop.
3. **VPS — PRE:** `/opt/incomex/logs/bang-den.json` + `mcpw-protection-guard pre` (lưu tệp PRE) + drift-check + `storage-watch` check. Liệt kê mọi lý do làm #11, #21, #22 đỏ và gán chủ (HJW/GJW/TQT/khác). Ngoài HJW: chỉ ghi.
4. **Đo cho A:** `du` từng thư mục/tệp con của `/var/lib/hjw-control` + tốc độ tăng 24h; ai ghi (tiến trình/script); phần nào tái tạo được từ nguồn khác (vd `workspace.git` là gương repo — Guard đọc §0 HJW từ đây, `HJW_MIRROR` trong `mcpw-protection-guard`).
5. **Đo cho B:** diff baseline Config Guard `hermes-config-yaml` ↔ `/var/lib/hermes/.hermes/config.yaml` (tên khoá + giá trị không bí mật; bí mật in `[che]`). Mỗi khoá lệch: giờ đổi, đường ghi (`gui.log`, `config.set` khi Hermes Desktop nối Remote — P309; plugin `hjw-control`; tay), có ảnh hưởng hành vi/an toàn không.
6. **Đo cho C:** lệnh check của `dot-connector-sync` cho nhóm agent-data (cái Guard INV20 gọi); tệp `/app/agent_data/*.py` khác nhau giữa image đang chạy (`2d36c21a…`, tag `agent-data-hvu:tqt-p38-20261012`) và HEAD `/opt/incomex/docker/agent-data-repo`; mỗi khác biệt thuộc commit nào, việc nào, KQ nghiệm thu nào (TQT P32–P38 đã Owner nhận G1; VPSC `9457406`, `8fe2ea8` chưa phát hành — đo host worker có đang chạy đúng bản HEAD không); test agent-data hiện có chạy trên HEAD (chưa build); đường deploy đúng như TQT P38 đã dùng (compose, tag); lệnh lùi về image cũ.
7. **Chốt S0:** một bảng ngắn `lý do đỏ · chủ · pha xử lý` + quyết định chạy A/B/C. Pha nào gặp điều kiện DỪNG của nó thì bỏ pha đó, làm pha khác.

## 2. A — VAN CHO `/var/lib/hjw-control` (#11)
- Chọn van theo số đo S0, dùng cơ chế có sẵn trong `vps-retention.sh`: luật (o) `git repack -d` cho kho git; luật xoá theo tuổi kiểu (n) Drive-first cho tệp xoay vòng. Không viết công cụ mới.
- Gương `workspace.git`: chỉ repack khi refs khớp nguồn, không tiến trình đang ghi (dùng `flock` như cron); sau đó Guard đọc §0 HJW vẫn được.
- Tệp xoay vòng (log/snapshot): giữ ≥7 ngày; quá hạn thì Drive-first rồi mới xoá.
- Sửa `/opt/incomex/scripts/vps-retention.sh` (nếu cần) và dòng `/var/lib/hjw-control` trong `/opt/incomex/scripts/storage-registry.tsv` qua apply-v0: `STATIC`/nợ → `ROTATING` `valve:…;cap=<7 ngày × tốc độ đo × 1,3>` (cùng cách dòng helper/mcp-roots).
- Chạy van một lượt thật → `storage-watch` check: hết `DEBT_OVERDUE /var/lib/hjw-control`; #11 xanh ở nhịp Kuma kế.
- **DỪNG pha A** (không xoá gì) nếu nguồn tăng không rõ chủ hoặc không tái tạo được và chưa Drive-first đọc ngược được ⇒ ghi một câu xin Owner gia hạn kèm số đo.

## 3. B — `hermes-config-yaml` (#21 + INV5_6 phần HJW)
- Khoá chỉ là tuỳ chọn giao diện do Hermes Desktop ghi khi nối Remote (`display.in_app_tips`, `display.in_app_tours` — P309): đưa vào baseline qua apply-v0, lý do «tuỳ chọn hiển thị, Desktop ghi lại cùng giá trị mỗi lần nối ⇒ lần sau trùng byte». Kiểm `_save_cfg` chỉ thêm dòng, không định dạng lại phần còn lại.
- Khoá ảnh hưởng hành vi/an toàn (vd `approvals.timeout`, model, provider, toolsets): có lời Owner hoặc RUN đã duyệt ⇒ vào baseline kèm dẫn chứng; không có ⇒ trả về giá trị baseline qua apply-v0. Cần khởi động lại `hermes-gateway` thì chỉ làm khi `ws-dispatch` rỗi (không vé HJW đang chạy), kiểm `/api/health` + nhịp #21 ngay sau.
- Không sửa mã Hermes, không nâng phiên bản, không bấm gì trên Hermes Desktop.
- Kiểm: drift-check `hermes-config-yaml MATCH`; #21 hết `drift=CONFIG`. #21 còn lý do khác của HJW (vd INV16 B19–B22 «nhịp #21 thiếu phần kiểm») ⇒ sửa chỉ khi là một chỗ nhỏ có đường apply-v0 sẵn, không thì ghi cho Host.

## 4. C — INV20 + STOP-HOOK (DỰNG AGENT-DATA MỘT LẦN)
- **Gốc lỗi stop-hook (Host đo, P314):** `agent_data/lifecycle.py` hàm `kq_added` chỉ đọc `git show … -- work`, nên KQ ghi ở `COLLAB.md` gốc (RUN chung VPS theo DROOT54a) không được ghi nhận ⇒ phiên dừng thì hook nhắc «chưa có KQ». Sửa: đọc thêm `COLLAB.md` gốc. Thêm test ở `tests/continuation/` trên 3 commit thật `0eaa062`, `1453fed`, `d0b2163` (phải tìm thấy đúng RUN_ID). Không đổi gì khác trong lifecycle. Đối chiếu thêm dòng `send failed: http` 14:36:04Z 16/10 của hook Mac (chỉ đọc, ghi nguyên nhân).
- **Điều kiện dựng — đủ cả 4, thiếu một ⇒ C DỪNG, giữ A/B, ghi đúng một câu hỏi cho Owner/TQT:**
  1. mọi khác biệt image ↔ HEAD có commit, việc chủ và KQ nghiệm thu; riêng `9457406`/`8fe2ea8` (VPSC) chỉ đưa vào khi chứng minh host worker đang chạy ổn định đúng bản đó;
  2. test agent-data hiện có + test mới PASS;
  3. không RUN nào khác STARTED đang dùng agent-data (xem COLLAB gốc + các Bảng); báo Owner một câu trong terminal trước khi khởi động lại (đầu nối AI gián đoạn ngắn) — chỉ báo, không chờ trả lời;
  4. image cũ giữ tag, lệnh lùi viết sẵn và đã chạy thử khô (in lệnh, không chạy).
- **Làm:** commit trong `docker/agent-data-repo` (chỉ local VPS) → dựng image đúng đường TQT P38, tag `agent-data-hvu:hjw-green-20261017` → recreate container **một lần** → trong 120 s: `/api/health` 200, đầu nối workspace đọc được, lifecycle nhận hook. Hỏng ⇒ recreate về image cũ ngay, C = `ROLLED_BACK`.
- **Ghim:** apply-v0 `connector-sync-registry` release agent-data = commit vừa dựng; check `dot-connector-sync` agent-data PASS ⇒ INV20 xanh. Baseline Config Guard các đích mã agent-data đổi (`agent-data-lifecycle-py` …) cập nhật theo byte mới qua apply-v0.
- **Kiểm stop-hook:** `kq_added` trên 3 commit thật trả đúng RUN_ID trong container mới; nếu được, phiên Claude Code của chính lượt này không bị nhắc sai khi dừng sau KQ.

## 5. POST · ĐIỀU 30/31 · DỌN · KQ
- `mcpw-protection-guard post --pre <PRE>` + 22 đèn: #11, #21 xanh; #22 chỉ còn đỏ không thuộc HJW (liệt kê chủ). same_or_better: không đèn/INV mới đỏ. Biên nhận theo đường Guard sẵn có; #22 còn đỏ của việc khác ⇒ ghi `GLOBAL_GUARD_PARTIAL`.
- **4 ô từng pha:** Đ30 (chạy đúng) · Đ31 (tệp đổi đã vào Config Guard/sổ mã; phép thử hỏng trên bản sao bị bắt) · canh (Guard 5′, Kuma) · lùi (`.pre`, image cũ, lệnh).
- **Dọn (DROOT54c) — lượt sẽ tạo:** `/root/incomex-config-changes/HJW-GREEN-FIX-20261017-01/` (bằng chứng, giữ) · thư mục tạm build (xoá) · image mới (giữ, là bản chạy) · image cũ (giữ làm đường lùi) · 0 tiến trình nền còn lại. Ghi `Dọn: <đã gỡ>/<đã tạo> · còn lại: … (lý do)`.
- **KQ:** dòng KQ của RUN này (XONG hoặc DỪNG) trong HJW COLLAB, trả VPS-GHI ở COLLAB gốc cùng commit, cập nhật Bảng (■, ➡) và dòng HJW ở COLLAB gốc. Nêu: tập đỏ PRE→POST · kết quả A/B/C (`PASS`/`DỪNG`/`ROLLED_BACK`) · đồ P313 đã dọn/giữ · số đo lịch Hermes Mac · chi phí model 0 · JEV.
- **NEXT:** XONG ⇒ Host quay lại Courier (làm lại phần còn thiếu của P313). DỪNG ⇒ đúng một blocker + một câu hỏi kèm đề xuất.
