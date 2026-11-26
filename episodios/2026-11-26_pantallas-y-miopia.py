"""Short 2026-11-26 20:00 — Pantallas y miopía: cada hora diaria, 21% más chances (Kim et al., JAMA Network Open, feb. 2025)."""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Fuente: JAMA Network Open, feb. 2025 (45 estudios)"
SKY = (90, 170, 255)

def eye(d, cx, cy, w, open_=1.0, iris=SKY, blur=0.0):
    """Ojo almendrado; open_ 0..1 (parpadeo)."""
    h = w * 0.36 * max(0.05, open_)
    d.ellipse([S(cx - w / 2), S(cy - h), S(cx + w / 2), S(cy + h)], fill=C)
    if open_ > 0.3:
        r = min(h * 0.95, w * 0.2)
        circle(d, cx, cy, r, fill=iris)
        circle(d, cx, cy, r * 0.45, fill=K)
        circle(d, cx + r * 0.3, cy - r * 0.3, r * 0.15, fill=C)
    d.ellipse([S(cx - w / 2), S(cy - h), S(cx + w / 2), S(cy + h)], outline=K2, width=S(6))

def chart_letters(d, cx, cy, blur):
    """Cartel de vista que se ve borroso según blur 0..1."""
    rows = [("E", 120), ("F P", 80), ("T O Z", 56), ("L P E D", 40)]
    y = cy
    for txt, sz in rows:
        if blur > 0:
            for k, (ox, oy) in enumerate(((-1, 0), (1, 0), (0, -1), (0, 1))):
                text_c(d, cx + ox * 8 * blur, y + oy * 6 * blur, txt, "Black", sz, mix(K, C, 0.25), bg=K)
        text_c(d, cx, y, txt, "Black", sz, mix(K, C, 1 - 0.75 * blur))
        y += sz * 1.25

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        blink = 1 - 0.95 * max(0, math.sin(clamp((t - 2.6) / 0.25) * math.pi))
        eye(d, 540, 520, 560 * e, open_=blink)
        # pantalla pegada al ojo
        px = lerp(1200, 860, ease_out(prog(t, 0.6, 0.5)))
        phone(d, px, 560, 200, 360, body=(40, 70, 140), outline=C)
    pop_line(d, t, 0.0, 540, 940, "¿TU HIJO VIVE", 140, C)
    pop_line(d, t, 0.3, 540, 1100, "CON LA PANTALLA", 140, C)
    pop_line(d, t, 0.6, 540, 1260, "PEGADA A LA CARA?", 125, Y)
    slide_line(d, t, 1.5, 540, 1420, "ojo con su vista de lejos", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "REVISARON", 130, C)
    pop_line(d, lt, 0.3, 540, 440, "45 ESTUDIOS", 170, Y)
    # hojas que se apilan
    n = int(45 * ease_out(prog(lt, 0.4, 1.2)))
    for k in range(n):
        x = 540 + ((k * 37) % 9 - 4) * 10
        y = 940 - k * 4
        rrect(d, x - 150, y - 100, x + 150, y + 100, 14, fill=mix(K2, C, 0.15 + 0.6 * (k == n - 1)), outline=(70, 70, 70), width=2)
    cnt = 335524 * ease_out(prog(lt, 0.6, 1.4))
    if lt > 0.6:
        sx, sy = shake(lt, 2.0, 0.3, 12)
        text_c(d, 540 + sx, 1140 + sy, fmt_num(cnt), "A", 190, C)
    pop_line(d, lt, 2.0, 540, 1300, "PERSONAS", 110, Y)
    slide_line(d, lt, 2.5, 540, 1440, SRC, 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "CADA HORA DIARIA", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "DE PANTALLA", 120, C)
    # barras por hora
    base = 1050
    for h in range(4):
        p = ease_out(prog(lt, 0.6 + h * 0.35, 0.35))
        if p <= 0: continue
        val = 1.21 ** (h + 1)
        hh = (val - 0.7) * 300 * p
        x = 230 + h * 210
        rrect(d, x - 70, base - hh, x + 70, base, 18, fill=mix(Y, R, h / 3))
        text_c(d, x, base + 50, f"{h + 1} H", "Black", 44, C)
    sx, sy = shake(lt, 2.2, 0.3, 14)
    pop_line(d, lt, 2.0, 540 + sx, 1280 + sy, "+21%", 210, Y, dur=0.28)
    slide_line(d, lt, 2.4, 540, 1430, "más chances de miopía", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.55, 540, 1490, "(ver borroso de lejos)", 44, G, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "MENOS DE 1 HORA", 130, GREEN)
    slide_line(d, lt, 0.3, 540, 420, "no se vio el riesgo", 54, C, kind="SemiBold", dy=25)
    blur = ease_in_out(prog(lt, 1.2, 1.4))
    e = ease_out(prog(lt, 0.3, 0.4))
    if e > 0.02:
        rrect(d, 300, 520, 780, 1000, 30, outline=mix(K, C, e), width=6)
        chart_letters(d, 540, 610, blur)
    pop_line(d, lt, 1.4, 540, 1130, "DE 1 A 4 HORAS", 120, R)
    slide_line(d, lt, 1.7, 540, 1260, "el riesgo sube fuerte", 54, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.3, 540, 1360, "es una relación, no prueba causa", 40, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y NO ES SOLO", 130, C)
    pop_line(d, lt, 0.3, 540, 440, "LA PANTALLA", 160, Y)
    # libro abierto + celu, muy cerca de un ojo
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        cx, cy = 540, 820
        w = 360 * e
        d.polygon([(S(cx), S(cy - 120 * e)), (S(cx - w / 2), S(cy - 150 * e)), (S(cx - w / 2), S(cy + 110 * e)), (S(cx), S(cy + 140 * e))], fill=C)
        d.polygon([(S(cx), S(cy - 120 * e)), (S(cx + w / 2), S(cy - 150 * e)), (S(cx + w / 2), S(cy + 110 * e)), (S(cx), S(cy + 140 * e))], fill=mix(C, K, 0.12))
        for k in range(5):
            y = cy - 80 * e + k * 40 * e
            d.line([S(cx - w * 0.4), S(y), S(cx - w * 0.08), S(y)], fill=G, width=S(5))
            d.line([S(cx + w * 0.08), S(y), S(cx + w * 0.4), S(y)], fill=G, width=S(5))
    slide_line(d, lt, 1.6, 540, 1110, "todo lo que se mira de cerca suma:", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.75, 540, 1170, "leer, escribir, pantallas", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.4, 540, 1310, 700, "MENOS TIEMPO DE CERCA", fill=Y, ink=K, size=44, h=100)

def b6(d, t):
    lt = t - 20
    e = back(prog(lt, 0.0, 0.4))
    if e > 0.02:
        sun(d, 540, 330, 110 * e, lt)
    slide_line(d, lt, 0.2, 540, 600, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.4, 540, 750, "MÁS TIEMPO", 150, Y)
    slide_line(d, lt, 0.55, 540, 900, "AL AIRE LIBRE", 150, Y)
    slide_line(d, lt, 1.2, 540, 1050, "y menos horas seguidas de cerca", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 1.8, 540, 1210, 860, "¿CUÁNTAS HORAS USA EL TUYO?", fill=Y, ink=K, size=44, h=110)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.3, "pop", 0.3); ev(0.6, "thump"); ev(0.6, "whoosh", 0.6); ev(1.5, "tap"); ev(2.6, "click")
ev(4.1, "tap"); ev(4.3, "stamp")
for k in range(10): ev(4.4 + k * 0.12, "rustle", 0.3 if k % 2 else -0.3)
for k in range(10): ev(4.6 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(6.0, "thump"); ev(6.0, "pop"); ev(6.5, "tap")
ev(8.1, "tap"); ev(8.3, "tap")
for h in range(4): ev(8.6 + h * 0.35, "pop", -0.5 + h * 0.33)
ev(10.0, "stamp"); ev(10.2, "thump"); ev(10.4, "tap"); ev(10.55, "tap")
ev(12.1, "pop"); ev(12.3, "tap"); ev(12.4, "shimmer"); ev(13.2, "whoosh"); ev(13.4, "buzz"); ev(13.4, "pop"); ev(13.7, "tap"); ev(14.3, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.6, "rustle"); ev(17.6, "tap"); ev(17.75, "tap"); ev(18.4, "pop"); ev(18.4, "ding")
ev(20.0, "shimmer"); ev(20.2, "tap"); ev(20.4, "pop", -0.2); ev(20.55, "pop", 0.2); ev(21.2, "tap"); ev(21.8, "pop"); ev(21.8, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
