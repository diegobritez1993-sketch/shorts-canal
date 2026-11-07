"""Short 2026-11-07 15:00 — Curiosidades y hábitos: caminar te vuelve más creativo.
Fuente: Oppezzo y Schwartz, "Give Your Ideas Some Legs", J. Exp. Psychol.: Learning, Memory and Cognition 2014
(vía Stanford Graduate School of Education / Stanford News, 24/04/2014): 176 universitarios y adultos;
caminando, la producción creativa subió en promedio 60% vs. sentados (cinta de correr mirando una pared en blanco);
el efecto siguió un rato al volver a sentarse; afuera, 100% de los que caminaban logró al menos una analogía
de alta calidad vs. 50% de los que estaban sentados adentro.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def bulb(d, cx, cy, s, glow):
    """Lamparita: glow 0 (apagada) .. 1 (prendida)."""
    if glow > 0.05:
        for k in range(8):
            a = k / 8 * math.tau - math.pi / 2
            r0, r1 = s * 0.62, s * (0.62 + 0.25 * glow)
            d.line([S(cx + math.cos(a) * r0), S(cy - s * 0.12 + math.sin(a) * r0),
                    S(cx + math.cos(a) * r1), S(cy - s * 0.12 + math.sin(a) * r1)], fill=mix(K, Y, glow), width=int(S(max(2, s * 0.05))))
    col = mix((70, 70, 70), Y, glow)
    circle(d, cx, cy - s * 0.12, s * 0.42, fill=col)
    d.polygon([(S(cx - s * 0.26), S(cy + s * 0.12)), (S(cx + s * 0.26), S(cy + s * 0.12)),
               (S(cx + s * 0.17), S(cy + s * 0.38)), (S(cx - s * 0.17), S(cy + s * 0.38))], fill=col)
    for k in range(3):
        y = cy + s * (0.42 + k * 0.1)
        rrect(d, cx - s * 0.17, y, cx + s * 0.17, y + s * 0.07, s * 0.03, fill=C)

def walker(d, cx, cy, s, t, col=C, speed=6.0):
    """Persona caminando (palitos) con piernas y brazos animados."""
    w = max(2, int(S(s * 0.09)))
    ph = math.sin(t * speed)
    hx, hy = cx, cy - s * 0.78
    circle(d, hx, hy, s * 0.13, fill=col)
    sh, hip = (cx, cy - s * 0.6), (cx, cy - s * 0.1)
    d.line([S(sh[0]), S(sh[1]), S(hip[0]), S(hip[1])], fill=col, width=w)
    for sg in (1, -1):
        a = sg * ph * 0.5
        d.line([S(hip[0]), S(hip[1]), S(hip[0] + math.sin(a) * s * 0.5), S(hip[1] + math.cos(a) * s * 0.5)], fill=col, width=w)
        b = -sg * ph * 0.45
        d.line([S(sh[0]), S(sh[1] + s * 0.05), S(sh[0] + math.sin(b) * s * 0.38), S(sh[1] + s * 0.05 + math.cos(b) * s * 0.38)], fill=col, width=w)

def sitter(d, cx, cy, s, col=C, chair=G):
    """Persona sentada en una silla."""
    w = max(2, int(S(s * 0.09)))
    d.line([S(cx - s * 0.05), S(cy - s * 0.1), S(cx + s * 0.45), S(cy - s * 0.1)], fill=chair, width=w)
    d.line([S(cx - s * 0.05), S(cy - s * 0.1), S(cx - s * 0.05), S(cy - s * 0.75)], fill=chair, width=w)
    d.line([S(cx + s * 0.05), S(cy - s * 0.1), S(cx + s * 0.05), S(cy + s * 0.4)], fill=chair, width=w)
    d.line([S(cx + s * 0.4), S(cy - s * 0.1), S(cx + s * 0.4), S(cy + s * 0.4)], fill=chair, width=w)
    circle(d, cx + s * 0.1, cy - s * 0.82, s * 0.13, fill=col)
    d.line([S(cx + s * 0.1), S(cy - s * 0.65), S(cx + s * 0.1), S(cy - s * 0.18)], fill=col, width=w)
    d.line([S(cx + s * 0.1), S(cy - s * 0.18), S(cx + s * 0.5), S(cy - s * 0.18), S(cx + s * 0.5), S(cy + s * 0.4)], fill=col, width=w)

def b1(d, t):
    # texto grande desde el frame 1
    text_c(d, 540, 820, "¿TE TRABÁS", "A", 190, C)
    pop_line(d, t, 0.3, 540, 1010, "CON UNA IDEA?", 150, C)
    e = back(prog(t, 0.0, 0.35))
    glow = 0.0 if t < 1.6 else (0.15 + 0.1 * math.sin(t * 40) if t < 2.4 else ease_out(prog(t, 2.4, 0.3)))
    if e > 0.02: bulb(d, 540, 420, 330 * e, glow)
    sx, sy = shake(t, 2.4, 0.35, 16)
    pop_line(d, t, 1.6, 540 + sx, 1225 + sy, "LEVANTATE", 170, Y)
    pop_line(d, t, 2.0, 540 + sx, 1425 + sy, "Y CAMINÁ", 170, Y)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "STANFORD LO PROBÓ", 115, C)
    slide_line(d, lt, 0.3, 540, 390, "sentados vs. caminando", 48, C, kind="SemiBold", dy=25)
    n = int(176 * ease_out(prog(lt, 0.5, 1.3)))
    pop_line(d, lt, 0.5, 540, 600, str(n), 230, Y)
    slide_line(d, lt, 0.8, 540, 760, "personas", 56, C, kind="Bold", dy=25)
    # fila de personitas que aparecen
    for k in range(7):
        p = back(prog(lt, 1.0 + k * 0.1, 0.3))
        if p > 0.02: person(d, 150 + k * 130, 1000, 140 * p, C if k % 2 else Y)
    pill(d, lt, 2.0, 540, 1230, 820, "TEST: USOS NUEVOS PARA OBJETOS", fill=K2, ink=C, size=38, h=100)
    slide_line(d, lt, 2.4, 540, 1340, "ej.: ¿para qué más sirve un botón?", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1420, "Oppezzo y Schwartz, Stanford, 2014", 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "CAMINANDO TUVIERON", 110, C)
    # barras sentado vs caminando
    base = 1250
    p = ease_out(prog(lt, 0.5, 1.0))
    h1 = 260 * p
    h2 = 260 * 1.6 * ease_out(prog(lt, 0.9, 1.2))
    rrect(d, 260, base - h1, 460, base, 20, fill=(80, 80, 80))
    rrect(d, 620, base - h2, 820, base, 20, fill=Y)
    if p > 0.05:
        sitter(d, 340, base + 160, 120)
        walker(d, 720, base + 150, 120, lt)
    slide_line(d, lt, 0.6, 360, base + 290, "sentados", 42, G, kind="Bold", dy=15)
    slide_line(d, lt, 1.0, 720, base + 290, "caminando", 42, Y, kind="Bold", dy=15)
    stamp(d, lt, 2.1, 540, 470, 260, 110, "+60%", fill=Y, ink=K, size=170)
    slide_line(d, lt, 2.4, 540, 610, "más ideas creativas, en promedio", 46, C, kind="SemiBold", dy=20)

def treadmill(d, cx, cy, w, t):
    rrect(d, cx - w / 2, cy, cx + w / 2, cy + 40, 20, fill=(70, 70, 70))
    off = (t * 220) % 60
    for k in range(int(w / 60) + 1):
        x = cx - w / 2 + 20 + k * 60 - off
        if cx - w / 2 + 10 < x < cx + w / 2 - 20:
            d.rectangle([S(x), S(cy + 14), S(x + 20), S(cy + 26)], fill=G)
    d.line([S(cx + w / 2 - 40), S(cy), S(cx + w / 2 - 10), S(cy - 300)], fill=C, width=S(12))
    rrect(d, cx + w / 2 - 70, cy - 330, cx + w / 2 + 40, cy - 290, 14, fill=C)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 270, "Y NI SIQUIERA", 120, C)
    pop_line(d, lt, 0.3, 540, 420, "HIZO FALTA SALIR", 130, Y)
    e = ease_out(prog(lt, 0.5, 0.4))
    if e > 0.02:
        # pared en blanco
        d.rectangle([S(850 + 200 * (1 - e)), S(620), S(1080), S(1200)], fill=(205, 200, 190))
        treadmill(d, 470, 1120, 520, lt)
        walker(d, 450, 1120 - 8, 230, lt, speed=9)
    slide_line(d, lt, 1.4, 540, 1340, "caminaban en una cinta", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.6, 540, 1410, "mirando una pared en blanco", 50, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.4, 540, 1570, 620, "Y FUNCIONÓ IGUAL", fill=R, ink=C, size=44, h=100)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 270, "Y AL VOLVER", 130, C)
    pop_line(d, lt, 0.3, 540, 420, "A SENTARSE...", 130, C)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        sitter(d, 470, 1080, 300 * e)
        glow = ease_out(prog(lt, 1.2, 0.4))
        bulb(d, 560, 655, 150 * e, glow)
    sx, sy = shake(lt, 1.6, 0.35, 14)
    pop_line(d, lt, 1.4, 540 + sx, 1300 + sy, "LAS IDEAS SEGUÍAN", 120, Y)
    slide_line(d, lt, 2.0, 540, 1430, "un rato después de caminar", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.3, 540, 1510, "Stanford, J. Exp. Psychol. 2014", 36, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "LA PRÓXIMA VEZ:", 110, C)
    pop_line(d, lt, 0.25, 540, 480, "5 MINUTOS", 150, Y)
    pop_line(d, lt, 0.45, 540, 630, "DE CAMINATA", 150, Y)
    walker(d, lerp(-100, 1180, prog(lt, 0.6, 2.6)), 1000, 200, lt, col=C)
    pop_line(d, lt, 1.2, 540, 1230, "¿VOS PENSÁS MEJOR", 105, C)
    pop_line(d, lt, 1.4, 540, 1360, "CAMINANDO?", 130, C)
    pill(d, lt, 1.9, 540, 1510, 560, "SÍ O NO", fill=Y, ink=K, size=50, h=110)
    slide_line(d, lt, 2.2, 540, 1630, "contalo en los comentarios", 44, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.3, "pop", 0.3)
for k in range(5): ev(1.65 + k * 0.15, "click", 0.4 if k % 2 else -0.4)
ev(1.6, "pop", -0.2); ev(2.0, "pop", 0.2); ev(2.4, "ding"); ev(2.45, "shimmer")
ev(4.1, "tap"); ev(4.3, "tap", 0.3)
for k in range(10): ev(4.5 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(4.8, "pop")
for k in range(7): ev(5.0 + k * 0.1, "pop", -0.6 + k * 0.2)
ev(6.0, "swipe"); ev(6.4, "tap"); ev(6.6, "tap")
ev(8.1, "tap")
for k in range(8): ev(8.5 + k * 0.14, "tick", 0.3 if k % 2 else -0.3)
ev(9.9, "stamp"); ev(10.1, "thump"); ev(10.4, "tap")
ev(12.1, "tap"); ev(12.3, "pop"); ev(12.5, "rustle")
for k in range(6): ev(12.8 + k * 0.33, "tap", 0.2 if k % 2 else -0.2)
ev(13.4, "tap"); ev(13.6, "tap"); ev(14.4, "thump")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.5, "pop"); ev(17.2, "ding"); ev(17.3, "shimmer")
ev(17.4, "thump"); ev(18.0, "tap"); ev(18.3, "tap")
ev(20.05, "tap"); ev(20.25, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.6, "swipe")
ev(21.2, "pop"); ev(21.4, "pop"); ev(21.9, "thump"); ev(22.2, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
