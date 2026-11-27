"""Video largo #3: 5 cosas raras que hace tu cerebro sin avisarte (3:00, 16:9). Pilar: Curiosidades y hábitos.
Profundiza Shorts que ya salieron (historial.md #38, #46, #54, #50, #4) con ángulo nuevo: "las trampas de tu cerebro".
Datos re-verificados el 27/11/2026:
 1 Primeras impresiones: Willis y Todorov, Princeton, Psychological Science 2006 (comunicado Princeton 22/08/2006):
   ~200 personas, 5 experimentos, 66 caras, 100 ms / 500 ms / 1 s; a los 100 ms ya correlacionaban mucho con los
   juicios sin límite; con más tiempo solo subía la confianza.
 2 Efecto puerta: Radvansky, Krawietz y Tamplin, Q. J. Exp. Psychol. 2011 (comunicado Notre Dame 16/11/2011):
   universitarios, piezas virtuales y reales; tras la puerta, más olvido; volver por más puertas no ayudó; "límite de evento".
 3 Cosquillas: Blakemore, Frith y Wolpert, UCL, J. Cognitive Neuroscience 1999 (+ The Conversation 2016): robot,
   16 personas; con demora (0,1-0,3 s; 0,2 s) o giro, cosquillas como si las hiciera otro; el cerebro predice y baja el volumen.
 4 Gusano musical: Jakubowski et al., Psychol. Aesthetics, Creativity and the Arts 2016 (APA 03/11/2016): 3.000 personas;
   n.º 1 "Bad Romance"; más rápidas, contorno melódico común, intervalos raros; trucos: escucharla entera, otra canción.
   Beaman et al., Univ. de Reading, QJEP 2015 (comunicado 22/04/2015): 98 voluntarios, chicle bajó un tercio.
 5 Vibración fantasma: Drouin, Kaiser y Miller, Computers in Human Behavior 2012: 89% de universitarios, ~cada 2 semanas
   (Psychology Today 2013); Rothberg et al., BMJ 2010: 115 de 169 personal de salud (68%); 93% poco o nada molesto;
   estrategias: sacar la vibración, cambiar de lugar el celu, otro aparato.
"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "motor"))
from engine_largo import *

DUR_TOTAL = 180.0
PINK = (255, 120, 170)
GRIS = (60, 60, 60)
def SI(v): return int(round(S(v)))

# ---------- intro (0-12) ----------
def brain(d, cx, cy, s, col, t=0.0):
    """Cerebro estilizado: dos lóbulos + surcos."""
    circle(d, cx - s * 0.28, cy, s * 0.42, fill=col)
    circle(d, cx + s * 0.28, cy, s * 0.42, fill=col)
    circle(d, cx, cy - s * 0.18, s * 0.38, fill=col)
    d.line([S(cx), S(cy - s * 0.5), S(cx), S(cy + s * 0.38)], fill=K, width=SI(max(4, s * 0.05)))
    for k, (ox, oy) in enumerate(((-0.4, -0.1), (-0.25, 0.18), (0.35, -0.05), (0.22, 0.22))):
        w = s * 0.18
        d.arc([S(cx + ox * s - w), S(cy + oy * s - w * 0.6), S(cx + ox * s + w), S(cy + oy * s + w * 0.6)],
              200, 340, fill=K, width=SI(max(3, s * 0.035)))

def intro(d, t):
    if t < 8:
        e = back(prog(t, 0.0, 0.4))
        if e > 0.02:
            sx, sy = shake(t, 1.2, 0.5, 8)
            brain(d, 960 + sx, 250 + sy, 230 * e, PINK)
            # "guiño": signo de pregunta que rebota
            q = back(prog(t, 1.0, 0.3))
            if q > 0.02:
                text_c(d, 1180, 170 - 14 * math.sin(t * 5), "?", "A", 140, Y, scale=q)
        pop_fit(d, t, 0.3, 960, 540, "¿TU CEREBRO TE HACE TRAMPA?", 130, C, 1750)
        slide_fit(d, t, 0.8, 960, 670, "todos los días, y ni te enterás", 52, C, 1500)
        if t >= 4:
            p = prog(t, 4.0, 0.22)
            sc = lerp(2.2, 1.0, ease_out(p)); sx, sy = shake(t, 4.2, 0.35, 16)
            rrect(d, 960 - 560 * sc + sx, 860 - 80 * sc + sy, 960 + 560 * sc + sx, 860 + 80 * sc + sy, 30 * sc, fill=Y)
            text_c(d, 960 + sx, 857 + sy, "Y LA CIENCIA LO PROBÓ", "A", 110, K, scale=sc, bg=Y)
    else:
        lt = t - 8
        pop_fit(d, lt, 0.05, 960, 360, "5 COSAS RARAS QUE HACE", 120, C, 1700)
        pop_fit(d, lt, 0.35, 960, 510, "TU CEREBRO SIN AVISARTE", 130, Y, 1700)
        for k in range(5):
            p = back(prog(lt, 0.9 + k * 0.25, 0.3))
            if p > 0.02:
                cx = 960 + (k - 2) * 170
                circle(d, cx, 720, 62 * p, fill=K2, outline=Y, width=6)
                text_c(d, cx, 718, str(k + 1), "A", 70, Y, scale=p, bg=K2)
        slide_fit(d, lt, 2.4, 960, 880, "cada una con su estudio · y la n.º 5 seguro te pasó hoy", 44, C, 1600)

# ---------- visuales de cada capítulo ----------
def face(d, cx, cy, r, mood=0.0, col=C):
    circle(d, cx, cy, r, fill=col)
    circle(d, cx - r * 0.35, cy - r * 0.15, r * 0.1, fill=K)
    circle(d, cx + r * 0.35, cy - r * 0.15, r * 0.1, fill=K)
    w = r * 0.45
    if mood >= 0:
        d.arc([S(cx - w), S(cy), S(cx + w), S(cy + r * 0.45)], 20, 160, fill=K, width=SI(r * 0.07))
    else:
        d.arc([S(cx - w), S(cy + r * 0.3), S(cx + w), S(cy + r * 0.7)], 200, 340, fill=K, width=SI(r * 0.07))

def vis_face(d, lt, cx, cy):
    """Cara que aparece un instante (flash), cronómetro 0,1 s y etiquetas de juicio que caen. Ciclo 7 s."""
    c = lt % 7.0
    # cronómetro
    ms = int(clamp(c / 0.6) * 100)
    rrect(d, cx - 170, cy - 380, cx + 170, cy - 270, 30, fill=K2, outline=Y if ms >= 100 else G, width=5)
    text_c(d, cx, cy - 327, f"0,{ms // 10:01d} S" if ms < 100 else "0,1 S", "A", 70, Y if ms >= 100 else C, bg=K2)
    # cara: visible fuerte durante el flash, luego queda como recuerdo gris
    if c < 0.6:
        circle(d, cx, cy - 30, 190 + 10 * math.sin(c * 30), fill=mix(K, C, 0.25))
        face(d, cx, cy - 30, 170, 1, C)
    else:
        face(d, cx, cy - 30, 170, 1, mix(K, C, 0.35))
        labels = [("CONFIABLE", GREEN, -230, -190), ("SIMPÁTICO", Y, 230, -120), ("¿CAPAZ?", C, -210, 150), ("AGRESIVO", R, 220, 200)]
        for k, (lab, col, ox, oy) in enumerate(labels):
            p = back(prog(c, 0.8 + k * 0.45, 0.3))
            if p > 0.02:
                w = 150
                rrect(d, cx + ox - w * p, cy + oy - 40 * p, cx + ox + w * p, cy + oy + 40 * p, 20 * p, fill=col)
                text_c(d, cx + ox, cy + oy - 2, lab, "A", 44, K, scale=p, bg=col)
    text_c(d, cx, cy + 330, "tu cerebro ya decidió", "SemiBold", 40, G)

def vis_door(d, lt, cx, cy):
    """Plano visto desde arriba: dos piezas y una puerta. La persona cruza y la idea se borra. Ciclo 8 s."""
    c = lt % 8.0
    x0, x1, y0, y1 = cx - 380, cx + 380, cy - 230, cy + 170
    rrect(d, x0, y0, x1, y1, 16, fill=K2, outline=C, width=8)
    # pared del medio con hueco (puerta)
    gy0, gy1 = cy - 60, cy + 60
    d.line([S(cx), S(y0), S(cx), S(gy0)], fill=C, width=SI(8))
    d.line([S(cx), S(gy1), S(cx), S(y1)], fill=C, width=SI(8))
    # hoja de la puerta que se abre cuando pasa
    px = lerp(cx - 280, cx + 280, ease_in_out(prog(c, 0.6, 4.0)))
    open_a = clamp(1 - abs(px - cx) / 160)
    a = math.radians(90 - 80 * open_a)
    d.line([S(cx), S(gy0), S(cx + math.cos(a) * 120), S(gy0 + math.sin(a) * 120)], fill=Y, width=SI(10))
    # mesas
    rrect(d, cx - 340, cy + 60, cx - 220, cy + 130, 10, fill=(90, 70, 50))
    rrect(d, cx + 220, cy + 60, cx + 340, cy + 130, 10, fill=(90, 70, 50))
    # persona (vista desde arriba = círculo)
    circle(d, px, cy, 34, fill=Y)
    circle(d, px, cy, 14, fill=K)
    # globo de pensamiento arriba
    bx, by = px, cy - 330
    crossed = px > cx + 20
    rrect(d, bx - 110, by - 70, bx + 110, by + 70, 34, fill=C)
    circle(d, bx - 20, by + 95, 14, fill=C); circle(d, bx - 8, by + 125, 8, fill=C)
    if not crossed:
        rrect(d, bx - 45, by - 40, bx + 45, by + 40, 8, fill=(200, 150, 80))
        d.line([S(bx - 45), S(by - 10), S(bx + 45), S(by - 10)], fill=K, width=SI(5))
    else:
        q = back(prog(c, 0.6 + 4.0 * 0.5 + 0.3, 0.3))
        text_c(d, bx, by - 4, "?", "A", 110, R, scale=max(q, 0.03), bg=C)
    text_c(d, cx - 190, cy + 220, "PIEZA 1", "A", 40, G)
    text_c(d, cx + 190, cy + 220, "PIEZA 2", "A", 40, G)
    text_c(d, cx, cy + 330, "la puerta \"archiva\" lo anterior", "SemiBold", 40, G)

def feather(d, x, y, s, ang, col=C):
    ca, sa = math.cos(ang), math.sin(ang)
    def P(u, v): return (S(x + u * ca - v * sa), S(y + u * sa + v * ca))
    pts = [P(-s, 0), P(-s * 0.4, -s * 0.28), P(s * 0.6, -s * 0.18), P(s, 0), P(s * 0.6, s * 0.18), P(-s * 0.4, s * 0.28)]
    d.polygon(pts, fill=col)
    d.line([P(-s * 1.3, 0), P(s, 0)], fill=K, width=SI(5))

def vis_tickle(d, lt, cx, cy):
    """Línea de tiempo 'mano -> toque' y medidor de cosquillas: sin demora casi nada, con 0,2 s sube. Ciclo 8 s."""
    c = lt % 8.0
    delayed = c >= 4.0
    cc = c - 4.0 if delayed else c
    # pluma moviéndose
    fx = cx - 120 + math.sin(lt * 6) * 60
    feather(d, fx, cy - 240, 110, -0.35 + math.sin(lt * 6) * 0.25, Y if delayed else C)
    # línea de tiempo
    ty = cy - 60
    d.line([S(cx - 360), S(ty), S(cx + 360), S(ty)], fill=GRIS, width=SI(6))
    circle(d, cx - 260, ty, 26, fill=C)
    text_c(d, cx - 260, ty + 60, "MOVÉS", "A", 36, C)
    tx = cx - 260 + (240 if delayed else 0)
    p = back(prog(cc, 0.4, 0.3))
    if delayed:
        d.line([S(cx - 260), S(ty), S(tx), S(ty)], fill=Y, width=SI(10))
        text_c(d, (cx - 260 + tx) / 2, ty - 55, "+0,2 S", "A", 44, Y)
    if p > 0.02:
        circle(d, tx, ty, 26 * p, fill=Y if delayed else R)
        if delayed:
            text_c(d, tx, ty + 60, "TOCA", "A", 36, Y)
    # medidor
    lvl = (0.88 if delayed else 0.15) * ease_out(prog(cc, 0.6, 1.0))
    lvl += 0.03 * math.sin(lt * 14) if delayed else 0
    mx0, mx1, my = cx - 330, cx + 330, cy + 150
    rrect(d, mx0, my - 40, mx1, my + 40, 40, fill=GRIS)
    if lvl > 0.06:
        rrect(d, mx0, my - 40, mx0 + (mx1 - mx0) * lvl, my + 40, 40, fill=Y if delayed else R)
    text_c(d, cx, my + 90, "COSQUILLAS", "A", 46, C)
    text_c(d, cx, cy + 330, "con demora sí, porque te sorprende" if delayed else "sin demora, tu cerebro lo predice",
           "SemiBold", 40, G)

def note(d, x, y, s, col):
    circle(d, x, y, s * 0.32, fill=col)
    d.line([S(x + s * 0.28), S(y), S(x + s * 0.28), S(y - s * 1.1)], fill=col, width=SI(max(4, s * 0.12)))
    d.line([S(x + s * 0.28), S(y - s * 1.1), S(x + s * 0.7), S(y - s * 0.8)], fill=col, width=SI(max(4, s * 0.12)))

def vis_song(d, lt, cx, cy):
    """Cabeza con notas dando vueltas en loop; aparece un chicle y se va un tercio de las notas. Ciclo 10 s."""
    c = lt % 10.0
    gum = c >= 5.0
    hx, hy = cx - 30, cy - 20
    # cabeza de perfil
    circle(d, hx, hy, 200, fill=K2, outline=C, width=8)
    rrect(d, hx - 70, hy + 170, hx + 70, hy + 290, 20, fill=K2, outline=C, width=8)
    circle(d, hx, hy, 192, fill=K2)
    d.polygon([(S(hx + 188), S(hy - 30)), (S(hx + 240), S(hy + 30)), (S(hx + 190), S(hy + 40))], fill=C)
    # mandíbula que mastica
    if gum:
        chew = abs(math.sin(lt * 7)) * 18
        rrect(d, hx + 150, hy + 70 + chew, hx + 250, hy + 120 + chew, 22, fill=PINK)
        text_c(d, hx + 200, hy + 170, "CHICLE", "A", 36, PINK)
    n = 6 if not gum else 4
    for k in range(n):
        a = lt * 1.8 + k * math.tau / n
        nx = hx + math.cos(a) * 110
        ny = hy - 10 + math.sin(a) * 90
        note(d, nx, ny + 20, 46, Y if k % 2 == 0 else C)
    # loop
    text_c(d, hx, hy - 260, "EN LOOP", "A", 56, Y)
    if gum:
        p = back(prog(c, 5.6, 0.3))
        if p > 0.02:
            rrect(d, cx + 290 - 130 * p, cy - 300 - 60 * p, cx + 290 + 130 * p, cy - 300 + 60 * p, 30 * p, fill=Y)
            text_c(d, cx + 290, cy - 302, "-1/3", "A", 70, K, scale=p, bg=Y)
    text_c(d, cx, cy + 340, "masticar ocupa tu \"voz interior\"" if gum else "rápida, simple y con un salto raro",
           "SemiBold", 40, G)

def vis_phone(d, lt, cx, cy):
    """Celu que 'vibra' sin aviso (pantalla vacía) y luego dos donas: 89% y 68%. Ciclo 9 s."""
    c = lt % 9.0
    if c < 4.0:
        bz = 1.0 if (c % 1.3) < 0.45 else 0.0
        sx = cx - 60
        phone(d, sx, cy - 40, 280, 520, buzz=bz, t=lt)
        text_c(d, sx, cy - 90, "0", "A", 120, G, bg=K2)
        text_c(d, sx, cy + 20, "avisos", "SemiBold", 38, G, bg=K2)
        if c > 1.4:
            q = back(prog(c, 1.4, 0.3))
            text_c(d, sx + 230, cy - 280, "?", "A", 150, R, scale=q)
        text_c(d, cx, cy + 320, "\"me vibró\"... y no había nada", "SemiBold", 40, G)
    else:
        cc = c - 4.0
        f1 = 0.89 * ease_out(prog(cc, 0.2, 1.2))
        f2 = 0.68 * ease_out(prog(cc, 1.4, 1.2))
        donut(d, cx - 190, cy - 60, 170, f1, f"{int(round(f1 * 100))}%", Y)
        donut(d, cx + 190, cy - 60, 170, f2, f"{int(round(f2 * 100))}%", R)
        text_c(d, cx - 190, cy + 160, "UNIVERSITARIOS", "A", 40, C)
        text_c(d, cx - 190, cy + 205, "2012", "SemiBold", 32, G)
        if cc > 1.4:
            text_c(d, cx + 190, cy + 160, "PERSONAL DE SALUD", "A", 40, C)
            text_c(d, cx + 190, cy + 205, "2010", "SemiBold", 32, G)
        text_c(d, cx, cy + 320, "les pasó alguna vez", "SemiBold", 40, G)

# ---------- capítulos ----------
CH = [
    (1, "TE JUZGAN EN 0,1 S", vis_face, "Willis y Todorov, Princeton, Psychological Science (2006)", [
        ("UNA DÉCIMA DE SEGUNDO", "lo que tarda tu cerebro en juzgar una cara"),
        ("PRINCETON, 2006", "unas 200 personas en 5 experimentos"),
        ("66 CARAS DESCONOCIDAS", "vistas 0,1 s, medio segundo o 1 segundo"),
        ("¿CONFIABLE? ¿SIMPÁTICO?", "también atractivo, capaz o agresivo"),
        ("A LOS 0,1 S YA DECIDÍAN", "casi igual que mirando sin límite de tiempo"),
        ("MÁS TIEMPO, MÁS SEGUROS", "no cambiaban de idea, solo se convencían más"),
        ("EL TRUCO PARA FRENAR", "antes de juzgar a alguien, dale una charla"),
    ]),
    (2, "LA PUERTA TE BORRA", vis_door, "Radvansky, Krawietz y Tamplin, Notre Dame, Q. J. Exp. Psychol. (2011)", [
        ("¿A QUÉ VENÍA YO?", "entrás a una pieza y te quedás en blanco"),
        ("NOTRE DAME, 2011", "universitarios en un juego de piezas virtuales"),
        ("LLEVABAN UN OBJETO", "de una mesa a otra, con o sin puerta en el medio"),
        ("TRAS LA PUERTA, MÁS OLVIDO", "y en piezas reales, con cajas, pasó lo mismo"),
        ("VOLVER NO AYUDA", "pasar más puertas de vuelta no lo arregló"),
        ("UN \"LÍMITE DE EVENTO\"", "el cerebro archiva lo de la pieza anterior"),
        ("EL TRUCO PARA FRENAR", "repetite a qué vas, o anotalo antes de salir"),
    ]),
    (3, "TUS PROPIAS COSQUILLAS", vis_tickle, "Blakemore, Frith y Wolpert, UCL, J. Cognitive Neuroscience (1999)", [
        ("PROBÁ HACERTE COSQUILLAS", "no funciona, y hay una razón"),
        ("TU CEREBRO SE ADELANTA", "predice lo que vas a sentir y le baja el volumen"),
        ("UCL, 1999: UN ROBOT", "16 personas lo movían con una mano"),
        ("Y LES TOCABA LA OTRA", "como una cosquilla en la palma"),
        ("SIN DEMORA: CASI NADA", "el cerebro ya sabía lo que venía"),
        ("CON 0,2 S DE DEMORA, SÍ", "o con un giro de 90°: como si fuera otro"),
        ("EL TRUCO DEL CEREBRO", "sin sorpresa no hay cosquillas: por eso otro sí"),
    ]),
    (4, "LA CANCIÓN PEGADA", vis_song, "Jakubowski y otros, Psychol. Aesthet. Creat. Arts (2016) · Beaman y otros, Univ. de Reading (2015)", [
        ("¿UNA CANCIÓN EN LOOP?", "se llama \"gusano musical\" (earworm)"),
        ("3.000 PERSONAS", "nombraron las canciones que más se les pegan"),
        ("LA N.º 1: BAD ROMANCE", "de Lady Gaga, en ese estudio de 2016"),
        ("SUELEN SER RÁPIDAS", "con una melodía simple, fácil de tararear"),
        ("Y CON UN SALTO RARO", "una nota que salta o se repite y sorprende"),
        ("MASCÁ CHICLE", "con 98 voluntarios, la \"escucharon\" un tercio menos"),
        ("EL TRUCO PARA FRENAR", "escuchala entera, o poné otra canción"),
    ]),
    (5, "LA VIBRACIÓN FANTASMA", vis_phone, "Drouin y otros, Computers in Human Behavior (2012) · Rothberg y otros, BMJ (2010)", [
        ("¿TE VIBRÓ EL CELU?", "lo mirás... y no había nada"),
        ("9 DE CADA 10", "universitarios lo sintieron (estudio de 2012)"),
        ("68% EN UN HOSPITAL", "médicos y personal de salud, encuesta de 2010"),
        ("MÁS O MENOS CADA 2 SEMANAS", "en los universitarios de ese estudio"),
        ("CASI NO MOLESTA", "a la mayoría le parece poco o nada molesto"),
        ("UNA EXPLICACIÓN", "tu cerebro espera el aviso y confunde un roce"),
        ("EL TRUCO PARA FRENAR", "sacá la vibración o cambiá el celu de bolsillo"),
    ]),
]
CH_T0 = 12.0
CH_DUR = 32.0

def outro_largo(d, t):
    lt = t - (CH_T0 + 5 * CH_DUR)       # 172
    if lt < 3.6:
        pop_fit(d, lt, 0.05, 960, 360, "LAS 5 TRAMPAS", 120, C, 1700)
        for k, (n, title, *_r) in enumerate(CH):
            p = back(prog(lt, 0.5 + k * 0.2, 0.3))
            if p > 0.02:
                text_fit(d, 960, 520 + k * 90, f"{n}. {title}", "A", 70, Y, 1400, scale=p)
    elif lt < 6.0:
        l2 = lt - 3.6
        pop_fit(d, l2, 0.05, 960, 380, "¿CUÁL TE PASÓ HOY?", 130, Y, 1700)
        slide_fit(d, l2, 0.4, 960, 520, "contalo en los comentarios", 52, C, 1400)
        p = back(prog(l2, 0.8, 0.3))
        if p > 0.02:
            rrect(d, 960 - 330 * p, 670 - 70 * p, 960 + 330 * p, 670 + 70 * p, 70 * p, fill=R)
            text_c(d, 960, 667, "SUSCRIBITE", "A", 90, C, scale=p, bg=R)
        slide_fit(d, l2, 1.2, 960, 860, "y mandáselo a alguien que siempre se olvida a qué fue", 40, G, 1500)
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
ev(0.0, "pop"); ev(0.3, "pop", -0.3); ev(0.8, "tap"); ev(1.0, "ding"); ev(4.0, "stamp")
ev(8.0, "pop", -0.2); ev(8.35, "thump", 0.2)
for k in range(5): ev(8.9 + k * 0.25, "tap", (k - 2) * 0.3)
ev(10.4, "tap")
for k in range(5):
    t0 = CH_T0 + k * CH_DUR
    ev(t0 - 0.14, "whoosh")
    chapter_sounds(t0, 7, CH_DUR)
# extras por capítulo (lt del visual = t - t0 - 3; dura 29 s)
def vend(k): return CH_T0 + k * CH_DUR + CH_DUR
v1 = CH_T0 + 3.0
for c in range(5):
    tb = v1 + c * 7
    if tb + 2.2 < vend(0):
        ev(tb, "click"); ev(tb + 0.6, "ding")
        for k in range(4): ev(tb + 0.8 + k * 0.45, "tap", (k - 1.5) * 0.4)
v2 = CH_T0 + CH_DUR + 3.0
for c in range(4):
    tb = v2 + c * 8
    if tb + 3.5 < vend(1):
        ev(tb + 2.4, "whoosh", 0.2); ev(tb + 3.1, "thump")
v3 = CH_T0 + 2 * CH_DUR + 3.0
for c in range(4):
    tb = v3 + c * 8
    if tb + 5 < vend(2):
        ev(tb + 0.1, "rustle", -0.3); ev(tb + 4.0, "rustle", 0.3); ev(tb + 4.6, "shimmer")
v4 = CH_T0 + 3 * CH_DUR + 3.0
for c in range(3):
    tb = v4 + c * 10
    if tb + 6 < vend(3):
        for k in range(4): ev(tb + 0.3 + k * 1.1, "ding", (k - 1.5) * 0.4)
        ev(tb + 5.6, "pop")
v5 = CH_T0 + 4 * CH_DUR + 3.0
for c in range(4):
    tb = v5 + c * 9
    if tb + 6 < vend(4):
        for k in range(3): ev(tb + k * 1.3, "buzz")
        ev(tb + 1.4, "thump"); ev(tb + 4.2, "tick"); ev(tb + 5.4, "tick")
to = CH_T0 + 5 * CH_DUR
ev(to - 0.14, "whoosh"); ev(to + 0.05, "pop")
for k in range(5): ev(to + 0.5 + k * 0.2, "tap", (k - 2) * 0.3)
ev(to + 3.6, "pop"); ev(to + 4.4, "thump"); ev(to + 6.0, "pop"); ev(to + 6.2, "stamp"); ev(to + 7.0, "click")

if __name__ == "__main__":
    main(SCENES_EP, DUR_TOTAL)
