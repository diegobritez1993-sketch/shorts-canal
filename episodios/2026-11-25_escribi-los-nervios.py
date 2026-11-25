"""Short 2026-11-25 20:00 — ¿Nervios antes de un examen? Escribilos 10 minutos (Ramirez y Beilock, Science 2011)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Fuente: Ramirez y Beilock, Univ. de Chicago, Science 2011"

def sheet(d, cx, cy, w, h, lines=0.0, scrib=False, t=0.0):
    """Hoja con renglones; lines 0..1 = cuánto se escribió."""
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 18, fill=C)
    n = 7
    for i in range(n):
        y = cy - h / 2 + h * (0.18 + i * 0.11)
        d.line([S(cx - w * 0.38), S(y), S(cx + w * 0.38), S(y)], fill=(210, 205, 195), width=S(3))
        fill_i = clamp(lines * n - i)
        if fill_i > 0:
            x0 = cx - w * 0.36
            x1 = x0 + (w * 0.72) * fill_i * (0.75 if i % 3 == 2 else 1.0)
            pts = []
            steps = max(2, int((x1 - x0) / 10))
            for k in range(steps + 1):
                x = lerp(x0, x1, k / steps)
                pts.append((S(x), S(y - 14 + 7 * math.sin(k * 1.7 + i))))
            d.line(pts, fill=(60, 60, 60), width=S(5))

def pencil(d, x, y, s):
    """Lápiz inclinado con la punta en (x, y)."""
    a = math.radians(-50)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    L, Wd = s, s * 0.16
    tip = (x, y)
    b0 = (x + ux * L * 0.18, y + uy * L * 0.18)
    body = [(b0[0] + px * Wd, b0[1] + py * Wd), (b0[0] - px * Wd, b0[1] - py * Wd),
            (b0[0] - px * Wd + ux * L, b0[1] - py * Wd + uy * L), (b0[0] + px * Wd + ux * L, b0[1] + py * Wd + uy * L)]
    d.polygon([(S(a_), S(b_)) for a_, b_ in body], fill=Y)
    d.polygon([(S(tip[0]), S(tip[1])), (S(body[0][0]), S(body[0][1])), (S(body[1][0]), S(body[1][1]))], fill=(230, 190, 140))
    e0 = (b0[0] + ux * L, b0[1] + uy * L)
    eraser = [(e0[0] + px * Wd, e0[1] + py * Wd), (e0[0] - px * Wd, e0[1] - py * Wd),
              (e0[0] - px * Wd + ux * L * 0.15, e0[1] - py * Wd + uy * L * 0.15), (e0[0] + px * Wd + ux * L * 0.15, e0[1] + py * Wd + uy * L * 0.15)]
    d.polygon([(S(a_), S(b_)) for a_, b_ in eraser], fill=(255, 130, 150))

def arrow(d, cx, cy, s, up, col):
    sg = -1 if up else 1
    d.rectangle([S(cx - s * 0.14), S(cy - s * 0.4), S(cx + s * 0.14), S(cy + s * 0.4)], fill=col)
    d.polygon([(S(cx - s * 0.4), S(cy + sg * s * 0.25)), (S(cx + s * 0.4), S(cy + sg * s * 0.25)), (S(cx), S(cy + sg * s * 0.75))], fill=col)

def grade(d, cx, cy, r, txt, col, e):
    if e <= 0.02: return
    circle(d, cx, cy, r * e, outline=col, width=12)
    text_c(d, cx, cy, txt, "A", int(r * 0.95 * e) + 1, col)

def b1(d, t):
    sx, sy = shake(t, 0.3, 3.5, 10)
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        sheet(d, 540 + sx, 560 + sy, 400 * e, 500 * e)
        text_c(d, 540 + sx, 410 + sy, "EXAMEN", "Black", int(54 * e) + 1, K, bg=C)
    stamp(d, t, 1.7, 790, 420, 70, 90, "!", fill=R, ink=C, size=150)
    pop_line(d, t, 0.0, 540, 1000, "¿TE BLOQUEÁS", 150, C)
    pop_line(d, t, 0.3, 540, 1150, "EN LOS EXÁMENES?", 130, Y)
    slide_line(d, t, 1.2, 540, 1290, "estudiaste, pero los nervios", 50, C, kind="SemiBold", dy=25)
    slide_line(d, t, 1.35, 540, 1355, "te dejan la mente en blanco", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "PROBARON ALGO", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "SÚPER SIMPLE", 140, Y)
    e = back(prog(lt, 0.5, 0.35))
    wp = prog(lt, 0.8, 2.6)
    if e > 0.02:
        sheet(d, 400, 800, 360 * e, 440 * e, lines=wp)
        n = clamp(wp * 7)
        i = min(6, int(n))
        frac = n - i
        py = 800 - 220 + 440 * (0.18 + i * 0.11) - 14
        px = 400 - 360 * 0.36 + 360 * 0.72 * frac
        if lt > 0.8:
            pencil(d, px, py, 150 * e)
    e2 = back(prog(lt, 0.7, 0.35))
    if e2 > 0.02:
        clock(d, 810, 740, 120 * e2, prog(lt, 0.8, 2.6), turns=1, fill_deg=360)
        text_c(d, 810, 920, "10 MIN", "A", int(80 * e2) + 1, Y)
    slide_line(d, lt, 1.6, 540, 1110, "escribir lo que te preocupa", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.75, 540, 1175, "justo antes de la prueba", 50, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "20 UNIVERSITARIOS", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "EXAMEN DE MATE", 130, Y)
    # presión: plata, cámara, equipo
    items = [("$", "premio"), ("REC", "cámara"), ("2", "en equipo")]
    for i, (sym, lab) in enumerate(items):
        e = back(prog(lt, 0.7 + i * 0.3, 0.35))
        if e > 0.02:
            x = 230 + i * 310
            circle(d, x, 720, 115 * e, fill=K2, outline=R if i == 1 else C, width=8)
            if sym == "REC":
                circle(d, x - 45 * e, 720, 18 * e, fill=R)
                text_c(d, x + 18 * e, 720, "REC", "Black", int(40 * e) + 1, C, bg=K2)
            elif sym == "2":
                person(d, x - 30 * e, 735, 110 * e, C); person(d, x + 30 * e, 735, 110 * e, Y)
            else:
                text_c(d, x, 715, "$", "A", int(130 * e) + 1, GREEN, bg=K2)
            text_c(d, x, 880, lab, "SemiBold", 42, C)
    pop_line(d, lt, 1.9, 540, 1060, "MUCHA PRESIÓN", 140, R)
    slide_line(d, lt, 2.4, 540, 1190, "la mitad escribió 10 min, la otra esperó", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1290, SRC, 32, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "¿RESULTADO?", 140, C)
    e1 = back(prog(lt, 0.5, 0.35)); e2 = back(prog(lt, 1.4, 0.35))
    if e1 > 0.02:
        rrect(d, 90, 460, 520, 1100, 44, fill=K2)
        text_c(d, 305, 540, "SIN ESCRIBIR", "Black", 44, C, bg=K2)
        arrow(d, 305, 740, 190 * e1, up=False, col=R)
        text_c(d, 305, 990, f"-{round(12 * clamp(prog(lt, 0.6, 0.7)))}%", "A", int(150 * e1) + 1, R, bg=K2)
    if e2 > 0.02:
        rrect(d, 560, 460, 990, 1100, 44, fill=K2)
        text_c(d, 775, 540, "ESCRIBIENDO", "Black", 44, C, bg=K2)
        arrow(d, 775, 760, 190 * e2, up=True, col=GREEN)
        text_c(d, 775, 990, f"+{round(5 * clamp(prog(lt, 1.5, 0.6)))}%", "A", int(150 * e2) + 1, GREEN, bg=K2)
    slide_line(d, lt, 2.3, 540, 1200, "de aciertos en la segunda prueba", 48, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.6, 540, 1330, 960, "LOS QUE NO ESCRIBIERON SE TRABARON", fill=Y, ink=K, size=34, h=90)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "Y EN EL COLE", 130, C)
    slide_line(d, lt, 0.3, 540, 410, "TAMBIÉN", 140, Y)
    slide_line(d, lt, 0.6, 540, 520, "chicos de 9.º grado muy nerviosos, examen final", 40, C, kind="SemiBold", dy=20)
    grade(d, 300, 800, 170, "B–", G, back(prog(lt, 0.9, 0.35)))
    grade(d, 780, 800, 170, "B+", GREEN, back(prog(lt, 1.6, 0.35)))
    text_c(d, 300, 1020, "no escribieron", "SemiBold", 42, C) if lt > 1.1 else None
    text_c(d, 780, 1020, "escribieron", "SemiBold", 42, C) if lt > 1.8 else None
    p = ease_out(prog(lt, 1.3, 0.3))
    if p > 0:
        d.line([S(500), S(800), S(lerp(500, 570, p)), S(800)], fill=Y, width=S(14))
    sx, sy = shake(lt, 2.4, 0.3, 12)
    pop_line(d, lt, 2.2, 540 + sx, 1180 + sy, "CASI 1 NOTA MÁS", 130, Y, dur=0.28)
    slide_line(d, lt, 2.6, 540, 1300, "(notas de EE.UU.: B+ es mejor que B–)", 38, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 300, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 450, "VACIÁ LA CABEZA", 140, Y)
    slide_line(d, lt, 0.5, 540, 580, "EN UN PAPEL", 120, C)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        sheet(d, 540, 820, 260 * e, 300 * e, lines=prog(lt, 0.8, 1.6))
    pill(d, lt, 1.4, 540, 1050, 820, "10 MINUTOS ANTES DEL EXAMEN", fill=Y, ink=K, size=38, h=100)
    slide_line(d, lt, 1.9, 540, 1190, "si los nervios te ganan siempre,", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.05, 540, 1250, "hablalo con alguien de confianza", 44, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop"); ev(0.05, "thump"); ev(0.3, "pop", 0.3); ev(0.4, "buzz"); ev(1.2, "tap"); ev(1.35, "tap"); ev(1.5, "whoosh"); ev(1.7, "stamp")
ev(4.1, "tap"); ev(4.3, "pop"); ev(4.5, "pop", -0.3); ev(4.7, "pop", 0.3)
for k in range(9): ev(4.9 + k * 0.28, "rustle", -0.3 + (k % 3) * 0.3)
ev(5.6, "tap"); ev(5.75, "tap"); ev(7.4, "ding")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.7, "pop", -0.5); ev(9.0, "pop"); ev(9.3, "pop", 0.5); ev(9.9, "thump"); ev(10.4, "tap"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.5, "pop", -0.4)
for k in range(6): ev(12.6 + k * 0.1, "tick", -0.4)
ev(13.0, "thump"); ev(13.4, "pop", 0.4)
for k in range(5): ev(13.5 + k * 0.11, "tick", 0.4)
ev(14.0, "shimmer"); ev(14.3, "tap"); ev(14.6, "pop")
ev(16.1, "tap"); ev(16.3, "tap"); ev(16.6, "tap"); ev(16.9, "pop", -0.4); ev(17.3, "whoosh"); ev(17.6, "pop", 0.4); ev(17.7, "ding"); ev(18.2, "stamp"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.5, "tap"); ev(20.7, "pop")
for k in range(5): ev(20.8 + k * 0.3, "rustle", 0.0)
ev(21.4, "pop"); ev(21.9, "tap"); ev(22.05, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
