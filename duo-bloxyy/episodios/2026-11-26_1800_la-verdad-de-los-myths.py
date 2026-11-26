"""Duo Bloxyy · 2026-11-26 18:00 · Misterios y leyendas · SOLO TEXTO + MISTERIO
Fuente: Sportskeeda "8 scariest Roblox myths & legends": los "myths" se llamaban antes creepypasta; en general se acepta que
son cuentas que existen para contar una historia; Noli, "el Señor del Vacío", visto por primera vez en 2007 según la leyenda;
"The Cult Family" fue creada por el grupo RM en 2012 y sus cuentas cerraron en 2014; "Roblox Myths" es una comunidad de
jugadores (más de 267.000 miembros), no Roblox. Se cuenta como leyenda y con la verdad al final."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="LEYENDAS DE ROBLOX", lines=[("¿QUIÉNES SON", "w"), ("LOS", "w"), ("MYTHS?", "r")],
         sizes=(124, 110, 200), icon="ghost", dur=3.6),
    dict(type="alert", lines=[("CUENTAS", "w"), ("MISTERIOSAS", "r")], sizes=(130, 140), sub="QUE APARECEN Y DESAPARECEN",
         dur=4.2),
    dict(type="hook", kicker="LA LEYENDA DE NOLI", lines=[("\"EL SEÑOR", "w"), ("DEL VACÍO\"", "y"), ("VISTO EN 2007", "w")],
         sizes=(130, 140, 100), icon="question", dur=4.4, source="Sportskeeda"),
    dict(type="hook", kicker="LA VERDAD", lines=[("SON CUENTAS", "w"), ("CREADAS PARA", "w"), ("CONTAR HISTORIAS", "y")],
         sizes=(130, 120, 104), icon="lock", dur=4.4, source="Sportskeeda"),
    dict(type="stat", title="LA COMUNIDAD ROBLOX MYTHS", value=267000, prefix="+", label="MIEMBROS",
         sub="son jugadores, no Roblox: un club de cuentos de miedo", source="Sportskeeda", dur=4.4),
    dict(type="question", q=["¿TE CREÍSTE", "ALGÚN MYTH?"], options=["SÍ, ME ASUSTÉ", "NUNCA"], dur=4.2),
    dict(type="outro", dur=3.0),
], title="la-verdad-de-los-myths", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
