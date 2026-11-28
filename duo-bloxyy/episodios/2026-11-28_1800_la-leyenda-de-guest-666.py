"""Duo Bloxyy · 2026-11-28 18:00 · Misterios y leyendas · SOLO TEXTO + MISTERIO
Fuente: Gaming Urban Legends Wiki (Fandom) "Guest 666": leyenda de un "hacker" que parecía un invitado común pero con
piel negra y ojos rojos, que pasaba de juego en juego usando comandos de admin; se hizo popular porque YouTubers
hablaban de él y hacían videos; la página aclara: "This rumor isn't true and is just one big creepypasta".
Los Guests eran cuentas temporales para jugar sin registrarse (ver historial #2). Se cuenta como leyenda y con la verdad al final."""
from _base import *
ep = Episode([
    dict(type="alert", lines=[("EL INVITADO", "w"), ("666", "r")], sizes=(130, 190), sub="¿TE LO CRUZASTE?", dur=3.8),
    dict(type="hook", kicker="ANTES EXISTÍAN", lines=[("LOS GUESTS:", "y"), ("JUGAR SIN", "w"), ("CREAR CUENTA", "w")],
         sizes=(140, 120, 120), icon="question", dur=4.2),
    dict(type="list", title="LA LEYENDA DICE", items=["PARECÍA UN GUEST COMÚN", "PERO CON OJOS ROJOS", "SALTABA DE JUEGO EN JUEGO"],
         icons=["ghost", "alert", "cube"], step=0.7, dur=5.0, source="Gaming Urban Legends Wiki"),
    dict(type="hook", kicker="Y ENCIMA", lines=[("USABA", "w"), ("COMANDOS", "r"), ("DE ADMIN", "w")],
         sizes=(130, 160, 130), icon="lock", dur=4.0),
    dict(type="hook", kicker="LA VERDAD", lines=[("ES UNA", "w"), ("CREEPYPASTA", "y"), ("DE YOUTUBE", "w")],
         sizes=(130, 150, 130), icon="check", dur=4.4, source="Gaming Urban Legends Wiki"),
    dict(type="question", q=["¿ALGUIEN TE", "DIJO QUE LO VIO?"], options=["SÍ, UN AMIGO", "NUNCA"], dur=4.4),
    dict(type="outro", dur=3.0),
], title="la-leyenda-de-guest-666", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
