from Tkinter import *
root = Tk( )
var1 = StringVar( )
var2 = StringVar( )
opt1 = OptionMenu(root, var1, 'spam', 'eggs',  'toast')     # like Menubutton
opt2 = OptionMenu(root, var2, 'ham',  'bacon', 'sausage')   # but shows choice
opt1.pack(fill=X)
opt2.pack(fill=X)
var1.set('spam')
var2.set('ham')
def state(): print var1.get(), var2.get( )                   # linked variables
Button(root, command=state, text='state').pack( )
root.mainloop( )


