gifdir = 'C:\gifs\\'
from Tkinter import *
win = Tk( )
img = PhotoImage(file=gifdir+"ora-lp.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW)           # x, y coordinates
win.mainloop( )


