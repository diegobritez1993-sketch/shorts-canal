"""Short 2026-11-12 15:00 — Cómo te enganchan las apps: los colores del celu te llaman; en escala de grises lo usás menos.

Fuente: Holte y Ferraro, Univ. de Dakota del Norte, "True colors: Grayscale setting reduces screen time in college students",
The Social Science Journal (2020). Vía CNN (11/06/2020) y Univ. de Cincinnati (UC Blue Ash, oct. 2022).
- Primer estudio: ~220 universitarios; con el celular en escala de grises, el tiempo de pantalla bajó en promedio 39 min por día
  ("casi 40 minutos"). Menos tiempo en internet y en redes sociales.
- Seguimiento (~135 participantes): baja significativa del tiempo de pantalla y menos ganas de revisar notificaciones.
- Idea: los colores fuertes de íconos y avisos atraen la atención; sin color, usar el celu resulta menos gratificante.
  El efecto varía según la persona.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

ICON_COLS = [(255, 59, 48), (52, 199, 89), (10, 132, 255), (255, 159, 10), (191, 90, 242), (255, 45, 85),
             (100, 210, 255), (255, 214, 10), (48, 209, 88), (94, 92, 230), (255, 105, 180), (255, 149, 0)]

def gray(c, g):
    """Mezcla un color hacia su gris (g 0..1)."""
    l = int(0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2])
    return mix(c, (l, l, l), g)

def app_grid(d, cx, cy, w, h, g=0.0, t=0.0, appear=1.0, badges=0.0, glow=0.0):
    """Pantalla de celu con grilla de íconos genéricos (sin marcas)."""
    phone(d, cx, cy, w, h)
    cols, rows = 3, 4
    s = w * 0.22
    gx = (w - 2 * s * 1.0) / 4
    for k in range(cols * rows):
        q = back(clamp(appear * 2.2 - k * 0.1))
        if q <= 0.02: continue
        i, j = k % cols, k // cols
        x = cx + (i - 1) * (s + gx * 0.9)
        y = cy - h * 0.3 + j * (s + gx * 0.9)
        pul = 1 + 0.06 * glow * math.sin(t * 7 + k)
        hs = s / 2 * q * pul
        col = gray(ICON_COLS[k], g)
        rrect(d, x - hs, y - hs, x + hs, y + hs, hs * 0.45, fill=col)
        # glifo simple dentro del ícono
        circle(d, x, y, hs * 0.32, fill=mix(col, C, 0.7))
        if badges > 0 and k in (0, 4, 7, 10):
            b = back(clamp(badges * 2 - (k % 3) * 0.3))
            if b > 0.02:
                circle(d, x + hs * 0.85, y - hs * 0.85, 26 * b, fill=gray(R, g))
                text_c(d, x + hs * 0.85, y - hs * 0.85, str(k % 9 + 1), "Black", 30 * b, C, bg=gray(R, g))

def b1(d, t):
    g = ease_in_out(prog(t, 2.0, 0.8))
    e = ease_out(prog(t, 0.0, 0.35))
    if e > 0.02:
        app_grid(d, 540, 520, 420, 640, g=g, t=t, appear=prog(t, 0.0, 1.0), badges=prog(t, 0.6, 0.6), glow=1 - g)
    pop_line(d, t, 0.1, 540, 1000, "PONÉ TU CELU", 150, C)
    pop_line(d, t, 0.4, 540, 1150, "EN BLANCO", 160, Y)
    pop_line(d, t, 0.6, 540, 1300, "Y NEGRO", 160, Y)
    pill(d, t, 2.4, 540, 1470, 560, "Y MIRÁ QUÉ PASA", fill=R, ink=C, size=46, h=96)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "LOS COLORES", 140, C)
    slide_line(d, lt, 0.3, 540, 420, "TE LLAMAN", 140, Y)
    # íconos flotando que "gritan"
    for k in range(6):
        q = back(prog(lt, 0.5 + k * 0.12, 0.35))
        if q <= 0.02: continue
        a = k / 6 * math.tau + lt * 0.6
        x = 540 + math.cos(a) * 280
        y = 860 + math.sin(a) * 200
        hs = 70 * q * (1 + 0.08 * math.sin(lt * 9 + k))
        rrect(d, x - hs, y - hs, x + hs, y + hs, hs * 0.45, fill=ICON_COLS[k * 2])
        circle(d, x, y, hs * 0.32, fill=mix(ICON_COLS[k * 2], C, 0.7))
    # punto rojo central que late
    p = back(prog(lt, 1.4, 0.3))
    if p > 0.02:
        pr = 1 + 0.15 * math.sin(lt * 10)
        for k in range(3):
            rr = (lt * 120 + k * 60) % 180
            circle(d, 540, 860, 70 + rr, outline=mix(K, R, 1 - rr / 180), width=6)
        circle(d, 540, 860, 70 * p * pr, fill=R)
        text_c(d, 540, 860, "9+", "Black", 54 * p, C, bg=R)
    slide_line(d, lt, 2.2, 540, 1210, "íconos brillantes y avisos rojos", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1280, "están hechos para atraer tu mirada", 46, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 290, "LO PROBARON", 130, C)
    pop_line(d, lt, 0.35, 540, 420, "CON ~220", 120, Y)
    slide_line(d, lt, 0.6, 540, 520, "estudiantes universitarios", 46, C, kind="SemiBold", dy=25)
    # toggle de escala de grises
    q = ease_in_out(prog(lt, 1.4, 0.35))
    sl = ease_out(prog(lt, 0.8, 0.35))
    if sl > 0:
        toggle_row(d, 110 + (1 - sl) * 600, 640, "Escala de grises", q, sub="ajustes del celu")
    # mini celu que pasa a gris
    e = ease_out(prog(lt, 1.0, 0.4))
    if e > 0.02:
        app_grid(d, 540, 1170, 300 * e, 440 * e, g=ease_in_out(prog(lt, 1.5, 0.6)), t=lt, appear=1.0)
    slide_line(d, lt, 2.4, 540, 1460, "y midieron su tiempo de pantalla", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1530, "Holte y Ferraro, Univ. de Dakota del Norte, 2020", 32, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO", 140, C)
    pr = prog(lt, 0.4, 1.4)
    if lt > 0.3:
        clock(d, 540, 640, 210, ease_out(pr), turns=2, fill_deg=234)
    n = int(39 * ease_out(pr))
    if lt > 0.4:
        text_c(d, 540, 935, f"-{n} MIN", "A", 190, Y)
    sx, sy = shake(lt, 2.0, 0.35, 14)
    stamp(d, lt, 1.95, 540 + sx, 1185 + sy, 280, 90, "POR DÍA", fill=R, ink=C, size=130)
    slide_line(d, lt, 2.5, 540, 1350, "casi 40 minutos menos de celu", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1420, "sobre todo en redes e internet", 46, Y, kind="Bold", dy=25)
    slide_line(d, lt, 2.9, 540, 1495, "The Social Science Journal (vía CNN)", 32, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "¿POR QUÉ", 140, C)
    pop_line(d, lt, 0.3, 540, 430, "FUNCIONA?", 140, Y)
    # barra de "premio" que se vacía al quitar color
    x0, x1, y = 170, 910, 700
    rrect(d, x0, y - 55, x1, y + 55, 55, outline=C, width=8)
    lvl = 1.0 - 0.7 * ease_in_out(prog(lt, 1.2, 1.0))
    if lt > 0.6:
        fw = (x1 - x0 - 30) * lvl * ease_out(prog(lt, 0.6, 0.4))
        n = len(ICON_COLS)
        seg = fw / n
        g = ease_in_out(prog(lt, 1.2, 1.0))
        for k in range(n):
            if seg * (k + 1) < 2: continue
            rrect(d, x0 + 15 + seg * k, y - 40, x0 + 15 + seg * (k + 1), y + 40, 12, fill=gray(ICON_COLS[k], g))
    slide_line(d, lt, 0.6, 540, 810, "premio para tu cerebro", 40, G, kind="SemiBold", dy=15)
    slide_line(d, lt, 2.1, 540, 960, "sin color, el celu", 56, C, kind="Bold", dy=25)
    slide_line(d, lt, 2.25, 540, 1040, "se vuelve aburrido", 56, Y, kind="Bold", dy=25)
    pill(d, lt, 2.7, 540, 1200, 820, "MENOS GANAS DE VER AVISOS", fill=K2, ink=C, size=42, h=96)
    slide_line(d, lt, 3.0, 540, 1300, "(en el estudio de seguimiento)", 34, G, kind="SemiBold", dy=15)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "PROBALO:", 120, Y)
    slide_line(d, lt, 0.35, 540, 420, "buscá \"escala de grises\"", 50, C, kind="Bold", dy=25)
    slide_line(d, lt, 0.5, 540, 490, "en los ajustes de tu celu", 50, C, kind="Bold", dy=25)
    pop_line(d, lt, 1.3, 540, 780, "¿TE ANIMÁS", 140, C)
    pop_line(d, lt, 1.55, 540, 930, "UNA SEMANA?", 140, Y)
    pill(d, lt, 2.0, 380, 1110, 220, "SÍ", fill=GREEN, ink=K, size=56, h=100)
    pill(d, lt, 2.15, 700, 1110, 220, "NO", fill=R, ink=C, size=56, h=100)
    slide_line(d, lt, 2.4, 540, 1250, "respondé en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.1, "pop"); ev(0.4, "thump"); ev(0.6, "pop", 0.2)
for k in range(6): ev(0.1 + k * 0.12, "tap", -0.5 + k * 0.2)
for k in range(4): ev(0.65 + k * 0.15, "pop", 0.3 - k * 0.15)
ev(2.0, "toggle"); ev(2.1, "shimmer"); ev(2.4, "click")
ev(4.1, "swipe"); ev(4.3, "swipe")
for k in range(6): ev(4.5 + k * 0.12, "pop", -0.5 + k * 0.2)
ev(5.4, "buzz"); ev(5.45, "ding"); ev(6.2, "tap"); ev(6.4, "tap")
ev(8.1, "pop"); ev(8.35, "thump"); ev(8.6, "tap"); ev(8.8, "swipe"); ev(9.4, "toggle"); ev(9.5, "shimmer"); ev(10.4, "tap"); ev(10.6, "tap")
ev(12.1, "swipe")
for k in range(13): ev(12.4 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(13.95, "stamp"); ev(14.5, "tap"); ev(14.7, "tap"); ev(14.9, "tap")
ev(16.1, "pop"); ev(16.3, "thump"); ev(16.6, "click")
for k in range(5): ev(17.2 + k * 0.2, "tick", 0.3 - k * 0.15)
ev(18.1, "tap"); ev(18.25, "tap"); ev(18.7, "click"); ev(19.0, "tap")
ev(20.1, "swipe"); ev(20.35, "tap"); ev(20.5, "tap"); ev(21.3, "pop"); ev(21.55, "thump"); ev(22.0, "pop", -0.3); ev(22.15, "pop", 0.3); ev(22.4, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
