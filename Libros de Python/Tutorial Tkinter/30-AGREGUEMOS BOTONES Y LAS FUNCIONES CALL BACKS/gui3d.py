from Tkinter import *

class HelloCallable:
    def __init__(self):                      # _ _init_ _ run on object creation
        self.msg = 'Hello _ _call_ _ world'
    def __call__(self):
        print self.msg                         # _ _call_ _ run later when called
        import sys; sys.exit( )               # class object looks like a function

widget = Button(None, text='Hello event world', command=HelloCallable( ))
widget.pack( )
widget.mainloop( )

