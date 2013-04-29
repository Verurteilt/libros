from Tkinter import *
from tkColorChooser import askcolor

def setBgColor( ):
    (triple, hexstr) = askcolor( )
    if hexstr:
        print hexstr
        push.config(bg=hexstr)

root = Tk( )
push = Button(root, text='Set Background Color', command=setBgColor)
push.config(height=3, font=('times', 20, 'bold'))
push.pack(expand=YES, fill=BOTH)
root.mainloop( )


