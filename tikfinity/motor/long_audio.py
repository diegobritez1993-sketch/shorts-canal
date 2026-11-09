from long import S, timeline
from audio import build
starts, total = timeline()
ev = []
for i, s in enumerate(S):
    t0 = starts[i]
    if i > 0: ev.append((t0 - 0.15, "whoosh"))
    if s["kind"] == "shot":
        for b in s["beats"]: ev.append((t0 + b["t"] + 0.05, "pop"))
    elif s["kind"] == "list":
        for k, tt in enumerate(s["times"]): ev.append((t0 + tt, "pop2" if k % 2 else "pop"))
    elif s["kind"] == "title":
        ev.append((t0 + 0.3, "ding"))
build(total, ev, "/home/claude/build/long_audio.wav", seed=0)
print("ok", total)
