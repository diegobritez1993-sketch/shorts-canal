"""Motor de Shorts para el canal "No digas que no te avisé".

Uso: un episodio define BEATS (escenas) y sonidos con ev(), y llama a build().
Ver episodios/ejemplo_celular_en_la_cama.py.
"""
import os, sys, math, random, subprocess, tempfile
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTDIR = os.path.join(HERE, "fonts")

FPS = 30
DUR = 25.0
NF = int(FPS * DUR)
SS = 2                     # supersampling
W, H = 1080 * SS, 1920 * SS

# ---------- paleta de marca ----------
K = (14, 14, 14)           # negro fondo
K2 = (28, 28, 28)          # gris tarjeta
Y = (255, 214, 10)         # amarillo advertencia
C = (245, 242, 234)        # crema texto
R = (255, 59, 48)          # rojo alerta
G = (120, 120, 120)        # gris fuente/notas
GREEN = (52, 199, 89)

_fc = {}
def font(kind, size):
    """kind: 'A' = Anton (titulares) o un peso de Montserrat: 'Medium','SemiBold','Bold','Black'."""
    size = max(4, int(size))
    key = (kind, size)
    if key not in _fc:
        if kind == "A":
            _fc[key] = ImageFont.truetype(os.path.join(FONTDIR, "Anton-Regular.ttf"), size)
        else:
            f = ImageFont.truetype(os.path.join(FONTDIR, "Montserrat.ttf"), size)
            f.set_variation_by_name(kind)
            _fc[key] = f
    return _fc[key]

# ---------- easing ----------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def prog(t, t0, d): return clamp((t - t0) / d)
def ease_out(p): return 1 - (1 - p) ** 3
def ease_in_out(p): return 3 * p * p - 2 * p * p * p
def back(p, s=1.9):
    p -= 1
    return p * p * ((s + 1) * p + s) + 1
def lerp(a, b, p): return a + (b - a) * p
def mix(c1, c2, p): return tuple(int(lerp(a, b, p)) for a, b in zip(c1, c2))
def S(v): return v * SS

def shake(t, t0, dur, amp):
    p = prog(t, t0, dur)
    if p <= 0 or p >= 1: return 0, 0
    a = amp * (1 - p)
    return a * math.sin(t * 90), a * math.cos(t * 70)

# ---------- texto ----------
def text_c(d, cx, cy, txt, kind, size, fill, scale=1.0, alpha=1.0, bg=K):
    """Texto centrado en (cx,cy) en coordenadas 1080x1920."""
    if scale <= 0.02 or alpha <= 0.01: return
    f = font(kind, size * SS * scale)
    col = mix(bg, fill, alpha) if alpha < 1 else fill
    d.text((cx * SS, cy * SS), txt, font=f, fill=col, anchor="mm")

def text_l(d, x, cy, txt, kind, size, fill):
    d.text((S(x), S(cy)), txt, font=font(kind, size * SS), fill=fill, anchor="lm")

def pop_line(d, t, t0, cx, cy, txt, size, fill, kind="A", bg=K, dur=0.32):
    """Aparece con rebote. Para titulares: kind 'A', size 90-200."""
    p = prog(t, t0, dur)
    if p <= 0: return
    text_c(d, cx, cy, txt, kind, size, fill, scale=back(p), alpha=clamp(p * 2.5), bg=bg)

def slide_line(d, t, t0, cx, cy, txt, size, fill, kind="A", bg=K, dur=0.3, dy=60):
    """Sube y aparece. Para subtítulos: kind 'SemiBold', size 40-50."""
    p = prog(t, t0, dur)
    if p <= 0: return
    e = ease_out(p)
    text_c(d, cx, cy + dy * (1 - e), txt, kind, size, fill, alpha=e, bg=bg)

