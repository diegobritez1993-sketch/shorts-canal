"""Short 2026-11-06 15:00 — Cómo te enganchan las apps: relojes de cuenta regresiva falsos (falsa urgencia).
Fuente: Comisión Europea, comunicado IP/23/418 (30/01/2023): "sweep" de 399 tiendas online en 23 países de la UE
+ Noruega e Islandia; 148 usaban al menos una práctica manipuladora: 42 con relojes de cuenta regresiva falsos,
54 con diseños que empujan a comprar o suscribirse, 70 que escondían información importante.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def timer(d, cx, cy, w, h, secs, col=R, frame=K2):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, h * 0.18, fill=frame, outline=col, width=8)
    secs = max(0, int(secs))
    txt = f"{secs // 3600:02d}:{(secs // 60) % 60:02d}:{secs % 60:02d}"
    text_c(d, cx, cy + 4, txt, "A", int(h * 0.62), col, bg=frame)

def cart(d, cx, cy, s, col):
    w = max(2, int(S(s * 0.07)))
    d.line([S(cx - s * 0.55), S(cy - s * 0.42), S(cx - s * 0.38), S(cy - s * 0.42), S(cx - s * 0.22), S(cy + s * 0.2),
            S(cx + s * 0.42), S(cy + s * 0.2)], fill=col, width=w, joint="curve")
    d.polygon([(S(cx - s * 0.33), S(cy - s * 0.25)), (S(cx + s * 0.55), S(cy - s * 0.25)),
               (S(cx + s * 0.45), S(cy + s * 0.08)), (S(cx - s * 0.25), S(cy + s * 0.08))], fill=col)
    circle(d, cx - s * 0.14, cy + s * 0.36, s * 0.09, fill=col)
    circle(d, cx + s * 0.34, cy + s * 0.36, s * 0.09, fill=col)

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        sx, sy = shake(t, 0.3, 0.3, 10)
        timer(d, 540 + sx, 470 + sy, 760 * e, 230 * e, 9 * 60 + 59 - int(t * 3))
    pop_line(d, t, 0.15, 540, 820, "¿ESE RELOJ", 175, C)
    sx, sy = shake(t, 0.75, 0.35, 18)
    pop_line(d, t, 0.55, 540 + sx, 1010 + sy, "ES REAL?", 230, Y, dur=0.28)
    slide_line(d, t, 1.4, 540, 1180, "\"la oferta termina en...\"", 50, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.2, 540, 1270, "muchas veces, no termina nunca", 46, R, kind="Bold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 260, "EUROPA REVISÓ", 130, C)
    n = int(399 * ease_out(prog(lt, 0.4, 1.4)))
    pop_line(d, lt, 0.35, 540, 465, fmt_num(n), 210, Y)
    slide_line(d, lt, 0.6, 540, 660, "TIENDAS ONLINE", 105, C)
    # grilla de tienditas que aparecen
    cols, rows = 10, 6
    for k in range(cols * rows):
        p = back(prog(lt, 0.5 + k * 0.025, 0.25))
        if p <= 0.02: continue
        x = 540 + (k % cols - (cols - 1) / 2) * 88
        y = 820 + (k // cols) * 88
        s = 30 * p
        rrect(d, x - s, y - s * 0.6, x + s, y + s, 8, fill=K2, outline=G, width=3)
        d.rectangle([S(x - s), S(y - s * 0.75), S(x + s), S(y - s * 0.45)], fill=Y)
    slide_line(d, lt, 2.2, 540, 1400, "en 25 países, buscando trampas", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1480, "Comisión Europea, enero 2023", 34, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    # 3 carritos, uno se pone rojo
    for i, x in enumerate((270, 540, 810)):
        p = back(prog(lt, 0.1 + i * 0.15, 0.3))
        if p <= 0.02: continue
        red = i == 1 and lt > 1.0
        col = R if red else C
        sx, sy = shake(lt, 1.0, 0.35, 12) if i == 1 else (0, 0)
        cart(d, x + sx, 470 + sy, 220 * p, col)
    if lt > 1.0:
        ban(d, 540, 470, 150, ease_out(prog(lt, 1.0, 0.25)), width=22)
    pop_line(d, lt, 1.1, 540, 780, "148 TIENDAS", 165, R)
    slide_line(d, lt, 1.4, 540, 920, "usaban trucos para manipularte", 48, C, kind="SemiBold", dy=25)
    stamp(d, lt, 2.0, 540, 1150, 440, 95, "MÁS DE 1 DE CADA 3", fill=Y, ink=K, size=115)
    slide_line(d, lt, 2.5, 540, 1300, "148 de 399 · Comisión Europea, 2023", 34, G, kind="SemiBold", dy=20)

def trick_row(d, lt, t0, y, label, n, col, maxn=70):
    p = ease_out(prog(lt, t0, 0.35))
    if p <= 0: return
    x0 = lerp(-900, 110, p)
    rrect(d, x0, y, x0 + 860, y + 190, 40, fill=K2)
    text_l(d, x0 + 45, y + 55, label, "Black", 44, C)
    b = ease_out(prog(lt, t0 + 0.3, 0.7))
    bw = 600 * (n / maxn) * b
    rrect(d, x0 + 45, y + 110, x0 + 45 + max(bw, 30), y + 160, 25, fill=col)
    text_l(d, x0 + 45 + max(bw, 30) + 25, y + 135, str(int(n * b)), "A", 70, col)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "LOS TRUCOS", 150, Y)
    trick_row(d, lt, 0.4, 420, "RELOJ FALSO", 42, R)
    trick_row(d, lt, 0.9, 650, "TE EMPUJAN A COMPRAR", 54, Y)
    trick_row(d, lt, 1.4, 880, "TE ESCONDEN INFO", 70, C)
    slide_line(d, lt, 2.2, 540, 1150, "cantidad de tiendas con cada truco", 42, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1225, "Comisión Europea, IP/23/418", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "¿PARA QUÉ?", 150, C)
    # reloj que corre cada vez más rápido + corazón que late
    sp = ease_in_out(prog(lt, 0.3, 2.5))
    secs = 30 - int(lt * (3 + 20 * sp)) if lt > 0.3 else 30
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        timer(d, 540, 540, 640 * e, 190 * e, max(secs, 0))
    beat = 1 + 0.12 * abs(math.sin(lt * (4 + 10 * sp)))
    if lt > 0.8:
        heart(d, 540, 820, 190 * beat * back(prog(lt, 0.8, 0.3)), R)
    pop_line(d, lt, 1.3, 540, 1070, "PARA QUE TE APURES", 120, Y)
    slide_line(d, lt, 1.7, 540, 1190, "con apuro comparás menos", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.0, 540, 1265, "y comprás sin pensarlo dos veces", 48, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 140, C)
    slide_line(d, lt, 0.3, 540, 450, "RECARGÁ LA PÁGINA", 120, Y)
    e = back(prog(lt, 0.5, 0.3))
    if e > 0.02:
        # reloj que se reinicia al recargar
        sec = 4 - int(max(0, lt - 0.6) * 4)
        shown = sec if sec >= 0 else 10 * 60
        timer(d, 540, 660, 560 * e, 160 * e, shown, col=R if sec >= 0 else Y)
    slide_line(d, lt, 1.0, 540, 820, "si vuelve a empezar, era falso", 48, C, kind="Bold", dy=25)
    pill(d, lt, 1.6, 540, 1010, 860, "¿TE PASÓ? SÍ O NO", fill=Y, ink=K, size=60, h=130)
    slide_line(d, lt, 2.0, 540, 1140, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.15, "pop", -0.3)
for k in range(12): ev(0.33 + k / 3, "tick", 0.3 if k % 2 else -0.3)
ev(0.55, "whoosh"); ev(0.75, "stamp"); ev(1.4, "tap"); ev(2.2, "tap", 0.3)
ev(4.1, "tap"); ev(4.35, "pop")
for k in range(12): ev(4.4 + k * 0.11, "tick", 0.2 if k % 2 else -0.2)
for k in range(8): ev(4.5 + k * 0.19, "pop", -0.6 + k * 0.17)
ev(4.6, "tap"); ev(6.2, "tap"); ev(6.5, "click")
ev(8.1, "pop", -0.5); ev(8.25, "pop"); ev(8.4, "pop", 0.5); ev(9.0, "buzz"); ev(9.1, "thump"); ev(9.4, "tap")
ev(9.8, "whoosh"); ev(10.0, "stamp"); ev(10.5, "tap")
ev(12.1, "tap")
for i, t0 in enumerate((12.4, 12.9, 13.4)):
    ev(t0, "swipe", -0.5); ev(t0 + 0.3, "ding" if i == 0 else "pop", 0.3)
ev(14.2, "tap"); ev(14.4, "click")
ev(16.1, "tap"); ev(16.3, "pop")
for k in range(14): ev(16.5 + k * (0.25 - k * 0.012), "tick", 0.2 if k % 2 else -0.2)
for k in range(5): ev(16.9 + k * 0.4, "thump")
ev(17.3, "pop"); ev(17.7, "tap"); ev(18.0, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.5, "pop")
for k in range(4): ev(20.6 + k * 0.25, "tick")
ev(21.6, "click"); ev(21.65, "shimmer"); ev(21.0, "tap"); ev(21.6, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
