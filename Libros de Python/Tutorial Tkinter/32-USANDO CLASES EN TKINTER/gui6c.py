from Tkinter import *                    # get Tk widget classes
from gui6 import Hello                   # get the subframe class

class HelloContainer(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack( )
        self.makeWidgets( )
    def makeWidgets(self):
        Hello(self).pack(side=RIGHT)     # attach a Hello to me
        Button(self, text='Attach', command=self.quit).pack(side=LEFT)

if __name__ == '__main__': HelloContainer().mainloop( )

