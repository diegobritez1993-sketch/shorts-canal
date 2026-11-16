import sys, os
from engine import Scene, render_scene

IMG = {"canales": "canales_en_directo.png", "trans": "transacciones.png", "ultimo": "ultimo.png",
       "inicio2": "inicio2.png"}

def shot(img, badge, title, beats, dur, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": IMG[img], "badge": badge, "title": title, "beats": out, "dur": dur, "flip": flip}

M_CANALES = (100, 418, 240, 442)
GRID = (334, 296, 992, 622)
CARD = (342, 300, 552, 354)
MAS = (500, 638, 620, 678)
T_HEAD = (400, 302, 988, 400)
T_LIKE = (560, 351, 900, 374)
T_DONUT = (560, 444, 940, 467)
T_TOTAL = (405, 542, 715, 568)
U_GTA = (800, 426, 1016, 532)
U_TECLAS = (800, 544, 1016, 674)
U_MC = (376, 544, 782, 652)
A_EVENTOS = (792, 242, 984, 356)
A_ATAJO = (792, 326, 984, 350)

S = [
    {"kind": "title", "kicker": "IDEAS PARA TU LIVE", "lines": ["5 ideas para un live", "más interactivo"],
     "sub": "Con TikFinity: que tu público juegue con vos", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Lo que vas a ver hoy", "dur": 9.5,
     "items": ["Inspirate en otros streamers", "Mirá qué regala la gente", "Que manejen tu GTA 5",
               "Que aprieten teclas en tu PC", "Minecraft controlado por el chat", "Dónde se activa todo"],
     "times": [0.8, 1.5, 2.2, 2.9, 3.6, 4.3]},
    shot("canales", "IDEA 1", "Canales en directo", [
        (M_CANALES, "En Inicio, abrí «Canales en directo».", 4.5),
        (GRID, "Ves streamers que usan TikFinity y están en vivo ahora.", 5.0),
        (CARD, "Cada tarjeta muestra cuánta gente lo está mirando.", 4.5),
        (MAS, "Tocá «Mostrar más» para ver más canales.", 4.0),
        (GRID, "Entrá a dos o tres y fijate qué alertas y metas usan.", 5.0),
    ], 25.0),
    shot("trans", "IDEA 2", "Transacciones en tiempo real", [
        (T_HEAD, "Usuario, cantidad y descripción de cada regalo, en vivo.", 5.0),
        (T_DONUT, "Ejemplo: un Doughnut son 30 coins.", 4.5),
        (T_LIKE, "También aparecen acciones, como un «like».", 4.5),
        (T_TOTAL, "Ya van más de 6.800 millones de transacciones.", 4.5),
        (T_HEAD, "Mirá qué regalos se repiten y usalos en tus metas.", 5.0),
    ], 25.0, flip=True),
    shot("ultimo", "IDEA 3", "Que manejen tu GTA 5", [
        (U_GTA, "En «Lo último y lo mejor»: el plugin de GTA 5 para TikFinity.", 5.0),
        (U_GTA, "Tus espectadores disparan acciones en el juego mandando regalos.", 5.5),
        (U_GTA, "Abajo está el link al tutorial oficial para instalarlo.", 5.0),
    ], 17.5),
    shot("ultimo", "IDEA 4", "Simulador de teclas", [
        (U_TECLAS, "Con regalos, tus viewers controlan apps de tu PC con Windows.", 5.5),
        (U_TECLAS, "La función se llama Simulación de Teclas.", 4.5),
        (U_TECLAS, "Está en Acciones y Eventos, y también tiene tutorial.", 5.0),
    ], 17.0, flip=True),
    shot("ultimo", "IDEA 5", "Minecraft controlado por el chat", [
        (U_MC, "Con la integración de Minecraft, controlan tu juego con regalos y otros eventos.", 5.5),
        (U_MC, "Mod de Fabric si jugás solo, plugin si tenés servidor.", 5.0),
        (U_MC, "La conexión paso a paso está en nuestro primer tutorial.", 4.5),
    ], 17.0),
    shot("inicio2", "DÓNDE SE ACTIVA", "Acciones y Eventos", [
        (A_EVENTOS, "Todo esto vive en «Acciones y Eventos»: dejalo en Habilitado.", 5.0),
        (A_EVENTOS, "Ahí unís cada regalo o evento con lo que tiene que pasar.", 5.0),
        (A_ATAJO, "«Establecer Atajo de Teclado»: manejalo con una tecla.", 5.0),
    ], 17.0, flip=True),
    {"kind": "list", "title": "Tu plan para el próximo live", "dur": 11.0,
     "items": ["Mirá 2 o 3 canales en directo", "Elegí los regalos que más se repiten", "Empezá con 1 o 2 acciones",
               "Uní cada regalo a su acción", "Probá todo antes de salir", "Contá en el live qué hace cada uno"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿CUÁL VAS A PROBAR?", "lines": ["Contame en", "los comentarios"],
     "sub": "Suscribite: tutoriales nuevos de TikFinity cada semana", "dur": 7.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Ideas para tu live"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l4_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
