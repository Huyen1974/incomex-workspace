#!/usr/bin/env python3
"""Máy kiểm CT-000.4 (MMOW 07) — công cụ dùng chung để mọi AI kiểm chéo.

Đọc 6 bảng trong Chi tiết CT-000.4 (ban-duyet.html) và CHẠY chúng như một chương trình:
  S  kiểm tĩnh: miền giá trị = công thức, mỗi trạng thái × giá trị đúng 1 dòng, tên thao tác/biến có khai
  B  bất biến (Bảng Bất biến): kiểm ở MỌI trạng thái tới được, duyệt hết (mô hình bên nhận, giờ, lượt cũ, người, Owner)
  L  sống: L1 không kẹt · L2 không vòng máy · L3 không mồ côi · L4 Owner luôn tới được Kết thúc
  C  ca thử: nhập dữ kiện, máy tự tính giá trị (không đưa sẵn nhãn)
  D  đột biến (--dot-bien): tự làm hỏng bảng từng chỗ; bản hỏng nào không bị bắt = máy kiểm còn hở
Mã thoát: 0 đạt · 1 có lỗi xác định (có vết chạy), ca trượt hoặc đột biến sống
          · 2 sai khuôn, chưa duyệt xong (INCONCLUSIVE), máy kiểm lỗi (CHECKER_ERROR) hoặc chỉ xét một phần kịch bản.
          Mã 2 KHÔNG được coi là đạt.
Kết quả đột biến: KILLED (bắt được, có bằng chứng) · SURVIVED · INCONCLUSIVE · CHECKER_ERROR; chỉ KILLED được tính là bắt.
Chạy: python3 work/mow-mot-moit-mout/kiem-ct000-4.py [--dot-bien] [--kb TÊN,TÊN | --kb -] [--gioi N] [--json ĐƯỜNG_DẪN] [--trang ĐƯỜNG_DẪN]
Master Công cụ ML-DEF-023 · mã python:kiem-ct000-4 (work/tools-quy-trinh/view.html). Phản biện độc lập: python:ct000-audit.
"""
import re, html, sys, ast, unicodedata, collections, time, json

def nf(s): return unicodedata.normalize('NFKC', s)

TRANG = 'work/mow-mot-moit-mout/ban-duyet.html'
COT = {'Bảng Trạng thái': 5, 'Bảng Biến': 3, 'Bảng Giá trị': 5, 'Bảng Thao tác': 4, 'Bảng Bất biến': 3, 'Bảng Chuyển trạng thái': 6}
BB = ['B%d' % i for i in range(1, 14)]
CODES = ['OK', 'PARTIAL', 'UNAVAILABLE', 'RESOURCE_EXHAUSTED', 'ABORTED', 'FAILED_PRECONDITION', 'PERMISSION_DENIED', 'INVALID_ARGUMENT', 'UNKNOWN', 'DEADLINE_EXCEEDED', 'HUMAN']
QUYET = ['thiếu ô', 'làm tiếp', 'giao lại', 'ngoại lệ', 'huỷ', 'rút huỷ']
CAP = ('làm tiếp', 'giao lại', 'rút huỷ')
NGUOI_MAX = 1
TRO_LAI = {'G1': 'Chấm G1', 'G2': 'Chấm G2', 'G3': 'Chấm G2', 'G4': 'Chấm G4', 'G5': 'Chấm G5', 'Bù': 'Bù',
           'ĐS·TT': 'Đối soát·TT', 'ĐS·Huỷ': 'Đối soát·Huỷ', 'ĐS·QH': 'Đối soát·QH', 'ĐS·Bù': 'Đối soát·Bù'}
TRAN = {'lần_nhận': 8, 'lần_gia_hạn': 6, 'vòng': 6, 'lần_bù': 8, 'đang_bay': 3, 'đã_làm': 3,
        'tổng_làm': 4, 'đã_bù': 4, 'bù_bay': 3, 'M': 8, 'N': 8, 'MB': 8, 'lần_thay': 4}
MAC_DINH = dict(lần_nhận=0, M=2, thế_hệ=0, gen_giữ=-1, người_giữ=True, có_lịch=True, giữ_chỗ=False, còn_chỗ=True,
                hết_hạn_giữ=False, lần_gia_hạn=0, GH=1,
                ý_định=False, kết_luận=False, đang_bay=0, đã_làm=0, tổng_làm=0, mã_mới=False, bay_mã_mới=False,
                chống_trùng=False, tra_được=True, xác_nhận_vắng=False, làm_một_phần=False, làm_sai=False,
                đã_bù=0, bù_bay=0, lần_bù=0, MB=2, có_cách_bù=True, miễn_bù=False,
                quá_hạn_gốc=False, có_hạn_PH=False, quá_hạn_PH=False,
                lần_quá_chờ=0, lần_thay=0, bằng_chứng=False, nguồn='không',
                cờ_huỷ=False, vòng=0, N=2,
                g1='đủ', miễn_g1=False, g2='đủ', q1=True, q2=True, miễn_q1=False, chờ_duyệt=False,
                g4_chưa_biết=False, g5='đủ', chờ_nhận=False, còn_tác_động_G5=False,
                bước='G1', trở_lại='G2', gửi_sau_hạn=False, bù_sai=False)
AN = {'_gửi_lượt': False, '_ma': -1, '_ma_thử': False, '_owner': 0}
NOB = {'__builtins__': {}}

class SaiKhuon(Exception):
    pass

def ev_(code, ns):
    return eval(code, NOB, ns)

# ---------- đọc trang ----------
def cat_bang(h):
    a = h.find('id="formula-ct-000-4"')
    if a < 0: raise SaiKhuon('không thấy thẻ CT-000.4')
    s = h[a:h.find('</section>', a)]
    T = {}
    for name, n in COT.items():
        i = s.find('head-label">' + name + '<')
        if i < 0: raise SaiKhuon('thiếu ' + name)
        t = s[i:s.find('</table>', i)]
        m = re.search(r'<tbody>(.*?)</tbody>', t, re.S)
        if not m: raise SaiKhuon('thiếu thân ' + name)
        rows = []
        for r in re.findall(r'<tr>(.*?)</tr>', m.group(1), re.S):
            cells = [nf(html.unescape(re.sub(r'<[^>]+>', '', c)).strip()) for c in re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)]
            if len(cells) != n: raise SaiKhuon('%s: dòng sai số cột %r' % (name, cells[:2]))
            rows.append(cells)
        if not rows: raise SaiKhuon(name + ' rỗng')
        T[name] = rows
    return T

def expand(cell):
    out = []
    for part in cell.split(' + '):
        part = part.strip()
        m = re.match(r'(.*?)\s*\[(\w+): ([^\]]+)\]$', part)
        if m:
            base, var, vals = m.groups()
            for v in [x.strip() for x in vals.split(',')]:
                out.append((base.replace('{' + var + '}', v), {var: v}))
        else:
            out.append((part, {}))
    return out

