"""Duo Bloxyy · 2026-11-27 20:00 · Secretos · SOLO TEXTO + MÚSICA
Fuentes: Roblox Creator Hub "Developer Console" (create.roblox.com/docs/studio/developer-console): se abre con F9,
escribiendo /console en el chat o desde Menú → Configuración; muestra registros, memoria, red y más.
Roblox Creator Hub "Identify performance issues": en el cliente, Shift+F5 muestra el resumen de estadísticas,
Shift+F3 las de red; Ctrl+Alt+F7 la barra de rendimiento (memoria, CPU, GPU, red y ping)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="SECRETO DE ROBLOX", lines=[("TECLAS", "y"), ("QUE CASI", "w"), ("NADIE USA", "w")],
         sizes=(200, 130, 130), icon="lock", dur=3.6),
    dict(type="hook", kicker="TECLA 1", lines=[("F9", "y"), ("ABRE LA CONSOLA", "w"), ("DE DESARROLLADOR", "w")],
         sizes=(240, 110, 104), icon="chat", dur=4.2, source="Roblox Creator Hub"),
    dict(type="hook", kicker="SIN TECLADO", lines=[("ESCRIBÍ", "w"), ("/console", "y"), ("EN EL CHAT", "w")],
         sizes=(130, 180, 130), icon="chat", dur=4.0, source="Roblox Creator Hub"),
    dict(type="list", title="MÁS ATAJOS", items=["SHIFT+F5: ESTADÍSTICAS", "SHIFT+F3: RED", "CTRL+ALT+F7: RENDIMIENTO"],
         icons=["star", "star", "check"], step=0.6, dur=4.6, source="Roblox Creator Hub"),
    dict(type="hook", kicker="¿PARA QUÉ SIRVE?", lines=[("VES TU PING,", "w"), ("MEMORIA", "y"), ("Y MÁS", "g")],
         sizes=(130, 160, 150), icon="clock", dur=4.0, source="Roblox Creator Hub"),
    dict(type="question", q=["¿CUÁL VAS", "A PROBAR?"], options=["F9", "SHIFT+F5", "/console"], dur=4.4),
    dict(type="outro", dur=3.0),
], title="teclas-secretas", audio="musica")
if __name__ == "__main__": main(ep)
