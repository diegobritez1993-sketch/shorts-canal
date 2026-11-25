"""Duo Bloxyy · 2026-11-25 14:00 · Cosas que no sabías · VOZ IA + MÚSICA
Fuente: GamesBeat (oct. 2025) sobre la carta a accionistas del 3er trimestre 2025 de Roblox: 151,5 millones de usuarios activos
por día, +70% interanual; los usuarios de 13 años o más crecieron 89% y los menores de 13, 44%."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="¿SABÍAS QUE...?", lines=[("¿CUÁNTOS JUEGAN", "w"), ("ROBLOX", "y"), ("CADA DÍA?", "w")],
         sizes=(110, 170, 130), icon="question", dur=3.6, vo="¿Cuánta gente juega Roblox cada día?"),
    dict(type="hook", kicker="TERCER TRIMESTRE 2025", lines=[("151,5", "y"), ("MILLONES", "w"), ("POR DÍA", "w")],
         sizes=(220, 140, 110), icon="cube", dur=4.4, source="GamesBeat / Roblox, 2025",
         vo="Ciento cincuenta y un millones y medio de personas. Por día."),
    dict(type="stat", title="EN UN SOLO AÑO", value=70, prefix="+", suffix="%", label="MÁS JUGADORES",
         sub="comparado con el mismo período del año anterior", source="GamesBeat / Roblox, 2025", dur=4.4,
         vo="Y en un solo año, creció un setenta por ciento."),
    dict(type="versus", title="¿QUIÉN CRECIÓ MÁS?", left=("MENORES DE 13", "+44%"), right=("13 AÑOS O MÁS", "+89%"),
         source="GamesBeat / Roblox, 2025", dur=4.6,
         vo="Y lo que más creció no fueron los chicos: fueron los de trece o más."),
    dict(type="question", q=["¿VOS JUGÁS", "TODOS LOS DÍAS?"], options=["SÍ, SIEMPRE", "A VECES", "CASI NUNCA"], dur=4.4,
         vo="¿Y vos, jugás todos los días? Comentá."),
    dict(type="outro", dur=3.0),
], title="150-millones-por-dia", audio="musica")
if __name__ == "__main__": main(ep)
