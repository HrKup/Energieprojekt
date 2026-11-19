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

# ---- Teil 4 Info 2: Verweis auf 2.4 (Tom 19.11.) ----
src=open('lernpfad.html').read()
_after_text('Welcher Dämmstoff fürs Dach?','<p class="lead" style="font-size:1rem">Hast du Aufgabe 2.4 bearbeitet? Vergleiche deine Tabelle mit diesem Text.</p>')
open('lernpfad.html','w').write(src); print('4 Info2 ok')

# ---- Kompass größer anzeigen (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='<img src=\\"fig/windrose.png\\"'
assert a in src
src=src.replace(a,'<img style=\\"max-height:none;width:min(100%,520px)\\" src=\\"fig/windrose.png\\"')
open('lernpfad.html','w').write(src); print('windrose ok')

# ---- ★-Aufgaben: deutlicher Kasten unten (Tom 19.11.) ----
src=open('lernpfad.html').read()
STARBOX='<div class=\\"where-box star\\"><span class=\\"ic\\">★</span><div>Freiwillige Aufgabe<p>Bearbeite sie, wenn du noch Zeit hast. Wird die Zeit knapp, lass sie weg.</p></div></div>'
cnt=0
def _star_obj(obj):
    global cnt
    if '\\"tag star\\"' not in obj or 'Freiwillige Aufgabe' in obj: return obj
    k=obj.find('<div class=\\"where-box mappe\\">')
    if k<0:
        k=obj.rfind('", "star": true')
        if k<0: return obj
    cnt+=1
    return obj[:k]+STARBOX+obj[k:]
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_parts=[src[:_st[0]]]
for _a,_b in zip(_st,_st[1:]+[None]):
    _o=src[_a:_b] if _b else src[_a:]
    _parts.append(_star_obj(_o) if '"star": true' in _o else _o)
src=''.join(_parts)
src=src.replace('.where-box.mappe{','.where-box.star{background:#FFF3BF;color:#8a5a00;border:2px solid #F59F00}\n.where-box.star .ic{color:#F59F00}\n.where-box.mappe{',1)
print('starbox',cnt)
open('lernpfad.html','w').write(src)

# ---- 4.4 ohne Mappe-Aufgabe: nur Ausprobieren (Tom 19.11.) ----
src=open('lernpfad.html').read()
a=src.index('{"k": "task", "n": "4.4"'); b=src.index('{"k": "task", "n": "4.5"')
h44=('<div class="eyebrow">Teil 4 · Aufgabe 4.4 <span class="tag screen">● hier am Bildschirm</span></div><h1>Übung: Balkonkraftwerk-Planer</h1>'
 '<p class="task-q">Ein Balkon zeigt laut Kompass-App nach 240°. Probiere den Planer aus:</p>'
 '<ul class="bullets" style="list-style:none;padding-left:0">'
 '<li>a) Stelle 240° ein (Zahl eingeben oder in die Rose klicken). Lies ab, welche Himmelsrichtung das ist und ob der Balkon geeignet ist.</li>'
 '<li>b) Wähle unten aus, wie viele Module an den Balkon passen, und lies den geschätzten Jahresertrag ab.</li>'
 '<li>c) Probiere andere Richtungen aus, zum Beispiel 180° (Süden) und 0° (Norden). Was fällt dir auf?</li></ul>'
 '<div class="tool-frame"><iframe src="tools/solar-helfer.html" title="Balkonkraftwerk-Planer" loading="lazy"></iframe></div>')
import json as _js
src=src[:a]+'{"k": "task", "n": "4.4", "t": "Übung: Balkonkraftwerk-Planer", "h": '+_js.dumps(h44,ensure_ascii=False)+'}, '+src[b:]
open('lernpfad.html','w').write(src); print('4.4 ok')

# ---- Kurze Aufgabentitel statt abgeschnittener Sätze (Tom 19.11.) ----
src=open('lernpfad.html').read()
TIT={'2.3':'Was die Thermoskanne mit dem Haus gemeinsam hat','2.4':'Dämmstoffe vergleichen','2.5':'Lohnt sich die Wanddämmung?',
'3.3':'Wann Wärmebilder täuschen','4.2':'Dachboden: Geschossdecke statt Dachschräge?','4.3':'Ein Dämmstoff für Familie B',
'4.5':'Ertrag mit PVGIS berechnen','5.2':'Wärmeverlust eines neuen Fensters berechnen','6.2':'Heizungsarten vergleichen',
'6.3':'Wozu braucht das Küstenkraftwerk einen Wärmespeicher?','6.4':'Der Kieler Wärmeplan','6.5':'Wie die Wärmepumpe Wärme aus kalter Luft holt',
'6.6':'Gasheizung oder Wärmepumpe?','6.7':'Heiz- und Lüftungstipps des Umweltbundesamts','7.2':'Föhn gegen WLAN-Router','7.3':'Lohnt sich ein neuer Kühlschrank?',
'7.4':'Stand-by-Verluste vermeiden','8.2':'Glühlampe oder LED?','9.2':'Der CO₂-Fußabdruck beim Wohnen','9.4':'„Was ich mache, ist doch egal“','Z.2':'Lohnen sich smarte Thermostate?'}
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_parts=[src[:_st[0]]]; _n=0
for _a,_b in zip(_st,_st[1:]+[None]):
    _o=src[_a:_b] if _b else src[_a:]
    m=_re.match(r'\{"k": "task", "n": "([^"]+)", "t": "((?:[^"\\]|\\.)*)"',_o)
    if m and m.group(1) in TIT:
        old=m.group(2); new=TIT[m.group(1)].replace('"','\\"')
        _o=_o.replace('"t": "'+old+'"','"t": "'+new+'"',1)
        if '<h1>'+old+'</h1>' in _o: _o=_o.replace('<h1>'+old+'</h1>','<h1>'+new+'</h1>',1); _n+=1
        else: print('kein h1',m.group(1))
    _parts.append(_o)
