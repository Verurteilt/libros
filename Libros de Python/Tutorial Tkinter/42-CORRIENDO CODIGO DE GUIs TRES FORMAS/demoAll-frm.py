from Tkinter import *
from quitter import Quitter
demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)                      # import by name string
        part = module.Demo(root)                      # attach an instance
        part.config(bd=2, relief=GROOVE)
        part.pack(side=LEFT, fill=BOTH)
        parts.append(part)                            # change list in-place

def dumpState( ):
    for part in parts:                                # run demo report if any
        print part.__module__ + ':',
        if hasattr(part, 'report'):
            part.report( )
        else:
            print 'none'

root = Tk( )                                          # default toplevel window
Label(root, text='Multiple Frame demo', bg='white').pack( )
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(expand=YES, fill=X)
addComponents(root)
mainloop( )
