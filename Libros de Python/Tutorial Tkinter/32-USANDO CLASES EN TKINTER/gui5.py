from Tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, **conf):         # add callback method        
        Button.__init__(self, parent, conf)          # and pack myself
        self.pack( )
        self.config(command=self.callback)
    def callback(self):                                # default press action
        print 'Goodbye world...'                       # replace in subclasses
        self.quit( )

if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop( )

