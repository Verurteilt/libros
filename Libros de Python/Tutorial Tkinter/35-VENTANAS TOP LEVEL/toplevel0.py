import sys
from Tkinter import Toplevel, Button, Label

win1 = Toplevel( )                  # two independent windows
win2 = Toplevel( )                  # but part of same process

Button(win1, text='Spam', command=sys.exit).pack( )
Button(win2, text='SPAM', command=sys.exit).pack( )

Label(text='Popups').pack()          # on default Tk( ) root window
win2.mainloop( )

