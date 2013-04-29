from Tkinter import *
from tkMessageBox import showinfo


class GUI(Tk):          
                                                                      
          def reply(self ):
                    showinfo(title='popup', message='Button pressed!')

          def button(self):
                    Button(self, text='press', command=self.reply).pack()

window = GUI( )
window.button()
window.mainloop( )
