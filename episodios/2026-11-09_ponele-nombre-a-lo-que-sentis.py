"""Short 2026-11-09 20:00 - Mente y emociones: ponerle nombre a la emoción baja la respuesta de la amígdala.
Fuente: Lieberman et al., UCLA, Psychological Science 2007 (comunicado UCLA Health, 21/06/2007)."""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def angry(d, cx, cy, r, col=R):
    circle(d, cx, cy, r, fill=col)
    for s in (-1, 1):
        circle(d, cx + s * r * 0.36, cy - r * 0.1, r * 0.11, fill=K)
        d.line([S(cx + s * r * 0.62), S(cy - r * 0.48), S(cx + s * r * 0.14), S(cy - r * 0.26)], fill=K, width=int(S(max(6, r * 0.1))))
    d.arc([S(cx - r * 0.42), S(cy + r * 0.28), S(cx + r * 0.42), S(cy + r * 0.85)], 200, 340, fill=K, width=int(S(max(6, r * 0.09))))

def brain(d, cx, cy, s, col, core=None):
    """cerebro simple: lóbulos + surco central"""
    circle(d, cx, cy, s * 0.4, fill=col)
    for dx, dy, r in [(-0.34, -0.16, 0.3), (-0.42, 0.14, 0.27), (-0.14, -0.3, 0.27), (-0.14, 0.24, 0.26),
                      (0.34, -0.16, 0.3), (0.42, 0.14, 0.27), (0.14, -0.3, 0.27), (0.14, 0.24, 0.26)]:
        circle(d, cx + dx * s, cy + dy * s, r * s, fill=col)
    d.line([S(cx), S(cy - s * 0.5), S(cx), S(cy + s * 0.46)], fill=K, width=int(S(max(4, s * 0.025))))
    if core: circle(d, cx, cy + s * 0.05, s * 0.13, fill=core)

def card(d, lt, t0, cy, w, h, title, a, b, hi):
    e = back(prog(lt, t0, 0.35))
    if e <= 0.02: return
    rrect(d, 540 - w / 2 * e, cy - h / 2 * e, 540 + w / 2 * e, cy + h / 2 * e, 40, fill=K2)
    text_c(d, 540, cy - 70, title, "SemiBold", 42, G, bg=K2)
    text_c(d, 340, cy + 40, a, "A", 90, hi, bg=K2)
    text_c(d, 740, cy + 40, b, "A", 90, hi, bg=K2)
    d.line([S(540), S(cy + 5), S(540), S(cy + 90)], fill=G, width=S(3))

