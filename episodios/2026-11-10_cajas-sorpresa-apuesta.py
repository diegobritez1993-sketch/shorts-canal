"""Short 2026-11-10 15:00 — Cómo te enganchan las apps: cajas sorpresa (loot boxes).

Fuentes:
- Comisión de Juego de Bélgica (abril 2018): las loot boxes de Overwatch, FIFA 18 y CS:GO son "juego de azar" ilegal;
  multas de hasta 800.000 € y hasta 5 años de prisión, penas que se duplican si hay menores (INQUIRER.net 26/04/2018).
- Zendle y Cairns, PLOS ONE 2018: encuesta a 7.422 jugadores; cuanto más gastaban en cajas, más severos sus problemas
  con el juego (relación, no causa).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

BROWN = (150, 90, 40)
PURPLE = (170, 90, 255)

def chest(d, cx, cy, w, open_p=0.0, wob=0.0, glow=0.0, t=0.0):
    """Cofre/caja sorpresa dibujado con primitivas. open_p 0..1 levanta la tapa."""
    ang = math.sin(t * 40) * 0.06 * wob
    ox = math.sin(t * 40) * 14 * wob
    h = w * 0.62
    x0, x1 = cx - w / 2 + ox, cx + w / 2 + ox
    if glow > 0:
        for k in range(5, 0, -1):
            circle(d, cx + ox, cy - h * 0.2, w * 0.35 + k * 40 * glow, fill=mix(K, Y, 0.06 * (6 - k) * glow))
        for k in range(12):
            a = k / 12 * math.tau + t * 0.6
            r0, r1 = w * 0.55, w * (0.75 + 0.35 * glow)
            d.line([S(cx + ox + math.cos(a) * r0), S(cy - h * 0.2 + math.sin(a) * r0),
                    S(cx + ox + math.cos(a) * r1), S(cy - h * 0.2 + math.sin(a) * r1)], fill=mix(K, Y, glow), width=S(10))
    # cuerpo
    rrect(d, x0, cy - h * 0.15, x1, cy + h * 0.5, 22, fill=BROWN, outline=C, width=8)
    d.rectangle([S(x0 + 8), S(cy + h * 0.05), S(x1 - 8), S(cy + h * 0.13)], fill=Y)
    # tapa
    lift = h * 0.55 * ease_out(open_p)
    ty = cy - h * 0.15 - lift
    rrect(d, x0 - 10 + ang * 200, ty - h * 0.38, x1 + 10 + ang * 200, ty, 40, fill=BROWN, outline=C, width=8)
    d.rectangle([S(x0 - 2 + ang * 200), S(ty - h * 0.12), S(x1 + 2 + ang * 200), S(ty - h * 0.04)], fill=Y)
    # cerradura
    rrect(d, cx - 34 + ox, cy - h * 0.18, cx + 34 + ox, cy + h * 0.02, 10, fill=Y)
    circle(d, cx + ox, cy - h * 0.1, 10, fill=K)

def coin(d, cx, cy, r):
    circle(d, cx, cy, r, fill=Y, outline=(200, 160, 0), width=6)
    text_c(d, cx, cy + 2, "$", "Black", int(r * 1.1), K, bg=Y)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        chest(d, 540, 640, 420 * e, wob=1.0 if (t % 1.2) < 0.35 else 0.0, t=t)
        for k, (qx, qy) in enumerate([(300, 380), (790, 360), (840, 560)]):
            pop_line(d, t, 0.3 + k * 0.15, qx, qy + math.sin(t * 3 + k) * 12, "?", 110, Y)
    pop_line(d, t, 0.4, 540, 1020, "¿ABRÍS CAJAS", 140, C)
    pop_line(d, t, 0.7, 540, 1170, "SORPRESA", 160, Y)
    pop_line(d, t, 1.0, 540, 1310, "EN LOS JUEGOS?", 120, C)
    pill(d, t, 1.7, 540, 1480, 560, "OJO CON ESTO", fill=R, ink=C, size=48, h=100)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "PAGÁS PLATA REAL", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "SIN SABER QUÉ TE TOCA", 100, Y)
    # moneda que cae en el cofre
    cp = prog(lt, 0.6, 0.6)
    if 0 < cp < 1:
        coin(d, 540, lerp(520, 820, ease_in_out(cp)), 60)
    op = prog(lt, 1.3, 0.5)
    chest(d, 540, 1000, 400, open_p=op, glow=ease_out(prog(lt, 1.4, 0.5)), t=lt)
    # premio al azar: rueda de opciones que gira y para en algo común
    items = ["ÉPICO", "COMÚN", "RARO", "COMÚN", "LEGENDARIO", "COMÚN"]
    rp = prog(lt, 1.6, 1.4)
    if rp > 0:
        idx = int(ease_out(rp) * 17) % len(items)
        if rp >= 1: idx = 1
        col = Y if rp < 1 else C
        rrect(d, 240, 545, 840, 665, 40, fill=K2, outline=col, width=6)
        text_c(d, 540, 603, items[idx], "A", 80, col, bg=K2)
    slide_line(d, lt, 3.0, 540, 1500, "el premio lo decide el azar", 46, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 330, "EN 2018", 150, C)
    pop_line(d, lt, 0.4, 540, 490, "BÉLGICA DIJO:", 130, Y)
    for k, g in enumerate(["OVERWATCH", "FIFA 18", "CS:GO"]):
        pill(d, lt, 0.8 + k * 0.2, 540, 700 + k * 130, 520, g, fill=K2, ink=C, size=46, h=100)
    stamp(d, lt, 1.9, 540, 1180, 440, 120, "ES APUESTA", fill=R, ink=C, size=150)
    slide_line(d, lt, 2.4, 540, 1380, "juego de azar ilegal", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1450, "Comisión de Juego de Bélgica, abril 2018", 36, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "MULTAS DE HASTA", 120, C)
    n = 800000 * ease_out(prog(lt, 0.4, 1.4))
    sx, sy = shake(lt, 1.8, 0.35, 16)
    pop_line(d, lt, 0.4, 540 + sx, 500 + sy, fmt_num(n) + " €", 170, Y, dur=0.25)
    # balanza de pena: barra que se duplica
    e = ease_out(prog(lt, 2.0, 0.4))
    if e > 0:
        rrect(d, 140, 760, 140 + 380 * e, 860, 30, fill=K2)
        text_l(d, 170, 810, "PENA", "Black", 44, C)
    e2 = ease_out(prog(lt, 2.5, 0.5))
    if e2 > 0:
        rrect(d, 140, 920, 140 + 800 * e2, 1020, 30, fill=R)
        if e2 > 0.6: text_l(d, 170, 970, "PENA x2", "Black", 44, C)
    slide_line(d, lt, 2.7, 540, 1150, "SI HAY MENORES", 130, R)
    slide_line(d, lt, 3.0, 540, 1290, "y hasta 5 años de cárcel", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 3.1, 540, 1360, "INQUIRER.net, 26/04/2018", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 300, "7.422 JUGADORES", 130, C)
    slide_line(d, lt, 0.4, 540, 420, "y un patrón:", 50, C, kind="SemiBold", dy=25)
    # barras crecientes: gasto en cajas vs problemas con el juego
    base = 1050
    for k in range(4):
        hh = (120 + k * 120) * ease_out(prog(lt, 0.7 + k * 0.25, 0.35))
        if hh > 1:
            x = 230 + k * 175
            rrect(d, x, base - hh, x + 130, base, 18, fill=mix(Y, R, k / 3))
    if lt > 0.6:
        d.line([S(180), S(base), S(900), S(base)], fill=C, width=S(6))
        text_c(d, 540, base + 45, "más gasto en cajas →", "SemiBold", 38, G)
    pop_line(d, lt, 1.9, 540, 1220, "MÁS PROBLEMAS", 130, R)
    pop_line(d, lt, 2.1, 540, 1360, "CON EL JUEGO", 130, C)
    slide_line(d, lt, 2.6, 540, 1490, "relación, no causa · Zendle y Cairns, PLOS ONE 2018", 34, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 140, C)
    slide_line(d, lt, 0.3, 540, 480, "PONÉ UN TOPE", 140, Y)
    q = ease_in_out(prog(lt, 0.8, 0.3))
    if lt > 0.6:
        toggle_row(d, 110, 640, "Compras en el juego", q, sub="con contraseña" if q > 0.5 else "sin control")
    pop_line(d, lt, 1.6, 540, 1000, "¿ALGUNA VEZ", 120, C)
    pop_line(d, lt, 1.8, 540, 1140, "PAGASTE UNA?", 130, Y)
    slide_line(d, lt, 2.2, 540, 1280, "contá en los comentarios: sí o no", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.3, "pop", -0.4); ev(0.45, "pop", 0.4); ev(0.6, "pop", 0.3)
ev(0.4, "pop", -0.2); ev(0.7, "thump"); ev(1.0, "pop", 0.2); ev(1.7, "click"); ev(1.2, "rustle"); ev(2.4, "rustle")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3); ev(4.6, "whoosh"); ev(5.2, "ding"); ev(5.3, "rustle"); ev(5.4, "shimmer")
for k in range(14): ev(5.6 + k * 0.09 + k * k * 0.004, "tick", 0.3 if k % 2 else -0.3)
ev(7.0, "thump"); ev(7.0, "tap")
ev(8.1, "pop"); ev(8.4, "pop"); ev(8.8, "click", -0.3); ev(9.0, "click"); ev(9.2, "click", 0.3)
ev(9.9, "stamp"); ev(10.4, "tap"); ev(10.6, "tap")
ev(12.1, "tap")
for k in range(12): ev(12.4 + k * 0.11, "tick", 0.3 if k % 2 else -0.3)
ev(13.8, "thump"); ev(14.0, "swipe"); ev(14.5, "swipe"); ev(14.7, "stamp"); ev(15.0, "tap"); ev(15.1, "tap")
ev(16.1, "pop"); ev(16.4, "tap")
for k in range(4): ev(16.7 + k * 0.25, "pop", -0.4 + k * 0.27)
ev(17.9, "thump"); ev(18.1, "pop"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.8, "toggle"); ev(21.6, "pop", -0.2); ev(21.8, "thump"); ev(22.2, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
