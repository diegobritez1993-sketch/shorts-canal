"""Duo Bloxyy · 2026-11-24 16:00 · Historia · VOZ IA + ASMR
Fuentes: Wikipedia "Roblox oof" (sonido del juego Messiah, 2000; retirado en julio de 2022 por un problema de licencia y
reemplazado por un sonido nuevo); Roblox DevForum 31/7/2025 ("Oof is back as default sound": vuelve como sonido por defecto);
Windows Central (anuncio del 18/7/2025, "A comeback so good it hurts")."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="HISTORIA DE ROBLOX", lines=[("EL OOF", "y"), ("NO ERA", "w"), ("DE ROBLOX", "r")],
         sizes=(170, 130, 130), icon="question", dur=3.6, vo="El famoso oof... no era de Roblox."),
    dict(type="hook", kicker="SU ORIGEN", lines=[("VENÍA DE UN JUEGO", "w"), ("DEL AÑO 2000:", "w"), ("MESSIAH", "y")],
         sizes=(104, 110, 160), icon="star", dur=4.4, source="Wikipedia",
         vo="Venía de un juego del año dos mil, llamado Mésaia."),
    dict(type="change", name="JULIO DE 2022", label="PROBLEMA DE LICENCIA", before="OOF", after="SONIDO NUEVO", up=False,
         note="Roblox tuvo que sacarlo", source="Wikipedia", dur=4.6,
         vo="En julio de dos mil veintidós, por un problema de licencia, lo sacaron."),
    dict(type="hook", kicker="JULIO DE 2025", lines=[("¡VOLVIÓ!", "g"), ("COMO SONIDO", "w"), ("POR DEFECTO", "y")],
         sizes=(170, 116, 130), icon="check", dur=4.4, source="Roblox DevForum, 2025",
         vo="Y en julio de dos mil veinticinco, volvió como sonido por defecto."),
    dict(type="question", q=["¿CUÁL", "PREFERÍS?"], options=["EL OOF", "EL NUEVO"], dur=4.4,
         vo="¿Vos cuál preferís? Comentá."),
    dict(type="outro", dur=3.0),
], title="el-oof-no-era-de-roblox", audio="asmr")
if __name__ == "__main__": main(ep)
