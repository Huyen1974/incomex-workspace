
/* ==== INCOMEX GUIDE · GS-MAC-UX-CLEAR-20261027-16 · bảng hướng dẫn tiếng Việt (chỉ đọc, chỉ dữ liệu đã nạp, 0 mạng) ==== */
(function () {
  "use strict";
  var G = null, D = null, panel = null, cur = null, show2 = false, lastSig = "";
  var VI_EDGE = {
    SELECTED_FOR_ORDER: "được chọn vào đơn", CANDIDATE_FOR_ORDER: "ứng viên của đơn (chưa chọn)",
    ORDER_FOR_COMPANY: "đơn của xí nghiệp", ORDER_MANAGED_BY_UNION: "đơn do nghiệp đoàn quản lý",
    part_of: "thuộc về", calls: "gọi", declares: "khai báo", evidences: "làm bằng chứng cho", imports: "nhập (import)",
    has_method: "có hàm", instantiates: "tạo đối tượng", implements: "hiện thực", EXECUTES: "chạy", ON_TABLE: "gắn trên bảng",
    REGISTERS: "đăng ký", PAIRED_WITH: "ghép cặp với", PERMISSION_ON: "quyền trên", DEPENDS_ON: "phụ thuộc", HAS_FK: "có khoá ngoại",
    REFERENCES: "tham chiếu", MAPS_TO_TABLE: "ứng với bảng", TRIGGERS: "kích hoạt", LISTENS_ON: "nghe ở cổng", PUBLISHED_BY: "do … mở cổng"
  };
  var VI_TRUST = [
    [/^EXACT_AT_SNAPSHOT/, "chính xác lúc chụp", "ok"], [/^EXACT_POSITIVE/, "khớp dương (luật)", "ok"],
    [/^DECLARED/, "khai báo", "ok"], [/^DERIVED_WITH_RULE/, "SUY LUẬN theo luật", "der"],
    [/^HIGH_CANDIDATE/, "ỨNG VIÊN (chưa xác nhận)", "cand"], [/^ADVISORY/, "gợi ý", "cand"],
    [/^UNKNOWN_FROM_GRAPH/, "chưa rõ", "unk"]
  ];
  function trustVi(t) { t = t || ""; for (var i = 0; i < VI_TRUST.length; i++) if (VI_TRUST[i][0].test(t)) return VI_TRUST[i]; return [null, t || "—", "unk"]; }
  function isCand(a) { return /CANDIDATE/i.test(a["Loại cạnh"] || a.label || "") || /^(HIGH_CANDIDATE|ADVISORY)/.test(a["Mức tin (trust)"] || ""); }
  function fmt(n) { return Number(n).toLocaleString("vi-VN"); }
  function el(tag, cls, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; return e; }
  function btn(txt, fn, title) { var b = el("button", "igx-btn", txt); b.type = "button"; if (title) b.title = title; b.onclick = fn; return b; }
  function nd(id) { return (D().nodeData[id]) || {}; }
  function lab(id) { var a = nd(id); return a.label || String(id); }

  var CSS = ".igx{position:fixed;right:12px;top:80px;z-index:2000;width:400px;max-height:calc(100vh - 100px);display:flex;flex-direction:column;" +
    "background:#fff;color:#1d2433;border:1px solid #b9c2d0;border-radius:8px;box-shadow:0 4px 16px rgba(0,0,0,.18);font:13px/1.4 -apple-system,system-ui,sans-serif}" +
    ".igx.min{max-height:none;width:auto}.igx.min .igx-body{display:none}" +
    ".igx-h{display:flex;align-items:center;gap:6px;padding:6px 10px;background:#22324d;color:#fff;border-radius:8px 8px 0 0;cursor:pointer;font-weight:600}" +
    ".igx.min .igx-h{border-radius:8px}.igx-h span{flex:1}.igx-body{overflow:auto;padding:8px 10px}" +
    ".igx-snap{background:#fff6dc;border:1px solid #e3c46a;border-radius:6px;padding:5px 7px;margin-bottom:6px;font-size:12px}" +
    ".igx-cnt{font-size:12px;color:#40506a;margin-bottom:6px}.igx-warn{background:#ffe9e6;border:1px solid #e08a7c;border-radius:6px;padding:6px 8px;margin-bottom:6px}" +
    ".igx-warn b{color:#a3271a}.igx-tabs{display:flex;gap:4px;margin:4px 0 6px}.igx-tab{flex:1;border:1px solid #b9c2d0;background:#eef1f6;border-radius:5px;padding:3px 0;cursor:pointer;font:inherit}" +
    ".igx-tab.on{background:#22324d;color:#fff;border-color:#22324d}.igx-btn{border:1px solid #8796ad;background:#f4f6fa;border-radius:5px;padding:2px 7px;margin:2px 4px 2px 0;cursor:pointer;font:inherit;font-size:12px}" +
    ".igx-btn:hover{background:#dfe6f1}.igx-card{border:1px solid #d3d9e3;border-radius:6px;padding:6px 8px;margin:6px 0}.igx-card .t{font-weight:700;font-size:14px}" +
    ".igx-sec{font-weight:700;margin:8px 0 2px;border-bottom:1px solid #d3d9e3}.igx-sec.cand{color:#8a5a00}.igx-sec.der{color:#5a3c8a}" +
    ".igx-row{display:flex;gap:4px;align-items:baseline;padding:1px 0;font-size:12px}.igx-row .d{width:16px;flex:none;color:#40506a;font-weight:700}" +
    ".igx-row a{color:#0b57d0;cursor:pointer;text-decoration:underline}.igx-b{display:inline-block;border-radius:4px;padding:0 4px;font-size:11px;margin-left:2px;white-space:nowrap}" +
    ".igx-b.ok{background:#e2f3e5;color:#1e6b2e}.igx-b.der{background:#ece4f8;color:#5a3c8a}.igx-b.cand{background:#fff0cf;color:#8a5a00}.igx-b.unk{background:#eceff3;color:#4a5568}" +
    ".igx-b.du{background:#d9f0ff;color:#0b4f7a}.igx-b.mp{background:#fde7d6;color:#8a3b00}.igx-b.ret{background:#a3271a;color:#fff}" +
    ".igx-src{color:#6b778a;font-size:11px}.igx-in{width:58%;font:inherit;padding:2px 4px;border:1px solid #8796ad;border-radius:4px}.igx dl{margin:0}.igx dt{font-weight:700;margin-top:5px}.igx dd{margin:0 0 0 8px}" +
    ".igx-muted{color:#6b778a;font-size:12px}";

  function n4b(v) { if (!v) return null; return el("span", "igx-b " + (/ĐỦ/.test(v) ? "du" : "mp"), v); }

  function snapText() {
    var d = (D().metadata && D().metadata.description) || "";
    var m1 = d.match(/(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) \(= Graph/), m2 = d.match(/giấy N4 (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)/);
    return "BẢN CHỤP TĨNH · dữ liệu Graph lúc " + (m1 ? m1[1] : "?") + " · giấy kiểm N4 lúc " + (m2 ? m2[1] : "?") +
      " (giờ UTC). PRIVATE, chỉ máy này. KHÔNG tự cập nhật, KHÔNG dùng để tự động hành động — cần câu trả lời có nhãn thì hỏi qua graph-v1.";
  }

  var tab = "rel";
  function render() {
    if (!panel) return;
    var body = panel.querySelector(".igx-body"); body.textContent = "";
    var full = D().fullGraph, fg = G.Ci.filteredGraph.get(), filters = (G.Ci.filters.get().filters || []).filter(function (f) { return !f.disabled; });
    body.appendChild(el("div", "igx-snap", snapText()));
    body.appendChild(el("div", "igx-cnt", "Đang vẽ " + fmt(fg.order) + "/" + fmt(full.order) + " nút · " + fmt(fg.size) + "/" + fmt(full.size) + " cạnh"));
    if (filters.length) {
      var hidden = 0; full.forEachEdge(function (e, a, s, t) { if (!fg.hasEdge(e) && (fg.hasNode(s) || fg.hasNode(t))) hidden++; });
      var w = el("div", "igx-warn"), ego = filters.find(function (f) { return f.type === "topological" && f.topologicalFilterId === "ego"; });
      if (ego) w.appendChild(el("div", null, "Đang xem quanh nút «" + lab(ego.parameters[0]) + "» (" + ego.parameters[1] + " bước)."));
      else w.appendChild(el("div", null, "Đang bật " + filters.length + " bộ lọc."));
      if (hidden) {
        var p = el("div"); p.appendChild(el("b", null, fmt(hidden) + " quan hệ đang BỊ ẨN"));
        p.appendChild(document.createTextNode(" vì nút ở đầu kia không nằm trong bộ lọc. Quan hệ VẪN CÓ trong dữ liệu, chỉ không được vẽ — không phải «không có quan hệ»."));
        if (fg.size === 0 && fg.order > 0) p.appendChild(el("div", null, "(Đang thấy " + fmt(fg.order) + " nút mà 0 cạnh: đúng là do lọc, không phải dữ liệu thiếu.)"));
        w.appendChild(p);
        w.appendChild(el("div", "igx-muted", "Muốn xem: bấm một nút trên hình (hoặc gõ mã ở mục Quan hệ) — danh sách quan hệ luôn đọc trên TOÀN BỘ dữ liệu."));
      }
      w.appendChild(btn("Bỏ mọi bộ lọc · xem toàn bộ", function () { G.ok.resetFilters(); }));
      if (cur && !ego) w.appendChild(btn("Xem «" + lab(cur) + "» + nút liên quan", function () { egoOn(cur, 1); }));
      body.appendChild(w);
    }
    var tabs = el("div", "igx-tabs");
    [["rel", "Quan hệ"], ["lbl", "Nghĩa nhãn"], ["menu", "Nút bấm"]].forEach(function (x) {
      var b = el("button", "igx-tab" + (tab === x[0] ? " on" : ""), x[1]); b.type = "button"; b.onclick = function () { tab = x[0]; render(); }; tabs.appendChild(b);
    });
    body.appendChild(tabs);
    if (tab === "rel") renderRel(body); else if (tab === "lbl") renderLbl(body); else renderMenu(body);
  }

  function egoOn(id, depth) {
    G.ok.setFilters({ filters: [{ type: "topological", topologicalFilterId: "ego", parameters: [id, depth, "both"] }] });
    setTimeout(function () { try { G.Ci.sigma.get().getCamera().animatedReset({ duration: 400 }); } catch (e) {} }, 300);
  }
  function pick(id) {
    cur = id;
    try { G.VK.select({ type: "nodes", items: new Set([id]), replace: true }); } catch (e) {}
    try { if (G.Ci.filteredGraph.get().hasNode(id)) G.focus(id); } catch (e) {}
    render();
  }

  function renderRel(body) {
    var f = el("div"), inp = el("input", "igx-in"); inp.placeholder = "Gõ mã nút"; inp.setAttribute("aria-label", "Tìm mã nút");
    var res = el("div");
    function go() {
      var q = inp.value.trim().toLowerCase(); res.textContent = ""; if (!q) return;
      var nodeData = D().nodeData, hits = [], exact = null;
      for (var id in nodeData) { var l = String(nodeData[id].label || id).toLowerCase(); if (l === q || id.toLowerCase() === q) { exact = id; break; } if (hits.length < 8 && l.indexOf(q) >= 0) hits.push(id); }
      if (exact) return pick(exact);
      if (!hits.length) { res.appendChild(el("div", "igx-muted", "Không thấy mã này trong bản chụp.")); return; }
      hits.forEach(function (id) { var r = el("div", "igx-row"), a = el("a", null, lab(id)); a.onclick = function () { pick(id); }; r.appendChild(a); r.appendChild(el("span", "igx-src", nd(id)["Loại nút"] || "")); res.appendChild(r); });
    }
    inp.onkeydown = function (e) { if (e.key === "Enter") go(); };
    f.appendChild(inp); f.appendChild(btn("Xem", go)); body.appendChild(f); body.appendChild(res);
    if (!cur || !D().fullGraph.hasNode(cur)) { body.appendChild(el("div", "igx-muted", "Bấm một nút trên hình, chọn trong ô «Search nodes, edges», hoặc gõ mã ở trên để xem các quan hệ của nó.")); return; }
    var g = D().fullGraph, a = nd(cur), c = el("div", "igx-card");
    c.appendChild(el("div", "t", lab(cur)));
    var meta = el("div"); meta.appendChild(el("span", "igx-src", (a["Loại nút"] || "") + " · " + (a["Lớp"] || "") + " "));
    var nb = n4b(a["Nhãn N4 tại T"]); if (nb) meta.appendChild(nb);
    var tv = trustVi(a["Mức tin (trust)"]); meta.appendChild(el("span", "igx-b " + tv[2], tv[1]));
    if (/RETIRED/.test(a["Trạng thái"] || "")) meta.appendChild(el("span", "igx-b ret", a["Trạng thái"]));
    c.appendChild(meta);
    var acts = el("div");
    acts.appendChild(btn("Chỉ xem nút này + 1 bước", function () { egoOn(cur, 1); }, "Dùng bộ lọc Ego network có sẵn của Gephi Lite"));
    acts.appendChild(btn("+ 2 bước", function () { egoOn(cur, 2); }));
    acts.appendChild(btn("Quay về toàn bộ", function () { G.ok.resetFilters(); }));
    c.appendChild(acts); body.appendChild(c);

    var direct = [], cand = [];
    g.forEachEdge(cur, function (e, ea, s, t) { var x = D().edgeData[e] || {}; (isCand(x) ? cand : direct).push({ e: e, out: s === cur, o: s === cur ? t : s, a: x }); });
    var fg = G.Ci.filteredGraph.get();
    function rows(list, title, cls, note) {
      body.appendChild(el("div", "igx-sec " + (cls || ""), title + " (" + list.length + ")"));
      if (note) body.appendChild(el("div", "igx-muted", note));
      list.sort(function (p, q) { return ((p.a["Loại cạnh"] || "") + lab(p.o)).localeCompare((q.a["Loại cạnh"] || "") + lab(q.o)); });
      list.slice(0, 150).forEach(function (r) {
        var row = el("div", "igx-row"), ty = r.a["Loại cạnh"] || r.a.label || "";
        row.appendChild(el("span", "d", r.out ? "→" : "←"));
        var w = el("span"); w.appendChild(el("span", null, (VI_EDGE[ty] || ty) + " "));
        var lk = el("a", null, lab(r.o)); lk.title = (nd(r.o)["Loại nút"] || "") + (fg.hasNode(r.o) ? "" : " · đang bị ẩn bởi bộ lọc"); lk.onclick = function () { pick(r.o); };
        w.appendChild(lk); w.appendChild(el("span", "igx-src", " " + (nd(r.o)["Loại nút"] || "")));
        var tv = trustVi(r.a["Mức tin (trust)"]); w.appendChild(el("span", "igx-b " + tv[2], tv[1]));
        var b = n4b(r.a["Nhãn N4 tại T"]); if (b) w.appendChild(b);
        if (!fg.hasEdge(r.e)) w.appendChild(el("span", "igx-b unk", "đang ẩn"));
        w.appendChild(el("div", "igx-src", ty + (r.a.source_file ? " · nguồn " + r.a.source_file : r.a.source ? " · nguồn " + r.a.source : "")));
        row.appendChild(w); body.appendChild(row);
      });
      if (list.length > 150) body.appendChild(el("div", "igx-muted", "… còn " + (list.length - 150) + " dòng (xem đủ ở Data › Edges)."));
    }
    rows(direct, "Quan hệ trực tiếp có trong dữ liệu", "", "→ = đi ra từ nút này · ← = đi vào nút này");
    if (cand.length) rows(cand, "Ứng viên — TÁCH RIÊNG, không phải quan hệ chính thức", "cand");
    var cb = el("label", "igx-muted"), ck = el("input"); ck.type = "checkbox"; ck.checked = show2; ck.onchange = function () { show2 = ck.checked; render(); };
    cb.appendChild(ck); cb.appendChild(document.createTextNode(" Hiện nút cách 2 bước (SUY LUẬN qua nút giữa, không phải cạnh trực tiếp)")); body.appendChild(cb);
    if (show2) {
      var seen = {}, two = []; seen[cur] = 1;
      direct.forEach(function (r) { seen[r.o] = 1; });
      direct.forEach(function (r) { g.forEachEdge(r.o, function (e, ea, s, t) { var x = D().edgeData[e] || {}; if (isCand(x)) return; var o = s === r.o ? t : s; if (seen[o]) return; seen[o] = 1; two.push({ via: r.o, o: o, ty: x["Loại cạnh"] || "" }); }); });
      body.appendChild(el("div", "igx-sec der", "2 bước — SUY LUẬN (" + two.length + ")"));
      body.appendChild(el("div", "igx-muted", "Ví dụ học viên → đơn → nghiệp đoàn: Graph KHÔNG có cạnh học viên–nghiệp đoàn; đây chỉ là đường đi qua nút giữa. Chỉ đi qua quan hệ trực tiếp, bỏ qua ứng viên."));
      two.slice(0, 100).forEach(function (r) {
        var row = el("div", "igx-row"); row.appendChild(el("span", "d", "⇢"));
        var w = el("span"), lk = el("a", null, lab(r.o)); lk.onclick = function () { pick(r.o); };
        w.appendChild(lk); w.appendChild(el("span", "igx-src", " " + (nd(r.o)["Loại nút"] || "") + " · qua " + lab(r.via) + " (" + (VI_EDGE[r.ty] || r.ty) + ")"));
        w.appendChild(el("span", "igx-b der", "suy luận")); row.appendChild(w); body.appendChild(row);
      });
      if (two.length > 100) body.appendChild(el("div", "igx-muted", "… còn " + (two.length - 100) + " nút."));
    }
  }

  function renderLbl(body) {
    var dl = el("dl");
    [["ĐỦ tại T", "Ô dữ liệu ghi ở «Ô giấy N4» đã được kiểm ĐỦ tại thời điểm T («Giấy cấp lúc (T)»). Chỉ đúng trong ô đó và tại lúc đó."],
     ["MỘT PHẦN", "Ô chưa được kiểm đủ. Vắng một đường nối KHÔNG có nghĩa là không có quan hệ. Ví dụ nút Code có thể «khớp dương (luật)» mà vẫn MỘT PHẦN."],
     ["chính xác lúc chụp (EXACT_AT_SNAPSHOT)", "Lấy đúng từ nguồn vào lúc chụp, chưa suy diễn."],
     ["khớp dương / SUY LUẬN theo luật (EXACT_POSITIVE / DERIVED_WITH_RULE)", "Mức tin do luật v0.6/R11 gán cho mã nguồn (Graph không tự lưu mức tin cho Code). SUY LUẬN = có thể đúng nhưng không phải số đo trực tiếp."],
     ["ỨNG VIÊN / gợi ý (CANDIDATE, HIGH_CANDIDATE, ADVISORY)", "Chưa được xác nhận. Ví dụ CANDIDATE_FOR_ORDER = học viên ứng tuyển đơn nhưng chưa được chọn. Luôn tách riêng, không cộng vào quan hệ chính thức."],
     ["chưa rõ (UNKNOWN_FROM_GRAPH)", "Graph có đường nối nhưng không biết độ tin."],
     ["2 bước — suy luận", "Đường đi qua một nút giữa (ví dụ học viên → đơn → xí nghiệp). Không có cạnh trực tiếp giữa hai đầu."],
     ["RETIRED", "Đã ngừng tồn tại trong hệ thống (ví dụ một cổng mạng cũ); giữ lại để tra lịch sử."],
     ["BẢN CHỤP / không realtime", "Toàn bộ màn hình này là ảnh chụp tĩnh (giờ ở khung vàng). Không dùng để tự động ra quyết định hay hành động."],
     ["đang ẩn", "Quan hệ có trong dữ liệu nhưng bộ lọc hiện tại không vẽ nó."]].forEach(function (x) { dl.appendChild(el("dt", null, x[0])); dl.appendChild(el("dd", null, x[1])); });
    body.appendChild(dl);
  }
  function renderMenu(body) {
    var dl = el("dl");
    [["Search nodes, edges", "Ô tìm (trên cùng): gõ mã rồi chọn một dòng."],
     ["Graph / Data", "Graph = hình đồ thị · Data = bảng Nodes/Edges (xem đủ mọi dòng)."],
     ["Filters", "Bộ lọc. «Topology › Ego network» = chỉ xem quanh một nút (nút «Chỉ xem nút này» ở mục Quan hệ dùng chính bộ lọc này)."],
     ["Appearance", "Màu, kích thước, nhãn trên hình."],
     ["Layout", "Sắp xếp lại vị trí nút (không đổi dữ liệu)."],
     ["Metrics", "Tính chỉ số (bậc, cộng đồng…) trên máy này."],
     ["+ / − / khung vuông (góc phải dưới)", "Phóng to · thu nhỏ · «See the whole graph» = xem lại toàn bộ."],
     ["Thu gọn bảng này", "Bấm thanh tiêu đề xanh của bảng."]].forEach(function (x) { dl.appendChild(el("dt", null, x[0])); dl.appendChild(el("dd", null, x[1])); });
    body.appendChild(dl);
  }

  // Đặt bảng vào khoảng trống giữa bảng trái và bảng chọn bên phải của Gephi Lite (không đè nút của Gephi Lite khi đủ chỗ)
  function place() {
    if (!panel) return;
    var L = 0, R = window.innerWidth;
    document.querySelectorAll(".panel-left").forEach(function (e) { var r = e.getBoundingClientRect(); if (r.width > 0) L = Math.max(L, r.right); });
    document.querySelectorAll(".panel-right").forEach(function (e) { var r = e.getBoundingClientRect(); if (r.width > 0) R = Math.min(R, r.left); });
    var w = Math.max(260, Math.min(400, R - L - 24)), B = window.innerHeight - 12;
    document.querySelectorAll("[class*=sigma-control]").forEach(function (e) { var r = e.getBoundingClientRect(); if (r.width > 0) B = Math.min(B, r.top - 8); });
    panel.style.maxHeight = Math.max(160, B - 80) + "px";
    panel.style.right = Math.max(4, window.innerWidth - R + 12) + "px";
    panel.style.width = panel.classList.contains("min") ? "auto" : w + "px";
  }
  function sig() { var fg = G.Ci.filteredGraph.get(); return fg.order + "/" + fg.size + "/" + JSON.stringify(G.Ci.filters.get().filters || []) + "/" + cur; }
  function onSel(v) {
    if (v && v.type === "nodes" && v.items && v.items.size) { var id = v.items.values().next().value; if (id !== cur) { cur = id; tab = "rel"; render(); } }
    else if (v && v.type === "edges" && v.items && v.items.size) { var e = v.items.values().next().value, g = D().fullGraph; if (g.hasEdge(e)) { cur = g.source(e); tab = "rel"; render(); } }
  }
  function boot() {
    G = window.__incomexGL; if (!G) return setTimeout(boot, 300);
    D = function () { return G.Ci.graphDataset.get(); };
    if (!D().fullGraph.order) return setTimeout(boot, 500);
    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    panel = el("div", "igx"); panel.id = "incomex-guide"; panel.setAttribute("role", "complementary"); panel.setAttribute("aria-label", "Hướng dẫn Graph Incomex");
    var h = el("div", "igx-h"); h.appendChild(el("span", null, "ⓘ Graph Incomex · Hướng dẫn & Quan hệ")); h.appendChild(el("b", "igx-tg", "–"));
    h.onclick = function () { panel.classList.toggle("min"); h.querySelector(".igx-tg").textContent = panel.classList.contains("min") ? "+" : "–"; place(); };
    panel.appendChild(h); panel.appendChild(el("div", "igx-body")); document.body.appendChild(panel);
    try { G.Ci.selection.bind(onSel); } catch (e) {}
    render(); lastSig = sig();
    place(); window.addEventListener("resize", place);
    setInterval(function () { place(); var s = sig(); if (s !== lastSig) { lastSig = s; render(); } }, 700);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
/* ==== /INCOMEX GUIDE ==== */
