import sys
import shorts
from shorts import hook, outro
from long3 import shot, Q_ALERTAS, Q_PANTALLAS, Q_TTS, Q_CLAVE

shorts.SHORTS.update({
    "s9_alertas": ("TikFinity · Alertas sin sonido", [
        hook("TIKFINITY", "¿Tus alertas", "no suenan?", "3 cosas para revisar"),
        shot("inicio2", "1", "Habilitalas", [
            ((580, 242, 772, 356), "Tildá «Habilitado» en Alertas de sonido.", 3.5),
        ], 6.0),
        shot("faq", "2 Y 3", "Evento y pantalla", [
            (Q_ALERTAS, "Uní la alerta a un evento en Acciones y Eventos.", 4.0),
            (Q_ALERTAS, "Agregá su pantalla como fuente en OBS o Live Studio.", 4.5),
        ], 11.0),
        outro(),
    ]),
    "s10_pantallas": ("TikFinity · Pantallas", [
        hook("TIKFINITY", "¿Pantalla", "desconectada?", "La solución oficial"),
        shot("faq", "SOLUCIÓN", "Pantallas offline", [
            (Q_PANTALLAS, "Agregá cada pantalla como fuente de navegador en OBS o Live Studio.", 4.5),
            (Q_PANTALLAS, "Bien agregada, TikFinity la marca online.", 3.5),
            (Q_PANTALLAS, "¿Nada? Reiniciá TikFinity y Live Studio.", 4.0),
        ], 14.0),
        outro(),
    ]),
    "s11_tts_filtro": ("TikFinity · Texto a voz", [
        hook("TIKFINITY", "¿Groserías en", "el texto a voz?", "Así lo controlás"),
        shot("faq", "TTS", "Filtro de palabras", [
            (Q_TTS, "TikFinity no trae filtro: activá el de TikTok.", 4.0),
            (Q_TTS, "Dejá la voz solo para top supporters o suscriptores.", 4.0),
            (Q_TTS, "Y poné un cooldown por usuario.", 3.5),
        ], 13.5),
        outro(),
    ]),
    "s12_clave": ("TikFinity · Clave de stream", [
        hook("TIKFINITY", "¿Clave de", "stream?", "En TikTok: lo que dice la FAQ oficial"),
        shot("faq", "LA VERDAD", "No hay requisitos fijos", [
            (Q_CLAVE, "TikTok se la da a creadores que elige y te contacta.", 4.5),
        ], 7.0),
        shot("agencias", "OTRA VÍA", "Agencias", [
            ((362, 284, 1016, 322), "Algunas agencias pueden pedirla por vos.", 3.5),
            ((500, 486, 800, 628), "¿No hay en tu región? Tocá «Avísame».", 4.0),
        ], 9.5),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