src=''.join(_parts); print('titel',_n)
open('lernpfad.html','w').write(src)

# ---- Teil 5: U-Wert-Info mit Aufgabe 5.2 zusammenlegen, 5.2 Pflicht (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
ui=[k for k,(a,b) in enumerate(_objs) if 'Teil 5 · Info 3 von 3</div><h1>Der U-Wert</h1>' in src[a:b]][0]
ti=[k for k,(a,b) in enumerate(_objs) if src[a:b].startswith('{"k": "task", "n": "5.2"')][0]
assert ti==ui+1
uo=src[_objs[ui][0]:_objs[ui][1]]; to=src[_objs[ti][0]:_objs[ti][1]]
body=uo[uo.index('<h1>Der U-Wert</h1>')+len('<h1>Der U-Wert</h1>'):uo.rindex('"}')]
old_t='Wärmeverlust eines neuen Fensters berechnen'
to=to.replace('"t": "'+old_t+'"','"t": "Der U-Wert: Wärmeverlust eines Fensters"',1)
to=to.replace('<h1>'+old_t+'</h1>','<h1>Der U-Wert: Wärmeverlust eines Fensters</h1>'+body+'<h2 style=\\"margin-top:28px\\">Deine Aufgabe</h2>',1)
to=_re.sub(r' <span class=\\"tag star\\">★ freiwillig</span>','',to,1)
to=_re.sub(r'<div class=\\"where-box star\\">.*?</div></div>','',to,1)
to=to.replace('<h2 style=\\"margin-top:28px\\">Deine Aufgabe</h2>','<h2 style=\\"margin-top:28px\\">Freiwillige Aufgabe</h2>'+STARBOX.replace('Freiwillige Aufgabe<p>Bearbeite sie','Nur die Rechnung ist freiwillig<p>Die Erklärung oben lesen alle. Rechne die Aufgabe'),1)
to=to.replace(', "star": true}','}',1)
to=to.replace('Berechne mit der Formel aus dem Info-Kasten,','Berechne mit der Formel oben,',1)
assert 'tag star' not in to and 'Nur die Rechnung' in to
src=src[:_objs[ui][0]]+to+src[_objs[ti][1]:]
src=src.replace('Teil 5 · Info 1 von 3','Teil 5 · Info 1 von 2').replace('Teil 5 · Info 2 von 3','Teil 5 · Info 2 von 2')
open('lernpfad.html','w').write(src); print('5.2 merged')

# ---- Zwei Fortschrittsbalken: gesamt + aktueller Teil (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='<span class="bar top-bar" aria-hidden="true"><i id="topBar"></i></span><span class="pct" id="topPct"></span>'
assert a in src
src=src.replace(a,'<div class="prog2"><div class="pr"><span class="pl">Lernpfad gesamt</span><span class="bar top-bar" aria-hidden="true"><i id="allBar"></i></span><span class="pct" id="allPct"></span></div><div class="pr" id="partRow"><span class="pl" id="partLbl"></span><span class="bar top-bar" aria-hidden="true"><i id="topBar"></i></span><span class="pct" id="topPct"></span></div></div>',1)
a='function updTop(){if(!cur)return;const p=pct(cur.c);$("#topPct").textContent=p+" %";$("#topBar").style.width=p+"%";}'
assert a in src
src=src.replace(a,'''function allPct(){let d=0,n=0;CH.forEach(ch=>{if(ch.id==="zusatz"||ch.id==="anhang")return;n+=ch.slides.length;d+=S.done[ch.id].filter(i=>i<ch.slides.length).length;});return n?Math.round(100*d/n):0;}
function updTop(){const g=allPct();$("#allPct").textContent=g+" %";$("#allBar").style.width=g+"%";
  if(!cur){$("#partRow").hidden=true;return;}
  const ch=chapter(cur.c),p=pct(cur.c);$("#partRow").hidden=false;$("#partLbl").textContent=ch.short+": "+ch.title;$("#topPct").textContent=p+" %";$("#topBar").style.width=p+"%";}''',1)
