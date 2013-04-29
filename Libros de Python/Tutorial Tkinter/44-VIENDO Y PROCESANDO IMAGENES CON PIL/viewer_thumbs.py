#######################################################
# display all images in a directory as thumbnail image
# buttons that display the full image when clicked;
# requires PIL for JPEGs and thumbnail img creation;
# to do: add scrolling if too many thumbs for window!
#######################################################

import os, sys, math
from Tkinter import *
import Image                          # <== required for thumbs
from ImageTk import PhotoImage        # <== required for JPEG display

def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    """
    get thumbnail images for all images in a directory;
    for each image, create and save a new thumb, or load
    and return an existing thumb; makes thumb dir if needed;
    returns list of (image filename, thumb image object);
    the caller can also run listdir on thumb dir to load;
    on bad file types we may get IOError, or other: overflow
    """
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)

    thumbs = []
    for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            thumbobj = Image.open(thumbpath)            # use already created
            thumbs.append((imgfile, thumbobj))
        else:
            print 'making', thumbpath
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath)            # make new thumb
                imgobj.thumbnail(size, Image.ANTIALIAS) # best downsize filter
                imgobj.save(thumbpath)                  # type via ext or passed
                thumbs.append((imgfile, imgobj))
            except:                                     # not always IOError
                print "Skipping: ", imgpath
    return thumbs

class ViewOne(Toplevel):
    """
    open a single image in a pop-up window when created;
    photoimage obj must be saved: erased if reclaimed;
    """
    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        imgobj  = PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack( )
        print imgpath, imgobj.width(), imgobj.height( )   # size in pixels
        self.savephoto = imgobj                           # keep reference on me

def viewer(imgdir, kind=Toplevel, cols=None):
    """
    make thumb links window for an image directory:
    one thumb button per image; use kind=Tk to show
    in main  app window, or Frame container (pack);
    imgfile differs per loop: must save with a default;
    photoimage objs must be saved: erased if reclaimed;
    """
    win = kind( )
    win.title('Viewer: ' + imgdir)
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs))))     # fixed or N x N

    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            photo   = PhotoImage(imgobj)
            link    = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)

    Button(win, text='Quit', command=win.quit).pack(fill=X)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'C:\gifs\\'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop( )

