#!/usr/bin/env python3
"""Read-only pilot runtime invariant, consumed by existing Protection Guard/Kuma #22."""
import copy,json,pathlib,subprocess,sys

REPOS=('agent-data-test','web-test')
SOCKET_CHECK=r'''
import pathlib,json
listeners=[]
for p in pathlib.Path('/proc').glob('[0-9]*'):
 try:
  if (p/'comm').read_text().strip()=='Runner.Listener': listeners.append(p)
 except OSError: pass
sockets=set()
for p in listeners:
 for f in (p/'fd').iterdir():
  try:
   x=str(f.readlink())
   if x.startswith('socket:['): sockets.add(x[8:-1])
  except OSError: pass
connected=0
for name in ('tcp','tcp6'):
 for line in pathlib.Path('/proc/net/'+name).read_text().splitlines()[1:]:
  row=line.split()
  if row[3]=='01' and row[2].endswith(':01BB') and row[9] in sockets: connected+=1
print(json.dumps({'listener':len(listeners),'tls_connections':connected}))
sys_exit=0 if listeners and connected else 1
raise SystemExit(sys_exit)
'''

def validate(d,repo,image):
 h=d['HostConfig']; c=d['Config']; s=d['State']; errors=[]
 expected={'User': '10001:10001'}
 if c['User']!=expected['User']: errors.append('user')
 if d['Image']!=image: errors.append('image')
 if h['Privileged']: errors.append('privileged')
 if h['NanoCpus']!=1000000000: errors.append('cpu')
 if h['Memory']!=1610612736 or h['MemorySwap']!=1610612736: errors.append('memory')
 if h['PidsLimit']!=256: errors.append('pids')
 if h['RestartPolicy']['Name']!='unless-stopped': errors.append('restart')
 if h['NetworkMode']!='ghm-ci': errors.append('network')
 if set(h.get('CapDrop') or [])!={'ALL'} or h.get('CapAdd'): errors.append('caps')
 if not any(x.split(':')[0]=='no-new-privileges' for x in h.get('SecurityOpt') or []): errors.append('nnp')
 if h.get('PortBindings'): errors.append('ports')
 if h.get('Devices') or h.get('DeviceRequests') or h.get('GroupAdd'): errors.append('extra-access')
 mounts={(m.get('Type'),m.get('Name'),m.get('Destination')) for m in d['Mounts']}
 if mounts!={('volume','ghm-ci-'+repo+'-data','/runner'),('volume','ghm-ci-build-lock','/ci-lock')}: errors.append('mounts')
 if not s['Running'] or s.get('OOMKilled'): errors.append('running')
 return errors

def main():
 image=pathlib.Path('/opt/incomex/ci-runner/image-id').read_text().strip()
 output=[]
 for repo in REPOS:
  name='ghm-ci-'+repo
  try:
   p=subprocess.run(['docker','inspect',name],text=True,capture_output=True,timeout=15,check=True)
   d=json.loads(p.stdout)[0]
   errors=validate(d,repo,image)
   p=subprocess.run(['docker','exec',name,'python3','-c',SOCKET_CHECK],text=True,capture_output=True,timeout=15)
   connection=json.loads(p.stdout) if p.returncode==0 else {'listener_or_connection':'unavailable'}
   if p.returncode: errors.append('listener-connection')
   output.append({'repo':repo,'ok':not errors,'errors':errors,'connection':connection})
  except Exception as e: output.append({'repo':repo,'ok':False,'errors':[type(e).__name__]})
 print(json.dumps({'ok':all(x['ok'] for x in output),'runners':output,'scope':'listener TLS connectivity + runtime limits; GitHub online API recorded separately at acceptance'},separators=(',',':')))
 return 0 if all(x['ok'] for x in output) else 1

if __name__=='__main__': sys.exit(main())