a='$("#topPct").textContent="";$("#topBar").style.width="0";'
assert a in src
src=src.replace(a,'updTop();',1)
a='.where{color:var(--muted);font-size:.95rem;min-width:0;flex:1}'
assert a in src
src=src.replace(a,a+'''
body:not([data-view="home"]) .where{visibility:hidden}
.prog2{display:flex;flex-direction:column;gap:3px;align-items:stretch}
.prog2 .pr{display:grid;grid-template-columns:minmax(0,15rem) 120px 3.2em;align-items:center;gap:8px}
.prog2 .pr[hidden]{display:none}
.prog2 .pl{font-size:.8rem;color:var(--muted);text-align:right;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.prog2 .pct{font-size:.8rem}
@media (max-width:900px){.prog2 .pr{grid-template-columns:minmax(0,9rem) 70px 3em}}''',1)
open('lernpfad.html','w').write(src); print('prog2 ok')

# ---- Teil 6 Info 1: Reaktionsgleichung erklärt (Tom 19.11.) ----
src=open('lernpfad.html').read()
def _b(e): return '<i class="at at-'+e.lower()+'">'+e+'</i>'
def _mol(*a): return '<span class="mol">'+''.join(_b(x) for x in a)+'</span>'
EQ=('<div class="card rgl"><div class="rg">'
 '<div class="f">CH<sub>4</sub></div><div class="op">+</div><div class="f">2 O<sub>2</sub></div><div class="op">→</div><div class="f">CO<sub>2</sub></div><div class="op">+</div><div class="f">2 H<sub>2</sub>O</div>'
 '<div class="m">'+_mol('H','H','C','H','H')+'</div><div></div><div class="m">'+_mol('O','O')+_mol('O','O')+'</div><div></div><div class="m">'+_mol('O','C','O')+'</div><div></div><div class="m">'+_mol('H','O','H')+_mol('H','O','H')+'</div>'
 '<div class="n">Methan</div><div></div><div class="n">Sauerstoff</div><div class="n">reagiert zu</div><div class="n">Kohlenstoff&shy;dioxid</div><div></div><div class="n">Wasser</div>'
 '<div class="br" style="grid-column:1/4">Ausgangsstoffe (Edukte)</div><div></div><div class="br" style="grid-column:5/8">Produkte</div>'
 '</div><div class="leg"><div class="lt">Legende</div><div>'+_b('C')+' Kohlenstoff-Atom (C)</div><div>'+_b('H')+' Wasserstoff-Atom (H)</div><div>'+_b('O')+' Sauerstoff-Atom (O)</div></div></div>'
 '<div class="text"><p><b>So liest du eine Reaktionsgleichung:</b> Links stehen die Ausgangsstoffe, rechts die Produkte. Der Pfeil bedeutet „reagiert zu“. Jeder Stoff besteht aus winzigen Teilchen, den Molekülen, und diese sind aus Atomen aufgebaut. Die Formel zeigt, welche Atome in einem Molekül stecken: CH<sub>4</sub> ist 1 Kohlenstoff-Atom mit 4 Wasserstoff-Atomen. Die kleine Zahl unten zählt die Atome in einem Molekül, die große Zahl davor zählt die Moleküle. Bei der Verbrennung gehen keine Atome verloren und es kommen keine neuen dazu. Sie werden nur neu zusammengesetzt. Zähl nach: Links und rechts sind es jeweils 1 C, 4 H und 4 O. Mehr dazu lernst du im Chemieunterricht.</p><p>')
a='Erdgas besteht vor allem aus Methan: CH₄ + 2 O₂ → CO₂ + 2 H₂O. '
assert a in src
src=src.replace(a,'Erdgas besteht vor allem aus Methan. Bei der Verbrennung reagiert es mit dem Sauerstoff aus der Luft:</p></div>'+EQ.replace('"','\\"'),1)
src=src.replace('.where{color:var(--muted)','''.rgl{padding:18px 12px}
.rg{display:grid;grid-template-columns:repeat(7,auto);justify-content:center;align-items:center;column-gap:10px;row-gap:6px;text-align:center}
.rg .f{font-size:1.6rem;font-weight:700}.rg .op{font-size:1.5rem;font-weight:700;color:var(--muted)}
.rg .n{font-size:.85rem;color:var(--muted)}
.rg .br{border-top:3px solid var(--accent);padding-top:4px;font-size:.85rem;font-weight:700;color:var(--accent);margin-top:4px}
.mol{display:inline-flex;align-items:center;margin:2px 4px}
.at{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;font-style:normal;font-size:.8rem;font-weight:700;margin-left:-4px;border:1.5px solid #333}
.at:first-child{margin-left:0}
.at-c{background:#333;color:#fff}.at-h{background:#fff;color:#333;width:21px;height:21px;font-size:.7rem}.at-o{background:#e03131;color:#fff;border-color:#a51111}
.rgl .leg{display:flex;flex-direction:column;gap:6px;width:max-content;margin:18px auto 0;padding:10px 16px;border:1.5px dashed var(--line);border-radius:8px;font-size:.85rem;color:var(--muted)}.rgl .leg .lt{font-weight:700;color:var(--ink);font-size:.8rem;text-transform:uppercase;letter-spacing:.05em}.rgl .leg .at{margin:0 8px 0 0;vertical-align:middle}.rgl .leg .at-h{margin:0 11px 0 4px}
@media (max-width:620px){.rg{column-gap:4px}.rg .f{font-size:1.15rem}.rg .op{font-size:1.1rem}.at{width:16px;height:16px;font-size:.55rem}.at-h{width:13px;height:13px}}
.where{color:var(--muted)''',1)
open('lernpfad.html','w').write(src); print('rgl ok')

