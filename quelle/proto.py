exec(open('/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/lib.py').read())
W = 16.0
NEWPAGE[0] = True
GREY = RGBColor(0x59, 0x59, 0x59)

# ------------------------------------------------------------------ Helfer
def zuhause(lines):
    box('Erhebe zu Hause, bevor du diesen Teil bearbeitest', ['• ' + l if isinstance(l, str) else ['• '] + l for l in lines], fill='E7E6E6', sz=12)

def dt(rows):
    """Daten-Tabelle: Frage | Antwort (grau) | Einheit."""
    t = d.add_table(rows=len(rows), cols=3); borders(t)
    for i, r in enumerate(rows):
        row = t.rows[i]; cant_split(row)
        cell_text(row.cells[0], r[0], size=10.5); shade(row.cells[1], ANSWER_FILL)
        u = r[1] if len(r) > 1 else ''
        if u:
            cell_text(row.cells[2], u, size=9.5)
            for run in row.cells[2].paragraphs[0].runs: run.font.color.rgb = GREY
    set_widths(t, (8.6, 5.6, 1.8))
    P('', after=2)
    return t

def rt(rows, title=None):
    """Rechentabelle: Schritt (mit Hilfe) | Rechenweg | Ergebnis | Einheit."""
    if title:
        p = P('', keep=True, before=2); add(p, title, bold=True, size=10.5)
    t = d.add_table(rows=len(rows) + 1, cols=4); borders(t)
    for j, h in enumerate(['Schritt', 'Rechenweg', 'Ergebnis', 'Einheit']):
        cell_text(t.rows[0].cells[j], h, bold=True, size=10); shade(t.rows[0].cells[j], 'D9D9D9')
    for i, r in enumerate(rows, 1):
        row = t.rows[i]; cant_split(row)
        step, hint, unit = r
        c = row.cells[0]; cell_text(c, step, bold=True, size=10)
        if hint:
            q = c.add_paragraph(); add(q, hint, italic=True, size=8.5); q.paragraph_format.space_after = Pt(1)
        shade(row.cells[1], ANSWER_FILL); shade(row.cells[2], ANSWER_FILL)
        cell_text(row.cells[3], unit, size=9.5)
        for run in row.cells[3].paragraphs[0].runs: run.font.color.rgb = GREY
    set_widths(t, (5.4, 6.0, 2.8, 1.8))
    p = P('', after=4); add(p, 'Tippen: Rechenweg in eine Zeile, z. B. 9 000 kWh * 0,06 = 540 kWh. Statt · darfst du * schreiben, statt m² auch m2. Mit der Tab-Taste springst du in die nächste Zelle.', italic=True, size=8)
    for r in p.runs: r.font.color.rgb = GREY
    return t

def wie(ref):
    p = P('', italic=True, keep=True); add(p, f'So bist du im Lernpfad vorgegangen: {ref}', italic=True, size=10)

def hinweis(text):
    last = d.paragraphs[-1]; prev = last._p.getprevious()
    if prev is not None and prev.tag == qn('w:tbl') and not ''.join(last._p.itertext()).strip():
        last.paragraph_format.keep_with_next = True
        for q in prev.iter(qn('w:p')):
            ppr = q.get_or_add_pPr()
            if ppr.find(qn('w:keepNext')) is None: ppr.append(OxmlElement('w:keepNext'))
    p = P('', keep=True); add(p, text, italic=True, size=10)

def bilder(n0, n):
    p = P('', keep=True); add(p, 'Foto einfügen: in das graue Feld klicken, dann Einfügen → Bilder.', italic=True, size=8)
    for r in p.runs: r.font.color.rgb = GREY
    for i in range(n0, n0 + n, 2):
        t = d.add_table(rows=2, cols=2); borders(t)
        for j in range(2):
            c = t.rows[0].cells[j]; shade(c, ANSWER_FILL); cell_text(c, f'Bild {i+j}', size=9)
            cell_text(t.rows[1].cells[j], f'Bild {i+j}: Was zeigt es? Wie bewertest du es?' + (' (freiwillig)' if i + j > 4 else ''), size=9); shade(t.rows[1].cells[j], ANSWER_FILL)
        row_height(t.rows[0], 4.4); row_height(t.rows[1], 1.4); cant_split(t.rows[0]); cant_split(t.rows[1])
        set_widths(t, (8.0, 8.0))
        P('', after=4)

def gutachten(prompt=None):
    sub('Für dein Gutachten')
    p = P('', keep=True); add(p, (prompt + ' ' if prompt else '') + 'Stichpunkte reichen. Ganze Sätze schreibst du erst im Gutachten (Teil 10).', italic=True, size=10)
    t = d.add_table(rows=3, cols=2); borders(t)
    for i, lab in enumerate(['Das ist gut:', 'Das ist verbesserungswürdig:', 'Mein Vorschlag (mit kWh, €, CO₂, falls berechnet):']):
        row = t.rows[i]; cant_split(row); row_height(row, 0.7)
        cell_text(row.cells[0], lab, bold=True, size=10); shade(row.cells[1], ANSWER_FILL)
    set_widths(t, (5.4, 10.6))
    _sp = P('', after=0); _sp.paragraph_format.line_spacing = Pt(4)