def tach_ct(ct, ten):
    out = []
    for ln in ct.split(' ; '):
        if ' ← ' not in ln: raise SaiKhuon('công thức thiếu ← ở %s: %s' % (ten, ln))
        v, ex = ln.split(' ← ', 1)
        out.append((v.strip(), compile(ex.strip(), ten, 'eval'), ex.strip()))
    return out

def nap(T):
    for k in COT:
        if k not in T: raise SaiKhuon('thiếu ' + k)
    S = {'E': []}
    S['bien'] = {x.strip() for r in T['Bảng Biến'] for x in r[1].split(',') if x.strip()}
    ST, GLOB = {}, collections.OrderedDict()
    for r in T['Bảng Trạng thái']:
        dom = collections.OrderedDict()
        if r[4] not in ('—', ''):
            for seg in r[4].split(' ; '):
                if ': ' not in seg: raise SaiKhuon('miền sai: ' + seg)
                ev, vals = seg.split(': ', 1)
                dom[ev.strip()] = [v.strip() for v in vals.split(' / ')]
        if r[0] == '*':
            GLOB = dom
            continue
        for n, _ in expand(r[0]):
            ST[n] = dict(kind=r[1], holder=r[2], check=r[3], dom=dom)
    nonterm = [n for n in ST if ST[n]['kind'] != 'kết thúc']
    S.update(ST=ST, GLOB=GLOB, nonterm=nonterm)
    FORM, OPS, INV = {}, {}, {}
    try:
        for r in T['Bảng Giá trị']:
            ev, where, src, cokhi, ct = r
            lines = tach_ct(ct, ev)
            tg = nonterm if where == '*' else [n for n, _ in expand(where)]
            for n in tg:
                if (n, ev) in FORM: S['E'].append(('S1 công thức trùng', n, ev))
                FORM[(n, ev)] = (src, compile(cokhi, ev, 'eval'), lines, cokhi)
        for r in T['Bảng Thao tác']:
            OPS[r[0]] = (r[1], None if r[2] in ('—', '') else compile(r[2], r[0], 'exec'), r[2])
        for r in T['Bảng Bất biến']:
            if r[2] not in ('—', ''):
                INV[r[0]] = (r[1], compile(r[2], r[0], 'eval'), r[2])
    except SyntaxError as e:
        raise SaiKhuon('công thức sai cú pháp: %s' % e)
    S.update(FORM=FORM, OPS=OPS, INV=INV)
    ROWS = []
    for r in T['Bảng Chuyển trạng thái']:
        tid, frm, ev, vals, act, to = r
        if frm.startswith('*'):
            exc = [x.strip() for x in frm.split('trừ', 1)[1].split(',')] if 'trừ' in frm else []
            froms = [(n, {}) for n in nonterm if n not in exc]
        else:
            froms = expand(frm)
        for f, b in froms:
            a2, t2 = act, to
            for k, v in b.items():
                a2 = a2.replace('{' + k + '}', v)
                t2 = t2.replace('{' + k + '}', v)
            ops = [] if a2 in ('—', '') else [x.strip() for x in a2.split(' · ')]
            for v in [x.strip() for x in vals.split(' / ')]:
                ROWS.append(dict(id=tid, frm=f, ev=ev, val=v, ops=ops, to=t2))
    idx = collections.defaultdict(list)
    for x in ROWS: idx[(x['frm'], x['ev'], x['val'])].append(x)
    dom = {}
    for n in nonterm:
        d = collections.OrderedDict((k, list(v)) for k, v in ST[n]['dom'].items())
        for k, v in GLOB.items():
            d.setdefault(k, [])
            for x in v:
                if x not in d[k]: d[k].append(x)
        dom[n] = d
    S.update(ROWS=ROWS, idx=idx, dom=dom)
    return S

# ---------- kiểm tĩnh ----------
def kiem_tinh(S):
    E = list(S['E'])
    ST, FORM, OPS = S['ST'], S['FORM'], S['OPS']
    for n in S['nonterm']:
        if ST[n]['holder'] in ('', '—') or ST[n]['check'] in ('', '—'): E.append(('S6 thiếu người giữ hoặc lúc kiểm', n))
        for ev, vals in S['dom'][n].items():
            f = FORM.get((n, ev))
            if not f:
                E.append(('S1 không có công thức', n, ev)); continue
            fv = [v for v, _, _ in f[2]]
            if ev in S['GLOB']:
                if not set(vals) <= set(fv): E.append(('S1 miền khác công thức', n, ev, vals, fv))
            elif fv != vals:
                E.append(('S1 miền khác công thức', n, ev, vals, fv))
            for v in vals:
                k = len(S['idx'].get((n, ev, v), []))
                if k != 1: E.append(('S2 thiếu hoặc trùng dòng', n, ev, v, k))
    for (n, ev, v), rs in list(S['idx'].items()):
        if rs and (n not in S['dom'] or ev not in S['dom'][n] or v not in S['dom'][n][ev]):
            E.append(('S2 dòng ngoài miền', rs[0]['id'], n, ev, v))
    for x in S['ROWS']:
        if x['to'] not in ST and x['to'] not in ('(giữ nguyên)', '[trở lại]'): E.append(('S3 đích lạ', x['id'], x['to']))
        for op in x['ops']:
            if op.split('(')[0] not in OPS: E.append(('S4 thao tác chưa khai', x['id'], op))
    ok = S['bien'] | {'st', 'tác_nhân', 'mã', 'quyết', 'đối_số'}
    def ten(src, mode):
        return {nf(x.id) for x in ast.walk(ast.parse(src, mode=mode)) if isinstance(x, ast.Name)}
    for (n, ev), f in FORM.items():
        for _, _, ex in f[2]:
            for x in ten(ex, 'eval') - ok: E.append(('S5 biến chưa khai', ev, x))
        for x in ten(f[3], 'eval') - ok: E.append(('S5 biến chưa khai', ev, x))
    for k, (loai, code, ct) in OPS.items():
        if code is not None:
            for x in ten(ct, 'exec') - ok: E.append(('S5 biến chưa khai', k, x))
    for k, (_, _, ct) in S['INV'].items():
        for x in ten(ct, 'eval') - ok: E.append(('S5 biến chưa khai', k, x))
    for b in BB:
        if b not in S['INV']: E.append(('S6 thiếu bất biến', b))
    for (n, ev), f in FORM.items():
        if ev == 'kết quả':
            for c in CODES:
                ns = dict(MAC_DINH); ns.update(st=n, mã=c)
                if not any(ev_(code, ns) for _, code, _ in f[2]): E.append(('S7 mã chưa có giá trị', n, c))
    # S9: cổng không được mở bằng nhánh mặc định; dữ liệu thiếu/sai phải có nhánh riêng đứng cuối
    for (n, ev), f in FORM.items():
        if n.startswith('Chấm G') and ev == 'chấm':
            for v, _, ex in f[2]:
                if v == 'đủ' and ex.strip() == 'True': E.append(('S9 «đủ» là nhánh mặc định: dữ liệu thiếu/sai sẽ lọt cổng', n))
            if not f[2] or f[2][-1][0] != 'dữ liệu sai': E.append(('S9 thiếu nhánh cuối «dữ liệu sai»', n))
    return list(dict.fromkeys(E))

