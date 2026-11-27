"""Duo Bloxyy · 2026-11-27 16:00 · Cosas que no sabías · SOLO TEXTO + ASMR
Fuente: Guinness World Records "Most visited videogame created in Roblox": Brookhaven RP, 37.200.000.000 visitas
al 29 de septiembre de 2023; juego de rol creado por los usuarios Wolfpaq y Aidanleewolf. Guinness aclara que el
número cambia todos los días."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="RÉCORD MUNDIAL", lines=[("UN JUEGO", "w"), ("DE ROBLOX TIENE", "w"), ("RÉCORD GUINNESS", "y")],
         sizes=(130, 116, 130), icon="trophy", dur=3.6),
    dict(type="trivia", q=["¿CUÁL ES EL JUEGO", "MÁS VISITADO?"], options=["A) ADOPT ME!", "B) BROOKHAVEN RP", "C) BLOX FRUITS"],
         answer=1, dur=7.0, source="Guinness World Records"),
    dict(type="stat", title="VISITAS A SEPT. 2023", value=37200, prefix="+", suffix=" M", label="DE VISITAS",
         sub="más de 37 mil millones de visitas", source="Guinness World Records", dur=4.4),
    dict(type="hook", kicker="¿QUIÉN LO HIZO?", lines=[("DOS JUGADORES:", "w"), ("WOLFPAQ Y", "y"), ("AIDANLEEWOLF", "y")],
         sizes=(116, 140, 130), icon="cube", dur=4.2, source="Guinness World Records"),
    dict(type="hook", kicker="EL DATO", lines=[("ES DE ROL", "g"), ("Y EL NÚMERO", "w"), ("SIGUE SUBIENDO", "y")],
         sizes=(160, 120, 120), icon="up", dur=4.0),
    dict(type="outro", dur=3.0),
], title="el-record-guinness-de-roblox", audio="asmr")
if __name__ == "__main__": main(ep)
