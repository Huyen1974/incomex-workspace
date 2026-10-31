"""RUN24 S2: N processes open a queue.sqlite that does not exist yet and enqueue the same operation_id.
Usage (repo root): PYTHONPATH=. python fresh_db_stress.py <rounds> <procs>; JSON summary on stdout."""
import json,os,subprocess,sys,tempfile,time,collections
CHILD='''
import json,sys,time
from agent_data.workspace_runtime import Queue
base,at=sys.argv[1],float(sys.argv[2])
while time.time()<at:pass
try:
    key,_,replayed=Queue(base).enqueue_once('tasks',{'tool':'x'},'same-op','h')
    print(json.dumps({'key':key,'replayed':replayed}))
except Exception as e:print(json.dumps({'error':type(e).__name__+': '+str(e)}))
'''
rounds,procs=int(sys.argv[1]),int(sys.argv[2])
errors=collections.Counter();bad=0;slowest=0.0
for r in range(rounds):
    with tempfile.TemporaryDirectory() as d:
        at=time.time()+.5;start=time.monotonic()
        ps=[subprocess.Popen([sys.executable,'-c',CHILD,d,str(at)],stdout=subprocess.PIPE,text=True,env=dict(os.environ)) for _ in range(procs)]
        out=[json.loads(p.communicate()[0].strip().splitlines()[-1]) for p in ps]
        slowest=max(slowest,time.monotonic()-start-.5)
        keys={o['key'] for o in out if 'key' in o}
        for o in out:
            if 'error' in o:errors[o['error']]+=1
        if len(keys)!=1 or any('error' in o for o in out):bad+=1
print(json.dumps({'rounds':rounds,'procs':procs,'bad_rounds':bad,'errors':errors,'slowest_round_s':round(slowest,3)}))
