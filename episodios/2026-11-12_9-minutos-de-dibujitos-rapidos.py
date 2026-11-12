"""Short 2026-11-12 20:00 — Chicos y pantallas: 9 minutos de dibujitos de ritmo rápido y la atención de chicos de 4 años.

Fuente: Lillard y Peterson, Univ. de Virginia, "The Immediate Impact of Different Types of Television on Young Children's
Executive Function", Pediatrics, octubre 2011 (DOI 10.1542/peds.2010-1919). Vía ScienceDaily (12/09/2011) y HealthDay.
- 60 chicos de 4 años, en 3 grupos, 9 minutos cada uno: dibujito animado de ritmo rápido y fantasioso / dibujito lento y
  realista (TV pública) / dibujar con lápices.
- Justo después: 4 pruebas de "funciones ejecutivas" (atención, resolver problemas, seguir reglas, esperar una recompensa;
  ej. torre de Hanoi y postergar un premio).
- Al grupo del dibujito rápido le fue bastante peor que a los otros dos; entre el lento y dibujar, poca diferencia.
  Se mantuvo controlando cuánta TV miraban habitualmente.
- Ojo: solo midieron el efecto inmediato; no se sabe cuánto dura ni si deja algo a largo plazo. "No toda la tele es mala"
  (editorial de D. Christakis). Sugerencias: elegir programas más lentos; dibujar, bloques, juegos de mesa, jugar afuera.
No se nombra ni se dibuja ningún programa ni personaje.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

FLASH = [(255, 59, 48), (10, 132, 255), (255, 214, 10), (191, 90, 242), (52, 199, 89), (255, 105, 180)]

def tv(d, cx, cy, w, t, mode="fast", q=1.0):
    """Tele genérica. mode fast: destellos y formas que saltan; slow: ola suave."""
    if q <= 0.02: return
    w = w * q
    h = w * 0.68
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    # antenas
    d.line([S(cx), S(y0), S(cx - w * 0.2), S(y0 - h * 0.3)], fill=C, width=int(S(max(3, w * 0.02))))
    d.line([S(cx), S(y0), S(cx + w * 0.2), S(y0 - h * 0.3)], fill=C, width=int(S(max(3, w * 0.02))))
    rrect(d, x0, y0, x1, y1, w * 0.08, fill=K2, outline=C, width=max(3, int(w * 0.02)))
    sx0, sy0, sx1, sy1 = x0 + w * 0.07, y0 + h * 0.1, x1 - w * 0.07, y1 - h * 0.1
    if mode == "fast":
        k = int(t * 9)
        rrect(d, sx0, sy0, sx1, sy1, w * 0.04, fill=FLASH[k % len(FLASH)])
        for j in range(4):
            a = (k * 37 + j * 91) % 100 / 100
            b = (k * 53 + j * 29) % 100 / 100
            px = lerp(sx0 + w * 0.1, sx1 - w * 0.1, a)
            py = lerp(sy0 + h * 0.12, sy1 - h * 0.12, b)
            r = w * (0.05 + 0.04 * ((k + j) % 3))
            col = FLASH[(k + j + 2) % len(FLASH)]
            if j % 2:
                circle(d, px, py, r, fill=col)
            else:
                d.polygon([(S(px), S(py - r)), (S(px + r), S(py + r)), (S(px - r), S(py + r))], fill=col)
    else:
        rrect(d, sx0, sy0, sx1, sy1, w * 0.04, fill=(70, 120, 150))
        pts = []
        for i in range(31):
            xx = lerp(sx0, sx1, i / 30)
            pts.append((S(xx), S((sy0 + sy1) / 2 + math.sin(i / 30 * math.tau + t * 1.2) * h * 0.08)))
        pts += [(S(sx1), S(sy1)), (S(sx0), S(sy1))]
        d.polygon(pts, fill=(150, 200, 170))
        circle(d, sx1 - w * 0.15, sy0 + h * 0.18, w * 0.06, fill=Y)

def pencil(d, cx, cy, s, rot, col=Y):
    ca, sa = math.cos(rot), math.sin(rot)
    def P(x, y): return (S(cx + (x * ca - y * sa) * s), S(cy + (x * sa + y * ca) * s))
    d.polygon([P(-0.5, -0.09), P(0.3, -0.09), P(0.3, 0.09), P(-0.5, 0.09)], fill=col)
    d.polygon([P(0.3, -0.09), P(0.5, 0), P(0.3, 0.09)], fill=(230, 200, 160))
    d.polygon([P(0.44, -0.03), P(0.5, 0), P(0.44, 0.03)], fill=K)
    d.polygon([P(-0.5, -0.09), P(-0.6, -0.09), P(-0.6, 0.09), P(-0.5, 0.09)], fill=(255, 140, 160))

def hanoi(d, cx, cy, s, t):
    """Torre de aros (prueba de atención)."""
    rrect(d, cx - s * 0.7, cy + s * 0.32, cx + s * 0.7, cy + s * 0.4, 6, fill=G)
    for k in (-1, 0, 1):
        rrect(d, cx + k * s * 0.45 - 5, cy - s * 0.35, cx + k * s * 0.45 + 5, cy + s * 0.34, 4, fill=G)
    cols = [R, Y, C]
    for j in range(3):
        w = s * (0.36 - j * 0.09)
        yy = cy + s * (0.25 - j * 0.12)
        xx = cx - s * 0.45
        if j == 2:   # el aro de arriba se mueve
            ph = (t * 0.6) % 1.0
            xx = lerp(cx - s * 0.45, cx + s * 0.45, ease_in_out(clamp(ph * 1.5)))
            yy -= math.sin(clamp(ph * 1.5) * math.pi) * s * 0.4
        rrect(d, xx - w / 2, yy - s * 0.05, xx + w / 2, yy + s * 0.05, s * 0.05, fill=cols[j])

def cookie(d, cx, cy, r):
    circle(d, cx, cy, r, fill=(196, 140, 80))
    for a, b in ((-0.3, -0.3), (0.35, -0.1), (-0.1, 0.35), (0.25, 0.4), (-0.45, 0.15)):
        circle(d, cx + a * r, cy + b * r, r * 0.12, fill=(80, 50, 30))

def b1(d, t):
    tv(d, 540, 560, 520, t, "fast", back(prog(t, 0.0, 0.4)))
    pop_line(d, t, 0.1, 540, 960, "9 MINUTOS", 170, Y)
    pop_line(d, t, 0.4, 540, 1125, "DE DIBUJITOS", 140, C)
    pop_line(d, t, 0.65, 540, 1265, "RÁPIDOS...", 140, C)
    pill(d, t, 1.7, 540, 1430, 640, "¿Y DESPUÉS QUÉ PASA?", fill=R, ink=C, size=44, h=96)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "60 CHICOS", 140, Y)
    slide_line(d, lt, 0.3, 540, 415, "DE 4 AÑOS", 120, C)
    slide_line(d, lt, 0.5, 540, 505, "en 3 grupos", 46, C, kind="SemiBold", dy=25)
    xs = [210, 540, 870]
    labs = [("RÁPIDO", "dibujito movido"), ("LENTO", "dibujito tranquilo"), ("DIBUJAR", "con lápices")]
    for k in range(3):
        q = back(prog(lt, 0.8 + k * 0.3, 0.35))
        x = xs[k]
        if k == 0: tv(d, x, 720, 260, lt, "fast", q)
        elif k == 1: tv(d, x, 720, 260, lt, "slow", q)
        elif q > 0.02:
            rrect(d, x - 115 * q, 720 - 95 * q, x + 115 * q, 720 + 95 * q, 14, fill=C)
            # garabato que se dibuja
            n = int(24 * prog(lt, 1.6, 1.5))
            pts = [(S(x - 80 + i * 6.6), S(720 + math.sin(i * 0.9) * 40)) for i in range(n + 1)]
            if len(pts) > 1: d.line(pts, fill=R, width=S(8), joint="curve")
            pencil(d, x + 70, 690 + math.sin(lt * 8) * 8, 170 * q, -0.8)
        pill(d, lt, 1.1 + k * 0.3, x, 900, 280, labs[k][0], fill=R if k == 0 else K2, ink=C, size=40, h=80)
        slide_line(d, lt, 1.3 + k * 0.3, x, 980, labs[k][1], 34, C, kind="SemiBold", dy=20)
    p = prog(lt, 2.2, 1.6)
    if lt > 2.0:
        clock(d, 540, 1230, 120, p, turns=1, fill_deg=54 * 1)
        text_c(d, 540, 1405, f"{int(9 * p)} MIN", "A", 70, Y)
    slide_line(d, lt, 2.4, 540, 1480, "Lillard y Peterson, Univ. de Virginia, Pediatrics 2011", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 290, "JUSTO DESPUÉS:", 120, C)
    slide_line(d, lt, 0.4, 540, 400, "juegos de atención y paciencia", 46, Y, kind="Bold", dy=25)
    q = back(prog(lt, 0.7, 0.35))
    if q > 0.02:
        hanoi(d, 300, 700, 360 * q, max(0, lt - 1.0))
    slide_line(d, lt, 1.0, 300, 900, "armar una torre", 38, C, kind="SemiBold", dy=20)
    q2 = back(prog(lt, 1.3, 0.35))
    if q2 > 0.02:
        cookie(d, 780, 680, 100 * q2)
        clock(d, 880, 590, 50 * q2, prog(lt, 1.5, 2.0), turns=2, fill_deg=180)
    slide_line(d, lt, 1.6, 780, 900, "esperar un premio", 38, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.3, 540, 1100, "seguir reglas, recordar,", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.45, 540, 1170, "frenar un impulso", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.8, 540, 1310, 620, "FUNCIONES EJECUTIVAS", fill=Y, ink=K, size=42, h=90)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO", 140, C)
    base = 1000
    bars = [(230, R, 210, "rápido"), (540, (110, 110, 110), 430, "lento"), (850, (110, 110, 110), 450, "dibujar")]
    for k, (x, col, hh, lab) in enumerate(bars):
        h = hh * ease_out(prog(lt, 0.5 + k * 0.25, 0.7))
        if h > 1:
            rrect(d, x - 110, base - h, x + 110, base, 18, fill=col)
        if lt > 0.5:
            text_c(d, x, base + 50, lab, "SemiBold", 40, C)
    if lt > 0.5:
        d.line([S(90), S(base), S(990), S(base)], fill=C, width=S(6))
    slide_line(d, lt, 0.6, 540, 470, "puntaje en las pruebas (ilustrativo)", 32, G, kind="SemiBold", dy=15)
    sx, sy = shake(lt, 2.0, 0.35, 14)
    stamp(d, lt, 1.95, 540 + sx, 1220 + sy, 400, 100, "LES FUE PEOR", fill=R, ink=C, size=120)
    slide_line(d, lt, 2.5, 540, 1380, "a los del dibujito rápido", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1450, "lento y dibujar: casi igual", 46, Y, kind="Bold", dy=25)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 300, "PERO OJO:", 140, Y)
    q = back(prog(lt, 0.4, 0.35))
    if q > 0.02:
        warning(d, 540, 590, 260 * q, rot=math.sin(lt * 5) * 0.06)
    slide_line(d, lt, 0.9, 540, 840, "midieron solo el efecto", 50, C, kind="Bold", dy=25)
    slide_line(d, lt, 1.05, 540, 910, "inmediato", 50, C, kind="Bold", dy=25)
    slide_line(d, lt, 1.5, 540, 1010, "no se sabe cuánto dura", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.3, 540, 1170, 760, "NO TODA LA TELE ES MALA", fill=K2, ink=C, size=42, h=96)
    slide_line(d, lt, 2.6, 540, 1270, "el ritmo importa", 46, Y, kind="Bold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL CONSEJO:", 120, Y)
    slide_line(d, lt, 0.35, 540, 420, "antes de la escuela o la tarea,", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 0.5, 540, 485, "algo lento: dibujar, bloques, jugar afuera", 40, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.3, 540, 760, "¿QUÉ DIBUJITOS", 130, C)
    pop_line(d, lt, 1.55, 540, 900, "MIRA EL TUYO?", 140, Y)
    slide_line(d, lt, 2.0, 540, 1040, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)
    q = back(prog(lt, 2.2, 0.35))
    if q > 0.02:
        bubble(d, 540, 1230, 170 * q, Y)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.1, "stamp")
for k in range(9): ev(0.3 + k * 0.11, "click", -0.5 + k * 0.12)
ev(0.4, "pop", -0.2); ev(0.65, "pop", 0.2); ev(1.7, "click"); ev(1.75, "pop")
ev(4.1, "swipe"); ev(4.3, "swipe"); ev(4.5, "tap")
for k in range(3): ev(4.8 + k * 0.3, "pop", -0.5 + k * 0.5); ev(5.1 + k * 0.3, "click", -0.5 + k * 0.5)
ev(5.6, "rustle")
for k in range(9): ev(6.2 + k * 0.18, "tick", 0.0)
ev(8.1, "pop"); ev(8.4, "swipe"); ev(8.7, "pop", -0.4); ev(9.0, "tap", -0.4); ev(9.3, "pop", 0.4); ev(9.6, "tap", 0.4)
ev(10.3, "tap"); ev(10.45, "tap"); ev(10.8, "click")
ev(12.1, "swipe")
for k in range(3): ev(12.5 + k * 0.25, "tick", -0.5 + k * 0.5)
ev(13.95, "stamp"); ev(14.5, "tap"); ev(14.7, "tap")
ev(16.1, "pop"); ev(16.4, "thump"); ev(16.9, "tap"); ev(17.05, "tap"); ev(17.5, "tap"); ev(18.3, "click"); ev(18.6, "tap")
ev(20.1, "swipe"); ev(20.35, "tap"); ev(20.5, "tap"); ev(21.3, "pop"); ev(21.55, "thump"); ev(22.0, "tap"); ev(22.2, "pop")

if __name__ == "__main__":
    main(BEATS_EP)
