# can fetch values after destroy with stringvars

from Tkinter import *
from entry3 import makeform, fetch, fields

def show(variables):
    popup.destroy( )                    # order doesn't matter here
    fetch(variables)                # variables live on after window destroyed

def ask( ):
    global popup
    popup = Toplevel( )              # show form in modal dialog window
    vars = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(vars)) ).pack( )
    popup.grab_set( )
    popup.focus_set( )
    popup.wait_window( )             # wait for destroy here

root = Tk( )
Button(root, text='Dialog', command=ask).pack( )
root.mainloop( )

