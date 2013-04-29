from Tkinter import *
from gui7 import HelloPackage      # or get from gui7c--_ _getattr_ _ added

frm = Frame( )
frm.pack( )
Label(frm, text='hello').pack( )

part = HelloPackage(frm)
part.top.pack(side=RIGHT)              # fails!--need part.top.pack(side=RIGHT)
frm.mainloop( )