def pill(d, t, t0, cx, cy, w, txt, fill=Y, ink=K, size=40, h=90):
    """Píldora que se expande con texto (Montserrat Black)."""
    p = prog(t, t0, 0.3)
    if p <= 0: return
    bw = w * ease_out(p)
    rrect(d, cx - bw / 2, cy - h / 2, cx + bw / 2, cy + h / 2, h / 2, fill=fill)
    if p > 0.6:
        text_c(d, cx, cy, txt, "Black", size, ink, alpha=clamp((p - 0.6) * 3), bg=fill)

def stamp(d, t, t0, cx, cy, w2, h2, txt, fill=Y, ink=K, size=130):
    """Sello que cae grande y golpea (usar con sonido 'stamp' en t0-0.2... t0)."""
    p = prog(t, t0, 0.22)
    if p <= 0: return
    sc = lerp(2.4, 1.0, ease_out(p))
    sx, sy = shake(t, t0 + 0.2, 0.35, 16)
    rrect(d, cx - w2 * sc + sx, cy - h2 * sc + sy, cx + w2 * sc + sx, cy + h2 * sc + sy, 30 * sc, fill=fill)
    text_c(d, cx + sx, cy - 3 + sy, txt, "A", size, ink, scale=sc, bg=fill)

# ---------- formas ----------
def rrect(d, x0, y0, x1, y1, r, fill=None, outline=None, width=1):
    d.rounded_rectangle([S(x0), S(y0), S(x1), S(y1)], radius=S(r), fill=fill, outline=outline, width=S(width) if outline else 0)

def circle(d, cx, cy, r, fill=None, outline=None, width=1):
    d.ellipse([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], fill=fill, outline=outline, width=S(width) if outline else 0)

# ---------- íconos ----------
def warning(d, cx, cy, size, col=Y, ink=K, rot=0.0):
    s = size / 400.0
    def P(x, y):
        x, y = (x - 200) * s, (y - 200) * s
        ca, sa = math.cos(rot), math.sin(rot)
        return (S(cx + x * ca - y * sa), S(cy + x * sa + y * ca))
    pts = [P(200, 34), P(372, 326), P(28, 326)]
    d.polygon(pts, fill=col)
    d.line(pts + [pts[0], pts[1]], fill=col, width=int(S(40 * s)), joint="curve")
    for p in pts:
        r = S(20 * s); d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=col)
    bx, by = P(200, 180); bw, bh = S(34 * s), S(122 * s)
    d.rounded_rectangle([bx - bw / 2, by - bh / 2, bx + bw / 2, by + bh / 2], radius=bw / 2, fill=ink)
    dx, dy = P(200, 284); r = S(20 * s)
    d.ellipse([dx - r, dy - r, dx + r, dy + r], fill=ink)

def heart(d, cx, cy, s, col):
    r = s * 0.28
    circle(d, cx - r * 0.95, cy - r * 0.6, r, fill=col)
    circle(d, cx + r * 0.95, cy - r * 0.6, r, fill=col)
    d.polygon([(S(cx - r * 1.9), S(cy - r * 0.35)), (S(cx + r * 1.9), S(cy - r * 0.35)), (S(cx), S(cy + s * 0.48))], fill=col)

def bubble(d, cx, cy, s, col, ink=K):
    rrect(d, cx - s * 0.5, cy - s * 0.42, cx + s * 0.5, cy + s * 0.25, s * 0.2, fill=col)
    d.polygon([(S(cx - s * 0.3), S(cy + s * 0.2)), (S(cx - s * 0.05), S(cy + s * 0.2)), (S(cx - s * 0.36), S(cy + s * 0.48))], fill=col)
    for i in (-1, 0, 1):
        circle(d, cx + i * s * 0.22, cy - s * 0.08, s * 0.065, fill=ink)

def bell(d, cx, cy, s, col):
    d.pieslice([S(cx - s * 0.32), S(cy - s * 0.45), S(cx + s * 0.32), S(cy + s * 0.2)], 180, 360, fill=col)
    d.rectangle([S(cx - s * 0.32), S(cy - s * 0.13), S(cx + s * 0.32), S(cy + s * 0.2)], fill=col)
    d.polygon([(S(cx - s * 0.32), S(cy + s * 0.1)), (S(cx + s * 0.32), S(cy + s * 0.1)), (S(cx + s * 0.46), S(cy + s * 0.3)), (S(cx - s * 0.46), S(cy + s * 0.3))], fill=col)
    circle(d, cx, cy + s * 0.38, s * 0.09, fill=col)
    circle(d, cx, cy - s * 0.47, s * 0.06, fill=col)

