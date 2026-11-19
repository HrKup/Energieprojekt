import re,sys
src=open('lernpfad_pilot.html').read()
teile=open('teile.js').read()
def rep(old,new,count=1):
    global src
    assert src.count(old)>=1, old[:80]
    src=src.replace(old,new,count)
# Schrift
rep("family=Atkinson+Hyperlegible:wght@400;700","family=Source+Sans+3:wght@400;600;700")
rep('--body:"Atkinson Hyperlegible"','--body:"Source Sans 3"')
# Folie nebeneinander entfernen
a=src.index(' {k:"info",t:"Zwei Fenster nebeneinander"'); b=src.index(' {k:"info",t:"Dein Weg durch das Projekt"')
src=src[:a]+src[b:]
# Bevor du beginnst Teil 1
rep("<p>Erhebe zu Hause die Daten aus dem Protokoll, Teil 1: Personen, Wohnfläche, Baujahr, Energieausweis, Heiz- und Stromverbrauch mit Kosten.</p>",
    "<p>Hake ab, welche Daten von zu Hause du schon hast. Was noch fehlt, notierst du als Hausaufgabe.</p><ul class=\"daten\"><li>Anzahl der Personen im Haushalt und Wohnfläche</li><li>Baujahr und, falls vorhanden, den Energieausweis</li><li>Heizverbrauch und Stromverbrauch pro Jahr mit Kosten (Jahresabrechnung, Eltern fragen)</li></ul>")
# Tipps 1.3 ohne Formelzeichen
rep('tips(["Rechne erst die Energie pro Tag: E = P · t. Achte darauf, Watt in Kilowatt umzurechnen.","100 W = 0,1 kW. Pro Tag: 0,1 kW · 4 h = 0,4 kWh. Jetzt mal 365 Tage, dann mal 0,35 €."])',
    'tips(["Rechne zuerst die Energie für einen Tag aus: Leistung mal Zeit. Dafür rechnest du die 100 W in Kilowatt um (durch 1 000 teilen).","100 W sind 0,1 kW. Der Fernseher läuft 4 Stunden, also rechnest du 0,1 kW mal 4 h. Das ist die Energie pro Tag in kWh.","Die Energie pro Tag nimmst du mal 365, dann hast du die Energie pro Jahr. Diese Zahl nimmst du mal 0,35 €, dann hast du die Kosten."])')
rep('tips(["Rechne Minuten in Stunden um (siehe Folie „Umrechnen“).","2 000 W = 2 kW und 3 min = 0,05 h. Pro Tag: 2 kW · 0,05 h = 0,1 kWh."])',
    'tips(["Rechne zuerst die Watt in Kilowatt um und die Minuten in Stunden (Folie „Umrechnen“).","2 000 W sind 2 kW. 3 Minuten sind 3 geteilt durch 60, also 0,05 Stunden.","Für einen Tag rechnest du 2 kW mal 0,05 h. Das Ergebnis nimmst du mal 365 und danach mal 0,35 €."])')
rep('tips(["Prozent wovon? Der Grundwert sind die 16 000 kWh.","16 000 kWh · 6 : 100 = 960 kWh. Diese 960 kWh nimmst du dann mal 0,12 € und mal 0,24 kg."])',
    'tips(["Prozent wovon? Die 6 % beziehen sich auf die 16 000 kWh, die der Haushalt im Jahr verbraucht.","Du rechnest 16 000 mal 6 und teilst das Ergebnis durch 100. Das ist die eingesparte Energie in kWh.","Die eingesparten kWh nimmst du einmal mal 0,12 € (das ist das Geld) und einmal mal 0,24 kg (das ist das CO₂)."])')
rep('tips(["Amortisationszeit = Anschaffungskosten : Ersparnis pro Jahr (Folie „Kosten, Amortisation, CO₂“).","12 € : 8 € pro Jahr = ? Jahre. Was passiert nach dieser Zeit?"])',
    'tips(["Die Frage ist: Nach wie vielen Jahren hat die Zeitschaltuhr so viel gespart, wie sie gekostet hat?","Du teilst den Preis (12 €) durch die Ersparnis in einem Jahr (8 €). Das Ergebnis sind Jahre.","Für den Satz: Was passiert mit dem Geld nach dieser Zeit, also im dritten, vierten, fünften Jahr?"])')
