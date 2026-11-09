# Canal "Mister DI YT": tutoriales de TikFinity (producción automática)

Canal de YouTube de Diego con tutoriales de **TikFinity** (herramienta para lives de TikTok).
Español con voseo, sin cara ni voz: capturas reales de TikFinity animadas (zoom + recuadro),
textos en pantalla, música y efectos originales generados por código (sin samples externos).

**Esta carpeta (`tikfinity/`) es la única que se toca.** El resto del repo `shorts-canal`
es de otro canal ("No digas que no te avisé"): nunca modificar `CLAUDE.md`, `historial.md`,
`episodios/`, `motor/` ni `publicados/` de la raíz.

## Calendario (hora de Paraguay, America/Asuncion)
- **Video largo** (horizontal 1920x1080, 2:30 a 4:00 min, con miniatura): **martes y viernes 18:30**.
- **Short** (vertical 1080x1920, 20 a 30 s): **todos los días 21:00**.
- Cada tanda produce 1 largo + los Shorts que cubran hasta la tanda siguiente:
  - Corrida del **lunes** → largo del martes + Shorts martes, miércoles y jueves (3).
  - Corrida del **jueves** → largo del viernes + Shorts viernes, sábado, domingo y lunes (4).
- Los Shorts salen del tema del largo de esa tanda (adelantos de cada parte).
- Antes de programar, revisar con getScheduledPosts (brandId 7851020) qué horarios ya están
  ocupados y **llenar todos los huecos libres** del período (si quedó algún día sin Short o un
  martes/viernes sin largo, cubrirlo). Nunca dejar un día sin Short ni un martes/viernes sin largo.

## Metricool
- Marca **7851020** ("Mitser Tikfinity"), SOLO provider `youtube`. Timezone America/Asuncion.
- Largo: `youtubeData.type "video"`, público, categoría EDUCATION, madeForKids false,
  `videoThumbnailUrl` = URL raw de la miniatura .jpg. Descripción con resumen, link
  https://tikfinity.zerody.one/, capítulos (0:00 ...) calculados de los tiempos de escena,
  y `#tikfinity #tiktoklive #streamer`. 8 tags.
- Short: `type "short"`, público, EDUCATION, madeForKids false, `videoCoverMilliseconds 1500`,
  **sin miniatura** (Diego no quiere miniaturas en Shorts). Texto: 1-2 frases + "Tutorial completo
  en el canal." + `#shorts #tikfinity` + 1 hashtag del tema.
- autoPublish true, draft false.
- Media = URL raw de GitHub:
  `https://raw.githubusercontent.com/diegobritez1993-sketch/shorts-canal/main/tikfinity/publicados/<archivo>`
  Confirmar con `curl -sI` que responde HTTP/2 200 antes de programar.

## Motor de video (`motor/`)
Los scripts usan rutas fijas: copiá `motor/*` y `capturas/*` a `/home/claude/build/`
y creá `/home/claude/out/` y `/home/claude/build/chk/`. Luego trabajá en `/home/claude/build`.
- `engine.py`: composición. Escenas `title`, `list`, `shot` (captura + panel de texto).
  En `shot`, cada beat = (recuadro en coordenadas de la captura ORIGINAL 1024x768, texto, segundos).
  El recuadro tiene que encerrar exactamente el elemento del que habla el texto: miralo en la captura.
- `audio.py`: música lo-fi original + efectos (`build(total, eventos, wav, seed, key)`).
  Cambiá `seed`/`key` en cada video para variar.
- Ejemplos completos: `long.py` + `long_audio.py` (ep. 1), `long2.py` + `l2_audio.py` (ep. 2),
  `shorts.py` / `shorts2.py` (Shorts), `thumb.py` / `thumb2.py` (miniaturas 1280x720).
- Para un episodio nuevo: copiá `long2.py` → `long3.py` (cambiá el prefijo de salida, p. ej. `l3_`),
  su audio, `shorts3.py` (nombres `s9_...`, `s10_...` correlativos) y `thumb3.py`.
- Renderizá escenas en 2 procesos en paralelo, uní con concat `-c copy` + audio (ver patrón en
  la conversación original: concat demuxer + `-map 0:v -map 1:a -c:a aac -b:a 192k -shortest
  -movflags +faststart`).
- **Antes del render completo**: dibujá cuadros de prueba en los momentos más cargados, armá una
  hoja de contacto y MIRALA. Corregí textos encimados, cortados o recuadros fuera de lugar.
  Después del render, sacá cuadros del mp4 final y miralos otra vez.
- Variá en cada video: kicker/estilo de títulos, orden de escenas (flip), seed/key de música,
  textos de tips. No repetir la misma estructura exacta (política de contenido repetitivo de YouTube).

## Contenido
- Solo tutoriales/tips/novedades de TikFinity y del live de TikTok relacionados.
- Investigá en la web lo actual de cada tema (TikFinity cambia: hay un "nuevo TikFinity" al que
  se puede migrar, app de escritorio para Windows, etiquetas PRO). **Nunca inventes** funciones,
  botones, precios ni pasos. Si una captura muestra PRO, decilo en el video.
- Todo lo que el video señale tiene que verse en las capturas de `capturas/` (ver `capturas/INDICE.md`).
- No repetir temas de `historial.md`. Un ángulo nuevo sobre una captura ya usada vale
  (p. ej. "errores comunes", "ideas para tu live") si aporta algo distinto.
- Cuando queden pocas capturas sin usar (menos de las necesarias para la próxima tanda),
  igual producí con lo que haya y **pedile a Diego capturas nuevas** en el resumen final,
  diciendo exactamente qué pantallas necesitás (p. ej. Sonidos, Acciones y Eventos, Chat de voz/TTS,
  Regalo Overlays, Últimos X, Temporizador, nuevo TikFinity).

## Al terminar
1. Copiar mp4 y miniatura a `tikfinity/publicados/`, actualizar `historial.md`, commit y push a main.
2. Programar en Metricool. Si algo falla, NO reintentar en bucle: mandar a Diego los archivos con
   SendUserFile y con SendUserMessage título, descripción, tags y hora para que lo suba él.
3. Resumen corto a Diego con SendUserMessage: títulos, días y horas, links del planner,
   y si hacen falta capturas nuevas.
