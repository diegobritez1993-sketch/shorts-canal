"""Motor de videos verticales (1080x1920) del canal "Duo Bloxyy" (Roblox: misterios, secretos, historia, datos).
Adaptado del motor de Clash. Estilo "bloques": fondo de cubos y grilla que se mueven, texto grande con borde.

Episode(scenes, title=..., audio="musica" | "asmr" | "misterio")
  musica   : música chiptune original alegre + efectos (default)
  asmr     : SIN música: efectos suaves tipo ASMR (taps, clicks, pops) + colchón de ruido suave
  misterio : pad oscuro original + latido lento + efectos (para leyendas y misterios)
Voz IA: poner vo="..." en las escenas (voz Piper "carlfm"). Sin vo en ninguna escena = video SOLO TEXTO.
mood="dark" en el Episode usa la paleta oscura (misterios).
Íconos extra: "cube", "ghost", "lock", "question", "trophy".


Un episodio es una lista de escenas (dicts). Cada escena dura `dur` segundos y tiene un `type`:
  hook      : lines=[(texto, color_key)], kicker="NOTICIA"         -> gancho grande
  stat      : value=186, prefix="", suffix="%", label="...", sub="...", source="..."  -> número que cuenta
  change    : name="FLECHA CONGELADA", before="40%", after="45%", label="RALENTIZACIÓN", up=True, source=""
  list      : title="...", items=["...", "..."], icon="up"/"down"/"star"/"check"  -> ítems uno por uno
  versus    : title="...", left=("A", "valor"), right=("B", "valor")
  alert     : lines=[...], sub="..."        -> aviso urgente (borde rojo que late + reloj)
  question  : q="¿...?", options=["SÍ", "NO"]   -> pregunta para comentarios
  trivia    : q=["¿CUÁNTOS...", "...?"], options=["A) ...", "B) ...", "C) ..."], answer=1, source=""
              -> opciones, cuenta regresiva 3-2-1 y revela la correcta en verde (usar dur=7)
  outro     : (sin campos)  -> "SEGUÍ @misterd.coc"
  vo="texto"  -> VOZ EN OFF de esa escena (voz masculina gratuita Piper "carlfm", motor/voz/). Frase corta en voseo,
                que se pueda decir en dur-0.5 s (~2,5 palabras por segundo). Si no entra, se acelera un poco (máx. 1,45x).
                El outro dice solo "¡Seguí a Duo Bloxyy para más secretos de Roblox!" si no tiene vo. La música baja cuando habla.
Campos comunes opcionales: color (índice de paleta 0-5), source (texto chico abajo), dur,
  bg="capturas/x.jpg"   -> fondo con una captura del juego (desenfocada, oscurecida, con zoom lento) en vez de rayos
  card="capturas/x.jpg" -> tarjeta con la captura (marco blanco, entra con rebote y hace zoom); card_y = centro vertical
                           (si la imagen es PNG transparente se dibuja como sticker, sin marco)
  sticker="capturas/kit_creador/x.png" -> PNG transparente del kit de creador, sin marco, con sombra + brillo,
                           entra con rebote y flota. sticker_x / sticker_y = centro, sticker_h = alto máx (def. 520),
                           sticker_t = segundo de entrada, sticker_flip=True lo espeja.
Episode(..., bg_pool=[...]) asigna capturas de fondo a las escenas que no tengan `bg` (rotando).
La primera escena muestra arriba la etiqueta "CLASH OF CLANS" (texto) para que se note de qué es el video.

Reglas de estilo: las ÚNICAS imágenes del juego permitidas son las de `capturas/` (capturas propias de Diego y el
kit oficial de creador de Supercell en `capturas/kit_creador/`, ver INDICE.md).
No descargar arte oficial, logos ni personajes de internet, ni dibujarlos. Íconos: solo los simples de este motor.
Uso:  python episodios/X.py preview DIR t1 t2 ...   |   python episodios/X.py build publicados/X.mp4
"""
import math, os, random, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
FB = os.path.join(HERE, "fonts", "Poppins-Bold.ttf")
FI = os.path.join(HERE, "fonts", "Poppins-BoldItalic.ttf")
FM = os.path.join(HERE, "fonts", "Poppins-Medium.ttf")
HANDLE = "DUO BLOXYY"
WHITE = (255, 255, 255); YELLOW = (255, 214, 10); RED = (255, 70, 55); GREEN = (70, 230, 120); GREY = (190, 195, 215)
COL = {"w": WHITE, "y": YELLOW, "r": RED, "g": GREEN}
PALETTE = [((226, 35, 26), (90, 8, 8)), ((0, 162, 255), (5, 35, 95)), ((140, 60, 220), (40, 10, 80)),
           ((0, 190, 90), (4, 55, 25)), ((255, 150, 0), (95, 45, 0)), ((0, 190, 210), (4, 50, 70))]
DARK = [((70, 30, 120), (8, 4, 20)), ((20, 70, 90), (2, 10, 16)), ((110, 20, 40), (12, 2, 6)), ((40, 40, 90), (4, 4, 14))]
MOOD = {"pal": PALETTE}

# ---------------- utilidades ----------------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def ease_in(x): x = clamp(x); return x ** 3
def back(x, s=2.4):
    x = clamp(x) - 1
    return 1 + (s + 1) * x ** 3 + s * x ** 2
_cache = {}
def text_img(text, size, fill=WHITE, stroke=10, font=FB):
    key = (text, size, fill, stroke, font)
    if key in _cache: return _cache[key]
    f = ImageFont.truetype(font, size)
    b = f.getbbox(text, stroke_width=stroke)
    im = Image.new("RGBA", (b[2] - b[0] + 20, b[3] - b[1] + 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(im); ox, oy = 10 - b[0], 10 - b[1]
    if stroke:
        d.text((ox, oy + 9), text, font=f, fill=(0, 0, 0, 255), stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    d.text((ox, oy), text, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
    _cache[key] = im; return im
def fit(text, size, maxw=1000, **kw):
    im = text_img(text, size, **kw)
    while im.width > maxw and size > 34:
        size -= 6; im = text_img(text, size, **kw)
    return im
def pill(text, color, size=48, ink=WHITE):
    key = ("pill", text, color, size, ink)
    if key in _cache: return _cache[key]
    t = text_img(text, size, stroke=6, fill=ink)
    w, h = t.width + 64, t.height + 18
    im = Image.new("RGBA", (w, h + 10), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 10, w, h + 10), radius=h // 2, fill=(0, 0, 0, 160))
    d.rounded_rectangle((0, 0, w, h), radius=h // 2, fill=color + (255,), outline=(0, 0, 0, 255), width=6)
    im.alpha_composite(t, (32, 5)); _cache[key] = im; return im
def paste(canvas, im, cx, cy, scale=1.0, alpha=1.0, rot=0.0):
    if scale <= 0.01 or alpha <= 0.01: return
    if abs(scale - 1) > 1e-3:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BILINEAR)
    if rot: im = im.rotate(rot, Image.BILINEAR, expand=True)
    if alpha < 1:
        im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * alpha)))
    x, y = int(cx - im.width / 2), int(cy - im.height / 2)
    x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + im.width), min(H, y + im.height)
    if x1 > x0 and y1 > y0:
        canvas.alpha_composite(im.crop((x0 - x, y0 - y, x1 - x, y1 - y)), (x0, y0))