def eignung(what, extra=None):
    text = f'**Eignung prüfen:** Entscheide, ob {what} für eure Wohnung oder euer Haus geeignet ist. Wenn nicht, begründe genau, woran es scheitert (zum Beispiel Ausrichtung, Platz, Mietwohnung, Kosten). Auch eine gut begründete Ablehnung ist ein Ergebnis für dein Gutachten.'
    task(extra + [' ' + text] if extra else text, 0)
    datatable([('Ergebnis (geeignet / bedingt geeignet / nicht geeignet)',), ('Begründung',), ('Empfehlung für das Gutachten',)])

def sub(title):
    p = P('', just=False, before=6, after=2, keep=True)
    add(p, title, bold=True, size=13); outline(p, 1)

def weiter_lp(n):
    t = d.add_table(rows=1, cols=1); borders(t, 12, '1D5FA8'); shade(t.rows[0].cells[0], 'E3EEFB')
    c = t.rows[0].cells[0]; c.paragraphs[0].text = ''
    p0 = c.paragraphs[0]; add(p0, f'Teil {n-1} im Protokoll fertig? Speichern und weiter im Lernpfad: ', bold=True)
    xlink(p0, f'Teil {n} öffnen', f'https://hrkup.github.io/Energieprojekt/#teil{n}-1', bold=True)
    add(p0, ' (Strg + Klick). Fortschrittscode sichern (Seite 1)!', italic=True, size=9)
    p0.paragraph_format.space_after = Pt(0)
    set_widths(t, (16.0,)); cant_split(t.rows[0])
    for q in t._tbl.iter(qn('w:p')):
        ppr = q.get_or_add_pPr(); k = ppr.find(qn('w:keepNext'))
        if k is not None: ppr.remove(k)
    sp = P('', after=0); sp.paragraph_format.line_spacing = Pt(2)

_section = section
def section(num, title, anchor, newpage=True):
    if isinstance(num, int) and 2 <= num <= 9:
        weiter_lp(num)
    _section(num, title, anchor, True)
    p = P('', just=False, after=4, align=WD_ALIGN_PARAGRAPH.RIGHT, keep=True)
    ilink(p, '↑ zurück zur Übersicht', 'uebersicht')

# ------------------------------------------------------------------ Titel
p = P('', just=False, after=2); add(p, 'Protokoll und Gutachten', bold=True, size=24)
p = P('', just=False, after=10); add(p, 'Energieberatung deiner Wohnung oder deines Hauses', size=15)
dt([('Name',), ('Was untersuchst du? (Wohnung im Mehrfamilienhaus, Reihenhaus, Doppelhaushälfte, freistehendes Haus). Bitte keine Adresse angeben.',)])
t = d.add_table(rows=1, cols=2); borders(t, 12, '1D5FA8')
cell_text(t.rows[0].cells[0], 'Mein Fortschrittscode', bold=True, size=10.5)
q = t.rows[0].cells[0].add_paragraph(); add(q, 'Am Stundenende im Lernpfad auf „Fortschritt sichern“ klicken, hier hineinklicken, Strg + V. Den alten Code vorher markieren und überschreiben.', italic=True, size=8.5)
shade(t.rows[0].cells[1], ANSWER_FILL); set_widths(t, (6.0, 10.0)); cant_split(t.rows[0])
p = P('', after=6, before=4); add(p, 'Lernpfad: ', bold=True); xlink(p, 'https://hrkup.github.io/Energieprojekt/', 'https://hrkup.github.io/Energieprojekt/'); add(p, ' (in Word mit gedrückter Strg-Taste klicken)', size=10)
P('In diesem Protokoll hältst du fest, was du über deine Wohnung oder dein Haus herausfindest, und rechnest mit euren eigenen Zahlen. Wie die Rechnungen gehen, hast du im Lernpfad geübt. Jeder Teil hier gehört zum Teil mit derselben Nummer im Lernpfad.')
p = P('', keep=True, before=4); add(p, 'So ist jeder Teil aufgebaut', bold=True)
infotable(['Baustein', 'Was du dort tust'], [
 ('Erhebe zu Hause', 'Der graue Kasten sagt dir, was du zu Hause herausfinden oder messen sollst. Erledige das, bevor du den Teil im Lernpfad bearbeitest.'),
 ('Daten', 'Trage die Werte ein. Die Einheit steht schon in der rechten Spalte.'),
 ('Auswerten', 'Rechne mit euren eigenen Zahlen. Der Hinweis „So bist du im Lernpfad vorgegangen“ zeigt dir, welche Aufgabe dort genauso funktioniert hat.'),
 ('Eignung prüfen', 'Entscheide, ob eine Technik (zum Beispiel Balkonkraftwerk oder Wärmepumpe) zu eurer Wohnung oder eurem Haus passt.'),
 ('Für dein Gutachten', 'Ein kurzes Zwischenfazit in Stichpunkten: Was ist gut, was nicht, was schlägst du vor? Aus diesen Stichpunkten schreibst du am Ende dein Gutachten.'),
], widths=(3.6, 12.4))
p = P('', keep=True, before=4); add(p, 'Wenn dir Angaben fehlen', bold=True)
P('Je mehr Daten du sammelst, desto besser wird dein Gutachten. Gerade in Mietwohnungen bekommst du aber nicht alle Angaben. Dafür gibt es keinen Punktabzug. Frag zuerst deine Eltern oder schau in Rechnungen und Verträgen nach. Fehlt ein Wert trotzdem, nimm einen Richtwert aus dem Lernpfad (Anhang „Wenn dir Angaben fehlen“) und markiere ihn mit **(Ø)**. Ø bedeutet Durchschnittswert (kein Grenzwert). Selbst geschätzte Werte markierst du mit **(geschätzt)**. Kosten darfst du weglassen, wenn deine Familie sie nicht weitergeben möchte. Dann rechnest du mit den Preisen aus dem Anhang des Lernpfads.')
p = P('', keep=True, before=4); add(p, 'Speichern', bold=True)
P('Speichere die Datei in IServ unter Dateien → Eigene → „Energieprojekt“ und ersetze im Dateinamen „Mein Name“ durch deinen Vor- und Nachnamen. Speichere nach jeder Stunde.')
material('Bewertung (50 Punkte)', [
 'Strukturiertes Vorgehen (10 Punkte) · Vollständigkeit der Daten und Umgang mit fehlenden Angaben (10) · Analyse und Verbesserungen (10) · Umgang mit erhobenen Daten (10) · Organisation und Mitarbeit im Unterricht (10). Der Lernpfad wird nicht benotet. Wenn du zeigen möchtest, wie gut du im Unterricht gearbeitet hast, kannst du deine Mappe abgeben.'])

