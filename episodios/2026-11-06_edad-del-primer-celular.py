"""Short 2026-11-06 20:00 — Chicos y pantallas: edad del primer smartphone y salud mental de adultos jóvenes.
Fuente: Sapien Labs, informe "Age of First Smartphone/Tablet and Mental Wellbeing Outcomes" (mayo 2023), Global Mind
Project: 27.969 jóvenes de 18 a 24 años de decenas de países (ene-abr 2023). Mujeres con su primer smartphone a los 6:
74% con dificultades de salud mental; a los 18: 46%. Varones: 42% vs 36%. "El bienestar fue consistentemente mayor
cuanto más tarde empezó la tenencia del smartphone". Autorreporte, sin revisión de pares (vía Scripps News/WPTV, 15/05/2023).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def cake(d, cx, cy, s, n, t):
    """Torta con n velitas."""
    rrect(d, cx - s * 0.5, cy - s * 0.1, cx + s * 0.5, cy + s * 0.3, 18, fill=C)
    rrect(d, cx - s * 0.5, cy - s * 0.1, cx + s * 0.5, cy + s * 0.0, 18, fill=R)
    for k in range(n):
        x = cx + (k - (n - 1) / 2) * s * 0.075
        d.rectangle([S(x - s * 0.025), S(cy - s * 0.3), S(x + s * 0.025), S(cy - s * 0.1)], fill=Y)
        fl = 1 + 0.15 * math.sin(t * 18 + k)
        circle(d, x, cy - s * 0.36, s * 0.035 * fl, fill=(255, 150, 30))

def age_slider(d, cx, cy, w, age, col=Y):
    x0, x1 = cx - w / 2, cx + w / 2
    rrect(d, x0, cy - 14, x1, cy + 14, 14, fill=(60, 60, 60))
    p = (age - 6) / 12
    rrect(d, x0, cy - 14, x0 + max(28, w * p), cy + 14, 14, fill=col)
    circle(d, x0 + w * p, cy, 44, fill=C)
    text_c(d, x0 + w * p, cy, str(int(round(age))), "A", 48, K, bg=C)
    text_c(d, x0, cy + 85, "6 años", "SemiBold", 36, G)
    text_c(d, x1, cy + 85, "18 años", "SemiBold", 36, G)

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        phone(d, 540, 520, 260 * e, 470 * e, buzz=clamp(1 - t * 0.6), t=t)
        if e > 0.8:
            text_c(d, 540, 520, "?", "A", 220, Y, bg=K2)
    pop_line(d, t, 0.15, 540, 920, "¿A QUÉ EDAD", 165, C)
    sx, sy = shake(t, 0.8, 0.35, 16)
    pop_line(d, t, 0.6, 540 + sx, 1100 + sy, "EL PRIMER CELU?", 150, Y, dur=0.28)
    slide_line(d, t, 1.5, 540, 1260, "un estudio con casi 28.000 jóvenes", 48, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.2, 540, 1340, "encontró algo que preocupa", 48, R, kind="Bold", dy=25)

def b2(d, t):
    lt = t - 4
    # multitud de personitas
    cols = 9
    for k in range(cols * 4):
        p = back(prog(lt, 0.1 + k * 0.03, 0.25))
        if p <= 0.02: continue
        x = 540 + (k % cols - (cols - 1) / 2) * 105
        y = 330 + (k // cols) * 125
        person(d, x, y, 90 * p, Y if k % 7 == 3 else C)
    n = int(27969 * ease_out(prog(lt, 0.4, 1.4)))
    pop_line(d, lt, 0.4, 540, 900, fmt_num(n), 190, Y)
    slide_line(d, lt, 0.7, 540, 1095, "JÓVENES DE 18 A 24", 110, C)
    slide_line(d, lt, 1.6, 540, 1200, "de decenas de países", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.9, 540, 1275, "Sapien Labs, Global Mind Project, 2023", 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "LES PREGUNTARON", 130, C)
    slide_line(d, lt, 0.3, 540, 420, "a qué edad tuvieron su primer smartphone", 42, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        cake(d, 540, 700, 420 * e, 6 if lt < 1.6 else 9 if lt < 2.2 else 12, lt)
    age = 6 + 12 * ease_in_out(prog(lt, 1.0, 1.8))
    if lt > 0.8:
        age_slider(d, 540, 1000, 760, age)
    pop_line(d, lt, 2.4, 540, 1250, "Y CÓMO ESTÁN HOY", 120, Y)

def compare(d, lt, title, a, b, col_a, col_b):
    slide_line(d, lt, 0.1, 540, 290, title, 150, C)
    slide_line(d, lt, 0.3, 540, 400, "con dificultades de salud mental", 44, C, kind="SemiBold", dy=25)
    fa = (a / 100) * ease_out(prog(lt, 0.5, 1.0))
    fb = (b / 100) * ease_out(prog(lt, 1.0, 1.0))
    if lt > 0.4:
        donut(d, 300, 700, 200 * back(prog(lt, 0.4, 0.3)), fa, f"{int(round(fa * 100))}%", col_a)
        text_c(d, 300, 950, "CELU A LOS 6", "Black", 42, col_a)
    if lt > 0.9:
        donut(d, 780, 700, 200 * back(prog(lt, 0.9, 0.3)), fb, f"{int(round(fb * 100))}%", col_b)
        text_c(d, 780, 950, "CELU A LOS 18", "Black", 42, col_b)

def b4(d, t):
    lt = t - 12
    compare(d, lt, "MUJERES", 74, 46, R, GREEN)
    stamp(d, lt, 2.3, 540, 1180, 440, 90, "28 PUNTOS MENOS", fill=Y, ink=K, size=105)
    slide_line(d, lt, 2.7, 540, 1330, "Sapien Labs, 2023 · encuesta autorreportada", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    compare(d, lt, "VARONES", 42, 36, R, GREEN)
    pop_line(d, lt, 2.1, 540, 1150, "MÁS TARDE, MEJOR", 130, Y)
    slide_line(d, lt, 2.4, 540, 1270, "el bienestar subía cuanto más tarde", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1340, "muestra una relación, no prueba la causa", 34, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "NO HAY APURO", 150, Y)
    slide_line(d, lt, 0.4, 540, 420, "esperar un poco más puede ayudar", 48, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        # calendario que pasa hojas
        rrect(d, 540 - 170 * e, 520, 540 + 170 * e, 520 + 300 * e, 30, fill=C)
        rrect(d, 540 - 170 * e, 520, 540 + 170 * e, 520 + 80 * e, 30, fill=R)
        d.rectangle([S(540 - 170 * e), S(520 + 40 * e), S(540 + 170 * e), S(520 + 80 * e)], fill=R)
        if e > 0.8:
            yr = 6 + min(7, int(max(0, lt - 0.9) * 6))
            text_c(d, 540, 735, str(yr), "A", 170, K, bg=C)
            text_c(d, 540, 560, "AÑOS", "Black", 40, C, bg=R)
    pill(d, lt, 1.6, 540, 990, 990, "¿A QUÉ EDAD TUVISTE EL TUYO?", fill=Y, ink=K, size=42, h=130)
    slide_line(d, lt, 2.0, 540, 1120, "dejalo en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "buzz"); ev(0.05, "pop"); ev(0.15, "pop", -0.3); ev(0.6, "whoosh"); ev(0.8, "stamp"); ev(1.5, "tap"); ev(2.2, "tap", 0.3)
for k in range(12): ev(4.1 + k * 0.09, "pop", -0.6 + (k % 9) * 0.15)
for k in range(10): ev(4.4 + k * 0.13, "tick", 0.2 if k % 2 else -0.2)
ev(4.7, "tap"); ev(5.6, "tap"); ev(5.9, "click")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.5, "pop"); ev(8.6, "shimmer")
for k in range(12): ev(9.0 + k * 0.15, "tick", -0.4 + k * 0.07)
ev(10.4, "pop"); ev(10.4, "thump")
for base in (12.0, 16.0):
    ev(base + 0.1, "tap"); ev(base + 0.3, "tap"); ev(base + 0.4, "pop", -0.4); ev(base + 0.9, "pop", 0.4)
    for k in range(8): ev(base + 0.5 + k * 0.12, "tick", -0.3 if k % 2 else 0.3)
ev(14.1, "whoosh"); ev(14.3, "stamp"); ev(14.7, "tap")
ev(18.1, "pop"); ev(18.1, "thump"); ev(18.4, "tap"); ev(18.6, "tap")
ev(20.1, "pop"); ev(20.4, "tap"); ev(20.6, "pop")
for k in range(7): ev(20.95 + k / 6, "rustle", 0.2 if k % 2 else -0.2)
ev(21.6, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
