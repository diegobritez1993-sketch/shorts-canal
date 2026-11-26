"""Duo Bloxyy · 2026-11-26 16:00 · Secretos · VOZ IA + ASMR
Fuentes: Roblox Help Center "Using Emotes" (en.help.roblox.com/hc/articles/203314300): comandos de chat por defecto
/e wave, /e point, /e cheer, /e laugh, /e dance, /e dance2, /e dance3 (no funciona si el chat está desactivado).
Roblox Newsroom 20/8/2019 "Expanding Emotes": escribí /e y el nombre del emote (ej. /e salute) y funciona con cualquier
emote de tu inventario aunque no lo tengas equipado; se pueden equipar hasta 8 en el menú de emotes."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="SECRETO DEL CHAT", lines=[("ESCRIBÍ ESTO", "w"), ("Y TU AVATAR", "w"), ("BAILA", "y")],
         sizes=(124, 124, 190), icon="chat", dur=3.6, vo="Escribí esto en el chat y tu avatar baila."),
    dict(type="hook", kicker="EL TRUCO", lines=[("/e", "y"), ("+ EL NOMBRE", "w"), ("DEL EMOTE", "w")],
         sizes=(220, 120, 120), icon="lock", dur=4.2, source="Roblox Help Center",
         vo="Barra, e, y el nombre del emote. Así de simple."),
    dict(type="list", title="LOS DE SIEMPRE", items=["/e dance", "/e dance2", "/e dance3", "/e wave"],
         icons=["star", "star", "star", "check"], step=0.5, dur=4.4, source="Roblox Help Center",
         vo="Dance, dance dos, dance tres... y wave para saludar."),
    dict(type="list", title="Y TAMBIÉN", items=["/e point", "/e cheer", "/e laugh"],
         icons=["check", "trophy", "chat"], step=0.55, dur=4.2, source="Roblox Help Center",
         vo="También point, cheer y laugh, para reírte."),
    dict(type="hook", kicker="EL SECRETO", lines=[("FUNCIONA CON", "w"), ("TUS EMOTES", "y"), ("AUNQUE NO LOS EQUIPES", "g")],
         sizes=(120, 150, 76), icon="gift", dur=4.4, source="Roblox Newsroom, 2019",
         vo="Y anda con cualquier emote que tengas, aunque no lo equipes."),
    dict(type="question", q=["¿CUÁL", "USÁS MÁS?"], options=["DANCE", "WAVE", "LAUGH"], dur=4.4,
         vo="¿Cuál usás más? Comentá."),
    dict(type="outro", dur=3.0),
], title="comandos-secretos-del-chat", audio="asmr")
if __name__ == "__main__": main(ep)
