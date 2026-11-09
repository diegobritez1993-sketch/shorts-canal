from PIL import Image, ImageDraw, ImageFilter
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((100,100,100+W,100+H)).copy()
src=source("follows.png").crop((700,560,2032,1120)).resize((700,294))
card=Image.new("RGBA",(720,314),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(700,294,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,709,303),24,outline=ACC+(255,),width=6)
card=card.rotate(-6,expand=True,resample=Image.BICUBIC)
bg.paste(card,(560,230),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="2026"
d.rounded_rectangle((60,60,60+bf.getlength(t)+40,120),18,fill=ACC);d.text((80,66),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,150),"METAS",font("title",150),TXT)
st((60,330),"EN TU LIVE",font("title",80),ACC2)
st((60,430),"TIKFINITY",font("title",64),TXT)
x=60
for c in ["Likes","Follows","Sorteos"]:
    f=font("bold",34);w=f.getlength(c)+44
    d.rounded_rectangle((x,540,x+w,604),32,fill=(26,28,38),outline=(90,94,112),width=2);d.text((x+22,552),c,font=f,fill=TXT);x+=w+20
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_metas.jpg",quality=92)