# ---------------- íconos simples (originales) ----------------
def icon(kind, size=120, col=YELLOW):
    key = ("icon", kind, size, col)
    if key in _cache: return _cache[key]
    s = size; im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    c = s / 2
    if kind in ("up", "down"):
        base = GREEN if kind == "up" else RED
        d.ellipse((4, 4, s - 4, s - 4), fill=base + (255,), outline=(0, 0, 0, 255), width=6)
        if kind == "up": pts = [(c, s * .2), (s * .78, s * .55), (s * .6, s * .55), (s * .6, s * .8), (s * .4, s * .8), (s * .4, s * .55), (s * .22, s * .55)]
        else: pts = [(c, s * .8), (s * .78, s * .45), (s * .6, s * .45), (s * .6, s * .2), (s * .4, s * .2), (s * .4, s * .45), (s * .22, s * .45)]
        d.polygon(pts, fill=WHITE + (255,), outline=(0, 0, 0, 255))
    elif kind == "star":
        pts = [(c + (s * .46 if k % 2 == 0 else s * .2) * math.cos(-math.pi / 2 + k * math.pi / 5),
                c + (s * .46 if k % 2 == 0 else s * .2) * math.sin(-math.pi / 2 + k * math.pi / 5)) for k in range(10)]
        d.polygon(pts, fill=col + (255,), outline=(0, 0, 0, 255), width=6)
    elif kind == "check":
        d.ellipse((4, 4, s - 4, s - 4), fill=GREEN + (255,), outline=(0, 0, 0, 255), width=6)
        d.line([(s * .27, s * .52), (s * .44, s * .7), (s * .75, s * .32)], fill=WHITE + (255,), width=int(s * .12), joint="curve")
    elif kind == "clock":
        d.ellipse((4, 4, s - 4, s - 4), fill=WHITE + (255,), outline=(0, 0, 0, 255), width=8)
        d.line([(c, c), (c, s * .22)], fill=(0, 0, 0, 255), width=int(s * .08))
        d.line([(c, c), (s * .72, c)], fill=RED + (255,), width=int(s * .07))
        d.ellipse((c - 6, c - 6, c + 6, c + 6), fill=(0, 0, 0, 255))
    elif kind == "alert":
        d.polygon([(c, 6), (s - 6, s - 10), (6, s - 10)], fill=YELLOW + (255,), outline=(0, 0, 0, 255), width=8)
        d.rectangle((c - s * .05, s * .32, c + s * .05, s * .64), fill=(0, 0, 0, 255))
        d.ellipse((c - s * .06, s * .7, c + s * .06, s * .82), fill=(0, 0, 0, 255))
    elif kind == "gift":
        d.rectangle((s * .12, s * .4, s * .88, s * .9), fill=RED + (255,), outline=(0, 0, 0, 255), width=6)
        d.rectangle((s * .06, s * .28, s * .94, s * .42), fill=RED + (255,), outline=(0, 0, 0, 255), width=6)
        d.rectangle((c - s * .07, s * .28, c + s * .07, s * .9), fill=YELLOW + (255,), outline=(0, 0, 0, 255), width=4)
        d.ellipse((s * .26, s * .08, c, s * .3), outline=YELLOW + (255,), width=8); d.ellipse((c, s * .08, s * .74, s * .3), outline=YELLOW + (255,), width=8)
    elif kind == "chat":
        d.rounded_rectangle((6, 10, s - 6, s * .72), radius=24, fill=WHITE + (255,), outline=(0, 0, 0, 255), width=6)
        d.polygon([(s * .25, s * .7), (s * .45, s * .7), (s * .2, s * .92)], fill=WHITE + (255,), outline=(0, 0, 0, 255))
        for k in range(3): d.ellipse((s * (.27 + k * .2) - 9, s * .41 - 9, s * (.27 + k * .2) + 9, s * .41 + 9), fill=(0, 0, 0, 255))
    elif kind == "cube":
        top = [(c, s * .08), (s * .92, s * .3), (c, s * .52), (s * .08, s * .3)]
        lf = [(s * .08, s * .3), (c, s * .52), (c, s * .94), (s * .08, s * .72)]
        rt = [(c, s * .52), (s * .92, s * .3), (s * .92, s * .72), (c, s * .94)]
        base = col
        d.polygon(top, fill=tuple(min(255, int(v * 1.0)) for v in base) + (255,), outline=(0, 0, 0, 255), width=6)
        d.polygon(lf, fill=tuple(int(v * .72) for v in base) + (255,), outline=(0, 0, 0, 255), width=6)
        d.polygon(rt, fill=tuple(int(v * .5) for v in base) + (255,), outline=(0, 0, 0, 255), width=6)
    elif kind == "ghost":
        d.pieslice((s * .14, s * .06, s * .86, s * .78), 180, 360, fill=WHITE + (255,), outline=(0, 0, 0, 255), width=6)
        d.rectangle((s * .14, s * .42, s * .86, s * .8), fill=WHITE + (255,))
        d.line([(s * .14, s * .42), (s * .14, s * .86)], fill=(0, 0, 0, 255), width=6); d.line([(s * .86, s * .42), (s * .86, s * .86)], fill=(0, 0, 0, 255), width=6)
        for k in range(3):
            x0 = s * (.14 + k * .24); d.polygon([(x0, s * .8), (x0 + s * .12, s * .94), (x0 + s * .24, s * .8)], fill=WHITE + (255,))
        d.ellipse((s * .32, s * .3, s * .44, s * .46), fill=(0, 0, 0, 255)); d.ellipse((s * .56, s * .3, s * .68, s * .46), fill=(0, 0, 0, 255))
        d.ellipse((s * .44, s * .52, s * .56, s * .66), fill=(0, 0, 0, 255))
    elif kind == "lock":
        d.arc((s * .26, s * .06, s * .74, s * .6), 180, 360, fill=(0, 0, 0, 255), width=int(s * .14))
        d.arc((s * .29, s * .09, s * .71, s * .57), 180, 360, fill=GREY + (255,), width=int(s * .08))
        d.rounded_rectangle((s * .14, s * .38, s * .86, s * .94), radius=int(s * .08), fill=col + (255,), outline=(0, 0, 0, 255), width=6)
        d.ellipse((c - s * .07, s * .54, c + s * .07, s * .68), fill=(0, 0, 0, 255)); d.rectangle((c - s * .03, s * .62, c + s * .03, s * .8), fill=(0, 0, 0, 255))
    elif kind == "question":
        d.ellipse((4, 4, s - 4, s - 4), fill=(140, 60, 220, 255), outline=(0, 0, 0, 255), width=6)
        f = ImageFont.truetype(FB, int(s * .7)); bb = d.textbbox((0, 0), "?", font=f)
        d.text((c - (bb[0] + bb[2]) / 2, c - (bb[1] + bb[3]) / 2), "?", font=f, fill=WHITE + (255,), stroke_width=6, stroke_fill=(0, 0, 0, 255))
    elif kind == "trophy":
        d.polygon([(s * .22, s * .1), (s * .78, s * .1), (s * .7, s * .5), (s * .3, s * .5)], fill=col + (255,), outline=(0, 0, 0, 255), width=6)
        d.arc((s * .04, s * .12, s * .34, s * .42), 90, 270, fill=col + (255,), width=int(s * .06)); d.arc((s * .66, s * .12, s * .96, s * .42), 270, 90, fill=col + (255,), width=int(s * .06))
        d.rectangle((s * .44, s * .5, s * .56, s * .74), fill=col + (255,), outline=(0, 0, 0, 255), width=4)
        d.rounded_rectangle((s * .24, s * .74, s * .76, s * .92), radius=10, fill=col + (255,), outline=(0, 0, 0, 255), width=6)
    _cache[key] = im; return im

