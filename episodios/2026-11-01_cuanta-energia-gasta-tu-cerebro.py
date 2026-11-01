"""Short 2026-11-01 20:00 — Curiosidades y hábitos: cuánta energía gasta tu cerebro.
Fuentes: NIH Record (2007) sobre Marcus Raichle (Washington Univ.): el cerebro es ~2% del peso corporal
y consume ~20% de la energía del cuerpo; los cambios por una tarea son "menos del 10%" de su gasto,
la actividad intrínseca (en reposo) más del 50%. Raichle y Gusnard, PNAS 2002.
Mito del 10%: BrainFacts.org (Society for Neuroscience), 2019.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

PINK = (255, 140, 170)

def brain(d, cx, cy, s, col=PINK, ink=K):
    """Cerebro estilizado: lóbulos con círculos + surcos."""
    r = s * 0.22
    for dx, dy in [(-0.25, -0.12), (0.0, -0.2), (0.25, -0.12), (-0.3, 0.1), (-0.08, 0.06), (0.15, 0.06), (0.32, 0.1)]:
        circle(d, cx + dx * s, cy + dy * s, r, fill=col)
    d.ellipse([S(cx - s * 0.12), S(cy + s * 0.12), S(cx + s * 0.18), S(cy + s * 0.36)], fill=col)  # tronco/cerebelo
    w = max(2, int(S(s * 0.025)))
    d.line([S(cx), S(cy - s * 0.38), S(cx), S(cy + s * 0.12)], fill=ink, width=w)
    for a0, x, y in [(200, -0.2, -0.1), (330, 0.2, -0.1), (180, -0.25, 0.12), (0, 0.25, 0.12)]:
        rr = s * 0.11
        d.arc([S(cx + x * s - rr), S(cy + y * s - rr), S(cx + x * s + rr), S(cy + y * s + rr)], a0, a0 + 150, fill=ink, width=w)

def body(d, cx, top, h, col):
    """Silueta humana simple de pie."""
    s = h
    circle(d, cx, top + s * 0.07, s * 0.07, fill=col)
    rrect(d, cx - s * 0.13, top + s * 0.16, cx + s * 0.13, top + s * 0.55, s * 0.05, fill=col)
    rrect(d, cx - s * 0.2, top + s * 0.17, cx - s * 0.145, top + s * 0.5, s * 0.03, fill=col)
    rrect(d, cx + s * 0.145, top + s * 0.17, cx + s * 0.2, top + s * 0.5, s * 0.03, fill=col)
    rrect(d, cx - s * 0.12, top + s * 0.54, cx - s * 0.02, top + s, s * 0.04, fill=col)
    rrect(d, cx + s * 0.02, top + s * 0.54, cx + s * 0.12, top + s, s * 0.04, fill=col)

def scale_bar(d, x0, y, w, frac, col, label, lt, t0):
    p = ease_in_out(prog(lt, t0, 0.9))
    rrect(d, x0, y, x0 + w, y + 90, 45, fill=K2)
    if p * frac > 0.01:
        rrect(d, x0, y, x0 + max(90, w * frac * p), y + 90, 45, fill=col)
    text_l(d, x0, y - 45, label, "Bold", 42, C)

def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 330, "¿CUÁNTA ENERGÍA", 130, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 480, "GASTA TU CEREBRO?", 130, Y, dur=0.25)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        pulse = 1 + 0.04 * math.sin(lt * 6)
        brain(d, 540, 940, 520 * e * pulse)
        # rayos de energía alrededor
        for k in range(8):
            a = k / 8 * math.tau + lt * 0.6
            q = prog(lt, 0.9 + k * 0.08, 0.2)
            if q > 0:
                r0, r1 = 330, 330 + 70 * q
                d.line([S(540 + math.cos(a) * r0), S(940 + math.sin(a) * r0), S(540 + math.cos(a) * r1), S(940 + math.sin(a) * r1)], fill=Y, width=S(14))
    slide_line(d, lt, 1.8, 540, 1370, "te vas a sorprender", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "PESA APENAS", 120, C)
    pop_line(d, lt, 0.3, 540, 450, "EL 2%", 200, Y)
    slide_line(d, lt, 0.5, 540, 580, "de tu cuerpo", 50, C, kind="SemiBold", dy=25)
    e = ease_out(prog(lt, 0.6, 0.4))
    if e > 0:
        body(d, 540, 700, 780, mix(K, (70, 70, 70), e))
        z = back(prog(lt, 1.3, 0.4))
        if z > 0.02:
            brain(d, 540, 755, 110 * z)
            # flecha y lupa: el cerebro "chiquito"
            q = ease_out(prog(lt, 1.8, 0.4))
            if q > 0:
                d.line([S(620), S(740), S(620 + 190 * q), S(680)], fill=Y, width=S(8))
                if q > 0.9: pill(d, lt, 2.2, 880, 640, 280, "CHIQUITO", fill=Y, ink=K, size=40, h=80)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "PERO SE COME", 120, C)
    n = 20 * ease_out(prog(lt, 0.6, 1.4))
    sx, sy = shake(lt, 2.0, 0.35, 16)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        donut(d, 540 + sx, 820 + sy, 330 * e, n / 100, f"{int(round(n))}%", col=Y)
    slide_line(d, lt, 2.0, 540, 1250, "DE TU ENERGÍA", 120, Y)
    slide_line(d, lt, 2.3, 540, 1370, "NIH Record, 2007 (Raichle, Washington Univ.)", 32, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "O SEA", 110, C)
    pop_line(d, lt, 0.3, 540, 440, "1 DE CADA 5", 170, Y)
    slide_line(d, lt, 0.5, 540, 570, "calorías que gastás se van ahí", 46, C, kind="SemiBold", dy=25)
    # 5 baterías/pilas: una se la lleva el cerebro
    for k in range(5):
        y = 740 + k * 140
        e = back(prog(lt, 0.7 + k * 0.12, 0.3))
        if e > 0.5:
            is_b = k == 2
            mv = ease_in_out(prog(lt, 1.9, 0.6)) if is_b else 0
            x = 540 + 160 * mv
            battery(d, x - 60, y, 300 * e, 100 * e, 1.0, Y if is_b else (90, 90, 90))
            if is_b and mv > 0.3:
                brain(d, 250, y, 150 * back(clamp((mv - 0.3) / 0.7)))

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y LA MAYOR PARTE", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "LA GASTA EN REPOSO", 110, Y)
    scale_bar(d, 110, 640, 860, 0.6, Y, "actividad de fondo: más del 50%", lt, 0.7)
    scale_bar(d, 110, 860, 860, 0.1, R, "pensar en una tarea: menos del 10%", lt, 1.3)
    slide_line(d, lt, 2.1, 540, 1110, "nunca está \"apagado\"", 56, C, kind="Bold", dy=25)
    slide_line(d, lt, 2.3, 540, 1190, "ni cuando estás sin hacer nada", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1260, "Raichle, NIH Record 2007", 32, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "¿EL MITO DEL 10%?", 120, C)
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        brain(d, 540, 700, 360 * e)
    stamp(d, lt, 0.9, 540, 1020, 240, 110, "FALSO", fill=R, ink=C, size=170)
    slide_line(d, lt, 1.5, 540, 1230, "lo usás todo, todo el tiempo", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.7, 540, 1300, "¿vos te lo creías? comentá", 46, Y, kind="Bold", dy=25)
    slide_line(d, lt, 1.9, 540, 1365, "BrainFacts.org (Society for Neuroscience)", 30, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.4, "thump")
for k in range(8): ev(0.9 + k * 0.08, "tick", -0.4 + k * 0.1)
ev(1.8, "tap")
ev(4.1, "tap"); ev(4.3, "thump"); ev(4.5, "tap"); ev(4.6, "swipe"); ev(5.3, "pop"); ev(5.8, "whoosh", 0.4); ev(6.2, "pop", 0.4)
ev(8.1, "tap"); ev(8.4, "pop")
for k in range(14): ev(8.6 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(10.0, "stamp"); ev(10.3, "tap")
ev(12.1, "tap"); ev(12.3, "thump"); ev(12.5, "tap")
for k in range(5): ev(12.7 + k * 0.12, "click", -0.3 + k * 0.15)
ev(13.9, "swipe", -0.4); ev(14.2, "pop", -0.5)
ev(16.1, "tap"); ev(16.3, "tap")
for k in range(8): ev(16.7 + k * 0.1, "tick", -0.2)
ev(17.3, "buzz"); ev(18.1, "pop"); ev(18.3, "tap")
ev(20.05, "pop"); ev(20.3, "pop"); ev(20.7, "whoosh"); ev(20.9, "stamp"); ev(21.5, "tap"); ev(21.7, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
