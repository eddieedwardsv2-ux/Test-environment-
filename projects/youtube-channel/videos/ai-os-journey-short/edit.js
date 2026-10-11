import fs from 'node:fs';
import path from 'node:path';

// Native Higgsedit. The voice ledger is the timeline source, not a clock callback.
export default async ({project,text,rect,path:vector}) => {
  const root=path.dirname(new URL(import.meta.url).pathname);
  const data=JSON.parse(fs.readFileSync(path.join(root,fs.existsSync(path.join(root,'aligned-source.json'))?'aligned-source.json':'timed-source.json'),'utf8'));
  const revision=Number(process.env.JOURNEY_REVISION||1);
  const p=await project({dir:path.join(root,`native-r${revision}`),size:'1080x1920',fps:30,background:'#05070d'});
  const monoFace=revision>=3?await p.add(path.join(root,'fontkit/fonts/jetbrains-mono-700.woff2')):null;
  const bodyFace=revision>=3?await p.add(path.join(root,'fontkit/fonts/dm-sans-700.woff2')):null;
  const C={bg:'#05070d',panel:'#101b2b',white:'#eef3fc',muted:'#a6b7cd',cyan:'#3ec1ff',green:'#7cf29a',amber:'#ffbd66',purple:'#c69cff',red:'#ff868c'};
  const colors=[C.cyan,C.green,C.cyan,C.green,C.purple,C.amber,C.red,C.cyan];
  const titles=['From a phone.\nTo my own AI OS.','Four parts.\nOne starting point.','A Router.\nThen specialists.','Useful context.\nNot every note.','I stay\nthe Chief.','The right tools.\nUseful work.','Confidence\nis not proof.','Next: a friend.\nOne useful step.'];
  const kickers=['01 / THE BEGINNING','02 / LEARN THE PARTS','03 / ROUTE INFORMATION','04 / LESS CONTEXT','05 / REAL CHOICES','06 / GIVE IT HANDS','07 / TEST THE RESULT','08 / WHAT COMES NEXT'];
  const captions=[];
  const tx=(str,x,y,w,h,size=48,color=C.white,mono=false,extra={})=>text(str,{x,y,width:w,height:h,fontFamily:mono?'JetBrains Mono':'DM Sans',...(monoFace?{typography:{fontAssetId:(mono?monoFace:bodyFace).id}}:{}),fontWeight:700,fontSize:size,lineHeight:1.12,color,...extra});
  const box=(x,y,w,h,color=C.panel,extra={})=>rect({x,y,width:w,height:h,fill:color,radius:24,...extra});
  const entrance=(at=0)=>[{property:'opacity',from:0,to:1,at,duration:.22},{property:'offsetY',from:16,to:0,at,duration:.3,easing:'house'}];
  const line=(a,b,color=C.cyan)=>vector({d:`M ${a[0]} ${a[1]} L ${b[0]} ${b[1]}`,width:1080,height:1920,stroke:{color,width:3,cap:'round'}});
  const dot=(a,b,at,dur=.8,color=C.cyan)=>box(a[0]-8,a[1]-8,16,16,color,{radius:8,at,duration:dur,animate:[{property:'offsetX',from:0,to:b[0]-a[0],duration:dur,easing:'linear'},{property:'offsetY',from:0,to:b[1]-a[1],duration:dur,easing:'linear'}]});
  function card(x,y,w,h,label,job,color,at=0,active=false){
    const labelSize=revision>=3?44:revision>=2?(label.length>11?38:44):(active?48:42);
    return [box(x,y,w,h,C.panel,{strokeColor:color,strokeWidth:active?3:1,at,animate:entrance()}),tx(label,x+16,y+18,w-32,54,labelSize,color,false,{at,animate:entrance()}),tx(job,x+16,y+78,w-32,50,revision>=3?36:revision>=2?32:36,C.muted,false,{at,animate:entrance()})];
  }
  function wordAt(s,needle,fallback=0){
    const search=needle.toLowerCase().replace(/[^a-z]/g,'');
    const found=s.words.find(w=>w.text.toLowerCase().replace(/[^a-z]/g,'')===search);
    return found?Math.max(0,found.start-s.start):fallback;
  }
  function graph(s,i){
    let nodes=[];
    const router=[540,1075], info=[540,710], arch=[265,900], qm=[765,900], desk=[540,710], check=[265,1255], save=[765,1255];
    // Fine seeded branches accumulate rather than replacing the whole visual identity.
    for(let k=0;k<12+i*4;k++){
      const a=k*2.399963, r=230+(k%3)*44;
      const q=[540+Math.cos(a)*r,1075+Math.sin(a)*r*.62];
      nodes.push(line(router,q,'#233c53'),box(q[0]-3,q[1]-3,6,6,'#355974',{radius:3}));
    }
    nodes.push(line(info,router,'#4b7187'));
    if(i<4){nodes.push(...card(325,645,430,140,'New information','video / tool / question',C.cyan));}
    else {nodes.push(...card(325,645,430,140,'Charlie = Chief','Desk: real choices',C.purple,0,i===4));}
    const routerTime=i===2?wordAt(s,'Router'):0;
    nodes.push(box(395,1010,290,135,C.white,{at:routerTime,animate:entrance()}),tx('Router',415,1036,250,60,58,C.bg,true,{at:routerTime,animate:entrance()}),tx('points the way',415,1098,250,46,32,'#344457',false,{at:routerTime,animate:entrance()}));
    if(i>=2){
      const t=i===2?wordAt(s,'specialist'):0;
      nodes.push(line(router,arch,'#3f83a0'),...card(100,835,330,140,'Architect','organises it',C.cyan,t,i===5));
      const qt=i===2?Math.min(wordAt(s,'Elders'),s.duration-1.3):0;
      nodes.push(line(router,qm,'#806348'),...card(600,835,330,140,'Quartermaster','picks tools',C.amber,qt,i===5));
      nodes.push(tx('ELDERS = SPECIALISTS',150,790,780,50,36,C.muted,true,{align:'center',at:t,animate:entrance()}));
      if(i>=4){
        nodes.push(line(router,desk,C.purple));
        if(i===4) nodes.push(dot(router,desk,wordAt(s,'choices'),.8,C.purple));
      }
      if(i>=5){
        nodes.push(line(qm,save,'#438664'),...card(600,1190,330,140,'Saved result','ready to use',C.green,0,true));
        if(i===5) nodes.push(dot(info,router,wordAt(s,'Quartermaster'),.7),dot(router,qm,wordAt(s,'tools'),.65,C.amber),dot(router,arch,wordAt(s,'Architect'),.7),dot(qm,save,wordAt(s,'use')-.7,.7,C.green));
      }
      if(i>=6){nodes.push(line(save,check,C.red),...card(100,1190,330,140,'Check result','test / evidence',C.red,0,i===6));}
      if(i===2) nodes.push(dot(info,router,wordAt(s,'information'),.7),dot(router,arch,wordAt(s,'specialist')+.35,.7));
      if(i===3){nodes.push(box(330,1190,420,140,C.bg),tx('Only what\nis useful',350,1200,380,120,44,C.green,false,{align:'center'}));}
    }
    return nodes;
  }
  for(let i=0;i<data.scenes.length;i++){
    const s=data.scenes[i],dur=s.duration,accent=colors[i];
    let nodes=[rect({width:1080,height:1920,fill:{kind:'radial',stops:[{offset:0,color:'#102a3e'},{offset:1,color:C.bg}]}}),rect({x:0,y:190,width:10,height:1360,fill:accent}),tx("CHARLIE'S AI OS",100,165,680,55,34,C.muted,true),tx('BUILD LOG / 01',100,235,800,60,36,accent,true),tx(kickers[i],100,310,850,65,38,accent,true)];
    nodes.push(tx(titles[i],100,410,880,200,76,C.white,true,{motion:{by:'character',at:.08,duration:1.1,from:{opacity:0},easing:'linear'}}));
    if(i===0){
      nodes.push(box(345,680,390,560,'#0e1622',{strokeColor:'#47758e',strokeWidth:3}),box(470,707,140,17,'#47758e',{radius:9}),tx('A PHONE',385,800,310,90,58,C.cyan,true,{align:'center'}),tx('A lot of\nquestions.',385,900,310,160,54,C.white,false,{align:'center',at:wordAt(s,'questions')-.2,animate:entrance()}),box(455,1130,170,7,C.cyan,{radius:3}),tx('No coding background',145,1270,790,60,42,C.muted,false,{align:'center',at:wordAt(s,'coding')-.3,animate:entrance()}));
    }else if(i===1){
      const parts=[['MODEL','thinks','model'],['TOOLS','act','tools'],['SKILLS','guide it','skills'],['CONTEXT','what it knows','context']];
      parts.forEach(([label,job,word],k)=>nodes.push(...card(105+(k%2)*445,735+Math.floor(k/2)*225,400,180,label,job,k%2?C.cyan:C.green,Math.min(wordAt(s,word),s.duration-1.3),true)));
    }else{
      nodes.push(...graph(s,i));
      if(i===6) nodes.push(tx('FAULT TEST: CAUGHT',150,1332,780,48,36,C.green,true,{align:'center',at:wordAt(s,'faults'),animate:entrance()}));
      if(i===7) nodes.push(tx('NEXT: A FRIEND’S SETUP',140,1332,800,48,36,C.cyan,true,{align:'center'}));
    }
    // Draft 1 uses six-word captions. Later revisions may split over-wide chunks.
    let chunk=[],sceneCaps=[];
    const flush=()=>{
      if(!chunk.length)return;
      const words=chunk.map(x=>x.text), str=words.join(' ');
      const start=chunk[0].start,end=Math.min(s.end,chunk.at(-1).end+.09);
      sceneCaps.push({scene:i+1,start,end,text:str});
      chunk=[];
    };
    for(const w of s.words){
      if(revision>=2 && chunk.length && (chunk.map(x=>x.text).join(' ').length+1+w.text.length>32 || w.start-chunk.at(-1).end>.35)) flush();
      chunk.push(w); if(chunk.length>=(revision>=2?5:6) || /[.!?]$/.test(w.text))flush();
    }
    flush();
    sceneCaps.forEach((c,k)=>{
      if(k+1<sceneCaps.length)c.end=Math.min(c.end,sceneCaps[k+1].start);
      if(c.end<=c.start)throw new Error(`Invalid caption clock: ${c.text}`);
      captions.push(c);
      nodes.push(box(90,1380,900,170,C.bg,{at:c.start-s.start,duration:c.end-c.start}),tx(c.text,125,1400,830,145,revision>=2?50:48,C.white,false,{at:c.start-s.start,duration:c.end-c.start,align:'center'}));
    });
    nodes.push(tx(i===7?'DOCUMENTING THE BUILD • AI NARRATION':'LEARNING IN PUBLIC • ONE STEP AT A TIME',100,1580,850,52,28,C.muted,true));
    for(let k=0;k<8;k++)nodes.push(box(100+k*109,1660,92,5,k<=i?accent:'#2b3d50',{radius:2}));
    // Native top-level nodes default to the FULL beat, not its remaining time.
    // Delayed nodes therefore need an explicit lifetime ending at this cut.
    // Top-level at is absolute; only nested frame children use a local clock.
    p.compose(nodes.map(n=>({...n,at:s.start+Number(n.at||0),duration:n.duration??dur-Number(n.at||0)})),{at:s.start,dur,name:`Scene ${i+1}: ${kickers[i]}`});
  }
  const audio=await p.add(path.join(root,'narration.wav'));
  p.cut(audio,{at:0,from:0,dur:data.duration});
  fs.writeFileSync(path.join(root,`captions-r${revision}.json`),JSON.stringify(captions,null,2));
  const before=Date.now();
  const report=await p.render(path.join(root,`draft-r${revision}.mp4`),{depth:8,bitrate:5000000,concurrency:2,shards:4});
  fs.writeFileSync(path.join(root,`render-r${revision}.json`),JSON.stringify({revision,elapsed_seconds:(Date.now()-before)/1000,report},null,2));
};
