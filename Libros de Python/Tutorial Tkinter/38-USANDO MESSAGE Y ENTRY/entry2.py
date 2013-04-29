# use Entry widgets directly and lay out by rows

from Tkinter import *
from quitter import Quitter
fields = 'Name', 'Job', 'Pay'

def fetch(entries):
    for entry in entries:
        print 'Input => "%s"' % entry.get( )          # get text

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)                           # make a new row
        lab = Label(row, width=5, text=field)       # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X)                  # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)    # grow horizontal
        entries.append(ent)
    return entries

if __name__ == '__main__':
    root = Tk( )
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch',
                 command= (lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop( )

