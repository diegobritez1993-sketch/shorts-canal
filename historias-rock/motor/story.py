import math, subprocess, os, sys, random, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy.signal import lfilter

import json
FD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts") + "/"
ANTON = FD + "anton-latin-400-normal.woff"
OSW = FD + "oswald-latin-500-normal.woff"
OSWB = FD + "oswald-latin-700-normal.woff"
TYPE = FD + "special-elite-latin-400-normal.woff"
HANDLE = "@diegoeditspy"
W, H, FPS = 1080, 1920, 30
BONE = (236, 228, 212); RED = (214, 32, 39); DIM = (150, 142, 130)
_f = {}
def F(p, s):
    if (p, s) not in _f: _f[(p, s)] = ImageFont.truetype(p, s)
    return _f[(p, s)]

def eo(t): t = max(0., min(1., t)); return 1 - (1 - t) ** 3

rng = np.random.default_rng(3)
# fondo: negro con viñeta + textura de grano y rayones
def make_bg():
    y, x = np.mgrid[0:H, 0:W]
    d = np.sqrt(((x - W / 2) / W) ** 2 + ((y - H * 0.45) / H) ** 2)
    base = np.clip(28 - d * 60, 4, 28)
    img = np.stack([base * 1.15, base * 0.9, base * 0.85], -1)
    return img.astype(np.float32)
BG = make_bg()
GRAINS = [(rng.standard_normal((H // 2, W // 2)) * 9).astype(np.float32) for _ in range(6)]

def background(fi):
    g = GRAINS[fi % 6].repeat(2, 0).repeat(2, 1)[:, :, None]
    a = np.clip(BG + g, 0, 255).astype(np.uint8)
    im = Image.fromarray(a, "RGB")
    d = ImageDraw.Draw(im)
    r = random.Random(fi // 2)
    for _ in range(2):  # rayones de película
        x = r.randint(0, W)
        d.line((x, 0, x + r.randint(-20, 20), H), fill=(60, 55, 50), width=1)
    return im

def ctext(d, y, s, f, fill, cx=W // 2, stroke=0):
    w = d.textlength(s, font=f)
    d.text((cx - w / 2, y), s, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0))

def layer_text(s, f, fill, stroke=0):
    bb = f.getbbox(s, stroke_width=stroke)
    im = Image.new("RGBA", (bb[2] + 20, bb[3] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), s, font=f, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0))
    return im

def paste_scaled(fr, im, cx, y, sc, a):
    if a <= 0: return
    im2 = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))), Image.BICUBIC)
    if a < 1:
        al = im2.getchannel("A").point(lambda v: int(v * a)); im2.putalpha(al)
    fr.paste(im2, (int(cx - im2.width / 2), int(y - im2.height / 2)), im2)

def wrap_lines(s, f, width):
    out, cur = [], ""
    for w_ in s.split():
        t_ = (cur + " " + w_).strip()
        if f.getlength(t_) <= width: cur = t_
        else: out.append(cur); cur = w_
    if cur: out.append(cur)
    return out

