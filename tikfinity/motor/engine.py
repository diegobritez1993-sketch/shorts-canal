import math, subprocess, os, sys, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FPS = 30
B = os.path.dirname(os.path.abspath(__file__))
INTER = "/usr/share/fonts/opentype/inter/"
POP = "/usr/share/fonts/truetype/google-fonts/"
ACC = (255, 45, 85)      # rojo/rosa TikFinity
ACC2 = (37, 244, 238)    # cian TikTok
TXT = (240, 242, 248)
SUB = (160, 166, 182)
CROP = (0, 84, 1016, 712)  # recorta barra del navegador y de Windows
SW, SH = CROP[2] - CROP[0], CROP[3] - CROP[1]

_fc = {}
def font(name, size):
    k = (name, size)
    if k not in _fc:
        path = {"title": POP + "Poppins-Bold.ttf", "body": INTER + "Inter-SemiBold.otf",
                "med": INTER + "Inter-Medium.otf", "black": INTER + "Inter-Black.otf",
                "bold": INTER + "Inter-Bold.otf"}[name]
        _fc[k] = ImageFont.truetype(path, size)
    return _fc[k]

def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def ease_out(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3

def wrap(text, f, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if f.getlength(test) <= width:
            cur = test
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

_src = {}
def source(name):
    if name not in _src:
        im = Image.open(os.path.join(B, name)).convert("RGB").crop(CROP)
        _src[name] = im.resize((SW * 2, SH * 2), Image.LANCZOS)
    return _src[name]

_bg = {}
def background(W, H):
    if (W, H) not in _bg:
        bw, bh = W + 200, H + 200
        bg = Image.new("RGB", (bw, bh), (12, 13, 19))
        glow = Image.new("RGB", (bw, bh), (0, 0, 0))
        d = ImageDraw.Draw(glow)
        d.ellipse((-200, -250, bw * 0.55, bh * 0.6), fill=(70, 12, 30))
        d.ellipse((bw * 0.55, bh * 0.45, bw + 300, bh + 300), fill=(8, 55, 60))
        glow = glow.filter(ImageFilter.GaussianBlur(220))
        bg = Image.blend(bg, glow, 0.6)
        # puntos de grilla sutiles
        d = ImageDraw.Draw(bg)
        for x in range(0, bw, 48):
            for y in range(0, bh, 48):
                d.point((x, y), fill=(40, 42, 54))
        _bg[(W, H)] = bg
    return _bg[(W, H)]

def rounded_mask(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255)
    return m

_tc = {}
def text_img(text, fname, size, color, width):
    k = (text, fname, size, color, width)
    if k not in _tc:
        f = font(fname, size)
        lines = wrap(text, f, width)
        lh = int(size * 1.28)
        im = Image.new("RGBA", (width + 10, lh * len(lines) + 10), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        for i, l in enumerate(lines):
            d.text((0, i * lh), l, font=f, fill=color)
        _tc[k] = im
    return _tc[k]

def fade(im, a):
    if a >= 0.999: return im
    r = im.copy()
    al = r.getchannel("A").point(lambda v: int(v * a))
    r.putalpha(al)
    return r

def cam_for_box(box):
    x0, y0, x1, y1 = box
    y0 -= CROP[1]; y1 -= CROP[1]
    bw, bh = x1 - x0, y1 - y0
    z = 0.62 * min(SW / bw, SH / bh)
    z = max(1.15, min(2.1, z))
    return ((x0 + x1) / 2, (y0 + y1) / 2, z)

def clamp_cam(c, ar):
    cx, cy, z = c
    vw = SW / z
    vh = vw / ar
    if vh > SH:
        vh = SH; vw = vh * ar
    cx = min(max(cx, vw / 2), SW - vw / 2)
    cy = min(max(cy, vh / 2), SH - vh / 2)
    return cx, cy, vw, vh

def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(len(a)))

def render_card(src, cam, box, t_box, cw, ch, pulse):
    ar = cw / ch
    cx, cy, vw, vh = clamp_cam(cam, ar)
    s = 2
    region = (int((cx - vw / 2) * s), int((cy - vh / 2) * s), int((cx + vw / 2) * s), int((cy + vh / 2) * s))
    card = src.crop(region).resize((cw, ch), Image.BICUBIC)
    if box is not None and t_box > 0:
        a = ease(t_box / 0.5)
        x0, y0, x1, y1 = box
        y0 -= CROP[1]; y1 -= CROP[1]
        def m(px, py):
            return ((px - (cx - vw / 2)) / vw * cw, (py - (cy - vh / 2)) / vh * ch)
        p0 = m(x0 - 8, y0 - 8); p1 = m(x1 + 8, y1 + 8)
        ov = Image.new("RGBA", (cw, ch), (5, 6, 10, int(150 * a)))
        md = ImageDraw.Draw(ov)
        md.rounded_rectangle((p0[0], p0[1], p1[0], p1[1]), 14, fill=(0, 0, 0, 0))
        card = card.convert("RGBA")
        card.alpha_composite(ov)
        d = ImageDraw.Draw(card)
        g = 6 + 6 * (0.5 + 0.5 * math.sin(pulse * 5))
        d.rounded_rectangle((p0[0] - g, p0[1] - g, p1[0] + g, p1[1] + g), 18,
                            outline=(ACC[0], ACC[1], ACC[2], int(90 * a)), width=3)
        d.rounded_rectangle((p0[0], p0[1], p1[0], p1[1]), 14,
                            outline=(ACC[0], ACC[1], ACC[2], int(255 * a)), width=5)
        card = card.convert("RGB")
    return card


class Scene:
    """kind: 'shot' (captura + panel), 'title', 'list', 'outro'"""
    def __init__(self, d):
        self.__dict__.update(d)


def draw_header(fr, W, H, t_global, total, label, vertical):
    d = ImageDraw.Draw(fr)
    if vertical:
        d.text((60, 70), "MISTER DI", font=font("black", 34), fill=TXT)
        d.text((60, 112), label, font=font("med", 26), fill=SUB)
    else:
        d.text((70, 44), "MISTER DI", font=font("black", 30), fill=TXT)
        lw = font("black", 30).getlength("MISTER DI")
        d.text((70 + lw + 22, 49), label, font=font("med", 24), fill=SUB)
    # barra de progreso
    p = t_global / total
    y = H - 10
    d.rectangle((0, y, W, H), fill=(30, 32, 42))
    d.rectangle((0, y, int(W * p), H), fill=ACC)


def compose(sc, t, W, H, t_global, total, label):
    vertical = H > W
    bg = background(W, H)
    ox = int(100 + 60 * math.sin(t_global * 0.05))
    oy = int(100 + 40 * math.cos(t_global * 0.04))
    fr = bg.crop((ox, oy, ox + W, oy + H)).copy()
    k = sc.kind
    if k == "shot":
        compose_shot(fr, sc, t, W, H, vertical)
    elif k == "title":
        compose_title(fr, sc, t, W, H, vertical)
    elif k == "list":
        compose_list(fr, sc, t, W, H, vertical)
    if k != "title":
        draw_header(fr, W, H, t_global, total, label, vertical)
    # fundido entre escenas
    fi = getattr(sc, "fade_in", 0.35); fo = getattr(sc, "fade_out", 0.35)
    a = min(1.0, t / fi if fi else 1.0, (sc.dur - t) / fo if fo else 1.0)
    if a < 1.0:
        fr = Image.blend(Image.new("RGB", (W, H), (12, 13, 19)), fr, max(0.0, a))
    return fr


def beat_index(sc, t):
    i = -1
    for j, b in enumerate(sc.beats):
        if t >= b["t"]: i = j
    return i


def compose_shot(fr, sc, t, W, H, vertical):
    src = source(sc.img)
    if vertical:
        cw, ch = W - 80, W - 220
        cx0, cy0 = 40, 230
        px, py, pw = 70, cy0 + ch + 70, W - 140
    else:
        cw, ch = 1180, 730
        left = getattr(sc, "flip", False)
        cx0 = 70 if not left else W - 70 - cw
        cy0 = 170
        px = cx0 + cw + 70 if not left else 70
        py, pw = 170, W - cw - 70 * 3
    # entrada de la tarjeta
    ein = ease_out(t / 0.7)
    dy = int((1 - ein) * 60)
    # cámara
    full = (SW / 2, SH / 2, 1.0)
    bi = beat_index(sc, t)
    cams = [cam_for_box(b["box"]) if b.get("box") else full for b in sc.beats]
    if bi < 0:
        cam = full; box = None; tb = 0
    else:
        prev = cams[bi - 1] if bi > 0 else full
        tt = (t - sc.beats[bi]["t"]) / 0.9
        same = bi > 0 and sc.beats[bi].get("box") == sc.beats[bi - 1].get("box")
        cam = cams[bi] if same else lerp(prev, cams[bi], ease(tt))
        box = sc.beats[bi].get("box")
        # el recuadro aparece al terminar el movimiento (o se mantiene si es igual)
        tb = 1.0 if same else (t - sc.beats[bi]["t"] - 0.6)
    if vertical:
        cam = (cam[0], cam[1], cam[2] * (1.0 + 0.4 * min(1.0, (cam[2] - 1.0) / 0.3)))
    card = render_card(src, cam, box, tb, cw, ch, t)
    # sombra + borde
    if (cw, ch) not in _shadow:
        s_ = Image.new("RGBA", (cw + 80, ch + 80), (0, 0, 0, 0))
        ImageDraw.Draw(s_).rounded_rectangle((40, 50, cw + 40, ch + 50), 26, fill=(0, 0, 0, 150))
        _shadow[(cw, ch)] = s_.filter(ImageFilter.GaussianBlur(18))
    sh = _shadow[(cw, ch)]
    fr.paste(sh, (cx0 - 40, cy0 - 40 + dy), sh)
    fr.paste(card, (cx0, cy0 + dy), rounded_mask_cached(cw, ch, 22))
    ImageDraw.Draw(fr).rounded_rectangle((cx0, cy0 + dy, cx0 + cw - 1, cy0 + ch - 1 + dy), 22,
                                         outline=(60, 63, 80), width=2)
    # panel de texto
    d = ImageDraw.Draw(fr)
    a0 = ease_out((t - 0.2) / 0.5)
    y = py
    if getattr(sc, "badge", None):
        bf = font("bold", 26 if not vertical else 30)
        bw = int(bf.getlength(sc.badge)) + 36
        badge = Image.new("RGBA", (bw, 46), (0, 0, 0, 0))
        ImageDraw.Draw(badge).rounded_rectangle((0, 0, bw - 1, 45), 23, fill=ACC + (255,))
        ImageDraw.Draw(badge).text((18, 8), sc.badge, font=bf, fill=(255, 255, 255))
        fr.paste(badge, (px - int((1 - a0) * 30), y), fade(badge, a0))
        y += 70
    ts = 54 if not vertical else 60
    ti = text_img(sc.title, "title", ts, TXT, pw)
    fr.paste(ti, (px - int((1 - a0) * 30), y), fade(ti, a0))
    y += ti.size[1] + 24
    d.rectangle((px, y, px + 90, y + 5), fill=ACC2)
    y += 38
    bs = 33 if not vertical else 44
    gap = 18 if not vertical else 26
    limit = H - 70 if not vertical else H - 110
    while bs > 24:
        hsum = sum(text_img(b["text"], "body", bs, TXT, pw - 40).size[1] + gap for b in sc.beats if b.get("text"))
        if y + hsum <= limit: break
        bs -= 1
    for j, b in enumerate(sc.beats):
        if not b.get("text"): continue
        lt = t - b["t"]
        if lt < 0: break
        a = ease_out(lt / 0.45)
        im = text_img(b["text"], "body", bs, TXT if j == bi else (196, 200, 214), pw - 40)
        dot = ACC if j == bi else (90, 94, 112)
        d.ellipse((px - int((1 - a) * 40), y + 12, px + 14 - int((1 - a) * 40), y + 26), fill=dot)
        fr.paste(im, (px + 32 - int((1 - a) * 40), y), fade(im, a))
        y += im.size[1] + (18 if not vertical else 26)


_rm = {}
_shadow = {}
def rounded_mask_cached(w, h, r):
    if (w, h, r) not in _rm: _rm[(w, h, r)] = rounded_mask(w, h, r)
    return _rm[(w, h, r)]


def compose_title(fr, sc, t, W, H, vertical):
    d = ImageDraw.Draw(fr)
    cx = W // 2
    a = ease_out(t / 0.8)
    kick = sc.kicker
    kf = font("bold", 34 if not vertical else 42)
    kw = kf.getlength(kick)
    ky = int(H * 0.30 if not vertical else H * 0.34)
    pill = Image.new("RGBA", (int(kw) + 50, 62), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((0, 0, int(kw) + 49, 61), 31, fill=ACC + (255,))
    ImageDraw.Draw(pill).text((25, 10), kick, font=kf, fill=(255, 255, 255))
    fr.paste(pill, (int(cx - pill.size[0] / 2), ky - int((1 - a) * 40)), fade(pill, a))
    tw = W - 240
    ts = 96 if not vertical else 104
    for i, line in enumerate(sc.lines):
        la = ease_out((t - 0.3 - i * 0.25) / 0.6)
        if la <= 0: continue
        f = font("title", ts)
        col = TXT if i == 0 else ACC2
        im = Image.new("RGBA", (int(f.getlength(line)) + 20, int(ts * 1.4)), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), line, font=f, fill=col)
        sc_ = 0.85 + 0.15 * la
        im2 = im.resize((max(1, int(im.size[0] * sc_)), max(1, int(im.size[1] * sc_))), Image.BICUBIC)
        y = ky + 110 + i * int(ts * 1.2)
        fr.paste(im2, (int(cx - im2.size[0] / 2), y), fade(im2, la))
    if getattr(sc, "sub", None):
        sa = ease_out((t - 1.0) / 0.6)
        sf = font("med", 36 if not vertical else 40)
        y = ky + 110 + len(sc.lines) * int(ts * 1.2) + 30
        for ln in wrap(sc.sub, sf, 1400 if not vertical else W - 160):
            im = Image.new("RGBA", (int(sf.getlength(ln)) + 10, int(sf.size * 1.4)), (0, 0, 0, 0))
            ImageDraw.Draw(im).text((0, 0), ln, font=sf, fill=SUB)
            fr.paste(im, (int(cx - im.size[0] / 2 + 5), y), fade(im, sa))
            y += int(sf.size * 1.3)


def compose_list(fr, sc, t, W, H, vertical):
    d = ImageDraw.Draw(fr)
    x = 160 if not vertical else 80
    a0 = ease_out(t / 0.5)
    ti = text_img(sc.title, "title", 64 if not vertical else 72, TXT, W - 2 * x)
    cols = getattr(sc, "cols", 2 if not vertical else 1)
    colw = (W - 2 * x) // cols
    rowh = 130 if not vertical else 150
    nrows = (len(sc.items) + cols - 1) // cols
    y = max(150, (H - (ti.size[1] + 40 + nrows * rowh)) // 2)
    fr.paste(ti, (x, y), fade(ti, a0))
    y += ti.size[1] + 40
    for i, (item, tt) in enumerate(zip(sc.items, sc.times)):
        lt = t - tt
        if lt < 0: continue
        a = ease_out(lt / 0.45)
        c, r = (i % cols, i // cols) if cols > 1 else (0, i)
        bx = x + c * colw - int((1 - a) * 40)
        by = y + r * rowh
        box = Image.new("RGBA", (colw - 40, rowh - 24), (0, 0, 0, 0))
        bd = ImageDraw.Draw(box)
        bd.rounded_rectangle((0, 0, colw - 41, rowh - 25), 20, fill=(26, 28, 38, 235), outline=(60, 63, 80, 255), width=2)
        num = sc.marks[i] if getattr(sc, "marks", None) else str(i + 1)
        bd.rounded_rectangle((22, (rowh - 24) // 2 - 30, 82, (rowh - 24) // 2 + 30), 16, fill=ACC + (255,))
        nf = font("black", 32)
        bd.text((52 - nf.getlength(num) / 2, (rowh - 24) // 2 - 21), num, font=nf, fill=(255, 255, 255))
        ti2 = text_img(item, "body", 36 if not vertical else 40, TXT, colw - 180)
        box.alpha_composite(ti2, (108, max(0, ((rowh - 24) - ti2.size[1]) // 2 + 4)))
        fr.paste(box, (bx, by), fade(box, a))


def render_scene(sc, W, H, t0, total, label, out):
    tmp = out + ".part.mp4"
    n = int(round(sc.dur * FPS))
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "20",
                          "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp],
                         stdin=subprocess.PIPE)
    for i in range(n):
        t = i / FPS
        fr = compose(sc, t, W, H, t0 + t, total, label)
        p.stdin.write(fr.tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, out)
    else:
        raise SystemExit("ffmpeg failed " + out)
