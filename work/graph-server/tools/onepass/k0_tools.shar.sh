#!/bin/sh
# K0 — bộ đọc nguồn + oracle GS-COV2-K0-LIVE-SOURCE-ORACLE-20261030-01 (P-ONEPASS-HOST-B12 F3). Giữ NGUYÊN BYTE 11 tệp nguồn trong một tệp văn bản.
# Chỉ chứa mã công cụ: 0 dữ liệu nguồn, 0 bí mật (trufflehog + mẫu riêng 31/10). Xem README.md cùng thư mục.
# Giải nén: sh k0_tools.shar.sh <thư mục mới>   (tự kiểm sha256 từng tệp)
set -eu
D=${1:?thu muc dich}; mkdir -p "$D"; cd "$D"
cat > k0_catalog.sql <<'__K0_EOF__'
\pset format unaligned
\pset fieldsep '\t'
\pset tuples_only on
begin transaction isolation level repeatable read read only;
set local statement_timeout='60s';
select 'meta',current_database(),current_user,now(),version(),pg_current_wal_lsn()::text,(select system_identifier from pg_control_system());
select 'schema',n.nspname from pg_namespace n where n.nspname !~ '^pg_' and n.nspname<>'information_schema' order by 2;
with extm as (select objid,classid from pg_depend where deptype='e')
select 'rel',c.relkind,n.nspname,c.relname,pg_get_userbyid(c.relowner),
 (exists(select 1 from extm e where e.objid=c.oid and e.classid='pg_class'::regclass))::text,
 md5(coalesce((select string_agg(a.attname||':'||format_type(a.atttypid,a.atttypmod)||':'||a.attnotnull,',' order by a.attnum) from pg_attribute a where a.attrelid=c.oid and a.attnum>0 and not a.attisdropped),'')),
 c.reltuples::bigint,(select count(*) from pg_attribute a where a.attrelid=c.oid and a.attnum>0 and not a.attisdropped),c.relrowsecurity::text
from pg_class c join pg_namespace n on n.oid=c.relnamespace
where n.nspname !~ '^pg_' and n.nspname<>'information_schema' and c.relkind in ('r','p','v','m','f','S','i','I','c') order by 2,3,4;
with extm as (select objid from pg_depend where deptype='e' and classid='pg_proc'::regclass)
select 'func',n.nspname,p.proname,pg_get_function_identity_arguments(p.oid),l.lanname,p.provolatile,p.prokind,md5(coalesce(p.prosrc,'')),(p.oid in (select objid from extm))::text,pg_get_userbyid(p.proowner),p.prosecdef::text,pg_catalog.oidvectortypes(p.proargtypes)
from pg_proc p join pg_namespace n on n.oid=p.pronamespace join pg_language l on l.oid=p.prolang
where n.nspname !~ '^pg_' and n.nspname<>'information_schema' order by 2,3,4;
select 'trigger',n.nspname,c.relname,t.tgname,t.tgenabled,fn.nspname,f.proname,pg_get_function_identity_arguments(f.oid)
from pg_trigger t join pg_class c on c.oid=t.tgrelid join pg_namespace n on n.oid=c.relnamespace join pg_proc f on f.oid=t.tgfoid join pg_namespace fn on fn.oid=f.pronamespace
where not t.tgisinternal order by 2,3,4;
select 'evttrigger',e.evtname,e.evtevent,e.evtenabled,f.proname from pg_event_trigger e join pg_proc f on f.oid=e.evtfoid order by 2;
select 'fk',n.nspname,c.relname,k.conname,fn.nspname,fc.relname,k.convalidated::text
from pg_constraint k join pg_class c on c.oid=k.conrelid join pg_namespace n on n.oid=c.relnamespace join pg_class fc on fc.oid=k.confrelid join pg_namespace fn on fn.oid=fc.relnamespace
where k.contype='f' order by 2,3,4;
select 'constraint',k.contype,n.nspname,c.relname,k.conname
from pg_constraint k join pg_class c on c.oid=k.conrelid join pg_namespace n on n.oid=c.relnamespace
where k.contype<>'f' and n.nspname !~ '^pg_' and n.nspname<>'information_schema' order by 3,4,5;
select distinct 'viewdep',vn.nspname,v.relname,v.relkind,rn.nspname,r.relname,r.relkind
from pg_rewrite w join pg_class v on v.oid=w.ev_class join pg_namespace vn on vn.oid=v.relnamespace
join pg_depend d on d.objid=w.oid and d.classid='pg_rewrite'::regclass and d.refclassid='pg_class'::regclass and d.deptype='n'
join pg_class r on r.oid=d.refobjid join pg_namespace rn on rn.oid=r.relnamespace
where r.oid<>v.oid and vn.nspname !~ '^pg_' and vn.nspname<>'information_schema' order by 2,3,5,6;
select distinct 'viewfunc',vn.nspname,v.relname,fn.nspname,f.proname
from pg_rewrite w join pg_class v on v.oid=w.ev_class join pg_namespace vn on vn.oid=v.relnamespace
join pg_depend d on d.objid=w.oid and d.classid='pg_rewrite'::regclass and d.refclassid='pg_proc'::regclass and d.deptype='n'
join pg_proc f on f.oid=d.refobjid join pg_namespace fn on fn.oid=f.pronamespace
where vn.nspname !~ '^pg_' and vn.nspname<>'information_schema' and fn.nspname<>'pg_catalog' order by 2,3,4,5;
select 'extension',x.extname,x.extversion,n.nspname,pg_get_userbyid(x.extowner) from pg_extension x join pg_namespace n on n.oid=x.extnamespace order by 2;
select 'fdwserver',s.srvname,w.fdwname from pg_foreign_server s join pg_foreign_data_wrapper w on w.oid=s.srvfdw order by 2;
select 'ftable',n.nspname,c.relname,s.srvname from pg_foreign_table f join pg_class c on c.oid=f.ftrelid join pg_namespace n on n.oid=c.relnamespace join pg_foreign_server s on s.oid=f.ftserver order by 2,3;
select 'rule',n.nspname,c.relname,r.rulename from pg_rewrite r join pg_class c on c.oid=r.ev_class join pg_namespace n on n.oid=c.relnamespace where r.rulename<>'_RETURN' order by 2,3,4;
select 'rlspolicy',n.nspname,c.relname,p.polname from pg_policy p join pg_class c on c.oid=p.polrelid join pg_namespace n on n.oid=c.relnamespace order by 2,3,4;
select 'publication',pubname from pg_publication order by 2;
select 'subscription_count',count(*) from pg_stat_subscription;
select 'depcount',classid::regclass::text,refclassid::regclass::text,deptype,count(*) from pg_depend group by 2,3,4 order by 2,3,4;
select 'shdepcount',classid::regclass::text,refclassid::regclass::text,deptype,count(*) from pg_shdepend where dbid in (0,(select oid from pg_database where datname=current_database())) group by 2,3,4 order by 2,3,4;
commit;
__K0_EOF__
cat > k0_derived.py <<'__K0_EOF__'
#!/usr/bin/env python3
# G5: quan hệ từ thân hàm = STATIC_DERIVED, thân hàm không rời VPS; chỉ in cặp (hàm, bảng) và cờ EXECUTE động.
import json,re,subprocess,sys
RO=sys.argv[1]; out=open(sys.argv[2],'w'); tot={}
for db in sys.argv[3:]:
    sql="""select json_build_object('f',n.nspname||'.'||p.proname||'('||pg_get_function_identity_arguments(p.oid)||')','s',p.prosrc,'l',l.lanname) from pg_proc p join pg_namespace n on n.oid=p.pronamespace join pg_language l on l.oid=p.prolang where n.nspname !~ '^pg_' and n.nspname<>'information_schema' and l.lanname in ('plpgsql','sql') and p.oid not in (select objid from pg_depend where deptype='e' and classid='pg_proc'::regclass)"""
    tbl="select n.nspname,c.relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where c.relkind in ('r','p','f','v','m') and n.nspname !~ '^pg_' and n.nspname<>'information_schema'"
    run=lambda q:subprocess.run(['docker','exec','-i','-e','PGOPTIONS=-c default_transaction_read_only=on -c statement_timeout=30000','postgres','psql','-XAtq','-F','\t','-U',RO,'-d',db,'-c',q],capture_output=True,text=True,check=True).stdout
    tb=[l.split('\t') for l in run(tbl).splitlines()]; names={}
    for s,n in tb: names.setdefault(n,[]).append(s)
    fs=[json.loads(l) for l in run(sql).splitlines() if l.strip()]
    pat=re.compile(r'\b(%s)\b'%'|'.join(sorted(map(re.escape,names),key=len,reverse=True))) if names else None
    e=0; dyn=0
    for f in fs:
        d=bool(re.search(r'\bEXECUTE\b',f['s'],re.I)); dyn+=d
        for n in sorted(set(pat.findall(f['s']))) if pat else []:
            for s in names[n]:
                out.write(json.dumps({'db':db,'f':f['f'],'r':s+'.'+n,'t':'REFERS_IN_BODY','dyn':d},ensure_ascii=False)+'\n'); e+=1
    tot[db]={'functions':len(fs),'edges':e,'with_execute':dyn}
