from Tkinter import *             # get base widget set
from dialogTable import demos     # get canned dialogs
from quitter import Quitter       # attach a quitter object to "me"

class Demo(Frame):
    def __init__(self, parent=None, **args):
        Frame.__init__(self, parent, args)
        self.pack( )
        self.tools( )
        Label(self, text="Check demos").pack( )
        self.vars = []
        for key in demos.keys( ):
            var = IntVar( )
            Checkbutton(self,
                        text=key,
                        variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)
    def report(self):
        for var in self.vars:
            print var.get( ),   # current toggle settings: 1 or 0
        print
    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)
    

if __name__ == '__main__': Demo().mainloop( )

