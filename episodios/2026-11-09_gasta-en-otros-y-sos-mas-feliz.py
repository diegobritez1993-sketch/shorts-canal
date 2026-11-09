"""Short 2026-11-09 15:00 - Curiosidades y hábitos (dinero): gastar en otros da más felicidad que gastar en uno.
Fuente: Dunn, Aknin y Norton, Science 2008 (vía Harvard Gazette, abr. 2008; ScienceDaily 20/03/2008)."""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

GB = (70, 170, 100)

def bill(d, cx, cy, w, col=GB, ink=K, label="$"):
    h = w * 0.5
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, w * 0.05, fill=col)
    rrect(d, cx - w * 0.44, cy - h * 0.38, cx + w * 0.44, cy + h * 0.38, w * 0.03, outline=ink, width=max(2, int(w * 0.012)))
    circle(d, cx, cy, h * 0.28, fill=ink)
    text_c(d, cx, cy - 2, label, "A", int(h * 0.36), col, bg=ink)

def flap(d, cx, cy, w, h, op):
    x0, y0, x1 = cx - w / 2, cy - h / 2, cx + w / 2
    if op > 0.05:
        fy = lerp(cy, y0 - h * 0.5, op)
        d.polygon([(S(x0), S(y0)), (S(x1), S(y0)), (S(cx), S(fy))], fill=(200, 196, 180))

def envelope(d, cx, cy, w, h, op):
    """op 0..1 = cerrado→abierto"""
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    rrect(d, x0, y0, x1, y1, 16, fill=C)
    d.polygon([(S(x0), S(y1)), (S(x1), S(y1)), (S(cx), S(cy - h * 0.05))], fill=(225, 220, 205))
    if op <= 0.05:
        d.polygon([(S(x0), S(y0)), (S(x1), S(y0)), (S(cx), S(cy + h * 0.1))], fill=(200, 196, 180))

def face(d, cx, cy, r, q, col=Y):
    """q: 0 serio → 1 sonrisa grande"""
    circle(d, cx, cy, r, fill=col)
    for s in (-1, 1):
        circle(d, cx + s * r * 0.36, cy - r * 0.22, r * 0.11, fill=K)
    w = r * 0.5
    if q < 0.15:
        d.line([S(cx - w), S(cy + r * 0.4), S(cx + w), S(cy + r * 0.4)], fill=K, width=int(S(max(6, r * 0.09))))
    else:
        dep = r * 0.15 + r * 0.45 * q
        d.arc([S(cx - w), S(cy + r * 0.3 - dep), S(cx + w), S(cy + r * 0.3 + dep)], 10, 170, fill=K, width=int(S(max(6, r * 0.09))))

