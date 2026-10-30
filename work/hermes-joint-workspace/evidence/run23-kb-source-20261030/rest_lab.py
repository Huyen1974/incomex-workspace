import ast,asyncio,importlib.util,json,os,sys
from pathlib import Path
repo=Path.cwd();sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'tests/unit'))
import pytest
import test_hjw_four_facts as t
from fastapi import FastAPI,Depends,Header,Request,HTTPException
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient
from agent_data import kb_declaration as kb
monkey=pytest.MonkeyPatch();monkey.setenv('WORKSPACE_DECLARATION_MODE','enforce');monkey.setenv('API_KEY','fixture-key-only')
fixture=t.kb_lab.__wrapped__(monkey);g,trace=next(fixture)
g2=dict(g,Request=Request,Header=Header,Depends=Depends,HTTPException=HTTPException,os=os)
g2['_error']=lambda status,code,message,**kw:HTTPException(status,{'code':code,'message':message})
tree=ast.parse((repo/'agent_data/server.py').read_text())
nodes=[n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name in ('require_api_key','_kb_input')]
exec(compile(ast.Module(body=nodes,type_ignores=[]),'actual-rest-dependencies','exec'),g2)
app=FastAPI();routes=[('POST','/documents','upload_document'),('PUT','/documents/alpha','update_document'),('PATCH','/documents/alpha','patch_document'),('DELETE','/documents/alpha','delete_document'),('POST','/ingest','ingest_document')]
def endpoint(name):
 async def call(ctx=Depends(g2['_kb_input'])):
  r=await t.kb_call(g,name,ctx)
  if isinstance(r,t.KBResponse):return JSONResponse(r.json(),status_code=r.status_code)
  return r.model_dump()
 return call
for method,path,name in routes:app.add_api_route(path,endpoint(name),methods=[method])
results=[]
with TestClient(app) as client:
 for method,path,name in routes:
  for kind in ('wrong_key','missing_facts','forged_header','forged_body','valid','legacy'):
   monkey.setenv('WORKSPACE_DECLARATION_MODE','advertise' if kind=='legacy' else 'enforce')
   headers={'X-API-Key':'wrong' if kind=='wrong_key' else 'fixture-key-only'}
   payload={}
   if kind not in ('missing_facts','legacy'):headers.update(kb.header(t.args()))
   if kind=='forged_header':headers[kb.HEADER]='{"_declaration":{}}'
   if kind=='forged_body':payload={'_hvu':{'authenticated':True}}
   trace.clear();response=client.request(method,path,headers=headers,json=payload)
   denied=kind not in ('valid','legacy')
   assert response.status_code==403 if denied else response.status_code in (200,202),(name,kind,response.status_code,response.text)
   assert (trace==[]) if denied else ('pg' in trace),(name,kind,trace)
   if kind=='valid':assert response.json()['declaration_receipt']['authenticated_actor']=='credential:shared-rest'
   if kind=='legacy':assert 'declaration_receipt' not in response.json()
   results.append({'method':method,'path':path,'case':kind,'status':response.status_code,'effects':list(trace)})
print(json.dumps({'passed':len(results),'scope':'FastAPI HTTP fixture with actual REST dependency + actual guarded handler bodies; fake storage, no production startup','cases':results},indent=2))
try:next(fixture)
except StopIteration:pass
monkey.undo()
