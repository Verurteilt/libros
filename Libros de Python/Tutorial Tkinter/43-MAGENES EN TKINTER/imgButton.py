gifdir = 'C:\gifs\\'
from Tkinter import *
win = Tk( )
igm = PhotoImage(file=gifdir+"ora-pp.gif")
Button(win, image=igm).pack( )
win.mainloop( )

