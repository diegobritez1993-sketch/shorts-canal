# Canal "GTA VI Clips Castellano": cómo se hacen los Shorts

Es un canal aparte de "No digas que no te avisé". Todo lo de este canal vive SOLO en la carpeta `gta6/`.
No tocar `CLAUDE.md`, `historial.md`, `episodios/`, `publicados/`, `tikfinity/` ni nada de los otros canales.

## Flujo
1. Diego pasa clips de Twitch (verticales u horizontales) y dice de qué streamer son, si no se ve en pantalla.
2. Mirar los clips: fotogramas cada 3 s, subtítulos cada 1 s y volumen por segundo. Elegir el gancho y recortar las partes muertas.
3. Agregar el trabajo a `JOBS` en `render.py` (o a `SETS` en `mix.py` para los mix) y renderizar:
   `python3 render.py <nombre>` / `python3 mix.py <nombre>`.
4. Antes de subir, MIRAR un fotograma de cada video.
5. Copiar a `gta6/publicados/AAAA-MM-DD_<nombre>.mp4`, commit y push a `main`. Comprobar que
   `https://raw.githubusercontent.com/diegobritez1993-sketch/shorts-canal/main/gta6/publicados/<archivo>` responde 200.
6. Programar en Metricool: marca **"Gta 6", blogId `8230703`**, timezone `America/Asuncion`, providers solo youtube,
   `type: short`, `category: GAMING`, `madeForKids: false`. NUNCA usar la marca 7762882 (es del otro canal).

## Estilo fijo (no cambiar sin que Diego lo pida)
- 1080×1920, 30 fps, audio normalizado a -14 LUFS.
- Cabecera negra de 0 a 330 px, dentro de la zona segura de Shorts (los íconos de YouTube tapan lo de más arriba):
  - "GTA VI CLIPS · CASTELLANO" en amarillo #FFD400 (Archivo Black, 30 px) en y=150, y el @ del streamer en gris a la derecha.
  - Título gancho en MAYÚSCULAS, Anton, blanco, centrado, con línea base fija (y = 262 - max_glyph_a).
  - Barra de progreso amarilla en y=322.
- Verticales: escalados a 1590 px de alto, debajo de la cabecera, con fondo desenfocado a los costados.
- Horizontales: cámara del streamer arriba (560 px de alto, y=350) y juego abajo (y=930). Si los subtítulos del
  juego son largos, usar `game="fit"` (ancho completo) en vez del recorte.
- Últimos 4 s: cartel amarillo "SUSCRÍBETE PARA TODO SOBRE GTA VI" en y=1530.
- Crédito del streamer: en pantalla (@) y en la descripción ("🎮 Clip de X → twitch.tv/x").
- Spoilers de la historia: "(SPOILER)" en el título del video y "⚠️ SPOILER" en el título de YouTube.

## Textos de YouTube
- Título: gancho con 1-2 palabras en MAYÚSCULAS + emoji + `#GTA6 #Shorts`.
- Descripción: 1 frase + crédito + "Seguí el canal para más clips de GTA VI en castellano 🔔" + hashtags
  (`#GTA6 #GTAVI #shorts` + streamer + `#GTA6Castellano`).
- Ritmo: entre 7 y 10 Shorts por día, más 1 mix por tanda de clips. Diego elige los horarios.
