import subprocess, sys, os

ANTON = "/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
ARCH = "/usr/share/fonts/truetype/google-fonts/ofl/archivoblack/ArchivoBlack-Regular.ttf"
Y = "0xFFD400"
SRC = "/home/claude/work/src"
OUT = "/home/claude/work/out"
os.makedirs(OUT, exist_ok=True)

def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace("%", "\\%")

def header(hook, credit, dur):
    size = 76 if len(hook) <= 26 else max(54, int(76 * 26 / len(hook)))
    f = [
        "drawbox=x=0:y=0:w=1080:h=210:color=0x0E0E10:t=fill",
        f"drawbox=x=0:y=0:w='1080*t/{dur}':h=10:color={Y}:t=fill",
        f"drawtext=fontfile={ARCH}:text='GTA VI CLIPS · CASTELLANO':fontsize=30:fontcolor={Y}:x=40:y=34",
        f"drawtext=fontfile={ANTON}:text='{esc(hook)}':fontsize={size}:fontcolor=white:x=(w-text_w)/2:y=88+(96-{size})/2",
    ]
    cta = f"enable='gte(t,{dur}-4)'"
    f.append(f"drawbox=x=90:y=1530:w=900:h=120:color={Y}:t=fill:{cta}")
    f.append(f"drawtext=fontfile={ANTON}:text='SUSCRÍBETE PARA TODO SOBRE GTA VI':fontsize=60:fontcolor=0x0E0E10:x=(w-text_w)/2:y=1530+(120-text_h)/2:{cta}")
    if credit:
        f.append(f"drawtext=fontfile={ARCH}:text='{esc(credit)}':fontsize=26:fontcolor=0xBBBBBB:x=w-text_w-40:y=38")
    return ",".join(f)

def render(name, src, kind, hook, credit, ss=0, to=None, cam=None, hdr=True, game="crop"):
    dur = (to or 30) - ss
    if kind == "v":
        fc = (f"[0:v]split[a][b];"
              f"[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.25[bg];"
              f"[b]scale=-2:1710[fg];"
              f"[bg][fg]overlay=(W-w)/2:210,")
    else:
        cx, cy, cw, ch = cam
        fc = (f"[0:v]split=3[a][b][c];"
              f"[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:2,eq=brightness=-0.3[bg];"
              f"[b]crop={cw}:{ch}:{cx}:{cy},scale=-2:620[cam];"
              + (f"[c]scale=-2:860,crop=1080:860[game];" if game == "crop" else f"[c]scale=1080:-2[game];") +
              f"[bg][cam]overlay=(W-w)/2:240[t1];[t1][game]overlay=0:870,")
    fc += (header(hook, credit, dur) + "," if hdr else "") + "fps=30,format=yuv420p[v];[0:a]loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(ss)]
    if to: cmd += ["-to", str(to)]
    cmd += ["-i", f"{SRC}/{src}", "-filter_complex", fc, "-map", "[v]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-ar", "48000",
            "-movflags", "+faststart", f"{OUT}/{name}.mp4"]
    subprocess.run(cmd, check=True)
    print("ok", name)

JOBS = {
 "1_buceo": dict(src="v1.mp4", kind="v", hook="ALGO SALE MAL BUCEANDO EN GTA VI", credit="@AURONPLAY"),
 "2_tesoro": dict(src="v2.mp4", kind="v", hook="¿HAY TESOROS BAJO EL MAR?", credit="@AURONPLAY", to=18),
 "3_lucia_jason": dict(src="h1.mp4", kind="h", hook="LUCÍA Y JASON HABLAN DE CAL (SPOILER)", credit="@PERXITAA", cam=(1897, 0, 663, 371)),
 "4_doblones": dict(src="h2.mp4", kind="h", hook="¡ENCONTRARON DOBLONES ESPAÑOLES!", credit="@AURONPLAY", cam=(10, 380, 356, 375)),
 "6_fieston": dict(src="h3.mp4", kind="h", hook="DUNK LA LÍA... Y QUIERE MONTAR UN FIESTÓN", credit="@AXOZER", to=37, cam=(1495, 100, 415, 370), game="fit"),
 "7_robar_moto": dict(src="h4.mp4", kind="h", hook="TE PIDE ROBAR UNA MOTO \"POR SU BIEN\"", credit="@AURONPLAY", cam=(10, 380, 356, 375)),
}
if __name__ == "__main__":
    for n in (sys.argv[1:] or JOBS):
        render(n, **JOBS[n])
