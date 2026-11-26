"""Short 2026-11-26 15:00 — ¿Una red social puede cambiar tu ánimo? El experimento de contagio emocional (Kramer, Guillory y Hancock, PNAS 2014)."""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SRC = "Kramer, Guillory y Hancock, PNAS 2014"
BLUE = (90, 140, 255)

def face(d, cx, cy, r, mood, col=Y, ink=K):
    """Carita: mood 1 = feliz, -1 = triste."""
    circle(d, cx, cy, r, fill=col)
    circle(d, cx - r * 0.35, cy - r * 0.22, r * 0.12, fill=ink)
    circle(d, cx + r * 0.35, cy - r * 0.22, r * 0.12, fill=ink)
    w = r * 0.5
    if mood >= 0:
        d.arc([S(cx - w), S(cy - w * 0.6), S(cx + w), S(cy + w * 0.9)], 20, 160, fill=ink, width=int(S(max(3, r * 0.1))))
    else:
        d.arc([S(cx - w), S(cy + w * 0.35), S(cx + w), S(cy + w * 1.6)], 200, 340, fill=ink, width=int(S(max(3, r * 0.1))))

def post(d, x0, y, w, h, mood, alpha=1.0, dx=0):
    """Tarjeta de publicación con carita y renglones."""
    if alpha <= 0.02: return
    col = mix(K, K2, alpha)
    rrect(d, x0 + dx, y, x0 + w + dx, y + h, 26, fill=col, outline=mix(K, (70, 70, 70), alpha), width=3)
    fc = mix(K, Y if mood > 0 else BLUE, alpha)
    face(d, x0 + dx + h * 0.5, y + h / 2, h * 0.3, mood, col=fc, ink=col)
    for i, fr in enumerate((0.9, 0.6)):
        yy = y + h * (0.38 + i * 0.26)
        rrect(d, x0 + dx + h, yy - 9, x0 + dx + h + (w - h - 40) * fr, yy + 9, 9, fill=mix(K, (110, 110, 110), alpha))

