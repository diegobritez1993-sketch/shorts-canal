"""Video largo #1: 5 trucos que usan las apps para que no sueltes el celular (3:00, 16:9).
Datos ya verificados en los Shorts (ver historial.md):
 1 Scroll infinito: Aza Raskin (2006), después se arrepintió públicamente.
 2 Likes: Sherman et al., UCLA, Psychological Science 2016.
 3 Notificaciones / revisar el celular: Reviews.org, encuesta Q4 2025 (EE.UU.): 186 veces/día, 85% en 10 min al despertar.
 4 Rachas: aversión a la pérdida (Kahneman y Tversky 1979); Duolingo Blog 2022: 7 días de racha -> 3,6 veces más probable terminar el curso.
 5 Patrones oscuros: FTC vs. Amazon, acuerdo US$ 2.500 M (AP, 25/09/2025); "Iliad"; Amazon no admitió culpa.
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine_largo import *

DUR_TOTAL = 180.0

# ---------- intro (0-12) ----------
def intro(d, t):
    e = back(prog(t, 0.0, 0.4))
    if e > 0.02 and t < 8:
        warning(d, 960, 300, 230 * e, rot=0.06 * math.sin(t * 6) if t > 0.6 else 0)
    if t < 8:
        pop_fit(d, t, 0.3, 960, 560, "TU CELULAR NO ES ADICTIVO", 130, C, 1700)
        pop_fit(d, t, 0.7, 960, 720, "POR CASUALIDAD", 150, Y, 1700)
        if t >= 4:
            p = prog(t, 4.0, 0.22)
            sc = lerp(2.2, 1.0, ease_out(p)); sx, sy = shake(t, 4.2, 0.35, 16)
            rrect(d, 960 - 520 * sc + sx, 900 - 80 * sc + sy, 960 + 520 * sc + sx, 900 + 80 * sc + sy, 30 * sc, fill=Y)
            text_c(d, 960 + sx, 897 + sy, "ESTÁ DISEÑADO ASÍ", "A", 110, K, scale=sc, bg=Y)
    else:
        lt = t - 8
        pop_fit(d, lt, 0.05, 960, 380, "5 TRUCOS QUE USAN LAS APPS", 120, C, 1700)
        pop_fit(d, lt, 0.35, 960, 530, "PARA QUE NO LO SUELTES", 120, Y, 1700)
        for k in range(5):
            p = back(prog(lt, 0.9 + k * 0.25, 0.3))
            if p > 0.02:
                cx = 960 + (k - 2) * 170
                circle(d, cx, 740, 62 * p, fill=K2, outline=Y, width=6)
                text_c(d, cx, 738, str(k + 1), "A", 70, Y, scale=p, bg=K2)
        slide_fit(d, lt, 2.4, 960, 900, "¿cuántos conocías? contalos mientras mirás", 46, C, 1600)

# ---------- visuales de cada capítulo ----------
def vis_scroll(d, lt, cx, cy):
    pw, ph = 330, 600
    x0, x1, top, bot = cx - pw / 2, cx + pw / 2, cy - ph / 2, cy + ph / 2
    rrect(d, x0, top, x1, bot, 54, fill=K2, outline=C, width=8)
    off = (lt * 420) % 230
    for i in range(-1, 5):
        y0 = top + 30 + i * 230 - off; y1 = y0 + 200
        c0, c1 = max(y0, top + 26), min(y1, bot - 26)
        if c1 - c0 > 10:
            rrect(d, x0 + 28, c0, x1 - 28, c1, 20, fill=(48, 48, 48))
            if c0 <= y0 + 4 and c1 >= y0 + 60:
                circle(d, x0 + 70, y0 + 36, 18, fill=Y if i % 2 == 0 else C)
                rrect(d, x0 + 100, y0 + 28, x0 + 240, y0 + 44, 8, fill=G)
            if c1 >= y0 + 180 and c0 <= y0 + 70:
                rrect(d, x0 + 48, y0 + 70, x1 - 48, y0 + 180, 12, fill=(70, 70, 70))
    rrect(d, cx - 55, top + 16, cx + 55, top + 30, 7, fill=C)
    # flecha infinita
    text_c(d, cx, bot + 70, "SIN FINAL", "A", 70, Y)

def vis_likes(d, lt, cx, cy):
    beat = 1 + 0.09 * max(0, math.sin(lt * 7))
    heart(d, cx, cy - 40, 300 * beat, R)
    n = random.Random(int(lt * 3)).choice([3, 12, 0, 48, 7, 230, 1, 19, 104, 5])
    text_c(d, cx, cy + 250, f"{n} likes", "A", 90, C)
    for k in range(3):
        tt = (lt * 0.8 + k / 3) % 1.0
        text_c(d, cx + (k - 1) * 150, cy - 220 - tt * 160, "+1", "Black", 54, R, alpha=1 - tt)

def vis_notifs(d, lt, cx, cy):
    for k in range(3):
        rp = (lt * 0.8 + k / 3) % 1.0
        circle(d, cx + 130, cy - 130, 70 + rp * 200, outline=mix(K, R, (1 - rp) * 0.8), width=6)
    rrect(d, cx - 150, cy - 150, cx + 150, cy + 150, 64, fill=C)
    bubble(d, cx, cy + 10, 170, K, ink=C)
    n = int(lt * 6) % 120 + 1
    lab = "99+" if n >= 99 else str(n)
    circle(d, cx + 140, cy - 140, 86, fill=K); circle(d, cx + 140, cy - 140, 76, fill=R)
    text_c(d, cx + 140, cy - 144, lab, "Black", 58 if len(lab) < 3 else 46, C, bg=R)
    text_c(d, cx, cy + 290, "186 veces al día", "A", 70, Y)

DAYS = "LMMJVSD"
def vis_streak(d, lt, cx, cy):
    lit = min(7, int(lt / 0.6) + 1)
    lost = lt > 9.0 and lt < 13.0
    for k in range(7):
        x = cx - 330 + k * 110
        on = k < lit
        col = (R if lost and k == 6 else Y) if on else (60, 60, 60)
        circle(d, x, cy - 40, 46, fill=col)
        text_c(d, x, cy - 42, DAYS[k], "A", 46, K if on else C, bg=col)
    sx, sy = shake(lt, 9.0, 0.5, 14) if lost else (0, 0)
    text_c(d, cx + sx, cy + 150 + sy, f"{lit} DÍAS" if not lost else "¡RACHA PERDIDA!", "A", 110, R if lost else Y)
    text_c(d, cx, cy + 260, "de racha", "SemiBold", 40, C) if not lost else None

def vis_dark(d, lt, cx, cy):
    rrect(d, cx - 280, cy - 110, cx + 280, cy + 30, 60, fill=Y)
    text_c(d, cx, cy - 42, "QUEDARME", "A", 90, K, bg=Y)
    # el botón de cancelar se escapa
    ph = int(lt / 1.6)
    rnd = random.Random(ph)
    tx = cx + rnd.uniform(-220, 220); ty = cy + rnd.uniform(140, 300)
    text_c(d, tx, ty, "cancelar", "Medium", 30, (90, 90, 90))
    d.line([S(tx - 60), S(ty + 22), S(tx + 60), S(ty + 22)], fill=(70, 70, 70), width=S(2))

# ---------- capítulos ----------
CH = [
    (1, "EL SCROLL INFINITO", vis_scroll, "Aza Raskin, creador del scroll infinito (2006)", [
        ("NO TIENE FINAL", "antes las páginas se terminaban; ahora no"),
        ("SIN FINAL NO HAY PAUSA", "tu cerebro nunca recibe la señal de \"listo, cortá\""),
        ("LO INVENTÓ AZA RASKIN", "en 2006, para que navegar fuera más cómodo"),
        ("AÑOS DESPUÉS SE ARREPINTIÓ", "y lo dijo públicamente"),
        ("SEGUÍS POR INERCIA", "no porque te guste lo que estás viendo"),
        ("PARECE QUE ES UN RATITO", "y se te va media hora"),
        ("EL TRUCO PARA FRENAR", "ponele un final vos: un temporizador"),
    ]),
    (2, "LOS LIKES", vis_likes, "Sherman y otros, UCLA, Psychological Science (2016)", [
        ("CADA LIKE ES UN PREMIO", "y tu cerebro lo registra como tal"),
        ("UCLA LO MIDIÓ EN 2016", "con escáneres cerebrales a adolescentes"),
        ("MÁS LIKES, MÁS ACTIVIDAD", "en el centro de recompensa del cerebro"),
        ("NO SABÉS CUÁNTOS VAS A TENER", "a veces 3, a veces 200"),
        ("COMO UNA TRAGAMONEDAS", "el premio impredecible engancha más"),
        ("POR ESO VOLVÉS A MIRAR", "a ver si \"pegó\" lo que subiste"),
        ("EL TRUCO PARA FRENAR", "ocultá el contador de likes en tus redes"),
    ]),
    (3, "LAS NOTIFICACIONES", vis_notifs, "Reviews.org, encuesta a ~1.000 adultos de EE.UU. (2025)", [
        ("SON ROJAS A PROPÓSITO", "el rojo es el color de la alarma"),
        ("TE INTERRUMPEN TODO EL DÍA", "y cada aviso te invita a entrar"),
        ("186 VECES POR DÍA", "revisa el celular una persona promedio"),
        ("UNA VEZ CADA 5 MINUTOS", "mientras está despierta"),
        ("EL 85% LO MIRA AL DESPERTAR", "en los primeros 10 minutos"),
        ("MUCHAS NI SON IMPORTANTES", "son la app pidiéndote que vuelvas"),
        ("EL TRUCO PARA FRENAR", "dejá las de personas, apagá las de apps"),
    ]),
    (4, "LAS RACHAS", vis_streak, "Kahneman y Tversky (1979) · Duolingo Blog (2022)", [
        ("DÍAS SEGUIDOS USANDO LA APP", "y un contador que te lo recuerda"),
        ("PERDERLA DUELE MÁS", "que lo que alegra mantenerla"),
        ("AVERSIÓN A LA PÉRDIDA", "lo describieron Kahneman y Tversky en 1979"),
        ("Y FUNCIONA", "las apps lo saben y lo usan"),
        ("3,6 VECES MÁS PROBABLE", "terminar el curso con 7 días de racha (Duolingo)"),
        ("NO ES MALO EN SÍ", "el problema es entrar solo para no perderla"),
        ("EL TRUCO PARA FRENAR", "preguntate: ¿quiero hacerlo o es por la racha?"),
    ]),
    (5, "LOS PATRONES OSCUROS", vis_dark, "AP, 25/09/2025: acuerdo FTC vs. Amazon (Amazon no admitió culpa)", [
        ("ENTRAR: UN CLIC", "salir: un laberinto"),
        ("SE LLAMAN PATRONES OSCUROS", "diseños para que hagas lo que la app quiere"),
        ("AMAZON LO LLAMABA \"ILÍADA\"", "a su trámite para cancelar Prime"),
        ("BOTONES QUE DAN CULPA", "\"no, gracias, no quiero envío gratis\""),
        ("US$ 2.500 MILLONES", "pagó Amazon para cerrar el caso con la FTC"),
        ("SIN ADMITIR CULPA", "pero con una multa récord"),
        ("EL TRUCO PARA FRENAR", "antes de suscribirte, fijate cómo se cancela"),
    ]),
]
CH_T0 = 12.0
CH_DUR = 32.0

def outro_largo(d, t):
    lt = t - (CH_T0 + 5 * CH_DUR)       # 172
    if lt < 3.6:
        pop_fit(d, lt, 0.05, 960, 360, "AHORA YA LOS CONOCÉS", 130, C, 1700)
        for k, (n, title, *_r) in enumerate(CH):
            p = back(prog(lt, 0.5 + k * 0.2, 0.3))
            if p > 0.02:
                text_fit(d, 960, 520 + k * 90, f"{n}. {title}", "A", 70, Y, 1400, scale=p)
    elif lt < 6.0:
        l2 = lt - 3.6
        pop_fit(d, l2, 0.05, 960, 420, "¿CUÁL TE ENGANCHA MÁS?", 130, Y, 1700)
        slide_fit(d, l2, 0.4, 960, 560, "contalo en los comentarios", 52, C, 1400)
        p = back(prog(l2, 0.8, 0.3))
        if p > 0.02:
            rrect(d, 960 - 330 * p, 700 - 70 * p, 960 + 330 * p, 700 + 70 * p, 70 * p, fill=R)
            text_c(d, 960, 697, "SUSCRIBITE", "A", 90, C, scale=p, bg=R)
    else:
        l3 = lt - 6.0
        e = back(prog(l3, 0, 0.35))
        if e > 0.02: warning(d, 960, 330, 260 * e)
        pop_fit(d, l3, 0.2, 960, 640, "NO DIGAS QUE NO TE AVISÉ", 140, Y, 1700)

SCENES_EP = [(0, CH_T0, intro)]
for k, (n, title, vis, src, beats) in enumerate(CH):
    SCENES_EP.append(chapter(n, title, beats, vis, src, CH_T0 + k * CH_DUR, CH_DUR))
SCENES_EP.append((CH_T0 + 5 * CH_DUR, DUR_TOTAL + 0.01, outro_largo))

# ---------- sonidos ----------
ev(0.0, "pop"); ev(0.3, "pop", -0.3); ev(0.7, "thump"); ev(4.0, "stamp")
ev(8.0, "pop", -0.2); ev(8.35, "pop", 0.2)
for k in range(5): ev(8.9 + k * 0.25, "tap", (k - 2) * 0.3)
ev(10.4, "tap")
for k in range(5):
    t0 = CH_T0 + k * CH_DUR
    ev(t0 - 0.14, "whoosh")
    chapter_sounds(t0, 7, CH_DUR)
for t0 in (CH_T0 + 2 * CH_DUR + 3.0,):
    for j in range(6): ev(t0 + 8.2 + j * 0.12, "tick", 0.3 if j % 2 else -0.3)
ev(CH_T0 + 3 * CH_DUR + 3.0 + 9.0, "buzz")
to = CH_T0 + 5 * CH_DUR
ev(to - 0.14, "whoosh"); ev(to + 0.05, "pop")
for k in range(5): ev(to + 0.5 + k * 0.2, "tap", (k - 2) * 0.3)
ev(to + 3.6, "pop"); ev(to + 4.4, "thump"); ev(to + 6.0, "pop"); ev(to + 6.2, "stamp"); ev(to + 7.0, "click")

if __name__ == "__main__":
    main(SCENES_EP, DUR_TOTAL)
