"""Video largo #2: 5 trucos con ciencia para calmar la cabeza (3:00, 16:9). Pilar: Mente y emociones.
Profundiza 5 Shorts que ya salieron (historial.md #27, #39, #55, #43, #31), con ángulo nuevo: caja de herramientas.
Datos re-verificados el 24/11/2026:
 1 Ponerle nombre: Lieberman et al., UCLA, Psychological Science 2007 (UCLA Health 21/06/2007): 30 personas; al
   etiquetar la emoción baja la respuesta de la amígdala; más activa la corteza prefrontal ventrolateral derecha.
 2 Hablarse por el nombre: Kross et al., J. Pers. Soc. Psychol. 2014 (U. de Michigan): discurso con 5 min de preparación;
   con su nombre/"vos" más confianza, mejor discurso según jueces, menos rumiación y vergüenza.
 3 Suspiro cíclico: Balban et al., Cell Reports Medicine 2023 (Stanford Medicine 09/02/2023): 111 voluntarios sanos,
   5 min/día, 1 mes; respiraciones +1,91 puntos/día de ánimo positivo vs. 1,22 meditación; suspiro cíclico el mejor.
 4 Gratitud: Emmons y McCullough, JPSP 2003 (vía Psychology Today dic. 2020): 10 semanas; grupo gratitud casi 1,5 h más
   de ejercicio por semana, más optimistas.
 5 Naturaleza: White et al., Univ. de Exeter, Scientific Reports 2019 (ScienceDaily 13/06/2019): casi 20.000 personas;
   120+ min/semana más probable buena salud y bienestar; con menos de 120 min no se vio; una visita o varias da igual.
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine_largo import *

DUR_TOTAL = 180.0

# ---------- intro (0-12) ----------
def intro(d, t):
    if t < 8:
        # cabeza con pensamientos dando vueltas
        e = back(prog(t, 0.0, 0.4))
        if e > 0.02:
            circle(d, 960, 270, 150 * e, fill=K2, outline=C, width=8)
            for k in range(6):
                a = t * 2.4 + k * math.tau / 6
                rr = 95 * e
                circle(d, 960 + math.cos(a) * rr, 270 + math.sin(a) * rr * 0.6, 16 * e, fill=R if k % 2 else Y)
        pop_fit(d, t, 0.3, 960, 540, "¿LA CABEZA NO TE PARA?", 140, C, 1700)
        slide_fit(d, t, 0.8, 960, 670, "nervios, pensamientos que dan vueltas, presión", 50, C, 1500)
        if t >= 4:
            p = prog(t, 4.0, 0.22)
            sc = lerp(2.2, 1.0, ease_out(p)); sx, sy = shake(t, 4.2, 0.35, 16)
            rrect(d, 960 - 600 * sc + sx, 860 - 80 * sc + sy, 960 + 600 * sc + sx, 860 + 80 * sc + sy, 30 * sc, fill=Y)
            text_c(d, 960 + sx, 857 + sy, "LA CIENCIA TIENE TRUCOS", "A", 110, K, scale=sc, bg=Y)
    else:
        lt = t - 8
        pop_fit(d, lt, 0.05, 960, 360, "5 TRUCOS PARA", 120, C, 1700)
        pop_fit(d, lt, 0.35, 960, 510, "CALMAR LA CABEZA", 140, Y, 1700)
        for k in range(5):
            p = back(prog(lt, 0.9 + k * 0.25, 0.3))
            if p > 0.02:
                cx = 960 + (k - 2) * 170
                circle(d, cx, 720, 62 * p, fill=K2, outline=Y, width=6)
                text_c(d, cx, 718, str(k + 1), "A", 70, Y, scale=p, bg=K2)
        slide_fit(d, lt, 2.4, 960, 880, "probados en estudios · no reemplazan a un profesional, suman", 44, C, 1600)

# ---------- visuales de cada capítulo ----------
def vis_label(d, lt, cx, cy):
    """Medidor de 'alarma' que baja cuando aparece la etiqueta con el nombre de la emoción."""
    c = lt % 7.0
    lvl = 0.92 if c < 3.0 else lerp(0.92, 0.3, ease_out(prog(c, 3.0, 1.4)))
    lvl += 0.03 * math.sin(lt * 9) if c < 3.0 else 0
    # arco del medidor
    r = 250; gy = cy + 60
    box = [S(cx - r), S(gy - r), S(cx + r), S(gy + r)]
    d.arc(box, 180, 360, fill=(55, 55, 55), width=S(46))
    col = mix(Y, R, clamp((lvl - 0.4) / 0.5))
    d.arc(box, 180, 180 + 180 * lvl, fill=col, width=S(46))
    a = math.pi + math.pi * lvl
    d.line([S(cx), S(gy), S(cx + math.cos(a) * r * 0.78), S(gy + math.sin(a) * r * 0.78)], fill=C, width=S(12))
    circle(d, cx, gy, 22, fill=C)
    text_c(d, cx, gy + 80, "ALARMA", "A", 60, col)
    if c < 3.0:
        sx, sy = shake(lt, lt - 0.1, 1.0, 6)
        warning(d, cx + sx, cy - 300 + sy, 120, col=R, ink=K)
    else:
        p = back(prog(c, 3.0, 0.3))
        if p > 0.02:
            rrect(d, cx - 190 * p, cy - 360 * 1, cx + 190 * p, cy - 360 + 110 * p, 30 * p, fill=Y)
            text_c(d, cx, cy - 360 + 52 * p, "\"ESTOY ENOJADO\"", "A", 50, K, scale=p, bg=Y)
    text_c(d, cx, cy + 300, "ponerle nombre la baja", "SemiBold", 38, G)

def say(d, cx, cy, w, h, txt, col, ink, size, p=1.0, tail=-1):
    if p <= 0.02: return
    w, h = w * p, h * p
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 40 * p, fill=col)
    tx = cx + tail * w * 0.25
    d.polygon([(S(tx - 30 * p), S(cy + h / 2 - 2)), (S(tx + 30 * p), S(cy + h / 2 - 2)), (S(tx + tail * 10 * p), S(cy + h / 2 + 50 * p))], fill=col)
    text_c(d, cx, cy - 3, txt, "A", size, ink, scale=p, bg=col)

def vis_name(d, lt, cx, cy):
    """Burbuja 'YO NO PUEDO' tachada -> 'MARTINA, VOS PODÉS'."""
    c = lt % 8.0
    sx, sy = shake(lt, lt - 0.1, 1.0, 5) if c < 3.6 else (0, 0)
    say(d, cx - 40 + sx, cy - 170 + sy, 520, 150, "YO NO PUEDO...", (70, 70, 70) if c > 3.6 else R, C, 64,
        back(prog(c, 0.1, 0.3)), tail=-1)
    if c > 3.0:
        p = ease_out(prog(c, 3.0, 0.4))
        x0, x1 = cx - 300, cx + 220
        d.line([S(x0), S(cy - 170), S(lerp(x0, x1, p)), S(cy - 170)], fill=R, width=S(14))
    say(d, cx + 40, cy + 110, 620, 150, "MARTINA, VOS PODÉS", Y, K, 60, back(prog(c, 4.0, 0.35)), tail=1)
    person(d, cx - 300, cy + 330, 150, C)
    text_c(d, cx + 60, cy + 330, "hablate como a un amigo", "SemiBold", 38, G)

def vis_breath(d, lt, cx, cy):
    """Círculo que respira: 2 inhalaciones (nariz) + exhalación larga (boca). Ciclo de 8 s."""
    c = lt % 8.0
    if c < 2.0:   s, lab = lerp(0.35, 0.8, ease_in_out(c / 2.0)), "INHALÁ"
    elif c < 3.0: s, lab = lerp(0.8, 1.0, ease_in_out(c - 2.0)), "UN POQUITO MÁS"
    else:         s, lab = lerp(1.0, 0.35, ease_in_out((c - 3.0) / 5.0)), "SOLTÁ DESPACIO"
    for k in range(3):
        circle(d, cx, cy - 20, 240 * s + k * 26, outline=mix(K, Y, 0.35 - k * 0.1), width=4)
    circle(d, cx, cy - 20, 240 * s, fill=mix(K2, Y, 0.25 + 0.5 * s))
    text_c(d, cx, cy - 370, lab, "A", 66, Y)
    sub = "por la nariz" if c < 3.0 else "por la boca"
    text_c(d, cx, cy + 300, sub, "SemiBold", 44, C)
    # dos puntitos de inhalación + barra de exhalación
    circle(d, cx - 120, cy + 380, 14, fill=Y if c >= 0 else G)
    circle(d, cx - 80, cy + 380, 14, fill=Y if c >= 2.0 else (60, 60, 60))
    rrect(d, cx - 40, cy + 372, cx + 160, cy + 388, 8, fill=(60, 60, 60))
    if c >= 3.0:
        rrect(d, cx - 40, cy + 372, cx - 40 + 200 * prog(c, 3.0, 5.0), cy + 388, 8, fill=Y)

def vis_journal(d, lt, cx, cy):
    """Cuaderno: aparecen hasta 5 cosas buenas, una por vez (ciclo de 12 s)."""
    c = lt % 12.0
    x0, y0, x1, y1 = cx - 260, cy - 330, cx + 260, cy + 310
    rrect(d, x0, y0, x1, y1, 26, fill=C)
    for k in range(7):
        circle(d, x0, y0 + 60 + k * 85, 16, fill=K)
    text_c(d, cx + 10, y0 + 70, "ESTA SEMANA AGRADEZCO", "A", 40, K, bg=C)
    items = ["un mate al sol", "la charla con mamá", "aprobé el parcial", "dormí bien", "me reí un montón"]
    for k, it in enumerate(items):
        p = prog(c, 0.6 + k * 1.6, 0.35)
        y = y0 + 170 + k * 100
        d.line([S(x0 + 50), S(y + 30), S(x1 - 40), S(y + 30)], fill=(200, 196, 186), width=S(3))
        if p > 0:
            e = back(p)
            circle(d, x0 + 85, y, 24 * e, fill=GREEN)
            d.line([S(x0 + 73), S(y), S(x0 + 82), S(y + 10), S(x0 + 98), S(y - 10)], fill=C, width=S(6)) if p > 0.5 else None
            text_l(d, x0 + 130, y, it, "SemiBold", 38, mix(C, K, clamp(p * 2)))
    text_c(d, cx, y1 + 60, "chiquitas también valen", "SemiBold", 38, G)

def vis_nature(d, lt, cx, cy):
    """Árbol + barra semanal que se llena hasta 120 minutos."""
    sw = math.sin(lt * 1.3) * 6
    tx, ty = cx - 220, cy - 30
    rrect(d, tx - 24, ty + 40, tx + 24, ty + 260, 10, fill=(120, 84, 52))
    for (ox, oy, r) in ((0, -60, 120), (-80, 10, 90), (80, 10, 90), (0, 40, 100)):
        circle(d, tx + ox + sw * (1 if oy < 0 else 0.5), ty + oy, r, fill=GREEN)
    sun(d, cx + 230, cy - 270, 60, lt)
    c = lt % 9.0
    mins = int(120 * ease_in_out(prog(c, 0.3, 5.0)))
    bx0, bx1, by = cx + 60, cx + 360, cy + 220
    rrect(d, cx + 160, by - 360, cx + 260, by, 30, fill=(48, 48, 48))
    hgt = 360 * mins / 120
    if hgt > 4:
        rrect(d, cx + 160, by - hgt, cx + 260, by, 30, fill=Y if mins >= 120 else GREEN)
    text_c(d, cx + 210, by + 60, f"{mins} MIN", "A", 60, Y if mins >= 120 else C)
    text_c(d, cx + 210, by + 115, "por semana", "SemiBold", 32, G)
    for k in range(7):
        on = k < int(7 * mins / 120 + 0.001)
        circle(d, cx - 360 + k * 50, cy + 330, 16, fill=GREEN if on else (60, 60, 60))
    text_l(d, cx - 380, cy + 390, "≈17 min por día", "SemiBold", 34, G)

# ---------- capítulos ----------
CH = [
    (1, "PONELE NOMBRE", vis_label, "Lieberman y otros, UCLA, Psychological Science (2007)", [
        ("DECÍ LO QUE SENTÍS", "en voz alta o en tu cabeza: \"estoy enojado\""),
        ("UCLA LO PROBÓ EN 2007", "con 30 personas dentro de un resonador"),
        ("VEÍAN CARAS ENOJADAS", "y elegían la palabra para esa emoción"),
        ("LA ALARMA BAJÓ", "la amígdala, tu detector de peligro, se calmó"),
        ("CON OTRA PALABRA, NO", "poner un nombre como \"Harry\" no tuvo ese efecto"),
        ("SE PRENDE EL FRENO", "una zona de la corteza prefrontal se activó más"),
        ("EL TRUCO", "nombrá lo que sentís: \"esto son nervios\""),
    ]),
    (2, "HABLATE POR TU NOMBRE", vis_name, "Kross y otros, Univ. de Michigan, J. Pers. Soc. Psychol. (2014)", [
        ("¿TE HABLÁS A VOS MISMO?", "todos lo hacemos: la clave es cómo"),
        ("UN DISCURSO EN 5 MINUTOS", "universitarios, sobre su trabajo soñado"),
        ("UNOS DECÍAN \"YO\"", "\"yo no puedo, yo me voy a trabar\""),
        ("OTROS, SU NOMBRE", "\"Martina, vos podés hacerlo\""),
        ("MÁS CONFIANZA", "y mejores discursos, según jueces externos"),
        ("MENOS VUELTAS DESPUÉS", "menos vergüenza y menos rumiar lo que pasó"),
        ("EL TRUCO", "antes de un examen, hablate como a un amigo"),
    ]),
    (3, "EL SUSPIRO CÍCLICO", vis_breath, "Balban y otros, Stanford, Cell Reports Medicine (2023)", [
        ("INHALÁ DOS VECES", "una larga y otra cortita, por la nariz"),
        ("SOLTALO DESPACIO", "una exhalación larga, por la boca"),
        ("5 MINUTOS POR DÍA", "durante un mes, en un estudio de Stanford"),
        ("MÁS DE 100 PERSONAS", "sanas, repartidas al azar en 4 grupos"),
        ("LE GANÓ A LA MEDITACIÓN", "respirar así subió más el ánimo cada día"),
        ("EL SUSPIRO FUE EL MEJOR", "el que más mejoró el ánimo de los 4"),
        ("EL TRUCO", "hacelo 5 minutos cuando sientas la presión"),
    ]),
    (4, "ANOTÁ LO BUENO", vis_journal, "Emmons y McCullough, J. Pers. Soc. Psychol. (2003)", [
        ("¿SOLO VES LO MALO?", "es fácil quedarse con lo que salió mal"),
        ("UN DIARIO POR SEMANA", "universitarios durante 10 semanas"),
        ("3 GRUPOS", "anotaban lo bueno, lo molesto o lo que pasó"),
        ("HASTA 5 COSAS", "que agradecían esa semana, chiquitas valen"),
        ("MÁS OPTIMISTAS", "con la semana que venía y con su vida"),
        ("1,5 H MÁS DE EJERCICIO", "casi, por semana, los del grupo gratitud"),
        ("EL TRUCO", "una vez por semana, anotá 5 cosas buenas"),
    ]),
    (5, "2 HORAS DE VERDE", vis_nature, "White y otros, Univ. de Exeter, Scientific Reports (2019)", [
        ("SALÍ AL VERDE", "parques, bosques, playas: cerca de casa vale"),
        ("CASI 20.000 PERSONAS", "en Inglaterra, estudio de la Univ. de Exeter"),
        ("120 MINUTOS POR SEMANA", "con eso, más chances de sentirse bien"),
        ("MENOS DE 2 HORAS", "no mostró ese beneficio en el estudio"),
        ("DA IGUAL CÓMO", "una salida larga o varias cortitas"),
        ("OJO: ES UNA RELACIÓN", "no prueba que el verde sea la causa"),
        ("EL TRUCO", "unos 17 minutos por día ya suman 2 horas"),
    ]),
]
CH_T0 = 12.0
CH_DUR = 32.0

def outro_largo(d, t):
    lt = t - (CH_T0 + 5 * CH_DUR)       # 172
    if lt < 3.6:
        pop_fit(d, lt, 0.05, 960, 360, "TU CAJA DE HERRAMIENTAS", 120, C, 1700)
        for k, (n, title, *_r) in enumerate(CH):
            p = back(prog(lt, 0.5 + k * 0.2, 0.3))
            if p > 0.02:
                text_fit(d, 960, 520 + k * 90, f"{n}. {title}", "A", 70, Y, 1400, scale=p)
    elif lt < 6.0:
        l2 = lt - 3.6
        pop_fit(d, l2, 0.05, 960, 380, "¿CUÁL VAS A PROBAR?", 130, Y, 1700)
        slide_fit(d, l2, 0.4, 960, 520, "contalo en los comentarios", 52, C, 1400)
        p = back(prog(l2, 0.8, 0.3))
        if p > 0.02:
            rrect(d, 960 - 330 * p, 670 - 70 * p, 960 + 330 * p, 670 + 70 * p, 70 * p, fill=R)
            text_c(d, 960, 667, "SUSCRIBITE", "A", 90, C, scale=p, bg=R)
        slide_fit(d, l2, 1.2, 960, 860, "si la ansiedad no se va, hablalo con alguien o buscá ayuda", 40, G, 1500)
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
ev(0.0, "pop"); ev(0.3, "pop", -0.3); ev(0.8, "tap"); ev(4.0, "stamp")
ev(8.0, "pop", -0.2); ev(8.35, "thump", 0.2)
for k in range(5): ev(8.9 + k * 0.25, "tap", (k - 2) * 0.3)
ev(10.4, "tap")
for k in range(5):
    t0 = CH_T0 + k * CH_DUR
    ev(t0 - 0.14, "whoosh")
    chapter_sounds(t0, 7, CH_DUR)
# extras por capítulo (lt del visual = t - t0 - 3)
v1 = CH_T0 + 3.0
for c in range(4):
    ev(v1 + c * 7 + 0.2, "buzz"); ev(v1 + c * 7 + 3.0, "ding")
v2 = CH_T0 + CH_DUR + 3.0
for c in range(4):
    ev(v2 + c * 8 + 3.0, "swipe", -0.3); ev(v2 + c * 8 + 4.0, "pop", 0.3)
v3 = CH_T0 + 2 * CH_DUR + 3.0
for c in range(4):
    ev(v3 + c * 8 + 0.1, "shimmer"); ev(v3 + c * 8 + 3.0, "whoosh")
v4 = CH_T0 + 3 * CH_DUR + 3.0
for c in range(3):
    for k in range(5):
        if c * 12 + 0.6 + k * 1.6 < 28: ev(v4 + c * 12 + 0.6 + k * 1.6, "tick", 0.3 if k % 2 else -0.3)
v5 = CH_T0 + 4 * CH_DUR + 3.0
for c in range(4):
    if c * 9 < 28:
        ev(v5 + c * 9 + 0.2, "rustle"); ev(v5 + c * 9 + 5.3, "ding")
to = CH_T0 + 5 * CH_DUR
ev(to - 0.14, "whoosh"); ev(to + 0.05, "pop")
for k in range(5): ev(to + 0.5 + k * 0.2, "tap", (k - 2) * 0.3)
ev(to + 3.6, "pop"); ev(to + 4.4, "thump"); ev(to + 6.0, "pop"); ev(to + 6.2, "stamp"); ev(to + 7.0, "click")

if __name__ == "__main__":
    main(SCENES_EP, DUR_TOTAL)
