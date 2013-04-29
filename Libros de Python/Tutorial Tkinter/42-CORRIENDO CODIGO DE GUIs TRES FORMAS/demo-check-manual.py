# check buttons, the hard way (without variables)

from Tkinter import *
states = []
def onPress(i):                        # keep track of states
    states[i] = not states[i]          # changes 0->1, 1->0

root = Tk( )
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)) )
    chk.pack(side=LEFT)
    states.append(0)
root.mainloop( )
print states                           # show all states on exit


