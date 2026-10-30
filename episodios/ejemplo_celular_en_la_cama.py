"""Episodio de ejemplo (Short #6). Copiar este archivo como plantilla para cada video nuevo.

Estructura fija de 25 s: 6 escenas de ~4 s + cierre de marca.
  0-4   gancho (pregunta o dato que frena el scroll)
  4-8, 8-12, 12-16, 16-20   desarrollo, un dato/idea por escena, con una animación distinta cada vez
  20-23.2  remate o consejo práctico
  23.2-25  outro de marca (engine.outro)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def b1(d, t):
    stars(d, t)
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02:
        moon(d, 830, 230, 80 * e)
        for k in range(6, 0, -1):
            circle(d, 540, 560, 120 + k * 40 * e, fill=mix(K, (90, 140, 255), 0.05 * (7 - k) * e))
        phone(d, 540, 560, 230 * e, 410 * e, body=(70, 120, 230), outline=C)
    pop_line(d, t, 0.4, 540, 960, "¿USÁS EL CELULAR", 140, C)
    pop_line(d, t, 0.7, 540, 1125, "EN LA CAMA?", 140, Y)
    pop_line(d, t, 1.4, 540, 1310, "MIRÁ LO QUE LE HACE", 90, C)
    pop_line(d, t, 1.6, 540, 1440, "A TU SUEÑO", 140, C)

def b2(d, t):
    lt = t - 4
    p = ease_in_out(prog(lt, 1.0, 0.6))
    bgc = mix(K, (40, 34, 10), p)
    d.rectangle([0, 0, S(1080), S(1920)], fill=bgc)
    slide_line(d, lt, 0.1, 540, 300, "LA LUZ DE LA PANTALLA", 100, C, bg=bgc)
    slide_line(d, lt, 0.3, 540, 430, "ENGAÑA A TU CEREBRO", 100, Y, bg=bgc)
    e = back(prog(lt, 0.3, 0.4))
    if p < 0.5 and e > 0.02:
        moon(d, 540, 860, 180 * e * (1 - p * 2), bg=bgc)
    if p >= 0.5:
        sun(d, 540, 860, 170 * back(clamp((p - 0.5) * 2)), lt)
    pop_line(d, lt, 1.8, 540, 1250, "CREE QUE", 110, C, bg=bgc)
    pop_line(d, lt, 2.0, 540, 1390, "TODAVÍA ES DE DÍA", 120, Y, bg=bgc)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "Y FRENA LA", 120, C)
    pop_line(d, lt, 0.3, 540, 450, "MELATONINA", 170, Y)
    slide_line(d, lt, 0.6, 540, 560, "la hormona que te da sueño", 46, C, kind="SemiBold", dy=25)
    e = ease_out(prog(lt, 0.4, 0.4))
    if e > 0:
        x0, x1, y0, y1 = 400, 680, 680, 1300
        rrect(d, x0, y0, x1, y1, 50, outline=C, width=10)
        lvl = 1 - 0.65 * ease_in_out(prog(lt, 1.1, 1.6))
        rrect(d, x0 + 24, y1 - 24 - (y1 - y0 - 48) * lvl * e, x1 - 24, y1 - 24, 30, fill=mix(R, Y, lvl))
        zzz(d, 760, 900, lt, col=mix(K, C, lvl))
    pill(d, lt, 2.8, 540, 1430, 720, "MENOS SUEÑO", fill=R, ink=C, size=44, h=100)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "EN UN ESTUDIO", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "tardaron en dormirse", 50, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        clock(d, 540, 760, 210 * e, ease_in_out(prog(lt, 0.7, 1.4)))
    sx, sy = shake(lt, 2.2, 0.35, 16)
    pop_line(d, lt, 1.0, 540 + sx, 1110 + sy, "CASI", 110, C)
    pop_line(d, lt, 2.0, 540 + sx, 1260 + sy, "10 MIN MÁS", 200, Y, dur=0.28)
    slide_line(d, lt, 2.6, 540, 1420, "leyendo en pantalla vs. en papel", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1480, "Harvard y Penn State, 2015", 38, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "Y AL OTRO DÍA", 130, C)
    pop_line(d, lt, 0.3, 540, 450, "MÁS CANSADO", 170, R)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        lvl = 1 - 0.85 * ease_in_out(prog(lt, 0.9, 1.4))
        battery(d, 520, 820, 480 * e, 230 * e, lvl, GREEN if lvl > 0.5 else (Y if lvl > 0.25 else R))
    pop_line(d, lt, 2.0, 540, 1130, "MENOS SUEÑO REM", 110, C)
    slide_line(d, lt, 2.4, 540, 1250, "y te cuesta más despertarte", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    stars(d, lt)
    slide_line(d, lt, 0.1, 540, 400, "EL TRUCO:", 140, C)
    slide_line(d, lt, 0.3, 540, 550, "DEJALO LEJOS", 150, Y)
    slide_line(d, lt, 0.45, 540, 700, "DE LA CAMA", 150, Y)
    phone(d, lerp(540, 1300, ease_in_out(prog(lt, 1.0, 0.9))), 1010, 150, 270)
    if lt > 1.2: zzz(d, 470, 1060, lt)
    slide_line(d, lt, 1.6, 540, 1240, "y apagá la pantalla un rato", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.75, 540, 1305, "antes de dormir", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

# Sonidos: cada texto que aparece = pop/tap; cada dato fuerte = thump o stamp; contadores = tick.
standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.2, "tap", 0.2)
ev(0.4, "pop", -0.3); ev(0.7, "pop", 0.3); ev(1.4, "pop", -0.2); ev(1.6, "thump")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3); ev(5.0, "swipe"); ev(5.3, "shimmer"); ev(5.8, "pop", -0.2); ev(6.0, "thump")
ev(8.1, "tap"); ev(8.3, "pop"); ev(8.6, "tap")
for k in range(12): ev(9.1 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(10.8, "stamp")
ev(12.1, "tap", -0.3); ev(12.3, "tap", 0.3)
for k in range(10): ev(12.7 + k * 0.13, "tick", 0.35 if k % 2 else -0.35)
ev(13.0, "pop"); ev(14.0, "thump"); ev(14.6, "tap")
ev(16.1, "tap"); ev(16.3, "thump")
for k in range(8): ev(16.9 + k * 0.17, "click", 0.2 if k % 2 else -0.2)
ev(18.0, "pop"); ev(18.3, "buzz"); ev(18.4, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "pop", 0.2); ev(21.0, "swipe", 0.6); ev(21.3, "shimmer"); ev(21.6, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