rep('tips(["Energiekennwert = Energie pro Jahr (kWh) : Wohnfläche (m²).","Beim Altbau ist der Verbrauch in m³ Erdgas angegeben: 1 m³ Erdgas ≈ 10 kWh."])',
    'tips(["Du teilst die Energie pro Jahr in kWh durch die Wohnfläche in m². Zum Beispiel Wohnung 1: 9 000 geteilt durch 72.","Beim Altbau steht der Verbrauch in m³ Erdgas. Ein m³ Erdgas sind etwa 10 kWh, also nimmst du die 2 800 erst mal 10."])')
# Teile 2-9 ersetzen
a=src.index('{id:"teil2",short:"Teil 2"'); b=src.index('];\nconst PLAN=')
src=src[:a]+'...CH_MORE,\n'+src[b:]
rep('/* ---------- Inhalte ---------- */','/* ---------- Inhalte ---------- */\n'+teile+'\nObject.assign(CHECKS,CHECKS_MORE);\n')
# Plan
a=src.index(' rows:[["Teil 1'); b=src.index(']]]};',a)+5
src=src[:a]+' rows:[["Teil 1 · Haus und Haushalt",[0]],["Teil 2 · Wände und Wärme",[1]],["Teil 3 · Wärmebilder",[2]],["Teil 4 · Dach und Sonnenstrom",[2,3]],["Teil 5 · Fenster und Türen",[3]],["Teil 6 · Heizung und Warmwasser",[4]],["Teil 7 · Strom und Geräte",[5]],["Teil 8 · Beleuchtung",[5]],["Teil 9 · CO₂-Bilanz",[6]],["Gutachten schreiben (Protokoll)",[6,7]]]};'+src[b:]
# Skala größer, Einheit in die Kästen
rep('.scale div{color:#fff;font-weight:700;text-align:center;padding:6px 2px;font-size:.9rem;line-height:1.1}\n.scale small{display:block;font-weight:400;font-size:.68rem}',
    '.scale div{color:#fff;font-weight:800;text-align:center;padding:10px 2px;font-size:1.2rem;line-height:1.15}\n.scale small{display:block;font-weight:600;font-size:.78rem;line-height:1.2;margin-top:3px}')
rep('d.innerHTML=k[0]+"<small>"+(k[2]>1e8?"über "+k[1]:k[0]==="A+"?"unter 30":k[1]+"–"+k[2])+"</small>"',
    'd.innerHTML=k[0]+"<small>"+(k[2]>1e8?"über "+k[1]:k[0]==="A+"?"unter 30":k[1]+"–"+k[2])+"<br>kWh/m²</small>"')