# ---------------- fondo ----------------
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
CX, CY = W / 2, 900
ANG = np.arctan2(yy - CY, xx - CX)
RAD = np.clip(1 - np.sqrt((xx - CX) ** 2 + (yy - CY) ** 2) / 1500, 0, 1)[..., None]
VIGN = np.clip(1.15 - np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2) * 1.3, 0.35, 1)[..., None]
EDGE = np.clip((np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) - 0.55) / 0.6, 0, 1)[..., None]
_rng = random.Random(7)
PARTS = [(_rng.uniform(0, W), _rng.uniform(0, H), _rng.uniform(40, 140), _rng.uniform(3, 9), _rng.uniform(0, 6.28)) for _ in range(45)]
_rb = random.Random(11)
CUBES = [(_rb.uniform(0, W), _rb.uniform(0, H), _rb.uniform(26, 70), _rb.uniform(25, 90), _rb.uniform(0, 6.28)) for _ in range(26)]
def _cube(d, cx, cy, r, col, a):
    top = [(cx, cy - r), (cx + r * .87, cy - r * .5), (cx, cy), (cx - r * .87, cy - r * .5)]
    lf = [(cx - r * .87, cy - r * .5), (cx, cy), (cx, cy + r), (cx - r * .87, cy + r * .5)]
    rt = [(cx, cy), (cx + r * .87, cy - r * .5), (cx + r * .87, cy + r * .5), (cx, cy + r)]
    d.polygon(top, fill=tuple(min(255, int(v * 1.25 + 30)) for v in col) + (a,))
    d.polygon(lf, fill=tuple(int(v * .8) for v in col) + (a,))
    d.polygon(rt, fill=tuple(int(v * .55) for v in col) + (a,))
def background(ci, t):
    pal = MOOD["pal"]
    c1, c2 = (np.array(c, np.float32) for c in pal[ci % len(pal)])
    base = c2 + (c1 - c2) * RAD
    gx = ((xx + t * 45) % 135 < 7) | ((yy + t * 45) % 135 < 7)          # grilla de bloques que se desliza
    img = Image.fromarray(np.clip((base + gx[..., None] * RAD * 34) * VIGN, 0, 255).astype(np.uint8)).convert("RGBA")
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    cc = tuple(int(v) for v in c1)
    for x, y, r, sp, ph in CUBES:
        py = (y - t * sp) % (H + 200) - 100; px = x + math.sin(t * 0.8 + ph) * 25
        _cube(d, px, py, r, cc, 90)
    img.alpha_composite(lay)
    return img

# ---------------- capturas de Diego ----------------
ROOT = os.path.dirname(HERE)
_imgs = {}
def load_rgba(path):
    if path not in _imgs:
        full = path if os.path.isabs(path) else os.path.join(ROOT, path)
        _imgs[path] = Image.open(full).convert("RGBA")
    return _imgs[path]
def has_alpha(path):
    return load_rgba(path).getchannel("A").getextrema()[0] < 250
def load_cap(path, under=(18, 18, 30)):
    """RGB; si es transparente se apoya sobre un color liso (para fondos)."""
    im = load_rgba(path)
    if not has_alpha(path): return im.convert("RGB")
    base = Image.new("RGBA", im.size, under + (255,)); base.alpha_composite(im)
    return base.convert("RGB")
_bgs = {}
def cap_background(path, ci, t, lt):
    key = (path, ci)
    if key not in _bgs:
        im = load_cap(path, tuple(int(v * 0.5) for v in PALETTE[ci % len(PALETTE)][1]))
        sc = max(W / im.width, H / im.height) * 1.15
        im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        im = im.crop(((im.width - int(W * 1.15)) // 2, (im.height - int(H * 1.15)) // 2,
                      (im.width - int(W * 1.15)) // 2 + int(W * 1.15), (im.height - int(H * 1.15)) // 2 + int(H * 1.15)))
        im = im.filter(ImageFilter.GaussianBlur(6))
        arr = np.asarray(im).astype(np.float32)
        tint = np.array(PALETTE[ci % len(PALETTE)][1], np.float32)
        arr = arr * 0.42 + tint * 0.30
        _bgs[key] = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
    big = _bgs[key]; z = 1.0 + 0.04 * min(lt, 5) / 5
    cw, ch = int(big.width / 1.15 / z), int(big.height / 1.15 / z)
    x0 = (big.width - cw) // 2 + int(30 * math.sin(t * 0.3)); y0 = (big.height - ch) // 2
    img = big.crop((x0, y0, x0 + cw, y0 + ch)).resize((W, H), Image.BILINEAR)
    arr = np.asarray(img).astype(np.float32)
    rays = (np.sin(ANG * 12 + t * 0.9) > 0.15).astype(np.float32)[..., None]
    arr = (arr + rays * RAD * 22) * VIGN
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
    d = ImageDraw.Draw(img)
    for x, y, sp, r, ph in PARTS[:25]:
        py = (y - t * sp) % H; px = x + math.sin(t * 1.5 + ph) * 20
        d.ellipse((px - r, py - r, px + r, py + r), fill=(255, 240, 180, 150))
    return img
_stk = {}
def cap_sticker(path, maxh=520, maxw=900, flip=False):
    """PNG transparente con sombra y halo claro, listo para pegar."""
    key = (path, maxh, maxw, flip)
    if key not in _stk:
        im = load_rgba(path)
        sc = min(maxh / im.height, maxw / im.width)
        im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.LANCZOS)
        if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
        pad = 40
        out = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
        a = im.getchannel("A")
        glow = Image.new("RGBA", out.size, (255, 230, 150, 0)); ga = Image.new("L", out.size, 0)
        ga.paste(a, (pad, pad)); ga = ga.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.55))
        glow.putalpha(ga); out.alpha_composite(glow)
        sh = Image.new("RGBA", out.size, (0, 0, 0, 0)); sa = Image.new("L", out.size, 0)
        sa.paste(a, (pad + 10, pad + 18)); sa = sa.filter(ImageFilter.GaussianBlur(10)).point(lambda v: int(v * 0.6))
        sh.putalpha(sa); out.alpha_composite(sh)
        out.alpha_composite(im, (pad, pad)); _stk[key] = out
    return _stk[key]
