from Tkinter import *
from sys import stdout, exit                 # lambda generates a function

widget = Button(None,                        # but contains just an expression
             text='Hello event world',
             command=(lambda: stdout.write('Hello lambda world\n') or exit( )) )

widget.pack( )
widget.mainloop( )

