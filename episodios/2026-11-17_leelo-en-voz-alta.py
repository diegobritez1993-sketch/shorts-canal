"""Short 2026-11-17 15:00 — Curiosidades y hábitos: leer en voz alta para acordarte (efecto de producción).

Fuente:
- Forrin y MacLeod, "This time it's personal: the memory benefit of hearing oneself", revista Memory (2017/2018).
  Comunicado Universidad de Waterloo (01/12/2017): "Study finds reading information aloud to yourself improves memory".
- 95 participantes; 4 formas de aprender: leer en silencio, escuchar a otro leer, escuchar una grabación de uno
  mismo leyendo, leer en voz alta en el momento. Leer en voz alta a uno mismo dio el mejor recuerdo.
- MacLeod: decirlo y escucharte hace la palabra "más distinta" en la memoria de largo plazo; "el aprendizaje y la
  memoria se benefician de la participación activa".
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

# ---------- íconos propios ----------
def book(d, cx, cy, s, col=C, page=K2):
    """Libro abierto."""
    for side in (-1, 1):
        x0, x1 = (cx - s * 0.5, cx - s * 0.02) if side < 0 else (cx + s * 0.02, cx + s * 0.5)
        d.polygon([(S(x0), S(cy - s * 0.28)), (S(x1), S(cy - s * 0.32 if side < 0 else cy - s * 0.28)),
                   (S(x1), S(cy + s * 0.3)), (S(x0), S(cy + s * 0.3))], fill=col)
        for k in range(4):
            yy = cy - s * 0.16 + k * s * 0.11
            d.line([S(x0 + s * 0.07), S(yy), S(x1 - s * 0.07), S(yy)], fill=page, width=SW(max(3, s * 0.025)))

def mouth(d, cx, cy, s, t, col=Y, talk=1.0):
    """Boca hablando + ondas de sonido."""
    o = (0.12 + 0.12 * abs(math.sin(t * 14))) * talk + 0.05
    d.ellipse([S(cx - s * 0.32), S(cy - s * o), S(cx + s * 0.32), S(cy + s * o)], fill=col)
    d.ellipse([S(cx - s * 0.2), S(cy - s * o * 0.5), S(cx + s * 0.2), S(cy + s * o * 0.5)], fill=K)
    for k in range(3):
        r = s * (0.45 + k * 0.15)
        a = clamp(talk * (0.5 + 0.5 * math.sin(t * 8 - k)))
        d.arc([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], -35, 35, fill=mix(K, col, a), width=SW(9))

def ear(d, cx, cy, s, col=C):
    d.arc([S(cx - s * 0.3), S(cy - s * 0.42), S(cx + s * 0.3), S(cy + s * 0.2)], 160, 400, fill=col, width=SW(max(6, s * 0.09)))
    d.line([S(cx + s * 0.28), S(cy - s * 0.0), S(cx + s * 0.05), S(cy + s * 0.42)], fill=col, width=SW(max(6, s * 0.09)))
    d.arc([S(cx - s * 0.12), S(cy - s * 0.2), S(cx + s * 0.12), S(cy + s * 0.05)], 180, 360, fill=col, width=SW(max(5, s * 0.06)))

def eye(d, cx, cy, s, col=C):
    d.chord([S(cx - s * 0.45), S(cy - s * 0.35), S(cx + s * 0.45), S(cy + s * 0.35)], 200, 340, fill=col)
    d.chord([S(cx - s * 0.45), S(cy - s * 0.35), S(cx + s * 0.45), S(cy + s * 0.35)], 20, 160, fill=col)
    d.rectangle([S(cx - s * 0.42), S(cy - s * 0.12), S(cx + s * 0.42), S(cy + s * 0.12)], fill=col)
    circle(d, cx, cy, s * 0.15, fill=K)

def play_btn(d, cx, cy, s, col=C):
    circle(d, cx, cy, s * 0.42, outline=col, width=int(max(4, s * 0.07)))
    d.polygon([(S(cx - s * 0.12), S(cy - s * 0.2)), (S(cx + s * 0.22), S(cy)), (S(cx - s * 0.12), S(cy + s * 0.2))], fill=col)

def trophy(d, cx, cy, s, col=Y):
    d.chord([S(cx - s * 0.35), S(cy - s * 0.7), S(cx + s * 0.35), S(cy + s * 0.1)], 0, 180, fill=col)
    d.rectangle([S(cx - s * 0.35), S(cy - s * 0.42), S(cx + s * 0.35), S(cy - s * 0.3)], fill=col)
    for sx in (-1, 1):
        d.arc([S(cx + sx * s * 0.38 - s * 0.16), S(cy - s * 0.38), S(cx + sx * s * 0.38 + s * 0.16), S(cy - s * 0.06)],
              90 if sx > 0 else -90 + 180, 270 if sx < 0 else 450 - 180, fill=col, width=SW(max(6, s * 0.06)))
    d.rectangle([S(cx - s * 0.06), S(cy + s * 0.05), S(cx + s * 0.06), S(cy + s * 0.3)], fill=col)
    rrect(d, cx - s * 0.25, cy + s * 0.28, cx + s * 0.25, cy + s * 0.4, 8, fill=col)

# ---------- escenas ----------
def b1(d, t):
    pop_line(d, t, 0.0, 540, 430, "¿ESTUDIÁS", 190, C, dur=0.25)
    pop_line(d, t, 0.3, 540, 640, "EN SILENCIO?", 170, Y, dur=0.25)
    e = back(prog(t, 0.6, 0.4))
    if e > 0.02:
        book(d, 540, 1080, 520 * e)
    # "shhh" se tacha
    if t > 1.6:
        ban(d, 540, 1080, 330, ease_out(prog(t, 1.8, 0.3)), width=26)
    slide_line(d, t, 2.4, 540, 1530, "ojo: te estás perdiendo un truco", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 330, "UN EXPERIMENTO", 130, C)
    slide_line(d, lt, 0.3, 540, 460, "Universidad de Waterloo, Canadá", 48, C, kind="SemiBold", dy=25)
    n = int(95 * ease_out(prog(lt, 0.6, 1.2)))
    if lt > 0.6:
        sx, sy = shake(lt, 1.8, 0.35, 14)
        text_c(d, 540 + sx, 780 + sy, str(n), "A", 400, Y)
        pop_line(d, lt, 1.8, 540, 1060, "PERSONAS", 130, C)
    # puntitos de personas
    for k in range(19):
        p = prog(lt, 0.6 + k * 0.06, 0.2)
        if p > 0:
            person(d, 120 + k * 44.5, 1260, 70 * back(p), mix(K, C, 0.8))
    slide_line(d, lt, 2.3, 540, 1430, "aprendieron palabras de 4 formas distintas", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.5, 540, 1500, "Forrin y MacLeod, revista Memory, 2017", 36, G, kind="SemiBold", dy=20)

ROWS = [("LEER EN SILENCIO", "eye"), ("ESCUCHAR A OTRO", "ear"), ("OÍR TU GRABACIÓN", "play"), ("LEER EN VOZ ALTA", "mouth")]

def row_icon(d, kind, cx, cy, s, t, col):
    if kind == "eye": eye(d, cx, cy, s, col)
    elif kind == "ear": ear(d, cx, cy, s, col)
    elif kind == "play": play_btn(d, cx, cy, s, col)
    else: mouth(d, cx - s * 0.1, cy, s, t, col)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "4 FORMAS", 150, C)
    slide_line(d, lt, 0.3, 540, 420, "de repasar lo mismo:", 50, C, kind="SemiBold", dy=25)
    for k, (lab, ic) in enumerate(ROWS):
        p = prog(lt, 0.6 + k * 0.45, 0.3)
        if p <= 0: continue
        e = ease_out(p)
        y = 560 + k * 230
        x0 = 110 - 700 * (1 - e)
        rrect(d, x0, y, x0 + 860, y + 190, 40, fill=K2)
        row_icon(d, ic, x0 + 120, y + 95, 120, lt, Y if ic == "mouth" else C)
        text_l(d, x0 + 230, y + 95, lab, "Black", 50, C)
    slide_line(d, lt, 2.6, 540, 1560, "¿cuál ayudó más a recordar?", 48, Y, kind="Bold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "LA QUE GANÓ:", 140, C)
    # las otras 3 quedan grises y chiquitas
    for k, (lab, ic) in enumerate(ROWS[:3]):
        p = prog(lt, 0.3 + k * 0.1, 0.3)
        if p <= 0: continue
        y = 470 + k * 120
        rrect(d, 200, y, 880, y + 95, 30, fill=(22, 22, 22))
        row_icon(d, ic, 270, y + 47, 62, lt, (90, 90, 90))
        text_l(d, 330, y + 47, lab, "Bold", 38, (100, 100, 100))
    e = back(prog(lt, 0.9, 0.45))
    if e > 0.02:
        trophy(d, 540, 1060, 300 * e)
    stamp(d, lt, 1.6, 540, 1380, 420, 95, "LEER EN VOZ ALTA", fill=Y, ink=K, size=110)
    slide_line(d, lt, 2.3, 540, 1560, "fue lo que mejor recordaron", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.5, 540, 1625, "Universidad de Waterloo, 2017", 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿POR QUÉ?", 160, C)
    # boca + oreja se juntan
    e1 = back(prog(lt, 0.4, 0.35)); e2 = back(prog(lt, 0.8, 0.35))
    if e1 > 0.02:
        mouth(d, 280, 700, 220 * e1, lt)
        pop_line(d, lt, 0.4, 280, 880, "LO DECÍS", 70, C)
    if e2 > 0.02:
        ear(d, 800, 700, 220 * e2, C)
        pop_line(d, lt, 0.8, 800, 880, "TE ESCUCHÁS", 70, C)
    pop_line(d, lt, 1.2, 540, 720, "+", 160, Y)
    sx, sy = shake(lt, 2.2, 0.35, 14)
    pop_line(d, lt, 2.0, 540 + sx, 1100 + sy, "QUEDA MÁS", 150, C, dur=0.25)
    pop_line(d, lt, 2.2, 540 + sx, 1270 + sy, "MARCADO", 170, Y, dur=0.25)
    slide_line(d, lt, 2.7, 540, 1420, "se le dice \"efecto de producción\"", 44, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 120, C)
    slide_line(d, lt, 0.3, 540, 460, "REPASÁ", 150, Y)
    slide_line(d, lt, 0.45, 540, 620, "EN VOZ ALTA", 150, Y)
    slide_line(d, lt, 0.9, 540, 760, "aunque sea bajito, lo importante", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 1.0, 540, 820, "es decirlo y escucharte", 44, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 1.2, 0.35))
    if e > 0.02:
        mouth(d, 540, 1020, 200 * e, lt)
    pop_line(d, lt, 1.9, 540, 1250, "¿ESTUDIÁS EN VOZ ALTA?", 88, C)
    pill(d, t, 22.3, 400, 1410, 220, "SÍ", fill=Y, ink=K, size=56, h=110)
    pill(d, t, 22.45, 680, 1410, 220, "NO", fill=K2, ink=C, size=56, h=110)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.3, "thump"); ev(0.6, "rustle"); ev(1.8, "click"); ev(1.85, "thump"); ev(2.4, "tap")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(12): ev(4.6 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(5.75, "pop"); ev(5.8, "stamp"); ev(6.3, "tap"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.3, "tap")
for k in range(4): ev(8.6 + k * 0.45, "swipe", -0.4 + k * 0.25); ev(8.65 + k * 0.45, "pop", -0.4 + k * 0.25)
ev(10.6, "tap")
ev(12.1, "tap"); ev(12.3, "click"); ev(12.4, "click"); ev(12.5, "click"); ev(12.9, "pop"); ev(13.4, "stamp"); ev(13.5, "shimmer")
ev(14.3, "tap"); ev(14.5, "tap")
ev(16.1, "pop"); ev(16.4, "pop", -0.4); ev(16.6, "pop"); ev(16.8, "pop", 0.4); ev(17.4, "whoosh"); ev(18.0, "pop"); ev(18.2, "thump"); ev(18.7, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.9, "tap"); ev(21.2, "pop"); ev(21.9, "pop"); ev(22.3, "tap", -0.3); ev(22.45, "tap", 0.3)

if __name__ == "__main__":
    main(BEATS_EP)
