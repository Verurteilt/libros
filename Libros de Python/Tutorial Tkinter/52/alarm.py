#!/usr/local/bin/python
from Tkinter import *

class Alarm(Frame):
    def repeater(self):                           # on every N millisecs
        self.bell( )                              # beep now
        self.stopper.flash( )                     # flash button now
        self.after(self.msecs, self.repeater)      # reschedule handler
    def __init__(self, msecs=1000):              # default = 1 second
        Frame.__init__(self)
        self.msecs = msecs
        self.pack( )
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack( )
        stopper.config(bg='navy', fg='white', bd=8)
        self.stopper = stopper
        self.repeater( )

if __name__ == '__main__': Alarm(msecs=1000).mainloop( )

