from Tkinter import *
import alarm

class Alarm(alarm.Alarm):                        # change alarm callback
    def repeater(self):                          # on every N millisecs
        self.bell( )                                  # beep now
        if self.shown:
            self.stopper.pack_forget( )              # hide or erase button now
        else:                                    # or reverse colors, flash...
            self.stopper.pack( )
        self.shown = not self.shown              # toggle state for next time
        self.after(self.msecs, self.repeater)    # reschedule handler
    def __init__(self, msecs=1000):                # default = 1 second
        self.shown = 0
        alarm.Alarm.__init__(self, msecs)

if __name__ == '__main__': Alarm(msecs=500).mainloop( )


