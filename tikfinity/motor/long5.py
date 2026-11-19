import sys, os
from engine import Scene, render_scene

IMG = {"config": "1793722086379_image.png", "error": "1793722108699_image.png",
       "puntos": "1793722117131_image.png", "obs": "1793722140819_image.png",
       "sbot": "1793722150579_image.png", "mc1": "1793722182059_image.png",
       "mc2": "1793722189452_image.png", "likes": "likes.png"}

def shot(img, badge, title, beats, dur=None, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out,
            "dur": dur or round(bt + 0.8, 1), "flip": flip}

# recuadros (coordenadas de la captura original 1024x768)
E_DIALOG = (307, 218, 852, 572)
E_INICIA = (322, 343, 836, 364)
E_CONFIG = (322, 362, 836, 382)
C_LABEL = (384, 408, 602, 436)
C_USER = (612, 403, 948, 438)
C_BTN = (612, 455, 788, 489)
O_REQ = (364, 354, 600, 376)
O_WS = (364, 375, 1016, 417)
O_IP = (364, 417, 1016, 439)
O_PORT = (612, 489, 948, 618)
O_TEST = (612, 627, 772, 663)
B_WS = (364, 384, 1016, 425)
B_DATA = (612, 496, 948, 624)
B_TEST = (612, 634, 772, 670)
M_AMBOS = (384, 478, 1016, 538)
M_DESC = (384, 560, 1016, 612)
M_SERV = (364, 268, 1016, 310)
N_NAME = (612, 247, 948, 282)
N_CASE = (384, 200, 1016, 228)
N_PASS = (612, 539, 948, 575)
N_TEST = (612, 585, 772, 621)
L_ROW = (364, 302, 1016, 374)
L_MISMATCH = (438, 494, 862, 528)
L_META = (364, 336, 556, 374)
L_TEST = (836, 380, 942, 416)
L_PRO = (96, 262, 300, 620)
P_MONEDA = (384, 323, 948, 360)
P_OTROS = (384, 373, 948, 460)
P_NOMBRE = (612, 258, 948, 293)

S = [
    {"kind": "title", "kicker": "ERRORES COMUNES", "lines": ["8 errores que", "arruinan tu live"],
     "sub": "TikFinity: cómo detectarlos y arreglarlos antes de salir en vivo", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Revisá si te pasa alguno", "dur": 10.0,
     "items": ["Conectar antes del live", "Usuario mal escrito", "OBS que no conecta", "Streamer.bot sin servidor",
               "Mod y plugin a la vez", "Nombre del jugador", "Metas con título equivocado", "Puntos solo por regalos"],
     "times": [0.8, 1.4, 2.0, 2.6, 3.2, 3.8, 4.4, 5.0]},
    shot("error", "ERROR 1", "Conectar antes del live", [
        (E_DIALOG, "«Tu transmisión está offline»: TikFinity no encuentra tu directo.", 5.0),
        (E_INICIA, "Primero iniciá el live en TikTok y recién ahí tocá Conectar.", 5.0),
        (E_CONFIG, "Lo bueno: la configuración la podés hacer con el live apagado.", 5.0),
    ]),
    shot("config", "ERROR 2", "Tu usuario mal escrito", [
        (C_LABEL, "«Tu Nombre en TikTok» es obligatorio.", 4.5),
        (C_USER, "Escribilo tal cual es tu usuario, sin el @.", 4.5),
        (C_BTN, "Con el live abierto, tocá «Conectar a TikTok LIVE».", 4.5),
    ], flip=True),
    shot("obs", "ERROR 3", "OBS que no conecta", [
        (O_REQ, "TikFinity pide OBS 28 o superior: si el tuyo es viejo, actualizalo.", 5.0),
        (O_WS, "En OBS: Herramientas → Configuración del Servidor WebSocket → habilitalo.", 5.5),
        (O_IP, "La IP 127.0.0.1 sirve solo si OBS corre en la misma PC.", 5.0),
        (O_PORT, "Copiá puerto y contraseña de «Mostrar Información de Conexión».", 5.0),
        (O_TEST, "Y tocá «Probar Conexión» antes de salir en vivo.", 4.5),
    ]),
    shot("sbot", "ERROR 4", "Streamer.bot sin servidor", [
        (B_WS, "En Streamer.bot activá el Servidor WebSocket (pestaña «Servidores/Clientes»).", 5.5),
        (B_DATA, "En TikFinity: dirección 127.0.0.1, puerto 8080 y punto final «/».", 5.0),
        (B_TEST, "Probá la conexión antes del live.", 4.0),
    ], flip=True),
    shot("mc1", "ERROR 5", "Mod y plugin a la vez", [
        (M_AMBOS, "Para Minecraft: elegí mod o plugin. «¡No uses ambos a la vez!»", 5.0),
        (M_DESC, "Mod de Fabric si jugás solo; plugin ServerTap si tenés servidor.", 5.0),
        (M_SERV, "El plugin va en servidores Bukkit, Spigot o PaperMC.", 4.5),
    ]),
    shot("mc2", "ERROR 6", "El nombre del jugador", [
        (N_NAME, "Con el plugin ServerTap, escribí tu nombre de jugador.", 4.5),
        (N_CASE, "Respetá mayúsculas y minúsculas, tal cual en el juego.", 4.5),
        (N_CASE, "Si lo dejás vacío, los comandos van a todos los jugadores (@a).", 5.0),
        (N_PASS, "La documentación de ServerTap explica cómo cambiar la contraseña.", 5.0),
        (N_TEST, "Validá todo con «Probar Conexión».", 4.0),
    ], flip=True),
    shot("likes", "ERROR 7", "Metas con título equivocado", [
        (L_ROW, "Cada meta tiene Meta, Título y qué pasa al alcanzarla.", 4.5),
        (L_MISMATCH, "Mirá este: el título dice 50000, pero la meta es 15.000.", 5.0),
        (L_META, "El número del título tiene que coincidir con la Meta.", 4.5),
        (L_TEST, "Tocá «Test» para ver cómo queda antes del live.", 4.5),
        (L_PRO, "Ojo: estas metas tienen la etiqueta PRO.", 4.5),
    ]),
    shot("puntos", "ERROR 8", "Puntos solo por regalos", [
        (P_MONEDA, "Si solo tildás «Puntos por moneda», suman únicamente los que regalan.", 5.5),
        (P_OTROS, "Tildá también compartir y minuto de chat: premiás a todos.", 5.0),
        (P_NOMBRE, "Y ponele un nombre propio a tu moneda.", 4.0),
    ], flip=True),
    {"kind": "list", "title": "Checklist antes de cada live", "dur": 11.0,
     "items": ["Live abierto, después Conectar", "Usuario sin el @", "OBS 28+ con WebSocket activo",
               "«Probar Conexión» en todo", "Un solo método en Minecraft", "Títulos de metas revisados"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿CUÁL TE PASÓ?", "lines": ["Contame en", "los comentarios"],
     "sub": "Suscribite: tutoriales nuevos de TikFinity cada semana", "dur": 7.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Errores comunes"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l5_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
