"""Duo Bloxyy · 2026-11-24 18:00 · Misterios y leyendas · SOLO TEXTO + MISTERIO
Fuente: Dot Esports "Who is 1x1x1x1 in Roblox" (2024): cuenta alternativa creada en 2010 por John Shedletsky, ex desarrollador
de Roblox, usada para pruebas; la comunidad la convirtió en un "hacker"; la cuenta fue cerrada; aparece como jefe final del
evento The Classic. Se cuenta como LEYENDA y con la verdad al final."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="LEYENDA DE ROBLOX", lines=[("EL HACKER", "w"), ("MÁS TEMIDO:", "w"), ("1X1X1X1", "r")],
         sizes=(120, 120, 170), icon="ghost", dur=3.8),
    dict(type="list", title="LO QUE SE DECÍA", items=["ERA UN HACKER", "ROMPÍA LAS REGLAS", "NADIE SABÍA QUIÉN ERA"],
         icons=["alert", "lock", "question"], step=0.7, dur=4.6),
    dict(type="trivia", q=["¿QUÉ ERA", "EN REALIDAD?"], options=["A) UN VIRUS", "B) UNA CUENTA DE PRUEBA", "C) UN BOT"],
         answer=1, dur=7.0),
    dict(type="hook", kicker="LA VERDAD", lines=[("LA CREÓ EN 2010", "w"), ("JOHN SHEDLETSKY", "y"), ("EX DESARROLLADOR", "w")],
         sizes=(110, 116, 100), icon="lock", dur=4.4, source="Dot Esports"),
    dict(type="hook", kicker="¿Y HOY?", lines=[("NUNCA FUE", "w"), ("UN HACKER", "g"), ("SOLO UNA LEYENDA", "y")],
         sizes=(120, 150, 104), icon="check", dur=4.0),
    dict(type="outro", dur=3.0),
], title="el-misterio-de-1x1x1x1", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
