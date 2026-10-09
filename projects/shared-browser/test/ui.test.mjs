import {test} from 'node:test';
import assert from 'node:assert/strict';
import {chromium} from 'playwright-core';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createApp} from '../server.mjs';
test('iPhone screen fits portrait and landscape with usable touch controls',async t=>{
 const dataDir=await mkdtemp(join(tmpdir(),'charlie-ui-'));
 const app=await createApp({dataDir,adminToken:'ui-test-token',allowHttp:true});
 await new Promise(r=>app.server.listen(0,'127.0.0.1',r));
 const origin=`http://127.0.0.1:${app.server.address().port}`;
 const b=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 t.after(async()=>{await b.close();await new Promise(r=>app.server.close(r));await rm(dataDir,{recursive:true,force:true});});
 const ctx=await b.newContext({viewport:{width:430,height:932},isMobile:true,hasTouch:true});const p=await ctx.newPage();
 const errors=[];p.on('pageerror',e=>errors.push(e.message));
 await p.goto(origin);
 assert.equal(await p.title(),"Charlie's Browser");
 await p.getByRole('button',{name:'Connect this iPhone'}).click();
 await p.locator('#pair-code').waitFor({state:'visible'});
 const code=await p.locator('#pair-code').textContent();
 await fetch(origin+'/api/admin/approve',{method:'POST',headers:{authorization:'Bearer ui-test-token','content-type':'application/json'},body:JSON.stringify({code})});
 await p.locator('#workspace').waitFor({state:'visible'});
 for(const viewport of [{width:430,height:932},{width:932,height:430}]){
  await p.setViewportSize(viewport);
  assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  for(const id of ['human-turn','ai-turn','keyboard','reconnect']){
   const box=await p.locator('#'+id).boundingBox();assert.ok(box.height>=44&&box.width>=44,id+' touch area');
  }
 }
 await p.getByRole('button',{name:'Keyboard',exact:true}).click();
 assert.equal(await p.locator('#type-text').isVisible(),true);
 assert.deepEqual(errors,[]);
});
