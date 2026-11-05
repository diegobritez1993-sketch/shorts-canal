"""Short 2026-11-05 20:00 — Curiosidades y hábitos (dinero): con tarjeta pagás más.
Fuente: Prelec y Simester (MIT), "Always Leave Home Without It", Marketing Letters 2001: subasta de entradas
para un partido de básquet; a la mitad le dijeron que pagaría en efectivo y a la otra mitad con tarjeta;
la oferta promedio con tarjeta fue casi el doble (vía MSU Extension). Idea del "dolor de pagar": Prelec y Loewenstein 1998.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def card(d, cx, cy, w, h, col=Y, rot=0.0):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, h * 0.1, fill=col)
    d.rectangle([S(cx - w / 2), S(cy - h * 0.28), S(cx + w / 2), S(cy - h * 0.12)], fill=K)
    rrect(d, cx - w * 0.38, cy + h * 0.0, cx - w * 0.2, cy + h * 0.2, 8, fill=mix(col, K, 0.35))
    for k in range(4):
        rrect(d, cx - w * 0.38 + k * w * 0.17, cy + h * 0.3, cx - w * 0.25 + k * w * 0.17, cy + h * 0.36, 4, fill=mix(col, K, 0.5))

def bill(d, cx, cy, w, h, col=GREEN):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 10, fill=col)
    rrect(d, cx - w / 2 + 12, cy - h / 2 + 12, cx + w / 2 - 12, cy + h / 2 - 12, 8, outline=mix(col, K, 0.4), width=5)
    circle(d, cx, cy, h * 0.24, fill=mix(col, K, 0.35))
    text_c(d, cx, cy, "$", "A", int(h * 0.38), col, bg=mix(col, K, 0.35))

def ticket(d, cx, cy, w, h, col=Y):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 18, fill=col)
    for sx in (-1, 1):
        circle(d, cx + sx * w / 2, cy, h * 0.16, fill=K)
    for k in range(6):
        y = cy - h * 0.35 + k * h * 0.14
        d.line([S(cx + w * 0.22), S(y), S(cx + w * 0.22), S(y + h * 0.07)], fill=K, width=S(6))
    text_c(d, cx - w * 0.1, cy, "ENTRADA", "A", int(h * 0.3), K, bg=col)

def ball(d, cx, cy, r, rot):
    circle(d, cx, cy, r, fill=(240, 130, 30))
    w = max(2, int(S(r * 0.07)))
    d.line([S(cx - r), S(cy), S(cx + r), S(cy)], fill=K, width=w)
    d.line([S(cx), S(cy - r), S(cx), S(cy + r)], fill=K, width=w)
    d.arc([S(cx - r * 1.6), S(cy - r), S(cx - r * 0.4), S(cy + r)], -50, 50, fill=K, width=w)
    d.arc([S(cx + r * 0.4), S(cy - r), S(cx + r * 1.6), S(cy + r)], 130, 230, fill=K, width=w)

def b1(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        card(d, 540 + math.sin(t * 2) * 10, 470, 460 * e, 290 * e, rot=0)
    pop_line(d, t, 0.15, 540, 860, "CON TARJETA", 150, C)
    pop_line(d, t, 0.45, 540, 1010, "OFRECIERON CASI", 110, C)
    sx, sy = shake(t, 1.25, 0.35, 18)
    pop_line(d, t, 1.05, 540 + sx, 1190 + sy, "EL DOBLE", 220, Y, dur=0.28)
    slide_line(d, t, 1.8, 540, 1360, "lo dice un experimento del MIT", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "SUBASTARON", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "ENTRADAS", 150, Y)
    slide_line(d, lt, 0.5, 540, 550, "para un partido de básquet", 48, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        ticket(d, 540, 820, 560 * e, 230 * e)
    # pelota que pica
    if lt > 1.0:
        ph = ((lt - 1.0) * 1.6) % 1.0
        by = 1235 - 140 * (1 - (2 * ph - 1) ** 2)
        ball(d, 540, by, 85, lt)
    pop_line(d, lt, 2.0, 540, 1400, "Y LOS DIVIDIERON", 110, C)
    slide_line(d, lt, 2.3, 540, 1520, "en dos grupos", 48, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    a = ease_out(prog(lt, 0.1, 0.45))
    b = ease_out(prog(lt, 0.6, 0.45))
    # columna izquierda: efectivo
    xl = lerp(-300, 290, a)
    xr = lerp(1380, 790, b)
    text_c(d, xl, 330, "MITAD", "A", 110, C)
    text_c(d, xl, 450, "EFECTIVO", "A", 110, GREEN)
    for k in range(3):
        bill(d, xl + (k - 1) * 18, 720 + k * 40, 380, 180)
    text_c(d, xr, 330, "MITAD", "A", 110, C)
    text_c(d, xr, 450, "TARJETA", "A", 110, Y)
    card(d, xr, 760, 380, 240)
    if lt > 1.2:
        d.line([S(540), S(280), S(540), S(1000)], fill=mix(K, G, ease_out(prog(lt, 1.2, 0.3))), width=S(4))
    pop_line(d, lt, 1.6, 540, 1200, "¿CUÁNTO", 120, C)
    pop_line(d, lt, 1.8, 540, 1340, "OFRECERÍAS?", 140, Y)
    slide_line(d, lt, 2.3, 540, 1470, "cada uno anotó su oferta", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "RESULTADO", 140, C)
    base = 1130
    a = ease_out(prog(lt, 0.4, 0.6))
    b = ease_out(prog(lt, 0.8, 1.2))
    hC, hT = 300 * a, 300 * 1.9 * b
    rrect(d, 220, base - hC, 470, base, 24, fill=GREEN)
    rrect(d, 610, base - hT, 860, base, 24, fill=Y)
    d.rectangle([S(150), S(base), S(930), S(base + 8)], fill=C)
    slide_line(d, lt, 0.5, 345, base + 60, "efectivo", 44, GREEN, kind="Bold", dy=20)
    slide_line(d, lt, 0.9, 735, base + 60, "tarjeta", 44, Y, kind="Bold", dy=20)
    stamp(d, lt, 2.1, 540, 1330, 420, 95, "CASI EL DOBLE", fill=R, ink=C, size=130)
    slide_line(d, lt, 2.6, 540, 1470, "oferta promedio · Prelec y Simester, MIT, 2001", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿POR QUÉ?", 140, C)
    slide_line(d, lt, 0.3, 540, 440, "EL EFECTIVO DUELE", 115, Y)
    slide_line(d, lt, 0.5, 540, 540, "ves cómo se va la plata de tu mano", 44, C, kind="SemiBold", dy=25)
    # billetes que se van volando
    for k in range(4):
        p = ease_in_out(prog(lt, 0.7 + k * 0.25, 0.9))
        if 0 < p < 1:
            bill(d, lerp(330, 330 + 120 * (k - 1.5), p), lerp(860, 600, p), 240 * (1 - 0.4 * p), 115 * (1 - 0.4 * p))
    rrect(d, 200, 820, 460, 1000, 40, fill=K2, outline=C, width=8)
    text_c(d, 330, 910, "BILLETERA", "Black", 30, C, bg=K2)
    # tarjeta que apoya y listo
    q = ease_out(prog(lt, 1.4, 0.4))
    card(d, 760, lerp(1000, 900, q), 280, 175)
    if lt > 1.9:
        c = back(prog(lt, 1.9, 0.3))
        circle(d, 870, 820, 50 * c, fill=GREEN)
        if c > 0.6:
            d.line([S(845), S(822), S(865), S(842), S(898), S(800)], fill=C, width=S(12), joint="curve")
    pop_line(d, lt, 2.2, 540, 1200, "CON TARJETA", 110, C)
    pop_line(d, lt, 2.4, 540, 1330, "NI LO SENTÍS", 140, R)
    slide_line(d, lt, 2.8, 540, 1450, "pagar se siente menos", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 140, C)
    slide_line(d, lt, 0.3, 540, 490, "PONETE UN TOPE", 135, Y)
    slide_line(d, lt, 0.6, 540, 610, "y mirá tus gastos cada semana", 46, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.8, 0.4))
    if e > 0.02:
        lvl = 0.6 * ease_in_out(prog(lt, 1.0, 1.0))
        battery(d, 520, 850, 480 * e, 200 * e, lvl, GREEN if lvl < 0.45 else Y)
        if e > 0.9:
            xl = 520 - 480 / 2 + 24 + (480 - 48) * 0.72
            d.rectangle([S(xl - 5), S(720), S(xl + 5), S(980)], fill=R)
            text_c(d, xl, 1010, "TOPE", "Black", 34, R)
    pill(d, lt, 1.8, 540, 1150, 820, "¿VOS CON QUÉ PAGÁS?", fill=Y, ink=K, size=50, h=120)
    slide_line(d, lt, 2.1, 540, 1280, "efectivo, tarjeta o celu: comentá", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "whoosh"); ev(0.15, "pop", -0.3); ev(0.45, "pop", 0.3); ev(1.05, "whoosh"); ev(1.25, "stamp"); ev(1.8, "tap")
ev(4.1, "tap", -0.3); ev(4.3, "pop", 0.3); ev(4.5, "tap"); ev(4.6, "rustle")
for k in range(5): ev(5.0 + k / 1.6 + 0.62, "thump", 0.2 if k % 2 else -0.2)
ev(6.0, "pop"); ev(6.3, "tap")
ev(8.1, "swipe", -0.6); ev(8.3, "rustle", -0.5); ev(8.6, "swipe", 0.6); ev(9.6, "pop"); ev(9.8, "pop", 0.2); ev(10.3, "tap")
ev(12.1, "tap")
for k in range(12): ev(12.5 + k * 0.12, "tick", 0.3 if k % 2 else -0.3)
ev(14.0, "whoosh"); ev(14.1, "stamp"); ev(14.6, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.5, "tap")
for k in range(4): ev(16.7 + k * 0.25, "rustle", -0.4 + k * 0.25)
ev(17.5, "click", 0.4); ev(17.9, "ding", 0.4); ev(18.2, "pop"); ev(18.4, "thump"); ev(18.8, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "tap")
for k in range(7): ev(21.0 + k * 0.14, "tick", 0.2 if k % 2 else -0.2)
ev(21.8, "pop"); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
