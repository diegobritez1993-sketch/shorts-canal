"""Duo Bloxyy · 2026-11-27 14:00 · Historia · VOZ IA + MÚSICA
Fuente: Wikipedia "David Baszucki": a fines de los 80 David Baszucki y su hermano Greg crearon Interactive Physics
(simulador de física 2D, suplemento educativo muy usado por estudiantes) con su empresa Knowledge Revolution; en diciembre
de 1998 MSC Software compró Knowledge Revolution por 20 millones de dólares; la idea de Roblox se inspiró en el éxito de
Interactive Physics entre estudiantes; en diciembre de 2003 Baszucki y Erik Cassel (su VP de Ingeniería en Interactive
Physics) arrancaron el prototipo (eBlocks → GoBlocks → DynaBlocks → Roblox en enero de 2004)."""
from _base import *
ep = Episode([
    dict(type="hook", kicker="HISTORIA DE ROBLOX", lines=[("ANTES DE ROBLOX", "w"), ("HUBO UN PROGRAMA", "w"), ("DE FÍSICA", "y")],
         sizes=(118, 118, 180), icon="cube", dur=3.6, vo="Antes de Roblox, hubo un programa de física."),
    dict(type="hook", kicker="FINES DE LOS 80", lines=[("INTERACTIVE", "y"), ("PHYSICS", "y"), ("PARA ESTUDIANTES", "w")],
         sizes=(150, 150, 100), icon="star", dur=4.2, source="Wikipedia",
         vo="Se llamaba Interáctiv Físics, y lo usaban estudiantes."),
    dict(type="list", title="LO CREARON", items=["DAVID BASZUCKI", "Y SU HERMANO GREG"],
         icons=["cube", "cube"], step=0.7, dur=4.0, source="Wikipedia",
         vo="Lo crearon David Basúki y su hermano Greg."),
    dict(type="stat", title="EN 1998 VENDIERON LA EMPRESA", value=20, prefix="US$ ", suffix=" M", label="DÓLARES",
         sub="su empresa se llamaba Knowledge Revolution", source="Wikipedia", dur=4.6,
         vo="En el noventa y ocho la vendieron por veinte millones de dólares."),
    dict(type="hook", kicker="DICIEMBRE DE 2003", lines=[("CON SU INGENIERO", "w"), ("ERIK CASSEL", "y"), ("EMPEZÓ ROBLOX", "g")],
         sizes=(110, 150, 130), icon="trophy", dur=4.4, source="Wikipedia",
         vo="Y en dos mil tres, con su ingeniero Erik Cásel, empezó Roblox."),
    dict(type="question", q=["¿SABÍAS QUE", "EMPEZÓ ASÍ?"], options=["SÍ", "NI IDEA"], dur=4.0,
         vo="¿Vos lo sabías? Comentá."),
    dict(type="outro", dur=3.0),
], title="antes-de-roblox", audio="musica")
if __name__ == "__main__": main(ep)
