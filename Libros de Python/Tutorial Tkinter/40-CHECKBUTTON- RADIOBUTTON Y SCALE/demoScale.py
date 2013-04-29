from Tkinter import *                # get base widget set
from dialogTable import demos        # button callback handlers
from quitter import Quitter          # attach a quit frame to me

class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack( )
        Label(self, text="Scale demos").pack( )
        self.var = IntVar( )
        Scale(self, label='Pick demo number',
                    command=self.onMove,                   # catch moves
                    variable=self.var,                     # reflects position
                    from_=0, to=len(demos)-1).pack( )
        Scale(self, label='Pick demo number',
                    command=self.onMove,                   # catch moves
                    variable=self.var,                     # reflects position
                    from_=0, to=len(demos)-1,
                    length=200, tickinterval=1,
                    showvalue=YES, orient='horizontal').pack( )
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State",    command=self.report).pack(side=RIGHT)
    def onMove(self, value):
        print 'in onMove', value
    def onRun(self):
        pos = self.var.get( )
        print 'You picked', pos
        pick = demos.keys( )[pos]    # map from position to key
        print demos[pick]( )
    def report(self):
        print self.var.get( )

if __name__ == '__main__':
    print demos.keys( )
    Demo().mainloop( )



