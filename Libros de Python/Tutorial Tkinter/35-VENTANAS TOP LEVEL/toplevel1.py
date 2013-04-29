import Tkinter
from Tkinter import Tk, Button
Tkinter.NoDefaultRoot( )

win1 = Tk( )         # two independent root windows
win2 = Tk( )

Button(win1, text='Spam', command=win1.destroy).pack( )
Button(win2, text='SPAM', command=win2.destroy).pack( )
win1.mainloop( )


