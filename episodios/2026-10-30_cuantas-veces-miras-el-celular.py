"""Short: ¿Cuántas veces mirás el celular por día?
Fuente: Reviews.org, encuesta Q4 2025 (~1.000 adultos de EE.UU., vía Pollfish), publicada dic 2025.
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

TAPS = [0.25, 0.75, 1.35, 1.9]

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        phone(d, 540, 520, 230 * e, 410 * e)
        for t0 in TAPS:           # anillos de toque
            p = prog(t, t0, 0.5)
            if 0 < p < 1:
                circle(d, 540, 560, 40 + 140 * ease_out(p), outline=mix(K, Y, 1 - p), width=8)
        # contador loco en la pantalla
        n = random.Random(int(t * 12)).randint(1, 999) if t < 2.4 else None
        text_c(d, 540, 560, str(n) if n else "?", "A", 120, Y if n is None else C, bg=K2)
    pop_line(d, t, 0.5, 540, 960, "¿CUÁNTAS VECES", 145, C)
    pop_line(d, t, 0.8, 540, 1125, "MIRÁS EL CELULAR", 125, C)
    pop_line(d, t, 1.1, 540, 1280, "POR DÍA?", 165, Y)
    pill(d, t, 2.6, 540, 1460, 660, "LA RESPUESTA ASUSTA", size=42)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "UNA PERSONA PROMEDIO", 100, C)
    slide_line(d, lt, 0.3, 540, 420, "LO REVISA", 100, C)
    n = 186 * ease_out(prog(lt, 0.5, 1.8))
    sx, sy = shake(lt, 2.3, 0.35, 18)
    if lt > 0.5:
        text_c(d, 540 + sx, 800 + sy, str(int(n)), "A", 420, Y)
    pop_line(d, lt, 2.3, 540, 1110, "VECES AL DÍA", 140, C)
    slide_line(d, lt, 2.7, 540, 1250, "encuesta a adultos de EE.UU.", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.85, 540, 1310, "Reviews.org, 2025", 38, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "ESO ES MÁS O MENOS", 100, C)
    pop_line(d, lt, 0.3, 540, 440, "UNA VEZ CADA", 130, C)
    e = back(prog(lt, 0.4, 0.4))
    cx, cy, r = 540, 820, 230
    if e > 0.02:
        rr = r * e
        circle(d, cx, cy, rr, fill=K2, outline=C, width=10)
        # 12 marcas = 12 x 5 minutos; se encienden una por una
        lit = int(clamp((lt - 0.8) / 2.0) * 12)
        for k in range(12):
            a = -math.pi / 2 + k / 12 * math.tau
            col = Y if k < lit else (70, 70, 70)
            circle(d, cx + math.cos(a) * rr * 0.78, cy + math.sin(a) * rr * 0.78, 18 * e, fill=col)
        ang = -math.pi / 2 + lit / 12 * math.tau
        d.line([S(cx), S(cy), S(cx + math.cos(ang) * rr * 0.6), S(cy + math.sin(ang) * rr * 0.6)], fill=Y, width=S(12))
        circle(d, cx, cy, 16, fill=Y)
    sx, sy = shake(lt, 2.3, 0.35, 16)
    pop_line(d, lt, 2.2, 540 + sx, 1190 + sy, "5 MINUTOS", 200, Y, dur=0.28)
    slide_line(d, lt, 2.7, 540, 1340, "durante todo el día que estás despierto", 42, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "Y APENAS", 120, C)
    slide_line(d, lt, 0.3, 540, 430, "TE DESPERTÁS...", 120, C)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        frac = 0.85 * ease_in_out(prog(lt, 0.8, 1.2))
        donut(d, 540, 790, 230 * e, frac, f"{int(round(frac * 100))}%")
    pop_line(d, lt, 2.1, 540, 1130, "LO MIRA EN LOS", 100, C)
    pop_line(d, lt, 2.3, 540, 1260, "PRIMEROS 10 MIN", 135, Y)
    slide_line(d, lt, 2.8, 540, 1390, "después de despertarse", 44, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "Y CUANDO LA BATERÍA", 100, C)
    slide_line(d, lt, 0.3, 540, 420, "BAJA DEL 20%...", 120, R)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        lvl = 0.9 - 0.72 * ease_in_out(prog(lt, 0.7, 1.3))
        col = GREEN if lvl > 0.5 else (Y if lvl > 0.2 else R)
        battery(d, 520, 760, 480 * e, 230 * e, lvl, col)
        pct = int(lvl * 100)
        if lt > 2.0 and int(lt * 4) % 2 == 0:
            text_c(d, 520, 762, f"{pct}%", "A", 90, C)
    pop_line(d, lt, 2.1, 540, 1090, "MÁS DE 4 DE CADA 10", 110, C)
    pop_line(d, lt, 2.35, 540, 1230, "SIENTEN ANSIEDAD", 140, Y)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 420, "¿Y VOS?", 190, Y)
    slide_line(d, lt, 0.35, 540, 590, "CONTÁ CUÁNTAS", 130, C)
    slide_line(d, lt, 0.5, 540, 730, "VECES HOY", 130, C)
    # palitos de conteo (de a 5)
    for k in range(12):
        tk = 0.9 + k * 0.13
        p = prog(lt, tk, 0.12)
        if p <= 0: continue
        grp, i = divmod(k, 5)
        gx = 300 + grp * 230
        if i < 4:
            x = gx + i * 36
            d.line([S(x), S(900), S(x), S(lerp(900, 1030, ease_out(p)))], fill=C, width=S(12))
        else:
            d.line([S(gx - 20), S(1010), S(lerp(gx - 20, gx + 128, ease_out(p))), S(lerp(1010, 920, ease_out(p)))], fill=Y, width=S(12))
    slide_line(d, lt, 2.0, 540, 1150, "y dejalo en los comentarios", 48, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
for t0 in TAPS: ev(t0, "tap", 0.2)
ev(0.5, "pop", -0.3); ev(0.8, "pop", 0.3); ev(1.1, "thump"); ev(2.6, "pop")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(16): ev(4.5 + k * 0.11, "tick", 0.35 if k % 2 else -0.35)
ev(6.3, "stamp"); ev(6.7, "tap")
ev(8.1, "tap", -0.3); ev(8.3, "pop"); ev(8.4, "pop", 0.2)
for k in range(12): ev(8.8 + k * 2.0 / 12, "click", 0.3 if k % 2 else -0.3)
ev(10.2, "thump"); ev(10.7, "tap")
ev(12.1, "tap", -0.3); ev(12.3, "tap", 0.3); ev(12.4, "ding")
for k in range(9): ev(12.8 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(14.1, "pop"); ev(14.3, "thump"); ev(14.8, "tap")
ev(16.1, "tap"); ev(16.3, "pop")
for k in range(8): ev(16.7 + k * 0.16, "tick", 0.2 if k % 2 else -0.2)
ev(18.0, "buzz"); ev(18.1, "pop", -0.2); ev(18.35, "thump")
ev(20.1, "pop"); ev(20.35, "tap", -0.2); ev(20.5, "tap", 0.2)
for k in range(12): ev(20.9 + k * 0.13, "click", 0.3 if k % 2 else -0.3)
ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
