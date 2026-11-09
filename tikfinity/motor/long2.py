import sys, os
from engine import Scene, render_scene

def shot(img, badge, title, beats, dur, flip=False):
    bt, out = 0.9, []
    for box, text, gap in beats:
        out.append({"t": bt, "box": box, "text": text}); bt += gap
    return {"kind": "shot", "img": img + ".png", "badge": badge, "title": title, "beats": out, "dur": dur, "flip": flip}

S = [
    {"kind": "title", "kicker": "TUTORIAL 2026", "lines": ["TikFinity", "Metas en tu live"],
     "sub": "Likes · Follows · Shares · Espectadores · Suscriptores", "dur": 6.5, "fade_in": 0.2},
    {"kind": "list", "title": "Lo que vas a aprender", "dur": 9.5,
     "items": ["Qué son las superposiciones", "Crear una meta de likes", "Meta de follows con sorteo",
               "Shares y espectadores", "Suscriptores y metas a medida", "Novedades de TikFinity"],
     "times": [0.8, 1.5, 2.2, 2.9, 3.6, 4.3]},
    shot("galeria", "PASO 1", "Superposiciones", [
        ((14, 333, 58, 380), "Entrá a Superposiciones: el ícono azul de la izquierda.", 5.0),
        ((346, 340, 1016, 435), "Son widgets que se ven arriba de tu live: metas, alertas, regalos y más.", 5.5),
        ((346, 340, 1016, 435), "Cada una tiene un link. Lo copiás y lo pegás como fuente en OBS o en TikTok Live Studio.", 6.0),
        ((76, 225, 312, 260), "Hoy vamos con Superposiciones de Metas.", 4.5),
    ], 23.5),
    shot("likes", "PASO 2", "Meta de likes", [
        ((368, 338, 455, 376), "Meta: cuántos likes querés juntar. Ej: 15.000.", 4.5),
        ((460, 338, 555, 376), "Título: lo que ve tu público. Ej: «llegamos a 15K y sorteo».", 5.0),
        ((560, 338, 745, 376), "Cuando se alcance: dejar la meta igual o subirla sola.", 4.5),
        ((749, 332, 897, 373), "Acción al alcanzar: dispara una alerta o sonido cuando llegás.", 5.0),
    ], 21.5, flip=True),
    shot("likes", "PASO 2", "Ponela en tu live", [
        ((688, 380, 834, 415), "Tocá «Copy URL» para copiar el link de la meta.", 4.5),
        ((838, 380, 940, 415), "Con «Test» ves cómo se llena sin estar en vivo.", 4.5),
        ((368, 425, 1016, 610), "Con las flechas cambiás el estilo: hay 7 diseños.", 4.5),
        ((14, 260, 312, 300), "Ojo: al lado de cada meta ves la etiqueta PRO. Revisá qué te deja usar tu plan.", 5.5),
    ], 20.5),
    shot("follows", "PASO 3", "Meta de follows", [
        ((368, 360, 455, 394), "Una meta chica funciona mejor: 50 follows se cumple en un live.", 5.0),
        ((460, 360, 555, 394), "En el título prometé algo: «a los 50 sorteamos 1».", 4.5),
        ((368, 450, 1016, 635), "La barra se llena en vivo: tu público ve cuánto falta y se suma.", 5.0),
    ], 16.0, flip=True),
    shot("shares", "PASO 4", "Meta de compartidos", [
        ((368, 447, 455, 482), "Shares: cuántas veces comparten tu live. Ej: 1.000.", 4.5),
        ((368, 537, 1016, 690), "Más compartidos = TikTok le muestra tu live a más gente.", 5.0),
    ], 11.0),
    shot("viewers", "PASO 5", "Meta de espectadores", [
        ((368, 371, 455, 407), "Viewer Count: cuántas personas mirando al mismo tiempo.", 5.0),
        ((460, 371, 555, 407), "Cambiá «Viewer Goal» por tu propio texto.", 4.0),
        ((368, 463, 1016, 610), "Sirve para motivar: «¡a los 100 hacemos reto!».", 4.5),
    ], 15.0, flip=True),
    shot("subs", "PASO 6", "Suscriptores y metas a medida", [
        ((348, 185, 1016, 575), "Nuevos suscriptores: ideal si ya tenés suscripciones en TikTok.", 5.0),
        ((348, 605, 1016, 700), "Objetivos personalizados: los controlás con Acciones y Eventos.", 5.0),
        ((348, 605, 1016, 700), "Ej: que un regalo especial sume o reste puntos a la meta.", 4.5),
    ], 16.0),
    shot("ultimo", "NOVEDADES", "Lo último de TikFinity", [
        ((380, 205, 780, 290), "Ya hay app de escritorio para Windows, más estable y con funciones extra.", 5.5),
        ((380, 325, 780, 375), "Integración con Voicemod: tus viewers te cambian la voz.", 5.0),
        ((380, 425, 780, 510), "Beneficios extra para los miembros de equipo de TikTok.", 5.0),
    ], 17.0, flip=True),
    {"kind": "list", "title": "Tips para que tus metas funcionen", "dur": 11.0,
     "items": ["Metas chicas y alcanzables", "Premio claro en el título", "Nombrá la meta en voz alta",
               "Probá con Test antes del live", "Una o dos metas, no todas", "Subí la meta al cumplirla"],
     "marks": ["✓"] * 6, "times": [0.6, 1.2, 1.8, 2.4, 3.0, 3.6]},
    {"kind": "title", "kicker": "¿TE SIRVIÓ?", "lines": ["Suscribite", "y activá la campanita"],
     "sub": "Tutoriales nuevos de TikFinity todas las semanas", "dur": 7.0, "fade_out": 0.8},
]
LABEL = "TikFinity · Metas en tu live"
W, H = 1920, 1080

def timeline():
    t, out = 0.0, []
    for s in S:
        out.append(t); t += s["dur"]
    return out, t

if __name__ == "__main__":
    starts, total = timeline()
    for i in [int(a) for a in sys.argv[1:]]:
        out = f"/home/claude/build/l2_{i:02d}.mp4"
        if os.path.exists(out): continue
        render_scene(Scene(S[i]), W, H, starts[i], total, LABEL, out)
        print("ok", i, flush=True)
