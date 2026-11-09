"""Música original (lo-fi) + efectos de sonido, sin samples externos."""
import numpy as np, wave, sys, json

SR = 44100
rng = np.random.default_rng(7)

def note(m):  # midi -> Hz
    return 440.0 * 2 ** ((m - 69) / 12)

def lp(x, cut):
    a = np.exp(-2 * np.pi * cut / SR)
    y = np.empty_like(x); acc = 0.0
    # filtro de 1 polo vectorizado por bloques
    from scipy.signal import lfilter
    return lfilter([1 - a], [1, -a], x)

def env(n, a, r):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
    return e

def music(total, bpm=86, seed=0, key=0):
    n = int((total + 10) * SR)
    L = np.zeros(n); R = np.zeros(n)
    beat = 60 / bpm
    bar = beat * 4
    progs = [
        [[57, 60, 64, 67, 71], [53, 57, 60, 64, 67], [48, 52, 55, 59, 64], [55, 59, 62, 66, 69]],
        [[50, 53, 57, 60, 64], [55, 59, 62, 65, 69], [48, 52, 55, 59, 62], [57, 60, 64, 67, 71]],
    ]
    prog = [[m + key for m in c] for c in progs[seed % 2]]
    t_bar = 0.0; bi = 0
    while t_bar < total:
        ch = prog[bi % 4]
        s = int(t_bar * SR); ln = int(bar * SR)
        tt = np.arange(ln) / SR
        # pad
        pad = np.zeros(ln)
        for m in ch[:4]:
            f = note(m)
            for det in (-0.12, 0.12):
                ff = f * 2 ** (det / 12)
                for h, amp in ((1, 1), (2, 0.35), (3, 0.15)):
                    pad += amp * np.sin(2 * np.pi * ff * h * tt + rng.random() * 6)
        pe = np.minimum(1, tt / 0.6) * np.minimum(1, (bar - tt) / 0.4)
        pad = pad * pe * 0.018
        L[s:s + ln] += pad; R[s:s + ln] += pad
        # bajo
        for k in (0, 2.5):
            bs = s + int(k * beat * SR); bl = int(beat * 1.4 * SR)
            tb = np.arange(bl) / SR
            b = np.sin(2 * np.pi * note(ch[0] - 24) * tb) * env(bl, 0.01, 0.5) * 0.16
            L[bs:bs + bl] += b; R[bs:bs + bl] += b
        # arpegio (corcheas)
        for k in range(8):
            if rng.random() < 0.3: continue
            m = ch[[0, 2, 4, 3, 1, 2, 4, 3][k]] + 12
            ks = s + int(k * beat / 2 * SR); kl = int(0.6 * SR)
            tk = np.arange(kl) / SR
            v = (np.sin(2 * np.pi * note(m) * tk) + 0.2 * np.sin(4 * np.pi * note(m) * tk)) * env(kl, 0.004, 0.18) * 0.045
            pan = 0.5 + 0.35 * np.sin(k)
            L[ks:ks + kl] += v * (1 - pan); R[ks:ks + kl] += v * pan
        # batería
        for k in range(4):
            ds = s + int(k * beat * SR)
            if k in (0, 2) or (k == 3 and bi % 2):
                kl = int(0.35 * SR); tk = np.arange(kl) / SR
                f = 45 + 80 * np.exp(-tk * 30)
                kick = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tk * 9) * 0.32
                L[ds:ds + kl] += kick; R[ds:ds + kl] += kick
            if k in (1, 3):
                sl = int(0.25 * SR); ts = np.arange(sl) / SR
                sn = (lp(rng.standard_normal(sl), 3500) * 0.5 + np.sin(2 * np.pi * 190 * ts) * 0.3) * np.exp(-ts * 16) * 0.16
                L[ds:ds + sl] += sn; R[ds:ds + sl] += sn
            for h in (0, 0.5):
                hs = ds + int(h * beat * SR) + int(0.012 * SR * (k % 2)); hl = int(0.06 * SR)
                hh = rng.standard_normal(hl)
                hh = (hh - lp(hh, 6000)) * np.exp(-np.arange(hl) / SR * 60) * 0.05
                L[hs:hs + hl] += hh * 0.8; R[hs:hs + hl] += hh
        t_bar += bar; bi += 1
    # crujido de vinilo
    cr = (rng.random(n) < 0.0004) * rng.standard_normal(n) * 0.05
    L += lp(cr, 4000); R += lp(cr, 4000)
    L = lp(L, 9000); R = lp(R, 9000)
    m = int(total * SR)
    L = L[:m]; R = R[:m]
    fi = np.minimum(1, np.arange(m) / (1.0 * SR)); fo = np.minimum(1, (m - np.arange(m)) / (3.0 * SR))
    return L * fi * fo, R * fi * fo

def whoosh():
    n = int(0.55 * SR); t = np.arange(n) / SR
    x = rng.standard_normal(n)
    from scipy.signal import lfilter
    y = np.zeros(n); seg = 512
    for i in range(0, n, seg):
        c = 300 + 5000 * np.sin(np.pi * min(1, i / n)) ** 2
        a = np.exp(-2 * np.pi * c / SR)
        y[i:i + seg] = lfilter([1 - a], [1, -a], x[i:i + seg])
    return y * np.sin(np.pi * t / t[-1]) ** 2 * 0.35

def pop(pitch=1.0):
    n = int(0.12 * SR); t = np.arange(n) / SR
    f = (900 + 700 * np.exp(-t * 40)) * pitch
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 35) * 0.22

def ding():
    n = int(0.9 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1318 * t) + 0.5 * np.sin(2 * np.pi * 1975 * t)) * np.exp(-t * 5) * 0.12

def build(total, events, out, seed=0, key=0):
    L, R = music(total, seed=seed, key=key)
    L *= 0.55; R *= 0.55
    sfx = {"whoosh": whoosh(), "pop": pop(), "pop2": pop(1.25), "ding": ding()}
    for t, k in events:
        s = int(t * SR); x = sfx[k]
        e = min(len(L), s + len(x))
        if s >= len(L): continue
        L[s:e] += x[:e - s]; R[s:e] += x[:e - s]
    st = np.stack([L, R], 1)
    st = st / max(1e-6, np.abs(st).max()) * 0.89
    w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()
