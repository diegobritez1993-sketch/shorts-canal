"""Short 2026-11-21 20:00 — Mente y emociones.
Mente que divaga: 46,9% del tiempo pensando en otra cosa, y eso nos hace menos felices.
Fuente: Killingsworth y Gilbert, Harvard, "A Wandering Mind Is an Unhappy Mind", Science 2010
(Harvard Gazette 11/11/2010; ScienceDaily 12/11/2010).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

BLUE = (90, 160, 255)

def cloud(d, cx, cy, s, col):
    """Nube de pensamiento."""
    for dx, dy, r in [(-0.32, 0.05, 0.26), (-0.1, -0.12, 0.3), (0.18, -0.08, 0.28), (0.36, 0.08, 0.22), (0.05, 0.12, 0.3)]:
        circle(d, cx + dx * s, cy + dy * s, r * s, fill=col)

def face(d, cx, cy, r, mood):
    """mood 1 = sonrisa, 0 = boca plana/triste."""
    circle(d, cx, cy, r, fill=mix(K2, Y, 0.25 + 0.75 * mood), outline=C, width=8)
    circle(d, cx - r * 0.35, cy - r * 0.2, r * 0.09, fill=K)
    circle(d, cx + r * 0.35, cy - r * 0.2, r * 0.09, fill=K)
    pts = []
    for i in range(21):
        x = -0.45 + 0.9 * i / 20
        y = 0.3 + (0.25 - (x / 0.45) ** 2 * 0.25) * (mood * 2 - 0.6)
        pts.append((S(cx + x * r), S(cy + y * r)))
    d.line(pts, fill=K, width=S(12), joint="curve")

def b1(d, t):
    # persona con una nube de pensamiento que se escapa como globo
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        person(d, 380, 760, 300 * e, C)
        fl = ease_in_out(prog(t, 0.8, 2.6))
        bx, by = 640 + fl * 220, 470 - fl * 160 + math.sin(t * 3) * 12
        d.line([S(410), S(640), S(bx - 40), S(by + 70)], fill=G, width=S(5))
        cloud(d, bx, by, 300 * e, BLUE)
        text_c(d, bx, by, "?", "A", 110, K, bg=BLUE)
    pop_line(d, t, 0.0, 540, 1100, "¿DÓNDE ESTÁ", 150, C)
    pop_line(d, t, 0.25, 540, 1260, "TU CABEZA", 150, Y)
    pop_line(d, t, 0.45, 540, 1420, "AHORA MISMO?", 150, Y)
    slide_line(d, t, 1.6, 540, 1570, "seguro no del todo acá", 46, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "UNA APP LES PREGUNTABA", 96, C)
    slide_line(d, lt, 0.25, 540, 410, "EN MOMENTOS AL AZAR", 100, Y)
    e = back(prog(lt, 0.3, 0.4))
    bz = 1.0 if 0.8 < lt < 1.6 else 0.0
    if e > 0.02:
        phone(d, 540, 820, 300 * e, 520 * e, buzz=bz, t=lt)
    p = prog(lt, 1.0, 0.3)
    if p > 0:
        sc = back(p)
        rrect(d, 540 - 230 * sc, 700 - 70 * sc, 540 + 230 * sc, 700 + 70 * sc, 30, fill=C)
        if p > 0.6:
            text_c(d, 540, 680, "¿EN QUÉ", "Black", 40, K, bg=C)
            text_c(d, 540, 725, "ESTÁS PENSANDO?", "Black", 40, K, bg=C)
    pop_line(d, lt, 1.8, 540, 1200, "2.250 PERSONAS", 130, C)
    slide_line(d, lt, 2.1, 540, 1320, "de 18 a 88 años, con una app en el celu", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.3, 540, 1385, "Killingsworth y Gilbert, Harvard, Science 2010", 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "SU MENTE ESTABA", 110, C)
    slide_line(d, lt, 0.25, 540, 420, "EN OTRA COSA EL", 110, C)
    p = ease_out(prog(lt, 0.5, 1.3))
    val = 46.9 * p
    sx, sy = shake(lt, 1.8, 0.35, 16)
    if lt > 0.45:
        txt = f"{val:.1f}%".replace(".", ",")
        text_c(d, 540 + sx, 680 + sy, txt, "A", 290, Y)
    slide_line(d, lt, 1.9, 540, 870, "del tiempo despiertos", 50, C, kind="SemiBold", dy=25)
    # barra de un día: mitad "acá", mitad "en otro lado"
    q = ease_in_out(prog(lt, 1.2, 1.0))
    x0, x1, y0, y1 = 140, 940, 1000, 1110
    rrect(d, x0, y0, x1, y1, 55, fill=K2)
    if q > 0.02:
        rrect(d, x0, y0, x0 + (x1 - x0) * 0.469 * q, y1, 55, fill=BLUE)
    if q > 0.9:
        text_c(d, 330, 1055, "EN OTRO LADO", "Black", 34, K, bg=BLUE)
        text_c(d, 730, 1055, "ACÁ", "Black", 34, C, bg=K2)
    pop_line(d, lt, 2.5, 540, 1260, "CASI LA MITAD", 130, C)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "Y CON LA CABEZA", 110, C)
    slide_line(d, lt, 0.25, 540, 410, "EN OTRO LADO...", 110, C)
    e = back(prog(lt, 0.3, 0.4))
    mood = 1 - ease_in_out(prog(lt, 1.0, 1.0))
    if e > 0.02:
        face(d, 540, 740, 210 * e, mood)
        if lt > 1.0:
            cloud(d, 810, 600, 150 * clamp((lt - 1.0) * 3), BLUE)
    sx, sy = shake(lt, 2.1, 0.35, 16)
    pop_line(d, lt, 1.9, 540 + sx, 1080 + sy, "ERAN MENOS", 150, C, dur=0.28)
    pop_line(d, lt, 2.05, 540 + sx, 1240 + sy, "FELICES", 190, R, dur=0.28)
    slide_line(d, lt, 2.6, 540, 1390, "lo dicen los autores: \"una mente que divaga", 40, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1445, "es una mente infeliz\"", 40, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "PESÓ MÁS DÓNDE", 110, C)
    slide_line(d, lt, 0.25, 540, 410, "ESTABA TU MENTE", 110, Y)
    slide_line(d, lt, 0.4, 540, 520, "que lo que estabas haciendo", 48, C, kind="SemiBold", dy=25)
    # balanza que se inclina hacia "MENTE"
    e = ease_out(prog(lt, 0.4, 0.4))
    if e > 0.02:
        tilt = 0.28 * ease_in_out(prog(lt, 1.0, 0.8)) + math.sin(lt * 6) * 0.015 * prog(lt, 1.0, 0.8)
        cx, cy, L = 540, 760, 300
        d.polygon([(S(cx), S(cy)), (S(cx - 70), S(cy + 430)), (S(cx + 70), S(cy + 430))], fill=K2)
        lx, ly = cx - math.cos(tilt) * L, cy + math.sin(tilt) * L
        rx, ry = cx + math.cos(tilt) * L, cy - math.sin(tilt) * L
        d.line([S(lx), S(ly), S(rx), S(ry)], fill=C, width=S(16))
        circle(d, cx, cy, 22, fill=C)
        for (x, y, lab, col, w) in [(lx, ly, "MENTE", BLUE, 250), (rx, ry, "LO QUE HACÉS", G, 300)]:
            d.line([S(x), S(y), S(x), S(y + 120)], fill=C, width=S(6))
            rrect(d, x - w / 2, y + 120, x + w / 2, y + 200, 24, fill=col)
            text_c(d, x, y + 160, lab, "Black", 30 if len(lab) > 6 else 44, K if col == BLUE else C, bg=col)
    pill(d, lt, 2.0, 540, 1330, 700, "MÁS DEL DOBLE", fill=Y, ink=K, size=56, h=120)
    slide_line(d, lt, 2.4, 540, 1460, "a la hora de explicar cómo se sentían", 44, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "PROBÁ ESTO:", 120, C)
    slide_line(d, lt, 0.3, 540, 480, "VOLVÉ AL AHORA", 140, Y)
    # tres "anclas": ojos / oído / respiración en círculos que se encienden
    for i, lab in enumerate(["MIRÁ", "ESCUCHÁ", "RESPIRÁ"]):
        p = back(prog(lt, 0.6 + i * 0.25, 0.3))
        if p > 0.02:
            x = 230 + i * 310
            circle(d, x, 760, 115 * p, fill=[BLUE, Y, C][i])
            text_c(d, x, 760, lab, "Black", int(36 * p) + 1, K, bg=[BLUE, Y, C][i])
    slide_line(d, lt, 1.4, 540, 960, "3 cosas que ves, 1 sonido, 1 respiración", 44, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.7, 540, 1150, "¿EN QUÉ PENSABAS", 110, C)
    pop_line(d, lt, 1.9, 540, 1280, "HACE UN RATO?", 110, Y)
    slide_line(d, lt, 2.3, 540, 1420, "si los pensamientos te pesan seguido,", 38, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.4, 540, 1470, "hablalo con alguien", 38, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.05, "shimmer"); ev(0.25, "pop", 0.3); ev(0.45, "thump"); ev(1.0, "whoosh", 0.5); ev(1.6, "tap")
ev(4.1, "tap", -0.3); ev(4.25, "tap", 0.3); ev(4.4, "pop"); ev(4.8, "buzz"); ev(5.0, "ding"); ev(5.8, "thump"); ev(6.1, "tap"); ev(6.3, "tap", 0.2)
ev(8.1, "tap"); ev(8.25, "tap")
for k in range(10): ev(8.5 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(9.8, "stamp"); ev(9.9, "tap"); ev(10.5, "pop")
ev(12.1, "tap"); ev(12.25, "tap"); ev(12.3, "pop"); ev(13.0, "shimmer"); ev(13.9, "pop"); ev(14.05, "thump"); ev(14.6, "tap"); ev(14.7, "tap")
ev(16.1, "tap"); ev(16.25, "tap"); ev(16.4, "tap"); ev(16.5, "pop")
for k in range(4): ev(17.0 + k * 0.2, "click", -0.3 if k % 2 else 0.3)
ev(17.8, "thump"); ev(18.0, "pop"); ev(18.4, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "pop", -0.5); ev(20.85, "pop"); ev(21.1, "pop", 0.5); ev(21.4, "tap"); ev(21.7, "pop"); ev(21.9, "thump"); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