# Übersicht
p = P('', just=False, after=4, keep=True); add(p, 'Übersicht', bold=True, size=16); bookmark(p, 'uebersicht'); outline(p, 0)
p.paragraph_format.space_before = Pt(10)
P('Die Namen der Teile sind Links (in Word mit gedrückter Strg-Taste klicken).', size=10, keep=True)
toc_par = P('')

# ------------------------------------------------------------------ 1
section(1, 'Haus und Haushalt', 's1')
p = P('', keep=True, after=4); add(p, 'Zuerst im Lernpfad: ', bold=True, size=10); xlink(p, 'Teil 1 öffnen', 'https://hrkup.github.io/Energieprojekt/#teil1-1'); add(p, ' (Strg + Klick). Danach trägst du hier deine Daten ein.', size=10)
zuhause([
 'Anzahl der Personen, Wohnfläche (steht zum Beispiel im Mietvertrag), Anzahl der Zimmer und Etagen',
 'Baujahr des Hauses und letzte Renovierung (Eltern oder Vermieter fragen)',
 'Gibt es einen Energieausweis? Wenn ja: Effizienzklasse und Energiekennwert',
 'Energie für Heizung und Warmwasser pro Jahr und die Kosten dafür (Heizkostenabrechnung, Gas- oder Fernwärmerechnung). Bei Gas in m³ gilt: 1 m³ Erdgas ≈ 10 kWh.',
 'Stromverbrauch pro Jahr und Stromkosten (Stromabrechnung)'])
sub('Daten')
dt([('Anzahl der Personen im Haushalt', 'Personen'), ('Wohnfläche', 'm²'), ('Anzahl der Zimmer / Etagen (bei Wohnung: Stockwerk)', ''),
    ('Baujahr des Hauses', ''), ('Letzte Renovierung: Jahr und was wurde gemacht?', ''),
    ('Keller (ja/nein, beheizt?) und Dachboden (ja/nein, bewohnt?)', ''),
    ('Energieausweis vorhanden? Effizienzklasse', ''), ('Energiekennwert laut Energieausweis', 'kWh pro m² und Jahr')])
p = P('', keep=True, before=4); add(p, 'Eure Energie pro Jahr', bold=True)
dt([('Womit wird geheizt? (Gas, Öl, Fernwärme, Pellets, Wärmepumpe, Strom)', ''),
    ('Energie für Heizung und Warmwasser pro Jahr', 'kWh'), ('Kosten für Heizung und Warmwasser pro Jahr', '€'),
    ('Preis pro kWh Heizenergie (Kosten : kWh, sonst Richtwert aus dem Lernpfad-Anhang, z. B. Gas 0,12 €, Fernwärme 0,14 €)', '€ pro kWh'),
    ('Stromverbrauch pro Jahr', 'kWh'), ('Stromkosten pro Jahr', '€'), ('Strompreis (Kosten : kWh, sonst Richtwert 0,35 €)', '€ pro kWh')])
hinweis('Diese Werte brauchst du in fast allen Teilen. Wird das Warmwasser mit Strom erwärmt (Durchlauferhitzer), steckt es im Stromverbrauch.')
sub('Auswerten')
task('Berechne die Wohnfläche pro Person und vergleiche sie mit dem Durchschnitt in Deutschland (rund 47 m² pro Person).', 0)
rt([('Wohnfläche pro Person', 'Wohnfläche : Anzahl der Personen', 'm²'), ('Vergleich mit 47 m²', 'mehr oder weniger, um wie viel?', '')])
task('Berechne den Energiekennwert eurer Wohnung oder eures Hauses und bestimme die Effizienzklasse. Gibt es einen Energieausweis, vergleiche dein Ergebnis mit ihm.', 0)
wie('Aufgabe 1.4 (Energieausweis-Rechner). Energiekennwert = Energie für Heizung und Warmwasser : Wohnfläche.')
rt([('Energiekennwert', 'kWh für Heizung und Warmwasser pro Jahr : Wohnfläche', 'kWh pro m²'), ('Effizienzklasse', 'Skala im Lernpfad, Teil 1', ''), ('Vergleich mit dem Energieausweis', 'nur, falls vorhanden', '')])

