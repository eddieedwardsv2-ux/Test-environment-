import assert from 'node:assert/strict';
import {chromium} from 'playwright-core';
import {createApp} from '../server.mjs';
import {mkdtemp,rm,mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';import {join} from 'node:path';
const dataDir=await mkdtemp(join(tmpdir(),'charlie-live-'));let app,server,client,remote;
try{
 app=await createApp({dataDir,adminToken:'live-test-token',allowHttp:true});server=app.server;
 await new Promise(r=>server.listen(0,'127.0.0.1',r));const origin=`http://127.0.0.1:${server.address().port}`;
 remote=await chromium.connectOverCDP('http://127.0.0.1:9222');const tab=remote.contexts()[0].pages()[0];tab.setDefaultTimeout(10000);
 const response=await tab.goto(origin+'/welcome.html');assert.equal(response.status(),200);await tab.bringToFront();await tab.locator('#keyboard-test').waitFor();await tab.context().addCookies([{name:'retention-test',value:'retained',url:origin,expires:Math.floor(Date.now()/1000)+86400}]);
 client=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const phone=await client.newContext({viewport:{width:430,height:932},isMobile:true,hasTouch:true});const p=await phone.newPage();p.setDefaultTimeout(10000);
 const errors=[];p.on('pageerror',e=>errors.push(e.message));await p.goto(origin);await p.locator('#pair-button').click();await p.locator('#pair-code').waitFor({state:'visible'});const code=await p.locator('#pair-code').textContent();
 await fetch(origin+'/api/admin/approve',{method:'POST',headers:{authorization:'Bearer live-test-token','content-type':'application/json'},body:JSON.stringify({code})});
 try{await p.locator('#connection.live').waitFor({timeout:15000});console.log('Live stream connected');}catch(e){console.log('STATUS:',await p.locator('#connection').textContent());throw e;}
 const rect=await p.locator('#screen canvas').boundingBox();assert.ok(rect.width>250&&rect.height>400,'live video fills phone');
 const input=await tab.locator('#keyboard-test').boundingBox();
 await p.touchscreen.tap(rect.x+(input.x+input.width/2)*rect.width/430,rect.y+(input.y+input.height/2)*rect.height/720);
 await p.locator('#keyboard').click();await p.locator('#type-text').fill('Phone keyboard works');await p.getByRole('button',{name:'Send',exact:true}).click();
 await tab.waitForFunction(()=>document.querySelector('#keyboard-test').value==='Phone keyboard works',null,{timeout:5000,polling:100});
 console.log('Touch and keyboard verified');await p.locator('#keyboard').click();
 await p.locator('#ai-turn').click();await p.locator('#screen-overlay').waitFor({state:'visible'});
 const status=await (await fetch(origin+'/api/agent/status',{headers:{authorization:'Bearer live-test-token'}})).json();
 let res=await fetch(origin+'/api/agent/action',{method:'POST',headers:{authorization:'Bearer live-test-token','content-type':'application/json'},body:JSON.stringify({type:'type',selector:'#keyboard-test',text:'Codex uses the same tab',lease:status.lease})});assert.equal(res.status,200);
 assert.equal(await tab.locator('#keyboard-test').inputValue(),'Codex uses the same tab');
 res=await fetch(origin+'/api/agent/snapshot',{headers:{authorization:'Bearer live-test-token'}});assert.equal(res.status,200);assert.equal(res.headers.get('content-type'),'image/png');
 console.log('AI action and snapshot verified');await p.locator('#human-turn').click();await p.locator('#connection.live').waitFor();
 res=await fetch(origin+'/api/agent/snapshot',{headers:{authorization:'Bearer live-test-token'}});assert.equal(res.status,409);
 await p.locator('#reconnect').click();await p.locator('#connection.live').waitFor();
 assert.equal(await tab.locator('#keyboard-test').inputValue(),'Codex uses the same tab');
 assert.equal((await tab.context().cookies(origin)).find(c=>c.name==='retention-test').value,'retained');
 console.log('Takeover and reconnect verified');await mkdir('/tmp/charlie-browser-proof',{recursive:true});await p.screenshot({path:'/tmp/charlie-browser-proof/iphone.png'});
 await p.setViewportSize({width:932,height:430});await p.screenshot({path:'/tmp/charlie-browser-proof/landscape.png'});
 console.log('Screenshots captured');assert.deepEqual(errors,[]);
 await tab.goto('http://127.0.0.1:8787/welcome.html',{waitUntil:'domcontentloaded',timeout:5000});
console.log('Test page restored');}finally{console.log('Closing test client');await client?.close();console.log('Client closed');/* Do not close the shared Chromium. */if(remote)await remote.close();console.log('CDP disconnected');if(app)await app.close();console.log('Test gateway closed');await rm(dataDir,{recursive:true,force:true});}

console.log("LIVE VERIFIED: touch, phone keyboard, same-tab Codex action, ownership, reconnect and cookie retention");
