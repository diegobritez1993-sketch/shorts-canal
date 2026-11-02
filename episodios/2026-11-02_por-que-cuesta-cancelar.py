"""Short 2026-11-02 15:00 — Cómo te enganchan las apps: por qué cuesta tanto cancelar una suscripción.
Fuentes: AP (ABC News, 25/09/2025): Amazon acordó pagar US$ 2.500 millones a la FTC (US$ 1.000 M de multa
civil, la mayor de la historia de la FTC, + US$ 1.500 M en reembolsos). El trámite para cancelar Prime se
llamaba internamente "Iliad" (por la Ilíada, el poema sobre el sitio de Troya) y pedía confirmar en tres
páginas. El acuerdo prohíbe frases como "No thanks, I don't want free shipping". Amazon no admitió culpa.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *


def cursor(d, x, y, s=1.0, col=C):
    """Flechita de mouse."""
    pts = [(0, 0), (0, 62), (16, 48), (28, 74), (40, 68), (28, 43), (50, 43)]
    d.polygon([(S(x + px * s), S(y + py * s)) for px, py in pts], fill=col, outline=K)


def maze(d, cx, cy, size, p, col=(90, 90, 90)):
    """Laberinto cuadrado simple, dibujado según p 0..1."""
    n = 6
    c = size / n
    x0, y0 = cx - size / 2, cy - size / 2
    walls = [
        (0, 0, 6, 0), (0, 6, 5, 6), (0, 0, 0, 6), (6, 0, 6, 5),
        (1, 1, 5, 1), (1, 1, 1, 5), (2, 2, 2, 6), (3, 1, 3, 4), (4, 2, 4, 5), (5, 1, 5, 4),
        (1, 5, 2, 5), (3, 5, 5, 5), (2, 2, 3, 2),
    ]
    k = int(len(walls) * p + 0.999)
    for (a, b, e, f) in walls[:k]:
        d.line([S(x0 + a * c), S(y0 + b * c), S(x0 + e * c), S(y0 + f * c)], fill=col, width=S(14))


def page_card(d, cx, cy, w, h, n, col=C):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 26, fill=K2, outline=col, width=6)
    text_c(d, cx, cy - h * 0.22, f"PÁGINA {n}", "A", 60, col, bg=K2)
    for k in range(3):
        rrect(d, cx - w * 0.36, cy + k * 34 - 5, cx + w * (0.36 - 0.12 * k), cy + k * 34 + 9, 7, fill=(70, 70, 70))
    rrect(d, cx - w * 0.3, cy + h * 0.3 - 26, cx + w * 0.3, cy + h * 0.3 + 26, 26, fill=Y)
    text_c(d, cx, cy + h * 0.3, "¿SEGURO?", "Black", 28, K, bg=Y)


def b1(d, t):
    lt = t
    pop_line(d, lt, 0.0, 540, 320, "¿POR QUÉ CUESTA", 125, C, dur=0.25)
    pop_line(d, lt, 0.2, 540, 470, "TANTO CANCELAR?", 125, Y, dur=0.25)
    # botón "CANCELAR" que se escapa del cursor
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        jumps = [(540, 900), (300, 1060), (780, 1150), (420, 820)]
        j = min(3, int(max(0, lt - 1.1) / 0.6))
        q = ease_out(prog(lt, 1.1 + j * 0.6, 0.18)) if lt > 1.1 else 1
        bx = lerp(jumps[max(0, j - 1)][0], jumps[j][0], q) if j > 0 else jumps[0][0]
        by = lerp(jumps[max(0, j - 1)][1], jumps[j][1], q) if j > 0 else jumps[0][1]
        w2, h2 = 220 * e, 70 * e
        rrect(d, bx - w2, by - h2, bx + w2, by + h2, 70 * e, fill=R)
        text_c(d, bx, by, "CANCELAR", "Black", 54 * e, C, bg=R)
        # el cursor persigue
        tx, ty = jumps[min(3, j + 1)] if lt > 0.9 else (540, 1350)
        cp = ease_in_out(prog((lt - 0.9) % 0.6, 0, 0.5)) if lt > 0.9 else 0
        cx = lerp(540, bx + 40, 0.5 + 0.5 * cp)
        cy = lerp(1350, by + 30, 0.5 + 0.5 * cp)
        cursor(d, cx, cy, 1.4)
    slide_line(d, lt, 2.6, 540, 1400, "no es casualidad", 52, C, kind="SemiBold", dy=25)


def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "TIENE NOMBRE:", 110, C)
    pop_line(d, lt, 0.35, 540, 440, "PATRONES OSCUROS", 125, Y)
    maze(d, 540, 900, 560, ease_out(prog(lt, 0.6, 1.0)))
    # bolita perdida dando vueltas
    if lt > 1.0:
        path = [(1.5, 0.5), (2.5, 0.5), (2.5, 1.5), (2.5, 3.5), (3.5, 4.5), (3.5, 3.5), (4.5, 1.5), (4.5, 4.5)]
        u = ((lt - 1.0) * 2.2) % (len(path) - 1)
        i = int(u); f = u - i
        px = lerp(path[i][0], path[i + 1][0], f); py = lerp(path[i][1], path[i + 1][1], f)
        c = 560 / 6
        circle(d, 540 - 280 + px * c, 900 - 280 + py * c, 26, fill=R)
    slide_line(d, lt, 1.8, 540, 1290, "diseños para que te cueste irte", 48, C, kind="SemiBold", dy=25)


def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 265, "AMAZON LE PUSO", 110, C)
    pop_line(d, lt, 0.35, 540, 445, "\"ILÍADA\"", 170, Y)
    slide_line(d, lt, 0.6, 540, 560, "a su trámite para cancelar Prime", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 0.8, 540, 612, "(como el poema de la guerra de Troya)", 36, G, kind="Medium", dy=20)
    for k in range(3):
        e = back(prog(lt, 1.2 + k * 0.45, 0.3))
        if e > 0.02:
            page_card(d, 470 + k * 70, 830 + k * 135, 460 * e, 340 * e, k + 1)
    pill(d, lt, 2.7, 540, 1365, 620, "3 PÁGINAS PARA IRTE", fill=R, ink=C, size=42)
    slide_line(d, lt, 2.9, 540, 1450, "FTC vs. Amazon (AP, 25/09/2025)", 32, G, kind="SemiBold", dy=20)


def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "Y BOTONES QUE TE", 110, C)
    slide_line(d, lt, 0.3, 540, 410, "HACEN SENTIR CULPA", 110, Y)
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        w2, h2 = 420 * e, 330 * e
        rrect(d, 540 - w2, 900 - h2, 540 + w2, 900 + h2, 40, fill=K2, outline=(70, 70, 70), width=4)
        if e > 0.8:
            text_c(d, 540, 665, "¿TE VAS A IR?", "A", 80, C, bg=K2)
            # botón grande para quedarse (late)
            pul = 1 + 0.04 * math.sin(lt * 9) if lt > 1.2 else 1
            rrect(d, 540 - 330 * pul, 820 - 65 * pul, 540 + 330 * pul, 820 + 65 * pul, 70, fill=Y)
            text_c(d, 540, 820, "¡QUIERO MIS BENEFICIOS!", "Black", 40 * pul, K, bg=Y)
            # opción chiquita y gris para salir
            q = prog(lt, 1.4, 0.3)
            text_c(d, 540, 960, "no gracias, no quiero", "SemiBold", 34, (110, 110, 110), alpha=q, bg=K2)
            text_c(d, 540, 1005, "envío gratis", "SemiBold", 34, (110, 110, 110), alpha=q, bg=K2)
            if lt > 2.0:
                cursor(d, lerp(800, 640, ease_out(prog(lt, 2.0, 0.5))), lerp(1150, 990, ease_out(prog(lt, 2.0, 0.5))), 1.2)
    slide_line(d, lt, 2.4, 540, 1340, "lo chiquito y gris es la salida", 48, C, kind="SemiBold", dy=25)


def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "¿EL RESULTADO?", 110, C)
    n = 2500 * ease_out(prog(lt, 0.5, 1.3))
    sx, sy = shake(lt, 1.8, 0.35, 18)
    pop_line(d, lt, 0.4, 540 + sx, 560 + sy, "US$ " + fmt_num(n), 175, Y)
    slide_line(d, lt, 0.6, 540, 700, "MILLONES", 100, C)
    slide_line(d, lt, 1.0, 540, 800, "para cerrar el caso con la FTC (EE.UU.)", 40, C, kind="SemiBold", dy=20)
    # dos barras: multa + reembolsos
    for k, (lab, v, col) in enumerate([("multa récord: US$ 1.000 M", 0.4, R), ("devoluciones: US$ 1.500 M", 0.6, GREEN)]):
        y = 950 + k * 190
        p = ease_in_out(prog(lt, 1.6 + k * 0.4, 0.6))
        text_l(d, 110, y, lab, "Bold", 42, C) if p > 0 else None
        rrect(d, 110, y + 40, 970, y + 120, 40, fill=K2)
        if p > 0.02:
            rrect(d, 110, y + 40, 110 + max(80, 860 * v * p), y + 120, 40, fill=col)
    slide_line(d, lt, 2.6, 540, 1400, "AP, 25/09/2025 · Amazon no admitió culpa", 32, G, kind="SemiBold", dy=20)


def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 300, "ANTES DE SUSCRIBIRTE", 105, C)
    pop_line(d, lt, 0.3, 540, 430, "FIJATE CÓMO SE SALE", 110, Y)
    stamp(d, lt, 0.8, 540, 760, 330, 120, "AVISADO", fill=Y, ink=K, size=160)
    slide_line(d, lt, 1.3, 540, 1020, "y anotá cuándo vence la prueba gratis", 42, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.7, 540, 1160, "¿alguna vez te costó cancelar algo?", 46, Y, kind="Bold", dy=25)
    slide_line(d, lt, 1.9, 540, 1230, "contalo en los comentarios", 42, C, kind="SemiBold", dy=25)


BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.2); ev(0.2, "pop", 0.2); ev(0.5, "pop")
for k in range(4): ev(1.1 + k * 0.6, "swipe", -0.4 + k * 0.25)
ev(1.0, "click"); ev(1.6, "click"); ev(2.2, "click"); ev(2.8, "click"); ev(2.6, "tap")
ev(4.1, "tap"); ev(4.35, "thump")
for k in range(6): ev(4.6 + k * 0.17, "click", -0.3 + k * 0.12)
ev(5.0, "rustle"); ev(5.8, "tap")
ev(8.1, "tap"); ev(8.35, "thump"); ev(8.6, "tap"); ev(8.8, "tap")
for k in range(3): ev(9.2 + k * 0.45, "pop", -0.4 + k * 0.4)
ev(10.7, "buzz"); ev(10.9, "tap")
ev(12.1, "tap"); ev(12.3, "tap"); ev(12.6, "pop"); ev(13.4, "tap", 0.2); ev(14.0, "whoosh", 0.4); ev(14.5, "click"); ev(14.4, "tap")
ev(16.1, "tap"); ev(16.4, "pop")
for k in range(13): ev(16.5 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(17.8, "thump"); ev(17.6, "tap"); ev(18.0, "swipe", -0.3); ev(18.4, "swipe", 0.3); ev(18.6, "tap")
ev(20.05, "tap"); ev(20.3, "pop"); ev(20.6, "whoosh"); ev(20.8, "stamp"); ev(21.3, "tap"); ev(21.7, "ding"); ev(21.9, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
