# PROMPT — HVU-DEEPLINK01 · DRAFT · NO RUN

## Trạng thái
DRAFT để tách deep-link khỏi MMIM. Không RUN tới khi Host đặt READY riêng sau khi child ID/bridge contract ổn định.

## 0. Mục tiêu
Owner yêu cầu URL Task html view thay đổi theo tab/khu vực/bảng con để link mở đúng chỗ đang trao đổi.

Input contract: `work/mow-mot-moit-mout/COLLAB.md` · MAP-R3 R3.8 + A1–A9.

## 1. Ranh giới SSOT
- Mã/runtime viewer: VPS là SSOT theo AGENTS/README §11.
- Không GitHub → VPS; không deploy repo sang runtime.
- `work/hpml-view-for-user/ui-assembly/**` chỉ reference/evidence.
- Runtime source cần read-gate trước RUN: `docker/nuxt-repo/scripts/hvu-b2/ui/app.vue` và build/view liên quan trên VPS.
- Không sửa MCP/connector.

## 2. Contract
URL ngoài:
`/knowledge/modules?task=<id>&view=<...>&section=<...>&step=<...>&detail=<...>`.

- query browser-visible do KB/top parent sở hữu;
- relay đủ hai tầng KB/top ↔ HVU app ↔ sandbox work HTML;
- child sandbox chỉ dùng hash nội bộ, không tự sửa query parent;
- không thêm `allow-same-origin`;
- message child xác thực bằng `event.source === iframe.contentWindow` + allowlist `view|section|step|detail`, value `^[a-z0-9._-]{1,40}$`;
- chiều xuống opaque child dùng `postMessage(..., '*')`;
- handshake `ready → route`, replay route mới nhất sau iframe recreate;
- Back/Forward phục hồi state;
- standalone/Mở rộng vẫn dùng hash.

## 3. Chia trách nhiệm
HVU-DEEPLINK01 sở hữu parent/top viewer relay + URL trên runtime VPS.
Child bridge trong `mow-mot-moit-mout.html` thuộc MMIM và được giao ở lượt riêng sau FIELD pilot. Không sửa MMIM từ prompt HVU.

## 4. Acceptance A1–A9
A1 link Step→MOT→step mở đúng vị trí.
A2 đổi tab → `view=`.
A3 đổi object → `section=`.
A4 mở step/detail → query đổi.
A5 Back/Forward phục hồi đúng.
A6 query lỗi fallback an toàn.
A7 giữ `task=<id>`.
A8 standalone hash mở đúng step.
A9 sandbox giữ nguyên, không thêm `allow-same-origin`.

## 5. Executor/Write Path
Chưa chốt trong DRAFT. Khi RUN, Host chọn surface có capability runtime VPS đã nghiệm thu, không theo hãng; ghi Executor_Surface + Write_Path + read-gate trước mutation.

Kết thúc DRAFT: NO RUN.
