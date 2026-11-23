# Canal "Duo Bloxyy": producción automática de Shorts de Roblox

Canal de YouTube de Diego y su hija sobre Roblox, en español con voseo ("mirá", "tenés", "comentá"). Sin cara.
Todo lo de este canal vive SOLO en la carpeta `duo-bloxyy/`. No tocar `CLAUDE.md` de la raíz, `episodios/`, `publicados/`,
`tikfinity/`, `gta6/`, `historias-rock/` ni nada de los otros canales.

## Tarea diaria
**4 Shorts por día, a las 14:00, 16:00, 18:00 y 20:00 (America/Asuncion)**, programados en Metricool.
- Revisar con `getScheduledPosts` (brandId **8312161**, timezone America/Asuncion) qué horarios de hoy ya están ocupados.
  Producir solo los horarios de hoy libres y que todavía no pasaron (con al menos 30 min de margen). Si no queda ninguno hoy,
  producir los 4 de mañana. Nunca duplicar un horario.

## Mezcla de cada día (variar, que no sea repetitivo)
- **2 con voz IA** (`vo="..."` en las escenas) y **2 solo texto** (sin `vo`). Alternar el orden día a día.
- Audio: `audio="musica"` (chiptune alegre), `audio="asmr"` (sin música, taps y clicks suaves) o `audio="misterio"`
  (pad oscuro + latido, con `mood="dark"`). Cada día al menos 1 con música y 1 con ASMR. Los misterios/leyendas van con "misterio".
- Temas (4 pilares, uno por video, rotando): **Misterios y leyendas** · **Secretos** (cosas ocultas, trucos, Roblox Studio) ·
  **Cosas que no sabías** · **Historia de Roblox** (cómo empezó, qué cambió). Ideas: hoja "Duo Bloxyy · Calendario de Shorts"
  y las que vayan surgiendo (juegos populares, novedades, eventos actuales de Roblox).
- Estructuras distintas: dato único, top 3 (escenas `change`/`list`), quiz (`trivia`), antes vs. ahora (`versus`/`change`),
  leyenda, línea de tiempo, encuesta (`question`). No repetir la misma secuencia de escenas dos veces el mismo día.
- Público real: chicos y adolescentes que juegan Roblox. Estilo dinámico (algo nuevo cada 3-5 s, gancho fuerte en el
  segundo 1) pero NO "contenido para niños": nada de tono infantil, "amiguitos", canciones de cuna. Siempre `madeForKids: false`.

## Reglas de contenido
1. **Verificar cada dato en la web** (WebSearch/WebFetch: Roblox Newsroom/blog/DevForum, Roblox Wiki de Fandom, medios de
   videojuegos serios). Guardar la fuente en el docstring del episodio y `source="..."` en la escena del dato. Nunca inventar
   fechas, cifras ni nombres. Si una fecha es dudosa (fuentes que no coinciden), no darla exacta.
2. **Leyendas y creepypastas** (John Doe, Guest 666, 1x1x1x1...): contarlas SIEMPRE como leyendas de la comunidad y decir
   la verdad al final. Nada de sustos fuertes, violencia ni contenido perturbador.
3. **Sin logos, personajes ni arte oficial de Roblox** dibujados ni descargados. Se puede nombrar "Roblox" y juegos en el texto.
   Los íconos del motor (cubo, fantasma, candado, trofeo, signo de pregunta, etc.) son genéricos.
   Si Diego sube capturas propias a `duo-bloxyy/capturas/`, se pueden usar con `bg=` o `card=` (ver motor).
4. No pedir datos personales, no promocionar estafas de "Robux gratis", no dar links externos.
5. No repetir temas de `historial.md` (ni el tema, ni el dato central, ni el gancho).

## Cómo se hace un episodio
- Copiar un episodio de `episodios/` a `episodios/AAAA-MM-DD_HHMM_slug.py` (empieza con `from _base import *`).
- Motor: `motor/bloxy_engine.py` (tipos de escena en su docstring: hook, stat, change, list, versus, alert, question,
  trivia, outro). 22-30 s en total, escenas de 3-5 s (trivia 7 s), siempre termina con `outro`.
  Al menos 2 de los 4 del día terminan con `question` (pregunta para comentarios). Titulares en MAYÚSCULAS y cortos.
- Voz IA (Piper "carlfm", se instala sola): frases cortas en voseo (~2,5 palabras por segundo de escena), números con letras
  ("dos mil seis"), nombres en inglés escritos como se pronuncian ("Yon Dou", "Daina Blocks", "Bílderman").
  Ojo: `stat` muestra números con punto de miles (2006 → "2.006"): para años usar `hook` con el texto.
- Preview: `python3 episodios/X.py preview /tmp/pv t1 t2 ...` (un tiempo por escena) y MIRAR la hoja (Read) antes de renderizar.
  Corregir textos encimados, cortados o fuera de pantalla.
- Build: `python3 episodios/X.py build publicados/X.mp4` (~2 min cada uno; se pueden hacer 2 en paralelo).

## Subir y programar
1. Actualizar `historial.md` (una fila por video), `git pull --rebase`, commit y push a `main`
   (si falla por cambios remotos: `git pull --rebase` y reintentar una vez).
2. Confirmar con `curl -sI` que `https://raw.githubusercontent.com/diegobritez1993-sketch/shorts-canal/main/duo-bloxyy/publicados/<archivo>.mp4` responde 200.
3. `createScheduledPost` con **blogId 8312161** (marca "Duo Bloxyy"; NUNCA otra marca), `publicationDate` con timezone America/Asuncion:
   - providers SOLO `[{"network":"youtube"}]`, media `[<url raw>]`, autoPublish true, draft false.
   - `youtubeData`: `{"title": ..., "type": "short", "privacy": "public", "madeForKids": false, "category": "GAMING", "tags": [...]}`.
   - **Título**: gancho con 1-2 palabras en MAYÚSCULAS + 1 emoji, máx. ~70 caracteres.
   - **Descripción** (`text`): 1-2 frases + pregunta para comentar + "Fuente: ..." + "Seguí a Duo Bloxyy para más secretos de Roblox 🧱"
     + 3 a 5 hashtags (siempre `#roblox #shorts` + 1-3 del tema, ej. `#robloxhistoria #misteriosderoblox #sabiasque`).
4. Si Metricool falla (plan/cuota u otro rechazo): NO reintentar en bucle. Modo manual: `SendUserFile` con cada mp4 y
   `SendUserMessage` con título, descripción, hashtags, hora y link raw, más los pasos para programarlo en YouTube Studio
   ("No, no es contenido para niños"). Marcar la hora en `historial.md` como "(manual)".
5. Resumen final a Diego (SendUserMessage): los 4 títulos con su hora y formato (voz IA / texto, música / ASMR / misterio),
   links del planner de Metricool, y suscriptores actuales (`getAnalyticsDataByMetrics`, brandId 8312161, métrica YTEV01).
