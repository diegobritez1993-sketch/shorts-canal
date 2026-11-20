"""Motor de videos LARGOS (16:9, 1920x1080) para "No digas que no te avisé".

Reusa la paleta, fuentes, íconos y sonidos de engine.py. Formato: intro + capítulos "Top N" + cierre.
Cada capítulo: tarjeta de número (3 s) y luego un visual animado a la izquierda + una idea nueva
a la derecha cada ~4 s. Ver largos/2026-11-20_5-trucos-de-las-apps.py.
"""
import os, sys, math, random, subprocess, tempfile
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine as E
from engine import *          # paleta, easing, formas, íconos, ev(), font()...
from PIL import Image, ImageDraw

LW, LH = 1920, 1080
W2, H2 = LW * SS, LH * SS
SCENES = []                   # [(t0, t1, fn)]
DURL = 180.0

def set_duration(seconds):
    global DURL
    DURL = float(seconds)
    E.DUR = DURL              # make_audio usa engine.DUR

def text_fit(d, cx, cy, txt, kind, size, fill, maxw, scale=1.0, alpha=1.0, bg=K):
    """Texto centrado que se achica solo para entrar en maxw px."""
    if scale <= 0.02 or alpha <= 0.01: return
    f = font(kind, size * SS)
    w = d.textlength(txt, font=f) / SS
    if w > maxw: size = size * maxw / w
    text_c(d, cx, cy, txt, kind, size, fill, scale=scale, alpha=alpha, bg=bg)

def pop_fit(d, t, t0, cx, cy, txt, size, fill, maxw, kind="A", bg=K, dur=0.32):
    p = prog(t, t0, dur)
    if p <= 0: return
    text_fit(d, cx, cy, txt, kind, size, fill, maxw, scale=back(p), alpha=clamp(p * 2.5), bg=bg)

def slide_fit(d, t, t0, cx, cy, txt, size, fill, maxw, kind="SemiBold", bg=K, dy=30):
    p = prog(t, t0, 0.3)
    if p <= 0: return
    e = ease_out(p)
    text_fit(d, cx, cy + dy * (1 - e), txt, kind, size, fill, maxw, alpha=e, bg=bg)

