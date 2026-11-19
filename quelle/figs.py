import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch, Circle, FancyBboxPatch, Wedge, Ellipse
import numpy as np, os

plt.rcParams['font.family'] = 'Carlito'
plt.rcParams['font.size'] = 12
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig')
os.makedirs(OUT, exist_ok=True)
HOT = '#D9480F'; WARM = '#F08C00'; COLD = '#1C7ED6'; GREEN = '#0E7A63'; INK = '#17302B'; GREY = '#868E96'; LIGHT = '#F1F3F5'
ELEC = '#F2C200'; ENV = '#40C057'

def save(fig, name):
    fig.savefig(os.path.join(OUT, name + '.png'), dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def arrow(ax, xy1, xy2, color=INK, lw=2, ms=18, style='-|>', **kw):
    ax.add_patch(FancyArrowPatch(xy1, xy2, arrowstyle=style, mutation_scale=ms, color=color, lw=lw, **kw))

# 1 Wärmeverluste Beispielhaus -------------------------------------------------
def haus():
    fig, ax = plt.subplots(figsize=(8, 4.6)); ax.set_xlim(0, 16); ax.set_ylim(0, 9.2); ax.axis('off')
    ax.add_patch(Rectangle((4, 1), 8, 4.5, fc='#FFF4E6', ec=INK, lw=2.5))
    ax.add_patch(Polygon([(3.4, 5.5), (8, 8.6), (12.6, 5.5)], fc='#FFE8CC', ec=INK, lw=2.5))
    for x in (5.0, 9.6):
        ax.add_patch(Rectangle((x, 3.3), 1.4, 1.3, fc='#D0EBFF', ec=INK, lw=1.5))
    ax.add_patch(Rectangle((7.4, 1), 1.2, 2.2, fc='#E9ECEF', ec=INK, lw=1.5))
    ax.add_patch(Rectangle((4, 0.3), 8, 0.7, fc='#DEE2E6', ec=INK, lw=1.5, hatch='//'))
    def lab(xy, xyt, txt, ha='left'):
        arrow(ax, xy, xyt, color=HOT, lw=3, ms=22)
        ax.text(xyt[0] + (0.15 if ha == 'left' else -0.15), xyt[1], txt, ha=ha, va='center', fontsize=13, color=INK, fontweight='bold')
    lab((11.5, 7.0), (13.4, 8.0), 'Dach  25 %')
    lab((12.0, 2.4), (13.6, 2.4), 'Außenwände  30 %')
    lab((10.9, 4.0), (13.6, 4.4), 'Fenster  25 %')
    lab((4.4, 7.0), (2.6, 8.0), 'Lüftung, Ritzen  10 %', ha='right')
    lab((5, 0.65), (2.6, 0.65), 'Boden, Keller  10 %', ha='right')
    ax.text(8, 4.9, 'Beispielhaus\nunsaniert', ha='center', va='center', fontsize=12, color=GREY)
    ax.text(8, -0.25, 'Zusammen 100 % der Wärme, die das Haus verliert. Die Anteile schwanken von Haus zu Haus.', ha='center', fontsize=10.5, color=GREY)
    save(fig, 'haus')

# 2 Drei Wege Wärmetransport -------------------------------------------------
def transport():
    fig, axs = plt.subplots(1, 3, figsize=(9, 3.0))
    for ax, t in zip(axs, ['Wärmeleitung', 'Wärmeströmung', 'Wärmestrahlung']):
        ax.set_xlim(0, 4); ax.set_ylim(0, 3.3); ax.axis('off'); ax.set_title(t, fontsize=14, fontweight='bold', color=INK)
    a = axs[0]
    for i, c in enumerate(['#C92A2A', '#E8590C', '#F08C00', '#FAB005', '#74C0FC', '#1C7ED6']):
        a.add_patch(Rectangle((0.3 + i * 0.57, 0.9), 0.57, 1.5, fc=c, ec='white'))
    arrow(a, (0.5, 0.5), (3.5, 0.5), color=HOT, lw=2.5)
    a.text(0.3, 2.65, 'warm', color='#C92A2A', fontsize=11); a.text(3.1, 2.65, 'kalt', color=COLD, fontsize=11)
    a.text(2, 0.05, 'durch einen Stoff hindurch', ha='center', fontsize=10, color=GREY)
    b = axs[1]
    b.add_patch(Rectangle((0.4, 0.4), 0.5, 1.4, fc='#ADB5BD', ec=INK)); 
    th = np.linspace(0, 2 * np.pi, 200)
    b.plot(2 + 1.2 * np.cos(th), 1.7 + 1.1 * np.sin(th), color='white')
    arrow(b, (0.8, 1.9), (0.9, 2.9), color=HOT, lw=2.5); arrow(b, (1.1, 3.0), (3.0, 3.0), color=WARM, lw=2.5)
    arrow(b, (3.3, 2.8), (3.3, 0.8), color=COLD, lw=2.5); arrow(b, (3.0, 0.5), (1.2, 0.5), color=COLD, lw=2.5)
    b.text(2, 0.05, 'warme Luft steigt, kalte sinkt', ha='center', fontsize=10, color=GREY)
    c = axs[2]
    c.add_patch(Circle((0.9, 1.7), 0.55, fc='#FA5252', ec=INK))
    for ang in np.linspace(-0.45, 0.45, 4):
        x0, y0 = 0.9 + 0.65 * np.cos(ang), 1.75 + 0.65 * np.sin(ang)
        xs = np.linspace(0, 1.8, 80); ys = 0.08 * np.sin(xs * 14)
        X = x0 + xs * np.cos(ang) - ys * np.sin(ang); Y = y0 + xs * np.sin(ang) + ys * np.cos(ang)
        c.plot(X, Y, color=HOT, lw=1.6)
    c.text(2, 0.05, 'unsichtbares Infrarot, auch ohne Luft', ha='center', fontsize=10, color=GREY)
    save(fig, 'transport')

# 3 Dach -------------------------------------------------------------------------
def dach():
    fig, ax = plt.subplots(figsize=(9, 4.4)); ax.set_xlim(0, 18); ax.set_ylim(0, 8.8); ax.axis('off')
    # Dachschräge schematisch: drei Ausschnitte
    def schnitt(x0, title, mode):
        ax.text(x0 + 2.2, 8.4, title, ha='center', fontsize=13, fontweight='bold', color=INK)
        ang = np.radians(35); L = 5.2
        def P(s, t):  # s entlang Dach, t senkrecht nach außen
            return (x0 + s * np.cos(ang) - t * np.sin(ang), 3.2 + s * np.sin(ang) + t * np.cos(ang))
        def band(t0, t1, fc, ec='none', hatch=None, lw=0):
            ax.add_patch(Polygon([P(0, t0), P(L, t0), P(L, t1), P(0, t1)], fc=fc, ec=ec, hatch=hatch, lw=lw))
        if mode == 'auf':
            band(0, 0.35, '#C8A27A'); band(0.35, 1.05, '#FFD43B'); band(1.05, 1.25, '#868E96')
            for s in np.arange(0.4, L, 1.6):
                ax.add_patch(Polygon([P(s, -0.9), P(s + 0.35, -0.9), P(s + 0.35, 0), P(s, 0)], fc='#8B5E34', ec=INK, lw=0.8))
        elif mode == 'zwischen':
            band(-0.9, 0, '#FFD43B'); band(0, 0.2, '#868E96'); band(-1.05, -0.9, '#CED4DA')
            for s in np.arange(0.4, L, 1.6):
                ax.add_patch(Polygon([P(s, -0.9), P(s + 0.35, -0.9), P(s + 0.35, 0), P(s, 0)], fc='#8B5E34', ec=INK, lw=0.8))
        else:
            band(-0.9, 0, '#FFD43B'); band(-1.5, -0.9, '#FFE066'); band(0, 0.2, '#868E96')
            for s in np.arange(0.4, L, 1.6):
                ax.add_patch(Polygon([P(s, -0.9), P(s + 0.35, -0.9), P(s + 0.35, 0), P(s, 0)], fc='#8B5E34', ec=INK, lw=0.8))
        ax.text(*P(L + 0.2, 0.6), 'außen', fontsize=9.5, color=COLD)
        ax.text(*P(L * 0.55, -2.4), 'innen', fontsize=9.5, color=HOT)
    schnitt(0.4, 'Zwischensparren', 'zwischen')
    schnitt(6.4, 'Aufsparren', 'auf')
    schnitt(12.4, 'Zwischen- + Untersparren', 'unter')
    # Legende
    items = [('#8B5E34', 'Sparren (tragende Holzbalken)'), ('#FFD43B', 'Dämmstoff'), ('#FFE066', 'zusätzliche Dämmschicht innen'), ('#868E96', 'Dachziegel / Eindeckung')]
    for i, (c, t) in enumerate(items):
        ax.add_patch(Rectangle((0.6 + (i % 2) * 8.5, 1.3 - (i // 2) * 0.8), 0.5, 0.45, fc=c, ec=INK, lw=0.6))
        ax.text(1.3 + (i % 2) * 8.5, 1.52 - (i // 2) * 0.8, t, va='center', fontsize=11)
    save(fig, 'dach')

def geschossdecke():
    fig, ax = plt.subplots(figsize=(7.4, 3.4)); ax.set_xlim(0, 14); ax.set_ylim(0, 6.6); ax.axis('off')
    ax.add_patch(Polygon([(0.5, 3.4), (6, 6.4), (11.5, 3.4)], fc='#F1F3F5', ec=INK, lw=2))
    ax.add_patch(Rectangle((1.2, 3.1), 9.6, 0.35, fc='#FFD43B', ec=INK, lw=1))
    ax.add_patch(Rectangle((1.2, 2.85), 9.6, 0.25, fc='#ADB5BD', ec=INK, lw=1))
    ax.add_patch(Rectangle((1.2, 0.4), 9.6, 2.45, fc='#FFF4E6', ec=INK, lw=2))
    ax.text(6, 4.35, 'Dachboden: ungeheizt, kalt', ha='center', fontsize=11.5, color=COLD)
    ax.text(6, 1.5, 'Wohnung: geheizt', ha='center', fontsize=11.5, color=HOT)
    ax.annotate('Dämmung auf der obersten\nGeschossdecke', xy=(10.3, 3.3), xytext=(10.6, 5.6), fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='-|>', color=INK, lw=1.5), ha='center')
    save(fig, 'geschossdecke')

# 4 Windrose ---------------------------------------------------------------------
def windrose():
    fig, ax = plt.subplots(figsize=(6.8, 7.6)); ax.set_xlim(-1.55, 1.55); ax.set_ylim(-1.6, 1.95); ax.set_aspect('equal'); ax.axis('off')
    ax.add_patch(Circle((0, 0), 1.38, fc='#E7F5FF', ec=COLD, lw=2.5))
    ax.add_patch(Circle((0, 0), 0.98, fc='#FFF4E6', ec=WARM, lw=2.5))
    ax.add_patch(Circle((0, 0), 0.55, fc='white', ec=GREY, lw=1))
    names = ['N', 'NO', 'O', 'SO', 'S', 'SW', 'W', 'NW']
    for i, n in enumerate(names):
        k = i * 45; a = np.radians(90 - k)
        ax.plot([0.55 * np.cos(a), 1.38 * np.cos(a)], [0.55 * np.sin(a), 1.38 * np.sin(a)], color='#CED4DA', lw=1)
        ax.text(0.4 * np.cos(a), 0.4 * np.sin(a), n, ha='center', va='center', fontsize=21 if len(n) == 1 else 17, fontweight='bold', color=INK)
        ax.text(1.18 * np.cos(a), 1.18 * np.sin(a), f'{k}°', ha='center', va='center', fontsize=17, color=COLD, fontweight='bold')
        az = k - 180 if k > 0 else 180
        s = ('+' if 0 < az < 180 else '') + f'{az}°' if az not in (180,) else '±180°'
        if k == 180: s = '0°'
        ax.text(0.765 * np.cos(a), 0.765 * np.sin(a), s, ha='center', va='center', fontsize=16, color='#D9480F', fontweight='bold')
    # Süd-Hervorhebung
    a = np.radians(-90)
    ax.add_patch(Wedge((0, 0), 1.38, 270 - 45, 270 + 45, width=0.83, fc='#FFE066', alpha=0.25, ec='none'))
    ax.text(0, -1.52, 'günstig für Solarmodule: Südost bis Südwest', ha='center', fontsize=15, color=INK)
    ax.text(-1.55, 1.93, 'außen (blau): Kompass\nzählt ab Norden\nim Uhrzeigersinn', fontsize=14.5, color=COLD, va='top')
    ax.text(1.55, 1.93, 'innen (orange): PVGIS-Azimut\nzählt ab Süden,\nWest +, Ost −', fontsize=14.5, color='#D9480F', va='top', ha='right')
    save(fig, 'windrose')

# 5 Fensterrechnung annotiert ----------------------------------------------------
def fenster():
    fig, ax = plt.subplots(figsize=(9.5, 6.2)); ax.set_xlim(0, 19); ax.set_ylim(0, 12.4); ax.axis('off')
    def zeile(y, parts, notes):
        cx = {}
        for i, (x, t, c) in enumerate(parts):
            ax.text(x, y, t, fontsize=21, color=c, fontweight='bold' if c != INK else 'normal', va='center', ha='center')
            cx[i] = (x, c)
        for i, txt, up in notes:
            x, c = cx[i]
            if up:
                arrow(ax, (x, y + 1.25), (x, y + 0.55), color=c, lw=1.6, ms=14)
                ax.text(x, y + 1.35, txt, ha='center', va='bottom', fontsize=11, color=c)
            else:
                arrow(ax, (x, y - 1.25), (x, y - 0.55), color=c, lw=1.6, ms=14)
                ax.text(x, y - 1.35, txt, ha='center', va='top', fontsize=11, color=c)
    zeile(9.0, [(1.4, '5,8', '#C92A2A'), (3.0, '·', INK), (4.6, '2', COLD), (6.2, '·', INK), (7.8, '12', '#2B8A3E'), (9.4, '=', INK), (11.4, '139 W', HOT)],
          [(0, 'U-Wert von\nEinfachglas', True), (2, 'Fläche:\n2 m²', True), (4, 'Temperatur-\nunterschied: 12 K', True), (6, 'Wärmeverlust-Leistung:\nso viel Wärme fließt in\njedem Moment ab', False)])
    zeile(3.6, [(1.8, '139 W', HOT), (3.6, '·', INK), (5.6, '5 000 h', '#7048E8'), (7.6, '=', INK), (10.4, '695 000 Wh', GREEN), (13.2, '=', INK), (15.4, '695 kWh', GREEN)],
          [(0, 'Leistung', True), (2, 'Heizzeit\nim Winter', True), (6, 'Energie: so viel Wärme geht\nim ganzen Winter verloren', False)])
    ax.text(0.3, 0.2, '695 kWh · 0,12 € pro kWh ≈ 83 € Heizkosten pro Jahr, nur für dieses eine Fenster', fontsize=13, color=INK)
    save(fig, 'fenster')

# 6 Wärmepumpe ------------------------------------------------------------------
def wp():
    fig, ax = plt.subplots(figsize=(9.5, 5.4)); ax.set_xlim(0, 19); ax.set_ylim(0, 10.8); ax.axis('off')
    ax.add_patch(Rectangle((9.5, 0.2), 9.3, 9.6, fc='#FFF4E6', ec='none')); ax.add_patch(Rectangle((0.2, 0.2), 9.3, 9.6, fc='#E7F5FF', ec='none'))
    ax.text(0.5, 9.3, 'außen: Luft, Erdreich oder Grundwasser', fontsize=11.5, color=COLD, fontweight='bold')
    ax.text(18.5, 9.3, 'innen: Heizung', fontsize=11.5, color=HOT, fontweight='bold', ha='right')
    def comp(x, y, w, h, t, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.12', fc=fc, ec=INK, lw=1.6))
        ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=11.5, fontweight='bold')
    comp(3.2, 4.2, 3.0, 1.8, '1 Verdampfer', '#A5D8FF')
    comp(7.9, 6.9, 3.2, 1.5, '2 Verdichter', '#FFE066')
    comp(12.8, 4.2, 3.0, 1.8, '3 Verflüssiger', '#FFA8A8')
    comp(7.9, 1.6, 3.2, 1.5, '4 Ventil', '#D0BFFF')
    arrow(ax, (5.3, 6.15), (7.8, 7.5), color=COLD, lw=3); arrow(ax, (11.2, 7.5), (13.7, 6.15), color=HOT, lw=3)
    arrow(ax, (13.7, 4.05), (11.2, 2.4), color=WARM, lw=3); arrow(ax, (7.8, 2.4), (5.3, 4.05), color=COLD, lw=3)
    arrow(ax, (0.6, 5.1), (3.0, 5.1), color=ENV, lw=4, ms=24); ax.text(0.5, 5.6, 'Umweltwärme\n(z. B. 0 °C)', fontsize=10.5, color='#2B8A3E')
    arrow(ax, (9.5, 10.6), (9.5, 8.6), color='#B08900', lw=4, ms=20); ax.text(9.8, 10.1, 'Strom für den Verdichter', fontsize=11, color='#B08900', fontweight='bold')
    arrow(ax, (16.0, 5.1), (18.6, 5.1), color=HOT, lw=4, ms=24); ax.text(16.1, 5.6, 'Heizwärme\n(z. B. 35 °C)', fontsize=10.5, color=HOT)
    ax.text(0.5, 3.6, 'Das Kältemittel verdampft schon\nbei sehr niedriger Temperatur\nund nimmt dabei Wärme auf.', fontsize=9.8, color=INK, va='top')
    ax.text(3.0, 8.9, 'Zusammendrücken macht\ndas Gas heiß.', fontsize=9.8, color=INK, va='top')
    ax.text(14.0, 3.2, 'Das Gas wird wieder flüssig\nund gibt die Wärme ab.', fontsize=9.8, color=INK, va='top')
    ax.text(7.4, 1.25, 'Druck sinkt, Kältemittel wird wieder kalt.', fontsize=9.8, color=INK, va='top')
    save(fig, 'wp')

def jaz():
    fig, ax = plt.subplots(figsize=(8.5, 2.4)); ax.set_xlim(0, 17); ax.set_ylim(-0.6, 2.4); ax.axis('off')
    def blk(x, n, c, t):
        for i in range(n):
            ax.add_patch(Rectangle((x + i * 1.15, 1.0), 1.0, 1.0, fc=c, ec=INK, lw=1))
        ax.text(x + n * 1.15 / 2 - 0.08, 0.8, t, ha='center', va='top', fontsize=11.5)
    blk(0.3, 1, ELEC, '1 kWh Strom'); ax.text(1.9, 1.5, '+', fontsize=24, va='center')
    blk(2.7, 3, ENV, '3 kWh Umweltwärme\n(kostenlos)'); ax.text(6.4, 1.5, '=', fontsize=24, va='center')
    blk(7.2, 4, HOT, '4 kWh Heizwärme')
    ax.text(12.4, 1.5, 'Jahresarbeitszahl\nJAZ = 4 kWh : 1 kWh = 4\n(ohne Einheit)', fontsize=12.5, va='center', color=INK, fontweight='bold')
    save(fig, 'jaz')

def kwk():
    fig, axs = plt.subplots(1, 2, figsize=(9, 2.6))
    data = [('Kraftwerk, das nur Strom erzeugt', [40, 0, 60]), ('Kraft-Wärme-Kopplung (Küstenkraftwerk)', [44.5, 47.5, 8])]
    for ax, (t, v) in zip(axs, data):
        left = 0
        for val, c, lab in zip(v, [ELEC, HOT, '#ADB5BD'], ['Strom', 'Wärme genutzt', 'Abwärme verloren']):
            if val:
                ax.barh(0, val, left=left, color=c, ec=INK)
                if val >= 15: ax.text(left + val / 2, 0, f'{lab}\n{val:g} %'.replace('.', ','), ha='center', va='center', fontsize=10.5)
                else: ax.text(left + val / 2, -0.42, f'{lab} {val:g} %'.replace('.', ','), ha='right', va='top', fontsize=9.5)
            left += val
        ax.set_xlim(0, 100); ax.set_ylim(-0.75, 0.5); ax.axis('off'); ax.set_title(t, fontsize=12, fontweight='bold', color=INK)
    fig.text(0.5, -0.04, '100 % = Energie im Erdgas. Werte gerundet (Küstenkraftwerk laut BDEW).', ha='center', fontsize=10, color=GREY)
    save(fig, 'kwk')

def fernwaerme():
    fig, ax = plt.subplots(figsize=(9, 4.4)); ax.set_xlim(-0.3, 18); ax.set_ylim(-1.0, 7.6); ax.axis('off')
    def node(x, y, w, h, t, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.12', fc=fc, ec=INK, lw=1.4))
        ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=10.5)
    node(0.3, 4.8, 5.0, 2.2, 'Küstenkraftwerk (Ostufer)\n20 Gasmotoren\nStrom + Wärme', '#FFE8CC')
    node(0.3, 1.6, 5.0, 2.6, 'Wärmespeicher (Ostufer):\n60 m hoch, 30 000 m³\nWasser mit 115 °C,\nreicht bis zu 8 Stunden', '#FFF3BF')
    node(0.3, -0.7, 5.0, 1.7, 'Müllverbrennung\nTheodor-Heuss-Ring:\nGrundlast, ganzjährig', '#E9ECEF')
    node(13.2, 4.6, 4.5, 2.4, 'Heizkraftwerk\nHumboldtstraße\n(am Schrevenpark)', '#FFE8CC')
    node(6.6, 2.4, 4.8, 2.6, 'Fernwärmenetz\nrund 374 km Rohre\nheißes Wasser hin,\nabgekühltes zurück', '#FFC9C9')
    node(13.2, 0.6, 4.5, 2.6, 'Wohnungen, Schulen,\nBüros: mehr als\n73 500 Anschlüsse', '#D3F9D8')
    for (bx, by, k) in [(0.3, 7.0, 1), (0.3, 4.2, 2), (0.3, 1.0, 3), (13.2, 7.0, 4)]:
        ax.add_patch(Circle((bx, by), 0.42, fc=INK, ec='white', lw=1.5, zorder=5))
        ax.text(bx, by, str(k), ha='center', va='center', color='white', fontsize=12, fontweight='bold', zorder=6)
    arrow(ax, (5.4, 5.6), (6.5, 4.4), color=HOT, lw=3); arrow(ax, (5.4, 2.9), (6.5, 3.2), color=HOT, lw=3)
    arrow(ax, (5.4, 0.2), (6.8, 2.3), color=HOT, lw=2)
    arrow(ax, (13.1, 5.6), (11.5, 4.4), color=HOT, lw=3); arrow(ax, (11.5, 3.0), (13.1, 2.2), color=HOT, lw=3)
    save(fig, 'fernwaerme')

def solarthermie():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.3), gridspec_kw=dict(width_ratios=[1.35, 1]))
    ax = axs[0]; ax.set_xlim(0, 15.6); ax.set_ylim(-0.6, 9); ax.axis('off')
    ax.add_patch(Polygon([(0.5, 5.0), (6.9, 8.6), (13.3, 5.0)], fc='#F1F3F5', ec=INK, lw=1.6))
    ax.add_patch(Polygon([(2.0, 6.0), (4.6, 7.7), (5.4, 7.2), (2.8, 5.5)], fc='#1864AB', ec=INK))
    ax.add_patch(Rectangle((1.2, 0.4), 11.4, 4.6, fc='#FFF4E6', ec=INK, lw=1.6))
    # Speicher mit Wärmetauscher-Wendel
    sx, sw = 5.6, 2.5
    ax.add_patch(FancyBboxPatch((sx, 0.8), sw, 3.4, boxstyle='round,pad=0.1', fc='#FFE3E3', ec=INK))
    ax.text(sx + sw / 2, 4.55, 'Speicher', ha='center', va='bottom', fontsize=10.5)
    # Solarkreislauf (geschlossen): heiß rein oben, kalt raus unten
    ax.plot([3.9, 3.9, sx + 0.3], [6.9, 3.5, 3.5], color=HOT, lw=2.5)
    ax.plot([3.2, 3.2, sx + 0.3], [6.2, 1.3, 1.3], color=COLD, lw=2.5)
    arrow(ax, (4.3, 3.5), (5.1, 3.5), color=HOT, lw=2); arrow(ax, (5.1, 1.3), (4.3, 1.3), color=COLD, lw=2)
    ys = np.linspace(3.5, 1.3, 9); xs = [sx + 0.3 if i % 2 == 0 else sx + 1.2 for i in range(9)]
    ax.plot(xs, ys, color='#C2410C', lw=2)
    ax.text(2.15, 2.4, 'Solar-\nkreislauf\n(ge-\nschlossen)', fontsize=9, color=INK, ha='center', va='center')
    ax.text(4.75, 2.4, 'Wärme-\ntauscher', fontsize=8.5, color=GREY, ha='center', va='center')
    # Trinkwasser: kalt von außen unten rein, warm oben raus zur Dusche
    ax.plot([15.3, sx + 1.9], [1.2, 1.2], color=COLD, lw=2.5)
    from matplotlib.colors import to_rgb
    c0, c1 = np.array(to_rgb(COLD)), np.array(to_rgb(HOT)); ys2 = np.linspace(1.2, 3.9, 25)
    for i in range(24):
        t = i / 23; ax.plot([sx + 1.9, sx + 1.9], [ys2[i], ys2[i + 1]], color=tuple(c0 * (1 - t) + c1 * t), lw=2.5, solid_capstyle='projecting')
    ax.plot([sx + 1.9, sx + sw + 0.1], [3.9, 3.9], color=HOT, lw=2.5)
    arrow(ax, (sx + 1.9, 2.3), (sx + 1.9, 2.75), color=tuple((c0 + c1) / 2), lw=0, ms=16)
    arrow(ax, (14.6, 1.2), (13.8, 1.2), color=COLD, lw=2)
    ax.text(14.2, 0.95, 'Kaltwasser\n(Leitung)', fontsize=9.5, ha='center', va='top')
    ax.plot([sx + sw + 0.1, 9.4, 9.4, 9.9], [3.9, 3.9, 3.0, 3.0], color=HOT, lw=2.5)
    arrow(ax, (8.45, 3.9), (9.1, 3.9), color=HOT, lw=2)
    ax.add_patch(Polygon([(9.6, 3.15), (10.4, 3.15), (10.25, 2.75), (9.75, 2.75)], fc='#ADB5BD', ec=INK, lw=1))
    for dx in (-0.15, 0.0, 0.15):
        ax.plot([10.0 + dx, 10.0 + dx * 1.8], [2.6, 1.9], color='#4DABF7', lw=1.2, ls=(0, (2, 2)))
    ax.text(10.6, 2.5, 'Dusche,\nWasser-\nhahn', fontsize=9.5, ha='left', va='center')
    ax.text(9.6, 4.15, 'Trinkwasser', fontsize=9.5, ha='center', va='bottom', color=INK)
    ax.add_patch(Circle((0.9, 8.3), 0.5, fc='#FAB005'))
    for i in range(3):
        arrow(ax, (1.5, 8.0 - i * 0.35), (2.4 + i * 0.4, 7.0 - i * 0.4), color='#FAB005', lw=1.8, ms=12)
    ax.text(5.7, 6.4, 'Kollektor', fontsize=10.5, ha='left')
    ax.set_title('So funktioniert Solarthermie', fontsize=12.5, fontweight='bold', color=INK)
    ax = axs[1]
    m = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
    need = [100] * 12; sun = [25, 40, 70, 100, 100, 100, 100, 100, 95, 60, 30, 18]
    ax.bar(range(12), need, color='#E9ECEF', ec=GREY, label='Warmwasserbedarf')
    ax.bar(range(12), sun, color='#FAB005', label='davon durch Sonne gedeckt')
    ax.set_xticks(range(12)); ax.set_xticklabels(m); ax.set_yticks([0, 50, 100]); ax.set_yticklabels(['0 %', '50 %', '100 %'])
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.legend(fontsize=9.5, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False)
    ax.set_title('Übers Jahr etwa 60 % gedeckt (schematisch)', fontsize=12.5, fontweight='bold', color=INK)
    save(fig, 'solarthermie')

def lampen():
    fig, axs = plt.subplots(1, 4, figsize=(10, 3.8))
    titles = ['Glühlampe', 'Halogenlampe', 'Leuchtstofflampe\n(„Energiesparlampe“)', 'LED-Lampe']
    light = [5, 7, 25, 40]
    for ax, t, l in zip(axs, titles, light):
        ax.set_xlim(0, 4); ax.set_ylim(-2.6, 5); ax.axis('off'); ax.set_title(t, fontsize=12, fontweight='bold', color=INK)
        ax.add_patch(Rectangle((1.45, 0), 1.1, 0.9, fc='#ADB5BD', ec=INK))
        for k in range(4): ax.plot([1.45, 2.55], [0.15 + k * 0.2, 0.25 + k * 0.2], color=INK, lw=0.8)
        ax.barh(-1.4, l, height=0.7, left=0, color='#FAB005', transform=ax.transData) if False else None
        # Energiebalken
        ax.add_patch(Rectangle((0.2, -2.2), 3.6 * l / 100, 0.6, fc='#FAB005', ec=INK, lw=0.6))
        ax.add_patch(Rectangle((0.2 + 3.6 * l / 100, -2.2), 3.6 * (100 - l) / 100, 0.6, fc='#FFA8A8', ec=INK, lw=0.6))
        ax.text(2, -1.35, f'Licht ≈ {l} %  ·  Wärme ≈ {100 - l} %', ha='center', fontsize=9.5)
    a = axs[0]; a.add_patch(Ellipse((2, 2.6), 2.6, 3.2, fc='#FFF9DB', ec=INK)); a.plot([1.7, 1.75, 2.0, 2.25, 2.3], [0.9, 2.4, 2.8, 2.4, 0.9], color=INK, lw=1)
    xs = np.linspace(1.75, 2.25, 60); a.plot(xs, 2.6 + 0.12 * np.sin(xs * 80), color='#E8590C', lw=1.5)
    a.text(2, 4.45, 'Wolframdraht, Schutzgas', ha='center', fontsize=9, color=GREY)
    b = axs[1]; b.add_patch(Ellipse((2, 2.6), 2.6, 3.2, fc='#FFF9DB', ec=INK)); b.add_patch(Rectangle((1.75, 1.6), 0.5, 1.6, fc='#E7F5FF', ec=INK))
    xs = np.linspace(1.85, 2.15, 60); b.plot(xs, 2.4 + 0.1 * np.sin(xs * 90), color='#E8590C', lw=1.5)
    b.text(2, 4.45, 'Glühdraht + Halogengas', ha='center', fontsize=9, color=GREY)
    c = axs[2]; c.add_patch(Rectangle((1.4, 0.9), 1.2, 0.6, fc='#DEE2E6', ec=INK))
    for xx in (1.6, 2.4):
        c.plot([xx, xx], [1.5, 3.9], color='#BAC8FF', lw=7, solid_capstyle='round'); c.plot([xx, xx], [1.5, 3.9], color=INK, lw=0.6)
    c.plot([1.6, 2.4], [3.9, 3.9], color='#BAC8FF', lw=7, solid_capstyle='round')
    c.text(2, 4.45, 'Quecksilberdampf, Leuchtstoff,\nElektronik im Sockel', ha='center', fontsize=9, color=GREY)
    e = axs[3]; e.add_patch(Ellipse((2, 2.7), 2.6, 3.0, fc='#F8F9FA', ec=INK)); e.add_patch(Rectangle((1.35, 0.9), 1.3, 0.6, fc='#495057', ec=INK))
    e.add_patch(Rectangle((1.45, 1.5), 1.1, 0.25, fc='#868E96', ec=INK))
    for xx in (1.65, 2.0, 2.35): e.add_patch(Rectangle((xx - 0.09, 1.75), 0.18, 0.15, fc='#FFE066', ec=INK, lw=0.5))
    e.text(2, 4.45, 'Halbleiter-Chips, Kühlkörper,\nTreiber-Elektronik', ha='center', fontsize=9, color=GREY)
    fig.text(0.5, 0.0, 'Schematisch, nicht maßstäblich. Anteile Licht/Wärme gerundet.', ha='center', fontsize=9.5, color=GREY)
    save(fig, 'lampen')

def co2():
    items = [('Ein Fernflug weniger (New York hin und zurück)', 3.9), ('Wärmepumpe statt Gasheizung (*)', 0.85),
             ('10 000 km Bus, Bahn, Rad statt Auto', 1.5), ('Ein Mallorca-Flug weniger (hin und zurück)', 0.7),
             ('Vegetarisch statt viel Fleisch', 0.5), ('Außenwand dämmen (*)', 0.35), ('Kurz statt lange duschen (Sparduschkopf)', 0.4),
             ('1 °C weniger heizen (*)', 0.1), ('LEDs statt Glühlampen (*)', 0.03), ('Stand-by halbieren (*)', 0.02)]
    items.sort(key=lambda x: x[1])
    fig, ax = plt.subplots(figsize=(9, 4.8))
    cols = [HOT if v >= 1 else (WARM if v >= 0.3 else '#74C0FC') for _, v in items]
    ax.barh([t for t, _ in items], [v for _, v in items], color=cols, ec=INK, lw=0.6)
    for i, (_, v) in enumerate(items): ax.text(v + 0.05, i, f'{v:g} t'.replace('.', ','), va='center', fontsize=12)
    ax.tick_params(labelsize=12)
    ax.set_xlabel('eingesparte Tonnen CO₂ pro Person und Jahr (gerundete Richtwerte)', fontsize=12)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    ax.set_xlim(0, 4.6)
    fig.text(0.01, -0.03, '(*) für einen Haushalt mit 15 000 kWh Heizwärme bzw. 2 500 kWh Strom, geteilt durch 2,5 Personen. Zum Vergleich: Ø-Fußabdruck rund 10 t, Ziel unter 1 t.', fontsize=10, color=GREY, wrap=True)
    save(fig, 'co2')

def concept():
    fig, ax = plt.subplots(figsize=(11, 5.4)); ax.set_xlim(0, 22); ax.set_ylim(0, 11.2); ax.axis('off')
    def node(x, y, w, h, t, fc, fs=14):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.2', fc=fc, ec=INK, lw=2))
        ax.text(x + w / 2, y + h / 2, t, ha='center', va='center', fontsize=fs)
    node(0.5, 6.2, 6, 3.6, 'Lernpfad\n\nInfo-Kasten lesen,\nAufgaben üben', '#D0EBFF')
    node(8.2, 6.2, 6, 3.6, 'Zu Hause\n\nDaten erheben, messen,\nWärmebilder aufnehmen', '#FFF3BF')
    node(15.6, 6.2, 6, 3.6, 'Protokoll\n\nDaten eintragen,\nmit eigenen Zahlen rechnen', '#D3F9D8')
    node(15.6, 0.6, 6, 3.6, 'Kasten\n„Für dein Gutachten“\n\nBewerten und Vorschlag', '#FFE8CC')
    node(3.6, 0.6, 10.1, 3.6, 'Gutachten (Protokoll Teil 10)\n\nAlle Bausteine zusammenfügen:\nStärken, Schwächen, Maßnahmen, Kosten, CO₂', '#FFC9C9')
    arrow(ax, (6.7, 8.0), (8.0, 8.0), lw=3, ms=26); arrow(ax, (14.4, 8.0), (15.4, 8.0), lw=3, ms=26)
    arrow(ax, (18.6, 6.0), (18.6, 4.4), lw=3, ms=26); arrow(ax, (15.4, 2.4), (13.7, 2.4), lw=3, ms=26)
    ax.annotate('', xy=(3.5, 10.0), xytext=(18.6, 10.0), arrowprops=dict(arrowstyle='-|>', lw=2, color=GREY, connectionstyle='arc3,rad=0.08', mutation_scale=22))
    ax.text(11, 10.75, 'nächster Teil: wieder von vorn (Teil 1 bis 9)', ha='center', fontsize=12, color=GREY)
    save(fig, 'concept')

def lampen_foto():
    from PIL import Image as _I
    L = os.path.join(os.path.dirname(OUT), 'lamp')
    fig, axs = plt.subplots(1, 4, figsize=(10, 3.7), gridspec_kw=dict(wspace=0.15))
    titles = ['Glühlampe', 'Halogenlampe', 'Energiesparlampe\n(Leuchtstofflampe)', 'LED-Lampe\n(geöffnet)']
    files = ['g_w.png', 'h_w.png', 'e_w.png', 'l_lamp.png']
    light = [5, 7, 25, 40]
    for ax, t, f, l in zip(axs, titles, files, light):
        im = _I.open(os.path.join(L, f)).convert('RGB'); w, h = im.size
        ax.set_xlim(0, 4); ax.set_ylim(-1.5, 4.7); ax.axis('off')
        ax.set_title(t, fontsize=11.5, fontweight='bold', color=INK)
        bw, bh = 3.6, 4.6; s = min(bw / w, bh / h); iw, ih = w * s, h * s
        ax.imshow(im, extent=(2 - iw / 2, 2 + iw / 2, (bh - ih) / 2, (bh + ih) / 2), aspect='auto', zorder=1)
        ax.add_patch(Rectangle((0.2, -1.4), 3.6 * l / 100, 0.5, fc='#FAB005', ec=INK, lw=0.6))
        ax.add_patch(Rectangle((0.2 + 3.6 * l / 100, -1.4), 3.6 * (100 - l) / 100, 0.5, fc='#FFA8A8', ec=INK, lw=0.6))
        ax.text(2, -0.6, f'Licht ≈ {l} %  ·  Wärme ≈ {100 - l} %', ha='center', fontsize=9.5)
    fig.text(0.5, -0.01, 'Fotos: Wikimedia Commons (bearbeitet; LED-Lampe: Loadmaster, CC BY-SA 4.0). Anteile Licht/Wärme gerundet. Die gelben Quadrate sind die Leuchtdioden.', ha='center', fontsize=9, color=GREY)
    save(fig, 'lampen_foto')

if __name__ == '__main__':
    for f in (haus, transport, dach, geschossdecke, windrose, fenster, wp, jaz, kwk, fernwaerme, solarthermie, lampen, co2, concept):
        f(); print('ok', f.__name__)

def dachformen():
    W, D, H, R = 4.0, 3.0, 2.2, 1.6
    def P(x, y, z): return (x + 0.55 * y, z + 0.35 * y)
    WALL, ROOF, ROOF2 = '#F1F3F2', '#C9D3D0', '#A9B7B3'
    def face(ax, pts, fc):
        ax.add_patch(Polygon([P(*p) for p in pts], closed=True, fc=fc, ec=INK, lw=1.1, joinstyle='round'))
    def walls(ax, zr=None):
        face(ax, [(0, 0, 0), (W, 0, 0), (W, 0, H), (0, 0, H)], WALL)
        face(ax, [(W, 0, 0), (W, D, 0), (W, D, H)] + (zr or []) + [(W, 0, H)], '#E2E6E4')
    def sattel(ax):
        walls(ax, [(W, D / 2, H + R)])
        face(ax, [(0, 0, H), (W, 0, H), (W, D / 2, H + R), (0, D / 2, H + R)], ROOF)
    def walm(ax):
        a = 1.2; walls(ax)
        face(ax, [(W, 0, H), (W, D, H), (W - a, D / 2, H + R)], ROOF2)
        face(ax, [(0, 0, H), (W, 0, H), (W - a, D / 2, H + R), (a, D / 2, H + R)], ROOF)
    def kruppel(ax):
        a, f = 0.6, 0.6; zc = H + f * R; y1 = f * D / 2
        walls(ax, [(W, D - y1, zc), (W, y1, zc)])
        face(ax, [(W, y1, zc), (W, D - y1, zc), (W - a, D / 2, H + R)], ROOF2)
        face(ax, [(0, 0, H), (W, 0, H), (W, y1, zc), (W - a, D / 2, H + R), (a, D / 2, H + R), (0, y1, zc)], ROOF)
    def pult(ax):
        r = 1.1; walls(ax, [(W, D, H + r)])
        face(ax, [(0, 0, H), (W, 0, H), (W, D, H + r), (0, D, H + r)], ROOF)
    def mansard(ax):
        b, z1, z2 = 0.45, H + 1.0, H + 1.45
        walls(ax, [(W, D - b, z1), (W, D / 2, z2), (W, b, z1)])
        face(ax, [(0, 0, H), (W, 0, H), (W, b, z1), (0, b, z1)], ROOF2)
        face(ax, [(0, b, z1), (W, b, z1), (W, D / 2, z2), (0, D / 2, z2)], ROOF)
    def flach(ax):
        walls(ax)
        face(ax, [(0, 0, H), (W, 0, H), (W, D, H), (0, D, H)], ROOF)
        face(ax, [(0, 0, H), (W, 0, H), (W, 0, H + 0.15), (0, 0, H + 0.15)], ROOF2)
    items = [('Satteldach', sattel), ('Walmdach', walm), ('Krüppelwalmdach', kruppel),
             ('Pultdach', pult), ('Mansarddach', mansard), ('Flachdach', flach)]
    fig, axs = plt.subplots(1, 6, figsize=(11, 2.4), gridspec_kw=dict(wspace=0.08))
    for ax, (t, fn) in zip(axs, items):
        fn(ax); ax.set_xlim(-0.3, W + 0.55 * D + 0.3); ax.set_ylim(-0.2, H + R + 0.35 * D + 0.3)
        ax.set_aspect('equal'); ax.axis('off'); ax.set_title(t, fontsize=12, fontweight='bold', color=INK, y=-0.18)
    save(fig, 'dachformen')