# ---------- chạy 1 bước ----------
KEYS = sorted(list(MAC_DINH) + list(AN) + ['st'])

def dong(s):
    """chuẩn hoá: chỉ quan hệ «trùng thế hệ hiện tại hay không» có nghĩa, nên quy thế hệ về giá trị tương đối"""
    s = dict(s); h = s['thế_hệ']
    def rel(g): return -1 if g < 0 else 3 - min(3, h - g)
    s['gen_giữ'] = rel(s['gen_giữ']); s['_ma'] = rel(s['_ma']); s['thế_hệ'] = 3
    st = s['st']
    if not st.startswith('Chờ người'): s['lần_quá_chờ'] = 0; s['lần_thay'] = 0
    if st not in ('Đang chạy', 'Bù'): s['hết_hạn_giữ'] = False; s['lần_gia_hạn'] = 0
    if st != 'Đang chạy': s['_gửi_lượt'] = False
    if not st.startswith('Chờ ĐK'): s['nguồn'] = 'không'
    if s['_ma_thử'] or s['_ma'] < 0: s['_ma'] = -1; s['_ma_thử'] = False
    return tuple(s[k] for k in KEYS)

def mo(t): return dict(zip(KEYS, t))

def ap_dung(S, s, ev, chon):
    st = s['st']
    f = S['FORM'].get((st, ev))
    if f is None: return None, ('L1 không có công thức', st, ev)
    ns = dict(s); ns.update(chon)
    v = None
    for val, code, _ in f[2]:
        if ev_(code, ns):
            v = val; break
    if v is None: return None, ('L1 công thức không ra giá trị', st, ev)
    rs = S['idx'].get((st, ev, v), [])
    if len(rs) != 1: return None, ('L1 không có đúng 1 dòng', st, ev, v)
    r = rs[0]
    new = dict(s)
    for k, x in chon.items():
        if not k.startswith('_'): new[k] = x
    names = []
    for op in r['ops']:
        name, arg = (op.split('(', 1)[0], op.split('(', 1)[1][:-1]) if '(' in op else (op, '')
        names.append(name)
        if name not in S['OPS']: return None, ('L1 thao tác chưa khai', r['id'], op)
        code = S['OPS'][name][1]
        if code is not None:
            new['đối_số'] = arg
            exec(code, NOB, new)
    for k in ('tác_nhân', 'mã', 'quyết', 'đối_số'): new.pop(k, None)
    to = r['to']
    if to == '(giữ nguyên)': to = st
    elif to == '[trở lại]':
        to = TRO_LAI.get(new['trở_lại'])
        if to is None: return None, ('L1 bước trở lại không hợp lệ', r['id'], new['trở_lại'])
    new['st'] = to
    if to.startswith('Chấm G'): new['bước'] = to[-2:]
    elif to in ('Chờ', 'Đang chạy', 'Chờ người·G3'): new['bước'] = 'G3'
    # thế giới: lượt bị thu hồi khi chưa gửi thì có thể vẫn còn sống và cố gửi
    if st == 'Đang chạy' and to != 'Đang chạy' and ev in ('hết hạn giữ', 'yêu cầu huỷ') and not s['_gửi_lượt']:
        new['_ma'], new['_ma_thử'] = s['gen_giữ'], False
    if 'nhận lượt' in names: new['_gửi_lượt'] = False
    if chon.get('_ai') == 'chính': new['_gửi_lượt'] = True
    if chon.get('_ai') == 'ma': new['_ma_thử'] = True
    if ev == 'kết quả' and st == 'Chờ người·G3' and chon.get('mã') == 'OK' and new['đã_làm'] == 0:
        new['đã_làm'] = 1; new['tổng_làm'] += 1
    if ev == 'quyết định' and chon.get('quyết') in CAP: new['_owner'] += 1
    return new, r['id']

def lua_chon(s, ev):
    st = s['st']
    if ev == 'kết quả':
        if st == 'Đang chạy':
            L = []
            if s['đã_làm'] >= 1 and s['đang_bay'] == 0: L += ['OK', 'UNKNOWN', 'DEADLINE_EXCEEDED'] + (['PARTIAL'] if s['làm_một_phần'] else [])
            if s['đang_bay'] > 0: L += ['UNKNOWN', 'DEADLINE_EXCEEDED', 'UNAVAILABLE']
            if s['đã_làm'] == 0 and s['đang_bay'] == 0: L += ['UNAVAILABLE', 'RESOURCE_EXHAUSTED', 'ABORTED', 'FAILED_PRECONDITION', 'HUMAN']
            return [{'mã': c} for c in dict.fromkeys(L)]
        return [{'mã': c} for c in ('OK', 'FAILED_PRECONDITION', 'HUMAN')]
    if ev == 'làm thao tác':
        L = []
        if st == 'Đang chạy' and not s['_gửi_lượt']: L.append({'tác_nhân': s['gen_giữ'], '_ai': 'chính'})
        if s['_ma'] >= 0 and not s['_ma_thử']: L.append({'tác_nhân': s['_ma'], '_ai': 'ma'})
        return L
    if ev == 'quyết định':
        return [{'quyết': q} for q in QUYET if not (q in CAP and s['_owner'] >= NGUOI_MAX)]
    return [{}]

def the_gioi(s):
    st = s['st']; out = []; term = st.startswith('Kết thúc')
    if not term:
        if not s['quá_hạn_gốc']: out.append(('qua hạn gốc', 'giờ', {'quá_hạn_gốc': True}))
        if s['có_hạn_PH'] and not s['quá_hạn_PH']: out.append(('qua hạn PH', 'giờ', {'quá_hạn_PH': True}))
        if st in ('Đang chạy', 'Bù') and not s['hết_hạn_giữ']: out.append(('qua hạn giữ', 'giờ', {'hết_hạn_giữ': True}))
        if st.startswith('Chờ người') and s['lần_quá_chờ'] == s['lần_thay'] and s['lần_quá_chờ'] < 2:
            out.append(('qua hạn chờ', 'giờ', {'lần_quá_chờ': s['lần_quá_chờ'] + 1}))
    if s['đang_bay'] > 0:
        d = 0 if (s['chống_trùng'] and s['đã_làm'] >= 1 and not s['bay_mã_mới']) else 1
        out.append(('bên nhận làm', 'ngoài', {'đang_bay': s['đang_bay'] - 1, 'đã_làm': s['đã_làm'] + d, 'tổng_làm': s['tổng_làm'] + d}))
        out.append(('bên nhận bỏ', 'ngoài', {'đang_bay': s['đang_bay'] - 1}))
    if s['bù_bay'] > 0:
        d = 0 if (s['chống_trùng'] and s['đã_bù'] >= s['tổng_làm']) else 1
        out.append(('bù làm', 'ngoài', {'bù_bay': s['bù_bay'] - 1, 'đã_bù': s['đã_bù'] + d}))
        out.append(('bù mất', 'ngoài', {'bù_bay': s['bù_bay'] - 1}))
    if s['nguồn'] == 'mở' and not term:
        fix = {'nguồn': 'gỡ'}
        if '·ĐS·' in st: fix['bằng_chứng'] = True
        else: fix.update({'G1': {'g1': 'đủ'}, 'G2': {'g2': 'đủ'}, 'G4': {'g4_chưa_biết': False}, 'G5': {'g5': 'đủ'}}.get(s['bước'], {}))
        out.append(('X6 gỡ', 'ngoài', fix))
        out.append(('X6 hỏng', 'ngoài', {'nguồn': 'hỏng'}))
        if s['bước'] == 'G1': out.append(('X6 đóng', 'ngoài', {'nguồn': 'đóng'}))
    return out