_cards = {}
def cap_card(path, width=900):
    if has_alpha(path): return cap_sticker(path, 620, width)
    key = (path, width)
    if key not in _cards:
        im = load_cap(path)
        h = int(im.height * width / im.width)
        if h > 700: width = int(width * 700 / h); h = 700
        im = im.resize((width, h), Image.LANCZOS).convert("RGBA")
        fr = Image.new("RGBA", (width + 24, h + 24), (0, 0, 0, 255))
        ImageDraw.Draw(fr).rounded_rectangle((5, 5, width + 18, h + 18), radius=12, fill=(255, 255, 255, 255))
        fr.alpha_composite(im, (12, 12)); _cards[key] = fr
    return _cards[key]
CLASH_TAG = None
def clash_tag():
    global CLASH_TAG
    if CLASH_TAG is None: CLASH_TAG = pill("DUO BLOXYY · ROBLOX", (226, 35, 26), 46, WHITE)
    return CLASH_TAG

# ---------------- escenas ----------------
def lines_stack(canvas, lines, lt, y0, sizes=(118, 150), gap=-14, delay=0.14, start=0.15, out=1.0, wob=True):
    y = y0
    for i, (txt, ck) in enumerate(lines):
        size = sizes[min(i, len(sizes) - 1)] if isinstance(sizes, (list, tuple)) else sizes
        im = fit(txt, size, fill=COL.get(ck, WHITE))
        p = back((lt - start - delay * i) / 0.3, 2.8) * out
        paste(canvas, im, W / 2, y + im.height / 2, p, rot=(2 * math.sin(lt * 4 + i) if lt > 1 and wob else 0))
        y += im.height + gap
    return y

