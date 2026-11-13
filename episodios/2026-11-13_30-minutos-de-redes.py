"""Short 2026-11-13 20:00 — Mente y emociones: limitar las redes a ~30 min por día bajó la soledad y la depresión.

Fuente: Hunt, Marx, Lipson y Young, Univ. de Pensilvania, "No More FOMO: Limiting Social Media Decreases Loneliness and
Depression", Journal of Social and Clinical Psychology (dic. 2018). Vía Quartz (nov. 2018).
- 143 estudiantes universitarios (dos tandas), con Facebook, Instagram y Snapchat en iPhone.
- 1 semana de base; luego 3 semanas: un grupo usó redes normal, el otro 10 min por app por día (≈30 min en total).
- El grupo con límite: baja significativa de soledad y depresión, sobre todo en quienes empezaron más deprimidos.
- Ansiedad y FOMO bajaron en LOS DOS grupos (posiblemente por prestar atención al propio uso).
- Conclusión de los autores: ~30 min por día puede mejorar el bienestar. (No hubo cambios en autoestima ni apoyo social.)
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

APP_COLS = [(10, 132, 255), (255, 45, 85), (255, 214, 10)]

def app_tile(d, cx, cy, s, col, q=1.0):
    """Ícono de app genérico (sin marca): cuadrado redondeado con un globito."""
    hs = s / 2 * q
    if hs < 2: return
    rrect(d, cx - hs, cy - hs, cx + hs, cy + hs, hs * 0.42, fill=col)
    bubble(d, cx, cy + hs * 0.05, hs * 1.1, mix(col, C, 0.85), ink=col)

def hourglass(d, cx, cy, s, p, t):
    """Reloj de arena: p 0..1 arena que cae."""
    w, h = s * 0.55, s
    rrect(d, cx - w * 0.65, cy - h / 2 - 22, cx + w * 0.65, cy - h / 2, 10, fill=C)
    rrect(d, cx - w * 0.65, cy + h / 2, cx + w * 0.65, cy + h / 2 + 22, 10, fill=C)
    top = [(S(cx - w / 2), S(cy - h / 2)), (S(cx + w / 2), S(cy - h / 2)), (S(cx + 8), S(cy)), (S(cx - 8), S(cy))]
    bot = [(S(cx - 8), S(cy)), (S(cx + 8), S(cy)), (S(cx + w / 2), S(cy + h / 2)), (S(cx - w / 2), S(cy + h / 2))]
    d.polygon(top, outline=C, width=S(8)); d.polygon(bot, outline=C, width=S(8))
    # arena arriba
    a = 1 - p
    if a > 0.02:
        yy = cy - h / 2 * a * 0.85
        ww = (cy - yy) / (h / 2) * (w / 2 - 8) + 8
        d.polygon([(S(cx - ww + 6), S(yy)), (S(cx + ww - 6), S(yy)), (S(cx + 4), S(cy - 6)), (S(cx - 4), S(cy - 6))], fill=Y)
    if p > 0.02:
        yy = cy + h / 2 - h / 2 * p * 0.8
        ww = (yy - cy) / (h / 2) * (w / 2 - 8) + 8
        d.polygon([(S(cx - ww + 6), S(yy)), (S(cx + ww - 6), S(yy)), (S(cx + w / 2 - 10), S(cy + h / 2 - 4)), (S(cx - w / 2 + 10), S(cy + h / 2 - 4))], fill=Y)
    if 0.02 < p < 0.98:
        d.line([S(cx), S(cy), S(cx), S(cy + h / 2 - 8)], fill=Y, width=S(5))

def arrow_down(d, cx, cy, s, col):
    rrect(d, cx - s * 0.12, cy - s * 0.5, cx + s * 0.12, cy + s * 0.1, 8, fill=col)
    d.polygon([(S(cx - s * 0.35), S(cy + s * 0.02)), (S(cx + s * 0.35), S(cy + s * 0.02)), (S(cx), S(cy + s * 0.5))], fill=col)

def b1(d, t):
    # tres apps que aparecen y laten
    for k in range(3):
        q = back(prog(t, 0.05 + k * 0.12, 0.35))
        if q > 0.02:
            pul = 1 + 0.05 * math.sin(t * 8 + k)
            app_tile(d, 270 + k * 270, 520, 200 * pul, APP_COLS[k], q)
    # tijera / corte: barra que se encoge
    pop_line(d, t, 0.0, 540, 880, "MENOS REDES,", 150, C)
    pop_line(d, t, 0.35, 540, 1050, "MENOS", 170, Y)
    pop_line(d, t, 0.55, 540, 1210, "SOLEDAD", 170, Y)
    pill(d, t, 2.2, 540, 1400, 800, "LO PROBARON CON UN LÍMITE", fill=R, ink=C, size=40, h=96)

def b2(d, t):
    lt = t - 4
    pop_line(d, lt, 0.1, 540, 290, "143", 200, Y)
    slide_line(d, lt, 0.35, 540, 440, "ESTUDIANTES", 120, C)
    # 143 puntitos que se separan en 2 grupos
    sep = ease_in_out(prog(lt, 1.4, 0.7))
    n = 143
    for i in range(n):
        q = prog(lt, 0.5 + i * 0.006, 0.2)
        if q <= 0: continue
        g = i % 2
        col_i, row_i = (i // 2) % 8, (i // 2) // 8
        x0 = 140 + (i % 16) * 53
        y0 = 600 + (i // 16) * 53
        x1 = (150 if g == 0 else 600) + col_i * 47
        y1 = 600 + row_i * 47
        x, y = lerp(x0, x1, sep), lerp(y0, y1, sep)
        col = mix(C, (C if g == 0 else Y), sep)
        circle(d, x, y, 16 * ease_out(q), fill=col)
    q = prog(lt, 2.0, 0.3)
    if q > 0:
        text_c(d, 315, 1100, "REDES NORMAL", "Black", 38, C, alpha=clamp(q * 2))
        text_c(d, 765, 1100, "CON LÍMITE", "Black", 38, Y, alpha=clamp(q * 2))
    slide_line(d, lt, 2.4, 540, 1200, "Hunt et al., Univ. de Pensilvania, 2018", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "10 MIN", 160, Y)
    slide_line(d, lt, 0.3, 540, 430, "POR APP, POR DÍA", 110, C)
    # 3 apps con barra de tiempo que se llena y se bloquea
    for k in range(3):
        q = back(prog(lt, 0.5 + k * 0.15, 0.3))
        y = 620 + k * 170
        if q <= 0.02: continue
        app_tile(d, 210, y, 120, APP_COLS[k], q)
        p = ease_out(prog(lt, 0.8 + k * 0.3, 0.8))
        rrect(d, 310, y - 30, 900, y + 30, 30, fill=K2)
        if p > 0.02:
            rrect(d, 310, y - 30, 310 + 590 * p, y + 30, 30, fill=APP_COLS[k] if p < 1 else R)
        if p >= 1:
            text_c(d, 605, y, "LÍMITE", "Black", 34, C, bg=R)
    pill(d, lt, 2.2, 540, 1210, 560, "≈ 30 MIN EN TOTAL", fill=Y, ink=K, size=46, h=100)
    # tira de 21 días
    for k in range(21):
        q = prog(lt, 2.4 + k * 0.03, 0.15)
        if q <= 0: continue
        x = 120 + (k % 21) * 40
        rrect(d, x, 1330, x + 30, 1380, 8, fill=mix(K, Y, q))
    slide_line(d, lt, 2.5, 540, 1440, "durante 3 semanas", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO", 140, C)
    for i, lab in enumerate(["SOLEDAD", "DEPRESIÓN"]):
        q = back(prog(lt, 0.5 + i * 0.5, 0.35))
        y = 560 + i * 260
        if q > 0.02:
            arrow_down(d, 230, y + math.sin(lt * 4 + i) * 8, 170 * q, GREEN)
            text_l(d, 360, y, lab, "A", 120, C)
            text_l(d, 360, y + 85, "bajó", "Bold", 44, GREEN)
    sx, sy = shake(lt, 1.9, 0.35, 14)
    stamp(d, lt, 1.85, 540 + sx, 1130 + sy, 330, 90, "EN 3 SEMANAS", fill=Y, ink=K, size=110)
    slide_line(d, lt, 2.4, 540, 1290, "sobre todo en los que", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.55, 540, 1360, "estaban peor al empezar", 46, Y, kind="Bold", dy=25)
    slide_line(d, lt, 2.8, 540, 1440, "Journal of Social and Clinical Psychology (vía Quartz)", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "DATO EXTRA", 130, Y)
    e = ease_out(prog(lt, 0.3, 0.4))
    if e > 0.02:
        hourglass(d, 540, 680, 380 * e, ease_in_out(prog(lt, 0.6, 2.8)), lt)
    slide_line(d, lt, 1.0, 540, 1000, "LA ANSIEDAD Y EL MIEDO", 80, C, kind="A", dy=30)
    slide_line(d, lt, 1.2, 540, 1095, "A PERDERTE ALGO", 80, C, kind="A", dy=30)
    pill(d, lt, 1.6, 540, 1240, 760, "BAJARON EN LOS DOS GRUPOS", fill=GREEN, ink=K, size=42, h=96)
    slide_line(d, lt, 2.2, 540, 1370, "tal vez con solo fijarte", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1440, "cuánto tiempo usás", 46, Y, kind="Bold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 280, "PROBALO:", 120, Y)
    q = ease_in_out(prog(lt, 0.5, 0.3))
    sl = ease_out(prog(lt, 0.2, 0.35))
    if sl > 0:
        toggle_row(d, 110 + (1 - sl) * 600, 380, "Límite de apps", q, sub="en los ajustes de tu celu")
    pop_line(d, lt, 1.1, 540, 730, "¿CUÁNTO USASTE", 125, C)
    pop_line(d, lt, 1.35, 540, 870, "LAS REDES HOY?", 125, Y)
    slide_line(d, lt, 1.8, 540, 1010, "fijate en tu celu y comentalo", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1140, "si te sentís mal seguido, hablalo", 34, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.3, 540, 1190, "con alguien de confianza o un profesional", 34, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop", -0.5); ev(0.17, "pop"); ev(0.29, "pop", 0.5); ev(0.35, "thump"); ev(0.55, "pop"); ev(2.2, "click")
ev(4.1, "thump"); ev(4.35, "swipe")
for k in range(12): ev(4.5 + k * 0.07, "tap", -0.6 + k * 0.1)
ev(5.4, "rustle"); ev(6.0, "pop", -0.4); ev(6.1, "pop", 0.4); ev(6.4, "tap")
ev(8.1, "swipe"); ev(8.3, "swipe"); ev(8.5, "pop", -0.3); ev(8.65, "pop"); ev(8.8, "pop", 0.3)
ev(9.6, "buzz"); ev(9.9, "buzz"); ev(10.2, "buzz"); ev(10.2, "click")
for k in range(7): ev(10.4 + k * 0.09, "tick")
ev(10.5, "tap")
ev(12.1, "swipe"); ev(12.5, "pop"); ev(13.0, "pop"); ev(13.85, "stamp"); ev(14.4, "tap"); ev(14.55, "tap"); ev(14.8, "tap")
ev(16.1, "pop"); ev(16.3, "rustle"); ev(17.0, "swipe"); ev(17.2, "swipe"); ev(17.6, "shimmer"); ev(18.2, "tap"); ev(18.35, "tap")
ev(20.1, "swipe"); ev(20.2, "click"); ev(20.5, "toggle"); ev(21.1, "pop"); ev(21.35, "thump"); ev(21.8, "tap"); ev(22.2, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