def buoc(S, s):
    st = s['st']; out = []
    if st not in S['ST']: return [('?', 'máy', ('L1 trạng thái lạ', st))]
    if not st.startswith('Kết thúc'):
        for ev in S['dom'][st]:
            f = S['FORM'].get((st, ev))
            if f is None:
                out.append((ev, 'máy', ('L1 không có công thức', st, ev))); continue
            lop = 'người' if f[0] == 'người' else 'máy'
            for chon in lua_chon(s, ev):
                ns = dict(s); ns.update(chon)
                if not ev_(f[1], ns): continue
                new, x = ap_dung(S, s, ev, chon)
                out.append((ev, lop, new if new is not None else x))
    for name, lop, d in the_gioi(s):
        new = dict(s); new.update(d); out.append((name, lop, new))
    return out

def vi_pham(S, s):
    E = []
    for k, (y, code, _) in S['INV'].items():
        try:
            if not ev_(code, dict(s)): E.append(('%s %s' % (k, y), s['st']))
        except Exception as e:
            E.append(('%s lỗi tính: %s' % (k, e), s['st']))
    for k, t in TRAN.items():
        if s.get(k, 0) > t: E.append(('L2 biến tăng không giới hạn', k, s['st']))
    return E

# ---------- duyệt hết ----------
def vet(nodes, cha, u, them=None):
    ist = KEYS.index('st'); out = []
    while u is not None and u in cha:
        p, ev = cha[u]; out.append('%s→%s' % (ev, nodes[u][ist])); u = p
    out.reverse()
    if them: out.append(them)
    return 'Mới · ' + ' · '.join(out)

GIOI = 400000   # --gioi N: trần trạng thái mỗi kịch bản; vượt trần = INCONCLUSIVE (không phải đạt)

def kham(S, init, gioi=None, nhanh=False):
    import array
    gioi = gioi or GIOI
    E = []; ids = {}; nodes = []; cha = {}; da_bao = set()
    ed = (array.array('i'), array.array('i'), array.array('b'))
    k0 = dong(init); ids[k0] = 0; nodes.append(k0)
    E += vi_pham(S, init)
    q = collections.deque([0])
    while q:
        u = q.popleft(); s = mo(nodes[u])
        for name, lop, nx in buoc(S, s):
            if isinstance(nx, tuple):
                if nx[0] not in da_bao:
                    da_bao.add(nx[0]); E.append(nx + ('VẾT: ' + vet(nodes, cha, u, name),))
                if nhanh: return E, None
                continue
            k = dong(nx)
            if k not in ids:
                ids[k] = len(nodes); nodes.append(k); q.append(ids[k]); cha[ids[k]] = (u, name)
                for e in vi_pham(S, nx):
                    if e[0] not in da_bao:
                        da_bao.add(e[0]); E.append(e + ('VẾT: ' + vet(nodes, cha, ids[k]),))
                    if nhanh: return E, None
            ed[0].append(u); ed[1].append(ids[k]); ed[2].append(0 if lop in ('máy', 'giờ') else 1)
        if len(nodes) > gioi:
            E.append(('INCONCLUSIVE quá trần trạng thái', len(nodes))); return E, None
    return E, (nodes, ed)

def scc(n, adj):
    index = [None] * n; low = [0] * n; on = [False] * n; st = []; comp = [None] * n; c = 0; idx = 0
    for v0 in range(n):
        if index[v0] is not None: continue
        index[v0] = low[v0] = idx; idx += 1; st.append(v0); on[v0] = True
        stack = [(v0, 0)]
        while stack:
            v, i = stack[-1]
            if i < len(adj[v]):
                stack[-1] = (v, i + 1); w = adj[v][i]
                if index[w] is None:
                    index[w] = low[w] = idx; idx += 1; st.append(w); on[w] = True; stack.append((w, 0))
                elif on[w]:
                    low[v] = min(low[v], index[w])
            else:
                stack.pop()
                if stack:
                    p = stack[-1][0]; low[p] = min(low[p], low[v])
                if low[v] == index[v]:
                    while True:
                        w = st.pop(); on[w] = False; comp[w] = c
                        if w == v: break
                    c += 1
    return comp

def bfs_rev(tgt, radj):
    seen = set(tgt); q = collections.deque(tgt)
    while q:
        v = q.popleft()
        for u in radj[v]:
            if u not in seen: seen.add(u); q.append(u)
    return seen

def song(nodes, ed):
    E = []; n = len(nodes)
    ist = KEYS.index('st'); st = [x[ist] for x in nodes]
    adj = [[] for _ in range(n)]; radj = [[] for _ in range(n)]; rall = [[] for _ in range(n)]
    for u, v, lop in zip(*ed):
        rall[v].append(u)
        if lop == 0 and u != v:
            adj[u].append(v); radj[v].append(u)
    comp = scc(n, adj); size = collections.Counter(comp)
    bad = sorted({st[i] for i in range(n) if size[comp[i]] > 1})
    if bad: E.append(('L2 vòng chỉ gồm máy và giờ', bad[:8]))
    tgt = [i for i in range(n) if st[i].startswith('Kết thúc') or st[i] == 'Chờ Owner']
    reach = bfs_rev(tgt, radj)
    orphan = sorted({st[i] for i in range(n) if i not in reach})
    if orphan: E.append(('L3 mồ côi: máy và giờ không đưa tới Kết thúc hoặc Chờ Owner', orphan[:8]))
    reach2 = bfs_rev([i for i in range(n) if st[i].startswith('Kết thúc')], rall)
    stuck = [i for i in range(n) if st[i] == 'Chờ Owner' and i not in reach2]
    if stuck: E.append(('L4 Chờ Owner không có đường tới Kết thúc', len(stuck)))
    return E