def header(d, a):
    if a <= 0: return
    c = tuple(int(v * a) for v in BONE)
    ctext(d, 250, "ROCK EN ASCENSO", F(OSWB, 46), c)
    d.rectangle((W // 2 - 60, 318, W // 2 + 60, 324), fill=tuple(int(v * a) for v in RED))

def footer(d, a, src):
    if a <= 0: return
    c = tuple(int(v * a) for v in BONE); c2 = tuple(int(v * a) for v in DIM)
    ctext(d, 1560, HANDLE, F(ANTON, 58), c)
    for k, ln in enumerate(wrap_lines(src, F(OSW, 28), W - 160)):
        ctext(d, 1636 + k * 36, ln, F(OSW, 28), c2)

L = {}
def frame(t, fi, S):
    fr = background(fi)
    d = ImageDraw.Draw(fr)
    for sc in S:
        lt = t - sc["t0"]
        if lt < 0 or lt > sc["dur"]: continue
        out = 1 - eo((lt - (sc["dur"] - 0.35)) / 0.35) if lt > sc["dur"] - 0.35 else 1
        for el in sc["els"]:
            k = (el["s"], el["f"], el.get("s2", 0))
            if k not in L:
                L[k] = layer_text(el["s"], F(el["f"], el["size"]), el.get("c", BONE), el.get("stroke", 0))
            et = lt - el.get("d", 0)
            a = eo(et / 0.35) * out
            if el.get("slam"):
                s = 1.0 + 0.6 * (1 - eo(et / 0.25)); a = min(1, et / 0.08) * out if et > 0 else 0
            else:
                s = 0.94 + 0.06 * eo(et / 0.5)
            dy = 0 if el.get("slam") else (1 - eo(et / 0.4)) * 30
            paste_scaled(fr, L[k], W / 2, el["y"] + dy, s, a)
            if el.get("bar") and et > 0:
                bw = int(eo(et / 0.4) * el["bar"])
                d.rectangle((W / 2 - bw / 2, el["y"] + el["size"] * 0.8, W / 2 + bw / 2, el["y"] + el["size"] * 0.8 + 10), fill=RED)
    last = S[-1]
    footer(d, eo((t - last["t0"] - 0.3) / 0.5) if t > last["t0"] else 0, SRC)
    # flash al cambiar de escena
    for sc in S[1:]:
        dt = t - sc["t0"]
        if 0 <= dt < 0.12:
            fr = Image.blend(fr, Image.new("RGB", (W, H), (255, 245, 230)), 0.35 * (1 - dt / 0.12))
    # fundido final
    if t > TOTAL - 0.5:
        fr = Image.blend(fr, Image.new("RGB", (W, H)), (t - (TOTAL - 0.5)) / 0.5)
    return fr

# ---------- música original: riff de power chords con distorsión ----------
SR = 44100
def riff(total, bpm=140, root=40):  # root midi 40 = E2
    n = int(total * SR); out = np.zeros(n)
    beat = 60 / bpm; step = beat / 2
    pat = [0, 0, None, 0, 3, None, 5, 0, 0, 0, None, 0, 7, 6, 5, 3]  # corcheas
    t0 = 0.0; i = 0
    while t0 < total:
        p = pat[i % 16]
        if p is not None:
            s = int(t0 * SR); ln = int(step * 0.95 * SR); tt = np.arange(ln) / SR
            f = 440 * 2 ** ((root + p - 69) / 12)
            sig = np.zeros(ln)
            for mul in (1, 1.4983, 2.0):
                for det in (-0.004, 0.004):
                    ph = (tt * f * mul * (1 + det)) % 1
                    sig += 2 * ph - 1
            mute = 0.55 if (i % 4 in (1, 2)) else 1.0
            env = np.minimum(1, tt / 0.004) * np.exp(-tt / (0.09 if mute < 1 else 0.35))
            out[s:s + ln] += sig * env * mute
        t0 += step; i += 1
    a = np.exp(-2 * np.pi * 2800 / SR)
    out = lfilter([1 - a], [1, -a], np.tanh(out * 3.5))
    return out * 0.32

def drums(total, bpm=140):
    n = int(total * SR); L_ = np.zeros(n); beat = 60 / bpm
    k = 0; t = 0.0
    while t < total:
        s = int(t * SR)
        if k % 2 == 0 or k % 8 == 7:
            kl = int(0.25 * SR); tk = np.arange(kl) / SR
            f = 50 + 90 * np.exp(-tk * 35)
            L_[s:s + kl] += (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk * 12) * 0.6)[:max(0, n - s)]
        if k % 4 == 2:
            sl = int(0.22 * SR); ts = np.arange(sl) / SR
            sn = rng.standard_normal(sl) * np.exp(-ts * 14) * 0.35 + np.sin(2 * np.pi * 200 * ts) * np.exp(-ts * 20) * 0.25
            L_[s:s + sl] += sn[:max(0, n - s)]
        hl = int(0.05 * SR); hh = rng.standard_normal(hl); hh = hh - lfilter([0.3], [1, -0.7], hh)
        L_[s:s + hl] += (hh * np.exp(-np.arange(hl) / SR * 70) * 0.08)[:max(0, n - s)]
        t += beat / 2; k += 1
    return L_

def hit(total, at):
    n = int(total * SR); o = np.zeros(n); s = int(at * SR); ln = int(1.2 * SR)
    tt = np.arange(ln) / SR
    x = (rng.standard_normal(ln) * 0.5 + np.sin(2 * np.pi * 41 * tt)) * np.exp(-tt * 3.2) * 0.5
    e = min(n, s + ln); o[s:e] += x[:e - s]; return o

def music(total, hits, out, bpm=140, root=40):
    m = riff(total, bpm, root) + drums(total, bpm)
    for h in hits: m += hit(total, h)
    tt = np.arange(len(m)) / SR
    m *= np.minimum(1, tt / 0.3) * np.minimum(1, (total - tt) / 0.8)
    m = m / np.abs(m).max() * 0.85
    st = np.stack([m, m * 0.97], 1)
    w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()

def render(S, out):
    global TOTAL
    TOTAL = S[-1]["t0"] + S[-1]["dur"]
    tmp = out + ".part.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-i", out + ".wav", "-map", "0:v", "-map", "1:a",
                          "-c:v", "libx264", "-crf", "19", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                          "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
    for i in range(int(TOTAL * FPS)):
        p.stdin.write(frame(i / FPS, i, S).tobytes())
    p.stdin.close()
    if p.wait() == 0: os.replace(tmp, out)

FONTS = {"anton": ANTON, "osw": OSW, "oswb": OSWB, "type": TYPE}
COLORS = {"bone": BONE, "red": RED, "dim": DIM}

def load(path):
    """JSON: {"fuente": str, "seed": int, "escenas": [{"t0","dur","els":[{"s","f","size","y","c"?,"slam"?,"d"?,"bar"?}]}]}"""
    j = json.load(open(path, encoding="utf-8"))
    S = []
    for sc in j["escenas"]:
        els = []
        for e in sc["els"]:
            e = dict(e); e["f"] = FONTS[e["f"]]; e["c"] = COLORS[e.get("c", "bone")]
            els.append(e)
        S.append({"t0": sc["t0"], "dur": sc["dur"], "els": els})
    return j, S

if __name__ == "__main__":
    # uso: python3 story.py datos/AAAA-MM-DD.json salida.mp4 [preview]
    j, S = load(sys.argv[1])
    SRC = j["fuente"]
    out = sys.argv[2]
    total = S[-1]["t0"] + S[-1]["dur"]
    if sys.argv[3:] == ["preview"]:
        TOTAL = total
        ts = [sc["t0"] + sc["dur"] - 0.6 for sc in S]
        ims = [frame(t, int(t * 30), S).resize((360, 640)) for t in ts]
        sheet = Image.new("RGB", (360 * len(ims), 640))
        for k, im in enumerate(ims): sheet.paste(im, (k * 360, 0))
        sheet.save(out, quality=85)
    else:
        rng = np.random.default_rng(j.get("seed", 3))
        music(total, [sc["t0"] + (0.5 if k else 0) for k, sc in enumerate(S)], out + ".wav", j.get("bpm", 140), j.get("tono", 40))
        render(S, out)
        os.remove(out + ".wav")
        print("ok", out)
