# add equivalent pack window

from Tkinter import *
colors = ['red', 'green', 'yellow', 'orange', 'blue', 'navy']

def gridbox(parent):
    r = 0
    for c in colors:
        l = Label(parent, text=c, relief=RIDGE,  width=25)
        e = Entry(parent, bg=c,   relief=SUNKEN, width=50)
        l.grid(row=r, column=0)
        e.grid(row=r, column=1)
        r = r+1

def packbox(parent):
    for c in colors:
        f = Frame(parent)
        l = Label(f, text=c, relief=RIDGE,  width=25)
        e = Entry(f, bg=c,   relief=SUNKEN, width=50)
        f.pack(side=TOP)
        l.pack(side=LEFT)
        e.pack(side=RIGHT)

if __name__ == '__main__':
    root = Tk( )
    gridbox(Toplevel( ))
    packbox(Toplevel( ))
    Button(root, text='Quit', command=root.quit).pack( )
    mainloop( )