# ---------- 2 việc cùng phạm vi, trần chỗ = 1 ----------
# Chạy ĐÚNG công thức «xin nhận», dòng chuyển và thao tác của bảng (ap_dung), không chạy chương trình riêng.
# còn_chỗ tính từ giữ_chỗ của cả hai việc. Có «khoá phạm vi»: đọc + ghi là 1 bước; không có: đọc trước, ghi sau
# (việc kia có thể xen giữa). Phủ: hết chỗ, tranh chỗ cuối, nhả chỗ rồi việc kia nhận lại.
def dong_thoi(S):
    TRAN_CHO = 1
    rs = S['idx'].get(('Chờ', 'xin nhận', 'được'), [])
    if len(rs) != 1: return ('D0 thiếu dòng Chờ · xin nhận · được',)
    nguyen_tu = 'khoá phạm vi' in [o.split('(')[0] for o in rs[0]['ops']]
    def goc():
        s = dict(MAC_DINH); s.update(AN); s.update(st='Chờ', bước='G3'); return s
    def dem(js): return sum(1 for j in js if j['giữ_chỗ'])
    def nhan(j, con_cho):
        s = dict(j); s['còn_chỗ'] = con_cho
        new, x = ap_dung(S, s, 'xin nhận', {})
        if new is None: return None, x
        new['còn_chỗ'] = True
        return new, None
    def xong(j):
        new, x = ap_dung(S, j, 'kết quả', {'mã': 'OK'})
        if new is None: return None, x
        new['st'] = 'Xong'; return new, None
    q = [((goc(), goc()), (None, None))]; seen = set(); ca_hai_xong = False
    while q:
        js, ps = q.pop()
        k = tuple(dong(j) for j in js) + ps
        if k in seen: continue
        seen.add(k)
        if sum(1 for j in js if j['st'] == 'Đang chạy') > TRAN_CHO or dem(js) > TRAN_CHO:
            return ('D1 hai việc cùng chạy khi trần chỗ = 1', [j['st'] for j in js])
        if all(j['st'] == 'Xong' for j in js):
            ca_hai_xong = True; continue
        for i in (0, 1):
            j, p = js[i], ps[i]; ra = []
            if j['st'] == 'Chờ':
                if nguyen_tu: ra.append(nhan(j, dem(js) < TRAN_CHO) + (None,))
                elif p is None: ra.append((j, None, dem(js) < TRAN_CHO))
                else: ra.append(nhan(j, p) + (None,))
            elif j['st'] == 'Đang chạy':
                ra.append(xong(j) + (None,))
            for nj, loi, np_ in ra:
                if nj is None: return ('D0 bảng không chạy được khi tranh chỗ', loi)
                js2 = list(js); js2[i] = nj; ps2 = list(ps); ps2[i] = np_
                q.append((tuple(js2), tuple(ps2)))
    if not ca_hai_xong: return ('D2 không có đường để cả hai việc cùng xong (chỗ không được nhả hoặc không nhận lại)',)
    return None

# ---------- ca thử: nhập dữ kiện, máy tự tính ----------
def chay_ca(S, ten, them, buoc_ds, cuoi, phai=(), cam=(), kiem=None):
    s = dict(MAC_DINH); s.update(AN); s.update(them); s['st'] = 'Mới'
    qua = ['Mới']
    for i, (ev, chon) in enumerate(buoc_ds):
        tg = [d for (n, l, d) in the_gioi(s) if n == ev]
        if tg:
            s = dict(s); s.update(tg[0])
        else:
            if ev not in S['dom'].get(s['st'], {}): return 'bước %d: «%s» không có ở %s · đường: %s' % (i + 1, ev, s['st'], ' → '.join(qua))
            chon = dict(chon or {})
            if ev == 'làm thao tác':
                ai = chon.get('_ai', 'chính')
                chon.update(_ai=ai, tác_nhân=s['gen_giữ'] if ai == 'chính' else s['_ma'])
            f = S['FORM'].get((s['st'], ev))
            ns = dict(s); ns.update(chon)
            if f is None or not ev_(f[1], ns): return 'bước %d: «%s» chưa được phép ở %s' % (i + 1, ev, s['st'])
            new, x = ap_dung(S, s, ev, chon)
            if new is None: return 'bước %d: %r' % (i + 1, x)
            s = new
        v = vi_pham(S, s)
        if v: return 'bước %d («%s»): vi phạm %r' % (i + 1, ev, v[0])
        qua.append(s['st'])
    if s['st'] != cuoi: return 'dừng ở %s, mong %s · đường: %s' % (s['st'], cuoi, ' → '.join(qua))
    for p in phai:
        if p not in qua: return 'không đi qua %s' % p
    for p in cam:
        if p in qua: return 'đi qua %s (cấm)' % p
    for k, v in (kiem or {}).items():
        if s.get(k) != v: return 'cuối: %s = %r, mong %r · đường: %s' % (k, s.get(k), v, ' → '.join(qua))
    return None