# ------------------------------------------------------------------ 2
section(2, 'Wände und Wärme', 's2')
zuhause([
 'Baumaterial der Außenwände (zum Beispiel Ziegel, Kalksandstein, Beton, Holz) und ob sie gedämmt sind',
 'Dämmmaterial, Dicke und Alter der Dämmung (Eltern oder Vermieter fragen)',
 'Wanddicke: Miss sie mit dem Zollstock an einem geöffneten Fenster oder an der Haustür (an der Laibung, also der Innenseite der Maueröffnung).',
 'Sind die Kellerwände bzw. die Kellerdecke gedämmt?'])
sub('Daten')
dt([('Baumaterial der Außenwände', ''), ('Wanddicke', 'cm'), ('Außenwände gedämmt? (ja / nein / teilweise)', ''),
    ('Dämmmaterial', ''), ('Dicke der Dämmung', 'cm'), ('Alter der Dämmung', 'Jahre'),
    ('Keller gedämmt? (Wände, Decke)', ''), ('Fläche eurer Außenwände (schätzen: Länge · Höhe der Außenwände, ohne Fenster)', 'm²')])
sub('Auswerten')
task('Bewerte eure Außenwand: Wie gut dämmt euer Baustoff laut λ-Tabelle im Lernpfad? Bestimme mit dem Dicken-Rechner im „Dämm-Quiz“, wie dick eure Wand aus diesem Baustoff sein müsste, um so gut zu dämmen wie 10 cm Styropor.', 0)
dt([('Wie gut dämmt euer Baustoff? (λ-Wert)', 'W/(m·K)'), ('So dick müsste die Wand sein (Dicken-Rechner)', 'cm'), ('Bewertung eurer Wand', '')])
gutachten()

# ------------------------------------------------------------------ 3
section(3, 'Wärmebilder', 's3')
hinweis('Bearbeite zuerst Teil 3 im Lernpfad. Danach planst du hier deine Aufnahmen und trägst dich in die Verleihliste für die Wärmebildkamera ein.')
sub('Aufnahmen planen')
P('Wie du die Kamera bedienst und die Bilder auf den Computer überträgst, steht in der Anleitung, die bei der Kamera liegt. Nimm die Außenbilder bei kaltem Wetter auf, am besten morgens oder abends ohne Sonne auf der Fassade. Fotografiere keine Personen, keine Hausnummern und keine Namensschilder.')
tipp('Hast du Fenster oder Türen im Verdacht, undicht oder alt zu sein? Nimm sie auf jeden Fall auf, von innen, besonders Rahmen, Ecken und Dichtungen. Die Bilder brauchst du in Teil 5. Auch Geräte und Lampen lassen sich gut aufnehmen, zum Beispiel die Rückseite des Kühlschranks.')
task('Nenne sechs bis acht Motive (außen und innen), die du aufnehmen willst, und was du jeweils herausfinden möchtest.', 0)
grid(['Motiv', 'Was will ich herausfinden?'], 6, widths=(6.0, 10.0))
sub('Deine Aufnahmen')
task('Füge mindestens vier, gern bis zu acht Wärmebilder ein. Beschreibe zu jedem Bild, was es zeigt, und bewerte es: Ist dort eine Schwachstelle zu sehen?', 0)
bilder(1, 8)
gutachten('Welche Schwachstellen zeigen die Wärmebilder, was schlägst du vor? Die Bilder nutzt du im Gutachten als Beleg.')

# ------------------------------------------------------------------ 4
section(4, 'Dach und Sonnenstrom', 's4')
zuhause([
 'Dachform, Dachneigung (schätzen oder mit einer Winkelmesser-App messen) und ungefähre Dachfläche',
 'Ist das Dach bzw. die oberste Geschossdecke gedämmt? Material, Dicke, Alter',
 'Die Himmelsrichtung von Balkon, Hauswänden oder Dachflächen (Aufgabe 4.1)',
 'Gibt es schon eine Photovoltaik- oder Solarthermieanlage? Falls ja: Fläche, Leistung, Ertrag pro Jahr',
 'Bei einer Wohnung: Gibt es einen Balkon oder eine Wand, an der Solarmodule hängen könnten? Ist dort Schatten?'])
sub('Daten')
p = P('', keep=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2); p.add_run().add_picture('/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/fig/dachformen.png', width=Cm(16))
dt([('Dachform (siehe Skizzen)', ''), ('Dachneigung (darf geschätzt werden)', 'Grad'), ('Dachfläche', 'm²'),
    ('Dach oder oberste Geschossdecke gedämmt? Material, Alter', ''), ('Dicke der Dämmung', 'cm'),
    ('Dachboden bewohnt? (ja / nein / kein Dachboden)', ''), ('Vorhandene Photovoltaik- oder Solarthermieanlage', '')])
