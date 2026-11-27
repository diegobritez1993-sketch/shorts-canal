"""Duo Bloxyy · 2026-11-27 18:00 · Misterios y leyendas · VOZ IA + MISTERIO
Fuentes: Sportskeeda "8 scariest Roblox myths & legends": "The Missing Dominus", leyenda sobre cuentas que se lo
equipaban y desaparecían (los myths son historias de la comunidad, antes llamadas creepypasta).
PocketGamer (2021) "Roblox catalog: 10 legendary items": Dominus Empyreus, sombrero publicado por Roblox en 2010,
precio original 13.337 Robux, solo 26 disponibles; valor estimado hoy en más de 5 millones de Robux.
Se cuenta como leyenda y con la verdad al final."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="LEYENDA DE ROBLOX", lines=[("EL SOMBRERO", "w"), ("QUE TE HACÍA", "w"), ("DESAPARECER", "r")],
         sizes=(130, 120, 150), icon="ghost", dur=3.8, vo="Dicen que había un sombrero que te hacía desaparecer."),
    dict(type="alert", lines=[("EL DOMINUS", "w"), ("PERDIDO", "r")], sizes=(130, 160), sub="¿CUENTAS QUE SE BORRABAN?",
         source="Sportskeeda", dur=4.4, vo="La leyenda del Dominus perdido: quien se lo ponía, perdía la cuenta."),
    dict(type="hook", kicker="LA VERDAD", lines=[("ES UN MYTH:", "w"), ("UN CUENTO", "y"), ("DE LA COMUNIDAD", "w")],
         sizes=(130, 150, 110), icon="lock", dur=4.0, source="Sportskeeda",
         vo="La verdad: es un myth, un cuento de la comunidad."),
    dict(type="stat", title="EL DOMINUS REAL (2010)", value=26, label="COPIAS", sub="costaba 13.337 Robux",
         source="PocketGamer", dur=4.6, vo="Pero el Dominus existe: en dos mil diez salieron solo veintiséis."),
    dict(type="hook", kicker="HOY SE ESTIMA EN", lines=[("MÁS DE", "w"), ("5 MILLONES", "g"), ("DE ROBUX", "y")],
         sizes=(120, 170, 140), icon="trophy", dur=4.2, source="PocketGamer (estimado)",
         vo="Y hoy se estima en más de cinco millones de Robux."),
    dict(type="question", q=["¿TE LO", "PONDRÍAS?"], options=["SÍ, OBVIO", "NI LOCO"], dur=4.0,
         vo="¿Vos te lo pondrías? Comentá."),
    dict(type="outro", dur=3.0),
], title="el-dominus-perdido", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
