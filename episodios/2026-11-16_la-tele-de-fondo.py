"""Short 2026-11-16 20:00 — Chicos y pantallas.
La tele prendida de fondo: ~3,9 h por día (menores de 2: 5,5 h) y los padres hablan ~20% menos.
Fuentes: Lapierre, Piotrowski y Linebarger, Pediatrics 2012 (vía Journalist's Resource);
Kirkorian et al., Univ. de Massachusetts, Child Development 2009 (comunicado EurekAlert 15/09/2009).
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def tv(d, cx, cy, w, h, t, on=1.0, glow=(70, 120, 230)):
    """Tele con estática. on 0..1 (0 = apagada, se cierra a una línea)."""
    # patas
    d.line([S(cx - w * 0.25), S(cy + h / 2), S(cx - w * 0.35), S(cy + h / 2 + 60)], fill=C, width=S(12))
    d.line([S(cx + w * 0.25), S(cy + h / 2), S(cx + w * 0.35), S(cy + h / 2 + 60)], fill=C, width=S(12))
    # antenas
    d.line([S(cx), S(cy - h / 2), S(cx - w * 0.22), S(cy - h / 2 - 110)], fill=C, width=S(10))
    d.line([S(cx), S(cy - h / 2), S(cx + w * 0.22), S(cy - h / 2 - 110)], fill=C, width=S(10))
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 40, fill=K2, outline=C, width=10)
    sx0, sy0, sx1, sy1 = cx - w / 2 + 40, cy - h / 2 + 40, cx + w / 2 - 40, cy + h / 2 - 40
    hh = (sy1 - sy0) * on
    if on > 0.02:
        mid = (sy0 + sy1) / 2
        rrect(d, sx0, mid - hh / 2, sx1, mid + hh / 2, 20, fill=mix(K, glow, 0.8))
        rnd = random.Random(int(t * 15))
        for k in range(int(70 * on)):
            x, y = rnd.uniform(sx0 + 10, sx1 - 20), rnd.uniform(mid - hh / 2 + 6, mid + hh / 2 - 12)
            v = rnd.uniform(0.3, 1)
            d.rectangle([S(x), S(y), S(x + 14), S(y + 6)], fill=mix(K, C, v * on))
    else:
        mid = (sy0 + sy1) / 2
        d.line([S(cx - 30), S(mid), S(cx + 30), S(mid)], fill=C, width=S(4))

def kid(d, cx, cy, s, col):
    circle(d, cx, cy - s * 0.32, s * 0.2, fill=col)
    rrect(d, cx - s * 0.22, cy - s * 0.08, cx + s * 0.22, cy + s * 0.35, s * 0.1, fill=col)
    # bloques de juguete
    rrect(d, cx + s * 0.35, cy + s * 0.15, cx + s * 0.55, cy + s * 0.35, 6, fill=Y)
    rrect(d, cx + s * 0.45, cy - s * 0.05, cx + s * 0.62, cy + s * 0.13, 6, fill=R)

def b1(d, t):
    tv(d, 540, 1350, 520, 360, t, on=back(prog(t, 0.0, 0.4)))
    pop_line(d, t, 0.0, 540, 480, "¿EN TU CASA", 160, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 660, "LA TELE QUEDA", 160, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 840, "PRENDIDA?", 175, Y, dur=0.25)
    slide_line(d, t, 1.4, 540, 1000, "aunque nadie la mire...", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "UN CHICO PROMEDIO", 120, C)
    slide_line(d, lt, 0.3, 540, 410, "en EE.UU. la tiene de fondo", 50, C, kind="SemiBold", dy=25)
    v = 3.9 * ease_out(prog(lt, 0.6, 1.4))
    if lt > 0.6:
        sx, sy = shake(lt, 2.0, 0.35, 14)
        text_c(d, 540 + sx, 720 + sy, f"{v:.1f}".replace(".", ","), "A", 380, Y)
        pop_line(d, lt, 1.9, 540, 1010, "HORAS POR DÍA", 130, C)
    slide_line(d, lt, 2.5, 540, 1160, "casi 1.500 familias, chicos de 8 meses a 8 años", 38, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.7, 540, 1220, "Lapierre y otros, Pediatrics 2012", 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "Y LOS MÁS CHIQUITOS,", 105, C)
    slide_line(d, lt, 0.3, 540, 410, "MÁS TODAVÍA", 120, R)
    base = 1350
    bars = [("MENORES DE 2", 5.5, R, 330), ("6 A 8 AÑOS", 2.7, (110, 110, 110), 750)]
    for k, (lab, val, col, x) in enumerate(bars):
        p = ease_out(prog(lt, 0.6 + k * 0.5, 0.9))
        if p <= 0: continue
        hgt = 100 * val * p
        rrect(d, x - 130, base - hgt, x + 130, base, 24, fill=col)
        text_c(d, x, base - hgt - 70, f"{val * p:.1f} H".replace(".", ","), "A", 110, C)
        text_c(d, x, base + 60, lab, "Black", 40, C)
    slide_line(d, lt, 2.4, 540, 1515, "horas de tele de fondo por día", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1580, "Lapierre y otros, Pediatrics 2012", 36, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "EN UN EXPERIMENTO", 115, C)
    slide_line(d, lt, 0.3, 540, 400, "padres jugando con su hijo, con la tele prendida", 38, C, kind="SemiBold", dy=20)
    # 10 globitos de charla: 2 se apagan
    off = ease_in_out(prog(lt, 1.4, 0.6))
    for k in range(10):
        p = prog(lt, 0.5 + k * 0.07, 0.25)
        if p <= 0: continue
        i, j = k % 5, k // 5
        x, y = 160 + i * 190, 600 + j * 200
        col = Y if k < 8 else mix(Y, (60, 60, 60), off)
        bubble(d, x, y, 150 * back(p), col)
    sx, sy = shake(lt, 2.1, 0.35, 16)
    pop_line(d, lt, 1.9, 540 + sx, 1060 + sy, "HABLARON", 120, C, dur=0.25)
    pop_line(d, lt, 2.05, 540 + sx, 1210 + sy, "20% MENOS", 190, R, dur=0.25)
    slide_line(d, lt, 2.4, 540, 1350, "menos tiempo hablándole a su hijo", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1415, "Kirkorian y otros, Univ. de Massachusetts, 2009", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y NO SOLO", 120, C)
    slide_line(d, lt, 0.3, 540, 410, "MENOS CHARLA:", 120, C)
    pill(d, t, 16.8, 540, 600, 760, "MENOS ATENTOS", fill=K2, ink=Y, size=52, h=120)
    pill(d, t, 17.2, 540, 760, 760, "MENOS RESPUESTAS", fill=K2, ink=Y, size=52, h=120)
    pill(d, t, 17.6, 540, 920, 760, "MENOS ACTIVOS", fill=K2, ink=Y, size=52, h=120)
    e = back(prog(lt, 1.0, 0.4))
    if e > 0.02:
        kid(d, 470, 1240, 260 * e, C)
    stamp(d, lt, 2.4, 540, 1480, 380, 85, "Y ELLOS APRENDEN HABLANDO", fill=Y, ink=K, size=58)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "SI NADIE MIRA,", 130, Y)
    slide_line(d, lt, 0.45, 540, 620, "APAGALA", 160, Y)
    if lt > 0.5:
        on = 1 - ease_in_out(prog(lt, 1.1, 0.3))
        tv(d, 540, 960, 380, 260, lt, on=on)
    slide_line(d, lt, 1.6, 540, 1230, "y nada de tele en el cuarto de los chicos", 42, C, kind="SemiBold", dy=20)
    pop_line(d, lt, 2.1, 540, 1380, "¿EN TU CASA QUEDA PRENDIDA?", 80, C)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.1, "rustle"); ev(0.25, "pop", 0.3); ev(0.5, "thump"); ev(1.4, "tap")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(11): ev(4.6 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(6.0, "stamp"); ev(5.9, "pop"); ev(6.5, "tap"); ev(6.7, "tap")
ev(8.1, "tap"); ev(8.3, "thump"); ev(8.6, "whoosh"); ev(9.1, "whoosh"); ev(10.4, "tap")
ev(12.1, "tap"); ev(12.3, "tap")
for k in range(10): ev(12.5 + k * 0.07, "pop", -0.5 + k * 0.1)
ev(13.5, "click"); ev(13.9, "pop"); ev(14.05, "stamp"); ev(14.6, "tap")
ev(16.1, "tap"); ev(16.3, "tap"); ev(16.8, "pop", -0.3); ev(17.2, "pop", 0.3); ev(17.6, "pop", -0.3)
ev(17.0, "pop"); ev(18.2, "stamp")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "thump"); ev(21.1, "click"); ev(21.15, "toggle"); ev(21.6, "tap"); ev(22.1, "pop")

if __name__ == "__main__":
    main(BEATS_EP)
