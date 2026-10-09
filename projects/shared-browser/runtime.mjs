import {chromium} from 'playwright-core';
import {mkdir,access} from 'node:fs/promises';
import {homedir} from 'node:os';import {resolve} from 'node:path';import {execFile} from 'node:child_process';import {promisify} from 'node:util';
process.env.PLAYWRIGHT_DISABLE_FORCED_CHROMIUM_PROXIED_LOOPBACK='1';
const dir=process.env.BROWSER_PROFILE_DIR||'/workspace/charlie-browser-private/profile';await mkdir(dir,{recursive:true,mode:0o700});
// Optional private-host proxy root, explicitly supplied by the operator.
// Import trust normally; never disable Chromium TLS verification.
if(process.env.BROWSER_TRUSTED_CA){const nss=resolve(homedir(),'.pki/nssdb');await mkdir(nss,{recursive:true,mode:0o700});const run=promisify(execFile);try{await access(resolve(nss,'cert9.db'));}catch{await run('certutil',['-N','--empty-password','-d','sql:'+nss]);}await run('certutil',['-A','-d','sql:'+nss,'-n','Private host proxy CA','-t','C,,','-i',process.env.BROWSER_TRUSTED_CA]);}
const url=process.env.https_proxy||process.env.HTTPS_PROXY;let proxy;
if(url){const p=new URL(url);proxy={server:`${p.protocol}//${p.hostname}:${p.port}`,bypass:'127.0.0.1,localhost',...(p.username?{username:decodeURIComponent(p.username),password:decodeURIComponent(p.password)}:{})};}
const ctx=await chromium.launchPersistentContext(dir,{executablePath:'/usr/bin/chromium',headless:false,chromiumSandbox:true,viewport:null,ignoreDefaultArgs:['--enable-automation'],env:{...process.env,DISPLAY:':99'},proxy,args:['--remote-debugging-port=9222','--app=http://127.0.0.1:8787/welcome.html','--window-position=0,0','--kiosk','--window-size=430,720','--force-device-scale-factor=1','--no-first-run']});
let p=ctx.pages().find(p=>p.url().includes('/welcome.html'));if(!p)p=await ctx.waitForEvent('page',{timeout:5000}).catch(()=>ctx.pages()[0]);for(const other of ctx.pages())if(other!==p&&other.url()==='about:blank')await other.close();if(p.url()==='about:blank')await p.goto('http://127.0.0.1:8787/welcome.html');
await p.bringToFront();console.log('Persistent shared Chromium ready');
process.on('SIGINT',async()=>{await ctx.close();process.exit(0);});
process.on('SIGTERM',async()=>{await ctx.close();process.exit(0);});
