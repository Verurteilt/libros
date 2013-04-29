#######################################################
# display all images in a directory in pop-up windows
# GIFs work, but JPEGs will be skipped without PIL
#######################################################

import os, sys
from Tkinter import *
from ImageTk import PhotoImage              # <== required for JPEGs and others

imgdir = 'C:\gifs\\'
if len(sys.argv) > 1: imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir)               # does not include directory prefix

main = Tk( )
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack( )
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    win = Toplevel( )
    win.title(imgfile)
    try:
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack( )
        print imgpath, imgobj.width(), imgobj.height( )       # size in pixels
        savephotos.append(imgobj)                              # keep a reference
    except:
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info( )[1])
        Label(win, text=errmsg).pack( )

main.mainloop( )

