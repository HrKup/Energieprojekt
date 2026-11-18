p='lernpfad.html';s=open(p).read()
a=s.index('function makeCode(){');b=s.index('/* ---------- Ansicht ---------- */')
new=r'''/* Feste Bitbreite je Teil (Folienzahl + Reserve), damit Codes gültig bleiben, wenn Folien ergänzt werden */
const W={start:6,teil1:16,teil2:12,teil3:9,teil4:12,teil5:9,teil6:18,teil7:10,teil8:10,teil9:11,zusatz:8,anhang:3};
const wid=c=>W[c.id]||8;
function makeCode(){
  let bits="1";
  CH.forEach(c=>{const n=wid(c);let m=Array(n).fill("0");S.done[c.id].forEach(i=>{if(i<n)m[n-1-i]="1";});bits+=m.join("");});
  const li=S.last?CH.findIndex(c=>c.id===S.last[0]):0;bits+=Math.max(0,li).toString(2).padStart(4,"0")+(S.last?S.last[1]:0).toString(2).padStart(5,"0");
  let sum=0;for(const b of bits)sum=(sum*2+ +b)%31;bits+=sum.toString(2).padStart(5,"0");
  while(bits.length%5)bits+="0";
  let s="";for(let i=0;i<bits.length;i+=5)s+=A[parseInt(bits.substr(i,5),2)];
  return "EB-"+s.match(/.{1,5}/g).join("-");
}
function readCode(str){
  const s=String(str).toUpperCase().replace(/^EB-?/,"").replace(/[^A-Z0-9]/g,"");
  if(!s)return false;let bits="";for(const ch of s){const v=A.indexOf(ch);if(v<0)return false;bits+=v.toString(2).padStart(5,"0");}
  const tot=CH.reduce((a,c)=>a+wid(c),0),need=1+tot+9+5;if(bits.length<need||bits[0]!=="1")return false;
  const body=bits.slice(0,1+tot+9);let sum=0;for(const b of body)sum=(sum*2+ +b)%31;
  if(parseInt(bits.substr(body.length,5),2)!==sum)return false;
  let o=1;CH.forEach(c=>{const n=wid(c),m=bits.substr(o,n);S.done[c.id]=[];for(let i=0;i<n;i++)if(m[n-1-i]==="1")S.done[c.id].push(i);o+=n;});
  const li=parseInt(bits.substr(o,4),2),ls=parseInt(bits.substr(o+4,5),2);
  S.last=CH[li]?[CH[li].id,Math.min(ls,Math.max(0,CH[li].slides.length-1))]:null;save();return true;
}

'''
s=s[:a]+new+s[b:];open(p,'w').write(s)