# ---- Teil 6: Karte zur Fernwärme (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='<figcaption>So kommt die Fernwärme in Kiel zu den Wohnungen (vereinfacht; Angaben: BDEW, ZfK, Stadtwerke Kiel)</figcaption></figure>'
assert a in src
k=('<figure class="fig"><img style="max-height:none;width:min(100%,700px)" src="fig/fernwaerme_karte.jpg" alt="Stadtplan von Kiel mit den Nummern 1 bis 4: 1 und 2 am Ostufer in Neumühlen-Dietrichsdorf, 3 am Theodor-Heuss-Ring südwestlich vom Südfriedhof, 4 am Schreventeich" loading="lazy">'
   '<figcaption>Wo die Anlagen liegen: 1 Küstenkraftwerk und 2 Wärmespeicher am Ostufer, 3 Müllverbrennung, 4 Heizkraftwerk Humboldtstraße. Die Fernwärmerohre verbinden sie unter der Erde mit den Häusern auf beiden Seiten der Förde. Karte: <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">© OpenStreetMap-Mitwirkende</a>, Lizenz ODbL</figcaption></figure>')
src=src.replace(a,a+k.replace('"','\\"'),1)
open('lernpfad.html','w').write(src); print('karte ok')

# ---- Wärmepumpen-Schema groß anzeigen ----
src=open('lernpfad.html').read()
a='<img src=\\"fig/wp_haus.png\\"'
assert a in src
src=src.replace(a,'<img style=\\"max-height:none;width:min(100%,860px)\\" src=\\"fig/wp_haus.png?v=3\\"',1)
open('lernpfad.html','w').write(src); print('wp_haus ok')

# ---- Teil 6: Info 4 (Heizen/Lüften) und Info 5 (Warmes Wasser) zusammenlegen (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
hi=[k for k,(a,b) in enumerate(_objs) if 'Teil 6 · Info 4 von 6</div><h1>Richtig heizen und lüften</h1>' in src[a:b]][0]
wi=[k for k,(a,b) in enumerate(_objs) if 'Teil 6 · Info 5 von 6</div><h1>Warmes Wasser</h1>' in src[a:b]][0]
assert wi==hi+1
ho=src[_objs[hi][0]:_objs[hi][1]]; wo=src[_objs[wi][0]:_objs[wi][1]]
hb=ho[ho.index('<h1>Richtig heizen und lüften</h1>')+len('<h1>Richtig heizen und lüften</h1>'):ho.rindex('"}')]
wb=wo[wo.index('<h1>Warmes Wasser</h1>')+len('<h1>Warmes Wasser</h1>'):wo.rindex('"}')]
NT='Kleine Stellschrauben: Heizen, Lüften, Duschen'
INTRO='<div class=\\"text\\"><p>Nicht nur eine neue Heizung spart Energie. Auch kleine Stellschrauben im Alltag bringen viel und kosten wenig oder gar nichts: die richtige Raumtemperatur, richtiges Lüften und sparsames Duschen.</p></div>'
H2='<h2 style=\\"margin-top:24px\\">%s</h2>'
new=ho[:ho.index('"t": "Richtig heizen und lüften"')]+'"t": "'+NT+'", "h": "<div class=\\"eyebrow\\">Teil 6 · Info 4 von 5</div><h1>'+NT+'</h1>'+INTRO+H2%'Richtig heizen und lüften'+hb+H2%'Warmes Wasser beim Duschen'+wb+'"}'+ho[ho.rindex('"}')+2:]
src=src[:_objs[hi][0]]+new+src[_objs[wi][1]:]
for i in (1,2,3): src=src.replace('Teil 6 · Info %d von 6'%i,'Teil 6 · Info %d von 5'%i)
src=src.replace('Teil 6 · Info 6 von 6','Teil 6 · Info 5 von 5')
assert 'von 6</div>' not in src.split('Teil 6 ·',1)[1].split('Teil 7')[0]
open('lernpfad.html','w').write(src); print('6 info merged')

