"""Short 2026-11-01 15:00 — Mente y emociones: el efecto foco (spotlight effect).
Fuente: Gilovich, Medvec y Savitsky, Cornell, Journal of Personality and Social Psychology (2000):
los que usaban una remera vergonzosa creían que ~46% la notaría; en realidad ~23%.
"""
import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine import *

SPOT = (60, 54, 30)

def spotlight(d, cx, top, bottom, half, alpha):
    """Cono de luz desde arriba hasta un óvalo en el piso."""
    if alpha <= 0.02: return
    col = mix(K, SPOT, alpha)
    d.polygon([(S(cx - 40), S(top)), (S(cx + 40), S(top)), (S(cx + half), S(bottom)), (S(cx - half), S(bottom))], fill=col)
    d.ellipse([S(cx - half), S(bottom - 45), S(cx + half), S(bottom + 45)], fill=mix(K, (110, 96, 30), alpha))

def eye(d, cx, cy, s, open_=1.0, col=C):
    """Ojo simple: almendra + pupila. open_ 0..1."""
    h = s * 0.45 * open_
    if h < 3:
        d.line([S(cx - s / 2), S(cy), S(cx + s / 2), S(cy)], fill=col, width=S(6)); return
    d.ellipse([S(cx - s / 2), S(cy - h / 2), S(cx + s / 2), S(cy + h / 2)], fill=col)
    r = min(s * 0.17, h * 0.45)
    circle(d, cx, cy, r, fill=K)

def tshirt(d, cx, cy, s, col, ink=K):
    w, h = s, s * 0.95
    pts = [(-0.5, -0.38), (-0.2, -0.48), (-0.08, -0.4), (0.08, -0.4), (0.2, -0.48), (0.5, -0.38),
           (0.62, -0.1), (0.38, 0.0), (0.38, 0.5), (-0.38, 0.5), (-0.38, 0.0), (-0.62, -0.1)]
    d.polygon([(S(cx + x * w), S(cy + y * h)) for x, y in pts], fill=col)
    return

def crowd(d, t, lt, n_lit, lit_p, y0=760, cols=5, rows=2, gap=170, s=150, look_col=Y):
    """Grilla de 10 personas; las primeras n_lit tienen ojos 'mirando' (amarillo)."""
    k = 0
    for r in range(rows):
        for c in range(cols):
            cx = 540 + (c - (cols - 1) / 2) * gap
            cy = y0 + r * 240
            e = back(prog(lt, 0.3 + k * 0.05, 0.3))
            if e > 0.02:
                on = k < n_lit
                q = lit_p if on else 0
                person(d, cx, cy, s * e, mix((70, 70, 70), look_col, q))
                if q > 0.3:
                    eye(d, cx, cy - s * 0.55 - 40, 46 * e, open_=q, col=C)
            k += 1

def b1(d, t):
    # gancho: persona bajo un reflector, ojos alrededor
    lt = t
    e = ease_out(prog(lt, 0.0, 0.35))
    spotlight(d, 540, 0, 900, 260 * e, e)
    person(d, 540, 790, 260 * back(prog(lt, 0.05, 0.35)), C)
    for k, (ex, ey) in enumerate([(150, 330), (930, 300), (120, 740), (960, 700), (230, 1000), (860, 1010)]):
        q = back(prog(lt, 0.9 + k * 0.12, 0.25))
        if q > 0.02:
            blink = 0.15 if abs(math.sin(lt * 2.3 + k)) > 0.97 else 1.0
            eye(d, ex, ey, 110 * q, open_=blink)
    pop_line(d, lt, 0.0, 540, 1220, "¿SENTÍS QUE", 150, C, dur=0.25)
    pop_line(d, lt, 0.25, 540, 1390, "TODOS TE MIRAN?", 150, Y, dur=0.25)
    slide_line(d, lt, 1.8, 540, 1540, "spoiler: muchos menos de los que creés", 42, C, kind="SemiBold", dy=25)

def b2(d, t):
    lt = t - 4
    slide_line(d, lt, 0.1, 540, 300, "EN CORNELL", 140, C)
    slide_line(d, lt, 0.3, 540, 430, "HICIERON LA PRUEBA", 110, Y)
    e = back(prog(lt, 0.5, 0.4))
    if e > 0.02:
        sw = math.sin(lt * 3) * 0.04
        tshirt(d, 540 + sw * 200, 830, 430 * e, Y)
        text_c(d, 540, 860, ":(", "Black", 120 * e, K, bg=Y)
    slide_line(d, lt, 1.5, 540, 1180, "un estudiante entraba a un aula", 46, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.7, 540, 1245, "con una remera vergonzosa", 46, C, kind="SemiBold", dy=25)
    pill(d, lt, 2.4, 540, 1400, 640, "¿CUÁNTOS LA NOTARON?", fill=C, ink=K, size=44, h=100)