K, C1, C2 = ('khai xong', {}), ('chấm', {}), ('chấm', {})
NHAN, GUI, LAM = ('xin nhận', {}), ('làm thao tác', {'_ai': 'chính'}), ('bên nhận làm', {})
def KQ(m): return ('kết quả', {'mã': m})
def QD(q): return ('quyết định', {'quyết': q})
VAO = [K, C1, C2, NHAN]
BD = ('bắt đầu', {})
HUY_SAU_LAM = VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('yêu cầu huỷ', {}), ('xét', {}), BD]   # đã làm 1 lần, huỷ → lần bù thứ nhất
CA = [
    ('1 việc bình thường tới đóng hồ sơ', {}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('chấm', {})], 'Kết thúc·Đạt'),
    ('2 M=1: lượt duy nhất vẫn chạy, lần xin sau bị chặn', {'M': 1, 'chống_trùng': True}, VAO + [KQ('UNAVAILABLE'), NHAN], 'Chờ Owner', ['Đang chạy']),
    ('3 gửi rồi máy chết, người xác nhận đã gửi', {'tra_được': False}, VAO + [GUI, LAM, ('qua hạn giữ', {}), ('hết hạn giữ', {}), ('đối soát', {}), ('trả lời', {}), ('đối soát', {})], 'Chấm G4', [], ['Chờ người·ĐS·Huỷ']),
    ('4 lượt cũ cố gửi sau khi bị thu hồi', {}, VAO + [('qua hạn giữ', {}), ('hết hạn giữ', {}), NHAN, ('làm thao tác', {'_ai': 'ma'}), GUI, LAM], 'Đang chạy'),
    ('5 không chống trùng, tra «chưa thấy»: không gửi lại', {}, VAO + [GUI, KQ('UNAVAILABLE'), ('đối soát', {}), ('qua hạn PH', {}), ('đến lúc kiểm', {}), ('kiểm lại', {})], 'Chờ Owner'),
    ('6 huỷ khi lệnh ngoài chưa rõ, lệnh cũ thành công sau', {'tra_được': False}, VAO + [GUI, ('yêu cầu huỷ', {}), ('xét', {}), ('đối soát', {}), LAM, ('trả lời', {}), ('đối soát', {}), BD, ('bù làm', {}), ('bù', {})], 'Kết thúc·Huỷ', ['Bắt đầu bù'], ['Chấm G4']),
    ('7 huỷ sau hạn chót', {}, [K, C1, C2, ('qua hạn gốc', {}), ('đến lúc kiểm', {}), ('quá hạn', {}), QD('huỷ'), ('xét', {})], 'Kết thúc·Huỷ'),
    ('8 chờ hợp lệ đến giờ kiểm: không thành mồ côi', {'g2': 'chờ'}, [K, C1, C2, ('kiểm lại', {}), ('kiểm lại', {})], 'Chờ ĐK·G2'),
    ('9 miễn G4.1 nhưng G4.2 vẫn sai: cổng không mở', {'q1': False, 'q2': False, 'N': 1}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), QD('ngoại lệ'), ('chấm', {})], 'Chờ Owner', [], ['Chấm G5']),
    ('10 miễn G4.1, câu khác đạt: cổng mở', {'q1': False, 'N': 1}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), QD('ngoại lệ'), ('chấm', {}), ('chấm', {})], 'Kết thúc·Đạt'),
    ('11 miễn G1 hợp lệ: chấm lại không bắt câu đã miễn', {'g1': 'thiếu'}, [K, C1, ('qua hạn chờ', {}), ('đến lúc kiểm', {}), ('qua hạn gốc', {}), ('kiểm lại', {}), ('quá hạn', {}), QD('ngoại lệ'), ('chấm', {})], 'Chấm G2'),
    ('12 lỗi điều kiện: sửa xong chấm lại G2 rồi mới chạy', {}, VAO + [KQ('FAILED_PRECONDITION'), ('X6 gỡ', {}), ('kiểm lại', {}), ('chấm', {})], 'Chờ'),
    ('13 bù mất phản hồi: đối soát lần bù, không bù 2 lần', {'tra_được': False, 'chờ_duyệt': True}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('yêu cầu huỷ', {}), ('xét', {}), BD, ('bù', {}), ('đối soát bù', {}), ('bù làm', {}), ('trả lời', {}), ('đối soát bù', {})], 'Kết thúc·Huỷ', [], [], {'lần_bù': 1}),
    ('14 giao lại lúc bù: về đúng bước bù', {'có_cách_bù': False, 'chờ_duyệt': True}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('yêu cầu huỷ', {}), ('xét', {}), BD, ('bù', {}), QD('giao lại')], 'Bù'),
    ('15 Owner chấp nhận phần không bù được: đóng huỷ', {'có_cách_bù': False, 'chờ_duyệt': True}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('yêu cầu huỷ', {}), ('xét', {}), BD, ('bù', {}), QD('ngoại lệ'), ('bù', {})], 'Kết thúc·Huỷ'),
    ('16 thử lại cùng mã khi có chống trùng: bên nhận làm 1 lần', {'chống_trùng': True}, VAO + [GUI, KQ('UNAVAILABLE'), NHAN, GUI, LAM, LAM, KQ('OK')], 'Chấm G4'),
    # P74 — 3 đường sai GPT v6 tái hiện + ca được phép tương ứng (sửa đúng chỗ bắt đầu lệnh mới, không chặn nhận kết quả)
    ('17 quá hạn gốc khi còn quyền giữ: không gửi mới', {}, VAO + [('qua hạn gốc', {}), GUI], 'Đang chạy', [], [], {'đang_bay': 0, 'gửi_sau_hạn': False}),
    ('18 lệnh gửi trước hạn vẫn nhận kết quả sau hạn', {}, VAO + [GUI, ('qua hạn gốc', {}), LAM, KQ('OK')], 'Chấm G4'),
    ('19 MB=1: bù mất rồi hết hạn giữ → không bù lần 2', {'MB': 1, 'chờ_duyệt': True}, HUY_SAU_LAM + [('bù mất', {}), ('qua hạn giữ', {}), ('hết hạn giữ', {}), BD], 'Chờ Owner', [], [], {'lần_bù': 1}),
    ('20 MB=2: lần bù thứ hai vẫn được', {'MB': 2, 'chờ_duyệt': True}, HUY_SAU_LAM + [('bù mất', {}), ('qua hạn giữ', {}), ('hết hạn giữ', {}), BD], 'Bù', [], [], {'lần_bù': 2, 'bù_bay': 1}),
    ('21 hết hạn phục hồi: không bắt đầu bù mới', {'MB': 3, 'chờ_duyệt': True}, HUY_SAU_LAM + [('bù mất', {}), ('qua hạn PH', {}), ('qua hạn giữ', {}), ('hết hạn giữ', {}), BD], 'Chờ Owner', [], [], {'lần_bù': 1}),
    ('22 hết hạn PH nhưng lệnh bù cũ vẫn được nhận kết quả', {'chờ_duyệt': True}, HUY_SAU_LAM + [('qua hạn PH', {}), ('bù làm', {}), ('bù', {})], 'Kết thúc·Huỷ'),
    # dữ liệu thiếu / sai / chưa biết không được mở cổng
    ('23 G2 thiếu dữ liệu', {'g2': None}, [K, C1, C2], 'Chờ ĐK·G2'),
    ('24 G2 giá trị lạ', {'g2': 'DU'}, [K, C1, C2], 'Chờ ĐK·G2'),
    ('25 G5 thiếu dữ liệu', {'g5': None}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('chấm', {})], 'Chờ ĐK·G5', [], ['Kết thúc·Đạt']),
    ('26 G5 chưa biết', {'g5': 'chưa biết'}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {}), ('chấm', {})], 'Chờ ĐK·G5', [], ['Kết thúc·Đạt']),
    ('27 G1 thiếu dữ liệu', {'g1': None}, [K, C1], 'Chờ ĐK·G1'),
    ('28 G4 thiếu dữ liệu câu 2 ở vòng cuối', {'q2': None, 'N': 1}, VAO + [GUI, LAM, KQ('OK'), ('chấm', {})], 'Chờ ĐK·G4'),
    # hết chỗ (17 kịch bản cũ đều còn_chỗ=True nên không bao giờ xét)
    ('29 hết chỗ: không vào chạy', {'còn_chỗ': False}, [K, C1, C2, NHAN], 'Chờ', [], ['Đang chạy'], {'giữ_chỗ': False}),
]

KICH_BAN = [
    ('thường', {}), ('chống trùng', {'chống_trùng': True}), ('M=1', {'M': 1}),
    ('không tra được', {'tra_được': False}), ('xác nhận vắng', {'xác_nhận_vắng': True, 'tra_được': False}),
    ('G1 thiếu', {'g1': 'thiếu'}), ('G1 chưa có Loại việc', {'g1': 'LV sai'}), ('G2 chờ', {'g2': 'chờ'}), ('G2 lỗi', {'g2': 'lỗi'}),
    ('G4 câu miễn được sai', {'q1': False, 'N': 1}), ('G4 câu khác sai', {'q2': False}), ('G4 chờ duyệt', {'chờ_duyệt': True}),
    ('G4 chưa biết', {'g4_chưa_biết': True}), ('G5 lỗi, chờ nhận', {'g5': 'lỗi', 'chờ_nhận': True, 'còn_tác_động_G5': True}),
    ('không có cách bù', {'có_cách_bù': False}), ('làm một phần', {'làm_một_phần': True}), ('làm sai', {'làm_sai': True}),
    ('hết chỗ', {'còn_chỗ': False}), ('G2 thiếu dữ liệu', {'g2': None}), ('G5 chưa biết', {'g5': 'chưa biết'}), ('MB=1', {'MB': 1}),
]
KB_CHON = None   # --kb: chỉ xét một phần; khi đó mã thoát tối đa là 2 (chưa kết luận toàn phạm vi)

