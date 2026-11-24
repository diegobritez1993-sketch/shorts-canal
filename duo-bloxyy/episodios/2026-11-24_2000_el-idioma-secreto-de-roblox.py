"""Duo Bloxyy · 2026-11-24 20:00 · Secretos (Roblox Studio) · VOZ IA + MÚSICA
Fuentes: Wikipedia "Luau (programming language)" (derivado de Lua 5.1, llegó a Roblox en agosto de 2019; lo usan Alan Wake 2,
Warframe); luau.org 3/11/2021 "Luau goes open-source" (código abierto, licencia MIT)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="SECRETO DE ROBLOX STUDIO", lines=[("ROBLOX TIENE", "w"), ("SU PROPIO", "w"), ("IDIOMA", "y")],
         sizes=(120, 120, 180), icon="lock", dur=3.6, vo="Roblox tiene su propio idioma secreto."),
    dict(type="hook", kicker="SE LLAMA", lines=[("LUAU", "y"), ("Y VIENE DE LUA", "w")],
         sizes=(190, 110), icon="cube", dur=4.2, source="Wikipedia",
         vo="Se llama Luau, y viene de otro lenguaje llamado Lua."),
    dict(type="list", title="LO QUE HACE", items=["SCRIPTS DE TUS JUEGOS", "PUERTAS Y BOTONES", "MONEDAS Y PUNTOS"],
         icons=["star", "lock", "trophy"], step=0.6, dur=4.6,
         vo="Con él se programan los juegos: puertas, botones y monedas."),
    dict(type="hook", kicker="DE 2019 A 2021", lines=[("LLEGÓ EN 2019", "w"), ("Y EN 2021 LO", "w"), ("LIBERARON GRATIS", "g")],
         sizes=(116, 110, 116), icon="check", dur=4.6, source="luau.org, 2021",
         vo="Llegó en dos mil diecinueve, y en dos mil veintiuno lo liberaron gratis."),
    dict(type="question", q=["¿QUERÉS APRENDER", "A PROGRAMAR?"], options=["SÍ", "NO"], dur=4.4,
         vo="¿Vos querés aprender a programar en Roblox? Comentá."),
    dict(type="outro", dur=3.0),
], title="el-idioma-secreto-de-roblox", audio="musica")
if __name__ == "__main__": main(ep)