# ---- Teil 6: „Wasserkocher“-Folie in die Stellschrauben-Folie (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
WT='Warmes Wasser in den Wasserkocher – lohnt sich das?'
ki=[k for k,(a,b) in enumerate(_objs) if src[a:b].startswith('{"k": "info", "t": "'+WT+'"')][0]
si=[k for k,(a,b) in enumerate(_objs) if '<h1>Kleine Stellschrauben' in src[a:b]][0]
ko=src[_objs[ki][0]:_objs[ki][1]]
kb=ko[ko.index('<h1>'+WT+'</h1>')+len('<h1>'+WT+'</h1>'):ko.rindex('"}')]
so=src[_objs[si][0]:_objs[si][1]]
p=so.rindex('"}')
so=so[:p]+'<h2 style=\\"margin-top:24px\\">'+WT+'</h2>'+kb+so[p:]
assert si<ki
src=src[:_objs[si][0]]+so+src[_objs[si][1]:_objs[ki][0]]+src[_objs[ki][1]:]
assert src.count(WT)==1
open('lernpfad.html','w').write(src); print('wasserkocher merged')

# ---- 6.2: Kurztexte statt co2online-Link (Tom 19.11.) ----
src=open('lernpfad.html').read()
a=src.index('<h1>Heizungsarten vergleichen</h1><p class=\\"task-q\\">'); b=src.index('</p>',a)+4
HA=[('Gasheizung (Brennwert)','Verbrennt Erdgas aus dem Gasnetz. Ein Brennwertgerät nutzt sogar die Wärme im Abgas. Die Anlage ist recht günstig und braucht wenig Platz. Beim Verbrennen entsteht aber viel CO₂, und der Gaspreis schwankt stark.'),
('Ölheizung','Verbrennt Heizöl, das in einem Tank im Keller lagert. Sie braucht kein Gasnetz. Pro kWh Wärme entsteht noch mehr CO₂ als bei Gas, und der Tank braucht Platz. Neue Ölheizungen werden kaum noch eingebaut.'),
('Fernwärme','Heißes Wasser kommt aus einem Kraftwerk oder aus Abwärme über Rohre ins Haus. Im Haus braucht man nur eine kleine Übergabestation, keinen eigenen Brenner und keinen Schornstein. Man ist aber an den örtlichen Anbieter gebunden. Wie klimafreundlich Fernwärme ist, hängt davon ab, womit das Kraftwerk heizt.'),
('Holzpelletheizung','Verbrennt kleine Presslinge aus Holzresten. Holz wächst nach und hat beim Wachsen so viel CO₂ aufgenommen, wie beim Verbrennen frei wird. Man braucht aber einen Lagerraum für die Pellets, und beim Verbrennen entsteht Feinstaub.'),
('Wärmepumpe','Holt mit Strom Wärme aus der Luft, dem Erdreich oder dem Grundwasser. Aus 1 kWh Strom werden 3 bis 4 kWh Wärme. Mit Ökostrom entsteht fast kein CO₂. Die Anschaffung ist teuer, und sie arbeitet am besten in einem gut gedämmten Haus mit großen Heizkörpern oder Fußbodenheizung.')]
txt='<p class=\\"task-q\\">Lies die Kurzinfos zu den fünf Heizungsarten. Lege die Tabelle in deiner Mappe an und trage für jede Heizungsart den Energieträger, einen Vorteil und einen Nachteil ein.</p><div class=\\"card\\"><h2>Kurzinfos</h2>'+''.join('<p><b>%s:</b> %s</p>'%(n,t) for n,t in HA)+'</div>'
src=src[:a]+'<h1>Heizungsarten vergleichen</h1>'+txt+src[b:]
c=src.index('<details class=\\"tip\\"><summary>Tipp 1</summary><div>Wenn die Seite von co2online nicht lädt'); d=src.index('</details>',c)+len('</details>')
src=src[:c]+src[d:]
open('lernpfad.html','w').write(src); print('6.2 ok')

# ---- 6.3 (Wärmespeicher) streichen, 6.4-6.8 umnummerieren (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
k3=[k for k,(a,b) in enumerate(_objs) if src[a:b].startswith('{"k": "task", "n": "6.3"')][0]
assert 'Wärmespeicher' in src[_objs[k3][0]:_objs[k3][1]]
src=src[:_objs[k3][0]]+src[_objs[k3+1][0]:]
for i in range(4,9):
    src=src.replace('"n": "6.%d"'%i,'"n": "6.%d"'%(i-1)).replace('Teil 6 · Aufgabe 6.%d '%i,'Teil 6 · Aufgabe 6.%d '%(i-1))
assert '"n": "6.8"' not in src
open('lernpfad.html','w').write(src); print('6.3 removed')

