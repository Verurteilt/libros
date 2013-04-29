from Tkinter import *

def hello(event):
    print 'Press twice to exit'              # on single-left click

def quit(event):                             # on double-left click
    print 'Hello, I must be going...'        # event gives widget, x/y, etc.
    import sys; sys.exit( )

widget = Button(None, text='Hello event world')
widget.pack( )
widget.bind('<Button-1>', hello)             # bind left mouse clicks
widget.bind('<Double-1>', quit)              # bind double-left clicks
widget.mainloop( )


