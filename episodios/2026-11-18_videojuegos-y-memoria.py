"""Short 2026-11-18 20:00 — Chicos y pantallas: videojuegos, memoria y control de impulsos.

Fuente:
- Chaarani et al., Univ. de Vermont, "Association of Video Gaming With Cognitive Performance Among Children",
  JAMA Network Open, 24/10/2022 (DOI 10.1001/jamanetworkopen.2022.35721). Datos del estudio ABCD (NIH).
- Comunicado NIH / EurekAlert 24/10/2022: casi 2.000 chicos de 9 y 10 años; los que jugaban 3 h o más por día
  vs. los que nunca jugaban: más rápidos y precisos en 2 tareas de control de impulsos y memoria; más actividad
  cerebral en zonas de atención y memoria (resonancia). Diseño transversal: no prueba causa y efecto
  (puede que los chicos con mejor rendimiento jueguen más). No midieron qué tipo de juegos.
  No avala el tiempo de pantalla ilimitado. La Academia Americana de Pediatría recomienda 1 a 2 h por día
  de videojuegos para chicos más grandes. Problemas de salud mental algo más altos en los que jugaban,
  pero sin diferencia significativa.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

def gamepad(d, cx, cy, s, col=C, ink=K, press=0.0):
    """Joystick genérico: cuerpo con dos agarres, cruz y 2 botones."""
    circle(d, cx - s * 0.32, cy + s * 0.08, s * 0.24, fill=col)
    circle(d, cx + s * 0.32, cy + s * 0.08, s * 0.24, fill=col)
    rrect(d, cx - s * 0.42, cy - s * 0.2, cx + s * 0.42, cy + s * 0.2, s * 0.18, fill=col)
    # cruz
    a, b = s * 0.04, s * 0.11
    d.rectangle([S(cx - s * 0.32 - b), S(cy - a), S(cx - s * 0.32 + b), S(cy + a)], fill=ink)
    d.rectangle([S(cx - s * 0.32 - a), S(cy - b), S(cx - s * 0.32 + a), S(cy + b)], fill=ink)
    # botones
    circle(d, cx + s * 0.25, cy + s * 0.05, s * 0.055 * (1 - 0.3 * press), fill=R)
    circle(d, cx + s * 0.38, cy - s * 0.07, s * 0.055, fill=Y if col != Y else K)

def brain(d, cx, cy, s, col, glow=0.0):
    """Cerebro estilizado: blobs + surco central; glow ilumina dos zonas en amarillo."""
    rnd = [(-0.25, -0.12, 0.26), (0.0, -0.22, 0.27), (0.25, -0.12, 0.26), (-0.3, 0.12, 0.22),
           (0.0, 0.06, 0.28), (0.3, 0.12, 0.22)]
    for x, y, r in rnd:
        circle(d, cx + x * s, cy + y * s, r * s, fill=col)
    d.line([S(cx), S(cy - s * 0.45), S(cx), S(cy + s * 0.3)], fill=K, width=SW(s * 0.025))
    for sd in (-1, 1):
        d.arc([S(cx + sd * s * 0.12 - s * 0.12), S(cy - s * 0.2), S(cx + sd * s * 0.12 + s * 0.12), S(cy + s * 0.04)],
              0 if sd > 0 else 180, 180 if sd > 0 else 360, fill=K, width=SW(s * 0.02))
    # tronco
    rrect(d, cx + s * 0.05, cy + s * 0.3, cx + s * 0.17, cy + s * 0.52, s * 0.05, fill=col)
    if glow > 0:
        for x, y in ((-0.22, -0.2), (0.22, -0.2)):
            circle(d, cx + x * s, cy + y * s, s * 0.12 * glow, fill=R)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 330, "¿LOS JUEGOS", 165, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 500, "LE QUEMAN", 175, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 680, "LA CABEZA?", 190, R, dur=0.25)
    e = back(prog(t, 0.8, 0.35))
    if e > 0.02:
        pr = 0.5 + 0.5 * math.sin(t * 18) if t > 1.2 else 0
        gamepad(d, 540, 1000, 520 * e, col=C, press=pr)
    slide_line(d, t, 2.3, 540, 1290, "un estudio grande encontró algo", 50, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.5, 540, 1360, "que no esperabas", 50, Y, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    n = int(2000 * ease_out(prog(lt, 0.1, 1.0)))
    text_c(d, 540, 300, "CASI " + fmt_num(n), "A", 170, Y)
    slide_line(d, lt, 0.4, 540, 450, "CHICOS DE 9 Y 10 AÑOS", 100, C)
    # dos grupos: nunca vs 3 h+
    p1 = prog(lt, 1.0, 0.35); p2 = prog(lt, 1.4, 0.35)
    if p1 > 0:
        e = back(p1)
        gamepad(d, 290, 760, 300 * e, col=(90, 90, 90))
        ban(d, 290, 760, 180 * e, ease_out(prog(lt, 1.3, 0.3)), width=22)
        text_c(d, 290, 990, "NUNCA JUEGAN", "Black", 44, C, alpha=clamp(p1 * 2))
    if p2 > 0:
        e = back(p2)
        gamepad(d, 790, 760, 300 * e, col=Y)
        text_c(d, 790, 990, "3 H O MÁS", "Black", 44, Y, alpha=clamp(p2 * 2))
        text_c(d, 790, 1045, "POR DÍA", "Black", 44, Y, alpha=clamp(p2 * 2))
    pop_line(d, lt, 2.2, 540, 1200, "VS.", 110, C)
    slide_line(d, lt, 2.6, 540, 1330, "Chaarani et al., Univ. de Vermont, JAMA Network Open 2022", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 280, "LOS QUE JUGABAN 3 H+", 105, C)
    slide_line(d, lt, 0.3, 540, 390, "en pruebas de memoria y control de impulsos:", 42, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        glow = ease_out(prog(lt, 1.2, 0.5)) * (0.85 + 0.15 * math.sin(lt * 10))
        brain(d, 540, 700, 440 * e, C, glow=glow)
    pill(d, t, 10.2, 540, 1030, 700, "MÁS RÁPIDOS", fill=Y, ink=K, size=50, h=115)
    pill(d, t, 10.6, 540, 1170, 700, "MÁS PRECISOS", fill=Y, ink=K, size=50, h=115)
    slide_line(d, lt, 3.0, 540, 1300, "y más actividad en zonas de atención y memoria", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 3.1, 540, 1360, "NIH / EurekAlert, 24/10/2022", 32, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    e = back(prog(lt, 0.0, 0.35))
    if e > 0.02: warning(d, 540, 390, 300 * e)
    pop_line(d, lt, 0.4, 540, 640, "OJO: RELACIÓN,", 120, C)
    pop_line(d, lt, 0.6, 540, 780, "NO CAUSA", 150, R)
    slide_line(d, lt, 1.2, 540, 920, "quizás los más hábiles juegan más", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 1.5, 540, 985, "y no midieron qué tipo de juegos", 46, C, kind="SemiBold", dy=20)
    stamp(d, t, 14.6, 540, 1180, 400, 85, "NO ES BARRA LIBRE", fill=Y, ink=K, size=82)
    slide_line(d, lt, 3.1, 540, 1310, "los autores no avalan pantalla sin límite", 38, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "LOS PEDIATRAS", 130, C)
    slide_line(d, lt, 0.3, 540, 400, "(Academia Americana de Pediatría) recomiendan", 40, C, kind="SemiBold", dy=20)
    pr = ease_out(prog(lt, 0.5, 1.2))
    if lt > 0.5:
        clock(d, 330, 700, 200, pr, turns=2, fill_deg=60)
        text_c(d, 760, 640, "1 A 2 H", "A", 150, Y)
        text_c(d, 760, 770, "POR DÍA", "Black", 52, C)
    toggle_row(d, 110, 950, "Jugá con él", ease_out(prog(lt, 1.8, 0.3)), sub="así ves qué juega")
    toggle_row(d, 110, 1130, "Primero la tarea", ease_out(prog(lt, 2.4, 0.3)), sub="y dormir bien; el juego después")
    slide_line(d, lt, 3.0, 540, 1340, "para chicos más grandes, vía NIH 2022", 32, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 280, "NI DEMONIO", 125, C)
    slide_line(d, lt, 0.3, 540, 440, "NI NIÑERA", 125, C)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02: gamepad(d, 540, 680, 300 * e, col=Y)
    pop_line(d, lt, 1.2, 540, 920, "¿CUÁNTO JUEGA", 125, Y)
    pop_line(d, lt, 1.4, 540, 1060, "EL TUYO?", 150, Y)
    slide_line(d, lt, 2.0, 540, 1200, "dejalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
ev(0.8, "pop")
for k in range(6): ev(1.3 + k * 0.17, "click", -0.3 + k * 0.12)
ev(2.3, "tap"); ev(2.5, "tap")
for k in range(10): ev(4.1 + k * 0.1, "tick")
ev(4.4, "tap"); ev(5.0, "pop", -0.4); ev(5.3, "swipe", -0.4); ev(5.4, "pop", 0.4); ev(6.2, "thump"); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.6, "pop"); ev(9.2, "shimmer"); ev(10.2, "pop", -0.2); ev(10.6, "pop", 0.2); ev(11.0, "tap")
ev(12.0, "pop"); ev(12.4, "thump"); ev(12.6, "thump"); ev(13.2, "tap"); ev(13.5, "tap"); ev(14.45, "whoosh"); ev(14.6, "stamp"); ev(15.1, "tap")
ev(16.1, "tap"); ev(16.3, "tap")
for k in range(10): ev(16.5 + k * 0.12, "tick")
ev(17.8, "toggle"); ev(18.4, "toggle"); ev(19.0, "tap")
ev(20.1, "tap"); ev(20.3, "tap"); ev(20.7, "pop"); ev(21.2, "pop"); ev(21.4, "thump"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