# ---- 6.5: JAZ erklären, Werte als Liste; 6.6: UBA-Seiten als Text (Tom 19.11.) ----
src=open('lernpfad.html').read()
_i=src.index('<h1>Gasheizung oder Wärmepumpe?</h1>')+len('<h1>Gasheizung oder Wärmepumpe?</h1>')
_j=src.index('</p>',_i)+4
assert 'JAZ 3,5' in src[_i:_j]
a=src[_i:_j]
b=('<p class=\\"task-q\\">Ein Haus braucht im Jahr 15&#8239;000 kWh Wärme. Vergleiche eine Gasheizung mit einer Luftwärmepumpe.</p>'
 '<div class=\\"card\\"><h2>Das brauchst du für die Rechnung</h2>'
 '<p><b>Jahresarbeitszahl (JAZ) 3,5:</b> Die Wärmepumpe macht übers Jahr gerechnet aus 1 kWh Strom 3,5 kWh Wärme. Den Rest holt sie kostenlos aus der Außenluft. Im kalten Winter schafft sie etwas weniger, in der Übergangszeit mehr. Die JAZ ist der Durchschnitt über das ganze Jahr.</p>'
 '<ul class=\\"bullets\\"><li><b>Gas:</b> 0,12 € pro kWh und 0,24 kg CO₂ pro kWh</li><li><b>Strom für die Wärmepumpe:</b> 0,28 € pro kWh und 0,34 kg CO₂ pro kWh</li></ul></div>')
src=src.replace(a,b,1)

UBA=('<div class=\\"card\\"><h2>Richtig heizen und lüften (nach dem Umweltbundesamt)</h2>'
 '<p><b>Die richtige Temperatur:</b> Das Umweltbundesamt empfiehlt etwa 20 °C im Wohnzimmer, 18 °C in der Küche und 17 °C im Schlafzimmer. Jedes Grad weniger spart etwa 6 % Heizenergie. Nachts und wenn niemand zu Hause ist, kann die Temperatur etwas sinken, die Räume sollten aber nicht ganz auskühlen. Am Thermostat entspricht Stufe 3 ungefähr 20 °C. Türen zwischen warmen und kühlen Räumen bleiben geschlossen.</p>'
 '<p><b>Die Wärme muss in den Raum kommen:</b> Heizkörper sollten nicht von Möbeln oder langen Vorhängen verdeckt sein. Nachts halten geschlossene Rollläden oder Vorhänge die Wärme im Raum. Gluckert der Heizkörper oder wird er oben nicht richtig warm, muss er entlüftet werden.</p>'
 '<p><b>Warum lüften?</b> Menschen geben beim Atmen, Duschen und Kochen viel Wasserdampf an die Raumluft ab. Bleibt die Feuchtigkeit im Raum, kann sich Schimmel bilden. Warme Luft kann viel Wasserdampf aufnehmen. Trifft sie auf eine kalte Fläche, wird ein Teil davon wieder zu Wasser, so wie am Badezimmerspiegel nach dem Duschen.</p>'
 '<p><b>So lüftet man richtig:</b> Mehrmals am Tag das Fenster für wenige Minuten weit öffnen (Stoßlüften), im Winter reichen etwa 5 Minuten. Noch besser ist Querlüften mit zwei gegenüberliegenden Fenstern. Dabei wird die feuchte Luft schnell ausgetauscht, die Wände bleiben aber warm. Während des Lüftens dreht man das Thermostat herunter. Nach dem Duschen und Kochen sollte man immer lüften.</p>'
 '<p><b>Das gekippte Fenster:</b> Durch einen Spalt wird die Luft nur langsam ausgetauscht. Das Fenster bleibt deshalb lange offen, und die Heizung darunter heizt die ganze Zeit nach draußen. Die Wand rund um das Fenster kühlt dabei stark aus.</p>'
 '<p style=\\"font-size:.85rem;color:var(--muted)\\">Zusammengefasst nach den Seiten „Richtiges Heizen“ und „Wie lüfte ich richtig?“ des Umweltbundesamts.</p></div>')
a=src.index('<h1>Heiz- und Lüftungstipps des Umweltbundesamts</h1><p class=\\"task-q\\">'); b=src.index('</p>',a)+4
src=src[:a]+'<h1>Heiz- und Lüftungstipps des Umweltbundesamts</h1><p class=\\"task-q\\">Lies den Text und bearbeite dann die Aufgaben.</p>'+UBA+src[b:]
c=src.index('<details class=\\"tip\\"><summary>Tipp 1</summary><div>Auf der Seite „Richtiges Heizen“'); d=src.index('</details>',c)+len('</details>')
src=src[:c]+'<details class=\\"tip\\"><summary>Tipp 1</summary><div>b) Verbinde zwei Stellen im Text: Was passiert mit der Wand neben dem Fenster? Und was passiert, wenn warme, feuchte Raumluft auf eine kalte Fläche trifft?</div></details>'+src[d:]
src=src.replace('<li>b) Erkläre, warum ein dauerhaft gekipptes Fenster im Winter Energie verschwendet und Schimmel fördern kann.</li>','<li>b) Erkläre, warum ein dauerhaft gekipptes Fenster im Winter Energie verschwendet und Schimmel fördern kann.</li>',1)
open('lernpfad.html','w').write(src); print('6.5/6.6 ok')