sub('Auswerten')
task('Bestimme die Himmelsrichtung von Balkon, Hauswänden oder Dachflächen. Wähle Weg A oder Weg B.', 0, sub=[
 '**Weg A, mit dem Handy:** Auf dem iPhone ist die App „Kompass“ schon installiert. Für Android empfehle ich die kostenlose App „Compass“ von Philipp Bobek (Suche: Compass Philipp Bobek). Sie hat keine Werbung und sammelt keine Daten. Den Standort darfst du verweigern. Stell dich mit dem Rücken flach an die Hauswand bzw. an das Balkongeländer und halte das Handy waagerecht vor dir. Die Oberkante zeigt von der Wand weg. Die Gradzahl ist die Richtung, in die die Wand zeigt. Halte Abstand zu Metall.',
 ['**Weg B, am Computer:** Öffne ', ('L', 'Google Maps', U['gmaps']), ', suche das Gebäude und wechsle zur Satellitenansicht. Oben ist Norden. Stell dir einen Pfeil vor, der senkrecht von der Wand oder Dachfläche weg zeigt, und schätze seine Richtung in Grad.'],
 'Rechne die Gradzahl dann mit dem „Balkonkraftwerk-Planer“ in Himmelsrichtung und Azimut für PVGIS um.',
 '**Neigung:** Auf einem Schrägdach liegen die Module so schräg wie das Dach. Am Balkongeländer hängen sie meist senkrecht (90°), auf einem Flachdach werden sie aufgeständert (etwa 15 bis 30°).'])
grid(['Ort (z. B. Balkon, Dach Süd)', 'Kompass (°)', 'Himmels-richtung', 'Azimut für PVGIS (°)', 'Neigung der Module / des Daches (°)', 'Schatten? (wann, wodurch)'],
     3, widths=(3.4, 1.9, 2.3, 2.3, 2.8, 3.3))
task(['Bestimme für den besten Ort den Jahresertrag eines Balkonkraftwerks (0,8 kWp, 450 €) mit ', ('L', 'PVGIS', U['pvgis']), ' und rechne aus, ob es sich lohnt.'], 0)
wie('Aufgabe 4.4 und 4.5 (Balkonkraftwerk-Planer und PVGIS am Beispielbalkon).')
_t = rt([('Jahresertrag laut PVGIS', 'ablesen', 'kWh'),
    ('eingesparte Kosten pro Jahr', 'die Hälfte des Ertrags* · Strompreis (Teil 1, sonst 0,35 €)', '€'),
    ('Amortisation', '450 € : eingesparte Kosten pro Jahr', 'Jahre')])
for c in _t.rows[-1].cells:
    for q in c.paragraphs: q.paragraph_format.keep_with_next = True
d.paragraphs[-1].paragraph_format.keep_with_next = True
hinweis('* Geld sparst du nur mit dem Strom, den ihr selbst verbraucht. Mittags erzeugt die Anlage oft mehr, als ihr gerade braucht. Dieser Rest fließt ins Netz und wird beim Balkonkraftwerk nicht bezahlt. Deshalb rechnet man mit etwa der Hälfte.')
eignung('ein Balkonkraftwerk oder eine Photovoltaikanlage')
gutachten()

# ------------------------------------------------------------------ 5
section(5, 'Fenster und Türen', 's5')
zuhause([
 'Anzahl der Fenster, ungefähre Größe und Himmelsrichtung, Alter und Rahmenmaterial',
 '**Feuerzeugtest:** Halte eine Feuerzeugflamme vor die Scheibe. Jede Glasscheibe spiegelt die Flamme einmal, so zählst du die Scheiben. Hat ein Spiegelbild eine andere Farbe, hat das Glas eine Wärmeschutzschicht. Bitte nur mit Erlaubnis deiner Eltern und nicht in der Nähe von Vorhängen.',
 '**Papiertest:** Klemm ein Blatt Papier ins Fenster und schließ es. Lässt sich das Blatt leicht herausziehen, ist die Dichtung undicht.',
 'Rollläden vorhanden? Haustür: Material, schließt sie dicht?'])
sub('Daten')
grid(['Raum / Lage', 'Anzahl', 'Größe je Fenster (m²)', 'Himmels-richtung', 'Scheiben (1/2/3), Schutzschicht?', 'dicht? (Papier-test)', 'Rahmen', 'Alter'], 4,
     widths=(2.6, 1.4, 1.9, 2.0, 2.6, 1.9, 1.9, 1.7))
dt([('Anzahl der Fenster insgesamt', ''), ('Rollläden vorhanden? (wo?)', ''), ('Haustür: Material, schließt sie dicht?', '')])
sub('Auswerten')
task('Bewerte eure Fenster und Türen mit den Ergebnissen aus Feuerzeug- und Papiertest. Welches Fenster ist das schlechteste? Woran erkennst du das? Hast du von diesem Fenster ein Wärmebild (Teil 3)? Nutze es als Beleg.', 1.2)
gutachten('Denk auch an günstige Maßnahmen, zum Beispiel neue Dichtungen, Rollläden nachts schließen oder Vorhänge nicht vor die Heizkörper hängen.')

