"""Duo Bloxyy · 2026-11-25 20:00 · Secretos (Studio) · SOLO TEXTO + MÚSICA
Fuentes: Roblox Newsroom sept. 2026 "Global impact of creation on Roblox": en 2025 los creadores ganaron más de 1.500 millones
de dólares, superando los 923 millones de 2024; más de 42.000 creadores en el programa DevEx.
Roblox Newsroom sept. 2025 (Economic Impact Report): en 2024 los 10 desarrolladores top ganaron en promedio 33,9 millones."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="SECRETO DE ROBLOX", lines=[("HACER JUEGOS", "w"), ("EN ROBLOX", "y"), ("PAGA. MUCHO.", "g")],
         sizes=(124, 150, 150), icon="gift", dur=3.6),
    dict(type="change", name="LO QUE GANARON", label="TODOS LOS CREADORES", before="US$ 923 M", after="+US$ 1.500 M", up=True,
         note="de 2024 a 2025", source="Roblox Newsroom, 2026", dur=4.6),
    dict(type="hook", kicker="LOS 10 MÁS TOP (2024)", lines=[("US$ 33,9", "g"), ("MILLONES", "w"), ("CADA UNO, EN PROMEDIO", "y")],
         sizes=(190, 140, 80), icon="trophy", dur=4.4, source="Roblox Newsroom, 2025"),
    dict(type="hook", kicker="¿CUÁNTOS COBRAN?", lines=[("MÁS DE", "w"), ("42.000", "y"), ("CREADORES", "w")],
         sizes=(120, 200, 130), icon="star", dur=4.2, source="Roblox Newsroom, 2026"),
    dict(type="list", title="¿CÓMO EMPEZAR?", items=["ROBLOX STUDIO ES GRATIS", "APRENDÉ LUAU", "PROBÁ CON AMIGOS"],
         icons=["check", "check", "star"], step=0.6, dur=4.4),
    dict(type="outro", dur=3.0),
], title="cuanto-ganan-los-creadores", audio="musica")
if __name__ == "__main__": main(ep)