# ---- 6.7 Warmduscher: Werte übersichtlich, Tabellenzeilen benannt (Tom 19.11.) ----
src=open('lernpfad.html').read()
a=src.index('<h1>Die Warmduscher-Rechnung</h1><p class=\\"task-q\\">'); b=src.index('</ul>',a)+5
assert 'Trage deine Ergebnisse' in src[a:b]
new=('<h1>Die Warmduscher-Rechnung</h1><p class=\\"task-q\\">Jemand duscht gern lange und warm. Wie viel Energie, Geld und CO₂ kostet das? Die Wohnung wird mit Gas beheizt.</p>'
 '<div class=\\"card\\"><h2>Das brauchst du für die Rechnung</h2><ul class=\\"bullets\\">'
 '<li><b>Normaler Duschkopf:</b> 13 Liter pro Minute</li>'
 '<li><b>Sparduschkopf:</b> 7 Liter pro Minute</li>'
 '<li><b>Wassertemperatur:</b> von 10 °C auf 40 °C, also 30 °C wärmer</li>'
 '<li><b>Gas:</b> 0,12 € und 0,24 kg CO₂ pro kWh Wärme</li>'
 '<li><b>Ein Jahr:</b> 300 Duschen</li></ul>'
 '<p><b>Rechenhilfe:</b> Energie (Wh) = Liter · 30 °C · 1,16 Wh pro Liter und °C<br>Kosten (€) = kWh · 0,12 €<br>CO₂ (kg) = kWh · 0,24 kg</p></div>'
 '<p class=\\"task-q\\">Berechne für jede Dusche die Wassermenge, die Energie, die Kosten und das CO₂. Trage die Ergebnisse in die Tabelle in deiner Mappe ein.</p>'
 '<ul class=\\"bullets\\" style=\\"list-style:none;padding-left:0\\">'
 '<li>a) 15 Minuten duschen mit normalem Duschkopf</li>'
 '<li>b) 15 Minuten duschen mit Sparduschkopf</li>'
 '<li>c) 5 Minuten duschen mit Sparduschkopf</li>'
 '<li>d) Rechne alle drei auf ein Jahr hoch.</li>'
 '<li>e) Berechne, wie viel Prozent Energie c) gegenüber a) spart.</li></ul>')
src=src[:a]+new+src[b:]
for o,n in (('a)','a) 15 min duschen'),('b)','b) 15 min + Sparduschkopf'),('c)','c) 5 min + Sparduschkopf')):
    x='<tr><td>%s</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>'%o
    i=src.index(x,a); src=src[:i]+x.replace('<td>%s</td>'%o,'<td style=\\"white-space:nowrap\\">%s</td>'%n,1)+src[i+len(x):]
open('lernpfad.html','w').write(src); print('6.7 ok')

# ---- Teil 7: drei Infos zu einer zusammenlegen, E = P · t erklären (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
def _find(s): return [k for k,(a,b) in enumerate(_objs) if s in src[a:b]][0]
i1=_find('Teil 7 · Info 1 von 3</div>'); i2=_find('Teil 7 · Info 2 von 3</div>'); i3=_find('Teil 7 · Info 3 von 3</div>')
assert i2==i1+1 and i3==i1+2
def _body(k,h1):
    o=src[_objs[k][0]:_objs[k][1]]; t='<h1>'+h1+'</h1>'
    return o[o.index(t)+len(t):o.rindex('"}')]
b1=_body(i1,'Leistung auf dem Typenschild'); b2=_body(i2,'Stand-by: heimliche Stromfresser'); b3=_body(i3,'Das Energielabel')
old='Erinnerung aus Teil 1, <b>E = P · t</b>.'
assert old in b1
b1=b1.replace(old,'Erinnerung aus Teil 1: <b>E = P · t</b>, also <b>Energie = Leistung · Zeit</b>. Ein Wasserkocher mit 2 000 W (= 2 kW), der 3 Minuten läuft (3 : 60 = 0,05 h, denn eine Stunde hat 60 Minuten), braucht 2 kW · 0,05 h = 0,1 kWh. Damit die Einheit kWh herauskommt, rechnet man die Leistung in kW und die Zeit in Stunden um.',1)
NT='Strom im Haushalt: Leistung, Stand-by und Energielabel'
H2='<h2 style=\\"margin-top:24px\\">%s</h2>'
o1=src[_objs[i1][0]:_objs[i1][1]]
new=o1[:o1.index('"t": "Leistung auf dem Typenschild"')]+'"t": "'+NT+'", "h": "<div class=\\"eyebrow\\">Teil 7 · Info</div><h1>'+NT+'</h1>'+H2%'Leistung auf dem Typenschild'+b1+H2%'Stand-by: heimliche Stromfresser'+b2+H2%'Das Energielabel'+b3+'"}'+o1[o1.rindex('"}')+2:]
src=src[:_objs[i1][0]]+new+src[_objs[i3][1]:]
open('lernpfad.html','w').write(src); print('teil7 merged')

