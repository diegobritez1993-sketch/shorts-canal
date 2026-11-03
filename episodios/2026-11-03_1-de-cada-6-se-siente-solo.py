"""Short 2026-11-03 20:00 — Mente y emociones: la soledad, 1 de cada 6 personas.
Fuente: OMS, Comisión sobre Conexión Social, comunicado del 30/06/2025: 1 de cada 6 personas en el mundo
está afectada por la soledad; entre 13 y 29 años lo reporta entre 17% y 21% (más en adolescentes);
más riesgo de ACV, enfermedades del corazón, diabetes y deterioro cognitivo; las personas solas tienen el
doble de probabilidad de deprimirse; adolescentes solos 22% más probabilidad de peores notas.
Consejos OMS: escribirle a un amigo, dejar el celular en las charlas, sumarse a un grupo; si es serio, buscar apoyo.
Tono: "ojo con esto", sin alarmismo; no se usa la cifra de muertes.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "OMS, Comisión sobre Conexión Social, 2025"
BLUE = (90, 140, 255)


def report(d, cx, cy, s, grade, col=C):
    """Hoja de libreta con nota."""
    w, h = s * 0.8, s
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 22, fill=col)
    for k in range(5):
        y = cy - h * 0.28 + k * h * 0.12
        d.line([S(cx - w * 0.38), S(y), S(cx + w * 0.1), S(y)], fill=(170, 170, 170), width=S(8))
    circle(d, cx + w * 0.24, cy + h * 0.18, s * 0.2, outline=R, width=10)
    text_c(d, cx + w * 0.24, cy + h * 0.18, grade, "A", s * 0.24, R, bg=col)


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 360, "¿TE SENTÍS SOLO", 135, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 520, "AUNQUE ESTÉS", 120, C, dur=0.25)
    pop_line(d, lt, 0.4, 540, 660, "CONECTADO?", 150, Y, dur=0.25)
    # una persona sola con burbujas de chat alrededor que se apagan
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        circle(d, 540, 1080, 220 * e, fill=K2)
        person(d, 540, 1100, 260 * e, C)
        for k, (dx, dy) in enumerate([(-300, -120), (300, -60), (-260, 170), (280, 200)]):
            fade = 1 - ease_in_out(prog(lt, 1.8 + k * 0.2, 0.5))
            if fade > 0.05:
                bubble(d, 540 + dx, 1080 + dy, 140 * e, mix(K, BLUE, fade))
    pop_line(d, lt, 2.8, 540, 1480, "NO SOS EL ÚNICO", 120, Y)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "EN TODO EL MUNDO", 110, C)
    pop_line(d, lt, 0.3, 540, 460, "1 DE CADA 6", 180, Y)
    slide_line(d, lt, 0.6, 540, 580, "personas se siente sola", 50, C, kind="SemiBold", dy=25)
    sep = ease_in_out(prog(lt, 1.6, 0.7))
    for i in range(6):
        p = back(prog(lt, 0.7 + i * 0.12, 0.3))
        if p <= 0.02: continue
        r, c = divmod(i, 3)
        x = 290 + c * 250
        y = 860 + r * 300
        lonely = (i == 5)
        if lonely:
            x += 90 * sep; y += 60 * sep
        person(d, x, y, 220 * p, Y if (lonely and sep > 0.3) else mix(K, C, 0.85))
    slide_line(d, lt, 2.6, 540, 1530, SRC, 34, G, kind="SemiBold", dy=20)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "Y EN LOS JÓVENES", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "de 13 a 29 años", 50, C, kind="SemiBold", dy=25)
    f = ease_out(prog(lt, 0.5, 1.3))
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        donut(d, 540, 800, 260 * e, 0.21 * f, f"{int(round(21 * f))}%" if lt > 0.5 else "", col=Y)
    pop_line(d, lt, 2.0, 540, 1170, "HASTA 1 DE CADA 5", 120, Y)
    slide_line(d, lt, 2.4, 540, 1300, "entre 17% y 21%: los adolescentes, los que más", 38, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1370, SRC, 34, G, kind="SemiBold", dy=20)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "NO ES SOLO", 130, C)
    pop_line(d, lt, 0.3, 540, 450, "TRISTEZA", 170, R)
    slide_line(d, lt, 0.6, 540, 570, "la OMS la vincula con más riesgo de:", 44, C, kind="SemiBold", dy=25)
    pill(d, lt, 0.9, 540, 720, 820, "PROBLEMAS DEL CORAZÓN", fill=K2, ink=C, size=42, h=100)
    pill(d, lt, 1.2, 540, 850, 820, "ACV Y DIABETES", fill=K2, ink=C, size=42, h=100)
    pill(d, lt, 1.5, 540, 980, 820, "DETERIORO COGNITIVO", fill=K2, ink=C, size=42, h=100)
    e = back(prog(lt, 2.1, 0.35))
    if e > 0.02:
        heart(d, 540, 1170, 130 * e, R)
    stamp(d, lt, 2.4, 540, 1350, 330, 85, "DOBLE RIESGO", fill=R, ink=C, size=105)
    slide_line(d, lt, 2.7, 540, 1480, "de caer en depresión", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1550, SRC, 34, G, kind="SemiBold", dy=20)


def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 300, "Y SE NOTA", 130, C)
    slide_line(d, lt, 0.3, 540, 440, "EN EL COLE", 130, Y)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        ang = math.sin(lt * 3) * 0.03
        report(d, 540, 820, 380 * e, "2")
    sx, sy = shake(lt, 1.8, 0.35, 16)
    pop_line(d, lt, 1.6, 540 + sx, 1150 + sy, "+22%", 200, R, dur=0.28)
    slide_line(d, lt, 2.1, 540, 1300, "más chance de peores notas", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.25, 540, 1365, "en adolescentes que se sienten solos", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1440, SRC, 34, G, kind="SemiBold", dy=20)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "EL AVISO:", 130, C)
    slide_line(d, lt, 0.2, 540, 480, "ESCRIBILE A", 140, Y)
    slide_line(d, lt, 0.35, 540, 630, "ALGUIEN HOY", 140, Y)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        phone(d, 540, 960, 270 * e, 400 * e, body=K2)
        for k in range(2):
            q = back(prog(lt, 0.9 + k * 0.4, 0.3))
            if q > 0.02:
                bx = 540 + (-30 if k == 0 else 30)
                rrect(d, bx - 80 * q, 880 + k * 110 - 35 * q, bx + 80 * q, 880 + k * 110 + 35 * q, 30, fill=Y if k == 0 else BLUE)
                if q > 0.8: text_c(d, bx, 880 + k * 110, "¿todo bien?" if k == 0 else "¡sí! ¿vos?", "Bold", 26, K if k == 0 else C, bg=Y if k == 0 else BLUE)
    slide_line(d, lt, 1.6, 540, 1240, "y guardá el celu cuando charlás con alguien", 42, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.9, 540, 1320, "si te pesa mucho, buscá ayuda", 42, Y, kind="SemiBold", dy=20)
    pop_line(d, lt, 2.3, 540, 1470, "¿A QUIÉN LE ESCRIBÍS?", 95, C)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.4, "thump"); ev(0.65, "shimmer")
for k in range(4): ev(1.8 + k * 0.2, "tap", -0.4 + k * 0.27)
ev(2.8, "pop")
ev(4.1, "tap"); ev(4.3, "thump"); ev(4.6, "tap")
for i in range(6): ev(4.7 + i * 0.12, "pop", -0.4 + i * 0.16)
ev(5.6, "whoosh", 0.5); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.3, "tap", 0.2)
for k in range(10): ev(8.5 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(10.0, "thump"); ev(10.4, "tap"); ev(10.6, "tap", 0.2)
ev(12.1, "tap"); ev(12.3, "thump"); ev(12.6, "tap")
ev(12.9, "pop", -0.3); ev(13.2, "pop", 0.3); ev(13.5, "pop", -0.1)
ev(14.1, "buzz"); ev(14.2, "whoosh"); ev(14.4, "stamp"); ev(14.8, "tap")
ev(16.1, "tap"); ev(16.3, "tap", 0.2); ev(16.4, "rustle"); ev(17.6, "thump"); ev(17.8, "stamp"); ev(18.1, "tap"); ev(18.25, "tap", 0.2)
ev(20.05, "tap"); ev(20.2, "pop", -0.2); ev(20.35, "pop", 0.2); ev(20.5, "pop")
ev(20.9, "ding", -0.2); ev(21.3, "ding", 0.2); ev(21.6, "tap"); ev(21.9, "tap"); ev(22.3, "pop")

if __name__ == "__main__":
    main(BEATS_EP)
