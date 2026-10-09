import http from 'node:http';
import net from 'node:net';
import { randomBytes, createHash, timingSafeEqual } from 'node:crypto';
import { readFile, writeFile, rename, mkdir, stat } from 'node:fs/promises';
import { resolve, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { WebSocketServer } from 'ws';
import { chromium } from 'playwright-core';
const root=dirname(fileURLToPath(import.meta.url));
const hash=v=>createHash('sha256').update(v).digest('hex');
const token=()=>randomBytes(32).toString('base64url');
const fail=(status,message)=>Object.assign(new Error(message),{status});
const safeEqual=(a,b)=>typeof a==='string'&&typeof b==='string'&&a.length===b.length&&timingSafeEqual(Buffer.from(a),Buffer.from(b));
const navigation=value=>{let u;try{u=new URL(value);}catch{throw fail(400,'Enter a complete website address');}if(!['http:','https:'].includes(u.protocol)||u.username||u.password)throw fail(400,'Only ordinary website addresses are supported');return u.href;};
async function body(req){let s='';for await(const b of req){s+=b;if(s.length>16384)throw fail(413,'Request too large');}try{return JSON.parse(s||'{}');}catch{throw fail(400,'Invalid JSON');}}
export async function createApp({dataDir,adminToken,allowHttp=false,cdp='http://127.0.0.1:9222',vncPort=5900,publicOrigin,trustProxy=false}={}){
 if(!dataDir||!adminToken)throw new Error('Private data directory and admin token required');
 await mkdir(dataDir,{recursive:true,mode:0o700});
 const dbPath=resolve(dataDir,'devices.json');
 let db={devices:{}};try{db=JSON.parse(await readFile(dbPath,'utf8'));}catch(e){if(e.code!=='ENOENT')throw e;}
 let now=()=>Date.now(),owner='human',lease=1,browser,browserPromise,epoch=0,transitioning=false,queue=Promise.resolve();
 const streams=new Map();const pending=new Map();const pairLimits=new Map();
 const save=async()=>{await writeFile(dbPath+'.tmp',JSON.stringify(db),{mode:0o600});await rename(dbPath+'.tmp',dbPath);};
 let saveQueue=Promise.resolve();const persist=()=>saveQueue=saveQueue.then(save);
 const admin=req=>safeEqual(req.headers.authorization,'Bearer '+adminToken);
 const device=req=>{const raw=(req.headers.cookie||'').split(';').map(v=>v.trim()).find(v=>v.startsWith('charlie_device='))?.slice(15);const id=raw?hash(raw):'';const d=db.devices[id];return d&&d.expires>now()?{id,...d}:null;};
 const originOk=req=>{const expected=publicOrigin||`${allowHttp?'http':'https'}://${req.headers.host}`;return req.headers.origin===expected;};
 const state=()=>({owner,lease,transitioning,aiAvailable:true});
 const closeStreams=id=>{for(const [ws,entry]of streams)if(!id||entry.id===id){entry.tcp.destroy();ws.terminate();}};
 async function page(){
  if(!browser?.isConnected()){
   if(!browserPromise){const started=epoch;browserPromise=chromium.connectOverCDP(cdp,{timeout:6000}).then(async b=>{if(started!==epoch){await b.close();throw fail(409,'Control changed');}return browser=b;}).finally(()=>browserPromise=null);}
   await browserPromise;
  }
  const ctx=browser.contexts()[0];const pages=ctx.pages();return pages.find(p=>!p.isClosed())||await ctx.newPage();
 }
 const sequential=fn=>{const run=queue.then(fn,fn);queue=run.catch(()=>{});return run;};
 async function transfer(next){
  if(transitioning)throw fail(409,'Control handoff is already in progress');
  transitioning=true;lease++;epoch++;closeStreams();
  const attached=browser;browser=undefined;
  try{if(attached){for(const ctx of attached.contexts())for(const p of ctx.pages()){try{const session=await ctx.newCDPSession(p);await session.send('Page.stopLoading');await session.detach();}catch{}}await attached.close();}
   await queue; if(browserPromise)try{await browserPromise;}catch{} owner=next;
  }finally{transitioning=false;}
 }
 const checkLease=expected=>{if(transitioning||owner!=='ai'||expected!==lease)throw fail(409,'Charlie has control. Ask for AI’s turn first.');};
 async function action(p,input){
  if(input.type==='navigate')await p.goto(navigation(input.url),{waitUntil:'domcontentloaded',timeout:20000});
  else if(input.type==='click')await p.locator(input.selector).click({timeout:5000});
  else if(input.type==='type')await p.locator(input.selector).fill(String(input.text),{timeout:5000});
  else if(input.type==='press')await p.keyboard.press(input.key);
  else if(input.type==='scroll')await p.mouse.wheel(0,Math.max(-1500,Math.min(1500,Number(input.y)||0)));
  else throw fail(400,'Unknown browser action');
 }
 const server=http.createServer(async(req,res)=>{
  const json=(status,data)=>{res.writeHead(status,{'content-type':'application/json','cache-control':'no-store'});res.end(JSON.stringify(data));};
  res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Referrer-Policy','no-referrer');
  res.setHeader('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data: blob:; connect-src 'self'; worker-src 'self' blob:; frame-ancestors 'none'; base-uri 'none'; form-action 'self'");
  if(!allowHttp)res.setHeader('Strict-Transport-Security','max-age=31536000');
  try{
   const path=new URL(req.url,'http://local').pathname;
   if(req.method==='POST'&&!path.startsWith('/api/admin/')&&!path.startsWith('/api/agent/')&&!originOk(req))throw fail(403,'Open the app directly to use this control');
   if(path==='/api/health'&&req.method==='GET'){
    const display=await new Promise(r=>{const socket=net.connect(vncPort,'127.0.0.1');socket.setTimeout(1000);socket.once('connect',()=>{socket.destroy();r(true);});socket.once('error',()=>r(false));socket.once('timeout',()=>{socket.destroy();r(false);});});
    let chrome=false;try{const r=await fetch(cdp+'/json/version',{signal:AbortSignal.timeout(1000)});const j=await r.json();chrome=r.ok&&typeof j.webSocketDebuggerUrl==='string';}catch{}
    return json(display&&chrome?200:503,{ready:display&&chrome});
   }
   if(path==='/api/pair'&&req.method==='POST'){
    for(const [id,d]of pending)if(d.expires<=now())pending.delete(id);
    for(const [ip,limit]of pairLimits)if(limit.until<=now())pairLimits.delete(ip);
    const forwarded=req.headers['x-real-ip'];const ip=trustProxy&&typeof forwarded==='string'&&net.isIP(forwarded)?forwarded:req.socket.remoteAddress;
    const limit=pairLimits.get(ip)||{count:0,until:now()+10*60*1000};if(limit.count>=6||pending.size>=1000)throw fail(429,'Too many pairing requests. Try shortly.');limit.count++;pairLimits.set(ip,limit);
    const raw=token(),id=hash(raw);let code;do{code=randomBytes(4).toString('hex').toUpperCase();}while([...pending.values()].some(v=>v.code===code));
    const expires=now()+10*60*1000;pending.set(id,{code,expires});
    res.setHeader('Set-Cookie',`charlie_device=${raw}; HttpOnly; SameSite=Strict; Path=/; Max-Age=2592000${allowHttp?'':'; Secure'}`);
    return json(201,{code,expires});
   }
   if(path.startsWith('/api/admin/')){
    if(!admin(req))throw fail(401,'Authorisation required');
    if(path==='/api/admin/pending'&&req.method==='GET')return json(200,{pending:[...pending.values()].filter(v=>v.expires>now()).map(({code,expires})=>({code,expires}))});
    if(path==='/api/admin/approve'&&req.method==='POST'){
     const {code}=await body(req);const match=[...pending].find(([,v])=>v.code===code&&v.expires>now());
     if(!match)throw fail(404,'Pairing request expired or not found');
     db.devices[match[0]]={expires:now()+30*24*3600000};await persist();pending.delete(match[0]);return json(200,{approved:true});
    }
    throw fail(404,'Unknown admin route');
   }
   if(path.startsWith('/api/agent/')){
    if(!admin(req))throw fail(401,'Authorisation required');
    if(path==='/api/agent/status')return json(200,state());
    checkLease(lease);
    if(path==='/api/agent/snapshot'&&req.method==='GET'){
     const expected=lease;return await sequential(async()=>{checkLease(expected);const p=await page();checkLease(expected);const png=await p.screenshot();checkLease(expected);res.writeHead(200,{'content-type':'image/png','cache-control':'no-store'});res.end(png);});
    }
    if(path==='/api/agent/action'&&req.method==='POST'){
     const input=await body(req);checkLease(input.lease);
     return await sequential(async()=>{checkLease(input.lease);const p=await page();checkLease(input.lease);await action(p,input);checkLease(input.lease);return json(200,{ok:true,url:p.url(),...state()});});
    }
    throw fail(404,'Unknown agent route');
   }
   if(path.startsWith('/api/')){
    const d=device(req);if(!d)throw fail(401,'Approve this device first');
    if(path==='/api/session'&&req.method==='GET')return json(200,state());
    if(path==='/api/logout'&&req.method==='POST'){delete db.devices[d.id];await persist();closeStreams(d.id);await transfer('human');res.setHeader('Set-Cookie',`charlie_device=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0${allowHttp?'':'; Secure'}`);return json(200,{ok:true});}
    if(path==='/api/control'&&req.method==='POST'){
     const input=await body(req);if(!['human','ai'].includes(input.owner))throw fail(400,'Invalid control');await transfer(input.owner);return json(200,state());
    }
    if(path==='/api/navigate'&&req.method==='POST'){
     const input=await body(req);const url=navigation(input.url);if(transitioning||owner!=='human')throw fail(409,'Choose My turn first');
     const expected=lease;await sequential(async()=>{if(owner!=='human'||lease!==expected)throw fail(409,'Control changed');const p=await page();if(transitioning||owner!=='human'||lease!==expected)throw fail(409,'Control changed');await action(p,{type:'navigate',url});});return json(200,{ok:true});
    }
    if(path==='/api/key'&&req.method==='POST'){
     const input=await body(req);if(transitioning||owner!=='human')throw fail(409,'Choose My turn first');
     if(!['Enter','Tab','Backspace','Escape','ArrowUp','ArrowDown','ArrowLeft','ArrowRight','Alt+ArrowLeft','Alt+ArrowRight','Control+r'].includes(input.key))throw fail(400,'Unsupported key');
     const expected=lease;await sequential(async()=>{const p=await page();if(transitioning||owner!=='human'||lease!==expected)throw fail(409,'Control changed');await p.keyboard.press(input.key);});return json(200,{ok:true});
    }
    if(path==='/api/text'&&req.method==='POST'){
     const input=await body(req);if(transitioning||owner!=='human')throw fail(409,'Choose My turn first');
     const expected=lease;await sequential(async()=>{const p=await page();if(transitioning||owner!=='human'||lease!==expected)throw fail(409,'Control changed');const focused=await Promise.all(p.frames().map(frame=>frame.evaluate(()=>{let e=document.activeElement;while(e?.shadowRoot?.activeElement)e=e.shadowRoot.activeElement;return document.hasFocus()&&!!e&&(e.isContentEditable||((e.tagName==='TEXTAREA'||(e.tagName==='INPUT'&&['text','search','email','password','url','tel','number'].includes(e.type)))&&!e.readOnly&&!e.disabled));}).catch(()=>false)));if(!focused.some(Boolean))throw fail(409,'Tap a text field in the browser, then press Send again. Your typing is kept here.');if(transitioning||owner!=='human'||lease!==expected)throw fail(409,'Control changed');await p.keyboard.insertText(String(input.text||'').slice(0,10000));});return json(200,{ok:true});
    }
    if(path==='/api/screen')throw fail(404,'Use the authenticated display stream');
    throw fail(404,'Unknown API route');
   }
   if(req.method!=='GET'&&req.method!=='HEAD')throw fail(405,'Method not allowed');
   let base,pathPart;
   if(path.startsWith('/vendor/')){base=resolve(root,'node_modules/@novnc/novnc');pathPart=path.slice(8);}
   else{base=resolve(root,'public');pathPart=path==='/'?'index.html':decodeURIComponent(path.slice(1));}
   const file=resolve(base,pathPart);if(!file.startsWith(base+'/')||!(await stat(file)).isFile())throw fail(404,'Not found');
   const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.json':'application/json','.webmanifest':'application/manifest+json','.png':'image/png'};
   res.writeHead(200,{'content-type':types[extname(file)]||'application/octet-stream','cache-control':'no-cache'});res.end(await readFile(file));
  }catch(e){if(!res.headersSent)json(e.status||503,{error:e.status?e.message:'Browser temporarily unavailable. Reconnect shortly.'});else res.end();}
 });
 const wss=new WebSocketServer({noServer:true,perMessageDeflate:false,maxPayload:1024*1024});
 server.on('upgrade',(req,socket,head)=>{
  const d=device(req);
  if(req.url!=='/stream'||!d||!originOk(req)||transitioning||owner!=='human')return socket.end('HTTP/1.1 403 Forbidden\r\nConnection: close\r\n\r\n');
  wss.handleUpgrade(req,socket,head,ws=>{
   const tcp=net.connect(vncPort,'127.0.0.1');const openedLease=lease;streams.set(ws,{id:d.id,tcp,lease:openedLease});
   tcp.on('data',data=>{if(ws.readyState===1)ws.send(data,{binary:true});});
   ws.on('message',data=>{if(!transitioning&&owner==='human'&&lease===openedLease&&device(req))tcp.write(data);else{tcp.destroy();ws.terminate();}});
   tcp.on('error',()=>ws.close(1011,'Display reconnecting'));tcp.on('close',()=>ws.close());
   ws.on('close',()=>{tcp.destroy();streams.delete(ws);});ws.on('error',()=>tcp.destroy());
  });
 });
 const heartbeat=setInterval(()=>{for(const [ws,entry]of streams)if(!db.devices[entry.id]||db.devices[entry.id].expires<=now())ws.close();},30000);heartbeat.unref();
 server.on('close',()=>{clearInterval(heartbeat);closeStreams();browser?.close().catch(()=>{});});
 async function close(){transitioning=true;lease++;epoch++;closeStreams();const attached=browser;browser=undefined;await attached?.close();if(browserPromise)try{await browserPromise;}catch{}server.closeAllConnections();await new Promise(r=>server.close(r));wss.close();}
 return {server,close,setClock:fn=>now=fn};
}
if(process.argv[1]===fileURLToPath(import.meta.url)){
 const dataDir=process.env.BROWSER_DATA_DIR||'/workspace/charlie-browser-private/gateway';await mkdir(dataDir,{recursive:true,mode:0o700});
 const secretPath=resolve(dataDir,'admin-token');let adminToken;try{adminToken=(await readFile(secretPath,'utf8')).trim();}catch(e){if(e.code!=='ENOENT')throw e;adminToken=token();await writeFile(secretPath,adminToken,{mode:0o600});}
 const app=await createApp({dataDir,adminToken,allowHttp:process.env.ALLOW_HTTP==='1',publicOrigin:process.env.APP_ORIGIN,trustProxy:process.env.TRUST_PROXY==='1',cdp:process.env.BROWSER_CDP||'http://127.0.0.1:9222'});
 process.on('SIGTERM',async()=>{await app.close();process.exit(0);});process.on('SIGINT',async()=>{await app.close();process.exit(0);});
 app.server.listen(Number(process.env.PORT||8787),process.env.GATEWAY_BIND||'127.0.0.1',()=>console.log('Private browser gateway listening'));
}