# ---- Sicherheitshinweis Lampen (Tom 19.11.) ----
src=open('lernpfad.html').read()
a='<li>Wie viele Stunden pro Tag brennen die Lampen in den meistgenutzten Räumen ungefähr?</li></ul>'
n=src.count(a); assert n==2, n
SAFE=('<div style=\\"margin-top:12px;padding:10px 14px;border:2px solid #c92a2a;border-radius:8px;background:#fff5f5;color:#1a1a1a\\">'
 '<b style=\\"color:#c92a2a\\">⚠ Sicherheit: Schraube keine Lampe heraus!</b> In der Fassung liegt Strom an, solange die Sicherung eingeschaltet ist, auch wenn der Lichtschalter aus ist. '
 'Eine eingeschaltete Lampe kann außerdem sehr heiß werden. Lies nur ab, was du siehst, ohne die Lampe anzufassen, schau auf Verpackungen von Ersatzlampen nach oder frag deine Eltern. '
 'Erkennst du eine Lampe nicht, schreib „unbekannt“.</div>')
src=src.replace(a,a+SAFE)
open('lernpfad.html','w').write(src); print('safety ok')

# ---- Teil 8: fünf Infos zu einer zusammenlegen (Tom 19.11.) ----
src=open('lernpfad.html').read()
_st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
_objs=[]
for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
ks=[[k for k,(a,b) in enumerate(_objs) if 'Teil 8 · Info %d von 5</div>'%i in src[a:b]][0] for i in range(1,6)]
assert ks==list(range(ks[0],ks[0]+5))
parts=[]
for n,k in enumerate(ks):
    o=src[_objs[k][0]:_objs[k][1]]
    h1=_re.search(r'<h1>(.*?)</h1>',o).group(1)
    body=o[o.index('</h1>')+5:o.rindex('"}')]
    parts.append(body if n==0 else '<h2 style=\\"margin-top:24px\\">'+h1+'</h2>'+body)
o1=src[_objs[ks[0]][0]:_objs[ks[0]][1]]
new=o1[:o1.index('<div class=\\"eyebrow\\">')]+'<div class=\\"eyebrow\\">Teil 8 · Info</div><h1>Lampen im Vergleich</h1>'+''.join(parts)+'"}'+o1[o1.rindex('"}')+2:]
src=src[:_objs[ks[0]][0]]+new+src[_objs[ks[4]][1]:]
open('lernpfad.html','w').write(src); print('teil8 merged')

# ---- Teil 9: vier Infos zu zwei zusammenlegen (Tom 19.11.) ----
src=open('lernpfad.html').read()
for (x,y,tit,neu) in ((1,2,'Der CO₂-Fußabdruck: was er misst und woher er kommt','1 von 2'),(3,4,'Was kann ich tun? Fußabdruck und Handabdruck','2 von 2')):
    _st=[m.start() for m in _re.finditer(r'\{"k": "',src)]
    _objs=[]
    for _a,_b in zip(_st,_st[1:]+[None]): _objs.append((_a,_b if _b else len(src)))
    ks=[[k for k,(a,b) in enumerate(_objs) if 'Teil 9 · Info %d von 4</div>'%i in src[a:b]][0] for i in (x,y)]
    assert ks[1]==ks[0]+1
    parts=[]
    for k in ks:
        o=src[_objs[k][0]:_objs[k][1]]
        h1=_re.search(r'<h1>(.*?)</h1>',o).group(1)
        parts.append('<h2 style=\\"margin-top:24px\\">'+h1+'</h2>'+o[o.index('</h1>')+5:o.rindex('"}')])
    o1=src[_objs[ks[0]][0]:_objs[ks[0]][1]]
    t0=_re.search(r'"t": "(.*?)", "h"',o1).group(1)
    head=o1[:o1.index('<div class=\\"eyebrow\\">')].replace('"t": "'+t0+'"','"t": "'+tit+'"',1)
    new=head+'<div class=\\"eyebrow\\">Teil 9 · Info '+neu+'</div><h1>'+tit+'</h1>'+''.join(parts)+'"}'+o1[o1.rindex('"}')+2:]
    src=src[:_objs[ks[0]][0]]+new+src[_objs[ks[1]][1]:]
open('lernpfad.html','w').write(src); print('teil9 merged')
