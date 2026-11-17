"""Música hard rock con instrumentos REALES grabados (no sintetizados).
Guitarra: Karoryfer «Black and Green Guitars» (Hofner Club grabada, CC0) pasada por distorsión + simulador de caja.
Batería: Karoryfer «Big Rusty Drums» (batería acústica grabada, CC0).
Las grabaciones están en motor/samples/ (ver samples/LICENCIA.txt). Riff original, no es canción de ninguna banda."""
import glob, os
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, resample_poly, fftconvolve

SR = 44100
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
_cache = {}

def _load(path):
    if path not in _cache:
        x, sr = sf.read(path, always_2d=True); x = x.mean(1)
        if sr != SR: x = resample_poly(x, SR, sr)
        _cache[path] = x
    return _cache[path]

def _pick(prefix, rng):
    fs = sorted(glob.glob(os.path.join(D, prefix + "_*.flac")))
    return _load(fs[rng.integers(len(fs))])

def _note(midi, kind, rng):
    """nota real de guitarra; transpone desde la grabación más cercana (rango grabado 52-64)."""
    base = min(64, max(52, midi if midi >= 52 else midi + 12 * ((52 - midi + 11) // 12)))
    x = _pick(f"g_{kind}_{base}", rng)
    semis = midi - base
    if semis:
        r = 2 ** (semis / 12); up, down = 1000, int(round(1000 * r))
        x = resample_poly(x, up, down)
    return x

def _f(kind, f, order=2):
    return butter(order, f, kind, fs=SR, output="sos")

def amp(x, gain=28.0):
    """amplificador de válvulas simulado + caja 4x12 (EQ): distorsión de hard rock."""
    x = sosfilt(_f("highpass", 110), x)
    x = sosfilt(butter(2, [600, 2500], "bandpass", fs=SR, output="sos"), x) * 0.6 + x * 0.4
    y = np.tanh(gain * x + 0.15) - np.tanh(0.15)
    y = np.tanh(1.6 * y)
    y = sosfilt(_f("lowpass", 5200, 4), y)
    y = sosfilt(_f("highpass", 75), y)
    # pico de presencia de caja
    y = y + 0.35 * sosfilt(butter(2, [1800, 3200], "bandpass", fs=SR, output="sos"), y)
    return y

def _place(buf, x, at, g=1.0):
    s = int(at * SR)
    if s >= len(buf): return
    e = min(len(buf), s + len(x)); buf[s:e] += x[:e - s] * g

# riff original en corcheas (2 compases). (offset, tipo) tipo m=muteada, a=acorde abierto, None=silencio
RIFF = [(0, "m"), (0, "m"), (0, "m"), (0, "m"), (3, "a"), (None, ""), (5, "a"), (0, "m"),
        (0, "m"), (0, "m"), (0, "m"), (0, "m"), (7, "a"), (5, "a"), (3, "a"), (2, "a")]

def guitar_track(total, bpm, root, rng):
    n = int(total * SR) + SR; dry = np.zeros(n); step = 60 / bpm / 2
    i = 0; t = 0.0
    while t < total:
        off, k = RIFF[i % 16]
        if off is not None:
            r = root + off
            ln = int(step * (0.92 if k == "m" else 1.9) * SR)
            kind = "st" if k == "m" else "tw"
            ch = np.zeros(ln)
            for iv, g in ((0, 1.0), (7, 0.8), (12, 0.55)):  # power chord: raíz, quinta, octava
                x = _note(r + iv, kind, rng)[:ln]; ch[:len(x)] += x * g
            ev = np.minimum(1, np.arange(ln) / (0.003 * SR)) * np.minimum(1, (ln - np.arange(ln)) / (0.02 * SR))
            _place(dry, ch * ev * (0.55 if k == "m" else 1.0), t + rng.uniform(0, 0.006))
        t += step; i += 1
    return amp(dry)

def bass_track(total, bpm, root, rng):
    n = int(total * SR) + SR; b = np.zeros(n); step = 60 / bpm / 2
    i = 0; t = 0.0
    while t < total:
        off, k = RIFF[i % 16]
        if off is not None:
            x = _note(root + off - 12, "st" if k == "m" else "tw", rng)[: int(step * 0.95 * SR)]
            _place(b, x, t)
        t += step; i += 1
    b = sosfilt(_f("lowpass", 900, 4), np.tanh(b * 3))
    return b

def drum_track(total, bpm, rng, crashes):
    n = int(total * SR) + 3 * SR; d = np.zeros(n); beat = 60 / bpm
    k = 0; t = 0.0
    while t < total:
        pos = k % 16
        if pos in (0, 4, 8, 11, 12) or (pos == 15 and k % 32 == 31): _place(d, _pick("d_kick", rng), t, 1.0)
        if pos in (4, 12): _place(d, _pick("d_snare", rng), t, 0.95)
        if pos == 14 and k % 32 == 30: _place(d, _pick("d_snare", rng), t, 0.6)
        if pos % 2 == 0: _place(d, _pick("d_hat", rng), t, 0.32 if pos % 4 else 0.42)
        else: _place(d, _pick("d_hat", rng), t, 0.2)
        t += beat / 4; k += 1
    for c in crashes: _place(d, _pick("d_crash", rng), c, 0.55)
    return d

def _room(x):
    ir_n = int(0.35 * SR); r = np.random.default_rng(7).standard_normal(ir_n)
    ir = r * np.exp(-np.arange(ir_n) / SR * 12); ir[0] = 0
    return fftconvolve(x, ir)[: len(x)] * 0.02

def rock(total, bpm=140, tono=40, seed=3, crashes=(0.0,)):
    """devuelve estéreo (n,2) normalizado. tono = nota midi de la raíz (40 = Mi grave)."""
    rng = np.random.default_rng(seed)
    root = 40 + ((tono - 40) % 5)  # Mi, Fa, Fa#, Sol o Lab grave
    n = int(total * SR)
    gL = guitar_track(total, bpm, root, rng)[:n]
    gR = guitar_track(total, bpm, root, rng)[:n]  # doble toma (como en estudio)
    ba = bass_track(total, bpm, root, rng)[:n]
    dr = drum_track(total, bpm, rng, crashes)[:n]
    dr = dr + _room(dr)
    for v in (gL, gR, ba, dr): v /= max(1e-6, np.abs(v).max())
    L = 0.55 * gL + 0.18 * gR + 0.45 * ba + 1.1 * dr
    R = 0.18 * gL + 0.55 * gR + 0.45 * ba + 1.1 * dr
    st = np.stack([L, R], 1)
    st = np.tanh(st * 1.3) / np.tanh(1.3)
    return st / np.abs(st).max()