def b1(d, t):
    # feed que baja solo, caritas que cambian
    e = ease_out(prog(t, 0.0, 0.4))
    if e > 0.02:
        x0, x1, y0, y1 = 300, 780, 240, 840
        rrect(d, x0, y0, x1, y1, 60, fill=K2, outline=C, width=8)
        off = (t * 160) % 140
        for k in range(6):
            y = y0 + 50 + k * 140 - off
            if y0 + 30 < y < y1 - 140:
                post(d, x0 + 30, y, 420, 115, 1 if k % 2 == 0 else -1, alpha=e)
    pop_line(d, t, 0.0, 540, 1010, "¿UNA RED SOCIAL", 140, C)
    pop_line(d, t, 0.3, 540, 1170, "PUEDE CAMBIAR", 140, C)
    pop_line(d, t, 0.6, 540, 1340, "TU HUMOR?", 170, Y)
    slide_line(d, t, 1.5, 540, 1500, "lo probaron con gente real", 50, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "EN 2012, FACEBOOK", 120, C)
    slide_line(d, lt, 0.3, 540, 420, "HIZO UN EXPERIMENTO", 100, Y)
    # muchedumbre de puntitos
    rnd = random.Random(5)
    n = int(220 * ease_out(prog(lt, 0.5, 1.4)))
    for k in range(n):
        x, y = rnd.uniform(110, 970), rnd.uniform(560, 950)
        person(d, x, y, 46, mix(K, C, 0.35 + 0.4 * rnd.random()))
    cnt = 689003 * ease_out(prog(lt, 0.5, 1.6))
    if lt > 0.5:
        sx, sy = shake(lt, 2.1, 0.3, 12)
        text_c(d, 540 + sx, 1110 + sy, fmt_num(cnt), "A", 210, Y)
    pop_line(d, lt, 2.0, 540, 1280, "USUARIOS", 110, C)
    slide_line(d, lt, 2.4, 540, 1410, "durante 1 semana, solo por aceptar", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1468, "las condiciones de uso", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1560, SRC, 36, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "LES TOCARON", 130, C)
    slide_line(d, lt, 0.3, 540, 430, "EL INICIO", 150, Y)
    # dos columnas de feed: a la izq se van las felices, a la der las tristes
    for side, mood, lab, tt in ((-1, 1, "MENOS POSTS FELICES", 1.0), (1, -1, "MENOS POSTS TRISTES", 1.6)):
        cx = 540 + side * 250
        e = ease_out(prog(lt, 0.4, 0.4))
        for k in range(4):
            m = mood if k % 2 == 0 else -mood
            y = 560 + k * 140
            gone = ease_in_out(prog(lt, tt + k * 0.12, 0.45)) if m == mood else 0
            post(d, cx - 200, y, 400, 115, m, alpha=e * (1 - gone), dx=side * 300 * gone)
        pill(d, lt, tt + 0.6, cx, 1180, 440, lab, fill=Y if mood > 0 else BLUE, ink=K, size=34, h=90)
    slide_line(d, lt, 2.6, 540, 1330, "el sistema escondía algunos posts", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.75, 540, 1390, "de su inicio por una semana", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "¿Y QUÉ PASÓ?", 140, C)
    # flecha feed -> persona -> carita
    e = back(prog(lt, 0.3, 0.4))
    if e > 0.02:
        mood = -1 if lt < 2.2 else 1
        face(d, 300, 640, 120 * e, mood, col=BLUE if mood < 0 else Y)
        e2 = back(prog(lt, 1.15, 0.35))
        if e2 > 0.02: face(d, 780, 640, 120 * e2, mood, col=BLUE if mood < 0 else Y)
        p = ease_in_out(prog(lt, 0.6, 0.6))
        if p > 0:
            d.line([S(440), S(640), S(lerp(440, 630, p)), S(640)], fill=C, width=S(14))
            if p > 0.95:
                d.polygon([(S(650), S(640)), (S(615), S(612)), (S(615), S(668))], fill=C)
    stamp(d, lt, 1.0, 540, 930, 360, 105, "SE CONTAGIA", fill=Y, ink=K, size=130)
    slide_line(d, lt, 1.5, 540, 1130, "con menos posts felices,", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.6, 540, 1192, "escribían más cosas negativas", 48, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 2.2, 540, 1320, "Y AL REVÉS", 110, Y)
    slide_line(d, lt, 2.6, 540, 1450, SRC, 36, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "EL EFECTO FUE", 120, C)
    pop_line(d, lt, 0.3, 540, 420, "CHIQUITO...", 150, C)
    # una gota que se multiplica en una grilla
    n = int(1 + 299 * ease_in_out(prog(lt, 1.0, 1.4)) ** 2)
    for k in range(n):
        gx, gy = k % 20, k // 20
        circle(d, 160 + gx * 40, 560 + gy * 36, 13, fill=Y if k == 0 else mix(K, Y, 0.75))
    pop_line(d, lt, 1.7, 540, 1170, "...PERO EN UNA RED GIGANTE", 92, Y)
    slide_line(d, lt, 2.1, 540, 1290, "suma cientos de miles", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1352, "de emociones por día", 50, C, kind="SemiBold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "FIJATE CÓMO", 140, Y)
    slide_line(d, lt, 0.45, 540, 630, "TE DEJA EL FEED", 140, Y)
    e = back(prog(lt, 0.7, 0.4))
    if e > 0.02:
        face(d, 540, 870, 120 * e, 1 if lt < 1.4 else -1, col=Y if lt < 1.4 else BLUE)
    slide_line(d, lt, 1.4, 540, 1070, "si salís peor de lo que entraste,", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.5, 540, 1130, "cerralo y hacé otra cosa", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.0, 540, 1290, 780, "¿TE PASÓ? SÍ O NO", fill=Y, ink=K, size=50, h=110)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "shimmer"); ev(0.0, "pop", -0.3); ev(0.3, "pop", 0.3); ev(0.6, "thump"); ev(1.5, "tap")
ev(0.2, "swipe", 0.4)
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3)
for k in range(12): ev(4.5 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(6.0, "stamp"); ev(6.1, "thump"); ev(6.4, "tap"); ev(6.7, "tap", 0.2)
ev(8.1, "tap"); ev(8.3, "pop")
for k in range(2): ev(9.0 + k * 0.24, "whoosh", -0.6); ev(9.6 + k * 0.24, "whoosh", 0.6)
ev(9.6, "pop", -0.4); ev(10.2, "pop", 0.4); ev(10.6, "tap"); ev(10.75, "tap")
ev(12.1, "tap"); ev(12.3, "pop", -0.3); ev(12.6, "swipe"); ev(12.8, "stamp"); ev(13.5, "tap"); ev(13.6, "tap")
ev(14.2, "pop"); ev(14.2, "shimmer"); ev(14.6, "tap")
ev(16.1, "tap"); ev(16.3, "pop")
for k in range(10): ev(17.0 + k * 0.13, "tick", 0.3 if k % 2 else -0.3)
ev(17.7, "thump"); ev(18.1, "tap"); ev(18.2, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.7, "pop"); ev(21.4, "tap"); ev(21.5, "tap"); ev(22.0, "ding")

if __name__ == "__main__":
    main(BEATS_EP)
