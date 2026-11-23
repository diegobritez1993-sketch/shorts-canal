"""Duo Bloxyy · 2026-11-23 18:00 · Misterios · VOZ IA + MISTERIO
Fuentes: Roblox Wiki (Fandom) "John Doe and Jane Doe" (cuentas de prueba de Baszucki y Cassel; rumor de feb. 2017 del hackeo
el 18 de marzo); PocketGamer "John Doe complete story" (Roblox lo aclaró oficialmente)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="LEYENDA DE ROBLOX", lines=[("¿QUIÉN ES", "w"), ("JOHN DOE?", "r")], sizes=(120, 170), icon="ghost", dur=4.0,
         vo="¿Quién es Yon Dou? La leyenda más famosa de Roblox."),
    dict(type="list", title="LO QUE SE DECÍA", items=["IBA A HACKEAR ROBLOX", "EL 18 DE MARZO", "JUNTO A JANE DOE"],
         icons=["alert", "clock", "ghost"], step=0.7, dur=5.0,
         vo="Se decía que el dieciocho de marzo iba a hackear Roblox, junto a Yein Dou."),
    dict(type="hook", kicker="LA VERDAD", lines=[("ERAN CUENTAS", "w"), ("DE PRUEBA", "y"), ("DE LOS CREADORES", "w")],
         sizes=(120, 140, 96), icon="lock", dur=4.6, source="Roblox Wiki · PocketGamer",
         vo="La verdad: eran cuentas de prueba, creadas por los fundadores de Roblox."),
    dict(type="hook", kicker="MARZO DE 2017", lines=[("EL RUMOR EXPLOTÓ", "w"), ("Y ESE DÍA...", "y"), ("NO PASÓ NADA", "g")],
         sizes=(104, 120, 130), icon="check", dur=4.6, vo="En dos mil diecisiete el rumor explotó. Y ese día... no pasó nada."),
    dict(type="question", q=["¿TE CONECTARÍAS", "EL 18 DE MARZO?"], options=["SÍ", "NO"], dur=4.4,
         vo="¿Vos te conectarías el dieciocho de marzo? Comentá."),
    dict(type="outro", dur=3.0),
], title="la-leyenda-de-john-doe", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