def b1(d, t):
    pulse = 1 + 0.08 * math.sin(t * 14)
    e = back(prog(t, 0.0, 0.3))
    if e > 0.02:
        for k in range(4, 0, -1):
            circle(d, 540, 1140, (170 + k * 60) * e * pulse, fill=mix(K, R, 0.1 * (5 - k)))
        angry(d, 540, 1140, 190 * e * pulse)
    pop_line(d, t, 0.0, 540, 300, "¿ESTÁS A PUNTO", 160, C)
    pop_line(d, t, 0.25, 540, 480, "DE EXPLOTAR?", 160, R)
    pop_line(d, t, 1.8, 540, 1660, "PROBÁ CON UNA PALABRA", 96, Y)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.05, 540, 290, "EN UCLA", 150, C)
    pop_line(d, lt, 0.35, 540, 450, "MIRARON 30 CEREBROS", 110, Y)
    e = back(prog(lt, 0.7, 0.4))
    if e > 0.02:
        brain(d, 540, 870, 520 * e, (200, 170, 180))
        ang = lt * 3.2
        yy = 870 + math.sin(ang) * 240
        if lt > 1.0:
            d.line([S(190), S(yy), S(890), S(yy)], fill=Y, width=S(8))
    pop_line(d, lt, 2.3, 540, 1320, "MIENTRAS VEÍAN", 100, C)
    pop_line(d, lt, 2.55, 540, 1440, "CARAS CON EMOCIONES", 100, R)
    slide_line(d, lt, 2.95, 540, 1550, "fotos de gente enojada, asustada...", 44, C, kind="SemiBold", dy=25)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.05, 540, 290, "ANTE CADA CARA", 130, C)
    slide_line(d, lt, 0.3, 540, 420, "tenían que elegir una palabra", 46, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.45, 0.35))
    if e > 0.02: angry(d, 540, 710, 150 * e)
    card(d, lt, 1.1, 1030, 880, 240, "la emoción", "ENOJADO", "ASUSTADO", Y)
    card(d, lt, 1.9, 1320, 880, 240, "o un nombre", "HARRY", "SALLY", C)
    slide_line(d, lt, 2.6, 540, 1530, "dos tareas, misma cara", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.05, 540, 290, "AL NOMBRAR LA EMOCIÓN", 96, C)
    pop_line(d, lt, 0.35, 540, 420, "BAJÓ LA ALARMA", 120, Y)
    e = back(prog(lt, 0.5, 0.35))
    lvl = 1 - 0.55 * ease_in_out(prog(lt, 1.0, 1.4))
    if e > 0.02:
        x0, x1, y0, y1 = 170, 910, 720, 840
        rrect(d, x0, y0, x1, y1, 60, fill=K2, outline=C, width=6)
        rrect(d, x0 + 16, y0 + 16, x0 + 16 + (x1 - x0 - 32) * lvl * e, y1 - 16, 44, fill=mix(GREEN, R, clamp((lvl - 0.45) / 0.55)))
        text_c(d, 540, 910, "la amígdala, tu alarma interna", "SemiBold", 42, C)
    pop_line(d, lt, 2.1, 540, 1090, "CON UN NOMBRE", 110, C)
    pop_line(d, lt, 2.35, 540, 1290, "NO PASÓ", 170, R)
    slide_line(d, lt, 2.8, 540, 1450, "Lieberman et al., UCLA, Psychological Science, 2007", 34, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.05, 540, 290, "Y SE PRENDIÓ", 130, C)
    pop_line(d, lt, 0.3, 540, 440, "OTRA ZONA", 150, Y)
    slide_line(d, lt, 0.6, 540, 545, "una parte de la corteza prefrontal", 44, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.6, 0.4))
    if e > 0.02:
        on = ease_in_out(prog(lt, 1.2, 0.6))
        brain(d, 540, 900, 460 * e, mix((110, 95, 100), (200, 170, 180), on))
        if on > 0.02:
            for k in range(4, 0, -1):
                circle(d, 700, 760, (22 + k * 22) * on, fill=mix((200, 170, 180), Y, 0.2 * (5 - k)))
            circle(d, 700, 760, 34 * on, fill=Y)
    pill(d, lt, 2.2, 540, 1320, 860, "ESTUDIO CHICO, PERO DA UNA PISTA", fill=K2, ink=C, size=42, h=110)
    pop_line(d, lt, 2.6, 540, 1490, "NOMBRAR AYUDA", 130, Y)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "LA PRÓXIMA VEZ", 130, C)
    pop_line(d, lt, 0.3, 540, 490, "DECILO:", 150, Y)
    for t0, cy, txt, col in [(0.6, 780, "“ESTOY ENOJADO”", Y), (1.2, 1015, "“ESTOY TRISTE”", C)]:
        e = back(prog(lt, t0, 0.3))
        if e > 0.02:
            rrect(d, 540 - 400 * e, cy - 85 * e, 540 + 400 * e, cy + 85 * e, 44, fill=col)
            d.polygon([(S(250), S(cy + 80 * e)), (S(330), S(cy + 80 * e)), (S(230), S(cy + 140 * e))], fill=col)
            text_c(d, 540, cy, txt, "A", 104, K, scale=e, bg=col)
    slide_line(d, lt, 2.0, 540, 1230, "ponerle nombre es un primer paso", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.2, 540, 1320, "si te supera seguido, buscá ayuda", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1385, "y hablalo con alguien de confianza", 46, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop", -0.2); ev(0.28, "pop", 0.2)
for k in range(6): ev(0.7 + k * 0.17, "tick", 0.3 if k % 2 else -0.3)
ev(1.8, "ding")
ev(4.1, "tap"); ev(4.4, "pop"); ev(4.75, "shimmer")
for k in range(8): ev(5.1 + k * 0.17, "click", 0.3 if k % 2 else -0.3)
ev(6.3, "tap", -0.2); ev(6.55, "pop", 0.2); ev(6.95, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.5, "pop"); ev(9.15, "pop", -0.3); ev(9.95, "pop", 0.3); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.4, "pop"); ev(12.6, "toggle")
for k in range(9): ev(13.0 + k * 0.14, "tick", 0.3 if k % 2 else -0.3)
ev(14.1, "tap"); ev(14.4, "stamp"); ev(14.8, "tap")
ev(16.1, "tap"); ev(16.35, "pop"); ev(16.6, "tap"); ev(17.25, "toggle"); ev(17.7, "shimmer"); ev(18.2, "tap"); ev(18.6, "thump")
ev(20.1, "tap"); ev(20.35, "pop"); ev(20.5, "pop", -0.3); ev(20.85, "tap", 0.3); ev(21.15, "pop", 0.3); ev(21.45, "tap", -0.3); ev(22.05, "tap"); ev(22.25, "tap"); ev(22.4, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
