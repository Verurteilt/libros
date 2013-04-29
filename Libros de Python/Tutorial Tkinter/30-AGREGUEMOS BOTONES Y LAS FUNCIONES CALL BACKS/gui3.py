from Tkinter import *

def quit( ):                                  # a custom callback handler
    print 'Hello, I must be going...'          # kill windows and process
    import sys; sys.exit( )

widget = Button(None, text='Hello event world', command=quit)
widget.pack( )
widget.mainloop( )

