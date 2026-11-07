"""Short 2026-11-07 20:00 — Mente y emociones: anotar los pendientes antes de dormir ayuda a dormirse antes.
Fuente: Scullin et al., Baylor University, J. Exp. Psychol.: General 2018 (comunicado Baylor 11/01/2018;
Baylor Proud; Medical News Today): 57 adultos sanos de 18 a 30 años, monitoreados de noche en laboratorio;
5 minutos antes de dormir, un grupo escribió su lista de pendientes y otro lo que ya había hecho.
El grupo de la lista se durmió en promedio 9 minutos antes; cuanto más específica la lista, más rápido se durmieron.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

ITEMS = ["pagar la luz", "mail al profe", "comprar pan", "llamar a mamá"]

def notepad(d, cx, cy, w, h, n_lines, tick_p, t, items=ITEMS, size=46):
    """Libreta con renglones que se van escribiendo y tildando."""
    x0, y0 = cx - w / 2, cy - h / 2
    rrect(d, x0, y0, x0 + w, y0 + h, 30, fill=C)
    for k in range(5):
        circle(d, x0 + 70 + k * (w - 140) / 4, y0, 16, fill=G)
    for i, it in enumerate(items):
        y = y0 + 110 + i * (h - 140) / len(items)
        p = clamp(n_lines - i)
        bx = x0 + 50
        rrect(d, bx, y - 26, bx + 52, y + 26, 10, outline=(60, 60, 60), width=6)
        if p > 0:
            # el texto se "escribe" de izquierda a derecha
            s = it[:max(1, int(len(it) * p))]
            text_l(d, bx + 90, y, s, "Bold", size, K)
        q = clamp(tick_p - i)
        if q > 0:
            d.line([S(bx + 8), S(y), S(bx + 22), S(y + 16), S(lerp(bx + 22, bx + 50, q)), S(lerp(y + 16, y - 22, q))],
                   fill=GREEN, width=S(10), joint="curve")

def head_loop(d, cx, cy, r, t, items, alpha=1.0):
    """Cabeza con pensamientos que giran (pendientes dando vueltas)."""
    circle(d, cx, cy, r, fill=K2, outline=C, width=8)
    for i, it in enumerate(items):
        a = t * 1.6 + i / len(items) * math.tau
        x, y = cx + math.cos(a) * r * 1.95, cy + math.sin(a) * r * 1.3
        text_c(d, x, y, it, "Bold", 40, Y if i % 2 else C, alpha=alpha)

def mini_list(d, cx, cy, ticked):
    for k in range(3):
        y = cy - 110 + k * 110
        rrect(d, cx - 170, y - 30, cx - 110, y + 30, 12, outline=C, width=6)
        if ticked:
            d.line([S(cx - 160), S(y), S(cx - 145), S(y + 18), S(cx - 115), S(y - 26)], fill=GREEN, width=S(10), joint="curve")
        rrect(d, cx - 80, y - 10, cx + 160 - k * 40, y + 10, 10, fill=Y if not ticked else G)

def bed(d, cx, cy, w, col=C):
    rrect(d, cx - w / 2, cy, cx + w / 2, cy + w * 0.12, 16, fill=col)
    rrect(d, cx - w / 2, cy - w * 0.22, cx - w / 2 + 30, cy + w * 0.25, 10, fill=col)
    rrect(d, cx + w / 2 - 30, cy - w * 0.08, cx + w / 2, cy + w * 0.25, 10, fill=col)
    rrect(d, cx - w / 2 + 50, cy - w * 0.1, cx - w / 2 + 50 + w * 0.22, cy, 20, fill=Y)

def b1(d, t):
    stars(d, t)
    # texto grande desde el frame 1
    text_c(d, 540, 300, "¿NO PODÉS DORMIR", "A", 135, C)
    pop_line(d, t, 0.3, 540, 450, "PENSANDO EN MAÑANA?", 104, Y)
    e = back(prog(t, 0.2, 0.4))
    if e > 0.02:
        head_loop(d, 540, 900, 170 * e, t, ITEMS, alpha=clamp(e))
        moon(d, 540, 900, 90 * e, col=Y, bg=K2)
    slide_line(d, t, 1.8, 540, 1300, "hay un truco de 5 minutos", 54, C, kind="SemiBold", dy=25)
    pill(d, t, 2.4, 540, 1430, 640, "Y TIENE CIENCIA", fill=Y, ink=K, size=46, h=100)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 260, "UN ESTUDIO EN BAYLOR", 105, C)
    slide_line(d, lt, 0.3, 540, 370, "57 jóvenes durmiendo en un laboratorio", 42, C, kind="SemiBold", dy=20)
    # dos tarjetas que entran desde los costados
    pa = ease_out(prog(lt, 0.6, 0.5)); pb = ease_out(prog(lt, 1.2, 0.5))
    if pa > 0:
        x = lerp(-400, 300, pa)
        rrect(d, x - 230, 520, x + 230, 1120, 40, fill=K2, outline=Y, width=8)
        text_c(d, x, 610, "GRUPO A", "A", 80, Y, bg=K2)
        text_c(d, x, 720, "anotó lo que", "SemiBold", 40, C, bg=K2)
        text_c(d, x, 775, "TENÍA QUE HACER", "Black", 40, Y, bg=K2)
        mini_list(d, x, 950, False)
    if pb > 0:
        x = lerp(1480, 780, pb)
        rrect(d, x - 230, 520, x + 230, 1120, 40, fill=K2, outline=G, width=8)
        text_c(d, x, 610, "GRUPO B", "A", 80, C, bg=K2)
        text_c(d, x, 720, "anotó lo que", "SemiBold", 40, C, bg=K2)
        text_c(d, x, 775, "YA HABÍA HECHO", "Black", 40, C, bg=K2)
        mini_list(d, x, 950, True)
    pop_line(d, lt, 2.2, 540, 1240, "5 MIN ANTES DE ACOSTARSE", 90, C)
    slide_line(d, lt, 2.6, 540, 1350, "Scullin et al., Baylor University, 2018", 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 260, "ESCRIBIR LO PENDIENTE", 105, C)
    slide_line(d, lt, 0.3, 540, 370, "lo saca de tu cabeza y lo pasa al papel", 42, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        nl = ease_in_out(prog(lt, 0.7, 2.4)) * len(ITEMS)
        notepad(d, 540, 900, 760 * e, 620 * e, nl, 0, lt) if e > 0.95 else rrect(d, 540 - 380 * e, 900 - 310 * e, 540 + 380 * e, 900 + 310 * e, 30, fill=C)
    # lápiz
    if lt > 0.7:
        i = min(len(ITEMS) - 1, int(ease_in_out(prog(lt, 0.7, 2.4)) * len(ITEMS)))
        px = 400 + (lt * 900) % 380
        py = 900 - 310 + 110 + i * (620 - 140) / len(ITEMS) - 30
        d.polygon([(S(px), S(py + 30)), (S(px + 30), S(py - 60)), (S(px + 60), S(py - 50)), (S(px + 18), S(py + 38))], fill=Y)
        d.polygon([(S(px), S(py + 30)), (S(px + 18), S(py + 38)), (S(px + 4), S(py + 48))], fill=K)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 260, "LOS QUE HICIERON", 120, C)
    slide_line(d, lt, 0.25, 540, 390, "LA LISTA SE DURMIERON", 105, C)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        clock(d, 540, 760, 200 * e, ease_in_out(prog(lt, 0.6, 1.4)), turns=2, fill_deg=54)
    sx, sy = shake(lt, 2.0, 0.35, 18)
    stamp(d, lt, 1.8, 540 + sx, 1130 + sy, 430, 115, "9 MIN ANTES", fill=Y, ink=K, size=150)
    slide_line(d, lt, 2.3, 540, 1300, "en promedio, que el otro grupo", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1380, "Baylor University, J. Exp. Psychol. 2018", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 260, "Y CUANTO MÁS", 125, C)
    pop_line(d, lt, 0.3, 540, 400, "DETALLADA LA LISTA", 120, Y)
    # lista corta vs lista detallada
    p = ease_out(prog(lt, 0.5, 0.4))
    if p > 0:
        rrect(d, 120, 560, 470, 560 + 200 * p, 26, fill=K2, outline=G, width=6)
        rrect(d, 610, 560, 960, 560 + 470 * p, 26, fill=K2, outline=Y, width=6)
        for k in range(2):
            if p > 0.5: rrect(d, 160, 620 + k * 60, 420, 640 + k * 60, 10, fill=G)
        nk = int(ease_out(prog(lt, 0.8, 1.0)) * 7)
        for k in range(nk):
            rrect(d, 650, 620 + k * 60, 920 - (k % 3) * 60, 640 + k * 60, 10, fill=Y)
        zzz(d, 260, 860, lt * 0.8, col=G)
        zzz(d, 760, 1120, lt * 1.8, col=C)
    sx, sy = shake(lt, 2.2, 0.3, 14)
    pop_line(d, lt, 2.0, 540 + sx, 1300 + sy, "MÁS RÁPIDO SE DURMIERON", 100, C)
    slide_line(d, lt, 2.5, 540, 1400, "ej.: no \"llamar\", sino \"llamar a mamá a las 10\"", 38, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    stars(d, lt)
    slide_line(d, lt, 0.05, 540, 330, "ESTA NOCHE:", 120, C)
    pop_line(d, lt, 0.25, 540, 480, "ANOTÁ LO DE MAÑANA", 115, Y)
    pop_line(d, lt, 0.45, 540, 610, "Y SOLTALO", 140, Y)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        bed(d, 540, 1020, 520 * e)
        if lt > 1.0: zzz(d, 470, 960, lt)
    slide_line(d, lt, 1.4, 540, 1250, "5 minutos, papel y lápiz", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.8, 540, 1340, "si el insomnio sigue semanas,", 42, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 1.95, 540, 1400, "consultá con un profesional", 42, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.3, "pop", 0.3); ev(0.2, "shimmer")
ev(1.8, "tap"); ev(2.4, "ding")
ev(4.1, "tap"); ev(4.3, "tap", 0.3)
ev(4.6, "swipe", -0.6); ev(5.2, "swipe", 0.6); ev(6.2, "pop"); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.3, "rustle")
for k in range(10): ev(8.7 + k * 0.24, "click", 0.3 if k % 2 else -0.3)
ev(12.1, "tap"); ev(12.25, "tap")
for k in range(10): ev(12.6 + k * 0.14, "tick", 0.3 if k % 2 else -0.3)
ev(13.75, "stamp"); ev(14.0, "thump"); ev(14.3, "tap"); ev(14.5, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.5, "rustle")
for k in range(7): ev(16.8 + k * 0.14, "pop", -0.5 + k * 0.15)
ev(18.0, "pop"); ev(18.2, "thump"); ev(18.5, "tap")
ev(20.05, "tap"); ev(20.25, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.6, "shimmer")
ev(21.4, "tap"); ev(21.8, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
