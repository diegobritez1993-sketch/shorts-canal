"""Short 2026-11-08 20:00 - Chicos y pantallas: leerle en papel vs. en tablet.
Fuentes: Munzer et al., Pediatrics 2019 (37 pares) y 2021 (72 pares, 24-36 meses), Univ. de Michigan."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def book(d, cx, cy, s, col=Y):
    """Libro abierto dibujado con primitivas."""
    w, h = s, s * 0.68
    d.polygon([(S(cx), S(cy - h * 0.38)), (S(cx - w), S(cy - h * 0.62)), (S(cx - w), S(cy + h * 0.42)), (S(cx), S(cy + h * 0.62))], fill=col)
    d.polygon([(S(cx), S(cy - h * 0.38)), (S(cx + w), S(cy - h * 0.62)), (S(cx + w), S(cy + h * 0.42)), (S(cx), S(cy + h * 0.62))], fill=mix(col, K, 0.2))
    d.line([(S(cx), S(cy - h * 0.38)), (S(cx), S(cy + h * 0.62))], fill=K, width=S(max(3, int(s * 0.03))))
    for k in range(3):
        y = cy - h * 0.25 + k * h * 0.25
        d.line([(S(cx - w * 0.75), S(y - h * 0.08)), (S(cx - w * 0.15), S(y + h * 0.08))], fill=K, width=S(max(3, int(s * 0.03))))

def tablet(d, cx, cy, w, h, screen=(70, 120, 230)):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 26, fill=K2, outline=C, width=8)
    rrect(d, cx - w / 2 + 22, cy - h / 2 + 22, cx + w / 2 - 22, cy + h / 2 - 22, 12, fill=screen)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 310, "¿LE LEÉS", 180, C)
    pop_line(d, t, 0.3, 540, 500, "CUENTOS EN", 150, C)
    pop_line(d, t, 0.6, 540, 680, "LA TABLET?", 190, Y)
    e = back(prog(t, 0.2, 0.4))
    if e > 0.02:
        book(d, 265, 1060, 165 * e)
        tablet(d, 815, 1060, 290 * e, 400 * e)
    pop_line(d, t, 1.4, 540, 1060, "VS", 110, R)
    pop_line(d, t, 2.0, 540, 1460, "ESTO CAMBIA LA CHARLA", 100, C)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.05, 540, 290, "LO ESTUDIARON", 140, C)
    slide_line(d, lt, 0.25, 540, 440, "PADRES LEYENDO", 120, Y)
    n = 72
    shown = int(n * ease_in_out(prog(lt, 0.6, 1.3)))
    for k in range(shown):
        c, r = k % 12, k // 12
        col = C if k % 2 else Y
        person(d, 150 + c * 71, 620 + r * 105, 62, col)
    pop_line(d, lt, 2.1, 540, 1290, "72 PAREJAS", 170, Y)
    slide_line(d, lt, 2.4, 540, 1420, "padres con hijos de 2 a 3 años", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1490, "Munzer, Univ. de Michigan · Pediatrics, 2021", 38, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.05, 540, 290, "CON EL LIBRO", 150, Y)
    slide_line(d, lt, 0.3, 540, 440, "EN PAPEL", 150, Y)
    book(d, 540, 1000, 250 * back(prog(lt, 0.3, 0.4)) + 1)
    positions = [(230, 640, 90), (850, 650, 100), (150, 880, 75), (930, 880, 80), (320, 1240, 85), (760, 1230, 95)]
    for k, (x, y, s) in enumerate(positions):
        p = back(prog(lt, 0.8 + k * 0.2, 0.25))
        if p > 0.02: bubble(d, x, y, s * p, C if k % 2 else Y)
    pop_line(d, lt, 2.2, 540, 1430, "HABLARON MÁS", 150, C)
    slide_line(d, lt, 2.5, 540, 1550, "y los chicos respondieron más", 46, C, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    bgc = mix(K, (55, 10, 10), ease_in_out(prog(lt, 1.8, 0.8)))
    d.rectangle([0, 0, S(1080), S(1920)], fill=bgc)
    slide_line(d, lt, 0.05, 540, 290, "CON LA TABLET", 150, R, bg=bgc)
    slide_line(d, lt, 0.3, 540, 440, "HABLARON MENOS", 130, C, bg=bgc)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        sx, sy = shake(lt, 1.8, 0.4, 14)
        tablet(d, 540 + sx, 880 + sy, 660 * e, 620 * e)
    bb = prog(lt, 1.0, 0.25)
    if bb > 0:
        bubble(d, 890, 590, 80 * back(bb), C)
    pop_line(d, lt, 1.8, 540, 880, "NO TOQUES AHÍ", 96, Y, bg=(70, 120, 230))
    slide_line(d, lt, 2.4, 540, 1290, "más retos y comentarios sobre el aparato", 46, C, kind="SemiBold", dy=20, bg=bgc)
    slide_line(d, lt, 2.6, 540, 1350, "y menos sobre el cuento", 46, C, kind="SemiBold", dy=20, bg=bgc)
    slide_line(d, lt, 2.85, 540, 1430, "Munzer et al., Pediatrics, 2019", 38, G, kind="SemiBold", dy=20, bg=bgc)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.05, 540, 300, "¿Y POR QUÉ", 150, C)
    slide_line(d, lt, 0.3, 540, 460, "IMPORTA?", 170, Y)
    words = [("SE CHARLA", 660, C), ("SE PREGUNTA", 830, C), ("SE RESPONDE", 1000, C)]
    for k, (txt, y, c) in enumerate(words):
        pop_line(d, lt, 0.8 + k * 0.4, 540, y, txt, 130, c)
    stamp(d, lt, 2.3, 540, 1260, 430, 110, "AYUDA AL LENGUAJE", fill=Y, ink=K, size=108)
    slide_line(d, lt, 2.8, 540, 1430, "leer juntos y conversar", 46, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 370, "SI PODÉS:", 130, C)
    slide_line(d, lt, 0.3, 540, 530, "CUENTO DE PAPEL", 140, Y)
    book(d, 540, 850, 200 * back(prog(lt, 0.5, 0.35)) + 1, Y)
    pop_line(d, lt, 1.3, 540, 1160, "¿Y SI ES TABLET?", 110, C)
    pop_line(d, lt, 1.6, 540, 1320, "HABLÁ IGUAL", 150, GREEN)
    slide_line(d, lt, 2.1, 540, 1450, "preguntale qué ve y qué pasaría después", 40, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "rustle"); ev(0.3, "pop", 0.2); ev(0.6, "thump"); ev(1.4, "stamp"); ev(2.0, "tap")
ev(4.05, "tap", -0.3); ev(4.25, "tap", 0.3)
for k in range(14): ev(4.65 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(6.1, "thump"); ev(6.4, "tap"); ev(6.6, "tap")
ev(8.05, "rustle"); ev(8.3, "tap")
for k in range(6): ev(8.8 + k * 0.2, "pop", 0.4 if k % 2 else -0.4)
ev(10.2, "thump"); ev(10.5, "tap")
ev(12.05, "tap", -0.3); ev(12.3, "tap", 0.3); ev(12.4, "pop"); ev(13.0, "pop", 0.4); ev(13.8, "buzz"); ev(14.4, "tap"); ev(14.6, "tap"); ev(14.85, "tap")
ev(16.05, "tap"); ev(16.3, "pop"); ev(16.8, "pop", -0.3); ev(17.2, "pop", 0.3); ev(17.6, "pop", -0.3); ev(18.3, "stamp"); ev(18.8, "tap")
ev(20.1, "tap"); ev(20.3, "rustle"); ev(20.5, "pop"); ev(21.3, "pop", -0.2); ev(21.6, "thump"); ev(22.1, "shimmer")

if __name__ == "__main__":
    main(BEATS_EP)