def draw_scene(canvas, sc, lt, idx):
    typ = sc["type"]; dur = sc["dur"]
    out = 1 - ease_in((lt - dur + 0.22) / 0.22) if typ != "outro" else 1
    if sc.get("kicker"):
        paste(canvas, pill(sc["kicker"], MOOD["pal"][sc["color"] % len(MOOD["pal"])][0], 52), W / 2 - (1 - ease_out((lt - 0.05) / 0.3)) * 1100, 300, 1, out)
    if typ == "hook":
        lines_stack(canvas, sc["lines"], lt, 560, sizes=sc.get("sizes", (110, 130, 170)), out=out)
        if sc.get("icon"): paste(canvas, icon(sc["icon"], 220), W / 2, 1420, back((lt - 0.7) / 0.35) * out * (1 + 0.05 * math.sin(lt * 6)))
    elif typ == "stat":
        if sc.get("title"): lines_stack(canvas, [(sc["title"], "w")], lt, 420, sizes=(84,), out=out)
        v = sc["value"]; k = ease_out((lt - 0.4) / 1.4)
        num = f'{sc.get("prefix","")}{(v * k):,.0f}{sc.get("suffix","")}'.replace(",", ".")
        im = fit(num, 300, fill=YELLOW, stroke=14)
        punch = 1 + 0.12 * math.exp(-max(0, lt - 1.8) * 8) * (lt > 1.8)
        paste(canvas, im, W / 2, 900, back((lt - 0.3) / 0.3) * out * punch)
        if sc.get("label"): lines_stack(canvas, [(sc["label"], "w")], lt, 1110, sizes=(96,), start=1.6, out=out)
        if sc.get("sub"): paste(canvas, fit(sc["sub"], 50, stroke=6, font=FM, fill=GREY), W / 2, 1300, ease_out((lt - 2.0) / 0.3) * out)
    elif typ == "change":
        lines_stack(canvas, [(sc["name"], "y")], lt, 380, sizes=(104,), out=out)
        if sc.get("label"): paste(canvas, pill(sc["label"], (20, 20, 40), 46), W / 2, 600, back((lt - 0.3) / 0.3) * out)
        bef = fit(sc["before"], 170, fill=GREY); aft = fit(sc["after"], 200, fill=GREEN if sc.get("up", True) else RED, stroke=12)
        paste(canvas, bef, W / 2, 830, back((lt - 0.5) / 0.3) * out)
        ar = icon("up" if sc.get("up", True) else "down", 150)
        paste(canvas, ar.rotate(180 if sc.get("up", True) else 0) if False else ar, W / 2, 1040, back((lt - 1.0) / 0.3) * out)
        punch = 1 + 0.15 * math.exp(-max(0, lt - 1.4) * 8) * (lt > 1.4)
        paste(canvas, aft, W / 2, 1270, back((lt - 1.4) / 0.3) * out * punch)
        if sc.get("note"): paste(canvas, fit(sc["note"], 54, stroke=7), W / 2, 1470, ease_out((lt - 2.0) / 0.3) * out)
    elif typ == "list":
        lines_stack(canvas, [(sc["title"], "y")], lt, 360, sizes=(96,), out=out)
        n = len(sc["items"]); gap = min(230, 900 / max(1, n)); y0 = 640
        for i, it in enumerate(sc["items"]):
            t0 = 0.5 + i * sc.get("step", 0.55); p = back((lt - t0) / 0.3) * out
            y = y0 + i * gap
            ic = sc.get("icons", [sc.get("icon", "check")] * n)[i]
            paste(canvas, icon(ic, 120), 140 - (1 - ease_out((lt - t0) / 0.3)) * 400, y, out)
            tim = fit(it, 72, maxw=800)
            paste(canvas, tim, 230 + tim.width / 2 - (1 - ease_out((lt - t0) / 0.3)) * 1200, y, out)
    elif typ == "versus":
        lines_stack(canvas, [(sc["title"], "y")], lt, 360, sizes=(96,), out=out)
        for side, (nm, val), x, t0, c in ((0, sc["left"], 290, 0.4, RED), (1, sc["right"], 790, 0.9, GREEN)):
            e = ease_out((lt - t0) / 0.35)
            card = Image.new("RGBA", (440, 560), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
            cd.rounded_rectangle((0, 0, 439, 559), radius=40, fill=(10, 14, 40, 210), outline=c + (255,), width=8)
            nim = fit(nm, 60, maxw=400); card.alpha_composite(nim, ((440 - nim.width) // 2, 40))
            vim = fit(val, 120, maxw=400, fill=c); card.alpha_composite(vim, ((440 - vim.width) // 2, 280 - vim.height // 2 + 40))
            paste(canvas, card, x + (1 - e) * (-700 if side == 0 else 700), 980, out, rot=-3 if side == 0 else 3)
        paste(canvas, text_img("VS", 150, fill=YELLOW, stroke=12), W / 2, 980, back((lt - 1.3) / 0.3, 3) * out * (1 + 0.06 * math.sin(lt * 8)))
    elif typ == "alert":
        y = lines_stack(canvas, sc["lines"], lt, 520, sizes=sc.get("sizes", (100, 140)), out=out)
        paste(canvas, icon("clock", 240), W / 2, y + 170, back((lt - 0.6) / 0.35) * out, rot=8 * math.sin(lt * 10))
        if sc.get("sub"): paste(canvas, pill(sc["sub"], RED, 50), W / 2, y + 380, back((lt - 1.1) / 0.3) * out * (1 + 0.04 * math.sin(lt * 7)))
    elif typ == "question":
        paste(canvas, icon("chat", 200), W / 2, 420, back((lt - 0.05) / 0.35) * out)
        lines_stack(canvas, [(l, "w" if i == 0 else "y") for i, l in enumerate(sc["q"])], lt, 600, sizes=(104, 120), out=out)
        for i, o in enumerate(sc.get("options", [])):
            c = [GREEN, RED, (30, 120, 230), (240, 130, 20)][i % 4]
            paste(canvas, pill(o, c, 64), W / 2, 1180 + i * 150, back((lt - 1.0 - 0.2 * i) / 0.3) * out)
        paste(canvas, fit("¡DEJALO EN LOS COMENTARIOS!", 58, stroke=7), W / 2, 1180 + len(sc.get("options", [])) * 150 + 40, ease_out((lt - 1.6) / 0.3) * out)
    elif typ == "trivia":
        paste(canvas, pill("TRIVIA", (230, 160, 0), 56, (20, 20, 30)), W / 2, 320, back((lt - 0.05) / 0.3) * out)
        lines_stack(canvas, [(l, "w" if i == 0 else "y") for i, l in enumerate(sc["q"])], lt, 440, sizes=(92, 104), out=out)
        reveal = sc["dur"] - 2.2
        for i, o in enumerate(sc["options"]):
            ok = i == sc["answer"]
            if lt < reveal: col, a = (40, 50, 110), 1.0
            else: col, a = (GREEN if ok else (90, 90, 110)), (1.0 if ok else 0.55)
            pz = 1 + (0.12 * math.exp(-(lt - reveal) * 6) if (ok and lt >= reveal) else 0)
            paste(canvas, pill(o, col, 60), W / 2, 980 + i * 165, back((lt - 0.9 - 0.25 * i) / 0.3) * out * pz, alpha=a)
            if ok and lt >= reveal:
                paste(canvas, icon("check", 110), W / 2 + pill(o, col, 60).width / 2 + 40, 980 + i * 165, back((lt - reveal) / 0.3) * out)
        cd_start = reveal - 2.4
        if cd_start <= lt < reveal:
            n = 3 - int((lt - cd_start) / 0.8)
            k = ((lt - cd_start) % 0.8) / 0.8
            paste(canvas, text_img(str(max(1, n)), 220, fill=YELLOW, stroke=12), W / 2, 1480, back(k / 0.35) * (1 - ease_in((k - 0.75) / 0.25)))
        elif lt >= reveal:
            paste(canvas, fit("¿ACERTASTE? ¡COMENTÁ!", 70, stroke=8), W / 2, 1470, back((lt - reveal - 0.3) / 0.3) * out)
    elif typ == "outro":
        lines_stack(canvas, [("SEGUÍ PARA MÁS", "w"), ("SECRETOS DE ROBLOX", "y")], lt, 640, sizes=(100, 96))
        paste(canvas, pill(HANDLE, (20, 20, 40), 80, YELLOW), W / 2, 1060, back((lt - 0.5) / 0.35) * (1 + 0.05 * math.sin(lt * 6)))
        paste(canvas, icon("cube", 190), W / 2, 1320, back((lt - 0.8) / 0.35), rot=10 * math.sin(lt * 3))
    if sc.get("card"):
        cd = cap_card(sc["card"])
        e = back((lt - sc.get("card_t", 0.5)) / 0.35, 1.8)
        z = 1 + 0.05 * clamp(lt / max(dur, 0.1))
        paste(canvas, cd, W / 2, sc.get("card_y", 1300), e * out * z, rot=2 * math.sin(lt * 1.6))
    if sc.get("sticker"):
        st = cap_sticker(sc["sticker"], sc.get("sticker_h", 520), 900, sc.get("sticker_flip", False))
        e = back((lt - sc.get("sticker_t", 0.35)) / 0.35, 2.0)
        bob = 14 * math.sin(lt * 2.4)
        paste(canvas, st, sc.get("sticker_x", W / 2), sc.get("sticker_y", 1300) + bob, e * out, rot=3 * math.sin(lt * 1.3))
    if idx == 0:
        paste(canvas, clash_tag(), W / 2, 200, back((lt - 0.05) / 0.3) * out)
    if sc.get("source"):
        paste(canvas, fit("Fuente: " + sc["source"], 34, stroke=5, font=FM, fill=GREY), W / 2, 1585, ease_out((lt - 0.8) / 0.3) * out)

# ---------------- voz en off (Piper, voz masculina gratuita "carlfm") ----------------
VOICE = os.path.join(HERE, "voz", "es-carlfm-x-low.onnx")
def _ensure_piper():
    try:
        import piper  # noqa
        return True
    except Exception:
        r = subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--break-system-packages", "piper-tts"],
                           capture_output=True)
        try:
            import piper  # noqa
            return True
        except Exception:
            print("AVISO: no se pudo instalar piper-tts; video sin voz en off", file=sys.stderr); return False
def tts(text, room, SR=44100, base_speed=1.08):
    """Devuelve la voz como array float32 (mono, SR), acelerada si hace falta para entrar en `room` segundos."""
    if not os.path.exists(VOICE) or not _ensure_piper(): return None
    import tempfile
    d = tempfile.mkdtemp(); raw = os.path.join(d, "raw.wav"); out = os.path.join(d, "out.wav")
    r = subprocess.run([sys.executable, "-m", "piper", "-m", VOICE, "-f", raw], input=text.encode(), capture_output=True)
    if r.returncode or not os.path.exists(raw):
        print("AVISO piper:", r.stderr.decode()[-300:], file=sys.stderr); return None
    with wave.open(raw) as wf: dur0 = wf.getnframes() / wf.getframerate()
    speed = min(1.45, max(base_speed, dur0 / max(room, 0.5)))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af",
                    f"atempo={speed:.3f},highpass=f=90,equalizer=f=3000:t=q:w=1.2:g=3,acompressor=threshold=-20dB:ratio=3,"
                    f"aresample={SR}", "-ac", "1", out], check=True)
    with wave.open(out) as wf: v = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32) / 32768
    lim = int(room * SR)
    if len(v) > lim: v = v[:lim]; v[-int(0.08 * SR):] *= np.linspace(1, 0, int(0.08 * SR))
    return v / (np.abs(v).max() + 1e-9) * 0.9

# ---------------- música de fondo original (chiptune gaming) ----------------
MUSIC_FROM = "2026-11-01"   # la música se activa automáticamente desde esta fecha (hora de Paraguay)
def music_enabled():
    import datetime
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).date().isoformat()
    return now >= MUSIC_FROM

