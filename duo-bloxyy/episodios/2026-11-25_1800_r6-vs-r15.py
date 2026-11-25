"""Duo Bloxyy · 2026-11-25 18:00 · Historia · VOZ IA + ASMR
Fuentes: Roblox Newsroom oct. 2023 "How Roblox avatar tech is evolving" (R6 = avatares clásicos de 6 partes; R15 = hasta 15 partes;
capas de ropa y expresiones solo en R15); Roblox Wiki (Fandom) "R15": "Avatar 2.0" anunciado en enero de 2016 con
recepción mayormente negativa y rehecho como R15; R15 salió al público el 29 de septiembre de 2016."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="HISTORIA DE ROBLOX", lines=[("TU AVATAR", "w"), ("ANTES TENÍA", "w"), ("6 PARTES", "y")],
         sizes=(130, 120, 170), icon="cube", dur=3.8, vo="Tu avatar antes tenía solo seis partes."),
    dict(type="list", title="EL CLÁSICO R6", items=["CABEZA Y TORSO", "DOS BRAZOS", "DOS PIERNAS"],
         icons=["cube", "cube", "cube"], step=0.6, dur=4.2, source="Roblox Newsroom, 2023",
         vo="Cabeza, torso, dos brazos y dos piernas. Nada más."),
    dict(type="hook", kicker="ENERO DE 2016", lines=[("AVATAR 2.0", "y"), ("A LA GENTE", "w"), ("NO LE GUSTÓ", "r")],
         sizes=(160, 120, 130), icon="alert", dur=4.2, source="Roblox Wiki",
         vo="En dos mil dieciséis mostraron un avatar nuevo... y a la gente no le gustó."),
    dict(type="versus", title="SEPT. 2016 · PARTES", left=("R6", "6"), right=("R15", "15"),
         source="Roblox Wiki / Newsroom", dur=4.6,
         vo="Lo rehicieron, y en septiembre llegó erre quince: quince partes."),
    dict(type="question", q=["¿CON CUÁL", "JUGÁS VOS?"], options=["R6", "R15"], dur=4.2,
         vo="¿Vos cuál preferís? Comentá."),
    dict(type="outro", dur=3.0),
], title="r6-vs-r15", audio="asmr")
if __name__ == "__main__": main(ep)
