import RFBModule from '@novnc/novnc/lib/rfb.js';
const RFB=RFBModule.default||RFBModule;
const $=id=>document.getElementById(id);let rfb,paired=false,owner='human',reconnectTimer,pollTimer,lastOwner;
async function api(path,body){const r=await fetch('/api/'+path,{method:body?'POST':'GET',headers:body?{'content-type':'application/json'}:{},body:body?JSON.stringify(body):undefined,cache:'no-store'});const j=await r.json();if(!r.ok)throw Object.assign(new Error(j.error),{status:r.status});return j;}
function message(s){$('message').textContent=s;}
function disconnect(){const previous=rfb;rfb=null;previous?.disconnect();}
function connect(){clearTimeout(reconnectTimer);if(!paired||owner!=='human')return;disconnect();$('screen').replaceChildren();$('connection').textContent='Connecting';$('connection').classList.remove('live');
 const next=new RFB($('screen'),`${location.protocol==='https:'?'wss':'ws'}://${location.host}/stream`);rfb=next;next.scaleViewport=true;next.clipViewport=false;next.resizeSession=false;next.background='#080c12';next.qualityLevel=6;next.compressionLevel=2;
 next.addEventListener('connect',()=>{if(rfb!==next)return;$('connection').textContent='Connected';$('connection').classList.add('live');message('');});
 next.addEventListener('disconnect',()=>{if(rfb!==next)return;rfb=null;$('connection').textContent=owner==='ai'?'AI has control':'Reconnecting';$('connection').classList.remove('live');if(owner==='human'&&paired)reconnectTimer=setTimeout(connect,2500);});
}
function applyState(s){owner=s.transitioning?'switching':s.owner;$('human-turn').classList.toggle('active',owner==='human');$('ai-turn').classList.toggle('active',owner==='ai');$('screen-overlay').hidden=owner==='human';if(owner!=='human'){disconnect();$('connection').textContent='AI has control';}else if(lastOwner!=='human')connect();lastOwner=owner;}
async function poll(){try{const s=await api('session');if(!paired){paired=true;$('pairing').hidden=true;$('workspace').hidden=false;}applyState(s);}catch(e){if(e.status===401&&paired){paired=false;disconnect();$('workspace').hidden=true;$('pairing').hidden=false;$('pair-button').hidden=false;$('pair-pending').hidden=true;}else if(paired)message('Connection interrupted. Your browser is still saved.');}pollTimer=setTimeout(poll,2000);}
$('pair-button').onclick=async()=>{try{const p=await api('pair',{});$('pair-code').textContent=p.code;$('pair-pending').hidden=false;$('pair-button').hidden=true;setTimeout(()=>{if(!paired){$('pair-error').textContent='Pairing expired. Request a new code.';$('pair-button').hidden=false;$('pair-pending').hidden=true;}},Math.max(0,p.expires-Date.now()));}catch(e){$('pair-error').textContent=e.message;}};
for(const [id,turn]of [['human-turn','human'],['ai-turn','ai']])$(id).onclick=async()=>{try{applyState(await api('control',{owner:turn}));}catch(e){message(e.message);}};
$('reconnect').onclick=()=>{if(owner==='human')connect();else message('Choose My turn to reconnect.');};
$('address-form').onsubmit=async e=>{e.preventDefault();let url=$('address').value.trim();if(!/^[a-z]+:/i.test(url))url='https://'+url;try{message('Opening website…');await api('navigate',{url});message('');}catch(e){message(e.message);}};
async function key(value){try{await api('key',{key:value});}catch(e){message(e.message);}}
$('back').onclick=()=>key('Alt+ArrowLeft');$('forward').onclick=()=>key('Alt+ArrowRight');
$('keyboard').onclick=()=>{$('keyboard-panel').hidden=!$('keyboard-panel').hidden;if(!$('keyboard-panel').hidden)$('type-text').focus();};
$('keyboard-panel').onsubmit=async e=>{e.preventDefault();try{await api('text',{text:$('type-text').value});$('type-text').value='';$('type-text').focus();}catch(e){message(e.message);}};
$('enter-key').onclick=()=>key('Enter');$('backspace-key').onclick=()=>key('Backspace');
$('logout').onclick=async()=>{try{await api('logout',{});paired=false;disconnect();location.reload();}catch(e){message(e.message);}};
addEventListener('online',()=>{if(paired&&owner==='human')connect();});addEventListener('pagehide',()=>{clearTimeout(pollTimer);clearTimeout(reconnectTimer);disconnect();});addEventListener('pageshow',e=>{if(e.persisted)poll();});
if('serviceWorker'in navigator)navigator.serviceWorker.register('/sw.js').catch(()=>{});poll();