def phone(d, cx, cy, w, h, body=K2, outline=C, buzz=0.0, t=0.0):
    ox = math.sin(t * 95) * 9 * buzz
    x0, y0, x1, y1 = cx - w / 2 + ox, cy - h / 2, cx + w / 2 + ox, cy + h / 2
    rrect(d, x0, y0, x1, y1, w * 0.16, fill=body, outline=outline, width=8)
    rrect(d, cx - w * 0.15 + ox, y0 + h * 0.035, cx + w * 0.15 + ox, y0 + h * 0.055, 6, fill=outline)
    if buzz > 0:
        for side in (-1, 1):
            for k in range(2):
                r = w * 0.32 + k * 42
                bx = cx + side * (w / 2 + 10) + ox
                a0, a1 = (-35, 35) if side == 1 else (145, 215)
                d.arc([S(bx - r), S(cy - r), S(bx + r), S(cy + r)], a0, a1, fill=mix(K, Y, buzz * (1 - k * 0.35)), width=S(10))

def person(d, cx, cy, s, col):
    circle(d, cx, cy - s * 0.28, s * 0.18, fill=col)
    d.pieslice([S(cx - s * 0.32), S(cy - s * 0.02), S(cx + s * 0.32), S(cy + s * 0.62)], 180, 360, fill=col)

def ban(d, cx, cy, r, p, width=34):
    circle(d, cx, cy, r, outline=R, width=width)
    if p > 0:
        a = math.radians(-135)
        x0, y0 = cx + math.cos(a) * (r - 10), cy + math.sin(a) * (r - 10)
        x1, y1 = cx - math.cos(a) * (r - 10), cy - math.sin(a) * (r - 10)
        d.line([S(x0), S(y0), S(lerp(x0, x1, p)), S(lerp(y0, y1, p))], fill=R, width=S(width))

def moon(d, cx, cy, r, col=Y, bg=K):
    circle(d, cx, cy, r, fill=col)
    circle(d, cx + r * 0.45, cy - r * 0.3, r * 0.85, fill=bg)

def sun(d, cx, cy, r, t, col=Y):
    for k in range(10):
        a = k / 10 * math.tau + t * 0.8
        d.line([S(cx + math.cos(a) * r * 1.3), S(cy + math.sin(a) * r * 1.3), S(cx + math.cos(a) * r * 1.7), S(cy + math.sin(a) * r * 1.7)], fill=col, width=S(16))
    circle(d, cx, cy, r, fill=col)

def stars(d, t, alpha=1.0):
    rnd = random.Random(11)
    for k in range(40):
        x, y = rnd.uniform(40, 1040), rnd.uniform(40, 1880)
        tw = 0.5 + 0.5 * math.sin(t * rnd.uniform(1.5, 4) + k)
        circle(d, x, y, rnd.uniform(2, 5), fill=mix(K, C, 0.25 * tw * alpha))

def zzz(d, cx, cy, t, col=C):
    for k in range(3):
        tt = (t * 0.7 + k / 3) % 1.0
        text_c(d, cx + k * 40 + tt * 60, cy - tt * 200 - k * 30, "z", "Black", 60 + k * 14, col, alpha=1 - tt)

def battery(d, cx, cy, w, h, level, col):
    rrect(d, cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, 24, outline=C, width=12)
    rrect(d, cx + w / 2 + 6, cy - h * 0.2, cx + w / 2 + 34, cy + h * 0.2, 8, fill=C)
    if level > 0.01:
        rrect(d, cx - w / 2 + 24, cy - h / 2 + 24, cx - w / 2 + 24 + (w - 48) * level, cy + h / 2 - 24, 12, fill=col)

