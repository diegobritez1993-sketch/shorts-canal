"""Short 2026-11-25 15:00 — ¿Consultalo con la almohada? Dormir duplica las ideas (Wagner et al., Nature 2004)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Fuente: Wagner et al., Univ. de Lübeck, Nature 2004"

def bulb(d, cx, cy, s, on=0.0, t=0.0):
    """Lamparita: on 0..1 = apagada -> prendida con rayos."""
    col = mix((70, 70, 70), Y, on)
    if on > 0.05:
        for k in range(10):
            a = k * math.tau / 10 + t * 0.6
            r0, r1 = s * 0.75, s * (0.75 + 0.35 * on)
            d.line([S(cx + math.cos(a) * r0), S(cy - s * 0.12 + math.sin(a) * r0),
                    S(cx + math.cos(a) * r1), S(cy - s * 0.12 + math.sin(a) * r1)], fill=col, width=S(10))
    circle(d, cx, cy - s * 0.12, s * 0.52, fill=col)
    rrect(d, cx - s * 0.24, cy + s * 0.32, cx + s * 0.24, cy + s * 0.62, 10, fill=C)
    for k in range(2):
        yy = cy + s * (0.41 + k * 0.11)
        d.line([S(cx - s * 0.24), S(yy), S(cx + s * 0.24), S(yy)], fill=G, width=S(5))
    rrect(d, cx - s * 0.12, cy + s * 0.62, cx + s * 0.12, cy + s * 0.72, 8, fill=G)

def pillow(d, cx, cy, w, h, col=C):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, h * 0.45, fill=col)
    d.line([S(cx - w * 0.3), S(cy + h * 0.1), S(cx + w * 0.3), S(cy + h * 0.1)], fill=mix(col, K, 0.25), width=S(6))

def bar(d, x, base, w, hmax, frac, col, label, val):
    hh = hmax * frac
    if hh > 2:
        rrect(d, x - w / 2, base - hh, x + w / 2, base, 24, fill=col)
    text_c(d, x, base - hh - 70, val, "A", 110, col)
    text_c(d, x, base + 60, label, "Black", 44, C)

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        pillow(d, 540, 760, 560 * e, 230 * e)
        bulb(d, 540, 470, 190 * e, on=ease_out(prog(t, 1.9, 0.4)), t=t)
    pop_line(d, t, 0.0, 540, 1050, "¿TRABADO CON", 140, C)
    pop_line(d, t, 0.3, 540, 1200, "UN PROBLEMA?", 150, Y)
    slide_line(d, t, 1.2, 540, 1340, "consultalo con la almohada:", 50, C, kind="SemiBold", dy=25)
    slide_line(d, t, 1.4, 540, 1405, "la ciencia dice que funciona", 50, C, kind="SemiBold", dy=25)
    if t < 1.9:
        zzz(d, 780, 620, t, col=G)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "66 PERSONAS", 150, Y)
    slide_line(d, lt, 0.3, 540, 420, "UN JUEGO DE NÚMEROS", 100, C)
    digits = "14419914"
    for i, ch in enumerate(digits):
        e = back(prog(lt, 0.6 + i * 0.09, 0.3))
        if e > 0.02:
            x = 540 + (i - 3.5) * 118
            rrect(d, x - 50 * e, 690 - 70 * e, x + 50 * e, 690 + 70 * e, 18, fill=K2, outline=C, width=4)
            text_c(d, x, 690, ch, "A", int(100 * e) + 1, C, bg=K2)
    stamp(d, lt, 1.7, 540, 930, 330, 85, "REGLA OCULTA", fill=R, ink=C, size=95)
    slide_line(d, lt, 2.3, 540, 1120, "había un atajo escondido", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.45, 540, 1185, "que nadie les contó", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1290, SRC, 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "PRACTICARON Y", 110, C)
    pop_line(d, lt, 0.3, 540, 440, "8 HORAS DESPUÉS", 135, Y)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        clock(d, 540, 700, 150 * e, prog(lt, 0.6, 2.4), turns=8, fill_deg=360)
    # dos grupos
    e1 = back(prog(lt, 1.4, 0.35)); e2 = back(prog(lt, 1.7, 0.35))
    if e1 > 0.02:
        rrect(d, 120, 920, 520, 1260, 40, fill=K2)
        moon(d, 320, 1040, 80 * e1, bg=K2)
        text_c(d, 320, 1190, "DURMIERON", "Black", 46, C, alpha=e1 if e1 < 1 else 1, bg=K2)
    if e2 > 0.02:
        rrect(d, 560, 920, 960, 1260, 40, fill=K2)
        circle(d, 760, 1040, 70 * e2, outline=C, width=12)
        for k in range(3):
            circle(d, 735 + k * 25, 1040, 9 * e2, fill=C)
        text_c(d, 760, 1190, "DESPIERTOS", "Black", 46, C, bg=K2)
    slide_line(d, lt, 2.4, 540, 1350, "(de noche o de día)", 44, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "¿QUIÉNES", 120, C)
    slide_line(d, lt, 0.25, 540, 410, "DESCUBRIERON EL ATAJO?", 92, Y)
    g1 = ease_out(prog(lt, 0.6, 1.0)); g2 = ease_out(prog(lt, 0.6, 1.0))
    base = 1130
    bar(d, 340, base, 260, 520, 0.591 * g1 / 0.6, Y, "DURMIERON", f"{round(59 * g1)}%")
    bar(d, 740, base, 260, 520, 0.227 * g2 / 0.6, G, "DESPIERTOS", f"{round(23 * g2)}%")
    stamp(d, lt, 1.9, 540, 1340, 310, 80, "MÁS DEL DOBLE", fill=Y, ink=K, size=92)
    slide_line(d, lt, 2.5, 540, 1470, "13 de 22 contra 5 de 22", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1530, SRC, 32, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿POR QUÉ?", 150, C)
    on = ease_out(prog(lt, 1.2, 0.5))
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        bulb(d, 540, 700, 230 * e, on=on, t=lt)
    slide_line(d, lt, 1.0, 540, 1030, "MIENTRAS DORMÍS,", 105, C)
    slide_line(d, lt, 1.25, 540, 1150, "EL CEREBRO REORDENA", 95, Y)
    slide_line(d, lt, 1.6, 540, 1270, "lo que aprendiste en el día", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.75, 540, 1335, "y a veces aparece la idea", 50, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 450, "PRACTICÁ Y DORMÍ", 135, Y)
    slide_line(d, lt, 0.7, 540, 580, "no lo resuelvas a las 3 AM", 50, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.9, 0.35))
    if e > 0.02:
        pillow(d, 540, 780, 420 * e, 170 * e)
    sx, sy = shake(lt, 1.6, 0.3, 12)
    pop_line(d, lt, 1.4, 540 + sx, 1020 + sy, "¿TE PASÓ DESPERTARTE", 92, C)
    pop_line(d, lt, 1.6, 540 + sx, 1130 + sy, "CON LA RESPUESTA?", 105, Y)
    pill(d, lt, 2.1, 540, 1290, 520, "SÍ O NO", fill=R, ink=C, size=50, h=100)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.05, "thump"); ev(0.3, "pop", 0.3); ev(1.2, "tap"); ev(1.4, "tap"); ev(1.9, "ding")
ev(4.1, "tap"); ev(4.3, "tap")
for i in range(8): ev(4.6 + i * 0.09, "click", -0.4 + i * 0.1)
ev(5.5, "whoosh"); ev(5.7, "stamp"); ev(6.3, "tap"); ev(6.45, "tap")
ev(8.1, "tap"); ev(8.3, "pop"); ev(8.5, "pop")
for k in range(12): ev(8.6 + k * 0.2, "tick", 0.2 if k % 2 else -0.2)
ev(9.4, "pop", -0.4); ev(9.7, "pop", 0.4); ev(10.4, "tap")
ev(12.1, "tap"); ev(12.25, "tap")
for k in range(10): ev(12.6 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(13.7, "whoosh"); ev(13.9, "stamp"); ev(14.5, "tap")
ev(16.1, "pop"); ev(16.3, "pop"); ev(17.0, "tap"); ev(17.2, "shimmer"); ev(17.25, "tap"); ev(17.6, "tap"); ev(17.75, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.7, "tap"); ev(20.9, "pop"); ev(21.4, "pop"); ev(21.6, "thump"); ev(22.1, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
