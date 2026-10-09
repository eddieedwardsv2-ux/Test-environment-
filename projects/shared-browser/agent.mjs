// Run on the private host. Does not print bearer tokens or page contents.
import {readFile,writeFile} from 'node:fs/promises';import {resolve} from 'node:path';
const dir=process.env.BROWSER_DATA_DIR||'/workspace/charlie-browser-private/gateway';
const bearer=(await readFile(resolve(dir,'admin-token'),'utf8')).trim();
const headers={authorization:'Bearer '+bearer,'content-type':'application/json'};
const origin='http://127.0.0.1:8787';const command=process.argv[2]||'status';
const r=await fetch(origin+'/api/agent/status',{headers});if(!r.ok)throw new Error('Agent connection unavailable');const state=await r.json();
if(command==='status')console.log(JSON.stringify(state));
else if(command==='snapshot'){
 const response=await fetch(origin+'/api/agent/snapshot',{headers});if(!response.ok)throw new Error('Choose AI’s turn first; response '+response.status);
 const path=process.argv[3]?resolve(process.argv[3]):resolve(dir,'snapshot.png');await writeFile(path,Buffer.from(await response.arrayBuffer()),{mode:0o600});console.log('Private screenshot saved');
}else{
 const args=process.argv.slice(3);let action;
 if(command==='navigate')action={type:command,url:args[0]};
 else if(command==='click')action={type:command,selector:args[0]};
 else if(command==='type')action={type:command,selector:args[0],text:args[1]};
 else if(command==='press')action={type:command,key:args[0]};
 else if(command==='scroll')action={type:command,y:Number(args[0])};
 else throw new Error('Use status, snapshot, navigate URL, click SELECTOR, type SELECTOR TEXT, press KEY, scroll PIXELS');
 const response=await fetch(origin+'/api/agent/action',{method:'POST',headers,body:JSON.stringify({...action,lease:state.lease})});if(!response.ok)throw new Error('Action failed; response '+response.status);await response.json();console.log('Browser action completed');
}