print(json.dumps(tot))
__K0_EOF__
cat > k0_directus_table.sql <<'__K0_EOF__'
\pset format unaligned
\pset fieldsep '\t'
\pset tuples_only on
begin transaction isolation level repeatable read read only;
set local statement_timeout='30s';
select 'dcol',collection,coalesce("group",''),coalesce(singleton::text,''),hidden::text from directus_collections order by 2;
select 'dfield',collection,field,coalesce(interface,'') from directus_fields order by 2,3;
select 'drel',many_collection,many_field,coalesce(one_collection,''),coalesce(one_field,'') from directus_relations order by 2,3;
select 'dflow',id,name,status,coalesce(trigger,''),coalesce(accountability,''),coalesce(date_created::text,''),md5(coalesce(options::text,'')) from directus_flows order by 2,3;
select 'dop',id,flow,type,key,md5(coalesce(options::text,'')),coalesce(resolve::text,''),coalesce(reject::text,'') from directus_operations order by 3,5;
select 'dpolicy',id,name,admin_access::text,app_access::text from directus_policies order by 3,2;
select 'drole',id,name from directus_roles order by 3,2;
select 'daccess',id,coalesce(role::text,''),coalesce("user"::text,''),policy from directus_access order by 2;
select 'dperm',id,collection,action,policy,md5(coalesce(permissions::text,'')||coalesce(validation::text,'')||coalesce(fields,'')||coalesce(presets::text,'')) from directus_permissions order by 3,4,2;
select 'dcount',t,c from (values ('directus_presets',(select count(*) from directus_presets)),('directus_settings',(select count(*) from directus_settings)),('directus_users',(select count(*) from directus_users)),('directus_activity',(select count(*) from directus_activity)),('directus_revisions',(select count(*) from directus_revisions)),('directus_webhooks_absent',0)) v(t,c);
select 'dwindow','activity',min("timestamp"),max("timestamp") from directus_activity;
select 'dflowact',a.item,count(*),max(a."timestamp") from directus_activity a where a.collection='directus_flows' group by 2 order by 2;
commit;
__K0_EOF__
cat > k0_fixtures.py <<'__K0_EOF__'
#!/usr/bin/env python3
# K2: lỗi bộ đọc/ACL/timeout/phân trang/xoá/thêm/tắt trên BẢN SAO ảnh T1 trong thư mục tạm; không chạm production.
import json,os,re,shutil,subprocess,sys,tempfile
E,TOOL,G,PREV=sys.argv[1:5]; R=[]
def case(name,mut,check):
    d=tempfile.mkdtemp(); t=os.path.join(d,'t'); shutil.copytree(E,t); o=os.path.join(d,'o')
    mut(t); p=subprocess.run([sys.executable,'-B',TOOL,t,'T1',G,o,'--prev',PREV],capture_output=True,text=True)
    if p.returncode: R.append((name,'CRASH',p.stderr[-160:]))
    else:
        s=json.load(open(os.path.join(o,'summary-T1.json'))); rc=json.load(open(os.path.join(o,'reconcile-T1.json'))); ok,obs=check(s,rc); R.append((name,'PASS' if ok else 'FAIL',obs))
    shutil.rmtree(d)
def edit(t,f,fn):
    p=os.path.join(t,f); b=open(p,encoding='utf-8',errors='replace').read(); n=fn(b); assert n!=b,f; open(p,'w',encoding='utf-8').write(n)
