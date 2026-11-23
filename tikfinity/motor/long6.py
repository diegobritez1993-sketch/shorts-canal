import sys, os
from engine import Scene, render_scene

IMG = {"puntos": "1793722117131_image.png", "bono": "1793722126692_image.png",
       "niveles": "1793722134762_image.png", "shares": "shares.png"}

def shot(img, badge, title, beats, dur=None, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out,
            "dur": dur or round(bt + 0.8, 1), "flip": flip}

# recuadros (captura original 1024x768)
P_NOMBRE = (612, 258, 948, 293)
P_MONEDA = (384, 324, 948, 360)
P_SHARE = (384, 373, 948, 410)
P_CHAT = (384, 423, 948, 460)
P_ALL = (380, 254, 952, 464)
B_TXT = (364, 316, 918, 362)
B_FIELD = (384, 410, 948, 446)
N_TXT = (364, 302, 1016, 390)
N_PTS = (384, 437, 948, 472)
N_MULT = (384, 483, 948, 518)
N_LIST = (612, 538, 780, 562)
MN_CONF = (100, 258, 300, 345)
MN_RESET = (100, 450, 300, 473)
S_CPE = (100, 450, 290, 472)
S_COINS = (100, 414, 290, 435)
S_PRO = (246, 264, 292, 620)
S_META = (364, 418, 1016, 530)

S = [
    {"kind": "title", "kicker": "PUNTOS Y NIVELES", "lines": ["Que tu público", "vuelva a cada live"],
     "sub": "TikFinity: puntos, bonos y niveles para premiar a tu comunidad", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Lo que vas a armar hoy", "dur": 10.0,
     "items": ["Tu propia moneda", "Puntos por regalar, compartir y chatear", "Bono para suscriptores",
               "Niveles que suben solos", "Una meta con tus puntos", "Ideas para tu live"],
     "times": [0.8, 1.4, 2.0, 2.6, 3.2, 3.8]},
    shot("niveles", "DÓNDE ESTÁ", "Configuración", [
        (MN_CONF, "Todo está en Configuración: Sistema de Puntos, Bono y Niveles.", 5.0),
        (MN_RESET, "Ojo con «Restablecer Puntos»: pensalo dos veces antes de tocarlo.", 5.0),
    ], flip=True),
    shot("puntos", "PARTE 1", "Tu moneda y tus puntos", [
        (P_NOMBRE, "Ponele nombre a tu moneda: uno con onda, que tu público repita.", 5.0),
        (P_MONEDA, "Puntos por moneda: acá está en 1.01 por cada moneda regalada.", 5.0),
        (P_SHARE, "Puntos por compartir: 3 cada vez que comparten tu live.", 5.0),
        (P_CHAT, "Puntos por minuto de chat: 0.5 por cada minuto chateando.", 5.0),
        (P_ALL, "Tildá las tres: suma el que regala, el que comparte y el que charla.", 5.5),
    ]),
    shot("bono", "PARTE 2", "Bono para suscriptores", [
        (B_TXT, "Un multiplicador de puntos solo para tus suscriptores.", 4.5),
        (B_FIELD, "Acá está en 0%: así no reciben nada extra.", 4.5),
        (B_FIELD, "Si tenés suscriptores, subilo y ganan más por lo mismo.", 4.5),
    ], flip=True),
    shot("niveles", "PARTE 3", "Niveles que suben solos", [
        (N_TXT, "Tus espectadores suben de nivel juntando puntos.", 4.5),
        (N_PTS, "Puntos de Nivel: la base para pasar al siguiente nivel (acá, 50).", 5.0),
        (N_MULT, "Multiplicador 1.03: cada nivel pide un 3% más.", 5.0),
        (N_TXT, "Resultado: subir cuesta cada vez más. Crece exponencialmente.", 5.0),
        (N_LIST, "Abrí «Mostrar lista de niveles» y revisá cuánto pide cada uno.", 4.5),
    ]),
    shot("shares", "PARTE 4", "Una meta con tus puntos", [
        (S_CPE, "En Superposiciones de Metas está «Channel Points Earned».", 5.0),
        (S_COINS, "Y también «Coins Earned», para las monedas.", 4.5),
        (S_PRO, "Ojo: todas estas metas tienen la etiqueta PRO.", 4.5),
        (S_META, "Se arman como las demás: Meta, Título y «Test».", 4.5),
    ], flip=True),
    {"kind": "list", "title": "Ideas para tu live", "dur": 13.0,
     "items": ["Explicá cómo se ganan puntos", "Recordá que compartir también suma",
               "Saludá a los que suben de nivel", "Nombrá a tu moneda en cada live"],
     "times": [0.8, 1.8, 2.8, 3.8]},
    {"kind": "list", "title": "Tu receta en 1 minuto", "dur": 13.0,
     "items": ["Moneda con nombre propio", "Las 3 formas de sumar tildadas", "Bono si tenés suscriptores",
               "Nivel base y multiplicador", "Lista de niveles revisada", "Meta de puntos (PRO)"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿Y VOS?", "lines": ["¿Cómo se llama", "tu moneda?"],
     "sub": "Contame en los comentarios y suscribite para más TikFinity", "dur": 8.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Puntos y niveles"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l6_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
