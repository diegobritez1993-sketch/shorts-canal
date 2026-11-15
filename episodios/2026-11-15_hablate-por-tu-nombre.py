"""Short 2026-11-15 20:00 — Mente y emociones: hablarte por tu nombre para los nervios (autodistanciamiento).

Fuente:
- Kross et al., "Self-talk as a regulatory mechanism: How you do it matters",
  Journal of Personality and Social Psychology, feb. 2014. Universidad de Michigan.
  Comunicado U. de Michigan, Depto. de Psicología (05/02/2014) "Talking in the 3rd person lowers anxiety: Study"
  y nota de Business Insider republicada por U. de Michigan (jun. 2015).
- Universitarios tenían que dar un discurso sobre por qué estaban calificados para el trabajo de sus sueños,
  con 5 minutos para prepararlo. Antes escribían cómo se preparaban: un grupo con "yo", otros con "vos"/su nombre.
- Los de "yo" anotaron pensamientos ansiosos ("¿cómo voy a escribir un discurso en 5 minutos?");
  los que usaron su nombre mostraron más confianza ("Vos podés, John"), jueces independientes los vieron
  rendir mejor y después le dieron menos vueltas y sintieron menos vergüenza.
- Kross: pensarte como si fueras otra persona da "espacio psicológico", como cuando aconsejás a un amigo.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def mic(d, cx, cy, s, col=C):
    rrect(d, cx - s * 0.18, cy - s * 0.5, cx + s * 0.18, cy + s * 0.1, s * 0.18, fill=col)
    d.arc([S(cx - s * 0.32), S(cy - s * 0.3), S(cx + s * 0.32), S(cy + s * 0.3)], 0, 180, fill=col, width=int(S(s * 0.07)))
    d.line([S(cx), S(cy + s * 0.3), S(cx), S(cy + s * 0.5)], fill=col, width=int(S(s * 0.07)))
    d.line([S(cx - s * 0.2), S(cy + s * 0.5), S(cx + s * 0.2), S(cy + s * 0.5)], fill=col, width=int(S(s * 0.07)))

def chat(d, t, t0, x0, y, w, txt, fill, ink, right=False, size=44):
    """Globo de chat que entra desde el costado."""
    p = prog(t, t0, 0.3)
    if p <= 0: return
    e = back(p, 1.4)
    h = 130
    off = (1 - e) * (300 if right else -300)
    rrect(d, x0 + off, y, x0 + w + off, y + h, 50, fill=fill)
    tx = x0 + w - 40 if right else x0 + 40
    tail = [(S(tx + off), S(y + h - 10)), (S(tx + off + (30 if right else -30)), S(y + h + 30)), (S(tx + off + (-40 if right else 40)), S(y + h - 10))]
    d.polygon(tail, fill=fill)
    text_c(d, x0 + w / 2 + off, y + h / 2, txt, "Bold", size, ink, alpha=clamp(p * 2), bg=fill)

def heartbeat(d, x0, x1, cy, amp, t, col, calm):
    """Línea de pulso: calm 0 = agitado, 1 = tranquilo."""
    pts = []
    n = 120
    freq = lerp(5, 2, calm)
    for i in range(n + 1):
        u = i / n
        ph = (u * freq + t * 0.8) % 1.0
        a = 0
        if 0.45 < ph < 0.5: a = -amp * lerp(1, 0.5, calm)
        elif 0.5 <= ph < 0.55: a = amp * 0.6 * lerp(1, 0.5, calm)
        pts.append((S(lerp(x0, x1, u)), S(cy + a)))
    d.line(pts, fill=col, width=S(10), joint="curve")

def b1(d, t):
    pop_line(d, t, 0.0, 540, 320, "¿NERVIOS?", 200, Y)
    pop_line(d, t, 0.3, 540, 500, "HABLATE POR", 140, C)
    pop_line(d, t, 0.5, 540, 650, "TU NOMBRE", 160, C)
    # "YO" tachado → "VOS"
    pk = back(prog(t, 1.2, 0.3))
    if pk > 0.02:
        circle(d, 330, 960, 150 * pk, fill=K2)
        text_c(d, 330, 960, "YO", "A", 120, C, scale=pk, bg=K2)
    q = ease_out(prog(t, 1.7, 0.25))
    if q > 0:
        d.line([S(220), S(1070), S(220 + 220 * q), S(1070 - 220 * q)], fill=R, width=S(22))
    pv = back(prog(t, 2.1, 0.3))
    if pv > 0.02:
        circle(d, 750, 960, 150 * pv, fill=Y)
        text_c(d, 750, 960, "JUAN", "A", 95, K, scale=pv, bg=Y)
    slide_line(d, t, 2.6, 540, 1230, "(o como te llames)", 46, G, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    pop_line(d, lt, 0.05, 540, 290, "EL EXPERIMENTO", 130, C)
    e = back(prog(lt, 0.3, 0.35))
    if e > 0.02:
        mic(d, 300, 640, 300 * e, C)
    # reloj de 5 minutos
    ce = ease_out(prog(lt, 0.6, 0.3))
    if ce > 0.01:
        clock(d, 760, 640, 170 * ce, ease_in_out(prog(lt, 0.9, 2.0)), turns=1, fill_deg=360)
        pop_line(d, lt, 1.0, 760, 870, "5 MINUTOS", 80, Y)
    slide_line(d, lt, 1.5, 540, 1010, "para preparar un discurso:", 48, C, kind="SemiBold", dy=25)
    pill(d, lt, 1.9, 540, 1130, 980, "¿POR QUÉ MERECÉS TU TRABAJO SOÑADO?", fill=Y, ink=K, size=34, h=100)
    slide_line(d, lt, 2.5, 540, 1260, "Kross et al., Univ. de Michigan, J. Pers. Soc. Psychol. 2014", 30, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.05, 540, 280, "ANTES SE HABLABAN:", 105, C)
    pill(d, lt, 0.4, 260, 440, 300, "CON \"YO\"", fill=K2, ink=C, size=40, h=90)
    chat(d, lt, 0.6, 90, 520, 900, "¿cómo voy a hacer esto en 5 min?", K2, C)
    pill(d, lt, 1.5, 760, 790, 460, "CON SU NOMBRE", fill=Y, ink=K, size=36, h=90)
    chat(d, lt, 1.7, 90, 870, 900, "vos podés, Juan", Y, K, right=True, size=52)
    stamp(d, lt, 2.5, 540, 1230, 290, 90, "¿Y QUÉ PASÓ?", fill=R, ink=C, size=95)

def b4(d, t):
    lt = t - 12
    pop_line(d, lt, 0.05, 540, 280, "LOS QUE USARON", 125, C)
    pop_line(d, lt, 0.25, 540, 410, "SU NOMBRE:", 125, Y)
    rows = [("MÁS CONFIANZA", "antes de hablar"),
            ("MEJOR DISCURSO", "según jueces independientes"),
            ("MENOS VUELTAS", "y menos vergüenza después")]
    for k, (a, b) in enumerate(rows):
        p = prog(lt, 0.7 + k * 0.5, 0.3)
        if p <= 0: continue
        e = ease_out(p)
        y = 540 + k * 210
        x0 = 90 + (1 - e) * -500
        rrect(d, x0, y, x0 + 900, y + 175, 40, fill=K2)
        circle(d, x0 + 95, y + 87, 50, fill=GREEN)
        d.line([S(x0 + 72), S(y + 88), S(x0 + 90), S(y + 106), S(x0 + 120), S(y + 66)], fill=K, width=S(11), joint="curve")
        text_l(d, x0 + 180, y + 62, a, "Black", 50, C)
        text_l(d, x0 + 180, y + 122, b, "SemiBold", 34, Y)
    hb = ease_out(prog(lt, 2.2, 0.4))
    if hb > 0:
        heartbeat(d, 120, 120 + 840 * hb, 1300, 80, lt, R if lt < 2.9 else GREEN, ease_in_out(prog(lt, 2.4, 1.0)))

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.05, 540, 280, "¿POR QUÉ FUNCIONA?", 115, C)
    # dos personas: amigo aconsejando
    for k, (x, col) in enumerate([(330, C), (750, Y)]):
        pk = back(prog(lt, 0.4 + k * 0.25, 0.3))
        if pk > 0.02:
            person(d, x, 700, 300 * pk, col)
    r = back(prog(lt, 1.0, 0.3))
    if r > 0.02:
        bubble(d, 560, 470, 170 * r, Y)
    slide_line(d, lt, 1.3, 540, 940, "es como aconsejar a un amigo:", 48, C, kind="SemiBold", dy=25)
    pop_line(d, lt, 1.7, 540, 1080, "VES EL PANORAMA", 120, Y)
    pop_line(d, lt, 1.9, 540, 1210, "COMPLETO", 120, Y)
    slide_line(d, lt, 2.4, 540, 1340, "\"te da espacio psicológico\", dice Kross", 40, G, kind="SemiBold", dy=20)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 300, "PROBALO ANTES DE", 110, C)
    slide_line(d, lt, 0.25, 540, 420, "UN EXAMEN O UNA CHARLA", 86, Y)
    pop_line(d, lt, 0.9, 540, 640, "¿TE HABLÁS", 150, C)
    pop_line(d, lt, 1.1, 540, 790, "A VOS MISMO?", 150, Y)
    for k, (lab, col, x) in enumerate([("SÍ", GREEN, 360), ("NO", R, 720)]):
        pk = back(prog(lt, 1.5 + k * 0.2, 0.3))
        if pk > 0.02:
            circle(d, x, 1010, 115 * pk, fill=col)
            if pk > 0.7:
                text_c(d, x, 1005, lab, "A", 100, K, bg=col)
    slide_line(d, lt, 2.1, 540, 1200, "si los nervios te superan seguido, buscá ayuda", 36, C, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop"); ev(0.3, "pop"); ev(0.5, "pop"); ev(1.2, "pop", -0.4); ev(1.7, "swipe", -0.4)
ev(2.1, "pop", 0.4); ev(2.15, "shimmer"); ev(2.6, "tap")
ev(4.05, "pop"); ev(4.3, "pop", -0.3); ev(4.6, "pop", 0.3)
for k in range(20): ev(4.9 + k * 0.1, "tick", 0.3)
ev(5.0, "thump"); ev(5.5, "swipe"); ev(5.9, "click"); ev(6.5, "tap")
ev(8.05, "pop"); ev(8.4, "click", -0.3); ev(8.6, "swipe", -0.4); ev(8.65, "pop", -0.4); ev(9.5, "click", 0.3); ev(9.7, "swipe", 0.4)
ev(9.75, "pop", 0.4); ev(10.5, "stamp")
ev(12.05, "pop"); ev(12.25, "thump")
for k in range(3): ev(12.7 + k * 0.5, "swipe", -0.3); ev(12.85 + k * 0.5, "ding" if k == 0 else "pop", 0)
ev(14.2, "rustle"); ev(14.9, "shimmer")
ev(16.05, "pop"); ev(16.4, "pop", -0.4); ev(16.65, "pop", 0.4); ev(17.0, "pop"); ev(17.3, "swipe")
ev(17.7, "thump"); ev(17.9, "pop"); ev(18.4, "tap")
ev(20.05, "swipe"); ev(20.25, "swipe"); ev(20.9, "pop"); ev(21.1, "thump"); ev(21.5, "pop", -0.3); ev(21.7, "pop", 0.3); ev(22.1, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
