# Canal "No digas que no te avisé" — producción automática de Shorts

Canal de YouTube en español rioplatense/paraguayo (voseo: "usás", "mirá", "dejalo"). Sin cara, sin voz:
motion graphics con texto + efectos de sonido ASMR. Dueño: Diego (Paraguay, zona America/Asuncion).

## Tarea diaria (lo que hace cada ejecución programada)
Producir **2 Shorts nuevos** y dejarlos programados en Metricool para **hoy a las 15:00 y 20:00 (America/Asuncion)**.
Si ya pasaron esas horas, programar para mañana a las mismas horas. Antes de programar, revisar con
`getScheduledPosts` que esos horarios no estén ya ocupados (no duplicar).

1. **Elegir 2 temas** que NO estén en `historial.md` (ni el tema, ni el dato central, ni el gancho). Alternar pilares:
   - Cómo te enganchan las apps (diseño persuasivo, algoritmos, trucos de UX)
   - Mente y emociones (ansiedad, comparación social, sueño, atención, soledad, autoestima)
   - Chicos y pantallas (edades, estudios, leyes, consejos para padres)
   - Curiosidades y hábitos (datos raros del cerebro, retos, la vida en general, dinero, relaciones)
   Los dos videos del día deben ser de pilares distintos.
2. **Verificar los datos con WebSearch/WebFetch** (fuentes primarias o medios serios). Solo usar cifras que
   estén confirmadas; si no hay cifra exacta, no inventarla: mostrar la idea sin número. Guardar la fuente.
   Salud mental: tono de "ojo con esto / buscá ayuda", nunca diagnóstico ni alarmismo, nada sobre métodos de autolesión.
3. **Escribir el episodio** copiando `episodios/ejemplo_celular_en_la_cama.py` a `episodios/AAAA-MM-DD_slug.py`.
   - 25 s exactos, algo nuevo en pantalla cada ~4 s: gancho (0-4), 4 escenas de desarrollo, remate/consejo (20-23.2), `outro` (23.2-25).
   - Usar las herramientas de `motor/engine.py` (pop_line, slide_line, pill, stamp, íconos, clock, donut, battery, toggle_row...).
     Variar las animaciones y metáforas visuales entre videos: no repetir la misma estructura escena por escena.
     Si hace falta un ícono nuevo, dibujarlo en el episodio con primitivas de PIL.
   - Estilo fijo: fondo negro, amarillo #FFD60A, crema, rojo para alertas; Anton para titulares, Montserrat para subtítulos.
     Textos de titular en MAYÚSCULAS y cortos (que entren en 1080 px de ancho); subtítulos en minúscula.
   - Fuente del dato en pantalla, chica y gris, en la escena donde aparece.
   - Sonidos: `standard_sounds(BEATS)` + un `ev()` por cada aparición (pop/tap), golpes (thump/stamp) en datos fuertes,
     tick en contadores, toggle en interruptores, buzz para vibraciones, etc.
4. **Revisar antes de renderizar**: `python episodios/X.py preview /tmp/prev 100 215 330 450 560 670` y MIRAR
   los PNG (Read). Corregir textos encimados, cortados o fuera de pantalla. Recién ahí `python episodios/X.py build publicados/AAAA-MM-DD_slug.mp4`.
5. **Subir a GitHub**: `git add` (episodio + mp4 + historial) → `git commit` → `git push` a `main`.
   El video queda público en `https://raw.githubusercontent.com/diegobritez1993-sketch/shorts-canal/main/publicados/<archivo>.mp4`.
   Verificar con `curl -sI` que responde 200 antes de programar (puede tardar unos segundos tras el push).
6. **Programar en Metricool** (`createScheduledPost`, blogId `7762882`, timezone `America/Asuncion`):
   - providers `[{"network":"youtube"}]`, media `[<url raw>]`, autoPublish true, draft false
   - `youtubeData`: `{"title": <título>, "type": "short", "privacy": "public", "madeForKids": false, "category": "EDUCATION", "tags": [...]}`
   - `text` = descripción: 1-2 frases que enganchen + "Fuente: ..." + hashtags.
   - **Título**: atractivo, máx. ~70 caracteres, con 1 emoji al final, en voseo.
   - **Hashtags**: mínimo 3, siempre `#shorts` y `#nodigasquenoteavisé` + 1-4 del tema (ej. `#saludmental #redessociales`).
7. **Actualizar `historial.md`** con una fila por video (fecha, hora, pilar, tema, dato/fuente, archivo) y hacer push.
8. Mandar al usuario (SendUserMessage) un resumen corto: los 2 títulos, horarios y el link del planner de Metricool.

## Meta: 100 suscriptores → videos largos
Por ahora SOLO Shorts. En cada ejecución, consultar suscriptores con `getAnalyticsDataByMetrics`
(brandId 7762882, métrica `YTEV01`, rango últimos 7 días; tomar el valor más reciente) e incluirlos en el resumen al usuario.
Cuando llegue a **100 o más** y NO exista el archivo `hito_100.md` en el repo: avisarle al usuario con un mensaje bien visible
("¡Llegamos a 100 suscriptores! Ya podemos empezar con los videos largos de hasta 3 minutos"), crear `hito_100.md`
con la fecha y el número, y hacer push (así se avisa una sola vez). Igual seguir con los Shorts del día.
No empezar videos largos por cuenta propia: eso se decide con el usuario.

## Reglas
- Nunca repetir un tema del historial. Nunca publicar datos no verificados.
- No usar personajes, logos ni marcas de terceros en los gráficos (se puede nombrar una app en texto si es parte del dato).
- No borrar videos ni publicaciones existentes.
- Si algo falla (Metricool rechaza el video, push denegado), no reintentar en bucle: dejar el video en el repo y avisar al usuario qué pasó.
