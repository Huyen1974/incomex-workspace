// Tinh toa do ForceAtlas2 (Graphology) cho tung khoi lop roi xep cac khoi thanh luoi (khuon layout.mjs VIEW0/R11).
// node layout_c1e.mjs <vendor_dir> <work_dir>  -> doc layout-input.json {order:[...], groups:{g:{nodes,edges}}}, ghi positions.json
// RUN GS-RAM-GATE-C1E-20261027-15. Seed co dinh => chay lai ra cung toa do. Canh cheo lop khong dung cho bo cuc.
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
const local = {}, report = {}, out = {};
for (const g of input.order) {
  const { nodes, edges } = input.groups[g];
  const graph = new Graph({ type: "undirected", multi: false });
  const rnd = mulberry32(20261027 + g.length);
  for (const k of nodes) graph.addNode(k, { x: rnd() * 1000 - 500, y: rnd() * 1000 - 500 });
  for (const [s, t] of edges) {
    if (s === t) continue;
    if (graph.hasEdge(s, t)) graph.updateEdgeAttribute(s, t, "weight", (w) => (w || 1) + 1);
    else graph.addEdge(s, t, { weight: 1 });
  }
  const settings = { ...forceAtlas2.inferSettings(graph), barnesHutOptimize: true, gravity: 1, scalingRatio: 10, linLogMode: false, edgeWeightInfluence: 1 };
  const t0 = Date.now();
  forceAtlas2.assign(graph, { iterations: 1500, settings, getEdgeWeight: "weight" });
  let cx = 0, cy = 0;
  graph.forEachNode((k, a) => { cx += a.x; cy += a.y; });
  cx /= graph.order; cy /= graph.order;
  const ds = [];
  graph.forEachNode((k, a) => ds.push(Math.hypot(a.x - cx, a.y - cy)));
  ds.sort((a, b) => a - b);
  const r98 = ds[Math.floor(ds.length * 0.98)] || 1;
  const R = 450 * Math.sqrt(Math.max(graph.order, 50) / 1000);
  const scale = R / r98;
  local[g] = { R, pos: {} };
  graph.forEachNode((k, a) => { local[g].pos[k] = [(a.x - cx) * scale, (a.y - cy) * scale]; });
  report[g] = { nodes: graph.order, layoutEdges: graph.size, ms: Date.now() - t0, R: Math.round(R) };
}
// hang tren: cac khoi nho trai->phai; hang duoi: khoi cuoi (Code, lon nhat) o giua
const gap = 250, top = input.order.slice(0, -1), last = input.order[input.order.length - 1];
const topH = Math.max(...top.map((g) => local[g].R));
let x = -top.reduce((s, g) => s + 2 * local[g].R + gap, -gap) / 2;
const centers = {};
for (const g of top) { centers[g] = [x + local[g].R, -(topH + gap / 2)]; x += 2 * local[g].R + gap; }
centers[last] = [0, local[last].R + gap / 2];
for (const g of input.order) {
  const [ox, oy] = centers[g];
  for (const [k, [px, py]] of Object.entries(local[g].pos)) out[k] = [ox + px, oy + py];
}
fs.writeFileSync(path.join(work, "positions.json"), JSON.stringify(out));
console.log(JSON.stringify(report));
