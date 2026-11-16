import sys
import shorts
from shorts import hook, outro
from long4 import shot, M_CANALES, GRID, CARD, U_GTA, U_TECLAS, A_EVENTOS

shorts.SHORTS.update({
    "s13_canales": ("TikFinity · Canales en directo", [
        hook("TIKFINITY", "Espiá a los", "que la rompen", "Streamers que usan TikFinity, en vivo"),
        shot("canales", "DÓNDE", "Canales en directo", [
            (M_CANALES, "En Inicio, abrí «Canales en directo».", 3.5),
            (GRID, "Streamers en vivo que usan TikFinity.", 3.5),
        ], 8.5),
        shot("canales", "EL TRUCO", "Robá ideas", [
            (CARD, "Ves cuánta gente mira a cada uno.", 3.5),
            (GRID, "Entrá y fijate qué alertas y metas usan.", 4.0),
        ], 9.0),
        outro(),
    ]),
    "s14_gta": ("TikFinity · GTA 5", [
        hook("TIKFINITY + GTA 5", "Que tu chat", "maneje tu GTA", "Con regalos, en tu live de TikTok"),
        shot("ultimo", "PLUGIN", "GTA 5 + TikFinity", [
            (U_GTA, "Está en «Lo último y lo mejor».", 3.5),
            (U_GTA, "Cada regalo dispara una acción en el juego.", 4.0),
            (U_GTA, "El link al tutorial oficial está ahí mismo.", 4.0),
        ], 13.5),
        outro(),
    ]),
    "s15_teclas": ("TikFinity · Simulador de teclas", [
        hook("TIKFINITY", "Regalos que", "aprietan teclas", "En tu PC con Windows"),
        shot("ultimo", "NUEVO", "Simulación de Teclas", [
            (U_TECLAS, "Con regalos, tus viewers controlan apps de tu PC.", 4.0),
        ], 6.5),
        shot("inicio2", "DÓNDE", "Acciones y Eventos", [
            (A_EVENTOS, "Se configura en Acciones y Eventos.", 3.5),
            (A_EVENTOS, "Dejalo Habilitado y probalo antes del live.", 4.0),
        ], 9.0),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