def make_music(total, seed, SR=44100):
    """Loop alegre tipo chiptune/gaming generado acá (sin samples ni temas de terceros)."""
    rng = random.Random(seed)
    bpm = rng.choice([124, 126, 128, 130]); beat = 60 / bpm; n = int(SR * (total + 0.5))
    out = np.zeros(n, np.float32)
    root = rng.choice([57, 58, 60, 62, 63, 65])            # tonalidad (MIDI)
    progs = [[0, 7, 9, 5], [0, 5, 9, 7], [9, 5, 0, 7], [0, 9, 5, 7]]
    prog = rng.choice(progs)
    def hz(m): return 440.0 * 2 ** ((m - 69) / 12)
    def env(m, a=0.005, r=0.08):
        t = np.arange(m) / SR; return np.minimum(1, t / a) * np.exp(-t / r)
    def sq(f, m, duty=0.5):
        t = np.arange(m) / SR; return np.where((t * f) % 1 < duty, 1.0, -1.0)
    def put(sig, at, g):
        i = int(at * SR)
        if i >= n: return
        k = min(len(sig), n - i); out[i:i + k] += (sig[:k] * g).astype(np.float32)
    nr = np.random.default_rng(seed)
    bars = int(total / (beat * 4)) + 2
    arp_pat = rng.choice([[0, 4, 7, 12, 7, 4, 0, 4], [0, 7, 12, 7, 4, 7, 12, 16], [0, 4, 7, 4, 12, 7, 4, 7]])
    for b in range(bars):
        ch = root + prog[b % 4]
        minor = prog[b % 4] == 9
        third = 3 if minor else 4
        for k in range(16):                                 # semicorcheas
            t0 = (b * 16 + k) * beat / 4
            if t0 > total: break
            if k % 4 == 0:                                  # bombo
                m = int(SR * 0.18); tt = np.arange(m) / SR
                put(np.sin(2 * np.pi * np.cumsum(50 + 110 * np.exp(-tt * 35)) / SR) * np.exp(-tt * 18), t0, 0.9)
            if k % 8 == 4:                                  # clap
                m = int(SR * 0.12); put(nr.standard_normal(m) * env(m, 0.002, 0.04), t0, 0.35)
            if k % 2 == 1:                                  # hi-hat
                m = int(SR * 0.04); put(np.diff(nr.standard_normal(m + 1)) * env(m, 0.001, 0.012), t0, 0.12)
            if k % 2 == 0:                                  # bajo
                m = int(SR * beat / 2 * 0.9); f = hz(ch - 24 + (12 if k % 4 == 2 else 0))
                t = np.arange(m) / SR; tri = 2 * np.abs(2 * ((t * f) % 1) - 1) - 1
                put(tri * env(m, 0.004, 0.18), t0, 0.32)
            iv = arp_pat[k % 8]; iv = third if iv == 4 else (third + 12 if iv == 16 else iv)
            m = int(SR * beat / 4 * 0.95)                   # arpegio (cuadrada)
            put(sq(hz(ch + 12 + iv), m, 0.25) * env(m, 0.003, 0.07), t0, 0.07)
        if b % 2 == 1:                                      # melodía simple cada 2 compases
            for j, iv in enumerate(rng.sample([0, 2, 4, 7, 9, 12], 4)):
                t0 = (b * 16 + j * 4) * beat / 4; m = int(SR * beat * 0.9)
                put(sq(hz(ch + 24 + (third if iv == 4 else iv)), m, 0.5) * env(m, 0.01, 0.25), t0, 0.05)
    # "ducking" bajo los bombos + fades
    t = np.arange(n) / SR; ph = (t % beat) / beat
    out *= (0.65 + 0.35 * np.minimum(1, ph / 0.35))
    out *= np.minimum(1, t / 0.6) * np.minimum(1, np.maximum(0, total - t) / 1.2)
    return out / (np.abs(out).max() + 1e-9)

