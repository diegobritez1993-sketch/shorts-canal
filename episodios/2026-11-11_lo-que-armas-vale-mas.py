"""Short 2026-11-11 15:00 — Curiosidades y hábitos: el "efecto IKEA" (lo que armás vos te parece que vale más).

Fuente: Norton, Mochon y Ariely, "The IKEA Effect: When Labor Leads to Love", Harvard Business School Working Paper 11-091
(2011; Journal of Consumer Psychology 22(3), 2012).
- Exp. 1A (52 personas): quienes armaron una caja de IKEA ofrecieron US$0,78 vs US$0,48 de quienes la recibieron armada (~63% más).
- Exp. 1B (106 personas): quienes hicieron un origami ofrecieron US$0,23 por el suyo; los que no lo hicieron, US$0,05 por esos
  mismos (~4,6 veces más: "casi 5 veces"). Lo valoraban casi como un origami de experto (US$0,27; diferencia no significativa).
- Exp. 2 (Lego): si lo armaban y lo desarmaban, la diferencia dejaba de ser significativa. Exp. 3: si no lo terminaban, ofrecían menos.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

CARD = (196, 150, 98)     # cartón
CARD_D = (150, 108, 64)
WOOD = (214, 170, 110)

def flatbox(d, cx, cy, w, open_p=0.0, t=0.0, wob=0.0):
    """Caja de cartón plana con solapas que se abren."""
    ox = math.sin(t * 38) * 10 * wob
    h = w * 0.6
    x0, x1, y0, y1 = cx - w / 2 + ox, cx + w / 2 + ox, cy - h / 2, cy + h / 2
    rrect(d, x0, y0, x1, y1, 14, fill=CARD, outline=CARD_D, width=8)
    d.rectangle([S(x0 + 8), S(cy - 10), S(x1 - 8), S(cy + 10)], fill=CARD_D)   # cinta
    # solapas
    a = ease_out(open_p) * 0.9
    for side in (-1, 1):
        px = cx + ox + side * w / 2
        ln = w * 0.48
        ex = px - side * ln * math.cos(a)
        ey = y0 - ln * math.sin(a)
        d.polygon([(S(px), S(y0)), (S(cx + ox), S(y0)), (S(lerp(cx + ox, ex, 1)), S(ey)), (S(ex), S(ey))] if a > 0.02 else
                  [(S(px), S(y0)), (S(cx + ox), S(y0)), (S(cx + ox), S(y0 + 2)), (S(px), S(y0 + 2))], fill=CARD_D)

def screw(d, cx, cy, s, rot):
    circle(d, cx, cy, s * 0.5, fill=(200, 200, 200))
    a = rot
    d.line([S(cx - math.cos(a) * s * 0.35), S(cy - math.sin(a) * s * 0.35),
            S(cx + math.cos(a) * s * 0.35), S(cy + math.sin(a) * s * 0.35)], fill=K2, width=int(S(max(3, s * 0.12))))
    d.line([S(cx + math.sin(a) * s * 0.35), S(cy - math.cos(a) * s * 0.35),
            S(cx - math.sin(a) * s * 0.35), S(cy + math.cos(a) * s * 0.35)], fill=K2, width=int(S(max(3, s * 0.12))))

def shelf(d, cx, cy, p):
    """Repisa que se arma pieza por pieza (p 0..1)."""
    pieces = [(-170, -170, 170, -140), (-170, -20, 170, 10), (-170, 130, 170, 160), (-185, -200, -160, 190), (160, -200, 185, 190)]
    for k, (a, b, c, e) in enumerate(pieces):
        q = ease_out(clamp(p * len(pieces) - k))
        if q <= 0: continue
        dx = (1 - q) * (300 if k % 2 else -300)
        rrect(d, cx + a + dx, cy + b, cx + c + dx, cy + e, 6, fill=WOOD)

def crane(d, cx, cy, s, col=Y):
    """Origami tipo grulla con triángulos."""
    P = lambda x, y: (S(cx + x * s), S(cy + y * s))
    d.polygon([P(-0.55, 0.15), P(0, -0.05), P(0.55, 0.15), P(0, 0.35)], fill=mix(col, K, 0.25))
    d.polygon([P(-0.05, 0.0), P(0.0, -0.75), P(0.25, 0.1)], fill=col)            # ala
    d.polygon([P(0.35, 0.2), P(0.75, -0.45), P(0.82, -0.38), P(0.48, 0.22)], fill=col)  # cuello
    d.polygon([P(0.75, -0.45), P(0.95, -0.4), P(0.82, -0.38)], fill=col)          # pico
    d.polygon([P(-0.4, 0.15), P(-0.85, -0.25), P(-0.25, 0.25)], fill=col)          # cola

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        flatbox(d, 540, 560, 460 * e, open_p=prog(t, 1.6, 0.5), t=t, wob=1.0 if t < 1.4 and (t % 0.8) < 0.3 else 0.0)
        for k in range(4):
            sp = prog(t, 2.0 + k * 0.15, 0.6)
            if sp > 0:
                screw(d, 400 + k * 95, lerp(470, 300 - (k % 2) * 40, ease_out(sp)), 34, t * 3 + k)
    pop_line(d, t, 0.15, 540, 940, "¿POR QUÉ AMÁS", 140, C)
    pop_line(d, t, 0.45, 540, 1090, "LO QUE ARMÁS", 160, Y)
    pop_line(d, t, 0.75, 540, 1230, "VOS MISMO?", 140, C)
    pill(d, t, 1.6, 540, 1410, 520, "TIENE NOMBRE", fill=R, ink=C, size=46, h=96)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "EXPERIMENTO", 130, C)
    slide_line(d, lt, 0.3, 540, 410, "DE HARVARD", 110, Y)
    # dos grupos
    for k, (x, lab, sub) in enumerate([(300, "GRUPO A", "lo armó"), (780, "GRUPO B", "lo recibió armado")]):
        q = back(prog(lt, 0.6 + k * 0.3, 0.35))
        if q > 0.02:
            person(d, x, 640, 200 * q, C if k == 0 else G)
        pill(d, lt, 0.8 + k * 0.3, x, 800, 300, lab, fill=Y if k == 0 else K2, ink=K if k == 0 else C, size=40, h=84)
        slide_line(d, lt, 1.0 + k * 0.3, x, 880, sub, 40, C, kind="SemiBold", dy=20)
    # A arma la repisa, B la mira ya hecha
    shelf(d, 300, 1180, prog(lt, 1.5, 1.6))
    if lt > 1.5:
        shelf(d, 780, 1180, 1.0)
    slide_line(d, lt, 2.6, 540, 1450, "la misma caja de muebles", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1520, "Norton, Mochon y Ariely, Harvard Business School, 2011", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 300, "¿CUÁNTO PAGARÍAN?", 120, C)
    base = 1060
    # barras: B = 100, A = 163
    hb = 330 * ease_out(prog(lt, 0.5, 0.5))
    ha = 538 * ease_out(prog(lt, 0.9, 1.0))
    if hb > 1:
        rrect(d, 600, base - hb, 860, base, 20, fill=(70, 70, 70))
        text_c(d, 730, base + 50, "lo recibió armado", "SemiBold", 34, G)
    if ha > 1:
        rrect(d, 220, base - ha, 480, base, 20, fill=Y)
        text_c(d, 350, base + 50, "lo armó", "SemiBold", 34, C)
    if lt > 0.5:
        d.line([S(160), S(base), S(920), S(base)], fill=C, width=S(6))
    n = 63 * ease_out(prog(lt, 0.9, 1.0))
    if lt > 0.9:
        text_c(d, 350, base - ha - 70, f"+{int(n)}%", "A", 110, Y)
    sx, sy = shake(lt, 2.0, 0.35, 14)
    stamp(d, lt, 1.95, 540 + sx, 1300 + sy, 380, 110, "63% MÁS", fill=Y, ink=K, size=150)
    slide_line(d, lt, 2.5, 540, 1460, "por algo que ellos mismos armaron", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1530, "HBS Working Paper 11-091", 32, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "CON ORIGAMI", 140, C)
    q = back(prog(lt, 0.3, 0.45))
    if q > 0.02:
        crane(d, 540, 560 + math.sin(lt * 3) * 10, 260 * q)
    # multiplicador x1 → x5 (4,6 real: "casi 5")
    m = 1 + 3.6 * ease_out(prog(lt, 1.0, 1.2))
    if lt > 1.0:
        text_c(d, 540, 860, f"x{m:.1f}".replace(".", ","), "A", 170, Y)
    pop_line(d, lt, 2.3, 540, 1040, "CASI 5 VECES MÁS", 120, C)
    slide_line(d, lt, 2.6, 540, 1170, "y lo valoraban casi como", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.75, 540, 1235, "el de un experto", 46, Y, kind="Bold", dy=25)
    slide_line(d, lt, 2.9, 540, 1330, "para los demás, valía casi nada", 40, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "PERO OJO:", 130, Y)
    slide_line(d, lt, 0.35, 540, 420, "SI LO DESARMABAN...", 110, C)
    # torre de bloques que se derrumba
    cols = [Y, C, R, Y, C, R]
    fall = prog(lt, 1.3, 0.9)
    for k in range(6):
        ap = ease_out(prog(lt, 0.5 + k * 0.1, 0.25))
        if ap <= 0: continue
        bx, by = 540, 1000 - k * 75
        if fall > 0:
            dirx = (1 if k % 2 else -1) * (60 + k * 40)
            bx += dirx * ease_out(fall)
            by += (1000 - by) * ease_in_out(fall) + (k % 3) * 20 * fall
        y0 = by - 70 * ap
        rrect(d, bx - 110, y0, bx + 110, by, 12, fill=cols[k])
        for j in (-1, 1):
            circle(d, bx + j * 55, y0 - 6, 18, fill=cols[k])
    stamp(d, lt, 2.3, 540, 1240, 420, 110, "SE ESFUMA", fill=R, ink=C, size=140)
    slide_line(d, lt, 2.8, 540, 1400, "si no lo terminaban, también valía menos", 40, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 320, "SE LLAMA", 110, C)
    slide_line(d, lt, 0.3, 540, 460, "\"EFECTO IKEA\"", 150, Y)
    slide_line(d, lt, 0.7, 540, 590, "tu esfuerzo te hace verlo más lindo", 44, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.4, 540, 860, "¿QUÉ ARMASTE VOS", 115, C)
    pop_line(d, lt, 1.65, 540, 1000, "Y NO SOLTÁS?", 140, Y)
    slide_line(d, lt, 2.1, 540, 1140, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)
    q = back(prog(lt, 2.3, 0.35))
    if q > 0.02:
        bubble(d, 540, 1330, 170 * q, Y)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.15, "pop", -0.2); ev(0.45, "thump"); ev(0.75, "pop", 0.2); ev(0.3, "tap"); ev(0.8, "tap")
ev(1.6, "click"); ev(1.65, "rustle")
for k in range(4): ev(2.0 + k * 0.15, "tick", -0.4 + k * 0.27)
ev(4.1, "swipe"); ev(4.3, "swipe"); ev(4.6, "pop", -0.4); ev(4.9, "pop", 0.4); ev(4.8, "click", -0.4); ev(5.1, "click", 0.4)
for k in range(5): ev(5.5 + k * 0.32, "tap", -0.4 if k % 2 else -0.2)
ev(6.6, "tap"); ev(6.8, "tap")
ev(8.1, "pop"); ev(8.5, "tap", 0.4)
for k in range(10): ev(8.9 + k * 0.1, "tick", -0.3)
ev(9.95, "stamp"); ev(10.5, "tap"); ev(10.7, "tap")
ev(12.1, "swipe"); ev(12.3, "rustle"); ev(12.35, "pop")
for k in range(8): ev(13.0 + k * 0.15, "tick", 0.3 if k % 2 else -0.3)
ev(14.3, "thump"); ev(14.6, "tap"); ev(14.75, "tap"); ev(14.9, "tap")
ev(16.1, "pop"); ev(16.35, "swipe")
for k in range(6): ev(16.5 + k * 0.1, "click", -0.3 + k * 0.12)
ev(17.3, "rustle"); ev(17.5, "thump"); ev(17.7, "tap", -0.5); ev(17.8, "tap", 0.5)
ev(18.3, "stamp"); ev(18.8, "tap")
ev(20.1, "swipe"); ev(20.3, "pop"); ev(20.7, "tap"); ev(21.4, "pop", -0.2); ev(21.65, "thump"); ev(22.1, "tap"); ev(22.3, "pop")

if __name__ == "__main__":
    main(BEATS_EP)
