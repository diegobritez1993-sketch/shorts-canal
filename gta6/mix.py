import subprocess
from render import render, header, JOBS, OUT

segs = [
    ("m1", "h2.mp4", "h", 0, 6),
    ("m2", "v1.mp4", "v", 6, 13),
    ("m3", "v2.mp4", "v", 3, 9),
    ("m4", "h1.mp4", "h", 8, 14),
    ("m5", "h2.mp4", "h", 19, 29),
]
cams = {"h1.mp4": JOBS["3_lucia_jason"]["cam"], "h2.mp4": JOBS["4_doblones"]["cam"]}
import os
for n, src, kind, ss, to in segs:
    if not os.path.exists(f"{OUT}/{n}.mp4"): render(n, src, kind, "", "", ss=ss, to=to, cam=cams.get(src), hdr=False)

dur = sum(to - ss for *_, ss, to in segs)
inputs = []
for n, *_ in segs:
    inputs += ["-i", f"{OUT}/{n}.mp4"]
k = len(segs)
fc = "".join(f"[{i}:v]setsar=1[s{i}];" for i in range(k)) + "".join(f"[s{i}][{i}:a]" for i in range(k)) + f"concat=n={k}:v=1:a=1[cv][ca];"
fc += "[cv]" + header("LA MISIÓN DEL TESORO DE GTA VI", "@AURONPLAY · @PERXITAA", dur) + "[v]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[ca]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                "-movflags", "+faststart", f"{OUT}/5_mix.mp4"], check=True)
for n, *_ in segs:
    import os; os.remove(f"{OUT}/{n}.mp4")
print("ok mix", dur)