def make_dark(total, seed, SR=44100):
    """Pad oscuro original para misterios: acordes graves + latido lento + campanita lejana (sin samples)."""
    rng = random.Random(seed); n = int(SR * (total + 0.5)); t = np.arange(n) / SR
    root = rng.choice([45, 46, 47, 48]); hz = lambda m: 440.0 * 2 ** ((m - 69) / 12)
    out = np.zeros(n, np.float32)
    for iv, g in ((0, .5), (3, .32), (7, .32), (12, .18), (15, .1)):
        f = hz(root + iv); lfo = 0.6 + 0.4 * np.sin(2 * np.pi * (0.07 + 0.03 * iv / 15) * t + iv)
        out += (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2.003 * t)) * g * lfo
    beat = rng.choice([1.0, 1.1, 1.2]); nb = int(total / beat) + 1
    for k in range(nb):
        for off, gg in ((0, 1.0), (0.22, 0.7)):
            i = int((k * beat + off) * SR); m = int(SR * 0.25); tt = np.arange(m) / SR
            sig = np.sin(2 * np.pi * np.cumsum(40 + 50 * np.exp(-tt * 30)) / SR) * np.exp(-tt * 14) * 1.6 * gg
            if i < n: out[i:i + min(m, n - i)] += sig[:min(m, n - i)]
    for k in range(int(total / 3.2)):
        i = int((1.5 + k * 3.2) * SR); m = int(SR * 1.6); tt = np.arange(m) / SR
        f = hz(root + 36 + rng.choice([0, 3, 7, 10]))
        sig = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * f * 2.76 * tt)) * np.exp(-tt * 2.5) * 0.25
        if i < n: out[i:i + min(m, n - i)] += sig[:min(m, n - i)]
    out *= np.minimum(1, t / 1.0) * np.minimum(1, np.maximum(0, total - t) / 1.2)
    return out / (np.abs(out).max() + 1e-9)

