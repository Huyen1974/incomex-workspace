import re,html,collections,sys
sys.setrecursionlimit(10000)
h=open('work/mow-mot-moit-mout/ban-duyet.html',encoding='utf-8').read()
a=h.index('id="formula-ct-000-4"'); s=h[a:h.index('</section>',a)]
def table(name):
  i=s.index('head-label">'+name+'<'); t=s[i:s.index('</table>',i)]
  body=re.search(r'<tbody>(.*?)</tbody>',t,re.S).group(1)
  return [[html.unescape(re.sub('<[^>]+>','',c)).strip() for c in re.findall(r'<td[^>]*>(.*?)</td>',r,re.S)] for r in re.findall(r'<tr>(.*?)</tr>',body,re.S)]
def expand(cell):
  out=[]
  for part in cell.split(' + '):
    m=re.match(r'(.*?)\s*\[(\w): ([^\]]+)\]$',part.strip())
    if m:
      base,var,vals=m.groups()
      for v in [x.strip() for x in vals.split(',')]: out.append((base.replace('{'+var+'}',v),{var:v}))
    else: out.append((part.strip(),{}))
  return out
ST={}
for c in table('Bảng Trạng thái'):
  dom={}
  if c[4] not in ('—',''):
    for seg in c[4].split(' ; '):
      ev,vals=seg.split(': ',1); dom[ev.strip()]=[v.strip() for v in vals.split(' / ')]
  for name,b in expand(c[0]): ST[name]=dict(kind=c[1],holder=c[2],check=c[3],dom=dom)
term={n for n,v in ST.items() if v['kind']=='kết thúc'}; nonterm=[n for n in ST if n not in term]
TT=table('Bảng Chuyển trạng thái'); ROWS=[]
for tid,frm,ev,vals,act,to in TT:
  if frm.startswith('*'):
    exc=[x.strip() for x in frm.split('trừ',1)[1].split(',')] if 'trừ' in frm else []
    froms=[(n,{}) for n in nonterm if n not in exc]
  else: froms=expand(frm)
  for f,b in froms:
    for v in [x.strip() for x in vals.split(' / ')]:
      t=to
      for k,val in b.items(): t=t.replace('{'+k+'}',val)
      tg=[f] if t=='(giữ nguyên)' else (['Chấm G1','Chấm G2','Chấm G4','Chấm G5'] if '[bước trở lại]' in t else [t])
      ROWS.append(dict(id=tid,frm=f,ev=ev,val=v,act=act,to=tg,bound=bool(re.search(r'(lần nhận|vòng) \+1|trần',act))))
glob=set(c[2] for c in TT if c[1].startswith('*')); HUMAN={'yêu cầu huỷ','trả lời','quyết định'}
err=[]; idx=collections.defaultdict(list)
for r in ROWS: idx[(r['frm'],r['ev'],r['val'])].append(r['id'])
def evs(n):
  e=dict(ST[n]['dom'])
  for g in glob: e.setdefault(g,['ok'])
  return e
for n in nonterm:
  for ev,vals in evs(n).items():
    for v in vals:
      if len(idx[(n,ev,v)])!=1: err.append(('1',n,ev,v,idx[(n,ev,v)]))
for (n,ev,v),ids in list(idx.items()):
  if ids and (n not in ST or n in term or ev not in evs(n) or v not in evs(n)[ev]): err.append(('1b',n,ev,v,ids))
E=[]
for r in ROWS:
  for t in r['to']:
    if t not in ST: err.append(('2',r['id'],t))
    else: E.append((r['frm'],t,r['bound'],r['id'],r['ev']))
G=collections.defaultdict(set); R=collections.defaultdict(set)
for e in E: G[e[0]].add(e[1]); R[e[1]].add(e[0])
seen={'Mới'}; st=['Mới']
while st:
  x=st.pop()
  for y in G[x]:
    if y not in seen: seen.add(y); st.append(y)
err+=[('3',n) for n in ST if n not in seen]
ok=set(term); st=list(term)
while st:
  x=st.pop()
  for y in R[x]:
    if y not in ok: ok.add(y); st.append(y)
err+=[('4',n) for n in nonterm if n not in ok]
def sccs(nodes,edges):
  adj=collections.defaultdict(list)
  for e in edges: adj[e[0]].append(e[1])
  index={};low={};stack=[];on=set();res=[];i=[0]
  def sc(v):
    index[v]=low[v]=i[0]; i[0]+=1; stack.append(v); on.add(v)
    for w in adj[v]:
      if w not in index: sc(w); low[v]=min(low[v],low[w])
      elif w in on: low[v]=min(low[v],index[w])
    if low[v]==index[v]:
      comp=set()
      while True:
        w=stack.pop(); on.discard(w); comp.add(w)
        if w==v: break
      res.append(comp)
  for v in nodes:
    if v not in index: sc(v)
  return res