def clock(d, cx, cy, r, pr, turns=3, fill_deg=60):
    """Reloj con aguja girando; pr 0..1."""
    circle(d, cx, cy, r, fill=K2, outline=C, width=10)
    if pr > 0:
        d.pieslice([S(cx - r + 22), S(cy - r + 22), S(cx + r - 22), S(cy + r - 22)], -90, -90 + fill_deg * pr, fill=Y)
    ang = -math.pi / 2 + pr * math.tau * turns
    d.line([S(cx), S(cy), S(cx + math.cos(ang) * r * 0.7), S(cy + math.sin(ang) * r * 0.7)], fill=C, width=S(12))
    circle(d, cx, cy, 16, fill=C)

def donut(d, cx, cy, r, frac, label, col=Y):
    circle(d, cx, cy, r, fill=(48, 48, 48))
    if frac > 0:
        d.pieslice([S(cx - r), S(cy - r), S(cx + r), S(cy + r)], -90, -90 + 360 * frac, fill=col)
    circle(d, cx, cy, r * 0.62, fill=K)
    text_c(d, cx, cy, label, "A", int(r * 0.52), C)

def toggle_row(d, x0, y, label, q, sub=None, w=860, h=150):
    """Fila tipo ajustes con interruptor; q 0..1 = apagado→encendido."""
    rrect(d, x0, y, x0 + w, y + h, 40, fill=K2)
    text_l(d, x0 + 50, y + (h / 2 if not sub else h / 2 - 22), label, "Bold", 50, C)
    if sub: text_l(d, x0 + 50, y + h / 2 + 32, sub, "SemiBold", 34, mix(K2, Y, q))
    tx0 = x0 + w - 230
    rrect(d, tx0, y + h / 2 - 40, tx0 + 180, y + h / 2 + 40, 40, fill=mix((80, 80, 80), GREEN, q))
    circle(d, lerp(tx0 + 40, tx0 + 140, q), y + h / 2, 32, fill=C)

def fmt_num(n):
    return f"{int(n):,}".replace(",", ".")

# ---------- escena final de marca (siempre igual) ----------
def outro(d, t, t0=23.2):
    lt = t - t0
    e = back(prog(lt, 0, 0.4))
    if e > 0.02: warning(d, 540, 640, 330 * e)
    pop_line(d, lt, 0.25, 540, 960, "NO DIGAS QUE", 130, C)
    pop_line(d, lt, 0.45, 540, 1110, "NO TE AVISÉ", 165, Y)
    p = prog(lt, 0.8, 0.3)
    if p > 0:
        bw = 300 * back(p)
        rrect(d, 540 - bw, 1270, 540 + bw, 1370, 50, outline=C, width=5)
        text_c(d, 540, 1320, "SEGUÍ EL CANAL", "Black", 46, C, alpha=clamp(p * 2))

# ---------- sonidos ----------
EV = []
def ev(t, kind, pan=0.0):
    """kinds: pop, tap, click, tick, toggle, whoosh, swipe, thump, stamp, buzz, rustle, shimmer, ding"""
    EV.append((t, kind, pan))

def standard_sounds(beats):
    """Whoosh en cada transición + sonidos del cierre. Llamar una vez por episodio."""
    for t0, _, _ in beats[1:]:
        ev(t0 - 0.12, "whoosh", 0)
    ev(23.2, "pop", 0); ev(23.45, "pop", -0.3); ev(23.65, "pop", 0.3); ev(24.0, "click", 0)

