############################################################################
# implement a GUI for viewing/updating class instances stored in a shelve;
# the shelve lives on machine this script runs on, as 1 or more local files
############################################################################

from Tkinter import *
from tkMessageBox import showerror
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets( ):
    global entries
    window = Tk( )
    window.title('People Shelve')
    form   = Frame(window)
    labels = Frame(form)
    values = Frame(form)
    labels.pack(side=LEFT)
    values.pack(side=RIGHT)
    form.pack( )
    entries = {}
    for label in ('key',) + fieldnames:
        Label(labels, text=label).pack( )
        ent = Entry(values)
        ent.pack( )
        entries[label] = ent
    Button(window, text="Fetch",  command=fetchRecord).pack(side=LEFT)
    Button(window, text="Update", command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit",   command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord( ):
    key = entries['key'].get( )
    try:
        record = db[key]                      # fetch by key, show in GUI
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord( ):
    key = entries['key'].get( )
    if key in db.keys( ):
        record = db[key]                      # update existing record
    else:
        from person import Person             # make/store new one for key
        record = Person(name='?', age='?')    # eval: strings must be quoted
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get( )))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets( )
window.mainloop( )
db.close( ) # back here after quit or window close


