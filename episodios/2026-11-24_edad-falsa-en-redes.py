"""Short 2026-11-24 20:00 — ¿Tu hijo tiene 18 en sus redes? (edad falsa, Ofcom 2022)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def id_card(d, cx, cy, w, h, age_txt, age_col=Y):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 36, fill=K2, outline=C, width=6)
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy - h / 2 + h * 0.2, 36, fill=Y)
    d.rectangle([S(cx - w / 2), S(cy - h / 2 + h * 0.12), S(cx + w / 2), S(cy - h / 2 + h * 0.2)], fill=Y)
    text_c(d, cx, cy - h / 2 + h * 0.1, "PERFIL", "Black", int(h * 0.09) + 1, K, bg=Y)
    px = cx - w * 0.27
    rrect(d, px - w * 0.15, cy - h * 0.18, px + w * 0.15, cy + h * 0.36, 20, fill=(50, 50, 50))
    person(d, px, cy + h * 0.1, w * 0.26, C)
    text_l(d, cx - w * 0.02, cy - h * 0.06, "EDAD", "Bold", int(h * 0.08) + 1, G)
    text_l(d, cx - w * 0.02, cy + h * 0.16, age_txt, "A", int(h * 0.26) + 1, age_col)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        id_card(d, 540, 620, 620 * e, 400 * e, "18")
    stamp(d, t, 1.6, 800, 470, 120, 60, "¿18?", fill=R, ink=C, size=80)
    pop_line(d, t, 0.2, 540, 1030, "¿TU HIJO TIENE", 135, C)
    pop_line(d, t, 0.5, 540, 1180, "18 EN SUS REDES?", 135, Y)
    slide_line(d, t, 1.3, 540, 1320, "aunque tenga 10", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "LAS REDES PIDEN", 120, C)
    slide_line(d, lt, 0.3, 540, 430, "13 AÑOS MÍNIMO", 135, Y)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        circle(d, 540, 780, 200 * e, outline=Y, width=16)
        text_c(d, 540, 780, "13", "A", int(220 * e) + 1, C)
    # el número cambia de año: se escribe otra fecha
    p = prog(lt, 1.6, 0.6)
    if p > 0:
        x0 = 220
        rrect(d, x0, 1080, 1080 - x0, 1200, 30, fill=K2, outline=G, width=4)
        full = "01/01/2000"
        n = int(len(full) * p)
        text_c(d, 540, 1140, full[:n] + ("|" if int(lt * 4) % 2 else ""), "Bold", 64, C, bg=K2)
    slide_line(d, lt, 2.4, 540, 1290, "pero alcanza con poner", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.55, 540, 1350, "una fecha de nacimiento falsa", 48, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "EN REINO UNIDO", 110, C)
    sx, sy = shake(lt, 0.55, 0.35, 16)
    pop_line(d, lt, 0.3, 540 + sx, 450 + sy, "1 DE CADA 3", 190, Y, dur=0.28)
    for i in range(3):
        e = back(prog(lt, 0.8 + i * 0.25, 0.35))
        if e > 0.02:
            x = 270 + i * 270
            red = (i == 1 and lt > 1.9)
            person(d, x, 830, 300 * e, R if red else C)
            if red:
                pill(d, lt, 1.9, x, 1040, 200, "18+", fill=R, ink=C, size=50, h=90)
    slide_line(d, lt, 2.2, 540, 1170, "chicos de 8 a 17 con redes", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1235, "tiene una edad de adulto", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1320, "Fuente: Ofcom (Reino Unido), oct. 2022", 36, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "Y LA APP", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "LO TRATA COMO", 120, C)
    pop_line(d, lt, 0.6, 540, 590, "ADULTO", 190, R)
    # escudo que se rompe
    e = back(prog(lt, 0.9, 0.4))
    if e > 0.02:
        cx, cy, s = 540, 920, 210 * e
        crack = ease_out(prog(lt, 1.8, 0.4)) * 50
        for side in (-1, 1):
            off = side * crack
            pts = [(cx + off, cy - s), (cx + off + side * s * 0.8, cy - s * 0.7), (cx + off + side * s * 0.75, cy + s * 0.1),
                   (cx + off, cy + s), (cx + off + side * s * 0.05, cy + s * 0.2), (cx + off - side * s * 0.08, cy - s * 0.3)]
            d.polygon([(S(x), S(y)) for x, y in pts], fill=GREEN if crack < 10 else mix(GREEN, (70, 70, 70), 0.6))
    slide_line(d, lt, 2.2, 540, 1220, "con menos protecciones", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1285, "pensadas para menores", 50, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "¿Y QUIÉN", 130, C)
    slide_line(d, lt, 0.3, 540, 450, "LOS AYUDÓ?", 150, Y)
    e1 = back(prog(lt, 0.6, 0.4)); e2 = back(prog(lt, 0.8, 0.4))
    if e1 > 0.02: person(d, 400, 850, 420 * e1, C)
    if e2 > 0.02: person(d, 640, 900, 260 * e2, Y)
    if lt > 1.0:
        phone(d, 520, 960, 90, 160, buzz=0.6 if 1.0 < lt < 1.6 else 0.0, t=lt)
    sx, sy = shake(lt, 1.85, 0.35, 14)
    pop_line(d, lt, 1.6, 540 + sx, 1180 + sy, "MUCHAS VECES", 110, C, dur=0.28)
    pop_line(d, lt, 1.8, 540 + sx, 1320 + sy, "LOS PADRES", 150, R, dur=0.28)
    slide_line(d, lt, 2.4, 540, 1450, "sobre todo con los de 8 a 12 años", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL CONSEJO:", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "SU EDAD REAL", 160, Y)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        id_card(d, 540, 820, 560 * e, 360 * e, "10", age_col=GREEN)
    slide_line(d, lt, 1.4, 540, 1100, "si le armás la cuenta,", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.55, 540, 1165, "poné su edad verdadera", 50, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.0, 540, 1310, 820, "Y REVISEN JUNTOS LA PRIVACIDAD", fill=Y, ink=K, size=38, h=100)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.2, "pop", -0.3); ev(0.5, "thump"); ev(1.3, "tap"); ev(1.45, "whoosh"); ev(1.6, "stamp")
ev(4.1, "tap"); ev(4.3, "pop"); ev(4.4, "thump")
for k in range(10): ev(5.6 + k * 0.06, "click", 0.3 if k % 2 else -0.3)
ev(6.4, "tap"); ev(6.55, "tap")
ev(8.1, "tap"); ev(8.3, "thump"); ev(8.55, "stamp"); ev(8.8, "pop", -0.5); ev(9.05, "pop"); ev(9.3, "pop", 0.5); ev(9.9, "ding"); ev(10.2, "tap"); ev(10.35, "tap")
ev(12.1, "tap"); ev(12.3, "tap"); ev(12.6, "thump"); ev(12.9, "pop"); ev(13.8, "stamp"); ev(14.2, "tap"); ev(14.35, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.6, "pop", -0.3); ev(16.8, "pop", 0.3); ev(17.0, "buzz"); ev(17.6, "pop"); ev(17.8, "thump"); ev(18.4, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "pop"); ev(21.0, "shimmer"); ev(21.4, "tap"); ev(21.55, "tap"); ev(22.0, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
