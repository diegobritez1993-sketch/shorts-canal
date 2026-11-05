"""Short 2026-11-05 15:00 — Mente y emociones: la "brecha del agrado" (liking gap).
Fuente: Boothby, Cooney, Sandstrom y Clark, "The Liking Gap in Conversations", Psychological Science 2018
(Cornell, Harvard, Yale, Univ. de Essex). Charlas de ~5 min entre desconocidos; en otro estudio de 2 a 45 min;
entre compañeros de residencia de primer año (Yale) la brecha duró meses (casi todo el año); los más tímidos la subestiman más.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def two_people(d, t, cx, cy, s, e, gap=260):
    person(d, cx - gap * e, cy, s, C)
    person(d, cx + gap * e, cy, s, Y)

def thought(d, cx, cy, r, col, ink, txt, sz):
    circle(d, cx, cy, r, fill=col)
    circle(d, cx - r * 0.55, cy + r * 1.05, r * 0.16, fill=col)
    circle(d, cx - r * 0.8, cy + r * 1.35, r * 0.09, fill=col)
    text_c(d, cx, cy, txt, "A", sz, ink, bg=col)

def b1(d, t):
    e = back(prog(t, 0.0, 0.45))
    if e > 0.02:
        two_people(d, t, 540, 560, 300 * e, 1.0, gap=220)
        if t > 0.5:
            q = back(prog(t, 0.5, 0.3))
            if q > 0.02:
                thought(d, 330, 260, 90 * q, R, C, "?", int(130 * q))
    pop_line(d, t, 0.2, 540, 900, "DESPUÉS DE CHARLAR", 105, C)
    pop_line(d, t, 0.5, 540, 1050, "¿SENTÍS QUE", 140, C)
    pop_line(d, t, 0.75, 540, 1210, "LE CAÍSTE MAL?", 160, Y)
    sx, sy = shake(t, 2.0, 0.35, 14)
    pop_line(d, t, 1.8, 540 + sx, 1400 + sy, "CASI SEGURO", 100, C)
    pop_line(d, t, 2.0, 540 + sx, 1530 + sy, "TE EQUIVOCÁS", 130, R)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "JUNTARON", 120, C)
    slide_line(d, lt, 0.25, 540, 430, "DESCONOCIDOS", 140, Y)
    slide_line(d, lt, 0.45, 540, 540, "a charlar unos 5 minutos", 48, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        clock(d, 540, 820, 190 * e, ease_in_out(prog(lt, 0.7, 1.3)), turns=1, fill_deg=360)
    pop_line(d, lt, 1.9, 540, 1130, "Y DESPUÉS", 100, C)
    slide_line(d, lt, 2.1, 540, 1250, "cada uno dijo cuánto le gustó el otro...", 42, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1320, "...y cuánto creía que le había gustado", 42, Y, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "LE GUSTASTE", 140, C)
    slide_line(d, lt, 0.3, 540, 430, "MÁS DE LO QUE CREÍAS", 105, Y)
    base = 1180
    # barra izquierda: lo que creías / barra derecha: lo que sintió el otro (ilustrativo, sin cifras)
    a = ease_out(prog(lt, 0.6, 0.9))
    b = ease_out(prog(lt, 0.9, 1.3))
    hL, hR = 260 * a, 520 * b
    rrect(d, 230, base - hL, 470, base, 24, fill=G)
    rrect(d, 610, base - hR, 850, base, 24, fill=Y)
    d.rectangle([S(160), S(base), S(920), S(base + 8)], fill=C)
    slide_line(d, lt, 0.7, 350, base + 60, "lo que creías", 40, C, kind="Bold", dy=20)
    slide_line(d, lt, 1.0, 730, base + 60, "lo que sintió", 40, Y, kind="Bold", dy=20)
    slide_line(d, lt, 1.0, 730, base + 108, "el otro", 40, Y, kind="Bold", dy=20)
    if lt > 2.3:
        hp = back(prog(lt, 2.3, 0.3))
        heart(d, 730, base - hR - 90, 120 * hp, R)
    slide_line(d, lt, 2.6, 540, 1480, "gráfico ilustrativo · Psychological Science, 2018", 32, G, kind="SemiBold", dy=15)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "SE LLAMA", 110, C)
    stamp(d, lt, 0.5, 540, 500, 400, 105, "LIKING GAP", fill=Y, ink=K, size=150)
    slide_line(d, lt, 0.9, 540, 660, "la “brecha del agrado”", 48, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.5, 540, 900, "Y APARECIÓ EN CHARLAS", 90, C)
    sx, sy = shake(lt, 2.2, 0.35, 16)
    pop_line(d, lt, 2.0, 540 + sx, 1080 + sy, "DE 2 A 45 MIN", 170, Y, dur=0.28)
    slide_line(d, lt, 2.6, 540, 1240, "cortas, medianas y largas: igual", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1300, "Cornell, Harvard y Yale", 36, G, kind="SemiBold", dy=20)

def calendar(d, cx, cy, w, h, label, col=C):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 30, fill=K2, outline=col, width=8)
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy - h / 2 + h * 0.26, 30, fill=R)
    d.rectangle([S(cx - w / 2 + 4), S(cy - h / 2 + h * 0.15), S(cx + w / 2 - 4), S(cy - h / 2 + h * 0.26)], fill=R)
    for sx in (-0.25, 0.25):
        rrect(d, cx + w * sx - 12, cy - h / 2 - 30, cx + w * sx + 12, cy - h / 2 + 30, 12, fill=col)
    text_c(d, cx, cy + h * 0.13, label, "A", int(h * 0.42), col, bg=K2)

MESES = ["SEP", "OCT", "NOV", "DIC", "ENE", "FEB", "MAR", "ABR", "MAY"]

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "ENTRE COMPAÑEROS", 110, C)
    slide_line(d, lt, 0.3, 540, 420, "DE RESIDENCIA", 110, C)
    slide_line(d, lt, 0.45, 540, 520, "universitarios de primer año", 44, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        k = min(len(MESES) - 1, int(max(0, lt - 0.9) / 0.15))
        calendar(d, 540, 820, 340 * e, 300 * e, MESES[k])
    sx, sy = shake(lt, 2.4, 0.35, 16)
    pop_line(d, lt, 2.2, 540 + sx, 1120 + sy, "DURÓ MESES", 170, Y, dur=0.28)
    slide_line(d, lt, 2.6, 540, 1270, "y a los más tímidos les pasa más", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "TU MENTE", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "EXAGERA", 170, R)
    slide_line(d, lt, 0.6, 540, 610, "la otra persona la pasó mejor", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 0.75, 540, 670, "de lo que pensás", 46, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.9, 0.4))
    if e > 0.02:
        person(d, 400, 960, 260 * e, C)
        person(d, 680, 960, 260 * e, Y)
        heart(d, 540, 820, 90 * e, R)
    pill(d, lt, 1.7, 540, 1260, 760, "¿TE PASA? SÍ O NO", fill=Y, ink=K, size=52, h=120)
    slide_line(d, lt, 2.0, 540, 1390, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.1, "pop", -0.3); ev(0.2, "tap"); ev(0.5, "pop", 0.3); ev(0.55, "ding", -0.4); ev(0.75, "pop", 0.2)
ev(1.8, "tap"); ev(2.0, "thump")
ev(4.1, "tap", -0.3); ev(4.25, "pop", 0.3); ev(4.45, "tap"); ev(4.4, "pop")
for k in range(10): ev(4.7 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(5.9, "pop"); ev(6.1, "tap", -0.2); ev(6.5, "tap", 0.2)
ev(8.1, "tap"); ev(8.3, "pop")
for k in range(9): ev(8.6 + k * 0.14, "tick", -0.3 if k % 2 else 0.3)
ev(10.3, "ding", 0.4); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.4, "whoosh"); ev(12.5, "stamp"); ev(12.9, "tap")
ev(13.5, "pop"); ev(14.0, "thump"); ev(14.6, "tap"); ev(14.8, "tap", 0.2)
ev(16.1, "tap", -0.3); ev(16.3, "tap", 0.3); ev(16.45, "tap"); ev(16.5, "pop")
for k in range(7): ev(16.9 + k * 0.2, "rustle", 0.2 if k % 2 else -0.2)
ev(18.2, "pop"); ev(18.4, "thump"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "tap"); ev(20.9, "pop"); ev(21.0, "shimmer"); ev(21.7, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