# ------------------------------------------------------------------ 6
section(6, 'Heizung und Warmwasser', 's6')
zuhause([
 'Art und Alter der Heizung (Typenschild am Heizkessel bzw. an der Fernwärmestation oder Eltern fragen), Anzahl der Heizkörper, Fußbodenheizung',
 'Raumtemperaturen in Wohnzimmer, Küche und Schlafzimmer messen. Wie wird im Winter gelüftet?',
 'Warmwasser: Wie wird es erwärmt (über die Heizung, Durchlauferhitzer, Boiler)? Sind die Rohre gedämmt?',
 '**Deine Dusche:** Stopp die Dauer einer typischen Dusche. **Eimer-Methode:** Halte einen Eimer 10 Sekunden unter die voll aufgedrehte Dusche, miss die Liter (Messbecher) und nimm sie mal 6. Das ergibt die Liter pro Minute. Kein Messbecher zu Hause? Leih dir einen bei Herrn Kuprat.'])
sub('Daten')
dt([('Art der Heizung', ''), ('Alter der Heizung', 'Jahre'), ('Heizkörper (Anzahl) / Fußbodenheizung (wo?)', ''),
    ('Thermostate (normal / programmierbar / smart)', ''), ('So wird im Winter gelüftet', ''),
    ('Warmwasser erwärmt durch', ''), ('Warmwasserrohre gedämmt? (ja / nein / weiß nicht)', ''),
    ('Wasser pro Minute beim Duschen (Eimer-Methode)', 'Liter'), ('Dauer deiner Dusche', 'Minuten'), ('Deine Duschen pro Woche', '')])
sub('Auswerten')
task(['Ordne euren Heizenergieverbrauch im ', ('L', 'HeizCheck (co2online)', U['co2o_heizcheck']), ' ein. Notiere die Einstufung und mögliche Gründe dafür.'], 1.4)
task('Vergleiche eure Raumtemperaturen mit den Empfehlungen des Umweltbundesamts (Aufgabe 6.6 im Lernpfad).', 0)
grid(['Raum', 'gemessen (°C)', 'empfohlen (°C)', 'Bewertung'], 3, widths=(3.5, 3.0, 3.0, 6.5), fill_cols=[1, 2, 3], prefill=[('Wohnzimmer',), ('Küche',), ('Schlafzimmer',)])
task('Und du? Rechne mit deinen eigenen Duschwerten. Wird das Wasser mit Gas erwärmt, rechne mit 0,12 € und 0,24 kg CO₂ pro kWh (andere Werte: Anhang im Lernpfad). Mit Strom (Durchlauferhitzer) nimmst du 0,35 € und 0,34 kg CO₂ pro kWh.', 0, sub=[
 'a) Fülle die Tabelle aus: deine Dusche heute und mit Sparduschkopf (7 Liter pro Minute) und so viel kürzer, wie du für dich vertretbar hältst. Trage deine neue Duschzeit in die Tabelle ein.'])
wie('Aufgabe 6.7, die Warmduscher-Rechnung. Energie (Wh) = Liter · Temperaturunterschied (30 °C) · 1,16 Wh pro Liter und °C.')
grid(['', 'heute', 'mit Sparduschkopf und kürzer'], 7, widths=(6.0, 5.0, 5.0), fill_cols=[1, 2],
     prefill=[('Duschdauer (min)',), ('Liter pro Dusche',), ('Duschen pro Jahr (pro Woche · 52)',), ('Liter pro Jahr',), ('Energie pro Jahr (kWh)',), ('Kosten pro Jahr (€)',), ('CO₂ pro Jahr (kg)',)])
p = P('', keep=True, before=4); p.paragraph_format.left_indent = Cm(0.5); add(p, 'b) Berechne, wie viel du im Jahr sparst (kWh, €, kg CO₂).')
answer(1.0)
p = P('', keep=True, before=4); p.paragraph_format.left_indent = Cm(0.5); add(p, 'c) Mach deinen Eltern einen Vorschlag, wofür ihr das gesparte Geld ausgebt. Eine Belohnung ist erlaubt.')
answer(1.0)
eignung('eine Wärmepumpe (Luft oder Erdwärme)', ['**Haus:** Mach den ', ('L', 'Gebäudecheck Wärmepumpe (Umweltbundesamt)', U['uba_wpcheck']), ' und notiere das Ergebnis. **Wohnung im Mehrfamilienhaus:** Prüfe mit dem Info-Kasten in Teil 6 des Lernpfads (Fußbodenheizung oder große Heizkörper, Platz für das Außengerät) und überlege, wer darüber entscheidet (Vermieter, Eigentümergemeinschaft).'])
eignung('eine Solarthermieanlage')
gutachten()

# ------------------------------------------------------------------ 7
section(7, 'Strom und Geräte', 's7')
zuhause([
 'Leistung der wichtigsten Geräte in Watt (Typenschild, meist hinten oder unten am Gerät) und ihre ungefähre Betriebszeit',
 'Effizienzklasse von Kühlschrank, Waschmaschine und Geschirrspüler, Alter des Kühlschranks',
 'Alle Geräte im Stand-by (Lämpchen, Display, Fernbedienung)'])
