#!/usr/bin/env python3
# GS-C1D · DIỄN TẬP CÔ LẬP lane c1d:* bằng CHÍNH graph-refresh ứng viên (cmd_rehearse: bản tạm từ điểm khôi phục → F → máy cấp giấy chấm
# ô lane trên bản tạm → I=PRE → F=NEW → đích tạm thứ hai: khô → F → NEW → (tiêm lỗi) → I → PRE). Không chạm production Graph/manifest;
# nhật ký/thư mục làm việc chuyển về thư mục bằng chứng. Giữ khoá graph-refresh trong lúc diễn tập (không chạy song song timer).
# Dùng: c1d_rehearse.py <stage_dir> <cert-cells> <lane> <out.json> [--inject-fail] [--expect-skip] [--mutate-drop-edge]
import importlib.machinery, importlib.util, json, os, sys, types
stage, cells, lane, out = sys.argv[1:5]
os.environ["GS_CERT_CELLS"] = cells
ev = os.path.dirname(os.path.dirname(os.path.abspath(out)))
sys.path.insert(0, stage)


def load(name, path):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    sys.modules[name] = m
    ldr.exec_module(m)
    return m
GC = load("graph_cert", stage + "/graph_cert.py")
GA = load("graph_autocover", stage + "/graph_autocover.py")
GA.RB = stage
if "--mutate-drop-edge" in sys.argv:                  # lỗi giả: bộ nạp hỏng làm rơi một cạnh ⇒ máy cấp giấy trên bản tạm phải chặn
    _d = GA.desired_infra

    def bad(*a, **k):
        n, e, r = _d(*a, **k)
        k0 = sorted(e)[0]
        e.pop(k0)
        r["fixture_dropped_edge"] = "|".join(k0)
        return n, e, r
    GA.desired_infra = bad
GRF = load("graph_refresh_c1d", stage + "/graph-refresh")
GRF.LOG = ev + "/w/graph-refresh-rehearse.jsonl"
GRF.STATE = ev + "/w/state-rehearse"
os.makedirs(GRF.STATE + "/runs", mode=0o700, exist_ok=True)
a = types.SimpleNamespace(lane=lane, size=0, inject_fail="--inject-fail" in sys.argv, expect_skip="--expect-skip" in sys.argv, out=out)
rc = GRF.cmd_rehearse(a)
d = json.load(open(out))
print("REHEARSE_RC", rc, d.get("result"), json.dumps({k: (d.get("report") or {}).get(k) for k in ("synthetic", "skip")}, ensure_ascii=False)[:400])
b = (d.get("report") or {}).get("build") or {}
print("GATE", json.dumps(b.get("gate"), ensure_ascii=False)[:600], "I=PRE", b.get("rehearse_I_eq_pre"), "F=NEW", b.get("rehearse_F_eq_new"),
      "APPLY", json.dumps((d.get("report") or {}).get("apply"), ensure_ascii=False)[:300], "CLEAN", b.get("temp_cleanup"), (d.get("report") or {}).get("target_cleanup"))
sys.exit(rc)
