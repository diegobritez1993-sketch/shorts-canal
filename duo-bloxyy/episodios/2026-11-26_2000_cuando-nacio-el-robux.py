"""Duo Bloxyy · 2026-11-26 20:00 · Historia · VOZ IA + MÚSICA
Fuente: Roblox Wiki (Fandom) "Robux": Robux se agregó el 14 de mayo de 2007 y convivió con Tix; el nombre lo pensó
Shedletsky, mezcla de "ROBLOX" y "BUX" (bucks, dólares); desde el 26 de septiembre de 2008 se pudo comprar en la web;
el 21 de noviembre de 2019 el viejo símbolo R$ se cambió por el hexágono dorado redondeado."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="HISTORIA DE ROBLOX", lines=[("LOS ROBUX", "y"), ("NO EXISTIERON", "w"), ("DESDE SIEMPRE", "r")],
         sizes=(170, 120, 120), icon="gift", dur=3.6, vo="Los Robux no existieron desde siempre."),
    dict(type="hook", kicker="14 DE MAYO", lines=[("NACIERON", "w"), ("EN 2007", "y")],
         sizes=(140, 190), icon="star", dur=4.0, source="Roblox Wiki",
         vo="Llegaron en mayo de dos mil siete."),
    dict(type="versus", title="¿DE DÓNDE SALE?", left=("ROBLOX", "ROB"), right=("BUCKS", "BUX"),
         source="Roblox Wiki", dur=4.4, vo="Rob, de Roblox, más bux, de bucks: dólares en inglés."),
    dict(type="hook", kicker="QUIÉN LO INVENTÓ", lines=[("SHEDLETSKY", "y"), ("DEL EQUIPO", "w"), ("DE ROBLOX", "w")],
         sizes=(150, 120, 120), icon="trophy", dur=4.2, source="Roblox Wiki",
         vo="Se le ocurrió a Shédletski, del equipo de Roblox."),
    dict(type="change", name="NOVIEMBRE 2019", label="CAMBIO DE SÍMBOLO", before="R$", after="HEXÁGONO", up=True,
         note="el ícono dorado que ves hoy", source="Roblox Wiki", dur=4.4,
         vo="Y en dos mil diecinueve, el viejo erre con signo pasó a ser un hexágono."),
    dict(type="outro", dur=3.0),
], title="cuando-nacio-el-robux", audio="musica")
if __name__ == "__main__": main(ep)
