// Run from repo root: node tools/test_hands_actions.cjs
// Faithful adapter contract tests, not proof of live Claude permissions/rendering.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const html=fs.readFileSync('research/hands/site/template.html','utf8');
const esc=html.match(/^const esc = .*$/m)[0];
const source=esc+'\n'+html.slice(html.indexOf('// Hands actions'),html.indexOf('function match(t)'));
function harness(){
 const elements={},disk={},get=id=>elements[id]??={textContent:'',innerHTML:'',value:'',disabled:false};
 const context={document:{getElementById:get},window:{},localStorage:{getItem:k=>disk[k],setItem:(k,v)=>disk[k]=v},crypto:require('node:crypto').webcrypto};
 vm.createContext(context);vm.runInContext(source,context);
 return {context,disk,get,run:s=>vm.runInContext(s,context),choose:(action,note='')=>{get('tool-action').value=action;get('tool-note').value=note;}};
}
const tool='{id:"n:creativeclaw",name:"CreativeClaw",url:"https://creativeclaw.co"}';
(async()=>{
 let checks=0;
 const h=harness();await h.run('connectActions()');h.choose('check','Read costs');
 await h.run(`saveAction(${tool})`);assert.equal(h.run('Object.values(actionRows)[0].action'),'check');assert(h.get('action-status').textContent.includes('device only'));checks++;
 const first=h.run('Object.keys(actionRows)[0]');await h.run(`saveAction(${tool})`);assert.equal(h.run('Object.keys(actionRows).length'),1);checks++;
 h.choose('implement','After checking');await h.run(`saveAction(${tool})`);assert.equal(h.run('Object.keys(actionRows).length'),2);assert(JSON.parse(h.disk['hands-actions'])[first]);checks++;
 h.run('actionRows={}');await h.run('connectActions()');assert.equal(h.run('Object.keys(actionRows).length'),2);checks++;
 const corrupt=harness();corrupt.disk['hands-actions']='invalid';await corrupt.run('connectActions()');corrupt.choose('check');await corrupt.run(`saveAction(${tool})`);assert.equal(corrupt.run('actionReady'),false);assert.equal(corrupt.disk['hands-actions'],'invalid');checks++;
 const remote=harness();let snapshot,onError,saved,release,writes=0;
 remote.context.window.claude={use:async()=>({collection:name=>{assert.equal(name,'tool_actions');return {onSnapshot:(s,e)=>{snapshot=s;onError=e},doc:id=>({set:r=>{writes++;saved={id,row:r};return new Promise(resolve=>{release=resolve})}})}}})};
 await remote.run('connectActions()');remote.choose('search');await remote.run(`saveAction(${tool})`);assert.equal(writes,0);snapshot({docs:[]});checks++;
 remote.run(`actionPanel(${tool})`);const pending=remote.run(`saveAction(${tool})`);assert(remote.get('send-action').disabled);await remote.run(`saveAction(${tool})`);assert.equal(writes,1);assert(saved.id.endsWith(saved.row.requestId));release();await pending;checks++;
 onError();assert.equal(remote.run('actionReady'),false);snapshot({docs:[]});assert.equal(remote.run('actionReady'),true);assert(!remote.get('queue-connection').textContent.includes('Could not'));checks++;
 snapshot({docs:[{id:'working',data:()=>({item:'n:creativeclaw',title:'CreativeClaw',action:'check',status:'in_progress',createdAt:'2026-10-09T00:00:00Z'})}]});assert(remote.get('send-action').disabled);await remote.run(`saveAction(${tool})`);assert.equal(writes,1);checks++;
 snapshot({docs:[]});remote.run('actionDb={collection:()=>({doc:()=>({set:async()=>{throw Error("permission denied")}})})}');await remote.run(`saveAction(${tool})`);assert(remote.get('action-status').textContent.startsWith('Not saved'));assert.equal(remote.run('Object.keys(actionRows).length'),0);checks++;
 remote.choose('delete');await remote.run(`saveAction(${tool})`);assert.equal(remote.run('Object.keys(actionRows).length'),0);checks++;
 h.run('actionRows={old:{item:"x",title:"Old",action:"search",createdAt:"2026-10-08",updatedAt:"2026-10-10"},new:{item:"x",title:"New",action:"check",createdAt:"2026-10-09",updatedAt:"2026-10-09"}}');assert.equal(h.run('latestAction("x").title'),'New');checks++;
 h.run('actionRows={x:{item:"x",title:"<img src=x onerror=alert(1)>",action:"check",note:"</textarea><script>x</script>",status:"answered"}};renderActions()');assert(!h.get('action-queue').innerHTML.includes('<img'));assert(!h.run('actionPanel({id:"x"})').includes('<script>'));checks++;
 assert(html.includes('${actionPanel(t)}'));assert(html.includes('button class="rank-item" data-id='));checks++;
 console.log(`PASS ${checks} Hands decision checks (mocked adapter; live persistence and visual QA remain separate).`);
})().catch(e=>{console.error(e);process.exitCode=1});
