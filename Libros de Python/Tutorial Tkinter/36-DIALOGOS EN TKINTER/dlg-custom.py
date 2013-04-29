import sys
from Tkinter import *
makemodal = (len(sys.argv) > 1)

def dialog( ):
    win = Toplevel( )                                     # make a new window
    Label(win,  text='Hard drive reformatted!').pack( )   # add a few widgets
    Button(win, text='OK', command=win.destroy).pack( )   # set destroy callback
    if makemodal:
        win.focus_set( )          # take over input focus,
        win.grab_set( )           # disable other windows while I'm open,
        win.wait_window( )        # and wait here until win destroyed
    print 'dialog exit'            # else returns right away

root = Tk( )
Button(root, text='popup', command=dialog).pack( )
root.mainloop( )