sub('Daten')
P('Euren Stromverbrauch hast du schon in Teil 1 eingetragen. Trage hier die Geräte ein. Energie pro Jahr (kWh) = Leistung (W) · Betriebsstunden pro Jahr : 1 000.', keep=True)
grid(['Gerät', 'Anzahl', 'Alter (Jahre)', 'Effizienz-klasse', 'Leistung (W)', 'Betriebs-stunden pro Jahr', 'Energie pro Jahr (kWh)'], 8,
     widths=(3.6, 1.4, 1.8, 1.8, 2.0, 2.5, 2.9), fill_cols=[1, 2, 3, 4, 5, 6],
     prefill=[('Kühlschrank',), ('Gefriergerät',), ('Herd / Backofen',), ('Waschmaschine',), ('Geschirrspüler',),
              ('Wäschetrockner',), ('Fernseher',), ('Computer / Spielkonsole',)])
sub('Auswerten')
task(['Ordne euren Stromverbrauch aus Teil 1 im ', ('L', 'StromCheck (Stromspiegel)', U['stromcheck']), ' ein. Notiere die Einstufung und welche Geräte vermutlich am meisten verbrauchen.'], 1.4)
task('Berechne euren Stand-by-Verbrauch pro Jahr in kWh und € (Strompreis aus Teil 1, sonst 0,35 €). Ohne Angabe auf dem Typenschild rechnest du mit 1 bis 3 W pro Gerät, bei älteren Geräten bis 10 W.', 0)
wie('Aufgabe 7.2 (Föhn oder Router?).')
grid(['Gerät im Stand-by', 'Stand-by-Leistung (W)', 'Stunden pro Tag im Stand-by', 'Energie pro Jahr (kWh)'], 4, widths=(5.4, 3.4, 3.6, 3.6))
answer(0.8)
gutachten()

# ------------------------------------------------------------------ 8
section(8, 'Beleuchtung', 's8')
zuhause([
 'Anzahl der Lampen nach Typ (Glühlampe, Halogenlampe, Energiesparlampe, LED). Auf der Lampe oder der Verpackung stehen Watt und Lumen.',
 'Wie viele Stunden pro Tag brennen die Lampen in den meistgenutzten Räumen ungefähr?'])
box('⚠ Sicherheit: Schraube keine Lampe heraus!', ['In der Fassung liegt Strom an, solange die Sicherung eingeschaltet ist, auch wenn der Lichtschalter aus ist. Eine eingeschaltete Lampe kann sehr heiß werden. Lies nur ab, was du siehst, ohne die Lampe anzufassen, schau auf Verpackungen nach oder frag deine Eltern. Erkennst du eine Lampe nicht, schreib „unbekannt“.'], fill='FFFFFF', sz=18)
sub('Daten')
grid(['Lampentyp', 'Anzahl', 'Leistung je Lampe (W)', 'Brennstunden pro Tag (ca.)', 'Energie pro Jahr (kWh)'], 4, widths=(3.8, 2.0, 3.2, 3.6, 3.4), fill_cols=[1, 2, 3, 4],
     prefill=[('Glühlampen',), ('Halogenlampen',), ('Energiesparlampen',), ('LED-Lampen',)])
hinweis('Energie pro Jahr (kWh) = Anzahl · Leistung (W) · Stunden pro Tag · 365 : 1 000')
sub('Auswerten')
task('Rechne aus, was es bringt, alle Glüh- und Halogenlampen durch LEDs zu ersetzen. Eine LED braucht für dieselbe Helligkeit nur etwa ein Achtel der Leistung und kostet etwa 5 €. Gibt es bei euch keine Glüh- oder Halogenlampen mehr, schreib „entfällt“ und bewerte das.', 0)
wie('Aufgabe 8.2 (Glühlampe gegen LED).')
rt([('Energie mit LEDs', 'kWh von Glüh- und Halogenlampen : 8', 'kWh'),
    ('eingesparte Energie pro Jahr', 'kWh heute − kWh mit LEDs', 'kWh'),
    ('eingesparte Kosten pro Jahr', 'kWh · Strompreis (Teil 1, sonst 0,35 €)', '€'),
    ('Kosten', 'Anzahl der Lampen · 5 €', '€'),
    ('Amortisation', 'Kosten : eingesparte Kosten pro Jahr', 'Jahre')])
gutachten()

