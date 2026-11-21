"""Short 2026-11-21 15:00 — Curiosidades y hábitos.
¿Una canción pegada en la cabeza? Gusano musical (earworm).
Fuentes: Jakubowski et al., Psychology of Aesthetics, Creativity and the Arts 2016 (comunicado APA 03/11/2016);
Beaman et al., Univ. de Reading, Quarterly J. Exp. Psychology 2015 (comunicado Univ. de Reading 22/04/2015).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

PINK = (255, 105, 180)

def note(d, cx, cy, s, col, double=False):
    """Nota musical con primitivas."""
    if double:
        circle(d, cx - s * 0.45, cy, s * 0.22, fill=col)
        circle(d, cx + s * 0.45, cy - s * 0.15, s * 0.22, fill=col)
        d.line([S(cx - s * 0.27), S(cy), S(cx - s * 0.27), S(cy - s * 0.9)], fill=col, width=int(S(max(4, s * 0.1))))
        d.line([S(cx + s * 0.63), S(cy - s * 0.15), S(cx + s * 0.63), S(cy - s * 1.05)], fill=col, width=int(S(max(4, s * 0.1))))
        d.polygon([(S(cx - s * 0.32), S(cy - s * 0.95)), (S(cx + s * 0.68), S(cy - s * 1.1)), (S(cx + s * 0.68), S(cy - s * 0.88)), (S(cx - s * 0.32), S(cy - s * 0.73))], fill=col)
    else:
        circle(d, cx, cy, s * 0.24, fill=col)
        d.line([S(cx + s * 0.19), S(cy), S(cx + s * 0.19), S(cy - s * 0.95)], fill=col, width=int(S(max(4, s * 0.1))))
        d.polygon([(S(cx + s * 0.15), S(cy - s * 0.97)), (S(cx + s * 0.55), S(cy - s * 0.6)), (S(cx + s * 0.5), S(cy - s * 0.48)), (S(cx + s * 0.15), S(cy - s * 0.75))], fill=col)

def head(d, cx, cy, s, col=C, fill=K2):
    """Cabeza de perfil simple (mirando a la derecha)."""
    circle(d, cx, cy, s * 0.5, fill=fill, outline=col, width=10)
    d.polygon([(S(cx + s * 0.42), S(cy + s * 0.05)), (S(cx + s * 0.62), S(cy + s * 0.22)), (S(cx + s * 0.4), S(cy + s * 0.3))], fill=col)
    rrect(d, cx - s * 0.12, cy + s * 0.47, cx + s * 0.1, cy + s * 0.68, 10, fill=col)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        head(d, 540, 640, 420 * e)
        # notas dando vueltas dentro de la cabeza
        for k in range(4):
            a = t * 2.2 + k * math.tau / 4
            note(d, 520 + math.cos(a) * 110 * e, 620 + math.sin(a) * 90 * e, 70 * e, Y, double=(k % 2 == 0))
    pop_line(d, t, 0.0, 540, 1120, "¿TENÉS UNA CANCIÓN", 120, C)
    pop_line(d, t, 0.25, 540, 1270, "PEGADA EN", 150, Y)
    pop_line(d, t, 0.45, 540, 1420, "LA CABEZA?", 150, Y)
    slide_line(d, t, 1.6, 540, 1570, "no es casualidad: tiene explicación", 44, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "SE LLAMA", 110, C)
    pop_line(d, lt, 0.3, 540, 450, "GUSANO MUSICAL", 150, Y)
    slide_line(d, lt, 0.6, 540, 570, "en inglés, \"earworm\"", 46, C, kind="SemiBold", dy=25)
    # gusano hecho de notas que avanza
    e = ease_out(prog(lt, 0.4, 0.5))
    for k in range(7):
        x = 230 + k * 95 + (lt * 40) % 95 * 0
        y = 860 + math.sin(lt * 5 - k * 0.9) * 45
        if e > k / 7:
            circle(d, x, y, 55 if k < 6 else 70, fill=mix(Y, PINK, k / 8) if k < 6 else Y)
    if e > 0.95:
        circle(d, 230 + 6 * 95 + 18, 860 + math.sin(lt * 5 - 6 * 0.9) * 45 - 18, 12, fill=K)
    pop_line(d, lt, 1.6, 540, 1110, "3.000 PERSONAS", 130, C)
    slide_line(d, lt, 1.9, 540, 1230, "contaron cuál se les pega más", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1300, "Jakubowski et al., APA 2016", 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "LAS QUE MÁS", 120, C)
    slide_line(d, lt, 0.25, 540, 420, "SE PEGAN TIENEN:", 120, Y)
    # contorno de melodía que sube y baja
    pts = [(160, 760), (300, 690), (440, 620), (580, 600), (720, 650), (860, 720), (940, 770)]
    p = ease_in_out(prog(lt, 0.4, 1.2))
    n = p * (len(pts) - 1)
    for i in range(len(pts) - 1):
        if n > i:
            q = min(1.0, n - i)
            x0, y0 = pts[i]; x1, y1 = pts[i + 1]
            d.line([S(x0), S(y0), S(lerp(x0, x1, q)), S(lerp(y0, y1, q))], fill=G, width=S(10))
    for i, (x, y) in enumerate(pts):
        if n >= i - 0.01:
            note(d, x, y, 60, Y if i != 3 else PINK)
    pill(d, lt, 1.4, 540, 960, 760, "1. RITMO MÁS RÁPIDO", fill=Y, ink=K, size=50, h=120)
    pill(d, lt, 1.9, 540, 1120, 760, "2. MELODÍA SIMPLE", fill=C, ink=K, size=50, h=120)
    pill(d, lt, 2.4, 540, 1280, 760, "3. UN SALTO RARO", fill=PINK, ink=K, size=50, h=120)
    slide_line(d, lt, 2.7, 540, 1410, "fácil de recordar + algo inesperado", 44, C, kind="SemiBold", dy=25)

def gum(d, cx, cy, s, col=PINK):
    rrect(d, cx - s * 0.6, cy - s * 0.3, cx + s * 0.6, cy + s * 0.3, s * 0.12, fill=col)
    d.line([S(cx - s * 0.45), S(cy - s * 0.12), S(cx + s * 0.45), S(cy - s * 0.12)], fill=mix(col, C, 0.5), width=S(8))

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "¿EL TRUCO MÁS RARO?", 110, C)
    sx, sy = shake(lt, 0.6, 0.35, 16)
    e = back(prog(lt, 0.35, 0.35))
    if e > 0.02:
        gum(d, 540 + sx, 560 + sy, 380 * e)
    pop_line(d, lt, 0.5, 540 + sx, 780 + sy, "MASCAR CHICLE", 150, PINK)
    slide_line(d, lt, 1.1, 540, 900, "probaron con 98 voluntarios", 48, C, kind="SemiBold", dy=25)
    # dos barras: sin chicle vs con chicle (1/3 menos)
    p = ease_out(prog(lt, 1.4, 0.9))
    base = 1330
    for i, (lab, h, col) in enumerate([("SIN CHICLE", 300, G), ("CON CHICLE", 200, PINK)]):
        x = 360 + i * 360
        rrect(d, x - 90, base - h * p, x + 90, base, 20, fill=col)
        if p > 0.3:
            text_c(d, x, base + 50, lab, "Black", 40, C, alpha=clamp((p - 0.3) * 2))
    pop_line(d, lt, 2.3, 760, 1050, "-1/3", 110, Y)
    slide_line(d, lt, 2.5, 540, 1460, "\"escucharon\" la canción un tercio menos", 42, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1525, "Univ. de Reading, Q. J. Exp. Psychology 2015", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿POR QUÉ?", 140, C)
    slide_line(d, lt, 0.3, 540, 450, "MASTICAR OCUPA", 120, Y)
    slide_line(d, lt, 0.45, 540, 580, "TU \"VOZ INTERIOR\"", 120, Y)
    # boca que mastica
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        op = 0.5 + 0.5 * math.sin(lt * 12)
        w, h = 420 * e, (60 + 150 * op) * e
        rrect(d, 540 - w / 2, 860 - h / 2, 540 + w / 2, 860 + h / 2, min(h / 2, 60), fill=R)
        rrect(d, 540 - w / 2 + 30, 860 - h / 2, 540 + w / 2 - 30, 860 - h / 2 + 22 * e, 8, fill=C)
        circle(d, 540, 860 + h * 0.15, 45 * e * op, fill=PINK)
    pill(d, lt, 1.8, 540, 1110, 820, "OTRO TRUCO: ESCUCHALA ENTERA", fill=C, ink=K, size=40, h=110)
    slide_line(d, lt, 2.2, 540, 1240, "terminarla puede cortar el bucle", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1300, "o poné otra canción", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    for k in range(5):
        a = lt * 1.5 + k * math.tau / 5
        note(d, 540 + math.cos(a) * 380, 1010 + math.sin(a) * 60, 55, mix(K, Y, 0.35), double=(k % 2 == 1))
    slide_line(d, lt, 0.1, 540, 420, "CONTAME:", 120, C)
    pop_line(d, lt, 0.3, 540, 580, "¿CUÁL SE TE", 150, Y)
    pop_line(d, lt, 0.5, 540, 740, "PEGÓ HOY?", 150, Y)
    pill(d, lt, 1.2, 540, 1200, 700, "DEJALA EN LOS COMENTARIOS", fill=Y, ink=K, size=40, h=100)
    slide_line(d, lt, 1.6, 540, 1330, "y si no se va... chicle", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.05, "shimmer"); ev(0.25, "pop", 0.3); ev(0.45, "thump"); ev(1.6, "tap")
for k in range(6): ev(0.2 + k * 0.5, "ding", 0.4 if k % 2 else -0.4)
ev(4.1, "tap"); ev(4.3, "pop"); ev(4.6, "tap")
for k in range(7): ev(4.45 + k * 0.07, "click", -0.5 + k * 0.15)
ev(5.6, "thump"); ev(5.9, "tap"); ev(6.2, "tap", 0.3)
ev(8.1, "tap", -0.3); ev(8.25, "tap", 0.3)
for k in range(7): ev(8.4 + k * 0.17, "ding", -0.6 + k * 0.2)
ev(9.4, "pop", -0.2); ev(9.9, "pop"); ev(10.4, "pop", 0.2); ev(10.7, "tap")
ev(12.1, "tap"); ev(12.35, "pop"); ev(12.5, "stamp"); ev(13.1, "tap")
for k in range(6): ev(13.4 + k * 0.14, "tick", 0.3 if k % 2 else -0.3)
ev(14.3, "thump"); ev(14.5, "tap"); ev(14.7, "tap", 0.2)
ev(16.1, "tap"); ev(16.3, "pop", -0.2); ev(16.45, "pop", 0.2)
for k in range(8): ev(16.6 + k * 0.26, "rustle", 0.2 if k % 2 else -0.2)
ev(17.8, "pop"); ev(18.2, "tap"); ev(18.4, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.5, "thump"); ev(21.2, "pop"); ev(21.6, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
