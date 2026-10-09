import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createApp } from '../server.mjs';
async function fixture(t, dir, options={}) {
 const dataDir=dir||await mkdtemp(join(tmpdir(),'charlie-browser-test-'));
 if(!dir)t.after(()=>rm(dataDir,{recursive:true,force:true}));
 const app=await createApp({dataDir,adminToken:'test-admin-token',allowHttp:true,...options});
 await new Promise(r=>app.server.listen(0,'127.0.0.1',r));
 t.after(()=>new Promise(r=>app.server.close(r)));
 const origin=`http://127.0.0.1:${app.server.address().port}`;
 const request=(path,body,cookie,admin=false)=>fetch(origin+path,{method:body?'POST':'GET',headers:{origin,...(body?{'content-type':'application/json'}:{}),...(cookie?{cookie}:{}),...(admin?{authorization:'Bearer test-admin-token'}:{})},body:body?JSON.stringify(body):undefined});
 return {app,dataDir,origin,request};
}
async function pair(f) {
 const res=await f.request('/api/pair',{});assert.equal(res.status,201);
 const cookie=res.headers.get('set-cookie').split(';')[0];
 const {code}=await res.json();
 assert.equal((await f.request('/api/admin/approve',{code},null,true)).status,200);
 assert.equal((await f.request('/api/session',null,cookie)).status,200);return cookie;
}
test('browser stream requires an approved device',async t=>{
 const f=await fixture(t);assert.equal((await f.request('/api/session')).status,401);
 assert.equal((await f.request('/api/screen')).status,401);
});
test('pairing code alone cannot authenticate another device',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 assert.equal((await f.request('/api/session')).status,401);
 assert.equal((await f.request('/api/admin/approve',{code:'bogus'})).status,401);
 assert.equal((await f.request('/api/session',null,cookie)).status,200);
});
test('approved session survives restart and more than 15 minutes',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 await new Promise(r=>f.app.server.close(r));
 const g=await fixture(t,f.dataDir);g.app.setClock(()=>Date.now()+16*60*1000);
 assert.equal((await g.request('/api/session',null,cookie)).status,200);
});
test('cross-site takeover is rejected',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 const res=await fetch(f.origin+'/api/control',{method:'POST',headers:{origin:'https://evil.example','content-type':'application/json',cookie},body:'{"owner":"ai"}'});
 assert.equal(res.status,403);
});
test('human takeover revokes the AI lease and forbids screenshots',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 assert.equal((await f.request('/api/agent/snapshot',null,null,true)).status,409);
 const res=await f.request('/api/control',{owner:'ai'},cookie);assert.equal(res.status,200);
 const ai=await res.json();const human=await (await f.request('/api/control',{owner:'human'},cookie)).json();
 assert.ok(human.lease>ai.lease);
 assert.equal((await f.request('/api/agent/action',{type:'navigate',url:'https://example.com',lease:ai.lease},null,true)).status,409);
});
test('unsafe navigation schemes are rejected before reaching Chromium',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 for(const url of ['javascript:alert(1)','file:///etc/passwd','data:text/html,bad'])
 assert.equal((await f.request('/api/navigate',{url},cookie)).status,400);
});
test('logout revokes the session',async t=>{
 const f=await fixture(t);const cookie=await pair(f);
 assert.equal((await f.request('/api/logout',{},cookie)).status,200);
 assert.equal((await f.request('/api/session',null,cookie)).status,401);
});

test('unapproved and cross-site WebSocket streams are rejected',async t=>{
 const {WebSocket}=await import('ws');const f=await fixture(t);const cookie=await pair(f);
 async function denied(headers){return new Promise((resolve,reject)=>{const ws=new WebSocket(f.origin.replace('http:','ws:')+'/stream',{headers});ws.on('unexpected-response',(req,res)=>{res.resume();ws.terminate();resolve(res.statusCode);});ws.on('open',()=>{ws.terminate();reject(new Error('Unauthorised stream opened'));});ws.on('error',()=>{});});}
 assert.equal(await denied({origin:f.origin}),403);
 assert.equal(await denied({origin:'https://evil.example',cookie}),403);
 await f.request('/api/control',{owner:'ai'},cookie);
 assert.equal(await denied({origin:f.origin,cookie}),403);
});

test('readiness fails when the browser or display is unavailable',async t=>{
 const dataDir=await mkdtemp(join(tmpdir(),'charlie-health-'));t.after(()=>rm(dataDir,{recursive:true,force:true}));
 const app=await createApp({dataDir,adminToken:'test-health-token',allowHttp:true,cdp:'http://127.0.0.1:1',vncPort:1});
 await new Promise(r=>app.server.listen(0,'127.0.0.1',r));t.after(()=>new Promise(r=>app.server.close(r)));
 const r=await fetch(`http://127.0.0.1:${app.server.address().port}/api/health`);
 assert.equal(r.status,503);assert.deepEqual(await r.json(),{ready:false});
});

test('one source cannot fill pairing capacity for another phone',async t=>{
 const f=await fixture(t,null,{trustProxy:true});
 async function pairFrom(ip){return fetch(f.origin+'/api/pair',{method:'POST',headers:{origin:f.origin,'content-type':'application/json','x-real-ip':ip},body:'{}'});}
 let blocked=0;for(let i=0;i<20;i++)if((await pairFrom('192.0.2.1')).status===429)blocked++;
 assert.ok(blocked>0,'burst is rate limited');
 assert.equal((await pairFrom('192.0.2.2')).status,201,'another phone can still pair');
});

test('shutdown closes an active approved display stream',async t=>{
 const net=await import('node:net');const {WebSocket}=await import('ws');
 let upstream;const vnc=net.createServer(s=>upstream=s);await new Promise(r=>vnc.listen(0,'127.0.0.1',r));
 const f=await fixture(t,null,{vncPort:vnc.address().port});const cookie=await pair(f);
 const ws=new WebSocket(f.origin.replace('http:','ws:')+'/stream',{headers:{origin:f.origin,cookie}});ws.on('error',()=>{});
 await new Promise(r=>ws.once('open',r));
 try{await Promise.race([f.app.close(),new Promise((_,reject)=>{const timer=setTimeout(()=>reject(new Error('Shutdown hung with a live stream')),1500);timer.unref();})]);assert.equal(f.app.server.listening,false);}
 finally{ws.terminate();upstream?.destroy();await new Promise(r=>vnc.close(r));}
});
