"""Short 2026-11-08 15:00 - Cómo te enganchan las apps: 260 videos para formar el hábito.
Fuente: NPR / Kentucky Public Radio, 11-12/10/2024 (partes antes tachadas de la demanda de Kentucky contra TikTok)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def tile(d, cx, cy, w, h, col):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 22, fill=col)
    r = min(w, h) * 0.2
    d.polygon([(S(cx - r * 0.6), S(cy - r)), (S(cx - r * 0.6), S(cy + r)), (S(cx + r), S(cy))], fill=K)

def b1(d, t):
    e = back(prog(t, 0.0, 0.35))
    pop_line(d, t, 0.0, 540, 300, "¿CUÁNTOS VIDEOS", 150, C)
    pop_line(d, t, 0.3, 540, 465, "HACEN FALTA", 150, C)
    pop_line(d, t, 0.6, 540, 640, "PARA ENGANCHARTE?", 122, Y)
    if e > 0.02:
        for k in range(3):
            y = 1150 + (k - 1) * 40
            phone(d, 540, 1150, 330 * e, 590 * e, outline=C)
        sc = (t * 2.6) % 1
        ye = ease_in_out(sc)
        for k, col in enumerate([Y, R, GREEN, C]):
            yy = 1150 + (k - ye) * 420
            if 930 < yy < 1370:
                tile(d, 540, yy, 260 * e, 360 * e, mix(K, col, 0.85))
    pop_line(d, t, 1.8, 540, 1590, "ALGUIEN YA LO MIDIÓ", 90, R)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.05, 540, 280, "DOCUMENTOS INTERNOS", 110, C)
    slide_line(d, lt, 0.25, 540, 410, "DE TIKTOK", 130, Y)
    slide_line(d, lt, 0.45, 540, 510, "la cantidad exacta para crear el hábito", 40, C, kind="SemiBold", dy=25)
    p = ease_in_out(prog(lt, 0.8, 1.7))
    n = int(260 * p)
    sx, sy = shake(lt, 2.55, 0.4, 20)
    cols = [Y, R, GREEN, C]
    for k in range(min(n // 26, 10)):
        x = 150 + (k % 5) * 195
        y = 680 + (k // 5) * 130
        tile(d, x, y, 170, 110, mix(K, cols[k % 4], 0.8))
    if lt > 0.75:
        text_c(d, 540 + sx, 1130 + sy, fmt_num(n), "A", 330, Y if p >= 1 else C)
    pop_line(d, lt, 2.55, 540, 1370, "VIDEOS", 170, R)
    slide_line(d, lt, 2.9, 540, 1510, "demanda de Kentucky, vía NPR (2024)", 38, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.05, 540, 300, "¿Y EN CUÁNTO", 130, C)
    pop_line(d, lt, 0.5, 540, 460, "TIEMPO PASA?", 130, Y)
    # línea de tiempo que se llena
    x0, x1, y0, y1 = 110, 970, 680, 790
    if lt > 0.6:
        rrect(d, x0, y0, x1, y1, 55, fill=K2)
        f = ease_in_out(prog(lt, 0.8, 1.6))
        if f > 0.03:
            rrect(d, x0, y0, x0 + (x1 - x0) * f, y1, 55, fill=mix(Y, R, f))
        text_c(d, 540, 735, f"{int(35 * f)} MIN", "A", 72, C if f < 0.4 else K, bg=K2)
    sx, sy = shake(lt, 2.5, 0.4, 18)
    pop_line(d, lt, 2.4, 540 + sx, 1030 + sy, "MENOS DE", 120, C)
    pop_line(d, lt, 2.55, 540 + sx, 1220 + sy, "35 MINUTOS", 220, R, dur=0.26)
    slide_line(d, lt, 2.95, 540, 1400, "calcularon los investigadores del estado", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 3.1, 540, 1465, "para enganchar a un usuario promedio", 40, C, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.05, 540, 290, "¿Y EL LÍMITE", 140, C)
    slide_line(d, lt, 0.25, 540, 440, "DE TIEMPO?", 140, Y)
    q = ease_in_out(prog(lt, 0.8, 0.3))
    if lt > 0.5:
        toggle_row(d, 110, 580, "Límite de tiempo", q)
    a = ease_out(prog(lt, 1.2, 0.3))
    if a > 0:
        text_c(d, 540, 900, "108,5 MIN POR DÍA", "A", 120, mix(K, C, a))
        slide_line(d, lt, 1.3, 540, 990, "sin la herramienta", 42, G, kind="SemiBold", dy=20)
    pop_line(d, lt, 1.9, 540, 1140, "107 MIN POR DÍA", 120, Y)
    slide_line(d, lt, 2.0, 540, 1230, "con la herramienta", 42, G, kind="SemiBold", dy=20)
    stamp(d, lt, 2.7, 540, 1420, 390, 95, "1,5 MIN MENOS", fill=R, ink=C, size=120)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.05, 540, 300, "UN EMPLEADO", 130, C)
    slide_line(d, lt, 0.25, 540, 450, "LO DIJO ASÍ:", 130, Y)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        rrect(d, 540 - 470 * e, 800 - 270 * e, 540 + 470 * e, 800 + 270 * e, 50, fill=K2)
    pop_line(d, lt, 0.8, 540, 690, "“NUESTRO OBJETIVO", 110, C, bg=K2)
    pop_line(d, lt, 1.1, 540, 815, "NO ES REDUCIR", 120, R, bg=K2)
    pop_line(d, lt, 1.4, 540, 935, "EL TIEMPO DE USO”", 110, C, bg=K2)
    slide_line(d, lt, 2.0, 540, 1180, "TikTok responde que son citas", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.2, 540, 1245, "sacadas de contexto y documentos viejos", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.5, 540, 1330, "NPR / Kentucky Public Radio, 2024", 38, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 430, "¿CUÁNTOS", 200, C)
    pop_line(d, lt, 0.4, 540, 640, "VISTE HOY?", 200, Y)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        bubble(d, 540, 1000, 240 * e, C)
    pill(d, lt, 1.5, 540, 1300, 800, "CONTALO EN LOS COMENTARIOS", fill=Y, ink=K, size=44, h=100)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.3, "pop", 0.2); ev(0.6, "thump")
for k in range(9): ev(0.5 + k * 0.385, "swipe", 0.2 if k % 2 else -0.2)
ev(1.8, "buzz")
ev(4.05, "tap", -0.3); ev(4.25, "tap", 0.3); ev(4.45, "tap")
for k in range(24): ev(4.8 + k * 0.07, "tick", 0.3 if k % 2 else -0.3)
ev(6.55, "stamp"); ev(6.9, "tap")
ev(8.05, "tap"); ev(8.5, "pop")
for k in range(12): ev(8.8 + k * 0.13, "tick", 0.2 if k % 2 else -0.2)
ev(10.4, "pop"); ev(10.55, "thump"); ev(10.95, "tap"); ev(11.1, "tap")
ev(12.05, "tap", -0.3); ev(12.25, "tap", 0.3); ev(12.8, "toggle"); ev(13.2, "pop", -0.3); ev(13.9, "pop", 0.3); ev(14.7, "stamp")
ev(16.05, "tap"); ev(16.25, "tap"); ev(16.5, "rustle"); ev(16.8, "pop", -0.2); ev(17.1, "thump"); ev(17.4, "pop", 0.2); ev(18.0, "tap"); ev(18.2, "tap")
ev(20.1, "pop", -0.2); ev(20.4, "thump"); ev(20.7, "pop"); ev(21.5, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
