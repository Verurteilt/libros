from Tkinter import *                # get base widget set
from dialogTable import demos        # button callback handlers
from quitter import Quitter          # attach a quit object to "me"

class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack( )
        Label(self, text="Radio demos").pack(side=TOP)
        self.var = StringVar( )
        for (key, value) in demos.items( ):
            Radiobutton(self, text=key,
                              command=self.onPress,
                              variable=self.var,
                              value=key).pack(anchor=NW)
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)
    def onPress(self):
        pick = self.var.get( )
        print 'you pressed', pick
        print 'result:', demos[pick]( )
    def report(self):
        print self.var.get( )

if __name__ == '__main__': Demo().mainloop( )


