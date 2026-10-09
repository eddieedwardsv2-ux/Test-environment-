import {spawn} from 'node:child_process';
import {setTimeout as delay} from 'node:timers/promises';
import net from 'node:net';
const children=[];let stopping=false;let runtime;
function start(command,args){const child=spawn(command,args,{stdio:'inherit'});children.push(child);child.on('error',()=>stop(1));child.on('exit',code=>{if(!stopping)stop(code||1);});return child;}
async function stop(code){if(stopping)return;stopping=true;if(runtime&&runtime.exitCode===null){runtime.kill('SIGTERM');await Promise.race([new Promise(r=>runtime.once('exit',r)),delay(25000)]);}for(const c of children)if(c!==runtime)c.kill('SIGTERM');setTimeout(()=>process.exit(code),1000);}
async function ready(port){const deadline=Date.now()+30000;while(Date.now()<deadline){const ok=await new Promise(r=>{const s=net.connect(port,'127.0.0.1');s.on('connect',()=>{s.destroy();r(true);});s.on('error',()=>r(false));});if(ok)return;await delay(200);}throw new Error('Service did not become ready');}
process.on('SIGTERM',()=>stop(0));process.on('SIGINT',()=>stop(0));
try{start('Xvfb',[':99','-screen','0','430x720x24','-ac','-nolisten','tcp']);await delay(600);start('x11vnc',['-display',':99','-rfbport','5900','-localhost','-forever','-shared','-nopw','-noxdamage','-quiet']);await ready(5900);start('node',['server.mjs']);await ready(8787);runtime=start('node',['runtime.mjs']);await ready(9222);}catch(e){console.error('Browser stack startup failed:',e.message);stop(1);}
