"""Short 2026-11-20 15:00 — Cómo te enganchan las apps: los juegos "gratis" los pagan unos pocos ("ballenas").

Fuente:
- Swrve, Mobile Games Monetization Report (comunicado PR Newswire, San Francisco, 26/02/2014).
  Datos de un mes (enero 2014), decenas de millones de jugadores de juegos gratuitos (free-to-play):
  solo 1,5% de los jugadores activos hizo una compra dentro del juego ese mes;
  apenas 0,15% de los jugadores aportó el 50% de la plata de compras dentro del juego;
  compra promedio US$ 5,94; la primera compra llega, en promedio, en poco menos de 24 horas.
  ("Ballenas" = término de la industria para los que más gastan.)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

BLUE = (90, 160, 230)

def gamepad(d, cx, cy, s, col=C, ink=K):
    """Joystick genérico."""
    rrect(d, cx - s * 0.5, cy - s * 0.22, cx + s * 0.5, cy + s * 0.22, s * 0.2, fill=col)
    circle(d, cx - s * 0.36, cy + s * 0.12, s * 0.2, fill=col)
    circle(d, cx + s * 0.36, cy + s * 0.12, s * 0.2, fill=col)
    # cruz
    d.rectangle([S(cx - s * 0.36 - s * 0.03), S(cy - s * 0.12), S(cx - s * 0.36 + s * 0.03), S(cy + s * 0.08)], fill=ink)
    d.rectangle([S(cx - s * 0.46), S(cy - s * 0.05), S(cx - s * 0.26), S(cy + s * 0.01)], fill=ink)
    # botones
    for dx, dy, c in ((0.3, -0.05, R), (0.4, 0.04, Y), (0.2, 0.04, GREEN)):
        circle(d, cx + s * dx, cy + s * dy, s * 0.045, fill=c)

def coin(d, cx, cy, r, col=Y):
    circle(d, cx, cy, r, fill=col)
    circle(d, cx, cy, r * 0.72, outline=mix(col, K, 0.35), width=int(max(2, r * 0.12)))
    text_c(d, cx, cy, "$", "Black", r * 1.0, mix(col, K, 0.55), bg=col)

def whale(d, cx, cy, s, col=BLUE, t=0.0):
    """Ballena simple con primitivas."""
    d.ellipse([S(cx - s * 0.5), S(cy - s * 0.26), S(cx + s * 0.36), S(cy + s * 0.24)], fill=col)
    # cola
    wv = math.sin(t * 5) * s * 0.05
    d.polygon([(S(cx + s * 0.3), S(cy)), (S(cx + s * 0.62), S(cy - s * 0.24 + wv)), (S(cx + s * 0.55), S(cy + wv)), (S(cx + s * 0.62), S(cy + s * 0.2 + wv))], fill=col)
    # panza
    d.chord([S(cx - s * 0.46), S(cy - s * 0.05), S(cx + s * 0.3), S(cy + s * 0.24)], 0, 180, fill=mix(col, C, 0.55))
    circle(d, cx - s * 0.28, cy - s * 0.06, s * 0.035, fill=K)
    # chorro
    for k in (-1, 0, 1):
        d.line([S(cx - s * 0.12), S(cy - s * 0.27), S(cx - s * 0.12 + k * s * 0.09), S(cy - s * 0.45)], fill=C, width=SW(8))

def b1(d, t):
    pop_line(d, t, 0.0, 540, 300, "¿ESE JUEGO", 160, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 470, "ES GRATIS?", 185, Y, dur=0.25)
    e = back(prog(t, 0.6, 0.35))
    if e > 0.02:
        gamepad(d, 540, 900, 560 * e)
    # monedas que caen dentro del joystick
    for k in range(5):
        p = prog(t, 1.4 + k * 0.25, 0.45)
        if 0 < p < 1:
            coin(d, 400 + k * 70, lerp(620, 860, ease_in_out(p)), 40, Y)
    slide_line(d, t, 2.7, 540, 1250, "ALGUIEN LO ESTÁ PAGANDO", 92, R, dy=30)
    slide_line(d, t, 3.0, 540, 1360, "y casi nunca sos vos", 50, C, kind="SemiBold", dy=20)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "EN UN MES", 140, C)
    slide_line(d, lt, 0.35, 540, 390, "decenas de millones de jugadores de juegos gratis", 37, C, kind="SemiBold", dy=20)
    # grilla de 200 personitas: 3 = 1,5%
    cols, rows = 20, 10
    for i in range(cols * rows):
        r_, c_ = divmod(i, cols)
        p = prog(lt, 0.6 + i * 0.004, 0.2)
        if p <= 0: continue
        x = 160 + c_ * 40; y = 520 + r_ * 48
        pay = i in (47, 112, 168)
        col = Y if (pay and lt > 1.8) else (75, 75, 75)
        rr = 13 * back(p) * (1.25 if pay and lt > 1.8 else 1)
        circle(d, x, y - 8, rr * 0.55, fill=col)
        d.pieslice([S(x - rr * 0.8), S(y), S(x + rr * 0.8), S(y + rr * 1.5)], 180, 360, fill=col)
    pop_line(d, lt, 1.8, 540, 1110, "SOLO 1,5%", 150, Y)
    slide_line(d, lt, 2.2, 540, 1230, "compró algo dentro del juego ese mes", 46, C, kind="Bold", dy=20)
    slide_line(d, lt, 2.6, 540, 1310, "Swrve, informe de monetización, datos de enero 2014", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "Y LA MITAD DE LA PLATA", 100, C)
    slide_line(d, lt, 0.35, 540, 370, "la pone apenas", 46, C, kind="SemiBold", dy=20)
    stamp(d, t, 8.8, 540, 500, 300, 100, "0,15%", fill=Y, ink=K, size=150)
    slide_line(d, lt, 1.2, 540, 640, "de los jugadores", 50, C, kind="Bold", dy=20)
    # ballena
    e = back(prog(lt, 1.6, 0.4))
    if e > 0.02:
        bob = math.sin(lt * 3) * 12
        whale(d, 540, 950 + bob, 520 * e, BLUE, lt)
    slide_line(d, lt, 2.3, 540, 1150, "en la industria les dicen", 46, C, kind="SemiBold", dy=20)
    pop_line(d, lt, 2.5, 540, 1260, "\"BALLENAS\"", 120, BLUE)
    slide_line(d, lt, 2.8, 540, 1370, "Swrve, comunicado del 26/02/2014", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "Y NO TARDA", 140, C)
    slide_line(d, lt, 0.35, 540, 390, "la primera compra llega, en promedio, en", 42, C, kind="SemiBold", dy=20)
    p = prog(lt, 0.6, 1.4)
    if lt > 0.5:
        clock(d, 540, 700, 210, ease_in_out(p), turns=2, fill_deg=345)
    pop_line(d, lt, 2.0, 540, 1010, "MENOS DE 24 HORAS", 120, Y)
    pill(d, t, 14.6, 540, 1170, 860, "COMPRA PROMEDIO: US$ 5,94", fill=C, ink=K, size=44, h=110)
    slide_line(d, lt, 3.0, 540, 1290, "Swrve, ene. 2014", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "EL TRUCO", 150, Y)
    slide_line(d, lt, 0.35, 540, 400, "ponele freno antes de que te agarre", 46, C, kind="SemiBold", dy=20)
    p1 = prog(lt, 0.6, 0.3)
    if p1 > 0:
        q = 1 - ease_in_out(prog(lt, 1.1, 0.3))
        toggle_row(d, 110, 520, "Compras en apps", q, sub="desactivadas" if q < 0.5 else "permitidas")
    p2 = prog(lt, 1.6, 0.3)
    if p2 > 0:
        q2 = ease_in_out(prog(lt, 2.0, 0.3))
        toggle_row(d, 110, 720, "Pedir contraseña", q2, sub="en cada compra")
    slide_line(d, lt, 2.6, 540, 1000, "\"gratis\" no siempre es gratis", 50, C, kind="Bold", dy=20)
    slide_line(d, lt, 2.8, 540, 1070, "mirá la tienda: dice \"compras dentro de la app\"", 38, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 340, "¿ALGUNA VEZ PAGASTE", 115, C)
    pop_line(d, lt, 0.35, 540, 490, "EN UN JUEGO \"GRATIS\"?", 115, Y)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        gamepad(d, 540, 760, 360 * e)
    pill(d, t, 21.4, 330, 1020, 300, "SÍ", fill=Y, ink=K, size=70, h=130)
    pill(d, t, 21.6, 750, 1020, 300, "NO", fill=C, ink=K, size=70, h=130)
    slide_line(d, lt, 2.0, 540, 1180, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "thump"); ev(0.6, "pop")
for k in range(5): ev(1.75 + k * 0.25, "ding", -0.4 + k * 0.2)
ev(2.7, "thump"); ev(3.0, "tap")
ev(4.1, "tap"); ev(4.35, "tap"); ev(4.6, "rustle"); ev(5.8, "shimmer"); ev(5.8, "pop"); ev(6.2, "tap"); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.35, "tap"); ev(8.6, "whoosh"); ev(8.8, "stamp"); ev(9.2, "tap"); ev(9.6, "pop"); ev(10.3, "tap"); ev(10.5, "thump"); ev(10.8, "tap")
ev(12.1, "tap"); ev(12.35, "tap")
for k in range(7): ev(12.6 + k * 0.2, "tick")
ev(14.0, "thump"); ev(14.6, "pop"); ev(15.0, "tap")
ev(16.1, "pop"); ev(16.35, "tap"); ev(16.6, "pop"); ev(17.1, "toggle"); ev(17.6, "pop"); ev(18.0, "toggle"); ev(18.6, "tap"); ev(18.8, "tap")
ev(20.1, "pop", -0.3); ev(20.35, "thump"); ev(20.7, "pop"); ev(21.4, "pop", -0.4); ev(21.6, "pop", 0.4); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
