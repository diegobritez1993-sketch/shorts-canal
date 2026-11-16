"""Short 2026-11-16 15:00 — Cómo te enganchan las apps.
¿Elegís vos lo que mirás? 70% del tiempo en YouTube viene de sus recomendaciones.
Fuente: Neal Mohan (jefe de producto de YouTube), CES enero 2018 (vía Tubefilter 11/01/2018, CBS News/CNET).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def thumb(d, x, y, w, h, col, play=True):
    rrect(d, x, y, x + w, y + h, 18, fill=col)
    if play:
        cx, cy, s = x + w / 2, y + h / 2, min(w, h) * 0.18
        d.polygon([(S(cx - s * 0.6), S(cy - s)), (S(cx - s * 0.6), S(cy + s)), (S(cx + s), S(cy))], fill=C)

def cursor(d, x, y, s, col=C):
    pts = [(0, 0), (0, 1.0), (0.27, 0.76), (0.45, 1.12), (0.6, 1.05), (0.42, 0.7), (0.75, 0.7)]
    d.polygon([(S(x + px * s), S(y + py * s)) for px, py in pts], fill=col, outline=K)

def b1(d, t):
    # grilla de videos con un cursor que duda
    e = ease_out(prog(t, 0.0, 0.35))
    cols = [(60, 60, 60), (80, 70, 40), (50, 60, 80), (80, 50, 50), (55, 75, 55), (70, 55, 80)]
    for k in range(6):
        i, j = k % 3, k // 3
        x, y = 120 + i * 290, 1500 + j * 190 + 200 * (1 - e)
        hl = 1.0 if (int(t * 2.5) % 6 == k and t > 1.0) else 0.0
        thumb(d, x, y, 260, 160, mix(cols[k], Y, 0.6 * hl))
    if t > 0.8:
        k = int(t * 2.5) % 6
        cursor(d, 120 + (k % 3) * 290 + 170, 1500 + (k // 3) * 190 + 100, 70)
    pop_line(d, t, 0.0, 540, 640, "¿ELEGÍS VOS", 170, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 830, "LO QUE MIRÁS?", 170, Y, dur=0.25)
    slide_line(d, t, 1.3, 540, 1030, "o lo elige otro por vos...", 50, C, kind="SemiBold", dy=25)
    pill(d, t, 2.2, 540, 1210, 520, "MIRÁ ESTO", fill=R, ink=C, size=46, h=100)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "EN YOUTUBE,", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "DE CADA 10 MINUTOS", 100, C)
    # 10 bloques de minutos
    for k in range(10):
        p = prog(lt, 0.6 + k * 0.12, 0.25)
        if p <= 0: continue
        e = back(p)
        x = 95 + k * 92
        col = Y if k < 7 else (90, 90, 90)
        rrect(d, x + 36 - 36 * e, 620 - 90 * e, x + 36 + 36 * e, 620 + 90 * e, 14, fill=col)
    pop_line(d, lt, 1.9, 540, 900, "7 TE LOS ELIGE", 140, Y)
    pop_line(d, lt, 2.15, 540, 1050, "EL ALGORITMO", 140, Y)
    slide_line(d, lt, 2.6, 540, 1200, "el 70% del tiempo viene de sus recomendaciones", 40, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1270, "Neal Mohan, jefe de producto de YouTube, CES 2018", 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "NO LO BUSCASTE:", 120, C)
    pop_line(d, lt, 0.35, 540, 430, "TE LO PUSIERON", 140, R)
    # feed que se mueve solo (cinta transportadora)
    e = ease_out(prog(lt, 0.4, 0.4))
    if e > 0:
        rrect(d, 330, 560, 750, 1330, 50, fill=(22, 22, 22), outline=C, width=8)
        d.rectangle([S(338), S(580), S(742), S(1310)], fill=(22, 22, 22))
        off = (lt * 260) % 250
        cols = [(80, 70, 40), (50, 60, 80), (80, 50, 50), (55, 75, 55)]
        for k in range(6):
            y = 600 + k * 250 - off
            if y < 585 or y + 200 > 1305: continue
            thumb(d, 365, y, 350, 200, cols[k % 4])
        # flecha de "siguiente" automática
        ay = 950 + 20 * math.sin(lt * 8)
        d.polygon([(S(820), S(ay - 60)), (S(820), S(ay + 60)), (S(900), S(ay))], fill=Y)
    slide_line(d, lt, 1.6, 540, 1430, "un \"flujo constante\" de videos", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.8, 540, 1495, "así lo describió el propio YouTube", 40, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "¿Y FUNCIONA?", 130, C)
    slide_line(d, lt, 0.3, 540, 410, "en el celular, una sesión promedio dura", 42, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        clock(d, 540, 730, 220 * e, ease_in_out(prog(lt, 0.6, 1.5)), turns=1, fill_deg=360)
    sx, sy = shake(lt, 2.3, 0.35, 16)
    pop_line(d, lt, 2.1, 540 + sx, 1090 + sy, "MÁS DE 1 HORA", 170, Y, dur=0.25)
    slide_line(d, lt, 2.6, 540, 1240, "según YouTube, en 2018", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "CUANTO MÁS MIRÁS", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "MÁS TE CONOCE", 130, Y)
    # ciclo: mirás -> aprende -> te recomienda
    cx, cy, r = 540, 860, 270
    e = ease_out(prog(lt, 0.5, 0.5))
    if e > 0:
        rot = lt * 1.3
        d.arc([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], 0, 360 * e, fill=(70, 70, 70), width=S(14))
        a = rot
        hx, hy = cx + math.cos(a) * r, cy + math.sin(a) * r
        circle(d, hx, hy, 24, fill=Y)
    labels = [("MIRÁS", -90), ("APRENDE", 30), ("TE DA MÁS", 150)]
    for k, (lab, ang) in enumerate(labels):
        a = math.radians(ang)
        x, y = cx + math.cos(a) * r, cy + math.sin(a) * r
        p = prog(lt, 0.7 + k * 0.35, 0.3)
        if p > 0:
            rrect(d, x - 170 * back(p), y - 50, x + 170 * back(p), y + 50, 50, fill=K2, outline=C, width=4)
            text_c(d, x, y, lab, "Black", 42, C, alpha=clamp(p * 2), bg=K2)
    pop_line(d, lt, 2.2, 540, 1290, "Y CUESTA MÁS SOLTARLO", 100, R)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "BUSCÁ VOS", 160, Y)
    slide_line(d, lt, 0.6, 540, 610, "y apagá la reproducción automática", 44, C, kind="SemiBold", dy=25)
    if lt > 0.6:
        q = ease_in_out(prog(lt, 1.1, 0.35))
        toggle_row(d, 110, 720, "Autoplay", 1 - q, sub="reproducción automática")
    pop_line(d, lt, 1.8, 540, 1080, "¿HOY ELEGISTE VOS?", 110, C)
    pill(d, t, 22.3, 540, 1240, 520, "SÍ O NO", fill=Y, ink=K, size=50, h=110)
    slide_line(d, lt, 2.5, 540, 1360, "contalo en los comentarios", 42, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.3, "whoosh")
for k in range(7): ev(1.0 + k * 0.4, "click", 0.4 if k % 2 else -0.4)
ev(1.3, "tap"); ev(2.2, "thump")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(10): ev(4.6 + k * 0.12, "pop", -0.5 + k * 0.1)
ev(5.9, "stamp"); ev(6.15, "thump"); ev(6.6, "tap"); ev(6.8, "tap")
ev(8.1, "tap"); ev(8.35, "thump"); ev(8.4, "swipe")
for k in range(5): ev(8.8 + k * 0.6, "rustle", 0.3 if k % 2 else -0.3)
ev(9.6, "tap"); ev(9.8, "tap")
ev(12.1, "pop"); ev(12.3, "tap")
for k in range(12): ev(12.6 + k * 0.125, "tick", 0.3 if k % 2 else -0.3)
ev(14.1, "stamp"); ev(14.6, "tap")
ev(16.1, "tap", -0.3); ev(16.3, "pop", 0.3); ev(16.5, "whoosh")
ev(16.7, "pop", 0.0); ev(17.05, "pop", 0.4); ev(17.4, "pop", -0.4); ev(18.2, "thump")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "tap"); ev(21.1, "toggle"); ev(21.8, "pop"); ev(22.3, "ding"); ev(22.5, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
