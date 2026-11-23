"""Short 2026-11-23 20:00 — Mente y emociones.
El suspiro cíclico: 5 minutos por día de respiración que subió el ánimo.
Fuente: Balban, Spiegel, Huberman et al., Stanford, "Brief structured respiration practices enhance mood and
reduce physiological arousal", Cell Reports Medicine, ene. 2023 (comunicado Stanford Medicine 09/02/2023):
108 personas sanas, 5 min por día durante 1 mes, 4 grupos (suspiro cíclico, respiración en caja,
hiperventilación cíclica, meditación mindfulness). Respirar subió el ánimo positivo 1,91 vs 1,22 puntos
(meditación); el suspiro cíclico fue el que más mejoró el ánimo y bajó la frecuencia respiratoria.
Estudio exploratorio, chico, gente sana, 1 mes.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

BLUE = (90, 170, 255)

def lungs(d, cx, cy, s, fill, col=BLUE):
    """Pulmones que se inflan: fill 0..1."""
    k = 0.75 + 0.35 * fill
    d.line([S(cx), S(cy - s * 0.55), S(cx), S(cy - s * 0.15)], fill=C, width=S(18))
    for side in (-1, 1):
        d.line([S(cx), S(cy - s * 0.15), S(cx + side * s * 0.16), S(cy)], fill=C, width=S(14))
        lx = cx + side * s * 0.3
        rrect(d, lx - s * 0.2 * k, cy - s * 0.38 * k, lx + s * 0.2 * k, cy + s * 0.42 * k, s * 0.18 * k,
              fill=mix(K2, col, 0.35 + 0.65 * fill), outline=C, width=6)

def wave(d, y, amp, freq, t, col, x0=110, x1=970, width=10):
    pts = []
    for k in range(121):
        x = lerp(x0, x1, k / 120)
        pts.append((S(x), S(y + amp * math.sin((x - x0) / (x1 - x0) * math.tau * freq - t * 3))))
    d.line(pts, fill=col, width=S(width), joint="curve")

def b1(d, t):
    text_c(d, 540, 330, "¿ESTRESADO?", "A", 170, Y)
    pop_line(d, t, 0.25, 540, 500, "PROBÁ RESPIRAR", 125, C)
    pop_line(d, t, 0.45, 540, 640, "ASÍ 5 MINUTOS", 125, C)
    e = back(prog(t, 0.6, 0.4))
    if e > 0.02:
        f = 0.5 + 0.5 * math.sin(t * 2.2)
        lungs(d, 540, 1060, 420 * e, f)
    slide_line(d, t, 1.8, 540, 1420, "lo comparó Stanford", 48, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.0, 540, 1485, "contra la meditación", 48, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "108 PERSONAS", 140, Y)
    slide_line(d, lt, 0.3, 540, 420, "UN MES ENTERO", 120, C)
    slide_line(d, lt, 0.5, 540, 525, "5 minutos por día", 48, C, kind="SemiBold", dy=25)
    # calendario que se va tachando
    days = int(28 * ease_in_out(prog(lt, 0.8, 1.6)))
    for i in range(28):
        r, c = divmod(i, 7)
        x, y = 205 + c * 100, 640 + r * 100
        p = prog(lt, 0.5 + i * 0.015, 0.2)
        if p <= 0: continue
        rrect(d, x, y, x + 80, y + 80, 16, fill=Y if i < days else K2)
        if i < days:
            d.line([S(x + 20), S(y + 42), S(x + 35), S(y + 58), S(x + 62), S(y + 24)], fill=K, width=S(8))
    pill(d, lt, 2.3, 540, 1140, 760, "4 GRUPOS AL AZAR", fill=C, ink=K, size=44, h=96)
    slide_line(d, lt, 2.6, 540, 1260, "3 formas de respirar  ·  1 de meditar", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.8, 540, 1720, "Balban, Spiegel, Huberman et al., Stanford, Cell Reports Medicine 2023", 27, G, kind="SemiBold", dy=15)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 280, "EL SUSPIRO", 140, C)
    slide_line(d, lt, 0.3, 540, 420, "CÍCLICO", 160, Y)
    # ciclo: 0-1.0 inhalar, 1.0-1.5 sorbito extra, 1.5-3.5 exhalar lento
    c = lt - 0.6
    if c < 0: f = 0.0
    elif c < 0.9: f = 0.7 * ease_out(c / 0.9)
    elif c < 1.3: f = 0.7 + 0.3 * ease_out((c - 0.9) / 0.4)
    else: f = 1.0 - ease_in_out(clamp((c - 1.3) / 2.0))
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        circle(d, 540, 850, (130 + 150 * f) * e, fill=mix(K, BLUE, 0.25 + 0.5 * f))
        circle(d, 540, 850, (130 + 150 * f) * e, outline=C, width=8)
    steps = [(0.6, "1. INHALÁ POR LA NARIZ"), (1.5, "2. OTRO SORBITO DE AIRE"), (1.9, "3. SOLTÁ LENTO POR LA BOCA")]
    for i, (t0, s) in enumerate(steps):
        active = (i == 0 and c < 0.9) or (i == 1 and 0.9 <= c < 1.3) or (i == 2 and c >= 1.3)
        pop_line(d, lt, t0, 540, 1240 + i * 120, s, 78, Y if active else C)
    slide_line(d, lt, 2.6, 540, 1610, "y repetí, más o menos 5 minutos", 44, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO:", 130, C)
    slide_line(d, lt, 0.3, 540, 430, "MÁS BUEN ÁNIMO", 130, Y)
    slide_line(d, lt, 0.5, 540, 540, "subida del ánimo positivo por día", 42, C, kind="SemiBold", dy=25)
    # barras 1,22 vs 1,91
    base = 1260
    for i, (lab, val, col, t0) in enumerate([("MEDITAR", 1.22, (150, 150, 150), 0.8), ("RESPIRAR", 1.91, Y, 1.2)]):
        q = ease_out(prog(lt, t0, 0.8))
        x = 300 + i * 300
        h = 260 * val * q
        if q > 0:
            rrect(d, x - 95, base - h, x + 95, base, 20, fill=col)
            text_c(d, x, base - h - 60, f"{val * q:.2f}".replace(".", ","), "A", 80, col)
        text_c(d, x, base + 55, lab, "Black", 44, C)
    sx, sy = shake(lt, 2.5, 0.35, 16)
    stamp(d, lt, 2.3, 540 + sx, 1480 + sy, 360, 85, "MÁS QUE MEDITAR", fill=Y, ink=K, size=96)
    slide_line(d, lt, 2.7, 540, 1620, "los que respiraron vs. los que meditaron", 40, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "EL QUE MÁS SUBIÓ", 120, C)
    slide_line(d, lt, 0.3, 540, 430, "EL SUSPIRO CÍCLICO", 120, Y)
    # onda de respiración que se hace más lenta
    q = ease_in_out(prog(lt, 1.0, 1.6))
    if lt > 0.5:
        wave(d, 780, 110, lerp(5, 2, q), lt * lerp(3, 1, q), mix(R, BLUE, q))
    pop_line(d, lt, 1.2, 540, 1030, "RESPIRABAN MÁS LENTO", 95, C)
    slide_line(d, lt, 1.6, 540, 1140, "y no solo durante el ejercicio:", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.8, 540, 1200, "durante todo el día", 44, Y, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1380, "ojo: estudio chico, con gente sana,", 38, G, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.75, 540, 1430, "de un solo mes", 38, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "EL TRUCO:", 130, C)
    slide_line(d, lt, 0.3, 540, 480, "DOS INHALES,", 140, Y)
    slide_line(d, lt, 0.45, 540, 630, "UN EXHALE LARGO", 125, Y)
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        f = 0.5 + 0.5 * math.sin(lt * 2.0)
        lungs(d, 540, 900, 360 * e, f)
    slide_line(d, lt, 1.2, 540, 1140, "probalo cuando te estreses", 46, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.6, 540, 1290, "¿LO PROBÁS HOY?", 110, C)
    slide_line(d, lt, 2.1, 540, 1440, "si la ansiedad no se va, buscá ayuda", 40, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.25, "pop", -0.3); ev(0.45, "pop", 0.3); ev(0.6, "whoosh"); ev(1.8, "tap"); ev(2.0, "tap")
ev(4.1, "thump"); ev(4.3, "tap"); ev(4.5, "tap")
for k in range(14): ev(4.8 + k * 0.11, "tick", 0.3 if k % 2 else -0.3)
ev(6.3, "pop"); ev(6.6, "tap")
ev(8.1, "tap"); ev(8.3, "pop"); ev(8.6, "whoosh"); ev(8.6, "pop", -0.2); ev(9.5, "pop", 0.2); ev(9.6, "shimmer")
ev(10.1, "pop"); ev(10.2, "whoosh"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.3, "pop"); ev(12.5, "tap")
for k in range(6): ev(12.8 + k * 0.13, "tick", -0.3)
for k in range(6): ev(13.2 + k * 0.13, "tick", 0.3)
ev(14.1, "whoosh"); ev(14.3, "stamp"); ev(14.7, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.5, "whoosh"); ev(17.2, "pop"); ev(17.6, "tap"); ev(17.8, "ding"); ev(18.6, "tap")
ev(20.1, "tap"); ev(20.3, "pop", -0.2); ev(20.45, "pop", 0.2); ev(20.6, "whoosh"); ev(21.2, "tap"); ev(21.6, "pop"); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
