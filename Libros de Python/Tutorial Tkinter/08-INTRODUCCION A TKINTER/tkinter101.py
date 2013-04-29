from Tkinter import *
from tkMessageBox import showinfo

def reply( ):
    showinfo(title='popup', message='Button pressed!')

window = Tk( )
Button(window, text='press', command=reply).pack( )
window.mainloop( )

