"""Duo Bloxyy · 2026-11-28 16:00 · Historia de Roblox · VOZ IA + ASMR
Fuentes: CNBC (10/3/2021) "Roblox starts trading at $64.50 after direct listing": empezó a cotizar el miércoles
10 de marzo de 2021 en la Bolsa de Nueva York (NYSE) por cotización directa; precio de referencia US$ 45; abrió a US$ 64,50.
GameSpot: cotiza como RBLX; terminó el primer día valuada en más de US$ 45.000 millones (según WSJ), más que EA y Take-Two.
Bloomberg: "Roblox Reaches $45 Billion Valuation as Shares Rise in Debut"."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="HISTORIA DE ROBLOX", lines=[("EL DÍA QUE", "w"), ("ROBLOX ENTRÓ", "w"), ("A LA BOLSA", "y")],
         sizes=(130, 130, 160), icon="up", dur=3.8, vo="¿Sabías que Roblox se vende en la Bolsa?"),
    dict(type="hook", kicker="10 DE MARZO DE 2021", lines=[("BOLSA DE", "w"), ("NUEVA YORK", "y")],
         sizes=(140, 160), icon="clock", dur=4.0, source="CNBC, 2021",
         vo="El diez de marzo de dos mil veintiuno empezó a cotizar en Nueva York."),
    dict(type="change", name="PRECIO DE LA ACCIÓN", label="EL PRIMER DÍA", before="US$ 45", after="US$ 64,50", up=True,
         note="de la referencia a la apertura", source="CNBC, 2021", dur=4.6,
         vo="La referencia era cuarenta y cinco dólares, y abrió a sesenta y cuatro."),
    dict(type="hook", kicker="AL CERRAR EL DÍA VALÍA", lines=[("MÁS DE", "w"), ("US$ 45.000", "g"), ("MILLONES", "y")],
         sizes=(120, 160, 140), icon="trophy", dur=4.4, source="GameSpot / WSJ",
         vo="Al cerrar el día, valía más de cuarenta y cinco mil millones de dólares."),
    dict(type="hook", kicker="MÁS QUE", lines=[("EA", "y"), ("Y TAKE-TWO", "y")],
         sizes=(170, 140), icon="star", dur=4.0, source="GameSpot",
         vo="Más que E A y que Teik Tu, los de grandes juegos de consola."),
    dict(type="hook", kicker="SU NOMBRE EN LA BOLSA", lines=[("RBLX", "g")],
         sizes=(220,), icon="cube", dur=3.6, source="GameSpot",
         vo="Y su código en la Bolsa es: R B L X."),
    dict(type="outro", dur=3.0),
], title="el-dia-que-roblox-entro-a-la-bolsa", audio="asmr")
if __name__ == "__main__": main(ep)
