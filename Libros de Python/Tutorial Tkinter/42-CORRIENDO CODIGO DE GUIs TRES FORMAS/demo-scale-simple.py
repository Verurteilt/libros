from Tkinter import *
root = Tk( )
scl = Scale(root, from_=-100, to=100, tickinterval=50, resolution=10)
scl.pack(expand=YES, fill=Y)
def report(): print scl.get( )
Button(root, text='state', command=report).pack(side=RIGHT)
root.mainloop( )