mach={n for n in ST if ST[n]['kind'] in ('tạm','máy')}
unb=[e for e in E if e[0] in mach and e[1] in mach and not e[2] and e[4] not in HUMAN]
for comp in sccs(mach,unb):
  inner=[e[3] for e in unb if e[0] in comp and e[1] in comp]
  if inner: err.append(('5',sorted(comp),sorted(set(inner))))
for n in nonterm:
  if ST[n]['holder'] in ('','—') or ST[n]['check'] in ('','—'): err.append(('6',n))
  if ST[n]['kind']=='chờ' and not any(e in ST[n]['dom'] for e in ('đến lúc kiểm','kiểm lại','quyết định')): err.append(('6b',n))
print('TRẠNG THÁI',len(ST),'· DÒNG',len(TT),'· LỖI',len(err))
for e in err: print('  ',e)
def run(stt,steps,ctx):
  path=[stt]
  for ev,val in steps:
    if ev=='xin nhận' and val is None: val='hết M' if ctx['lan']>=ctx['M'] else 'được'
    ids=idx.get((stt,ev,val),[])
    if len(ids)!=1: return None,path+['KẸT %s|%s=%s'%(stt,ev,val)]
    r=[x for x in ROWS if x['id']==ids[0] and x['frm']==stt and x['ev']==ev and x['val']==val][0]
    if 'lần nhận +1' in r['act']: ctx['lan']+=1
    stt=r['to'][0] if len(r['to'])==1 else ctx['trolai']; path.append(r['id']+'→'+stt)
  return stt,path
TR=[
('1 bình thường','Mới',[('khai xong','ok'),('chấm','đủ'),('chấm','đủ'),('xin nhận',None),('kết quả','Đạt'),('chấm','đủ'),('chấm','đủ')],'Kết thúc·Đạt',{},None),
('2 M=1','Chờ',[('xin nhận',None),('kết quả','Lỗi tạm an toàn'),('xin nhận',None)],'Chờ ĐK·G2',{'M':1},'Đang chạy'),
('3 B hoặc C','Chờ ĐK·G2',[('kiểm lại','còn chờ'),('kiểm lại','thoả'),('chấm','đủ')],'Chờ',{},None),
('4 chờ nghiệm thu','Chấm G4',[('chấm','chờ người'),('đến lúc kiểm','chưa quá'),('trả lời','có'),('chấm','đủ')],'Chấm G5',{},None),
('5 G5 lỗi trước','Chấm G5',[('chấm','lỗi')],'Chờ ĐK·G5',{},None),
('6 gửi rồi chết','Đang chạy',[('hết hạn giữ','có dở'),('đối soát','không kết luận'),('trả lời','có'),('đối soát','đủ')],'Chấm G4',{},None),
('7 chưa thấy','Đang chạy',[('kết quả','Lỗi tạm không an toàn'),('đối soát','không kết luận'),('đến lúc kiểm','quá hạn PH')],'Chờ ĐK·ĐS·TT',{},None),
('8 huỷ khi lệnh chưa rõ','Đang chạy',[('yêu cầu huỷ','ok'),('xét','có dở'),('đối soát','đủ'),('bù','xong')],'Kết thúc·Huỷ',{},'!Chấm G4'),
('9 huỷ sau hạn','Chờ',[('đến lúc kiểm','quá hạn gốc'),('quá hạn','không dở'),('quyết định','huỷ'),('xét','có tác động'),('bù','xong')],'Kết thúc·Huỷ',{},None),
('10 đến giờ không mồ côi','Chờ ĐK·G2',[('kiểm lại','còn chờ'),('kiểm lại','còn chờ')],'Chờ ĐK·G2',{},None),
('11 miễn 1 câu','Chấm G4',[('chấm','sai, hết vòng'),('quyết định','ngoại lệ'),('chấm','sai, hết vòng')],'Chờ Owner',{'trolai':'Chấm G4'},'!Chấm G5'),
('12 lỗi điều kiện','Đang chạy',[('kết quả','Lỗi điều kiện'),('kiểm lại','thoả'),('chấm','đủ')],'Chờ',{},None),
('13 quá hạn rồi huỷ','Quá hạn',[('quá hạn','có dở'),('đối soát','không kết luận'),('yêu cầu huỷ','ok'),('xét','có dở'),('đối soát','đủ'),('bù','xong')],'Kết thúc·Huỷ',{},None),
('14 chết 2 lần, M=2','Chờ',[('xin nhận',None),('hết hạn giữ','không dở'),('xin nhận',None),('hết hạn giữ','không dở'),('xin nhận',None)],'Chờ ĐK·G2',{'M':2},None),
]
np=0
for name,start,steps,exp,ctx,need in TR:
  c=dict(lan=0,M=99); c.update(ctx); end,path=run(start,steps,c); okk=(end==exp)
  if need and need.startswith('!'): okk=okk and not any(p.endswith('→'+need[1:]) for p in path)
  elif need: okk=okk and any(p.endswith('→'+need) for p in path)
  np+=okk; print(('ĐẠT ' if okk else 'TRƯỢT ')+name+' :: '+' · '.join(path))
print('CA THỬ ĐẠT',np,'/',len(TR))