rep('@media (max-width:520px){.scale small{display:none}','@media (max-width:520px){.scale div{font-size:.95rem;padding:8px 1px}.scale small{font-size:.6rem}')
# Zusätzliches CSS
rep('/* Startseite */','''.fig{margin:0;display:flex;flex-direction:column;gap:6px;align-items:flex-start}
.fig img{max-width:100%;max-height:360px;height:auto;border-radius:8px;background:#fff;border:1px solid var(--line)}
.fig figcaption{font-size:.85rem;color:var(--muted)}
.steck dl{display:grid;grid-template-columns:max-content 1fr;gap:4px 14px;margin:0}
.steck dt{font-weight:700}.steck dd{margin:0}
.tool-frame{border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff}
.tool-frame iframe{display:block;width:100%;min-height:520px;border:0}
table.grid td{height:2em}
.tbl{overflow-x:auto}
@media (max-width:520px){.steck dl{grid-template-columns:1fr}.steck dd{margin-bottom:6px}}
ul.daten{list-style:none;padding:0;margin:6px 0 0;display:flex;flex-direction:column;gap:6px;font-weight:400;color:var(--ink)}
ul.daten label{display:flex;gap:10px;align-items:flex-start;cursor:pointer}
ul.daten input{width:1.25rem;height:1.25rem;margin-top:.15rem;flex:none;accent-color:var(--done)}
ul.daten li.hab span{color:var(--muted)}
.offen{font-weight:700;margin-top:6px}
/* Startseite */''')
# NBSP + iframe-Höhe in show()
rep('$("#slide").innerHTML=s.h+extra;','$("#slide").innerHTML=nb(s.h)+extra;\n  document.querySelectorAll(".tool-frame iframe").forEach(f=>f.addEventListener("load",()=>{try{f.style.height=(f.contentDocument.documentElement.scrollHeight+20)+"px";}catch(e){}}));')
rep('const CHECKS={};','''const CHECKS={};
const UNITS="W|kW|kWh|Wh|MWh|€|ct|%|°C|°|K|m²|m³|kg|g|t|h|min|s|Jahre|Jahr|Liter|l|lm|cm|mm|m|Personen|Prozent";
const RE_TH=/(\\d) (\\d{3})(?!\\d)/g, RE_U=new RegExp("(\\\\d) ("+UNITS+")(?![\\\\wäöüß])","g");
function nb(h){return h.replace(/>([^<]+)</g,(m,t)=>">"+t.replace(RE_TH,"$1\\u00a0$2").replace(RE_TH,"$1\\u00a0$2").replace(RE_U,"$1\\u00a0$2")+"<");}''')
# Kapitelnummern auf Startseite
rep('<span class="num">${k?k:"★"}</span>','<span class="num">${c.id==="start"?"★":c.id==="zusatz"?"Z":c.id==="anhang"?"A":c.id.replace("teil","")}</span>')
open('lernpfad.html','w').write(src)
print(len(src))

# ---- Datenlisten zum Abhaken (Tom 19.11.) ----
src=open('lernpfad.html').read()
JS=r'''
/* Datenlisten zum Abhaken: Folie wird erst grün, wenn alle Daten da sind */
const DKEY="eb-daten-v1";let DAT={};try{DAT=JSON.parse(localStorage.getItem(DKEY)||"{}")||{};}catch(e){}
const dsave=()=>{try{localStorage.setItem(DKEY,JSON.stringify(DAT));}catch(e){}};
const dtext=h=>h.replace(/<[^>]+>/g,"").replace(/\s+/g," ").trim();
function datenOf(s){if(s._d===undefined){const m=s.h.match(/<ul class="daten">([\s\S]*?)<\/ul>/);s._d=m?[...m[1].matchAll(/<li>([\s\S]*?)<\/li>/g)].map(x=>dtext(x[1])):null;}return s._d;}
const allHave=s=>{const d=datenOf(s);return !d||d.every(k=>DAT[k]);};
function syncDaten(){CH.forEach(c=>c.slides.forEach((s,i)=>{if(s.k==="info"&&datenOf(s)&&isDone(c.id,i)!==allHave(s))setDone(c.id,i,allHave(s));}));}
function wireDaten(cid,i){
  const s=chapter(cid).slides[i],d=datenOf(s);if(!d)return;
  if(s.k==="info"&&isDone(cid,i))d.forEach(k=>{if(DAT[k]===undefined)DAT[k]=true;});
  const ul=document.querySelector("#slide ul.daten");if(!ul)return;
  const sum=document.createElement("p");sum.className="offen";ul.after(sum);
  const upd=()=>{const n=d.filter(k=>!DAT[k]).length;sum.textContent=n?("Noch offen: "+n+" von "+d.length+". Notiere sie als Hausaufgabe in deiner Mappe."):"Alles da. Du kannst loslegen.";};
  [...ul.children].forEach((li,k)=>{const key=d[k];li.className=DAT[key]?"hab":"";
    li.innerHTML=`<label><input type="checkbox" ${DAT[key]?"checked":""}><span>${li.innerHTML}</span></label>`;
    li.querySelector("input").onchange=e=>{DAT[key]=e.target.checked;li.className=DAT[key]?"hab":"";dsave();syncDaten();upd();renderSide(cid);updTop();};});
  upd();
}
'''
src=src.replace('/* Fortschritt sichern */',JS+'\n/* Fortschritt sichern */',1)
src=src.replace('  wire();\n','  wire();wireDaten(cid,i);\n',1)
src=src.replace('if(s.k==="info")setDone(cur.c,cur.i,true);','if(s.k==="info"&&allHave(s))setDone(cur.c,cur.i,true);',1)
assert 'wireDaten(cid,i)' in src and 'allHave(s))setDone' in src
open('lernpfad.html','w').write(src)
print('daten ok')