def make_audio(path):
    import numpy as np
    from scipy.io import wavfile
    from scipy.signal import butter, sosfilt
    sr = 48000
    n = int(sr * DUR)
    out = np.zeros((n, 2))
    rng = np.random.default_rng(4)
    def tt(dur): return np.arange(int(sr * dur)) / sr
    def bp(x, lo, hi): return sosfilt(butter(2, [lo, hi], btype="band", fs=sr, output="sos"), x)
    def hp(x, f): return sosfilt(butter(2, f, btype="high", fs=sr, output="sos"), x)
    def lp(x, f): return sosfilt(butter(2, f, btype="low", fs=sr, output="sos"), x)
    def snd(kind):
        if kind == "pop":
            x = tt(0.09); f = 700 * np.exp(-x * 30) + 260
            y = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-x * 55)
            return (y + lp(rng.normal(0, 1, len(x)), 2500) * np.exp(-x * 400) * 0.25) * 0.55
        if kind == "tap":
            x = tt(0.06)
            y = bp(rng.normal(0, 1, len(x)), 1500, 6000) * np.exp(-x * 180)
            return (y + np.sin(2 * np.pi * 320 * x) * np.exp(-x * 90) * 0.3) * 0.35
        if kind == "click":
            x = tt(0.04); return hp(rng.normal(0, 1, len(x)), 3000) * np.exp(-x * 400) * 0.45
        if kind == "tick":
            x = tt(0.05)
            return np.sin(2 * np.pi * 3400 * x) * np.exp(-x * 220) * 0.16 + hp(rng.normal(0, 1, len(x)), 5000) * np.exp(-x * 600) * 0.1
        if kind == "toggle":
            x = tt(0.12)
            a = hp(rng.normal(0, 1, len(x)), 2500) * np.exp(-x * 500)
            b = np.zeros_like(a); off = int(0.045 * sr)
            b[off:] = hp(rng.normal(0, 1, len(x) - off), 1800) * np.exp(-x[: len(x) - off] * 350)
            return a * 0.4 + b * 0.5 + np.sin(2 * np.pi * 900 * x) * np.exp(-x * 120) * 0.1
        if kind == "whoosh":
            x = tt(0.42); env = np.sin(np.pi * x / x[-1]) ** 2
            return bp(rng.normal(0, 1, len(x)), 300, 3000) * env * 0.22
        if kind == "swipe":
            x = tt(0.25); env = np.sin(np.pi * x / x[-1]) ** 1.5
            return bp(rng.normal(0, 1, len(x)), 2000, 9000) * env * 0.16
        if kind == "thump":
            x = tt(0.4); f = 120 * np.exp(-x * 12) + 45
            y = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-x * 9)
            return (y + lp(rng.normal(0, 1, len(x)), 1200) * np.exp(-x * 60) * 0.25) * 0.7
        if kind == "stamp":
            x = tt(0.45); f = 95 * np.exp(-x * 10) + 40
            y = np.sin(2 * np.pi * np.cumsum(f) / sr) * np.exp(-x * 8) * 0.75
            return y + bp(rng.normal(0, 1, len(x)), 400, 5000) * np.exp(-x * 45) * 0.45
        if kind == "buzz":
            x = tt(0.3)
            f0 = 175 + 6 * np.sin(2 * np.pi * 9 * x)
            ph = 2 * np.pi * np.cumsum(f0) / sr
            y = lp(np.sign(np.sin(ph)) * 0.35 + np.sin(ph) * 0.6 + np.sin(2 * ph) * 0.25, 1400)
            y += bp(rng.normal(0, 1, len(x)), 800, 3000) * (0.5 + 0.5 * np.sin(ph)) * 0.18
            env = np.minimum(1, x / 0.015) * np.minimum(1, (x[-1] - x) / 0.03)
            return y * env * 0.5
        if kind == "rustle":
            x = tt(0.9)
            nz = bp(rng.normal(0, 1, len(x)), 1200, 7000)
            gr = np.abs(lp(rng.normal(0, 1, len(x)), 18)); gr = gr / gr.max()
            return nz * gr * np.sin(np.pi * x / x[-1]) * 0.35
        if kind == "shimmer":
            x = tt(1.6)
            y = sum(np.sin(2 * np.pi * f * x + k) for k, f in enumerate((880, 1108.7, 1318.5, 1760)))
            return y * (0.6 + 0.4 * np.sin(2 * np.pi * 6 * x)) * np.minimum(1, x / 0.3) * np.exp(-x * 1.8) * 0.06
        if kind == "ding":
            x = tt(1.2)
            y = np.sin(2 * np.pi * 1318.5 * x) + 0.5 * np.sin(2 * np.pi * 1975.5 * x) + 0.25 * np.sin(2 * np.pi * 2637 * x)
            return y * np.minimum(1, x / 0.004) * np.exp(-x * 4.5) * 0.2
        raise ValueError("sonido desconocido: " + kind)
    for t0, kind, pan in EV:
        y = snd(kind); i0 = max(0, int(t0 * sr))
        i1 = min(n, i0 + len(y)); y = y[: i1 - i0]
        gl = math.cos((pan + 1) * math.pi / 4); gr = math.sin((pan + 1) * math.pi / 4)
        out[i0:i1, 0] += y * gl; out[i0:i1, 1] += y * gr
    rv = np.zeros_like(out)
    for dl, g in [(0.023, 0.18), (0.041, 0.12), (0.067, 0.08), (0.097, 0.05)]:
        k = int(dl * sr)
        rv[k:, 0] += out[:-k, 1] * g; rv[k:, 1] += out[:-k, 0] * g
    out = out + rv
    out = out / np.max(np.abs(out)) * 0.85
    wavfile.write(path, sr, (out * 32767).astype(np.int16))

