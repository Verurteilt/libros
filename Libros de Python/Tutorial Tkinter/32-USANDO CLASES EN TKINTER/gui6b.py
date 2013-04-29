from sys import exit
from Tkinter import *                    # get Tk widget classes
from gui6 import Hello                   # get the subframe class

parent = Frame(None)                     # make a container widget
parent.pack( )
Hello(parent).pack(side=RIGHT)           # attach Hello instead of running it

Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop( )

