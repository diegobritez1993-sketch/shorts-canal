"""Short 2026-11-04 20:00 — Chicos y pantallas: cuántas notificaciones recibe un adolescente por día.
Fuente: Common Sense Media, "Constant Companion: A Week in the Life of a Young Person's Smartphone Use" (sept. 2023),
EE.UU., ~200 chicos de 11 a 17 años, datos reales de uso del celular (vía CNN/KEYT y Deseret News, 26-27/09/2023).
- La mitad recibió 237 notificaciones o más en un día típico.
- Cerca de 1 de cada 4 llegó en horario de clase; ~5% de noche.
- Casi todos usaron el celular en horario escolar, promedio ~43 minutos.
- Más de la mitad lo usó de noche en días de escuela.
Consejos del informe/expertos: silenciar notificaciones, "No molestar", celular fuera del cuarto de noche.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Common Sense Media, \"Constant Companion\", 2023 (EE.UU., 11-17 años)"


def badge(d, cx, cy, r, txt):
    circle(d, cx, cy, r, fill=R, outline=K, width=8)
    text_c(d, cx, cy, txt, "Black", r * 0.8, C, bg=R)


def notif_card(d, cx, cy, w, alpha):
    """Tarjetita de notificación genérica (sin marcas)."""
    if alpha <= 0.02: return
    col = mix(K, K2, alpha)
    rrect(d, cx - w / 2, cy - 48, cx + w / 2, cy + 48, 26, fill=mix(K, (44, 44, 44), alpha))
    rrect(d, cx - w / 2 + 22, cy - 28, cx - w / 2 + 78, cy + 28, 14, fill=mix(K, Y, alpha))
    rrect(d, cx - w / 2 + 100, cy - 22, cx + w * 0.25, cy - 8, 7, fill=mix(K, C, alpha * 0.9))
    rrect(d, cx - w / 2 + 100, cy + 8, cx + w * 0.05, cy + 22, 7, fill=mix(K, (130, 130, 130), alpha))


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 300, "¿CUÁNTAS", 150, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 450, "NOTIFICACIONES", 135, Y, dur=0.25)
    pop_line(d, lt, 0.4, 540, 590, "LE LLEGAN A TU HIJO?", 100, C, dur=0.25)
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        bz = 1.0 if (lt > 1.0 and (lt * 3) % 1 < 0.5) else 0.0
        phone(d, 540, 1050, 300 * e, 560 * e, buzz=bz, t=lt)
        if e > 0.8:
            bell(d, 540, 1040, 150, Y)
            n = int(99 * ease_in_out(prog(lt, 1.0, 2.2)))
            if n > 0: badge(d, 660, 790, 70, f"{n}+" if n >= 99 else str(n))
    slide_line(d, lt, 2.6, 540, 1450, "en un solo día", 50, C, kind="SemiBold", dy=25)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "LA MITAD RECIBE", 115, C)
    n = 237 * ease_out(prog(lt, 0.4, 1.5))
    sx, sy = shake(lt, 1.9, 0.35, 18)
    if lt > 0.4:
        text_c(d, 540 + sx, 500 + sy, str(int(n)), "A", 280, Y)
    slide_line(d, lt, 1.9, 540, 710, "O MÁS POR DÍA", 100, C)
    # lluvia de notificaciones apilándose
    for k in range(6):
        q = ease_out(prog(lt, 0.5 + k * 0.22, 0.3))
        if q <= 0: continue
        y = lerp(1500, 860 + k * 105, q)
        notif_card(d, 540, y, 760, q)
    slide_line(d, lt, 2.6, 540, 1530, SRC, 26, G, kind="SemiBold", dy=15)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 280, "1 DE CADA 4", 160, Y)
    slide_line(d, lt, 0.3, 540, 430, "LLEGA EN CLASE", 120, C)
    # pizarrón con avisos que interrumpen
    e = ease_out(prog(lt, 0.5, 0.35))
    if e > 0.02:
        rrect(d, 540 - 400 * e, 590, 540 + 400 * e, 1060, 24, fill=(30, 60, 45), outline=(150, 110, 60), width=18)
        if e > 0.9:
            text_c(d, 540, 700, "2 + 2 = ?", "Bold", 80, C, bg=(30, 60, 45))
            for k in range(3):
                q = back(prog(lt, 1.1 + k * 0.4, 0.3))
                if q > 0.02:
                    x = [300, 760, 520][k]; y = [860, 900, 980][k]
                    bubble(d, x, y, 150 * q, Y)
    donut(d, 540, 1270, 160, 0.25 * ease_out(prog(lt, 1.5, 0.8)), "25%", col=Y)
    slide_line(d, lt, 2.2, 540, 1490, "de las notificaciones, en horario escolar", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.6, 540, 1570, SRC, 26, G, kind="SemiBold", dy=15)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "CASI TODOS USARON", 110, C)
    slide_line(d, lt, 0.3, 540, 410, "EL CELU EN LA ESCUELA", 105, C)
    pr = ease_in_out(prog(lt, 0.7, 1.6))
    clock(d, 540, 800, 260, pr, turns=1, fill_deg=258)    # 43 de 60 minutos
    m = int(43 * pr)
    sx, sy = shake(lt, 2.3, 0.35, 16)
    if lt > 0.7:
        text_c(d, 540 + sx, 1190 + sy, f"~{m} MINUTOS", "A", 170, Y)
    slide_line(d, lt, 2.3, 540, 1330, "en promedio, en horario de clase", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.5, 540, 1420, SRC, 26, G, kind="SemiBold", dy=15)


def b5(d, t):
    lt = t - 16
    stars(d, lt, alpha=clamp(lt * 2))
    slide_line(d, lt, 0.1, 540, 280, "Y DE NOCHE...", 140, C)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        moon(d, 820, 560, 110 * e, Y)
        # cama + celu iluminado
        rrect(d, 150, 900, 930, 1040, 30, fill=K2)
        rrect(d, 150, 830, 330, 930, 40, fill=(60, 60, 60))
        glow = 0.6 + 0.4 * math.sin(lt * 7)
        phone(d, 640, 760, 130 * e, 230 * e, body=mix(K2, (80, 110, 160), glow), buzz=1.0 if lt > 1.0 else 0, t=lt)
    pop_line(d, lt, 1.3, 540, 1210, "MÁS DE LA MITAD", 130, Y)
    slide_line(d, lt, 1.6, 540, 1340, "lo usó de madrugada en días de escuela", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.4, 540, 1430, SRC, 26, G, kind="SemiBold", dy=15)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 280, "MENOS AVISOS,", 125, C)
    pop_line(d, lt, 0.3, 540, 445, "MÁS PAZ", 150, Y)
    rows = [("No molestar", 0.6, True), ("Avisos de apps", 0.95, False), ("Celu fuera del cuarto", 1.3, True)]
    for k, (lab, t0, on) in enumerate(rows):
        q = prog(lt, t0 - 0.2, 0.25)
        if q <= 0: continue
        sw = ease_in_out(prog(lt, t0 + 0.2, 0.3))
        toggle_row(d, 110, 590 + k * 190, lab, sw if on else 1 - sw)
    slide_line(d, lt, 1.9, 540, 1220, "¿cuántas te llegaron hoy a vos?", 48, Y, kind="Bold", dy=25)
    slide_line(d, lt, 2.1, 540, 1290, "fijate en ajustes y contalo abajo", 42, C, kind="SemiBold", dy=25)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.4, "pop"); ev(0.6, "pop")
for k in range(5): ev(1.0 + k * 0.667, "buzz")
for k in range(12): ev(1.1 + k * 0.17, "tick", 0.3 if k % 2 else -0.3)
ev(2.6, "tap")
ev(4.1, "tap")
for k in range(15): ev(4.4 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
for k in range(6): ev(4.5 + k * 0.22, "ding" if k % 2 else "pop", -0.4 + k * 0.16)
ev(5.9, "thump"); ev(6.0, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.5, "swipe")
for k in range(3): ev(9.1 + k * 0.4, "pop", [-0.4, 0.4, 0.0][k])
ev(9.5, "shimmer"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.3, "tap")
for k in range(16): ev(12.7 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(14.3, "thump"); ev(14.4, "tap")
ev(16.1, "tap"); ev(16.4, "shimmer"); ev(17.0, "buzz"); ev(17.3, "pop"); ev(17.6, "tap"); ev(18.4, "tap"); ev(18.2, "buzz")
ev(20.05, "tap"); ev(20.3, "pop")
for k, t0 in enumerate([0.6, 0.95, 1.3]): ev(20 + t0 - 0.2, "tap"); ev(20 + t0 + 0.25, "toggle")
ev(21.9, "ding"); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
