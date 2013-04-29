from Tkinter import *
root = Tk( )                                                     # explicit root

trees = [('The Larch!',          'light blue'),
         ('The Pine!',           'light green'),
         ('The Giant Redwood!',  'red')]

for (tree, color) in trees:
    win = Toplevel(root)                                        # new window
    win.title('Sing...')                                        # set border
    win.protocol('WM_DELETE_WINDOW', lambda:0)                  # ignore close
    win.iconbitmap('py-blue-trans-out.ico')                     # not red Tk

    msg = Button(win, text=tree, command=win.destroy)           # kills one win
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

root.title('Lumberjack demo')
Label(root, text='Main window', width=30).pack( )
Button(root, text='Quit All', command=root.quit).pack( )         # kills all app
root.mainloop( )




