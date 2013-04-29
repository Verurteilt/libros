from Tkinter import *                # get base widget set
from glob import glob                # filename expansion list
import demoCheck                     # attach checkbutton demo to me
import random                        # pick a picture at random
gifdir = 'C:\gifs\\'                 # where to look for GIF files
 
 


def draw( ):
    name, photo = random.choice(images)
    lbl.config(text=name)
    pix.config(image=photo)

root=Tk( )
lbl = Label(root,  text="none", bg='blue', fg='red')
pix = Button(root, text="Press me", command=draw, bg='white')
lbl.pack(fill=BOTH)
pix.pack(pady=10)
demoCheck.Demo(root, relief=SUNKEN, bd=2).pack(fill=BOTH)

files = glob(gifdir + "*.gif")                              # GIFs for now
images = map((lambda x: (x, PhotoImage(file=x))), files)    # load and hold
print files
root.mainloop( )

