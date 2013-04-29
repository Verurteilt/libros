# a simple text or file viewer component

print 'PP3E scrolledtext'
from Tkinter import *

class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)                 # make me expandable
        self.makewidgets( )
        self.settext(text, file)
    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                  # xlink sbar and text
        text.config(yscrollcommand=sbar.set)             # move one moves other
        sbar.pack(side=RIGHT, fill=Y)                    # pack first=clip last
        text.pack(side=LEFT, expand=YES, fill=BOTH)      # text clipped first
        self.text = text
    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read( )
        self.text.delete('1.0', END)                     # delete current text
        self.text.insert('1.0', text)                    # add at line 1, col 0
        self.text.mark_set(INSERT, '1.0')                # set insert cursor
        self.text.focus( )                                    # save user a click
    def gettext(self):                                   # returns a string
        return self.text.get('1.0', END+'-1c')           # first through last

if __name__ == '__main__':
    root = Tk( )
    try:
        st = ScrolledText(file=sys.argv[1])              # filename on cmdline
    except IndexError:
        st = ScrolledText(text='Words\ngo here')         # or not: two lines
    def show(event): print repr(st.gettext( ))               # show as raw string
    root.bind('<Key-Escape>', show)                      # esc = dump text
    root.mainloop( )

