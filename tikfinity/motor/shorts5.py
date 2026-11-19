import sys
import shorts
from shorts import hook, outro
from long5 import (shot, L_MISMATCH, L_META, L_TEST, O_REQ, O_WS, O_IP, O_TEST,
                   B_WS, B_DATA, B_TEST, N_NAME, N_CASE, N_TEST)

shorts.SHORTS.update({
    "s16_meta_titulo": ("TikFinity · Metas", [
        hook("TIKFINITY", "¿Tu meta dice", "otro número?", "El error que se ve en muchos lives"),
        shot("likes", "EL ERROR", "Título vs. meta", [
            (L_MISMATCH, "El título dice 50000, pero la meta es 15.000.", 4.0),
            (L_META, "El número del título tiene que coincidir con la Meta.", 4.0),
            (L_TEST, "Tocá «Test» y mirá cómo queda antes del live.", 4.0),
        ], 13.5),
        outro(),
    ]),
    "s17_obs_error": ("TikFinity · OBS no conecta", [
        hook("TIKFINITY + OBS", "¿OBS no", "se conecta?", "Revisá estas 3 cosas"),
        shot("obs", "REVISÁ", "OBS + TikFinity", [
            (O_REQ, "Necesitás OBS 28 o superior.", 3.5),
            (O_WS, "Habilitá el Servidor WebSocket en Herramientas de OBS.", 4.0),
            (O_IP, "127.0.0.1 solo si OBS está en la misma PC.", 4.0),
            (O_TEST, "Y después: «Probar Conexión».", 3.5),
        ], 16.5),
        outro(),
    ]),
    "s18_streamerbot": ("TikFinity · Streamer.bot", [
        hook("TIKFINITY + STREAMER.BOT", "¿Streamer.bot", "no responde?", "El paso que muchos se olvidan"),
        shot("sbot", "EL PASO", "Activá el servidor", [
            (B_WS, "En Streamer.bot: Servidor WebSocket activo («Servidores/Clientes»).", 4.5),
            (B_DATA, "En TikFinity: 127.0.0.1, puerto 8080, punto final «/».", 4.5),
            (B_TEST, "Probá la conexión y listo.", 3.5),
        ], 14.0),
        outro(),
    ]),
    "s19_mc_nombre": ("TikFinity · Minecraft", [
        hook("TIKFINITY + MINECRAFT", "¿Los comandos", "van a todos?", "Mirá el nombre del jugador"),
        shot("mc2", "SERVERTAP", "Nombre del jugador", [
            (N_NAME, "Con el plugin ServerTap, escribí tu nombre de jugador.", 4.0),
            (N_CASE, "Vacío = los comandos van a todos (@a).", 4.0),
            (N_CASE, "Respetá mayúsculas y minúsculas.", 3.5),
            (N_TEST, "Validalo con «Probar Conexión».", 3.5),
        ], 16.5),
        outro(),
    ]),
})

if __name__ == "__main__":
    for n in sys.argv[1:]:
        shorts.render(n, list(shorts.SHORTS).index(n) + 1)