def kiem_het(T, nhanh=False, in_ra=False):
    S = nap(T)
    E = [('S',) + tuple(e) if not str(e[0]).startswith('S') else e for e in kiem_tinh(S)]
    if E and nhanh: return E, S
    d = dong_thoi(S)
    if d:
        E.append(d)
        if nhanh: return E, S
    for ca in CA:
        r = chay_ca(S, *ca)
        if r:
            E.append(('C ' + ca[0], r))
            if nhanh: return E, S
        elif in_ra: print('  ✓ ca', ca[0])
    for ten, them in KICH_BAN:
        if KB_CHON and ten not in KB_CHON: continue
        s0 = dict(MAC_DINH); s0.update(AN); s0.update(them); s0['st'] = 'Mới'
        e, g = kham(S, s0, nhanh=nhanh)
        E += [('K ' + ten,) + tuple(x) for x in e]
        if g and not e:
            E += [('K ' + ten,) + tuple(x) for x in song(*g)]
            if in_ra: print('  ✓ kịch bản %-24s %6d trạng thái · %7d bước' % (ten, len(g[0]), len(g[1][0])))
        if E and nhanh: return E, S
    return E, S

def dot_bien(T):
    M = []
    rows = T['Bảng Chuyển trạng thái']
    loai = {r[0]: r[1] for r in T['Bảng Thao tác']}
    for i, r in enumerate(rows):
        M.append(('xoá dòng ' + r[0], dict(T, **{'Bảng Chuyển trạng thái': rows[:i] + rows[i + 1:]})))
    for i, r in enumerate(rows):
        ops = [] if r[4] in ('—', '') else r[4].split(' · ')
        for j, op in enumerate(ops):
            if loai.get(op.split('(')[0]) in ('trạng thái', 'đồng thời'):
                r2 = list(r); rest = ops[:j] + ops[j + 1:]; r2[4] = ' · '.join(rest) if rest else '—'
                M.append(('bỏ «%s» ở %s' % (op, r[0]), dict(T, **{'Bảng Chuyển trạng thái': rows[:i] + [r2] + rows[i + 1:]})))
    def sua(bang, loc, cot, cu, moi, ten, cot2=None, moi2=None):
        B = T[bang]
        for i, r in enumerate(B):
            if loc(r) and cu in r[cot]:
                r2 = list(r); r2[cot] = r2[cot].replace(cu, moi)
                if cot2 is not None: r2[cot2] = moi2
                M.append((ten, dict(T, **{bang: B[:i] + [r2] + B[i + 1:]}))); return
        M.append((ten + ' (KHÔNG ÁP ĐƯỢC)', None))
    G, C = 'Bảng Giá trị', 'Bảng Chuyển trạng thái'
    sua(G, lambda r: r[0] == 'xin nhận', 4, 'lần_nhận >= M', 'lần_nhận > M', 'xét M sau khi tăng')
    sua(G, lambda r: r[0] == 'gia hạn', 4, ' and lần_gia_hạn < GH', '', 'gia hạn không trần')
    sua(G, lambda r: r[0] == 'làm thao tác', 4, 'tác_nhân == thế_hệ and not hết_hạn_giữ', 'True', 'gửi không kiểm thế hệ')
    sua(G, lambda r: r[0] == 'đối soát', 4, 'đã_làm == 0 and đang_bay == 0 and', 'đã_làm == 0 and', 'coi «chưa thấy» là «chưa làm»')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G4', 4, '(q1 is False and not miễn_q1)', '(q1 is False)', 'G4 bỏ qua miễn')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G4', 4, 'or q2 is False) and', 'or not q2) and', 'thiếu G4 coi là sai (hết vòng)')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G1', 4, ' and not miễn_g1', '', 'G1 bỏ qua miễn')
    sua(G, lambda r: r[0] == 'kết quả' and r[1] == 'Đang chạy', 4, ' and chống_trùng', '', 'coi mọi lỗi tạm là an toàn')
    sua(G, lambda r: r[0] == 'bù', 4, ' and bù_bay == 0 and', ' and', 'đóng huỷ khi lệnh bù còn bay')
    sua(C, lambda r: r[3] == 'Lỗi tạm không an toàn', 5, 'Đối soát·TT', 'Chờ', 'T24 gửi lại ngay không đối soát')
    sua(C, lambda r: r[1] == 'Đối soát·TT' and 'chưa thấy' in r[3], 4, 'cùng mã', 'kết luận · mã mới', 'thử lại bằng mã mới khi lệnh cũ còn bay')
    sua(G, lambda r: r[0] == 'làm thao tác', 4, ' and (not ý_định or kết_luận or chống_trùng)', '', 'gửi khi ý định cũ chưa kết luận')
    sua(G, lambda r: r[0] == 'quyết định', 4, " or (quyết == 'huỷ' and cờ_huỷ)", '', 'Owner huỷ lại khi đang huỷ')
    sua(C, lambda r: r[1] == 'Xét huỷ' and r[3] == 'có dở', 5, 'Đối soát·Huỷ', 'Kết thúc·Huỷ', 'huỷ đóng luôn khi còn lệnh dở')
    sua(C, lambda r: r[1] == 'Bù' and r[3] == 'chưa biết', 5, 'Đối soát·Bù', 'Bù', 'bù mất phản hồi thì bù lại ngay', 4, 'lần bù +1 · gửi bù')
    sua(C, lambda r: r[2] == 'quyết định' and r[3] == 'giao lại', 5, '[trở lại]', 'Chấm G2', 'giao lại lúc bù quay về nghiệp vụ')
    sua(C, lambda r: r[2] == 'quyết định' and r[3] == 'ngoại lệ', 5, '[trở lại]', 'Chấm G5', 'ngoại lệ tự mở cả cổng')
    # P74 — đột biến cho 3 đường sai GPT v6, dữ liệu thiếu/sai, hết chỗ
    sua(G, lambda r: r[0] == 'làm thao tác', 4, ' and not quá_hạn_gốc', '', 'gửi mới sau hạn gốc')
    sua(G, lambda r: r[0] == 'bắt đầu', 4, 'lần_bù >= MB', 'lần_bù > MB', 'trần lần bù lệch 1')
    sua(G, lambda r: r[0] == 'bắt đầu', 4, 'quá hạn PH ← quá_hạn_PH', 'quá hạn PH ← False', 'bắt đầu bù sau hạn PH')
    sua(C, lambda r: r[1] == 'Đối soát·Bù' and r[3] == 'chắc chưa làm', 5, 'Bắt đầu bù', 'Bù', 'bù lại vòng qua cửa Bắt đầu bù', 4, 'cùng mã · nhận lượt · lần bù +1 · gửi bù')
    sua(C, lambda r: r[1] == 'Bù' and r[3] == 'không dở', 5, 'Bắt đầu bù', 'Bù', 'hết hạn giữ bù lại ngay', 4, 'thế hệ +1 · nhận lượt · lần bù +1 · gửi bù')
    sua(G, lambda r: r[0] == 'xin nhận', 4, 'hết chỗ ← not còn_chỗ', 'hết chỗ ← False', 'hết chỗ luôn báo còn')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G2', 4, "đủ ← g2 == 'đủ'", 'đủ ← True', 'G2 mặc định đủ')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G5', 4, "đủ ← g5 == 'đủ' and chờ_nhận is False", 'đủ ← True', 'G5 mặc định đủ')
    sua(G, lambda r: r[0] == 'chấm' and r[1] == 'Chấm G5', 4, " ; chưa biết ← g5 == 'chưa biết'", '', 'G5 bỏ nhánh chưa biết')
    T2 = dict(T); T2.pop('Bảng Giá trị')
    M.append(('xoá Bảng Giá trị', T2))
    return M

