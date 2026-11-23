"""Duo Bloxyy · 2026-11-23 14:00 · Historia · VOZ IA + MÚSICA
Fuentes: PocketGamer "When was Roblox made" (GoBlocks/DynaBlocks, lanzamiento 1/9/2006); TechCrunch 2019 (Baszucki y Cassel, 2004-2005)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="¿SABÍAS QUE...?", lines=[("ROBLOX NO SE", "w"), ("LLAMABA", "w"), ("ROBLOX", "y")], icon="cube", dur=3.6,
         vo="Roblox no siempre se llamó Roblox."),
    dict(type="list", title="SUS PRIMEROS NOMBRES", items=["GOBLOCKS", "DYNABLOCKS"], icons=["cube", "cube"], dur=4.4,
         vo="Al principio pensaron en Go Blocks, o en Daina Blocks."),
    dict(type="change", name="EL NOMBRE FINAL", label="ROBOTS + BLOCKS", before="DYNABLOCKS", after="ROBLOX", up=True,
         note="robots + bloques = ROBLOX", dur=4.6, vo="Hasta que eligieron Roblox: robots, más blocks, o sea bloques."),
    dict(type="hook", kicker="LOS CREADORES", lines=[("DAVID BASZUCKI", "y"), ("Y ERIK CASSEL", "y"), ("EMPEZARON EN 2004", "w")],
         sizes=(110, 110, 96), icon="trophy", dur=4.4, source="TechCrunch, 2019", vo="Lo crearon David Baszucki y Erik Cassel. Empezaron en dos mil cuatro."),
    dict(type="hook", kicker="LANZAMIENTO", lines=[("SALIÓ AL PÚBLICO", "w"), ("EL 1 DE SEPTIEMBRE", "y"), ("DE 2006", "y")],
         sizes=(100, 110, 150), icon="star", dur=4.2, source="PocketGamer", vo="Y salió para todos el uno de septiembre de dos mil seis."),
    dict(type="question", q=["¿QUÉ NOMBRE", "LE PONDRÍAS VOS?"], options=["ROBLOX", "DYNABLOCKS", "OTRO"], dur=4.6,
         vo="¿Y vos? ¿Qué nombre le pondrías? Dejalo en los comentarios."),
    dict(type="outro", dur=3.0),
], title="roblox-no-se-llamaba-roblox", audio="musica")
if __name__ == "__main__": main(ep)
