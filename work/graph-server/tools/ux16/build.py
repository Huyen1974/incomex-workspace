# Dựng lại bundle từ bản sao lưu byte-exact + 1 dòng hook + bảng hướng dẫn (lặp lại được)
import sys
B='/Users/nmhuyen/Incomex-Graph-View/ux16/backup/index-CWSVxO7S.js.truoc'
OUT='/Users/nmhuyen/Incomex-Graph-View/app/gephi-lite/v1.0.2/assets/index-CWSVxO7S.js'
s=open(B,encoding='utf-8').read(); g=open(sys.argv[1],encoding='utf-8').read().strip('\n')
old=';tze.render(y.jsx(me.StrictMode'; assert s.count(old)==1
s=s.replace(old,';window.__incomexGL={Ci:Ci,ok:ok,VK:VK,focus:bve};tze.render(y.jsx(me.StrictMode')
t='export default nze();\n'; assert s.count(t)==1
s=s.replace(t,t+g+'\n')
open(OUT,'w',encoding='utf-8').write(s); print('built')
