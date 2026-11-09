import sys
import shorts
from shorts import hook, outro
from long2 import shot

shorts.SHORTS.update({
    "s5_meta_likes": ("TikFinity · Meta de likes", [
        hook("TIKFINITY", "Meta de likes", "en tu live", "Que tu público vea cuánto falta"),
        shot("likes", "PASO 1", "Configurala", [
            ((368, 338, 455, 376), "Meta: cuántos likes. Ej: 15.000.", 3.5),
            ((460, 338, 555, 376), "Título: lo que ve tu público.", 3.5),
        ], 8.5),
        shot("likes", "PASO 2", "Ponela en pantalla", [
            ((688, 380, 834, 415), "Copiá el link con «Copy URL».", 3.5),
            ((368, 425, 1016, 610), "Pegalo como fuente en OBS o Live Studio.", 4.0),
        ], 9.0),
        outro(),
    ]),
    "s6_sorteo": ("TikFinity · Meta de follows", [
        hook("TIKFINITY", "El truco del", "sorteo en vivo", "Más follows en un solo live"),
        shot("follows", "EL TRUCO", "Meta chica + premio", [
            ((368, 360, 455, 394), "Poné una meta chica: 50 follows.", 3.5),
            ((460, 360, 555, 394), "Título con premio: «a los 50 sorteamos 1».", 4.0),
            ((368, 450, 1016, 635), "La barra se llena en vivo y la gente se suma.", 4.0),
        ], 13.0),
        outro(),
    ]),
    "s7_superposiciones": ("TikFinity · Superposiciones", [
        hook("TIKFINITY", "¿Cómo pongo", "widgets en mi live?", "Metas, alertas y regalos en pantalla"),
        shot("galeria", "SUPERPOSICIONES", "Así se hace", [
            ((14, 333, 58, 380), "Entrá a Superposiciones (ícono azul).", 3.5),
            ((76, 185, 320, 545), "Elegí el widget: metas, regalos, últimos X...", 4.0),
            ((346, 340, 1016, 435), "Copiá su link y pegalo como fuente en OBS o Live Studio.", 4.5),
        ], 13.5),
        outro(),
    ]),
    "s8_novedades": ("TikFinity · Novedades", [
        hook("TIKFINITY", "3 novedades", "que no conocías", "Lo último de TikFinity"),
        shot("ultimo", "NOVEDADES", "Lo último", [
            ((380, 205, 780, 290), "App de escritorio para Windows, más estable.", 4.0),
            ((380, 325, 780, 375), "Voicemod: tus viewers te cambian la voz.", 4.0),
            ((380, 425, 780, 510), "Beneficios para miembros de equipo de TikTok.", 4.0),
        ], 14.0),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
