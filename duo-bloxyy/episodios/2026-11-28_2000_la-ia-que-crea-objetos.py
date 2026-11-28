"""Duo Bloxyy · 2026-11-28 20:00 · Secretos (Roblox Studio) · VOZ IA + MÚSICA
Fuentes: Roblox Newsroom (17/3/2025) "Introducing Roblox Cube": el modelo se llama Cube 3D, genera objetos 3D a partir
de texto; beta en Roblox Studio (Assistant, "/generate a motorcycle") y como API en Lua (Mesh Generation API);
Roblox libera una versión de código abierto (GitHub / Hugging Face). Ejemplos de prompts: "a red buggy with knobby tires",
"a green crystal fantasy sword with gold accents". TechCrunch (17/3/2025) lo confirma."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="SECRETO DE STUDIO", lines=[("ESCRIBÍS UNA", "w"), ("FRASE Y APARECE", "w"), ("UN OBJETO 3D", "y")],
         sizes=(130, 116, 140), icon="cube", dur=3.8, vo="Escribís una frase, y aparece un objeto en tres dé."),
    dict(type="hook", kicker="SE LLAMA", lines=[("CUBE 3D", "y"), ("LA IA DE ROBLOX", "w")],
         sizes=(180, 116), icon="star", dur=4.0, source="Roblox Newsroom, 2025",
         vo="Se llama Kiub tres dé: la inteligencia artificial de Roblox."),
    dict(type="hook", kicker="EN EL ASISTENTE DE STUDIO", lines=[("/GENERATE", "g"), ("A MOTORCYCLE", "w")],
         sizes=(160, 130), icon="chat", dur=4.2, source="Roblox Newsroom, 2025",
         vo="En el asistente de Studio escribís: yénereit a motorsaicol."),
    dict(type="list", title="EJEMPLOS DE ROBLOX", items=["UN BUGGY ROJO", "UNA ESPADA DE CRISTAL", "UN SILLÓN VERDE"],
         icons=["cube", "star", "check"], step=0.7, dur=4.8, source="Roblox Newsroom, 2025",
         vo="Un buggy rojo, una espada de cristal, un sillón verde."),
    dict(type="hook", kicker="MARZO 2025", lines=[("Y ES DE", "w"), ("CÓDIGO ABIERTO", "g")],
         sizes=(140, 140), icon="lock", dur=4.0, source="Roblox Newsroom / TechCrunch",
         vo="Salió en marzo de dos mil veinticinco, y es de código abierto."),
    dict(type="question", q=["¿QUÉ OBJETO", "CREARÍAS VOS?"], options=["UN AUTO", "UNA ESPADA", "OTRO: COMENTÁ"], dur=4.2,
         vo="¿Qué objeto crearías vos? Comentá."),
    dict(type="outro", dur=3.0),
], title="la-ia-que-crea-objetos", audio="musica")
if __name__ == "__main__": main(ep)
