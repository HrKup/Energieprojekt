const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1366,height:800}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://localhost:8765/');await p.waitForTimeout(500);
const out=await p.evaluate(()=>CH.map(c=>c.id+':'+c.slides.length).join(' '));console.log(out);
// visit every slide
const ids=await p.evaluate(()=>CH.map(c=>[c.id,c.slides.length]));
let bad=[];
for(const [id,n] of ids){for(let i=1;i<=n;i++){await p.evaluate(h=>location.hash=h,`#${id}-${i}`);await p.waitForTimeout(30);
 const t=await p.evaluate(()=>document.querySelector('#slide').innerText.length);if(t<40)bad.push(id+'-'+i);}}
console.log('short',bad);
// checks without stub
const missing=await p.evaluate(()=>{const r=[];CH.forEach(c=>c.slides.forEach(s=>{const m=[...s.h.matchAll(/data-check="([^"]+)"/g)];m.forEach(x=>{if(!CHECKS[x[1]])r.push(x[1])})}));return r});console.log('missing checks',missing);
// code roundtrip
await p.evaluate(()=>{setDone('teil6',3,true);setDone('anhang',0,true);});const code=await p.evaluate(()=>makeCode());
const ok=await p.evaluate(c=>{localStorage.clear();S={done:{}};return readCode(c)&&isDone('teil6',3)&&isDone('anhang',0)},code);console.log('code',code,ok);
for(const [h,f] of [['#start-seite','home'],['#teil1-8','t1_8'],['#teil2-6','t2_6'],['#teil6-2','t6_2'],['#teil6-15','t6_15'],['#teil9-9','t9_9'],['#anhang-1','anh']]){await p.evaluate(x=>location.hash=x,h);await p.waitForTimeout(700);await p.screenshot({path:'/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/web/x_'+f+'.png'});}
await p.setViewportSize({width:390,height:800});await p.evaluate(x=>location.hash=x,'#teil1-8');await p.waitForTimeout(300);await p.screenshot({path:'/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/web/x_mob.png'});
const ov=await p.evaluate(()=>document.documentElement.scrollWidth);console.log('mobile width',ov);
console.log('errors',errs);await b.close();})();
