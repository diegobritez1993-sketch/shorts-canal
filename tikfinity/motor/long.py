import sys, json, os
from engine import Scene, render_scene

IMG = {
    "inicio": "1793722010486_image.png", "config": "1793722086379_image.png",
    "error": "1793722108699_image.png", "puntos": "1793722117131_image.png",
    "bono": "1793722126692_image.png", "niveles": "1793722134762_image.png",
    "obs": "1793722140819_image.png", "sbot": "1793722150579_image.png",
    "mc1": "1793722182059_image.png", "mc2": "1793722189452_image.png",
}

def shot(img, badge, title, beats, dur, flip=False):
    bt, out = 0.9, []
    for b in beats:
        box, text, gap = b
        out.append({"t": bt, "box": box, "text": text})
        bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out, "dur": dur, "flip": flip}

S = [
    {"kind": "title", "kicker": "TUTORIAL 2026", "lines": ["TikFinity", "Configuración completa"],
     "sub": "Cuenta de TikTok · Puntos · Niveles · OBS · Streamer.bot · Minecraft", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Hoy dejás listo todo esto", "dur": 10,
     "items": ["Lo básico activado", "Tu cuenta de TikTok", "Sistema de puntos y niveles",
               "Conexión con OBS", "Conexión con Streamer.bot", "Minecraft con regalos"],
     "times": [0.8, 1.6, 2.4, 3.2, 4.0, 4.8]},
    shot("inicio", "PASO 1", "Activá lo básico", [
        ((368, 447, 984, 558), "En Inicio → Acceso Rápido tildá TTS, Sound Alerts y Acciones y Eventos.", 5.5),
        ((368, 447, 984, 558), "Si están destildados, la voz y las alertas no suenan en tu live.", 5.0),
        ((10, 256, 62, 322), "Ahora andá a Configuración: el ícono verde de la izquierda.", 5.0),
    ], 17.5),
    shot("config", "PASO 2", "Conectá tu cuenta de TikTok", [
        ((612, 403, 948, 438), "Escribí tu usuario de TikTok tal cual, sin el @.", 5.0),
        ((612, 455, 788, 489), "Tocá «Conectar a TikTok LIVE».", 4.5),
        ((612, 455, 788, 489), "Ojo: solo se conecta si YA estás en vivo.", 5.0),
        ((330, 86, 700, 106), "Arriba ves que ya está el nuevo TikFinity. Pronto hacemos video de cómo migrar.", 6.0),
    ], 22.5, flip=True),
    shot("error", "ERROR COMÚN", "«Tu transmisión está offline»", [
        ((307, 218, 852, 572), "Te sale cuando tu live de TikTok está apagado.", 5.0),
        ((307, 218, 852, 572), "Solución: primero abrí tu live en TikTok y después tocá Conectar.", 5.5),
        ((307, 218, 852, 572), "El resto de la configuración la podés hacer sin estar en vivo.", 5.0),
    ], 17.0),
    shot("puntos", "PASO 3", "Sistema de puntos", [
        ((612, 258, 948, 293), "Ponele nombre a tu moneda. Ej: «Tereré coins».", 5.0),
        ((388, 323, 948, 359), "Puntos por moneda: cuánto gana alguien por cada moneda que regala.", 5.5),
        ((388, 373, 948, 460), "Activá puntos por compartir y por minuto de chat para premiar a los que no regalan.", 6.0),
        ((388, 258, 948, 460), "Con esos puntos después suben de nivel y usan comandos.", 4.5),
    ], 22.5, flip=True),
    shot("bono", "PASO 4", "Bono para suscriptores", [
        ((612, 410, 948, 446), "Si tenés suscriptores en TikTok, dales más puntos.", 4.5),
        ((612, 410, 948, 446), "Ej: 50% = ganan la mitad más que el resto.", 4.5),
        ((612, 410, 948, 446), "¿Todavía sin suscriptores? Dejalo en 0%.", 4.0),
    ], 14.5),
    shot("niveles", "PASO 5", "Niveles de espectadores", [
        ((612, 437, 948, 472), "Puntos de Nivel: lo que hace falta para subir al nivel 2.", 5.0),
        ((612, 483, 948, 518), "Multiplicador: cada nivel pide un poco más. 1.03 = 3% más por nivel.", 5.5),
        ((612, 538, 780, 562), "Tocá «Mostrar lista de niveles» para ver cuánto pide cada uno.", 5.0),
    ], 17.0, flip=True),
    shot("obs", "PASO 6", "Conectá OBS", [
        ((368, 315, 1016, 430), "TikFinity puede cambiar escenas y fuentes de OBS con regalos. Necesitás OBS 28 o más nuevo.", 6.0),
        ((368, 315, 1016, 430), "En OBS: Herramientas → Configuración del Servidor WebSocket → habilitalo.", 6.0),
        ((612, 489, 948, 572), "Copiá los datos de «Mostrar información de conexión»: IP 127.0.0.1 y puerto 4455.", 6.0),
        ((612, 581, 948, 663), "Si OBS tiene contraseña, pegala y tocá «Probar Conexión».", 5.0),
    ], 25.0),
    shot("sbot", "PASO 7", "Conectá Streamer.bot", [
        ((368, 320, 1016, 445), "Con Streamer.bot disparás sus acciones desde los regalos de TikFinity.", 5.5),
        ((368, 320, 1016, 445), "En Streamer.bot activá el Servidor WebSocket (pestaña Servidores/Clientes).", 5.5),
        ((612, 496, 948, 670), "Dejá 127.0.0.1, puerto 8080 y punto final «/», y probá la conexión.", 5.5),
    ], 18.5, flip=True),
    shot("mc1", "PASO 8", "Minecraft con regalos", [
        ((368, 230, 1016, 310), "Tus viewers pueden invocar mobs o ejecutar comandos con regalos.", 5.0),
        ((388, 560, 1016, 612), "Mod de Fabric = jugás solo. Plugin ServerTap = servidor (Paper, Spigot o Bukkit).", 6.0),
        ((388, 478, 868, 537), "Importante: elegí uno solo. No uses los dos a la vez.", 5.0),
    ], 18.0),
    shot("mc2", "PASO 8", "Minecraft: últimos datos", [
        ((612, 247, 948, 282), "Con ServerTap poné tu nombre de jugador exacto (respeta mayúsculas).", 5.0),
        ((612, 447, 948, 530), "IP 127.0.0.1 y puerto 4567 ya vienen listos.", 4.5),
        ((612, 539, 948, 575), "Cambiá la contraseña «change_me» por una tuya y tocá «Probar Conexión».", 5.5),
    ], 17.0, flip=True),
    {"kind": "list", "title": "Checklist final", "dur": 10.5,
     "items": ["Acceso Rápido tildado", "Usuario sin @ y live abierto", "Puntos y niveles a tu gusto",
               "OBS: puerto 4455", "Streamer.bot: puerto 8080", "Minecraft: mod O plugin"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿TE SIRVIÓ?", "lines": ["Suscribite", "y activá la campanita"],
     "sub": "Todos los días hay un tutorial nuevo de TikFinity para tu live", "dur": 7.0, "fade_out": 0.8},
]

LABEL = "TikFinity · Configuración completa"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    idx = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else range(len(S))
    if sys.argv[1:] == ["events"]:
        pass
    for i in idx:
        out = f"/home/claude/build/long_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
