from PIL import Image, ImageDraw
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((160,60,160+W,60+H)).copy()
src=source("shares.png").crop((150,300,640,1300)).resize((330,674))
src=src.crop((0,0,330,520))
card=Image.new("RGBA",(350,540),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(330,520,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,339,529),24,outline=ACC+(255,),width=7)
card=card.rotate(-4,expand=True,resample=Image.BICUBIC)
bg.paste(card,(860,110),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="TIKFINITY 2026"
d.rounded_rectangle((60,50,60+bf.getlength(t)+40,110),18,fill=ACC);d.text((80,56),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,125),"GRATIS",font("title",140),TXT)
st((55,285),"VS PRO",font("title",140),ACC2)
st((60,460),"¿TENÉS QUE PAGAR?",font("title",56),TXT)
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_gratis_vs_pro.jpg",quality=92)
