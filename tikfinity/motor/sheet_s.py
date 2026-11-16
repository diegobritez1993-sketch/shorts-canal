import sys
from PIL import Image
from engine import Scene, compose
import shorts4, shorts
fr=[]
for n in sys.argv[1:]:
    label,S=shorts.SHORTS[n]; st=0; tot=sum(s["dur"] for s in S)
    for s in S:
        ts=[b["t"]+1.5 for b in s["beats"]] if s["kind"]=="shot" else [s["dur"]-0.8]
        for t in ts: fr.append(compose(Scene(s),t,1080,1920,st+t,tot,label))
        st+=s["dur"]
tw,th=270,480;cols=6;rows=(len(fr)+cols-1)//cols
o=Image.new("RGB",(cols*tw,rows*th))
for k,f in enumerate(fr): o.paste(f.resize((tw,th)),((k%cols)*tw,(k//cols)*th))
o.save("chk/s_sheet.png");print(len(fr))
