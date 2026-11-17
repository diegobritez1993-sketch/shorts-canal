"""Short 2026-11-17 20:00 — Mente y emociones: anotar lo que agradecés (diario de gratitud).

Fuente:
- Emmons y McCullough, "Counting blessings versus burdens", J. Personality and Social Psychology, 2003.
  Estudio 1: ~200 universitarios, 10 semanas, un diario por semana. Tres grupos: hasta 5 cosas por las que
  estaban agradecidos / molestias / cosas que pasaron (neutral).
- Resultados del grupo gratitud (vía Psychology Today, "How gratitude leads to a happier life", nov. 2015):
  se sintieron mejor con su vida en general, más optimistas con la semana siguiente, menos síntomas físicos,
  más tiempo de ejercicio.
- "Casi 1,5 horas más de ejercicio por semana" (Psychology Today, "Can being grateful motivate us to exercise more?", dic. 2020).
- Tono: no es magia ni reemplaza ayuda profesional.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

def notebook(d, cx, cy, w, h, lines=5, filled=0.0, t=0.0, col=C, ink=Y):
    """Cuaderno con espiral y renglones; filled 0..lines = renglones escritos con tilde."""
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 26, fill=col)
    for k in range(7):
        yy = cy - h / 2 + 40 + k * (h - 80) / 6
        circle(d, cx - w / 2, yy, 16, fill=K, outline=(150, 150, 150), width=5)
    for k in range(lines):
        yy = cy - h / 2 + h * 0.18 + k * h * 0.16
        x0 = cx - w / 2 + w * 0.2
        d.line([S(x0), S(yy + 22), S(cx + w / 2 - 40), S(yy + 22)], fill=(200, 196, 186), width=SW(3))
        q = clamp(filled - k)
        if q > 0:
            # tilde
            d.line([S(x0), S(yy), S(x0 + 18), S(yy + 16)], fill=GREEN, width=SW(9))
            d.line([S(x0 + 18), S(yy + 16), S(x0 + 44), S(yy - 16)], fill=GREEN, width=SW(9))
            # garabato escrito
            L = (w * 0.55) * q
            pts = []
            for i in range(int(L / 8) + 1):
                xx = x0 + 64 + i * 8
                pts += [S(xx), S(yy + math.sin(i * 1.3 + k) * 8)]
            if len(pts) >= 4:
                d.line(pts, fill=(60, 60, 60), width=SW(6))

def pencil(d, x, y, s, col=Y):
    a = -0.8
    ca, sa = math.cos(a), math.sin(a)
    def P(u, v): return (S(x + u * ca - v * sa), S(y + u * sa + v * ca))
    d.polygon([P(0, 0), P(s * 0.18, -s * 0.07), P(s, -s * 0.07), P(s, s * 0.07), P(s * 0.18, s * 0.07)], fill=col)
    d.polygon([P(0, 0), P(s * 0.08, -s * 0.03), P(s * 0.08, s * 0.03)], fill=K)
    d.polygon([P(s, -s * 0.07), P(s * 1.12, -s * 0.07), P(s * 1.12, s * 0.07), P(s, s * 0.07)], fill=R)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 400, "¿TE ACORDÁS", 175, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 580, "SOLO DE", 175, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 770, "LO MALO?", 200, R, dur=0.25)
    # nubecitas rojas de "malo" que se van tapando con una amarilla
    for k in range(5):
        p = prog(t, 0.8 + k * 0.12, 0.25)
        if p > 0:
            circle(d, 220 + k * 160, 1100 + (k % 2) * 60, 55 * back(p), fill=R)
    e = back(prog(t, 1.9, 0.4))
    if e > 0.02:
        circle(d, 540, 1130, 150 * e, fill=Y)
        text_c(d, 540, 1130, "+", "A", int(200 * e) + 4, K, bg=Y)
    slide_line(d, t, 2.4, 540, 1400, "hay un hábito de 1 vez por semana", 48, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.6, 540, 1465, "que se probó en un experimento", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "CASI 200", 170, Y)
    slide_line(d, lt, 0.3, 540, 450, "UNIVERSITARIOS", 120, C)
    slide_line(d, lt, 0.5, 540, 560, "escribieron un diario 1 vez por semana", 44, C, kind="SemiBold", dy=20)
    # calendario de 10 semanas que se va tildando
    for k in range(10):
        p = prog(lt, 0.8 + k * 0.15, 0.2)
        i, j = k % 5, k // 5
        x, y = 180 + i * 180, 760 + j * 200
        rrect(d, x - 70, y - 70, x + 70, y + 70, 24, fill=K2)
        text_c(d, x, y - 42, f"S{k + 1}", "Black", 26, G, bg=K2)
        if p > 0:
            e = back(p)
            circle(d, x, y + 18, 34 * e, fill=Y)
    sx, sy = shake(lt, 2.5, 0.3, 12)
    pop_line(d, lt, 2.4, 540 + sx, 1250 + sy, "10 SEMANAS", 150, C, dur=0.25)
    slide_line(d, lt, 2.7, 540, 1400, "Emmons y McCullough, J. Pers. Soc. Psychol. 2003", 34, G, kind="SemiBold", dy=20)

GROUPS = [("LO QUE", "AGRADECÉS", Y), ("LAS", "MOLESTIAS", R), ("LO QUE", "PASÓ Y YA", (130, 130, 130))]

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "3 GRUPOS", 160, C)
    slide_line(d, lt, 0.3, 540, 430, "cada uno anotaba hasta 5 cosas:", 46, C, kind="SemiBold", dy=20)
    for k, (a, b, col) in enumerate(GROUPS):
        p = prog(lt, 0.7 + k * 0.5, 0.35)
        if p <= 0: continue
        e = back(p)
        x = 200 + k * 340
        notebook(d, x, 820, 230 * e, 300 * e, lines=5, filled=0, col=col)
        text_c(d, x, 1050, a, "Black", 36, C, alpha=clamp(p * 2))
        text_c(d, x, 1100, b, "Black", 40, col, alpha=clamp(p * 2))
    # el amarillo se destaca
    q = ease_out(prog(lt, 2.4, 0.4))
    if q > 0:
        rrect(d, 200 - 150, 620, 200 + 150, 1150, 34, outline=mix(K, Y, q), width=8)
    slide_line(d, lt, 2.6, 540, 1300, "¿a quién le fue mejor?", 56, Y, kind="Bold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 275, "LOS QUE ANOTARON", 105, C)
    slide_line(d, lt, 0.3, 540, 415, "LO QUE AGRADECÍAN:", 105, Y)
    pill(d, t, 12.7, 540, 580, 820, "MÁS OPTIMISTAS CON LA SEMANA", fill=K2, ink=C, size=42, h=110)
    pill(d, t, 13.1, 540, 720, 820, "MENOS SÍNTOMAS FÍSICOS", fill=K2, ink=C, size=42, h=110)
    pill(d, t, 13.5, 540, 860, 820, "MEJOR CON SU VIDA", fill=K2, ink=C, size=42, h=110)
    v = 1.5 * ease_out(prog(lt, 2.0, 0.9))
    if lt > 2.0:
        sx, sy = shake(lt, 2.9, 0.3, 14)
        text_c(d, 540 + sx, 1110 + sy, "+" + f"{v:.1f}".replace(".", ",") + " H", "A", 230, Y)
        pop_line(d, lt, 2.6, 540, 1270, "DE EJERCICIO POR SEMANA (CASI)", 64, C)
    slide_line(d, lt, 3.0, 540, 1370, "Emmons y McCullough 2003, vía Psychology Today", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "CÓMO HACERLO", 140, C)
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        notebook(d, 540, 760, 560 * e, 600 * e, lines=5, filled=5 * ease_in_out(prog(lt, 0.8, 2.0)), col=C)
    if lt > 0.8:
        k = min(4.0, 5 * ease_in_out(prog(lt, 0.8, 2.0)))
        pencil(d, 540 - 280 * 0.6 + 64 + 300 * (k % 1), 760 - 300 + 600 * 0.18 + int(k) * 600 * 0.16 - 10, 200)
    pill(d, t, 17.4, 540, 1180, 640, "1 VEZ POR SEMANA", fill=Y, ink=K, size=46, h=110)
    pill(d, t, 17.9, 540, 1320, 640, "HASTA 5 COSAS", fill=Y, ink=K, size=46, h=110)
    slide_line(d, lt, 2.4, 540, 1460, "chiquitas valen: un mate, un mensaje, el sol", 42, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "OJO: NO ES MAGIA", 120, C)
    slide_line(d, lt, 0.4, 540, 420, "si estás mal seguido, hablalo con alguien", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 0.5, 540, 475, "o buscá ayuda profesional", 42, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 0.8, 0.4))
    if e > 0.02:
        heart(d, 540, 760, 260 * e, Y)
    pop_line(d, lt, 1.4, 540, 1020, "¿QUÉ ANOTARÍAS", 120, Y)
    pop_line(d, lt, 1.6, 540, 1160, "HOY?", 150, Y)
    slide_line(d, lt, 2.2, 540, 1300, "dejalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
for k in range(5): ev(0.8 + k * 0.12, "pop", -0.5 + k * 0.25)
ev(1.9, "ding"); ev(2.4, "tap"); ev(2.6, "tap")
ev(4.1, "tap"); ev(4.3, "tap"); ev(4.5, "tap")
for k in range(10): ev(4.8 + k * 0.15, "tick", -0.4 + k * 0.09)
ev(6.4, "pop"); ev(6.5, "stamp"); ev(6.7, "tap")
ev(8.1, "tap"); ev(8.3, "tap")
for k in range(3): ev(8.7 + k * 0.5, "pop", -0.4 + k * 0.4); ev(8.72 + k * 0.5, "rustle", -0.4 + k * 0.4)
ev(10.4, "click"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.3, "tap"); ev(12.7, "pop", -0.3); ev(13.1, "pop", 0.3); ev(13.5, "pop", -0.3)
for k in range(8): ev(14.0 + k * 0.1, "tick")
ev(14.6, "pop"); ev(14.9, "stamp"); ev(15.0, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.8, "rustle"); ev(17.4, "pop", -0.2); ev(17.9, "pop", 0.2); ev(18.4, "tap")
ev(20.1, "tap"); ev(20.4, "tap"); ev(20.8, "pop"); ev(20.85, "shimmer"); ev(21.4, "pop"); ev(21.6, "thump"); ev(22.2, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
