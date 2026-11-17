# Stories de historia del rock: Instagram @diegoeditspy (producción automática)

Cuenta personal de Diego (la que más quiere). Una **story por día a las 20:00** (America/Asuncion)
con un dato de historia del rock que no todos saben: "¿Sabías que...?".
Temas: rock paraguayo, rock argentino, rock brasilero, rock europeo/anglo, metal, heavy metal,
thrash, punk, hard rock, todo el mundo del rock. Rotá región y subgénero (no dos días seguidos
del mismo país ni de la misma banda). Español con voseo.

**Esta carpeta (`historias-rock/`) es la única que se toca** del repo `shorts-canal`
(el resto es de otros canales: no modificar nada fuera de esta carpeta, ni leer/seguir el CLAUDE.md de la raíz).

## Reglas de contenido
- Cada dato verificado en al menos una fuente confiable en la web (prensa musical, Wikipedia con
  referencias, entrevistas, biografías). **Nunca inventes** fechas, nombres, cifras ni anécdotas.
  Si dos fuentes se contradicen, elegí otro dato.
- Nada de rumores ni de muertes recientes tratadas con morbo. Tono de "dato curioso" respetuoso.
- **Sin fotos ni videos de artistas ni tapas de discos** (derechos de autor y política propia): solo
  el diseño tipográfico del motor. **Sin canciones de las bandas**: la música la genera el motor.
- **Música = hard rock con instrumentos REALES grabados** (pedido de Diego 17/11/2026: nada de sonido sintetizado tipo videojuego).
  `motor/rock.py` arma un riff original con guitarra eléctrica y batería acústica grabadas (CC0, en `motor/samples/`,
  ver `LICENCIA.txt`), con distorsión de amplificador. Requiere `pip install soundfile scipy --break-system-packages`.
  No volver al sintetizador viejo.
- Diseño aprobado por Diego (no cambiarlo): fondo negro con grano, títulos Anton que golpean,
  firma **@diegoeditspy** abajo y la fuente debajo. **NO poner "Rock en Ascenso"**.
- Dejá libres arriba (y < 450) y abajo (y > 1700): ahí Instagram pone su interfaz.

**Efectos de sonido obligatorios** en cada story (whoosh en transiciones, impacto en títulos `slam`, tecleo en textos `type`): los pone el motor solo. Cada escena con al menos un `slam` o `type`.

## Cómo armar una story
1. Escribí `datos/AAAA-MM-DD.json` siguiendo `datos/ejemplo_hermetica.json`:
   - 3 a 5 escenas, 14 a 18 s en total. Primera escena: gancho ("¿SABÍAS QUE...?" u otra variante:
     "DATO ROCKERO", "POCOS LO SABEN", "¿TE ACORDÁS?"...). Última: el remate/fecha.
   - Fuentes: `anton` (títulos), `oswb` (datos), `osw`, `type` (máquina de escribir). Colores `bone`, `red`, `dim`.
   - Textos cortos: una palabra/nombre grande por escena (máx. ~11 caracteres en size 170-190;
     frases largas en size 46-62). `y` entre 600 y 1150.
   - `fuente`: "Fuente: <medio>, «<título>» (<año>)". `url_fuente`: el link. Variá `seed`, `bpm` (120-170) y `tono` (38-45).
2. Preview: `python3 historias-rock/motor/story.py datos/X.json /home/claude/prev.jpg preview` y **MIRÁ la hoja**:
   nada cortado, encimado ni fuera del ancho. Corregí y repetí.
3. Render: `python3 historias-rock/motor/story.py datos/X.json historias-rock/publicados/AAAA-MM-DD.mp4`.
   Mirá 2-3 cuadros del mp4 final (ffmpeg -ss).
4. Copiá, agregá al historial, commit y push a main. Confirmá con `curl -sI` que
   `https://raw.githubusercontent.com/diegobritez1993-sketch/shorts-canal/main/historias-rock/publicados/AAAA-MM-DD.mp4`
   responde HTTP/2 200.

## Metricool
- Marca **7851020** (comparte con el YouTube de TikFinity: **providers SOLO instagram**).
- `instagramData: {"type": "STORY"}`, media = URL raw del mp4, autoPublish true, draft false,
  **sin text** (una story sola no lleva texto). networkData solo instagramData.
- Antes, getScheduledPosts (timezone America/Asuncion) para no duplicar la story de ese día.
- Si falla, NO reintentes en bucle: mandale a Diego el mp4 con SendUserFile y con SendUserMessage
  el dato y la fuente, para que la suba él.