P=lambda s,_:(s['verdict']=='PARTIAL' and bool(s['reader_errors']),str(s['reader_errors'])[:110])
case('reader fail: mất TOC directus',lambda t:os.remove(os.path.join(t,'toc-T1-directus.txt')),P)
case('reader fail: TOC rỗng rc=0',lambda t:open(os.path.join(t,'toc-T1-workflow.txt'),'w').close(),P)
case('ACL: catalog bị từ chối',lambda t:open(os.path.join(t,'cat-directus.err'),'w').write('ERROR: permission denied for table pg_proc\n'),P)
case('timeout/cắt cụt: TOC mất 500 dòng',lambda t:edit(t,'toc-T1-directus.txt',lambda b:'\n'.join(b.split('\n')[:-500])),P)
case('phân trang/cắt: snapshot Directus JSON cụt',lambda t:edit(t,'directus-schema-T1.json',lambda b:b[:len(b)//2]),P)
case('runtime: nginx -T lỗi',lambda t:edit(t,'runtime-T1.json',lambda b:b.replace('"errors": []','"errors": [{"where":"nginx-T","rc":1,"stderr":""}]',1)),P)
case('TOC có TABLE DATA (rò dữ liệu)',lambda t:edit(t,'toc-T1-workflow.txt',lambda b:b+'9999; 0 16999 TABLE DATA public x owner\n'),lambda s,_:(s['forbidden_toc'].get('TABLE DATA')==1 and s['verdict']=='PARTIAL',str(s['forbidden_toc'])+s['verdict']))
case('loại mới chưa biết',lambda t:edit(t,'toc-T1-workflow.txt',lambda b:b+'9998; 1 1 STATISTICS public st owner\n'),lambda s,_:(any('STATISTICS' in k for k in s['new_class_unhandled']) and s['verdict']=='PARTIAL',str(s['new_class_unhandled'])))
def rmrow(t):
    edit(t,'cat-T1-directus.tsv',lambda b:re.sub(r'(?m)^rel\tr\tpublic\ttai_san_luat\t.*\n','',b))
case('xoá bảng trên bản sao ⇒ REMOVE',rmrow,lambda s,r:('pg:directus:table:public.tai_san_luat' in r['REMOVE'],'REMOVE=%d'%len(r['REMOVE'])))
case('thêm bảng ⇒ ADD',lambda t:edit(t,'cat-T1-workflow.tsv',lambda b:b+'rel\tr\tpublic\tzz_moi\towner\tfalse\tabc\t0\t1\tfalse\n'),lambda s,r:('pg:workflow:table:public.zz_moi' in r['ADD'],'ADD=%d'%len(r['ADD'])))
def trg(t):
    edit(t,'cat-T1-directus.tsv',lambda b:re.sub(r'(?m)^(trigger\tpublic\tpivot_definitions\ttrg_after_pivot_definitions_change\t)O','\\1D',b))
case('tắt trigger ⇒ CHANGE+DISABLED',trg,lambda s,r:(any('trg_after_pivot_definitions_change' in x for x in r['DISABLED']),'DIS=%d CHG=%d'%(len(r['DISABLED']),len(r['CHANGE']))))
def cron(t):
    d=json.load(open(os.path.join(t,'runtime-T1.json')))
    x=next(c for c in d['cron'] if not c['disabled']); x['disabled']=True; json.dump(d,open(os.path.join(t,'runtime-T1.json'),'w'))
case('tắt dòng cron ⇒ DISABLED không phải REMOVE',cron,lambda s,r:(len(r['DISABLED'])==1 and not [x for x in r['REMOVE'] if x.startswith('cron:')],'DIS=%d'%len(r['DISABLED'])))
def fl(t):
    edit(t,'dt-T1.tsv',lambda b:re.sub(r'(?m)^(dflow\t\S+\t[^\t]*\t)active\t','\\1inactive\t',b,count=1))
case('tắt flow ⇒ DISABLED',fl,lambda s,r:(len(r['DISABLED'])>=1,'DIS=%d'%len(r['DISABLED'])))
case('không đổi gì ⇒ 0 sự kiện',lambda t:None,lambda s,r:(not any(r[k] for k in('ADD','REMOVE','CHANGE','DISABLED')),str({k:len(r[k]) for k in('ADD','REMOVE','CHANGE')})))
for x in R: print(x[1],'·',x[0],'·',x[2])
print('TOTAL',sum(1 for x in R if x[1]=='PASS'),'/',len(R))
json.dump([dict(case=x[0],verdict=x[1],observed=x[2]) for x in R],open(sys.argv[5],'w'),ensure_ascii=False,indent=1)
__K0_EOF__
cat > k0_graph_export.py <<'__K0_EOF__'
#!/usr/bin/env python3
# Đọc Graph production CHỈ ĐỌC (MATCH/RETURN) ra JSON: gs_key, nhãn, lớp, retired, cạnh; không ghi Neo4j.
import sys,json,importlib.machinery,importlib.util,time
sys.dont_write_bytecode=True
l=importlib.machinery.SourceFileLoader('graph_cert_k0','/opt/incomex/graph-server/prod-v1/bin/refresh/graph_cert.py')
s=importlib.util.spec_from_loader(l.name,l); m=importlib.util.module_from_spec(s); sys.modules[l.name]=m; l.exec_module(m)
g,pw=m.load_graph()
at=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
nodes=g.rows(g.http_cypher([("MATCH (n:GS) RETURN n.gs_key AS k, [x IN labels(n) WHERE x<>'GS' AND x<>'__Node__'] AS l, n.gs_layer AS layer, n.gs_status AS st, n.retired_at AS ra, n.enabled_code AS en, n.schema AS sc, n.name AS nm, n.source AS src",{})],pw,timeout=300))
edges=g.rows(g.http_cypher([("MATCH (a:GS)-[x]->(b:GS) RETURN a.gs_key AS s, type(x) AS t, b.gs_key AS d",{})],pw,timeout=300))
print(json.dumps({'at':at,'nodes':nodes,'edges':edges},ensure_ascii=False))
__K0_EOF__
cat > k0_reconcile.py <<'__K0_EOF__'
#!/usr/bin/env python3
"""GS-COV2-K0-LIVE: đối chiếu oracle hãng (pg_restore --list, catalog PG, Directus snapshot, OS) ↔ Graph; dựng ứng viên JSONL/SQLite trên Mac.
Dùng: k0_reconcile.py <dir ảnh T> <tag> <graph.json> <out dir> [--prev <out dir trước>]
Fail-closed: thiếu tệp/rc lỗi/rỗng/cắt cụt của một nguồn ⇒ nguồn đó PARTIAL, không bao giờ PASS. Loại TOC lạ ⇒ NEW_CLASS_UNHANDLED."""
import json,os,re,sys,glob,hashlib,sqlite3,collections
T,TAG,GRAPH,OUT=sys.argv[1:5]; PREV=sys.argv[sys.argv.index('--prev')+1] if '--prev' in sys.argv else None
os.makedirs(OUT,exist_ok=True)
H=lambda it: hashlib.sha256('\n'.join(sorted(it)).encode()).hexdigest()[:16]
errs=collections.defaultdict(list)
def rd(n,src):
    p=os.path.join(T,n)
    if not os.path.exists(p): errs[src].append('MISSING '+n); return None
    if os.path.getsize(p)==0: errs[src].append('EMPTY '+n); return None
    return open(p,encoding='utf-8',errors='replace').read()
def rows(s):
    return [l.split('\t') for l in (s or '').split('\n') if l]
DBS=sorted(re.sub(r'^cat-%s-|\.tsv$'%TAG,'',os.path.basename(p)) for p in glob.glob(os.path.join(T,'cat-%s-*.tsv'%TAG)))
if not DBS: errs['pg'].append('NO_CATALOG')
TYPES=['CHECK CONSTRAINT','FOREIGN DATA WRAPPER','MATERIALIZED VIEW','SEQUENCE OWNED BY','SEQUENCE SET','EVENT TRIGGER','FK CONSTRAINT','FOREIGN TABLE','TABLE ATTACH','INDEX ATTACH','USER MAPPING','ROW SECURITY','TABLE DATA','LARGE OBJECT','TEXT SEARCH CONFIGURATION','TEXT SEARCH DICTIONARY','DEFAULT ACL','ACCESS METHOD','AGGREGATE','CONSTRAINT','EXTENSION','PROCEDURE','FUNCTION','SEQUENCE','DEFAULT','TRIGGER','COMMENT','COLLATION','OPERATOR','PUBLICATION','DOMAIN','POLICY','SCHEMA','SERVER','INDEX','TABLE','TYPE','VIEW','RULE','CAST','ACL','BLOBS']
KNOWN={'CHECK CONSTRAINT','TABLE','VIEW','MATERIALIZED VIEW','FOREIGN TABLE','FUNCTION','PROCEDURE','AGGREGATE','TRIGGER','EVENT TRIGGER','FK CONSTRAINT','CONSTRAINT','INDEX','SEQUENCE','SCHEMA','EXTENSION','SERVER','USER MAPPING','POLICY','RULE','ROW SECURITY','COMMENT','ACL','DEFAULT','SEQUENCE OWNED BY','TABLE ATTACH','INDEX ATTACH','TYPE','DOMAIN','FOREIGN DATA WRAPPER','CAST','COLLATION','OPERATOR','DEFAULT ACL','PUBLICATION'}
FORBID={'TABLE DATA','SEQUENCE SET','BLOBS','LARGE OBJECT'}
def toc(db):
    r=collections.defaultdict(set); unk=collections.Counter(); forb=collections.Counter()
    s=rd('toc-%s-%s.txt'%(TAG,db),'pg:toc:'+db)
    for l in (s or '').split('\n'):
        if not l or l.startswith(';'): continue
        m=re.match(r'^\d+;\s+\d+\s+\d+\s+(.*)$',l)
        if not m: unk['BAD_LINE']+=1; continue
        b=m.group(1); t=next((x for x in TYPES if b.startswith(x+' ')),None)
        if not t: unk[b.split(' ')[0]]+=1; continue
        if t in FORBID: forb[t]+=1
        if t not in KNOWN and t not in FORBID: unk[t]+=1
        rest=b[len(t)+1:].rsplit(' ',1)[0]
        r[t].add(rest)
    if s is not None:
        m=re.search(r'^;\s+TOC Entries: (\d+)$',s,re.M); lines=sum(1 for l in s.split('\n') if l and not l.startswith(';'))
        if not m: errs['pg:toc:'+db].append('TOC_HEADER_MISSING')
        elif not 0<=int(m.group(1))-lines<=10: errs['pg:toc:'+db].append('TOC_TRUNCATED %s!=%s'%(m.group(1),lines))  # 5–6 mục ENCODING/STDSTRINGS/SEARCHPATH/DATABASE… có đếm nhưng --list không in
    te=os.path.join(T,'toce-%s.err'%db)
    if os.path.exists(te) and os.path.getsize(te): errs['pg:toc:'+db].append('PG_RESTORE_STDERR')
    return r,unk,forb
cat={};tocs={};unkall=collections.Counter();forball=collections.Counter()
for db in DBS:
    s=rd('cat-%s-%s.tsv'%(TAG,db),'pg:cat:'+db); e=rd('cat-%s.err'%db,'x') if os.path.exists(os.path.join(T,'cat-%s.err'%db)) and os.path.getsize(os.path.join(T,'cat-%s.err'%db)) else None
    if e: errs['pg:cat:'+db].append('STDERR '+e[:120])
    d=collections.defaultdict(list)
    for f in rows(s): d[f[0]].append(f[1:])
    cat[db]=d
    if s and 'publication' not in s and 'depcount' not in s: errs['pg:cat:'+db].append('CATALOG_TRUNCATED')
    tocs[db],u,fb=toc(db); unkall.update({(db,k):v for k,v in u.items()}); forball.update(fb)
# ---- nút/cạnh native (có db; khoá Graph không có db nên so theo khoá bỏ db + ghi trùng)
N={};E={}
def node(i,cls,src,**a): N[i]=dict(id=i,cls=cls,src=src,prov='EXACT_NATIVE',**a)
def edge(s,t,d,prov='EXACT_NATIVE',src='pg_catalog'): E[(s,t,d)]=dict(s=s,t=t,d=d,prov=prov,src=src)
tvs=[];gmap=collections.defaultdict(list)
for db in DBS:
    c=cat[db]; tc=tocs[db]
    def cmp(name,catset,tocset):
        tvs.append(dict(db=db,cls=name,cat=len(catset),toc=len(tocset),only_cat=sorted(catset-tocset)[:6],only_toc=sorted(tocset-catset)[:6],n_only_cat=len(catset-tocset),n_only_toc=len(tocset-catset),cat_sha=H(catset),toc_sha=H(tocset)))
    rel=[r for r in c['rel'] if r[4]=='false']
    for kind,cls,tt in (('r p','table','TABLE'),('f','foreign_table','FOREIGN TABLE'),('v','view','VIEW'),('m','matview','MATERIALIZED VIEW'),('S','sequence','SEQUENCE')):
        cs=set()
        for r in rel:
            if r[0] in kind.split():
                k=r[1]+' '+r[2]; cs.add(k); node('pg:%s:%s:%s.%s'%(db,cls,r[1],r[2]),cls,'pg:'+db,db=db,hash=r[5],owner=r[3],ncol=r[7],relkind=r[0])
                if cls in('table','foreign_table'): gmap['pg:table:%s.%s'%(r[1],r[2])].append(db)
                if cls in('view','matview'): gmap['pg:view:%s.%s'%(r[1],r[2])].append(db)
        cmp(cls,cs,tc.get(tt,set()))
    fns=[r for r in c['func'] if r[7]=='false']
    cs={'%s %s(%s)'%(r[0],r[1],r[10] if len(r)>10 else r[2]) for r in fns if r[5]!='a'}; ts=tc.get('FUNCTION',set())|tc.get('PROCEDURE',set())
    for r in fns:
        node('pg:%s:function:%s.%s(%s)'%(db,r[0],r[1],r[2]),'function','pg:'+db,db=db,hash=r[6],lang=r[3],vol=r[4],kind=r[5],secdef=r[9])
        gmap['pg:function:%s.%s(%s)'%(r[0],r[1],r[2])].append(db)
    norm=lambda st:{re.sub(r'\((.*)\)$',lambda m:'('+re.sub(r'\s*,\s*',',',m.group(1))+')',x) for x in st}
    cmp('function',norm(cs),norm(ts))
    cs=set()
    for r in c['trigger']:
        cs.add('%s %s %s'%(r[0],r[1],r[2]))
        i='pg:%s:trigger:%s.%s.%s'%(db,r[0],r[1],r[2]); node(i,'trigger','pg:'+db,db=db,enabled=r[3]); gmap['pg:trigger:%s.%s.%s'%(r[0],r[1],r[2])].append(db)
        rk={(x[1],x[2]):x[0] for x in rel}.get((r[0],r[1]),'r'); edge(i,'ON_TABLE','pg:%s:%s:%s.%s'%(db,{'v':'view','m':'matview','f':'foreign_table'}.get(rk,'table'),r[0],r[1])); edge(i,'EXECUTES','pg:%s:function:%s.%s(%s)'%(db,r[4],r[5],r[6]))
    cmp('trigger',cs,tc.get('TRIGGER',set()))
    cs=set()
    for r in c['fk']:
        cs.add('%s %s %s'%(r[0],r[1],r[2])); i='pg:%s:fk:%s.%s.%s'%(db,r[0],r[1],r[2]); node(i,'fk','pg:'+db,db=db,validated=r[5]); gmap['pg:fk:%s.%s.%s'%(r[0],r[1],r[2])].append(db)
        edge('pg:%s:table:%s.%s'%(db,r[0],r[1]),'HAS_FK',i); edge(i,'REFERENCES','pg:%s:table:%s.%s'%(db,r[3],r[4]))
    cmp('fk',cs,tc.get('FK CONSTRAINT',set()))
    # CHECK/NOT NULL nội tuyến nằm trong DDL của TABLE, không thành mục TOC; chỉ so PK/UNIQUE/EXCLUDE + CHECK tách riêng
    tcon=tc.get('CONSTRAINT',set())|tc.get('CHECK CONSTRAINT',set())
    cmp('constraint_pux',{'%s %s %s'%(r[1],r[2],r[3]) for r in c['constraint'] if r[0] in('p','u','x')}|{x for x in tc.get('CHECK CONSTRAINT',set())},tcon)
    cmp('event_trigger',{r[0] for r in c['evttrigger']},{x.replace('- ','',1) for x in tc.get('EVENT TRIGGER',set())})
    for r in c['evttrigger']: node('pg:%s:event_trigger:%s'%(db,r[0]),'event_trigger','pg:'+db,db=db,enabled=r[2])
    cmp('schema',{r[0] for r in c['schema'] if r[0]!='public'},{x.replace('- ','',1) for x in tc.get('SCHEMA',set())})
    for r in c['schema']: node('pg:%s:schema:%s'%(db,r[0]),'schema','pg:'+db,db=db)
    cmp('extension',{r[0] for r in c['extension'] if r[0]!='plpgsql'},{x.replace('- ','',1) for x in tc.get('EXTENSION',set())})
    for r in c['extension']: node('pg:%s:extension:%s'%(db,r[0]),'extension','pg:'+db,db=db,ver=r[1],owner=r[3])
    for r in c['rlspolicy']: node('pg:%s:rls:%s.%s.%s'%(db,r[0],r[1],r[2]),'rls_policy','pg:'+db,db=db)
    for r in c['rule']: node('pg:%s:rule:%s.%s.%s'%(db,r[0],r[1],r[2]),'rule','pg:'+db,db=db)
    for r in c['fdwserver']: node('pg:%s:server:%s'%(db,r[0]),'fdw_server','pg:'+db,db=db)
    for r in c['ftable']: edge('pg:%s:foreign_table:%s.%s'%(db,r[0],r[1]),'USES_SERVER','pg:%s:server:%s'%(db,r[2]))
    kk={r[1]:r for r in rel}
    for r in c['viewdep']:
        vcls='matview' if r[2]=='m' else 'view'; dc={'r':'table','p':'table','f':'foreign_table','v':'view','m':'matview','S':'sequence','i':'index','I':'index','c':'type'}.get(r[5],'?')
        edge('pg:%s:%s:%s.%s'%(db,vcls,r[0],r[1]),'DEPENDS_ON','pg:%s:%s:%s.%s'%(db,dc,r[3],r[4]))
    byname=collections.defaultdict(list)
    for x in fns: byname[(x[0],x[1])].append(x[2])
    for r in c['viewfunc']:
        for a in byname.get((r[2],r[3]),[]): edge('pg:%s:view:%s.%s'%(db,r[0],r[1]),'CALLS','pg:%s:function:%s.%s(%s)'%(db,r[2],r[3],a))
# ---- thân hàm: suy từ mã, tách nhãn (G5)
p=os.path.join(T,'derived-%s.jsonl'%TAG)
derived=collections.Counter()
if os.path.exists(p):
    for l in open(p):
        x=json.loads(l); edge('pg:%s:function:%s'%(x['db'],x['f']),x.get('t','REFERS_IN_BODY'),'pg:%s:table:%s'%(x['db'],x['r']),prov='STATIC_DERIVED',src='prosrc'); derived['edges']+=1
# ---- Directus
dt=collections.defaultdict(list)
for f in rows(rd('dt-%s.tsv'%TAG,'directus:table')): dt[f[0]].append(f[1:])
snap=None; ps=rd('directus-schema-%s.json'%TAG,'directus:api')
if ps:
    try: snap=json.loads(ps)
    except Exception as e: errs['directus:api'].append('JSON '+str(e)[:80])
tcol={r[0] for r in dt['dcol']}; tfld={r[0]+'.'+r[1] for r in dt['dfield']}; trel={r[0]+'.'+r[1] for r in dt['drel']}
acol=afld=arel=aperm=None
if snap:
    s=snap.get('data',snap); acol={c['collection'] for c in s.get('collections',[])}; afld={f['collection']+'.'+f['field'] for f in s.get('fields',[])}; arel={r['collection']+'.'+r['field'] for r in s.get('relations',[])}
    pm=(snap.get('x_dot') or {}).get('permissions') or {}
    aperm={str(x.get('id')) for x in (pm.get('rows') or []) if isinstance(x,dict)} if isinstance(pm,dict) else set()
    apol={str(x.get('id')) for x in (pm.get('policies') or [])} if isinstance(pm,dict) else set()
for c in tcol: node('directus:collection:'+c,'directus_collection','directus_collections')
for f in tfld: node('directus:field:'+f,'directus_field','directus_fields')
for r in dt['drel']: node('directus:relation:%s.%s'%(r[0],r[1]),'directus_relation','directus_relations')
for r in dt['dflow']: node('directus:flow:'+r[0],'directus_flow','directus_flows',name=r[1],status=r[2],trigger=r[3],hash=r[6])
for r in dt['dop']: node('directus:operation:'+r[0],'directus_operation','directus_operations',type=r[2],hash=r[4]); edge('directus:operation:'+r[0],'OPERATION_OF','directus:flow:'+r[1],src='directus_operations')
for r in dt['dpolicy']: node('directus:policy:'+r[0],'directus_policy','directus_policies',admin=r[2])
for r in dt['drole']: node('directus:role:'+r[0],'directus_role','directus_roles')
for r in dt['daccess']: node('directus:access:'+r[0],'directus_access','directus_access')
for r in dt['dperm']:
    node('directus:permission:'+r[0],'directus_permission','directus_permissions',coll=r[1],action=r[2],hash=r[4]); edge('directus:permission:'+r[0],'PERMISSION_ON','directus:collection:'+r[1],src='directus_permissions')
# ---- runtime
rt=None; pr=rd('runtime-%s.json'%TAG,'runtime')
if pr:
    try: rt=json.loads(pr)
    except Exception as e: errs['runtime'].append('JSON')
if rt:
    for e in rt['errors']: errs['runtime'].append('%s rc=%s'%(e['where'],e['rc']))
    for c in rt['cron']: node('cron:%s:%s:%s'%(c['src'],c['user'],c['line']),'cron_entry',c['src'],state='DISABLED' if c['disabled'] else 'ENABLED',hash=c['sha'],pivot=c['pivot'],matrix=c.get('matrix',False),head=c['cmd_head'])
    for u in rt['units']: node('systemd:unit:'+u['unit'],'systemd_unit','systemctl',active=u['active'],sub=u['sub'],load=u['load'])
    for u in rt['unit_files']:
        if 'systemd:unit:'+u['unit'] not in N: node('systemd:unit:'+u['unit'],'systemd_unit','systemctl',active='not-loaded',ufs=u.get('state'))
    for d in rt['dropins']: node('systemd:dropin:'+d,'systemd_dropin','filesystem')
    for c in rt['containers']: node('docker:container:'+c['name'],'docker_container','docker',state=c['state'],image=c['image_id'])
    for l in rt['listeners']: node('net:%s:%s'%(l['proto'],l['listen']),'net_listener','ss',procs=','.join(l['procs']))
    if rt.get('nginx'):
        for s in rt['nginx']['server_names']: node('nginx:server_name:'+s,'nginx_server_name','nginx -T')
        for u in rt['nginx']['upstream_targets']: node('nginx:upstream:'+u,'nginx_upstream','nginx -T')
# ---- ứng viên
at=(open(os.path.join(T,'at.txt')).read().strip() if os.path.exists(os.path.join(T,'at.txt')) else TAG)
with open(os.path.join(OUT,'candidate-nodes-%s.jsonl'%TAG),'w') as f:
    for k in sorted(N): f.write(json.dumps(N[k],ensure_ascii=False,sort_keys=True)+'\n')
with open(os.path.join(OUT,'candidate-edges-%s.jsonl'%TAG),'w') as f:
    for k in sorted(E): f.write(json.dumps(E[k],ensure_ascii=False,sort_keys=True)+'\n')
dbp=os.path.join(OUT,'candidate-%s.sqlite'%TAG)
if os.path.exists(dbp): os.remove(dbp)
cx=sqlite3.connect(dbp); cx.execute('create table nodes(id text primary key,cls text,src text,prov text,attrs text)'); cx.execute('create table edges(s text,t text,d text,prov text,src text,primary key(s,t,d))')
cx.executemany('insert into nodes values(?,?,?,?,?)',[(n['id'],n['cls'],n['src'],n['prov'],json.dumps(n,ensure_ascii=False,sort_keys=True)) for n in N.values()])
cx.executemany('insert into edges values(?,?,?,?,?)',[(e['s'],e['t'],e['d'],e['prov'],e['src']) for e in E.values()]); cx.commit()
SYS=re.compile(r':(pg_catalog|information_schema|pg_toast)\.')
sysdep=sum(1 for e in E.values() if SYS.search(e['d']))
dangling=[e for e in E.values() if e['prov']=='EXACT_NATIVE' and not SYS.search(e['d']) and (e['s'] not in N or e['d'] not in N)]
cdiff=None
if PREV:
    a={json.loads(l)['id']:json.loads(l) for fn in glob.glob(os.path.join(PREV,'candidate-nodes-*.jsonl')) for l in open(fn)}
    b=N; add=sorted(set(b)-set(a)); rem=sorted(set(a)-set(b)); chg=[]; dis=[]
    TRANS=re.compile(r'^systemd:unit:(session-\d+\.scope|run-.*)$')  # phiên ssh/lệnh tạm: không tính là đổi nguồn
    trans=[k for k in add+rem if TRANS.match(k)]; add=[k for k in add if not TRANS.match(k)]; rem=[k for k in rem if not TRANS.match(k)]
    strip=lambda n:{x:y for x,y in n.items() if x!='matrix'}  # cờ matrix thêm vào bộ đọc giữa hai ảnh, không phải nguồn đổi
    for k in set(a)&set(b):
        if strip(a[k])!=strip(b[k]):
            chg.append(k)
            if (a[k].get('state'),b[k].get('state'))==('ENABLED','DISABLED') or (a[k].get('status'),b[k].get('status'))==('active','inactive') or (a[k].get('enabled') not in(None,'D') and b[k].get('enabled')=='D'): dis.append(k)
    pe={(json.loads(l)['s'],json.loads(l)['t'],json.loads(l)['d']) for fn in glob.glob(os.path.join(PREV,'candidate-edges-*.jsonl')) for l in open(fn) if json.loads(l)['prov']=='EXACT_NATIVE'}
    ne={k for k,v in E.items() if v['prov']=='EXACT_NATIVE'}
    cdiff=dict(ADD=add,REMOVE=rem,CHANGE=sorted(chg),DISABLED=sorted(dis),EDGE_ADD=[list(x) for x in sorted(ne-pe)],EDGE_REMOVE=[list(x) for x in sorted(pe-ne)],TRANSIENT=trans)
    json.dump(cdiff,open(os.path.join(OUT,'reconcile-%s.json'%TAG),'w'),ensure_ascii=False,indent=0)
# ---- so Graph
G=json.load(open(GRAPH)); gn=collections.defaultdict(set); ge=collections.Counter(); gedge=set()
retired=0
for n in G['nodes']:
    lb=n['l'][0] if n['l'] else '?'
    if n.get('ra') or n.get('st')=='RETIRED': retired+=1; continue
    gn[lb].add(n['k'])
for e in G['edges']: ge[e['t']]+=1; gedge.add((e['s'],e['t'],e['d']))
pg_cls={'PgTable':('pg:table:',lambda i:re.sub(r'^pg:[^:]+:(?:table|foreign_table):','pg:table:',i),('table','foreign_table')),'PgView':('pg:view:',lambda i:re.sub(r'^pg:[^:]+:(?:view|matview):','pg:view:',i),('view','matview')),'PgFunction':('pg:function:',lambda i:re.sub(r'^pg:[^:]+:function:','pg:function:',i),('function',)),'PgTrigger':('pg:trigger:',lambda i:re.sub(r'^pg:[^:]+:trigger:','pg:trigger:',i),('trigger',)),'PgForeignKey':('pg:fk:',lambda i:re.sub(r'^pg:[^:]+:fk:','pg:fk:',i),('fk',))}
cmpg=[]
def side(name,nat,gr,why=''):
    nat=set(nat); gr=set(gr); cmpg.append(dict(cls=name,native=len(nat),graph=len(gr),both=len(nat&gr),only_native=len(nat-gr),only_graph=len(gr-nat),native_sha=H(nat),graph_sha=H(gr),sample_only_native=sorted(nat-gr)[:5],sample_only_graph=sorted(gr-nat)[:5],why=why))
for lb,(pre,fn,cl) in pg_cls.items():
    nat={fn(i) for i,n in N.items() if n['cls'] in cl}
    side(lb,nat,gn.get(lb,set()))
def edge_norm(e):
    f=lambda i:re.sub(r'^pg:[^:]+:(table|foreign_table):','pg:table:',re.sub(r'^pg:[^:]+:(view|matview):','pg:view:',re.sub(r'^pg:[^:]+:(function|trigger|fk):',r'pg:\1:',i)))
    return (f(e[0]),e[1],f(e[2]))
for t in ('ON_TABLE','EXECUTES','HAS_FK','REFERENCES','DEPENDS_ON'):
    nat={edge_norm(k) for k,v in E.items() if k[1]==t and v['prov']=='EXACT_NATIVE'}
    gr={x for x in gedge if x[1]==t}
    side('edge:'+t,{'|'.join(x) for x in nat},{'|'.join(x) for x in gr})
side('DirectusCollection',{'directus:collection:'+c for c in tcol},gn.get('DirectusCollection',set()))
side('DirectusRelation',{'directus:relation:'+r for r in trel},gn.get('DirectusRelation',set()))
side('DirectusPermission',{'directus:permission:'+r[0] for r in dt['dperm']},gn.get('DirectusPermission',set()))
side('DirectusFlow',{'directus:flow:'+r[0] for r in dt['dflow']},gn.get('DirectusFlow',set()),'lớp chưa nạp')
side('DirectusOperation',{'directus:operation:'+r[0] for r in dt['dop']},gn.get('DirectusOperation',set()),'lớp chưa nạp')
side('DirectusPolicy',{'directus:policy:'+r[0] for r in dt['dpolicy']},gn.get('DirectusPolicy',set()),'lớp chưa nạp')
side('DirectusRole',{'directus:role:'+r[0] for r in dt['drole']},gn.get('DirectusRole',set()),'lớp chưa nạp')
if rt:
    side('SystemdUnit',{i for i,n in N.items() if n['cls']=='systemd_unit'},gn.get('SystemdUnit',set()))
    side('DockerContainer',{'docker:container:'+c['name'] for c in rt['containers']},gn.get('DockerContainer',set()))
    side('NetListener(TCP)',{'net:listen:'+l['listen'] for l in rt['listeners'] if l['proto']=='tcp'},gn.get('NetListener',set()))
    side('CronEntry',{i for i,n in N.items() if n['cls']=='cron_entry'},gn.get('CronEntry',set()),'lớp chưa nạp')
    side('NginxUpstream',{i for i,n in N.items() if n['cls']=='nginx_upstream'},gn.get('NginxRoute',set()),'lớp chưa nạp')
# ---- Directus 2 góc
api=dict(collections=None if acol is None else dict(table=len(tcol),api=len(acol),only_table=sorted(tcol-acol)[:8],n_only_table=len(tcol-acol),only_api=sorted(acol-tcol)[:8],n_only_api=len(acol-tcol)),
 fields=None if afld is None else dict(table=len(tfld),api=len(afld),n_only_table=len(tfld-afld),n_only_api=len(afld-tfld),only_table=sorted(tfld-afld)[:8],only_api=sorted(afld-tfld)[:8]),
 relations=None if arel is None else dict(table=len(trel),api=len(arel),n_only_table=len(trel-arel),n_only_api=len(arel-trel),only_table=sorted(trel-arel)[:8],only_api=sorted(arel-trel)[:8]),
 permissions=None if aperm is None else dict(table=len(dt['dperm']),api=len(aperm),n_only_table=len({r[0] for r in dt['dperm']}-aperm),n_only_api=len(aperm-{r[0] for r in dt['dperm']}),only_table_outside_collections=sum(1 for r in dt['dperm'] if r[0] not in aperm and r[1] not in tcol),only_table_inside_collections=sum(1 for r in dt['dperm'] if r[0] not in aperm and r[1] in tcol),policies_api=len(apol),policies_table=len(dt['dpolicy'])))
# ---- đích kiểm: mới/hồi quy
chk={}
exists=lambda pat:sorted(i for i in N if re.search(pat,i))
gany=lambda pat:sorted(k for s in gn.values() for k in s if re.search(pat,k))
chk['tai_san_luat']=dict(native=exists(r':(table|foreign_table):[^:]*\.tai_san_luat$'),graph=gany(r'tai_san_luat'))
chk['cron_matrix']=dict(total=sum(1 for n in N.values() if n['cls']=='cron_entry' and n.get('matrix')),disabled=sum(1 for n in N.values() if n['cls']=='cron_entry' and n.get('matrix') and n['state']=='DISABLED'))
chk['law_registry_kind']=[(i,N[i]['cls']) for i in N if i.endswith('.law_registry')]
chk['cron_pivot']=dict(native_total=sum(1 for n in N.values() if n['cls']=='cron_entry' and n.get('pivot')),disabled=sum(1 for n in N.values() if n['cls']=='cron_entry' and n.get('pivot') and n['state']=='DISABLED'),enabled=sum(1 for n in N.values() if n['cls']=='cron_entry' and n.get('pivot') and n['state']=='ENABLED'),graph=len(gany(r'^cron:')))
chk['flow_count_refresh']=dict(native=[dict(id=r[0][:8],name=r[1],status=r[2],trigger=r[3]) for r in dt['dflow'] if re.search('count.*refresh',r[1],re.I) or r[0].startswith('e79e00c7')],graph=gany(r'directus:flow'))
PV={'#8 pivot_definitions':r':table:public\.pivot_definitions$','#9 pivot_results':r':table:public\.pivot_results$','#17 meta_catalog':r':table:public\.meta_catalog$','#10 trg_after_pivot_definitions_change':r':trigger:public\.pivot_definitions\.trg_after_pivot_definitions_change$','#11 trg_birth_pivot_definitions':r':trigger:public\.pivot_definitions\.trg_birth_pivot_definitions$','#11 trg_birth_pivot_results':r':trigger:public\.pivot_results\.trg_birth_pivot_results$','#12 trg_matrix_config_changed':r':trigger:.*\.trg_matrix_config_changed$','#13 trg_birth_change_flag_matrix':r':trigger:public\.birth_registry\.trg_birth_change_flag_matrix$','#14 refresh_pivot_results':r':function:public\.refresh_pivot_results\(','#14 refresh_meta_catalog_from_pivot':r':function:public\.refresh_meta_catalog_from_pivot\(','#14 refresh_matrix_results':r':function:public\.refresh_matrix_results\(','#15 pivot_query':r':function:public\.pivot_query\(','#15 pivot_count':r':function:public\.pivot_count\(','#15 pivot_matrix':r':function:public\.pivot_matrix\(','#15 fn_registries_pivot_node_substrate':r':function:public\.fn_registries_pivot_node_substrate\(','#16 views *pivot*':r':(view|matview):[^:]*pivot[^:]*$','#16 views v_rp_*':r':(view|matview):public\.v_rp_','#21 dir pivot_definitions':r'^directus:collection:pivot_definitions$','#21 dir pivot_results':r'^directus:collection:pivot_results$','#21 dir meta_catalog':r'^directus:collection:meta_catalog$'}
reg=[]
for k,p_ in PV.items():
    nat=exists(p_); gp=p_.replace(r':(view|matview):',':view:').replace(':table:',':table:')
    gr=gany(p_.replace('(view|matview)','view'))
    reg.append(dict(item=k,native=len(nat),graph=len(gr),status='MATCH' if nat and gr and len(nat)==len(gr) else ('GRAPH_MISSING' if nat and not gr else ('NATIVE_ABSENT' if not nat else 'PARTIAL'))))
chk['pivot_regression']=reg
sumr=dict(tag=TAG,at=at,dbs=DBS,node_total=len(N),edge_total=len(E),exact_edges=sum(1 for e in E.values() if e['prov']=='EXACT_NATIVE'),derived_edges=sum(1 for e in E.values() if e['prov']=='STATIC_DERIVED'),by_class=dict(collections.Counter(n['cls'] for n in N.values()).most_common()),system_catalog_edges=sysdep,dangling=len(dangling),dangling_sample=[list((d['s'],d['t'],d['d'])) for d in dangling[:6]],node_sha=H(N),edge_sha=H('|'.join(k) for k in E),toc_vs_catalog=tvs,graph_compare=cmpg,graph_at=G['at'],graph_retired=retired,directus_two_angles=api,checks=chk,reader_errors=dict(errs),new_class_unhandled={'%s:%s'%k:v for k,v in unkall.items()},forbidden_toc=dict(forball),graph_key_collisions=sorted(k for k,v in gmap.items() if len(set(v))>1)[:10],graph_key_collision_count=sum(1 for k,v in gmap.items() if len(set(v))>1),diff=None if not cdiff else {k:len(v) for k,v in cdiff.items()},verdict='PARTIAL' if (errs or unkall or forball) else 'READERS_OK')
json.dump(sumr,open(os.path.join(OUT,'summary-%s.json'%TAG),'w'),ensure_ascii=False,indent=1)
print(json.dumps({k:sumr[k] for k in('node_total','edge_total','exact_edges','derived_edges','dangling','dangling_sample','verdict','reader_errors','new_class_unhandled','forbidden_toc','graph_key_collision_count','diff','node_sha','edge_sha')},ensure_ascii=False))
__K0_EOF__
cat > k0_run.sh <<'__K0_EOF__'
set -u; umask 077
RUN=GS-COV2-K0-LIVE-SOURCE-ORACLE-20261030-01; TAG=$1
T=$(mktemp -d /dev/shm/gsk0.XXXXXX); trap 'rm -rf "$T"' EXIT
base64 -d <<<"$2" | tar -xzf - -C $T
RO=$(grep -E '^(export )?PG_USER_RO=' /opt/incomex/secrets/.env.production | sed -E "s/^(export )?PG_USER_RO=//; s/[\"']//g")
DOT=/opt/incomex/dot/bin/dot-stack-cutover; CONF=/opt/incomex/dot/config/stack-cutover.prod-vps1.conf
P(){ docker exec -i -e PGOPTIONS='-c default_transaction_read_only=on' postgres psql -X -q -v ON_ERROR_STOP=1 -U "$RO" -d "$1"; }
DBS=$(docker exec -e PGOPTIONS='-c default_transaction_read_only=on' postgres psql -XAtq -U "$RO" -d postgres -c "select datname from pg_database where datallowconn and not datistemplate order by 1")
echo "DBS=$(echo $DBS)"; date -u +%FT%TZ > $T/out_t0
mkdir $T/out; for db in $DBS; do P $db < $T/k0_stat.sql > $T/out/stat-$TAG-$db.tsv 2>$T/out/stat-$TAG-$db.err; echo "stat $db rc=$? rows=$(wc -l < $T/out/stat-$TAG-$db.tsv)"; done
for db in $DBS; do a=$(date +%s%3N); $DOT source-dump --db $db --schema-only --mode prod --conf $CONF --run-id $RUN 2>$T/out/dump-$db.err </dev/null > $T/$db.dump; rc=$?; b=$(date +%s%3N)
 docker exec -i postgres pg_restore --list < $T/$db.dump > $T/out/toc-$TAG-$db.txt 2>$T/out/toce-$db.err; rl=$?
 echo "dump $db rc=$rc ms=$((b-a)) bytes=$(stat -c %s $T/$db.dump) sha=$(sha256sum $T/$db.dump | cut -c1-16) list_rc=$rl toc=$(grep -cvE '^;' $T/out/toc-$TAG-$db.txt) DATA=$(grep -c 'TABLE DATA' $T/out/toc-$TAG-$db.txt) BLOBS=$(grep -cE 'BLOBS|LARGE OBJECT' $T/out/toc-$TAG-$db.txt) SEQSET=$(grep -c 'SEQUENCE SET' $T/out/toc-$TAG-$db.txt)"; cp $T/$db.dump $T/out/$db-$TAG.dump; done
$DOT source-dump --globals --mode prod --conf $CONF --run-id $RUN 2>$T/out/glob.err </dev/null > $T/out/globals-$TAG.sql; echo "globals rc=$? bytes=$(stat -c %s $T/out/globals-$TAG.sql) role_pw=$(grep -c "PASSWORD '" $T/out/globals-$TAG.sql) create_role=$(grep -c '^CREATE ROLE' $T/out/globals-$TAG.sql)"
for db in $DBS; do P $db < $T/k0_catalog.sql > $T/out/cat-$TAG-$db.tsv 2>$T/out/cat-$db.err; echo "catalog $db rc=$? rows=$(wc -l < $T/out/cat-$TAG-$db.tsv) err=$(wc -c < $T/out/cat-$db.err)"; done
P directus < $T/k0_directus_table.sql > $T/out/dt-$TAG.tsv 2>$T/out/dt.err; echo "directus-table rc=$? rows=$(wc -l < $T/out/dt-$TAG.tsv) err=$(cat $T/out/dt.err | cut -c1-160)"
python3 $T/k0_runtime.py > $T/out/runtime-$TAG.json 2>$T/out/runtime.err; echo "runtime rc=$? bytes=$(stat -c %s $T/out/runtime-$TAG.json)"
LIST=$(awk -F'\t' '$1=="dcol"{print $2}' $T/out/dt-$TAG.tsv | paste -sd,)
/opt/incomex/dot/bin/dot-schema-snapshot --output=$T/out/directus-schema-$TAG.json --permissions=$LIST </dev/null > $T/out/ds.out 2>$T/out/ds.err; echo "dot-schema-snapshot rc=$? bytes=$(stat -c %s $T/out/directus-schema-$TAG.json 2>/dev/null) $(tail -1 $T/out/ds.out | cut -c1-140) $(tail -1 $T/out/ds.err | cut -c1-140)"
for db in $DBS; do P $db < $T/k0_stat.sql > $T/out/stat2-$TAG-$db.tsv 2>/dev/null; done
echo at=$(date -u +%FT%TZ) > $T/out/at.txt; python3 $T/k0_derived.py "$RO" $T/out/derived-$TAG.jsonl $DBS; python3 $T/k0_usage_vps.py > $T/out/usage-$TAG.json; tar -C $T/out -czf $T/out.tgz . ; echo "OUTB64_BYTES=$(stat -c %s $T/out.tgz)"; base64 -w0 $T/out.tgz > $T/out.b64; echo "::BEGIN::"; cat $T/out.b64; echo; echo "::END::"
__K0_EOF__
cat > k0_runtime.py <<'__K0_EOF__'
#!/usr/bin/env python3
# K0 đọc runtime từ hệ điều hành (G4): cron mọi user kể cả dòng tắt, systemd mọi unit/drop-in/timer, docker, cổng, tiến trình; không in argv/env/nội dung tệp.
import json,os,re,subprocess,glob,hashlib,time
def sh(c,t=60):
    try:
        p=subprocess.run(c,shell=True,capture_output=True,text=True,timeout=t); return p.returncode,p.stdout,p.stderr[-300:]
    except Exception as e: return 99,'',repr(e)[:300]
o={'at':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'errors':[]}
def need(where,c,t=60):
    rc,s,e=sh(c,t)
    if rc: o['errors'].append({'where':where,'rc':rc,'stderr':e})
    return s
SCHED=re.compile(r'^\s*(?:#[A-Za-z0-9_\-]*\s*)?(@(reboot|hourly|daily|weekly|monthly|yearly|annually)|([\d\*/,\-]+\s+){4}[\d\*/,\-A-Za-z]+)\s+\S')
cron=[]
def cf(p,src,user):
    try:
        for i,l in enumerate(open(p,errors='replace'),1):
            s=l.rstrip('\n')
            if not s.strip() or not SCHED.match(s): continue
            d=s.lstrip().startswith('#'); b=re.sub(r'^\s*#[A-Za-z0-9_\-]*\s*','',s).strip()
            cron.append({'src':src,'user':user,'line':i,'disabled':d,'sha':hashlib.sha256(b.encode()).hexdigest()[:16],'pivot':bool(re.search('pivot',b,re.I)),'matrix':bool(re.search('matrix',b,re.I)),'cmd_head':os.path.basename(re.split(r'\s+',re.sub(r'^(@\S+|(\S+\s+){5})','',b))[0])[:60]})
    except OSError as e: o['errors'].append({'where':p,'rc':1,'stderr':str(e)[:200]})
for p in sorted(glob.glob('/var/spool/cron/crontabs/*')): cf(p,'spool',os.path.basename(p))
for p in ['/etc/crontab']+sorted(glob.glob('/etc/cron.d/*')): cf(p,p,'field')
o['cron']=cron
o['cron_dirs']={d:sorted(os.path.basename(x) for x in glob.glob('/etc/cron.%s/*'%d)) for d in ('hourly','daily','weekly','monthly')}
units=[]
for l in need('list-units','systemctl list-units --all --no-legend --plain --no-pager').splitlines():
    f=l.split(None,4)
    if len(f)>=4: units.append({'unit':f[0],'load':f[1],'active':f[2],'sub':f[3]})
o['units']=units
o['unit_files']=[dict(zip(('unit','state'),l.split()[:2])) for l in need('unit-files','systemctl list-unit-files --no-legend --plain --no-pager').splitlines() if l.strip()]
o['timers']=[l.split()[-2:] for l in need('timers','systemctl list-timers --all --no-legend --plain --no-pager').splitlines() if l.strip()]
o['dropins']=sorted(glob.glob('/etc/systemd/system/*.d/*.conf')+glob.glob('/run/systemd/system/*.d/*.conf')+glob.glob('/usr/lib/systemd/system/*.d/*.conf'))
o['containers']=[json.loads(l) for l in need('docker-ps',"docker ps -a --no-trunc --format '{{json .}}'").splitlines() if l.strip()]
slim=[]
for c in o['containers']:
    i=json.loads(need('inspect','docker inspect %s'%c['ID']) or '[{}]')[0]
    slim.append({'name':c['Names'],'id':c['ID'][:12],'image_ref':i.get('Config',{}).get('Image'),'image_id':i.get('Image'),'state':i.get('State',{}).get('Status'),'started':i.get('State',{}).get('StartedAt'),'created':i.get('Created'),'restart':i.get('RestartCount'),'mounts':sorted(m.get('Source','')+'->'+m.get('Destination','') for m in i.get('Mounts',[])),'nets':sorted(i.get('NetworkSettings',{}).get('Networks',{}).keys())})
o['containers']=slim
ss=[]
for l in need('ss','ss -H -ltnup').splitlines():
    f=l.split(); 
    if len(f)>=5:
        m=re.findall(r'"([^"]+)",pid=(\d+)',l); ss.append({'proto':f[0],'listen':f[4],'procs':sorted({x[0] for x in m})})
o['listeners']=ss
cg={}
for p in glob.glob('/proc/[0-9]*'):
    try:
        c=open(p+'/cgroup').read().strip().split('::')[-1]; comm=open(p+'/comm').read().strip()
        k=('docker' if 'docker' in c else c.split('/')[-1] if c else '?'); cg.setdefault(k,set()).add(comm)
    except OSError: pass
o['proc_cgroups']={k:sorted(v) for k,v in cg.items()}
rc,s,e=sh('docker exec incomex-nginx nginx -T')
o['nginx_rc']=rc
if rc==0:
    server=len(re.findall(r'^\s*server\s*\{',s,re.M)); pp=[]
    for l in s.splitlines():
        m=re.match(r'^\s*proxy_pass\s+(\S+);',l)
        if m: pp.append(m.group(1))
    names=[]
    for l in s.splitlines():
        m=re.match(r'^\s*server_name\s+([^;]+);',l)
        if m: names+=m.group(1).split()
    o['nginx']={'server_blocks':server,'proxy_pass':len(pp),'upstream_targets':sorted({re.sub(r'^https?://','',x).split('/')[0] for x in pp}),'server_names':sorted(set(names)),'locations':len(re.findall(r'^\s*location\s',s,re.M)),'config_sha':hashlib.sha256(s.encode()).hexdigest()}
else: o['errors'].append({'where':'nginx-T','rc':rc,'stderr':'' })
o['versions']={k:sh(v)[1].strip()[:120] for k,v in dict(docker="docker version --format '{{.Server.Version}}'",nginx="docker exec incomex-nginx nginx -v 2>&1",directus="docker inspect incomex-directus --format '{{.Config.Image}}'",os="sed -n 's/^PRETTY_NAME=//p' /etc/os-release",kernel='uname -r').items()}
o['windows']={'journal_oldest':sh("journalctl -q --no-pager -o short-iso -n 1 --reverse --output=short-iso -b -999 2>/dev/null | head -1")[1].strip()[:40],'journal_first':sh("journalctl -q --no-pager -o short-iso | head -1",90)[1].strip()[:32],'journal_disk':sh('journalctl --disk-usage')[1].strip()[:80],'uptime_since':sh('uptime -s')[1].strip()}
print(json.dumps(o,ensure_ascii=False))
__K0_EOF__
cat > k0_stat.sql <<'__K0_EOF__'
\pset format unaligned
\pset fieldsep '\t'
\pset tuples_only on
begin transaction isolation level read committed read only;
set local statement_timeout='30s';
select 'statpg',pg_postmaster_start_time(),now(),(select setting from pg_settings where name='track_functions');
select 'statdb',datname,now(),stats_reset,xact_commit,tup_inserted,tup_updated,tup_deleted from pg_stat_database where datname=current_database();
select 'stattable',schemaname,relname,seq_scan,last_seq_scan,idx_scan,last_idx_scan,n_tup_ins,n_tup_upd,n_tup_del,n_live_tup from pg_stat_user_tables order by 2,3;
select 'statfunc',schemaname,funcname,funcid,calls,total_time from pg_stat_user_functions order by 2,3;
commit;
__K0_EOF__
cat > k0_usage.py <<'__K0_EOF__'
#!/usr/bin/env python3
import csv,glob,json,os,sys,collections,re
E=sys.argv[1]; res={}
def load(p):
    t={};f={};d=None;pg=None
    for l in open(p,errors='replace'):
        x=l.rstrip('\n').split('\t')
        if x[0]=='statdb': d=x[1:]
        elif x[0]=='statpg': pg=x[1:]
        elif x[0]=='stattable': t[x[1]+'.'+x[2]]=dict(seq=int(x[3]),lseq=x[4],idx=int(x[5] or 0),lidx=x[6],ins=int(x[7]),upd=int(x[8]),dl=int(x[9]),live=int(x[10]))
        elif x[0]=='statfunc': f[x[1]+'.'+x[2]+'#'+x[3]]=dict(calls=int(x[4]),total=float(x[5]))
    return d,t,f,pg
base={}
cur=None
for l in open(os.path.join(E,'..','GS-COV2-P-SCHEMA-READONLY-USAGE-METERS-20261030-01','g2-pgstat-baseline-truoc-p1.txt'),errors='replace'):
    if l.startswith('##DB '): cur=l.split()[1]; base[cur]={}; continue
    x=l.rstrip('\n').split('|')
    if cur and len(x)==10: base[cur][x[0]+'.'+x[1]]=dict(seq=int(x[2]),idx=int(x[4] or 0),ins=int(x[6]),upd=int(x[7]),dl=int(x[8]))
out={}
for db in ('directus','incomex_metadata','postgres','workflow'):
    d1,t1,f1,_=load(os.path.join(E,'T1','stat-T1-%s.tsv'%db)); d2,t2,f2,pg=load(os.path.join(E,'T2','stat2-T2-%s.tsv'%db))
    b=base.get(db,{})
    delta={k:dict(seq=t2[k]['seq']-b[k]['seq'],idx=t2[k]['idx']-b[k]['idx'],w=(t2[k]['ins']+t2[k]['upd']+t2[k]['dl'])-(b[k]['ins']+b[k]['upd']+b[k]['dl'])) for k in t2 if k in b}
    lifetime_w=sum(1 for v in t2.values() if v['ins']+v['upd']+v['dl']>0); lifetime_r=sum(1 for v in t2.values() if v['seq']+v['idx']>0)
    self_tables={'public.directus_collections','public.directus_fields','public.directus_relations','public.directus_flows','public.directus_operations','public.directus_policies','public.directus_roles','public.directus_access','public.directus_permissions','public.directus_presets','public.directus_settings','public.directus_users','public.directus_activity','public.directus_revisions'}
    out[db]=dict(stats_reset=(d2[2] if d2 else None),postmaster_start=pg[0] if pg else None,sample_at=d2[1] if d2 else None,track_functions=pg[2] if pg else None,tables=len(t2),tables_with_lifetime_write=lifetime_w,tables_with_lifetime_read=lifetime_r,tables_no_counter=len(t2)-sum(1 for v in t2.values() if v['ins']+v['upd']+v['dl']+v['seq']+v['idx']>0),window_write_tables=sorted(k for k,v in delta.items() if v['w']>0)[:40],window_write_n=sum(1 for v in delta.values() if v['w']>0),window_read_n=sum(1 for k,v in delta.items() if v['seq']+v['idx']>0),self_touched=sorted(k for k,v in delta.items() if v['seq']+v['idx']>0 and k in self_tables),func_rows=len(f2),func_calls={k.split('#')[0]:v['calls'] for k,v in f2.items()})
    if db=='directus':
        chk={}
        for k in ('public.pivot_definitions','public.pivot_results','public.meta_catalog','public.birth_registry','public.tai_san_luat','public.law_registry'):
            v=t2.get(k); chk[k]=(dict(seq=v['seq'],last_seq=v['lseq'][:19],idx=v['idx'],last_idx=v['lidx'][:19],ins=v['ins'],upd=v['upd'],dl=v['dl'],live=v['live'],window=delta.get(k)) if v else 'NOT_IN_pg_stat_user_tables')
        out[db]['pivot_tables']=chk
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
for db,v in out.items(): print(db,{k:v[k] for k in('stats_reset','postmaster_start','sample_at','track_functions','tables','tables_with_lifetime_write','tables_with_lifetime_read','tables_no_counter','window_write_n','window_read_n','func_rows')},v['func_calls'],v['self_touched'][:3],v['window_write_tables'][:8])
print(json.dumps(out['directus']['pivot_tables'],ensure_ascii=False))
__K0_EOF__
cat > k0_usage_vps.py <<'__K0_EOF__'
#!/usr/bin/env python3
# G1/K2: cửa sổ dấu dùng có thật và số lượt theo đường (chỉ đếm, không in IP/UA/query).
import json,glob,os,re,subprocess,collections,datetime as dt
d=subprocess.run("docker inspect incomex-nginx --format '{{.LogPath}}'",shell=True,capture_output=True,text=True).stdout.strip()
P={'/knowledge/pivot':r'"[A-Z]+ /knowledge/pivot[/ ?]','/knowledge/registries-pivot':r'"[A-Z]+ /knowledge/registries-pivot','/knowledge/registries':r'"[A-Z]+ /knowledge/registries(?!-pivot)','/api/registry/pivot-query':r'"[A-Z]+ /api/registry/pivot-query','/api/registry/refresh-counts':r'"[A-Z]+ /api/registry/refresh-counts','/api/registries-pivot':r'"[A-Z]+ /api/registries-pivot'}
P={k:re.compile(v) for k,v in P.items()}; BOT=re.compile(r'bot|crawl|spider|slurp|curl|python|wget|scan|Go-http|zgrab|httpx',re.I)
c={k:collections.Counter() for k in P}; first=last=None; n=0
for f in sorted(glob.glob(d+'*'),key=os.path.getmtime):
    for line in open(f,'rb'):
        try: o=json.loads(line)
        except Exception: continue
        n+=1; first=first or o['time']; last=o['time']; m=o.get('log','')
        for k,r in P.items():
            if r.search(m):
                c[k]['bot' if BOT.search(m) else 'non_bot']+=1
                s=re.search(r'" (\d{3}) ',m); c[k]['s'+(s.group(1)[0]+'xx' if s else '?')]+=1
print(json.dumps({'nginx_window':[first,last],'lines':n,'paths':{k:dict(v) for k,v in c.items()}},ensure_ascii=False))
__K0_EOF__
cat > SHA256SUMS <<'__K0_EOF__'
eed8dbf4b77031fded0826d5650ab21fedf72593c37167105fb198420c2ec776  k0_catalog.sql
187d1e77121ff782d834be8bf045a7fcb888d460ca692aeec96312b09c069d14  k0_derived.py
efad9f6a65322b84c24a5a4f74475c154e74d72ef5ab3f3f25bbf5b91b16ef29  k0_directus_table.sql
45f678b3f76bf102b8d6db81ceb14171b878977fed0536bef3d40c7baf6bf894  k0_fixtures.py
6694b276b54f8c8802522b5fdc13b4f4d3116cdcd1e015e486636fcd4b7396dd  k0_graph_export.py
f6afbb50061b8533c5e62526634f16b16ee6f12a52e35d19d8713df31ee37c5e  k0_reconcile.py
6d841415d16ae49cb91c7f0b6864f8edb3bb76f7797f49ef35bb81dc24b0923b  k0_run.sh
e9ad2b684796627630039c8ce6982d790dc640e780cf02c38446b0b396e16c62  k0_runtime.py
26e1e11c3ec931384cb4b298ed2fc199269a5d90fe702e0d9ac86a9d72f60d65  k0_stat.sql
7c2bf5b2b38af51785f70e2018e615b44b8b48108c74847d8a97ebf6f1864005  k0_usage.py
ee7a7fa7ddadbbc3d7695ed24cf6860ae6119f33e357c28d081db16a21a134b7  k0_usage_vps.py
__K0_EOF__
shasum -a 256 -c SHA256SUMS 2>/dev/null || sha256sum -c SHA256SUMS