# ---------- capítulo genérico ----------
def chapter(n, title, beats, visual, source, t0, dur=32.0, accent=Y):
    """Devuelve una escena (t0, t1, fn). beats: lista de (TITULAR, subtítulo), uno cada 4 s.
    visual(d, lt, cx, cy): dibuja la animación del panel izquierdo (lt = segundos desde que arranca)."""
    t1 = t0 + dur
    def fn(d, t):
        lt = t - t0
        if lt < 3.0:                                   # tarjeta del número
            sx, sy = shake(lt, 0.25, 0.35, 18)
            p = prog(lt, 0.0, 0.22)
            if p > 0:
                sc = lerp(2.2, 1.0, ease_out(p))
                text_c(d, 960 + sx, 420 + sy, f"#{n}", "A", 300, accent, scale=sc)
            pop_fit(d, lt, 0.45, 960, 700, title, 130, C, 1700)
            slide_fit(d, lt, 0.8, 960, 820, f"truco {n} de 5", 44, G, 800)
            return
        lt2 = lt - 3.0
        # encabezado
        text_l(d, 80, 70, f"#{n} · {title}", "A", 46, accent)
        # visual izquierdo
        visual(d, lt2, 500, 590)
        # separador
        d.line([S(960), S(220), S(960), S(960)], fill=(40, 40, 40), width=S(3))
        # idea actual (una cada 4 s)
        i = min(len(beats) - 1, int(lt2 // 4))
        bt = lt2 - i * 4
        big, small = beats[i]
        col = accent if big.startswith("EL TRUCO") else C
        pop_fit(d, bt, 0.05, 1440, 520, big, 96, col, 880)
        slide_fit(d, bt, 0.35, 1440, 640, small, 42, C, 880)
        # puntitos de avance
        for k in range(len(beats)):
            circle(d, 1440 + (k - (len(beats) - 1) / 2) * 34, 800, 9, fill=accent if k <= i else (60, 60, 60))
        # fuente
        if source:
            text_fit(d, 1440, 1010, source, "SemiBold", 28, G, 900)
    return (t0, t1, fn)

def chapter_sounds(t0, nbeats, dur=32.0):
    ev(t0, "stamp"); ev(t0 + 0.45, "pop"); ev(t0 + 0.8, "tap")
    for k in range(nbeats):
        tb = t0 + 3.0 + k * 4
        if k: ev(tb - 0.05, "swipe", 0.3)
        ev(tb + 0.05, "pop", -0.2); ev(tb + 0.35, "tap", 0.2)

# ---------- render ----------
def frame(i):
    t = i / FPS
    im = Image.new("RGB", (W2, H2), K)
    d = ImageDraw.Draw(im)
    for t0, t1, fn in SCENES:
        if t0 <= t < t1:
            fn(d, t)
    for t0, _, _ in SCENES[1:]:                 # barrida amarilla horizontal entre escenas
        p = prog(t, t0 - 0.14, 0.28)
        if 0 < p < 1:
            xc = lerp(-300, 2220, ease_in_out(p))
            d.rectangle([S(xc - 220), 0, S(xc + 220), H2], fill=Y)
    d.rectangle([0, 0, int(W2 * t / DURL), S(8)], fill=Y)   # barra de progreso
    return im.reduce(SS)

def _scene(args):
    idx, f0, f1, outdir = args
    final = os.path.join(outdir, f"scene{idx:03d}.mp4")
    tmp = os.path.join(outdir, f"scene{idx:03d}.tmp.mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{LW}x{LH}", "-r", str(FPS), "-i", "-",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(f0, f1):
        pr.stdin.write(frame(i).tobytes())
    pr.stdin.close()
    if pr.wait() != 0:
        raise RuntimeError(f"ffmpeg falló en escena {idx}")
    os.replace(tmp, final)
    return final

def ambient_bed(path_in, path_out, gain=0.10):
    """Mezcla un colchón ambiental suave (acordes lentos) debajo de los efectos."""
    import numpy as np
    from scipy.io import wavfile
    from scipy.signal import butter, sosfilt
    sr, x = wavfile.read(path_in)
    x = x.astype(np.float64) / 32767
    n = len(x); t = np.arange(n) / sr
    chords = [(110.0, 164.81, 220.0, 261.63), (98.0, 146.83, 196.0, 246.94), (87.31, 130.81, 174.61, 220.0), (98.0, 146.83, 196.0, 233.08)]
    pad = np.zeros(n)
    seg = 8.0
    for k in range(int(DURL // seg) + 1):
        a, b = int(k * seg * sr), min(n, int((k + 1) * seg * sr) + int(sr))
        if a >= n: break
        tt = t[a:b] - k * seg
        env = np.minimum(1, tt / 2.0) * np.minimum(1, np.maximum(0, (seg + 1 - tt)) / 2.0)
        for f in chords[k % len(chords)]:
            pad[a:b] += np.sin(2 * np.pi * f * tt) * env * (0.6 + 0.4 * np.sin(2 * np.pi * 0.15 * tt + f))
    pad = sosfilt(butter(2, 900, btype="low", fs=sr, output="sos"), pad)
    pad = pad / (np.max(np.abs(pad)) + 1e-9)
    fade = np.minimum(1, t / 3) * np.minimum(1, (t[-1] - t) / 3)
    out = x + (pad * fade * gain)[:, None]
    out = out / np.max(np.abs(out)) * 0.85
    wavfile.write(path_out, sr, (out * 32767).astype(np.int16))

def preview(times, outdir):
    os.makedirs(outdir, exist_ok=True)
    paths = []
    for tt in times:
        f = int(round(tt * FPS)); p = os.path.join(outdir, f"t{tt:06.1f}.png"); frame(f).save(p); paths.append(p)
    return paths

def build(out_mp4, workers=2):
    nf = int(DURL * FPS)
    work = tempfile.mkdtemp(prefix="largo_")
    # trozos de ~6 s para repartir entre procesos
    bounds = list(range(0, nf, 180)) + [nf]
    jobs = [(k, bounds[k], bounds[k + 1], work) for k in range(len(bounds) - 1)]
    with Pool(workers) as pool:
        files = pool.map(_scene, jobs)
    lst = os.path.join(work, "list.txt")
    with open(lst, "w") as fh:
        for f in files: fh.write(f"file '{f}'\n")
    joined = os.path.join(work, "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined], check=True)
    sfx = os.path.join(work, "sfx.wav"); mixw = os.path.join(work, "mix.wav")
    make_audio(sfx); ambient_bed(sfx, mixw)
    tmp = out_mp4[:-4] + ".tmp.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-i", mixw, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp], check=True)
    os.replace(tmp, out_mp4)
    return out_mp4

def main(scenes, duration):
    """python largo.py preview DIR t1 t2 ... (segundos) | python largo.py build salida.mp4"""
    set_duration(duration)
    SCENES[:] = scenes
    if len(sys.argv) >= 3 and sys.argv[1] == "preview":
        print("\n".join(preview([float(x) for x in sys.argv[3:]], sys.argv[2])))
    elif len(sys.argv) >= 3 and sys.argv[1] == "build":
        print(build(sys.argv[2]))
    else:
        print(main.__doc__)
