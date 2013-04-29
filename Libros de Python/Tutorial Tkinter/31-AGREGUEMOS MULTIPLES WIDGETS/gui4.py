from Tkinter import *

def greeting( ):
    print 'Hello stdout world!...'

win = Frame( )
win.pack(expand=YES, fill=BOTH)

Label(win,  text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit',  command=win.quit).pack(side=RIGHT)

win.mainloop( )

