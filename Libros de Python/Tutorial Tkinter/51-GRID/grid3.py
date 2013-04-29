# add label and resizing

from Tkinter import *
colors = ['red',  'white',  'blue']

def gridbox(root):
    Label(root, text='Grid').grid(columnspan=2)
    r = 1
    for c in colors:
        l = Label(root, text=c, relief=RIDGE,  width=25)
        e = Entry(root, bg=c,   relief=SUNKEN, width=50)
        l.grid(row=r, column=0, sticky=NSEW)
        e.grid(row=r, column=1, sticky=NSEW)
        root.rowconfigure(r, weight=1)
        r = r+1
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

def packbox(root):
    Label(root, text='Pack').pack( )
    for c in colors:
        f = Frame(root)
        l = Label(f, text=c, relief=RIDGE,  width=25)
        e = Entry(f, bg=c,   relief=SUNKEN, width=50)
        f.pack(side=TOP,   expand=YES, fill=BOTH)
        l.pack(side=LEFT,  expand=YES, fill=BOTH)
        e.pack(side=RIGHT, expand=YES, fill=BOTH)

root = Tk( )
gridbox(Toplevel(root))
packbox(Toplevel(root))
Button(root, text='Quit', command=root.quit).pack( )
mainloop( )

