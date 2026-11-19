"""Short 2026-11-19 15:00 — Curiosidades y hábitos: el "efecto puerta" (entrás a una pieza y te olvidás a qué ibas).

Fuente:
- Radvansky, Krawietz y Tamplin, Quarterly Journal of Experimental Psychology 2011.
- Comunicado Univ. de Notre Dame (16-17/11/2011), "Walking through doorways causes forgetting":
  universitarios en un entorno virtual llevaban un objeto de una mesa a otra, en otra pieza (pasando una puerta)
  o a la misma distancia dentro de la misma pieza; tras pasar la puerta se olvidaban más.
  En un laboratorio real (objetos escondidos en cajas) pasó lo mismo. Pasar varias puertas que volvían
  a la pieza de inicio NO mejoró la memoria. Radvansky: la puerta funciona como un "límite de evento"
  y lo de la pieza anterior queda "compartimentado". (El comunicado no da porcentajes: no se muestran cifras.)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

BROWN = (150, 105, 60)

def door(d, cx, cy, w, h, open_p, col=C):
    """Marco de puerta con hoja que se abre (open_p 0..1)."""
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    d.rectangle([S(x0), S(y0), S(x1), S(y1)], fill=(5, 5, 5))
    d.line([S(x0), S(y1), S(x0), S(y0), S(x1), S(y0), S(x1), S(y1)], fill=col, width=SW(14), joint="curve")
    # hoja: se achica en perspectiva hacia la izquierda
    ww = w * (1 - 0.72 * open_p)
    sk = h * 0.08 * open_p
    d.polygon([(S(x0), S(y0)), (S(x0 + ww), S(y0 + sk)), (S(x0 + ww), S(y1 - sk)), (S(x0), S(y1))], fill=BROWN)
    circle(d, x0 + ww - w * 0.12 * (1 - open_p * 0.6), cy, max(4, 14 * (1 - open_p * 0.5)), fill=Y)

def thought(d, cx, cy, r, txt, col, alpha=1.0):
    """Globo de pensamiento con texto adentro."""
    if alpha <= 0.02: return
    c = mix(K, col, alpha)
    circle(d, cx, cy, r, fill=c)
    circle(d, cx - r * 0.7, cy + r * 1.05, r * 0.18, fill=c)
    circle(d, cx - r * 0.95, cy + r * 1.4, r * 0.1, fill=c)
    text_c(d, cx, cy, txt, "A", r * 0.9, K, bg=c)

def folder(d, cx, cy, w, h, col, label=None):
    rrect(d, cx - w / 2, cy - h / 2 - h * 0.14, cx - w / 2 + w * 0.4, cy - h / 2 + 20, 14, fill=col)
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 22, fill=col)
    if label: text_c(d, cx, cy + 8, label, "Black", 38, K, bg=col)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 290, "¿ENTRASTE A UNA PIEZA", 105, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 420, "Y TE OLVIDASTE", 130, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 570, "A QUÉ IBAS?", 170, Y, dur=0.25)
    e = back(prog(t, 0.7, 0.35))
    if e > 0.02:
        op = ease_in_out(prog(t, 1.1, 0.6))
        door(d, 640, 1050, 300 * e, 520 * e, op)
        # la persona camina hacia la puerta
        px = lerp(260, 600, ease_in_out(prog(t, 1.4, 1.2)))
        person(d, px, 1150, 260 * e, C)
        # el pensamiento se borra al llegar a la puerta
        a = 1 - prog(t, 2.4, 0.4)
        thought(d, px - 110, 820, 80, "!", Y, alpha=a * clamp(e))
        if t > 2.7:
            sx, sy = shake(t, 2.7, 0.3, 10)
            thought(d, px - 110 + sx, 820 + sy, 80 * back(prog(t, 2.7, 0.3)), "?", R)
    slide_line(d, t, 2.9, 540, 1440, "y la culpa puede ser de la puerta", 52, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "LO PROBARON", 140, C)
    slide_line(d, lt, 0.3, 540, 390, "universitarios en un juego de piezas virtuales", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 0.45, 540, 445, "llevaban un objeto de una mesa a otra", 40, Y, kind="SemiBold", dy=20)
    # dos planos: misma pieza vs. pasando una puerta
    for k, (cx, lab, has_door, col) in enumerate([(290, "MISMA PIEZA", False, GREEN), (790, "OTRA PIEZA", True, R)]):
        p = prog(lt, 0.7 + k * 0.4, 0.35)
        if p <= 0: continue
        e = back(p)
        w, h = 420 * e, 380 * e
        cy = 780
        rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 20, outline=C, width=8)
        if e > 0.8:
            if has_door:
                d.line([S(cx), S(cy - h / 2), S(cx), S(cy - 50)], fill=C, width=SW(8))
                d.line([S(cx), S(cy + 50), S(cx), S(cy + h / 2)], fill=C, width=SW(8))
                rrect(d, cx - 10, cy - 50, cx + 10, cy + 50, 4, fill=BROWN)
            # mesas
            rrect(d, cx - 170, cy - 30, cx - 110, cy + 30, 8, fill=Y)
            rrect(d, cx + 110, cy - 30, cx + 170, cy + 30, 8, fill=Y)
            # punto que viaja
            q = ease_in_out(prog(lt, 1.6, 1.2))
            circle(d, lerp(cx - 140, cx + 140, q), cy, 22, fill=col)
        text_c(d, cx, 1020, lab, "Black", 44, col, alpha=clamp(p * 2))
    slide_line(d, lt, 2.2, 540, 1150, "MISMA DISTANCIA", 110, C)
    slide_line(d, lt, 2.5, 540, 1280, "Radvansky y cols., Univ. de Notre Dame, Q. J. Exp. Psychol. 2011", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "DESPUÉS DE LA PUERTA", 105, C)
    stamp(d, t, 8.6, 540, 500, 420, 105, "SE OLVIDABAN MÁS", fill=R, ink=K, size=110)
    # barra de "memoria" que se vacía al cruzar
    p = prog(lt, 1.2, 0.3)
    if p > 0:
        a = clamp(p * 2)
        text_c(d, 540, 720, "lo que tenían en la cabeza", "SemiBold", 40, C, alpha=a)
        lvl = 1 - 0.55 * ease_out(prog(lt, 1.6, 0.8))
        rrect(d, 170, 790, 910, 880, 30, outline=C, width=8)
        rrect(d, 190, 810, 190 + 700 * lvl, 860, 20, fill=mix(R, Y, lvl))
    # y en la vida real también: cajas
    for k in range(3):
        q = back(prog(lt, 2.3 + k * 0.15, 0.3))
        if q > 0.02:
            x = 360 + k * 180
            rrect(d, x - 70 * q, 1100 - 60 * q, x + 70 * q, 1100 + 60 * q, 10, fill=BROWN)
            d.line([S(x - 70 * q), S(1100 - 20 * q), S(x + 70 * q), S(1100 - 20 * q)], fill=K, width=SW(6))
    slide_line(d, lt, 2.4, 540, 1250, "y en un laboratorio real, con cajas: igual", 44, Y, kind="Bold", dy=20)
    slide_line(d, lt, 2.8, 540, 1330, "comunicado Univ. de Notre Dame, 16/11/2011", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "¿POR QUÉ PASA?", 140, C)
    slide_line(d, lt, 0.4, 540, 400, "para tu cerebro la puerta es un", 46, C, kind="SemiBold", dy=20)
    pop_line(d, lt, 0.7, 540, 510, "\"LÍMITE DE EVENTO\"", 115, Y)
    # carpeta de la pieza anterior que se cierra y se va a un costado
    p = prog(lt, 1.3, 0.3)
    if p > 0:
        e = back(p)
        mv = ease_in_out(prog(lt, 2.2, 0.6))
        folder(d, lerp(540, 300, mv), 820, 340 * e, 220 * e, mix(Y, (90, 90, 90), mv), "PIEZA 1" if e > 0.8 else None)
        if mv > 0.05:
            folder(d, lerp(800, 780, mv), 820, 340 * mv, 220 * mv, Y, "PIEZA 2" if mv > 0.8 else None)
    slide_line(d, lt, 2.7, 540, 1060, "archiva lo de la pieza anterior", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.85, 540, 1120, "y abre una carpeta nueva", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 3.1, 540, 1230, "Gabriel Radvansky, autor del estudio", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "¿Y SI VOLVÉS?", 140, C)
    slide_line(d, lt, 0.35, 540, 395, "pasar más puertas hasta la pieza del inicio", 42, C, kind="SemiBold", dy=20)
    pop_line(d, lt, 0.7, 540, 490, "NO LES AYUDÓ", 100, R)
    pill(d, t, 17.3, 540, 680, 620, "EL TRUCO", fill=Y, ink=K, size=60, h=120)
    # globo con lo que vas a buscar, que se mantiene
    e = back(prog(lt, 1.6, 0.35))
    if e > 0.02:
        door(d, 760, 960, 180, 300, 0.8)
        person(d, 420, 1010, 200, C)
        thought(d, 380, 820, 70 * e, "!", Y)
    slide_line(d, lt, 2.2, 540, 1210, "antes de cruzar, repetite a qué vas", 48, C, kind="Bold", dy=20)
    slide_line(d, lt, 2.4, 540, 1280, "o llevalo anotado en el celu", 44, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 360, "¿CUÁNTAS VECES", 150, C)
    pop_line(d, lt, 0.35, 540, 530, "TE PASÓ HOY?", 165, Y)
    # contador
    n = int(3 * ease_out(prog(lt, 0.8, 0.9)))
    if lt > 0.8:
        rrect(d, 380, 680, 700, 940, 40, fill=K2, outline=Y, width=8)
        text_c(d, 540, 805, str(n), "A", 210, Y, bg=K2)
    pill(d, t, 21.8, 540, 1080, 520, "¿0? ¿1? ¿3+?", fill=C, ink=K, size=52, h=120)
    slide_line(d, lt, 2.1, 540, 1230, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
ev(0.7, "pop"); ev(1.1, "click", 0.3); ev(1.4, "tap", -0.4); ev(1.8, "tap", -0.2); ev(2.2, "tap", 0.1)
ev(2.4, "shimmer"); ev(2.7, "pop", 0.2); ev(2.9, "tap")
ev(4.1, "tap"); ev(4.3, "tap"); ev(4.45, "tap"); ev(4.7, "pop", -0.4); ev(5.1, "pop", 0.4); ev(5.6, "swipe"); ev(6.2, "tap"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.4, "whoosh"); ev(8.6, "stamp"); ev(9.2, "tap"); ev(9.6, "swipe")
ev(10.3, "pop", -0.4); ev(10.45, "pop", 0); ev(10.6, "pop", 0.4); ev(10.8, "tap")
ev(12.1, "tap"); ev(12.4, "tap"); ev(12.7, "thump"); ev(13.3, "pop"); ev(14.2, "rustle"); ev(14.7, "tap"); ev(14.85, "tap")
ev(16.1, "tap"); ev(16.35, "tap"); ev(16.7, "thump"); ev(17.3, "pop"); ev(17.6, "pop"); ev(17.6, "ding"); ev(18.2, "tap"); ev(18.4, "tap")
ev(20.1, "pop", -0.3); ev(20.35, "thump")
for k in range(3): ev(21.0 + k * 0.25, "tick")
ev(21.8, "pop"); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
