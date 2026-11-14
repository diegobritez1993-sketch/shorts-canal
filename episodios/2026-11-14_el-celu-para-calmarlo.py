"""Short 2026-11-14 20:00 — Chicos y pantallas: darle el celu a un chico para que se calme.

Fuente:
- Radesky, Kaciroti, Weeks, Schaller y Miller, JAMA Pediatrics 2022 (doi 10.1001/jamapediatrics.2022.4793),
  Univ. de Michigan / Michigan Medicine. Vía ScienceDaily (12/12/2022) y News-Medical.
- 422 padres y 422 chicos de 3 a 5 años; seguimiento de 6 meses (antes de la pandemia).
- Usar seguido celulares/tablets para calmar a chicos alterados se asoció con más desregulación emocional:
  cambios bruscos de tristeza a excitación, cambios repentinos de ánimo, más impulsividad.
  Más fuerte en varones y en chicos con hiperactividad, impulsividad o temperamento fuerte. Asociación, no causa.
- Radesky: el dispositivo "distrae" pero "no enseña una habilidad"; de vez en cuando (viajes) es realista.
- Alternativas: abrazos, hamacarse/saltar, música, mirar un libro, ponerle nombre a la emoción.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def kid_face(d, cx, cy, r, mood, t):
    """Carita genérica: mood -1 = llora, 0 = neutra, 1 = contenta."""
    circle(d, cx, cy, r, fill=C)
    # ojos
    for sx in (-1, 1):
        ex, ey = cx + sx * r * 0.35, cy - r * 0.15
        if mood < -0.3:
            d.arc([S(ex - r * 0.14), S(ey - r * 0.1), S(ex + r * 0.14), S(ey + r * 0.15)], 200, 340, fill=K, width=int(S(max(4, r * 0.06))))
            # lágrimas
            for k in range(2):
                tt = (t * 1.3 + k * 0.5) % 1.0
                circle(d, ex + sx * r * 0.05, ey + r * 0.2 + tt * r * 0.7, r * 0.07 * (1 - tt * 0.4), fill=(90, 170, 255))
        else:
            circle(d, ex, ey, r * 0.08, fill=K)
    # boca
    mw, my = r * 0.38, cy + r * 0.42
    if mood < -0.3:
        d.ellipse([S(cx - mw * 0.55), S(my - r * 0.12), S(cx + mw * 0.55), S(my + r * 0.14)], fill=K)
    elif mood > 0.3:
        d.arc([S(cx - mw), S(my - r * 0.35), S(cx + mw), S(my + r * 0.05)], 20, 160, fill=K, width=int(S(max(4, r * 0.07))))
    else:
        d.line([S(cx - mw * 0.6), S(my - r * 0.1), S(cx + mw * 0.6), S(my - r * 0.1)], fill=K, width=int(S(max(4, r * 0.06))))

def meter(d, cx, cy, r, val):
    """Medidor semicircular: val 0 (rojo, alterado) .. 1 (verde, calmo)."""
    segs = [(R, 180, 240), (Y, 240, 300), (GREEN, 300, 360)]
    for col, a0, a1 in segs:
        d.arc([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], a0, a1, fill=col, width=S(44))
    ang = math.radians(180 + 180 * val)
    d.line([S(cx), S(cy), S(cx + math.cos(ang) * r * 0.85), S(cy + math.sin(ang) * r * 0.85)], fill=C, width=S(14))
    circle(d, cx, cy, 24, fill=C)

def wave(d, x0, x1, cy, amp, t, col, p):
    pts = []
    n = 60
    for i in range(int(n * p) + 1):
        x = lerp(x0, x1, i / n)
        # cambios bruscos: zigzag irregular
        a = amp * (math.sin(i * 0.9 + t * 3) * 0.6 + (1 if (i // 6) % 2 else -1) * 0.5)
        pts.append((S(x), S(cy + a)))
    if len(pts) > 1:
        d.line(pts, fill=col, width=S(12), joint="curve")

def note(d, cx, cy, s, col):
    circle(d, cx - s * 0.18, cy + s * 0.3, s * 0.16, fill=col)
    circle(d, cx + s * 0.32, cy + s * 0.2, s * 0.16, fill=col)
    d.line([S(cx - s * 0.04), S(cy + s * 0.3), S(cx - s * 0.04), S(cy - s * 0.35)], fill=col, width=int(S(s * 0.08)))
    d.line([S(cx + s * 0.46), S(cy + s * 0.2), S(cx + s * 0.46), S(cy - s * 0.45)], fill=col, width=int(S(s * 0.08)))
    d.line([S(cx - s * 0.04), S(cy - s * 0.35), S(cx + s * 0.46), S(cy - s * 0.45)], fill=col, width=int(S(s * 0.12)))

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        kid_face(d, 400, 640, 190 * e, -1 if t < 2.2 else 1, t)
    pp = ease_out(prog(t, 1.4, 0.5))
    if pp > 0.01:
        phone(d, 760 + (1 - pp) * 400, 700, 180, 300)
        rrect(d, 700 + (1 - pp) * 400, 600, 820 + (1 - pp) * 400, 780, 18, fill=Y)
    pop_line(d, t, 0.0, 540, 1050, "¿LE DAS EL CELU", 135, C)
    pop_line(d, t, 0.3, 540, 1200, "PARA QUE SE CALME?", 120, Y)
    pill(d, t, 2.3, 540, 1380, 520, "OJO CON ESTO", fill=R, ink=C, size=50, h=100)

def b2(d, t):
    lt = t - 4
    n = int(round(422 * ease_out(prog(lt, 0.1, 1.0))))
    pop_line(d, lt, 0.05, 540, 310, fmt_num(n), 220, Y)
    slide_line(d, lt, 0.35, 540, 470, "FAMILIAS", 120, C)
    # filas de personitas grandes y chicas
    for k in range(5):
        pk = back(prog(lt, 0.7 + k * 0.1, 0.3))
        if pk > 0.02:
            x = 180 + k * 180
            person(d, x - 30, 760, 170 * pk, C)
            person(d, x + 40, 800, 100 * pk, Y)
    pill(d, lt, 1.6, 540, 990, 600, "CHICOS DE 3 A 5 AÑOS", fill=Y, ink=K, size=44, h=96)
    slide_line(d, lt, 2.0, 540, 1120, "los siguieron durante 6 meses", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1200, "Radesky et al., Univ. de Michigan, JAMA Pediatrics 2022", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 290, "EN EL MOMENTO", 130, C)
    pop_line(d, lt, 0.35, 540, 420, "FUNCIONA…", 140, GREEN)
    e = ease_out(prog(lt, 0.5, 0.3))
    if e > 0.01:
        val = ease_in_out(prog(lt, 0.9, 0.8))
        meter(d, 540, 900, 300 * e, val)
        text_c(d, 540 - 300, 960, "ALTERADO", "Black", 34, R)
        text_c(d, 540 + 300, 960, "CALMO", "Black", 34, GREEN)
    sx, sy = shake(lt, 2.15, 0.35, 14)
    stamp(d, lt, 2.1, 540 + sx, 1150 + sy, 260, 90, "PERO…", fill=R, ink=C, size=130)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "USARLO SEGUIDO", 125, C)
    slide_line(d, lt, 0.3, 540, 420, "SE ASOCIÓ CON", 110, C)
    wave(d, 120, 960, 650, 120, lt, Y, ease_out(prog(lt, 0.5, 1.0)))
    pop_line(d, lt, 1.3, 540, 880, "CAMBIOS BRUSCOS", 115, R)
    pop_line(d, lt, 1.5, 540, 1010, "DE HUMOR", 115, R)
    pill(d, lt, 1.9, 540, 1160, 520, "+ IMPULSIVIDAD", fill=Y, ink=K, size=46, h=96)
    slide_line(d, lt, 2.3, 540, 1290, "sobre todo en varones y chicos muy inquietos", 40, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1360, "es una relación, no prueba que lo cause", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "EL CELU DISTRAE", 125, C)
    pop_line(d, lt, 0.35, 540, 420, "PERO NO ENSEÑA", 125, Y)
    slide_line(d, lt, 0.7, 540, 540, "a calmarse solo, dice la autora", 44, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.0, 540, 680, "MEJOR PROBÁ:", 90, C)
    items = [("ABRAZO", lambda x, y, s: heart(d, x, y, s, R)),
             ("MOVERSE", lambda x, y, s: person(d, x, y + s * 0.1, s * 1.1, Y)),
             ("MÚSICA", lambda x, y, s: note(d, x, y, s, C)),
             ("NOMBRAR", lambda x, y, s: bubble(d, x, y, s, Y))]
    for k, (lab, ico) in enumerate(items):
        pk = back(prog(lt, 1.3 + k * 0.25, 0.3))
        if pk > 0.02:
            x = 300 + (k % 2) * 480
            y = 900 + (k // 2) * 330
            rrect(d, x - 200 * pk, y - 130 * pk, x + 200 * pk, y + 130 * pk, 40, fill=K2)
            if pk > 0.8:
                ico(x, y - 30, 120)
                text_c(d, x, y + 85, lab, "Black", 40, C, bg=K2)
    slide_line(d, lt, 2.6, 540, 1500, "ponerle nombre: \"estás enojado\"", 40, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "DE VEZ EN CUANDO", 110, C)
    slide_line(d, lt, 0.3, 540, 420, "(UN VIAJE) ESTÁ BIEN", 100, GREEN)
    pop_line(d, lt, 0.9, 540, 660, "¿Y A VOS QUÉ", 140, C)
    pop_line(d, lt, 1.15, 540, 810, "TE FUNCIONA?", 150, Y)
    pill(d, lt, 1.7, 540, 1000, 800, "CONTALO EN COMENTARIOS", fill=R, ink=C, size=42, h=100)
    slide_line(d, lt, 2.1, 540, 1130, "y mandáselo a alguien con chicos", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop"); ev(0.3, "pop"); ev(1.4, "swipe"); ev(2.2, "shimmer"); ev(2.3, "click")
ev(4.05, "pop")
for k in range(10): ev(4.1 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(4.35, "swipe")
for k in range(5): ev(4.7 + k * 0.1, "pop", -0.4 + k * 0.2)
ev(5.6, "click"); ev(6.0, "swipe"); ev(6.4, "tap")
ev(8.1, "pop"); ev(8.35, "pop"); ev(8.5, "swipe")
for k in range(8): ev(8.9 + k * 0.1, "tick", 0.0)
ev(9.7, "ding"); ev(10.1, "stamp")
ev(12.1, "swipe"); ev(12.3, "swipe"); ev(12.5, "rustle"); ev(13.3, "thump"); ev(13.5, "pop"); ev(13.9, "click"); ev(14.3, "swipe"); ev(14.5, "tap")
ev(16.1, "pop"); ev(16.35, "thump"); ev(16.7, "swipe"); ev(17.0, "pop")
for k in range(4): ev(17.3 + k * 0.25, "pop", -0.3 if k % 2 == 0 else 0.3)
ev(18.6, "tap")
ev(20.1, "swipe"); ev(20.3, "shimmer"); ev(20.9, "pop"); ev(21.15, "thump"); ev(21.7, "click"); ev(22.1, "swipe")

if __name__ == "__main__":
    main(BEATS_EP)
