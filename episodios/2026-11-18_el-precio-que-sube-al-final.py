"""Short 2026-11-18 15:00 — Cómo te enganchan las apps: cargos que aparecen al final de la compra (drip pricing).

Fuente:
- Blake, Moshary, Sweeney y Tadelis, "Price Salience and Product Choice", Marketing Science 2021.
  Experimento de StubHub (desde otoño 2015): a la mitad de los usuarios de EE.UU. (millones) les mostraron
  el precio sin cargos y los cargos recién al final; a la otra mitad, el precio total desde el inicio.
- Comunicado UC Berkeley Haas (vía Phys.org, 22/02/2021): con cargos al final gastaron ~21% más y fueron
  14% más propensos a completar la compra; los que entraban seguido (10+ visitas) igual gastaron 15% más.
  Tadelis: "la gente termina haciendo compras que, mirando para atrás, no habría hecho".
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

def tag(d, cx, cy, w, h, col=Y, ink=K, txt=None, size=90, rot=0.0):
    """Etiqueta de precio con agujerito (sin rotación para mantenerlo simple)."""
    x0, x1 = cx - w / 2, cx + w / 2
    d.polygon([(S(x0), S(cy)), (S(x0 + h * 0.45), S(cy - h / 2)), (S(x1), S(cy - h / 2)),
               (S(x1), S(cy + h / 2)), (S(x0 + h * 0.45), S(cy + h / 2))], fill=col)
    circle(d, x0 + h * 0.42, cy, h * 0.1, fill=K)
    if txt: text_c(d, cx + h * 0.2, cy, txt, "A", size, ink, bg=col)

def cart(d, cx, cy, s, col=C):
    """Carrito de compras."""
    d.line([S(cx - s * 0.6), S(cy - s * 0.45), S(cx - s * 0.4), S(cy - s * 0.45), S(cx - s * 0.25), S(cy + s * 0.2),
            S(cx + s * 0.45), S(cy + s * 0.2), S(cx + s * 0.55), S(cy - s * 0.25), S(cx - s * 0.35), S(cy - s * 0.25)],
           fill=col, width=SW(s * 0.07), joint="curve")
    circle(d, cx - s * 0.15, cy + s * 0.38, s * 0.09, fill=col)
    circle(d, cx + s * 0.35, cy + s * 0.38, s * 0.09, fill=col)

def screen(d, cx, cy, w, h, title, lines, col, p):
    """Pantallita de compra con filas de texto."""
    if p <= 0: return
    e = back(p)
    ww, hh = w * e, h * e
    rrect(d, cx - ww / 2, cy - hh / 2, cx + ww / 2, cy + hh / 2, 30 * e, fill=K2, outline=col, width=6)
    if p > 0.6:
        a = clamp((p - 0.6) * 3)
        text_c(d, cx, cy - h * 0.36, title, "Black", 40, col, alpha=a, bg=K2)
        for k, (txt, c) in enumerate(lines):
            text_c(d, cx, cy - h * 0.12 + k * 80, txt, "Bold", 38, c, alpha=a, bg=K2)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 330, "¿POR QUÉ EL", 150, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 490, "PRECIO SUBE", 165, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 660, "AL FINAL?", 190, R, dur=0.25)
    # etiqueta que crece con cargos
    e = back(prog(t, 0.8, 0.35))
    if e > 0.02:
        grow = ease_out(prog(t, 1.6, 0.9))
        w = 420 + 260 * grow
        sx, sy = shake(t, 2.5, 0.3, 12)
        tag(d, 540 + sx, 1000 + sy, w * e, 200 * e, col=mix(Y, R, grow), ink=K)
        if t > 1.1:
            text_c(d, 540 + 40 + sx, 1000 + sy, "PRECIO" if grow < 0.5 else "+ CARGOS", "A", 95, K, bg=mix(Y, R, grow))
    slide_line(d, t, 2.4, 540, 1300, "no es casualidad:", 50, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.6, 540, 1370, "lo probaron con millones de personas", 50, Y, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "UNA WEB DE ENTRADAS", 105, C)
    slide_line(d, lt, 0.3, 540, 410, "(StubHub) partió en 2 a sus usuarios de EE.UU.", 40, C, kind="SemiBold", dy=20)
    screen(d, 290, 790, 440, 520, "MITAD A", [("precio TOTAL", C), ("desde el inicio", C), ("sin sorpresas", GREEN)], GREEN, prog(lt, 0.6, 0.35))
    screen(d, 790, 790, 440, 520, "MITAD B", [("precio SIN cargos", C), ("y los cargos...", C), ("¡AL FINAL!", R)], R, prog(lt, 1.1, 0.35))
    pop_line(d, lt, 2.0, 540, 1150, "¿QUIÉN GASTÓ MÁS?", 110, Y)
    slide_line(d, lt, 2.6, 540, 1290, "Blake, Moshary, Sweeney y Tadelis, Marketing Science 2021", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "LOS DE CARGOS AL FINAL", 100, C)
    v = 21 * ease_out(prog(lt, 0.4, 1.0))
    if lt > 0.4:
        sx, sy = shake(lt, 1.4, 0.3, 16)
        text_c(d, 540 + sx, 560 + sy, f"+{int(round(v))}%", "A", 300, R)
        pop_line(d, lt, 1.4, 540, 760, "GASTARON MÁS", 120, C)
    # barra comparativa
    p = ease_out(prog(lt, 1.7, 0.6))
    if p > 0:
        rrect(d, 140, 900, 140 + 640 * p, 980, 20, fill=GREEN)
        text_l(d, 160, 940, "A", "Black", 44, K) if p > 0.2 else None
        rrect(d, 140, 1010, 140 + 775 * p, 1090, 20, fill=R)
        text_l(d, 160, 1050, "B", "Black", 44, K) if p > 0.2 else None
    pill(d, t, 10.6, 540, 1230, 900, "Y 14% MÁS PROPENSOS A COMPRAR", fill=Y, ink=K, size=42, h=110)
    slide_line(d, lt, 3.0, 540, 1350, "UC Berkeley Haas, vía Phys.org 22/02/2021", 32, G, kind="SemiBold", dy=20)

STEPS = ["ELEGÍS", "ASIENTO", "DATOS", "PAGO"]

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "¿POR QUÉ FUNCIONA?", 120, C)
    # embudo de pasos de compra
    for k, s in enumerate(STEPS):
        p = prog(lt, 0.4 + k * 0.3, 0.25)
        if p <= 0: continue
        x = 165 + k * 250
        e = back(p)
        last = k == len(STEPS) - 1
        col = R if (last and lt > 1.9) else Y
        circle(d, x, 560, 70 * e, fill=col)
        text_c(d, x, 560, str(k + 1), "A", int(80 * e) + 2, K, bg=col)
        text_c(d, x, 670, s, "Black", 34, C, alpha=clamp(p * 2))
        if k > 0:
            d.line([S(x - 175), S(560), S(x - 85), S(560)], fill=G, width=SW(8))
    pop_line(d, lt, 1.9, 805, 430, "+ CARGOS", 70, R)
    slide_line(d, lt, 2.2, 540, 840, "cuando aparecen los cargos ya elegiste,", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.35, 540, 900, "ya te imaginaste ahí y te da pereza volver", 44, C, kind="SemiBold", dy=20)
    cart(d, 540, 1120, 220 * back(prog(lt, 2.6, 0.35)), Y) if lt > 2.6 else None
    slide_line(d, lt, 3.0, 540, 1330, "hasta los que entraban seguido gastaron 15% más", 40, Y, kind="Bold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "EL TRUCO:", 150, Y)
    pop_line(d, lt, 0.4, 540, 470, "COMPARÁ EL TOTAL", 120, C)
    pop_line(d, lt, 0.6, 540, 600, "NO EL PRECIO", 120, R)
    # ticket con "TOTAL" subrayado
    e = back(prog(lt, 1.0, 0.35))
    if e > 0.02:
        w, h = 600 * e, 380 * e
        rrect(d, 540 - w / 2, 960 - h / 2, 540 + w / 2, 960 + h / 2, 24, fill=C)
        if e > 0.8:
            for k in range(2):
                d.line([S(540 - w / 2 + 60), S(860 + k * 60), S(540 + w / 2 - 60), S(860 + k * 60)], fill=(190, 186, 176), width=SW(6))
            text_l(d, 540 - w / 2 + 60, 1040, "TOTAL", "Black", 64, K)
            q = ease_out(prog(lt, 1.5, 0.5))
            if q > 0:
                d.line([S(540 - w / 2 + 50), S(1090), S(540 - w / 2 + 50 + (w - 100) * q), S(1090)], fill=R, width=SW(12))
    slide_line(d, lt, 2.0, 540, 1260, "avanzá hasta el último paso antes de pagar", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.2, 540, 1320, "y recién ahí decidí", 44, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "\"COMPRAS QUE NO", 105, C)
    slide_line(d, lt, 0.25, 540, 420, "HABRÍAN HECHO\"", 105, C)
    slide_line(d, lt, 0.5, 540, 515, "Steven Tadelis, UC Berkeley, autor del estudio", 34, G, kind="SemiBold", dy=20)
    pop_line(d, lt, 1.0, 540, 760, "¿TE PASÓ?", 170, Y)
    pill(d, t, 21.5, 360, 1000, 280, "SÍ", fill=GREEN, ink=K, size=70, h=140)
    pill(d, t, 21.7, 720, 1000, 280, "NO", fill=R, ink=K, size=70, h=140)
    slide_line(d, lt, 2.1, 540, 1180, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
ev(0.8, "pop"); ev(1.6, "whoosh"); ev(2.5, "stamp"); ev(2.4, "tap"); ev(2.6, "tap")
ev(4.1, "tap"); ev(4.3, "tap"); ev(4.6, "pop", -0.4); ev(5.1, "pop", 0.4); ev(5.9, "buzz", 0.4); ev(6.0, "pop"); ev(6.6, "tap")
ev(8.1, "tap")
for k in range(10): ev(8.4 + k * 0.1, "tick")
ev(9.4, "thump"); ev(9.4, "pop"); ev(9.7, "swipe"); ev(10.6, "pop"); ev(11.0, "tap")
ev(12.1, "tap")
for k in range(4): ev(12.4 + k * 0.3, "click", -0.6 + k * 0.4)
ev(13.9, "stamp"); ev(14.2, "tap"); ev(14.35, "tap"); ev(14.6, "pop"); ev(15.0, "tap")
ev(16.1, "whoosh"); ev(16.4, "pop"); ev(16.6, "thump"); ev(17.0, "rustle"); ev(17.5, "swipe"); ev(18.0, "tap"); ev(18.2, "tap")
ev(20.1, "tap"); ev(20.25, "tap"); ev(20.5, "tap"); ev(21.0, "pop"); ev(21.5, "pop", -0.4); ev(21.7, "pop", 0.4); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
