#!/usr/bin/env python3
# GS-C1D2-SCOPED-AUTOCOVER-20261026-13 · chạy một bộ lỗi giả với graph_cert/graph_autocover ỨNG VIÊN đã nạp sẵn vào sys.modules
# (graph-refresh `import graph_cert/graph_autocover` lấy đúng bản ứng viên, không phải bản production). Dùng: run_with_cands.py <gc> <ga> <script> args…
import importlib.machinery, importlib.util, runpy, sys
sys.path.insert(0, "/opt/incomex/graph-server/prod-v1/bin/refresh")
for name, path in (("graph_cert", sys.argv[1]), ("graph_autocover", sys.argv[2])):
    ldr = importlib.machinery.SourceFileLoader(name, path)
    m = importlib.util.module_from_spec(importlib.util.spec_from_loader(name, ldr))
    ldr.exec_module(m)
    sys.modules[name] = m
script = sys.argv[3]
sys.argv = [script] + sys.argv[4:]
runpy.run_path(script, run_name="__main__")
