from Tkinter import *

class HelloPackage:                            # not a widget subbclass
    def __init__(self, parent=None):
        self.top = Frame(parent)               # embed a Frame
        self.top.pack( )
        self.data = 0
        self.make_widgets( )                    # attach widgets to self.top
    def make_widgets(self):
        Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
        Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)
    def message(self):
        self.data += 1
        print 'Hello number', self.data

if __name__ == '__main__': HelloPackage().top.mainloop( )

