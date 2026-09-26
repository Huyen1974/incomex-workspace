#!/usr/bin/env python3
# ==== CÔNG CỤ QUY TRÌNH · nguồn chuẩn: GitHub incomex-workspace · work/mow-mot-moit-mout/cong-cu/ ====
# Mã:           dot-page-shot   (dòng trong 🛠 của ban-duyet.html · sổ công cụ = dòng 35 CAT-006 · chưa đăng ký dot_tools)
# Thuộc:        🔁 Chung — Nhà máy xem trước trang Owner duyệt; Máy có thể dùng lại để xem trước UI của quy trình thương mại
# Phạm vi kiểm: K05 · workspace.view · verify (trước khi ghi, trên bản dự kiến) · loại A (chỉ đọc, chỉ ghi ảnh cục bộ)
# Việc:         Dựng trang HTML offline bằng Chromium không màn hình, ở từng bề ngang (mặc định máy tính 1280 + điện thoại 390):
#               bấm phần tử nếu cần (vd mở tab) → kiểm từng vùng bắt buộc có và cao > 0 → chụp vùng nếu yêu cầu → bắt lỗi JS.
#               Bổ trợ cho ui_screenshot của cổng (chụp trang THẬT sau khi ghi); công cụ này chạy TRƯỚC khi ghi.
# Đầu vào:      tệp HTML · --click SEL · --need SEL (lặp được) · --shot SEL=tệp.png (lặp được) · --widths 1280,390
# Đầu ra:       vị trí từng vùng, số lỗi JS · exit 0 = 0 lỗi JS và đủ vùng · 1 = có lỗi · 2 = không mở được trình duyệt/tệp
# Cách chạy:    python3 dot-page-shot.py ban-duyet.html --click '#matrix-tab-master-lists' --need '#ml6-nha-may' --need '#ml5-cho-ai'
# Cần:          Python ≥ 3.8 + playwright (pip install playwright; playwright install chromium) — sandbox Cowork có sẵn
# Ca thử:       ban-duyet.html ở commit "MMIM-C12" · --click '#matrix-tab-master-lists' --need '#ml6-nha-may' --need '#ml6-cc'
#               --need '#ml6-phu' --need '#ml5-walk' --need '#ml5-cho-ai'
# Kết quả mong đợi: mỗi bề ngang 5/5 vùng · lỗi JS 0 · exit 0
# Nguồn gốc:    dựng lại từ shot_c10.py / shot_c11.py phiên Cowork 26/09: giữ cách bấm tab + đo vùng + bắt pageerror;
#               bỏ tên vùng cứng, nhận tham số.
# Luật:         theo TEMPLATE-DOT-SCRIPT: không đường dẫn cứng, exit 0/1. Không tạo bản xem trên VPS (AGENTS A8).
# Chép lên VPS: chỉ khi phải chạy ở đó · theo lệnh · ghi sha256 + nguồn@commit vào sổ công cụ · không sửa bản chép.
import asyncio, json, os, sys


def parse(argv):
    o = {'click': None, 'need': [], 'shot': [], 'widths': '1280,390', 'page': None, 'wait': '800'}
    it = iter(argv)
    for a in it:
        if a in ('--click', '--widths', '--wait'):
            o[a[2:]] = next(it, None)
        elif a in ('--need', '--shot'):
            o[a[2:]].append(next(it, None))
        else:
            o['page'] = a
    return o


async def run(o):
    from playwright.async_api import async_playwright
    bad = 0
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for w in [int(x) for x in o['widths'].split(',')]:
            errs = []
            pg = await b.new_page(viewport={'width': w, 'height': 900})
            pg.on('pageerror', lambda e, errs=errs: errs.append(str(e)))
            await pg.goto('file://' + os.path.abspath(o['page']))
            await pg.wait_for_timeout(int(o['wait']))
            if o['click']:
                await pg.evaluate('(s)=>{const t=document.querySelector(s); if(t) t.click();}', o['click'])
                await pg.wait_for_timeout(500)
            found = 0
            for sel in o['need']:
                box = await pg.evaluate('(s)=>{const e=document.querySelector(s); if(!e) return null;'
                                        'const r=e.getBoundingClientRect(); return [Math.round(r.top+scrollY), Math.round(r.height)]}', sel)
                ok = bool(box and box[1] > 0)
                found += ok
                print('  %4d px · %-22s %s' % (w, sel, ('y=%d cao=%d' % tuple(box)) if box else 'KHÔNG CÓ'))
            for spec in o['shot']:
                sel, _, name = spec.partition('=')
                box = await pg.evaluate('(s)=>{const e=document.querySelector(s); if(!e) return null;'
                                        'const r=e.getBoundingClientRect(); return [r.top+scrollY, r.height]}', sel)
                if box:
                    root, ext = os.path.splitext(name or 'shot.png')
                    await pg.screenshot(path='%s-%d%s' % (root, w, ext or '.png'), full_page=True,
                                        clip={'x': 0, 'y': max(0, box[0] - 8), 'width': w, 'height': min(box[1] + 16, 6000)})
            print('%4d px · vùng %d/%d · lỗi JS %d%s' % (w, found, len(o['need']), len(errs),
                                                      (' · ' + json.dumps(errs[:3], ensure_ascii=False)) if errs else ''))
            bad += len(errs) + (len(o['need']) - found)
            await pg.close()
        await b.close()
    return bad


def main(argv):
    o = parse(argv)
    if not o['page'] or not os.path.exists(o['page']):
        print('cách chạy: python3 dot-page-shot.py TRANG.html [--click SEL] [--need SEL]… [--shot SEL=tệp.png]… [--widths 1280,390]')
        return 2
    try:
        bad = asyncio.run(run(o))
    except Exception as e:  # noqa: BLE001
        print('KHÔNG MỞ ĐƯỢC TRÌNH DUYỆT/TRANG:', e)
        return 2
    print('KẾT QUẢ:', 'ĐẠT' if bad == 0 else 'CÓ LỖI')
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
