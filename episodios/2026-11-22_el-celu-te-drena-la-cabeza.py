"""Short 2026-11-22 15:00 — Cómo te enganchan las apps: con el celu cerca rendís menos ("brain drain").

Fuentes:
- Ward, Duke, Gneezy y Bos, "Brain Drain: The Mere Presence of One's Own Smartphone Reduces Available
  Cognitive Capacity", J. of the Association for Consumer Research 2017 (DOI 10.1086/691462),
  vía UT News (Univ. de Texas en Austin, 26/06/2017):
  casi 800 usuarios de smartphone; celu en la mesa boca abajo, en el bolsillo/bolso o en otra pieza
  (en silencio); pruebas que piden concentración total; los de "otra pieza" rindieron bastante mejor que
  los de la mesa y un poco mejor que los de bolsillo/bolso; no importó si estaba prendido o apagado,
  boca arriba o boca abajo; los más dependientes del celu, peor (solo si lo tenían cerca).
  Ward: "It's a brain drain."
- Réplica parcial: Hartmann et al., Univ. de Berna, Consciousness and Cognition 2020 (vía BPS Research
  Digest 18/01/2021): 302 personas, no encontró diferencia en pruebas de memoria.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

PINK = (255, 140, 170)

def brain(d, cx, cy, s, col=PINK, ink=K):
    """Cerebro simple: lóbulos con círculos + surcos."""
    for dx, dy, r in ((-0.22, -0.08, 0.26), (0.0, -0.18, 0.27), (0.22, -0.08, 0.26),
                      (-0.26, 0.12, 0.22), (0.26, 0.12, 0.22), (0.0, 0.08, 0.28)):
        circle(d, cx + dx * s, cy + dy * s, r * s, fill=col)
    d.line([S(cx), S(cy - s * 0.4), S(cx), S(cy + s * 0.3)], fill=ink, width=SW(s * 0.025))
    for side in (-1, 1):
        d.arc([S(cx + side * s * 0.08 - s * 0.14), S(cy - s * 0.25), S(cx + side * s * 0.08 + s * 0.14), S(cy - s * 0.02)],
              200 if side < 0 else -20, 340 if side < 0 else 160, fill=ink, width=SW(s * 0.022))
        d.arc([S(cx + side * s * 0.25 - s * 0.12), S(cy + s * 0.0), S(cx + side * s * 0.25 + s * 0.12), S(cy + s * 0.22)],
              0, 180, fill=ink, width=SW(s * 0.022))

def table(d, cy, x0=140, x1=940):
    rrect(d, x0, cy, x1, cy + 34, 12, fill=(110, 80, 50))
    d.rectangle([S(x0 + 60), S(cy + 34), S(x0 + 90), S(cy + 260)], fill=(90, 64, 40))
    d.rectangle([S(x1 - 90), S(cy + 34), S(x1 - 60), S(cy + 260)], fill=(90, 64, 40))

def flat_phone(d, cx, cy, w):
    """Celu boca abajo sobre la mesa (visto de costado)."""
    rrect(d, cx - w / 2, cy - 26, cx + w / 2, cy, 12, fill=K2, outline=C, width=5)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 290, "TU CELU AL LADO", 140, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 440, "TE BAJA LA CABEZA", 118, Y, dur=0.25)
    e = back(prog(t, 0.6, 0.35))
    if e > 0.02:
        brain(d, 540, 760, 380 * e)
    # batería del cerebro que baja
    p = prog(t, 1.2, 1.4)
    if t > 1.1:
        lvl = lerp(0.95, 0.25, ease_in_out(p))
        battery(d, 540, 1030, 300, 120, lvl, R if lvl < 0.4 else GREEN)
    if t > 0.8:
        table(d, 1150, 300, 780)
        flat_phone(d, 540, 1150, 220)
    slide_line(d, t, 2.8, 540, 1500, "AUNQUE NI LO TOQUES", 100, R, dy=30)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "CASI 800 PERSONAS", 130, C)
    slide_line(d, lt, 0.35, 540, 390, "pruebas que piden concentración total", 44, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 0.55, 540, 450, "con el celu en silencio en uno de 3 lugares:", 38, G, kind="SemiBold", dy=20)
    labels = [("EN LA MESA", "boca abajo"), ("EN EL BOLSILLO", "o en la mochila"), ("EN OTRA PIEZA", "lejos de vista")]
    for i, (a, b) in enumerate(labels):
        p = prog(lt, 0.9 + i * 0.55, 0.3)
        if p <= 0: continue
        y = 620 + i * 230
        x = lerp(-500, 0, ease_out(p))
        rrect(d, 110 + x, y, 970 + x, y + 190, 40, fill=K2)
        circle(d, 210 + x, y + 95, 55, fill=Y)
        text_c(d, 210 + x, y + 95, str(i + 1), "A", 70, K, bg=Y)
        text_l(d, 300 + x, y + 70, a, "A", 70, C)
        text_l(d, 300 + x, y + 135, b, "SemiBold", 36, G)
    slide_line(d, lt, 2.8, 540, 1400, "Ward et al., Univ. de Texas en Austin, 2017", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "¿QUIÉN RINDIÓ MEJOR?", 120, C)
    # barras (sin cifras: el comunicado no las da; solo el orden)
    bars = [("MESA", 0.45, (90, 90, 90)), ("BOLSILLO", 0.72, (150, 150, 150)), ("OTRA PIEZA", 0.88, Y)]
    base = 1080
    for i, (lab, v, col) in enumerate(bars):
        p = ease_out(prog(lt, 0.5 + i * 0.35, 0.6))
        if p <= 0: continue
        cx = 250 + i * 290
        hgt = 560 * v * p
        rrect(d, cx - 100, base - hgt, cx + 100, base, 24, fill=col)
        text_c(d, cx, base + 60, lab, "A", 54 if i < 2 else 50, C)
    stamp(d, t, 10.1, 540, 1280, 400, 90, "LEJOS = MEJOR", fill=Y, ink=K, size=120)
    slide_line(d, lt, 2.6, 540, 1420, "bastante mejor que con el celu en la mesa", 42, C, kind="Bold", dy=20)
    slide_line(d, lt, 2.8, 540, 1490, "UT News, 26/06/2017 · barras ilustrativas (el orden, no la cifra)", 28, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "Y NO IMPORTÓ SI ESTABA", 96, C)
    p1 = prog(lt, 0.5, 0.3)
    if p1 > 0:
        q = 0.5 + 0.5 * math.sin(lt * 5) if lt > 0.9 else 1
        toggle_row(d, 110, 430, "Prendido o apagado", q, sub=None)
    p2 = prog(lt, 1.1, 0.3)
    if p2 > 0:
        q2 = 0.5 + 0.5 * math.sin(lt * 5 + 1.5) if lt > 1.5 else 0
        toggle_row(d, 110, 630, "Boca arriba o abajo", q2, sub=None)
    slide_line(d, lt, 1.6, 540, 830, "= MISMO EFECTO", 70, R, dy=20)
    pop_line(d, lt, 1.9, 540, 960, "\"ES UN DRENAJE", 110, Y)
    pop_line(d, lt, 2.1, 540, 1080, "DE CEREBRO\"", 110, Y)
    slide_line(d, lt, 2.5, 540, 1190, "Adrian Ward, autor del estudio", 40, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.8, 540, 1270, "los más pegados al celu, peor (solo con el celu cerca)", 34, C, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    e = back(prog(lt, 0.05, 0.35))
    if e > 0.02:
        warning(d, 540, 400, 260 * e)
    pop_line(d, lt, 0.3, 540, 660, "OJO: NO ES LEY", 140, R)
    slide_line(d, lt, 0.8, 540, 790, "en 2020, otro estudio con 302 personas", 42, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 1.0, 540, 850, "no encontró diferencia en pruebas de memoria", 42, C, kind="SemiBold", dy=20)
    pill(d, t, 17.6, 540, 1000, 900, "LA CIENCIA TODAVÍA LO DISCUTE", fill=C, ink=K, size=40, h=110)
    slide_line(d, lt, 2.4, 540, 1140, "pero alejarlo no te cuesta nada", 50, Y, kind="Bold", dy=20)
    slide_line(d, lt, 2.7, 540, 1220, "Hartmann et al., Univ. de Berna, 2020 (vía BPS)", 30, G, kind="SemiBold", dy=20)

def door(d, cx, cy, w, h, open_=0.0):
    rrect(d, cx - w / 2 - 14, cy - h / 2 - 14, cx + w / 2 + 14, cy + h / 2, 10, fill=(70, 70, 70))
    ww = w * (1 - 0.7 * open_)
    rrect(d, cx - w / 2, cy - h / 2, cx - w / 2 + ww, cy + h / 2, 8, fill=(140, 100, 60))
    circle(d, cx - w / 2 + ww - 26, cy, 12, fill=Y)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 330, "¿VAS A ESTUDIAR", 125, C)
    pop_line(d, lt, 0.3, 540, 470, "O A TRABAJAR?", 125, Y)
    if lt > 0.6:
        op = ease_in_out(prog(lt, 0.7, 0.4)) - ease_in_out(prog(lt, 1.9, 0.3))
        door(d, 760, 830, 240, 420, max(0, op))
        # celu que viaja hacia la puerta
        p = ease_in_out(prog(lt, 0.9, 0.9))
        if p < 1:
            phone(d, lerp(300, 720, p), 830, lerp(170, 60, p), lerp(300, 110, p))
    pop_line(d, lt, 2.0, 540, 1180, "DEJALO EN OTRA PIEZA", 105, Y)
    slide_line(d, lt, 2.4, 540, 1290, "aunque sea mientras te concentrás", 44, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "thump"); ev(0.6, "pop"); ev(0.8, "tap")
for k in range(6): ev(1.3 + k * 0.22, "tick")
ev(2.8, "thump")
ev(4.1, "tap"); ev(4.35, "tap"); ev(4.55, "tap")
for k in range(3): ev(4.9 + k * 0.55, "swipe", -0.5 + k * 0.5)
ev(6.8, "tap")
ev(8.1, "tap")
for k in range(3): ev(8.5 + k * 0.35, "pop", -0.4 + k * 0.4)
ev(9.9, "whoosh"); ev(10.1, "stamp"); ev(10.6, "tap"); ev(10.8, "tap")
ev(12.1, "tap"); ev(12.5, "pop"); ev(12.9, "toggle"); ev(13.1, "pop"); ev(13.5, "toggle"); ev(13.9, "thump"); ev(14.1, "thump"); ev(14.5, "tap"); ev(14.8, "tap")
ev(16.05, "pop"); ev(16.3, "thump"); ev(16.8, "tap"); ev(17.0, "tap"); ev(17.6, "pop"); ev(18.4, "ding"); ev(18.7, "tap")
ev(20.1, "pop", -0.3); ev(20.3, "pop", 0.3); ev(20.7, "click"); ev(20.9, "swipe", 0.4); ev(21.9, "click"); ev(22.0, "thump"); ev(22.4, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
