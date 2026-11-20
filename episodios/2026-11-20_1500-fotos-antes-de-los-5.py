"""Short 2026-11-20 20:00 — Chicos y pantallas: cuántas fotos de un chico suben los padres antes de los 5 años (sharenting).

Fuente:
- Nominet, estudio "Share with Care" (encuesta hecha por The Parent Zone, 1-17 de agosto de 2016,
  2.000 padres de chicos de 0 a 13 años, Reino Unido):
  en promedio 1.498 fotos de un chico subidas antes de que cumpla 5 años (54% más que el año anterior);
  "casi 300" por año; 85% revisó la privacidad de sus redes por última vez hace más de un año;
  solo 10% se siente "muy seguro" manejándola. Consejo: revisar la privacidad seguido y ojo con las
  fotos del primer día de clases (pueden mostrar nombre y ubicación de la escuela).
- Consejo de Nominet 2015: pensar si el chico te lo agradecería de grande.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

SKY = (90, 160, 230)

def polaroid(d, cx, cy, s, col=C, kid=Y, rot=0.0):
    """Foto tipo polaroid con un chico (sin rotación real: desplaza levemente)."""
    w, h = s, s * 1.18
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, s * 0.04, fill=col)
    ix0, iy0, ix1, iy1 = cx - w * 0.42, cy - h * 0.43, cx + w * 0.42, cy + h * 0.24
    d.rectangle([S(ix0), S(iy0), S(ix1), S(iy1)], fill=SKY)
    circle(d, ix1 - w * 0.14, iy0 + w * 0.14, w * 0.07, fill=Y)
    person(d, cx, iy1 - w * 0.12, w * 0.5, kid)

def counter_box(d, cx, cy, n, col=Y):
    rrect(d, cx - 330, cy - 120, cx + 330, cy + 120, 40, fill=K2, outline=col, width=8)
    text_c(d, cx, cy, fmt_num(n), "A", 190, col, bg=K2)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 290, "¿CUÁNTAS FOTOS", 150, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 440, "DE TU HIJO", 150, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 600, "HAY EN INTERNET?", 135, Y, dur=0.25)
    # fotos que caen y se apilan
    spots = [(330, 950), (750, 930), (540, 1010), (300, 1180), (780, 1170), (540, 1240)]
    for k, (x, y) in enumerate(spots):
        p = prog(t, 0.9 + k * 0.28, 0.3)
        if p <= 0: continue
        e = back(p)
        polaroid(d, x, y, 250 * e, kid=(Y if k % 2 == 0 else R))
    slide_line(d, t, 2.9, 540, 1500, "contalas antes de que te lo diga", 50, C, kind="SemiBold", dy=20)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "ANTES DE LOS 5 AÑOS", 120, C)
    slide_line(d, lt, 0.35, 540, 390, "fotos subidas, en promedio, por sus padres", 42, C, kind="SemiBold", dy=20)
    if lt > 0.6:
        n = 1498 * ease_out(prog(lt, 0.6, 1.6))
        counter_box(d, 540, 640, n, Y)
    stamp(d, t, 6.4, 540, 940, 330, 95, "CASI 1.500", fill=R, ink=K, size=120)
    slide_line(d, lt, 2.9, 540, 1110, "54% más que el año anterior", 46, C, kind="Bold", dy=20)
    slide_line(d, lt, 3.0, 540, 1190, "Nominet / The Parent Zone, 2.000 padres, Reino Unido, 2016", 29, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 280, "CASI 300 POR AÑO", 130, Y)
    slide_line(d, lt, 0.35, 540, 390, "casi 6 por semana, desde que nace", 46, C, kind="SemiBold", dy=20)
    # tira de 5 años: velitas / bloques que se llenan
    for k in range(5):
        p = prog(lt, 0.7 + k * 0.3, 0.3)
        if p <= 0: continue
        x = 180 + k * 180
        hgt = 380 * ease_out(p)
        rrect(d, x - 65, 1050 - hgt, x + 65, 1050, 18, fill=mix(K2, Y, 0.35 + 0.13 * k))
        text_c(d, x, 1110, f"{k + 1}", "A", 70, C)
        if p > 0.8:
            # mini fotos apiladas dentro de la barra
            for j in range(3):
                polaroid(d, x, 1050 - hgt + 60 + j * 100, 70, col=C, kid=K)
    slide_line(d, lt, 2.5, 540, 1220, "años", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.7, 540, 1300, "y cada foto puede quedar para siempre", 46, R, kind="Bold", dy=20)
    slide_line(d, lt, 2.9, 540, 1370, "Nominet, \"Share with Care\", ago. 2016", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "¿Y QUIÉN LAS VE?", 140, C)
    slide_line(d, lt, 0.35, 540, 390, "revisó la privacidad hace más de un año", 44, C, kind="SemiBold", dy=20)
    if lt > 0.6:
        f = 0.85 * ease_out(prog(lt, 0.6, 1.1))
        donut(d, 540, 680, 220, f, f"{int(round(f * 100))}%", R)
    pill(d, t, 14.1, 540, 1000, 900, "SOLO 10% SE SIENTE MUY SEGURO", fill=Y, ink=K, size=44, h=110)
    slide_line(d, lt, 2.5, 540, 1110, "manejando esos ajustes", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1190, "Nominet / The Parent Zone, 2016", 30, G, kind="SemiBold", dy=20)

def check_row(d, t, t0, y, txt, sub):
    p = prog(t, t0, 0.3)
    if p <= 0: return
    a = clamp(p * 2)
    rrect(d, 90, y, 990, y + 150, 40, fill=K2)
    q = back(prog(t, t0 + 0.35, 0.25))
    circle(d, 175, y + 75, 46, outline=Y, width=8)
    if q > 0.02:
        d.line([S(150), S(y + 77), S(170), S(y + 97), S(205), S(y + 52)], fill=Y, width=SW(12 * min(1, q)), joint="curve")
    text_l(d, 250, y + 52, txt, "Bold", 44, C)
    text_l(d, 250, y + 105, sub, "SemiBold", 32, Y)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "ANTES DE SUBIRLA", 130, Y)
    check_row(d, lt, 0.5, 420, "¿Me lo agradecería de grande?", "pensalo como si fuera tu foto")
    check_row(d, lt, 1.1, 610, "¿Se ve la escuela o el uniforme?", "eso muestra dónde está tu hijo")
    check_row(d, lt, 1.7, 800, "¿Quién la puede ver?", "revisá la privacidad seguido")
    slide_line(d, lt, 2.6, 540, 1060, "compartir no está mal: hacelo con cuidado", 44, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 340, "¿CUÁNTAS SUBISTE", 140, C)
    pop_line(d, lt, 0.35, 540, 500, "ESTE AÑO?", 170, Y)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        polaroid(d, 400, 800, 230 * e, kid=Y)
        polaroid(d, 680, 800, 230 * e, kid=R)
    pill(d, t, 21.6, 540, 1060, 560, "¿10? ¿100? ¿300+?", fill=C, ink=K, size=52, h=120)
    slide_line(d, lt, 2.0, 540, 1200, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
for k in range(6): ev(0.9 + k * 0.28, "click", -0.5 + k * 0.2)
ev(2.9, "tap")
ev(4.1, "tap"); ev(4.35, "tap")
for k in range(12): ev(4.6 + k * 0.13, "tick")
ev(6.2, "whoosh"); ev(6.4, "stamp"); ev(6.9, "tap"); ev(7.0, "tap")
ev(8.1, "thump"); ev(8.35, "tap")
for k in range(5): ev(8.7 + k * 0.3, "pop", -0.6 + k * 0.3)
ev(10.5, "tap"); ev(10.7, "thump"); ev(10.9, "tap")
ev(12.1, "tap"); ev(12.35, "tap"); ev(12.6, "rustle"); ev(13.7, "thump"); ev(14.1, "pop"); ev(14.5, "tap"); ev(14.8, "tap")
ev(16.1, "thump")
for k in range(3): ev(16.5 + k * 0.6, "pop"); ev(16.85 + k * 0.6, "ding")
ev(18.6, "tap")
ev(20.1, "pop", -0.3); ev(20.35, "thump"); ev(20.7, "click", -0.3); ev(20.75, "click", 0.3); ev(21.6, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
