from Tkinter import *
demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']

demoObjects = []
for demo in demoModules:
    module = __import__(demo)             # import by name string
    window = Toplevel( )                   # make a new window
    demo   = module.Demo(window)            # parent is the new window
    demoObjects.append(demo)

def allstates( ):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print obj.__module__,
            obj.report( )

Label(text='Multiple Toplevel window demo', bg='white').pack( )
Button(text='States', command=allstates).pack(fill=X)
mainloop( )
