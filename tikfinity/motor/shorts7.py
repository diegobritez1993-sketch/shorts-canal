import sys
import shorts
from shorts import hook, outro
from long7 import shot, G_PRO_BTN, G_SEG, G_REGR, G_DESK, I_TTS, I_SND, I_ACC, I_ALL, C_PUNTOS, C_PRO

def lst(title, items, dur, marks=None):
    d = {"kind": "list", "title": title, "dur": dur, "items": items,
         "times": [0.6 + 0.8 * k for k in range(len(items))]}
    if marks: d["marks"] = marks
    return d

shorts.SHORTS.update({
    "s23_limites_gratis": ("TikFinity · Gratis vs PRO", [
        hook("TIKFINITY GRATIS", "¿Tiene", "límites?", "Lo que te deja usar sin pagar"),
        shot("inicio", "PLAN GRATIS", "Acceso Rápido", [
            (I_TTS, "Texto a voz: hasta 100 mensajes por día.", 4.0),
            (I_SND, "Alertas de sonido: hasta 5.", 3.5),
            (I_ACC, "Acciones y Eventos: hasta 5.", 3.5),
            (I_ALL, "¿Necesitás más? Ahí entra PRO.", 3.5),
        ], 16.5),
        outro(),
    ]),
    "s24_que_es_pro": ("TikFinity · PRO", [
        hook("TIKFINITY PRO", "¿Qué te da", "PRO?", "Y dónde lo ves en TikFinity"),
        shot("galeria", "DÓNDE ESTÁ", "La etiqueta PRO", [
            (G_PRO_BTN, "Siempre abajo a la izquierda: «Actualizar a PRO».", 3.8),
            (G_SEG, "«Número de seguidores»: etiqueta PRO.", 3.5),
            (G_REGR, "«Metas de cuenta regresiva»: también.", 3.5),
        ], 12.5),
        lst("Lo que suma PRO", ["Sin topes de texto a voz", "Sin topes de alertas", "Superposiciones premium",
                                "Hasta 10 perfiles de stream"], 6.5),
        outro(),
    ]),
    "s25_app_escritorio": ("TikFinity · App de escritorio", [
        hook("TIKFINITY", "La app de", "escritorio", "3 cosas que el navegador no hace"),
        shot("galeria", "SOLO WINDOWS", "TikFinity Desktop App", [
            (G_DESK, "Te la ofrece arriba: «TikFinity Desktop App» para Windows.", 4.5),
            (G_DESK, "¿Usás Mac? Te queda la versión del navegador.", 4.0),
        ], 10.0),
        lst("Lo que suma la app", ["Chatbot", "Event API", "Sonidos con atajo de teclado"], 6.0, ["✓"] * 3),
        outro(),
    ]),
    "s26_gratis_de_verdad": ("TikFinity · Gratis", [
        hook("TIKFINITY", "Esto es", "GRATIS", "No pagues por lo que ya tenés"),
        shot("config", "PLAN GRATIS", "Sistema de puntos", [
            (C_PUNTOS, "El sistema de puntos entra en el plan gratis.", 4.0),
            (C_PUNTOS, "Moneda propia y puntos por regalar, compartir y chatear.", 4.5),
        ], 10.0),
        lst("También gratis", ["Los juegos", "Superposiciones básicas", "1 contador de regalos",
                               "1 perfil de stream"], 6.5, ["✓"] * 4),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
