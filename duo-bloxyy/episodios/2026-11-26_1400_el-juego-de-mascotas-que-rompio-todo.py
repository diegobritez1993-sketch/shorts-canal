"""Duo Bloxyy · 2026-11-26 14:00 · Cosas que no sabías · SOLO TEXTO + MÚSICA
Fuentes: playadopt.me (sitio oficial de Adopt Me!, 15/4/2020): el 11 de abril de 2020, con la actualización "Dress Your Pets",
Adopt Me! llegó a 1.615.085 jugadores a la vez, récord de Roblox (el anterior era 707.814); en ese momento tenía más jugadores
que cualquier juego de Steam, incluido Counter-Strike: Global Offensive, que marcaba su propio récord de 1.270.315.
GameSpot (abril 2021): la actualización "Ocean Egg" llegó a 1,92 millones a la vez (récord anterior 1,78 M)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="¿SABÍAS ESTO?", lines=[("UN JUEGO DE", "w"), ("MASCOTAS", "y"), ("LE GANÓ A STEAM", "r")],
         sizes=(120, 180, 112), icon="star", dur=3.6),
    dict(type="stat", title="ADOPT ME! · 11/4/2020", value=1615085, label="JUGANDO A LA VEZ",
         sub="todo por una actualización: vestir a tus mascotas", source="playadopt.me (oficial)", dur=4.6),
    dict(type="versus", title="MILLONES A LA VEZ", left=("CS:GO", "1,27"), right=("ADOPT ME!", "1,61"),
         source="playadopt.me, 2020", dur=4.6),
    dict(type="change", name="Y AL AÑO SIGUIENTE...", label="ACTUALIZACIÓN OCEAN EGG", before="1,61 M", after="1,92 M", up=True,
         note="abril de 2021: otro récord", source="GameSpot, 2021", dur=4.6),
    dict(type="question", q=["¿TENÉS UNA", "MASCOTA LEGENDARIA?"], options=["SÍ, VARIAS", "TODAVÍA NO"], dur=4.4),
    dict(type="outro", dur=3.0),
], title="el-juego-de-mascotas-que-rompio-todo", audio="musica")
if __name__ == "__main__": main(ep)
