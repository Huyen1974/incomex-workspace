MÀN HÌNH GRAPH INCOMEX — chỉ trên máy Mac này
(Hướng dẫn tại chỗ. Tài liệu gốc của việc nằm ở repo: work/graph-server/COLLAB.md và GS-RM1.)

BẢN ĐANG XEM
  data/graph-merged.gexf = bản chụp Graph lúc 26/10/2026 10:52:58Z (giờ UTC), xuất ngày 27/10/2026:
  8.968 nút, 20.984 quan hệ, bốn khối: Code (xanh lá, khối lớn) · Base88 (cam/đỏ/nâu: công ty, đơn hàng,
  học viên, nghiệp đoàn) · PG/DOT + catalog L1 (xanh dương) · Hạ tầng (tím, khối nhỏ).
  Nhãn «ĐỦ tại T / MỘT PHẦN» theo giấy kiểm N4 lúc 27/10/2026 05:03:22Z.
  PRIVATE: chỉ máy này (127.0.0.1). Không đưa lên mạng, Git hay Google Drive; không chép vào Desktop/Documents
  (iCloud) hay Google Drive.
  Đây là ẢNH CHỤP TĨNH: không tự cập nhật, không realtime, không dùng để tự động hành động. Câu trả lời có nhãn
  máy đọc được thì hỏi qua cổng đọc chính thức graph-v1 (MCP get-schema / read-cypher).

MỞ / ĐÓNG
  Bấm đúp OPEN-GRAPH.command. Một cửa sổ Terminal nhỏ hiện ra và trình duyệt tự mở trang đồ thị (~5–7 giây).
  Đóng: đóng cửa sổ Terminal (chọn "Terminate"/"Kết thúc") hoặc bấm Ctrl+C trong cửa sổ đó.

BẢNG «ⓘ Graph Incomex · Hướng dẫn & Quan hệ» (góc phải trên, thêm 28/10/2026)
  Khung vàng: giờ bản chụp và giờ giấy kiểm. Dòng dưới: đang vẽ bao nhiêu nút/cạnh trên tổng số.
  Mục «Quan hệ»: bấm một nút trên hình, chọn trong ô "Search nodes, edges", hoặc gõ mã nút vào ô của bảng.
    - «Quan hệ trực tiếp»: mọi đường nối có trong dữ liệu, → đi ra / ← đi vào, đầu kia, mức tin, nhãn N4, tệp nguồn.
    - «Ứng viên — TÁCH RIÊNG»: ví dụ học viên ứng tuyển đơn nhưng chưa được chọn; không phải quan hệ chính thức.
    - Ô «Hiện nút cách 2 bước»: đường đi qua một nút giữa (ví dụ học viên → đơn → nghiệp đoàn) = SUY LUẬN,
      Graph không có cạnh trực tiếp giữa hai đầu.
    - Nút «Chỉ xem nút này + 1 bước» / «+ 2 bước» (dùng bộ lọc Ego network sẵn có) và «Quay về toàn bộ».
    - Bấm tên ở đầu kia để chuyển sang xem nút đó.
  Khi đang lọc: bảng báo bao nhiêu quan hệ đang BỊ ẨN vì đầu kia bị lọc. Quan hệ vẫn có trong dữ liệu, chỉ là
    không được vẽ. Ví dụ lọc Loại nút = B88Order cho 269 nút mà 0 cạnh: đó là do lọc, không phải dữ liệu thiếu.
    Có nút «Bỏ mọi bộ lọc» và «Xem <nút đang chọn> + nút liên quan».
  Mục «Nghĩa nhãn»: ĐỦ tại T, MỘT PHẦN, chính xác lúc chụp, SUY LUẬN theo luật, ỨNG VIÊN, RETIRED, BẢN CHỤP.
  Mục «Nút bấm»: nghĩa tiếng Việt của các nút thường dùng của Gephi Lite (Search, Data, Filters, Layout…).
  Bấm thanh tiêu đề xanh để thu gọn/mở bảng.

XEM / PHÓNG TO
  Nút càng to = càng nhiều quan hệ. Lăn chuột (hoặc nút + / − góc phải dưới) để phóng to, thu nhỏ.
  Nút khung vuông góc phải dưới ("See the whole graph") = xem lại toàn bộ.
  Bấm một nút/cạnh: ô bên phải của Gephi Lite hiện mọi thuộc tính (Lớp, Loại nút/cạnh, Mức tin, Nguồn mức tin,
  «Ô giấy N4», «Nhãn N4 tại T», «Giấy cấp lúc (T)», «Trạng thái» đang có/RETIRED, «Quyền xem» PRIVATE).
  Với Code, «Nguồn mức tin» = "luật v0.6/R11": Graph không lưu mức tin cho mã, mức tin suy theo luật đã đo.
  Một nút có thể «khớp dương (luật)» mà vẫn MỘT PHẦN.

GIỚI HẠN
  Mọi thứ ngoài ô «ĐỦ tại T» coi là MỘT PHẦN · NOT_ACTION_SAFE: vắng đường nối ≠ không có quan hệ; nhiều nguồn
  (view, khoá ngoại, Directus, Docker, lịch chạy, Lark khác base 88, KB/Qdrant…) chưa nằm hết trong Graph.
  Giấy kiểm chứng gốc nằm trên VPS: prod-v1/state/refresh/cert/current.json.

BẢN CŨ (chỉ để tra lịch sử)
  data-r11-20261021  = bản chụp 21/10/2026 (8.650 nút, 20.662 quan hệ; 4 tệp, chưa có nhãn N4).
  data-view0-20261012 = bản 11/10/2026 (3.596 nút, 6.823 quan hệ).
  Con số 8.650/20.662 là của bản 21/10 cũ; bản đang xem là 8.968/20.984.

LÙI BẢNG HƯỚNG DẪN (nếu cần)
  ux16/backup/ giữ bản gốc byte-exact: chép index-CWSVxO7S.js.truoc về app/gephi-lite/v1.0.2/assets/index-CWSVxO7S.js
  và README.txt.truoc về README.txt (SHA256 trong ux16/backup/SHA256SUMS). Dữ liệu GEXF không đổi.
