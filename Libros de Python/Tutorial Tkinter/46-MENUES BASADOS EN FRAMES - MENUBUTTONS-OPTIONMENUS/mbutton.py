from Tkinter import *
root    = Tk( )
mbutton = Menubutton(root, text='Food')     # the pull-down stands alone
picks   = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='spam',  command=root.quit)
picks.add_command(label='eggs',  command=root.quit)
picks.add_command(label='bacon', command=root.quit)
mbutton.pack( )
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop( )