def b1(d, t):
    rnd = random.Random(4)
    for k in range(9):
        x = rnd.uniform(90, 990); sp = rnd.uniform(0.09, 0.16); ph = rnd.uniform(0, 1)
        y = 760 + ((t * sp + ph) % 1) * 1250
        w = rnd.uniform(140, 210)
        bill(d, x, y, w, mix(K, GB, 0.75))
    pop_line(d, t, 0.0, 540, 300, "¿LA PLATA", 180, C)
    pop_line(d, t, 0.25, 540, 480, "COMPRA", 180, C)
    pop_line(d, t, 0.5, 540, 660, "FELICIDAD?", 180, Y)
    if t > 1.7:
        rrect(d, 90, 1420, 990, 1590, 50, fill=K)
    pop_line(d, t, 1.8, 540, 1505, "DEPENDE EN QUIÉN LA GASTES", 76, C)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.05, 540, 290, "UN EXPERIMENTO", 140, C)
    slide_line(d, lt, 0.3, 540, 420, "les dieron un sobre con plata", 46, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        op = ease_out(prog(lt, 1.1, 0.5))
        up = ease_out(prog(lt, 1.5, 0.6))
        flap(d, 540, 1080, 640 * e, 400 * e, op)
        bill(d, 390, 980 - up * 260, 340, GB, label="$5")
        bill(d, 690, 980 - up * 200, 340, GB, label="$20")
        envelope(d, 540, 1080, 640 * e, 400 * e, op)
    pop_line(d, lt, 2.2, 540, 1420, "5 O 20 DÓLARES", 130, Y)
    slide_line(d, lt, 2.6, 540, 1540, "y tenían que gastarlos ese mismo día", 44, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.05, 540, 290, "LA MITAD", 130, C)
    slide_line(d, lt, 0.25, 540, 410, "PODÍA GASTAR EN SÍ MISMA", 90, C)
    pop_line(d, lt, 0.9, 540, 510, "LA OTRA, EN ALGUIEN MÁS", 90, Y)
    p = back(prog(lt, 1.1, 0.4))
    if p > 0.02:
        rrect(d, 80, 690, 520, 1250, 44, fill=K2)
        person(d, 300, 900, 300 * p, C)
        text_c(d, 300, 1160, "EN VOS", "A", 86, C, bg=K2)
    q = back(prog(lt, 1.6, 0.4))
    if q > 0.02:
        rrect(d, 560, 690, 1000, 1250, 44, fill=K2)
        person(d, 700, 900, 220 * q, C)
        person(d, 860, 900, 220 * q, Y)
        heart(d, 780, 790, 90 * q, R)
        text_c(d, 780, 1160, "EN OTRO", "A", 86, Y, bg=K2)
    pop_line(d, lt, 2.5, 540, 1440, "¿QUIÉN TERMINÓ", 110, C)
    pop_line(d, lt, 2.8, 540, 1570, "MÁS CONTENTO?", 110, Y)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.05, 540, 290, "A LA NOCHE", 130, C)
    pl = ease_in_out(prog(lt, 0.5, 1.4))
    for side, cx, lab, q, col in [(-1, 300, "EN SÍ MISMOS", 0.05, (150, 150, 150)), (1, 780, "EN OTROS", pl, Y)]:
        e = back(prog(lt, 0.3 if side < 0 else 0.5, 0.35))
        if e > 0.02:
            face(d, cx, 700, 170 * e, q, col)
            text_c(d, cx, 930, lab, "A", 62, col)
    stamp(d, lt, 2.1, 540, 1200, 410, 120, "MÁS FELICES", fill=Y, size=150)
    slide_line(d, lt, 2.5, 540, 1380, "los que gastaron en otros", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1470, "Dunn, Aknin y Norton, Science, 2008", 38, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.05, 540, 290, "Y LO MÁS RARO", 130, C)
    pop_line(d, lt, 0.3, 540, 440, "EL MONTO NO IMPORTÓ", 110, Y)
    # balanza
    e = ease_out(prog(lt, 0.7, 0.4))
    if e > 0:
        tilt = math.sin(max(0, lt - 1.0) * 5) * 22 * (1 - prog(lt, 1.2, 1.0))
        y0 = 720
        d.line([S(540), S(y0), S(540), S(1180)], fill=C, width=S(14))
        rrect(d, 420, 1170, 660, 1200, 14, fill=C)
        d.line([S(200), S(y0 - tilt), S(880), S(y0 + tilt)], fill=C, width=S(14))
        circle(d, 540, y0, 22, fill=Y)
        for x, y, lab in [(200, y0 - tilt, "$5"), (880, y0 + tilt, "$20")]:
            d.line([S(x), S(y), S(x), S(y + 160)], fill=C, width=S(6))
            bill(d, x, y + 220, 270, GB, label=lab)
    pop_line(d, lt, 2.2, 540, 1330, "DIO IGUAL", 170, R)
    slide_line(d, lt, 2.6, 540, 1460, "importó en quién la gastaron", 46, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "PROBALO HOY:", 130, C)
    pop_line(d, lt, 0.3, 540, 500, "INVITÁ UN CAFÉ", 150, Y)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        cx, cy = 540, 860
        rrect(d, cx - 150 * e, cy - 110 * e, cx + 150 * e, cy + 130 * e, 40 * e, fill=C)
        d.arc([S(cx + 110 * e), S(cy - 80 * e), S(cx + 240 * e), S(cy + 70 * e)], -90, 90, fill=C, width=S(26))
        for k in range(3):
            xx = cx + (k - 1) * 80
            yy = cy - 180 - 40 * math.sin(lt * 4 + k)
            circle(d, xx, yy, 22 * e, fill=mix(K, C, 0.4))
    pop_line(d, lt, 1.5, 540, 1190, "¿A QUIÉN", 140, C)
    pop_line(d, lt, 1.8, 540, 1350, "LE INVITÁS?", 150, Y)
    slide_line(d, lt, 2.3, 540, 1500, "contame en los comentarios", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.05, "pop", -0.2); ev(0.28, "pop", 0.2); ev(0.52, "thump"); ev(1.8, "tap")
for k in range(5): ev(0.8 + k * 0.2, "rustle", 0.4 if k % 2 else -0.4)
ev(4.1, "tap"); ev(4.3, "tap", 0.2); ev(4.55, "pop"); ev(5.1, "rustle"); ev(5.5, "shimmer"); ev(6.2, "thump"); ev(6.6, "tap")
ev(8.1, "tap", -0.3); ev(8.3, "tap", 0.3); ev(8.9, "pop"); ev(9.1, "pop", -0.4); ev(9.6, "pop", 0.4); ev(10.5, "tap"); ev(10.8, "pop")
ev(12.1, "tap"); ev(12.3, "pop", -0.4); ev(12.5, "pop", 0.4); ev(13.3, "shimmer"); ev(14.1, "stamp"); ev(14.5, "tap"); ev(14.8, "tap")
ev(16.1, "tap"); ev(16.3, "pop")
for k in range(9): ev(16.8 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(18.2, "thump"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.5, "pop", 0.3); ev(21.5, "pop", -0.2); ev(21.8, "thump"); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
