"""Short 2026-11-15 15:00 — Curiosidades y hábitos: primeras impresiones en una décima de segundo.

Fuente:
- Willis y Todorov, "First impressions: Making up your mind after a 100-ms exposure to a face",
  Psychological Science, julio 2006 (doi 10.1111/j.1467-9280.2006.01750.x). Princeton University.
  Comunicado de Princeton (22/08/2006): "Snap judgments decide a face's character, psychologist finds".
- ~200 personas en 5 experimentos; 66 caras desconocidas; exposiciones de 100 ms, 500 ms y 1 s.
- Juicios: atractivo, simpatía (likeability), confiabilidad, competencia y agresividad.
- Los juicios a los 100 ms se correlacionaron mucho con los juicios sin límite de tiempo; más tiempo no
  aumentó mucho esa correlación. Con más tiempo la gente se sintió MÁS SEGURA (confianza), no cambió su juicio de fondo.
- Todorov: "todavía no sabemos qué rasgos físicos de una cara llevan a esa impresión".
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def face(d, cx, cy, r, col=C, ink=K, var=0):
    """Cara genérica (sin rasgos de nadie real). var cambia cejas/boca."""
    circle(d, cx, cy, r, fill=col)
    # pelo
    d.chord([S(cx - r), S(cy - r), S(cx + r), S(cy + r * 0.2)], 180 + var * 8, 360 - var * 8, fill=(60, 60, 60) if var % 2 == 0 else (110, 80, 50))
    for sx in (-1, 1):
        ex, ey = cx + sx * r * 0.36, cy + r * 0.05
        circle(d, ex, ey, r * 0.09, fill=ink)
        by = ey - r * 0.22
        tilt = (0.08 if var == 1 else -0.06 if var == 2 else 0) * r * sx
        d.line([S(ex - r * 0.16), S(by + tilt), S(ex + r * 0.16), S(by - tilt)], fill=ink, width=int(S(max(3, r * 0.06))))
    my = cy + r * 0.48
    if var == 1:
        d.line([S(cx - r * 0.25), S(my), S(cx + r * 0.25), S(my)], fill=ink, width=int(S(max(3, r * 0.06))))
    else:
        d.arc([S(cx - r * 0.3), S(my - r * 0.3), S(cx + r * 0.3), S(my + r * 0.08)], 25, 155, fill=ink, width=int(S(max(3, r * 0.06))))

def flash(d, t, t0, a=0.85):
    """Destello de cámara: pantalla crema que se desvanece."""
    p = prog(t, t0, 0.25)
    if 0 < p < 1:
        col = mix(C, K, ease_out(p)) if a else C
        rrect(d, 300, 660, 780, 1140, 30, fill=col)

def viewfinder(d, cx, cy, w, h, col=Y, L=70, wd=10):
    for sx in (-1, 1):
        for sy in (-1, 1):
            x, y = cx + sx * w / 2, cy + sy * h / 2
            d.line([S(x), S(y), S(x - sx * L), S(y)], fill=col, width=S(wd))
            d.line([S(x), S(y), S(x), S(y - sy * L)], fill=col, width=S(wd))

def b1(d, t):
    pop_line(d, t, 0.0, 540, 330, "¿CUÁNTO TARDAN", 140, C)
    pop_line(d, t, 0.2, 540, 480, "EN JUZGARTE?", 150, Y)
    flash(d, t, 2.1)
    e = back(prog(t, 0.5, 0.35))
    if e > 0.02:
        viewfinder(d, 540, 900, 460 * e, 460 * e)
        face(d, 540, 900, 170 * e)
    # cronómetro
    p = prog(t, 1.2, 0.9)
    if p > 0:
        v = 0.1 * ease_out(p)
        txt = f"{v:.2f}".replace(".", ",") + " s"
        text_c(d, 540, 1280, txt, "A", 200, R if p >= 1 else C)
    pill(d, t, 2.5, 540, 1480, 680, "UNA DÉCIMA DE SEGUNDO", fill=R, ink=C, size=44, h=100)

def b2(d, t):
    lt = t - 4
    n = int(round(200 * ease_out(prog(lt, 0.1, 0.9))))
    pop_line(d, lt, 0.05, 540, 300, "~" + str(n), 210, Y)
    slide_line(d, lt, 0.35, 540, 450, "PERSONAS", 110, C)
    slide_line(d, lt, 0.6, 540, 560, "vieron 66 caras de desconocidos", 46, C, kind="SemiBold", dy=25)
    # tres tarjetas de tiempo
    tiempos = [("0,1 s", R), ("0,5 s", Y), ("1 s", GREEN)]
    for k, (lab, col) in enumerate(tiempos):
        pk = back(prog(lt, 1.0 + k * 0.3, 0.3))
        if pk > 0.02:
            x = 230 + k * 310
            rrect(d, x - 130 * pk, 820 - 170 * pk, x + 130 * pk, 820 + 190 * pk, 30, fill=K2)
            if pk > 0.8:
                face(d, x, 790, 85, var=k)
                text_c(d, x, 950, lab, "A", 70, col, bg=K2)
    slide_line(d, lt, 2.1, 540, 1130, "y tenían que juzgarlas", 50, C, kind="Bold", dy=25)
    slide_line(d, lt, 2.4, 540, 1220, "Willis y Todorov, Princeton, Psychological Science 2006", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.05, 540, 280, "5 COSAS AL TOQUE", 125, C)
    rasgos = [("¿ES ATRACTIVO?", Y), ("¿ME CAE BIEN?", C), ("¿ES CONFIABLE?", Y), ("¿ES CAPAZ?", C), ("¿ES AGRESIVO?", R)]
    for k, (lab, col) in enumerate(rasgos):
        p = prog(lt, 0.45 + k * 0.32, 0.28)
        if p <= 0: continue
        e = ease_out(p)
        y = 470 + k * 165
        x0 = 110 + (1 - e) * 600
        rrect(d, x0, y, x0 + 860, y + 130, 36, fill=K2)
        text_l(d, x0 + 50, y + 65, lab, "Black", 50, col)
        q = prog(lt, 0.6 + k * 0.32, 0.15)
        if q > 0:
            cx, cy = x0 + 770, y + 65
            circle(d, cx, cy, 42 * back(q), fill=col)
            if q >= 1:
                d.line([S(cx - 18), S(cy), S(cx - 4), S(cy + 16), S(cx + 20), S(cy - 16)], fill=K, width=S(9), joint="curve")
    slide_line(d, lt, 2.4, 540, 1340, "atractivo, simpatía, confianza, capacidad, agresividad", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.05, 540, 280, "¿Y CON MÁS TIEMPO?", 108, C)
    # dos barras: opinión (igual) vs seguridad (sube)
    p = ease_in_out(prog(lt, 0.6, 1.2))
    labels = [("OPINIÓN", 0.62, 0.62, Y), ("SEGURIDAD", 0.35, 0.92, GREEN)]
    for k, (lab, a, b, col) in enumerate(labels):
        pk = ease_out(prog(lt, 0.4 + k * 0.15, 0.3))
        if pk <= 0: continue
        y = 470 + k * 200
        text_l(d, 110, y, lab, "Black", 46, C)
        rrect(d, 110, y + 40, 110 + 860 * pk, y + 120, 40, fill=K2)
        v = lerp(a, b, p)
        if pk > 0.9:
            rrect(d, 110, y + 40, 110 + 860 * v, y + 120, 40, fill=col)
    pop_line(d, lt, 1.9, 540, 960, "NO CAMBIARON", 140, R)
    pop_line(d, lt, 2.1, 540, 1100, "DE IDEA", 140, R)
    slide_line(d, lt, 2.5, 540, 1240, "solo se sintieron más seguros", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1305, "de lo que ya pensaban", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1390, "Comunicado de Princeton, 22/08/2006", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.05, 540, 280, "OJO: UNA CARA", 130, C)
    pop_line(d, lt, 0.3, 540, 420, "NO ES UNA PERSONA", 115, Y)
    # cara que se "abre" como libro
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        face(d, 330, 750, 140 * e, var=1)
        q = ease_out(prog(lt, 1.0, 0.4))
        if q > 0:
            d.line([S(500), S(750), S(500 + 110 * q), S(750)], fill=Y, width=S(14))
            d.polygon([(S(500 + 110 * q), S(725)), (S(500 + 110 * q + 40), S(750)), (S(500 + 110 * q), S(775))], fill=Y)
        r = back(prog(lt, 1.3, 0.3))
        if r > 0.02:
            bubble(d, 790, 760, 250 * r, C)
    slide_line(d, lt, 1.6, 540, 1010, "ni los científicos saben qué rasgo", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.75, 540, 1075, "de la cara genera esa impresión", 44, C, kind="SemiBold", dy=25)
    stamp(d, lt, 2.2, 540, 1270, 400, 95, "DALE UNA CHARLA", fill=Y, ink=K, size=100)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.05, 540, 330, "¿TE PASÓ DE JUZGAR", 115, C)
    pop_line(d, lt, 0.3, 540, 470, "A ALGUIEN", 130, C)
    pop_line(d, lt, 0.55, 540, 610, "Y EQUIVOCARTE?", 130, Y)
    for k, (lab, col, x) in enumerate([("SÍ", GREEN, 360), ("NO", R, 720)]):
        pk = back(prog(lt, 1.1 + k * 0.2, 0.3))
        if pk > 0.02:
            circle(d, x, 870, 130 * pk, fill=col)
            if pk > 0.7:
                text_c(d, x, 865, lab, "A", 110, K, bg=col)
    pill(d, lt, 1.8, 540, 1100, 680, "CONTALO EN COMENTARIOS", fill=K2, ink=C, size=42, h=100)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop"); ev(0.25, "pop"); ev(0.55, "pop")
for k in range(9): ev(1.2 + k * 0.1, "tick", 0.0)
ev(2.1, "click"); ev(2.12, "shimmer"); ev(2.5, "tap")
ev(4.05, "pop")
for k in range(9): ev(4.1 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(4.35, "swipe"); ev(4.6, "swipe")
for k in range(3): ev(5.0 + k * 0.3, "pop", -0.4 + k * 0.4)
ev(6.1, "swipe"); ev(6.4, "tap")
ev(8.05, "pop")
for k in range(5): ev(8.45 + k * 0.32, "swipe", 0.3); ev(8.6 + k * 0.32 + 0.15, "tap", 0.3)
ev(10.4, "tap")
ev(12.05, "swipe"); ev(12.4, "click"); ev(12.55, "click"); ev(12.6, "rustle")
ev(13.9, "thump"); ev(14.1, "pop"); ev(14.5, "swipe"); ev(14.7, "tap")
ev(16.05, "pop"); ev(16.3, "pop"); ev(16.6, "pop"); ev(17.0, "whoosh"); ev(17.3, "pop")
ev(17.6, "swipe"); ev(17.75, "swipe"); ev(18.0, "whoosh"); ev(18.2, "stamp")
ev(20.05, "pop"); ev(20.3, "pop"); ev(20.55, "thump"); ev(21.1, "pop", -0.3); ev(21.3, "pop", 0.3); ev(21.8, "click")

if __name__ == "__main__":
    main(BEATS_EP)
