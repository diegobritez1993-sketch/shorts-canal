"""Short: ¿Por qué te duele tanto perder una racha?
Fuentes: Duolingo Blog, "How the Duolingo streak builds habit" (31/01/2022): con racha de 7 días, 3,6 veces más
probable terminar el curso; más de 6 millones con racha de 7+ días; protector de racha (Streak Freeze).
Aversión a la pérdida: Kahneman y Tversky, Prospect Theory (Econometrica, 1979).
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

ORANGE = (255, 149, 0)
ICE = (140, 210, 255)

def flame(d, cx, cy, s, t, col=ORANGE, core=Y):
    """Llama tipo gota con punta que se mueve."""
    def drop(r, c, by, ph):
        tip = (cx + math.sin(t * 7 + ph) * r * 0.25, by - r * 2.4)
        a = math.asin(r / math.hypot(tip[0] - cx, tip[1] - by))
        base_ang = math.atan2(tip[1] - by, tip[0] - cx)
        p1 = (cx + r * math.cos(base_ang + math.pi / 2 + a * 0), by + r * math.sin(base_ang + math.pi / 2))
        p2 = (cx + r * math.cos(base_ang - math.pi / 2), by + r * math.sin(base_ang - math.pi / 2))
        d.polygon([(S(p1[0]), S(p1[1])), (S(tip[0]), S(tip[1])), (S(p2[0]), S(p2[1]))], fill=c)
        circle(d, cx, by, r, fill=c)
    r = s * 0.42
    drop(r, col, cy + s * 0.35, 0)
    drop(r * 0.62, core, cy + s * 0.5, 1.3)

def ice_cube(d, cx, cy, s, alpha=1.0):
    col = mix(K, ICE, alpha)
    rrect(d, cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2, s * 0.18, outline=col, width=14)

def scale_bal(d, cx, cy, ang, lt):
    """Balanza: plato izq = GANAR, plato der = PERDER."""
    d.polygon([(S(cx - 70), S(cy + 300)), (S(cx + 70), S(cy + 300)), (S(cx), S(cy + 200))], fill=C)
    d.line([S(cx), S(cy + 210), S(cx), S(cy)], fill=C, width=S(16))
    L = 330
    ca, sa = math.cos(ang), math.sin(ang)
    for side, lab, col in ((-1, "GANAR", GREEN), (1, "PERDER", R)):
        px, py = cx + side * L * ca, cy + side * L * sa
        d.line([S(cx), S(cy), S(px), S(py)], fill=C, width=S(14))
        d.line([S(px), S(py), S(px), S(py + 110)], fill=C, width=S(6))
        rrect(d, px - 150, py + 110, px + 150, py + 190, 30, fill=col)
        text_c(d, px, py + 150, lab, "A", 58, K if side < 0 else C, bg=col)
    circle(d, cx, cy, 24, fill=Y)

# 0-4: gancho
def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        flame(d, 540, 520, 300 * e, t)
        n = min(147, int(147 * ease_out(prog(t, 0.2, 1.4))))
        text_c(d, 540, 640, str(n), "A", 100, K, bg=Y)
    pop_line(d, t, 0.4, 540, 960, "¿POR QUÉ TE DUELE", 125, C)
    pop_line(d, t, 0.7, 540, 1115, "TANTO PERDER", 135, C)
    pop_line(d, t, 1.0, 540, 1280, "UNA RACHA?", 175, Y)
    pill(d, t, 2.5, 540, 1460, 700, "NO ES CASUALIDAD", size=44)

# 4-8: aversión a la pérdida
def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "TU CEREBRO SIENTE", 105, C)
    slide_line(d, lt, 0.3, 540, 410, "MÁS FUERTE", 120, Y)
    p = prog(lt, 0.5, 0.35)
    if p > 0:
        ang = math.radians(16) * ease_out(prog(lt, 1.0, 0.8)) + math.radians(3) * math.sin(lt * 6) * (1 - prog(lt, 1.0, 1.4))
        scale_bal(d, 540, 640 + (1 - ease_out(p)) * 80, ang, lt)
    pop_line(d, lt, 2.1, 540, 1200, "PERDER QUE GANAR", 130, R)
    slide_line(d, lt, 2.5, 540, 1330, "se llama aversión a la pérdida", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1400, "Kahneman y Tversky, 1979", 34, G, kind="SemiBold", dy=20)

# 4-8 -> 8-12: el dato de los 7 días
def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "UNA APP DE IDIOMAS", 100, C)
    slide_line(d, lt, 0.3, 540, 425, "LO MIDIÓ", 110, Y)
    days = "LMMJVSD"
    for k in range(7):
        t0 = 0.6 + k * 0.17
        p = prog(lt, t0, 0.25)
        cx = 150 + k * 130
        circle(d, cx, 600, 52, fill=(50, 50, 50))
        if p > 0:
            circle(d, cx, 600, 52 * back(p), fill=ORANGE)
        text_c(d, cx, 600, days[k], "Black", 40, K if p > 0.5 else C, bg=ORANGE if p > 0.5 else (50, 50, 50))
    slide_line(d, lt, 1.9, 540, 730, "con 7 días de racha seguidos", 46, C, kind="SemiBold", dy=25)
    stamp(d, lt, 2.2, 540, 940, 300, 120, "3,6 VECES", size=150)
    slide_line(d, lt, 2.6, 540, 1140, "MÁS PROBABLE QUE", 80, C, dy=25)
    slide_line(d, lt, 2.75, 540, 1235, "TERMINES EL CURSO", 80, C, dy=25)
    slide_line(d, lt, 3.0, 540, 1350, "Duolingo Blog, 2022", 34, G, kind="SemiBold", dy=20)

# 12-16: 6 millones de personas
def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "EN ESA APP HABÍA", 105, C)
    rnd = random.Random(3)
    lit = int(60 * ease_in_out(prog(lt, 0.4, 1.4)))
    for k in range(60):
        r, c = divmod(k, 10)
        x, y = 135 + c * 90, 450 + r * 105
        person(d, x, y, 78, ORANGE if k < lit else (60, 60, 60))
    n = 6 * ease_out(prog(lt, 0.4, 1.6))
    sx, sy = shake(lt, 2.1, 0.35, 16)
    if lt > 0.4:
        text_c(d, 540 + sx, 1180 + sy, f"+{int(n)} MILLONES", "A", 150, Y)
    slide_line(d, lt, 2.3, 540, 1320, "con una racha de 7 días o más", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1390, "Duolingo Blog, 2022", 34, G, kind="SemiBold", dy=20)

# 16-20: el protector de racha
def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y SI FALLÁS UN DÍA...", 100, C)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        flame(d, 540, 680, 240 * e, t)
    pi = prog(lt, 1.0, 0.4)
    if pi > 0:
        ice_cube(d, 540, 700, lerp(700, 380, ease_out(pi)), alpha=clamp(pi * 2))
    pop_line(d, lt, 1.6, 540, 1060, "TE OFRECE UN", 110, C)
    pop_line(d, lt, 1.85, 540, 1190, "\"PROTECTOR\"", 150, ICE)
    slide_line(d, lt, 2.4, 540, 1320, "para que no la pierdas...", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.9, 540, 1385, "ni la app a vos", 46, Y, kind="Bold", dy=25)

# 20-23.2: pregunta
def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 400, "¿CUÁL ES TU", 150, C)
    slide_line(d, lt, 0.3, 540, 560, "RACHA MÁS LARGA?", 120, Y)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        flame(d, 540, 820, 160 * e, t)
        text_c(d, 540, 880, "?", "A", 70, K, bg=Y)
    slide_line(d, lt, 1.4, 540, 1080, "contala en los comentarios", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.7, 540, 1150, "usala a tu favor, no al revés", 44, G, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer")
for k in range(14): ev(0.2 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(0.4, "pop", -0.3); ev(0.7, "pop", 0.3); ev(1.0, "thump"); ev(2.5, "pop")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3); ev(4.5, "pop"); ev(5.0, "click"); ev(5.8, "thump", 0.3)
ev(6.1, "stamp"); ev(6.5, "tap")
ev(8.1, "tap", -0.3); ev(8.3, "pop")
for k in range(7): ev(8.6 + k * 0.17, "pop", -0.6 + k * 0.2)
ev(9.9, "tap"); ev(10.2, "stamp"); ev(10.6, "tap"); ev(10.75, "tap")
ev(12.1, "pop")
for k in range(14): ev(12.4 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(14.1, "thump"); ev(14.3, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(17.0, "whoosh"); ev(17.3, "ding")
ev(17.6, "pop", -0.2); ev(17.85, "thump"); ev(18.4, "tap"); ev(18.9, "tap")
ev(20.1, "pop"); ev(20.3, "pop", 0.2); ev(20.6, "shimmer"); ev(21.4, "tap"); ev(21.7, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
