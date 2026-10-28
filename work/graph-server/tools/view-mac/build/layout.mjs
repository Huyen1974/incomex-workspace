// Tinh toa do ForceAtlas2 (Graphology) cho tung lop roi xep 3 lop thanh tam giac.
// node layout.mjs <vendor_dir> <work_dir>  -> doc layout-input.json, ghi positions.json
// RUN GS-VIEW0-MAC-LOCAL-20261011-17. Seed co dinh => chay lai ra cung toa do.
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";

const [vendor, work] = process.argv.slice(2);
const require = createRequire(path.join(vendor, "package.json"));
const Graph = require("graphology");
const forceAtlas2 = require("graphology-layout-forceatlas2");

function mulberry32(a) {
  return () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const input = JSON.parse(fs.readFileSync(path.join(work, "layout-input.json"), "utf8"));
const order = ["base88", "pgdot", "code"];
const out = {};
const local = {};
const report = {};
for (const g of order) {
  const { nodes, edges } = input[g];
  const graph = new Graph({ type: "undirected", multi: false });
  const rnd = mulberry32(20261012 + g.length);
  for (const k of nodes) graph.addNode(k, { x: rnd() * 1000 - 500, y: rnd() * 1000 - 500 });
  for (const [s, t] of edges) {
    if (s === t) continue;
    if (graph.hasEdge(s, t)) graph.updateEdgeAttribute(s, t, "weight", (w) => (w || 1) + 1);
    else graph.addEdge(s, t, { weight: 1 });
  }
  const settings = { ...forceAtlas2.inferSettings(graph), barnesHutOptimize: true, gravity: 1, scalingRatio: 10, linLogMode: false, edgeWeightInfluence: 1 };
  const t0 = Date.now();
  forceAtlas2.assign(graph, { iterations: 1500, settings, getEdgeWeight: "weight" });
  // chuan hoa ve hinh tron ban kinh R ~ sqrt(so nut), tam (0,0); xep 3 lop sau vong lap
  let cx = 0, cy = 0;
  graph.forEachNode((k, a) => { cx += a.x; cy += a.y; });
  cx /= graph.order; cy /= graph.order;
  const ds = [];
  graph.forEachNode((k, a) => ds.push(Math.hypot(a.x - cx, a.y - cy)));
  ds.sort((a, b) => a - b);
  const r98 = ds[Math.floor(ds.length * 0.98)] || 1;
  const R = 450 * Math.sqrt(graph.order / 1000);
  const scale = R / r98;
  local[g] = { R, pos: {} };
  graph.forEachNode((k, a) => { local[g].pos[k] = [(a.x - cx) * scale, (a.y - cy) * scale]; });
  report[g] = { nodes: graph.order, layoutEdges: graph.size, ms: Date.now() - t0, R: Math.round(R) };
}
// xep tam giac (hai lop tren, Code duoi) de khung hinh gan vuong: mo ra vua man hinh, khung trai khong che lop nao
const gap = 250, Rb = local.base88.R, Rp = local.pgdot.R, Rc = local.code.R;
const topY = -(Math.max(Rb, Rp) + gap / 2);
const centers = { base88: [-(Rb + gap / 2), topY], pgdot: [Rp + gap / 2, topY], code: [0, Rc + gap / 2] };
for (const g of order) {
  const [ox, oy] = centers[g];
  for (const [k, [x, y]] of Object.entries(local[g].pos)) out[k] = [ox + x, oy + y];
}
fs.writeFileSync(path.join(work, "positions.json"), JSON.stringify(out));
console.log(JSON.stringify(report));
