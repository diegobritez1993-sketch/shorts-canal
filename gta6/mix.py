import subprocess
from render import render, header, JOBS, OUT, STREAMER_X

import sys
SETS = {
 "5_mix": ("LA MISIÓN DEL TESORO DE GTA VI", "@AURONPLAY · @PERXITAA", [
    ("m1", "h2.mp4", "h", 0, 6), ("m2", "v1.mp4", "v", 6, 13), ("m3", "v2.mp4", "v", 3, 9),
    ("m4", "h1.mp4", "h", 8, 14), ("m5", "h2.mp4", "h", 19, 29)]),
 "d2_6_mix": ("LO MÁS LOCO DEL DÍA 2 EN GTA VI", " · ".join(x for x in ["@AURONPLAY", STREAMER_X] if x), [
    ("d1", "h8.mp4", "h", 20, 28), ("d2", "h7.mp4", "h", 18, 26), ("d3", "h6.mp4", "h", 9, 16),
    ("d4", "h5.mp4", "h", 18, 23), ("d5", "h9.mp4", "h", 30, 38)]),
 "8_mix": ("EN GTA VI NADIE ES NORMAL", "@AURONPLAY · @AXOZER", [
    ("n1", "h4.mp4", "h", 2, 13), ("n2", "h3.mp4", "h", 0, 6), ("n3", "h3.mp4", "h", 26, 37)]),
}
OUTNAME = sys.argv[1] if len(sys.argv) > 1 else "5_mix"
HOOK, CREDIT, segs = SETS[OUTNAME]
cams = {"h1.mp4": JOBS["3_lucia_jason"]["cam"], "h2.mp4": JOBS["4_doblones"]["cam"],
        "h3.mp4": JOBS["6_fieston"]["cam"], "h4.mp4": JOBS["7_robar_moto"]["cam"],
        "h5.mp4": JOBS["d2_2_sigilo"]["cam"], "h8.mp4": JOBS["d2_1_grulla"]["cam"], "h6.mp4": JOBS["d2_4_carcel"]["cam"],
        "h7.mp4": JOBS["d2_3_pelea"]["cam"], "h9.mp4": JOBS["d2_5_lucia"]["cam"]}
import os
for n, src, kind, ss, to in segs:
    if not os.path.exists(f"{OUT}/{n}.mp4"): render(n, src, kind, "", "", ss=ss, to=to, cam=cams.get(src), hdr=False, game="fit" if src in ("h3.mp4", "h6.mp4", "h7.mp4", "h9.mp4") else "crop")

dur = sum(to - ss for *_, ss, to in segs)
inputs = []
for n, *_ in segs:
    inputs += ["-i", f"{OUT}/{n}.mp4"]
k = len(segs)
fc = "".join(f"[{i}:v]setsar=1[s{i}];" for i in range(k)) + "".join(f"[s{i}][{i}:a]" for i in range(k)) + f"concat=n={k}:v=1:a=1[cv][ca];"
fc += "[cv]" + header(HOOK, CREDIT, dur) + "[v]"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[ca]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
                "-movflags", "+faststart", f"{OUT}/{OUTNAME}.mp4"], check=True)
for n, *_ in segs:
    import os; os.remove(f"{OUT}/{n}.mp4")
print("ok mix", dur)
