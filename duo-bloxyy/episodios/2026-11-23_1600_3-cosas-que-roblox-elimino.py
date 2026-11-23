"""Duo Bloxyy · 2026-11-23 16:00 · Cosas que no sabías · SOLO TEXTO + ASMR
Fuentes: Roblox Newsroom sept. 2019 (Premium reemplaza a Builders Club); Roblox Wiki (Fandom): Tix 10 por día, retirados abr. 2016; invitados retirados en PC oct. 2017."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="YA NO EXISTEN", lines=[("3 COSAS QUE", "w"), ("ROBLOX", "y"), ("ELIMINÓ", "r")], icon="lock", dur=3.4),
    dict(type="change", name="#3 MODO INVITADO", label="JUGAR SIN CUENTA", before="EXISTÍA", after="CHAU EN 2017", up=False,
         note="se podía entrar sin registrarse", dur=4.4),
    dict(type="change", name="#2 LOS TIX", label="MONEDA GRATIS", before="10 POR DÍA", after="CHAU EN 2016", up=False,
         note="se ganaban solo por entrar", source="Roblox Wiki", dur=4.4),
    dict(type="change", name="#1 BUILDERS CLUB", label="LA MEMBRESÍA", before="BUILDERS CLUB", after="PREMIUM", up=True,
         note="la reemplazó en septiembre de 2019", source="Roblox Newsroom, 2019", dur=4.6),
    dict(type="question", q=["¿CUÁL EXTRAÑÁS", "MÁS?"], options=["INVITADOS", "TIX", "BUILDERS CLUB"], dur=4.6),
    dict(type="outro", dur=3.0),
], title="3-cosas-que-roblox-elimino", audio="asmr")
if __name__ == "__main__": main(ep)
