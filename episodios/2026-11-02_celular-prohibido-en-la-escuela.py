"""Short 2026-11-02 20:00 — Chicos y pantallas: cada vez más países sacan el celular del aula.
Fuentes: UNESCO, equipo del Informe GEM (seguimiento de leyes y políticas), citado por Business Today
(22/03/2026) y Europe 1: 114 sistemas educativos (~58% de los países) prohíben o restringen el celular en la
escuela; eran 24% en junio de 2023 (menos de 1 de cada 4) y 40% a comienzos de 2025.
Informe GEM 2023 (vía Foro Económico Mundial, 04/08/2023): tener el celular cerca afectó el aprendizaje en
14 países; un estudio citado: puede llevar hasta 20 minutos volver a concentrarse.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *


def school(d, cx, cy, s, col, ink=K):
    """Escuelita: techo, cuerpo, puerta y banderita."""
    d.polygon([(S(cx - s * 0.5), S(cy - s * 0.05)), (S(cx), S(cy - s * 0.42)), (S(cx + s * 0.5), S(cy - s * 0.05))], fill=col)
    d.rectangle([S(cx - s * 0.4), S(cy - s * 0.06), S(cx + s * 0.4), S(cy + s * 0.4)], fill=col)
    d.rectangle([S(cx - s * 0.09), S(cy + s * 0.12), S(cx + s * 0.09), S(cy + s * 0.4)], fill=ink)
    circle(d, cx, cy - s * 0.15, s * 0.08, fill=ink)
    d.line([S(cx), S(cy - s * 0.42), S(cx), S(cy - s * 0.62)], fill=col, width=max(2, int(S(s * 0.04))))
    d.polygon([(S(cx), S(cy - s * 0.62)), (S(cx + s * 0.2), S(cy - s * 0.56)), (S(cx), S(cy - s * 0.5))], fill=col)


def notebook(d, cx, cy, w, h):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 18, fill=C)
    for k in range(6):
        y = cy - h / 2 + 60 + k * (h - 90) / 6
        d.line([S(cx - w / 2 + 30), S(y), S(cx + w / 2 - 30), S(y)], fill=(170, 200, 230), width=S(4))
    d.line([S(cx - w / 2 + 70), S(cy - h / 2), S(cx - w / 2 + 70), S(cy + h / 2)], fill=(240, 130, 130), width=S(4))


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 320, "¿CELULAR", 150, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 480, "EN EL AULA?", 150, Y, dur=0.25)
    e = back(prog(lt, 0.4, 0.35))
    if e > 0.02:
        b = 1.0 if 0.8 < lt < 1.6 else 0.0
        phone(d, 540, 930, 300 * e, 540 * e, buzz=b, t=lt)
        if e > 0.9:
            bell(d, 540, 900, 120, Y)
            circle(d, 600, 840, 30, fill=R)
    p = ease_out(prog(lt, 1.7, 0.4))
    if p > 0:
        ban(d, 540, 930, 360, p, width=40)
    slide_line(d, lt, 2.4, 540, 1390, "cada vez más países dicen que no", 50, C, kind="SemiBold", dy=25)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "EN 2023", 120, C)
    pop_line(d, lt, 0.3, 540, 420, "MENOS DE 1 DE CADA 4", 105, Y)
    slide_line(d, lt, 0.5, 540, 530, "países lo prohibía o limitaba en la escuela", 44, C, kind="SemiBold", dy=25)
    # grilla 5x5 de escuelas: 6 se marcan (24%)
    lit = {1, 7, 12, 15, 19, 23}
    for k in range(25):
        r, c = divmod(k, 5)
        x, y = 220 + c * 160, 690 + r * 150
        e = back(prog(lt, 0.6 + k * 0.025, 0.25))
        if e > 0.02:
            on = k in lit and lt > 1.5 + sorted(lit).index(k) * 0.12 if k in lit else False
            school(d, x, y, 110 * e, Y if on else (75, 75, 75))
    q = prog(lt, 2.4, 0.3)
    if q > 0:
        pill(d, lt, 2.4, 540, 1490, 300, "24%", fill=Y, ink=K, size=56, h=100)
    slide_line(d, lt, 2.6, 540, 1580, "UNESCO, Informe GEM (junio 2023)", 32, G, kind="SemiBold", dy=20)


def bars(d, lt, vals, t0s, x0=170, base=1300, hmax=780, labels=("2023", "2025", "2026")):
    d.line([S(110), S(base), S(970), S(base)], fill=(90, 90, 90), width=S(6))
    for k, (v, tt) in enumerate(zip(vals, t0s)):
        if v is None: continue
        p = ease_out(prog(lt, tt, 0.7))
        x = x0 + k * 280
        h = hmax * v / 100 * p
        col = Y if k == len([u for u in vals if u is not None]) - 1 else (95, 95, 95)
        if p > 0.01:
            rrect(d, x, base - h, x + 180, base, 20, fill=col)
            text_c(d, x + 90, base - h - 60, f"{int(round(v * p))}%", "A", 80, C)
        text_c(d, x + 90, base + 55, labels[k], "Bold", 44, C)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 280, "EN 2025", 120, C)
    pop_line(d, lt, 0.3, 540, 420, "YA ERAN 4 DE CADA 10", 105, Y)
    bars(d, lt, [24, 40, None], [0.0, 0.7])
    slide_line(d, lt, 2.2, 540, 1460, "y siguió creciendo...", 50, C, kind="SemiBold", dy=25)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.05, 540, 280, "HOY", 120, C)
    sx, sy = shake(lt, 1.3, 0.35, 16)
    bars(d, lt, [24, 40, 58], [-5, -5, 0.4])
    stamp(d, lt, 1.4, 540 + sx, 440 + sy, 400, 90, "CASI 6 DE CADA 10", fill=R, ink=C, size=110)
    slide_line(d, lt, 2.0, 540, 1460, "114 sistemas educativos lo prohíben o limitan", 40, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1530, "UNESCO, Informe GEM (marzo 2026)", 32, G, kind="SemiBold", dy=20)


def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 280, "¿POR QUÉ?", 120, C)
    slide_line(d, lt, 0.3, 540, 410, "SOLO TENERLO CERCA DISTRAE", 90, Y)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        notebook(d, 400, 800, 420 * e, 520 * e)
        bz = 1.0 if 1.0 < lt < 1.7 else 0.0
        phone(d, 760, 840, 170 * e, 300 * e, buzz=bz, t=lt)
    # reloj que corre 20 min
    q = prog(lt, 1.6, 1.2)
    if lt > 1.5:
        clock(d, 540, 1230, 120, q, turns=1, fill_deg=120)
        pop_line(d, lt, 1.6, 540, 1430, "HASTA 20 MIN", 110, C)
        slide_line(d, lt, 1.9, 540, 1530, "para volver a concentrarte", 46, C, kind="SemiBold", dy=25)
        slide_line(d, lt, 2.1, 540, 1600, "estudio citado por UNESCO, Informe GEM 2023", 32, G, kind="SemiBold", dy=20)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "¿EN TU ESCUELA", 130, C)
    slide_line(d, lt, 0.25, 540, 480, "SE PUEDE USAR?", 130, Y)
    for k, (lab, col, ink) in enumerate([("SÍ", GREEN, K), ("NO", R, C)]):
        e = back(prog(lt, 0.7 + k * 0.25, 0.3))
        if e > 0.02:
            x = 330 + k * 420
            circle(d, x, 820, 150 * e, fill=col)
            text_c(d, x, 815, lab, "A", 130 * e, ink, bg=col)
    slide_line(d, lt, 1.5, 540, 1080, "comentá y mandáselo a alguien", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.7, 540, 1150, "que tenga hijos en la escuela", 48, C, kind="SemiBold", dy=25)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.4, "pop"); ev(0.8, "buzz"); ev(1.3, "ding", 0.2)
ev(1.7, "swipe"); ev(2.05, "thump"); ev(2.4, "tap")
ev(4.1, "tap"); ev(4.3, "pop"); ev(4.5, "tap")
for k in range(0, 25, 5): ev(4.6 + k * 0.025, "click")
for k in range(6): ev(5.5 + k * 0.12, "pop", -0.5 + k * 0.2)
ev(6.4, "thump"); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.3, "pop")
for k in range(10): ev(8.0 + k * 0.07, "tick", -0.3)
for k in range(10): ev(8.7 + k * 0.07, "tick", 0.1)
ev(10.2, "tap")
ev(12.05, "tap")
for k in range(12): ev(12.4 + k * 0.06, "tick", 0.4)
ev(13.2, "stamp"); ev(14.0, "tap"); ev(14.2, "tap")
ev(16.1, "tap"); ev(16.3, "tap"); ev(16.5, "rustle"); ev(17.0, "buzz", 0.4)
ev(17.6, "pop")
for k in range(10): ev(17.7 + k * 0.12, "tick")
ev(17.9, "tap"); ev(18.1, "tap")
ev(20.05, "tap"); ev(20.25, "tap"); ev(20.7, "pop", -0.4); ev(20.95, "pop", 0.4); ev(21.5, "ding"); ev(21.7, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
