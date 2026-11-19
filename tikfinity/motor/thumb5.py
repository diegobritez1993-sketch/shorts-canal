from PIL import Image, ImageDraw
from engine import font, source, background, ACC, ACC2, TXT, rounded_mask
W,H=1280,720
bg=background(W,H).crop((200,90,200+W,90+H)).copy()
src=source("1793722108699_image.png").crop((600,250,1720,990)).resize((560,370))
card=Image.new("RGBA",(580,390),(0,0,0,0))
card.paste(src,(10,10),rounded_mask(560,370,24))
ImageDraw.Draw(card).rounded_rectangle((10,10,569,379),24,outline=ACC+(255,),width=7)
card=card.rotate(5,expand=True,resample=Image.BICUBIC)
bg.paste(card,(660,250),card)
d=ImageDraw.Draw(bg)
bf=font("black",40);t="ERRORES COMUNES"
d.rounded_rectangle((60,50,60+bf.getlength(t)+40,110),18,fill=ACC);d.text((80,56),t,font=bf,fill="white")
st=lambda xy,s,f,c:d.text(xy,s,font=f,fill=c,stroke_width=8,stroke_fill=(8,8,12))
st((55,125),"8 ERRORES",font("title",124),TXT)
st((55,265),"QUE ARRUINAN",font("title",78),ACC2)
st((55,365),"TU LIVE",font("title",78),ACC2)
st((60,500),"TIKFINITY 2026",font("title",50),TXT)
d.text((62,630),"MISTER DI",font=font("black",36),fill=(200,204,216))
bg.save("/home/claude/out/miniatura_errores.jpg",quality=92)
