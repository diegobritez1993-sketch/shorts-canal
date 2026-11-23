"""Duo Bloxyy · 2026-11-23 20:00 · Trivia · SOLO TEXTO + MÚSICA
Fuentes: Wikipedia "David Baszucki" (cofundador y CEO de Roblox, usuario builderman); Charlie INTEL (builderman era amigo
por defecto; quienes empezaron después de agosto de 2021 ya no lo tienen)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="TRIVIA ROBLOX", lines=[("SOLO LOS VETERANOS", "w"), ("SABEN ESTO", "y")], sizes=(100, 140), icon="question", dur=3.2),
    dict(type="trivia", q=["¿QUIÉN ERA", "BUILDERMAN?"], options=["A) UN BOT", "B) SU CREADOR", "C) UN HACKER"], answer=1, dur=7.0),
    dict(type="hook", kicker="RESPUESTA", lines=[("ERA LA CUENTA DE", "w"), ("DAVID BASZUCKI", "y"), ("COFUNDADOR DE ROBLOX", "w")],
         sizes=(96, 120, 84), icon="trophy", dur=4.4, source="Wikipedia"),
    dict(type="hook", kicker="¿TE ACORDÁS?", lines=[("ERA EL AMIGO", "w"), ("QUE TE APARECÍA", "y"), ("AL CREAR TU CUENTA", "w")],
         sizes=(110, 110, 96), icon="cube", dur=4.4, source="Charlie INTEL"),
    dict(type="question", q=["¿LO TENÍAS", "DE AMIGO?"], options=["SÍ", "NO"], dur=4.2),
    dict(type="outro", dur=3.0),
], title="quien-era-builderman", audio="musica")
if __name__ == "__main__": main(ep)
