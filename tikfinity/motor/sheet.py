import sys, importlib
from PIL import Image
from engine import Scene, compose
mod = importlib.import_module(sys.argv[1]); out = sys.argv[2]
S = mod.S; W, H = mod.W, mod.H
starts, total = mod.timeline()
fr = []
for i, s in enumerate(S):
    ts = [b["t"] + 1.6 for b in s["beats"]] if s["kind"] == "shot" else [s["dur"] - 1.0]
    for t in ts: fr.append(compose(Scene(s), t, W, H, starts[i] + t, total, mod.LABEL))
sc = 0.25; tw, th = int(W*sc), int(H*sc); cols = 4
rows = (len(fr)+cols-1)//cols
sheet = Image.new("RGB", (cols*tw, rows*th), "black")
for k, f in enumerate(fr): sheet.paste(f.resize((tw, th)), ((k%cols)*tw, (k//cols)*th))
sheet.save(out); print(len(fr))
