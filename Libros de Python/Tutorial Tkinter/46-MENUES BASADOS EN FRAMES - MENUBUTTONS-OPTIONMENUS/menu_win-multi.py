from menu_win import makemenu
from Tkinter import *

root = Tk( )
for i in range(3):                  # Three pop-up windows with menus   
    makemenu(root)
    Label(root, bg='black', height=5, width=15).pack(expand=YES, fill=BOTH)
Button(root, text="Bye", command=root.quit).pack( )
root.mainloop( )


