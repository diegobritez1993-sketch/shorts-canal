"""Short 2026-11-03 15:00 — Curiosidades y hábitos: ¿21 días para crear un hábito? Mito.
Fuentes: Lally et al., UCL, European Journal of Social Psychology 2010 (96 voluntarios, 84 días; mediana 66 días
para que el hábito se vuelva automático; rango estimado 18 a 254 días; saltearse una vez no afectó de forma
importante). Universidad de Surrey, entrevista a Pippa Lally (21/01/2026): "el promedio fue 66 días, el rango
18 a 254"; consejo: plan claro de cuándo y dónde.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Lally y otros, UCL, 2010"


def calendar(d, cx, cy, s, num, col=C, head=R, ink=K):
    """Hoja de calendario con número grande."""
    w, h = s, s * 1.05
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, s * 0.1, fill=col)
    d.rounded_rectangle([S(cx - w / 2), S(cy - h / 2), S(cx + w / 2), S(cy - h / 2 + h * 0.26)], radius=S(s * 0.1), fill=head)
    d.rectangle([S(cx - w / 2), S(cy - h / 2 + h * 0.14), S(cx + w / 2), S(cy - h / 2 + h * 0.26)], fill=head)
    for k in (-1, 1):
        rrect(d, cx + k * w * 0.25 - s * 0.04, cy - h / 2 - s * 0.08, cx + k * w * 0.25 + s * 0.04, cy - h / 2 + s * 0.08, s * 0.04, fill=(60, 60, 60))
    text_c(d, cx, cy + h * 0.12, str(num), "A", s * 0.55, ink, bg=col)


def check(d, cx, cy, s, p, col=GREEN):
    if p <= 0: return
    a, b, c = (cx - s * 0.45, cy), (cx - s * 0.12, cy + s * 0.33), (cx + s * 0.5, cy - s * 0.35)
    if p < 0.4:
        q = p / 0.4
        d.line([S(a[0]), S(a[1]), S(lerp(a[0], b[0], q)), S(lerp(a[1], b[1], q))], fill=col, width=int(S(s * 0.16)))
    else:
        q = (p - 0.4) / 0.6
        d.line([S(a[0]), S(a[1]), S(b[0]), S(b[1]), S(lerp(b[0], c[0], q)), S(lerp(b[1], c[1], q))], fill=col, width=int(S(s * 0.16)), joint="curve")


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 330, "¿21 DÍAS PARA", 150, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 490, "CREAR UN HÁBITO?", 135, Y, dur=0.25)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        calendar(d, 540, 960, 420 * e, 21)
    stamp(d, lt, 1.9, 540, 1010, 260, 100, "MITO", fill=R, ink=C, size=150)
    slide_line(d, lt, 2.6, 540, 1380, "todos lo repiten, pero un estudio dice otra cosa", 38, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 2.9, 540, 1520, "MIRÁ EL DATO REAL", 100, Y)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "UN ESTUDIO", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "SIGUIÓ A 96 PERSONAS", 100, Y)
    # grilla de personitas que aparecen
    for i in range(24):
        r, c = divmod(i, 6)
        p = back(prog(lt, 0.5 + i * 0.045, 0.3))
        if p > 0.02:
            person(d, 215 + c * 130, 640 + r * 150, 120 * p, Y if i % 5 == 2 else C)
    pill(d, lt, 1.9, 540, 1300, 640, "DURANTE 12 SEMANAS", fill=Y, ink=K, size=44, h=100)
    slide_line(d, lt, 2.3, 540, 1430, "comer, tomar agua o hacer ejercicio cada día", 40, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1500, SRC, 34, G, kind="SemiBold", dy=20)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "PARA QUE SE VUELVA", 100, C)
    slide_line(d, lt, 0.3, 540, 430, "AUTOMÁTICO TARDARON", 100, C)
    p = ease_out(prog(lt, 0.6, 1.4))
    n = int(round(66 * p))
    if lt > 0.6:
        sx, sy = shake(lt, 2.0, 0.35, 18)
        # páginas de calendario que se apilan
        for k in range(3):
            off = (2 - k) * 22
            calendar(d, 540 + off + sx, 860 - off + sy, 380, n if k == 2 else "", col=mix(K, C, 0.4 + 0.3 * k))
    pop_line(d, lt, 2.0, 540, 1220, "66 DÍAS", 210, Y, dur=0.28)
    slide_line(d, lt, 2.5, 540, 1380, "en promedio: ¡más del triple!", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1450, SRC, 34, G, kind="SemiBold", dy=20)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "PERO DEPENDE", 140, C)
    pop_line(d, lt, 0.3, 540, 450, "DE CADA UNO", 140, Y)
    # barra de rango 18 → 254
    x0, x1, y = 120, 960, 820
    rrect(d, x0, y - 22, x1, y + 22, 22, fill=(48, 48, 48))
    p = ease_in_out(prog(lt, 0.8, 1.4))
    if lt > 0.6:
        xa = x0 + (x1 - x0) * 18 / 254
        xb = lerp(xa, x1, p)
        rrect(d, xa, y - 22, max(xa + 44, xb), y + 22, 22, fill=Y)
        circle(d, xa, y, 40, fill=C)
        circle(d, xb, y, 40, fill=R if p > 0.95 else C)
        n = int(round(lerp(18, 254, p)))
        text_c(d, xa + 20, y - 110, "18", "A", 110, C)
        if p > 0.15:
            text_c(d, min(xb, 880), y - 110, str(n), "A", 110, R if p > 0.95 else Y)
    pop_line(d, lt, 0.7, 540, 1000, "DE 18 A 254 DÍAS", 120, C)
    slide_line(d, lt, 2.4, 540, 1150, "algunos tardaron más de 8 meses", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1220, SRC, 34, G, kind="SemiBold", dy=20)


def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿TE SALTEASTE", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "UN DÍA?", 130, C)
    # cadena de días: uno falla, la cadena sigue
    for i in range(7):
        p = back(prog(lt, 0.6 + i * 0.16, 0.25))
        if p <= 0.02: continue
        cx = 150 + i * 130
        miss = (i == 3)
        circle(d, cx, 760, 52 * p, fill=(60, 20, 18) if miss else K2, outline=R if miss else GREEN, width=8)
        if miss:
            s = 26 * p
            d.line([S(cx - s), S(760 - s), S(cx + s), S(760 + s)], fill=R, width=S(10))
            d.line([S(cx - s), S(760 + s), S(cx + s), S(760 - s)], fill=R, width=S(10))
        else:
            check(d, cx, 760, 50 * p, 1.0)
    stamp(d, lt, 2.0, 540, 1060, 380, 95, "NO PASA NADA", fill=GREEN, ink=K, size=120)
    slide_line(d, lt, 2.5, 540, 1250, "fallar una vez no arruinó el hábito", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1320, "lo que cuenta es volver al otro día", 46, C, kind="SemiBold", dy=25)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.2, 540, 480, "MISMA HORA", 150, Y)
    slide_line(d, lt, 0.35, 540, 640, "MISMO LUGAR", 150, Y)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        clock(d, 540, 940, 150 * e, ease_in_out(prog(lt, 0.6, 1.0)), turns=1, fill_deg=90)
    slide_line(d, lt, 1.2, 540, 1180, "y no te rindas a los 21 días", 46, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.7, 540, 1330, "¿QUÉ HÁBITO", 110, C)
    pop_line(d, lt, 1.9, 540, 1460, "ARRANCÁS HOY?", 110, Y)
    slide_line(d, lt, 2.3, 540, 1580, "contamelo en los comentarios", 42, C, kind="SemiBold", dy=20)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.45, "rustle"); ev(1.7, "whoosh"); ev(1.9, "stamp"); ev(2.6, "tap"); ev(2.9, "thump")
ev(4.1, "tap", -0.3); ev(4.3, "pop", 0.3)
for i in range(24): ev(4.5 + i * 0.045, "tap", -0.4 + (i % 6) * 0.16)
ev(5.9, "swipe"); ev(6.3, "tap"); ev(6.5, "tap", 0.3)
ev(8.1, "tap", -0.2); ev(8.3, "tap", 0.2)
for k in range(12): ev(8.6 + k * 0.11, "tick", 0.3 if k % 2 else -0.3)
ev(10.0, "thump"); ev(10.5, "tap"); ev(10.7, "tap", 0.2)
ev(12.1, "tap"); ev(12.3, "pop"); ev(12.7, "pop")
for k in range(10): ev(12.8 + k * 0.14, "tick", -0.4 + k * 0.08)
ev(14.2, "ding"); ev(14.4, "tap"); ev(14.6, "tap", 0.2)
ev(16.1, "tap", -0.2); ev(16.3, "tap", 0.2)
for i in range(7): ev(16.6 + i * 0.16, "buzz" if i == 3 else "click", -0.45 + i * 0.15)
ev(17.8, "whoosh"); ev(18.0, "stamp"); ev(18.5, "tap"); ev(18.7, "tap", 0.2)
ev(20.05, "tap"); ev(20.2, "pop", -0.2); ev(20.35, "pop", 0.2); ev(20.5, "shimmer")
for k in range(6): ev(20.6 + k * 0.16, "tick", 0.2 if k % 2 else -0.2)
ev(21.2, "tap"); ev(21.7, "pop", -0.2); ev(21.9, "pop", 0.2); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
