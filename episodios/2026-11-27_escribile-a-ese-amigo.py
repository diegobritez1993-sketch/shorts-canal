"""Short 2026-11-27 20:00 — Mente y emociones.
¿Hace cuánto no le escribís a ese amigo? Subestimamos cuánto valoran que los contactemos.
Fuente: Liu, Rim, Min y Min, "The Surprise of Reaching Out: Appreciated More Than We Think",
Journal of Personality and Social Psychology, 11/07/2022 (comunicado APA 11/07/2022).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

BLUE = (90, 150, 255)
SRC = "Liu et al., J. Pers. Soc. Psychol. 2022 (APA)"

def gift(d, cx, cy, s, lid=0.0, col=Y, rib=R):
    """Cajita de regalo; lid 0..1 levanta la tapa."""
    rrect(d, cx - s * 0.45, cy - s * 0.25, cx + s * 0.45, cy + s * 0.45, s * 0.05, fill=col)
    d.rectangle([S(cx - s * 0.07), S(cy - s * 0.25), S(cx + s * 0.07), S(cy + s * 0.45)], fill=rib)
    ly = cy - s * 0.25 - lid * s * 0.3
    rot = lid * 0.25
    rrect(d, cx - s * 0.52 + lid * s * 0.2, ly - s * 0.16, cx + s * 0.52 + lid * s * 0.2, ly, s * 0.04, fill=mix(col, C, 0.25))
    d.rectangle([S(cx - s * 0.07 + lid * s * 0.2), S(ly - s * 0.16), S(cx + s * 0.07 + lid * s * 0.2), S(ly)], fill=rib)
    for sd in (-1, 1):
        circle(d, cx + sd * s * 0.12 + lid * s * 0.2, ly - s * 0.22, s * 0.1, outline=rib, width=max(4, int(s * 0.05)))

def gauge_bar(d, x, y0, y1, w, lvl, col, label, lt, t0):
    rrect(d, x - w / 2, y0, x + w / 2, y1, 30, fill=K2)
    h = (y1 - y0 - 24) * lvl
    if h > 4:
        rrect(d, x - w / 2 + 12, y1 - 12 - h, x + w / 2 - 12, y1 - 12, 22, fill=col)
    slide_line(d, lt, t0, x, y1 + 70, label, 56, C, dy=20)

# ---------- escenas ----------
def b1(d, t):
    pop_line(d, t, 0.05, 540, 230, "¿HACE CUÁNTO", 140, C)
    pop_line(d, t, 0.3, 540, 380, "NO LE ESCRIBÍS", 140, Y)
    pop_line(d, t, 0.55, 540, 530, "A ESE AMIGO?", 140, Y)
    e = back(prog(t, 0.4, 0.45))
    if e > 0.02:
        phone(d, 540, 960, 300 * e, 520 * e, body=K2)
        if e > 0.7:
            # chat vacío: el último mensaje es viejísimo
            rrect(d, 430, 790, 640, 850, 26, fill=(60, 60, 60))
            text_c(d, 535, 820, "hace 2 años", "SemiBold", 26, C)
            # cursor parpadeando
            if int(t * 3) % 2 == 0:
                d.rectangle([S(420), S(1100), S(428), S(1150)], fill=Y)
            rrect(d, 410, 1090, 670, 1160, 30, outline=(90, 90, 90), width=4)
    slide_line(d, t, 1.6, 540, 1320, "lo pensás, lo escribís...", 50, C, kind="SemiBold", dy=25)
    pop_line(d, t, 2.3, 540, 1440, "Y LO BORRÁS", 130, R)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "PENSÁS QUE", 120, C)
    slide_line(d, lt, 0.3, 540, 440, "VA A MOLESTAR", 140, Y)
    # burbujas de dudas que aparecen
    thoughts = [("¿y si le parece raro?", 320, 650, 0.6), ("ni se acuerda de mí", 760, 800, 0.9), ("¿qué le digo?", 320, 950, 1.2), ("mejor no...", 750, 1100, 1.5)]
    for txt, x, y, t0 in thoughts:
        p = back(prog(lt, t0, 0.35))
        if p > 0.02:
            w = 540 * p
            rrect(d, x - w / 2, y - 55 * p, x + w / 2, y + 55 * p, 50 * p, fill=K2, outline=(80, 80, 80), width=4)
            text_c(d, x, y, txt, "SemiBold", 40, C, scale=p, bg=K2)
    pop_line(d, lt, 2.2, 540, 1300, "SPOILER:", 110, C)
    pop_line(d, lt, 2.45, 540, 1430, "TE EQUIVOCÁS", 140, R)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "LO PROBARON CON", 100, C)
    n = int(5900 * ease_out(prog(lt, 0.3, 1.2)))
    sx, sy = shake(lt, 1.5, 0.3, 14)
    pop_line(d, lt, 0.3, 540 + sx, 430 + sy, "+" + fmt_num(n), 200, Y, dur=0.25)
    slide_line(d, lt, 0.6, 540, 620, "PERSONAS", 110, C)
    # notita volando de una persona a otra
    person(d, 230, 900, 260, C)
    person(d, 850, 900, 260, (110, 110, 110))
    p = ease_in_out(prog(lt, 1.2, 1.1))
    if 0 < p:
        x = lerp(330, 750, p); y = 860 - math.sin(p * math.pi) * 180
        rrect(d, x - 55, y - 40, x + 55, y + 40, 10, fill=Y)
        d.line([S(x - 55), S(y - 40), S(x), S(y + 5), S(x + 55), S(y - 40)], fill=K, width=S(5))
    if lt > 2.3:
        heart(d, 850, 700 - (lt - 2.3) * 60, 90, R)
    slide_line(d, lt, 2.4, 540, 1150, "le mandaron una notita o un regalito", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.55, 540, 1215, "a alguien que no veían hace tiempo", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1310, SRC, 34, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 260, "LO QUE CREÍAN", 110, C)
    slide_line(d, lt, 0.3, 540, 390, "VS. LO QUE PASÓ", 120, Y)
    e = ease_out(prog(lt, 0.4, 0.3))
    if e > 0:
        gauge_bar(d, 310, 520, 1180, 250, 0.45 * ease_out(prog(lt, 0.7, 0.8)), G, "EL QUE ESCRIBE", lt, 0.5)
        gauge_bar(d, 770, 520, 1180, 250, 0.9 * ease_out(prog(lt, 1.4, 1.0)), GREEN, "EL QUE RECIBE", lt, 0.7)
    slide_line(d, lt, 1.0, 310, 1310, "cuánto creía que gustaría", 34, C, kind="SemiBold", dy=15)
    slide_line(d, lt, 1.6, 770, 1310, "cuánto le gustó", 34, C, kind="SemiBold", dy=15)
    pill(d, lt, 2.5, 540, 1460, 900, "LO VALORAN MÁS DE LO QUE CREÉS", fill=Y, ink=K, size=42, h=104)
    slide_line(d, lt, 2.8, 540, 1570, "esquema ilustrativo, no son cifras del estudio", 32, G, kind="SemiBold", dy=15)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "Y CUANTO MÁS", 120, C)
    pop_line(d, lt, 0.3, 540, 430, "SORPRESA", 190, Y)
    slide_line(d, lt, 0.5, 540, 560, "más tiempo sin hablar", 48, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 0.5, 0.4))
    lid = ease_out(prog(lt, 1.2, 0.5))
    if e > 0.02:
        # estallido de corazones al abrir
        if lid > 0.3:
            for k in range(7):
                a = -math.pi / 2 + (k - 3) * 0.38
                rr = 110 + 150 * ease_out(prog(lt, 1.3, 0.8))
                heart(d, 540 + math.cos(a) * rr, 980 + math.sin(a) * rr, 70, R if k % 2 else Y)
        gift(d, 540, 1010, 300 * e, lid)
    pop_line(d, lt, 2.1, 540, 1300, "MÁS LO VALORAN", 140, C)
    slide_line(d, lt, 2.5, 540, 1430, "sobre todo si era alguien no tan cercano", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.7, 540, 1500, SRC, 34, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 290, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 430, "MANDÁ ESE MENSAJE", 120, Y)
    p = back(prog(lt, 0.7, 0.4))
    if p > 0.02:
        w = 760 * p
        rrect(d, 540 - w / 2, 560, 540 + w / 2, 720, 60, fill=BLUE)
        d.polygon([(S(540 + w / 2 - 80), S(700)), (S(540 + w / 2 - 10), S(760)), (S(540 + w / 2 - 20), S(690))], fill=BLUE)
        text_c(d, 540, 640, "¡hola! me acordé de vos", "Bold", 52, C, scale=p, bg=BLUE)
    if lt > 1.3:
        text_c(d, 840, 790, "enviado", "SemiBold", 34, mix(K, BLUE, clamp((lt - 1.3) * 3)))
    slide_line(d, lt, 1.4, 540, 900, "no hace falta una excusa", 48, C, kind="SemiBold", dy=20)
    pop_line(d, lt, 1.8, 540, 1100, "¿A QUIÉN LE", 120, C)
    pop_line(d, lt, 2.0, 540, 1240, "ESCRIBÍS HOY?", 140, Y)
    slide_line(d, lt, 2.4, 540, 1370, "contalo en los comentarios", 44, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.05, "pop", -0.3); ev(0.3, "pop", 0.3); ev(0.55, "thump"); ev(0.5, "swipe")
for k in range(5): ev(1.0 + k * 0.12, "click", 0.2 if k % 2 else -0.2)
ev(1.6, "tap")
for k in range(6): ev(1.85 + k * 0.07, "tick", -0.2)
ev(2.3, "stamp")
ev(4.1, "tap", -0.3); ev(4.3, "pop", 0.3)
ev(4.6, "pop", -0.4); ev(4.9, "pop", 0.4); ev(5.2, "pop", -0.4); ev(5.5, "pop", 0.4)
ev(6.2, "tap"); ev(6.45, "thump")
ev(8.1, "tap")
for k in range(10): ev(8.3 + k * 0.12, "tick", 0.3 if k % 2 else -0.3)
ev(9.5, "thump"); ev(8.6, "tap"); ev(9.2, "swipe", 0.4); ev(10.3, "ding", 0.5); ev(10.4, "tap"); ev(10.8, "tap")
ev(12.1, "tap"); ev(12.3, "pop")
ev(12.7, "rustle", -0.4); ev(13.4, "rustle", 0.4); ev(14.2, "ding", 0.4); ev(14.5, "pop")
ev(16.1, "tap"); ev(16.3, "thump"); ev(16.5, "tap"); ev(16.6, "pop"); ev(17.2, "shimmer")
for k in range(4): ev(17.35 + k * 0.1, "pop", -0.4 + k * 0.27)
ev(18.1, "pop"); ev(18.5, "tap"); ev(18.7, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.7, "swipe", 0.5); ev(21.3, "ding", 0.4); ev(21.4, "tap"); ev(21.8, "pop", -0.2); ev(22.0, "thump"); ev(22.4, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