import json as _j
_z=_j.load(open('content.json'))['proto']['2']['zuhause']
_hw='<div class="where-box mappe"><span class="ic">⌂</span><div>Hausaufgabe für die nächste Stunde<p>Finde zu Hause heraus, was du für Teil 2 brauchst. Hake ab, was du schon hast:</p><ul class="daten">'+''.join('<li>'+x+'</li>' for x in _z)+'</ul></div></div>'
src=open('lernpfad.html').read()
m='<p class="small">Klicke auf „Aufgabe erledigt“, wenn du Teil 1 im Protokoll fertig hast.'
assert m in src
src=src.replace(m,_hw+'\n  '+m,1)
open('lernpfad.html','w').write(src); print('t1 hw ok')

# ---- Dämm-Quiz ohne Mappe (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='Teil 2 · Aufgabe 2.2 <span class=\\"tag screen\\">● hier am Bildschirm</span> <span class=\\"tag mappe\\">✎ Mappe</span>'
assert a in src; src=src.replace(a,'Teil 2 · Aufgabe 2.2 <span class=\\"tag screen\\">● hier am Bildschirm</span>',1)
a=' Notiere zwei Ergebnisse, die dich überrascht haben.</p><div class=\\"tool-frame\\"><iframe src=\\"tools/daemm-quiz.html\\" title=\\"Dämm-Quiz\\" loading=\\"lazy\\"></iframe></div><div class=\\"where-box mappe\\"><span class=\\"ic\\">✎</span><div>In deine Mappe<p>Bearbeite die Aufgabe in deiner Mappe.</p></div></div>'
assert a in src; src=src.replace(a,'</p><div class=\\"tool-frame\\"><iframe src=\\"tools/daemm-quiz.html\\" title=\\"Dämm-Quiz\\" loading=\\"lazy\\"></iframe></div>',1)
open('lernpfad.html','w').write(src); print('quiz ok')

# ---- 2.4 UBA-Seite präzisieren (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='</a> über die drei Gruppen von Dämmstoffen. Trage je Gruppe'
assert a in src
src=src.replace(a,'</a> über die drei Gruppen von Dämmstoffen. Du brauchst nur einen kurzen Abschnitt: Scrolle zur Überschrift <b>„Gewusst wie“</b> und lies dort den fett gedruckten Absatz <b>„Dämmstoffe“</b> (er steht nach „Fenster“). Schneller geht es mit <b>Strg + F</b> und dem Suchwort „Dämmstoffe“. Trage je Gruppe',1)
a='Auf der Seite des Umweltbundesamts steht ein Abschnitt „Dämmstoffe“. Die drei Gruppen heißen dort nicht ausdrücklich so. Ordne die Beispiele selbst zu: Steinwolle und Glaswolle sind mineralisch, Polystyrol ist ein Kunststoff, Holzfaser und Zellulose wachsen nach.'
assert a in src
src=src.replace(a,'Im Absatz „Dämmstoffe“ kommen die drei Gruppen nacheinander: erst die <b>mineralischen</b> (Steinwolle, Glaswolle), dann die aus <b>Kunststoff</b> (Polystyrol, aus Erdöl), dann die <b>natürlichen</b> (zum Beispiel Holzfaser, Stroh, Zellulose aus Altpapier). Den Rest der Seite brauchst du nicht.',1)
a='Wenn du einen Nachteil nicht findest: Mineralwolle'
assert a in src
src=src.replace(a,'Nicht jeder Nachteil steht auf der Seite. Hier sind Hilfen: Mineralwolle',1)
open('lernpfad.html','w').write(src); print('2.4 ok')

