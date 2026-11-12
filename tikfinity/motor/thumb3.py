from PIL import Image, ImageDraw
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((100,100,100+W,100+H)).copy()
src=source("faq.png").crop((720,400,2030,880)).resize((600,220))
card=Image.new("RGBA",(620,240),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(600,220,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,609,229),24,outline=ACC+(255,),width=6)
card=card.rotate(5,expand=True,resample=Image.BICUBIC)
bg.paste(card,(640,425),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="SOLUCIONES"
d.rounded_rectangle((60,50,60+bf.getlength(t)+40,110),18,fill=ACC);d.text((80,56),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,125),"¿TIKFINITY",font("title",120),TXT)
st((55,265),"NO ANDA?",font("title",120),ACC2)
st((60,420),"8 PROBLEMAS",font("title",60),TXT)
st((60,500),"RESUELTOS",font("title",60),TXT)
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_problemas.jpg",quality=92)
