"""Short 2026-11-22 20:00 — Chicos y pantallas: 5 días sin pantallas y leen mejor las emociones.

Fuente:
- Uhls, Michikyan, Morris, Garcia, Small, Zgourou y Greenfield, UCLA, Computers in Human Behavior
  (oct. 2014). Comunicado UCLA Health 21/08/2014 ("In our digital world, are young people losing the
  ability to read emotions?"):
  51 chicos de 6.º grado de una escuela pública del sur de California, 5 días en un campamento de
  naturaleza (Pali Institute) que no permite aparatos electrónicos; grupo control: 54 de la misma escuela
  que siguieron con sus pantallas (fueron al campamento después).
  Pruebas al inicio y al final: 48 fotos de caras (feliz, triste, enojado, asustado) y videos de actores.
  Campamento: errores en fotos de 14,02 a 9,41 en promedio; el control cambió bastante menos.
  En videos, el grupo del campamento mejoró y el control no cambió.
  Uso normal: ~4,5 h por día de escuela (mensajes, tele, videojuegos).
  Greenfield: la interacción social hace falta para aprender a entender las emociones de otros.
  Uhls: "We need device-free time." Estudio chico, de una sola escuela.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

FOREST = (60, 160, 90)

def face(d, cx, cy, r, mood, col=Y, ink=K):
    """Carita: 'feliz', 'triste', 'enojado', 'asustado'."""
    circle(d, cx, cy, r, fill=col)
    ey = cy - r * 0.18
    if mood == "asustado":
        for s in (-1, 1): circle(d, cx + s * r * 0.33, ey, r * 0.15, fill=ink)
    else:
        for s in (-1, 1): circle(d, cx + s * r * 0.33, ey, r * 0.1, fill=ink)
    w = SW(r * 0.09)
    if mood == "feliz":
        d.arc([S(cx - r * 0.45), S(cy - r * 0.2), S(cx + r * 0.45), S(cy + r * 0.55)], 20, 160, fill=ink, width=w)
    elif mood == "triste":
        d.arc([S(cx - r * 0.4), S(cy + r * 0.3), S(cx + r * 0.4), S(cy + r * 0.85)], 200, 340, fill=ink, width=w)
    elif mood == "enojado":
        for s in (-1, 1):
            d.line([S(cx + s * r * 0.55), S(ey - r * 0.32), S(cx + s * r * 0.15), S(ey - r * 0.14)], fill=ink, width=w)
        d.line([S(cx - r * 0.3), S(cy + r * 0.45), S(cx + r * 0.3), S(cy + r * 0.45)], fill=ink, width=w)
    elif mood == "asustado":
        d.ellipse([S(cx - r * 0.17), S(cy + r * 0.25), S(cx + r * 0.17), S(cy + r * 0.65)], fill=ink)

def tree(d, cx, by, s, col=FOREST):
    d.rectangle([S(cx - s * 0.06), S(by - s * 0.3), S(cx + s * 0.06), S(by)], fill=(110, 80, 50))
    for k, (w, y) in enumerate(((0.5, 0.3), (0.4, 0.55), (0.28, 0.78))):
        d.polygon([(S(cx - s * w), S(by - s * y)), (S(cx + s * w), S(by - s * y)), (S(cx), S(by - s * (y + 0.42)))], fill=col)

def tent(d, cx, by, s, col=Y):
    d.polygon([(S(cx - s * 0.6), S(by)), (S(cx + s * 0.6), S(by)), (S(cx), S(by - s * 0.75))], fill=col)
    d.polygon([(S(cx - s * 0.16), S(by)), (S(cx + s * 0.16), S(by)), (S(cx), S(by - s * 0.42))], fill=K)

def fire(d, cx, by, s, t):
    fl = 1 + 0.12 * math.sin(t * 14)
    d.polygon([(S(cx - s * 0.3), S(by)), (S(cx + s * 0.3), S(by)), (S(cx), S(by - s * 0.9 * fl))], fill=(255, 120, 30))
    d.polygon([(S(cx - s * 0.15), S(by)), (S(cx + s * 0.15), S(by)), (S(cx), S(by - s * 0.5 * fl))], fill=Y)
    for s2 in (-1, 1):
        d.line([S(cx - s * 0.45), S(by + s * 0.05 * s2 + 6), S(cx + s * 0.45), S(by - s * 0.05 * s2 + 6)], fill=(110, 80, 50), width=SW(s * 0.1))

def b1(d, t):
    pop_line(d, t, 0.0, 540, 290, "5 DÍAS SIN PANTALLAS", 108, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 430, "¿Y QUÉ CAMBIÓ?", 150, Y, dur=0.25)
    moods = ["feliz", "triste", "enojado", "asustado"]
    for i, m in enumerate(moods):
        e = back(prog(t, 0.7 + i * 0.25, 0.3))
        if e > 0.02:
            x = 240 + (i % 2) * 600 if i < 2 else 240 + (i % 2) * 600
            y = 680 if i < 2 else 1000
            face(d, [270, 810, 270, 810][i], [700, 700, 1010, 1010][i], 120 * e, m, Y if t < 2.8 or i == 0 else C)
    # celular tachado en el medio
    e = back(prog(t, 1.8, 0.3))
    if e > 0.02:
        phone(d, 540, 855, 130 * e, 230 * e)
        ban(d, 540, 855, 150 * e, prog(t, 2.1, 0.25), width=22)
    slide_line(d, t, 2.8, 540, 1300, "LEER CARAS, ALGO QUE SE APRENDE", 70, C, dy=30)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 270, "UN CAMPAMENTO", 140, C)
    slide_line(d, lt, 0.35, 540, 380, "en la naturaleza, sin ningún aparato electrónico", 40, C, kind="SemiBold", dy=20)
    for i, (x, s) in enumerate(((150, 260), (950, 300), (270, 190))):
        e = back(prog(lt, 0.5 + i * 0.15, 0.3))
        if e > 0.02: tree(d, x, 900, s * e)
    e = back(prog(lt, 0.8, 0.35))
    if e > 0.02: tent(d, 680, 900, 360 * e)
    if lt > 1.1: fire(d, 420, 900, 110 * clamp((lt - 1.1) * 3), lt)
    d.rectangle([S(80), S(900), S(1000), S(910)], fill=(70, 70, 70))
    pill(d, t, 5.5, 330, 1050, 380, "51 CHICOS", fill=Y, ink=K, size=52, h=110)
    pill(d, t, 5.7, 750, 1050, 380, "5 DÍAS", fill=C, ink=K, size=52, h=110)
    slide_line(d, lt, 2.1, 540, 1180, "de 6.º grado, de una escuela de California", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.4, 540, 1240, "y otros 54 de la misma escuela siguieron con sus pantallas", 34, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1320, "Uhls, Greenfield y otros, UCLA, 2014", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "LA PRUEBA", 150, C)
    slide_line(d, lt, 0.35, 540, 380, "antes y después: ¿qué siente esta persona?", 42, C, kind="SemiBold", dy=20)
    # tarjeta con caras que van pasando (48 fotos)
    rrect(d, 240, 470, 840, 1000, 40, fill=K2)
    moods = ["feliz", "triste", "enojado", "asustado"]
    k = int(max(0, lt - 0.6) / 0.45) % 4
    if lt > 0.6:
        face(d, 540, 700, 170, moods[k], C)
        names = {"feliz": "FELIZ", "triste": "TRISTE", "enojado": "ENOJADO", "asustado": "ASUSTADO"}
        text_c(d, 540, 940, names[moods[k]] + "?", "A", 60, Y, bg=K2)
    pop_line(d, lt, 1.0, 540, 1110, "48 FOTOS DE CARAS", 100, Y)
    slide_line(d, lt, 1.6, 540, 1220, "+ videos de actores para leer lo que sienten", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1300, "UCLA Health, 21/08/2014", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 270, "ERRORES EN LAS FOTOS", 115, C)
    slide_line(d, lt, 0.35, 540, 370, "promedio del grupo del campamento", 42, C, kind="SemiBold", dy=20)
    # contador que baja de 14,02 a 9,41
    p = ease_in_out(prog(lt, 0.7, 1.4))
    if lt > 0.5:
        v = lerp(14.02, 9.41, p)
        col = mix(R, GREEN, p)
        text_c(d, 540, 640, f"{v:.2f}".replace(".", ","), "A", 260, col)
        # barras antes / después
        rrect(d, 200, 830, 200 + 680 * 14.02 / 15, 890, 20, fill=(90, 90, 90))
        text_l(d, 200, 920, "ANTES: 14,02", "Bold", 36, G)
        if p > 0:
            rrect(d, 200, 970, 200 + 680 * v / 15, 1030, 20, fill=col)
            text_l(d, 200, 1060, "DESPUÉS DE 5 DÍAS", "Bold", 36, col)
    pill(d, t, 14.4, 540, 1180, 900, "LOS DE PANTALLA CAMBIARON MENOS", fill=Y, ink=K, size=38, h=110)
    slide_line(d, lt, 2.8, 540, 1300, "Computers in Human Behavior, 2014", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "¿POR QUÉ?", 150, Y)
    slide_line(d, lt, 0.4, 540, 400, "a las emociones se las aprende cara a cara", 44, C, kind="Bold", dy=20)
    # dos personas charlando con burbuja
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        person(d, 360, 700, 300 * e, C)
        person(d, 720, 700, 300 * e, Y)
    e2 = back(prog(lt, 1.1, 0.3))
    if e2 > 0.02:
        bubble(d, 540, 520, 150 * e2, C)
    slide_line(d, lt, 1.6, 540, 960, "en casa usaban ~4,5 h de pantalla por día de escuela", 37, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.0, 540, 1050, "\"necesitamos tiempo sin aparatos\"", 48, Y, kind="Bold", dy=20)
    slide_line(d, lt, 2.2, 540, 1110, "Yalda Uhls, autora", 34, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1200, "ojo: estudio chico, de una sola escuela", 36, R, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 330, "¿CUÁNTO AGUANTA", 125, C)
    pop_line(d, lt, 0.3, 540, 470, "EL TUYO SIN PANTALLA?", 100, Y)
    pill(d, t, 20.8, 540, 680, 520, "1 TARDE", fill=C, ink=K, size=56, h=120)
    pill(d, t, 21.0, 540, 830, 520, "1 DÍA", fill=C, ink=K, size=56, h=120)
    pill(d, t, 21.2, 540, 980, 520, "5 DÍAS", fill=Y, ink=K, size=56, h=120)
    slide_line(d, lt, 1.6, 540, 1140, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.0, 540, 1210, "y probá un finde con más charla y menos pantalla", 38, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "thump")
for i in range(4): ev(0.7 + i * 0.25, "pop", [-0.5, 0.5, -0.5, 0.5][i])
ev(1.8, "pop"); ev(2.1, "swipe"); ev(2.8, "tap")
ev(4.1, "tap"); ev(4.35, "tap"); ev(4.5, "rustle"); ev(4.8, "pop"); ev(5.1, "rustle"); ev(5.5, "pop", -0.3); ev(5.7, "pop", 0.3); ev(6.1, "tap"); ev(6.4, "tap"); ev(6.8, "tap")
ev(8.1, "tap"); ev(8.35, "tap")
for k in range(7): ev(8.6 + k * 0.45, "click")
ev(9.0, "thump"); ev(9.6, "tap"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.35, "tap")
for k in range(10): ev(12.7 + k * 0.14, "tick")
ev(14.15, "ding"); ev(14.4, "pop"); ev(14.8, "tap")
ev(16.1, "pop"); ev(16.4, "tap"); ev(16.7, "pop", -0.3); ev(16.8, "pop", 0.3); ev(17.1, "pop"); ev(17.6, "tap"); ev(18.0, "tap"); ev(18.2, "tap"); ev(18.6, "thump")
ev(20.1, "pop", -0.3); ev(20.3, "thump"); ev(20.8, "pop", -0.2); ev(21.0, "pop"); ev(21.2, "pop", 0.2); ev(21.6, "tap"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
