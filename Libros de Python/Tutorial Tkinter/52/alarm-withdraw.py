from Tkinter import *
import alarm

class Alarm(alarm.Alarm):
    def repeater(self):                            # on every N millisecs
        self.bell( )                               # beep now
        if self.master.state( ) == 'normal':       # is window displayed?
            self.master.withdraw( )                # hide entire window, no icon
        else:                                       # iconify shrinks to an icon
            self.master.deiconify( )               # else redraw entire window
            self.master.lift( )                    # and raise above others
        self.after(self.msecs, self.repeater)       # reschedule handler

if __name__ == '__main__': Alarm().mainloop( )    # master = default Tk root

