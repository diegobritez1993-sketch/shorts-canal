"""Short: ¿Cuánta pantalla puede ver un chico según la OMS?
Fuente: OMS, guías de actividad física, sedentarismo y sueño para menores de 5 años (24/04/2019).
https://www.who.int/news/item/24-04-2019-to-grow-up-healthy-children-need-to-sit-less-and-play-more
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "OMS, guía para menores de 5 años, 2019"

def tv(d, cx, cy, w, h, glow=0.0, t=0.0):
    """Tele simple con patas y antena."""
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 30, fill=K2, outline=C, width=10)
    rrect(d, cx - w / 2 + 34, cy - h / 2 + 34, cx + w / 2 - 34, cy + h / 2 - 34, 18, fill=mix(K2, (60, 90, 140), glow))
    d.line([S(cx - w * 0.25), S(cy + h / 2), S(cx - w * 0.32), S(cy + h / 2 + 50)], fill=C, width=S(10))
    d.line([S(cx + w * 0.25), S(cy + h / 2), S(cx + w * 0.32), S(cy + h / 2 + 50)], fill=C, width=S(10))
    d.line([S(cx), S(cy - h / 2), S(cx - 70), S(cy - h / 2 - 90)], fill=C, width=S(8))
    d.line([S(cx), S(cy - h / 2), S(cx + 70), S(cy - h / 2 - 90)], fill=C, width=S(8))

def baby(d, cx, cy, s, col=C):
    """Bebé: cabeza grande con rulito + cuerpito."""
    circle(d, cx, cy - s * 0.2, s * 0.3, fill=col)
    d.arc([S(cx - s * 0.06), S(cy - s * 0.62), S(cx + s * 0.1), S(cy - s * 0.46)], 180, 450, fill=col, width=S(8))
    circle(d, cx - s * 0.1, cy - s * 0.22, s * 0.035, fill=K)
    circle(d, cx + s * 0.1, cy - s * 0.22, s * 0.035, fill=K)
    rrect(d, cx - s * 0.24, cy + s * 0.12, cx + s * 0.24, cy + s * 0.5, s * 0.15, fill=col)

def book(d, cx, cy, s, open_p=1.0):
    a = lerp(0.15, 1.0, open_p)
    d.polygon([(S(cx), S(cy - s * 0.3)), (S(cx - s * 0.5 * a), S(cy - s * 0.38)), (S(cx - s * 0.5 * a), S(cy + s * 0.3)), (S(cx), S(cy + s * 0.38))], fill=C)
    d.polygon([(S(cx), S(cy - s * 0.3)), (S(cx + s * 0.5 * a), S(cy - s * 0.38)), (S(cx + s * 0.5 * a), S(cy + s * 0.3)), (S(cx), S(cy + s * 0.38))], fill=Y)
    for k in range(3):
        yy = cy - s * 0.18 + k * s * 0.16
        d.line([S(cx - s * 0.4 * a), S(yy), S(cx - s * 0.08), S(yy + s * 0.03)], fill=G, width=S(6))

# 0-4: gancho
def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        baby(d, 400, 560, 330 * e)
        phone(d, 700, 560, 170 * e, 300 * e, buzz=1.0 if 0.4 < t < 1.6 else 0.0, t=t)
    pop_line(d, t, 0.3, 540, 960, "¿CUÁNTA PANTALLA", 125, C)
    pop_line(d, t, 0.6, 540, 1110, "PUEDE VER", 135, C)
    pop_line(d, t, 0.9, 540, 1270, "UN CHICO?", 170, Y)
    pill(d, t, 2.4, 540, 1460, 620, "SEGÚN LA OMS", size=46)

# 4-8: menos de 1 año = cero
def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "BEBÉS DE", 110, C)
    slide_line(d, lt, 0.3, 540, 430, "MENOS DE 1 AÑO", 120, Y)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        tv(d, 540, 790, 420 * e, 300 * e, glow=1.0)
        ban(d, 540, 790, 270 * e, ease_out(prog(lt, 1.2, 0.35)), width=30)
    stamp(d, lt, 2.0, 540, 1170, 230, 95, "CERO", fill=R, ink=C, size=140)
    slide_line(d, lt, 2.5, 540, 1340, "no se recomienda nada de pantalla", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1410, SRC, 34, G, kind="SemiBold", dy=20)

# 8-12: 1 año, tampoco
def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 320, "¿Y CON 1 AÑO?", 140, C)
    rows = [("Tele", 0.6), ("Videos", 1.1), ("Jueguitos", 1.6)]
    for k, (lab, t0) in enumerate(rows):
        p = prog(lt, t0, 0.3)
        if p <= 0: continue
        x0 = lerp(1200, 110, ease_out(p))
        # arranca prendido y se apaga
        q = 1 - ease_in_out(prog(lt, t0 + 0.4, 0.25))
        toggle_row(d, x0, 520 + k * 190, lab, q)
    pop_line(d, lt, 2.4, 540, 1180, "TAMPOCO", 190, R)
    slide_line(d, lt, 2.8, 540, 1340, "pantalla sentado, todavía no", 46, C, kind="SemiBold", dy=25)

# 12-16: 2 a 4 años, máximo 1 hora
def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "DE 2 A 4 AÑOS", 130, Y)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        pr = ease_in_out(prog(lt, 0.7, 1.4))
        clock(d, 540, 700, 230 * e, pr, turns=1, fill_deg=360)
    sx, sy = shake(lt, 2.25, 0.35, 16)
    pop_line(d, lt, 2.1, 540 + sx, 1080 + sy, "MÁXIMO 1 HORA", 150, C)
    slide_line(d, lt, 2.4, 540, 1210, "por día, mirando sentado", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.8, 540, 1360, 600, "Y MENOS ES MEJOR", fill=Y, size=44)

# 16-20: lo que sí: 180 min de juego + cuentos
def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "LO QUE SÍ PIDE:", 120, C)
    base = 1060
    # barras: juego 180 vs pantalla 60 (máx)
    p = ease_out(prog(lt, 0.5, 1.2))
    hj, hp = 450 * p, 450 / 3 * p
    rrect(d, 250, base - hj, 470, base, 24, fill=Y)
    rrect(d, 610, base - hp, 830, base, 24, fill=(80, 80, 80))
    if p > 0.05:
        text_c(d, 360, base - hj - 60, f"{int(180 * p)} MIN", "A", 80, Y)
        text_c(d, 720, base - hp - 60, f"{int(60 * p)} MIN", "A", 70, C)
    slide_line(d, lt, 0.8, 360, base + 50, "jugar y moverse", 36, C, kind="Bold", dy=15)
    slide_line(d, lt, 0.9, 720, base + 50, "pantalla (tope)", 36, G, kind="Bold", dy=15)
    eb = back(prog(lt, 2.0, 0.4))
    if eb > 0.02:
        book(d, 260, 1330, 200 * eb, open_p=ease_out(prog(lt, 2.1, 0.5)))
    slide_line(d, lt, 2.2, 640, 1295, "Y SI ESTÁ QUIETO:", 70, C, dy=20)
    slide_line(d, lt, 2.4, 640, 1380, "LEERLE UN CUENTO", 70, Y, dy=20)
    slide_line(d, lt, 2.8, 540, 1520, SRC, 34, G, kind="SemiBold", dy=20)

# 20-23.2: pregunta para comentar
def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 420, "¿EN TU CASA", 150, C)
    slide_line(d, lt, 0.3, 540, 580, "SE CUMPLE?", 170, Y)
    for k, (lab, col, ink, t0) in enumerate([("SÍ", GREEN, K, 0.8), ("NO", R, C, 1.0)]):
        p = prog(lt, t0, 0.3)
        if p <= 0: continue
        cx = 330 + k * 420
        bw = 170 * back(p)
        rrect(d, cx - bw, 800, cx + bw, 960, 80, fill=col)
        if p > 0.5: text_c(d, cx, 878, lab, "A", 100, ink, bg=col)
    slide_line(d, lt, 1.6, 540, 1080, "respondé en los comentarios", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.9, 540, 1150, "y pasáselo a alguien con chicos", 44, G, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
for k in range(4): ev(0.45 + k * 0.3, "buzz", 0.3)
ev(0.3, "pop", -0.3); ev(0.6, "pop", 0.3); ev(0.9, "thump"); ev(2.4, "pop")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3); ev(4.5, "pop"); ev(5.2, "swipe")
ev(5.8, "stamp"); ev(6.5, "tap")
ev(8.1, "pop")
for t0 in (0.6, 1.1, 1.6): ev(8 + t0, "swipe", 0.3); ev(8 + t0 + 0.42, "toggle", -0.2)
ev(10.4, "thump"); ev(10.8, "tap")
ev(12.1, "tap"); ev(12.3, "pop")
for k in range(12): ev(12.7 + k * 1.4 / 12, "tick", 0.3 if k % 2 else -0.3)
ev(14.1, "stamp"); ev(14.4, "tap"); ev(14.8, "pop")
ev(16.1, "tap")
for k in range(8): ev(16.5 + k * 0.15, "tick", 0.3 if k % 2 else -0.3)
ev(17.7, "thump"); ev(18.0, "pop"); ev(18.1, "rustle"); ev(18.2, "tap", 0.2); ev(18.4, "tap", -0.2)
ev(20.1, "pop"); ev(20.3, "thump"); ev(20.8, "pop", -0.3); ev(21.0, "pop", 0.3); ev(21.6, "tap"); ev(21.9, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
