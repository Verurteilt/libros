from Tkinter import *
from tkMessageBox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):                            # inherit init
    def reply(self):                               # replace reply
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack( )
    mainloop( )