# ---- 3.2 schwerer, mit Wärmebild (Tom 19.11.) ----
src=open('lernpfad.html').read()
a=src.index('{"k": "task", "n": "3.2"'); b=src.index('{"k": "task", "n": "3.3"')
h32=('<div class="eyebrow">Teil 3 · Aufgabe 3.2 <span class="tag mappe">✎ Mappe</span></div><h1>Ein Wärmebild auswerten</h1>'
 '<figure class="fig"><img src="fig/thermo_passivhaus.png" alt="Wärmebild: links ein Altbau mit gelb-grüner Fassade, rechts ein gedämmtes Haus mit blauer Fassade und helleren Fenstern; Farbskala rechts von 3 bis 9 °C"><figcaption>Wärmebild im Winter: links ein Altbau, rechts ein gedämmtes Haus (Passivhaus). Bild: Passivhaus Institut, <a href="https://commons.wikimedia.org/wiki/File:Passivhaus_thermogram_gedaemmt_ungedaemmt.png" target="_blank" rel="noopener">Wikimedia Commons</a>, Lizenz <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.de" target="_blank" rel="noopener">CC BY-SA 3.0</a></figcaption></figure>'
 '<p class="task-q">Draußen ist es etwa 0 °C, drinnen sind beide Häuser gleich warm geheizt.</p>'
 '<ul class="bullets" style="list-style:none;padding-left:0">'
 '<li>a) Lies an der Farbskala ab, wie warm die Außenwand des Altbaus und die des gedämmten Hauses ungefähr sind.</li>'
 '<li>b) Erkläre, warum ausgerechnet das gut gedämmte Haus die kältere Fassade hat.</li>'
 '<li>c) Beim gedämmten Haus erscheinen die Fenster heller als die Wand. Beurteile, ob man daraus schließen kann, dass die Fenster schlecht dämmen.</li>'
 '<li>d) Von innen fotografiert zeigt eine Zimmerecke an der Außenwand 12 °C, die übrige Wand 18 °C. Erläutere, welches Problem dort entstehen kann und warum.</li></ul>'
 '<div class="where-box mappe"><span class="ic">✎</span><div>In deine Mappe<p>Schreib deine Antworten in ganzen Sätzen in deine Mappe.</p></div></div>'
 '<details class="tip"><summary>Tipp 1</summary><div>a) Die Farbskala steht rechts am Bildrand. Blau bedeutet etwa 3 bis 4 °C, Grün etwa 5 bis 6 °C, Gelb etwa 7 °C.</div></details>'
 '<details class="tip"><summary>Tipp 2</summary><div>b) Die Kamera misst nur die Oberfläche. Überlege: Wie viel Wärme aus dem Inneren kommt bei einer guten Dämmung noch an der Außenseite an?</div></details>'
 '<details class="tip"><summary>Tipp 3</summary><div>c) Lies noch einmal die Info-Folie „So gelingen gute Wärmebilder“: Was passiert bei Glas? Und: Auch sehr gute Fenster dämmen weniger als eine dick gedämmte Wand.</div></details>'
 '<details class="tip"><summary>Tipp 4</summary><div>d) Denk an eine kalte Flasche aus dem Kühlschrank: Was passiert mit der feuchten Raumluft an einer kalten Oberfläche?</div></details>'
 '<details class="tip"><summary>Lösung anzeigen</summary><div class="sol">a) Altbau: etwa 5 bis 7 °C (grün bis gelb). Gedämmtes Haus: etwa 3 bis 4 °C (blau), also fast so kalt wie die Außenluft.<br>'
 'b) Die Dämmung lässt kaum Wärme nach außen durch. Deshalb bleibt die Außenseite der Wand kalt. Beim Altbau dringt viel Wärme durch die Wand, die Fassade wird warm. Eine warme Fassade bedeutet also: Hier geht Wärme verloren.<br>'
 'c) Nur bedingt. Glas spiegelt die Wärmestrahlung der Umgebung, die Temperatur auf Scheiben ist deshalb oft falsch. Außerdem dämmt auch ein gutes Fenster weniger als eine dick gedämmte Wand. Die Fenster sind hier nur etwa 5 °C warm, das ist für Fenster wenig. Dass sie schlecht sind, kann man daraus nicht schließen.<br>'
 'd) Die Ecke ist eine Wärmebrücke. An der kalten Stelle kühlt die feuchte Raumluft ab, Wasser schlägt sich nieder (wie an einer kalten Flasche). Die Wand wird feucht, und dort kann sich Schimmel bilden.</div></details>')
