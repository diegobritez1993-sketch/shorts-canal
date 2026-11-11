"""Short 2026-11-11 20:00 — Mente y emociones: 2 horas por semana en la naturaleza.

Fuente: White et al., Universidad de Exeter, "Spending at least 120 minutes a week in nature is associated with good health
and wellbeing", Scientific Reports, 13/06/2019 (vía ECEHH/Univ. de Exeter y MedicalXpress).
- Casi 20.000 personas en Inglaterra (encuesta MENE de Natural England).
- Con al menos 120 min por semana en la naturaleza: más probable reportar buena salud y mayor bienestar psicológico.
- Con menos de 2 horas, igual que quienes no salían nada.
- Daba igual una visita larga o varias cortas. Vale parques, bosques, playas. La mayoría, a menos de ~3 km (2 millas) de casa.
- Valía para hombres y mujeres, jóvenes y mayores, con o sin enfermedades crónicas. Es una asociación, no prueba causa.
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

LEAF = (60, 170, 80)
LEAF2 = (40, 130, 60)
TRUNK = (140, 95, 55)

def tree(d, cx, by, s, sway=0.0):
    """Árbol simple: tronco + copa de círculos. by = base."""
    rrect(d, cx - s * 0.07, by - s * 0.55, cx + s * 0.07, by, 8, fill=TRUNK)
    ox = sway * s * 0.04
    for dx, dy, r, c in [(-0.2, -0.6, 0.24, LEAF2), (0.2, -0.62, 0.24, LEAF2), (0, -0.85, 0.3, LEAF), (-0.12, -0.7, 0.22, LEAF), (0.14, -0.72, 0.22, LEAF)]:
        circle(d, cx + dx * s + ox, by + dy * s, r * s, fill=c)

def leaf(d, cx, cy, s, a, col=LEAF):
    pts = []
    for k in range(12):
        u = k / 11 * math.pi
        x, y = math.cos(u) * s, math.sin(u) * s * 0.4
        pts.append((x, y))
    pts += [(x, -y) for x, y in reversed(pts)]
    ca, sa = math.cos(a), math.sin(a)
    d.polygon([(S(cx + x * ca - y * sa), S(cy + x * sa + y * ca)) for x, y in pts], fill=col)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        tree(d, 540, 760, 520 * e, sway=math.sin(t * 2))
    for k in range(5):
        lp = (t * 0.35 + k * 0.21) % 1.0
        if t > 0.6:
            leaf(d, 220 + k * 160 + math.sin(t * 2 + k) * 40, 260 + lp * 600, 34, t * 2 + k, LEAF if k % 2 else Y)
    pop_line(d, t, 0.2, 540, 950, "¿CUÁNTO TIEMPO", 140, C)
    pop_line(d, t, 0.5, 540, 1100, "AL AIRE LIBRE", 160, GREEN)
    pop_line(d, t, 0.8, 540, 1240, "NECESITÁS?", 140, C)
    pill(d, t, 1.6, 540, 1420, 620, "HAY UN NÚMERO", fill=Y, ink=K, size=48, h=100)

def b2(d, t):
    lt = t - 4
    n = 20000 * ease_out(prog(lt, 0.1, 1.3))
    pop_line(d, lt, 0.1, 540, 300, "CASI " + fmt_num(round(n, -2)), 160, Y, dur=0.25)
    slide_line(d, lt, 0.4, 540, 430, "PERSONAS ESTUDIADAS", 100, C)
    # grilla de personitas que se encienden
    rnd = random.Random(3)
    for r in range(6):
        for c in range(9):
            k = r * 9 + c
            q = prog(lt, 0.4 + k * 0.03, 0.2)
            if q <= 0: continue
            x, y = 140 + c * 100, 600 + r * 120
            person(d, x, y, 80 * ease_out(q), C if rnd.random() > 0.15 else Y)
    slide_line(d, lt, 2.4, 540, 1380, "en Inglaterra, sobre salud y bienestar", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1450, "White et al., Univ. de Exeter, Scientific Reports 2019", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "LA CLAVE:", 120, C)
    pr = prog(lt, 0.4, 1.6)
    clock(d, 540, 720, 260, ease_out(pr), turns=2, fill_deg=360)
    if lt > 0.4:
        m = int(120 * ease_out(pr))
        text_c(d, 540, 1070, f"{m} MIN", "A", 170, Y)
    pop_line(d, lt, 2.2, 540, 1230, "POR SEMANA", 130, C)
    sx, sy = shake(lt, 2.75, 0.35, 14)
    stamp(d, lt, 2.6, 540 + sx, 1420 + sy, 300, 90, "= 2 HORAS", fill=GREEN, ink=K, size=120)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "CON MENOS DE 2 H", 120, C)
    slide_line(d, lt, 0.3, 540, 410, "NO HUBO DIFERENCIA", 100, R)
    base = 1060
    bars = [("0 min", 240, (80, 80, 80), 0.6), ("1 hora", 240, (80, 80, 80), 0.9), ("2 h o más", 400, GREEN, 1.6)]
    for k, (lab, hh, col, t0) in enumerate(bars):
        h = hh * ease_out(prog(lt, t0, 0.5))
        x = 190 + k * 260
        if h > 1:
            rrect(d, x, base - h, x + 180, base, 20, fill=col)
        if lt > t0:
            text_c(d, x + 90, base + 50, lab, "Bold", 38, C)
    if lt > 0.6:
        d.line([S(150), S(base), S(930), S(base)], fill=C, width=S(6))
    if lt > 2.0:
        heart(d, 710 + 90, base - 400 - 75 + math.sin(lt * 6) * 6, 90, Y)
    pop_line(d, lt, 2.3, 540, 1250, "MÁS SALUD Y BIENESTAR", 100, GREEN)
    slide_line(d, lt, 2.7, 540, 1370, "es una relación, no prueba que lo cause", 40, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "DE UNA VEZ", 140, C)
    pop_line(d, lt, 0.35, 540, 430, "O EN PARTES", 140, Y)
    days = ["L", "M", "M", "J", "V", "S", "D"]
    for k, dname in enumerate(days):
        q = back(prog(lt, 0.7 + k * 0.12, 0.3))
        if q <= 0.02: continue
        x = 100 + k * 128
        rrect(d, x, 600, x + 110, 600 + 150 * q, 20, fill=K2, outline=GREEN, width=5)
        if q > 0.7:
            text_c(d, x + 55, 640, dname, "Black", 40, C, bg=K2)
            text_c(d, x + 55, 700, "17'", "A", 52, GREEN, bg=K2)
    for k, lab in enumerate(["PARQUE", "BOSQUE", "PLAYA"]):
        pill(d, lt, 1.8 + k * 0.2, 540, 900 + k * 120, 440, lab, fill=GREEN, ink=K, size=46, h=96)
    slide_line(d, lt, 2.5, 540, 1300, "y la mayoría, cerca de su casa", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 320, "HOY:", 140, C)
    slide_line(d, lt, 0.3, 540, 470, "SALÍ 17 MINUTOS", 130, GREEN)
    q = back(prog(lt, 0.6, 0.35))
    if q > 0.02:
        tree(d, 340, 860, 260 * q, sway=math.sin(lt * 2))
        sun(d, 760, 700, 70 * q, lt)
    pop_line(d, lt, 1.4, 540, 1020, "¿CUÁNTO SALISTE", 110, C)
    pop_line(d, lt, 1.6, 540, 1150, "ESTA SEMANA?", 130, Y)
    slide_line(d, lt, 2.0, 540, 1280, "contá en los comentarios", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.3, 540, 1360, "si el bajón no se va, hablá con alguien", 38, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "rustle"); ev(0.2, "pop", -0.2); ev(0.5, "thump"); ev(0.8, "pop", 0.2)
ev(1.2, "rustle", -0.4); ev(1.6, "click"); ev(2.4, "rustle", 0.4); ev(3.2, "shimmer")
ev(4.1, "thump")
for k in range(12): ev(4.2 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(4.4, "swipe")
for k in range(9): ev(4.45 + k * 0.18, "pop", -0.5 + k * 0.12)
ev(6.4, "tap"); ev(6.6, "tap")
ev(8.1, "swipe")
for k in range(16): ev(8.4 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(10.0, "ding"); ev(10.2, "pop"); ev(10.6, "stamp")
ev(12.1, "swipe"); ev(12.3, "thump"); ev(12.6, "tap", -0.4); ev(12.9, "tap", 0); ev(13.6, "pop", 0.4); ev(13.7, "shimmer")
ev(14.0, "pop"); ev(14.3, "thump"); ev(14.7, "tap")
ev(16.1, "pop", -0.2); ev(16.35, "pop", 0.2)
for k in range(7): ev(16.7 + k * 0.12, "pop", -0.5 + k * 0.16)
ev(17.8, "click", -0.3); ev(18.0, "click"); ev(18.2, "click", 0.3); ev(18.5, "tap"); ev(18.7, "rustle")
ev(20.1, "swipe"); ev(20.3, "tap"); ev(20.6, "pop"); ev(20.7, "rustle"); ev(21.4, "pop", -0.2); ev(21.6, "thump"); ev(22.0, "tap"); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