# ---------- render ----------
BEATS = []

def frame(i):
    t = i / FPS
    im = Image.new("RGB", (W, H), K)
    d = ImageDraw.Draw(im)
    for t0, t1, fn in BEATS:
        if t0 <= t < t1:
            fn(d, t)
    for t0, _, _ in BEATS[1:]:           # barrida amarilla entre escenas
        p = prog(t, t0 - 0.12, 0.24)
        if 0 < p < 1:
            yc = lerp(-200, 2120, ease_in_out(p))
            d.rectangle([0, S(yc - 160), W, S(yc + 160)], fill=Y)
    d.rectangle([0, 0, int(W * t / DUR), S(10)], fill=Y)   # barra de progreso
    return im.reduce(SS)

def _scene(args):
    idx, f0, f1, outdir = args
    final = os.path.join(outdir, f"scene{idx:02d}.mp4")
    tmp = os.path.join(outdir, f"scene{idx:02d}.tmp.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(f0, f1):
        pr.stdin.write(frame(i).tobytes())
    pr.stdin.close()
    if pr.wait() != 0:
        raise RuntimeError(f"ffmpeg falló en escena {idx}")
    os.replace(tmp, final)
    return final

def preview(frames, outdir):
    """Guarda PNGs de cuadros sueltos para revisar antes del render completo."""
    os.makedirs(outdir, exist_ok=True)
    paths = []
    for f in frames:
        p = os.path.join(outdir, f"f{f:04d}.png"); frame(f).save(p); paths.append(p)
    return paths

def build(out_mp4, workers=2):
    """Renderiza escenas en paralelo, las une y agrega el audio."""
    assert BEATS, "definí BEATS"
    work = tempfile.mkdtemp(prefix="short_")
    bounds = sorted(set([0] + [int(round(t0 * FPS)) for t0, _, _ in BEATS] + [NF]))
    jobs = [(k, bounds[k], bounds[k + 1], work) for k in range(len(bounds) - 1)]
    with Pool(workers) as pool:
        files = pool.map(_scene, jobs)
    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as fh:
        for f in files: fh.write(f"file '{f}'\n")
    joined = os.path.join(work, "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined], check=True)
    wav = os.path.join(work, "sfx.wav")
    make_audio(wav)
    tmp = out_mp4[:-4] + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, out_mp4)
    return out_mp4

def main(beats):
    """CLI de un episodio: python episodio.py preview DIR f1 f2 ... | python episodio.py build salida.mp4"""
    BEATS[:] = beats
    if len(sys.argv) >= 3 and sys.argv[1] == "preview":
        print("\n".join(preview([int(x) for x in sys.argv[3:]], sys.argv[2])))
    elif len(sys.argv) >= 3 and sys.argv[1] == "build":
        print(build(sys.argv[2]))
    else:
        print(main.__doc__)