def b3(d, t):
    lt = t - 8
    slide_line(d, lt, 0.1, 540, 300, "ÉL CREÍA QUE", 120, C)
    pop_line(d, lt, 0.3, 540, 450, "CASI LA MITAD", 150, Y)
    lit = ease_in_out(prog(lt, 1.0, 0.8))
    crowd(d, t, lt, 5, lit, y0=780)
    n = int(round(46 * ease_out(prog(lt, 1.0, 1.2))))
    if lt > 1.0:
        text_c(d, 540, 1380, f"{n}%", "A", 200, Y)
    slide_line(d, lt, 2.4, 540, 1520, "lo iba a notar", 46, C, kind="SemiBold", dy=25)

def b4(d, t):
    lt = t - 12
    slide_line(d, lt, 0.1, 540, 300, "EN REALIDAD", 140, C)
    # empiezan 5 mirando y se apagan hasta 2-3 (23%)
    off = ease_in_out(prog(lt, 0.6, 0.9))
    k = 0
    for r in range(2):
        for c in range(5):
            cx = 540 + (c - 2) * 170
            cy = 600 + r * 240
            q = 1.0 if k < 2 else (1 - off if k < 5 else 0)
            if k == 2: q = 1 - off * 0.5  # "casi" una tercera persona: 23% ≈ 2,3 de 10
            person(d, cx, cy, 150, mix((70, 70, 70), Y, q))
            if q > 0.3: eye(d, cx, cy - 122, 46, open_=q)
            k += 1
    stamp(d, lt, 1.7, 540, 1210, 260, 130, "23%", fill=Y, ink=K, size=190)
    slide_line(d, lt, 2.2, 540, 1420, "menos de 1 de cada 4", 54, C, kind="Bold", dy=25)
    slide_line(d, lt, 2.4, 540, 1500, "Gilovich y otros, Cornell, J. Pers. Soc. Psychol., 2000", 30, G, kind="SemiBold", dy=20)

def b5(d, t):
    lt = t - 16
    slide_line(d, lt, 0.1, 540, 290, "SE LLAMA", 110, C)
    pop_line(d, lt, 0.3, 540, 430, "EFECTO FOCO", 170, Y)
    # tres reflectores: cada persona en su propio foco
    for k, cx in enumerate((230, 540, 850)):
        e = ease_out(prog(lt, 0.7 + k * 0.25, 0.4))
        spotlight(d, cx, 560, 1080, 120 * e, e * 0.9)
        person(d, cx, 990, 170 * back(prog(lt, 0.75 + k * 0.25, 0.35)), C)
    slide_line(d, lt, 2.0, 540, 1250, "cada uno está pendiente", 50, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 2.15, 540, 1320, "de SU propio foco", 50, Y, kind="Bold", dy=25)

def b6(d, t):
    lt = t - 20
    slide_line(d, lt, 0.05, 540, 330, "¿Y VOS?", 170, Y)
    pop_line(d, lt, 0.35, 540, 520, "¿CUÁNTAS VECES", 120, C)
    pop_line(d, lt, 0.55, 540, 650, "NO HICISTE ALGO", 120, C)
    pop_line(d, lt, 0.75, 540, 780, "POR VERGÜENZA?", 120, R)
    e = back(prog(lt, 1.2, 0.35))
    if e > 0.02:
        bubble(d, 540, 1060, 260 * e, Y)
    slide_line(d, lt, 1.6, 540, 1300, "contalo en los comentarios", 48, C, kind="SemiBold", dy=25)
    slide_line(d, lt, 1.8, 540, 1370, "(nadie te está mirando tanto)", 42, G, kind="SemiBold", dy=20)

BEATS_EP = [(0, 4, b1), (4, 8, b2), (8, 12, b3), (12, 16, b4), (16, 20, b5), (20, 23.2, b6), (23.2, 25.01, outro)]

standard_sounds(BEATS_EP)
ev(0.0, "thump"); ev(0.05, "shimmer"); ev(0.25, "pop", 0.2)
for k in range(6): ev(0.9 + k * 0.12, "pop", -0.5 if k % 2 == 0 else 0.5)
ev(1.8, "tap")
ev(4.1, "tap", -0.3); ev(4.3, "tap", 0.3); ev(4.5, "pop"); ev(5.5, "rustle"); ev(5.7, "tap"); ev(6.4, "click")
ev(8.1, "tap"); ev(8.3, "thump")
for k in range(10): ev(8.3 + k * 0.05, "pop", -0.4 + k * 0.09)
for k in range(12): ev(9.0 + k * 0.1, "tick", 0.3 if k % 2 else -0.3)
ev(10.4, "tap")
ev(12.1, "tap")
for k in range(3): ev(12.6 + k * 0.3, "click", -0.3 + k * 0.3)
ev(13.5, "stamp"); ev(14.2, "tap"); ev(14.4, "tap", 0.2)
ev(16.1, "tap"); ev(16.3, "thump")
for k in range(3): ev(16.7 + k * 0.25, "shimmer", -0.5 + k * 0.5)
ev(18.0, "tap"); ev(18.15, "pop")
ev(20.05, "pop"); ev(20.35, "pop", -0.3); ev(20.55, "pop", 0.3); ev(20.75, "thump"); ev(21.2, "ding"); ev(21.6, "tap"); ev(21.8, "tap")

if __name__ == "__main__":
    main(BEATS_EP)
