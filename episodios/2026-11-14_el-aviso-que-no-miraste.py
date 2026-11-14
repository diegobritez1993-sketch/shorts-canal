"""Short 2026-11-14 15:00 — Cómo te enganchan las apps: un aviso que no mirás igual te distrae.

Fuente:
- Stothart, Mitchum y Yehnert (2015), "The attentional cost of receiving a cell phone notification",
  J. Exp. Psychology: Human Perception and Performance 41(4):893 (Florida State University).
  Vía Association for Psychological Science (APS), "You're A Distracted Driver Even When You Ignore That Text".
- 166 universitarios; tarea de atención (SART): apretar una tecla con cada número, menos con el 3.
- Grupos al azar: llamada, mensaje de texto o sin aviso; los investigadores llamaron/escribieron a su propio celular.
  No se les pidió revisar el celular.
- Los que recibieron un aviso cometieron más errores: "tres veces la probabilidad de equivocarse".
- El costo de atención fue comparable al de otros estudios donde la gente sí agarraba el celular.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

def x_mark(d, cx, cy, s, col=R, w=18):
    d.line([S(cx - s), S(cy - s), S(cx + s), S(cy + s)], fill=col, width=S(w))
    d.line([S(cx - s), S(cy + s), S(cx + s), S(cy - s)], fill=col, width=S(w))

def check(d, cx, cy, s, col=GREEN, w=18):
    d.line([S(cx - s), S(cy), S(cx - s * 0.3), S(cy + s * 0.7), S(cx + s), S(cy - s * 0.7)], fill=col, width=S(w), joint="curve")

def notif_card(d, cx, cy, w, p, title, sub, col=Y):
    """Tarjeta de notificación genérica que baja desde arriba."""
    if p <= 0.01: return
    yy = cy - (1 - ease_out(p)) * 120
    rrect(d, cx - w / 2, yy - 70, cx + w / 2, yy + 70, 34, fill=(40, 40, 40))
    rrect(d, cx - w / 2 + 26, yy - 40, cx - w / 2 + 106, yy + 40, 20, fill=col)
    bell(d, cx - w / 2 + 66, yy + 2, 60, K)
    text_l(d, cx - w / 2 + 130, yy - 20, title, "Bold", 38, C)
    text_l(d, cx - w / 2 + 130, yy + 26, sub, "SemiBold", 30, G)

def b1(d, t):
    # celu boca abajo vibrando en la mesa + aviso
    bz = 1.0 if (t % 0.9) < 0.45 and t > 0.2 else 0.0
    e = back(prog(t, 0.0, 0.35))
    if e > 0.02:
        phone(d, 540, 640, 300 * e, 520 * e, buzz=bz, t=t)
        if e > 0.9:
            circle(d, 540 + 130, 640 - 240, 46, fill=R)
            text_c(d, 540 + 130, 640 - 242, "1", "Black", 50, C, bg=R)
    pop_line(d, t, 0.0, 540, 1040, "¿TE LLEGÓ UN AVISO", 120, C)
    pop_line(d, t, 0.3, 540, 1180, "Y NO LO MIRASTE?", 120, C)
    pop_line(d, t, 1.4, 540, 1360, "IGUAL TE DISTRAJO", 125, Y)
    pill(d, t, 2.4, 540, 1530, 640, "LO MIDIÓ UN EXPERIMENTO", fill=R, ink=C, size=40, h=92)

def b2(d, t):
    lt = t - 4
    n = int(round(166 * ease_out(prog(lt, 0.1, 1.0))))
    pop_line(d, lt, 0.05, 540, 300, fmt_num(n), 200, Y)
    slide_line(d, lt, 0.3, 540, 450, "UNIVERSITARIOS", 110, C)
    # pantalla con números que cambian; el 3 aparece en rojo
    q = back(prog(lt, 0.7, 0.35))
    if q > 0.02:
        rrect(d, 540 - 260 * q, 560, 540 + 260 * q, 960, 50, fill=K2, outline=C, width=6)
        if q > 0.9:
            seq = [7, 2, 9, 3, 5, 1, 8, 3, 6]
            k = int(max(0, lt - 0.9) / 0.32) % len(seq)
            num = seq[k]
            col = R if num == 3 else C
            text_c(d, 540, 750, str(num), "A", 260, col, bg=K2)
            if num == 3:
                ban(d, 540, 760, 150, 1.0, width=20)
    slide_line(d, lt, 1.4, 540, 1050, "tenían que apretar una tecla", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.55, 540, 1120, "con cada número…", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.0, 540, 1240, 520, "MENOS CON EL 3", fill=R, ink=C, size=50, h=100)
    slide_line(d, lt, 2.6, 540, 1370, "Stothart et al., Florida State Univ., 2015", 32, G, kind="SemiBold", dy=20)

def b3(d, t):
    lt = t - 8
    pop_line(d, lt, 0.1, 540, 290, "EN PLENA TAREA", 130, C)
    pop_line(d, lt, 0.3, 540, 420, "LES SONÓ EL CELU", 120, Y)
    bz = 1.0 if 0.8 < lt < 2.4 and (lt % 0.5) < 0.3 else 0.0
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        phone(d, 540, 890, 220 * e, 370 * e, buzz=bz, t=t)
    notif_card(d, 540, 590, 760, prog(lt, 0.9, 0.35), "Mensaje nuevo", "tocá para ver", col=Y)
    pill(d, lt, 1.7, 360, 1180, 300, "LLAMADA", fill=C, ink=K, size=44, h=92)
    pill(d, lt, 1.85, 720, 1180, 300, "MENSAJE", fill=C, ink=K, size=44, h=92)
    slide_line(d, lt, 2.2, 540, 1300, "a su propio celular, y nadie", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.35, 540, 1370, "les pidió que lo miraran", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "RESULTADO:", 120, C)
    # dos columnas: sin aviso / con aviso
    for i, (lab, col) in enumerate([("SIN AVISO", C), ("CON AVISO", Y)]):
        x = 300 + i * 480
        p = ease_out(prog(lt, 0.4 + i * 0.2, 0.3))
        if p > 0:
            rrect(d, x - 200, 420, x + 200, 500, 40, fill=K2)
            text_c(d, x, 460, lab, "Black", 40, col, alpha=p, bg=K2)
    # errores
    if lt > 0.8:
        x_mark(d, 300, 640, 50 * back(prog(lt, 0.8, 0.25)))
    for k in range(3):
        tk = 1.1 + k * 0.3
        if lt > tk:
            x_mark(d, 780, 600 + k * 130 - 0, 50 * back(prog(lt, tk, 0.25)))
    sx, sy = shake(lt, 2.15, 0.35, 14)
    stamp(d, lt, 2.1, 540 + sx, 1060 + sy, 330, 100, "3 VECES", fill=R, ink=C, size=140)
    slide_line(d, lt, 2.5, 540, 1240, "más probable equivocarse", 52, C, kind="Bold", dy=25)
    slide_line(d, lt, 2.7, 540, 1320, "J. Exp. Psychology: HPP 2015 (vía APS)", 32, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    pop_line(d, lt, 0.1, 540, 290, "NI LO TOCARON", 140, C)
    pop_line(d, lt, 0.35, 540, 430, "Y SE DISTRAJERON", 120, Y)
    # cabeza con burbujas de pensamiento que se van al celu
    e = back(prog(lt, 0.5, 0.35))
    if e > 0.02:
        person(d, 330, 860, 340 * e, C)
        for k in range(3):
            pk = prog(lt, 0.9 + k * 0.2, 0.2)
            if pk > 0:
                circle(d, 460 + k * 70, 760 - k * 30, (16 + k * 12) * back(pk), fill=Y)
        pp = back(prog(lt, 1.5, 0.3))
        if pp > 0.02:
            phone(d, 790, 690, 150 * pp, 250 * pp, buzz=1.0 if (lt % 0.5) < 0.25 else 0.0, t=t)
            text_c(d, 790, 700, "?", "A", 110 * pp, Y, bg=K2)
    slide_line(d, lt, 1.9, 540, 1130, "casi como en otros estudios", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.05, 540, 1200, "donde la gente sí agarraba el celu", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.5, 540, 1330, 700, "LA CABEZA SE VA AL AVISO", fill=Y, ink=K, size=42, h=92)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 290, "EL TRUCO:", 120, Y)
    q = ease_in_out(prog(lt, 0.5, 0.3))
    sl = ease_out(prog(lt, 0.2, 0.35))
    if sl > 0:
        toggle_row(d, 110 + (1 - sl) * 600, 420, "No molestar", q, sub="para concentrarte")
    pop_line(d, lt, 1.1, 540, 780, "SIN SONIDO", 130, C)
    pop_line(d, lt, 1.35, 540, 920, "Y SIN VIBRAR", 130, C)
    pill(d, lt, 1.8, 540, 1100, 620, "Y EL CELU LEJOS", fill=R, ink=C, size=48, h=100)
    slide_line(d, lt, 2.2, 540, 1240, "mandáselo a alguien que estudia", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "pop"); ev(0.3, "pop")
for k in range(4): ev(0.2 + k * 0.9, "buzz", 0.2 if k % 2 else -0.2)
ev(1.4, "thump"); ev(2.4, "click")
ev(4.05, "pop")
for k in range(10): ev(4.1 + k * 0.1, "tick", -0.2 if k % 2 else 0.2)
ev(4.3, "swipe"); ev(4.7, "pop"); ev(5.4, "swipe"); ev(5.55, "swipe"); ev(6.0, "thump"); ev(6.6, "tap")
ev(8.1, "pop"); ev(8.3, "pop"); ev(8.5, "pop")
for k in range(4): ev(8.8 + k * 0.5, "buzz", 0.0)
ev(8.9, "ding"); ev(9.7, "tap", -0.3); ev(9.85, "tap", 0.3); ev(10.2, "swipe"); ev(10.35, "swipe")
ev(12.1, "swipe"); ev(12.4, "tap", -0.3); ev(12.6, "tap", 0.3)
ev(12.8, "thump", -0.4); ev(13.1, "thump", 0.4); ev(13.4, "thump", 0.4); ev(13.7, "thump", 0.4)
ev(14.1, "stamp"); ev(14.5, "swipe"); ev(14.7, "tap")
ev(16.1, "pop"); ev(16.35, "thump"); ev(16.5, "pop")
ev(16.9, "tap"); ev(17.1, "tap"); ev(17.3, "tap"); ev(17.5, "pop"); ev(17.6, "buzz", 0.4)
ev(17.9, "swipe"); ev(18.05, "swipe"); ev(18.5, "click")
ev(20.1, "swipe"); ev(20.2, "click"); ev(20.5, "toggle"); ev(21.1, "pop"); ev(21.35, "pop"); ev(21.8, "thump"); ev(22.2, "swipe")

if __name__ == "__main__":
    main(BEATS_EP)
