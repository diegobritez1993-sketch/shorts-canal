"""Short 2026-11-28 20:00 — ¿Tu hijo duerme con el celu al lado? 20 min menos de sueño (Falbe et al., Pediatrics 2015)."""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Falbe et al., Pediatrics 2015"
BLUE = (90, 140, 255)

def bed(d, cx, cy, w, glow=0.0, t=0.0, kid=True):
    """Cama vista de costado con un chico tapado y un celu brillando en la mesita."""
    x0, x1 = cx - w / 2, cx + w / 2
    rrect(d, x0, cy - 40, x0 + 30, cy + 120, 10, fill=C)            # cabecera
    rrect(d, x0, cy + 20, x1, cy + 80, 16, fill=(80, 80, 80))       # colchón
    rrect(d, x1 - 24, cy + 20, x1, cy + 120, 8, fill=C)              # pie
    if kid:
        circle(d, x0 + 90, cy - 5, 42, fill=C)                       # cabeza
        rrect(d, x0 + 60, cy - 10, x1 - 30, cy + 40, 30, fill=BLUE)  # frazada
    # mesita + celu
    mx = x1 + 110
    rrect(d, mx - 70, cy + 10, mx + 70, cy + 120, 10, fill=K2, outline=C, width=5)
    if glow > 0:
        for k in range(3):
            r = 60 + k * 40 + 8 * math.sin(t * 6 + k)
            circle(d, mx, cy - 25, r, outline=mix(K, Y, glow * (0.6 - k * 0.18)), width=6)
    rrect(d, mx - 30, cy - 75, mx + 30, cy + 10, 10, fill=mix(K2, Y, glow), outline=C, width=4)

def b1(d, t):
    stars(d, t)
    e = ease_out(prog(t, 0.0, 0.35))
    if e > 0.02:
        moon(d, 860, 260, 90 * e)
        bed(d, 470, 610, 520 * e, glow=0.6 + 0.4 * math.sin(t * 7), t=t)
    pop_line(d, t, 0.0, 540, 1010, "¿TU HIJO DUERME", 130, C)
    pop_line(d, t, 0.3, 540, 1160, "CON EL CELU", 150, C)
    pop_line(d, t, 0.6, 540, 1330, "AL LADO?", 180, Y)
    slide_line(d, t, 1.5, 540, 1490, "un estudio midió cuánto le cuesta", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "PREGUNTARON A", 120, C)
    # grilla de chicos que se llena
    n = int(160 * ease_out(prog(lt, 0.3, 1.2)))
    for k in range(n):
        gx, gy = k % 16, k // 16
        person(d, 120 + gx * 56, 440 + gy * 52, 44, mix(K, C, 0.7))
    cnt = 2048 * ease_out(prog(lt, 0.3, 1.4))
    if lt > 0.3:
        sx, sy = shake(lt, 1.7, 0.3, 12)
        text_c(d, 540 + sx, 1090 + sy, fmt_num(cnt), "A", 230, Y)
    pop_line(d, lt, 1.7, 540, 1260, "CHICOS", 120, C)
    slide_line(d, lt, 2.1, 540, 1380, "de 4.º y 7.º grado (9 a 12 años)", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1440, "en escuelas públicas de EE.UU.", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1540, SRC, 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "MÁS DE LA MITAD", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "DORMÍA CERCA DE", 110, C)
    slide_line(d, lt, 0.45, 540, 540, "UN CELU O TABLET", 110, Y)
    p = ease_out(prog(lt, 0.7, 1.2))
    if lt > 0.7:
        e = back(prog(lt, 0.7, 0.35))
        donut(d, 540, 870, 230 * e, 0.54 * p, f"{int(54 * p)}%", col=Y)
    slide_line(d, lt, 2.1, 540, 1190, "y 3 de cada 4 tenían", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1252, "una tele en la pieza", 48, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO:", 120, C)
    # reloj al que le "comen" un pedazo
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        clock(d, 540, 640, 230 * e, prog(lt, 0.5, 1.2), turns=2, fill_deg=0)
        q = ease_out(prog(lt, 0.6, 1.0))
        if q > 0:
            r = 230 * e - 22
            d.pieslice([S(540 - r), S(640 - r), S(540 + r), S(640 + r)], -90, -90 + 120 * q, fill=R)
            circle(d, 540, 640, 16, fill=C)
    stamp(d, lt, 1.6, 540, 1000, 400, 100, "20 MIN MENOS", fill=R, ink=C, size=130)
    slide_line(d, lt, 2.0, 540, 1180, "de sueño cada noche de semana", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.15, 540, 1242, "(con la tele en la pieza: 18 menos)", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1340, "se iban a dormir más tarde", 48, Y, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1440, SRC, 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y AL OTRO DÍA", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "SIN PILAS", 150, Y)
    lvl = lerp(0.85, 0.15, ease_in_out(prog(lt, 0.5, 1.2)))
    if lt > 0.4:
        battery(d, 520, 690, 460, 220, lvl, mix(R, GREEN, (lvl - 0.15) / 0.7))
    slide_line(d, lt, 1.7, 540, 940, "con el celu al lado, más chicos", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.8, 540, 1002, "sentían que no habían descansado", 48, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.4, 540, 1160, 760, "OJO: ES RELACIÓN, NO CAUSA", fill=C, ink=K, size=40, h=96)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "EL CELU DUERME", 130, Y)
    slide_line(d, lt, 0.45, 540, 570, "AFUERA", 130, Y)
    q = ease_in_out(prog(lt, 0.9, 0.4))
    if lt > 0.6:
        toggle_row(d, 110, 690, "Cargador en el living", q, sub="no en la mesita de luz")
    slide_line(d, lt, 1.4, 540, 940, "y la tele, fuera del cuarto", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 1.8, 540, 1100, 960, "¿DÓNDE DUERME EL CELU EN TU CASA?", fill=Y, ink=K, size=42, h=110)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.0, "pop", -0.3); ev(0.3, "pop", 0.3); ev(0.6, "thump"); ev(1.0, "buzz", 0.4); ev(1.5, "tap")
ev(4.1, "tap")
for k in range(13): ev(4.3 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(5.7, "thump"); ev(5.7, "pop"); ev(6.1, "tap"); ev(6.2, "tap"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.45, "pop")
for k in range(10): ev(8.8 + k * 0.1, "tick", 0.2)
ev(10.1, "tap"); ev(10.2, "tap")
ev(12.1, "tap"); ev(12.3, "pop")
for k in range(8): ev(12.5 + k * 0.14, "tick", -0.2)
ev(13.4, "stamp"); ev(13.6, "thump"); ev(14.0, "tap"); ev(14.15, "tap"); ev(14.5, "pop"); ev(14.7, "tap")
ev(16.1, "tap"); ev(16.3, "pop")
for k in range(6): ev(16.6 + k * 0.2, "tick")
ev(17.7, "tap"); ev(17.8, "tap"); ev(18.4, "thump")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.45, "pop"); ev(20.9, "toggle"); ev(21.4, "tap"); ev(21.8, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
