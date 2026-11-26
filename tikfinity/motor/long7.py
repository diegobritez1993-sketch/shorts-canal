import sys, os
from engine import Scene, render_scene

IMG = {"galeria": "galeria.png", "inicio": "1793722010486_image.png", "config": "1793722117131_image.png",
       "shares": "shares.png", "ultimo": "ultimo.png"}

def shot(img, badge, title, beats, dur=None, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out,
            "dur": dur or round(bt + 0.8, 1), "flip": flip}

# recuadros (captura original 1024x768)
G_PRO_BTN = (76, 637, 316, 678)
G_SEG = (76, 266, 316, 301)
G_REGR = (76, 308, 316, 344)
G_DESK = (347, 188, 1016, 221)
I_TTS = (368, 447, 560, 559)
I_SND = (580, 447, 772, 559)
I_ACC = (792, 447, 984, 559)
I_ALL = (348, 386, 1016, 580)
C_PRO = (100, 482, 300, 506)
C_PAT = (100, 513, 300, 538)
C_PUNTOS = (348, 185, 1016, 510)
SH_LIST = (92, 264, 300, 622)
SH_PRO = (246, 264, 292, 622)
U_DESK = (372, 200, 782, 292)

S = [
    {"kind": "title", "kicker": "GRATIS VS PRO", "lines": ["¿Tenés que pagar", "TikFinity PRO?"],
     "sub": "Qué usás gratis, qué pide PRO y cuándo te conviene (2026)", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Lo que vas a saber hoy", "dur": 10.0,
     "items": ["Dónde aparece PRO", "Los límites del plan gratis", "Lo que es gratis de verdad",
               "Lo que suma PRO", "App de escritorio y celular", "Si te conviene pagar"],
     "times": [0.8, 1.4, 2.0, 2.6, 3.2, 3.8]},
    shot("galeria", "DÓNDE ESTÁ", "La etiqueta PRO", [
        (G_PRO_BTN, "Abajo a la izquierda, siempre a la vista: «Actualizar a PRO».", 5.0),
        (G_SEG, "En Superposiciones, «Número de seguidores» lleva la etiqueta PRO.", 5.0),
        (G_REGR, "Y «Metas de cuenta regresiva» también.", 4.5),
    ], flip=True),
    shot("config", "DÓNDE ESTÁ", "En Configuración", [
        (C_PRO, "En Configuración hay una sección propia: «TikFinity Pro».", 5.0),
        (C_PAT, "Justo abajo está «Conexión con Patreon».", 4.5),
    ]),
    shot("inicio", "PARTE 1", "Los límites del plan gratis", [
        (I_ALL, "Acceso Rápido: las tres herramientas que más vas a usar.", 5.0),
        (I_TTS, "Texto a voz: gratis hasta 100 mensajes por día.", 5.0),
        (I_SND, "Alertas de sonido: hasta 5 en el plan gratis.", 5.0),
        (I_ACC, "Acciones y Eventos: también hasta 5.", 5.0),
        (I_ALL, "Datos del blog oficial de TikFinity (setup, sept. 2026).", 5.0),
    ], flip=True),
    shot("config", "PARTE 2", "Lo que es gratis de verdad", [
        (C_PUNTOS, "El sistema de puntos entra en el plan gratis.", 5.0),
        (C_PUNTOS, "Moneda, puntos por regalar, compartir y chatear: sin pagar.", 5.0),
    ]),
    {"kind": "list", "title": "También gratis", "dur": 10.0,
     "items": ["Los juegos", "Las superposiciones básicas", "1 contador de regalos", "1 perfil de stream"],
     "marks": ["✓"] * 4, "times": [0.8, 1.6, 2.4, 3.2]},
    shot("shares", "PARTE 3", "Lo que marca PRO", [
        (SH_LIST, "En Superposiciones de Metas, mirá la columna de la derecha.", 5.0),
        (SH_PRO, "Cada tipo de meta muestra la etiqueta PRO.", 4.5),
        (SH_LIST, "Antes de armar tu live, fijate qué lleva PRO.", 4.5),
    ], flip=True),
    {"kind": "list", "title": "Lo que suma PRO", "dur": 12.0,
     "items": ["Sin topes de texto a voz", "Sin topes de alertas y acciones", "Superposiciones premium",
               "Más contadores de regalos", "Hasta 10 perfiles de stream", "Novedades antes que nadie"],
     "times": [0.8, 1.5, 2.2, 2.9, 3.6, 4.3]},
    shot("galeria", "PARTE 4", "App de escritorio", [
        (G_DESK, "Arriba te ofrece la «TikFinity Desktop App» para Windows.", 5.0),
        (G_DESK, "Trae chatbot, Event API y sonidos con atajo de teclado.", 5.0),
    ]),
    shot("ultimo", "PARTE 4", "App de escritorio", [
        (U_DESK, "Según TikFinity: más estabilidad y funciones exclusivas.", 5.0),
        (U_DESK, "¿Usás Mac? Te queda la versión del navegador.", 4.5),
    ], flip=True),
    {"kind": "list", "title": "Ojo con el celular", "dur": 11.0,
     "items": ["TikFinity Mobile es otra app", "Gratis: 75 textos a voz por día", "Gratis: 3 alertas",
               "Tiene su propia suscripción", "El PRO de PC no pasa al celu"],
     "times": [0.8, 1.6, 2.4, 3.2, 4.0]},
    {"kind": "list", "title": "¿Te conviene PRO?", "dur": 13.0,
     "items": ["Empezá gratis y probá todo", "¿Pasás los 100 textos a voz por día?",
               "¿Necesitás más de 5 alertas o acciones?", "¿Querés superposiciones premium?",
               "Si decís que sí, recién ahí PRO"],
     "marks": ["1", "?", "?", "?", "✓"], "times": [0.8, 1.8, 2.8, 3.8, 4.8]},
    {"kind": "list", "title": "Resumen rápido", "dur": 12.0,
     "items": ["PRO: abajo a la izquierda", "Gratis: 100 TTS, 5 alertas, 5 acciones",
               "Puntos y juegos: gratis", "Metas: mirá la etiqueta PRO", "Celular: suscripción aparte"],
     "marks": ["✓"] * 5, "times": [0.6, 1.4, 2.2, 3.0, 3.8]},
    {"kind": "title", "kicker": "¿Y VOS?", "lines": ["¿Usás TikFinity", "gratis o PRO?"],
     "sub": "Contame en los comentarios y suscribite para más TikFinity", "dur": 8.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Gratis vs PRO"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l7_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
