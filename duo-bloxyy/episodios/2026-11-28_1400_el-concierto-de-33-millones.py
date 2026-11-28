"""Duo Bloxyy · 2026-11-28 14:00 · Cosas que no sabías · SOLO TEXTO + MÚSICA
Fuentes: PC Gamer (17/11/2020) "Lil Nas X's Roblox concert has been viewed 33 million times": la viewership acumulada
fue de 33 millones; Roblox programó una función el sábado y una repetición el domingo, y por la demanda la repitió
dos veces más el lunes (4 funciones); fue la promoción de su nuevo single "Holiday".
GameSpot: "más de 30 millones" lo vieron y el cantante estrenó un single nuevo."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="NOVIEMBRE 2020", lines=[("UN CONCIERTO", "w"), ("DENTRO DE", "w"), ("ROBLOX", "y")],
         sizes=(130, 120, 170), icon="star", dur=3.4),
    dict(type="trivia", q=["¿CUÁNTAS VISTAS", "TUVO EL SHOW?"], options=["A) 3 MILLONES", "B) 33 MILLONES", "C) 330 MIL"],
         answer=1, dur=7.0, source="PC Gamer, 2020"),
    dict(type="stat", title="EL SHOW DE LIL NAS X", value=33, suffix=" M", label="DE VISTAS",
         sub="sumando todas las funciones", source="PC Gamer, 2020", dur=4.0),
    dict(type="list", title="LO PEDÍAN TANTO QUE...", items=["SÁBADO: EL SHOW", "DOMINGO: REPETICIÓN", "LUNES: 2 MÁS"],
         icons=["star", "clock", "up"], step=0.7, dur=4.6, source="PC Gamer, 2020"),
    dict(type="hook", kicker="Y ADEMÁS", lines=[("AHÍ ESTRENÓ", "w"), ("SU CANCIÓN", "w"), ("\"HOLIDAY\"", "y")],
         sizes=(120, 120, 160), icon="gift", dur=3.8, source="GameSpot"),
    dict(type="question", q=["¿IRÍAS A UN", "CONCIERTO EN ROBLOX?"], options=["SÍ, OBVIO", "PREFIERO JUGAR"], dur=4.2),
    dict(type="outro", dur=3.0),
], title="el-concierto-de-33-millones", audio="musica")
if __name__ == "__main__": main(ep)
