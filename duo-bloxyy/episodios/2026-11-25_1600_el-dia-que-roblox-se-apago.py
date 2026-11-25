"""Duo Bloxyy · 2026-11-25 16:00 · Misterios · SOLO TEXTO + MISTERIO
Fuente: DataCenterDynamics (2022) sobre el informe oficial de Roblox "Return to Service 10/28-10/31 2021": caída de 73 horas
desde el 28 de octubre de 2021, volvió por etapas el 30 de octubre; causa: una falla en Consul, su sistema interno
(una función nueva, "streaming", después de una actualización); le costó unos 25 millones de dólares en ventas."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="EL GRAN MISTERIO", lines=[("EL DÍA QUE", "w"), ("ROBLOX", "y"), ("SE APAGÓ", "r")],
         sizes=(120, 170, 160), icon="ghost", dur=3.6),
    dict(type="alert", lines=[("OCTUBRE 2021", "w"), ("73 HORAS", "r")], sizes=(100, 170), sub="NADIE PODÍA ENTRAR",
         source="DataCenterDynamics", dur=4.4),
    dict(type="trivia", q=["¿QUÉ LO", "APAGÓ?"], options=["A) UNOS HACKERS", "B) UNA FALLA INTERNA", "C) UN VIRUS"],
         answer=1, dur=7.0),
    dict(type="hook", kicker="LA VERDAD", lines=[("SE TRABÓ SU", "w"), ("PROPIO SISTEMA", "y"), ("TRAS UNA ACTUALIZACIÓN", "w")],
         sizes=(116, 120, 74), icon="lock", dur=4.4, source="Roblox / DataCenterDynamics"),
    dict(type="stat", title="LE COSTÓ CERCA DE", value=25, prefix="US$ ", suffix=" M", label="EN VENTAS",
         sub="volvió por etapas el 30 de octubre", source="DataCenterDynamics", dur=4.2),
    dict(type="outro", dur=3.0),
], title="el-dia-que-roblox-se-apago", audio="misterio", mood="dark")
if __name__ == "__main__": main(ep)