def kiem_cau_truc(h):
    """S8: mọi bảng trong CT-000.1 / .2 / .4 có số ô mỗi dòng = số cột đầu bảng.
    (Phép kiểm dùng tay ở P70–P72, gộp vào đây để không phải viết lại.)"""
    E = []; da = 0
    for sid in ('formula-ct-000-1', 'formula-ct-000-2', 'formula-ct-000-4'):
        a = h.find('id="%s"' % sid)
        if a < 0: E.append(('S8 không thấy mục', sid)); continue
        b = h.find('<section', a + 10); s = h[a:b if b > 0 else len(h)]
        for t in re.findall(r'<table[^>]*>(.*?)</table>', s, re.S):
            th = re.search(r'<thead>(.*?)</thead>', t, re.S)
            if not th: continue
            nh = len(re.findall(r'<th[ >]', th.group(1))) + sum(int(x) - 1 for x in re.findall(r'colspan="(\d+)"', th.group(1)))
            m = re.search(r'<caption>(.*?)</caption>', t, re.S); cap = re.sub(r'<[^>]+>', '', m.group(1))[:40] if m else '?'
            bd = re.search(r'<tbody>(.*?)</tbody>', t, re.S); da += 1
            for r in re.findall(r'<tr>(.*?)</tr>', bd.group(1) if bd else '', re.S):
                n = len(re.findall(r'<td[ >]', r)) + sum(int(x) - 1 for x in re.findall(r'<td[^>]*colspan="(\d+)"', r))
                if n == 0: continue
                if n != nh: E.append(('S8 lệch cột', sid, cap, nh, n, re.sub(r'<[^>]+>', '', r)[:50]))
    return E, da

def main():
    global KB_CHON, GIOI
    a = sys.argv[1:]
    if '--gioi' in a: GIOI = int(a[a.index('--gioi') + 1])
    path = a[a.index('--trang') + 1] if '--trang' in a else TRANG
    if '--kb' in a: KB_CHON = set(a[a.index('--kb') + 1].split(','))
    t0 = time.time()
    try:
        h = open(path, encoding='utf-8').read()
        T = cat_bang(h)
        E, S = kiem_het(T, in_ra=True)
    except SaiKhuon as e:
        print('SAI KHUÔN:', e); sys.exit(2)
    e8, n8 = kiem_cau_truc(h); E = e8 + E
    xet = [k for k, _ in KICH_BAN if not KB_CHON or k in KB_CHON]; bo = [k for k, _ in KICH_BAN if k not in xet]
    print('BẢNG: %d trạng thái · %d dòng chuyển · %d cặp trạng thái×giá trị · %d thao tác · %d bất biến · %d ca · %d/%d kịch bản · %d bảng kiểm cấu trúc' % (
        len(S['ST']), len(T['Bảng Chuyển trạng thái']), len([k for k in S['idx'] if S['idx'][k]]), len(S['OPS']), len(S['INV']), len(CA), len(xet), len(KICH_BAN), n8))
    if bo: print('  ⚠ KHÔNG xét (phần này chưa kết luận):', ', '.join(bo))
    chua = [e for e in E if 'INCONCLUSIVE' in repr(e)]; loi = [e for e in E if e not in chua]
    for e in loi[:80]: print('  ✗', e)
    for e in chua: print('  ⏳', e)
    print('LỖI XÁC ĐỊNH: %d · CHƯA KẾT LUẬN: %d · %.0f giây' % (len(loi), len(chua), time.time() - t0))
    kq = collections.OrderedDict((k, []) for k in ('KILLED', 'SURVIVED', 'INCONCLUSIVE', 'CHECKER_ERROR'))
    if '--dot-bien' in a:
        if loi or chua:
            print('ĐỘT BIẾN: chưa chạy — bản gốc chưa sạch thì kết quả đột biến không có nghĩa')
        else:
            for ten, T2 in dot_bien(T):
                if T2 is None: kq['CHECKER_ERROR'].append((ten, 'không áp được đột biến')); continue
                try:
                    e, _ = kiem_het(T2, nhanh=True)
                except SaiKhuon as x:
                    e = [('sai khuôn', str(x))]
                except Exception as x:
                    kq['CHECKER_ERROR'].append((ten, repr(x)[:160])); continue
                if not e: kq['SURVIVED'].append((ten, ''))
                elif any('INCONCLUSIVE' in repr(x) for x in e): kq['INCONCLUSIVE'].append((ten, repr(e[0])[:160]))
                else: kq['KILLED'].append((ten, repr(e[0])[:200]))
            print('ĐỘT BIẾN: ' + ' · '.join('%s %d' % (k, len(v)) for k, v in kq.items()) + ' · %.0f giây' % (time.time() - t0))
            for k in ('SURVIVED', 'INCONCLUSIVE', 'CHECKER_ERROR'):
                for t, why in kq[k]: print('  ☠' if k == 'SURVIVED' else '  ⏳', k, t, why)
    ma = 1 if (loi or kq['SURVIVED']) else (2 if (chua or bo or kq['INCONCLUSIVE'] or kq['CHECKER_ERROR']) else 0)
    if ma == 0 and '--dot-bien' not in a: print('  ℹ chưa chạy --dot-bien: chưa đủ điều kiện đưa duyệt')
    print('MÃ THOÁT:', ma, {0: 'ĐẠT trong phạm vi đã khai', 1: 'CÒN LỖI', 2: 'CHƯA KẾT LUẬN (không phải đạt)'}[ma])
    if '--json' in a:
        with open(a[a.index('--json') + 1], 'w', encoding='utf-8') as f:
            json.dump({'trang': path, 'mã_thoát': ma, 'kịch_bản_xét': xet, 'kịch_bản_bỏ': bo, 'số_ca': len(CA),
                       'lỗi': [list(map(str, e)) for e in loi], 'chưa_kết_luận': [list(map(str, e)) for e in chua],
                       'đột_biến': {k: v for k, v in kq.items()}, 'giây': round(time.time() - t0)}, f, ensure_ascii=False, indent=1)
    sys.exit(ma)

if __name__ == '__main__':
    main()