# ---------------- render ----------------
class Episode:
    def __init__(self, scenes, title="", bg_pool=None, music=None, voice=None, audio="musica", mood=None):
        self.scenes = []; t = 0.0; k = 0
        for i, sc in enumerate(scenes):
            sc = dict(sc); sc.setdefault("dur", 4.0); sc.setdefault("color", i)
            if bg_pool and "bg" not in sc and sc["type"] != "outro":
                sc["bg"] = bg_pool[k % len(bg_pool)]; k += 1
            sc["t0"] = t; t += sc["dur"]; self.scenes.append(sc)
        self.total = t; self.title = title
        self.mode = audio
        self.music = (audio != "asmr") if music is None else music
        if mood == "dark" or audio == "misterio": MOOD["pal"] = DARK
        else: MOOD["pal"] = PALETTE
        self.voice = any(sc.get("vo") for sc in self.scenes) if voice is None else voice
    def scene_at(self, t):
        for i, sc in enumerate(self.scenes):
            if t < sc["t0"] + sc["dur"] or i == len(self.scenes) - 1: return i, sc
    def frame(self, t):
        i, sc = self.scene_at(t); lt = t - sc["t0"]
        canvas = cap_background(sc["bg"], sc["color"], t, lt) if sc.get("bg") else background(sc["color"], t)
        # zoom-in de escena (cámara) + temblor al entrar
        draw_scene(canvas, sc, lt, i)
        if sc["type"] == "alert":
            k = 0.7 * abs(math.sin(lt * math.pi * 2.0))
            arr = np.asarray(canvas.convert("RGB")).astype(np.float32)
            arr = arr * (1 - k * EDGE) + np.array([230, 20, 20], np.float32) * k * EDGE
            canvas = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert("RGBA")
        z = 1 + 0.05 * math.exp(-lt * 6) + 0.01 * lt
        a = 18 * math.exp(-lt * 10)
        if z > 1.002 or a > 0.5:
            cw, ch = W / z, H / z
            x0 = (W - cw) / 2 + a * math.sin(t * 97) / z; y0 = (H - ch) / 2 + a * math.cos(t * 71) / z
            canvas = canvas.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.BILINEAR)
        d = ImageDraw.Draw(canvas)                      # barra de progreso
        d.rounded_rectangle((60, 110, W - 60, 124), radius=7, fill=(0, 0, 0, 110))
        d.rounded_rectangle((60, 110, 60 + max(14, (W - 120) * t / self.total), 124), radius=7, fill=(255, 255, 255, 235))
        rgb = canvas.convert("RGB")
        fl = 0.8 * (1 - lt / 0.15) if lt < 0.15 else 0
        if fl > 0: rgb = Image.blend(rgb, Image.new("RGB", rgb.size, WHITE), fl)
        return rgb

    # ---------- sonido ----------
    def audio(self, path):
        SR = 44100; n = int(SR * (self.total + 0.5)); aud = np.zeros(n, np.float32); nr = np.random.default_rng(1)
        def add(sig, at, g=1.0):
            i = int(at * SR)
            if i < 0: sig = sig[-i:]; i = 0
            m = min(len(sig), n - i)
            if m > 0: aud[i:i + m] += sig[:m] * g
        def whoosh(dur=0.4):
            m = int(SR * dur); tt = np.linspace(0, 1, m); x = nr.standard_normal(m)
            al = 1 - np.exp(-2 * np.pi * np.linspace(300, 5000, m) / SR); y = np.zeros(m); prev = 0.0
            for k in range(m): prev += al[k] * (x[k] - prev); y[k] = prev
            y *= np.sin(np.pi * tt) ** 2; return (y / (np.abs(y).max() + 1e-9)).astype(np.float32)
        def impact(dur=0.6, f0=140, f1=38):
            m = int(SR * dur); tt = np.arange(m) / SR
            ph = 2 * np.pi * np.cumsum(f1 + (f0 - f1) * np.exp(-tt * 9)) / SR
            return np.tanh((np.sin(ph) * np.exp(-tt * 5) + nr.standard_normal(m) * np.exp(-tt * 60) * 0.6) * 2.2).astype(np.float32)
        def pop(f=700):
            m = int(SR * 0.12); tt = np.arange(m) / SR
            ph = 2 * np.pi * np.cumsum(f * (1 + 1.2 * (1 - np.exp(-tt * 40)))) / SR
            return (np.sin(ph) * np.exp(-tt * 35)).astype(np.float32)
        def tick():
            m = int(SR * 0.03); tt = np.arange(m) / SR
            return (np.sin(2 * np.pi * 2400 * tt) * np.exp(-tt * 200)).astype(np.float32)
        def ding():
            m = int(SR * 0.6); tt = np.arange(m) / SR
            return ((np.sin(2 * np.pi * 1568 * tt) + 0.4 * np.sin(2 * np.pi * 3136 * tt)) * np.exp(-tt * 8)).astype(np.float32)
        def siren(dur):
            m = int(SR * dur); tt = np.arange(m) / SR
            ph = 2 * np.pi * np.cumsum(np.where(np.sin(2 * np.pi * 1.1 * tt) > 0, 880, 660)) / SR
            return (np.sin(ph) * np.minimum(1, tt / 0.1) * np.minimum(1, (dur - tt) / 0.3)).astype(np.float32)
        for i, sc in enumerate(self.scenes):
            t0 = sc["t0"]; typ = sc["type"]
            if i > 0: add(whoosh(0.4), t0 - 0.3, 0.55)
            add(impact(0.5), t0, 0.7)
            if sc.get("kicker"): add(pop(900), t0 + 0.1, 0.4)
            if typ in ("hook", "alert"):
                for k in range(len(sc["lines"])): add(pop(600 + 150 * k), t0 + 0.15 + 0.14 * k, 0.5)
            if typ == "hook" and sc.get("icon"): add(impact(0.4, 250, 80), t0 + 0.7, 0.5)
            if typ == "stat":
                for k in range(14): add(tick(), t0 + 0.4 + k * 0.1, 0.35)
                add(impact(0.8), t0 + 1.8, 0.9); add(pop(800), t0 + 1.6, 0.5)
            if typ == "change":
                add(pop(600), t0 + 0.5, 0.5); add(whoosh(0.3), t0 + 0.9, 0.4); add(impact(0.8), t0 + 1.4, 0.9); add(ding(), t0 + 1.45, 0.35)
            if typ == "list":
                for k in range(len(sc["items"])): add(pop(700 + 100 * k), t0 + 0.5 + k * sc.get("step", 0.55), 0.55)
            if typ == "versus":
                add(whoosh(0.4), t0 + 0.3, 0.5); add(whoosh(0.4), t0 + 0.8, 0.5); add(impact(0.7), t0 + 1.3, 0.9)
            if typ == "alert": add(siren(min(2.5, sc["dur"] - 0.4)), t0 + 0.3, 0.22)
            if typ == "question":
                for k in range(len(sc.get("options", []))): add(pop(800 + 120 * k), t0 + 1.0 + 0.2 * k, 0.5)
            if typ == "trivia":
                for k in range(len(sc["options"])): add(pop(700 + 120 * k), t0 + 0.9 + 0.25 * k, 0.5)
                rv = sc["dur"] - 2.2
                for k in range(3): add(tick(), t0 + rv - 2.4 + 0.8 * k, 0.8); add(impact(0.25, 300, 90), t0 + rv - 2.4 + 0.8 * k, 0.35)
                add(ding(), t0 + rv, 0.6); add(impact(0.7), t0 + rv, 0.8)
            if typ == "outro": add(pop(900), t0 + 0.5, 0.5); add(ding(), t0 + 0.8, 0.4)
        if self.mode == "asmr":
            from scipy.signal import butter, sosfilt
            aud = sosfilt(butter(2, 5500, btype="low", fs=SR, output="sos"), aud).astype(np.float32) * 0.75
            def softtap(f=1800):
                m = int(SR * 0.05); tt = np.arange(m) / SR
                x = nr.standard_normal(m) * np.exp(-tt * 140) + 0.5 * np.sin(2 * np.pi * f * tt) * np.exp(-tt * 90)
                return sosfilt(butter(2, [600, 6000], btype="band", fs=SR, output="sos"), x).astype(np.float32)
            for sc in self.scenes:
                k = 0; tt0 = sc["t0"] + 0.12
                while tt0 < sc["t0"] + min(1.6, sc["dur"] - 0.3):
                    add(softtap(1400 + 300 * (k % 4)), tt0, 0.35); tt0 += 0.11 + 0.05 * (k % 3); k += 1
            br = np.cumsum(nr.standard_normal(n)).astype(np.float32); br -= np.convolve(br, np.ones(4410) / 4410, "same")
            br = sosfilt(butter(2, [200, 3000], btype="band", fs=SR, output="sos"), nr.standard_normal(n)).astype(np.float32)
            aud += br / (np.abs(br).max() + 1e-9) * 0.05
        aud = aud / (np.abs(aud).max() + 1e-9)
        vox = np.zeros(n, np.float32)
        if self.voice:
            for sc in self.scenes:
                txt = sc.get("vo") or ("¡Seguí a Duo Bloxyy para más secretos de Roblox!" if sc["type"] == "outro" else "")
                if not txt: continue
                at = sc["t0"] + sc.get("vo_t", 0.25); room = sc["dur"] - sc.get("vo_t", 0.25) - 0.2
                v = tts(txt, room, SR)
                if v is None: continue
                i = int(at * SR); m = min(len(v), n - i); vox[i:i + m] += v[:m]
        talking = np.convolve((np.abs(vox) > 0.02).astype(np.float32), np.ones(int(SR * 0.25)) / (SR * 0.25), "same")
        duck = 1 - 0.6 * np.clip(talking * 3, 0, 1)
        if self.music:
            seed = __import__("zlib").crc32((self.title or "bloxy").encode()) % 100000
            mus = make_dark(self.total, seed, SR) if self.mode == "misterio" else make_music(self.total, seed, SR)
            aud = aud * (0.8 - 0.3 * (1 - duck)) + mus[:n] * 0.28 * duck
            aud = np.tanh(aud * 1.1)
        if self.voice and vox.any():
            aud = aud / (np.abs(aud).max() + 1e-9) * 0.6 + vox * 0.95
            aud = np.tanh(aud * 1.05)
        aud = aud / (np.abs(aud).max() + 1e-9) * 0.85
        pcm = (np.repeat(aud[:, None], 2, axis=1) * 32767).astype(np.int16)
        with wave.open(path, "wb") as wf:
            wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes(pcm.tobytes())

    def build(self, out):
        wav = out + ".wav"; self.audio(wav)
        p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                              "-r", str(FPS), "-i", "-", "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "22",
                              "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out],
                             stdin=subprocess.PIPE)
        for fi in range(int(self.total * FPS)):
            p.stdin.write(self.frame(fi / FPS).tobytes())
        p.stdin.close(); p.wait(); os.remove(wav); print("ok", out, f"{self.total:.1f}s")

    def preview(self, outdir, times):
        os.makedirs(outdir, exist_ok=True); ims = []
        for t in times:
            im = self.frame(float(t)); im.save(os.path.join(outdir, f"t{float(t):05.1f}.png")); ims.append(im.resize((270, 480)))
        sheet = Image.new("RGB", (270 * min(6, len(ims)), 480 * ((len(ims) + 5) // 6)))
        for i, im in enumerate(ims): sheet.paste(im, ((i % 6) * 270, (i // 6) * 480))
        sheet.save(os.path.join(outdir, "hoja.jpg")); print("preview", os.path.join(outdir, "hoja.jpg"))

def main(ep):
    if len(sys.argv) >= 2 and sys.argv[1] == "build": ep.build(sys.argv[2])
    elif len(sys.argv) >= 2 and sys.argv[1] == "preview":
        times = sys.argv[3:] or [sc["t0"] + 2.2 for sc in ep.scenes]
        ep.preview(sys.argv[2], times)
    else: print("uso: build SALIDA.mp4 | preview DIR [t ...]")
