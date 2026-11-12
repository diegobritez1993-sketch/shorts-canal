import sys, os
from engine import Scene, render_scene

IMG = {"faq": "faq.png", "inicio2": "inicio2.png", "agencias": "agencias.png",
       "tutoriales": "tutoriales_video.png", "oficial": "canal_oficial.png"}

def shot(img, badge, title, beats, dur, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out, "dur": dur, "flip": flip}

Q_CONECTA = (366, 295, 690, 319)
Q_MC = (366, 351, 952, 375)
Q_ALERTAS = (366, 379, 1006, 403)
Q_PANTALLAS = (366, 407, 642, 431)
Q_TTS = (366, 435, 794, 459)
Q_MOVIL = (366, 491, 614, 515)
Q_CLAVE = (366, 547, 905, 571)
Q_LIMIT = (366, 575, 994, 599)

S = [
    {"kind": "title", "kicker": "SOLUCIONES 2026", "lines": ["¿TikFinity no anda?", "8 problemas resueltos"],
     "sub": "Las respuestas oficiales de la FAQ, explicadas fácil", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Lo que vas a resolver hoy", "dur": 9.5,
     "items": ["No se conecta a tu live", "Alertas y sonidos mudos", "Pantallas desconectadas",
               "Filtro de palabras en el TTS", "Minecraft y el celular", "Clave de stream y lives limitados"],
     "times": [0.8, 1.5, 2.2, 2.9, 3.6, 4.3]},
    shot("faq", "DÓNDE ESTÁ", "Preguntas frecuentes", [
        ((100, 450, 252, 474), "En Inicio, bajá hasta «Preguntas frecuentes».", 5.0),
        ((366, 290, 1012, 604), "Tocá cada pregunta y se abre la respuesta oficial.", 5.0),
    ], 12.0),
    shot("faq", "PROBLEMA 1", "No se conecta a tu live", [
        (Q_CONECTA, "Revisá tu usuario: va tu @ de TikTok, no tu nombre visible.", 5.5),
        (Q_CONECTA, "Conectá cuando el live ya esté abierto.", 4.5),
        (Q_CONECTA, "Dato: podés configurar todo sin estar conectado.", 4.5),
    ], 16.5, flip=True),
    shot("inicio2", "PROBLEMA 2", "Alertas que no suenan", [
        ((580, 242, 772, 356), "Primero: «Alertas de sonido» tiene que estar en Habilitado.", 5.0),
        ((792, 242, 984, 356), "La alerta tiene que estar creada en Acciones y Eventos, unida a un evento.", 5.5),
    ], 12.5),
    shot("faq", "PROBLEMA 2", "Revisá la pantalla", [
        (Q_ALERTAS, "Fijate en qué pantalla (Screen) se reproduce esa acción.", 5.0),
        (Q_ALERTAS, "Agregá esa pantalla como fuente de enlace en Live Studio u OBS.", 5.5),
        (Q_ALERTAS, "Probala con Play/Test. En el celu, dejá TikFinity abierto.", 5.5),
    ], 17.5, flip=True),
    shot("faq", "PROBLEMA 3", "Pantallas desconectadas", [
        (Q_PANTALLAS, "Cada pantalla tiene que estar como fuente de navegador en OBS o Live Studio.", 5.5),
        (Q_PANTALLAS, "Bien agregada, TikFinity la muestra como online.", 4.5),
        (Q_PANTALLAS, "¿Sigue igual? Reiniciá TikFinity y Live Studio, o volvé a agregar la fuente.", 5.5),
    ], 17.5),
    shot("faq", "PROBLEMA 4", "Filtro de palabras en el TTS", [
        (Q_TTS, "TikFinity no tiene filtro propio: usá el filtro de palabras de TikTok.", 5.0),
        (Q_TTS, "Podés dejar la voz solo para top supporters o suscriptores.", 5.0),
        (Q_TTS, "Y ponerle un tiempo de espera por usuario (cooldown).", 4.5),
    ], 16.0, flip=True),
    shot("faq", "PROBLEMA 5", "Minecraft no conecta", [
        (Q_MC, "Abrí run.bat: el servidor tiene que estar corriendo.", 5.0),
        (Q_MC, "Confirmá que el plugin ServerTap esté instalado.", 4.5),
        (Q_MC, "Si el servidor es externo, revisá la IP y abrí el puerto 4567.", 4.5),
    ], 15.5),
    shot("faq", "PROBLEMA 6", "¿Y desde el celular?", [
        (Q_MOVIL, "Sí: las alertas de sonido funcionan en el celu mientras TikFinity esté abierto.", 5.5),
    ], 7.5, flip=True),
    shot("faq", "PROBLEMA 7", "Clave de stream", [
        (Q_CLAVE, "No hay requisitos fijos: TikTok se la da a creadores que elige.", 5.5),
        (Q_CLAVE, "Y te contacta TikTok directamente.", 4.0),
    ], 11.0),
    shot("agencias", "PROBLEMA 7", "La vía de las agencias", [
        ((362, 284, 1016, 322), "Algunas agencias pueden pedir la clave por vos.", 4.5),
        ((500, 486, 800, 628), "Si sale «No hay agencias en tu región», tocá «Avísame».", 5.0),
    ], 11.0, flip=True),
    shot("faq", "PROBLEMA 8", "Lives limitados", [
        (Q_LIMIT, "Lo único fijo son las Normas de TikTok: el algoritmo cambia seguido.", 5.5),
        (Q_LIMIT, "Consejo de la comunidad: no pidas regalos ni likes a cada rato.", 5.0),
        (Q_LIMIT, "Y evitá mostrar imágenes de regalos o palabras como «follow» y «like» en pantalla.", 6.0),
    ], 18.5),
    shot("tutoriales", "MÁS AYUDA", "Tutoriales en video", [
        ((712, 196, 954, 316), "En «Tutoriales en video» hay guías de alertas y chat de voz.", 5.0),
    ], 7.0, flip=True),
    shot("oficial", "MÁS AYUDA", "Canal oficial", [
        ((362, 236, 1016, 292), "En TikTok, tikfinity.official sube novedades y tutoriales.", 5.0),
    ], 7.0),
    {"kind": "list", "title": "Antes de abrir tu live, chequeá", "dur": 11.0,
     "items": ["Tu @ bien escrito", "Live abierto antes de conectar", "Alertas habilitadas",
               "Pantallas como fuente en OBS", "Probar todo con Test", "TikFinity abierto en el celu"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿QUÉ PROBLEMA TENÉS?", "lines": ["Dejalo en", "los comentarios"],
     "sub": "Suscribite: tutoriales nuevos de TikFinity cada semana", "dur": 7.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Problemas y soluciones"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l3_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
