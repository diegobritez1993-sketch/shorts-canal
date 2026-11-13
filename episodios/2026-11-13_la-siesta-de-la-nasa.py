"""Short 2026-11-13 15:00 — Curiosidades y hábitos: la siesta corta que midió la NASA (~26 min).

Fuentes:
- Rosekind et al. (1995), "Alertness management: strategic naps in operational settings", J. Sleep Research 4(S2):62-66
  (estudio NASA con pilotos de vuelos largos transpacíficos). Vía Sleep Foundation ("NASA nap") y TIME (2011, M. Rosekind).
- A los pilotos se les dio una oportunidad de 40 min para dormir en vuelo mientras los otros pilotos volaban;
  durmieron en promedio ~26 min ("about 25 minutes" según TIME).
- Resultado: hasta +34% de rendimiento y hasta +54% de alerta frente a los que no durmieron.
- Siestas largas: más inercia del sueño (te despertás atontado). Consejo: menos de 30 min (Sleep Foundation).
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def rocket(d, cx, cy, s, t, flame=1.0):
    """Cohete genérico con primitivas."""
    w, h = s * 0.36, s
    # llama
    if flame > 0:
        fl = h * 0.35 * flame * (1 + 0.18 * math.sin(t * 40))
        d.polygon([(S(cx - w * 0.32), S(cy + h * 0.38)), (S(cx + w * 0.32), S(cy + h * 0.38)), (S(cx), S(cy + h * 0.38 + fl))], fill=R)
        d.polygon([(S(cx - w * 0.18), S(cy + h * 0.38)), (S(cx + w * 0.18), S(cy + h * 0.38)), (S(cx), S(cy + h * 0.38 + fl * 0.6))], fill=Y)
    # aletas
    d.polygon([(S(cx - w / 2), S(cy + h * 0.1)), (S(cx - w * 0.95), S(cy + h * 0.42)), (S(cx - w / 2), S(cy + h * 0.38))], fill=R)
    d.polygon([(S(cx + w / 2), S(cy + h * 0.1)), (S(cx + w * 0.95), S(cy + h * 0.42)), (S(cx + w / 2), S(cy + h * 0.38))], fill=R)
    # cuerpo
    rrect(d, cx - w / 2, cy - h * 0.2, cx + w / 2, cy + h * 0.4, w * 0.2, fill=C)
    d.pieslice([S(cx - w / 2), S(cy - h * 0.55), S(cx + w / 2), S(cy + h * 0.15)], 180, 360, fill=C)
    # ventanita
    circle(d, cx, cy - h * 0.05, w * 0.22, fill=K2, outline=Y, width=8)

def plane(d, cx, cy, s, col=C):
    """Avión genérico visto desde arriba (apunta a la derecha)."""
    rrect(d, cx - s * 0.5, cy - s * 0.07, cx + s * 0.45, cy + s * 0.07, s * 0.07, fill=col)
    d.polygon([(S(cx + s * 0.45), S(cy - s * 0.07)), (S(cx + s * 0.6), S(cy)), (S(cx + s * 0.45), S(cy + s * 0.07))], fill=col)
    d.polygon([(S(cx - s * 0.05), S(cy - s * 0.06)), (S(cx - s * 0.25), S(cy - s * 0.48)), (S(cx - s * 0.12), S(cy - s * 0.48)), (S(cx + s * 0.18), S(cy - s * 0.06))], fill=col)
    d.polygon([(S(cx - s * 0.05), S(cy + s * 0.06)), (S(cx - s * 0.25), S(cy + s * 0.48)), (S(cx - s * 0.12), S(cy + s * 0.48)), (S(cx + s * 0.18), S(cy + s * 0.06))], fill=col)
    d.polygon([(S(cx - s * 0.42), S(cy - s * 0.05)), (S(cx - s * 0.55), S(cy - s * 0.22)), (S(cx - s * 0.47), S(cy - s * 0.22)), (S(cx - s * 0.32), S(cy - s * 0.05))], fill=col)
    d.polygon([(S(cx - s * 0.42), S(cy + s * 0.05)), (S(cx - s * 0.55), S(cy + s * 0.22)), (S(cx - s * 0.47), S(cy + s * 0.22)), (S(cx - s * 0.32), S(cy + s * 0.05))], fill=col)

def b1(d, t):
    stars(d, t, alpha=1.0)
    e = ease_out(prog(t, 0.0, 0.5))
    if e > 0.02:
        ry = 640 - 40 * math.sin(t * 2.2) + (1 - e) * 500
        rocket(d, 540, ry, 380, t)
        zzz(d, 640, ry - 120, t, col=Y)
    pop_line(d, t, 0.0, 540, 1050, "LA NASA MIDIÓ", 140, C)
    pop_line(d, t, 0.3, 540, 1200, "LA SIESTA", 170, Y)
    pop_line(d, t, 0.5, 540, 1360, "PERFECTA", 170, Y)
    pill(d, t, 2.2, 540, 1530, 760, "¿CUÁNTO TIENE QUE DURAR?", fill=R, ink=C, size=42, h=96)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "PILOTOS EN", 130, C)
    slide_line(d, lt, 0.3, 540, 420, "VUELOS LARGOS", 130, Y)
    # avión cruzando con estela
    px = lerp(-200, 560, ease_out(prog(lt, 0.4, 1.2)))
    if lt > 0.4:
        for k in range(6):
            circle(d, px - 180 - k * 70, 780, 14 - k * 2, fill=mix(K, C, 0.5 - k * 0.07))
        plane(d, px, 780, 360)
    # dos asientos: uno duerme, otro vuela
    q = back(prog(lt, 1.5, 0.35))
    if q > 0.02:
        for i, (lab, col) in enumerate([("DUERME", Y), ("VUELA", C)]):
            x = 340 + i * 400
            rrect(d, x - 150 * q, 1000, x + 150 * q, 1160, 30, fill=K2, outline=col, width=6)
            person(d, x, 1080, 120 * q, col)
            text_c(d, x, 1210, lab, "Black", 40, col, alpha=clamp(q))
    slide_line(d, lt, 2.3, 540, 1330, "les dieron 40 minutos para dormir", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.45, 540, 1400, "mientras el otro piloto volaba", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1480, "Rosekind et al., estudio NASA, 1995", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 290, "DURMIERON", 140, C)
    pop_line(d, lt, 0.3, 540, 420, "EN PROMEDIO", 110, C)
    pr = prog(lt, 0.5, 1.6)
    if lt > 0.4:
        # anillo de 40 min, se llena hasta 26
        r = 260
        circle(d, 540, 820, r, fill=(48, 48, 48))
        d.pieslice([S(540 - r), S(820 - r), S(540 + r), S(820 + r)], -90, -90 + 360 * 26 / 40 * ease_out(pr), fill=Y)
        circle(d, 540, 820, r * 0.7, fill=K)
        n = int(round(26 * ease_out(pr)))
        text_c(d, 540, 800, f"{n}", "A", 220, C)
        text_c(d, 540, 930, "MIN", "A", 70, Y)
        text_c(d, 540 + r + 20, 820 - r + 10, "40", "Black", 40, G)
    sx, sy = shake(lt, 2.2, 0.35, 14)
    stamp(d, lt, 2.15, 540 + sx, 1220 + sy, 330, 90, "26 MINUTOS", fill=Y, ink=K, size=120)
    slide_line(d, lt, 2.6, 540, 1380, "de los 40 que tenían disponibles", 44, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "AL DESPERTAR", 140, C)
    # dos barras que suben
    base = 1150
    for i, (val, lab, col) in enumerate([(34, "RENDIMIENTO", C), (54, "ALERTA", Y)]):
        p = ease_out(prog(lt, 0.5 + i * 0.6, 1.0))
        x = 330 + i * 420
        hh = 600 * val / 54 * p
        if p > 0:
            rrect(d, x - 120, base - hh, x + 120, base, 24, fill=col)
            text_c(d, x, base - hh - 70, f"+{int(round(val * p))}%", "A", 120, col)
            text_c(d, x, base + 60, lab, "Black", 42, col)
    pill(d, lt, 2.2, 540, 1330, 360, "HASTA", fill=R, ink=C, size=50, h=96)
    slide_line(d, lt, 2.5, 540, 1450, "comparado con los que no durmieron", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.7, 540, 1520, "J. Sleep Research 1995 (vía Sleep Foundation y TIME)", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "¿Y SI DORMÍS", 130, C)
    pop_line(d, lt, 0.35, 540, 430, "DE MÁS?", 150, R)
    # batería que sube y luego "se atonta": cara mareada
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        cx, cy, r = 540, 800, 200 * e
        wob = math.sin(lt * 5) * 18 * ease_out(prog(lt, 1.3, 0.4))
        circle(d, cx + wob, cy, r, fill=K2, outline=C, width=8)
        # ojos en espiral
        for sx_ in (-1, 1):
            ex, ey = cx + wob + sx_ * r * 0.38, cy - r * 0.15
            for k in range(3):
                rr = r * (0.06 + k * 0.05)
                a0 = (lt * 300 + k * 60) % 360
                d.arc([S(ex - rr), S(ey - rr), S(ex + rr), S(ey + rr)], a0, a0 + 260, fill=Y, width=S(6))
        d.arc([S(cx + wob - r * 0.35), S(cy + r * 0.2), S(cx + wob + r * 0.35), S(cy + r * 0.55)], 200, 340, fill=C, width=S(10))
    slide_line(d, lt, 1.5, 540, 1100, "INERCIA DEL SUEÑO", 100, Y, kind="A", dy=30)
    slide_line(d, lt, 2.0, 540, 1220, "en siestas largas es más fácil", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.15, 540, 1290, "despertarte atontado y pesado", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.5, 540, 1370, "Sleep Foundation", 32, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 290, "EL TRUCO:", 120, Y)
    # alarma
    q = ease_in_out(prog(lt, 0.4, 0.3))
    sl = ease_out(prog(lt, 0.2, 0.35))
    if sl > 0:
        toggle_row(d, 110 + (1 - sl) * 600, 400, "Alarma siesta", q, sub="menos de 30 min")
    pop_line(d, lt, 1.2, 540, 760, "¿VOS DORMÍS", 140, C)
    pop_line(d, lt, 1.45, 540, 910, "SIESTA?", 160, Y)
    pill(d, lt, 1.9, 380, 1090, 220, "SÍ", fill=GREEN, ink=K, size=56, h=100)
    pill(d, lt, 2.05, 700, 1090, 220, "NO", fill=R, ink=C, size=56, h=100)
    slide_line(d, lt, 2.3, 540, 1230, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "whoosh"); ev(0.3, "pop"); ev(0.5, "thump"); ev(1.0, "rustle"); ev(2.2, "click")
ev(4.1, "swipe"); ev(4.3, "swipe"); ev(4.5, "whoosh", -0.4); ev(5.5, "pop", -0.3); ev(5.6, "pop", 0.3)
ev(6.3, "tap"); ev(6.45, "tap"); ev(6.7, "tap")
ev(8.1, "pop"); ev(8.3, "pop")
for k in range(15): ev(8.5 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(10.15, "stamp"); ev(10.6, "tap")
ev(12.1, "swipe"); ev(12.5, "shimmer", -0.3); ev(13.1, "shimmer", 0.3); ev(14.2, "thump"); ev(14.5, "tap"); ev(14.7, "tap")
ev(16.1, "pop"); ev(16.35, "thump"); ev(16.6, "pop"); ev(17.3, "rustle"); ev(17.5, "swipe"); ev(18.0, "tap"); ev(18.15, "tap")
ev(20.1, "swipe"); ev(20.2, "click"); ev(20.4, "toggle"); ev(20.6, "ding"); ev(21.2, "pop"); ev(21.45, "thump")
ev(21.9, "pop", -0.3); ev(22.05, "pop", 0.3); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
