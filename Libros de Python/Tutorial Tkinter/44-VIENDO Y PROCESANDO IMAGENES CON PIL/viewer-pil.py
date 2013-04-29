#######################################################
# show one image with PIL photo replacement object
# install PIL first: placed in Lib\site-packages
#######################################################

import os, sys
from Tkinter import *
from ImageTk import PhotoImage           # <== use PIL replacement class
                                         # rest of code unchanged
imgdir  = 'C:\gifs\\'
imgfile = 'newmarket-uk-1.jpg'
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk( )
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)        # now JPEGs work!
Label(win, image=imgobj).pack( )
win.mainloop( )
print imgobj.width(), imgobj.height( )    # show size in pixels on exit

