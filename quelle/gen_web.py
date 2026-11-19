"""Erzeugt teile.js (Teile 2-9, Zusatz, Anhang) aus content.json + Extras (Tipps, Prüffelder)."""
import json, re, html
SP = '/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/web/'
D = json.load(open(SP + 'content.json'))
LP, PR = D['lp'], {int(k): v for k, v in D['proto'].items()}
SITE = 'https://hrkup.github.io/Energieprojekt/'

def md(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    return t

def rich(parts):
    out = ''
    for p in parts:
        if p[0] == 't': out += md(p[1])
        else: out += f'<a href="{p[2]}" target="_blank" rel="noopener">{md(p[1])}</a>'
    return out

def fix_task_text(t):
    t = t.replace('direkt in die Tabelle hier in der Datei ein', 'in eine Tabelle in deiner Mappe ein')
    t = t.replace('Trage deine Ergebnisse direkt in die Tabelle hier in der Datei ein.', 'Lege dafür die Tabelle unten in deiner Mappe an.')
    return t

TOOLS = {'Dämm-Quiz': 'daemm-quiz.html', 'Solar-Helfer': 'solar-helfer.html', 'CO₂-Regler': 'co2-regler.html', 'Energieausweis-Rechner': 'energieausweis-rechner.html'}

# ---------- Extras: Tipps (konkret, ohne Formelzeichen) und Prüffelder ----------
# check: (label, richtig, toleranz, einheit)
X = {
 '2.4': {'tips': [
   'Auf der Seite des Umweltbundesamts steht ein Abschnitt „Dämmstoffe“. Die drei Gruppen heißen dort nicht ausdrücklich so. Ordne die Beispiele selbst zu: Steinwolle und Glaswolle sind mineralisch, Polystyrol ist ein Kunststoff, Holzfaser und Zellulose wachsen nach.',
   'Wenn du einen Nachteil nicht findest: Mineralwolle kratzt bei der Verarbeitung und ihre Herstellung braucht viel Energie (siehe auch Teil 4). Kunststoff wird aus Erdöl hergestellt und lässt sich schwer recyceln. Nachwachsende Dämmstoffe dämmen etwas schlechter, die Schicht muss also dicker sein.']},
 '2.5': {'tips': [
   'a) Wie viel geht durch die Wände? 35 % von 20 000 kWh: 20 000 kWh · 35 : 100 = 7 000 kWh.',
   'b) Die Dämmung spart 70 % von diesen 7 000 kWh: 7 000 kWh · 70 : 100 = … kWh. Für das Geld nimmst du das Ergebnis mal 0,12 €.',
   'c) Teile die Einsparung durch die 20 000 kWh des ganzen Hauses und nimm mal 100. d) 24 000 € geteilt durch die Ersparnis pro Jahr in €.'],
  'check': [('a) Verlust über die Wände', 7000, 10, 'kWh'), ('b) Einsparung', 4900, 10, 'kWh'), ('b) Einsparung', 588, 2, '€'), ('c) Anteil am ganzen Haus', 24.5, 0.6, '%'), ('d) Amortisationszeit', 40.8, 0.6, 'Jahre')],
  'sol': 'a) 20 000 kWh · 35 : 100 = <b>7 000 kWh</b><br>b) 7 000 kWh · 70 : 100 = <b>4 900 kWh</b>; 4 900 kWh · 0,12 € = <b>588 €</b><br>c) 4 900 : 20 000 · 100 = <b>24,5 %</b><br>d) 24 000 € : 588 € pro Jahr ≈ <b>41 Jahre</b>. Das ist sehr lang. Nur wegen der Heizkosten lohnt sich die Dämmung kaum, sinnvoll ist sie, wenn die Fassade ohnehin erneuert wird.'},
 '4.4': {'tips': ['240° liegt zwischen Süden (180°) und Westen (270°), also Südwest.', 'Für PVGIS rechnest du: 240° minus 180° = 60°.'],
  'check': [('Azimut für PVGIS', 60, 0.5, '°')], 'sol': '240° ist <b>Südwest</b>. Azimut: 240° − 180° = <b>60°</b>. Südwest ist gut geeignet: Der Balkon bekommt viel Nachmittagssonne.'},
 '4.5': {'tips': ['Beispiel, falls PVGIS 500 kWh liefert: Die Hälfte nutzt der Haushalt selbst, also 250 kWh. 250 kWh · 0,35 € = 87,50 € Ersparnis pro Jahr.', 'Amortisation im Beispiel: 450 € : 87,50 € ≈ 5,1 Jahre. Rechne genauso mit deinem Wert aus PVGIS.']},
 '5.2': {'tips': [
   'a) Mach es wie in der Grafik, nur mit dem U-Wert von Dreifachglas aus der Tabelle: 0,6 · 2 · 12 = … W.',
   'b) Das Ergebnis aus a) mal 5 000 Stunden ergibt Wattstunden. Durch 1 000 geteilt sind es kWh. c) kWh mal 0,12 €.',
   'd) Das Einfachfenster kostet laut Grafik etwa 83 € im Jahr. Zieh deine Kosten aus c) davon ab. e) 900 € geteilt durch die Ersparnis aus d).'],
  'check': [('a) Leistung', 14.4, 0.2, 'W'), ('b) Energie', 72, 1, 'kWh'), ('c) Kosten', 8.64, 0.1, '€'), ('d) Ersparnis', 74.5, 1, '€'), ('e) Amortisationszeit', 12, 0.4, 'Jahre')],
  'sol': 'a) 0,6 · 2 · 12 = <b>14,4 W</b><br>b) 14,4 W · 5 000 h = 72 000 Wh = <b>72 kWh</b><br>c) 72 kWh · 0,12 € ≈ <b>8,64 €</b><br>d) 83,40 € − 8,64 € ≈ <b>75 € pro Jahr</b><br>e) 900 € : 75 € ≈ <b>12 Jahre</b>. Nur wegen der Heizkosten lohnt sich der Tausch kaum. Dazu kommen aber weniger Zugluft und mehr Behaglichkeit.'},
 '6.2': {'tips': ['Wenn die Seite von co2online nicht lädt, nutze diese Übersicht:<div class="tbl"><table><thead><tr><th>Heizungsart</th><th>Energieträger</th><th>ein Vorteil</th><th>ein Nachteil</th></tr></thead><tbody>'
   '<tr><td>Gasheizung</td><td>Erdgas</td><td>günstig in der Anschaffung</td><td>verursacht viel CO₂, Gaspreis kann steigen</td></tr>'
   '<tr><td>Ölheizung</td><td>Heizöl</td><td>unabhängig vom Gasnetz</td><td>noch mehr CO₂, Tank braucht Platz</td></tr>'
   '<tr><td>Fernwärme</td><td>Wärme aus Kraftwerk oder Abwärme</td><td>keine eigene Heizung im Haus nötig</td><td>man ist an einen Anbieter gebunden</td></tr>'
   '<tr><td>Wärmepumpe</td><td>Strom und Umweltwärme</td><td>sehr wenig CO₂, wenn Ökostrom genutzt wird</td><td>teuer in der Anschaffung, braucht gut gedämmtes Haus</td></tr>'
   '<tr><td>Pelletheizung</td><td>Holz</td><td>fast CO₂-neutral</td><td>Lager für Pellets nötig, Feinstaub</td></tr></tbody></table></div>']},
 '6.6': {'tips': [
   'a) Gas: 15 000 kWh · 0,12 € = … €.',
   'b) Die Wärmepumpe macht aus 1 kWh Strom 3,5 kWh Wärme. Strombedarf: 15 000 kWh : 3,5 ≈ 4 286 kWh. Kosten: 4 286 kWh · 0,28 € = … €.',
   'c) Ersparnis: Gaskosten minus Wärmepumpenkosten. CO₂: 15 000 kWh · 0,24 kg und 4 286 kWh · 0,34 kg ausrechnen und abziehen. d) 12 000 € geteilt durch die Ersparnis pro Jahr.'],
  'check': [('a) Gas', 1800, 2, '€'), ('b) Strombedarf', 4286, 5, 'kWh'), ('b) Wärmepumpe', 1200, 3, '€'), ('c) Ersparnis', 600, 4, '€'), ('c) CO₂-Ersparnis', 2143, 10, 'kg'), ('d) Amortisationszeit', 20, 0.3, 'Jahre')],
  'sol': 'a) 15 000 kWh · 0,12 € = <b>1 800 €</b><br>b) 15 000 kWh : 3,5 ≈ <b>4 286 kWh</b> Strom; 4 286 kWh · 0,28 € ≈ <b>1 200 €</b><br>c) 1 800 € − 1 200 € = <b>600 €</b> pro Jahr; CO₂: 3 600 kg − 1 457 kg ≈ <b>2 143 kg</b><br>d) 12 000 € : 600 € = <b>20 Jahre</b>. Finanziell dauert es lange, fürs Klima bringt die Wärmepumpe sehr viel.'},
 '6.7': {'tips': ['Auf der Seite „Richtiges Heizen“ stehen die Temperaturen im Abschnitt mit den Empfehlungen für die Räume.']},
 '6.8': {'tips': [
   'a) Erst die Liter: 15 Minuten · 13 Liter = 195 Liter. Dann die Energie: 195 Liter · 30 °C · 1,16 Wh ≈ 6 786 Wh, das sind etwa 6,8 kWh.',
   'Kosten und CO₂: 6,8 kWh · 0,12 € und 6,8 kWh · 0,24 kg. Für b) und c) rechnest du genauso mit 7 Litern pro Minute.',
   'd) Jedes Ergebnis mal 300. e) Unterschied zwischen a) und c) geteilt durch a), mal 100.'],
  'check': [('a) Energie', 6.79, 0.1, 'kWh'), ('b) Energie', 3.65, 0.1, 'kWh'), ('c) Energie', 1.22, 0.05, 'kWh'), ('d) a) pro Jahr', 2036, 30, 'kWh'), ('e) Ersparnis', 82, 1, '%')],
  'sol': 'a) 195 l · 30 · 1,16 Wh ≈ <b>6,8 kWh</b>, 0,81 €, 1,6 kg CO₂<br>b) 105 l → <b>3,7 kWh</b>, 0,44 €, 0,9 kg<br>c) 35 l → <b>1,2 kWh</b>, 0,15 €, 0,3 kg<br>d) pro Jahr: a) <b>2 036 kWh</b> und 244 €, b) 1 096 kWh und 132 €, c) 365 kWh und 44 €<br>e) (6,8 − 1,2) : 6,8 · 100 ≈ <b>82 %</b>'},
 '7.2': {'tips': [
   'Föhn: 1 800 W sind 1,8 kW, 6 Minuten sind 0,1 Stunden. Pro Tag: 1,8 kW · 0,1 h = 0,18 kWh. Mal 365 Tage, dann mal 0,35 €.',
   'Router: 8 W sind 0,008 kW. Er läuft das ganze Jahr, also 8 760 Stunden: 0,008 kW · 8 760 h = … kWh. Dann mal 0,35 €.'],
  'check': [('Föhn pro Jahr', 65.7, 0.5, 'kWh'), ('Föhn', 23.0, 0.3, '€'), ('Router pro Jahr', 70.1, 0.5, 'kWh'), ('Router', 24.53, 0.3, '€')],
  'sol': 'Föhn: 0,18 kWh · 365 = <b>65,7 kWh</b>, 65,7 · 0,35 € ≈ <b>23,00 €</b><br>Router: 0,008 kW · 8 760 h ≈ <b>70,1 kWh</b>, ≈ <b>24,53 €</b><br>Der kleine Router kostet mehr, weil er nie ausgeschaltet wird.'},
 '7.3': {'tips': ['a) Ersparnis: 360 kWh − 120 kWh = 240 kWh. Dann mal 0,35 € und mal 0,34 kg.', 'b) 650 € geteilt durch die Ersparnis in € pro Jahr.'],
  'check': [('a) Ersparnis', 240, 1, 'kWh'), ('a) Ersparnis', 84, 0.5, '€'), ('a) CO₂', 81.6, 0.5, 'kg'), ('b) Amortisationszeit', 7.7, 0.2, 'Jahre')],
  'sol': 'a) <b>240 kWh</b>, 240 · 0,35 € = <b>84 €</b>, 240 · 0,34 kg = <b>81,6 kg CO₂</b><br>b) 650 € : 84 € ≈ <b>7,7 Jahre</b><br>c) Lohnt sich, wenn der alte Kühlschrank viel verbraucht oder ohnehin kaputt ist. Ein noch gutes, sparsames Gerät weiterzunutzen ist oft besser, weil die Herstellung eines neuen auch Energie kostet.'},
 '8.2': {'tips': [
   'a) Eine Glühlampe hält etwa 1 000 Stunden (Tabelle). Für 15 000 Stunden brauchst du 15 000 : 1 000 = 15 Glühlampen. Kaufkosten: 15 · 1,50 €.',
   'b) Glühlampe: 60 W sind 0,06 kW. 0,06 kW · 15 000 h = … kWh, dann mal 0,35 €. LED genauso mit 0,008 kW.'],
  'check': [('a) Kauf Glühlampen', 22.5, 0.1, '€'), ('b) Strom Glühlampe', 315, 1, '€'), ('b) Strom LED', 42, 0.5, '€')],
  'sol': 'a) 15 Glühlampen · 1,50 € = <b>22,50 €</b>, LED: <b>5 €</b><br>b) Glühlampe: 900 kWh · 0,35 € = <b>315 €</b>; LED: 120 kWh · 0,35 € = <b>42 €</b><br>c) Die LED spart über ihre Lebensdauer rund 290 €.'},
 '9.2': {'tips': ['a) Heizung: 12 000 kWh · 0,24 kg. Strom: 2 700 kWh · 0,34 kg. Zusammenzählen, dann durch 3 Personen teilen.', 'b) Rechne kg in t um (durch 1 000) und vergleiche mit 10 t: Anteil = dein Wert : 10 · 100.'],
  'check': [('a) Heizung', 2880, 5, 'kg'), ('a) Strom', 918, 3, 'kg'), ('a) pro Person', 1266, 10, 'kg'), ('b) Anteil', 12.7, 0.5, '%')],
  'sol': 'a) Heizung <b>2 880 kg</b>, Strom <b>918 kg</b>, zusammen 3 798 kg, pro Person ≈ <b>1 266 kg</b> (1,3 t)<br>b) 1,27 t : 10 t · 100 ≈ <b>13 %</b>'},
}

def checker_html(tid, ch, sol):
    cid = 'c' + tid.replace('.', '_')
    f = ''.join(f'<label for="{cid}_{i}">{html.escape(c[0])}<input id="{cid}_{i}" inputmode="decimal" autocomplete="off" placeholder="{c[3]}"></label>' for i, c in enumerate(ch))
    return (f'<div class="card"><h2>Ergebnis prüfen</h2><div class="check">{f}<button class="btn" data-check="{cid}">Prüfen</button></div>'
            f'<div class="fb" id="{cid}_fb" hidden></div><details class="tip"><summary>Lösung anzeigen</summary><div class="sol">{sol}</div></details></div>'), cid, [[c[1], c[2]] for c in ch]

def tips_html(tl):
    return ''.join(f'<details class="tip"><summary>Tipp {i+1}</summary><div>{t}</div></details>' for i, t in enumerate(tl))

MAPPE = '<div class="where-box mappe"><span class="ic">✎</span><div>In deine Mappe<p>Bearbeite die Aufgabe in deiner Mappe.</p></div></div>'
CALC_MAPPE = '<div class="where-box mappe"><span class="ic">✎</span><div>In deine Mappe<p>Schreib den Rechenweg und die Ergebnisse mit Einheit in deine Mappe. Hier kannst du sie danach prüfen.</p></div></div>'

def zuhause_box(teil, first):
    z = PR.get(teil, {}).get('zuhause') or []
    if not z: return ''
    li = ''.join(f'<li>{md(x)}</li>' for x in z)
    return (f'<div class="where-box proto"><span class="ic">▤</span><div>Bevor du beginnst<p>Hake ab, welche Daten von zu Hause du schon hast. Was noch fehlt, notierst du als Hausaufgabe.</p>'
            f'<ul class="daten">{li}</ul></div></div>')

def build():
    chapters = []; checks = {}
    cur = None; num = 0; info_group = None; pending_task = None
    for i, e in enumerate(LP):
        ev = e['ev']
        if ev == 'section':
            n = e['n']
            if isinstance(n, int):
                cid, short, title = f'teil{n}', f'Teil {n}', e['t']
            elif n == 'zsmart':
                cid, short, title = 'zusatz', '★ Zusatz', 'Smart Home'
            else:
                cid, short, title = 'anhang', 'Anhang', 'Wenn dir Angaben fehlen'
            cur = {'id': cid, 'short': short, 'title': title, 'teil': n, 'slides': [], 'intro': None}
            chapters.append(cur); num = 0
            if cid == 'anhang':
                cur['slides'].append({'k': 'info', 't': 'So gehst du vor', 'h': f'<div class="eyebrow">Anhang</div><h1>Wenn dir Angaben fehlen</h1><div class="text">'})
            continue
        if ev == 'darum':
            star = ' <span class="tag star">★ freiwillig</span>' if cur['id'] == 'zusatz' else ''
            h = (f'<div class="eyebrow">{cur["short"]} · {md(cur["title"])}{star}</div><h1>Darum geht es</h1><div class="text"><p class="lead">{md(e["t"])}</p></div>')
            if isinstance(cur['teil'], int):
                h += zuhause_box(cur['teil'], True)
                if cur['teil'] == 3:
                    h += '<div class="where-box proto"><span class="ic">▤</span><div>Wärmebilder<p>Bearbeite diesen Teil zuerst. Danach planst du im Protokoll deine Aufnahmen und trägst dich in die Verleihliste für die Kamera ein.</p></div></div>'
            cur['slides'].append({'k': 'info', 't': 'Darum geht es', 'h': h}); continue
        if ev == 'vorher': continue
        if ev == 'p':
            t = e['t']
            if cur['id'] == 'anhang':
                s = cur['slides'][-1]
                if e['bold'] and not t.startswith('**'):
                    s['h'] += f'</div><h2>{md(t)}</h2><div class="text">'
                elif '1. **' in t:
                    pre, rest = t.split('1. **', 1)
                    items = re.split(r'\s\d\.\s(?=\*\*)', '**' + rest)
                    s['h'] += (f'<p>{md(pre.strip())}</p>' if pre.strip() else '') + '<ol class="bullets">' + ''.join(f'<li>{md(i)}</li>' for i in items) + '</ol>'
                else:
                    s['h'] += f'<p{" class=small" if e["italic"] else ""}>{md(t)}</p>'
                continue
            if t.startswith('Für diesen Teil brauchst du'):
                cur['slides'][-1]['h'] += f'<div class="where-box proto"><span class="ic">▤</span><div>Bevor du beginnst<p>{md(t)}</p></div></div>'
            elif t.startswith('Geschafft!'):
                cur['geschafft'] = md(t.replace('**', ''))
            continue
        if ev == 'table':
            s = cur['slides'][-1]
            th = ''.join(f'<th>{md(x)}</th>' for x in e['head'])
            tb = ''.join('<tr>' + ''.join(f'<td>{md(x)}</td>' for x in r) + '</tr>' for r in e['rows'])
            s['h'] += f'</div><div class="card tbl"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div><div class="text">'
            continue
        if ev == 'lies':
            num += 1; info_group = f'{cur["teil"] if isinstance(cur["teil"], int) else "Z"}.{num}'; continue
        if ev == 'info':
            groups = []; g = None
            for it in e['items']:
                if it[0] == 'H':
                    g = {'t': it[1], 'items': []}; groups.append(g)
                else:
                    if g is None: g = {'t': e['t'], 'items': []}; groups.append(g)
                    g['items'].append(it)
            for k, g in enumerate(groups, 1):
                body = render_items(g['items'])
                h = (f'<div class="eyebrow">{cur["short"]} · Info {k} von {len(groups)}</div><h1>{md(g["t"])}</h1>{body}')
                cur['slides'].append({'k': 'info', 'n': info_group, 't': g['t'], 'h': h})
            continue
        if ev == 'side':
            body = ''.join(f'<p>{rich(l)}</p>' for l in e['lines'])
            cur['slides'].append({'k': 'info', 't': e['t'], 'h': f'<div class="eyebrow">{cur["short"]} · Schon gewusst?</div><h1>{md(e["t"])}</h1><div class="text">{body}</div>'})
            continue
        if ev in ('task', 'tool'):
            num += 1
            tid = f'{cur["teil"] if isinstance(cur["teil"], int) else "Z"}.{num}'
            if ev == 'task':
                text = rich([[p[0]] + [fix_task_text(p[1]) if p[0] == 't' else p[1]] + p[2:] for p in e['t']])
            else:
                text = md(fix_task_text(e['t']))
            star = text.startswith('★')
            text = text.lstrip('★ ').strip()
            subs = [md(fix_task_text(s)) for s in e['sub']]
            sub_html = ''
            if subs:
                sub_html = '<ul class="bullets" style="list-style:none;padding-left:0">' + ''.join(f'<li>{s}</li>' for s in subs) + '</ul>'
            x = X.get(tid, {})
            has_check = 'check' in x
            title_txt = ('Übung: ' + e['name']) if ev == 'tool' else short_title(text)
            tags = ''
            if ev == 'tool': tags += '<span class="tag screen">● hier am Bildschirm</span> '
            tags += '<span class="tag mappe">✎ Mappe</span>'
            if star: tags += ' <span class="tag star">★ freiwillig</span>'
            h = f'<div class="eyebrow">{cur["short"]} · Aufgabe {tid} {tags}</div><h1>{md(title_txt)}</h1><p class="task-q">{text}</p>{sub_html}'
            if ev == 'tool':
                h += f'<div class="tool-frame"><iframe src="tools/{TOOLS[e["name"]]}" title="{e["name"]}" loading="lazy"></iframe></div>'
            h += CALC_MAPPE if has_check else MAPPE
            if x.get('tips'): h += tips_html(x['tips'])
            if has_check:
                c_html, cid, cdata = checker_html(tid, x['check'], x['sol'])
                h += c_html; checks[cid] = cdata
            slide = {'k': 'task', 'n': tid, 't': title_txt, 'h': h}
            if star: slide['star'] = True
            cur['slides'].append(slide); pending_task = slide
            continue
        if ev == 'grid':
            th = ''.join(f'<th>{md(x)}</th>' for x in e['head'])
            rows = ''
            for r in range(e['n']):
                pre = e['prefill'][r] if r < len(e['prefill']) else []
                rows += '<tr>' + ''.join(f'<td>{md(pre[j]) if j < len(pre) else "&nbsp;"}</td>' for j in range(len(e['head']))) + '</tr>'
            pending_task['h'] = pending_task['h'].replace(MAPPE, '').replace(CALC_MAPPE, '')
            mark = CALC_MAPPE if 'data-check' in pending_task['h'] else MAPPE
            pending_task['h'] = pending_task['h'].replace('<details class="tip">', f'<div class="card"><h2>Diese Tabelle legst du in deiner Mappe an</h2><div class="tbl"><table class="grid"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div></div>{mark}<details class="tip">', 1) if '<details class="tip">' in pending_task['h'] else pending_task['h'] + f'<div class="card"><h2>Diese Tabelle legst du in deiner Mappe an</h2><div class="tbl"><table class="grid"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div></div>{mark}'
            continue
        if ev == 'weiter':
            n = e['n']; pr = PR.get(n, {}); k = pr.get('tasks', 0)
            nxt = PR.get(n + 1, {}).get('zuhause') or []
            steps = []
            if PR.get(n, {}).get('zuhause'): steps.append('Trag die <b>Daten</b> ein, die du zu Hause erhoben hast.')
            if n == 3: steps.append('Plane deine <b>Aufnahmen</b> und trag dich in die <b>Verleihliste</b> für die Wärmebildkamera ein.')
            if k: steps.append(f'Bearbeite die Aufgaben <b>{n}.1</b> bis <b>{n}.{k}</b>.' if k > 1 else f'Bearbeite <b>Aufgabe {n}.1</b>.')
            if n != 3: steps.append('Schreib unter <b>Für dein Gutachten</b> deine Stichpunkte.')
            hw = ''
            if nxt:
                hw = ('<div class="where-box mappe"><span class="ic">⌂</span><div>Hausaufgabe für die nächste Stunde<p>Finde zu Hause heraus, was du für Teil ' + str(n + 1) + ' brauchst. Hake ab, was du schon hast:</p>'
                      '<ul class="daten">' + ''.join(f'<li>{md(z)}</li>' for z in nxt) + '</ul></div></div>')
            ges = f'<div class="merk">{cur["geschafft"]}</div>' if cur.get('geschafft') else ''
            h = (f'<div class="eyebrow">{cur["short"]} · Wechsel <span class="tag proto">▤ Protokoll</span></div><h1>Jetzt arbeitest du im Protokoll weiter</h1>{ges}'
                 f'<div class="where-box proto"><span class="ic">▤</span><div>Öffne dein Protokoll, Teil {n}<p>Dort arbeitest du mit den Zahlen deiner eigenen Wohnung oder deines Hauses.</p></div></div>'
                 f'<div class="card"><ol class="bullets">' + ''.join(f'<li>{s}</li>' for s in steps) + '</ol></div>' + hw +
                 f'<p class="small">Klicke auf „Aufgabe erledigt“, wenn du Teil {n} im Protokoll fertig hast.</p>')
            cur['slides'].append({'k': 'switch', 't': 'Jetzt ins Protokoll', 'h': h})
            continue
        raise SystemExit('unbekannt ' + ev)
    for c in chapters:
        for s in c['slides']:
            if s['k'] == 'info' and s['h'].count('<div class="text">') > s['h'].count('</div><h2>') and c['id'] == 'anhang':
                pass
        if c['id'] == 'anhang':
            c['slides'][-1]['h'] += '</div>'
            c['slides'][-1]['h'] = c['slides'][-1]['h'].replace('<div class="text"></div>', '')
    return chapters, checks

def short_title(text):
    t = re.sub('<[^>]+>', '', text)
    t = html.unescape(t)
    first = re.split(r'(?<=[.!?:])\s', t)[0]
    if len(first) > 60: first = first[:57].rsplit(' ', 1)[0] + ' …'
    return first.rstrip('.:')

def render_items(items):
    out = '<div class="text">'
    for it in items:
        k = it[0]
        if k == 'P': out += f'<p>{md(it[1])}</p>'
        elif k == 'R': out += f'<p>{rich(it[1])}</p>'
        elif k == 'IMG':
            cap = f'<figcaption>{md(it[3])}</figcaption>' if len(it) > 3 and it[3] else ''
            out += f'</div><figure class="fig"><img src="fig/{it[1]}.png" alt="{html.escape(it[3] or it[1]) if len(it) > 3 else it[1]}" loading="lazy">{cap}</figure><div class="text">'
        elif k == 'T':
            th = ''.join(f'<th>{md(x)}</th>' for x in it[1])
            tb = ''.join('<tr>' + ''.join(f'<td>{md(x)}</td>' for x in r) + '</tr>' for r in it[2])
            src = f'<p class="small">({md(it[3])})</p>' if len(it) > 3 else ''
            out += f'</div><div class="card tbl"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table>{src}</div><div class="text">'
        elif k == 'S':
            v = it[2]
            out += (f'</div><div class="card steck"><h2>Kosten und Nutzen: {md(it[1])}</h2><dl>'
                    f'<dt>Kosten (ca.)</dt><dd>{md(v[0])}</dd><dt>Einsparung</dt><dd>{md(v[1])}</dd><dt>CO₂</dt><dd>{md(v[2])}</dd><dt>Lohnt sich nach</dt><dd>{md(v[3])}</dd></dl></div><div class="text">')
        elif k == 'SRC': out += f'<p class="small">({md(it[1])})</p>'
    out += '</div>'
    return out.replace('<div class="text"></div>', '')

ch, checks = build()
js = 'const CH_MORE=' + json.dumps([{k: c[k] for k in ('id', 'short', 'title', 'slides')} for c in ch], ensure_ascii=False) + ';\nconst CHECKS_MORE=' + json.dumps(checks) + ';\n'
open(SP + 'teile.js', 'w').write(js)
for c in ch: print(c['id'], len(c['slides']), [s['t'][:25] for s in c['slides']])
