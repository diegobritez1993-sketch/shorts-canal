import sys
import shorts
from shorts import hook, outro
from long6 import shot, B_TXT, B_FIELD, N_TXT, N_PTS, N_MULT, N_LIST, S_CPE, S_COINS, S_PRO, S_META

shorts.SHORTS.update({
    "s20_bono_subs": ("TikFinity · Bono suscriptores", [
        hook("TIKFINITY", "¿Tenés", "suscriptores?", "Dales puntos extra en tu live"),
        shot("bono", "BONO", "Bono para suscriptores", [
            (B_TXT, "Un multiplicador de puntos solo para tus suscriptores.", 4.5),
            (B_FIELD, "En 0% no reciben nada extra.", 4.0),
            (B_FIELD, "Subilo y ganan más puntos por lo mismo.", 4.0),
        ], 14.0),
        outro(),
    ]),
    "s21_multiplicador": ("TikFinity · Niveles", [
        hook("TIKFINITY", "¿Qué es el", "multiplicador?", "Niveles para tu público"),
        shot("niveles", "NIVELES", "Puntos y multiplicador", [
            (N_PTS, "Puntos de Nivel: la base para subir (acá, 50).", 4.0),
            (N_MULT, "Multiplicador 1.03: cada nivel pide un 3% más.", 4.0),
            (N_TXT, "Subir cuesta cada vez más: crece exponencialmente.", 4.0),
            (N_LIST, "Revisalo en «Mostrar lista de niveles».", 3.5),
        ], 16.5),
        outro(),
    ]),
    "s22_meta_puntos": ("TikFinity · Metas", [
        hook("TIKFINITY", "Una meta con", "tus puntos", "Para tu live de TikTok"),
        shot("shares", "METAS", "Channel Points Earned", [
            (S_CPE, "En Superposiciones de Metas: «Channel Points Earned».", 4.0),
            (S_COINS, "Y «Coins Earned» para las monedas.", 3.5),
            (S_PRO, "Ojo: tienen la etiqueta PRO.", 3.5),
            (S_META, "Meta, Título y «Test», como las demás.", 3.5),
        ], 16.0),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
