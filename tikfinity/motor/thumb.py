from PIL import Image, ImageDraw, ImageFilter
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((100,100,100+W,100+H)).copy()
# captura de OBS/config a la derecha, inclinada
src=source("1793722140819_image.png").crop((700,380,2032,1160)).resize((700,410))
card=Image.new("RGBA",(720,430),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(700,410,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,709,419),24,outline=ACC+(255,),width=6)
card=card.rotate(-6,expand=True,resample=Image.BICUBIC)
sh=Image.new("RGBA",card.size,(0,0,0,0));sh.putalpha(card.getchannel("A").point(lambda v:int(v*0.6)))
sh=sh.filter(ImageFilter.GaussianBlur(20))
bg.paste((0,0,0),(560,190),sh);bg.paste(card,(540,170),card)
d=ImageDraw.Draw(bg)
# badge
bf=font("black",40);t="2026"
d.rounded_rectangle((60,60,60+bf.getlength(t)+40,120),18,fill=ACC);d.text((80,66),t,font=bf,fill="white")
def stroke_text(xy,txt,f,fill):
    d.text(xy,txt,font=f,fill=fill,stroke_width=8,stroke_fill=(8,8,12))
stroke_text((55,150),"TIKFINITY",font("title",128),TXT)
stroke_text((60,300),"CONFIGURACIÓN",font("title",76),ACC2)
stroke_text((60,390),"COMPLETA",font("title",76),ACC2)
# chips
y=520
for i,c in enumerate(["OBS","Minecraft","Puntos"]):
    f=font("bold",34);w=f.getlength(c)+44
    x=60+sum(font("bold",34).getlength(k)+64 for k in ["OBS","Minecraft","Puntos"][:i])
    d.rounded_rectangle((x,y,x+w,y+64),32,fill=(26,28,38),outline=(90,94,112),width=2)
    d.text((x+22,y+12),c,font=f,fill=TXT)
d.text((62,620),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_configuracion_completa.jpg",quality=92)
