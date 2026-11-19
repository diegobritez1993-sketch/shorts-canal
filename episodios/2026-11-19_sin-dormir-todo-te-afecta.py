"""Short 2026-11-19 20:00 — Mente y emociones: dormir mal dispara la "alarma" emocional del cerebro.

Fuente:
- Yoo, Gujar, Hu, Jolesz y Walker, Current Biology 22/10/2007 (UC Berkeley y Harvard Medical School).
- Comunicado UC Berkeley (22/10/2007): 26 adultos sanos de 18 a 30 años en 2 grupos; un grupo estuvo despierto
  35 horas seguidas, el otro durmió normal. En resonancia vieron 100 imágenes, de neutras a muy negativas.
  En los que no durmieron, la amígdala (centro de alerta del cerebro) reaccionó "más de 60%" más.
  Sin sueño se debilitó la conexión con la corteza prefrontal (la que razona y calma la reacción) y se conectó
  más con el locus coeruleus (noradrenalina). Walker: el cerebro "volvió a patrones más primitivos".
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *
def SW(v): return max(1, int(S(v)))

def siren(d, cx, cy, s, t, on=True):
    """Luz de alarma con destellos."""
    col = R if on else (90, 30, 30)
    d.pieslice([S(cx - s * 0.5), S(cy - s * 0.55), S(cx + s * 0.5), S(cy + s * 0.45)], 180, 360, fill=col)
    rrect(d, cx - s * 0.5, cy - s * 0.06, cx + s * 0.5, cy + s * 0.08, 6, fill=col)
    rrect(d, cx - s * 0.65, cy + s * 0.08, cx + s * 0.65, cy + s * 0.25, 10, fill=C)
    if on:
        f = 0.5 + 0.5 * math.sin(t * 18)
        for k in range(5):
            a = math.radians(-160 + k * 35)
            r0, r1 = s * 0.65, s * (0.85 + 0.12 * f)
            d.line([S(cx + math.cos(a) * r0), S(cy - s * 0.1 + math.sin(a) * r0),
                    S(cx + math.cos(a) * r1), S(cy - s * 0.1 + math.sin(a) * r1)], fill=mix(K, Y, 0.5 + 0.5 * f), width=SW(14))

def brain_blob(d, cx, cy, r, col, label, lsize=40):
    circle(d, cx, cy, r, fill=col)
    text_c(d, cx, cy, label, "Black", lsize, K, bg=col)

def b1(d, t):
    pop_line(d, t, 0.0, 540, 300, "¿DORMISTE MAL", 145, C, dur=0.25)
    pop_line(d, t, 0.25, 540, 450, "Y HOY TODO", 145, C, dur=0.25)
    pop_line(d, t, 0.5, 540, 610, "TE IRRITA?", 180, R, dur=0.25)
    e = back(prog(t, 0.8, 0.35))
    if e > 0.02:
        lvl = 0.8 * (1 - ease_out(prog(t, 1.2, 1.2))) + 0.08
        col = GREEN if lvl > 0.5 else (Y if lvl > 0.25 else R)
        battery(d, 540, 960, 520 * e, 230 * e, lvl, col)
        if t > 2.4:
            sx, sy = shake(t, 2.4, 0.3, 10)
            text_c(d, 540 + sx, 960 + sy, "!", "A", 160, C, bg=K)
    slide_line(d, t, 2.6, 540, 1250, "no es tu imaginación:", 52, C, kind="SemiBold", dy=25)
    slide_line(d, t, 2.8, 540, 1320, "lo midieron en el cerebro", 52, Y, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 280, "26 PERSONAS", 140, C)
    slide_line(d, lt, 0.3, 540, 390, "adultos sanos de 18 a 30 años, en 2 grupos", 42, C, kind="SemiBold", dy=20)
    # grupo A: durmió / grupo B: despierto 35 h
    pa = back(prog(lt, 0.6, 0.35))
    if pa > 0.02:
        person(d, 290, 720, 260 * pa, C)
        moon(d, 380, 560, 50 * pa)
        if lt > 1.0: zzz(d, 400, 750, lt)
        text_c(d, 290, 930, "DURMIÓ", "A", 80, GREEN, alpha=clamp(pa))
        text_c(d, 290, 1000, "normal", "SemiBold", 38, C, alpha=clamp(pa))
    pb = prog(lt, 1.0, 0.35)
    if pb > 0:
        e = back(pb)
        h = int(35 * ease_out(prog(lt, 1.3, 1.4)))
        clock(d, 790, 680, 150 * e, prog(lt, 1.3, 1.4), turns=3, fill_deg=300)
        text_c(d, 790, 930, f"{h} HORAS", "A", 80, R, alpha=clamp(pb * 2))
        text_c(d, 790, 1000, "despiertos seguidos", "SemiBold", 38, C, alpha=clamp(pb * 2))
    slide_line(d, lt, 2.8, 540, 1160, "después: resonancia mirando 100 imágenes", 42, Y, kind="Bold", dy=20)
    slide_line(d, lt, 3.0, 540, 1220, "de neutras a muy feas", 42, C, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 270, "LA ALARMA DEL CEREBRO", 100, C)
    slide_line(d, lt, 0.3, 540, 370, "(la amígdala) en los que no durmieron:", 42, C, kind="SemiBold", dy=20)
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        siren(d, 540, 590, 200 * e, t, on=lt > 0.9)
    v = 60 * ease_out(prog(lt, 0.9, 1.0))
    if lt > 0.9:
        sx, sy = shake(lt, 1.9, 0.3, 16)
        text_c(d, 540 + sx, 900 + sy, f"+{int(round(v))}%", "A", 280, R)
    pop_line(d, lt, 1.95, 540, 1100, "MÁS REACTIVA", 120, C)
    slide_line(d, lt, 2.3, 540, 1210, "\"más de 60%\", según el autor, Matthew Walker", 40, Y, kind="Bold", dy=20)
    slide_line(d, lt, 2.6, 540, 1290, "Yoo y cols., UC Berkeley y Harvard, Current Biology 2007", 30, G, kind="SemiBold", dy=20)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 280, "Y EL FRENO", 140, C)
    pop_line(d, lt, 0.35, 540, 420, "SE DESCONECTA", 130, R)
    pa = back(prog(lt, 0.8, 0.3))
    pb = back(prog(lt, 1.0, 0.3))
    # cable entre "razón" y "alarma" que se corta
    cut = prog(lt, 1.8, 0.3)
    if pa > 0.02 and pb > 0.02:
        if cut <= 0:
            d.line([S(330), S(700), S(750), S(700)], fill=Y, width=SW(16))
        else:
            g = 40 * ease_out(cut)
            d.line([S(330), S(700), S(540 - g), S(700 + g * 0.6)], fill=Y, width=SW(16))
            d.line([S(540 + g), S(700 - g * 0.6), S(750), S(700)], fill=Y, width=SW(16))
            if cut < 1:
                for k in range(6):
                    a = k * math.tau / 6 + lt * 3
                    circle(d, 540 + math.cos(a) * 60 * cut, 700 + math.sin(a) * 60 * cut, 8, fill=Y)
    if pa > 0.02: brain_blob(d, 280, 700, 140 * pa, GREEN, "RAZÓN" if pa > 0.8 else "", 40)
    if pb > 0.02:
        sx, sy = shake(lt, 2.0, 1.5, 8)
        brain_blob(d, 800 + sx, 700 + sy, 140 * pb, R, "ALARMA" if pb > 0.8 else "", 38)
    slide_line(d, lt, 2.2, 540, 950, "la parte que razona y te calma", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.35, 540, 1010, "pierde el control de la alarma", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.7, 540, 1120, "\"patrones más primitivos\"", 56, Y, kind="Black", dy=20)
    slide_line(d, lt, 3.0, 540, 1200, "comunicado UC Berkeley, 22/10/2007", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 270, "OJO CON ESTO", 140, Y)
    slide_line(d, lt, 0.35, 540, 380, "si dormiste mal, antes de reaccionar:", 44, C, kind="SemiBold", dy=20)
    rows = [("Discutir cansado", None, 0.0, 0.6), ("Dejarlo para mañana", "dormí y después hablalo", 1.0, 1.0),
            ("Contestar en caliente", None, 0.0, 1.4)]
    for k, (lab, sub, target, t0) in enumerate(rows):
        p = prog(lt, t0, 0.3)
        if p <= 0: continue
        e = ease_out(p)
        q = lerp(1 - target, target, ease_in_out(prog(lt, t0 + 0.4, 0.3)))
        toggle_row(d, 110 + (1 - e) * 80, 480 + k * 190, lab, q, sub=sub)
    slide_line(d, lt, 2.3, 540, 1120, "si no podés dormir seguido", 46, C, kind="SemiBold", dy=20)
    slide_line(d, lt, 2.45, 540, 1180, "o te sentís mal muchos días: consultá", 46, C, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    pop_line(d, lt, 0.1, 540, 330, "¿CUÁNTAS HORAS", 150, C)
    pop_line(d, lt, 0.35, 540, 490, "DORMISTE ANOCHE?", 135, Y)
    e = back(prog(lt, 0.7, 0.35))
    if e > 0.02:
        moon(d, 540, 760, 130 * e)
        if lt > 1.0: zzz(d, 690, 880, lt, Y)
    pill(d, t, 21.6, 540, 1010, 640, "¿MENOS DE 6? ¿MÁS?", fill=C, ink=K, size=50, h=120)
    slide_line(d, lt, 2.0, 540, 1160, "contalo en los comentarios", 46, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "pop", -0.3); ev(0.25, "pop", 0.3); ev(0.5, "thump")
ev(0.8, "pop"); ev(1.4, "tick"); ev(1.8, "tick"); ev(2.2, "tick"); ev(2.4, "buzz"); ev(2.6, "tap"); ev(2.8, "tap")
ev(4.1, "tap"); ev(4.3, "tap"); ev(4.6, "pop", -0.4); ev(5.0, "pop", 0.4)
for k in range(8): ev(5.3 + k * 0.17, "tick", 0.4)
ev(6.8, "tap"); ev(7.0, "tap")
ev(8.1, "tap"); ev(8.3, "tap"); ev(8.5, "pop"); ev(8.9, "buzz")
for k in range(10): ev(8.9 + k * 0.1, "tick")
ev(9.9, "thump"); ev(9.95, "pop"); ev(10.3, "tap"); ev(10.6, "tap")
ev(12.1, "tap"); ev(12.35, "thump"); ev(12.8, "pop", -0.4); ev(13.0, "pop", 0.4); ev(13.8, "stamp"); ev(14.0, "buzz", 0.4)
ev(14.2, "tap"); ev(14.35, "tap"); ev(14.7, "pop"); ev(15.0, "tap")
ev(16.1, "tap"); ev(16.35, "tap"); ev(16.6, "swipe"); ev(17.0, "toggle"); ev(17.0, "swipe"); ev(17.4, "toggle"); ev(17.4, "swipe"); ev(17.8, "toggle")
ev(18.3, "tap"); ev(18.45, "tap")
ev(20.1, "pop", -0.3); ev(20.35, "thump"); ev(20.7, "pop"); ev(21.0, "shimmer"); ev(21.6, "pop"); ev(22.0, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
