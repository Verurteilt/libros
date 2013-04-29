from Tkinter import *
from gui6 import Hello

class HelloExtender(Hello):
    def make_widgets(self):                       # extend method here
        Hello.make_widgets(self)
        Button(self, text='Extend', command=self.quit).pack(side=RIGHT)
    def message(self):
        print 'hello', self.data                  # redefine method here

if __name__ == '__main__': HelloExtender().mainloop( )

