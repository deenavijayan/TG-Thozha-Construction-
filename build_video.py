# Builds images/construction/process.mp4 from stages/*.jpg (sorted by name). Needs: pip install pillow, and ffmpeg.
# Usage: python build_video.py [width=1280] [crf=26] [out=images/construction/process.mp4]
import sys,glob,subprocess,io
from PIL import Image
W=int(sys.argv[1]) if len(sys.argv)>1 else 1280
CRF=sys.argv[2] if len(sys.argv)>2 else "26"
OUT=sys.argv[3] if len(sys.argv)>3 else "images/construction/process.mp4"
H=W*9//16//2*2;FPS=24;N=FPS*9
im=[Image.open(f).convert("RGB").resize((W,H)) for f in sorted(glob.glob("stages/*.jpg"))];n=len(im)
p=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-","-c:v","libx264","-pix_fmt","yuv420p","-g","1","-crf",CRF,"-preset","fast","-movflags","+faststart",OUT],stdin=subprocess.PIPE)
sm=lambda x:x*x*(3-2*x)
for f in range(N):
    t=f/(N-1)*(n-1);fr=im[0].copy()
    for k in range(1,n):
        v=sm(min(1,max(0,(t-(k-1)-.15)/.7)))
        if v>0:
            h=int(H*v)
            if h>0: fr.paste(im[k].crop((0,H-h,W,H)),(0,H-h))
    z=1+.06*t/(n-1);cw,ch=W/z,H/z;fr=fr.crop((int((W-cw)/2),int((H-ch)/2),int((W+cw)/2),int((H+ch)/2))).resize((W,H))
    b=io.BytesIO();fr.save(b,"JPEG",quality=90);p.stdin.write(b.getvalue())
p.stdin.close();p.wait()
