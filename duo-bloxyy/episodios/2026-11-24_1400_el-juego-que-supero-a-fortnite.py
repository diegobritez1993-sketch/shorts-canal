"""Duo Bloxyy · 2026-11-24 14:00 · Cosas que no sabías · SOLO TEXTO + MÚSICA
Fuentes: PC Gamer (26/5/2025): Grow a Garden, hecho por un adolescente, salió el 25/3/2025, pico de 8,9 millones en mayo;
PocketGamer.biz (25/6/2025): récord de 21,3 millones a la vez el 21/6/2025, más que el pico histórico de Fortnite (15,3 M, 2020)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="¿SABÍAS QUE...?", lines=[("UN JUEGO DE ROBLOX", "w"), ("LE GANÓ A", "w"), ("FORTNITE", "r")],
         sizes=(100, 120, 170), icon="trophy", dur=3.6),
    dict(type="hook", kicker="GROW A GARDEN", lines=[("UN JUEGO DE", "w"), ("PLANTAR VERDURAS", "y"), ("HECHO POR UN ADOLESCENTE", "w")],
         sizes=(110, 116, 76), icon="cube", dur=4.2, source="PC Gamer, 2025"),
    dict(type="change", name="JUGADORES A LA VEZ", label="DE MAYO A JUNIO 2025", before="8,9 MILLONES", after="21,3 MILLONES", up=True,
         note="récord el 21 de junio de 2025", source="PocketGamer.biz", dur=4.6),
    dict(type="versus", title="RÉCORD DE JUGADORES", left=("FORTNITE", "15,3M"), right=("GROW A GARDEN", "21,3M"),
         source="PocketGamer.biz", dur=4.4),
    dict(type="question", q=["¿LO JUGASTE", "ALGUNA VEZ?"], options=["SÍ, MUCHO", "UN POCO", "NUNCA"], dur=4.6),
    dict(type="outro", dur=3.0),
], title="el-juego-que-supero-a-fortnite", audio="musica")
if __name__ == "__main__": main(ep)
