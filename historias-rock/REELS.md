# Reels de prueba (Trial Reels) de @diegoeditspy

Mismo estilo y reglas de contenido que las stories (leé INSTRUCCIONES.md: datos verificados,
sin fotos de artistas ni canciones de las bandas, firma @diegoeditspy, sin "Rock en Ascenso").
**2 Reels de prueba por día**, todos los días (America/Asuncion):

| Hora | Formato | Detalle |
|---|---|---|
| 12:30 | **Dato de rock en formato Reel** | 24-32 s, 5-7 escenas: gancho con pregunta → contexto → giro → remate → "¿Lo sabías? Contame abajo". Ejemplo: `reels/datos/2026-11-17_1230.json` (Sepultura). |
| 18:30 | **Top / ranking** | 25-35 s: "3 discos de...", "3 bandas paraguayas de metal que tenés que conocer", "3 canciones que...". Escena de título + una escena por puesto (nombre grande + año/dato verificable) + cierre con pregunta "¿Cuál agregarías?". |

- Rotá región y subgénero (paraguayo, argentino, brasilero, europeo/anglo, metal, heavy, punk, hard rock).
  Que el dato de las 12:30, el top de las 18:30 y la story de las 20:00 del mismo día no repitan banda.
- Nada de opiniones presentadas como hechos ("la mejor banda", "la más grande"): los tops se presentan
  como selección ("3 discos para empezar con...") y cada dato del top tiene que ser verificable (año, disco, ciudad).
- Mismo motor: `motor/story.py datos.json salida.mp4 [preview]`. En Reels poné `"footer_y": 1360`
  (abajo Instagram tapa con la descripción). Mirá la hoja de preview antes del render y cuadros del mp4 después.
- Archivos: `reels/datos/AAAA-MM-DD_HHMM.json` y `reels/publicados/AAAA-MM-DD_HHMM.mp4`
  (el motor limita el bitrate; si un mp4 pasa de 50 MB, recomprimilo antes de commitear: GitHub rechaza >100 MB).
- Metricool: blogId 7851020, providers SOLO instagram, `instagramData: {"type": "TRIAL_REEL",
  "showReelOnFeed": true, "isAiGenerated": false}`, autoPublish true, draft false, media = URL raw del mp4.
  Texto (caption): 2-3 líneas con el dato + pregunta + "Fuente: ..." + 4-5 hashtags (siempre #historiadelrock).
- Antes, getScheduledPosts para no duplicar horarios. Si un horario de hoy ya pasó o está ocupado, no lo dupliques.
- Anotá cada Reel en `reels/historial.md` (fecha, hora, formato, tema, fuente).
