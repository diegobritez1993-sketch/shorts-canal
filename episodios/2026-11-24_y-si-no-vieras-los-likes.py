"""Short 2026-11-24 15:00 — ¿Y si no vieras los likes? (Instagram ocultó los "me gusta")."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def like_card(d, cx, cy, s, count_txt, hide=0.0):
    rrect(d, cx - s, cy - s * 0.42, cx + s, cy + s * 0.42, 40, fill=K2, outline=C, width=6)
    heart(d, cx - s * 0.55, cy, s * 0.5, R)
    tx = cx + s * 0.22
    text_c(d, tx, cy, count_txt, "A", int(s * 0.36), C, bg=K2)
    if hide > 0:
        tx = tx + s * 0.06
        w = s * 0.44 * ease_out(hide)
        rrect(d, tx - w, cy - s * 0.2, tx + w, cy + s * 0.2, 24, fill=(70, 70, 70))
        if hide > 0.7:
            for i in (-1, 0, 1):
                circle(d, tx + i * s * 0.16, cy, s * 0.045, fill=C)

def gauge(d, cx, cy, r, p):
    for k in range(18):
        a0 = 180 + k * 10
        col = mix(GREEN, R, k / 17)
        d.arc([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], a0, a0 + 9, fill=col, width=S(44))
    ang = math.radians(180 + 180 * p)
    d.line([S(cx), S(cy), S(cx + math.cos(ang) * r * 0.8), S(cy + math.sin(ang) * r * 0.8)], fill=C, width=S(16))
    circle(d, cx, cy, 26, fill=C)

def face(d, cx, cy, r, col, happy):
    circle(d, cx, cy, r, fill=col)
    circle(d, cx - r * 0.35, cy - r * 0.2, r * 0.11, fill=K)
    circle(d, cx + r * 0.35, cy - r * 0.2, r * 0.11, fill=K)
    if happy:
        d.arc([S(cx - r * 0.5), S(cy - r * 0.2), S(cx + r * 0.5), S(cy + r * 0.55)], 20, 160, fill=K, width=S(14))
    else:
        d.line([S(cx - r * 0.45), S(cy - r * 0.55), S(cx - r * 0.15), S(cy - r * 0.42)], fill=K, width=S(12))
        d.line([S(cx + r * 0.45), S(cy - r * 0.55), S(cx + r * 0.15), S(cy - r * 0.42)], fill=K, width=S(12))
        d.line([S(cx - r * 0.4), S(cy + r * 0.38), S(cx + r * 0.4), S(cy + r * 0.38)], fill=K, width=S(14))

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        n = int(lerp(87, 1240, ease_in_out(prog(t, 0.3, 2.2))))
        like_card(d, 540, 640, 330 * e, fmt_num(n))
    pop_line(d, t, 0.2, 540, 1060, "¿Y SI NO VIERAS", 135, C)
    pop_line(d, t, 0.5, 540, 1210, "LOS LIKES?", 175, Y)
    slide_line(d, t, 1.4, 540, 1360, "ni los tuyos ni los de nadie", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "INSTAGRAM", 140, C)
    slide_line(d, lt, 0.3, 540, 440, "LOS ESCONDIÓ", 150, Y)
    slide_line(d, lt, 0.5, 540, 560, "en pruebas desde 2019", 48, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        like_card(d, 540, 900, 300 * e, "1.240", hide=prog(lt, 1.3, 0.5))
    pill(d, lt, 2.3, 540, 1250, 640, "LIKES OCULTOS", fill=Y, ink=K, size=46, h=100)
    slide_line(d, lt, 2.5, 540, 1390, "Fuente: Instagram, mayo 2021", 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "LA IDEA ERA", 120, C)
    pop_line(d, lt, 0.3, 540, 450, "BAJAR LA PRESIÓN", 125, Y)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        p = lerp(0.92, 0.18, ease_in_out(prog(lt, 1.0, 1.4)))
        gauge(d, 540, 960, 300 * e, p)
    slide_line(d, lt, 2.2, 540, 1170, "que no vivas pendiente", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1235, "de cuántos te dieron like", 50, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "¿Y QUÉ PASÓ?", 140, C)
    # balanza con efectos chicos
    e = ease_out(prog(lt, 0.4, 0.4))
    if e > 0:
        wob = math.sin(lt * 4) * 0.05 * (1 - prog(lt, 1.0, 2.0))
        cx, cy = 540, 720
        d.line([S(cx), S(cy - 40), S(cx), S(cy + 260 * e)], fill=C, width=S(14))
        rrect(d, cx - 140, cy + 250 * e, cx + 140, cy + 280 * e, 12, fill=C)
        x0, y0 = cx - 300 * math.cos(wob), cy - 300 * math.sin(wob)
        x1, y1 = cx + 300 * math.cos(wob), cy + 300 * math.sin(wob)
        d.line([S(x0), S(y0), S(x1), S(y1)], fill=C, width=S(12))
        circle(d, cx, cy, 22, fill=Y)
        for (px, py, sg, col) in ((x0, y0, "+", GREEN), (x1, y1, "−", R)):
            d.line([S(px), S(py), S(px), S(py + 90)], fill=G, width=S(6))
            circle(d, px, py + 140, 60 * e, fill=col)
            text_c(d, px, py + 135, sg, "A", int(90 * e) + 1, K, bg=col)
    sx, sy = shake(lt, 1.8, 0.35, 14)
    pop_line(d, lt, 1.6, 540 + sx, 1180 + sy, "CAMBIÓ MUY POCO", 125, Y, dur=0.28)
    slide_line(d, lt, 2.2, 540, 1310, "en cómo se sentía la gente", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1370, "y en cuánto usaba la app", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1450, "Adam Mosseri (Instagram) en TechCrunch, 2021", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pr = ease_in_out(prog(lt, 0.2, 0.5))
    d.rectangle([0, 0, S(540 * pr), S(1920)], fill=(14, 34, 20))
    d.rectangle([S(1080 - 540 * pr), 0, S(1080), S(1920)], fill=(40, 14, 14))
    e1 = back(prog(lt, 0.5, 0.4)); e2 = back(prog(lt, 1.4, 0.4))
    if e1 > 0.02: face(d, 270, 760, 150 * e1, GREEN, True)
    if e2 > 0.02: face(d, 810, 760, 150 * e2, R, False)
    pop_line(d, lt, 0.7, 270, 1020, "A ALGUNOS", 90, C, bg=(14, 34, 20))
    pop_line(d, lt, 0.85, 270, 1120, "LES SIRVIÓ", 90, GREEN, bg=(14, 34, 20))
    pop_line(d, lt, 1.6, 810, 1020, "A OTROS", 90, C, bg=(40, 14, 14))
    pop_line(d, lt, 1.75, 810, 1120, "LES MOLESTÓ", 90, R, bg=(40, 14, 14))
    pill(d, lt, 2.5, 540, 1350, 760, "POR ESO AHORA ELEGÍS VOS", fill=Y, ink=K, size=40, h=100)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 140, C)
    slide_line(d, lt, 0.3, 540, 480, "OCULTALOS", 160, Y)
    q = ease_in_out(prog(lt, 0.9, 0.35))
    if lt > 0.5:
        toggle_row(d, 110, 640, "Ocultar likes", q, sub="en la configuración de la app")
    slide_line(d, lt, 1.4, 540, 960, "¿Y VOS?", 150, C)
    slide_line(d, lt, 1.6, 540, 1110, "¿LOS ESCONDERÍAS?", 110, Y)
    slide_line(d, lt, 1.9, 540, 1240, "contame en los comentarios", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop")
for k in range(14): ev(0.3 + k * 0.15, "tick", 0.3 if k % 2 else -0.3)
ev(0.2, "pop", -0.3); ev(0.5, "thump"); ev(1.4, "tap")
ev(4.1, "tap", -0.3); ev(4.3, "pop", 0.3); ev(4.5, "tap"); ev(4.4, "pop"); ev(5.3, "swipe"); ev(6.3, "pop"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.3, "pop"); ev(8.4, "pop", 0.2); ev(9.0, "whoosh"); ev(10.2, "tap"); ev(10.35, "tap")
ev(12.1, "tap"); ev(12.4, "pop"); ev(13.0, "click", -0.3); ev(13.4, "click", 0.3); ev(13.6, "stamp"); ev(14.2, "tap"); ev(14.6, "tap")
ev(16.2, "swipe"); ev(16.5, "pop", -0.5); ev(16.7, "tap", -0.5); ev(17.4, "pop", 0.5); ev(17.6, "tap", 0.5); ev(18.5, "thump")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.5, "tap"); ev(20.9, "toggle"); ev(21.4, "pop"); ev(21.6, "thump"); ev(21.9, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