import json as _js
new='{"k": "task", "n": "3.2", "t": "Ein Wärmebild auswerten", "h": '+_js.dumps(h32,ensure_ascii=False)+'}, '
src=src[:a]+new+src[b:]
open('lernpfad.html','w').write(src); print('3.2 ok')

# ---- Teil 3 Info: Beispiel-Wärmebilder (Tom 19.11.) ----
import re as _re
src=open('lernpfad.html').read()
def _fig(title,img,alt,cap):
    global src
    m=_re.search(r'<h1>'+_re.escape(title)+r'</h1><div class=\\"text\\">.*?</div>',src)
    assert m, title
    f='<figure class=\\"fig\\"><img style=\\"width:520px\\" src=\\"fig/'+img+'\\" alt=\\"'+alt+'\\"><figcaption>'+cap+'</figcaption></figure>'
    src=src[:m.end()]+f+src[m.end():]
_fig('Wärmebrücken finden','thermo_altbau.jpg','Wärmebild eines ungedämmten Altbaus im Winter mit Messpunkten: Fenster und Wand gelb bis rot, Dach und Himmel blau bis violett',
 'Beispiel: ungedämmter Altbau im Winter, von außen. Die Kästchen sind Messpunkte in °C. Rund um die Fenster und an der Wand ist es deutlich wärmer (gelb, rot) als am Dach: Hier entweicht viel Wärme. Bild: Lutz Weidner, <a href=\\"https://commons.wikimedia.org/wiki/File:Ungedaemmte_Aussenwand.jpg\\" target=\\"_blank\\" rel=\\"noopener\\">Wikimedia Commons</a>, Lizenz <a href=\\"https://creativecommons.org/licenses/by-sa/3.0/deed.de\\" target=\\"_blank\\" rel=\\"noopener\\">CC BY-SA 3.0</a>, verkleinert')
open('lernpfad.html','w').write(src); print('Teil3 Bilder ok')

# ---- Schrift lokal statt Google Fonts (Datenschutz, 19.11.) ----
src=open('lernpfad.html').read()
src=re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*','',src)
src=re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com/[^"]*">','<link rel="stylesheet" href="fonts/fonts.css">',src)
assert 'googleapis' not in src
open('lernpfad.html','w').write(src); print('fonts lokal ok')

# ---- Teil 3 Info 3 + Info 2: Links zu Beispielbildern (Tom 19.11.) ----
src=open('lernpfad.html').read()
def _after_text(title,html):
    global src
    m=_re.search(r'<h1>'+_re.escape(title)+r'</h1><div class=\\"text\\">.*?</div>',src)
    assert m, title
    src=src[:m.end()]+html.replace('"','\\"')+src[m.end():]
_after_text('So gelingen gute Wärmebilder','<p class="lead" style="font-size:1rem">Beispielbild ansehen: Auf der Seite <a href="https://www.co2online.de/modernisieren-und-bauen/sanierung-modernisierung/thermografie/" target="_blank" rel="noopener">„Thermografie“ von co2online</a> siehst du oben ein Mehrfamilienhaus als Foto und als Wärmebild. Weiter unten unter „Welche Fehler kann man bei einer Thermografieaufnahme machen?“ steht, warum Sonne und Fenster das Ergebnis verfälschen.</p>')
_after_text('Wärmebrücken finden','<p class="lead" style="font-size:1rem">Weitere Beispiele von innen: <a href="https://www.berlin.de/ba-steglitz-zehlendorf/politik-und-verwaltung/beauftragte/klimaschutz/beispielhafte_thermographieaufnahmen.pdf" target="_blank" rel="noopener">Wärmebilder aus Berliner Wohnungen</a> (undichte Fenster und Türen, ungedämmte Hausecke, schlecht gedämmte Geschossdecke).</p>')
open('lernpfad.html','w').write(src); print('Teil3 Links ok')
