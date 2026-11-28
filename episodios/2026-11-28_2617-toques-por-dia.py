"""Short 2026-11-28 15:00 — ¿Cuántas veces tocás el celu por día? 2.617 toques (dscout, estudio Mobile Touches 2016)."""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "dscout, estudio \"Mobile Touches\", 2016"

def finger(d, cx, cy, s, col=C):
    """Dedo índice simple apuntando hacia abajo (punta en cx, cy)."""
    rrect(d, cx - s * 0.16, cy - s * 0.9, cx + s * 0.16, cy, s * 0.16, fill=col)
    rrect(d, cx - s * 0.34, cy - s * 1.35, cx + s * 0.34, cy - s * 0.7, s * 0.2, fill=col)

def ripple(d, cx, cy, t, t0, col=Y, rmax=110):
    p = prog(t, t0, 0.45)
    if 0 < p < 1:
        r = 20 + rmax * ease_out(p)
        circle(d, cx, cy, r, outline=mix(K, col, 1 - p), width=8)

def b1(d, t):
    # celu con un dedo que toca sin parar
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        phone(d, 540, 560, 300 * e, 540 * e)
        if e > 0.9:
            rnd = random.Random(3)
            for k in range(14):
                tt = 0.4 + k * 0.25
                x, y = rnd.uniform(440, 640), rnd.uniform(380, 740)
                ripple(d, x, y, t, tt, rmax=60)
                if tt <= t < tt + 0.25:
                    finger(d, x, y - lerp(30, 0, prog(t, tt, 0.1)), 150)
    pop_line(d, t, 0.0, 540, 1010, "¿CUÁNTAS VECES", 140, C)
    pop_line(d, t, 0.3, 540, 1170, "TOCÁS EL CELU", 140, C)
    pop_line(d, t, 0.6, 540, 1340, "POR DÍA?", 180, Y)
    slide_line(d, t, 1.5, 540, 1500, "pensá un número antes de seguir", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "LO MIDIERON", 140, C)
    slide_line(d, lt, 0.3, 540, 430, "CON UNA APP", 120, Y)
    # 94 personitas en grilla
    n = int(94 * ease_out(prog(lt, 0.5, 1.0)))
    for k in range(n):
        gx, gy = k % 12, k // 12
        person(d, 155 + gx * 70, 560 + gy * 62, 54, mix(K, C, 0.75))
    pill(d, lt, 1.6, 300, 1130, 400, "94 PERSONAS", fill=Y, ink=K, size=44, h=96)
    pill(d, lt, 1.9, 780, 1130, 420, "5 DÍAS, 24 H", fill=C, ink=K, size=44, h=96)
    slide_line(d, lt, 2.3, 540, 1270, "contó cada toque, cada deslizada", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1330, "y cada clic en la pantalla", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1430, SRC, 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "EN PROMEDIO", 130, C)
    # contador gigante con dedos que tocan alrededor
    rnd = random.Random(9)
    for k in range(26):
        tt = 0.5 + k * 0.08
        ripple(d, rnd.uniform(120, 960), rnd.uniform(520, 1000), lt, tt, col=C, rmax=70)
    cnt = 2617 * ease_out(prog(lt, 0.4, 1.6))
    if lt > 0.4:
        sx, sy = shake(lt, 2.0, 0.35, 14)
        text_c(d, 540 + sx, 760 + sy, fmt_num(cnt), "A", 330, Y)
    stamp(d, lt, 2.0, 540, 1110, 380, 100, "TOQUES POR DÍA", fill=Y, ink=K, size=110)
    slide_line(d, lt, 2.5, 540, 1300, "y eso que es un número bajo:", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1360, "con el celu bloqueado no contaba todo", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "LOS QUE MÁS", 130, C)
    slide_line(d, lt, 0.3, 540, 430, "LO USAN (10%)", 130, R)
    # dos barras que crecen: promedio vs. los que más
    base = 1230
    for i, (val, lab, col, t0) in enumerate(((2617, "PROMEDIO", C, 0.6), (5427, "EL 10% QUE MÁS", R, 1.2))):
        x = 330 + i * 420
        p = ease_out(prog(lt, t0, 0.8))
        hgt = 470 * val / 5427 * p
        if p > 0:
            rrect(d, x - 120, base - hgt, x + 120, base, 24, fill=col)
            text_c(d, x, base - hgt - 70, fmt_num(val * p), "A", 100, col)
            text_c(d, x, base + 60, lab, "Black", 38, C)
    pop_line(d, lt, 2.2, 540, 1420, "EL DOBLE: 5.427", 120, R)
    slide_line(d, lt, 2.6, 540, 1540, SRC, 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    # luna + reloj nocturno
    e = back(prog(lt, 0.1, 0.4))
    if e > 0.02:
        moon(d, 540, 470, 150 * e)
        zzz(d, 640, 420, lt)
    slide_line(d, lt, 0.5, 540, 760, "Y DE NOCHE...", 130, C)
    cnt = 87 * ease_out(prog(lt, 0.8, 1.0))
    if lt > 0.8:
        sx, sy = shake(lt, 1.8, 0.3, 12)
        text_c(d, 540 + sx, 980 + sy, f"{int(cnt)}%", "A", 260, Y)
    slide_line(d, lt, 1.8, 540, 1170, "lo agarró al menos una vez", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.9, 540, 1235, "entre las 0 y las 5 de la mañana", 50, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.4, 540, 1380, 900, "LO AGARRAMOS 76 VECES POR DÍA", fill=C, ink=K, size=38, h=96)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 320, "OJO:", 130, C)
    slide_line(d, lt, 0.3, 540, 470, "2 DE CADA 3", 150, Y)
    slide_line(d, lt, 0.45, 540, 610, "CREÍAN QUE LO", 110, C)
    slide_line(d, lt, 0.6, 540, 730, "USABAN MENOS", 110, C)
    slide_line(d, lt, 1.1, 540, 880, "mirá tu tiempo de pantalla en ajustes", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.2, 540, 940, "y compará con lo que pensabas", 44, C, kind="SemiBold", dy=25)
    pill(d, lt, 1.8, 540, 1110, 900, "¿CUÁNTAS VECES CREÉS VOS?", fill=Y, ink=K, size=48, h=110)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.0, "pop", -0.3); ev(0.3, "pop", 0.3); ev(0.6, "thump"); ev(1.5, "tap")
for k in range(14): ev(0.4 + k * 0.25, "tap", 0.3 if k % 2 else -0.3)
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(10): ev(4.5 + k * 0.1, "pop", -0.4 + k * 0.08)
ev(5.6, "pop", -0.4); ev(5.9, "pop", 0.4); ev(6.3, "tap"); ev(6.4, "tap"); ev(6.6, "tap")
ev(8.1, "tap")
for k in range(16): ev(8.4 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(9.8, "stamp"); ev(10.0, "thump"); ev(10.5, "tap"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.3, "tap")
for k in range(8): ev(12.6 + k * 0.1, "tick", -0.4)
for k in range(8): ev(13.2 + k * 0.1, "tick", 0.4)
ev(14.2, "thump"); ev(14.6, "tap")
ev(16.1, "shimmer")
for k in range(9): ev(16.8 + k * 0.11, "tick")
ev(17.8, "thump"); ev(17.8, "buzz"); ev(18.4, "pop")
ev(20.1, "tap"); ev(20.3, "stamp"); ev(20.45, "tap"); ev(20.6, "tap"); ev(21.1, "tap"); ev(21.2, "tap"); ev(21.8, "pop"); ev(22.0, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
