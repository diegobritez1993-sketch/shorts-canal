from PIL import Image, ImageDraw
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((160,60,160+W,60+H)).copy()
src=source("transacciones.png").crop((660,436,1976,972)).resize((600,244))
card=Image.new("RGBA",(620,264),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(600,244,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,609,253),24,outline=ACC2+(255,),width=6)
card=card.rotate(-4,expand=True,resample=Image.BICUBIC)
bg.paste(card,(630,395),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="IDEAS PARA TU LIVE"
d.rounded_rectangle((60,50,60+bf.getlength(t)+40,110),18,fill=ACC);d.text((80,56),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,125),"5 IDEAS",font("title",130),TXT)
st((55,270),"INTERACTIVAS",font("title",96),ACC2)
st((60,420),"QUE TU PÚBLICO",font("title",54),TXT)
st((60,490),"JUEGUE CON VOS",font("title",54),TXT)
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_ideas.jpg",quality=92)
