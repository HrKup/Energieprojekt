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
    "<p>Hast du diese Daten schon von zu Hause? Wenn nicht, notiere dir als Hausaufgabe: Das brauchst du für die nächste Stunde.</p><ul class=\"bullets\" style=\"color:var(--ink);font-weight:400\"><li>Anzahl der Personen im Haushalt und Wohnfläche</li><li>Baujahr und, falls vorhanden, den Energieausweis</li><li>Heizverbrauch und Stromverbrauch pro Jahr mit Kosten (Jahresabrechnung, Eltern fragen)</li></ul>")
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