# ------------------------------------------------------------------ 9
section(9, 'CO₂-Bilanz', 's9')
hinweis('Für diesen Teil brauchst du keine neuen Daten von zu Hause. Du nutzt eure Zahlen aus Teil 1 und deine Rechnungen aus den Teilen 2 bis 8.')
sub('Auswerten')
task('Öffne den CO₂-Regler im Lernpfad (Teil 9, Aufgabe 9.3). Stelle euren Haushalt ein: Personen, Wohnfläche, Heizung, Dämmung, Raumtemperatur, deine Duschzeit. Den Rest (Auto, Flüge, Ernährung) darfst du schätzen. Notiere den Fußabdruck pro Person und vergleiche ihn mit dem Durchschnitt in Deutschland (10 t) und dem Ziel (1 t). Welcher Bereich ist bei euch am größten?', 0)
dt([('Fußabdruck pro Person laut CO₂-Regler', 't CO₂'), ('Davon Heizen, Warmwasser und Strom', 't CO₂'), ('Größter Bereich bei euch', ''), ('Vergleich mit 10 t und 1 t', '')])
task('Trage deine Maßnahmen aus den Teilen 2 bis 8 ein und ordne sie: Was spart am meisten CO₂, was lohnt sich am schnellsten? Diese Tabelle ist die Grundlage für dein Gutachten.', 0)
grid(['Maßnahme', 'Kosten (€)', 'Ersparnis pro Jahr (€)', 'CO₂-Ersparnis pro Jahr (kg)', 'Amortisation (Jahre)', 'Rang'], 7, widths=(5.0, 2.0, 2.4, 2.6, 2.4, 1.6))
gutachten('Beurteile die CO₂-Bilanz eures Haushalts. Welche Maßnahmen sparen am meisten CO₂, welche am meisten Geld? Gibt es Maßnahmen, die nur der Vermieter oder die Politik umsetzen kann?')

# ------------------------------------------------------------------ 10
section(10, 'Gutachten', 's10')
P('Im Gutachten fasst du als Energieberaterin oder Energieberater deine Ergebnisse für die Bewohnerinnen und Bewohner zusammen. Es soll 1 bis 2 Seiten lang sein (Schriftgröße 12) und in ganzen Sätzen geschrieben werden. Grundlage sind deine Stichpunkte „Für dein Gutachten“ und die Tabelle aus Aufgabe 9.2.')
material('So baust du dein Gutachten auf', [
 '**1. Die Wohnung oder das Haus:** kurze Beschreibung (Haustyp, Baujahr, Wohnfläche, Personen, Heizung, Effizienzklasse).',
 '**2. Bewertung:** Geh die Bereiche Wände, Dach, Fenster und Türen, Heizung und Warmwasser, Strom und Beleuchtung durch. Vergleiche jeweils mit einem Maßstab (Effizienzklasse, HeizCheck, StromCheck, Empfehlungen des Umweltbundesamts) und nutze deine Wärmebilder als Beleg.',
 '**3. Verbesserungsvorschläge:** Nenne die wichtigsten Maßnahmen, begründe sie fachlich und gib an, was sie kosten und einsparen (kWh, €, kg CO₂). Ordne sie: Was lohnt sich sofort und günstig, was ist eine größere Investition? Bei Technik, die nicht geeignet ist, erklärst du, warum.',
 '**4. Fehlende Daten:** Welche Angaben fehlen? Was hast du versucht, um sie zu bekommen, bzw. warum ging es nicht? Wo hast du Richtwerte (Ø) verwendet?',
 '**5. Fazit:** Gesamturteil in wenigen Sätzen.'])
p = P('', keep=True); add(p, 'Dein Gutachten', bold=True, size=13)
answer(12)

# ------------------------------------------------------------------ 11
section(11, 'Anhang und Quellen', 's11')
P('Füge hier weitere Unterlagen ein, zum Beispiel Fotos oder Auszüge aus Rechnungen. Schwärze vorher persönliche Daten wie Namen, Adresse und Kundennummern.')
answer(4)
p = P('', keep=True); add(p, 'Quellen', bold=True, size=13)
P('Liste die Internetseiten auf, die du genutzt hast (Titel und Adresse).')
answer(3)

t = d.add_table(rows=len(SECTIONS), cols=2); borders(t, 4, 'BFBFBF')
for i, (num, title, anc) in enumerate(SECTIONS):
    cell_text(t.rows[i].cells[0], str(num), bold=True)
    c = t.rows[i].cells[1]; c.paragraphs[0].text = ''
    ilink(c.paragraphs[0], title, anc, bold=True)
set_widths(t, (1.2, 14.8))
toc_par._p.addnext(t._tbl); toc_par._p.getparent().remove(toc_par._p)
exec(open('/tmp/claude-0/-home-user/4ea94787-b298-5048-82ac-b19bdfe2c68e/scratchpad/schemafix.py').read())
def _fld(run, code):
    for typ, txt in (('begin', None), (None, code), ('separate', None), (None, '1'), ('end', None)):
        if typ:
            e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), typ); run._r.append(e)
        elif txt == code:
            e = OxmlElement('w:instrText'); e.set(qn('xml:space'), 'preserve'); e.text = ' ' + code + ' '; run._r.append(e)
        else:
            e = OxmlElement('w:t'); e.text = txt; run._r.append(e)
for sec in d.sections:
    for ft in [sec.footer] + ([sec.first_page_footer] if sec.different_first_page_header_footer else []):
        ft.is_linked_to_previous = False
        fp = ft.paragraphs[0]; fp.text = ''; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for code, pre in (('PAGE', 'Seite '), ('NUMPAGES', ' von ')):
            r = fp.add_run(pre); r.font.size = Pt(9); r.font.color.rgb = GREY
            r = fp.add_run(); r.font.size = Pt(9); r.font.color.rgb = GREY; _fld(r, code)
keep_tables(); print('schema', fix_schema(d.element)); d.save(OUT); print('ok', len(SECTIONS))
