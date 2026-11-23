from PIL import Image, ImageDraw
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((240,40,240+W,40+H)).copy()
src=source("1793722134762_image.png").crop((700,560,1900,1130)).resize((580,276))
card=Image.new("RGBA",(600,296),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(580,276,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,589,285),24,outline=ACC+(255,),width=7)
card=card.rotate(4,expand=True,resample=Image.BICUBIC)
bg.paste(card,(650,330),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="TIKFINITY 2026"
d.rounded_rectangle((60,50,60+bf.getlength(t)+40,110),18,fill=ACC);d.text((80,56),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,125),"PUNTOS",font("title",130),TXT)
st((55,270),"Y NIVELES",font("title",104),ACC2)
st((60,430),"QUE TU PÚBLICO",font("title",54),TXT)
st((60,500),"VUELVA",font("title",54),TXT)
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_puntos_niveles.jpg",quality=92)
