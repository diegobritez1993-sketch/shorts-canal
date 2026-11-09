import sys, os
from engine import Scene, render_scene
from long import shot
from audio import build

def hook(kicker, l1, l2, sub=None, dur=3.2):
    return {"kind": "title", "kicker": kicker, "lines": [l1, l2], "sub": sub, "dur": dur, "fade_in": 0.05}

def outro(dur=4.0):
    return {"kind": "title", "kicker": "MISTER DI", "lines": ["Tutorial completo", "en el canal"],
            "sub": "Seguime para un truco nuevo de TikFinity cada día", "dur": dur, "fade_out": 0.5}

SHORTS = {
    "s1_offline": ("TikFinity · Error de conexión", [
        hook("TIKFINITY", "¿No se conecta", "a tu live?", "Esto lo arregla en 10 segundos"),
        shot("error", "EL ERROR", "«Tu transmisión está offline»", [
            ((307, 218, 852, 572), "Sale cuando tu live de TikTok está apagado.", 4.0),
            ((307, 218, 852, 572), "Primero abrí el live en TikTok. Después tocá Conectar.", 4.5),
        ], 10.0),
        shot("config", "REVISÁ ESTO", "Tu usuario, bien escrito", [
            ((612, 403, 948, 438), "Tu usuario de TikTok tal cual, sin el @.", 4.0),
            ((612, 455, 788, 489), "Con el live abierto, tocá «Conectar a TikTok LIVE».", 4.5),
        ], 10.0),
        outro(),
    ]),
    "s2_obs": ("TikFinity · OBS", [
        hook("TIKFINITY + OBS", "Conectá OBS", "en 30 segundos", "Para que los regalos cambien tus escenas"),
        shot("obs", "OBS 28 O MÁS NUEVO", "Conectá OBS", [
            ((368, 315, 1016, 430), "En OBS: Herramientas → Configuración del Servidor WebSocket → habilitalo.", 5.0),
            ((612, 489, 948, 572), "En TikFinity: IP 127.0.0.1 y puerto 4455.", 4.5),
            ((612, 581, 948, 663), "Pegá la contraseña (si tiene) y tocá «Probar Conexión».", 4.5),
        ], 15.5),
        outro(),
    ]),
    "s3_minecraft": ("TikFinity · Minecraft", [
        hook("TIKFINITY + MINECRAFT", "¿Mod o plugin?", "No uses los dos", "Que tus viewers controlen tu Minecraft"),
        shot("mc1", "ELEGÍ UNO", "Mod o plugin", [
            ((388, 560, 1016, 612), "Mod de Fabric: jugás solo. Plugin ServerTap: servidor.", 4.5),
            ((388, 478, 868, 537), "Nunca los dos a la vez: no va a funcionar.", 4.0),
        ], 10.0),
        shot("mc2", "ÚLTIMO PASO", "Datos de conexión", [
            ((612, 447, 948, 530), "IP 127.0.0.1 y puerto 4567 ya vienen listos.", 4.0),
            ((612, 539, 948, 575), "Cambiá «change_me» por tu contraseña y probá.", 4.5),
        ], 10.0),
        outro(),
    ]),
    "s4_puntos": ("TikFinity · Puntos y niveles", [
        hook("TIKFINITY", "Premiá a los", "que no regalan", "Puntos y niveles para tu live"),
        shot("puntos", "PUNTOS", "Sistema de puntos", [
            ((612, 258, 948, 293), "Nombre de tu moneda: ponele algo tuyo.", 3.5),
            ((388, 373, 948, 460), "Activá puntos por compartir y por minuto de chat.", 4.5),
        ], 9.5),
        shot("niveles", "NIVELES", "Que suban de nivel", [
            ((612, 437, 948, 472), "Puntos de Nivel: lo que pide el nivel 2.", 3.5),
            ((612, 483, 948, 518), "Multiplicador: cada nivel pide un poco más.", 4.0),
        ], 9.0),
        outro(),
    ]),
}

W, H = 1080, 1920

def render(name, seed):
    label, S = SHORTS[name]
    starts, t = [], 0.0
    for s in S:
        starts.append(t); t += s["dur"]
    total = t
    parts = []
    for i, s in enumerate(S):
        out = f"/home/claude/build/{name}_{i}.mp4"
        if not os.path.exists(out):
            render_scene(Scene(s), W, H, starts[i], total, label, out)
        parts.append(out)
    ev = []
    for i, s in enumerate(S):
        if i: ev.append((starts[i] - 0.15, "whoosh"))
        if s["kind"] == "shot":
            for b in s["beats"]: ev.append((starts[i] + b["t"] + 0.05, "pop"))
        else:
            ev.append((starts[i] + 0.3, "ding"))
    wav = f"/home/claude/build/{name}.wav"
    build(total, ev, wav, seed=seed, key=[0, 2, -3, 5][seed % 4])
    lst = f"/home/claude/build/{name}.txt"
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    os.system(f"ffmpeg -loglevel error -y -f concat -safe 0 -i {lst} -i {wav} -map 0:v -map 1:a -c:v copy "
              f"-c:a aac -b:a 192k -shortest -movflags +faststart /home/claude/out/{name}.mp4")
    print("ok", name, total, flush=True)

if __name__ == "__main__":
    for k, n in enumerate(sys.argv[1:]):
        render(n, list(SHORTS).index(n) + 1)
