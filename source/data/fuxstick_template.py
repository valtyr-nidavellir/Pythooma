#valtyr
#get out of my code plz uwu
import playsound
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
from random import randint
from time import time

class ImageLabel(tk.Label):
    def load(self, im):
        self.winfo_toplevel().title("bwahahahahahaha")

        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
  
gifs=['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif','7.gif','8.gif','9.gif','10.gif','11.gif','12.gif','13.gif','14.gif','15.gif','16.gif']
sounds=['bwahahahaha','finalfant','shoop']
start=0
counter=0
while True:
    root = tk.Tk()
    ws = root.winfo_screenwidth()-100
    hs = root.winfo_screenheight()-100
    root.geometry("+"+str(randint(0,ws))+'+'+str(randint(0,hs)))
    for i in range(35+(counter*2)):
        window = tk.Toplevel()
        window.geometry("+"+str(randint(0,ws))+'+'+str(randint(0,hs)))
        lbl=ImageLabel(window)
        lbl.pack()
        if i==7:
            lbl.load('gifs/valtyr_gif.gif')
        else:
            lbl.load('gifs/'+str(gifs[randint(0,len(gifs)-1)]))
    if start==0:
        start=time()
        playsound.playsound('sounds/'+sounds[randint(0,len(sounds)-1)]+'.mp3',block=False)
    if start!=0:
        tmp=time()-start
        if tmp>=3600:
            start=0
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load('gifs/'+str(gifs[randint(0,len(gifs)-1)]))
    root.mainloop()
    counter=counter+1
