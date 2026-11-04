"""Short 2026-11-04 15:00 — Cómo te enganchan las apps: nadie lee los términos y condiciones.
Fuente: Obar y Oeldorf-Hirsch, "The biggest lie on the internet", Information, Communication & Society (2018/2020).
Experimento con 543 estudiantes universitarios (UConn) que se anotaban a una red social falsa ("NameDrop").
- 74% eligió "unirse rápido" y salteó la política de privacidad.
- Leer la política llevaba ~29-32 min y los términos ~15-17 min (250-280 palabras/min).
- Tiempo promedio real: 73 s en la política (quienes la abrieron) y 51 s en los términos.
- 98% no vio las cláusulas trampa: compartir datos con la NSA y entregar a su primer hijo como pago.
(La cláusula del hijo era una broma de los investigadores, no tiene validez.)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Obar y Oeldorf-Hirsch, Information, Communication & Society, 2018"


def checkbox(d, cx, cy, s, q, col=Y):
    """Casilla que se tilda (q 0..1)."""
    rrect(d, cx - s / 2, cy - s / 2, cx + s / 2, cy + s / 2, s * 0.18, fill=K2, outline=C, width=8)
    if q > 0:
        a = (cx - s * 0.28, cy + s * 0.02); b = (cx - s * 0.06, cy + s * 0.24); c = (cx + s * 0.3, cy - s * 0.24)
        if q < 0.4:
            f = q / 0.4
            pts = [a, (lerp(a[0], b[0], f), lerp(a[1], b[1], f))]
        else:
            f = (q - 0.4) / 0.6
            pts = [a, b, (lerp(b[0], c[0], f), lerp(b[1], c[1], f))]
        d.line([(S(x), S(y)) for x, y in pts], fill=col, width=int(S(s * 0.13)), joint="curve")


def doc(d, cx, cy, w, h, scroll=0.0, lines=60, hl=None):
    """Documento larguísimo con renglones grises que se desplazan."""
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    rrect(d, x0, y0, x1, y1, 30, fill=C)
    gap = 42
    for k in range(lines):
        y = y0 + 50 + k * gap - scroll
        if y < y0 + 30 or y > y1 - 30: continue
        ln = 0.55 + 0.4 * ((k * 37) % 10) / 10
        d.line([S(x0 + 50), S(y), S(x0 + 50 + (w - 100) * ln), S(y)], fill=(185, 185, 185), width=S(12))
    # barra de scroll
    sp = clamp(scroll / max(1, lines * gap - h))
    rrect(d, x1 - 26, y0 + 30 + (h - 160) * sp, x1 - 14, y0 + 130 + (h - 160) * sp, 6, fill=(120, 120, 120))


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 330, "¿LEÉS LOS", 150, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 500, "TÉRMINOS Y", 150, C, dur=0.25)
    pop_line(d, lt, 0.4, 540, 670, "CONDICIONES?", 160, Y, dur=0.25)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        rrect(d, 540 - 400 * e, 1000 - 110 * e, 540 + 400 * e, 1000 + 110 * e, 40, fill=K2)
        if e > 0.8:
            checkbox(d, 260, 1000, 120, ease_out(prog(lt, 1.4, 0.25)))
            text_l(d, 360, 985, "Leí y acepto los", "Bold", 44, C)
            text_l(d, 360, 1040, "términos", "Bold", 44, C)
    pop_line(d, lt, 1.75, 540, 1260, "(MENTIRA)", 110, R)
    slide_line(d, lt, 2.5, 540, 1400, "casi nadie los lee... y hay pruebas", 46, C, kind="SemiBold", dy=25)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "UN EXPERIMENTO:", 110, C)
    n = 543 * ease_out(prog(lt, 0.4, 1.0))
    pop_line(d, lt, 0.35, 540, 450, f"{int(n)} ESTUDIANTES", 140, Y)
    # grilla de personitas que se llena
    for i in range(24):
        p = back(prog(lt, 0.5 + i * 0.04, 0.25))
        if p <= 0.02: continue
        r, c = divmod(i, 6)
        person(d, 190 + c * 140, 700 + r * 150, 120 * p, mix(K, C, 0.85))
    pill(d, lt, 1.8, 540, 1340, 860, "SE ANOTAN A UNA RED SOCIAL FALSA", size=38)
    slide_line(d, lt, 2.4, 540, 1450, "inventada por los investigadores", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1530, SRC, 28, G, kind="SemiBold", dy=15)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "LEERLOS LLEVABA", 110, C)
    pop_line(d, lt, 0.35, 540, 420, "15 A 17 MINUTOS", 135, C)
    # barra larga (lo que llevaría) vs barra mínima (lo que hicieron)
    pa = ease_in_out(prog(lt, 0.6, 0.7))
    text_l(d, 110, 600, "lo que llevaría leerlos", "Bold", 40, C) if pa > 0 else None
    rrect(d, 110, 640, 970, 720, 40, fill=K2)
    if pa > 0.02: rrect(d, 110, 640, 110 + 860 * pa, 720, 40, fill=C)
    pb = ease_out(prog(lt, 1.3, 0.3))
    text_l(d, 110, 800, "lo que tardaron de verdad", "Bold", 40, Y) if pb > 0 else None
    rrect(d, 110, 840, 970, 920, 40, fill=K2)
    if pb > 0.02: rrect(d, 110, 840, 110 + 80 * pb, 920, 40, fill=Y)   # 51 s / 16 min ≈ 5%
    # contador en segundos
    s = 51 * ease_out(prog(lt, 1.5, 1.1))
    sx, sy = shake(lt, 2.6, 0.35, 16)
    if lt > 1.5:
        text_c(d, 540 + sx, 1130 + sy, f"{int(s)} SEGUNDOS", "A", 190, Y)
    slide_line(d, lt, 2.6, 540, 1290, "en promedio", 50, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1380, SRC, 28, G, kind="SemiBold", dy=15)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 270, "Y LA POLÍTICA", 115, C)
    slide_line(d, lt, 0.25, 540, 400, "DE PRIVACIDAD...", 115, C)
    # documento que se scrollea a toda velocidad
    e = ease_out(prog(lt, 0.4, 0.3))
    if e > 0.02:
        sc = 2400 * ease_in_out(prog(lt, 0.6, 1.6))
        doc(d, 540, 830, 640 * e, 480, scroll=sc, lines=70)
    # sello: 74% la salteó
    stamp(d, lt, 2.0, 540, 1240, 380, 115, "74% LA SALTEÓ", fill=R, ink=C, size=120)
    slide_line(d, lt, 2.6, 540, 1420, "tocaron \"unirse rápido\" sin abrirla", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1500, SRC, 28, G, kind="SemiBold", dy=15)


def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 270, "LA LETRA CHICA", 120, C)
    pop_line(d, lt, 0.3, 540, 410, "ESCONDÍA UNA TRAMPA", 105, Y)
    e = ease_out(prog(lt, 0.4, 0.3))
    if e > 0.02:
        x0, y0, x1, y1 = 540 - 420 * e, 520, 540 + 420 * e, 1060
        rrect(d, x0, y0, x1, y1, 30, fill=C)
        for k in range(10):
            y = y0 + 50 + k * 46
            if 3 <= k <= 6: continue
            d.line([S(x0 + 50), S(y), S(x0 + 50 + (x1 - x0 - 100) * (0.6 + 0.35 * ((k * 3) % 4) / 4)), S(y)], fill=(185, 185, 185), width=S(12))
        if e > 0.9:
            q = ease_out(prog(lt, 0.9, 0.5))
            rrect(d, 150, 705, 150 + 780 * q, 830, 18, fill=Y)
            text_c(d, 540, 745, "como pago, entregás a", "Bold", 42, K, alpha=clamp((lt - 1.0) * 3), bg=Y if q > 0.6 else C)
            text_c(d, 540, 795, "TU PRIMER HIJO", "Black", 46, K, alpha=clamp((lt - 1.1) * 3), bg=Y if q > 0.6 else C)
    stamp(d, lt, 1.9, 540, 1220, 390, 115, "98% NO LO VIO", fill=R, ink=C, size=120)
    slide_line(d, lt, 2.5, 540, 1390, "(era una broma de los investigadores)", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.7, 540, 1470, SRC, 28, G, kind="SemiBold", dy=15)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 290, "ANTES DE \"ACEPTO\"", 120, C)
    pop_line(d, lt, 0.3, 540, 430, "BUSCÁ 3 COSAS", 125, Y)
    items = ["qué datos guardan", "con quién los comparten", "cómo borrar tu cuenta"]
    for k, it in enumerate(items):
        q = prog(lt, 0.7 + k * 0.3, 0.3)
        if q <= 0: continue
        y = 610 + k * 150
        rrect(d, 120, y - 55, 960, y + 55, 30, fill=K2)
        checkbox(d, 200, y, 70, ease_out(prog(lt, 0.85 + k * 0.3, 0.25)))
        text_l(d, 270, y, it, "Bold", 44, C)
    slide_line(d, lt, 1.8, 540, 1130, "¿vos leíste alguno alguna vez?", 48, Y, kind="Bold", dy=25)
    slide_line(d, lt, 2.0, 540, 1200, "contalo en los comentarios", 42, C, kind="SemiBold", dy=25)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.4, "pop"); ev(0.7, "pop")
ev(1.4, "click"); ev(1.6, "tap"); ev(1.75, "thump"); ev(2.5, "tap")
ev(4.1, "tap"); ev(4.35, "pop")
for k in range(10): ev(4.4 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
for k in range(8): ev(4.5 + k * 0.12, "pop", -0.5 + k * 0.14)
ev(5.8, "pop"); ev(6.4, "tap")
ev(8.1, "tap"); ev(8.35, "pop"); ev(8.6, "swipe", -0.3); ev(9.3, "tap")
for k in range(11): ev(9.5 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(10.6, "thump"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.25, "tap"); ev(12.4, "rustle")
for k in range(6): ev(12.6 + k * 0.25, "swipe", -0.3 + k * 0.12)
ev(13.8, "whoosh"); ev(14.0, "stamp"); ev(14.6, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.4, "rustle"); ev(16.9, "shimmer"); ev(17.1, "tap")
ev(17.7, "whoosh"); ev(17.9, "stamp"); ev(18.5, "tap")
ev(20.05, "tap"); ev(20.3, "pop")
for k in range(3): ev(20.85 + k * 0.3, "click", -0.3 + k * 0.3)
ev(21.8, "ding"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
