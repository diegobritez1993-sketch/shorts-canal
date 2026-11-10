"""Short 2026-11-10 20:00 — Chicos y pantallas: tecnoferencia (el celu de los padres interrumpe).

Fuente: McDaniel (Illinois State) y Radesky (Univ. de Michigan / C.S. Mott), Child Development 2017 (online, mayo).
170 familias con dos padres. Interrupciones por tecnología en un día típico: 48% tres o más, 24% dos, 17% una, 11% ninguna.
Incluso niveles bajos de interrupción se asociaron a más problemas de conducta (sensibilidad, berrinches, hiperactividad,
lloriqueo). Estudio transversal: relación, no causa. Consejo: momentos o lugares sin tecnología (comidas, juego).
Vía Michigan Medicine Health Lab.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

BLUE = (90, 140, 255)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        person(d, 360, 620, 380 * e, C)          # adulto
        person(d, 760, 720, 230 * e, Y)          # chico
        phone(d, 430, 690, 90 * e, 160 * e, body=BLUE, outline=C, buzz=1.0 if t % 1.0 < 0.4 else 0.0, t=t)
    if t > 0.5:
        bubble(d, 830, 440 + math.sin(t * 4) * 8, 150 * back(prog(t, 0.5, 0.3)), C)
    pop_line(d, t, 0.4, 540, 1020, "¿MIRÁS EL CELU", 135, C)
    pop_line(d, t, 0.7, 540, 1170, "CUANDO TU HIJO", 135, Y)
    pop_line(d, t, 1.0, 540, 1320, "TE HABLA?", 150, Y)
    slide_line(d, t, 1.8, 540, 1470, "esto te va a interesar", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "TIENE NOMBRE:", 120, C)
    pop_line(d, lt, 0.4, 540, 460, "TECNOFERENCIA", 150, Y)
    # hilo entre los dos que se corta cuando aparece el celular
    ax, bx, y = 250, 830, 860
    person(d, ax, 900, 260, C); person(d, bx, 930, 190, Y)
    cut = prog(lt, 1.6, 0.3)
    lp = ease_out(prog(lt, 0.7, 0.6))
    if lp > 0:
        x_end = lerp(ax + 90, bx - 70, lp)
        if cut <= 0:
            d.line([S(ax + 90), S(y), S(x_end), S(y)], fill=Y, width=S(12))
        else:
            gap = 90 * ease_out(cut)
            d.line([S(ax + 90), S(y), S(540 - gap), S(y + 20 * cut)], fill=mix(Y, G, cut), width=S(12))
            d.line([S(540 + gap), S(y + 20 * cut), S(bx - 70), S(y)], fill=mix(Y, G, cut), width=S(12))
    if cut > 0:
        ph = back(cut)
        phone(d, 540, 760 - 60 * ph, 110 * ph, 190 * ph, body=BLUE, outline=C)
    slide_line(d, lt, 2.2, 540, 1230, "cuando la pantalla", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1295, "corta el momento con tu hijo", 48, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "UN ESTUDIO CON", 120, C)
    n = 170 * ease_out(prog(lt, 0.3, 1.2))
    pop_line(d, lt, 0.3, 540, 500, f"{int(n)} FAMILIAS", 170, Y, dur=0.25)
    # grilla de casitas que se llenan
    for k in range(17):
        c, r = k % 6, k // 6
        x, yy = 215 + c * 130, 720 + r * 150
        p = back(prog(lt, 0.4 + k * 0.06, 0.25))
        if p > 0.02:
            s = 50 * p
            d.polygon([(S(x - s), S(yy)), (S(x + s), S(yy)), (S(x), S(yy - s * 0.9))], fill=Y)
            d.rectangle([S(x - s * 0.75), S(yy), S(x + s * 0.75), S(yy + s * 0.9)], fill=Y)
            d.rectangle([S(x - s * 0.2), S(yy + s * 0.35), S(x + s * 0.2), S(yy + s * 0.9)], fill=K)
    slide_line(d, lt, 2.0, 540, 1250, "papás y mamás contaron cuántas veces", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.15, 540, 1310, "el celu los interrumpe con sus hijos", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1390, "Univ. de Michigan e Illinois State, Child Development", 34, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    e = back(prog(lt, 0.1, 0.4))
    fr = 0.48 * ease_out(prog(lt, 0.4, 1.3))
    if e > 0.02:
        donut(d, 540, 620, 300 * e, fr, f"{int(round(fr * 100))}%", col=R)
    pop_line(d, lt, 1.8, 540, 1060, "3 O MÁS VECES", 140, C)
    pop_line(d, lt, 2.0, 540, 1200, "POR DÍA", 140, R)
    slide_line(d, lt, 2.5, 540, 1340, "solo 11% dijo: ninguna", 48, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y LOS CHICOS", 120, C)
    slide_line(d, lt, 0.3, 540, 410, "MOSTRABAN MÁS...", 110, Y)
    for k, w in enumerate(["BERRINCHES", "HIPERACTIVIDAD", "LLORIQUEO"]):
        sx, sy = shake(lt, 0.8 + k * 0.4 + 0.3, 0.3, 12)
        stamp(d, lt, 0.8 + k * 0.4, 540 + sx, 620 + k * 190 + sy, 360, 70, w, fill=R if k != 1 else Y,
              ink=C if k != 1 else K, size=90)
    slide_line(d, lt, 2.3, 540, 1280, "incluso con pocas interrupciones", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1350, "es una relación, no prueba la causa", 40, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "COMIDAS SIN CELU", 125, Y)
    q = ease_in_out(prog(lt, 0.8, 0.3))
    if lt > 0.5:
        toggle_row(d, 110, 580, "Celu en la mesa", 1 - q, sub="apagado" if q > 0.5 else "encendido")
    pop_line(d, lt, 1.5, 540, 950, "¿Y VOS?", 150, C)
    pop_line(d, lt, 1.7, 540, 1100, "¿CUÁNTAS VECES HOY?", 110, Y)
    slide_line(d, lt, 2.1, 540, 1230, "contalo en los comentarios", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.1, "buzz", -0.3); ev(1.1, "buzz", -0.3); ev(2.1, "buzz", -0.3); ev(3.1, "buzz", -0.3)
ev(0.4, "pop", -0.2); ev(0.5, "tap", 0.4); ev(0.7, "pop", 0.2); ev(1.0, "thump"); ev(1.8, "tap")
ev(4.1, "tap"); ev(4.4, "pop"); ev(4.7, "swipe"); ev(5.6, "click"); ev(5.65, "thump"); ev(6.2, "tap"); ev(6.35, "tap")
ev(8.1, "tap")
for k in range(10): ev(8.3 + k * 0.12, "tick", 0.3 if k % 2 else -0.3)
for k in range(17): ev(8.4 + k * 0.06, "click", -0.5 + k * 0.06)
ev(9.6, "thump"); ev(10.0, "tap"); ev(10.15, "tap"); ev(10.4, "tap")
ev(12.1, "pop")
for k in range(12): ev(12.4 + k * 0.11, "tick", 0.3 if k % 2 else -0.3)
ev(13.8, "pop"); ev(14.0, "thump"); ev(14.5, "tap")
ev(16.1, "tap"); ev(16.3, "tap")
for k in range(3): ev(16.8 + k * 0.4 + 0.15, "stamp", -0.3 + k * 0.3)
ev(18.3, "tap"); ev(18.5, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.8, "toggle"); ev(21.5, "pop"); ev(21.7, "thump"); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
