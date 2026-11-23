"""Short 2026-11-23 15:00 — Curiosidades y hábitos.
¿Por qué no te podés hacer cosquillas? Tu cerebro predice tu propio toque y le baja el volumen.
Fuente: Blakemore, Frith y Wolpert (UCL), "Spatio-Temporal Prediction Modulates the Perception of
Self-Produced Stimuli", Journal of Cognitive Neuroscience 11(5), 1999: 16 personas (19-30 años), robot,
demoras de 100/200/300 ms y giros de 30/60/90°; con 200 ms o 90° ya no se distinguía de que te lo haga otro.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

PINK = (255, 120, 150)

def feather(d, cx, cy, s, ang, col=C):
    """Pluma: eje + vane en forma de hoja, rotada ang (rad)."""
    ca, sa = math.cos(ang), math.sin(ang)
    def P(x, y): return (S(cx + x * ca - y * sa), S(cy + x * sa + y * ca))
    pts = []
    for k in range(21):
        u = k / 20
        pts.append(P(lerp(-0.5, 0.5, u) * s, -math.sin(u * math.pi) * 0.16 * s))
    for k in range(20, -1, -1):
        u = k / 20
        pts.append(P(lerp(-0.5, 0.5, u) * s, math.sin(u * math.pi) * 0.13 * s))
    d.polygon(pts, fill=col)
    for k in range(1, 8):
        u = k / 8
        x = lerp(-0.5, 0.5, u) * s
        d.line([P(x, 0), P(x + 0.06 * s, -math.sin(u * math.pi) * 0.16 * s)], fill=K, width=S(3))
    d.line([P(-0.62 * s, 0), P(0.5 * s, 0)], fill=K2 if col != K2 else C, width=S(6))
    d.line([P(-0.68 * s, 0), P(-0.5 * s, 0)], fill=col, width=S(8))

def hand(d, cx, cy, s, col=C):
    """Mano abierta (palma vista de frente)."""
    rrect(d, cx - s * 0.36, cy - s * 0.1, cx + s * 0.36, cy + s * 0.55, s * 0.16, fill=col)
    for i, (dx, h) in enumerate([(-0.27, 0.42), (-0.09, 0.52), (0.09, 0.5), (0.27, 0.4)]):
        rrect(d, cx + (dx - 0.075) * s, cy - h * s, cx + (dx + 0.075) * s, cy + 0.05 * s, s * 0.075, fill=col)
    d.polygon([(S(cx - 0.34 * s), S(cy + 0.32 * s)), (S(cx - 0.62 * s), S(cy + 0.02 * s)),
               (S(cx - 0.5 * s), S(cy - 0.06 * s)), (S(cx - 0.25 * s), S(cy + 0.12 * s))], fill=col)
    circle(d, cx - 0.56 * s, cy - 0.02 * s, s * 0.075, fill=col)

def brain(d, cx, cy, s, col=PINK):
    for (dx, dy, r) in [(-0.25, -0.1, 0.3), (0.0, -0.22, 0.3), (0.25, -0.1, 0.3), (-0.18, 0.12, 0.28), (0.18, 0.12, 0.28)]:
        circle(d, cx + dx * s, cy + dy * s, r * s, fill=col)
    d.line([S(cx), S(cy - 0.45 * s), S(cx), S(cy + 0.35 * s)], fill=mix(col, K, 0.35), width=S(8))
    for k in (-1, 1):
        d.arc([S(cx + k * 0.25 * s - 0.15 * s), S(cy - 0.25 * s), S(cx + k * 0.25 * s + 0.15 * s), S(cy + 0.05 * s)],
              0, 180, fill=mix(col, K, 0.35), width=S(7))

def b1(d, t):
    # pluma que hace cosquillas a una mano, con texto grande desde el frame 1
    text_c(d, 540, 330, "¿POR QUÉ NO TE", "A", 125, C)
    text_c(d, 540, 480, "PODÉS HACER", "A", 125, C)
    pop_line(d, t, 0.0, 540, 650, "COSQUILLAS?", 170, Y, dur=0.25)
    e = back(prog(t, 0.3, 0.4))
    if e > 0.02:
        hand(d, 470, 1130, 330 * e, C)
        wig = math.sin(t * 14) * 0.25
        feather(d, 700 + math.sin(t * 7) * 25, 1000 + math.cos(t * 7) * 18, 340 * e, -0.7 + wig, Y)
    slide_line(d, t, 1.6, 540, 1470, "probalo ahora: no funciona", 48, C, kind="SemiBold", dy=25)
    pop_line(d, t, 2.3, 540, 1600, "Y HAY UNA RAZÓN", 110, Y)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 290, "TU CEREBRO", 140, C)
    slide_line(d, lt, 0.3, 540, 440, "SE ADELANTA", 150, Y)
    e = back(prog(lt, 0.4, 0.4))
    if e > 0.02:
        brain(d, 540, 760, 330 * e)
    # rayo de "predicción": puntos que viajan del cerebro hacia abajo
    if lt > 0.9:
        for k in range(5):
            u = ((lt - 0.9) * 1.2 + k / 5) % 1.0
            circle(d, 540, lerp(900, 1110, u), 12, fill=mix(K, Y, 1 - u))
    slide_line(d, lt, 1.2, 540, 1180, "cuando te movés, predice", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.4, 540, 1245, "lo que vas a sentir", 48, C, kind="SemiBold", dy=25)
    # barras de volumen que bajan
    q = ease_in_out(prog(lt, 2.0, 1.0))
    if lt > 1.8:
        for i in range(6):
            h = (60 + i * 38) * (1 - 0.75 * q)
            x = 380 + i * 64
            rrect(d, x, 1500 - h, x + 40, 1500, 10, fill=mix(Y, R, q) if i < 6 - int(q * 4) else (60, 60, 60))
    pill(d, lt, 2.4, 540, 1600, 620, "Y LE BAJA EL VOLUMEN", fill=R, ink=C, size=42, h=96)

def robot_arm(d, x, y, s, ang, col=(170, 170, 170)):
    """Brazo robótico simple de 2 tramos con una pluma de goma espuma en la punta."""
    rrect(d, x - 0.35 * s, y, x + 0.35 * s, y + 0.18 * s, 0.05 * s, fill=col)
    j1 = (x, y)
    j2 = (x + math.cos(ang) * 0.7 * s, y - math.sin(ang) * 0.7 * s)
    j3 = (j2[0] + 0.55 * s, j2[1] + 0.25 * s)
    d.line([S(j1[0]), S(j1[1]), S(j2[0]), S(j2[1])], fill=col, width=int(S(0.12 * s)))
    d.line([S(j2[0]), S(j2[1]), S(j3[0]), S(j3[1])], fill=col, width=int(S(0.1 * s)))
    for j in (j1, j2):
        circle(d, j[0], j[1], 0.09 * s, fill=C, outline=K, width=4)
    rrect(d, j3[0] - 0.08 * s, j3[1] - 0.06 * s, j3[0] + 0.14 * s, j3[1] + 0.12 * s, 0.04 * s, fill=Y)
    return j3

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 290, "LO PROBARON", 140, C)
    slide_line(d, lt, 0.3, 540, 430, "CON UN ROBOT", 140, Y)
    slide_line(d, lt, 0.6, 540, 545, "16 personas de 19 a 30 años", 46, C, kind="SemiBold", dy=25)
    e = ease_out(prog(lt, 0.5, 0.5))
    if e > 0.02:
        ang = 0.9 + 0.25 * math.sin(lt * 5)
        robot_arm(d, 330, 1060 + (1 - e) * 300, 330, ang)
        hand(d, 780, 1080 + (1 - e) * 300, 250, C)
    pop_line(d, lt, 1.4, 540, 1330, "MOVÍAN EL ROBOT", 100, C)
    slide_line(d, lt, 1.8, 540, 1440, "con una mano, y les tocaba la otra", 44, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.4, 540, 1560, "resultado: casi no daba cosquillas", 44, Y, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.6, 540, 1720, "Blakemore, Frith y Wolpert, UCL, J. Cognitive Neuroscience 1999", 28, G, kind="SemiBold", dy=15)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 290, "PERO SI EL ROBOT", 125, C)
    slide_line(d, lt, 0.3, 540, 430, "SE DEMORABA...", 125, Y)
    # cronómetro digital que cuenta de 0 a 200 ms
    e = back(prog(lt, 0.4, 0.35))
    if e > 0.02:
        rrect(d, 540 - 330 * e, 600, 540 + 330 * e, 860, 50, fill=K2, outline=C, width=8)
        ms = int(200 * ease_in_out(prog(lt, 0.9, 1.0)))
        if e > 0.6:
            text_c(d, 540, 730, f"0,{ms:03d} s", "A", 150, Y if ms >= 200 else C, bg=K2)
    slide_line(d, lt, 1.0, 540, 930, "apenas 2 décimas de segundo", 46, C, kind="SemiBold", dy=25)
    # medidor de cosquillas que sube
    q = ease_in_out(prog(lt, 1.8, 1.0))
    if lt > 1.5:
        text_c(d, 540, 1060, "COSQUILLÓMETRO", "Black", 44, G)
        rrect(d, 160, 1110, 920, 1190, 40, fill=K2)
        if q > 0.02:
            rrect(d, 170, 1120, 170 + 740 * q, 1180, 30, fill=mix(Y, R, q))
    sx, sy = shake(lt, 2.85, 0.35, 16)
    pop_line(d, lt, 2.7, 540 + sx, 1340 + sy, "COSQUILLAS", 150, Y, dur=0.28)
    slide_line(d, lt, 3.0, 540, 1470, "igual que si te las hace otro", 46, C, kind="SemiBold", dy=25)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "Y SI CAMBIABA", 130, C)
    slide_line(d, lt, 0.3, 540, 430, "LA DIRECCIÓN", 140, Y)
    # flecha que gira 0→90°
    rot = math.radians(90) * ease_in_out(prog(lt, 0.8, 1.0))
    e = back(prog(lt, 0.4, 0.35))
    if e > 0.02:
        cx, cy, L = 540, 860, 240 * e
        circle(d, cx, cy, 270 * e, outline=(60, 60, 60), width=6)
        d.pieslice([S(cx - 200 * e), S(cy - 200 * e), S(cx + 200 * e), S(cy + 200 * e)], -math.degrees(rot), 0, fill=mix(K, Y, 0.35))
        ex, ey = cx + math.cos(-rot) * L, cy + math.sin(-rot) * L
        d.line([S(cx), S(cy), S(ex), S(ey)], fill=C, width=S(22))
        a = -rot
        tip = [(ex + math.cos(a) * 50, ey + math.sin(a) * 50), (ex + math.cos(a + 2.4) * 50, ey + math.sin(a + 2.4) * 50),
               (ex + math.cos(a - 2.4) * 50, ey + math.sin(a - 2.4) * 50)]
        d.polygon([(S(x), S(y)) for x, y in tip], fill=C)
        circle(d, cx, cy, 22, fill=Y)
        if lt > 0.8:
            text_c(d, cx + 150, cy + 90, f"{int(math.degrees(rot))}°", "A", 90, Y)
    slide_line(d, lt, 2.0, 540, 1220, "giro de 90°: el cerebro ya no lo predice", 42, C, kind="SemiBold", dy=25)
    stamp(d, lt, 2.6, 540, 1420, 330, 95, "SORPRESA", fill=Y, ink=K, size=120)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.1, 540, 330, "LA CLAVE ES", 120, C)
    pop_line(d, lt, 0.3, 540, 480, "LA SORPRESA", 160, Y)
    slide_line(d, lt, 0.6, 540, 600, "por eso solo te las puede hacer otro", 44, C, kind="SemiBold", dy=25)
    e = back(prog(lt, 0.6, 0.35))
    if e > 0.02:
        feather(d, 540, 820, 380 * e, -0.3 + math.sin(lt * 10) * 0.2, Y)
    pop_line(d, lt, 1.3, 540, 1060, "¿VOS TENÉS MUCHAS", 100, C)
    pop_line(d, lt, 1.5, 540, 1180, "COSQUILLAS?", 130, Y)
    pill(d, lt, 1.9, 370, 1360, 260, "SÍ", fill=GREEN, ink=K, size=60, h=110)
    pill(d, lt, 2.05, 710, 1360, 260, "NO", fill=R, ink=C, size=60, h=110)
    slide_line(d, lt, 2.3, 540, 1490, "contalo en los comentarios", 44, C, kind="SemiBold", dy=25)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.3, "rustle")
for k in range(6): ev(0.6 + k * 0.17, "tap", 0.4 if k % 2 else -0.4)
ev(1.6, "tap"); ev(2.3, "pop")
ev(4.1, "tap", -0.3); ev(4.3, "pop", 0.3); ev(4.4, "shimmer")
for k in range(4): ev(4.9 + k * 0.25, "click", 0.2 if k % 2 else -0.2)
ev(5.2, "tap"); ev(5.4, "tap")
for k in range(5): ev(6.0 + k * 0.2, "tick", 0.3 if k % 2 else -0.3)
ev(6.4, "thump")
ev(8.1, "tap", -0.3); ev(8.3, "pop", 0.3); ev(8.6, "tap"); ev(8.5, "whoosh")
for k in range(6): ev(9.0 + k * 0.2, "click", 0.4 if k % 2 else -0.4)
ev(9.4, "pop"); ev(9.8, "tap"); ev(10.4, "tap"); ev(10.6, "tap", 0.2)
ev(12.1, "tap", -0.3); ev(12.3, "pop", 0.3); ev(12.4, "pop")
for k in range(8): ev(12.9 + k * 0.125, "tick", 0.35 if k % 2 else -0.35)
ev(13.0, "tap"); ev(13.5, "rustle")
for k in range(5): ev(13.8 + k * 0.2, "click", 0.2 if k % 2 else -0.2)
ev(14.7, "thump"); ev(15.0, "tap")
ev(16.1, "tap"); ev(16.3, "pop"); ev(16.4, "swipe")
for k in range(6): ev(16.8 + k * 0.17, "tick", 0.3 if k % 2 else -0.3)
ev(18.0, "tap"); ev(18.45, "whoosh"); ev(18.6, "stamp")
ev(20.1, "tap"); ev(20.3, "pop"); ev(20.6, "tap"); ev(20.6, "rustle")
ev(21.3, "pop", -0.2); ev(21.5, "pop", 0.2); ev(21.9, "toggle", -0.4); ev(22.05, "toggle", 0.4); ev(22.3, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
