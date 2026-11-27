"""Short 2026-11-27 15:00 — Curiosidades y hábitos.
¿Mirar fotos de gatitos te ayuda a concentrarte? ("el poder del kawaii")
Fuente: Nittono, Fukushima, Yano y Moriya, Univ. de Hiroshima, PLoS ONE 2012
(vía Association for Psychological Science, 30/01/2015, y Scientific American).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

PINK = (255, 140, 170)
SRC = "Nittono et al., Univ. de Hiroshima, PLoS ONE 2012"

def tri(d, pts, col):
    d.polygon([(S(x), S(y)) for x, y in pts], fill=col)

def kitten(d, cx, cy, s, col=C, cute=True, blink=0.0):
    """Cara de gatito (cute=True: ojos grandes, cara redonda) o gato adulto (ojos chicos, cara larga)."""
    hw = s * (0.5 if cute else 0.42)
    hh = s * (0.44 if cute else 0.5)
    ear = s * (0.3 if cute else 0.36)
    for sd in (-1, 1):
        tri(d, [(cx + sd * hw * 0.95, cy - hh * 0.15), (cx + sd * hw * 0.25, cy - hh * 0.8), (cx + sd * hw * 0.9, cy - hh - ear * 0.6)], col)
        tri(d, [(cx + sd * hw * 0.82, cy - hh * 0.3), (cx + sd * hw * 0.4, cy - hh * 0.72), (cx + sd * hw * 0.8, cy - hh - ear * 0.3)], PINK)
    d.ellipse([S(cx - hw), S(cy - hh), S(cx + hw), S(cy + hh)], fill=col)
    ey = cy - hh * (0.05 if cute else 0.15)
    er = s * (0.12 if cute else 0.06)
    for sd in (-1, 1):
        ex = cx + sd * hw * 0.42
        if blink > 0.5:
            d.line([S(ex - er), S(ey), S(ex + er), S(ey)], fill=K, width=S(8))
        else:
            circle(d, ex, ey, er, fill=K)
            if cute:
                circle(d, ex - er * 0.35, ey - er * 0.35, er * 0.33, fill=C)
            else:
                d.ellipse([S(ex - er * 0.25), S(ey - er * 0.9), S(ex + er * 0.25), S(ey + er * 0.9)], fill=Y)
    ny = cy + hh * (0.25 if cute else 0.3)
    tri(d, [(cx - s * 0.05, ny), (cx + s * 0.05, ny), (cx, ny + s * 0.045)], PINK)
    for sd in (-1, 1):
        for k in (-1, 0, 1):
            d.line([S(cx + sd * s * 0.12), S(ny + s * 0.04 + k * s * 0.03), S(cx + sd * s * 0.42), S(ny + k * s * 0.07)], fill=(90, 90, 90), width=S(4))
    if cute:
        for sd in (-1, 1):
            circle(d, cx + sd * hw * 0.62, ny + s * 0.02, s * 0.06, fill=mix(col, PINK, 0.6))

def tweezers(d, x, y, open_, col=C):
    """Pinza: punta en (x,y), se abre con open_ 0..1."""
    g = 10 + 26 * open_
    d.line([S(x - 4), S(y), S(x - 45 - g), S(y - 220)], fill=col, width=S(16))
    d.line([S(x + 4), S(y), S(x + 45 + g), S(y - 220)], fill=col, width=S(16))
    d.line([S(x - 45 - g), S(y - 220), S(x + 45 + g), S(y - 220)], fill=col, width=S(16))

def magnifier(d, cx, cy, r, col=Y):
    circle(d, cx, cy, r, outline=col, width=22)
    a = math.radians(45)
    d.line([S(cx + math.cos(a) * r), S(cy + math.sin(a) * r), S(cx + math.cos(a) * r * 1.9), S(cy + math.sin(a) * r * 1.9)], fill=col, width=S(40))

def check(d, cx, cy, s, col=GREEN, p=1.0):
    pts = [(cx - s * 0.4, cy), (cx - s * 0.1, cy + s * 0.3), (cx + s * 0.45, cy - s * 0.35)]
    if p <= 0: return
    if p < 0.5:
        q = p * 2
        d.line([S(pts[0][0]), S(pts[0][1]), S(lerp(pts[0][0], pts[1][0], q)), S(lerp(pts[0][1], pts[1][1], q))], fill=col, width=int(S(s * 0.14)))
    else:
        q = (p - 0.5) * 2
        d.line([S(pts[0][0]), S(pts[0][1]), S(pts[1][0]), S(pts[1][1]), S(lerp(pts[1][0], pts[2][0], q)), S(lerp(pts[1][1], pts[2][1], q))], fill=col, width=int(S(s * 0.14)), joint="curve")

# ---------- escenas ----------
def b1(d, t):
    e = back(prog(t, 0.0, 0.45))
    if e > 0.02:
        for k in range(5, 0, -1):
            circle(d, 540, 760, 150 + k * 30 * e, fill=mix(K, PINK, 0.035 * (6 - k) * e))
        blink = 1.0 if 2.3 < t < 2.45 else 0.0
        kitten(d, 540, 760 + math.sin(t * 3) * 8, 360 * e, cute=True, blink=blink)
    pop_line(d, t, 0.1, 540, 210, "¿MIRÁS FOTOS", 140, C)
    pop_line(d, t, 0.35, 540, 360, "DE GATITOS?", 150, Y)
    pop_line(d, t, 1.3, 540, 1090, "PUEDE QUE TE AYUDEN", 96, C)
    pop_line(d, t, 1.6, 540, 1230, "A CONCENTRARTE", 140, Y)
    slide_line(d, t, 2.4, 540, 1370, "y lo dice un estudio en serio", 46, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "UNIVERSIDAD", 110, C)
    slide_line(d, lt, 0.25, 540, 400, "DE HIROSHIMA", 130, Y)
    n = int(132 * ease_out(prog(lt, 0.6, 1.3)))
    # grilla de personitas que se van encendiendo
    for i in range(36):
        r_, c_ = divmod(i, 9)
        x, y = 150 + c_ * 97, 560 + r_ * 125
        on = i < n / 132 * 36
        person(d, x, y + 40, 95, Y if on else (55, 55, 55))
    pop_line(d, lt, 0.6, 540, 1160, fmt_num(n), 200, C, dur=0.25)
    pop_line(d, lt, 0.9, 540, 1320, "ESTUDIANTES", 120, C)
    pill(d, lt, 2.2, 540, 1470, 560, "3 EXPERIMENTOS", fill=Y, ink=K, size=46, h=100)
    slide_line(d, lt, 2.5, 540, 1600, SRC, 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "UN JUEGO", 120, C)
    slide_line(d, lt, 0.25, 540, 400, "CON PINZAS", 140, Y)
    slide_line(d, lt, 0.5, 540, 510, "sacar piezas sin tocar los bordes", 46, C, kind="SemiBold", dy=25)
    e = ease_out(prog(lt, 0.4, 0.4))
    if e > 0.02:
        rrect(d, 200, 700 + 300 * (1 - e), 880, 1260 + 300 * (1 - e), 50, fill=K2, outline=C, width=6)
        circle(d, 540, 1040, 120 * e, fill=K, outline=R if 1.6 < lt < 1.9 else (70, 70, 70), width=10)
        # pieza que sube con la pinza
        up = ease_in_out(prog(lt, 1.9, 1.0))
        tip_y = lerp(760, 1020, ease_out(prog(lt, 0.6, 0.6))) - 180 * up
        py = 1055 if lt < 1.9 else tip_y + 35
        rrect(d, 505, py - 30, 575, py + 30, 14, fill=Y)
        sx, sy = shake(lt, 1.6, 0.3, 10)
        tweezers(d, 540 + sx, tip_y + sy, 0.2 if lt > 1.3 else 0.8)
    if 1.6 < lt < 2.0:
        pop_line(d, lt, 1.6, 810, 800, "¡BZZ!", 90, R, dur=0.15)
    pill(d, lt, 2.7, 540, 1420, 640, "48 ESTUDIANTES, 2 RONDAS", fill=C, ink=K, size=40, h=96)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 240, "ENTRE RONDA Y RONDA", 100, C)
    slide_line(d, lt, 0.3, 540, 350, "VIERON 7 FOTOS", 120, Y)
    for k, (x, cute, lab1, lab2, t0) in enumerate([(290, True, "CACHORROS", "Y GATITOS", 0.6), (790, False, "PERROS Y", "GATOS ADULTOS", 0.9)]):
        e = back(prog(lt, t0, 0.4))
        if e > 0.02:
            rrect(d, x - 230 * e, 470, x + 230 * e, 1260, 40, fill=K2)
            kitten(d, x, 720, 300 * e, col=C if cute else (200, 190, 170), cute=cute)
        slide_line(d, lt, t0 + 0.3, x, 960, lab1, 62, C, dy=25)
        slide_line(d, lt, t0 + 0.35, x, 1030, lab2, 62 if cute else 52, C, dy=25)
    # resultado
    p = prog(lt, 1.9, 0.5)
    if p > 0:
        check(d, 290, 1150, 140, GREEN, p)
        text_c(d, 790, 1150, "=", "A", 140, G, alpha=clamp(p * 2))
    pop_line(d, lt, 2.3, 290, 1370, "MEJORARON", 84, GREEN)
    pop_line(d, lt, 2.5, 790, 1370, "IGUAL QUE ANTES", 62, G)
    slide_line(d, lt, 2.8, 540, 1520, "en la segunda ronda del juego", 44, C, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 260, "MÁS DESPACIO", 130, C)
    pop_line(d, lt, 0.3, 540, 410, "Y CON MÁS CUIDADO", 120, Y)
    # lupa que achica el foco sobre una grilla de números
    rnd = __import__("random").Random(5)
    foc = ease_in_out(prog(lt, 0.8, 1.2))
    for r_ in range(5):
        for c_ in range(7):
            x, y = 180 + c_ * 120, 600 + r_ * 100
            dist = math.hypot(x - 540, y - 800)
            vis = 1.0 if dist < 140 else 1 - 0.75 * foc
            text_c(d, x, y, str(rnd.randint(0, 9)), "Black", 64, mix(K, C, vis))
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        magnifier(d, 540, 800, lerp(260, 150, foc) * e)
    pop_line(d, lt, 2.0, 540, 1250, "TE ENFOCA", 150, C)
    slide_line(d, lt, 2.4, 540, 1380, "las fotos de comida rica no ayudaron", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1460, SRC, 34, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "ANTES DE ALGO DIFÍCIL", 100, Y)
    slide_line(d, lt, 0.45, 540, 560, "MIRÁ ALGO TIERNO", 120, Y)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        phone(d, 540, 900, 230 * e, 400 * e, body=K2)
        if e > 0.6:
            kitten(d, 540, 910, 170 * e, cute=True, blink=1.0 if 1.8 < lt < 1.95 else 0.0)
    slide_line(d, lt, 0.9, 540, 1150, "un ratito y después, a lo tuyo", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 1.6, 540, 1320, 880, "¿CUÁL ES TU FONDO DE PANTALLA?", fill=C, ink=K, size=42, h=104)
    slide_line(d, lt, 2.0, 540, 1450, "contalo en los comentarios", 44, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.1, "pop", -0.3); ev(0.35, "pop", 0.3); ev(1.3, "tap", -0.2); ev(1.6, "thump"); ev(2.3, "click", 0.2); ev(2.4, "tap")
ev(4.1, "tap", -0.3); ev(4.25, "tap", 0.3)
for k in range(12): ev(4.6 + k * 0.11, "tick", 0.3 if k % 2 else -0.3)
ev(4.9, "pop"); ev(6.2, "toggle"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.25, "pop"); ev(8.5, "tap"); ev(8.6, "swipe"); ev(9.6, "buzz", 0.3); ev(9.9, "click"); ev(10.7, "pop")
ev(12.1, "tap"); ev(12.3, "pop"); ev(12.6, "pop", -0.4); ev(12.9, "pop", 0.4); ev(13.9, "ding", -0.4); ev(14.3, "thump", -0.3); ev(14.5, "tap", 0.3); ev(14.8, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.6, "pop")
for k in range(6): ev(16.9 + k * 0.18, "rustle", 0.2 if k % 2 else -0.2)
ev(18.0, "stamp"); ev(18.4, "tap"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.6, "shimmer"); ev(20.9, "tap"); ev(21.6, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
