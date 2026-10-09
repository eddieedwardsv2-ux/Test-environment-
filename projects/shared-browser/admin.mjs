// Local operator helper: never prints or accepts the gateway secret in chat.
import {readFile} from 'node:fs/promises';import {resolve} from 'node:path';
const dir=process.env.BROWSER_DATA_DIR||'/workspace/charlie-browser-private/gateway';
const token=(await readFile(resolve(dir,'admin-token'),'utf8')).trim();
const action=process.argv[2]||'pending';const code=process.argv[3];
if(!['pending','approve','status'].includes(action))throw new Error('Use pending, approve CODE, or status');
const path=action==='status'?'/api/agent/status':'/api/admin/'+action;
const r=await fetch('http://127.0.0.1:8787'+path,{method:action==='approve'?'POST':'GET',headers:{authorization:'Bearer '+token,'content-type':'application/json'},body:action==='approve'?JSON.stringify({code}):undefined});
if(!r.ok)throw new Error('Operator request failed: '+r.status);console.log(JSON.stringify(await r.json()));
